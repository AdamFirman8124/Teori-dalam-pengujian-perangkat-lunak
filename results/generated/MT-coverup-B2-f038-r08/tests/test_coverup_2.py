# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest

from f038 import decode_cyclic


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", ""),
        ("a", "a"),
        ("ab", "ab"),
        ("abc", "cab"),
        ("abcdefg", "cabfdeg"),
    ],
)
def test_decode_cyclic(value, expected):
    assert decode_cyclic(value) == expected
