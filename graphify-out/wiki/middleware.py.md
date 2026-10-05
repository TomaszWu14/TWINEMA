# middleware.py

> 15 nodes · cohesion 0.13

## Key Concepts

- **middleware.py** (5 connections) — `web/core/middleware.py`
- **RequestIDMiddleware** (4 connections) — `web/core/middleware.py`
- **SecurityHeadersMiddleware** (4 connections) — `web/core/middleware.py`
- **RequestIDLogFilter** (3 connections) — `web/core/middleware.py`
- **client_ip()** (2 connections) — `web/core/middleware.py`
- **Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…** (1 connections) — `web/core/middleware.py`
- **Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem).** (1 connections) — `web/core/middleware.py`
- **Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi.** (1 connections) — `web/core/middleware.py`
- **Permissions-Policy + Content-Security-Policy (domyślnie report-only).** (1 connections) — `web/core/middleware.py`
- **IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…** (1 connections) — `web/core/middleware.py`
- **.filter()** (1 connections) — `web/core/middleware.py`
- **.__call__()** (1 connections) — `web/core/middleware.py`
- **.__init__()** (1 connections) — `web/core/middleware.py`
- **.__call__()** (1 connections) — `web/core/middleware.py`
- **.__init__()** (1 connections) — `web/core/middleware.py`

## Relationships

- No strong cross-community connections detected

## Source Files

- `web/core/middleware.py`

## Audit Trail

- EXTRACTED: 28 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*