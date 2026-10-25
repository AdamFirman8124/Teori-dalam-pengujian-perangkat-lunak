# file: project/f099/__init__.py:1-21
# asked: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}
# gained: {"lines": [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 17, 19, 21], "branches": [[5, 7], [5, 10], [7, 8], [7, 10], [11, 12], [11, 16], [12, 13], [12, 15], [16, 17], [16, 19]]}

from f099 import closest_integer


def test_closest_integer_rounds_half_away_from_zero_and_removes_trailing_zeros():
    assert closest_integer("1.5000") == 2
    assert closest_integer("-1.5000") == -2


def test_closest_integer_rounds_non_half_values():
    assert closest_integer("1.6") == 2
    assert closest_integer("2") == 2


def test_closest_integer_handles_zero_length_value():
    class FloatLike:
        def count(self, substring):
            return 0

        def __float__(self):
            return 1.25

        def __getitem__(self, key):
            return ""

        def __len__(self):
            return 0

    assert closest_integer(FloatLike()) == 0
