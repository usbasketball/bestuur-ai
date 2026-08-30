---
name: registration-form-link
description: Generates signed, expiring registration links (/register) for https://usbasketball.nl (production) via scripts/generate_registration_link.py. Use when the user asks for a registration URL, register link, or expiring registration form link.
---

# Registration Form Link

Generate signed, expiring access links for the private registration page (`/register`) of https://usbasketball.nl. Links are HMAC-signed by `scripts/generate_registration_link.py`, which reads `REGISTRATION_SECRET` from `.env.local` automatically.

## Step 1 — Base URL

Always generate for **production**: `https://usbasketball.nl`.

## Step 2 — Determine the duration

Parse the desired validity in hours from the request. Default to 72 hours when unspecified. Reject non-positive values.

## Step 3 — Generate the link

From the repository root, run:

```bash
python3 scripts/generate_registration_link.py <hours>
```

Notes:

- Never read, print, or echo `REGISTRATION_SECRET`. If the script fails because it is missing, tell the user to add it to `.env.local` (and to Vercel/GCP Secret Manager env vars for deployed environments) — do not ask them to paste the secret into chat.
- Do not modify any project files while generating links; this skill only runs the script and reports its output.

## Step 4 — Report

Reply with:

- The full signed URL in a code block, ready to copy-paste and share.
- The exact expiry date/time shown by the script.
- Which environment the link targets.
- A one-line reminder that the link is a bearer token: anyone who has it can register until it expires.
