# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], None),
        ([5, 5], None),
        ([3, 1, 2, 1], 2),
    ],
)
def test_next_smallest(values, expected):
    original = values.copy()

    assert next_smallest(values) == expected
    assert values == original
