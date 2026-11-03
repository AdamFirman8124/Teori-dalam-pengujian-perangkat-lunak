# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f054 import same_chars


@pytest.mark.parametrize(
    "s0, s1, expected",
    [
        # Same set of characters in different order -> True
        ("eabcdzzzz", "dddzzzzzzzddeddabc", True),
        ("abcd", "abcd", True),
        ("aabb", "ab", True),          # duplicates collapse to same set
        # Different sets of characters -> False
        ("abcd", "d2cbad", False),
        ("abc", "abd", False),
        # Empty string edge cases
        ("", "", True),
        ("", "a", False),
        ("a", "", False),
        # Unicode characters
        ("héllo", "olléh", True),
        ("héllo", "hello", False),
    ],
)
def test_same_chars(s0, s1, expected):
    assert same_chars(s0, s1) is expected
