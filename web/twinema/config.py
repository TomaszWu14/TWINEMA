"""Typowana, walidowana konfiguracja z env (pydantic-settings).

`AppEnv()` jest tworzone RAZ na górze `settings.py`: brakująca albo zła zmienna wywala
start aplikacji z jednym zbiorczym komunikatem, a nie w środku żądania.
"""
from __future__ import annotations

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

DEV_SECRET = "dev-only-change-me"


class AppEnv(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, extra="ignore")

    # ── Django ──────────────────────────────────────────────────────────────
    DJANGO_SECRET_KEY: str = DEV_SECRET
    DJANGO_DEBUG: bool = False
    DJANGO_ALLOWED_HOSTS: str = "127.0.0.1,localhost"
    DJANGO_CSRF_TRUSTED_ORIGINS: str = "http://localhost"
    DJANGO_SSL_REDIRECT: bool = False
    DJANGO_LOG_LEVEL: str = "INFO"
    APP_NAME: str = "TWINEMA"

    # ── Baza / pliki ────────────────────────────────────────────────────────
    DATABASE_URL: str = ""          # puste = SQLite (dev/CI bez Postgresa)
    DB_PATH: str = ""
    DB_SSLMODE: str = ""
    DB_CONN_MAX_AGE: int = 600
    MEDIA_ROOT: str = ""

    # ── Sesja / bezpieczeństwo ──────────────────────────────────────────────
    SESSION_COOKIE_AGE: int = 28800
    CSP_REPORT_ONLY: bool = True

    # ── Render (worker Blendera poza serwerem, pobiera zlecenia po HTTPS) ────
    RENDER_WORKER_TOKEN: str = ""      # puste = API workera wyłączone (403)
    RENDER_MAX_MB: int = 500           # limit pliku wyniku (PNG/MP4)
    RENDER_STALE_MIN: int = 120        # zlecenie „w toku” dłużej niż tyle minut wraca do kolejki

    # ── Studio prezentacji (na zewnątrz idzie wyłącznie tekst narracji) ─────
    ANTHROPIC_API_KEY: str = ""        # puste = szkic scenariusza z Claude wyłączony
    CLAUDE_MODEL: str = "claude-opus-5"

    # ── Obserwowalność ──────────────────────────────────────────────────────
    SENTRY_DSN: str = ""
    SENTRY_ENVIRONMENT: str = "production"

    @model_validator(mode="after")
    def _cross_field_checks(self) -> "AppEnv":
        if not self.DJANGO_DEBUG and self.DJANGO_SECRET_KEY == DEV_SECRET:
            raise ValueError("DJANGO_SECRET_KEY musi być ustawiony, gdy DJANGO_DEBUG=false.")
        if self.RENDER_WORKER_TOKEN and len(self.RENDER_WORKER_TOKEN) < 32:
            raise ValueError("RENDER_WORKER_TOKEN musi mieć co najmniej 32 znaki (np. secrets.token_urlsafe(32)).")
        return self


def load_env() -> AppEnv:
    """Zwraca zwalidowany env; błąd → ImproperlyConfigured (czysty komunikat na starcie)."""
    try:
        return AppEnv()
    except Exception as exc:
        from django.core.exceptions import ImproperlyConfigured
        raise ImproperlyConfigured(f"Błąd konfiguracji środowiska:\n{exc}") from exc
