# Cloud Status API

A small API built step by step as a cloud and DevOps portfolio project.

## Stage 1: local API

This version exposes a health endpoint. In later stages, you will add tests, CI/CD, Docker, cloud infrastructure, monitoring, and a recovery runbook.

## Run it

```powershell
cd C:\Users\User\Documents\Codex\2026-07-18\create-a-scheduled-task-called-weekday\outputs\cloud-status-api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs`, then try `GET /health`.

## What you are learning

- An API endpoint: a URL that lets another program ask your service for information.
- A health check: a simple endpoint used by people, load balancers, and monitoring tools to confirm a service is working.
- UTC: a standard time zone that services use so logs stay consistent across countries.
