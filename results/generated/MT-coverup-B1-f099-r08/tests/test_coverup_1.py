# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}

from f099 import closest_integer


def test_no_dot_integer():
    assert closest_integer("10") == 10
    assert closest_integer("-10") == -10


def test_positive_half_away_from_zero():
    # covers: count('.')==1 True, while False (no stripping), .5 True, num>0 True
    assert closest_integer("14.5") == 15
    assert closest_integer("0.5") == 1


def test_negative_half_away_from_zero():
    # covers: .5 True, num>0 False
    assert closest_integer("-14.5") == -15
    assert closest_integer("-0.5") == -1


def test_single_trailing_zero_stripped_to_half():
    # covers: while True (one iteration) -> .5 True
    assert closest_integer("14.50") == 15
    assert closest_integer("-14.50") == -15


def test_multiple_trailing_zeros_stripped_to_half():
    # covers: while True multiple iterations
    assert closest_integer("14.5000") == 15
    assert closest_integer("-0.5000") == -1


def test_dot_non_half_rounding():
    # covers: while False, .5 False, elif True
    assert closest_integer("15.3") == 15
    assert closest_integer("-15.3") == -15
    assert closest_integer("14.4") == 14


def test_trailing_zeros_stripped_to_dot():
    # covers: while True then .5 False -> round(float("15.")) etc.
    assert closest_integer("15.0") == 15
    assert closest_integer("0.0") == 0
    assert closest_integer("10.000") == 10


def test_empty_string_returns_zero_with_mocked_float(monkeypatch):
    # covers: elif False -> else res = 0
    import builtins
    orig_float = builtins.float

    def fake_float(x):
        if x == "":
            return 0.0
        return orig_float(x)

    monkeypatch.setattr(builtins, "float", fake_float)
    assert closest_integer("") == 0
