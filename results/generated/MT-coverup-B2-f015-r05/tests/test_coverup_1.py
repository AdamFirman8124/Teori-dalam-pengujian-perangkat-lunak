# file: project/f015/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f015 import string_sequence


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, "0"),
        (3, "0 1 2 3"),
    ],
)
def test_string_sequence_returns_space_separated_sequence(n, expected):
    assert string_sequence(n) == expected
