# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


def test_any_int_x_plus_y_equals_z():
    assert any_int(2, 3, 5) is True


def test_any_int_x_plus_z_equals_y():
    assert any_int(2, 5, 3) is True


def test_any_int_y_plus_z_equals_x():
    assert any_int(5, 2, 3) is True


def test_any_int_all_ints_no_sum_matches():
    assert any_int(1, 2, 4) is False


@pytest.mark.parametrize(
    "x, y, z",
    [
        ("2", 3, 5),
        (2, "3", 5),
        (2, 3, "5"),
        (2, 3, 5.0),
        (None, 3, 5),
        (2, None, 5),
        (2, 3, None),
    ],
)
def test_any_int_non_int_inputs(x, y, z):
    assert any_int(x, y, z) is False
