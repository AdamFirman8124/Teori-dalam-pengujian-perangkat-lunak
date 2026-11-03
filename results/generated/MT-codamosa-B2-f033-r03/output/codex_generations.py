

# Generated at 2026-11-02 10:49:29.406721
# Unit test for function sort_third
def test_sort_third():
    # No sorting needed when fewer than 2 elements at every-third positions
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 8, -12, 4, 23, 2, 3, 11, 12, -10]) == [-10, 8, -12, 3, 23, 2, 4, 11, 12, 5]
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 1, -10]
    assert module_0.sort_third([2, 4, 3, 0, 1, 5]) == [0, 4, 3, 2, 1, 5]

    # Edge cases
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([1]) == [1]
    assert module_0.sort_third([1, 2]) == [1, 2]
    assert module_0.sort_third([3, 3, 3, 1, 1, 1]) == [1, 3, 3, 3, 1, 1]

    # Duplicates and negatives handled correctly
    assert module_0.sort_third([-1, -2, -3, -4]) == [-4, -2, -3, -1]

    # Original input list must not be mutated
    original = [3, 1, 2, 0]
    result = module_0.sort_third(original)
    assert result == [0, 1, 2, 3]
    assert original == [3, 1, 2, 0]
    assert result is not original

# Generated at 2026-11-02 10:49:52.041995
# Unit test for function sort_third
def test_sort_third():
    # nonce:4d153673
    # Basic case: elements at indices 0, 3, 6, ... are sorted, others unchanged
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 1, 3, 4, 8, 9, 2, 6]) == [2, 1, 3, 4, 8, 9, 5, 6]

    # Longer list
    assert module_0.sort_third([10, 3, 7, 1, 8, 6, 5, 2, 9, 4]) == [1, 3, 7, 4, 8, 6, 5, 2, 9, 10]

    # Empty list
    assert module_0.sort_third([]) == []

    # Lists shorter than 3 (only index 0 is in the slice)
    assert module_0.sort_third([1]) == [1]
    assert module_0.sort_third([2, 1]) == [2, 1]

    # Exactly one third-position element pair to sort
    assert module_0.sort_third([9, 1, 2, 3, 8, 7]) == [3, 1, 2, 9, 8, 7]

    # Negative numbers
    assert module_0.sort_third([-1, 5, 3, -5, 2]) == [-5, 5, 3, -1, 2]

    # Duplicates
    assert module_0.sort_third([2, 2, 2, 1, 1, 1]) == [1, 2, 2, 2, 1, 1]

    # Floats mixed with ints
    assert module_0.sort_third([3.5, 1, 2, 0.5]) == [0.5, 1, 2, 3.5]

    # Input list must not be mutated (function works on a copy)
    original = [9, 1, 2, 3, 8, 7]
    result = module_0.sort_third(original)
    assert original == [9, 1, 2, 3, 8, 7]
    assert result == [3, 1, 2, 9, 8, 7]

    # Result should be a list even if a tuple-like input is passed
    assert module_0.sort_third((9, 1, 2, 3, 8, 7)) == [3, 1, 2, 9, 8, 7]

# Generated at 2026-11-02 10:50:21.226067
# Unit test for function sort_third
def test_sort_third():
    # Basic cases: elements at indices 0, 3, 6, ... are sorted
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2, 1]) == [2, 6, 3, 4, 8, 9, 5, 1]

    # Longer list: indices 0, 3, 6, 9 sorted -> whole list becomes sorted
    assert module_0.sort_third([10, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Already sorted multiples of 3 remain unchanged
    assert module_0.sort_third([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([42]) == [42]

    # Two elements
    assert module_0.sort_third([3, 1]) == [3, 1]

    # Negative numbers
    assert module_0.sort_third([-1, -5, 3, -10, 0, 7]) == [-10, -5, 3, -1, 0, 7]

    # Duplicates
    assert module_0.sort_third([3, 1, 2, 3, 1, 2]) == [3, 1, 2, 3, 1, 2]
    assert module_0.sort_third([9, 1, 1, 2, 1, 1, 3]) == [2, 1, 1, 3, 1, 1, 9]

    # Floats
    assert module_0.sort_third([3.5, 1.0, 2.0, 1.5]) == [1.5, 1.0, 2.0, 3.5]

    # Original list is not modified
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert result is not original  # returns a new list

    # Accepts other iterables (tuple input)
    assert module_0.sort_third((5, 6, 3, 4)) == [4, 6, 3, 5]

    print("All test_sort_third tests passed!")


test_sort_third()

# Generated at 2026-11-02 10:50:52.652383
# Unit test for function sort_third
def test_sort_third():
    # No elements at indices 0, 3, 6... need sorting
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    # Only one element at a multiple-of-3 index
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    # Mixed positive/negative values across sorted positions
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]
    # Empty list
    assert module_0.sort_third([]) == []
    # Single element
    assert module_0.sort_third([7]) == [7]
    # Fewer than 3 elements: only index 0 exists
    assert module_0.sort_third([3, 1]) == [3, 1]
    # Duplicates at sorted positions
    assert module_0.sort_third([3, 1, 2, 3, 1, 2]) == [3, 1, 2, 3, 1, 2]
    # Negative numbers at sorted positions
    assert module_0.sort_third([-1, 5, 2, -3]) == [-3, 5, 2, -1]
    # Longer list: indices 0,3,6,9 -> [10,4,7,1] sorted -> [1,4,7,10]
    assert module_0.sort_third([10, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_sort_third_does_not_mutate_input():
    original = [5, 6, 3, 4, 8, 9, 2]
    copy = list(original)
    result = module_0.sort_third(original)
    assert original == copy  # input unchanged
    assert result is not original  # returns a new list


def test_sort_third_preserves_unsorted_positions():
    result = module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    # Non-multiple-of-3 indices stay identical
    assert result[1::3] == [8, 5, 2]
    assert result[2::3] == [7, 4, 1]
    # Multiple-of-3 indices sorted
    assert result[::3] == sorted([9, 6, 3, 0])
    assert result == [3, 8, 7, 6, 5, 4, 9, 2, 1, 0]


def test_sort_third_accepts_tuples():
    assert module_0.sort_third((4, 1, 1, 2, 2, 3)) == [2, 1, 1, 4, 2, 3]

# Generated at 2026-11-02 10:51:12.650757
# Unit test for function sort_third
def test_sort_third():
# nonce:42b53c56
    # Basic case: single element at index 0
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]

    # Elements at indices 0 and 3 get sorted, others stay in place
    assert module_0.sort_third([5, 6, 3, 4, 1, 2]) == [4, 6, 3, 5, 1, 2]

    # Longer list with negatives: indices 0,3,6,9 hold 5,2,9,1 -> 1,2,5,9
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == \
        [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element list
    assert module_0.sort_third([42]) == [42]

    # Two elements: only index 0 is touched
    assert module_0.sort_third([10, 2]) == [10, 2]

    # Already sorted third positions remain unchanged
    assert module_0.sort_third([1, 9, 9, 2, 8, 8, 3, 7, 7]) == [1, 9, 9, 2, 8, 8, 3, 7, 7]

    # Duplicates handled correctly
    assert module_0.sort_third([3, 1, 2, 3, 1, 2]) == [3, 1, 2, 3, 1, 2]
    assert module_0.sort_third([4, 0, 0, 2, 0, 0, 4, 0, 0]) == [2, 0, 0, 4, 0, 0, 4, 0, 0]

    # Reverse-sorted thirds get fully sorted
    assert module_0.sort_third([9, 1, 1, 6, 1, 1, 3, 1, 1, 0, 1, 1]) == \
        [0, 1, 1, 3, 1, 1, 6, 1, 1, 9, 1, 1]

    # Input list must not be mutated
    original = [5, 6, 3, 4, 1, 2]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [4, 6, 3, 5, 1, 2]
    assert result is not original

    # Works with tuples as input (function copies via list())
    assert module_0.sort_third((5, 6, 3, 4, 1, 2)) == [4, 6, 3, 5, 1, 2]

    # Works with floats
    assert module_0.sort_third([3.5, 1.0, 1.0, 1.5, 1.0, 1.0]) == [1.5, 1.0, 1.0, 3.5, 1.0, 1.0]

    # Property check: non-third positions are untouched, thirds are sorted
    data = [7, 5, 4, 2, 9, 8, 6, 3, 1, 0]
    out = module_0.sort_third(data)
    assert out[1::3] == data[1::3]
    assert out[2::3] == data[2::3]
    assert out[::3] == sorted(data[::3])
    assert len(out) == len(data)

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()