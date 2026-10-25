

# Generated at 2026-10-24 10:31:41.913024
# Unit test for function can_arrange
def test_can_arrange():import pytest
from solution import can_arrange

def test_empty():
    assert module_0.can_arrange([]) == -1

def test_single():
    assert module_0.can_arrange([1]) == -1

def test_sorted_ascending():
    assert module_0.can_arrange([1, 2, 3, 4]) == -1

def test_sorted_descending():
    assert module_0.can_arrange([4, 3, 2, 1]) == 2   # last descent is the final index

def test_single_descent():
    assert module_0.can_arrange([1, 3, 2]) == 2
    assert module_0.can_arrange([2, 1, 3]) == 1

def test_multiple_descents_returns_last():
    assert module_0.can_arrange([1, 2, 3, 2, 4]) == 3
    assert module_0.can_arrange([5, 1, 4, 2, 6]) == 3

def test_duplicates_are_not_descents():
    assert module_0.can_arrange([1, 1, 1]) == -1
    assert module_0.can_arrange([2, 2, 1]) == 2

def test_negative_numbers():
    assert module_0.can_arrange([-1, -2, -3]) == 2

# Generated at 2026-10-24 10:31:43.236529
# Unit test for function can_arrange
def test_can_arrange():import pytest
from solution import can_arrange

def test_empty():
    assert module_0.can_arrange([]) == -1

def test_single():
    assert module_0.can_arrange([1]) == -1

def test_sorted_ascending():
    assert module_0.can_arrange([1, 2, 3, 4]) == -1

def test_sorted_descending():
    assert module_0.can_arrange([4, 3, 2, 1]) == 2   # last descent is the final index

def test_single_descent():
    assert module_0.can_arrange([1, 3, 2]) == 2
    assert module_0.can_arrange([2, 1, 3]) == 1

def test_multiple_descents_returns_last():
    assert module_0.can_arrange([1, 2, 3, 2, 4]) == 3
    assert module_0.can_arrange([5, 1, 4, 2, 6]) == 3

def test_duplicates_are_not_descents():
    assert module_0.can_arrange([1, 1, 1]) == -1
    assert module_0.can_arrange([2, 2, 1]) == 2

def test_negative_numbers():
    assert module_0.can_arrange([-1, -2, -3]) == 2

# Generated at 2026-10-24 10:31:44.551609
# Unit test for function can_arrange
def test_can_arrange():import pytest
from solution import can_arrange

def test_empty():
    assert module_0.can_arrange([]) == -1

def test_single():
    assert module_0.can_arrange([1]) == -1

def test_sorted_ascending():
    assert module_0.can_arrange([1, 2, 3, 4]) == -1

def test_sorted_descending():
    assert module_0.can_arrange([4, 3, 2, 1]) == 2   # last descent is the final index

def test_single_descent():
    assert module_0.can_arrange([1, 3, 2]) == 2
    assert module_0.can_arrange([2, 1, 3]) == 1

def test_multiple_descents_returns_last():
    assert module_0.can_arrange([1, 2, 3, 2, 4]) == 3
    assert module_0.can_arrange([5, 1, 4, 2, 6]) == 3

def test_duplicates_are_not_descents():
    assert module_0.can_arrange([1, 1, 1]) == -1
    assert module_0.can_arrange([2, 2, 1]) == 2

def test_negative_numbers():
    assert module_0.can_arrange([-1, -2, -3]) == 2

# Generated at 2026-10-24 10:31:46.008355
# Unit test for function can_arrange
def test_can_arrange():import pytest
from solution import can_arrange

def test_empty():
    assert module_0.can_arrange([]) == -1

def test_single():
    assert module_0.can_arrange([1]) == -1

def test_sorted_ascending():
    assert module_0.can_arrange([1, 2, 3, 4]) == -1

def test_sorted_descending():
    assert module_0.can_arrange([4, 3, 2, 1]) == 2   # last descent is the final index

def test_single_descent():
    assert module_0.can_arrange([1, 3, 2]) == 2
    assert module_0.can_arrange([2, 1, 3]) == 1

def test_multiple_descents_returns_last():
    assert module_0.can_arrange([1, 2, 3, 2, 4]) == 3
    assert module_0.can_arrange([5, 1, 4, 2, 6]) == 3

def test_duplicates_are_not_descents():
    assert module_0.can_arrange([1, 1, 1]) == -1
    assert module_0.can_arrange([2, 2, 1]) == 2

def test_negative_numbers():
    assert module_0.can_arrange([-1, -2, -3]) == 2

# Generated at 2026-10-24 10:31:47.331314
# Unit test for function can_arrange
def test_can_arrange():import pytest
from solution import can_arrange

def test_empty():
    assert module_0.can_arrange([]) == -1

def test_single():
    assert module_0.can_arrange([1]) == -1

def test_sorted_ascending():
    assert module_0.can_arrange([1, 2, 3, 4]) == -1

def test_sorted_descending():
    assert module_0.can_arrange([4, 3, 2, 1]) == 2   # last descent is the final index

def test_single_descent():
    assert module_0.can_arrange([1, 3, 2]) == 2
    assert module_0.can_arrange([2, 1, 3]) == 1

def test_multiple_descents_returns_last():
    assert module_0.can_arrange([1, 2, 3, 2, 4]) == 3
    assert module_0.can_arrange([5, 1, 4, 2, 6]) == 3

def test_duplicates_are_not_descents():
    assert module_0.can_arrange([1, 1, 1]) == -1
    assert module_0.can_arrange([2, 2, 1]) == 2

def test_negative_numbers():
    assert module_0.can_arrange([-1, -2, -3]) == 2