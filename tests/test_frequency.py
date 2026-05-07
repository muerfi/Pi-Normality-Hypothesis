import unittest

from pi_lab.statistics import block_frequencies, digit_frequencies


class TestFrequencySummaries(unittest.TestCase):
    def test_digit_frequencies_include_zero_counts(self):
        counts = digit_frequencies("314159")
        self.assertEqual(counts["1"], 2)
        self.assertEqual(counts["0"], 0)
        self.assertEqual(set(counts.keys()), set("0123456789"))

    def test_overlapping_block_frequencies(self):
        counts = block_frequencies("314159", block_size=2)
        self.assertEqual(counts["31"], 1)
        self.assertEqual(counts["15"], 1)
        self.assertNotIn("99", counts)


if __name__ == "__main__":
    unittest.main()
