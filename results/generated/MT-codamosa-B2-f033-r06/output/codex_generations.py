

# Generated at 2026-11-01 20:10:43.958673
# Unit test for function sort_third
def test_sort_third():
    # Every third element (indices 0, 3, 6, ...) should be sorted,
    # while other elements stay in place.

    # No change needed when thirds already sorted
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]

    # Classic example: indices 0,3,6 -> [5,4,2] becomes [2,4,5]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]

    # Non-third positions untouched even if unsorted
    assert module_0.sort_third([5, 3, -2, 1, 0, 9, 8, 7, 6, 4]) == [1, 3, -2, 4, 0, 9, 5, 7, 6, 8]

    # Empty list
    assert module_0.sort_third([]) == []

    # Fewer than three elements: only index 0 participates
    assert module_0.sort_third([10]) == [10]
    assert module_0.sort_third([10, 2]) == [10, 2]

    # Duplicates among every-third elements
    assert module_0.sort_third([3, 1, 1, 3, 1, 1, 1, 1]) == [1, 1, 1, 3, 1, 1, 3, 1]

    # Negative and mixed values
    assert module_0.sort_third([-5, 4, 0, -1, 2, 2, -9, 8]) == [-9, 4, 0, -5, 2, 2, -1, 8]

    # Original input list must not be mutated
    original = [9, 8, 7, 6, 5, 4]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot
    assert result == [6, 8, 7, 9, 5, 4]

    # Works on tuples/other iterables as input
    assert module_0.sort_third((7, 6, 5, 4, 3, 2, 1)) == [1, 6, 5, 4, 3, 2, 7]

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_third()

# Generated at 2026-11-01 20:11:09.866039
# Unit test for function sort_third
def test_sort_third():
    # Basic case: elements at indices 0, 3, 6, ... are sorted
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Empty list
    assert module_0.sort_third([]) == []

    # Short lists (fewer than 3 elements)
    assert module_0.sort_third([2]) == [2]
    assert module_0.sort_third([3, 1]) == [3, 1]

    # Duplicates
    assert module_0.sort_third([4, 4, 4, 4, 4, 4]) == [4, 4, 4, 4, 4, 4]
    assert module_0.sort_third([7, 1, 2, 3, 4, 5]) == [3, 1, 2, 7, 4, 5]

    # Original list must not be modified
    original = [9, 8, 7, 6, 5, 4]
    result = module_0.sort_third(original)
    assert original == [9, 8, 7, 6, 5, 4]
    assert result == [6, 8, 7, 9, 5, 4]
    assert result is not original

    # Elements at other indices remain untouched
    assert module_0.sort_third([10, 1, 2, 0, 5, 8]) == [0, 1, 2, 10, 5, 8]

    print("All tests passed!")

# Generated at 2026-11-01 20:11:26.480799
# Unit test for function sort_third
def test_sort_third():
    # Basic case: sort every third element starting from index 0
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 1, 3, 4, 8, 9, 2, 7]) == [2, 1, 3, 4, 8, 9, 5, 7]

    # Empty list
    assert module_0.sort_third([]) == []

    # Single element
    assert module_0.sort_third([42]) == [42]

    # Two elements (only index 0 is a multiple of 3)
    assert module_0.sort_third([10, 2]) == [10, 2]
    assert module_0.sort_third([10, 1]) == [10, 1]

    # Elements at indices not divisible by 3 remain unchanged
    result = module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert result == [3, 8, 7, 6, 5, 4, 9, 2, 1]
    assert result[1] == 8
    assert result[2] == 7
    assert result[4] == 5
    assert result[5] == 4
    assert result[7] == 2
    assert result[8] == 1

    # Already sorted third positions
    assert module_0.sort_third([1, 100, 200, 2, 300, 400, 3]) == [1, 100, 200, 2, 300, 400, 3]

    # Reverse sorted third positions
    assert module_0.sort_third([9, 0, 0, 6, 0, 0, 3, 0, 0, 1]) == [1, 0, 0, 3, 0, 0, 6, 0, 0, 9]

    # Duplicates
    assert module_0.sort_third([5, 1, 1, 5, 2, 2, 5]) == [5, 1, 1, 5, 2, 2, 5]
    assert module_0.sort_third([3, 1, 1, 2, 2, 2, 1]) == [1, 1, 1, 2, 2, 2, 3]

    # Negative numbers
    assert module_0.sort_third([-3, 0, 0, -1, 0, 0, -2]) == [-3, 0, 0, -2, 0, 0, -1]

    # Floats
    assert module_0.sort_third([2.5, 0, 0, 1.5]) == [1.5, 0, 0, 2.5]

    # Original list is not mutated
    original = [5, 6, 3, 4, 8, 9, 2]
    copy_of_original = list(original)
    _ = module_0.sort_third(original)
    assert original == copy_of_original

    # Input as a tuple works (list() conversion)
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]
    assert isinstance(module_0.sort_third((1, 2, 3)), list)

    # Longer list with varied third-position values
    l = [10, 1, 2, 8, 3, 4, 6, 5, 7, 9]
    assert module_0.sort_third(l) == [6, 1, 2, 8, 3, 4, 9, 5, 7, 10]

# Generated at 2026-11-01 20:11:47.975143
# Unit test for function sort_third
def test_sort_third():
    # Every third element (indices 0, 3, 6, ...) sorted, others unchanged
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Edge cases
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([4]) == [4]
    assert module_0.sort_third([2, 1]) == [2, 1]
    assert module_0.sort_third([1, 2]) == [1, 2]

    # Duplicates among third positions
    assert module_0.sort_third([3, 1, 1, 3, 1, 1, 2, 1, 1]) == [2, 1, 1, 3, 1, 1, 3, 1, 1]

    # Original list must not be mutated; a new list should be returned
    original = [9, 1, 2, 3, 4, 5]
    result = module_0.sort_third(original)
    assert original == [9, 1, 2, 3, 4, 5]
    assert result == [3, 1, 2, 9, 4, 5]
    assert result is not original

    print("All tests passed!")


test_sort_third()

# Generated at 2026-11-01 20:12:22.774618
# Unit test for function sort_third
def test_sort_third():
    # Elements at indices 0, 3, 6, ... are sorted; others stay in place
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == \
        [1, 3, -5, 2, -3, 3, 5, 0, 123, 9, -10]

    # Edge cases
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([42]) == [42]
    assert module_0.sort_third([7, 1]) == [7, 1]  # fewer than 3 elements -> only index 0

    # Two positions among every-third group
    assert module_0.sort_third([9, 5, 5, 1]) == [1, 5, 5, 9]

    # Duplicates
    assert module_0.sort_third([3, 1, 2, 3, 1, 2]) == [3, 1, 2, 3, 1, 2]

    # Negative numbers
    assert module_0.sort_third([-1, -5, 0, -10, 4]) == [-10, -5, 0, -1, 4]


def test_sort_third_does_not_mutate_input():
    original = [5, 6, 3, 4, 8, 9, 2]
    snapshot = list(original)
    result = module_0.sort_third(original)
    assert original == snapshot          # input unchanged
    assert result is not original        # returns a new list


def test_sort_third_accepts_iterables():
    # Function copies its input via list(l), so tuples work too
    assert module_0.sort_third((5, 6, 3, 4, 8, 9, 2)) == [2, 6, 3, 4, 8, 9, 5]


def test_sort_third_long_list():
    lst = [10, 1, 2, 9, 3, 4, 8, 5, 6, 7, 11, 12]
    # Every-third values: 10, 9, 8, 7 -> sorted: 7, 8, 9, 10
    expected = [7, 1, 2, 8, 3, 4, 9, 5, 6, 10, 11, 12]
    assert module_0.sort_third(lst) == expected


test_sort_third()
test_sort_third_does_not_mutate_input()
test_sort_third_accepts_iterables()
test_sort_third_long_list()
print("All tests passed!")