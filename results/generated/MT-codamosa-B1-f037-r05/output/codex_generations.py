

# Generated at 2026-10-24 22:17:44.797193
# Unit test for function sort_even
def test_sort_even():
    # Empty / single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([5]) == [5]

    # Even-length: only indices 0, 2, ... are sorted
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert module_0.sort_even([-1, 10, -3, 20]) == [-3, 10, -1, 20]

    # Odd-length: last even-index element is included
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 2, 3]) == [3, 2, 5]
    assert module_0.sort_even([4, 1, 3, 2, 2]) == [2, 1, 3, 2, 4]
    assert module_0.sort_even([10, 9, 8, 7, 6]) == [6, 9, 8, 7, 10]

    # Duplicates
    assert module_0.sort_even([3, 100, 3, 1, 3]) == [3, 100, 3, 1, 3]

    # Original list is not mutated
    data = [5, 2, 3]
    module_0.sort_even(data)
    assert data == [5, 2, 3]

# Generated at 2026-10-24 22:17:46.120849
# Unit test for function sort_even
def test_sort_even():
    # Empty / single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([5]) == [5]

    # Even-length: only indices 0, 2, ... are sorted
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert module_0.sort_even([-1, 10, -3, 20]) == [-3, 10, -1, 20]

    # Odd-length: last even-index element is included
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 2, 3]) == [3, 2, 5]
    assert module_0.sort_even([4, 1, 3, 2, 2]) == [2, 1, 3, 2, 4]
    assert module_0.sort_even([10, 9, 8, 7, 6]) == [6, 9, 8, 7, 10]

    # Duplicates
    assert module_0.sort_even([3, 100, 3, 1, 3]) == [3, 100, 3, 1, 3]

    # Original list is not mutated
    data = [5, 2, 3]
    module_0.sort_even(data)
    assert data == [5, 2, 3]

# Generated at 2026-10-24 22:17:47.440109
# Unit test for function sort_even
def test_sort_even():
    # Empty / single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([5]) == [5]

    # Even-length: only indices 0, 2, ... are sorted
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert module_0.sort_even([-1, 10, -3, 20]) == [-3, 10, -1, 20]

    # Odd-length: last even-index element is included
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 2, 3]) == [3, 2, 5]
    assert module_0.sort_even([4, 1, 3, 2, 2]) == [2, 1, 3, 2, 4]
    assert module_0.sort_even([10, 9, 8, 7, 6]) == [6, 9, 8, 7, 10]

    # Duplicates
    assert module_0.sort_even([3, 100, 3, 1, 3]) == [3, 100, 3, 1, 3]

    # Original list is not mutated
    data = [5, 2, 3]
    module_0.sort_even(data)
    assert data == [5, 2, 3]

# Generated at 2026-10-24 22:17:48.777673
# Unit test for function sort_even
def test_sort_even():
    # Empty / single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([5]) == [5]

    # Even-length: only indices 0, 2, ... are sorted
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert module_0.sort_even([-1, 10, -3, 20]) == [-3, 10, -1, 20]

    # Odd-length: last even-index element is included
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 2, 3]) == [3, 2, 5]
    assert module_0.sort_even([4, 1, 3, 2, 2]) == [2, 1, 3, 2, 4]
    assert module_0.sort_even([10, 9, 8, 7, 6]) == [6, 9, 8, 7, 10]

    # Duplicates
    assert module_0.sort_even([3, 100, 3, 1, 3]) == [3, 100, 3, 1, 3]

    # Original list is not mutated
    data = [5, 2, 3]
    module_0.sort_even(data)
    assert data == [5, 2, 3]

# Generated at 2026-10-24 22:17:50.110743
# Unit test for function sort_even
def test_sort_even():
    # Empty / single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([5]) == [5]

    # Even-length: only indices 0, 2, ... are sorted
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert module_0.sort_even([-1, 10, -3, 20]) == [-3, 10, -1, 20]

    # Odd-length: last even-index element is included
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 2, 3]) == [3, 2, 5]
    assert module_0.sort_even([4, 1, 3, 2, 2]) == [2, 1, 3, 2, 4]
    assert module_0.sort_even([10, 9, 8, 7, 6]) == [6, 9, 8, 7, 10]

    # Duplicates
    assert module_0.sort_even([3, 100, 3, 1, 3]) == [3, 100, 3, 1, 3]

    # Original list is not mutated
    data = [5, 2, 3]
    module_0.sort_even(data)
    assert data == [5, 2, 3]