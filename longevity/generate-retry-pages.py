#!/usr/bin/env python3
"""Generate heartbeat-retry.json and longevity-retry.html from the retry log.

One write per round: edit longevity/2026-11-16-retry.md, then run:
  python3 longevity/generate-retry-pages.py
The log is the only source of truth. This script never invents a round.
"""
import json, re, pathlib

BASE = pathlib.Path(__file__).resolve().parent
LOG = BASE / "2026-11-16-retry.md"
HEARTBEAT = BASE / "heartbeat-retry.json"
HTML = BASE.parent / "longevity-retry.html"

text = LOG.read_text()
sections = re.split(r"\n### Round (\d+) — ", text)[1:]
rounds = {}
for i in range(0, len(sections), 2):
    num = int(sections[i])
    body = sections[i + 1]
    header, _, rest = body.partition("\n")
    m = re.match(r"(\d\d:\d\d CST) — (complete|in progress|pending)", header)
    if not m:
        continue  # stale "### Round N — pending" placeholder, no time, no round
    time, status = m.groups()
    tokens = re.search(r"A-03 Gemini \(API, gemini-2\.5-flash, (\d+) total tokens\)", rest)
    has_gemini = "A-03 Gemini" in rest and "PASS" in rest
    has_chatgpt = "A-04 ChatGPT (manual paste" in rest and "PASS" in rest
    rounds[num] = {"time": time, "status": status, "tokens": int(tokens.group(1)) if tokens else None,
                   "gemini": has_gemini, "chatgpt": has_chatgpt}

completed = [n for n, r in sorted(rounds.items()) if r["status"] == "complete"]
last = rounds[max(completed)] if completed else None
last_chatgpt = max([n for n, r in rounds.items() if r["chatgpt"]], default=None)
gemini_tokens = sum(r["tokens"] for r in rounds.values() if r["tokens"])

heartbeat = {
    "test": "2026-11-16 longevity retry",
    "code_word": "BEACON",
    "mode": "live in chat",
    "sprint_start_cst": "2026-11-16 05:07",
    "rounds_completed": len(completed),
    "rounds_total": 8,
    "status": "complete" if len(completed) >= 8 else "running",
    "last_heartbeat_cst": f"2026-11-16 {last['time'][:5]}" if last else None,
    "gemini_total_tokens_all_rounds": gemini_tokens,
    "agents": {
        "A-01 Muse": {"status": "up", "last_heartbeat_cst": f"2026-11-16 {last['time'][:5]}" if last else None},
        "A-03 Gemini": {"status": "up", "last_heartbeat_cst": f"2026-11-16 {last['time'][:5]}" if last else None,
                         "last_call_tokens_total": last["tokens"] if last else None},
        "A-04 ChatGPT": {"status": "up-manual-paste",
                         "last_heartbeat_cst": f"2026-11-16 {rounds[last_chatgpt]['time'][:5]}" if last_chatgpt else None},
        "A-06 Laptop agent": {"status": "awaiting-doctor-fix", "last_heartbeat_cst": None},
    },
}
HEARTBEAT.write_text(json.dumps(heartbeat, indent=2) + "\n")

def summary(n, r):
    if r["gemini"] and r["chatgpt"]:
        return f"Round {n}: Gemini and ChatGPT verified PASS."
    if r["gemini"]:
        return f"Round {n}: Gemini verified PASS, ChatGPT reply pending."
    return f"Round {n}: {r['status']}."
summary_line = " ".join(summary(n, r) for n, r in sorted(rounds.items()) if r["status"] in ("complete", "in progress"))
status_line = (f"Round {max(completed)} of 8 complete." if len(completed) >= 1
               else "No rounds complete yet.")
if last and last["status"] == "in progress":
    status_line = f"Round {max(rounds)} of 8 in progress."

HTML.write_text(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Longevity retry — Agent Shared Context</title>
<style>body{{font-family:system-ui,sans-serif;max-width:720px;margin:2rem auto;padding:0 1rem;line-height:1.5}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ccc;padding:.4rem .6rem;text-align:left}}.up{{color:green}}.await{{color:#a60}}</style></head>
<body>
<h1>Longevity retry — 2026-11-16</h1>
<p>Code word: <strong>BEACON</strong>. Live in chat, starting 05:07 CST. First sprint ended FAIL, 2 of 8 rounds.</p>
<p>Status: <strong>{heartbeat["status"]}</strong> — {status_line}</p>
<table><tr><th>Agent</th><th>Role</th><th>Status</th></tr>
<tr><td>A-01 Muse</td><td>Coordinator</td><td class="up">up</td></tr>
<tr><td>A-03 Gemini</td><td>Research &amp; verification (API)</td><td class="up">up</td></tr>
<tr><td>A-04 ChatGPT</td><td>Strategy &amp; drafting</td><td class="up">up — manual paste</td></tr>
<tr><td>A-06 Laptop agent</td><td>Local seat, x390 OpenClaw</td><td class="await">awaiting doctor --fix</td></tr>
</table>
<p>{summary_line} Laptop still awaiting. Full log: <a href="longevity/2026-11-16-retry.md">longevity/2026-11-16-retry.md</a></p>
<p><em>Heartbeat and this page are generated from the log by longevity/generate-retry-pages.py. One write per round.</em></p>
</body></html>
""")
print(f"rounds completed: {len(completed)}, gemini tokens total: {gemini_tokens}, last: {last['time'] if last else None}")
