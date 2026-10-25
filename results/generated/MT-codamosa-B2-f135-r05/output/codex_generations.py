

# Generated at 2026-10-24 07:33:53.961598
# Unit test for function can_arrange

# Generated at 2026-10-24 07:33:56.379234
# Unit test for function can_arrange

# Generated at 2026-10-24 07:33:58.792888
# Unit test for function can_arrange

# Generated at 2026-10-24 07:34:01.208544
# Unit test for function can_arrange

# Generated at 2026-10-24 07:34:03.621463
# Unit test for function can_arrange

# Generated at 2026-10-24 07:34:06.035888
# Unit test for function can_arrange

# Generated at 2026-10-24 07:34:08.450665
# Unit test for function can_arrange

# Generated at 2026-10-24 07:34:18.681240
# Unit test for function can_arrange
def test_can_arrange():assert module_0.can_arrange([1, 2, 3, 4]) == -1

# Generated at 2026-10-24 07:34:25.586700
# Unit test for function can_arrange
def test_can_arrange():
    # No element smaller than its predecessor -> -1
    assert module_0.can_arrange([1, 2, 3, 4]) == -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([5]) == -1

    # Largest index where arr[i] < arr[i-1]
    assert module_0.can_arrange([1, 2, 4, 3, 5]) == 3
    assert module_0.can_arrange([1, 2, 3, 4, 3]) == 4   # later drop wins over earlier one
    assert module_0.can_arrange([2, 1]) == 1

    # Duplicates count as a drop (strictly less)
    assert module_0.can_arrange([1, 2, 2, 2]) == -1
    assert module_0.can_arrange([1, 2, 2, 1]) == 3

    # Decreasing array -> last index
    assert module_0.can_arrange([5, 4, 3, 2, 1]) == 4

    print("All tests passed.")

test_can_arrange()

# Generated at 2026-10-24 07:35:03.346750
# Unit test for function can_arrange
def test_can_arrange():
    # already sorted -> -1
    assert module_0.can_arrange([]) == -1
    assert module_0.can_arrange([1]) == -1
    assert module_0.can_arrange([1, 2, 3, 4, 5]) == -1
    assert module_0.can_arrange([1, 1, 1, 1]) == -1
    assert module_0.can_arrange([-3, -2, -1, 0]) == -1

    # single descent
    assert module_0.can_arrange([2, 1]) == 1
    assert module_0.can_arrange([1, 3, 2, 4]) == 2
    assert module_0.can_arrange([0, -1]) == 1

    # multiple descents -> returns last index i with arr[i] < arr[i-1]
    assert module_0.can_arrange([4, 3, 2, 1]) == 3
    assert module_0.can_arrange([1, 5, 4, 3, 6]) == 3
    assert module_0.can_arrange([3, 1, 2]) == 1
    assert module_0.can_arrange([1, 2, 5, 3, 4, 0, 6]) == 5