import pytest

from pi_lab.digits import load_pi_digits, save_pi_digits


def test_load_pi_digits_removes_whitespace_from_digit_file(tmp_path):
    digit_file = tmp_path / "pi_digits.txt"
    digit_file.write_text("31415\n 92653\t58979\n", encoding="utf-8")

    assert load_pi_digits(digit_file) == "314159265358979"


def test_load_pi_digits_raises_for_missing_file(tmp_path):
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError, match="Pi digit file not found"):
        load_pi_digits(missing_file)


def test_load_pi_digits_rejects_non_digit_content(tmp_path):
    digit_file = tmp_path / "bad_digits.txt"
    digit_file.write_text("31415x92653", encoding="utf-8")

    with pytest.raises(ValueError, match="non-digit"):
        load_pi_digits(digit_file)


def test_save_pi_digits_round_trips_with_loader(tmp_path):
    output_file = tmp_path / "nested" / "pi.txt"

    saved_path = save_pi_digits("314159", output_file)

    assert saved_path == output_file
    assert output_file.read_text(encoding="utf-8") == "314159"
    assert load_pi_digits(output_file) == "314159"


def test_save_pi_digits_rejects_non_digit_content(tmp_path):
    with pytest.raises(ValueError, match="digits only"):
        save_pi_digits("31415.9", tmp_path / "pi.txt")
