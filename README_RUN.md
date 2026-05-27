# DiBISOreports — Guide de démarrage et génération de rapports

Ce guide décrit comment démarrer l'application en développement local (Windows) et générer un rapport BiSO, en illustrant avec le labo **LGI** (année **2024**).

---

## Prérequis

| Outil | Version testée | Rôle |
|-------|---------------|------|
| Python | 3.12+ | Backend API + bibliothèques |
| Node.js / npm | 22+ | Frontend React |
| pip / venv | — | Gestion des dépendances Python |

---

## 1. Structure du projet

```
dibisoreports/
├── dibiso-html-templates/   ← Templates Jinja2 HTML (local)
│   └── dibiso-html/         ← Utilisé directement pour éviter le téléchargement GitHub
├── dibiso-reporting-api/    ← FastAPI backend
│   ├── app/
│   │   ├── main.py          ← Point d'entrée API
│   │   ├── auth.py          ← JWT authentification
│   │   └── users.py         ← Gestion utilisateurs (SQLite)
│   ├── api_data/            ← Base SQLite (créée au 1er démarrage)
│   ├── .env                 ← Variables d'environnement (à configurer)
│   └── requirements.txt
├── dibiso-reporting-webapp/ ← React frontend
│   ├── src/App.jsx          ← Composant unique
│   └── .env                 ← VITE_API_URL
├── dibisoreporting/         ← Bibliothèque Python locale (source)
├── dibisoplot/              ← Bibliothèque Python locale (source)
└── .venv/                   ← Environnement virtuel
```

---

## 2. Installation des dépendances

### 2.1 Environnement virtuel Python

```bash
# Depuis la racine du projet
python -m venv .venv

# Activation (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Activation (bash / Git Bash)
source .venv/Scripts/activate
```

### 2.2 Installer les bibliothèques locales (IMPORTANT)

Les bibliothèques locales `dibisoreporting` et `dibisoplot` contiennent des fonctionnalités
(templates HTML, `render_from_saved`) non encore publiées sur PyPI. Il faut les installer
en mode développement depuis les sources locales :

```bash
pip install -e dibisoreporting/ -e dibisoplot/
```

> ⚠️ **Ne pas** faire `pip install dibisoreporting` (version PyPI obsolète).

### 2.3 Installer les dépendances de l'API

```bash
pip install -r dibiso-reporting-api/requirements.txt
```

### 2.4 Installer les dépendances du frontend

```bash
cd dibiso-reporting-webapp
npm install
cd ..
```

---

## 3. Configuration

### 3.1 API — `dibiso-reporting-api/.env`

Copier `.env.template` vers `.env` et remplir les secrets. Points critiques pour Windows :

```dotenv
## Chemin de la base SQLite (relatif à l'API, pas /api_data Linux)
USERS_DATABASE_NAME=users.db
USERS_DATABASE_DIRECTORY=./api_data

## Admin créé automatiquement au 1er démarrage si aucun admin n'existe
ADMIN_USERNAME=hb.admin
ADMIN_PASSWORD=hb__2026

## Clé JWT (longue chaîne aléatoire)
SECRET_KEY=<générer avec: python -c "import secrets; print(secrets.token_hex(64))">

## Templates HTML — utiliser le chemin local si disponible (évite le téléchargement GitHub)
HTML_TEMPLATE_URL=https://github.com/dibiso-upsaclay/dibiso-html-templates/releases/latest
## IMPORTANT: pointer vers le DOSSIER PARENT de dibiso-html/, pas dibiso-html/ lui-même.
## render_from_saved cherche {root}/dibiso-html/ et get_html_template_from_path copie
## le CONTENU du répertoire pointé, donc dibiso-html/ doit être à l'intérieur.
HTML_TEMPLATE_PATH=C:/path/to/dibisoreports/dibiso-html-templates

## Cache OpenAlex — utiliser le répertoire par défaut de openalex-analysis
## pour que les données persistent entre sessions
OPENALEX_ANALYSIS_CACHE_PATH=C:/path/to/openalex-analysis/data

## Timeout de récupération des données (1ère exécution : 20 min minimum)
DATA_FETCHING_TIMEOUT_SECONDS=1200

## ScanR
SCANR_API_PASSWORD=<mot_de_passe>
SCANR_API_URL=cluster-production.elasticsearch.dataesr.ovh
SCANR_API_USERNAME=paris-saclay
SCANR_BSO_INDEX=bso-publications
SCANR_PUBLICATIONS_INDEX=scanr-publications

## OpenAlex
OPENALEX_API_KEY=<clé_api>
OPENALEX_EMAIL=<email>

## CORS
CORS_ALLOW_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
CORS_ALLOW_CREDENTIALS=true
CORS_ALLOW_METHODS=*
CORS_ALLOW_HEADERS=*

## Pool de threads
THREAD_POOL_MAX_WORKERS=4
ACCESS_TOKEN_EXPIRE_HOURS=48
PROJECTS_PERSISTENCE_TIME_HOURS=4
PROJECTS_ANALYSES_RETENTION_DAYS=30
```

> **Attention aux chemins Windows** : utiliser des slashes (`/`) ou des doubles
> anti-slashes (`\\`). Les anti-slashes simples (`\`) dans les valeurs `.env`
> provoquent des erreurs `SyntaxError: unicode escape` dans le sous-processus Python.

### 3.2 Webapp — `dibiso-reporting-webapp/.env`

```dotenv
VITE_API_URL=http://127.0.0.1:8000
```

---

## 4. Démarrage des services

### 4.1 Démarrer l'API

```powershell
# Depuis dibiso-reporting-api/ (important : ne pas lancer depuis la racine du projet)
cd dibiso-reporting-api
..\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Au 1er démarrage :
- La base SQLite est créée dans `api_data/users.db`
- L'utilisateur admin est créé automatiquement (depuis `ADMIN_USERNAME`/`ADMIN_PASSWORD`)

Vérification :

```bash
curl http://localhost:8000/health
# → {"status":"healthy","message":"API is running"}
```

### 4.2 Démarrer le frontend

```bash
cd dibiso-reporting-webapp
npm run dev
```

L'interface est accessible sur **http://localhost:3000**.

---

## 5. Génération d'un rapport BiSO — exemple LGI 2024

### 5.1 Se connecter

Ouvrir http://localhost:3000 → cliquer **Login** → saisir les identifiants admin.

### 5.2 Remplir le formulaire

| Champ | Valeur (exemple LGI) |
|-------|---------------------|
| Année | 2024 |
| Acronyme | LGI |
| Nom complet | Laboratoire Génie Industriel |
| Collection HAL | LGI |
| Max entités | 500 |

> Le champ **Collection HAL** est l'identifiant utilisé dans l'URL HAL :
> `https://hal.science/search/index/?q=*&collCode_s=LGI`

### 5.3 Lancer la génération

Cliquer **Generate Report**. L'interface affiche une barre de progression.

### 5.4 Déroulement du processus

```
1. Vérification de la collection HAL  (2%)
2. Démarrage du sous-processus         (5%)
3. Récupération des données            (10%)   ← LONG (voir ci-dessous)
   ├── HAL API — publications, revues, conférences
   ├── OpenAlex — analyse bibliométrique, collaborations
   └── ScanR — projets ANR et européens
4. Génération des figures Plotly       (10-70%)
5. Rendu HTML via Jinja2               (72%)
6. Conversion HTML → PDF (WeasyPrint)  (80-88%)
7. Création de l'archive ZIP           (98%)
8. Terminé                            (100%)
```

### 5.5 Durée estimée

| Situation | Durée approximative |
|-----------|-------------------|
| 1ère exécution (aucun cache OpenAlex) | ~5 min pour LGI/2024 (169 pubs) |
| Exécutions suivantes (cache OpenAlex) | ~2–3 min |
| Labo avec > 500 publications | 15–40 min (1ère exécution) |

> Le cache OpenAlex est stocké dans `OPENALEX_ANALYSIS_CACHE_PATH`.
> Une fois les données téléchargées, les exécutions suivantes sont beaucoup plus rapides.

### 5.6 Télécharger les résultats

Après complétion :
- **Download PDF** — rapport principal
- **Download Biblio PDF** — bibliographie
- **Download ZIP** — projet complet (figures SVG + HTML + données)

### 5.7 Éditer le rapport (facultatif)

Cliquer **Edit Report** pour accéder à l'éditeur Markdown :
- Chaque section affiche la figure correspondante
- Les analyses textuelles sont sauvegardées automatiquement
- Cliquer **Export PDF & HTML** pour régénérer les PDFs avec les analyses

---

## 6. Bugs corrigés lors de la mise en place

Les bugs suivants ont été identifiés et corrigés pour faire fonctionner l'application
en développement local sous Windows :

### Bug 1 — Chemins Linux dans `.env` (erreur au démarrage)

**Symptôme** : `sqlite3.OperationalError: unable to open database file`

**Cause** : `USERS_DATABASE_DIRECTORY=/api_data` est un chemin absolu Linux invalide sous Windows.

**Correction** :
```dotenv
# Avant
USERS_DATABASE_DIRECTORY=/api_data
OPENALEX_ANALYSIS_CACHE_PATH=/tmp/openalex-analysis-cache

# Après
USERS_DATABASE_DIRECTORY=./api_data
OPENALEX_ANALYSIS_CACHE_PATH=C:/Users/<username>/AppData/Local/Temp/openalex-analysis-cache
```

### Bug 2 — Variable `latex_compilation_processes` non définie

**Symptôme** : `NameError: name 'latex_compilation_processes' is not defined`
(lors d'une annulation de compilation)

**Cause** : La variable est référencée dans `run_latex_compile_command` et
`cancel_compilation` mais jamais déclarée.

**Correction** dans `app/main.py` :
```python
# Ajouter avec data_fetching_processes
data_fetching_processes: Dict[str, subprocess.Popen] = {}
latex_compilation_processes: Dict[str, subprocess.Popen] = {}
process_lock = threading.Lock()
```

### Bug 3 — Anti-slashes Windows dans le sous-processus Python

**Symptôme** :
```
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes
in position 2-3: truncated \UXXXXXXXX escape
```

**Cause** : Le chemin du répertoire de travail (ex: `C:\Users\<username>\...`) est
injecté via f-string dans du code Python sans échappement. Python interprète `\U`
comme une séquence Unicode.

**Correction** dans `app/main.py` — utiliser `json.dumps()` pour échapper les chemins :
```python
import json as _json
_cwd = _json.dumps(os.getcwd())          # "C:\\Users\\<username>\\..."
_project_dir = _json.dumps(str(project_dir))

# Dans la f-string du sous-processus :
sys.path.insert(0, {_cwd})              # les guillemets sont inclus par json.dumps
root_path={_project_dir},
```

### Bug 4 — Version PyPI de `dibisoreporting` obsolète

**Symptôme** :
```
TypeError: Biso.__init__() got an unexpected keyword argument 'html_template_url'
AttributeError: type object 'DibisoReporting' has no attribute 'render_from_saved'
```

**Cause** : La version installée depuis PyPI (v0.8) ne contient pas le support des
templates HTML ni la méthode `render_from_saved`. La version locale dans le workspace
est plus récente.

**Correction** :
```bash
pip install -e dibisoreporting/ -e dibisoplot/
```

### Bug 5 — Kaleido 0.2.1 ne répond plus sous Windows (blocage complet)

**Symptôme** : Le sous-processus de génération de rapport se bloque indéfiniment (>30 min)
sans produire de sorties, après la phase de récupération des données.

**Cause** : `kaleido 0.2.1` (version installée par défaut via PyPI) utilise un sous-processus
Node.js pour exporter les figures Plotly en SVG. Ce mécanisme est connu pour bloquer
définitivement sur Windows.

**Correction** :
```bash
pip install "kaleido>=1.0.0"
```

Le fichier `requirements.txt` a été mis à jour pour inclure cette contrainte.

> Note : `openalex-analysis 0.15.2` déclare `kaleido<1.0` comme dépendance mais
> n'utilise kaleido que pour ses propres graphiques (non utilisés ici). Le conflit
> peut être ignoré sans impact fonctionnel.

### Bug 6 — Timeout trop court pour la récupération des données

**Symptôme** : `Process timeout - data fetching took too long` après 5 minutes.

**Cause** : Le timeout du sous-processus était codé en dur à 300 secondes (5 min),
insuffisant pour la 1ère exécution avec appels API HAL + OpenAlex + ScanR.

**Correction** dans `.env` et `app/main.py` :
```dotenv
DATA_FETCHING_TIMEOUT_SECONDS=1200
```

### Bug 7 — Dossier `.git` inclus dans le ZIP généré

**Symptôme** : Le ZIP de téléchargement contient des fichiers `.git/...` (artefacts du dépôt git
du template HTML).

**Cause** : `get_html_template_from_path()` copie le CONTENU du répertoire `HTML_TEMPLATE_PATH`
(ici `dibiso-html-templates/`) dans le répertoire de projet temporaire. Ce répertoire est un
dépôt git, donc son dossier `.git/` est aussi copié.

**Correction** dans `dibisoreporting/dibisoreporting/dibisoreporting.py` :
```python
_skip = {".git", ".hg", ".svn", "__pycache__"}
for item in os.listdir(self.html_template_path):
    if item in _skip:
        continue
    ...
```

### Limitation — PDF non disponible sous Windows (GTK manquant)

**Symptôme** : `status=partial` au lieu de `status=completed`. Pas de bouton "Download PDF".

**Cause** : WeasyPrint (conversion HTML → PDF) nécessite les bibliothèques GTK3 (`libgobject-2.0-0`,
`libpango-1.0-0`, `libcairo-2`) qui ne sont pas disponibles sur Windows par défaut.

**En développement Windows** : le statut `partial` est attendu. Les fichiers disponibles sont :
- ZIP (figures SVG + HTML rendu + données JSON)
- HTML (rapport rendu par Jinja2, téléchargeable via `/download-html`)

**En production (Docker/Linux)** : PDF généré normalement.

**Pour activer le PDF sur Windows** : installer le runtime GTK3 pour Windows :
```powershell
# Option 1 : Via Chocolatey (nécessite droits admin)
choco install gtk-runtime -y

# Option 2 : Télécharger manuellement depuis
# https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
# puis ajouter C:\Program Files\GTK3-Runtime Win64\bin\ au PATH
```

---

## 7. Architecture du flux de génération

```
Utilisateur (navigateur)
    │  POST /generate-report
    ▼
FastAPI (app/main.py)
    │  asyncio.create_task → ThreadPoolExecutor
    ▼
run_compilation()
    ├── Vérification HAL (requests)
    └── your_latex_project_generator()
            │  subprocess.Popen(python -c "...")
            ▼
        Sous-processus isolé :
            ├── openalex_analysis_config
            ├── Biso("LGI", 2024, ...)
            └── biso.generate_report()
                    ├── WorksType   → HAL API
                    ├── Journals    → HAL + BSO (ScanR)
                    ├── CollaborationMap → OpenAlex
                    ├── AnrProjects → ScanR
                    └── ... (12 visualisations)
            ▼
        Répertoire temporaire :
            ├── figures/           ← SVG Plotly
            ├── report.html        ← Jinja2 rendu
            ├── biblio.html
            ├── figures.json
            └── context.json
    ▼
render_html_to_pdf() → WeasyPrint → report.pdf + biblio.pdf
    ▼
create_zip_archive() → project.zip
    ▼
GET /download-pdf  (authentifié)
GET /download-zip  (authentifié)
```

---

## 8. Notes pour la production (Docker)

En production Docker, les chemins Linux (`/api_data`, `/tmp/...`) sont corrects.
Les variables `HTML_TEMPLATE_PATH` et `OPENALEX_ANALYSIS_CACHE_PATH` doivent
pointer vers des volumes montés. Voir `docker-compose.yml`.
