"""Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT."""
from unittest import TestCase

from studio.voice import LINE_CHARS, build_srt, cues, duration, offsets, srt_time, voice_key, words


def align(text, per_char=0.05, start=0.0):
    """Sztuczne wyrównanie: każdy znak trwa per_char sekund."""
    n = len(text)
    return {"characters": list(text),
            "character_start_times_seconds": [round(start + i * per_char, 3) for i in range(n)],
            "character_end_times_seconds": [round(start + (i + 1) * per_char, 3) for i in range(n)]}


class VoiceKeyTests(TestCase):
    def test_same_input_same_key_any_change_new_key(self):
        k = voice_key("Hala z góry.", "glos1", "m1")
        self.assertEqual(k, voice_key("  Hala z góry. ", "glos1", "m1"))
        self.assertNotEqual(k, voice_key("Hala z góry!", "glos1", "m1"))
        self.assertNotEqual(k, voice_key("Hala z góry.", "glos2", "m1"))
        self.assertNotEqual(k, voice_key("Hala z góry.", "glos1", "m2"))


class AlignmentTests(TestCase):
    def test_duration_and_words(self):
        al = align("Ala  ma kota.")
        self.assertEqual(duration(al), 0.65)
        self.assertEqual(duration({}), 0.0)
        self.assertEqual([w for w, _, _ in words(al)], ["Ala", "ma", "kota."])
        self.assertEqual(words(al)[1][1:], (0.25, 0.35))


class CueTests(TestCase):
    def test_lines_never_exceed_limits(self):
        text = ("Hala ma dwa tysiące trzysta miejsc paletowych na czterech poziomach regałów. "
                "Średnia droga do miejsca to czterdzieści metrów, a do strefy A dwadzieścia. "
                "Cztery roboty obsługują kompletację.")
        cs = cues(words(align(text)))
        self.assertGreater(len(cs), 2)
        for start, end, t in cs:
            lines = t.split("\n")
            self.assertLessEqual(len(lines), 2)
            self.assertTrue(all(len(x) <= LINE_CHARS for x in lines))
            self.assertLessEqual(end - start, 6.0 + 1.0)
        self.assertEqual(" ".join(t.replace("\n", " ") for _, _, t in cs), text)   # nic nie zginęło
        self.assertEqual([c[0] for c in cs], sorted(c[0] for c in cs))

    def test_short_text_single_cue(self):
        self.assertEqual(cues(words(align("Krótko."))), [(0.0, 0.35, "Krótko.")])
        self.assertEqual(cues([]), [])


class SrtTests(TestCase):
    def test_time_format(self):
        self.assertEqual(srt_time(0), "00:00:00,000")
        self.assertEqual(srt_time(3725.4567), "01:02:05,457")

    def test_build_with_offsets(self):
        srt = build_srt([(0, [(0.0, 1.5, "Pierwsza.")]), (10.0, [(0.2, 2.0, "Druga\nlinia.")])])
        self.assertEqual(srt, "1\n00:00:00,000 --> 00:00:01,500\nPierwsza.\n\n"
                              "2\n00:00:10,200 --> 00:00:12,000\nDruga\nlinia.\n")

    def test_offsets(self):
        self.assertEqual(offsets([2.0, 3.5, 1.0]), [0.0, 2.0, 5.5])
        self.assertEqual(offsets([2.0, 3.0], gap_s=0.5, start_s=4.0), [4.0, 6.5])
