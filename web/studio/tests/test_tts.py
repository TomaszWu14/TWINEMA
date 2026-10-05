"""Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)."""
import base64
import io
import json
import urllib.error

from django.test import SimpleTestCase, override_settings

from studio.tts import TTSError, enabled, synthesize

AL = {"characters": ["O", "k"], "character_start_times_seconds": [0, 0.1], "character_end_times_seconds": [0.1, 0.4]}


class FakeResp(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def opener_ok(payload, seen=None):
    def _open(req, timeout):
        if seen is not None:
            seen.append(req)
        return FakeResp(json.dumps(payload).encode())
    return _open


def opener_err(exc):
    def _open(req, timeout):
        raise exc
    return _open


@override_settings(ELEVENLABS_API_KEY="el-test")
class SynthesizeTests(SimpleTestCase):
    def test_disabled_without_key_or_voice(self):
        with override_settings(ELEVENLABS_API_KEY=""):
            self.assertFalse(enabled())
            with self.assertRaisesMessage(TTSError, "ELEVENLABS_API_KEY"):
                synthesize("Tekst.", "glos", "m", opener=opener_ok({}))
        with self.assertRaisesMessage(TTSError, "głosu"):
            synthesize("Tekst.", "", "m", opener=opener_ok({}))

    def test_ok_sends_only_text_and_returns_audio_and_alignment(self):
        seen = []
        audio, al = synthesize("Tekst kwestii.", "glos/1", "eleven_multilingual_v2", opener=opener_ok(
            {"audio_base64": base64.b64encode(b"ID3mp3").decode(), "alignment": AL}, seen))
        self.assertEqual((audio, al), (b"ID3mp3", AL))
        req = seen[0]
        self.assertIn("/text-to-speech/glos%2F1/with-timestamps", req.full_url)
        self.assertEqual(req.get_header("Xi-api-key"), "el-test")
        self.assertEqual(json.loads(req.data), {"text": "Tekst kwestii.", "model_id": "eleven_multilingual_v2"})

    def test_http_errors_become_messages(self):
        for code, msg in [(401, "odrzucony"), (404, "głosu"), (429, "Limit"), (500, "500")]:
            exc = urllib.error.HTTPError("u", code, "x", {}, None)
            with self.subTest(code=code), self.assertRaisesMessage(TTSError, msg):
                synthesize("T.", "g", "m", opener=opener_err(exc))
        with self.assertRaisesMessage(TTSError, "niedostępny"):
            synthesize("T.", "g", "m", opener=opener_err(urllib.error.URLError("dns")))

    def test_bad_payloads(self):
        for payload, msg in [({}, "nie zwrócił audio"), ({"audio_base64": "!!"}, "nie zwrócił audio"),
                             ({"audio_base64": base64.b64encode(b"x").decode()}, "znaczników")]:
            with self.subTest(payload=payload), self.assertRaisesMessage(TTSError, msg):
                synthesize("T.", "g", "m", opener=opener_ok(payload))
