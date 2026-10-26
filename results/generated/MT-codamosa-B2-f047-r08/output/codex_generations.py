

# Generated at 2026-10-25 12:53:45.036489
# Unit test for function median
def test_median():
    # odd length
    assert module_0.median([1]) == 1
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([3, 1, 2]) == 2  # unsorted
    assert module_0.median([-5, -1, 0]) == -1

    # even length
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([4, 3, 2, 1]) == 2.5  # unsorted
    assert module_0.median([1, 3]) == 2.0
    assert module_0.median([1.5, 2.5]) == 2.0

    # does not modify input
    data = [3, 1, 2]
    module_0.median(data)
    assert data == [3, 1, 2]

# Generated at 2026-10-25 12:53:50.770914
# Unit test for function median
def test_median():
    # odd length
    assert module_0.median([1]) == 1
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([3, 1, 2]) == 2  # unsorted
    assert module_0.median([-5, -1, 0]) == -1

    # even length
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([4, 3, 2, 1]) == 2.5  # unsorted
    assert module_0.median([1, 3]) == 2.0
    assert module_0.median([1.5, 2.5]) == 2.0

    # does not modify input
    data = [3, 1, 2]
    module_0.median(data)
    assert data == [3, 1, 2]

# Generated at 2026-10-25 12:53:53.187589
# Unit test for function median

# Generated at 2026-10-25 12:53:55.603402
# Unit test for function median

# Generated at 2026-10-25 12:53:58.013710
# Unit test for function median

# Generated at 2026-10-25 12:54:00.701482
# Unit test for function median

# Generated at 2026-10-25 12:54:03.294030
# Unit test for function median

# Generated at 2026-10-25 12:54:05.708128
# Unit test for function median

# Generated at 2026-10-25 12:54:08.119589
# Unit test for function median

# Generated at 2026-10-25 12:54:10.533892
# Unit test for function median

# Generated at 2026-10-25 12:54:12.949135
# Unit test for function median