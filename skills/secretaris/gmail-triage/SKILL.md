---
name: gmail-triage
description: >
  Scan a Gmail inbox, categorize emails by relevance, summarize relevant ones, and safely delete irrelevant ones with user confirmation. Use this skill whenever the user asks to triage, clean up, process, or go through their inbox or mailbox — even if they don't use the word "triage". Also trigger when the user says things like "check my emails", "what's in my inbox", "handle my mail", "clear out my inbox", "what emails need my attention", or "go through my messages". Works for both US Basketball club mail and general inbox. Always use this skill before running any Gmail searches or deletions.
---

# Gmail Triage Skill

## Purpose

Scan the inbox over a given time window, classify every email into one of three buckets, present a structured summary, resolve uncertain cases interactively, then delete irrelevant emails only after explicit user confirmation.

---

## Step 1: Determine Time Window

- If the user specifies a time window (e.g. "last 2 weeks", "since Monday"), use that.
- Otherwise, default to **the last 7 days**.
- Convert to a Gmail `after:` date filter (format: `YYYY/MM/DD`).

---

## Step 2: Fetch Emails

Use the Gmail tool to search the inbox with:
```
in:inbox after:YYYY/MM/DD
```

Retrieve enough metadata to classify each thread: sender, subject, snippet/body preview. Aim to fetch all threads in the window; paginate if needed.

---

## Step 3: Classify Each Thread

Assign each thread to exactly one bucket:

### 🟢 DEFINITELY RELEVANT
Threads that match any of the following:
- **Registration / deregistration requests** — someone asking to join or leave the club
- **Club info inquiries** — questions about the club, training, fees, schedule, location
- **Amstelcampus / USC Sport** — any communication from Amstelcampus or USC Sport (venue / facility), including zaalreservering@uscsport.nl
- **US OMNI** — communications from US OMNI (umbrella sports association)
- **NBB** — any communication from the NBB (Nederlands Basketball Bond) or NBB federation
- **Board members / bestuur** — emails from known board members
- **Penningmeester** — emails from the treasurer
- **Coaches** — emails from any coach of the club
- **Inter-club or federation business** — scheduling, referees, competition, fines, compliance
- Any email that **directly requires a decision or response** from the club secretary

### 🔴 DEFINITELY IRRELEVANT
Threads that match any of the following:
- Promotional or marketing emails
- Automated newsletters the user did not request a response to
- Delivery / shipping notifications unrelated to club activity
- Social media notifications
- Automated system alerts with no action required
- Spam

### 🟡 UNCERTAIN
Anything that doesn't clearly fit the above two buckets. When in doubt, put it here — do not delete without asking.

---

## Step 4: Present Structured Summary

Present results in this format:

---
### 🟢 Definitely Relevant (N threads)
For each thread:
- **From**: sender name / address
- **Subject**: subject line
- **Summary**: 1–2 sentence summary of what the email is about and what (if anything) it seems to require
- **Suggested next action**: e.g. "Draft a reply", "No action needed, for your awareness", "Forward to penningmeester"

---
### 🟡 Uncertain — Your Call (N threads)
For each thread:
- **From** / **Subject** / **Summary** (same format as above)
- **Why uncertain**: brief explanation of why classification wasn't clear
- **❓ Keep or delete?** — ask the user explicitly for each one, or offer to go through them one by one

---
### 🔴 To Delete (N threads)
List each thread with sender + subject only (no need for full summary).
**Do not delete yet.** End with:

> "I'd like to delete the N emails listed above. Shall I go ahead?"

---

## Step 5: Resolve Uncertain Threads

For each uncertain thread, wait for the user's decision:
- If **keep**: move it to the 🟢 Relevant section and offer suggested next actions
- If **delete**: add it to the 🔴 delete list

You can offer to go through uncertain threads one at a time or all at once — ask the user which they prefer if there are more than 3.

---

## Step 6: Execute Deletions

Only after the user confirms the delete list (including any uncertain threads they've decided to delete):

1. Use the Gmail tool to move each thread to Trash (apply the `TRASH` label or use the delete/trash endpoint)
2. Report back: "Done — N emails moved to trash."

Do **not** permanently delete (bypass trash). Moving to trash is sufficient and reversible.

---

## Notes & Edge Cases

- **Never delete a thread that's in the 🟢 bucket**, even if the user seems to be in a hurry.
- If a thread has multiple emails (a conversation), classify the whole thread as a unit based on the most recent message and the overall topic.
- If the inbox is very large (50+ threads in the window), mention the count upfront and ask if the user wants to proceed or narrow the window.
- If Gmail tool returns an error or auth issue, report it clearly and suggest reconnecting the Gmail integration.
- The skill intentionally does **not** draft replies or take further actions on relevant emails — that is handled by a separate follow-up skill.
