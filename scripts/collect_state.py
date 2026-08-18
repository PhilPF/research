#!/usr/bin/env python3
"""Collect MAGI state from every session branch into static JSON.

Read-only by contract: reads git objects and writes ONLY under --out.
Never writes to state/, reviews/, or LOG.md.

Emits:
  <out>/index.json       list of sessions
  <out>/<session>.json   full snapshot for one session
  <out>/build-id.json    {"sha": ..., "built_at": ...}
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

SAFE = re.compile(r"[^A-Za-z0-9._-]")


def git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=False
    ).stdout.strip()


def branches():
    """Every branch we can see: remote refs first, local heads as fallback.

    actions/checkout with fetch-depth: 0 normally populates
    refs/remotes/origin/*, but we don't rely on it — a run that only has
    local heads must still work, or sessions silently vanish.
    """
    seen, out = set(), []
    for ref in ("refs/remotes/origin", "refs/heads"):
        for b in git("for-each-ref", "--format=%(refname:short)", ref).splitlines():
            b = b.strip()
            if not b or b.endswith("/HEAD"):
                continue
            key = b.removeprefix("origin/")
            if key in seen:
                continue
            seen.add(key)
            out.append(b)
    return out


def ls(branch, path):
    """List files under path on branch."""
    out = git("ls-tree", "-r", "--name-only", branch, path)
    return [l for l in out.splitlines() if l.strip()]


def read(branch, path):
    r = subprocess.run(
        ["git", "show", f"{branch}:{path}"], capture_output=True, text=True, check=False
    )
    return r.stdout if r.returncode == 0 else None


def read_json(branch, path, errors):
    raw = read(branch, path)
    if raw is None:
        return None
    try:
        return json.loads(raw)
    except json.JSONDecodeError as e:
        # Never repair. Record the fault so the UI can show it.
        errors.append({"path": path, "error": f"malformed JSON: {e}"})
        return None


def collect(branch):
    errors = []
    session = read_json(branch, "state/session.json", errors)
    if session is None:
        return None  # not a session branch

    snap = {
        "branch": branch.removeprefix("origin/"),
        "session": session,
        "live": read_json(branch, "state/live.json", errors),
        "rounds": [],
        "verdicts": {},
        "lilith": {},
        "reviews": {},
        "log": read(branch, "LOG.md"),
        "errors": errors,
    }

    for p in sorted(ls(branch, "state/rounds")):
        d = read_json(branch, p, errors)
        if d:
            snap["rounds"].append(d)
    snap["rounds"].sort(key=lambda r: (r.get("claim_id", ""), r.get("round", 0)))

    for p in sorted(ls(branch, "state/verdicts")):
        d = read_json(branch, p, errors)
        if d:
            snap["verdicts"][os.path.basename(p)] = d

    # The generative agent was renamed Eve -> Lilith. Read both
    # directories so old sessions stay readable and new ones work.
    for legacy in ("state/lilith", "state/eve"):
        for p in sorted(ls(branch, legacy)):
            d = read_json(branch, p, errors)
            if d:
                snap["lilith"][os.path.basename(p)] = d

    # Review prose, keyed by filename. Kept as raw markdown; the client
    # renders it. Missing files are simply absent — the UI shows
    # "no report written" rather than inventing an empty one.
    for p in sorted(ls(branch, "reviews")):
        if p.endswith(".md"):
            body = read(branch, p)
            if body is not None:
                snap["reviews"][os.path.basename(p)] = body

    return snap


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    out = os.path.abspath(args.out)
    os.makedirs(out, exist_ok=True)

    index = []
    for b in branches():
        snap = collect(b)
        if not snap:
            continue
        sid = snap["session"].get("session_id") or snap["branch"]
        sid = SAFE.sub("-", sid)
        with open(os.path.join(out, f"{sid}.json"), "w") as f:
            json.dump(snap, f, separators=(",", ":"))
        prob = snap["session"].get("problem", {})
        index.append(
            {
                "session_id": sid,
                "branch": snap["branch"],
                "title": prob.get("title"),
                "claim_id": prob.get("claim_id"),
                "status": snap["session"].get("status"),
                "latest_round": snap["session"].get("latest_round"),
                "started_at": snap["session"].get("started_at"),
                "file": f"{sid}.json",
                "has_errors": bool(snap["errors"]),
            }
        )

    index.sort(key=lambda s: s.get("started_at") or "", reverse=True)

    with open(os.path.join(out, "index.json"), "w") as f:
        json.dump({"sessions": index}, f, indent=1)

    with open(os.path.join(out, "build-id.json"), "w") as f:
        json.dump(
            {
                "sha": os.environ.get("GITHUB_SHA", git("rev-parse", "HEAD"))[:12],
                "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "sessions": len(index),
            },
            f,
        )

    print(f"collected {len(index)} session(s)", file=sys.stderr)


if __name__ == "__main__":
    main()
