# src/sequence_search.py
import argparse
import os

def load_pi_decimals():
    """Load π decimals from a file."""
    if not os.path.exists("data/pi_decimals.txt"):
        raise FileNotFoundError("The file data/pi_decimals.txt does not exist. Run pi_generator.py first.")
    with open("data/pi_decimals.txt", "r") as f:
        return f.read().strip()

def search_sequence(sequence, pi_decimals):
    """Search for a sequence in π's decimals."""
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
