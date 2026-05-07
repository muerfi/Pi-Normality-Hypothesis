"""Compatibility wrappers for the original ``src.utils`` module."""

from pi_lab.digits import load_pi_digits


def load_pi_decimals():
    """Load the default finite prefix of pi digits."""
    return load_pi_digits()
