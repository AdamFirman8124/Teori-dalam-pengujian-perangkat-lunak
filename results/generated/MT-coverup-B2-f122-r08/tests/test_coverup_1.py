# file: project/f122/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f122 import add_elements


def test_add_elements_includes_only_short_elements_within_k():
    arr = [1, 100, 20, 2]

    result = add_elements(arr, 3)

    assert result == 21
    assert arr == [1, 100, 20, 2]


def test_add_elements_handles_empty_slice():
    assert add_elements([1, 2, 3], 0) == 0
