

# Generated at 2026-11-02 20:32:55.738428
# Unit test for function sort_third
def test_sort_third():
    # Elements at indices divisible by 3 are sorted; others stay in place
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4]) == [4, 6, 3, 5]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

    # Longer list: indices 0, 3, 6, 9 sorted
    assert module_0.sort_third([9, 1, 1, 6, 2, 3, 3, 4, 5, 0]) == [0, 1, 1, 3, 2, 3, 6, 4, 5, 9]

    # Empty and short lists
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([42]) == [42]
    assert module_0.sort_third([2, 1]) == [2, 1]

    # Duplicates and negatives
    assert module_0.sort_third([3, -1, 2, 1, -1, 5, 2]) == [1, -1, 2, 2, -1, 5, 3]

    # Non-multiple-of-3 positions untouched
    assert module_0.sort_third([10, 100, 100]) == [10, 100, 100]

    # Input list is not mutated; a new list is returned
    original = [5, 6, 3, 4]
    result = module_0.sort_third(original)
    assert original == [5, 6, 3, 4]
    assert result is not original

    # Works with strings too
    assert module_0.sort_third(["d", "a", "c", "b"]) == ["b", "a", "c", "d"]

    # Already sorted thirds remain unchanged
    assert module_0.sort_third([1, 9, 9, 2, 8, 8, 3, 7, 7]) == [1, 9, 9, 2, 8, 8, 3, 7, 7]


test_sort_third()
print("All tests passed!")

# Generated at 2026-11-02 20:35:16.577342
# Unit test for function sort_third
def test_sort_third():
    # No elements at indices 0, 3, 6, ... need sorting (already sorted or single element)
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]

    # Elements at every third index are unsorted and get sorted
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 1, -10]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

    # All elements identical
    assert module_0.sort_third([2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([42]) == [42]

    # Exactly one index-0 element and one index-3 element, reversed
    assert module_0.sort_third([9, 0, 0, 1]) == [1, 0, 0, 9]

    # Duplicates among sorted positions
    assert module_0.sort_third([3, 1, 1, 3, 1, 1, 1]) == [1, 1, 1, 3, 1, 1, 3]

    # Original input list must not be mutated
    original = [5, 6, 3, 4, 8, 9, 2]
    result = module_0.sort_third(original)
    assert original == [5, 6, 3, 4, 8, 9, 2]
    assert result == [2, 6, 3, 4, 8, 9, 5]

    # Result should be a new list object
    lst = [1, 2, 3]
    assert module_0.sort_third(lst) is not lst

    # Works with negative numbers and mixed values at third positions
    assert module_0.sort_third([-1, 100, 50, -5, 100, 50, -10]) == [-10, 100, 50, -5, 100, 50, -1]

    # Longer list: indices 0, 3, 6, 9 sorted; others untouched
    assert module_0.sort_third([10, 1, 1, 5, 1, 1, 2, 1, 1, 7]) == [2, 1, 1, 5, 1, 1, 7, 1, 1, 10]

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-02 20:37:18.258838
# Unit test for function sort_third
def test_sort_third():
    # Basic case: no third-position elements beyond index 0
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]

    # Classic case: third positions sorted, others untouched
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

    # Longer list with negatives
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([42]) == [42]

    # Two elements: only index 0 is a third position
    assert module_0.sort_third([9, 1]) == [9, 1]

    # Third positions already sorted -> unchanged
    assert module_0.sort_third([1, 7, 2, 3, 8, 9, 5]) == [1, 7, 2, 3, 8, 9, 5]

    # Duplicates among third positions
    assert module_0.sort_third([3, 1, 1, 3, 2, 2, 1]) == [1, 1, 1, 3, 2, 2, 3]

    # Non-third indices keep original (unsorted) order
    assert module_0.sort_third([0, 9, 8, 0, 7, 6]) == [0, 9, 8, 0, 7, 6]

    # Input list must not be mutated; a new list is returned
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert result is not original

    # Works with tuples as input (list() copy accepts iterables)
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]
# nonce:643c0d95

# Generated at 2026-11-02 20:38:44.560750
# Unit test for function sort_third
def test_sort_third():
    # Basic cases where no change is needed
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]

    # Classic example: indices 0, 3, 6 -> [5, 4, 2] sorted -> [2, 4, 5]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

    # Edge cases
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([7]) == [7]
    assert module_0.sort_third([3, 1]) == [3, 1]  # only index 0 is a "third" position

    # Duplicates and negative numbers
    assert module_0.sort_third([9, -2, 0, 5, 5, -1]) == [5, -2, 0, 9, 5, -1]

    # Original list must not be mutated
    original = [10, 2, 3, 1]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [1, 2, 3, 10]

    # Works with non-list iterables (function converts via list(l))
    assert module_0.sort_third((4, 1, 1, 2)) == [2, 1, 1, 4]

    # Randomized cross-check against a reference implementation
    import random

    def reference(l):
        third = sorted(l[::3])
        it = iter(third)
        return [next(it) if i % 3 == 0 else x for i, x in enumerate(l)]

    for _ in range(100):
        lst = [random.randint(-50, 50) for _ in range(random.randint(0, 30))]
        assert module_0.sort_third(lst) == reference(lst)

    print("test_sort_third passed")


if __name__ == "__main__":
    test_sort_third()