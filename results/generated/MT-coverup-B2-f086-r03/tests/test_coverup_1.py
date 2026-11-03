# file: project/f086/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

"""Tests for f086.anti_shuffle.

anti_shuffle(s) splits ``s`` on single spaces, sorts the characters of each
token, and rejoins the sorted tokens with single spaces.  The tests below
exercise the list comprehension on line 3 with several kinds of input
(single word, multiple words, empty string, consecutive spaces, mixed
character classes) and assert the exact postconditions.

The function is pure (no I/O, no globals, no side effects), so no
monkeypatching or cleanup is required; each test leaves no state behind.
"""

import pytest

from f086 import anti_shuffle


def test_anti_shuffle_single_word():
    """Characters of a single word are sorted ascending."""
    assert anti_shuffle("bca") == "abc"


def test_anti_shuffle_multiple_words():
    """Each space-separated token is sorted independently; token count preserved."""
    result = anti_shuffle("hello world")
    assert result == "ehllo dlorw"
    # Postcondition: same number of tokens, each token is a sorted anagram.
    assert len(result.split(" ")) == 2
    assert sorted(result.split(" ")[0]) == sorted("hello")
    assert sorted(result.split(" ")[1]) == sorted("world")


def test_anti_shuffle_empty_string():
    """An empty string produces a single empty token and thus an empty result."""
    assert anti_shuffle("") == ""


def test_anti_shuffle_consecutive_spaces():
    """Empty tokens between consecutive spaces are preserved verbatim."""
    assert anti_shuffle("a  b") == "a  b"


def test_anti_shuffle_mixed_case_and_symbols():
    """Sorting follows code-point order across digits, symbols, upper and lower case."""
    assert anti_shuffle("Ba1!") == "!1Ba"


def test_anti_shuffle_already_sorted_is_idempotent():
    """A string whose tokens are already sorted is returned unchanged."""
    assert anti_shuffle("abc def") == "abc def"
