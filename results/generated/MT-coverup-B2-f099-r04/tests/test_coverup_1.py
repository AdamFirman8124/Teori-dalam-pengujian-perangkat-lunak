# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}

import builtins

from f099 import closest_integer


def test_integer_string_without_decimal_point():
    """No '.' present: the trailing-zero loop is skipped, round() branch taken."""
    assert closest_integer("10") == 10
    assert closest_integer("-3") == -3


def test_non_half_decimal_rounds_to_nearest():
    """Value whose last two chars are not '.5' goes through int(round(num))."""
    assert closest_integer("15.3") == 15
    assert closest_integer("-15.3") == -15
    assert closest_integer("2.8") == 3


def test_positive_half_rounds_up():
    """Positive value ending in '.5' is ceiled (away from zero)."""
    assert closest_integer("14.5") == 15
    assert closest_integer("0.5") == 1
    assert closest_integer("2.5") == 3


def test_negative_half_rounds_down():
    """Negative value ending in '.5' is floored (away from zero)."""
    assert closest_integer("-14.5") == -15
    assert closest_integer("-0.5") == -1
    assert closest_integer("-2.5") == -3


def test_trailing_zeros_are_removed_before_parsing():
    """Exactly one '.' plus trailing zeros exercises the while-loop body."""
    assert closest_integer("14.500") == 15    # stripped to "14.5"  -> ceil
    assert closest_integer("-14.500") == -15  # stripped to "-14.5" -> floor
    assert closest_integer("10.00") == 10     # stripped to "10."   -> round
    assert closest_integer("0.50") == 1       # stripped to "0.5"   -> ceil


def test_empty_value_yields_zero(monkeypatch):
    """The len(value) == 0 fallback branch returns 0.

    float('') would normally raise ValueError, so the builtin float is
    temporarily widened (monkeypatch restores it afterwards) to let the
    empty string fall through to the final ``else: res = 0`` branch.
    """
    real_float = builtins.float

    def tolerant_float(value):
        return 0.0 if value == "" else real_float(value)

    monkeypatch.setattr(builtins, "float", tolerant_float)
    assert closest_integer("") == 0
