"""Minimal Flask application for searching loaded pi digits."""

from pathlib import Path

from flask import Flask, render_template, request

from pi_lab.digits import load_pi_digits
from pi_lab.search import search_sequence
from pi_lab.utils.paths import default_visualization_path

PACKAGE_DIR = Path(__file__).resolve().parent
VISUALIZATION_FILE = default_visualization_path("digit_frequency.png")
WEB_STATIC_FILE = PACKAGE_DIR / "static" / "digit_frequency.png"


def ensure_frequency_plot_link() -> None:
    """Expose the generated frequency plot under the package static directory."""
    if WEB_STATIC_FILE.exists() or not VISUALIZATION_FILE.exists():
        return

    WEB_STATIC_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        WEB_STATIC_FILE.symlink_to(VISUALIZATION_FILE)
    except OSError:
        WEB_STATIC_FILE.write_bytes(VISUALIZATION_FILE.read_bytes())


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__, template_folder="templates", static_folder="static")

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
                pi_digits = load_pi_digits()
                position = search_sequence(sequence, pi_digits)
                if position is not None:
                    result = f"Sequence '{sequence}' found at zero-based position {position}."
                else:
                    result = f"Sequence '{sequence}' was not found in the loaded digits."

        return render_template("index.html", result=result, sequence=sequence)

    @app.route("/frequency")
    def frequency():
        """Display the frequency histogram when it is available."""
        ensure_frequency_plot_link()
        plot_available = WEB_STATIC_FILE.exists()
        return render_template("result.html", plot_available=plot_available)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
