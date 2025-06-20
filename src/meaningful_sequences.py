# src/meaningful_sequences.py
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
    if position == -1:
        return None
    return position

def text_to_binary(text):
    """
    Convert text to binary (ASCII).
    
    Args:
        text (str): The text to convert.
    
    Returns:
        str: The binary representation of the text.
    """
    binary = ""
    for char in text:
        binary += format(ord(char), '08b')
    return binary

if __name__ == "__main__":
    pi_decimals = load_pi_decimals()

    # 1. Search for the first 10 prime numbers
    prime_numbers = ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29"]
    print("Searching for the first 10 prime numbers:")
    for prime in prime_numbers:
        position = search_sequence(prime, pi_decimals)
        if position is not None:
            print(f"Prime number '{prime}' found at position {position}")
        else:
            print(f"Prime number '{prime}' not found")

    # 2. Search for a birth date (e.g., March 15, 1995 → 19950315)
    birth_date = "19950315"
    position = search_sequence(birth_date, pi_decimals)
    print("\nSearching for a birth date (19950315):")
    if position is not None:
        print(f"Date '{birth_date}' found at position {position}")
    else:
        print(f"Date '{birth_date}' not found")

    # 3. Search for a message encoded in binary ("HI" in ASCII → "01001000 01001001")
    message = "HI"
    binary_message = text_to_binary(message).replace(" ", "")
    position = search_sequence(binary_message, pi_decimals)
    print("\nSearching for an encoded message ('HI' in binary: 0100100001001001):")
    if position is not None:
        print(f"Binary message '{binary_message}' found at position {position}")
    else:
        print(f"Binary message '{binary_message}' not found")
