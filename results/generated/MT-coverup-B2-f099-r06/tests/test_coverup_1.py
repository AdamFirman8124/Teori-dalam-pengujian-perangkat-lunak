# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17]]}

import pytest

from f099 import closest_integer


def test_strips_trailing_zeros_before_rounding():
    """Covers lines 3, 5, 7-8 (while loop) and 16-17 (elif branch).

    "15.700" has exactly one '.', so trailing zeros are stripped to "15.7",
    then int(round(15.7)) == 16.
    """
    assert closest_integer("15.700") == 16


def test_decimal_without_trailing_zeros_skips_while_loop():
    """Covers the False branch of the while-loop condition (line 7)."""
    assert closest_integer("15.3") == 15


def test_positive_half_rounds_up():
    """Covers lines 11-13: '.5' suffix with num > 0 -> ceil."""
    assert closest_integer("14.5") == 15


def test_positive_half_after_stripping_zeros():
    """The while loop runs, then the value lands on '.5' with num > 0 -> ceil."""
    assert closest_integer("14.50") == 15


def test_negative_half_rounds_down():
    """Covers lines 14-15: '.5' suffix with num <= 0 -> floor."""
    assert closest_integer("-14.5") == -15


def test_negative_half_after_stripping_zeros():
    """The while loop runs, then '.5' with a non-positive value -> floor."""
    assert closest_integer("-14.50") == -15


def test_negative_small_half_rounds_down():
    """floor(-0.5) == -1: inner else with a small magnitude."""
    assert closest_integer("-0.5") == -1


def test_positive_small_half_rounds_up():
    """ceil(0.5) == 1."""
    assert closest_integer("0.5") == 1


def test_integer_string_rounds():
    """Covers the False branch of `value.count('.') == 1` (line 5) and line 17."""
    assert closest_integer("10") == 10


def test_negative_decimal_rounds_away_from_zero():
    """int(round(-15.7)) == -16."""
    assert closest_integer("-15.7") == -16


def test_zero_string_rounds_to_zero():
    assert closest_integer("0") == 0


def test_float_with_only_trailing_point():
    """'10.00' is stripped to '10.', which float() still parses as 10.0."""
    assert closest_integer("10.00") == 10


def test_empty_string_raises_value_error():
    """Note: the `else: res = 0` branch (line 19) is unreachable.

    When len(value) == 0, float('') raises ValueError on line 10 before the
    branch is ever reached; and the while loop can never empty the string
    because it stops at the '.' (which is not '0'). This test pins down the
    actual behavior for the empty input instead.
    """
    with pytest.raises(ValueError):
        closest_integer("")
