# PiSequence

PiSequence is a small Python project for exploring the decimal expansion of π.
It does **not** try to prove that π is normal. Instead, it provides practical tools to:

- generate a local file of π digits,
- search for digit sequences,
- inspect digit frequencies,
- and experiment with simple examples (including binary-encoded text).

The project is intentionally lightweight and educational.

## What this project does (and does not do)

- ✅ It helps you inspect finite prefixes of π and test ideas on real data.
- ✅ It shows how often digits 0-9 appear in the sampled prefix.
- ✅ It lets you look up where a sequence first appears.
- ❌ It does **not** establish statistical normality.
- ❌ It does **not** imply that a sequence has semantic meaning just because it appears.

## Features

- Generate and store the first `N` digits of π (`src/pi_generator.py`)
- Search for a sequence in those digits (`src/sequence_search.py`)
- Plot digit frequencies as a histogram (`src/frequency_analysis.py`)
- Run exploratory sequence demos (`src/meaningful_sequences.py`)
- Use a minimal Flask web UI (`web/app.py`)

## Repository layout

```text
Pi-Normality-Hypothesis/
├── src/
│   ├── pi_generator.py
│   ├── sequence_search.py
│   ├── frequency_analysis.py
│   ├── meaningful_sequences.py
│   └── utils.py
├── web/
│   ├── app.py
│   ├── templates/
│   └── static/
├── docs/
│   ├── pi_normal_hypothesis.md
│   └── user_guide.md
├── tests/
├── data/
└── visualizations/
```

## Requirements

- Python 3.10+
- Dependencies in `requirements.txt`

```bash
pip install -r requirements.txt
```

## Quick start

1. **Generate π digits** (default: 1,000,000 digits):
   ```bash
   python src/pi_generator.py
   ```

2. **Search for a sequence**:
   ```bash
   python src/sequence_search.py --sequence 314159
   ```

3. **Build a digit-frequency plot**:
   ```bash
   python src/frequency_analysis.py
   ```

4. **Run the web app**:
   ```bash
   python web/app.py
   ```

## Testing

```bash
python -m unittest discover tests
```

## Notes on interpretation

The normality of π in base 10 is still unproven. This repository should be treated as an exploratory sandbox for finite data, not as evidence of a proof.
