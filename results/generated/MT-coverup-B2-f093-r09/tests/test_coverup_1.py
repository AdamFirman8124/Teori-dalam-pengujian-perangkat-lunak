# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

import pytest

from f093 import encode


@pytest.mark.parametrize(
    ("message", "expected"),
    [
        # Mixed case with vowels and consonants: exercises both branches of
        # the conditional expression on line 6 (vowel replacement and
        # pass-through of non-vowels).
        ("test", "TGST"),
        ("This is a message", "tHKS KS C MGSSCGG"),
        # Only vowels, both lower and upper case: only the "if" branch of
        # line 6 is taken, and every entry of vowels_replace is used.
        ("aeiouAEIOU", "CGKQWcgkqw"),
        # No vowels at all: only the "else" branch of line 6 is taken.
        ("xyz", "XYZ"),
        # Empty string edge case (loop body never runs).
        ("", ""),
        # Non-letter characters must pass through untouched.
        ("a1!", "C1!"),
        # Single characters hitting each vowel mapping after swapcase.
        ("u", "W"),
        ("U", "w"),
    ],
)
def test_encode(message, expected):
    assert encode(message) == expected


def test_encode_is_pure_and_does_not_mutate_argument():
    original = "Test"
    result = encode(original)
    # Postconditions: correct transformation, input untouched, new object.
    # "Test" -> swapcase -> "tEST" -> 'E' becomes 'G' -> "tGST".
    assert result == "tGST"
    assert original == "Test"
    assert result is not original
