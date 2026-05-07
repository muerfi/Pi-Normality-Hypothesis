# pi_lab User Guide

This guide covers the installable command-line tools and web interface included
in `pi_lab`.

## 1. Install the package

From the repository root:

```bash
python -m pip install -e .
```

For tests, install the development requirements as well:

```bash
python -m pip install -r requirements-dev.txt
```

## 2. Generate π digits

Create `data/pi_decimals.txt`:

```bash
python -m pi_lab generate --digits 1000000 --overwrite
```

The stored string follows the original repository convention: it starts with the
leading `3` and omits the decimal point.

## 3. Search for a target string

```bash
python -m pi_lab search --sequence 314159
```

The reported position is zero-based in the stored digit string. A target that is
absent from the loaded finite prefix might still occur later in π.

## 4. Count frequencies

Count single digits and generate `visualizations/digit_frequency.png`:

```bash
python -m pi_lab frequency --block-size 1
```

Count larger overlapping blocks without making a single-digit plot:

```bash
python -m pi_lab frequency --block-size 2 --no-plot
```

These counts are finite-prefix summaries only. They do not prove that π is
normal.

## 5. Run compatibility examples

```bash
python src/meaningful_sequences.py
```

This legacy script demonstrates target-string lookups for a few hardcoded
examples. Treat it as compatibility output only: finding a target string in a
finite prefix is not evidence of semantic content.

## 6. Launch the web interface

```bash
python -m pi_lab.web.app
```

Open the local URL shown by Flask, typically `http://127.0.0.1:5000`.

## 7. Run tests

```bash
pytest
```
