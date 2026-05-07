"""Compatibility examples for searching target digit strings.

The examples are demonstrations only. A target string appearing in a finite
prefix of pi does not imply semantic meaning.
"""

from pi_lab.digits import load_pi_digits
from pi_lab.search import search_sequence


def text_to_binary(text):
    """Convert text to an ASCII binary digit string."""
    return "".join(format(ord(char), "08b") for char in text)


if __name__ == "__main__":
    pi_digits = load_pi_digits()

    prime_numbers = ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29"]
    print("Searching for example prime-number digit strings:")
    for prime in prime_numbers:
        position = search_sequence(prime, pi_digits)
        if position is not None:
            print(f"Target '{prime}' found at zero-based position {position}")
        else:
            print(f"Target '{prime}' not found in the loaded digits")

    birth_date = "19950315"
    position = search_sequence(birth_date, pi_digits)
    print("\nSearching for example date-like target string (19950315):")
    if position is not None:
        print(f"Target '{birth_date}' found at zero-based position {position}")
    else:
        print(f"Target '{birth_date}' not found in the loaded digits")

    message = "HI"
    binary_message = text_to_binary(message)
    position = search_sequence(binary_message, pi_digits)
    print("\nSearching for an example ASCII-binary target string ('HI'):")
    if position is not None:
        print(f"Target '{binary_message}' found at zero-based position {position}")
    else:
        print(f"Target '{binary_message}' not found in the loaded digits")
