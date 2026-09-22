"""
PAN Number Validation Program
-------------------------------
Validates a PAN (Permanent Account Number) using a regular expression.

Format: AAAAA9999A
- First 5 characters: uppercase letters (A-Z)
- Next 4 characters: digits (0-9)
- Last character: uppercase letter (A-Z)
"""

import re

# Regular expression for PAN format
PAN_PATTERN = r'^[A-Z]{5}[0-9]{4}[A-Z]$'


def is_valid_pan(pan):
    """Return True if the given PAN matches the required pattern."""
    return bool(re.fullmatch(PAN_PATTERN, pan))


def main():
    print("=== PAN Number Validation ===")
    pan = input("Enter PAN Number: ").strip()

    if is_valid_pan(pan):
        print("Valid PAN Number")
    else:
        print("Invalid PAN Number")


if __name__ == "__main__":
    main()
