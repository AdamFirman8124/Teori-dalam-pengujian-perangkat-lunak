# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", False),
        ("a", False),
        ("ab", True),
        ("abc", True),
        ("abcd", False),
    ],
)
def test_prime_length(value, expected):
    assert prime_length(value) is expected


def test_prime_length_checks_composite_length():
    value = "abcdeabcdeabcdeabcde"

    assert len(value) == 20
    assert prime_length(value) is False
