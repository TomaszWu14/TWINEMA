# CLAUDE.md — TWINEMA

Aplikacja do projektowania magazynów 3D, symulacji przepływów i prezentacji (Blender +
ElevenLabs). Plan i decyzje: `docs/PLAN.md`. Pochodzenie kodu: `PROVENANCE.md`.

## Zasady
- **UI i teksty po polsku.** Marka przez `{{ app_name }}` (env `APP_NAME`).
- **Bez nazw firm, klientów i lokalizacji** w kodzie, danych demo i dokumentach — scenariusz
  referencyjny jest anonimowy. Dane demo = syntetyczne.
- **Konfiguracja tylko przez `web/twinema/config.py`** (pydantic, fail-fast). Nowa zmienna =
  pole tam + wpis w `.env.example`, jeśli krytyczna dla wdrożenia.
- **Grupy ról w `core/roles.py` to zamrożony kontrakt** (wiersze `auth_group`); pilnuje
  `core/tests/test_foundation.py`.
- Logika obliczeniowa (symulacja, ML, geometria) = **czysty Python bez Django**, testowalny bez bazy.
- Wszystko synchroniczne (WSGI). Długie prace (TTS, montaż) → kolejka (F3), rendery → zewnętrzny worker.
- Front: bez CDN w runtime — biblioteki JS vendorowane.

## Testy (przed każdym PR)
```bash
cd web
export DJANGO_DEBUG=true DJANGO_ALLOWED_HOSTS='*'
python manage.py check && python manage.py test
ruff check ..
```

## Git
Gałąź `claude/<nazwa>` → PR na `main` → CI (`test`) → auto-merge → `deploy.yml` (Coolify + smoke).
Jedna zmiana = jeden PR. PR od razu gotowy (nie draft).
