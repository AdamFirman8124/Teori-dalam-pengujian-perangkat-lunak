# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f151 import double_the_difference


def test_double_the_difference_covers_all_filter_conditions():
    values = [-3, 2, 3.0, 3, 5]

    result = double_the_difference(values)

    assert result == 34
    assert values == [-3, 2, 3.0, 3, 5]
