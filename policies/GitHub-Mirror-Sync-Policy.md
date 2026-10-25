# GitHub Mirror Sync Policy — Roy's Agent Ecosystem (2026-10-25)

**Purpose:** GitHub (`royhodge812/agent-shared-context`, public) is the backup mirror of the live Drive record (`Agent-Coordination`). It must not drift from Drive, the Registry, or the Pages site.

**Rule:** When the shared record changes, GitHub is updated at the next checkpoint. No material change is left unmirrored beyond the work session in which it was made.

## What triggers a sync

A sync is required after any verified change to:
- Registry (roster, ranks, roles, code words, titles — e.g. Copilot QA title, 2026-10-25)
- Identities (including Agent Swarm Custom Templates)
- Policies (including this policy)
- History or Check-ins
- Dashboard v2, Agent Coordination in Motion, or Agent Task Queue Board (Pages files)
- Any approval or denial recorded in chat that changes the record

## Checkpoint definition

1. **On change:** A-01 prepares the mirror (Drive updated first, then GitHub files staged).
2. **At session close:** Before the end-of-session summary, if any record change in that session is not yet mirrored, A-01 mirrors it and verifies it, or states plainly that it is still unmirrored and why.
3. **Before a demo or presentation:** Pages and GitHub must be re-verified live before Roy presents them, not assumed from a repo push.
4. **No empty syncs:** If nothing changed, no sync is made just to make a commit. If changes pile up without a sync, the next checkpoint syncs all of them together and lists what changed.

## How a sync is verified (every time)

- Drive file updated in place (same ID) where a Drive file already exists, or a new file created in the correct subfolder.
- GitHub push to `main` with a commit message naming what changed.
- Read-back from GitHub after the push, confirming the new title, code word, or content is actually in the repo file — not just that a push was attempted.
- If Pages files changed, a live Pages check (HTTP 200, correct title/content) after rebuild — a repo push alone is not "live".

## Approval gate (unchanged by this policy)

This policy does not override Roy's approval gate. Nothing spends, sends, posts, files, or is published on a general yes. A-01 prepares the mirror; Roy approves the specific deployment or filing in chat before it is pushed, except where Roy already approved the underlying change *and* its mirroring in the same decision (for example, approving a role title and its Registry/Dashboard/GitHub update together).

## What never goes to GitHub

No passwords, keys, tokens, private IDs, tenant/financial detail, or any other secret — ever. GitHub is public. If a file contains such material, it is not mirrored, and A-01 says so instead of pushing it.

## Record

This policy was adopted by Roy 2026-10-25, in the same decision that approved mirroring the updated Agent Swarm Custom Templates to GitHub and adding back-and-forth navigation to all Pages.
