# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}

import pytest

from f099 import closest_integer


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("2.5000", 3),
        ("-2.5", -3),
        ("2.4", 2),
        ("4", 4),
    ],
)
def test_closest_integer(value, expected):
    assert closest_integer(value) == expected


def test_closest_integer_empty_length_branch():
    class FloatLike:
        def count(self, character):
            return 0

        def __float__(self):
            return 0.0

        def __getitem__(self, key):
            return ""

        def __len__(self):
            return 0

    assert closest_integer(FloatLike()) == 0
