# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f155 import even_odd_count


def test_even_odd_count_negative_mixed():
    """Covers abs() handling of negative numbers, both even and odd branches."""
    assert even_odd_count(-12) == (1, 1)


def test_even_odd_count_positive_mixed():
    """Covers the loop with both even and odd digits."""
    assert even_odd_count(123) == (1, 2)


def test_even_odd_count_zero():
    """Zero is a single even digit."""
    assert even_odd_count(0) == (1, 0)


def test_even_odd_count_all_even():
    """Only the even branch executes."""
    assert even_odd_count(2468) == (4, 0)


def test_even_odd_count_all_odd():
    """Only the odd (else) branch executes."""
    assert even_odd_count(1357) == (0, 4)
