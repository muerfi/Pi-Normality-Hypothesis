"""Compatibility wrapper for pi digit generation.

Prefer ``python -m pi_lab generate`` in new code.
"""

from pi_lab.digits import generate_pi_digits


def generate_pi_decimals(num_decimals=1_000_000):
    """Generate a finite prefix of pi digits using the original function name."""
    return generate_pi_digits(num_decimals)


if __name__ == "__main__":
    generate_pi_decimals(1_000_000)
