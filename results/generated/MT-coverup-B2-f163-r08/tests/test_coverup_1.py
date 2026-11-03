# file: project/f163/__init__.py:1-6
# asked: {"lines": [3, 4, 6], "branches": []}
# gained: {"lines": [3, 4, 6], "branches": []}

"""Tests for f163.generate_integers covering lines 3-6 and all branches."""

from f163 import generate_integers


def test_generate_integers_typical_range():
    # Exercises lines 3, 4 and 6: lower=2, upper=8, both even and odd
    # candidates are evaluated, covering both outcomes of `i % 2 == 0`.
    assert generate_integers(2, 8) == [2, 4, 6, 8]


def test_generate_integers_reversed_arguments():
    # min/max handle swapped arguments; same expected result.
    assert generate_integers(8, 2) == [2, 4, 6, 8]


def test_generate_integers_lower_clamped_to_two():
    # min(a, b) == 1 forces `lower` to be clamped up to 2 via max(2, ...).
    # Range 2..5 contains odd numbers, exercising the False branch of the
    # even-number filter.
    assert generate_integers(1, 5) == [2, 4]


def test_generate_integers_upper_clamped_to_eight():
    # max(a, b) == 100 forces `upper` to be clamped down to 8 via min(8, ...).
    # Range 6..8 contains the odd number 7, exercising the False branch again.
    assert generate_integers(6, 100) == [6, 8]


def test_generate_integers_empty_result():
    # upper < lower yields an empty range, so the comprehension returns [].
    assert generate_integers(1, 1) == []
