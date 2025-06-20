# src/sequence_search.py
import argparse
from src.utils import load_pi_decimals


def search_sequence(sequence, pi_decimals):
    """
    Search for a sequence in π's decimals.
    
    Args:
        sequence (str): The sequence to search for.
        pi_decimals (str): The decimal expansion of π.
    
    Returns:
        int or None: The position of the first occurrence of the sequence, or None if not found.
    """
    position = pi_decimals.find(sequence)
    if position != -1:
        return position
    return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search for a sequence in π's decimals")
    parser.add_argument("--sequence", required=True, help="Sequence to search for (e.g., '12345')")
    args = parser.parse_args()

    pi_decimals = load_pi_decimals()
    position = search_sequence(args.sequence, pi_decimals)
    if position is not None:
        print(f"Sequence '{args.sequence}' found at position {position} in π's decimals")
    else:
        print(f"Sequence '{args.sequence}' not found in π's decimals")
