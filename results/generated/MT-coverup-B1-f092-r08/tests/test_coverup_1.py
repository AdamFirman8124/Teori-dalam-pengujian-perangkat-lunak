# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ((1, 2, 3), True),
        ((1, 3, 2), True),
        ((3, 1, 2), True),
        ((1, 2, 4), False),
    ],
)
def test_any_int_with_integer_arguments(values, expected):
    assert any_int(*values) is expected


@pytest.mark.parametrize(
    "values",
    [
        (None, 2, 3),
        (1, None, 3),
        (1, 2, None),
    ],
)
def test_any_int_rejects_non_integer_arguments(values):
    assert any_int(*values) is False
