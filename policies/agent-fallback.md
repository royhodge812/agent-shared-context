# Agent fallback and redelegation — 2026-11-16

Roy's rule, set 2026-11-16 05:23 CST: no single agent being inaccessible may stop the team. The team keeps operating and coordinating autonomously, and roles move to whoever is up.

## The rule in one line
The repo is the memory. Coordinator is a role, not a person. Any agent that can read the repo can take the role.

## Coordinator fallback order
1. A-01 Muse — lead coordinator, default.
2. A-03 Gemini — acting coordinator if Muse misses 2 rounds in a row, or Roy says "Muse is down — you are acting coordinator until Muse returns".
3. A-04 ChatGPT — acting coordinator if Muse and Gemini are both down.
4. A-06 Laptop agent — local coordinator if all cloud agents are down; runs on Roy's x390, on his own hardware.

No agent claims coordinator while the current coordinator is still producing verified rounds. A claim is logged in the round log with who, when, and why.

## Gemini carries ChatGPT when it is down (adopted 2026-11-16 05:29 CST)
ChatGPT's API is down (HTTP 429). When a paste round-trip is not available either, Gemini does ChatGPT's task in the same 3-line format and says which role it is covering. ChatGPT rejoins by paste when it is back, reads the log first, and does not replay missed rounds.

## If a specialist is down
- A round still counts if at least 2 agents verify it. A missing agent is logged as "awaiting", not as a fail of the round.
- The coordinator reassigns the missing agent's work to the next capable agent, and logs the swap:
  - Research / verification (Gemini) -> ChatGPT, then laptop agent.
  - Strategy / drafting / analysis (ChatGPT) -> Gemini, then laptop agent.
  - Stress-testing (Grok) -> Gemini, then ChatGPT.
- The replacement does the same task, in the same 3-line check-in format, and says which role it is covering.

## What never changes without Roy
- Roy is Tier 0. He breaks ties and approves anything consequential: spending, sending, posting, publishing, filing externally, provisioning, deleting, sharing publicly, changing an account, signing.
- Routine rounds, check-ins, and log pushes do not need Roy's yes each time — he approved all rounds on 2026-11-16 05:17 CST for this retry.
- A returning agent reads the repo log first, then rejoins at the next round. It does not replay or redo rounds it missed.

## How to trigger it
Paste to the backup agent: "[Agent name] is down — you are acting coordinator until [agent] returns. Read the repo royhodge812/agent-shared-context, longevity/2026-11-16-retry.md, and continue the next round."
