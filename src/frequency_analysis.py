# src/frequency_analysis.py
import matplotlib.pyplot as plt
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

def analyze_frequency(pi_decimals):
    """
    Analyze the frequency of digits in π's decimals and generate a histogram.
    
    Args:
        pi_decimals (str): The decimal expansion of π.
    """
    # Count the frequency of each digit (0 to 9)
    freq = {str(i): 0 for i in range(10)}
    for digit in pi_decimals:
        freq[digit] += 1
    
    # Create a histogram
    plt.bar(freq.keys(), freq.values(), color='skyblue')
    plt.xlabel("Digit")
    plt.ylabel("Frequency")
    plt.title("Frequency of Digits in π's Decimals")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig("visualizations/digit_frequency.png", dpi=300, bbox_inches="tight")
    plt.close()
    print("Histogram saved to visualizations/digit_frequency.png")

if __name__ == "__main__":
    pi_decimals = load_pi_decimals()
    analyze_frequency(pi_decimals)
