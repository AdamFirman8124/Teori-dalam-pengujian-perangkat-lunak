# file: project/f082/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[4, 5], [4, 6], [6, 7], [6, 9], [7, 6], [7, 8]]}

"""Tests for f082.prime_length.

prime_length is a pure function (no I/O, no globals, no side effects),
so no monkeypatching or fixture-based cleanup is required; each test
leaves no state behind.

Coverage targets:
- line 3 (l = len(string)) and line 4 (the `l == 0 or l == 1` check):
  exercised by every test.
- line 5 (return False for l == 0 or l == 1): empty-string and
  single-character tests, covering both operands of the `or`.
- line 6 (loop header): composite, prime, and length-2 tests.
- line 7 (divisor check) and line 8 (return False for composite):
  composite-length test.
- line 9 (return True for prime): prime-length and length-2 tests
  (length 2 skips the loop body entirely since range(2, 2) is empty).
"""

from f082 import prime_length


def test_empty_string_returns_false():
    # l == 0: first operand of the `or` is True -> line 5 executes.
    assert prime_length("") is False


def test_single_character_returns_false():
    # l == 1: second operand of the `or` is True -> line 5 executes.
    assert prime_length("a") is False


def test_composite_length_returns_false():
    # l == 4: loop finds divisor i == 2 -> lines 6-8 execute, returns False.
    assert prime_length("abcd") is False


def test_prime_length_returns_true():
    # l == 3: loop runs, no divisor found -> lines 6, 7, 9 execute.
    assert prime_length("abc") is True


def test_length_two_returns_true():
    # l == 2: range(2, 2) is empty, loop body never runs -> lines 6 and 9.
    assert prime_length("ab") is True


def test_larger_prime_length_returns_true():
    # l == 7: loop checks 2..6, none divide 7 -> returns True.
    assert prime_length("abcdefg") is True


def test_larger_composite_length_returns_false():
    # l == 9: divisor found at i == 3 -> returns False.
    assert prime_length("abcdefghi") is False
