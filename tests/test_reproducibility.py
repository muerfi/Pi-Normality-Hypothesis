from pi_lab.digits import generate_pi_digits, load_pi_digits
from pi_lab.statistics import block_frequencies, extract_blocks


def test_generate_pi_digits_is_reproducible_for_same_digit_count(tmp_path):
    first_path = tmp_path / "first.txt"
    second_path = tmp_path / "second.txt"

    generate_pi_digits(30, first_path)
    generate_pi_digits(30, second_path)

    assert load_pi_digits(first_path) == load_pi_digits(second_path)
    assert load_pi_digits(first_path) == "314159265358979323846264338327"


def test_generate_pi_digits_does_not_overwrite_existing_file_without_flag(tmp_path):
    output_path = tmp_path / "pi.txt"
    output_path.write_text("12345", encoding="utf-8")

    returned_path = generate_pi_digits(20, output_path, overwrite=False)

    assert returned_path == output_path
    assert load_pi_digits(output_path) == "12345"


def test_generate_pi_digits_overwrites_when_requested(tmp_path):
    output_path = tmp_path / "pi.txt"
    output_path.write_text("12345", encoding="utf-8")

    generate_pi_digits(20, output_path, overwrite=True)

    assert load_pi_digits(output_path) == "31415926535897932384"


def test_frequency_and_extraction_outputs_are_deterministic():
    digits = "314159265358979323846264338327"

    first_blocks = extract_blocks(digits, block_size=4)
    second_blocks = extract_blocks(digits, block_size=4)
    first_counts = block_frequencies(digits, block_size=3)
    second_counts = block_frequencies(digits, block_size=3)

    assert first_blocks == second_blocks
    assert first_counts == second_counts
    assert list(first_counts.items()) == sorted(first_counts.items())
