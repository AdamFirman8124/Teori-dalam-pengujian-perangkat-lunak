

# Generated at 2026-10-24 05:50:31.425791
# Unit test for function sort_array
def test_sort_array():
    # Empty array -> empty
    assert module_0.sort_array([]) == []

    # Single element -> same array
    assert module_0.sort_array([5]) == [5]

    # Sum even -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7 odd? no wait

    # (2+5)=7 odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # (2+6)=8 even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 6]) == [6, 4, 3, 2, 1, 0]

    # (1+3)=4 even -> descending
    assert module_0.sort_array([1, 3]) == [3, 1]

    # (1+2)=3 odd -> ascending
    assert module_0.sort_array([2, 1]) == [1, 2]

    # Duplicates
    assert module_0.sort_array([3, 3, 1, 1]) == [3, 3, 1, 1]   # 3+1=4 even -> descending
    assert module_0.sort_array([1, 1, 2, 2]) == [1, 1, 2, 2]   # 1+2=3 odd -> ascending

    # Negatives
    assert module_0.sort_array([-2, -1, 0, 1]) == [1, 0, -1, -2]   # -2+1=-1, (-1)%2=1 odd -> ascending? check

    print("All tests passed!")

# Generated at 2026-10-24 05:50:32.843547
# Unit test for function sort_array
def test_sort_array():
    # Empty array -> empty
    assert module_0.sort_array([]) == []

    # Single element -> same array
    assert module_0.sort_array([5]) == [5]

    # Sum even -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7 odd? no wait

    # (2+5)=7 odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # (2+6)=8 even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 6]) == [6, 4, 3, 2, 1, 0]

    # (1+3)=4 even -> descending
    assert module_0.sort_array([1, 3]) == [3, 1]

    # (1+2)=3 odd -> ascending
    assert module_0.sort_array([2, 1]) == [1, 2]

    # Duplicates
    assert module_0.sort_array([3, 3, 1, 1]) == [3, 3, 1, 1]   # 3+1=4 even -> descending
    assert module_0.sort_array([1, 1, 2, 2]) == [1, 1, 2, 2]   # 1+2=3 odd -> ascending

    # Negatives
    assert module_0.sort_array([-2, -1, 0, 1]) == [1, 0, -1, -2]   # -2+1=-1, (-1)%2=1 odd -> ascending? check

    print("All tests passed!")

# Generated at 2026-10-24 05:50:35.099220
# Unit test for function sort_array
def test_sort_array():
    # Empty array -> empty
    assert module_0.sort_array([]) == []

    # Single element -> same array
    assert module_0.sort_array([5]) == [5]

    # Sum even -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7 odd? no wait

    # (2+5)=7 odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # (2+6)=8 even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 6]) == [6, 4, 3, 2, 1, 0]

    # (1+3)=4 even -> descending
    assert module_0.sort_array([1, 3]) == [3, 1]

    # (1+2)=3 odd -> ascending
    assert module_0.sort_array([2, 1]) == [1, 2]

    # Duplicates
    assert module_0.sort_array([3, 3, 1, 1]) == [3, 3, 1, 1]   # 3+1=4 even -> descending
    assert module_0.sort_array([1, 1, 2, 2]) == [1, 1, 2, 2]   # 1+2=3 odd -> ascending

    # Negatives
    assert module_0.sort_array([-2, -1, 0, 1]) == [1, 0, -1, -2]   # -2+1=-1, (-1)%2=1 odd -> ascending? check

    print("All tests passed!")

# Generated at 2026-10-24 05:50:36.528202
# Unit test for function sort_array
def test_sort_array():
    # Empty array -> empty
    assert module_0.sort_array([]) == []

    # Single element -> same array
    assert module_0.sort_array([5]) == [5]

    # Sum even -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7 odd? no wait

    # (2+5)=7 odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # (2+6)=8 even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 6]) == [6, 4, 3, 2, 1, 0]

    # (1+3)=4 even -> descending
    assert module_0.sort_array([1, 3]) == [3, 1]

    # (1+2)=3 odd -> ascending
    assert module_0.sort_array([2, 1]) == [1, 2]

    # Duplicates
    assert module_0.sort_array([3, 3, 1, 1]) == [3, 3, 1, 1]   # 3+1=4 even -> descending
    assert module_0.sort_array([1, 1, 2, 2]) == [1, 1, 2, 2]   # 1+2=3 odd -> ascending

    # Negatives
    assert module_0.sort_array([-2, -1, 0, 1]) == [1, 0, -1, -2]   # -2+1=-1, (-1)%2=1 odd -> ascending? check

    print("All tests passed!")

# Generated at 2026-10-24 05:50:37.962856
# Unit test for function sort_array
def test_sort_array():
    # Empty array -> empty
    assert module_0.sort_array([]) == []

    # Single element -> same array
    assert module_0.sort_array([5]) == [5]

    # Sum even -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2+5=7 odd? no wait

    # (2+5)=7 odd -> ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]

    # (2+6)=8 even -> descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 6]) == [6, 4, 3, 2, 1, 0]

    # (1+3)=4 even -> descending
    assert module_0.sort_array([1, 3]) == [3, 1]

    # (1+2)=3 odd -> ascending
    assert module_0.sort_array([2, 1]) == [1, 2]

    # Duplicates
    assert module_0.sort_array([3, 3, 1, 1]) == [3, 3, 1, 1]   # 3+1=4 even -> descending
    assert module_0.sort_array([1, 1, 2, 2]) == [1, 1, 2, 2]   # 1+2=3 odd -> ascending

    # Negatives
    assert module_0.sort_array([-2, -1, 0, 1]) == [1, 0, -1, -2]   # -2+1=-1, (-1)%2=1 odd -> ascending? check

    print("All tests passed!")