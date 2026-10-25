# file: project/f090/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f090 import next_smallest


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], None),
        ([1, 1], None),
        ([5, 1, 3, 1], 3),
    ],
)
def test_next_smallest(values, expected):
    original = values.copy()

    assert next_smallest(values) == expected
    assert values == original
