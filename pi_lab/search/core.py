"""Core search routines for finite pi digit prefixes."""


def validate_digit_sequence(sequence: str) -> str:
    """Return a normalized digit sequence or raise ``ValueError``."""
    normalized = sequence.strip()
    if not normalized:
        raise ValueError("sequence must not be empty")
    if not normalized.isdigit():
        raise ValueError("sequence must contain digits only")
    return normalized


def search_sequence(sequence: str, pi_digits: str) -> int | None:
    """Return the zero-based first position of ``sequence`` in ``pi_digits``.

    ``None`` is returned when the sequence is absent from the finite prefix.
    Absence from a finite prefix is not evidence that the sequence never occurs
    in pi.
    """
    query = validate_digit_sequence(sequence)
    position = pi_digits.find(query)
    return None if position == -1 else position
