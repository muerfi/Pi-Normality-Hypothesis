"""Frequency summaries for finite digit strings."""

from collections import Counter


def block_frequencies(pi_digits: str, block_size: int = 1) -> dict[str, int]:
    """Count overlapping blocks of length ``block_size`` in ``pi_digits``.

    For ``block_size=1`` the returned dictionary includes all ten decimal
    digits, even if some counts are zero. For larger block sizes, only observed
    blocks are returned to avoid creating very large sparse dictionaries.
    """
    if block_size < 1:
        raise ValueError("block_size must be at least 1")
    if not pi_digits:
        return {str(i): 0 for i in range(10)} if block_size == 1 else {}
    if len(pi_digits) < block_size:
        return {str(i): 0 for i in range(10)} if block_size == 1 else {}

    counts = Counter(
        pi_digits[index : index + block_size]
        for index in range(0, len(pi_digits) - block_size + 1)
    )
    if block_size == 1:
        return {str(digit): counts.get(str(digit), 0) for digit in range(10)}
    return dict(sorted(counts.items()))


def digit_frequencies(pi_digits: str) -> dict[str, int]:
    """Count individual decimal digits in ``pi_digits``."""
    return block_frequencies(pi_digits, block_size=1)
