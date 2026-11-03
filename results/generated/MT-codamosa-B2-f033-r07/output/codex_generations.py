

# Generated at 2026-11-02 15:40:30.890537
# Unit test for function sort_third
def test_sort_third():
    # Classic example: indices 0, 3, 6 hold values 5, 4, 2 -> sorted to 2, 4, 5
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

    # Longer list including negative numbers
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Short list: only index 0 is affected
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([7]) == [7]

    # Duplicates among the sorted positions
    assert module_0.sort_third([3, 1, 1, 2, 1, 1, 1, 1, 1]) == [1, 1, 1, 2, 1, 1, 3, 1, 1]

    # Already sorted at every third position stays the same
    assert module_0.sort_third([1, 9, 9, 2, 9, 9, 3, 9, 9]) == [1, 9, 9, 2, 9, 9, 3, 9, 9]

    # Original list must not be mutated
    original = [9, 8, 7, 6, 5, 4]
    result = module_0.sort_third(original)
    assert original == [9, 8, 7, 6, 5, 4]
    assert result == [6, 8, 7, 9, 5, 4]

    # Works with tuples as input (function copies via list())
    assert module_0.sort_third((4, 1, 1, 3, 1, 1)) == [3, 1, 1, 4, 1, 1]

# Generated at 2026-11-02 15:43:24.614146
# Unit test for function sort_third
def test_sort_third():
    # Every third element (indices 0, 3, 6, ...) sorted, others unchanged

    # Basic cases
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2, 2]) == [2, 6, 3, 4, 8, 9, 5, 2]

    # Every third element already sorted
    assert module_0.sort_third([1, 5, 3, 2, 6, 9]) == [1, 5, 3, 2, 6, 9]

    # Unsorted thirds in reverse order
    assert module_0.sort_third([9, 5, 3, 6, 2, 1]) == [3, 5, 3, 6, 2, 1]

    # Duplicates among every third element
    assert module_0.sort_third([4, 1, 1, 4, 1, 1, 4, 1, 1]) == [4, 1, 1, 4, 1, 1, 4, 1, 1]

    # Negative numbers
    assert module_0.sort_third([-3, 0, 7, -1, 5, 2, -5, 8]) == [-5, 0, 7, -1, 5, 2, -3, 8]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([42]) == [42]

    # Long list where every third element needs sorting
    assert module_0.sort_third([10, 1, 2, 8, 3, 4, 6, 5, 7, 4, 9, 0]) == [4, 1, 2, 6, 3, 4, 8, 5, 7, 10, 9, 0]

    # Original list must not be modified
    original = [5, 6, 3, 4, 8, 9, 2]
    result = module_0.sort_third(original)
    assert original == [5, 6, 3, 4, 8, 9, 2]
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert result is not original

    # Works with tuples as input (converted to list)
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]

    # Floats
    assert module_0.sort_third([3.5, 1.0, 2.0, 1.5, 0.5]) == [1.5, 1.0, 2.0, 3.5, 0.5]

    print("All tests passed!")

# Generated at 2026-11-02 15:46:00.060618
# Unit test for function sort_third
def test_sort_third():
    # Basic case: elements at indices 0, 3, 6... are sorted, others unchanged
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([7]) == [7]

    # Two elements (only index 0 is "every third")
    assert module_0.sort_third([3, 1]) == [3, 1]

    # Exactly three elements: only index 0 sorted
    assert module_0.sort_third([9, 8, 7]) == [9, 8, 7]

    # Four elements: indices 0 and 3 sorted
    assert module_0.sort_third([4, 1, 2, 3]) == [3, 1, 2, 4]

    # Duplicates handled correctly
    assert module_0.sort_third([3, 0, 0, 3, 0, 0, 1, 0, 0]) == [1, 0, 0, 3, 0, 0, 3, 0, 0]

    # Negative numbers
    assert module_0.sort_third([-5, 1, 2, -3, 4, 5, -1, 6]) == [-5, 1, 2, -1, 4, 5, -3, 6]

    # Original list must not be modified
    original = [5, 6, 3, 4, 8, 9, 2]
    original_copy = list(original)
    result = module_0.sort_third(original)
    assert original == original_copy
    assert result == [2, 6, 3, 4, 8, 9, 5]

    # Result is a new list object
    lst = [1, 2, 3, 4]
    assert module_0.sort_third(lst) is not lst

    # Already sorted every-third positions remain unchanged
    assert module_0.sort_third([1, 100, 100, 2, 100, 100, 3]) == [1, 100, 100, 2, 100, 100, 3]

    # Works with tuples as input (any iterable)
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]

    # Floats
    assert module_0.sort_third([3.5, 1.1, 2.2, 1.5]) == [1.5, 1.1, 2.2, 3.5]

    # Longer list: indices 0, 3, 6, 9 sorted
    assert module_0.sort_third([10, 1, 1, 9, 1, 1, 8, 1, 1, 7, 1, 1]) == [7, 1, 1, 8, 1, 1, 9, 1, 1, 10, 1, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-02 15:47:33.079447
# Unit test for function sort_third
def test_sort_third():
    # Elements at indices 0, 3, 6, ... are sorted; others stay in place
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2, 1, 7]) == [2, 6, 3, 4, 8, 9, 5, 1, 7]

    # Empty and single-element lists
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([42]) == [42]

    # Two elements (only index 0 is a multiple of 3)
    assert module_0.sort_third([9, 1]) == [9, 1]

    # Already sorted multiples-of-3 positions
    assert module_0.sort_third([1, 5, 4, 2, 6, 3]) == [1, 5, 4, 2, 6, 3]

    # Reverse-ordered values at every-third positions
    assert module_0.sort_third([9, 0, 0, 6, 0, 0, 3, 0, 0, 1]) == [1, 0, 0, 3, 0, 0, 6, 0, 0, 9]

    # Duplicates handled correctly
    assert module_0.sort_third([3, 1, 2, 3, 1, 2, 1, 2, 3]) == [1, 1, 2, 2, 2, 2, 3, 3, 3]

    # Negative numbers
    assert module_0.sort_third([-5, 1, 1, -10, 1, 1, 0]) == [-10, 1, 1, -5, 1, 1, 0]

    # Input list is not mutated
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert result is not original  # returns a new list

    # Works with tuples as input (list(l) copy)
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]

    # Property check: non-multiple-of-3 positions unchanged
    data = [7, 1, 8, 2, 9, 3, 4, 5, 6, 10]
    result = module_0.sort_third(data)
    for i in range(len(data)):
        if i % 3 != 0:
            assert result[i] == data[i]

    # Property check: values at multiples of 3 are sorted
    assert result[::3] == sorted(data[::3])