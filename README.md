# pi_lab

`pi_lab` is a small Python package for exploring finite prefixes of the decimal
expansion of π. It can generate a local digit file, search for target digit
strings, summarize finite block frequencies, plot single-digit frequencies, and
serve a minimal Flask UI.

This project does **not** prove that π is normal, and it does **not** imply that
a digit sequence has semantic meaning just because it appears in a finite prefix.
The normality of π in base 10 remains unproven.

## Features

- Generate and store the first `N` characters of π's digit string, beginning with
  the leading `3`.
- Search a loaded finite prefix for digit sequences.
- Count overlapping blocks with configurable block size.
- Plot single-digit frequencies for a loaded finite prefix.
- Run a lightweight Flask web interface.
- Keep reusable code in the installable `pi_lab` package while leaving data,
  notebooks, experiments, and generated visualizations outside the package.

## Repository layout

```text
Pi-Normality-Hypothesis/
├── pi_lab/
│   ├── digits/
│   ├── search/
│   ├── statistics/
│   ├── visualization/
│   ├── web/
│   └── utils/
├── src/                 # Compatibility wrappers for the original scripts
├── web/                 # Compatibility entry point and legacy assets
├── tests/
├── docs/
├── notebooks/
├── data/                # Local/generated digit data
└── visualizations/      # Generated plots
```

## Installation

Install the project in editable mode from the repository root:

```bash
pip install -e .
```

For the legacy dependency-only workflow, `requirements.txt` is still available,
but new development should use the package metadata in `pyproject.toml`.

## Quick start

Generate a digit file. By default, this writes `data/pi_decimals.txt`:

```bash
python -m pi_lab generate --digits 1000000
```

Search the loaded digit file for a target sequence:

```bash
python -m pi_lab search --sequence 314159
```

Count single-digit frequencies and create `visualizations/digit_frequency.png`:

```bash
python -m pi_lab frequency --block-size 1
```

Count larger overlapping blocks without generating a plot:

```bash
python -m pi_lab frequency --block-size 2 --no-plot
```

Run the web app:

```bash
python -m pi_lab.web.app
```

## Compatibility commands

The original script paths remain as thin wrappers around `pi_lab`:

```bash
python src/pi_generator.py
python src/sequence_search.py --sequence 314159
python src/frequency_analysis.py
python web/app.py
```

## Testing

```bash
python -m pip install -r requirements.txt -r requirements-dev.txt
pytest
```

## Notes on interpretation

All results are observations about a finite loaded prefix. Single-digit or block
frequencies in a finite prefix are not a proof of base-10 normality. Finding a
sequence in a prefix is a string-search result, not evidence of hidden meaning.
