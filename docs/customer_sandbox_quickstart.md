# ⚡ Customer Sandbox Quickstart

## Purpose

This sandbox lets a customer submit an example AI dependency and receive a board-facing boundary decision with a receipt.

---

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Run Sandbox

```bash
python app/sandbox_app.py
```

Open:

```text
http://127.0.0.1:5000/
```

---

## Submit Demo Review

```bash
curl -X POST http://127.0.0.1:5000/sandbox/review \
  -H "Content-Type: application/json" \
  -d '{
    "name": "AI Claims Routing Assistant",
    "criticality": "critical",
    "consequence_classes": ["regulated", "customer"],
    "persistent_memory": true,
    "autonomous_execution": true,
    "cross_border_exposure": true,
    "authority_clear": false,
    "receipt_available": false,
    "replay_available": false,
    "exit_path_available": false,
    "conditions_changed": false,
    "existing_deployment": true
  }'
```

---

## Expected Result

The sandbox returns:

- classification
- recommended outcome
- reason
- decision receipt
- revalidation triggers
- buyer rules

---

## Buyer Rules

**No receipt, no board assurance.**  
**No replay, no dependency confidence.**  
**No proof surface, no category claim.**
