# src/utils.py
import os

def load_pi_decimals():
    """
    Load the decimal expansion of π from a file.
    
    Returns:
        str: The decimal expansion of π as a string.
    
    Raises:
        FileNotFoundError: If the pi_decimals.txt file does not exist.
    """
    if not os.path.exists("data/pi_decimals.txt"):
        raise FileNotFoundError("The file data/pi_decimals.txt does not exist. Run pi_generator.py first.")
    with open("data/pi_decimals.txt", "r") as f:
        return f.read().strip()
