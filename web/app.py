"""Compatibility entry point for the package Flask app.

Prefer ``python -m pi_lab.web.app`` in new code.
"""

from pi_lab.web.app import app


if __name__ == "__main__":
    app.run(debug=True)
