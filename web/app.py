# web/app.py
from flask import Flask, render_template, request
import os
from src.sequence_search import search_sequence, load_pi_decimals

app = Flask(__name__)

# Ensure the digit_frequency.png exists
if not os.path.exists("static/digit_frequency.png"):
    os.symlink("../visualizations/digit_frequency.png", "static/digit_frequency.png")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    sequence = None
    if request.method == "POST":
        sequence = request.form["sequence"]
        pi_decimals = load_pi_decimals()
        position = search_sequence(sequence, pi_decimals)
        if position is not None:
            result = f"Sequence '{sequence}' found at position {position}"
        else:
            result = f"Sequence '{sequence}' not found"
    return render_template("index.html", result=result, sequence=sequence)

@app.route("/frequency")
def frequency():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
