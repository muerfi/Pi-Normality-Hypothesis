from pathlib import Path

from flask import Flask, render_template, request

from src.sequence_search import search_sequence
from src.utils import load_pi_decimals

app = Flask(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
VISUALIZATION_FILE = PROJECT_ROOT / "visualizations" / "digit_frequency.png"
WEB_STATIC_FILE = Path(__file__).resolve().parent / "static" / "digit_frequency.png"


def ensure_frequency_plot_link() -> None:
    """Expose the generated frequency plot under web/static for Flask."""
    if WEB_STATIC_FILE.exists() or not VISUALIZATION_FILE.exists():
        return

    WEB_STATIC_FILE.parent.mkdir(parents=True, exist_ok=True)
    WEB_STATIC_FILE.symlink_to(VISUALIZATION_FILE)


@app.route("/", methods=["GET", "POST"])
def index():
    """Render the search form and optionally process a sequence query."""
    result = None
    sequence = None

    if request.method == "POST":
        sequence = request.form["sequence"].strip()

        if not sequence.isdigit():
            result = "Please enter digits only (0-9)."
        else:
            pi_decimals = load_pi_decimals()
            position = search_sequence(sequence, pi_decimals)
            if position is not None:
                result = f"Sequence '{sequence}' found at position {position}."
            else:
                result = f"Sequence '{sequence}' was not found in the loaded digits."

    return render_template("index.html", result=result, sequence=sequence)


@app.route("/frequency")
def frequency():
    """Display the frequency histogram when it is available."""
    ensure_frequency_plot_link()
    plot_available = WEB_STATIC_FILE.exists()
    return render_template("result.html", plot_available=plot_available)


if __name__ == "__main__":
    app.run(debug=True)
