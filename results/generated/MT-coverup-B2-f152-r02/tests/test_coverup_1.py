# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import f152


def test_compare_returns_absolute_pairwise_differences():
    assert f152.compare([1, 5, -2], [4, 3, -7]) == [3, 2, 5]
