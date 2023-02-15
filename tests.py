import unittest
from lyrics import sing

class LyricsTest(unittest.TestCase):
    def test_sing(self):
        self.assertEquals(sing(), ["When I find myself in times of trouble, Mother Mary comes to me"])
    