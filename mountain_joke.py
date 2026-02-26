"""
A script that prints a random mountain-themed joke.

Run this file to get a random joke about mountains each time.
"""

import random

JOKES = [
    "Why do mountains make great comedians? Because they have peak performances!",
    "What's a mountain's favorite game? Peak-a-boo!",
    "Why did the mountain go to the doctor? It had a peak cough!",
    "What do you call a mountain that tells jokes? Mount Hilarious!",
    "Why are mountains so good at keeping secrets? They keep them under their peaks!",
    "What's a mountain's favorite type of music? Rock and roll!",
    "Why don't mountains ever get lost? They always know their peak location!",
    "What did one mountain say to the other? Let's rock and roll!",
    "Why did the mountain break up with the hill? Because she wanted someone with more elevation!",
    "What's a mountain's favorite dessert? Rocky road ice cream!",
]

def main() -> None:
    """Print a random mountain-themed joke."""
    print(random.choice(JOKES))

if __name__ == "__main__":
    main()