"""
An interactive script that displays four randomized toddler stories.

Run this file to get four randomly picked stories for a three-year-old.
You can pick a story to read, reroll for new stories, or quit.
"""

import random
import sys

STORIES = [
    {
        "title": "The Little Blue Bear",
        "text": "Once there was a little blue bear. He loved to play in the sunshine. One day, he found a yellow bee. The bee said hello! The bear smiled and waved. They played chase in the grass until it was time for nap time.",
        "age": 3,
        "tags": ["friendship", "animals"]
    },
    {
        "title": "Bunny's Big Hug",
        "text": "Little Bunny hopped through the meadow. She saw her friend Duck. Duck looked sad. Bunny gave Duck a big, soft hug. Duck smiled! They played together with a shiny red ball. What a happy day!",
        "age": 3,
        "tags": ["kindness", "animals"]
    },
    {
        "title": "Twinkle the Star",
        "text": "High in the sky, there was a little star named Twinkle. Every night, she twinkled bright. The moon was her friend. Together they watched over all the sleeping children. Twinkle said goodnight to the world.",
        "age": 3,
        "tags": ["bedtime", "nature"]
    },
    {
        "title": "The Happy Sun",
        "text": "Mr. Sun woke up early. He painted the sky with orange and pink. The flowers opened up to say hello. The birds sang sweet songs. Everyone smiled because it was a beautiful day.",
        "age": 3,
        "tags": ["morning", "nature"]
    },
    {
        "title": "Kitty's New Toy",
        "text": "Little Kitty had a new ball. It was round and blue. She batted it with her paw. The ball rolled away. Kitty chased it! She found it under the bed. What a fun game!",
        "age": 3,
        "tags": ["play", "animals"]
    },
    {
        "title": "The Big Red Apple",
        "text": "On a tall tree, there was a big red apple. Squirrel saw it and climbed up. She grabbed the apple with her tiny paws. It was so yummy! She shared it with her friend Chipmunk.",
        "age": 3,
        "tags": ["sharing", "animals"]
    },
    {
        "title": "Ducky's Pond",
        "text": "Ducky loved his pond. The water was cool and nice. Froggy hopped on a lily pad. They made splashes together. Splash! Splash, splash! The fish came out to play too.",
        "age": 3,
        "tags": ["water", "animals"]
    },
    {
        "title": "The Cozy Blanket",
        "text": "Baby Bear had a soft, cozy blanket. It was warm and fuzzy. When the wind blew, Bear wrapped up tight. He felt safe and happy. Soon, Bear fell fast asleep.",
        "age": 3,
        "tags": ["bedtime", "comfort"]
    },
    {
        "title": "Puppy's First Walk",
        "text": "Little Puppy went outside for the first time. He saw a butterfly! He sniffed a flower. He met a nice dog named Spot. They wagged their tails together. What an adventure!",
        "age": 3,
        "tags": ["adventure", "animals"]
    },
    {
        "title": "The Magic Rainbow",
        "text": "After the rain, a rainbow appeared. It had so many colors! Red, orange, yellow, green, blue, and purple. Little Bird flew through it. Her feathers sparkled. It was magical!",
        "age": 3,
        "tags": ["wonder", "nature"]
    },
    {
        "title": "Balloons for You",
        "text": "A boy had three balloons. One red, one blue, one yellow. They floated up high! But the strings were in his hand. He walked down the street, showing everyone his happy balloons.",
        "age": 3,
        "tags": ["toys", "happiness"]
    },
    {
        "title": "The Sleepy Owl",
        "text": "Owl was very sleepy. He opened his big eyes and looked at the moon. Other animals were going to bed. Owl said hoot-hoot, goodnight. Then he fluffed his feathers and went to sleep in his nest.",
        "age": 3,
        "tags": ["bedtime", "animals"]
    },
    {
        "title": "Tiny Turtle",
        "text": "Tiny Turtle moved very slow. She carried her house on her back. She saw a butterfly. She saw a flower. She made it to her favorite rock and took a very long nap.",
        "age": 3,
        "tags": ["patience", "animals"]
    },
    {
        "title": "The Moon's Smile",
        "text": "The big round moon smiled down at the world. Stars danced around him. Children looked out their windows and waved. The moon stayed awake all night, keeping watch. Sweet dreams, little ones.",
        "age": 3,
        "tags": ["bedtime", "peaceful"]
    },
    {
        "title": "Cookie Time!",
        "text": "Mommy baked cookies. They smelled so good! The cookies were warm and soft. Little one got one cookie. It was chocolate chip! Yummy, yummy in the tummy!",
        "age": 3,
        "tags": ["food", "family"]
    }
]


def display_menu(selected_stories: list[dict]) -> None:
    """Display the menu of four selected stories."""
    print("\nTonight's Stories (randomly picked):")
    print("-" * 40)
    for i, story in enumerate(selected_stories, start=1):
        print(f"{i}) {story['title']}")
    print("-" * 40)


def display_story(story: dict) -> None:
    """Display a full story with title and text."""
    print(f"\n📖 {story['title']}")
    print("-" * 40)
    print(f"{story['text']}")
    print("-" * 40)


def get_user_choice() -> str:
    """Get and validate user input."""
    return input("\nPick a story (1-4), (r)eroll for 4 new stories, or (q)uit: ").strip().lower()


def main() -> None:
    """Run the interactive story picker."""
    if len(STORIES) < 4:
        print("Error: Need at least 4 stories to run!", file=sys.stderr)
        sys.exit(1)

    # Initial random selection
    selected_stories = random.sample(STORIES, k=4)

    print("\n🌟 Welcome to Toddler Story Time! 🌟")

    while True:
        display_menu(selected_stories)
        
        choice = get_user_choice()

        if choice == 'q':
            print("\nGoodnight! Sweet dreams! 💤")
            break
        elif choice == 'r':
            selected_stories = random.sample(STORIES, k=4)
            print("\n🔄 Rerolling... here are new stories!")
        elif choice in ('1', '2', '3', '4'):
            story_index = int(choice) - 1
            if 0 <= story_index < len(selected_stories):
                display_story(selected_stories[story_index])
                input("\nPress Enter to return to the menu...")
            else:
                print("Invalid story number. Please try again.")
        else:
            print("Please enter 1-4, 'r', or 'q'.")


if __name__ == "__main__":
    main()