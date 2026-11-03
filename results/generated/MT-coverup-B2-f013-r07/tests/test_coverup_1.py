# file: project/f013/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

import pytest

from f013 import greatest_common_divisor


def test_gcd_loop_body_executes_multiple_iterations():
    # Covers line 3 (while b:), line 4 (loop body) and line 5 (return).
    assert greatest_common_divisor(48, 18) == 6
    assert greatest_common_divisor(18, 48) == 6  # a < b: first iteration swaps
    assert greatest_common_divisor(1071, 462) == 21


def test_gcd_coprime_inputs():
    assert greatest_common_divisor(7, 13) == 1
    assert greatest_common_divisor(13, 7) == 1


def test_gcd_loop_body_skipped_when_b_is_zero():
    # Covers the false branch of `while b:` (line 3) and the return on line 5.
    assert greatest_common_divisor(5, 0) == 5
    assert greatest_common_divisor(0, 0) == 0


def test_gcd_zero_first_argument():
    # Loop body runs exactly once (0 % b == 0 terminates it).
    assert greatest_common_divisor(0, 5) == 5


def test_gcd_equal_arguments():
    assert greatest_common_divisor(12, 12) == 12


def test_gcd_negative_arguments():
    # Python's modulo semantics: gcd(-48, 18) == 6, gcd(18, -48) == -6.
    assert greatest_common_divisor(-48, 18) == 6
    assert greatest_common_divisor(18, -48) == -6


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (48, 18, 6),
        (18, 48, 6),
        (7, 13, 1),
        (1071, 462, 21),
        (12, 12, 12),
        (0, 5, 5),
        (5, 0, 5),
        (0, 0, 0),
        (-48, 18, 6),
        (18, -48, -6),
    ],
)
def test_greatest_common_divisor_matches_math_gcd(a: int, b: int, expected: int) -> None:
    result = greatest_common_divisor(a, b)
    assert result == expected
    # Postcondition: the result divides both inputs (for nonzero results).
    if result != 0:
        assert a % result == 0
        assert b % result == 0
