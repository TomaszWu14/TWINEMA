"""Lektor ElevenLabs: tekst kwestii → MP3 + wyrównanie znaków (timestamps). Do API idzie
wyłącznie tekst narracji. Biblioteka standardowa (urllib) — bez dodatkowej zależności.

Brak ELEVENLABS_API_KEY albo głosu → `TTSError` z komunikatem (funkcja wyłączona).
"""
import base64
import binascii
import json
import urllib.error
import urllib.request

from django.conf import settings

API = "https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128"
TIMEOUT_S = 60


class TTSError(Exception):
    """Błąd do pokazania użytkownikowi."""


def enabled():
    return bool(settings.ELEVENLABS_API_KEY)


def synthesize(text, voice_id, model_id, opener=urllib.request.urlopen):
    """→ (mp3 bytes, alignment dict). `opener` podmieniany w testach."""
    if not settings.ELEVENLABS_API_KEY:
        raise TTSError("Lektor wyłączony — ustaw ELEVENLABS_API_KEY w zmiennych serwera.")
    if not voice_id:
        raise TTSError("Brak głosu lektora — ustaw ELEVENLABS_VOICE_ID albo głos w prezentacji.")
    body = json.dumps({"text": text, "model_id": model_id}).encode("utf-8")
    req = urllib.request.Request(API.format(voice=urllib.request.quote(voice_id, safe="")), data=body, headers={
        "xi-api-key": settings.ELEVENLABS_API_KEY, "Content-Type": "application/json", "Accept": "application/json"})
    try:
        with opener(req, timeout=TIMEOUT_S) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        msg = {401: "Klucz ELEVENLABS_API_KEY został odrzucony.",
               404: "Nie ma takiego głosu — sprawdź ELEVENLABS_VOICE_ID.",
               422: "ElevenLabs odrzucił tekst kwestii (422).",
               429: "Limit ElevenLabs (znaki lub równoległe zapytania) — spróbuj za chwilę."}
        raise TTSError(msg.get(exc.code, f"ElevenLabs odpowiedział błędem {exc.code}.")) from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise TTSError("ElevenLabs jest chwilowo niedostępny — spróbuj ponownie.") from exc
    except json.JSONDecodeError as exc:
        raise TTSError("ElevenLabs zwrócił nieczytelną odpowiedź.") from exc
    try:
        audio = base64.b64decode(data["audio_base64"], validate=True)
    except (KeyError, TypeError, binascii.Error) as exc:
        raise TTSError("ElevenLabs nie zwrócił audio.") from exc
    alignment = data.get("alignment") or data.get("normalized_alignment") or {}
    if not audio or not alignment.get("character_end_times_seconds"):
        raise TTSError("ElevenLabs nie zwrócił znaczników czasu kwestii.")
    return audio, alignment
