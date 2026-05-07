"""Compatibility wrapper for digit-frequency analysis.

Prefer ``python -m pi_lab frequency --block-size 1`` in new code.
"""

from pi_lab.digits import load_pi_digits
from pi_lab.statistics import digit_frequencies
from pi_lab.visualization import plot_digit_frequencies


def analyze_frequency(pi_decimals):
    """Return single-digit counts and generate the default histogram."""
    counts = digit_frequencies(pi_decimals)
    output = plot_digit_frequencies(pi_decimals)
    print(f"Histogram saved to {output}")
    return counts


if __name__ == "__main__":
    analyze_frequency(load_pi_digits())
