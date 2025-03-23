# tests/test_search.py
import unittest
from src.sequence_search import search_sequence
from src.utils import load_pi_decimals

class TestSequenceSearch(unittest.TestCase):
    def setUp(self):
        """
        Set up the test by loading π's decimals before each test case.
        """
        self.pi_decimals = load_pi_decimals()

    def test_known_sequence(self):
        """
        Test searching for a known sequence (the first few decimals of π).
        The first decimals of π are 314159..., so searching for "314159" should return position 0.
        """
        position = search_sequence("314159", self.pi_decimals)
        self.assertEqual(position, 0)

    def test_non_existent_sequence(self):
        """
        Test searching for a sequence that is unlikely to exist (e.g., a long sequence of 9s).
        """
        position = search_sequence("999999999", self.pi_decimals)
        self.assertIsNone(position)

if __name__ == "__main__":
    unittest.main()
