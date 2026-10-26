

# Generated at 2026-10-25 14:22:54.936428
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([7]) == 7
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([1, 2, 2, 3]) == 2.0

# Generated at 2026-10-25 14:23:05.601392
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([1]) == 1
    assert module_0.median([1, 2, 3, 4, 5]) == 3
    assert module_0.median([-1, -3, -2]) == -2


if __name__ == "__main__":
    test_median()
    print("All tests passed.")

# Generated at 2026-10-25 14:23:14.556788
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([7]) == 7
    assert module_0.median([5, 1, 9, 3, 7]) == 5
    assert module_0.median([-3, -1, -2]) == -2


def test_median_does_not_modify_original_list():
    numbers = [3, 1, 2]
    module_0.median(numbers)
    assert numbers == [3, 1, 2]


def test_median_empty_list():
    with pytest.raises(IndexError):
        module_0.median([])

# Generated at 2026-10-25 14:23:22.201500
# Unit test for function median
def test_median():
    assert module_0.median([1, 3, 2]) == 2
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([7]) == 7
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([2, 2, 4, 4]) == 3.0

# Generated at 2026-10-25 14:23:28.028341
# Unit test for function median
def test_median():
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([5, 1, 3]) == 3
    assert module_0.median([-5, -1, -3, -2]) == -2.5
    assert module_0.median([7]) == 7
    assert module_0.median([2, 2, 2, 2]) == 2.0