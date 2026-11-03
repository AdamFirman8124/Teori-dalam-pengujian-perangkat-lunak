

# Generated at 2026-11-02 13:01:31.495832
# Unit test for function sort_third
def test_sort_third():
    # Basic case: mixed values
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 1]) == [1, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Indices 0, 3, 6, 9 sorted; others unchanged
    assert module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 8, 7, 3, 5, 4, 6, 2, 1, 9]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([42]) == [42]

    # Two elements (only index 0 is "third" position)
    assert module_0.sort_third([2, 1]) == [2, 1]

    # Duplicates among sorted positions
    assert module_0.sort_third([3, 1, 1, 3, 1, 1, 1]) == [1, 1, 1, 3, 1, 1, 3]

    # Already sorted every-third positions
    assert module_0.sort_third([1, 9, 9, 2, 9, 9, 3, 9]) == [1, 9, 9, 2, 9, 9, 3, 9]

    # Negative numbers
    assert module_0.sort_third([-5, 0, 0, -3, 0, 0, -1]) == [-5, 0, 0, -3, 0, 0, -1]

    # Input list must not be mutated
    original = [3, 2, 1, 6, 5, 4]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [3, 2, 1, 6, 5, 4]  # already sorted at 0,3

    # Works with tuples as input (list() copy accepts iterables)
    assert module_0.sort_third((5, 0, 0, 1, 0, 0)) == [1, 0, 0, 5, 0, 0]

    # Floats
    assert module_0.sort_third([2.5, 1.0, 0.0, 1.5, 0.0]) == [1.5, 1.0, 0.0, 2.5, 0.0]

    # Long list check
    l = list(range(30))
    shuffled = l[::-1]
    expected = list(shuffled)
    expected[::3] = sorted(shuffled[::3])
    assert module_0.sort_third(shuffled) == expected

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-02 13:04:14.280908
# Unit test for function sort_third
def test_sort_third():
    # Canonical example: indices 0, 3, 6 hold values 5, 4, 2 -> sorted to 2, 4, 5
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

    # Elements at every third position already sorted
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]

    # Empty list
    assert module_0.sort_third([]) == []

    # Fewer than 3 elements: only index 0 is in the slice, unchanged
    assert module_0.sort_third([2]) == [2]
    assert module_0.sort_third([3, 1]) == [3, 1]

    # Exactly 3 elements: only index 0 in slice, unchanged
    assert module_0.sort_third([3, 2, 1]) == [3, 2, 1]

    # Length 4: indices 0 and 3 are sorted
    assert module_0.sort_third([9, 1, 2, 3]) == [3, 1, 2, 9]

    # Length 6: indices 0 and 3 are sorted
    assert module_0.sort_third([10, 5, 5, 2, 8, 8]) == [2, 5, 5, 10, 8, 8]

    # Negative numbers and duplicates
    assert module_0.sort_third([-1, 0, 0, -5, 7, 7, 3]) == [-5, 0, 0, -1, 7, 7, 3]

    # Original list must not be mutated
    original = [3, 1, 2, 1, 5, 4]
    result = module_0.sort_third(original)
    assert original == [3, 1, 2, 1, 5, 4]
    assert result == [1, 1, 2, 3, 5, 4]

    # Returns a new list even when given a list
    lst = [1, 2, 3]
    assert module_0.sort_third(lst) is not lst

    # Accepts any iterable (tuple input) and returns a list
    out = module_0.sort_third((5, 6, 3, 4, 8, 9, 2))
    assert out == [2, 6, 3, 4, 8, 9, 5] and isinstance(out, list)

    # Property check against an independent reference
    import random
    for _ in range(50):
        data = [random.randint(-100, 100) for _ in range(random.randint(0, 30))]
        expected = list(data)
        expected[::3] = sorted(expected[::3])
        assert module_0.sort_third(data) == expected

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-02 13:06:13.698997
# Unit test for function sort_third
def test_sort_third():
    # Elements at indices 0, 3, 6, ... are sorted; others unchanged
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 6, 7, 4, 8, 9, 1, 2, 3]) == [1, 6, 7, 4, 8, 9, 5, 2, 3]
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([1]) == [1]
    assert module_0.sort_third([3, 1]) == [3, 1]
    assert module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 8, 7, 6, 5, 4, 9, 2, 1]
    assert module_0.sort_third([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [3, 1, 2, 6, 4, 5, 9, 7, 8, 10]
    # Input list must not be mutated
    original = [5, 6, 3, 4, 8, 9, 2]
    copy = list(original)
    module_0.sort_third(original)
    assert original == copy
    # Duplicates handled correctly
    assert module_0.sort_third([2, 2, 2, 1, 1, 1]) == [1, 2, 2, 2, 1, 1]
    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-02 13:09:11.965835
# Unit test for function sort_third
def test_sort_third():
    # Basic case: only every third element (indices 0, 3, 6, ...) are sorted
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Edge cases
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([42]) == [42]

    # Fewer than 3 elements: only index 0 participates
    assert module_0.sort_third([3, 1]) == [3, 1]
    assert module_0.sort_third([9, 8, 7, 6]) == [6, 8, 7, 9]

    # Third positions already sorted -> unchanged
    assert module_0.sort_third([1, 5, 5, 2, 5, 5, 3, 5, 5]) == [1, 5, 5, 2, 5, 5, 3, 5, 5]

    # Duplicates among third positions
    assert module_0.sort_third([2, 2, 2, 1, 1, 1]) == [1, 2, 2, 2, 1, 1]

    # Negative numbers
    assert module_0.sort_third([-1, 0, 0, -5, 0, 0, -3]) == [-5, 0, 0, -3, 0, 0, -1]

    # Floats
    assert module_0.sort_third([3.5, 0, 0, 1.5]) == [1.5, 0, 0, 3.5]

    # Accepts tuples (any iterable), returns a list
    assert module_0.sort_third((4, 3, 2, 1)) == [1, 3, 2, 4]

    # Original input list must not be mutated
    original = [9, 1, 1, 3, 1, 1, 6, 1, 1]
    result = module_0.sort_third(original)
    assert original == [9, 1, 1, 3, 1, 1, 6, 1, 1]
    assert result == [3, 1, 1, 6, 1, 1, 9, 1, 1]

    # Result is a new list object
    lst = [1, 2, 3]
    assert module_0.sort_third(lst) is not lst