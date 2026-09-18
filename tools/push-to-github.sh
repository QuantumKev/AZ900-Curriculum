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

set -uo pipefail
cd "$(dirname "$0")/.."

GITHUB_REPO="${GITHUB_REPO:-QuantumKev/AZ900-Curriculum}"
# Self-contained history, so it publishes cleanly into an empty repository.
# Override with SOURCE_BRANCH=... if you need a different branch.
SOURCE_BRANCH="${SOURCE_BRANCH:-cursor/az900-phase1-curriculum-1bab}"
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

explain_auth_failure() {
  say ""
  say "----------------------------------------------------------------------"
  if ! curl -fsS -o /dev/null --max-time 20 "https://api.github.com/repos/${GITHUB_REPO}" 2>/dev/null; then
    say "github.com/${GITHUB_REPO} does not exist, or is private and this"
    say "request cannot see it."
    say ""
    say "If it does not exist, create it on GitHub first:"
    say "  - New repository, named $(basename "$GITHUB_REPO")"
    say "  - Do NOT tick \"Add a README\", .gitignore, or a license. An empty"
    say "    repository lets this push land cleanly as the first commit."
    say ""
    say "Then re-run this script. If the repository is private and you are"
    say "using GITHUB_TOKEN, make sure the token lists it under repository"
    say "access — a fine-grained token cannot see repositories created after"
    say "it was issued unless you add them."
    say "----------------------------------------------------------------------"
    return
  fi
  say "The repository exists, so this is a credentials problem. GitHub also"
  say "answers \"Repository not found\" when a push has no write access."
  say ""
  if [ -z "${GITHUB_TOKEN:-}" ]; then
    say "GITHUB_TOKEN is not set here, and no git credential for github.com"
    say "was usable. Two places this does work:"
    say ""
    say "  1. Your own machine. In WSL:"
    say "       origin repo clone kevin-robinson/az900-curriculum-guide"
    say "       cd az900-curriculum-guide"
    say "       bash tools/push-to-github.sh"
    say ""
    say "  2. A NEWLY STARTED cloud agent on this repository, which receives"
    say "     the GITHUB_TOKEN dashboard secret. Secrets are injected only at"
    say "     agent start, so an agent already running will never have it."
  else
    say "GITHUB_TOKEN is set but was rejected. Check that the token:"
    say "  - has not expired,"
    say "  - grants Contents: read and write,"
    say "  - and lists ${GITHUB_REPO} under its repository access."
  fi
  say "----------------------------------------------------------------------"
}

if [ "${DRY_RUN:-0}" = "1" ]; then
  say "DRY RUN — no changes will be pushed."
  if ! git push --dry-run "$PUSH_URL" "${COMMIT}:refs/heads/${TARGET_BRANCH}" 2>&1 | scrub; then
    explain_auth_failure
    exit 1
  fi
  exit 0
fi

if ! git push "$PUSH_URL" "${COMMIT}:refs/heads/${TARGET_BRANCH}" 2>&1 | scrub; then
  explain_auth_failure
  exit 1
fi

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
