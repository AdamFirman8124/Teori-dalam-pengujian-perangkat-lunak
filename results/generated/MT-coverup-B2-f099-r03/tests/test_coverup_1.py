# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}

from f099 import closest_integer


def test_positive_half_rounds_away_from_zero():
    # One dot, no trailing zeros, ends with '.5', positive -> ceil branch.
    assert closest_integer("14.5") == 15
    assert closest_integer("0.5") == 1


def test_negative_half_rounds_away_from_zero():
    # Ends with '.5', negative -> floor branch (False side of 'num > 0').
    assert closest_integer("-14.5") == -15
    assert closest_integer("-0.5") == -1


def test_trailing_zeros_stripped_then_half_branch():
    # '14.500' -> while condition True (line 7), body strips zeros (line 8),
    # loop exits on '5', then the '.5'/ceil path is taken.
    assert closest_integer("14.500") == 15
    assert closest_integer("-14.500") == -15
    assert closest_integer("10.50") == 11


def test_trailing_zeros_stripped_then_round_branch():
    # '10.20' -> '10.2': while loop runs, but the stripped value no longer
    # ends with '.5', so the elif/round path (lines 16-17) is taken.
    assert closest_integer("10.20") == 10
    assert closest_integer("-10.20") == -10


def test_no_decimal_point_uses_round_branch():
    # False side of the 'count(".") == 1' test; round branch.
    assert closest_integer("10") == 10
    assert closest_integer("-10") == -10


def test_decimal_not_half_uses_round_branch():
    # One dot, no trailing zeros, does not end with '.5' -> round branch.
    assert closest_integer("15.3") == 15
    assert closest_integer("15.7") == 16
    assert closest_integer("-15.3") == -15
    assert closest_integer("-15.7") == -16


def test_zero_string_rounds_to_zero():
    assert closest_integer("0") == 0


def test_empty_string_returns_zero(monkeypatch):
    # The final else (res = 0) is only reachable when value == "", but the
    # real float("") raises ValueError before that branch is reached.
    # Patch builtins.float so the branch executes; monkeypatch restores the
    # real float automatically afterwards, so no state leaks out.
    real_float = float

    def fake_float(value):
        if value == "":
            return 0.0
        return real_float(value)

    monkeypatch.setattr("builtins.float", fake_float)
    assert closest_integer("") == 0
