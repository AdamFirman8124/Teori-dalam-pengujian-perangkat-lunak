# file: script_38.py:1-9
# asked: {"lines": [6, 8, 9], "branches": []}
# gained: {"lines": [6, 8, 9], "branches": []}

import pytest
from script_38 import encode_cyclic


def test_encode_cyclic_empty_string():
    """Test encoding an empty string."""
    result = encode_cyclic("")
    assert result == ""


def test_encode_cyclic_single_character():
    """Test encoding a single character."""
    result = encode_cyclic("a")
    assert result == "a"


def test_encode_cyclic_two_characters():
    """Test encoding two characters."""
    result = encode_cyclic("ab")
    assert result == "ab"


def test_encode_cyclic_three_characters():
    """Test encoding exactly three characters."""
    result = encode_cyclic("abc")
    assert result == "bca"


def test_encode_cyclic_four_characters():
    """Test encoding four characters (one full group + one partial)."""
    result = encode_cyclic("abcd")
    assert result == "bcad"


def test_encode_cyclic_five_characters():
    """Test encoding five characters (one full group + two partial)."""
    result = encode_cyclic("abcde")
    assert result == "bcade"


def test_encode_cyclic_six_characters():
    """Test encoding six characters (two full groups)."""
    result = encode_cyclic("abcdef")
    assert result == "bcaefd"


def test_encode_cyclic_seven_characters():
    """Test encoding seven characters (two full groups + one partial)."""
    result = encode_cyclic("abcdefg")
    assert result == "bcaefdg"


def test_encode_cyclic_nine_characters():
    """Test encoding nine characters (three full groups)."""
    result = encode_cyclic("abcdefghi")
    assert result == "bcaefdhig"
