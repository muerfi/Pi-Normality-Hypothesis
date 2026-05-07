import pytest

from pi_lab.search import search_sequence, validate_digit_sequence


PI_PREFIX = "314159265358979323846264338327950288419716939937510"


def test_search_sequence_finds_first_zero_based_position():
    assert search_sequence("314159", PI_PREFIX) == 0
    assert search_sequence("9265", PI_PREFIX) == 5
    assert search_sequence("26", PI_PREFIX) == 6


def test_search_sequence_returns_none_when_absent_from_finite_prefix():
    assert search_sequence("000000", PI_PREFIX) is None


def test_search_sequence_returns_first_occurrence_for_repeated_sequence():
    digits = "0012300123"

    assert search_sequence("00123", digits) == 0
    assert search_sequence("123", digits) == 2


def test_validate_digit_sequence_strips_surrounding_whitespace():
    assert validate_digit_sequence("  271828  ") == "271828"


@pytest.mark.parametrize("sequence", ["", "   ", "31.4", "abc", "12 34"])
def test_validate_digit_sequence_rejects_invalid_queries(sequence):
    with pytest.raises(ValueError):
        validate_digit_sequence(sequence)
