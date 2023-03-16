import unittest
from lyrics import sing, first_verse, second_verse

class LyricsTest(unittest.TestCase):
    def test_sing(self):
        self.assertEquals(sing(), [
            "Quand je me retrouve dans des moments difficiles, Mère Marie vient à moi",
            "Prononçant des paroles de sagesse, laisse être",
            "Et dans mon heure sombre elle se tient juste devant moi",
            "Prononçant des paroles de sagesse, laisse être.",
            ])

    def test_first_verse(self):
        self.assertEquals(first_verse(), [
            "Lorsque je me retrouve dans des moments difficiles, Mère Marie vient à moi",
            "Prononçant des paroles de sagesse, laisse les être",
            "Et dans mon heure de ténèbres, elle se tient juste devant moi",
            "Prononçant des paroles de sagesse, laisse les être.",
        ])

    def test_second_verse(self):
        self.assertEquals(second_verse(), [
            "Laissez-le être, laissez-le être, laissez-le être, laissez-le être,"
            "Chuchotez des paroles de sagesse, laissez-le être.",
        ])
    