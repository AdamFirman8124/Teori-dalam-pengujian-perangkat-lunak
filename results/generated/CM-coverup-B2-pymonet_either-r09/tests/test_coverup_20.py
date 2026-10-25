# file: project/pymonet/either.py:175-180
# asked: {"lines": [180], "branches": []}
# gained: {"lines": [180], "branches": []}

from pymonet.either import Either, Left, Right


def test_right_is_right_returns_true():
    right = Right(42)
    try:
        result = right.is_right()
        assert result is True
        assert result == True
        assert isinstance(result, bool)
    finally:
        del right


def test_right_is_right_various_values():
    for value in [None, 0, "", [], {}, False, "success"]:
        instance = Right(value)
        try:
            assert instance.is_right() is True
            assert instance.is_left() is False
        finally:
            del instance


def test_right_is_right_via_either_reference():
    either: Either = Right(100)
    try:
        assert either.is_right() is True
    finally:
        del either
