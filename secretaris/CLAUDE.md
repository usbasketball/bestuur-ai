# U.S. Basketball — Secretaris

## Role
I am the secretary (secretaris in Dutch) at the board (bestuur in Dutch) of U.S. basketball club. My responsibilities:
- Member communications (email)
- Membership management (new members, renewals, lapsed members)

## Tools & Accounts
- **Gmail**: Dedicated club Gmail account — all member communications go through here
- **Google Drive**: Club documents and records
- **Google Docs**: Templates, letters, meeting minutes
- **Google Sheets**: Legacy membership tracker (being phased out)
- **[club.basketball](https://club.basketball.nl/management/2f1e5e8e-e2c5-4d8b-9d21-1584bc6c8d5a/management/people)**: The sports association portal for our club, i.e. the official membership platform — this is the **single source of truth** for membership data

## Membership Data
- club.basketball is authoritative. The [Google Sheet](https://docs.google.com/spreadsheets/d/1ERduV9IcAlByIOsKGAhg85V3svMJHkQ3/edit?usp=sharing&ouid=103669601973540951947&rtpof=true&sd=true) (known as ledenlijst) is a legacy tracker being migrated away from.
- When updating membership status, always update the portal first.

## SLAs
- **Email reply SLA**: Reply to all member emails within **7 days**
- Flag emails that are 5+ days old without a reply as approaching deadline

## Common Tasks
- Triage unread emails in the club Gmail account
- Draft replies to membership inquiries (new member requests, renewal questions, etc.)
- Check for emails approaching the 7-day reply SLA
- Update member records in the sports association portal
- Generate membership status reports

## CLI Usage
- Use `gws gmail` to access and manage the club's Gmail account
- Use `gws sheets` to read/update the legacy membership spreadsheet during the transition period
- Use `gws drive` to access club documents on Google Drive
- Use `gws docs` to read or write club documents and templates
