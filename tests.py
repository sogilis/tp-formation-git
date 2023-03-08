import unittest
from lyrics import first_verse, second_verse

class LyricsTest(unittest.TestCase):
    def test_first_verse(self):
        self.assertEquals(first_verse(), [
            "When I find myself in times of trouble, Mother Mary comes to me",
            "Speaking words of wisdom, let it be",
            "And in my hour of darkness she is standing right in front of me",
            "Speaking words of wisdom, let it be",
        ])

    def test_second_verse(self):
        self.assertEquals(second_verse(), [
            "Let it be, let it be, let it be, let it be",
            "Whisper words of wisdom, let it be",
        ])
    