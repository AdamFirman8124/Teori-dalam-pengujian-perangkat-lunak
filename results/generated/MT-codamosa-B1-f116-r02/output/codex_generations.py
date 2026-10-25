

# Generated at 2026-10-24 12:01:35.392646
# Unit test for function sort_array
def test_sort_array():
    # empty and single element
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([1]) == [1]
    assert module_0.sort_array([0]) == [0]

    # sorts by number of 1-bits: 1=1, 2=10, 4=100 -> 1 bit, 3=11 -> 2 bits

# Generated at 2026-10-24 12:01:46.206430
# Unit test for function sort_array
def test_sort_array():
    # empty and single
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]

    # ties keep ascending numeric order (stable sort)
    assert module_0.sort_array([3, 1, 2, 4]) == [1, 2, 4, 3]
    assert module_0.sort_array([5, 3, 6, 2]) == [2, 3, 5, 6]

    # primary key is popcount
    assert module_0.sort_array([7, 1]) == [1, 7]
    assert module_0.sort_array([8, 3]) == [8, 3]

    # duplicates preserved
    assert module_0.sort_array([1, 1, 2]) == [1, 1, 2]

    # input not mutated
    arr = [4, 2, 1]
    module_0.sort_array(arr)
    assert arr == [4, 2, 1]

    # negatives: bin(-5) -> '-0b101' -> 'b101' -> 2 ones
    assert module_0.sort_array([-5, 1]) == [1, -5]


@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([6, 5, 3], [3, 5, 6]),
    ([10, 100, 1000, 10000], [10, 100, 1000, 10000]),
    ([0, 1, 2, 3], [0, 1, 2, 3]),
])
def test_sort_array_parametrized(arr, expected):
    assert module_0.sort_array(arr) == expected

# Generated at 2026-10-24 12:01:47.554582
# Unit test for function sort_array
def test_sort_array():
    # empty and single
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]

    # ties keep ascending numeric order (stable sort)
    assert module_0.sort_array([3, 1, 2, 4]) == [1, 2, 4, 3]
    assert module_0.sort_array([5, 3, 6, 2]) == [2, 3, 5, 6]

    # primary key is popcount
    assert module_0.sort_array([7, 1]) == [1, 7]
    assert module_0.sort_array([8, 3]) == [8, 3]

    # duplicates preserved
    assert module_0.sort_array([1, 1, 2]) == [1, 1, 2]

    # input not mutated
    arr = [4, 2, 1]
    module_0.sort_array(arr)
    assert arr == [4, 2, 1]

    # negatives: bin(-5) -> '-0b101' -> 'b101' -> 2 ones
    assert module_0.sort_array([-5, 1]) == [1, -5]


@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([6, 5, 3], [3, 5, 6]),
    ([10, 100, 1000, 10000], [10, 100, 1000, 10000]),
    ([0, 1, 2, 3], [0, 1, 2, 3]),
])
def test_sort_array_parametrized(arr, expected):
    assert module_0.sort_array(arr) == expected

# Generated at 2026-10-24 12:01:48.888405
# Unit test for function sort_array
def test_sort_array():
    # empty and single
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]

    # ties keep ascending numeric order (stable sort)
    assert module_0.sort_array([3, 1, 2, 4]) == [1, 2, 4, 3]
    assert module_0.sort_array([5, 3, 6, 2]) == [2, 3, 5, 6]

    # primary key is popcount
    assert module_0.sort_array([7, 1]) == [1, 7]
    assert module_0.sort_array([8, 3]) == [8, 3]

    # duplicates preserved
    assert module_0.sort_array([1, 1, 2]) == [1, 1, 2]

    # input not mutated
    arr = [4, 2, 1]
    module_0.sort_array(arr)
    assert arr == [4, 2, 1]

    # negatives: bin(-5) -> '-0b101' -> 'b101' -> 2 ones
    assert module_0.sort_array([-5, 1]) == [1, -5]


@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([6, 5, 3], [3, 5, 6]),
    ([10, 100, 1000, 10000], [10, 100, 1000, 10000]),
    ([0, 1, 2, 3], [0, 1, 2, 3]),
])
def test_sort_array_parametrized(arr, expected):
    assert module_0.sort_array(arr) == expected

# Generated at 2026-10-24 12:01:50.204761
# Unit test for function sort_array
def test_sort_array():
    # empty and single
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([7]) == [7]

    # ties keep ascending numeric order (stable sort)
    assert module_0.sort_array([3, 1, 2, 4]) == [1, 2, 4, 3]
    assert module_0.sort_array([5, 3, 6, 2]) == [2, 3, 5, 6]

    # primary key is popcount
    assert module_0.sort_array([7, 1]) == [1, 7]
    assert module_0.sort_array([8, 3]) == [8, 3]

    # duplicates preserved
    assert module_0.sort_array([1, 1, 2]) == [1, 1, 2]

    # input not mutated
    arr = [4, 2, 1]
    module_0.sort_array(arr)
    assert arr == [4, 2, 1]

    # negatives: bin(-5) -> '-0b101' -> 'b101' -> 2 ones
    assert module_0.sort_array([-5, 1]) == [1, -5]


@pytest.mark.parametrize("arr,expected", [
    ([1, 2, 3], [1, 2, 3]),
    ([6, 5, 3], [3, 5, 6]),
    ([10, 100, 1000, 10000], [10, 100, 1000, 10000]),
    ([0, 1, 2, 3], [0, 1, 2, 3]),
])
def test_sort_array_parametrized(arr, expected):
    assert module_0.sort_array(arr) == expected