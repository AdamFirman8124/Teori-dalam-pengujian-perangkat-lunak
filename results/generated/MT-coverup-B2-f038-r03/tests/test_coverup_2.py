# file: project/f038/__init__.py:10-12
# asked: {"lines": [12], "branches": []}
# gained: {"lines": [12], "branches": []}

import pytest

from f038 import decode_cyclic


@pytest.mark.parametrize(
    ("encoded", "expected"),
    [
        ("", ""),
        ("a", "a"),
        ("ab", "ab"),
        ("abc", "cab"),
        ("abcdefg", "cabfdeg"),
    ],
)
def test_decode_cyclic(encoded, expected):
    assert decode_cyclic(encoded) == expected
