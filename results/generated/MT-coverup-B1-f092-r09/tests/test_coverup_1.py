# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

from f092 import any_int


def test_any_int_x_plus_y_equals_z():
    assert any_int(2, 3, 5) is True


def test_any_int_x_plus_z_equals_y():
    assert any_int(2, 5, 3) is True


def test_any_int_y_plus_z_equals_x():
    assert any_int(5, 2, 3) is True


def test_any_int_all_ints_no_sum_returns_false():
    assert any_int(1, 2, 4) is False


def test_any_int_x_not_int_returns_false():
    assert any_int("a", 2, 3) is False


def test_any_int_y_not_int_returns_false():
    assert any_int(1, "b", 3) is False


def test_any_int_z_not_int_returns_false():
    assert any_int(1, 2, "c") is False


def test_any_int_floats_return_false():
    assert any_int(1.0, 2.0, 3.0) is False
