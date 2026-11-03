# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

import pytest

from f103 import rounded_avg


class TestRoundedAvg:
    """Tests for f103.rounded_avg covering all lines and branches."""

    @pytest.mark.parametrize(
        "n, m",
        [
            (1, 5),    # normal range
            (3, 3),    # single-element range (n == m)
            (0, 0),    # single element at zero
            (-5, 5),   # range including negatives
            (10, 20),  # larger range
        ],
    )
    def test_valid_range_returns_binary_string(self, n, m):
        """Lines 5-8 execute: summation loop and average return."""
        result = rounded_avg(n, m)

        # Compute expected value independently.
        summation = sum(range(n, m + 1))
        expected = bin(round(summation / (m - n + 1)))

        assert result == expected
        # Postcondition: result is a binary literal string.
        assert isinstance(result, str)
        assert result.startswith("0b")

    def test_single_element_range(self):
        """When n == m the average is simply n itself."""
        assert rounded_avg(3, 3) == bin(3) == "0b11"

    def test_known_value(self):
        """rounded_avg(1, 5): average of 1..5 is 3 -> binary 0b11."""
        assert rounded_avg(1, 5) == "0b11"

    def test_m_less_than_n_returns_minus_one(self):
        """Line 3 evaluates True (m < n branch): returns -1 early (line 4)."""
        assert rounded_avg(5, 1) == -1
        assert rounded_avg(10, 9) == -1
        assert rounded_avg(0, -1) == -1

    def test_m_not_less_than_n_takes_else_branch(self):
        """Line 3 evaluates False (n <= m branch): proceeds past the guard."""
        # n == m boundary of the false branch already covered, but assert
        # explicitly that a valid call does NOT yield the sentinel -1.
        result = rounded_avg(2, 4)
        assert result != -1
        assert result == bin(round((2 + 3 + 4) / 3)) == "0b11"
