"""Frequency summaries for finite digit strings."""

from collections import Counter


def _validate_digit_string(pi_digits: str) -> None:
    """Raise ``ValueError`` when ``pi_digits`` is not a decimal digit string."""
    if pi_digits and not pi_digits.isdigit():
        raise ValueError("pi_digits must contain digits only")


def extract_blocks(pi_digits: str, block_size: int = 1) -> list[str]:
    """Return overlapping blocks of length ``block_size`` from ``pi_digits``.

    The extraction is deterministic and left-to-right. For example,
    ``extract_blocks("314159", 2)`` returns ``["31", "14", "41", "15", "59"]``.
    """
    if block_size < 1:
        raise ValueError("block_size must be at least 1")
    _validate_digit_string(pi_digits)
    if len(pi_digits) < block_size:
        return []
    return [
        pi_digits[index : index + block_size]
        for index in range(0, len(pi_digits) - block_size + 1)
    ]


def block_frequencies(pi_digits: str, block_size: int = 1) -> dict[str, int]:
    """Count overlapping blocks of length ``block_size`` in ``pi_digits``.

    For ``block_size=1`` the returned dictionary includes all ten decimal
    digits, even if some counts are zero. For larger block sizes, only observed
    blocks are returned to avoid creating very large sparse dictionaries.
    """
    blocks = extract_blocks(pi_digits, block_size=block_size)
    if not blocks:
        return {str(i): 0 for i in range(10)} if block_size == 1 else {}

    counts = Counter(blocks)
    if block_size == 1:
        return {str(digit): counts.get(str(digit), 0) for digit in range(10)}
    return dict(sorted(counts.items()))


def digit_frequencies(pi_digits: str) -> dict[str, int]:
    """Count individual decimal digits in ``pi_digits``."""
    return block_frequencies(pi_digits, block_size=1)
