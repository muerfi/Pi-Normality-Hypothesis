import pytest

from pi_lab.statistics import block_frequencies, digit_frequencies, extract_blocks


def test_digit_frequencies_count_digits_and_include_zero_counts():
    counts = digit_frequencies("314159")

    assert counts == {
        "0": 0,
        "1": 2,
        "2": 0,
        "3": 1,
        "4": 1,
        "5": 1,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 1,
    }


def test_digit_frequencies_for_empty_input_returns_all_zero_counts():
    assert digit_frequencies("") == {str(digit): 0 for digit in range(10)}


def test_extract_blocks_returns_overlapping_blocks_in_order():
    assert extract_blocks("314159", block_size=2) == ["31", "14", "41", "15", "59"]
    assert extract_blocks("314159", block_size=3) == ["314", "141", "415", "159"]


def test_extract_blocks_returns_empty_list_when_block_is_larger_than_input():
    assert extract_blocks("314", block_size=4) == []


def test_block_frequencies_count_overlapping_blocks():
    counts = block_frequencies("1111", block_size=2)

    assert counts == {"11": 3}


def test_block_frequencies_sort_multi_digit_blocks_for_reproducible_output():
    counts = block_frequencies("312312", block_size=2)

    assert list(counts.items()) == [("12", 2), ("23", 1), ("31", 2)]


@pytest.mark.parametrize("block_size", [0, -1])
def test_block_functions_reject_non_positive_block_sizes(block_size):
    with pytest.raises(ValueError, match="block_size"):
        extract_blocks("314159", block_size=block_size)
    with pytest.raises(ValueError, match="block_size"):
        block_frequencies("314159", block_size=block_size)


@pytest.mark.parametrize("digits", ["31.4159", "31 4159", "abc"])
def test_frequency_functions_reject_non_digit_input(digits):
    with pytest.raises(ValueError, match="digits only"):
        extract_blocks(digits, block_size=2)
    with pytest.raises(ValueError, match="digits only"):
        digit_frequencies(digits)
