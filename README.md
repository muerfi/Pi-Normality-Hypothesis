# PiSequence

A project to explore the decimal expansion of π and the fascinating hypothesis that π is a normal number, potentially containing every possible sequence of digits.

## Motivation

The number π is an irrational number whose decimal expansion extends infinitely without repeating patterns. A captivating but unproven hypothesis suggests that π is a normal number, meaning that each digit from 0 to 9 appears with equal frequency, and every finite sequence of digits can be found somewhere in its decimals. If true, this implies that any combination of digits—such as a credit card number, phone number, or secret code—could be found within π's infinite decimals. In other words, π might contain all possible numerical information, including computer code, encoded texts, and even images converted to binary. This project explores this property by allowing users to search for sequences, analyze digit frequencies, and reflect on the philosophical implications of this hypothesis.

## Features

- Generate or load the decimal expansion of π (up to 1 million decimals or more)
- Search for specific sequences in π's decimals (e.g., a birth date or phone number)
- Analyze the frequency of digits (0 to 9) with a histogram visualization
- Search for meaningful sequences (prime numbers, encoded messages in binary, etc..)
- Documentation on the normality hypothesis and its philosophical implications
- Interactive web interface to explore π's decimals

## Repository Structure

- **PiSequence/**: Main project directory
  - **notebooks/**: Contains Jupyter Notebooks for exploring the project
    - PiSequence.ipynb: Jupyter Notebook providing a comprehensive exploration of the project, covering all scripts, analyses, and visualizations
  - **src/**: Contains Python source code for the project
    - pi_generator.py: Script to generate or load the decimal expansion of π
    - sequence_search.py: Script to search for specific sequences within π's decimals
    - frequency_analysis.py: Script to analyze the frequency of digits (0 to 9) in π's decimals
    - meaningful_sequences.py: Script to search for meaningful sequences, such as prime numbers or encoded messages
    - utils.py: Utility functions shared across scripts
  - **data/**: Stores data files used by the project
    - pi_decimals.txt: File containing the decimal expansion of π (generated or preloaded)
    - test_sequences.txt: Optional file with sequences to test
  - **visualizations/**: Directory for generated visualizations
    - digit_frequency_pi.png: Histogram showing the frequency of digits in π's decimals
    - sequence_positions_pi.png: Visualization of the positions of found sequences (placeholder for future implementation)
  - **docs/**: Documentation files for the project
    - pi_normal_hypothesis.md: Document explaining the normality hypothesis of π and its philosophical implications
    - user_guide.md: Guide on how to use the project and its features
  - **tests/**: Unit tests to validate the project’s functionality
    - test_search.py: Tests for the sequence searching functionality
  - **web/**: Web interface for interactive exploration
    - app.py: Flask application for the web interface
    - **templates/**: HTML templates for the web interface
      - index.html: Main page for sequence searching
      - result.html: Page to display the digit frequency histogram
    - **static/**: Static files for the web interface (CSS, JavaScript)
      - style.css: CSS file for styling the web interface
  
  - **README.md**: Project overview, instructions, and documentation
  - **requirements.txt**: List of Python dependencies required for the project
  - **CONTRIBUTING.md**: Guide for contributors on how to contribute to the project

## Prerequisites

- Python 3.x
- Python libraries: `mpmath`, `matplotlib`, `flask`
  ```bash
  pip install -r requirements.txt
