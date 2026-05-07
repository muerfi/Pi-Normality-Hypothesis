"""Plotting helpers for digit-frequency summaries."""

from pathlib import Path

import matplotlib.pyplot as plt

from pi_lab.statistics import digit_frequencies
from pi_lab.utils.paths import default_visualization_path


def plot_digit_frequencies(pi_digits: str, output: str | Path | None = None) -> Path:
    """Create a bar chart of single-digit frequencies and return its path."""
    counts = digit_frequencies(pi_digits)
    output_path = Path(output) if output is not None else default_visualization_path()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    plt.bar(counts.keys(), counts.values(), color="skyblue")
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.title("Frequency of Digits in a Finite Prefix of Pi")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()
    return output_path
