

# Generated at 2026-11-03 02:09:09.209435
# Unit test for function sort_third
def test_sort_third():
    # nonce:5436190d
    # Basic case: single slice element, nothing to sort
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]

    # Standard case: elements at indices 0, 3, 6 get sorted
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

    # Slice already sorted -> result identical
    assert module_0.sort_third([5, 3, 4, 6, 2, 1, 9, 8, 7]) == [5, 3, 4, 6, 2, 1, 9, 8, 7]

    # Empty list
    assert module_0.sort_third([]) == []

    # Short lists
    assert module_0.sort_third([42]) == [42]
    assert module_0.sort_third([9, 1]) == [9, 1]

    # Negative numbers
    assert module_0.sort_third([-5, 0, 1, -2, 0]) == [-2, 0, 1, -5, 0]

    # Floats
    assert module_0.sort_third([3.5, 1.5, 2.5, 0.5]) == [0.5, 1.5, 2.5, 3.5]

    # Duplicates
    assert module_0.sort_third([3, 1, 1, 3, 1, 2, 2]) == [2, 1, 1, 3, 1, 2, 3]

    # Larger list: only positions ::3 change
    assert module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 8, 7, 3, 5, 4, 6, 2, 1, 9]

    # Input list must not be modified (function works on a copy)
    original = [5, 6, 3, 4, 8, 9, 2]
    result = module_0.sort_third(original)
    assert original == [5, 6, 3, 4, 8, 9, 2]
    assert result == [2, 6, 3, 4, 8, 9, 5]

    # Accepts any iterable (tuple input)
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]

    # Property check against a simple reference implementation
    def _reference(l):
        res = list(l)
        vals = sorted(res[::3])
        for i, v in zip(range(0, len(res), 3), vals):
            res[i] = v
        return res

    samples = [
        [7, 6, 5, 4, 3, 2, 1],
        [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        [3, -1, 0, -3, 2, -2, 1],
        [1],
        [],
    ]
    for s in samples:
        assert module_0.sort_third(s) == _reference(s), f"mismatch for input {s}"

    # Non-slice positions are preserved exactly
    l = [4, 100, -100, 2, 99, -99, 0, 98, -98]
    out = module_0.sort_third(l)
    for i in range(len(l)):
        if i % 3 != 0:
            assert out[i] == l[i]
        else:
            assert out[i] == sorted(l[::3])[i // 3]

# Generated at 2026-11-03 02:09:48.219149
# Unit test for function sort_third
def test_sort_third():
    # Basic case: elements at indices 0, 3, 6, ... are sorted
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([42]) == [42]

    # Two elements (only index 0 is a multiple of 3)
    assert module_0.sort_third([9, 1]) == [9, 1]

    # Exactly four elements: indices 0 and 3 sorted together
    assert module_0.sort_third([4, 2, 1, 3]) == [3, 2, 1, 4]

    # Already sorted at every third position
    assert module_0.sort_third([1, 5, 2, 3, 6, 7, 9, 8]) == [1, 5, 2, 3, 6, 7, 9, 8]

    # Reverse sorted at every third position
    assert module_0.sort_third([9, 0, 0, 5, 0, 0, 1, 0, 0, 7, 0]) == [1, 0, 0, 5, 0, 0, 7, 0, 0, 9, 0]

    # Negative numbers and duplicates
    assert module_0.sort_third([-1, -2, -3, -1, -2, -3]) == [-1, -2, -3, -1, -2, -3]
    assert module_0.sort_third([3, 3, 3, 1, 1, 1, 2, 2, 2]) == [1, 3, 3, 2, 1, 1, 3, 2, 2]

    # Non-multiple-of-3 indices must be unchanged
    original = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
    result = module_0.sort_third(original)
    assert result[1] == 1 and result[2] == 2
    assert result[4] == 4 and result[5] == 5
    assert result[7] == 7 and result[8] == 8
    assert result[10] == 11 and result[11] == 12
    # Indices 0, 3, 6, 9 are sorted: [3, 6, 9, 10]
    assert result[0] == 3 and result[3] == 6 and result[6] == 9 and result[9] == 10

    # Original list must not be modified
    original = [5, 6, 3, 4, 8, 9, 2]
    _ = module_0.sort_third(original)
    assert original == [5, 6, 3, 4, 8, 9, 2]

    # Result is a new list object
    original = [1, 2, 3]
    result = module_0.sort_third(original)
    assert result is not original

    # Works with tuples as input (any iterable)
    assert module_0.sort_third((3, 2, 1, 2, 1, 3)) == [2, 2, 1, 3, 1, 3]

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-03 02:10:32.355147
# Unit test for function sort_third
def test_sort_third():
    # Basic case: elements at indices 0, 3, 6, ... are sorted
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2, 1]) == [2, 6, 3, 4, 8, 9, 5, 1]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2, 1, 0]) == [2, 6, 3, 4, 8, 9, 5, 1, 0]

    # Empty and single-element lists
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([10]) == [10]

    # Two elements: only index 0 is in the slice, no reordering possible
    assert module_0.sort_third([3, 1]) == [3, 1]

    # Negative numbers
    assert module_0.sort_third([-5, 1, 2, -3, 4]) == [-5, 1, 2, -3, 4]
    assert module_0.sort_third([3, 0, 0, 1, 0, 0, 2, 0, 0]) == [1, 0, 0, 2, 0, 0, 3, 0, 0]

    # Duplicates
    assert module_0.sort_third([2, 2, 2, 1, 1, 1]) == [1, 2, 2, 2, 1, 1]

    # Input list must not be mutated
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert result is not original

    # Accepts any iterable (e.g., tuple) and returns a list
    assert module_0.sort_third((3, 2, 1, 2, 1, 3)) == [2, 2, 1, 3, 1, 3]
    assert isinstance(module_0.sort_third((1, 2, 3)), list)

    # Longer list with already/needs sorting mixed
    assert module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [3, 8, 7, 6, 5, 4, 9, 2, 1, 0]

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-03 02:12:19.057069
# Unit test for function sort_third
def test_sort_third():
    # Elements at indices 0, 3, 6, ... are sorted; others unchanged
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Duplicates
    assert module_0.sort_third([3, 1, 2, 3, 1, 2, 3]) == [3, 1, 2, 3, 1, 2, 3]
    assert module_0.sort_third([4, 4, 4, 1, 1, 1, 2, 2, 2]) == [1, 4, 4, 2, 1, 1, 4, 2, 2]

    # Negative numbers
    assert module_0.sort_third([-5, -1, -3, -2, -4]) == [-5, -1, -2, -3, -4]

    # Edge cases
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([7]) == [7]
    assert module_0.sort_third([2, 1]) == [2, 1]
    assert module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 8, 7, 6, 5, 4, 9, 2, 1]

    # Original list must not be modified
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [2, 6, 3, 4, 8, 9, 5]
    assert result is not original

    # Works with tuples as input
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-03 02:13:32.481623
# Unit test for function sort_third
def test_sort_third():
    # Every third element (indices 0, 3, 6, ...) sorted, others unchanged
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4]) == [4, 6, 3, 5]
    assert module_0.sort_third([5, 6, 7, 4, 5, 6]) == [4, 6, 7, 5, 5, 6]
    assert module_0.sort_third([5, 3, 4, 1, 2, 6, 9, 8, 7]) == [1, 3, 4, 5, 2, 6, 7, 8, 9]

    # Edge cases
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([42]) == [42]
    assert module_0.sort_third([3, 1]) == [3, 1]

    # Duplicates and negatives
    assert module_0.sort_third([2, 2, 2, 1, 1, 1]) == [1, 2, 2, 2, 1, 1]
    assert module_0.sort_third([-3, 0, 5, -1, 4, -2]) == [-3, 0, 5, -1, 4, -2]
    assert module_0.sort_third([9, 1, 1, 3, 1, 1, 6, 1, 1]) == [3, 1, 1, 6, 1, 1, 9, 1, 1]

    # Input list must not be mutated
    original = [5, 6, 3, 4]
    copy = list(original)
    result = module_0.sort_third(original)
    assert original == copy
    assert result == [4, 6, 3, 5]

    # Works with tuples as input (list-like iterables)
    assert module_0.sort_third((5, 6, 3, 4)) == [4, 6, 3, 5]

    # Long list sanity check
    lst = list(range(10, 0, -1))
    expected = lst[:]
    expected[::3] = sorted(expected[::3])
    assert module_0.sort_third(lst) == expected

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()