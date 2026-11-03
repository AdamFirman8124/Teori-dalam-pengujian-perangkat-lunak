

# Generated at 2026-11-02 16:19:31.538455
# Unit test for function next_smallest
def test_next_smallest():
# nonce:a7923629
    # Typical case with distinct integers
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Unsorted input
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    # Duplicates should be ignored
    assert module_0.next_smallest([1, 1, 4, 2, 2, 3]) == 2
    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3]) == -3
    assert module_0.next_smallest([0, -1, 1]) == 0
    # Mixed floats and ints
    assert module_0.next_smallest([1.5, 2.5, 3.5]) == 2.5
    # All identical elements -> None
    assert module_0.next_smallest([3, 3, 3, 3]) is None
    # Exactly two identical elements -> None
    assert module_0.next_smallest([2, 2]) is None
    # Single element -> None
    assert module_0.next_smallest([7]) is None
    # Empty list -> None
    assert module_0.next_smallest([]) is None

# Generated at 2026-11-02 16:20:59.007911
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case with distinct elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2

    # Unsorted list
    assert module_0.next_smallest([5, 3, 1, 4, 2]) == 2

    # List with duplicates
    assert module_0.next_smallest([5, 1, 4, 3, 2, 1, 2]) == 2

    # Duplicates of the smallest element
    assert module_0.next_smallest([1, 1, 1, 2]) == 2

    # Two elements only
    assert module_0.next_smallest([2, 1]) == 2

    # Negative numbers
    assert module_0.next_smallest([-1, -2, -3, -4]) == -3

    # Mixed positive and negative
    assert module_0.next_smallest([0, -5, 3, -2]) == -2

    # Single element -> None
    assert module_0.next_smallest([10]) is None

    # Empty list -> None
    assert module_0.next_smallest([]) is None

    # All identical elements -> None (only one unique value)
    assert module_0.next_smallest([7, 7, 7]) is None

    # Two identical + one different
    assert module_0.next_smallest([3, 3, 1]) == 3

    # Large values
    assert module_0.next_smallest([1000000, 999999, 1000000]) == 1000000

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 16:22:04.103007
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case with distinct integers
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Unsorted input
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    # Duplicates should be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([3, 3, 3, 1, 1, 4]) == 3
    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3
    assert module_0.next_smallest([-1, 0, 1]) == 0
    # Two unique elements
    assert module_0.next_smallest([7, 3]) == 7
    assert module_0.next_smallest([3, 7]) == 7
    # Single element -> None
    assert module_0.next_smallest([42]) is None
    # All duplicates -> None
    assert module_0.next_smallest([5, 5, 5, 5]) is None
    # Empty list -> None
    assert module_0.next_smallest([]) is None
    # Mixed positive/negative with duplicates
    assert module_0.next_smallest([0, -2, 0, -2, 3]) == 0
    # Floats supported
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5
    # Large values
    assert module_0.next_smallest([1000000, 999999, 1000001]) == 1000000
    # Already sorted list
    assert module_0.next_smallest([1, 2]) == 2
    print("All tests passed!")

test_next_smallest()

# Generated at 2026-11-02 16:23:37.428140
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case with distinct elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Unsorted input
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    # Duplicates should be ignored
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([3, 3, 3, 1, 1, 2]) == 2
    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3
    assert module_0.next_smallest([-1, 0, 1]) == 0
    # Mixed positive/negative with duplicates
    assert module_0.next_smallest([0, -2, -2, 5, 5, 1]) == -2
    # Fewer than 2 unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([4, 4, 4]) is None
    # Two unique elements
    assert module_0.next_smallest([10, 2]) == 10
    assert module_0.next_smallest([2, 10, 2]) == 10
    # Floats included
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

# Generated at 2026-11-02 16:24:47.215825
# Unit test for function next_smallest
def test_next_smallest():import pytest


def test_next_smallest_basic():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2


def test_next_smallest_unsorted():
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2


def test_next_smallest_duplicates():
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2


def test_next_smallest_all_duplicates():
    assert module_0.next_smallest([1, 1, 1]) is None


def test_next_smallest_single_element():
    assert module_0.next_smallest([7]) is None


def test_next_smallest_empty():
    assert module_0.next_smallest([]) is None


def test_next_smallest_two_elements():
    assert module_0.next_smallest([3, 1]) == 3


def test_next_smallest_two_equal_elements():
    assert module_0.next_smallest([4, 4]) is None


def test_next_smallest_negative_numbers():
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3


def test_next_smallest_mixed_signs():
    assert module_0.next_smallest([0, -2, 5, -2, 3]) == 0


def test_next_smallest_floats():
    assert module_0.next_smallest([2.5, 1.5, 3.5]) == 2.5


def test_next_smallest_int_float_mix():
    assert module_0.next_smallest([2, 1.5, 3]) == 2


def test_next_smallest_large_list():
    lst = list(range(100, 0, -1))
    assert module_0.next_smallest(lst) == 2


def test_next_smallest_string_elements():
    assert module_0.next_smallest(["b", "a", "c"]) == "b"


def test_next_smallest_does_not_modify_original():
    lst = [3, 1, 2]
    module_0.next_smallest(lst)
    assert lst == [3, 1, 2]