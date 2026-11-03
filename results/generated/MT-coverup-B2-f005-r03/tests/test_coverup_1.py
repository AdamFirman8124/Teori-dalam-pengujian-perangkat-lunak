# file: project/f005/__init__.py:4-17
# asked: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}
# gained: {"lines": [6, 7, 9, 11, 12, 13, 15, 17], "branches": [[6, 7], [6, 9], [11, 12], [11, 15]]}

"""Tests for f005.intersperse, targeting the previously uncovered lines 6-17."""

from typing import List

import pytest

from f005 import intersperse


def test_intersperse_empty_list_returns_empty() -> None:
    """Covers lines 6-7 (the `if not numbers:` True branch)."""
    result: List[int] = intersperse([], 7)

    assert result == []
    assert isinstance(result, list)


def test_intersperse_single_element_skips_loop() -> None:
    """Covers the `for` loop never executing (numbers[:-1] is empty),
    while still exercising lines 9, 15 and 17."""
    result: List[int] = intersperse([42], 7)

    # No delimiter should be added around a lone element.
    assert result == [42]


def test_intersperse_multiple_elements() -> None:
    """Covers lines 9-13 (loop body) plus lines 15 and 17."""
    result: List[int] = intersperse([1, 2, 3], 4)

    assert result == [1, 4, 2, 4, 3]
    assert len(result) == 2 * len([1, 2, 3]) - 1


def test_intersperse_two_elements() -> None:
    """Minimal case where the loop body runs exactly once."""
    result: List[int] = intersperse([10, 20], 99)

    assert result == [10, 99, 20]


def test_intersperse_with_negative_delimiter_and_values() -> None:
    """Ensures arbitrary ints (including negatives) are handled correctly."""
    result: List[int] = intersperse([-1, -2, -3], -100)

    assert result == [-1, -100, -2, -100, -3]


@pytest.mark.parametrize(
    "numbers, delimeter, expected",
    [
        ([], 0, []),
        ([5], 0, [5]),
        ([1, 2], 0, [1, 0, 2]),
        ([1, 2, 3, 4], 0, [1, 0, 2, 0, 3, 0, 4]),
    ],
)
def test_intersperse_parametrized(
    numbers: List[int], delimeter: int, expected: List[int]
) -> None:
    """Table-driven coverage of every branch: empty, single, and multi-element."""
    assert intersperse(numbers, delimeter) == expected


def test_intersperse_does_not_mutate_input() -> None:
    """Postcondition: the input list is left untouched (pure function)."""
    original = [1, 2, 3]
    snapshot = list(original)

    result = intersperse(original, 0)

    assert original == snapshot
    assert result == [1, 0, 2, 0, 3]
    assert result is not original
