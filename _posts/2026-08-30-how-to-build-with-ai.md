---
layout: post
title: "How to Build with AI: From Idea to Production in 28 Prompts"
date: 2026-08-30
categories: [AI, Software Engineering]
---

Notes from Alexey Grigorev's post ["From Idea to Production in 28 Prompts"](https://aishippingblog.com/p/from-idea-to-production). It lays out a framework of 28 prompts you can feed to an AI coding agent, step by step, to take an app from idea to a running, monitored production system.

## Stage 1: Build

1. **Specification** — Discuss the idea with the assistant, then have it summarize the scope into `_docs/specs.md`.
2. **Frontend** — Build the UI with a mocked backend. Centralize all backend calls in one services layer.
3. **Manual test** — Write down a sequence of user actions that validates the core flow. Save it under `_docs`.
4. **AGENTS.md** — Add a rule: make focused commits and explain decisions in the commit messages so they double as logs.
5. **OpenAPI schema** — Read the frontend's API client and generate `openapi.yaml` defining every endpoint.
6. **Choose backend stack** — Ask for 2-3 stack options based on the schema, with pros/cons and a recommendation. Save to `_docs/stack.md`.
7. **Backend** — Implement the backend per the OpenAPI spec, using an in-memory store, hashed passwords, bearer tokens, and tests.
8. **Makefile** — Add one so the app is easy to run.
9. **Connect frontend and backend** — Switch the frontend to the real backend client and test with the manual scenario.
10. **Database** — Replace the in-memory store with SQLite via an ORM, so switching databases later is easy.

## Stage 2: Deploy

11. **Containerization** — Dockerfile that builds frontend (Node) then backend, with the backend serving the frontend.
12. **Production database** — Add Postgres support and verify with the test scenario.
13. **Docker Compose** — Two services: database and app. Run with `docker compose up`.
14. **Integration tests** — Tests that run against the Compose stack, checking backend-database correctness.
15. **End-to-end test** — Playwright tests against the Compose stack, placed in `e2e/`.
16. **Deployment stack** — Ask for 2-3 deployment options, compared on cost and complexity, plus infrastructure-as-code options.
17. **Deployment** — Deploy using the chosen option and IaC tool.
18. **CI/CD pipeline** — Run frontend/backend tests in parallel, build and test the Compose stack, deploy, then verify via a health check.

## Stage 3: Operate

19. **Second environment** — Duplicate the infrastructure: one copy becomes production, the original stays as dev.
20. **Manual promotion workflow** — A GitHub Actions workflow to promote dev to production.
21. **Split build/deploy** — Separate into a Build stage (image → registry) and a Deploy stage (pull → serve). Tag images as `YYYYMMDD-HHMMSS-shortsha`.
22. **Observability with OpenTelemetry** — Instrument the backend with service name, environment, and deployed version.
23. **Choose observability backend** — Ask for 2-3 options for storing metrics/logs/traces and displaying them.
24. **OTel Collector stack** — Add an `observability/` directory with Compose config, deployed separately and shared across dev/prod.
25. **Application metrics** — Ask for the top 5 product metrics, then track them with OTel.
26. **Dashboards** — Display the exported metrics, filterable by environment and deployed version.
27. **Alerts** — Actionable alerts including service, environment, version, owner, and dashboard URL.
28. **On-call worker** — A script that listens for alerts and wakes an on-call agent (running headless) to resolve issues and commit fixes autonomously.

## Takeaway

Each step is just a prompt for a coding assistant — the tools, languages, and cloud platform are up to you. The value is in the sequence: go from spec to UI to backend to database, then containerize, deploy, and automate, and finally close the loop with observability and self-healing alerts.
