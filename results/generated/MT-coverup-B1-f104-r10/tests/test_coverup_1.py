# file: project/f104/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f104 import unique_digits


def test_unique_digits_mixed_input():
    result = unique_digits([15, 0, 311, 103, 53, 723, 135, 103, 31])
    assert result == [15, 31, 53, 135, 311]
