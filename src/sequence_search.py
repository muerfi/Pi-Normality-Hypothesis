"""Compatibility wrapper for sequence search.

Prefer ``python -m pi_lab search --sequence ...`` or importing from
``pi_lab.search`` in new code.
"""

import argparse

from pi_lab.digits import load_pi_digits
from pi_lab.search import search_sequence


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a sequence in pi digits")
    parser.add_argument("--sequence", required=True, help="Digit sequence to search for, e.g. 314159")
    args = parser.parse_args()

    pi_digits = load_pi_digits()
    position = search_sequence(args.sequence, pi_digits)
    if position is not None:
        print(f"Sequence '{args.sequence}' found at zero-based position {position}.")
    else:
        print(f"Sequence '{args.sequence}' was not found in the loaded digits.")
