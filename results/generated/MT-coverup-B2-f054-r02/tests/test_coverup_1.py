# file: project/f054/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f054 import same_chars


@pytest.mark.parametrize(
    "s0, s1, expected",
    [
        ("eabcdzzzz", "dddzzzzzzzddeddabc", True),
        ("abcd", "dddddddabc", True),
        ("abcd", "dddddddabce", False),
        ("eabcdzzzz", "dddzzzzzzzddddabc", False),
        ("", "", True),
        ("a", "", False),
    ],
)
def test_same_chars(s0, s1, expected):
    assert same_chars(s0, s1) is expected
