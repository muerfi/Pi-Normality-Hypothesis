# PiSequenceExplorer

A project to explore the decimal expansion of π and the fascinating hypothesis that π is a normal number, potentially containing every possible sequence of digits.

## Motivation

The number π is an irrational number whose decimal expansion extends infinitely without repeating patterns. A captivating but unproven hypothesis suggests that π is a normal number, meaning that each digit from 0 to 9 appears with equal frequency, and every finite sequence of digits can be found somewhere in its decimals. If true, this implies that any combination of digits—such as a credit card number, phone number, or secret code—could be found within π's infinite decimals. In other words, π might contain all possible numerical information, including computer code, encoded texts, and even images converted to binary. This project explores this property by allowing users to search for sequences, analyze digit frequencies, and reflect on the philosophical implications of this hypothesis.

## Features

- Generate or load the decimal expansion of π (up to 1 million decimals or more).
- Search for specific sequences in π's decimals (e.g., a birth date or phone number).
- Analyze the frequency of digits (0 to 9) with a histogram visualization.
- Search for meaningful sequences (prime numbers, encoded messages in binary, etc.).
- Documentation on the normality hypothesis and its philosophical implications.
- Interactive web interface to explore π's decimals.

## Repository Structure

- `src/` : Python scripts for generating decimals, searching sequences, and analyzing data.
  - `pi_generator.py` : Generates or loads π decimals.
  - `sequence_search.py` : Searches for a sequence in the decimals.
  - `frequency_analysis.py` : Analyzes digit frequency.
  - `meaningful_sequences.py` : Searches for meaningful sequences.
  - `utils.py` : Utility functions.
- `data/` : Files containing π decimals and test sequences.
- `visualizations/` : Generated graphs (e.g., digit frequency histogram).
- `docs/` : Documentation on the normality hypothesis and user guide.
- `web/` : Web interface for interactive exploration.
- `tests/` : Unit tests to validate functionality.

## Prerequisites

- Python 3.x
- Python libraries: `mpmath`, `matplotlib`, `flask`
  ```bash
  pip install -r requirements.txt
