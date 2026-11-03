# file: project/f078/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f078 import hex_key


def test_hex_key_empty_string():
    """Empty input: loop body never runs, result is 0."""
    assert hex_key("") == 0


def test_hex_key_no_primes():
    """Only non-prime hex digits: the if-branch is never taken."""
    assert hex_key("1010") == 0
    assert hex_key("01489ACEF") == 0


def test_hex_key_all_primes():
    """Every character is a prime hex digit: the if-branch is always taken."""
    assert hex_key("2357BD") == 6


def test_hex_key_mixed():
    """Mixed digits exercise both branches of the if."""
    assert hex_key("AB") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2
