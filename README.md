# Personal Flask Website — Render Ready

A modern responsive personal website built with Python + Flask.

## Run locally

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Run:
```bash
python app.py
```

Open:
http://127.0.0.1:5000

## Deploy to Render

1. Upload/push this project to GitHub.
2. In Render, create a **New Web Service**.
3. Select the GitHub repository.
4. Build Command:
   `pip install -r requirements.txt`
5. Start Command:
   `gunicorn app:app`
6. Deploy.

The included `render.yaml` can also be used with Render Blueprint deployment.

## Customize

Edit `templates/index.html` to change your name, biography, projects, email, and social links.

Keep this structure:

templates/index.html
static/css/style.css
static/js/script.js
app.py
requirements.txt
render.yaml
