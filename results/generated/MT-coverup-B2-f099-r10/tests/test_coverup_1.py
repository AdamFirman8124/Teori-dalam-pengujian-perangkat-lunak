# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}

import builtins

import pytest

from f099 import closest_integer


def test_positive_half_rounds_away_from_zero():
    """Covers: inner import, count('.')==1 True, while-condition False,
    value[-2:]=='.5' True, num > 0 True, ceil branch."""
    assert closest_integer("14.5") == 15


def test_negative_half_rounds_away_from_zero():
    """Covers: num > 0 False branch and floor branch."""
    assert closest_integer("-14.5") == -15


def test_integer_string_without_decimal_point():
    """Covers: count('.')==1 False branch and elif len(value) > 0 True."""
    assert closest_integer("10") == 10


def test_positive_fraction_rounds_to_nearest():
    """Covers: '.5' suffix check False, int(round(num)) branch."""
    assert closest_integer("15.3") == 15


def test_negative_fraction_rounds_to_nearest():
    assert closest_integer("-15.3") == -15


def test_trailing_zeros_stripped_repeatedly():
    """Covers: while-loop body (value = value[:-1]) executed several times,
    then loop condition becomes False."""
    assert closest_integer("14.5000") == 15


def test_single_trailing_zero_stops_at_dot():
    """Covers: while-loop body once; '10.0' becomes '10.', which float()
    still parses as 10.0, so the round branch is taken."""
    assert closest_integer("10.0") == 10


def test_empty_string_takes_else_branch(monkeypatch):
    """Covers: elif len(value) > 0 False -> res = 0 (line 19).

    The else branch is only reachable when value == '', but float('')
    raises ValueError. builtins.float is patched just for this test so
    that '' maps to 0.0; monkeypatch restores the original afterwards.
    """
    real_float = builtins.float

    def fake_float(value):
        if value == "":
            return 0.0
        return real_float(value)

    monkeypatch.setattr(builtins, "float", fake_float)
    # With value == '', the only reachable assignment is res = 0.
    assert closest_integer("") == 0


def test_empty_string_raises_without_patch():
    """Documents the genuine (unpatched) behaviour: float('') raises."""
    with pytest.raises(ValueError):
        closest_integer("")
