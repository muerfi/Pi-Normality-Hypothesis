# PiSequenceExplorer User Guide

## Prerequisites

- Python 3.x
- Python libraries: `mpmath`, `matplotlib`, `flask`
  ```bash
  pip install -r requirements.txt
```

## Generating π Decimals
Run the generator to create `data/pi_decimals.txt`:
```bash
python src/pi_generator.py
```

## Searching for Sequences
You can search for any digit pattern:
```bash
python src/sequence_search.py --sequence 12345
```

## Web Interface
Start the Flask application to explore via the browser:
```bash
python web/app.py
```

## Running Tests
```bash
python -m unittest
```
