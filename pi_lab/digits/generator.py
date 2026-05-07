"""Generate finite prefixes of pi digits."""

from pathlib import Path

from mpmath import mp

from .io import save_pi_digits


def generate_pi_digits(
    digits: int = 1_000_000,
    output: str | Path | None = None,
    *,
    overwrite: bool = False,
) -> Path:
    """Generate ``digits`` characters from pi and write them to ``output``.

    The generated string follows the original project convention: it starts
    with the leading ``3`` and then continues with decimal digits, so searching
    for ``314159`` returns position 0. This function creates finite data for
    experiments only and makes no claim about normality.
    """
    if digits < 1:
        raise ValueError("digits must be at least 1")

    output_path = Path(output) if output is not None else None
    if output_path is not None and output_path.exists() and not overwrite:
        return output_path

    mp.dps = digits + 2
    pi_digits = str(mp.pi).replace(".", "")[:digits]
    return save_pi_digits(pi_digits, output_path)
