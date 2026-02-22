#!/usr/bin/env python3
"""Multiply two numbers provided by user input."""


def main():
    """Get two numbers from user, multiply them, and print the result."""
    try:
        a_str = input("Enter the first number: ")
        b_str = input("Enter the second number: ")

        a = float(a_str)
        b = float(b_str)

        product = a * b
        print(f"Result: {product}")

    except ValueError:
        print("Error: Please enter valid numeric values.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()