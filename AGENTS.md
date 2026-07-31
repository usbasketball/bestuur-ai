# US Basketball Amsterdam – Bestuur (Board)

## About US Basketball

[U.S. Basketball Amsterdam](https://www.usbasketball.nl) is one of Amsterdam's basketball clubs, founded in 1951. The club motto is *"If you can't beat US, join US."* It is a senior-only club (18+) with 12 teams (men's and women's), playing home games on Sundays at the **Amstelcampushal** (Tweede Boerhaavestraat 10, Amsterdam). The club is affiliated with the **NBB** (Nederlandse Basketball Bond) and uses **club.basketball** (powered by Focus on Your Sport) as its primary membership management system.

Membership types at US:
- **Competition players** (wedstrijdspelend) — play in official NBB leagues, train 1–2x per week
- **Recreational members** (recreanten) — training only, allowed to play max. 3 games per season (except in D1 promotion division, where only competition members may play)
- **Free training members** (vrij trainen leden) — train without federation membership
- **3x3 members** — participate in 3x3 basketball

---

## The Board (Het Bestuur)

The board is responsible for running the club. It consists of five roles:

| Role | Dutch | Responsibility | Details |
|------|-------|----------------|---------|
| Chairperson | Voorzitter | Leads the board, chairs meetings, represents the club externally | — |
| Secretary | Secretaris | Administration, membership records, correspondence, meeting minutes | [SECRETARIS.md](./SECRETARIS.md) |
| Treasurer | Penningmeester | Club finances: budgets, payments, financial reporting | — |
| Game Secretary | Wedstrijdsecretaris | Match organisation, scheduling, coordination with leagues and teams | — |
| General Member | Algemeen Lid | Supports the board with tasks, projects, and events as needed | — |

The board can be reached at **bestuur@usbasketball.nl**.

---

## Key Resources

| Resource | URL / Contact |
|----------|---------------|
| Club website | https://www.usbasketball.nl |
| Membership system | https://club.basketball.nl |
| NBB club page | https://basketball.nl/basketball/competities/vereniging-zoeken/#/clubs/2f1e5e8e-e2c5-4d8b-9d21-1584bc6c8d5a/details |
| Duty schedule | https://www.usbasketball.nl/takenschema |
| Training schedule | https://www.usbasketball.nl/trainingschema |
| Board email | bestuur@usbasketball.nl |
| Secretary email | secretaris@usbasketball.nl |
| Annual planning | See Jaarplanning.docx (Google Drive) |
| Board handbook | See [Bestuur Overzicht](https://docs.google.com/document/d/1lmasOPzf8m-lbooAG6N3aaCkbhVtw8O9NRXfyZXwK3c/edit) |

---

## Using AI Agents in This Repository

This repository makes board work easier with the help of AI agents. Each role has its own dedicated markdown file with detailed context and agent use cases. It is agent-agnostic: it works with any AI coding agent that reads `AGENTS.md` (Claude Code, opencode, Cursor, Codex, Gemini CLI, GitHub Copilot, etc.).

When working with an AI agent in this repo:
- Provide relevant context (e.g. current membership lists, email threads, season dates) for best results
- For sensitive member data, do not paste raw personal information — use anonymised or summarised inputs where possible
- Agents can help draft communications, summarise documents, check consistency, and generate structured data, but final decisions and approvals always rest with the board member responsible

---

## Role Files

Per-role context lives in nested `AGENTS.md` files, which agents read based on the working directory:

| Role | File |
|------|------|
| Secretary | [SECRETARIS.md](./SECRETARIS.md) (overview) · [secretaris/AGENTS.md](./secretaris/AGENTS.md) (agent context) |

---

## Skills

Specialised workflows are bundled as skills using the [Agent Skills](https://agentskills.io) standard (`SKILL.md` with YAML frontmatter). They live in `.agents/skills/` and are auto-discovered by tools that support Agent Skills (Claude Code via `.claude/skills/`, opencode, Codex, Gemini CLI, Cursor, and others).

| Skill | Path | What it does |
|-------|------|--------------|
| gmail-triage | `.agents/skills/gmail-triage/SKILL.md` | Scans a Gmail inbox, classifies each email as relevant / uncertain / irrelevant, presents a structured summary, and deletes irrelevant emails only after user confirmation |

If a tool does not support Agent Skills natively, read the `SKILL.md` file directly and follow its steps.

---

## Repository Layout

```
AGENTS.md                     # This file — repo-wide context
SECRETARIS.md                 # Secretary role overview
secretaris/AGENTS.md          # Secretary role context for agents
.agents/skills/               # Skills (canonical, Agent Skills standard)
.claude/skills/               # Symlinks so Claude Code auto-discovers skills
```
