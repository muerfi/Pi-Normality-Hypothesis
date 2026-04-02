# PiSequence User Guide

This guide covers the command-line tools and web interface included in PiSequence.

## 1) Install dependencies

```bash
pip install -r requirements.txt
```

## 2) Generate π digits

Create `data/pi_decimals.txt`:

```bash
python src/pi_generator.py
```

By default, the script writes 1,000,000 digits (without the decimal point).

## 3) Search for a sequence

```bash
python src/sequence_search.py --sequence 12345
```

The reported position is zero-based in the stored digit string.

## 4) Plot digit frequencies

```bash
python src/frequency_analysis.py
```

This generates:

- `visualizations/digit_frequency.png`

## 5) Run exploratory examples

```bash
python src/meaningful_sequences.py
```

This script demonstrates sequence lookups for a few hardcoded examples. Treat it as exploratory output, not statistical evidence.

## 6) Launch the web interface

```bash
python web/app.py
```

Open the local URL shown by Flask (typically `http://127.0.0.1:5000`).

## 7) Run tests

```bash
python -m unittest discover tests
```
