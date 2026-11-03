# file: project/f038/__init__.py:1-7
# asked: {"lines": [4, 6, 7], "branches": []}
# gained: {"lines": [4, 6, 7], "branches": []}

import pytest

from f038 import encode_cyclic


def test_encode_cyclic_empty_string():
    """Empty string: comprehension body never runs, join of nothing is ''."""
    assert encode_cyclic("") == ""


def test_encode_cyclic_single_char():
    """Group of length 1 takes the 'else' branch (unchanged)."""
    assert encode_cyclic("a") == "a"


def test_encode_cyclic_two_chars():
    """Group of length 2 takes the 'else' branch (unchanged)."""
    assert encode_cyclic("ab") == "ab"


def test_encode_cyclic_exact_group():
    """Single full group of 3 is cycled: first char moves to the end."""
    assert encode_cyclic("abc") == "bca"


def test_encode_cyclic_full_and_partial_groups():
    """Full group cycled, trailing partial group left unchanged."""
    assert encode_cyclic("abcd") == "bcad"
    assert encode_cyclic("abcde") == "bcade"


def test_encode_cyclic_multiple_full_groups():
    """Each full group of 3 is cycled independently."""
    assert encode_cyclic("abcdef") == "bcaefd"


def test_encode_cyclic_seven_chars():
    """Two full groups plus a single-char remainder."""
    assert encode_cyclic("abcdefg") == "bcaefdg"


def test_encode_cyclic_non_alpha_characters():
    """Cycling works for arbitrary characters, not just letters."""
    assert encode_cyclic("1!@#$%") == "!@1$%#"


@pytest.mark.parametrize(
    "s",
    ["", "a", "ab", "abc", "abcd", "abcde", "abcdef", "abcdefg", "hello world!"],
)
def test_encode_cyclic_triple_application_is_identity(s):
    """Cycling each group of 3 three times restores the original string."""
    assert encode_cyclic(encode_cyclic(encode_cyclic(s))) == s
