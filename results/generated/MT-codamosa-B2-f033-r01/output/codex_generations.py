

# Generated at 2026-11-02 19:44:58.457664
# Unit test for function sort_third
def test_sort_third():
    # Elements at indices 0, 3, 6, ... are sorted; others unchanged
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2, 1]) == [2, 6, 3, 4, 8, 9, 5, 1]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([7]) == [7]

    # Duplicates and negatives
    assert module_0.sort_third([9, -2, 0, 3, 5, 5, 1, 1]) == [1, -2, 0, 3, 5, 5, 9, 1]

    # Longer list: indices 0,3,6,9 sorted
    l = [10, 1, 2, 7, 4, 5, 3, 8, 9, 0]
    assert module_0.sort_third(l) == [0, 1, 2, 3, 4, 5, 7, 8, 9, 10]

    # Original list must not be mutated
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [2, 6, 3, 4, 8, 9, 5]

    # Accepts any iterable (tuple input)
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]

    # Result is a new list object
    src = [3, 1, 2]
    assert module_0.sort_third(src) is not src

# Generated at 2026-11-02 19:47:37.601033
# Unit test for function sort_third
def test_sort_third():
    # Basic case: no elements at indices 0, 3, 6, ... need sorting
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]

    # Elements at every third index get sorted, others stay in place
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

    # Longer list with negative numbers and duplicates
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([42]) == [42]

    # Two elements (only index 0 is affected)
    assert module_0.sort_third([9, 1]) == [9, 1]

    # Already sorted at third positions
    assert module_0.sort_third([1, 5, 2, 3, 6, 7]) == [1, 5, 2, 3, 6, 7]

    # Reverse-sorted third positions
    assert module_0.sort_third([9, 0, 0, 6, 0, 0, 3, 0, 0, 1]) == [1, 0, 0, 3, 0, 0, 6, 0, 0, 9]

    # Duplicates at sorted positions
    assert module_0.sort_third([3, 1, 1, 3, 1, 1, 1, 1, 1]) == [1, 1, 1, 3, 1, 1, 3, 1, 1]

    # Input list is not mutated
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert result is not original

    # Works with tuples as input (any iterable)
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]

    # Non-integer comparable values
    assert module_0.sort_third(["c", "a", "b", "a", "a", "a"]) == ["a", "a", "b", "c", "a", "a"]

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-02 19:49:59.401213
# Unit test for function sort_third
def test_sort_third():
    # Basic case: length divisible by 3
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    
    # Classic example: indices 0, 3, 6 (values 5, 4, 2) get sorted
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    
    # Negative numbers
    assert module_0.sort_third([5, 3, -2, 3, 8, 9, -1]) == [-1, 3, -2, 3, 8, 9, 5]
    
    # Edge cases: empty and short lists
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([1]) == [1]
    assert module_0.sort_third([2, 1]) == [2, 1]
    
    # Longer list: indices 0, 3, 6, 9 (values 10, 4, 7, 1) sorted
    assert module_0.sort_third([10, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Duplicates among sorted positions
    assert module_0.sort_third([3, 1, 2, 3, 5, 6, 1, 8, 9]) == [1, 1, 2, 3, 5, 6, 3, 8, 9]
    
    # Already sorted third positions remain unchanged
    assert module_0.sort_third([1, 9, 9, 2, 9, 9, 3, 9, 9]) == [1, 9, 9, 2, 9, 9, 3, 9, 9]
    
    # Input list must not be mutated (function copies via list(l))
    original = [5, 6, 3, 4, 8, 9, 2]
    result = module_0.sort_third(original)
    assert original == [5, 6, 3, 4, 8, 9, 2]
    assert result == [2, 6, 3, 4, 8, 9, 5]
    
    # Works with tuples as input (iterable converted to list)
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]

# Generated at 2026-11-02 19:52:03.750536
# Unit test for function sort_third
def test_sort_third():
    # Elements at indices 0, 3, 6, ... are sorted; all others stay in place.

    # Already sorted thirds
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    # Unsorted thirds
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 1, 3, 4, 8]) == [4, 1, 3, 5, 8]

    # Larger case with negatives
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Duplicates among the third positions
    assert module_0.sort_third([3, 1, 1, 2, 2, 2]) == [2, 1, 1, 3, 2, 2]

    # Negatives
    assert module_0.sort_third([-1, -2, -3, -4]) == [-4, -2, -3, -1]

    # Edge cases
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([7]) == [7]
    assert module_0.sort_third([3, 1]) == [3, 1]

    # Floats
    assert module_0.sort_third([2.5, 1.0, 0.5, 1.5]) == [1.5, 1.0, 0.5, 2.5]

    # Input list must not be mutated
    original = [5, 6, 3, 4, 8, 9, 2]
    result = module_0.sort_third(original)
    assert original == [5, 6, 3, 4, 8, 9, 2]
    assert result == [2, 6, 3, 4, 8, 9, 5]

    # Accepts any iterable (e.g. tuple) and always returns a list
    result = module_0.sort_third((5, 6, 3, 4, 8, 9, 2))
    assert isinstance(result, list)
    assert result == [2, 6, 3, 4, 8, 9, 5]