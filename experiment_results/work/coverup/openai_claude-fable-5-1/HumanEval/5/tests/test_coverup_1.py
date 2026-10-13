# file: script_5.py:4-22
# asked: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}
# gained: {"lines": [11, 12, 14, 16, 17, 18, 20, 22], "branches": [[11, 12], [11, 14], [16, 17], [16, 20]]}

from typing import List
import pytest


def test_intersperse_empty():
    from script_5 import intersperse
    assert intersperse([], 4) == []


def test_intersperse_nonempty():
    from script_5 import intersperse
    result = intersperse([1, 2, 3], 4)
    assert result == [1, 4, 2, 4, 3]
    assert len(result) == 2 * len([1, 2, 3]) - 1


def test_intersperse_single_element():
    from script_5 import intersperse
    assert intersperse([7], 5) == [7]
