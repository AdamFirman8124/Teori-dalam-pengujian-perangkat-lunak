# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

"""Tests for f103.rounded_avg.

The function under test is pure (no I/O, no module-level or global state is
read or mutated), so no monkeypatching or teardown is required: every test
depends only on its own literal inputs and cannot pollute or be polluted by
other tests.
"""

from f103 import rounded_avg


def test_m_less_than_n_returns_minus_one():
    # Covers lines 3-4: the early-return branch when m < n.
    result = rounded_avg(5, 3)
    assert result == -1
    assert isinstance(result, int)


def test_m_equal_n_single_element_range():
    # Covers lines 5-8 with a loop body that runs exactly once.
    assert rounded_avg(5, 5) == "0b101"


def test_exact_average():
    # Covers lines 5-8 where the mean is an exact integer (no rounding drift).
    assert rounded_avg(1, 5) == "0b11"      # (1+2+3+4+5) / 5 == 3
    assert rounded_avg(7, 13) == "0b1010"   # 70 / 7 == 10


def test_rounded_average_uses_bankers_rounding():
    # Covers lines 5-8 where round() actually changes the value:
    # 4.5 -> 4 and 996.5 -> 996 and 26.5 -> 26 (round-half-to-even).
    assert rounded_avg(4, 5) == "0b100"
    assert rounded_avg(996, 997) == "0b1111100100"
    assert rounded_avg(20, 33) == "0b11010"  # 371 / 14 == 26.5 -> 26


def test_negative_bounds():
    # Covers lines 5-8 with negative inputs; bin() of a negative int.
    assert rounded_avg(-3, 1) == "-0b1"  # (-3-2-1+0+1) / 5 == -1


def test_success_return_type_is_binary_string():
    # Postcondition: successful path returns a str binary literal.
    result = rounded_avg(1, 5)
    assert isinstance(result, str)
    assert result.startswith("0b")
    int(result, 2) == 3  # sanity: parses as binary
    assert int(result, 2) == 3
