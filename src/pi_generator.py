# src/pi_generator.py
from mpmath import mp
import os

def generate_pi_decimals(num_decimals=1000000):
    """
    Generate the decimal expansion of π and save it to a file.
    
    Args:
        num_decimals (int): Number of decimals to generate (default: 1,000,000).
    """
    # Check if the file already exists
    if os.path.exists("data/pi_decimals.txt"):
        print("π decimals already exist in data/pi_decimals.txt")
        return

    # Generate π with the requested precision
    mp.dps = num_decimals + 1  # Precision (number of decimals)
    pi_str = str(mp.pi).replace(".", "")  # Remove the decimal point
    with open("data/pi_decimals.txt", "w") as f:
        f.write(pi_str[:num_decimals])  # Save only the requested number of decimals
    print(f"The first {num_decimals} decimals of π have been saved to data/pi_decimals.txt")

if __name__ == "__main__":
    generate_pi_decimals(1000000)  # Generate 1 million decimals by default
