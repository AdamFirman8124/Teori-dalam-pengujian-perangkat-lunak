

# Generated at 2026-10-24 13:52:23.194783
# Unit test for function sort_even
def test_sort_even():
    # empty and single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # even length
    assert module_0.sort_even([2, 1]) == [2, 1]
    assert module_0.sort_even([5, 2, 4, 1, 3, 0]) == [3, 2, 4, 1, 5, 0]

    # odd length - last even-index element is max after sort
    assert module_0.sort_even([3, 2, 1]) == [1, 2, 3]
    assert module_0.sort_even([4, 1, 3, 2, 5]) == [3, 1, 4, 2, 5]

    # already sorted on even indices stays same
    assert module_0.sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    # odd indices stay in place, even indices get sorted
    assert module_0.sort_even([9, 0, 8, 1, 7, 2]) == [7, 0, 8, 1, 9, 2]

    # duplicates
    assert module_0.sort_even([3, 1, 3, 1, 2, 1]) == [2, 1, 3, 1, 3, 1]

    # negatives
    assert module_0.sort_even([0, -1, -2, -3, 5, 10]) == [-2, -1, 0, -3, 5, 10]

# Generated at 2026-10-24 13:52:24.555773
# Unit test for function sort_even
def test_sort_even():
    # empty and single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # even length
    assert module_0.sort_even([2, 1]) == [2, 1]
    assert module_0.sort_even([5, 2, 4, 1, 3, 0]) == [3, 2, 4, 1, 5, 0]

    # odd length - last even-index element is max after sort
    assert module_0.sort_even([3, 2, 1]) == [1, 2, 3]
    assert module_0.sort_even([4, 1, 3, 2, 5]) == [3, 1, 4, 2, 5]

    # already sorted on even indices stays same
    assert module_0.sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    # odd indices stay in place, even indices get sorted
    assert module_0.sort_even([9, 0, 8, 1, 7, 2]) == [7, 0, 8, 1, 9, 2]

    # duplicates
    assert module_0.sort_even([3, 1, 3, 1, 2, 1]) == [2, 1, 3, 1, 3, 1]

    # negatives
    assert module_0.sort_even([0, -1, -2, -3, 5, 10]) == [-2, -1, 0, -3, 5, 10]

# Generated at 2026-10-24 13:52:25.902777
# Unit test for function sort_even
def test_sort_even():
    # empty and single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # even length
    assert module_0.sort_even([2, 1]) == [2, 1]
    assert module_0.sort_even([5, 2, 4, 1, 3, 0]) == [3, 2, 4, 1, 5, 0]

    # odd length - last even-index element is max after sort
    assert module_0.sort_even([3, 2, 1]) == [1, 2, 3]
    assert module_0.sort_even([4, 1, 3, 2, 5]) == [3, 1, 4, 2, 5]

    # already sorted on even indices stays same
    assert module_0.sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    # odd indices stay in place, even indices get sorted
    assert module_0.sort_even([9, 0, 8, 1, 7, 2]) == [7, 0, 8, 1, 9, 2]

    # duplicates
    assert module_0.sort_even([3, 1, 3, 1, 2, 1]) == [2, 1, 3, 1, 3, 1]

    # negatives
    assert module_0.sort_even([0, -1, -2, -3, 5, 10]) == [-2, -1, 0, -3, 5, 10]

# Generated at 2026-10-24 13:52:27.249545
# Unit test for function sort_even
def test_sort_even():
    # empty and single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # even length
    assert module_0.sort_even([2, 1]) == [2, 1]
    assert module_0.sort_even([5, 2, 4, 1, 3, 0]) == [3, 2, 4, 1, 5, 0]

    # odd length - last even-index element is max after sort
    assert module_0.sort_even([3, 2, 1]) == [1, 2, 3]
    assert module_0.sort_even([4, 1, 3, 2, 5]) == [3, 1, 4, 2, 5]

    # already sorted on even indices stays same
    assert module_0.sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    # odd indices stay in place, even indices get sorted
    assert module_0.sort_even([9, 0, 8, 1, 7, 2]) == [7, 0, 8, 1, 9, 2]

    # duplicates
    assert module_0.sort_even([3, 1, 3, 1, 2, 1]) == [2, 1, 3, 1, 3, 1]

    # negatives
    assert module_0.sort_even([0, -1, -2, -3, 5, 10]) == [-2, -1, 0, -3, 5, 10]

# Generated at 2026-10-24 13:52:28.608428
# Unit test for function sort_even
def test_sort_even():
    # empty and single element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # even length
    assert module_0.sort_even([2, 1]) == [2, 1]
    assert module_0.sort_even([5, 2, 4, 1, 3, 0]) == [3, 2, 4, 1, 5, 0]

    # odd length - last even-index element is max after sort
    assert module_0.sort_even([3, 2, 1]) == [1, 2, 3]
    assert module_0.sort_even([4, 1, 3, 2, 5]) == [3, 1, 4, 2, 5]

    # already sorted on even indices stays same
    assert module_0.sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]

    # odd indices stay in place, even indices get sorted
    assert module_0.sort_even([9, 0, 8, 1, 7, 2]) == [7, 0, 8, 1, 9, 2]

    # duplicates
    assert module_0.sort_even([3, 1, 3, 1, 2, 1]) == [2, 1, 3, 1, 3, 1]

    # negatives
    assert module_0.sort_even([0, -1, -2, -3, 5, 10]) == [-2, -1, 0, -3, 5, 10]