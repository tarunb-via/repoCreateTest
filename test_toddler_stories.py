"""
Unit tests for toddler_stories.py module.
"""

import io
import unittest
from unittest.mock import patch

import toddler_stories


class TestStoriesData(unittest.TestCase):
    """Test the STORIES data structure."""

    def test_stories_length(self):
        """Test that there are at least 4 stories."""
        self.assertGreaterEqual(len(toddler_stories.STORIES), 4)

    def test_stories_structure(self):
        """Test that each story has required keys."""
        for story in toddler_stories.STORIES:
            self.assertIn("title", story)
            self.assertIn("text", story)
            self.assertIn("age", story)
            self.assertIn("tags", story)

    def test_story_types(self):
        """Test that story fields have correct types."""
        for story in toddler_stories.STORIES:
            self.assertIsInstance(story["title"], str)
            self.assertIsInstance(story["text"], str)
            self.assertIsInstance(story["age"], int)
            self.assertIsInstance(story["tags"], list)


class TestDisplayMenu(unittest.TestCase):
    """Test the display_menu function."""

    def test_display_menu_output(self):
        """Test that display_menu prints correct output."""
        selected_stories = [
            {"title": "Story A"},
            {"title": "Story B"},
            {"title": "Story C"},
            {"title": "Story D"},
        ]

        # Capture stdout
        captured_output = io.StringIO()
        with unittest.mock.patch("sys.stdout", captured_output):
            toddler_stories.display_menu(selected_stories)

        output = captured_output.getvalue()

        # Check for expected content
        self.assertIn("Tonight's Stories", output)
        self.assertIn("1) Story A", output)
        self.assertIn("2) Story B", output)
        self.assertIn("3) Story C", output)
        self.assertIn("4) Story D", output)
        self.assertIn("-" * 40, output)


class TestDisplayStory(unittest.TestCase):
    """Test the display_story function."""

    def test_display_story_output(self):
        """Test that display_story prints story correctly."""
        story = {
            "title": "Test Story",
            "text": "Once upon a time..."
        }

        # Capture stdout
        captured_output = io.StringIO()
        with unittest.mock.patch("sys.stdout", captured_output):
            toddler_stories.display_story(story)

        output = captured_output.getvalue()

        # Check for expected content
        self.assertIn("Test Story", output)
        self.assertIn("Once upon a time...", output)
        self.assertIn("-" * 40, output)


class TestGetUserChoice(unittest.TestCase):
    """Test the get_user_choice function."""

    def test_get_user_choice_normalization(self):
        """Test that input is normalized (stripped and lowercased)."""
        # Patch input to return a value with whitespace and mixed case
        with patch("builtins.input") as mock_input:
            mock_input.return_value = "  R  "
            result = toddler_stories.get_user_choice()
            self.assertEqual(result, "r")

    def test_get_user_choice_lowercase(self):
        """Test that lowercase input works correctly."""
        with patch("builtins.input") as mock_input:
            mock_input.return_value = "q"
            result = toddler_stories.get_user_choice()
            self.assertEqual(result, "q")

    def test_get_user_choice_uppercase(self):
        """Test that uppercase input is lowercased."""
        with patch("builtins.input") as mock_input:
            mock_input.return_value = "Q"
            result = toddler_stories.get_user_choice()
            self.assertEqual(result, "q")


class TestMain(unittest.TestCase):
    """Test the main function."""

    def test_main_error_when_fewer_than_4_stories(self):
        """Test that main exits with error when fewer than 4 stories exist."""
        # Patch STORIES to have only 3 stories
        short_stories = [
            {"title": "A", "text": "Text", "age": 3, "tags": ["tag"]},
            {"title": "B", "text": "Text", "age": 3, "tags": ["tag"]},
            {"title": "C", "text": "Text", "age": 3, "tags": ["tag"]},
        ]

        with patch.object(toddler_stories, "STORIES", short_stories):
            with self.assertRaises(SystemExit) as context:
                toddler_stories.main()
            self.assertEqual(context.exception.code, 1)

    def test_main_error_message(self):
        """Test that main prints error message when fewer than 4 stories exist."""
        short_stories = [
            {"title": "A", "text": "Text", "age": 3, "tags": ["tag"]},
            {"title": "B", "text": "Text", "age": 3, "tags": ["tag"]},
            {"title": "C", "text": "Text", "age": 3, "tags": ["tag"]},
        ]

        captured_error = io.StringIO()
        with patch.object(toddler_stories, "STORIES", short_stories):
            with self.assertRaises(SystemExit):
                with unittest.mock.patch("sys.stderr", captured_error):
                    toddler_stories.main()

        error_output = captured_error.getvalue()
        self.assertIn("at least 4 stories", error_output)

    def test_main_happy_path_quit(self):
        """Test that main exits cleanly when user chooses to quit."""
        # Create deterministic test stories
        test_stories = [
            {"title": "Story A", "text": "Text A", "age": 3, "tags": ["tag"]},
            {"title": "Story B", "text": "Text B", "age": 3, "tags": ["tag"]},
            {"title": "Story C", "text": "Text C", "age": 3, "tags": ["tag"]},
            {"title": "Story D", "text": "Text D", "age": 3, "tags": ["tag"]},
        ]

        # Patch random.sample to return test_stories
        # Patch get_user_choice to return 'q' immediately
        captured_output = io.StringIO()

        with patch.object(toddler_stories, "STORIES", test_stories):
            with patch("random.sample") as mock_sample:
                mock_sample.return_value = test_stories[:4]
                with patch.object(toddler_stories, "get_user_choice") as mock_choice:
                    mock_choice.return_value = "q"
                    with unittest.mock.patch("sys.stdout", captured_output):
                        toddler_stories.main()

        output = captured_output.getvalue()
        # Check for expected messages
        self.assertIn("Welcome to Toddler Story Time", output)
        self.assertIn("Goodnight! Sweet dreams!", output)
        # Verify the loop exited (get_user_choice called once)
        mock_choice.assert_called_once()

    def test_main_reroll_path(self):
        """Test that main handles reroll correctly."""
        test_stories = [
            {"title": "Story A", "text": "Text A", "age": 3, "tags": ["tag"]},
            {"title": "Story B", "text": "Text B", "age": 3, "tags": ["tag"]},
            {"title": "Story C", "text": "Text C", "age": 3, "tags": ["tag"]},
            {"title": "Story D", "text": "Text D", "age": 3, "tags": ["tag"]},
            {"title": "Story E", "text": "Text E", "age": 3, "tags": ["tag"]},
        ]

        captured_output = io.StringIO()

        with patch.object(toddler_stories, "STORIES", test_stories):
            with patch("random.sample") as mock_sample:
                # First call: returns first 4, second call: returns last 4 (with overlap)
                mock_sample.side_effect = [
                    test_stories[:4],
                    test_stories[1:5],
                ]
                with patch.object(toddler_stories, "get_user_choice") as mock_choice:
                    # First return 'r' for reroll, then 'q' to quit
                    mock_choice.side_effect = ["r", "q"]
                    with unittest.mock.patch("sys.stdout", captured_output):
                        toddler_stories.main()

        output = captured_output.getvalue()
        self.assertIn("Rerolling", output)
        self.assertIn("Goodnight! Sweet dreams!", output)
        self.assertEqual(mock_choice.call_count, 2)
        self.assertEqual(mock_sample.call_count, 2)

    def test_main_display_story_path(self):
        """Test that main handles displaying a story correctly."""
        test_stories = [
            {"title": "Story A", "text": "Text A", "age": 3, "tags": ["tag"]},
            {"title": "Story B", "text": "Text B", "age": 3, "tags": ["tag"]},
            {"title": "Story C", "text": "Text C", "age": 3, "tags": ["tag"]},
            {"title": "Story D", "text": "Text D", "age": 3, "tags": ["tag"]},
        ]

        captured_output = io.StringIO()

        with patch.object(toddler_stories, "STORIES", test_stories):
            with patch("random.sample") as mock_sample:
                mock_sample.return_value = test_stories[:4]
                with patch.object(toddler_stories, "get_user_choice") as mock_choice:
                    # First return '1' to display first story, then 'q' to quit
                    mock_choice.side_effect = ["1", "q"]
                    with patch("builtins.input") as mock_press_enter:
                        mock_press_enter.return_value = ""
                        with unittest.mock.patch("sys.stdout", captured_output):
                            toddler_stories.main()

        output = captured_output.getvalue()
        self.assertIn("Story A", output)
        self.assertIn("Text A", output)
        self.assertIn("Goodnight! Sweet dreams!", output)


if __name__ == "__main__":
    unittest.main()