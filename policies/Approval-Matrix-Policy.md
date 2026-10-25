# Approval Matrix Policy

**Date:** 2026-10-25
**Operator:** Roy Albert Hodge Jr. — Tier 0
**Coordinator:** A-01 @Muse
**Roster:** A-02 @Copilot (IRONWOOD), Task Analysis, Planning, and Quality Assurance Agent; A-03 @Gemini (JUNIPER), Specialist; A-04 @ChatGPT (SUNSTONE), Specialist; A-05 @Grok (OBSIDIAN), Specialist

This policy sets how pending tasks in Roy's agent ecosystem are approved. It is designed so Roy only has to do one check-in a day to approve or deny everything that needs him, while consequential actions never move without his explicit yes.

## The standing gate does not change

Nothing spends, sends, posts, publishes, files externally, provisions, deletes, shares publicly, changes an account, or signs anything without Roy's explicit yes on that specific item.

A-01 @Muse must not approve for Roy. Silence is never a yes for a consequential action.

## Action kind comes before priority

Every pending item is split by kind of action first. Priority is applied only after that split.

**Consequential** means any action in the standing gate above: spending, sending, posting, publishing, filing externally, provisioning, deleting, sharing publicly, changing an account, or signing.

**Internal / Reversible** means a step that stays inside the system, never spends, and can be undone or re-decided by Roy. Examples are:

- Moving a Queue Board card from one stage to another
- Filing a verified note to Drive or GitHub
- Marking a return verified
- Preparing a draft for Roy's review

An internal step is not a consequential action, and a consequential action is never reclassified as internal because it is old, low priority, or waiting a long time.

## Priority decides who approves and what a timeout means

| Priority | Who decides | Notice or deadline | If there is no answer |
| --- | --- | --- | --- |
| Urgent | Roy only | Immediate, escalating reminders, no timeout | No Muse approval; item stays with Roy |
| High | Roy only for consequential items | Deadline set by Roy per item; A-01 prepares the decision packet | Held, not approved |
| Medium | Muse may approve internal steps only | 72-hour notice period | Internal step may proceed after 72 hours; consequential item stays Held |
| Low | Muse may approve internal steps only | 24-hour notice period | Internal step may proceed after 24 hours; consequential item stays Held |

For Medium and Low items, Muse's approval power is limited to Internal / Reversible steps only. It does not extend to any consequential action at any priority.

Every Medium or Low internal approval by Muse requires a full audit log entry covering the task ID, what was approved, why it qualified, and how to reverse it.

## The fail-safe direction is hold, not approve

Timeout means Hold for every consequential item. It never means auto-approve.

A consequential item that times out is carried to the next daily digest as **Held, not approved**. It remains pending until Roy gives an explicit yes or no on that specific item.

## One daily check-in covers everything Roy must decide

A-01 delivers **one consolidated Approval Digest per day**. All pending Roy-only items are bundled in that single message.

Each item in the digest is named exactly, with:

- Its task ID
- What it would do
- Its priority

Roy can approve or deny each item in that single check-in. There are no separate approval pings for the same items that day.

The one exception is Urgent items, which may still escalate immediately, outside the daily digest.

Items Roy does not answer in the digest are not auto-approved:

- Consequential items stay Held and return in the next day's digest.
- Internal Medium and Low items follow their notice periods in this policy, and are listed in the digest for review or reversal.

## Daily Approval Digest delivered at 9:00 AM CT daily

The Daily Approval Digest is delivered at **9:00 AM CT daily** (America/Chicago), as confirmed by Roy.

## The switch is on for internal approvals and never on for consequential ones

- The matrix is **ON** for Internal / Reversible Medium and Low approvals, as configured in this policy.
- The matrix is **OFF — and never on — for consequential auto-approval**. There is no switch setting that turns consequential auto-approval on.

Roy can turn the whole matrix off, change the notice periods, or change the digest time. An agent can never flip the switch.

The switch does not apply retroactively to items already pending as Roy-only. An item that was pending as Roy-only stays Roy-only under this policy.

## The clock starts on delivery, and every Muse approval is logged

The notice clock starts when the decision packet reaches Roy in chat — not when the card was created. The clock pauses if the packet is incomplete.

Every approval Muse makes under this policy is logged with:

- Task ID
- Date
- Action taken
- Reason it qualified
- Reversal path

Every such approval is also reported in the next daily digest, so Roy can review it and reverse it if he chooses.

## How to use it: worked examples

### Example A — Low internal queue move after 24 hours

A Queue Board card needs to move from Assigned to Awaiting Roy decision. That is Internal / Reversible, and its priority is Low.

What happens: A-01 delivers the decision packet to Roy in chat, and the 24-hour notice clock starts at that moment. If Roy does not reverse or decide it in that period, Muse may approve the stage move after 24 hours.

What is logged: task ID, date, the stage move taken, that it qualified as Low and Internal / Reversible after the full notice period, and the reversal path — move the card back to its prior stage.

What Roy sees in the digest: the approval is reported in the next Daily Approval Digest at 9:00 AM CT, listed for review or reversal.

### Example B — Medium internal verified-note filing after 72 hours

A verified note needs to be filed to Drive or GitHub. That is Internal / Reversible, and its priority is Medium.

What happens: A-01 delivers the decision packet to Roy in chat, and the 72-hour notice clock starts at that moment. The clock pauses if the packet is incomplete. If Roy does not reverse or decide it in that period, Muse may approve the filing after 72 hours.

What is logged: task ID, date, the filing taken, that it qualified as Medium and Internal / Reversible after the full notice period, and the reversal path — remove or supersede the filed note with a dated correction.

What Roy sees in the digest: the item is listed in the digests during its notice period, and the approval is reported in the next Daily Approval Digest at 9:00 AM CT after it proceeds, for review or reversal.

### Example C — High consequential DEV post held past its deadline

A draft is ready to post to DEV. Posting is consequential, and its priority is High.

What happens: A-01 prepares the decision packet and Roy sets the deadline for that item. If the deadline passes without Roy's explicit yes on that specific post, the item is not posted. Timeout means Held, not approved.

What is logged: the item is carried as Held, not approved, with its task ID and deadline. No Muse approval is entered, because Muse has no approval power over a consequential action.

What Roy sees in the digest: the post appears in the next Daily Approval Digest at 9:00 AM CT as Held, so Roy can approve or deny it in that single check-in.

### Example D — Urgent consequential item escalating the same day

An urgent item would spend, send, post, provision, or otherwise take a consequential action the same day.

What happens: the item stays Roy-only, with no timeout and no Muse approval. A-01 escalates it to Roy immediately with escalating reminders, even though a Daily Approval Digest is also delivered that day.

What is logged: the escalation, its task ID, what the action would do, and that it is awaiting Roy's explicit decision. Nothing proceeds on silence.

What Roy sees in the digest: in addition to the immediate escalation, the item is named in the Daily Approval Digest at 9:00 AM CT if it is still pending at that time, with its task ID, what it would do, and its Urgent priority.

---

Policy adopted 2026-10-25 by Roy's approval of the safe matrix design. Consequential auto-approval is explicitly excluded and cannot be enabled by this policy.
