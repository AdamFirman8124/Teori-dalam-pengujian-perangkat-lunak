# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

from typing import List

from script_0 import has_close_elements


def test_has_close_elements_true():
    numbers: List[float] = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
    assert has_close_elements(numbers, 0.3) is True
    # postcondition: a pair closer than threshold exists
    found = any(
        abs(a - b) < 0.3
        for i, a in enumerate(numbers)
        for j, b in enumerate(numbers)
        if i != j
    )
    assert found is True


def test_has_close_elements_false():
    numbers: List[float] = [1.0, 2.0, 3.0]
    assert has_close_elements(numbers, 0.5) is False
    # postcondition: no pair closer than threshold
    found = any(
        abs(a - b) < 0.5
        for i, a in enumerate(numbers)
        for j, b in enumerate(numbers)
        if i != j
    )
    assert found is False


def test_has_close_elements_empty():
    assert has_close_elements([], 1.0) is False
