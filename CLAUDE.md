# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a multi-module workspace for generating automated bibliometric reports at Université Paris-Saclay's DiBISO department. Two report types are supported:
- **BiSO** (Bilan Science Ouverte): open-science annual reports for research labs
- **PubPart** (Publications & Partnerships): topic/institution/collaboration analysis

The workspace contains 5 subprojects: two Python libraries (`dibisoreporting`, `dibisoplot`), a LaTeX template collection (`dibiso-latex-templates`), a FastAPI backend (`dibiso-reporting-api`), and a React frontend (`dibiso-reporting-webapp`).

## Development Commands

### Python libraries

```bash
# Install in development mode from repo root
pip install -e dibisoreporting/
pip install -e dibisoplot/

# Build a distribution
cd dibisoreporting/   # or dibisoplot/
python -m build
python -m twine upload dist/*
```

### API (`dibiso-reporting-api/`)

```bash
cp .env.template .env   # then fill in secrets
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or via Docker
docker-compose up
```

### Webapp (`dibiso-reporting-webapp/`)

```bash
cp .env.template .env   # set VITE_API_URL
npm install
npm run dev      # dev server
npm run build    # production build
npm run lint     # ESLint
docker-compose up
```

There are no automated test suites; validation is done manually via the API and webapp.

## Architecture

### Data flow

```
React Webapp  →  FastAPI  →  background thread:
                               1. fetch data (HAL / OpenAlex / ScanR APIs)
                               2. dibisoplot  → Plotly figures (PDF + LaTeX)
                               3. dibisoreporting → names_and_macros.tex + figure layout
                               4. LuaTeX compilation (3 passes + Biber + 2 more passes)
                             ↓
                          PDF/ZIP download via authenticated endpoint
```

### Key class hierarchy

**`DibisoReporting`** (`dibisoreporting/dibisoreporting/dibisoreporting.py`)
- Manages LaTeX project directory, acquires template files (local path or GitHub release URL)
- Creates `names_and_macros.tex` with all LaTeX macro definitions
- Orchestrates figure generation by instantiating `dibisoplot` classes
- `Biso` and `PubPart` subclasses live in their respective subdirectories

**`Dibisoplot`** (`dibisoplot/dibisoplot/dibisoplot.py`)
- Base for all chart types; wraps Plotly with consistent styling
- Tracks per-figure data status: `NOT_FETCHED`, `OK`, `NO_DATA`, `ERROR`
- Converts DataFrames to LaTeX `longtable` output
- Dynamic height calculation for horizontal bar charts
- 12 BiSO visualization subclasses in `dibisoplot/dibisoplot/biso/biso.py` (e.g. `AnrProjects`, `CollaborationMap`, `Journals`, `WorksType`)

**FastAPI app** (`dibiso-reporting-api/app/main.py`)
- JWT auth (48-hour tokens, `OAuth2PasswordBearer`)
- Report jobs run in a `ThreadPoolExecutor` (default 4 workers, configurable via env)
- Compilation status tracked with progress % and current step; supports cancellation by terminating the subprocess
- Auto-cleanup of old temp directories (configurable retention period)
- Key endpoints: `POST /generate-report`, `GET /compilation-status/{comp_id}`, `POST /cancel-compilation/{comp_id}`, `GET /download-pdf`, `GET /download-zip`

**React frontend** (`dibiso-reporting-webapp/src/App.jsx`)
- Single-file component handling auth, report form, status polling, downloads, and admin user management

### LaTeX compilation details

LuaTeX is invoked via subprocess with a default 180-second timeout. The sequence is:
1. `lualatex` × 3 on main file
2. `biber` for bibliography
3. `lualatex` × 2 on biblio file

Default latexmkrc: `$pdflatex = 'lualatex %O %S --shell-escape'; $pdf_mode = 1;`

### External API dependencies

- **HAL** (`https://api.archives-ouvertes.fr/`) — publication metadata
- **OpenAlex** — bibliometric analysis (via `openalex-analysis` / `pyalex`)
- **ScanR** — French research project data
- **GitHub API** — fetching latest LaTeX template releases

### Environment configuration

Both `dibiso-reporting-api/.env.template` and `dibiso-reporting-webapp/.env.template` must be copied to `.env` and filled in before running. The API template defines 55+ variables covering JWT secrets, admin credentials, LaTeX paths, external API credentials, CORS settings, thread-pool size, database location, and timeouts.

The SQLite user database schema: `id, username, email, hashed_password, role (user|admin), is_active, created_at`.
