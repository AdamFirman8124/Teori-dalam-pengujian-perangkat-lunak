# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

from f093 import encode


def test_encode_replaces_vowels_after_swapping_case():
    assert encode("aeiouAEIOU") == "CGKQWcgkqw"


def test_encode_preserves_non_vowels_after_swapping_case():
    assert encode("Python 3!") == "pYTHQN 3!"
