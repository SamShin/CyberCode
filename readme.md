# VulnLens — AI-Powered Web Application Security Scanner

> A hybrid static + AI-assisted vulnerability scanner for web applications. Scan GitHub repos or local projects, get severity-rated findings, and sync results across a web dashboard and CLI.

---

## Table of Contents

- [Overview](#overview)
- [Research Background](#research-background)
- [Architecture](#architecture)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Repository Structure](#repository-structure)
- [Modules In Detail](#modules-in-detail)
  - [Static Scanner](#1-static-scanner)
  - [AI Analysis Engine](#2-ai-analysis-engine)
  - [CLI](#3-cli)
  - [Backend (FastAPI)](#4-backend-fastapi)
  - [Frontend (React)](#5-frontend-react)
  - [Docker](#6-docker)
- [Scan Pipeline](#scan-pipeline)
- [Severity System](#severity-system)
- [API Key & CLI Sync](#api-key--cli-sync)
- [Website Pages](#website-pages)
- [Comparison / Show-Off Page](#comparison--show-off-page)
- [Phase 2 — Dynamic Analysis (Placeholder)](#phase-2--dynamic-analysis-placeholder)
- [Environment Variables](#environment-variables)
- [Getting Started](#getting-started)
- [Development Roadmap](#development-roadmap)
- [Contributing](#contributing)

---

## Overview

**VulnLens** is a research-driven security scanning tool that evaluates web applications for common vulnerabilities. It was built to support empirical research into whether AI-generated web applications are more vulnerable than human-developed ones.

The tool operates in two phases:

1. **Static Scanner** — a rule-based engine that reads source code and flags suspicious patterns, missing security headers, unsafe coding practices, and more.
2. **AI Analysis Engine** — an LLM (configurable to use a local or cloud model via API) that reviews flagged findings and important files (auth, config, etc.) to produce a deeper, context-aware security report with Low / Medium / High severity ratings.

There are two interfaces:
- A **CLI** for local or remote repo scanning, with optional account sync
- A **Website** (React + FastAPI) for remote repo scanning, account management, scan history, and a public comparison page

---

## Research Background

This project is built alongside academic research on the security of AI-generated web applications. The core research question is:

> *Are AI-generated web applications more vulnerable to common web security threats than human-developed applications?*

The scanner is designed to test for the OWASP Top 10 and other common vulnerability categories, producing CVSS-aligned severity scores that can be used to compare AI-generated vs human-written codebases. The website includes a dedicated **Comparison / Show-Off page** that presents static research findings visually.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                        User                             │
│              CLI  ──────────────  Website               │
└────────────────┬────────────────────────┬───────────────┘
                 │                        │
                 ▼                        ▼
        Local file path /         GitHub repo URL
        GitHub repo URL
                 │                        │
                 └──────────┬─────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Static Scanner    │  ← Phase 1
                 │  (Python engine)    │
                 │                     │
                 │ • Keyword matching  │
                 │ • Pattern checks    │
                 │ • File prioritizer  │
                 └────────┬────────────┘
                          │
                    Flagged findings +
                    important files
                          │
                          ▼
                 ┌─────────────────────┐
                 │  AI Analysis Engine │  ← Phase 1
                 │  (API — local or    │
                 │   cloud model)      │
                 │                     │
                 │ • Reviews findings  │
                 │ • Reads auth files  │
                 │ • Assigns severity  │
                 │ • Writes report     │
                 └────────┬────────────┘
                          │
                    Severity Report
                    (Low/Med/High)
                          │
              ┌───────────┴───────────┐
              ▼                       ▼
         CLI output             FastAPI backend
      (pretty print /          stores result in DB
       export JSON)            ← synced via API key
                                       │
                                       ▼
                                React Frontend
                               (dashboard, history,
                                comparison page)

  ┌─────────────────────────────────────────────────┐
  │  [Phase 2 — Placeholder]  Dynamic Analysis      │
  │  Docker spins up target repo → live HTTP probes │
  └─────────────────────────────────────────────────┘
```

---

## Features

### Core
- Scan a **GitHub repo URL** or **local project directory**
- **Static scanner** checks source code for vulnerability patterns without executing it
- **AI engine** performs deeper analysis on flagged files and priority files (auth, config, env)
- **Low / Medium / High** severity ratings per finding, plus an overall risk score
- Configurable AI backend — point to a **local model** (e.g. Ollama) or a **cloud model** (e.g. Claude, OpenAI) via API

### CLI
- Run scans directly from the terminal
- Accepts local path or GitHub repo URL as input
- Pretty-printed terminal output
- Optional JSON/HTML export of scan report
- **API key login** — syncs all scan results to your website account automatically
- Config stored at `~/.vulnlens/config.json`

### Website
- **Account system** — register, login, manage profile
- **Scan dashboard** — submit a GitHub repo URL, view results
- **Scan history** — all past scans with filterable results
- **Settings page** — manage API key, configure preferred AI model endpoint
- **Comparison / Show-Off page** — static research showcase comparing AI-generated vs human-written app scans
- **About page** — project background, research context

### Phase 2 (Placeholder — not yet implemented)
- Docker-based sandboxed environment to run target applications
- Live HTTP probing, header inspection, form fuzzing
- Dynamic analysis results merged into the report

---

## Tech Stack

| Layer | Technology |
|---|---|
| Static Scanner | Python |
| AI Engine | Python + HTTP (any OpenAI-compatible API) |
| CLI | Python (Click or Typer) |
| Backend | Python — FastAPI |
| Database | PostgreSQL (via SQLAlchemy) |
| Auth | JWT tokens + API key system |
| Frontend | React (Vite) + Tailwind CSS |
| Containerization | Docker + Docker Compose |
| Version Control | Git + GitHub |

---

## Repository Structure

```
vulnlens/
│
├── README.md
├── .env.example
├── docker-compose.yml
│
├── scanner/                        # Core scanning engine (shared by CLI + backend)
│   ├── __init__.py
│   ├── static/
│   │   ├── __init__.py
│   │   ├── engine.py               # Main static scan orchestrator
│   │   ├── rules/
│   │   │   ├── headers.py          # Missing security header checks
│   │   │   ├── secrets.py          # Hardcoded secrets, API keys
│   │   │   ├── injection.py        # SQL injection patterns, eval() usage
│   │   │   ├── auth.py             # Weak auth logic, password handling
│   │   │   ├── config.py           # Debug mode, dangerous framework settings
│   │   │   ├── cookies.py          # Insecure cookie flags
│   │   │   └── misc.py             # HTTP vs HTTPS, exposed admin pages, etc.
│   │   └── file_prioritizer.py     # Identifies important files (auth, config, .env)
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── engine.py               # AI analysis orchestrator
│   │   ├── prompts.py              # Prompt templates for the LLM
│   │   ├── client.py               # API client (supports local + cloud models)
│   │   └── severity.py             # Low/Med/High scoring logic
│   │
│   ├── report/
│   │   ├── __init__.py
│   │   ├── builder.py              # Assembles final report from static + AI output
│   │   ├── formatter_cli.py        # Pretty terminal output
│   │   └── formatter_export.py     # JSON and HTML export formats
│   │
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── local.py                # Reads a local directory
│   │   └── github.py               # Clones / fetches a GitHub repo
│   │
│   └── dynamic/                    # PHASE 2 PLACEHOLDER
│       ├── __init__.py
│       ├── placeholder.py          # Returns "dynamic analysis coming in phase 2"
│       └── README_phase2.md        # Notes on what dynamic analysis will involve
│
├── cli/                            # CLI interface
│   ├── __init__.py
│   ├── main.py                     # Entry point (Click/Typer app)
│   ├── commands/
│   │   ├── scan.py                 # `vulnlens scan <path|url>`
│   │   ├── login.py                # `vulnlens login` — set API key
│   │   ├── logout.py               # `vulnlens logout`
│   │   ├── history.py              # `vulnlens history` — list past synced scans
│   │   └── config.py               # `vulnlens config` — view/edit local config
│   └── auth.py                     # API key storage + sync logic
│
├── backend/                        # FastAPI backend
│   ├── __init__.py
│   ├── main.py                     # FastAPI app entry point
│   ├── config.py                   # App settings (reads from .env)
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── auth.py             # Register, login, logout
│   │   │   ├── scans.py            # Submit scan, get results, list history
│   │   │   ├── users.py            # Profile, settings
│   │   │   └── apikeys.py          # Generate / revoke API keys
│   │   └── dependencies.py         # Auth middleware, DB session injection
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py                 # User DB model
│   │   ├── scan.py                 # Scan job + results DB model
│   │   └── apikey.py               # API key DB model
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py                 # Pydantic schemas for user
│   │   ├── scan.py                 # Pydantic schemas for scan
│   │   └── report.py               # Pydantic schemas for report output
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── scan_service.py         # Orchestrates scanner pipeline for backend
│   │   └── user_service.py         # User business logic
│   │
│   └── db/
│       ├── __init__.py
│       ├── session.py              # SQLAlchemy session setup
│       └── migrations/             # Alembic migrations
│
├── frontend/                       # React (Vite) frontend
│   ├── index.html
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── package.json
│   └── src/
│       ├── main.jsx
│       ├── App.jsx
│       ├── api/                    # Axios API client calls
│       │   ├── auth.js
│       │   ├── scans.js
│       │   └── user.js
│       ├── components/             # Reusable UI components
│       │   ├── Navbar.jsx
│       │   ├── Footer.jsx
│       │   ├── ScanCard.jsx
│       │   ├── SeverityBadge.jsx
│       │   ├── FindingRow.jsx
│       │   └── ReportViewer.jsx
│       └── pages/
│           ├── Home.jsx            # Landing page
│           ├── Login.jsx
│           ├── Register.jsx
│           ├── Dashboard.jsx       # Submit scan + view results
│           ├── History.jsx         # Past scan list
│           ├── ScanDetail.jsx      # Full report for a single scan
│           ├── Settings.jsx        # API key, model config
│           ├── Comparison.jsx      # Static show-off / research comparison page
│           └── About.jsx
│
├── docker/
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── nginx.conf                  # Reverse proxy config
│
├── tests/
│   ├── scanner/
│   │   ├── test_static_engine.py
│   │   ├── test_rules.py
│   │   └── test_ai_engine.py
│   ├── backend/
│   │   ├── test_auth.py
│   │   └── test_scans.py
│   └── cli/
│       └── test_commands.py
│
└── docs/
    ├── architecture.md             # Detailed architecture notes
    ├── scan_rules.md               # Full list of static scan rules and what they catch
    ├── ai_prompts.md               # Prompt design documentation
    ├── api_reference.md            # FastAPI endpoint reference
    └── phase2_dynamic.md           # Phase 2 dynamic analysis design notes
```

---

## Modules In Detail

### 1. Static Scanner

Located in `scanner/static/`. This runs first, before any AI call.

**What it checks:**

| Category | Examples |
|---|---|
| Security headers | Missing `Content-Security-Policy`, `X-Frame-Options`, `HSTS` |
| Secrets | Hardcoded API keys, passwords, tokens in source files |
| Injection | String-concatenated SQL queries, `eval()` usage, unsanitized inputs |
| Auth | Weak password hashing, unsafe session logic, missing rate limiting signals |
| Configuration | Debug mode enabled, dangerous framework settings, exposed admin/debug pages |
| Cookies | Missing `HttpOnly`, `Secure`, `SameSite` flags |
| Misc | HTTP instead of HTTPS, suspicious query parameters, exposed `.env` files |

**File prioritizer** (`file_prioritizer.py`) identifies high-importance files regardless of findings — files with names like `auth`, `login`, `config`, `settings`, `.env`, `middleware`, `session`, `password`, `token`, `jwt`, `user` — these are always passed to the AI engine.

**Output:** A structured list of `Finding` objects, each with:
- File path
- Line number (where applicable)
- Rule that triggered
- Code snippet
- Preliminary severity suggestion (Low / Med / High)

---

### 2. AI Analysis Engine

Located in `scanner/ai/`. Runs after the static scanner.

**Inputs:**
- List of flagged findings from the static scanner
- Contents of prioritized files (auth, config, etc.)

**What it does:**
- Sends structured prompts to the configured LLM API
- Asks the model to review each finding in context
- Asks for a holistic review of auth and config files
- Produces per-finding severity adjustments and explanations
- Generates an overall risk summary

**Model config** (`scanner/ai/client.py`):
- Reads the model endpoint from environment or user config
- Compatible with any OpenAI-format API (Claude via API, OpenAI, Ollama locally, etc.)
- Configurable from the website settings page or CLI config

**Severity logic** (`scanner/ai/severity.py`):
- Each finding is rated **Low**, **Medium**, or **High**
- An overall repo score is computed as a weighted average
- Aligned with CVSS scoring philosophy

---

### 3. CLI

Located in `cli/`. Built with **Typer** (or Click).

**Commands:**

```bash
vulnlens scan <path_or_url>        # Scan a local path or GitHub repo URL
vulnlens scan <url> --export json  # Export report to JSON file
vulnlens scan <url> --export html  # Export report to HTML file
vulnlens scan <url> --no-sync      # Scan without syncing to account

vulnlens login                     # Enter API key to link to website account
vulnlens logout                    # Remove stored API key
vulnlens history                   # List past scans synced to your account
vulnlens config                    # View or edit local config (model endpoint etc.)
```

**Config file** at `~/.vulnlens/config.json`:
```json
{
  "api_key": "vl_xxxxxxxxxxxx",
  "api_base_url": "https://yourdomain.com/api",
  "model_endpoint": "https://api.anthropic.com/v1",
  "model_name": "claude-3-5-sonnet-20241022",
  "default_export": null
}
```

When an API key is set, every scan result is automatically posted to the backend and appears in the website's scan history.

---

### 4. Backend (FastAPI)

Located in `backend/`. The API server that powers the website and receives CLI syncs.

**Key endpoints:**

| Method | Route | Description |
|---|---|---|
| POST | `/auth/register` | Create account |
| POST | `/auth/login` | Login, receive JWT |
| POST | `/auth/logout` | Invalidate token |
| GET | `/users/me` | Get current user profile |
| PUT | `/users/me` | Update profile / settings |
| POST | `/apikeys/generate` | Generate a new CLI API key |
| DELETE | `/apikeys/{id}` | Revoke an API key |
| POST | `/scans/` | Submit a new scan (website or CLI sync) |
| GET | `/scans/` | List all scans for current user |
| GET | `/scans/{id}` | Get full report for a scan |
| DELETE | `/scans/{id}` | Delete a scan from history |

**Auth:**
- Website users authenticate with JWT (stored in HTTP-only cookie)
- CLI authenticates via `Authorization: Bearer vl_xxx` API key header

---

### 5. Frontend (React)

Located in `frontend/`. Built with **Vite + React + Tailwind CSS**.

**Pages:**

| Page | Route | Description |
|---|---|---|
| Home | `/` | Landing page — what is VulnLens, how it works |
| Login | `/login` | User login |
| Register | `/register` | User registration |
| Dashboard | `/dashboard` | Submit GitHub repo URL, view latest scan |
| History | `/history` | Browse all past scans with filters |
| Scan Detail | `/scans/:id` | Full report — findings, severities, AI analysis |
| Settings | `/settings` | Manage API key, model endpoint preference |
| Comparison | `/comparison` | Static research showcase page (see below) |
| About | `/about` | Project background, research context, team |

---

### 6. Docker

Located in `docker/` and `docker-compose.yml`.

**Services:**
- `backend` — FastAPI app
- `frontend` — React build served via Nginx
- `db` — PostgreSQL database
- `nginx` — Reverse proxy routing `/api` to backend, `/` to frontend

**Phase 2 placeholder:** A `sandbox` service stub is included in `docker-compose.yml` with a comment explaining it will spin up target repos for dynamic analysis in phase 2.

---

## Scan Pipeline

Here is the full flow from input to report:

```
1. Input received
   └── GitHub URL → clone repo to temp dir   (scanner/ingestion/github.py)
   └── Local path → read directly            (scanner/ingestion/local.py)

2. File prioritizer runs
   └── Flags auth/config/session/env files as high-priority
                                             (scanner/static/file_prioritizer.py)

3. Static scanner runs on all files
   └── Applies all rules from scanner/static/rules/
   └── Produces list of Finding objects with preliminary severity

4. AI engine runs
   └── Receives: flagged findings + priority file contents
   └── Sends structured prompts to model API
   └── Receives: per-finding severity review + overall summary
                                             (scanner/ai/engine.py)

5. Report assembled
   └── Findings merged with AI analysis
   └── Overall severity score computed
                                             (scanner/report/builder.py)

6. Output
   └── CLI: pretty-printed to terminal, optional JSON/HTML export
   └── Website: stored in DB, displayed in React frontend
   └── CLI with API key: also POSTed to backend and stored
```

---

## Severity System

Each finding is rated on a three-tier system:

| Level | Color | Description | Example |
|---|---|---|---|
| 🔴 High | Red | Directly exploitable, critical risk | Hardcoded DB password, SQL injection, no auth |
| 🟡 Medium | Yellow | Significant weakness, requires conditions to exploit | Missing CSRF protection, weak hashing |
| 🟢 Low | Green | Best practice violation, low direct impact | Missing security header, verbose error messages |

The static scanner assigns a **preliminary** severity based on rule definitions. The AI engine can **confirm, upgrade, or downgrade** the severity based on context.

An **overall risk score** (0–100) is computed as a weighted sum across all findings and displayed prominently in the report.

---

## API Key & CLI Sync

1. User creates an account on the website
2. User goes to **Settings → API Keys → Generate**
3. A key like `vl_abc123xyz` is shown once — user copies it
4. User runs `vulnlens login` in the terminal and pastes the key
5. Key is saved to `~/.vulnlens/config.json`
6. All future CLI scans are automatically synced to the user's account
7. Results appear in the website's History and Dashboard instantly

The user can revoke keys from the Settings page at any time. Multiple keys can exist (e.g. one per machine).

---

## Website Pages

### Comparison / Show-Off Page (`/comparison`)

This is a **static, hardcoded** page (no live scanning) that presents research findings visually. It is the public-facing research showcase. Content includes:

- Explanation of why AI-generated code security matters
- Side-by-side scan report of a known AI-generated web app vs a human-written web app
  - Finding counts by severity
  - Categories of vulnerabilities found
  - Overall risk scores
- Key takeaways from the research
- A call to try the scanner

This page requires no login and is meant to be shared and presented.

### About Page (`/about`)

- What is VulnLens
- Research background and motivation
- How the scanner works (plain English)
- Tech stack overview

---

## Phase 2 — Dynamic Analysis (Placeholder)

Dynamic analysis is **not implemented in phase 1** but the codebase is structured to support it.

**Placeholder:** `scanner/dynamic/placeholder.py` returns a standard "Phase 2 — coming soon" response. The frontend Scan Detail page has a greyed-out "Dynamic Analysis" section with a "Coming soon" label.

**What phase 2 will involve** (documented in `docs/phase2_dynamic.md`):
- Docker sandbox spins up the target repo as a live service
- HTTP probes check actual response headers in a live context
- Form endpoints are discovered and tested
- Input fuzzing checks for reflected output
- Network-level checks (HTTP vs HTTPS enforcement, redirect behavior)
- Results merged into the existing report format under a new `dynamic_findings` field

---

## Environment Variables

Copy `.env.example` to `.env` and fill in:

```env
# Backend
DATABASE_URL=postgresql://user:password@db:5432/vulnlens
SECRET_KEY=your_jwt_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# AI Model
AI_MODEL_ENDPOINT=https://api.anthropic.com/v1        # or local Ollama URL
AI_MODEL_NAME=claude-3-5-sonnet-20241022
AI_API_KEY=your_model_api_key_here

# Frontend (Vite)
VITE_API_BASE_URL=http://localhost:8000
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Docker + Docker Compose
- A model API key (Claude, OpenAI, or local Ollama running)

### Run with Docker (recommended)

```bash
git clone https://github.com/yourname/vulnlens.git
cd vulnlens
cp .env.example .env
# Fill in your .env values
docker-compose up --build
```

Frontend at `http://localhost:3000`, backend at `http://localhost:8000`

### Run locally (development)

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**CLI:**
```bash
cd cli
pip install -e .
vulnlens --help
```

---

## Development Roadmap

### Phase 1 — Current Scope
- [x] Repository structure and architecture design
- [ ] Static scanner engine + rules
- [ ] File prioritizer
- [ ] AI analysis engine + prompt design
- [ ] Report builder (CLI + JSON/HTML export)
- [ ] Repo ingestion (local + GitHub)
- [ ] CLI with login/sync
- [ ] FastAPI backend (auth, scans, API keys)
- [ ] React frontend (all pages)
- [ ] Docker Compose setup
- [ ] Comparison / show-off page with research data
- [ ] Tests

### Phase 2 — Future
- [ ] Docker sandbox for target apps
- [ ] Dynamic HTTP probing
- [ ] Form discovery and fuzzing
- [ ] Network-level checks
- [ ] Merge dynamic findings into report

---

## Contributing

This is a school research project. If you are a collaborator:

1. Branch naming: `feature/your-feature-name`, `fix/bug-description`
2. Keep scanner rules modular — one file per category in `scanner/static/rules/`
3. All prompts go in `scanner/ai/prompts.py` — do not hardcode prompt strings elsewhere
4. Run tests before pushing: `pytest tests/`
5. Document any new scan rule in `docs/scan_rules.md`