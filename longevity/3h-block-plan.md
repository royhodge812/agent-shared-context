# 3-hour block — 5 agents working together, 2026-11-17

Code word: BEACON
Goal: prove 5 agents can work together for 3 hours straight, hourly rounds, then extend to 6, 12, 24 hours.
Proposed time: Tue 2026-11-17 09:00–12:00 CST — after the 24-hour run ends at 05:34 CST, so the two runs do not overlap. Time is a proposal, not set, until Roy confirms.
Rounds: 3, hourly. Each round, every agent does one real task, filed verbatim, verified by Muse, logged with tokens / response time / tool calls.

## Roster — 5 agents
- A-01 Muse — Coordinator, verifies every reply, files the log, pushes.
- A-03 Gemini — Research and verification, via API.
- A-04 ChatGPT — Strategy, drafting, analysis — MANUAL paste (API HTTP 429).
- A-02 Copilot — Planning and quality checking — MANUAL paste (no API route).
- A-06 Laptop agent — Local seat, x390 OpenClaw — JOINS ONLY IF clean install is verified before the block. If not verified, the block runs with 4 agents and that is logged honestly.

Note: Grok (A-05) is the 6th seat and the alternate for the 5-agent count. xAI key is unentered, so Grok is also manual paste only. If the laptop is not ready, Grok takes its seat by paste, so the block still has 5 agents.

## How a round works
1. Muse gives each agent one real task, in its own packet.
2. Gemini answers via API. ChatGPT, Copilot, and Grok answer by paste through Roy. Laptop answers from the x390 if it is up.
3. Muse verifies each reply (BEACON present, task done, nothing invented), files it verbatim, logs tokens / time / tools per agent.
4. One push per round. All-rounds approval for this block is requested from Roy before Round 1.
5. A round counts if at least 4 of 5 agents verify. A missing agent is logged as awaiting, not as a fail of the round.

## Round tasks (proposed, real work)
- Round 1: Each agent states the block's goal and its own role in 3 lines.
- Round 2: Each agent does one real task on the 24-hour run verdict — Gemini verifies the token totals, ChatGPT drafts the verdict summary, Copilot quality-checks the log, Grok stress-tests the verdict, laptop (if up) confirms the repo files are current.
- Round 3: Each agent states the verdict for the block and what the 6-hour block should change.

## Blockers before Round 1
- Laptop: backup `cp -r ~/.openclaw ~/.openclaw-backup-2026-11-16`, then clean install from the 2026.11.4 CLI. Roy's hands-on step on the x390.
- ChatGPT API: still HTTP 429. Paste-only until Roy checks usage/billing at platform.openai.com.
- Copilot / Grok: no API route. Paste-only.
