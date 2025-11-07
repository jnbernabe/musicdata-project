# Music Insights

Music Insights is a small Django application that turns the CSV download you get from [Exportify](https://exportify.net/) into useful stats and curation prompts. Upload any exported Spotify playlist and the site ingests track, album, artist, and playlist metadata, then renders a lightweight dashboard with summaries, charts, and plain‑language recommendations about your listening habits.

## Features
- **Upload & parsing** – drop in an Exportify CSV and the `exportify_parser` service normalizes tracks, albums, artists, and playlist entries in SQLite.
- **Snapshot dashboards** – see total track counts plus ranked tables for artists, songs, and playlists along with a Chart.js line graph of additions per month.
- **Personalized nudges** – the recommendation service scans listening streaks (top artists, time of day, biggest playlists) and surfaces actionable suggestions.
- **File history** – every upload is stored so new files can be processed without touching older data.
- **Extensible services** – parsing, stats, and recommendations live in `musicinsights/services/`, making it easy to plug in new heuristics or support JSON inputs later.

## Tech Stack
- Python 3.11+ and Django 5.2.8
- SQLite for local persistence (configurable via `DATABASES` in `musicdata/settings.py`)
- Chart.js over CDN for the dashboard visualization

## Getting Started
1. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
2. **Install dependencies**  
   The project currently uses core Django only:
   ```bash
   pip install "Django>=5.2,<6.0"
   ```
3. **Apply migrations & run the dev server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```
4. Open http://127.0.0.1:8000/ in your browser.

## Usage
1. Export a playlist from Exportify (CSV format).  
2. Visit the upload page (`/`) and submit the CSV file.  
3. You are redirected to `/dashboard/<upload_id>/`, which shows:
   - Total tracks processed
   - Top artists, tracks, and playlists tables
   - Monthly track additions chart
   - Context-aware recommendations list

You can repeat the upload workflow for as many playlists as you like; each file is stored as an `Upload` record so nothing is overwritten.

## Project Layout
```
musicdata-project/
├── manage.py                # Django entry point
├── musicdata/               # Project settings & URL routing
├── musicinsights/           # Core app (models, views, services)
│   ├── models.py            # Upload, Artist, Album, Track, PlaylistEntry
│   ├── services/
│   │   ├── exportify_parser.py
│   │   ├── stats_service.py
│   │   └── recommendation_service.py
│   └── views.py             # Upload form + dashboard views
├── templates/
│   ├── base.html
│   └── musicinsights/
│       ├── upload.html
│       └── dashboard.html
└── media/                   # Stored uploads (via `Upload.original_file`)
```

## Extending the App
- Add new recommendation heuristics in `musicinsights/services/recommendation_service.py`.
- Support additional Exportify fields or alternate formats in `exportify_parser.py`.
- Enhance the dashboard by passing more data through `stats_service.build_dashboard_context`.
- Swap SQLite for Postgres by editing `DATABASES` in `musicdata/settings.py` and updating environment variables.

## Troubleshooting
- If a CSV fails to upload, confirm it ends with `.csv` and matches Exportify’s header names (`Track URI`, `Track Name`, etc.).
- The chart requires JavaScript; make sure the CDN is reachable from your environment.
- When editing locally, restart `runserver` after adding new dependencies or changing settings.

Happy playlist digging!
