# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

import pytest

from f082 import prime_length


@pytest.mark.parametrize(
    "string, expected",
    [
        ("", False),          # l == 0 -> line 5
        ("a", False),         # l == 1 -> line 5
        ("ab", True),         # l == 2, loop body never runs -> line 9
        ("abcd", False),      # l == 4, divisible by 2 -> line 8
        ("abcdef", False),    # l == 6, divisible by 2 -> line 8
        ("abcdefg", True),    # l == 7, prime -> line 9
        ("abcdefghij", False),  # l == 10, divisible by 2 -> line 8
        ("abcdefghijk", True),  # l == 11, prime -> line 9
        ("abcdefghijklm", True),  # l == 13, prime -> line 9
        ("abcdefghijklmn", False),  # l == 14, divisible by 2 -> line 8
        ("abcdefghijklmno", False),  # l == 15, divisible by 3 -> line 8
    ],
)
def test_prime_length(string, expected):
    result = prime_length(string)
    assert result is expected
    assert isinstance(result, bool)


def test_prime_length_empty_and_single_char_are_not_prime():
    assert prime_length("") is False
    assert prime_length("x") is False


def test_prime_length_two_is_prime():
    # Smallest prime length: the for-loop range(2, 2) is empty.
    assert prime_length("hi") is True


def test_prime_length_composite_lengths_return_false():
    for n in (4, 6, 8, 9, 10, 12, 15, 16, 25):
        assert prime_length("a" * n) is False, f"length {n} should not be prime"


def test_prime_length_prime_lengths_return_true():
    for n in (2, 3, 5, 7, 11, 13, 17, 19, 23):
        assert prime_length("a" * n) is True, f"length {n} should be prime"


def test_prime_length_does_not_mutate_input():
    s = "abcdefg"
    prime_length(s)
    assert s == "abcdefg"
