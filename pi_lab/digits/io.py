"""Input/output helpers for finite prefixes of pi digits."""

from pathlib import Path

from pi_lab.utils.paths import default_data_path


def load_pi_digits(path: str | Path | None = None) -> str:
    """Load a finite prefix of pi digits from ``path``.

    The file is expected to contain digits only, optionally separated by
    whitespace. By default this loads ``data/pi_decimals.txt`` from the
    project root for compatibility with the original repository layout.
    """
    digit_path = Path(path) if path is not None else default_data_path()
    if not digit_path.exists():
        raise FileNotFoundError(
            f"Pi digit file not found at {digit_path}. Run `python -m pi_lab generate` first."
        )

    raw_digits = digit_path.read_text(encoding="utf-8")
    digits = "".join(raw_digits.split())
    if not digits.isdigit():
        raise ValueError(f"Pi digit file contains non-digit characters: {digit_path}")
    return digits


def save_pi_digits(digits: str, path: str | Path | None = None) -> Path:
    """Save ``digits`` to ``path`` and return the resolved output path."""
    if not digits.isdigit():
        raise ValueError("Pi digit data must contain digits only.")

    digit_path = Path(path) if path is not None else default_data_path()
    digit_path.parent.mkdir(parents=True, exist_ok=True)
    digit_path.write_text(digits, encoding="utf-8")
    return digit_path
