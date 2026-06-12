# 🚀 Deployment Guide

## Purpose

This repository includes a bounded customer sandbox for the **Board AI Dependency Boundary Review**.

The deployment surface is intentionally limited. It exposes the customer-facing proof surface only and does not expose the protected Elyria Systems substrate, kernel, private research corpus, unpublished mathematical derivations, or proprietary enforcement architecture.

---

## Deployment Modes

| Mode | Use |
|---|---|
| **Local Sandbox** | Quick customer demo on a laptop |
| **Docker Sandbox** | Reproducible container demo |
| **Cloud Sandbox** | Public or private hosted pilot environment |

---

## 1. Local Sandbox

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app/sandbox_app.py
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app/sandbox_app.py
```

Open:

```text
http://127.0.0.1:5000/
```

---

## 2. Docker Sandbox

```bash
docker build -t elyria-board-ai-boundary-sandbox .
docker run -p 5000:5000 elyria-board-ai-boundary-sandbox
```

Open:

```text
http://127.0.0.1:5000/
```

---

## 3. Docker Compose

```bash
docker compose up --build
```

Open:

```text
http://127.0.0.1:5000/
```

---

## 4. Sandbox Review Endpoint

```text
POST /sandbox/review
```

Example request:

```bash
curl -X POST http://127.0.0.1:5000/sandbox/review \
  -H "Content-Type: application/json" \
  -d @examples/customer_sandbox_payload.json
```

Expected response:

- dependency decision
- classification
- reason
- receipt
- revalidation triggers
- buyer rules

---

## Deployment Boundary

This deployment is **not open source** and does not grant production rights.

It is public-viewable for evaluation, pilot review, and commercial discussion only.

The customer sandbox is safe to demo because it exposes:

- intake surface
- classification surface
- receipt surface
- revalidation trigger surface

It does not expose:

- protected substrate
- kernel internals
- private research corpus
- unpublished math
- internal enforcement logic
- real customer data
- production secrets

---

## Buyer Rules

**No receipt, no board assurance.**  
**No replay, no dependency confidence.**  
**No proof surface, no category claim.**
