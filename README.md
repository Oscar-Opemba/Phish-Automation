# Phish-Automation — Ethical Phishing Simulation Platform

This project is **strictly for defensive security**: security awareness training, red-team simulations with written authorization, and detection testing. It does **not** send real phishing emails, harvest credentials, or bypass protections. All offensive actions are simulated or stubbed.

## Purpose
Organizations need a safe way to rehearse how phishing *would* look without harming users. This platform models campaign lifecycles, metrics, and blue-team telemetry while keeping execution inert.

## Scope & Guardrails
- No real email delivery (uses mock transports).
- No credential collection (uses synthetic events).
- Explicit authorization banner and audit logging.
- Default-deny: any outbound action is a no-op unless a mock backend is enabled.

## Repository Layout
```
Phish-Automation/
├─ docs/
│  ├─ README.md
│  ├─ architecture.md
│  ├─ threat-model.md
│  └─ ethics-and-authorization.md
├─ src/
│  ├─ app/
│  │  ├─ __init__.py
│  │  ├─ config.py
│  │  ├─ models.py
│  │  ├─ campaign.py
│  │  ├─ simulator.py
│  │  └─ metrics.py
│  ├─ api/
│  │  ├─ __init__.py
│  │  └─ routes.py
│  └─ cli.py
└─ README.md
```

---

## Top-Level README

### What This Is
A **simulation framework** for planning, validating, and measuring phishing *defense* readiness.

### What This Is Not
A live phishing toolkit. Anything resembling delivery, credential capture, or evasion is intentionally mocked.

### Quick Start
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # optional; stubs run without deps
python src/cli.py demo
```

---

## docs/README.md
Explains how to run tabletop exercises and purple-team simulations using synthetic events.

## docs/architecture.md
Describes components:
- **Campaign Planner**: defines scenarios (themes, targets as roles, timing windows).
- **Simulator**: generates synthetic opens/clicks without contacting users.
- **Metrics Engine**: calculates resilience scores.
- **API**: read-only endpoints for dashboards.

## docs/threat-model.md
STRIDE-style model focusing on *abuse prevention* of this tool itself.

## docs/ethics-and-authorization.md
Rules of engagement, consent requirements, and logging obligations.

---

## src/app/config.py (stub)
Configuration loader with safe defaults and a hard kill-switch.

## src/app/models.py (stub)
Dataclasses for Campaign, Role, Scenario, Event.

## src/app/campaign.py (stub)
Creates and validates campaigns against guardrails.

## src/app/simulator.py (stub)
Generates **synthetic** events only. No network I/O.

## src/app/metrics.py (stub)
Computes click-through *risk* and reporting *health* from synthetic data.

## src/api/routes.py (stub)
Read-only endpoints for metrics export.

## src/cli.py (stub)
CLI for demo runs and report export.

---

## Roadmap
- Role-based difficulty curves
- Detection signal mapping (SIEM-friendly)
- Report templates for CISSP/ISO audiences

## License
Defensive use only. Requires written authorization for any simulation involving real users.

