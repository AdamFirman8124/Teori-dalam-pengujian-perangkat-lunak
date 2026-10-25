

# Generated at 2026-10-24 12:00:30.120064
# Unit test for function sort_array
def test_sort_array():
    # sum of first + last is odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]      # 2+5=7 odd
    # sum of first + last is even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 even
    assert module_0.sort_array([1, 3, 5]) == [5, 3, 1]                        # 1+5=6 even
    # single element (first == last, sum even -> reversed, same result)
    assert module_0.sort_array([5]) == [5]
    # empty array
    assert module_0.sort_array([]) == []
    # duplicates
    assert module_0.sort_array([3, 3, 1, 2]) == [1, 2, 3, 3]                  # 3+2=5 odd
    # original array is not mutated
    original = [2, 4, 3, 0, 1, 5]
    module_0.sort_array(original)
    assert original == [2, 4, 3, 0, 1, 5]
    print("All tests passed!")

test_sort_array()

# Generated at 2026-10-24 12:00:32.734675
# Unit test for function sort_array

# Generated at 2026-10-24 12:00:35.152066
# Unit test for function sort_array

# Generated at 2026-10-24 12:00:52.945023
# Unit test for function sort_array
def test_sort_array():assert module_0.sort_array([]) == []

# Generated at 2026-10-24 12:00:54.274730
# Unit test for function sort_array
def test_sort_array():
    # sum of first + last is odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]      # 2+5=7 odd
    # sum of first + last is even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 even
    assert module_0.sort_array([1, 3, 5]) == [5, 3, 1]                        # 1+5=6 even
    # single element (first == last, sum even -> reversed, same result)
    assert module_0.sort_array([5]) == [5]
    # empty array
    assert module_0.sort_array([]) == []
    # duplicates
    assert module_0.sort_array([3, 3, 1, 2]) == [1, 2, 3, 3]                  # 3+2=5 odd
    # original array is not mutated
    original = [2, 4, 3, 0, 1, 5]
    module_0.sort_array(original)
    assert original == [2, 4, 3, 0, 1, 5]
    print("All tests passed!")

test_sort_array()

# Generated at 2026-10-24 12:00:55.852874
# Unit test for function sort_array
def test_sort_array():
    # sum of first + last is odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]      # 2+5=7 odd
    # sum of first + last is even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 even
    assert module_0.sort_array([1, 3, 5]) == [5, 3, 1]                        # 1+5=6 even
    # single element (first == last, sum even -> reversed, same result)
    assert module_0.sort_array([5]) == [5]
    # empty array
    assert module_0.sort_array([]) == []
    # duplicates
    assert module_0.sort_array([3, 3, 1, 2]) == [1, 2, 3, 3]                  # 3+2=5 odd
    # original array is not mutated
    original = [2, 4, 3, 0, 1, 5]
    module_0.sort_array(original)
    assert original == [2, 4, 3, 0, 1, 5]
    print("All tests passed!")

test_sort_array()

# Generated at 2026-10-24 12:00:57.161810
# Unit test for function sort_array
def test_sort_array():
    # sum of first + last is odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]      # 2+5=7 odd
    # sum of first + last is even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2+6=8 even
    assert module_0.sort_array([1, 3, 5]) == [5, 3, 1]                        # 1+5=6 even
    # single element (first == last, sum even -> reversed, same result)
    assert module_0.sort_array([5]) == [5]
    # empty array
    assert module_0.sort_array([]) == []
    # duplicates
    assert module_0.sort_array([3, 3, 1, 2]) == [1, 2, 3, 3]                  # 3+2=5 odd
    # original array is not mutated
    original = [2, 4, 3, 0, 1, 5]
    module_0.sort_array(original)
    assert original == [2, 4, 3, 0, 1, 5]
    print("All tests passed!")

test_sort_array()