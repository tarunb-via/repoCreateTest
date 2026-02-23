"""
A simple script that prints a random joke to the console.

This module contains a collection of jokes and randomly selects one
to output to stdout each time it's run.
"""

import random

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the developer go broke? Because he used up all his cache.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "A SQL query walks into a bar, walks up to two tables and asks, 'Can I join you?'",
    "Why do Java developers wear glasses? Because they can't C#.",
]


def tell_joke():
    """Return a random joke from the JOKES list."""
    return random.choice(JOKES)


def main():
    """Print a random joke to the console."""
    print(tell_joke())


if __name__ == "__main__":
    main()