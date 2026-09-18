#!/usr/bin/env bash
# Publish this curriculum to the GitHub repository.
#
# Usage:
#   bash tools/push-to-github.sh              # push to main
#   bash tools/push-to-github.sh <branch>     # push to another branch name
#   DRY_RUN=1 bash tools/push-to-github.sh    # show what would happen, push nothing
#
# Authentication, in order of preference:
#   1. $GITHUB_TOKEN  — a fine-grained PAT with Contents: read and write on the
#      target repository. Cloud agents get this from the dashboard secret.
#   2. Whatever git credentials the machine already has (a normal local clone).
#
# The token is never written to .git/config and is scrubbed from any output.

set -euo pipefail
cd "$(dirname "$0")/.."

GITHUB_REPO="${GITHUB_REPO:-QuantumKev/AZ900-Curriculum}"
SOURCE_BRANCH="${SOURCE_BRANCH:-cursor/az900-github-ready-1bab}"
TARGET_BRANCH="${1:-main}"

say() { printf '%s\n' "$*"; }

# Resolve the commit to publish, preferring the remote copy of the branch so
# this works from a fresh clone that has not checked the branch out.
if git rev-parse --verify --quiet "origin/$SOURCE_BRANCH" >/dev/null; then
  git fetch -q origin "$SOURCE_BRANCH" || true
  COMMIT="$(git rev-parse "origin/$SOURCE_BRANCH")"
  SOURCE_DESC="origin/$SOURCE_BRANCH"
elif git rev-parse --verify --quiet "$SOURCE_BRANCH" >/dev/null; then
  COMMIT="$(git rev-parse "$SOURCE_BRANCH")"
  SOURCE_DESC="$SOURCE_BRANCH"
else
  say "Branch '$SOURCE_BRANCH' not found locally or on origin."
  say "Run 'git fetch origin' first, or set SOURCE_BRANCH to the branch you want."
  exit 1
fi

if [ -n "${GITHUB_TOKEN:-}" ]; then
  PUSH_URL="https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git"
  AUTH_DESC="GITHUB_TOKEN"
else
  PUSH_URL="https://github.com/${GITHUB_REPO}.git"
  AUTH_DESC="this machine's existing git credentials"
fi

say "Repository:  github.com/${GITHUB_REPO}"
say "Source:      ${SOURCE_DESC} (${COMMIT:0:7})"
say "Target:      ${TARGET_BRANCH}"
say "Auth:        ${AUTH_DESC}"
say ""

# Scrub the token from anything git prints, including error output.
scrub() {
  if [ -n "${GITHUB_TOKEN:-}" ]; then
    sed -e "s#${GITHUB_TOKEN}#[REDACTED]#g" -e "s#x-access-token:[^@]*@#x-access-token:[REDACTED]@#g"
  else
    cat
  fi
}

if [ "${DRY_RUN:-0}" = "1" ]; then
  say "DRY RUN — no changes will be pushed."
  git push --dry-run "$PUSH_URL" "${COMMIT}:refs/heads/${TARGET_BRANCH}" 2>&1 | scrub
  exit 0
fi

git push "$PUSH_URL" "${COMMIT}:refs/heads/${TARGET_BRANCH}" 2>&1 | scrub

REMOTE_HEAD="$(git ls-remote "$PUSH_URL" "refs/heads/${TARGET_BRANCH}" 2>/dev/null | cut -f1 | scrub)"
say ""
if [ "$REMOTE_HEAD" = "$COMMIT" ]; then
  say "Verified: github.com/${GITHUB_REPO} ${TARGET_BRANCH} is now at ${COMMIT:0:7}."
  say "View it at https://github.com/${GITHUB_REPO}"
else
  say "Push reported success but the remote head does not match."
  say "  expected ${COMMIT}"
  say "  found    ${REMOTE_HEAD:-<none>}"
  exit 1
fi
