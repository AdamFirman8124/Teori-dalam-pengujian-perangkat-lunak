# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

import pytest

from f132 import is_nested


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("[[]]", True),
        ("[][]", False),
        ("[", False),
        ("][", False),
        ("", False),
    ],
)
def test_is_nested_covers_all_branches(value, expected):
    assert is_nested(value) is expected
