import unittest

from pi_lab.digits import load_pi_digits
from pi_lab.search import search_sequence


class TestSequenceSearch(unittest.TestCase):
    def setUp(self):
        """Load the finite pi digit prefix before each test case."""
        self.pi_digits = load_pi_digits()

    def test_known_sequence(self):
        """The checked-in prefix starts with 314159."""
        position = search_sequence("314159", self.pi_digits)
        self.assertEqual(position, 0)

    def test_non_existent_sequence(self):
        """A long sequence of 9s is absent from the small checked-in prefix."""
        position = search_sequence("999999999", self.pi_digits)
        self.assertIsNone(position)


if __name__ == "__main__":
    unittest.main()
