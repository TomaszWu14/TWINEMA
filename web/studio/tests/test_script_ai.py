"""Klient Claude: brak klucza, mapowanie błędów, odmowa, poprawny szkic. Zawsze mock — bez sieci."""
from types import SimpleNamespace
from unittest import mock

import anthropic
import httpx2
from django.test import SimpleTestCase, override_settings

from studio import script_ai
from studio.script_ai import ScriptAIError, ScriptDraft, ShotDraft, draft_script

FACTS = ["Miejsca paletowe: 2 304."]


def _client(resp=None, exc=None):
    c = mock.Mock()
    c.messages.parse.side_effect = exc
    c.messages.parse.return_value = resp
    return c


def _resp(shots, stop="end_turn"):
    return SimpleNamespace(stop_reason=stop, parsed_output=ScriptDraft(shots=shots) if shots is not None else None)


@override_settings(ANTHROPIC_API_KEY="sk-test", CLAUDE_MODEL="claude-opus-5")
class DraftScriptTests(SimpleTestCase):
    def test_disabled_without_key(self):
        with override_settings(ANTHROPIC_API_KEY=""):
            self.assertFalse(script_ai.enabled())
            with self.assertRaisesMessage(ScriptAIError, "ANTHROPIC_API_KEY"):
                draft_script(FACTS, client=_client())

    def test_no_facts_no_call(self):
        c = _client()
        with self.assertRaises(ScriptAIError):
            draft_script([], client=c)
        c.messages.parse.assert_not_called()

    def test_ok_sends_only_facts_and_returns_clean_shots(self):
        c = _client(_resp([ShotDraft(preset="przelot", text=" Hala. "), ShotDraft(preset="plan", text="Plan.")]))
        shots, warnings = draft_script(FACTS, client=c)
        self.assertEqual(shots, [{"preset": "przelot", "text": "Hala."}, {"preset": "plan", "text": "Plan."}])
        self.assertEqual(warnings, [])
        kw = c.messages.parse.call_args.kwargs
        self.assertEqual(kw["model"], "claude-opus-5")
        self.assertIs(kw["output_format"], ScriptDraft)
        self.assertIn("Miejsca paletowe: 2 304.", kw["messages"][0]["content"])

    def test_refusal_and_truncation(self):
        with self.assertRaisesMessage(ScriptAIError, "odmówił"):
            draft_script(FACTS, client=_client(_resp(None, stop="refusal")))
        with self.assertRaisesMessage(ScriptAIError, "niekompletny"):
            draft_script(FACTS, client=_client(_resp(None, stop="max_tokens")))

    def test_api_errors_become_readable_messages(self):
        req = httpx2.Request("POST", "https://api.anthropic.com/v1/messages")
        cases = [
            (anthropic.AuthenticationError("x", response=httpx2.Response(401, request=req), body=None), "odrzucony"),
            (anthropic.RateLimitError("x", response=httpx2.Response(429, request=req), body=None), "Limit"),
            (anthropic.APITimeoutError(request=req), "na czas"),
            (anthropic.APIConnectionError(request=req), "niedostępna"),
        ]
        for exc, msg in cases:
            with self.subTest(exc=type(exc).__name__), self.assertRaisesMessage(ScriptAIError, msg):
                draft_script(FACTS, client=_client(exc=exc))
