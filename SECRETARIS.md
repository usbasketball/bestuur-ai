# Secretary (Secretaris)

> Part of the [US Basketball Bestuur](./AGENTS.md). Contact: secretaris@usbasketball.nl

The secretary owns the **membership records** for the club, which are kept in sync across three systems:

| System | Purpose |
|--------|---------|
| **club.basketball** | Source of truth: membership, team, contact, and financial info |
| **Ledenlijst** | Internal record: extra info such as bench team (bankteam), referee license, etc. |
| **Google Contacts** | Used for sending email announcements to members |

> ⚠️ The information across all three systems must always be kept in sync.

---

## Membership Updates

Membership record changes only happen through two official channels:
1. **Team talks** (teamgesprekken) — typically at the start of the season
2. **Email requests** to the secretary

For 5v5 members (competition and recreational), updates are usually finalised after team talks. For 3x3 and free training members, the secretary reaches out at the start of the season to confirm their list.

---

## Membership Types

*Club membership (clublidmaatschap)* — determines what the club invoices members:
- Wedstrijdspelend 2x trainen
- Wedstrijdspelend 1,5x trainen
- Wedstrijdspelend 1x trainen
- Recreanten (incl. vrij trainen lid)
- 3x3 lid

*Federation membership (bondslidmaatschap)* — determines what the club pays to the NBB:
- Wedstrijd spelend lid (incl. 3x3 lid)
- Recreant lid
- Niet-spelend lid
- G-spelend lid

> ℹ️ Free training members (vrij trainen lid) do **not** have a federation membership.

---

## Cross-Role Dependencies

- Works with **Game Secretary** on the duty schedule (takenschema) — requires the up-to-date list of playing members responsible for referee/table duties
- Works with **Treasurer** on auto-invoicing (incasso) — requires financial info (incl. discount type) and both membership types to be filled in for all active members

---

## Key Policies

- Registration and de-registration must always happen via email (including 3x3 and free training members)
- Recreational members (recreanten) may play max. 3 games per season — except in D1 (promotion division), where only competition members may participate
- The SEPA authorisation form (machtigingsformulier) is kept for internal records only (audit proof)
- The proof of enrolment (Bewijs van Inschrijving, BVI) is used internally as proof for student discounts

---

## club.basketball Support

- Kennisbank: https://club.basketball.nl/kb/articles
- Support email: support@focusonyoursport.nl
- Support tickets: https://support.focusonyoursport.nl/support/tickets

---

## Future AI Use Cases

- Drafting member registration/de-registration confirmation emails
- Checking consistency between membership lists
- Answering member queries about membership types, fees, or deadlines
- Generating communication for the start-of-season member confirmation flow
