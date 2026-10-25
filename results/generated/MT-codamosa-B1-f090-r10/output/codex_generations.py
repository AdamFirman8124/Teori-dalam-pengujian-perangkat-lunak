

# Generated at 2026-10-25 03:50:11.874912
# Unit test for function next_smallest

# Generated at 2026-10-25 03:50:14.289818
# Unit test for function next_smallest

# Generated at 2026-10-25 03:50:16.707618
# Unit test for function next_smallest

# Generated at 2026-10-25 03:50:19.119385
# Unit test for function next_smallest

# Generated at 2026-10-25 03:50:21.535395
# Unit test for function next_smallest

# Generated at 2026-10-25 03:50:23.951385
# Unit test for function next_smallest

# Generated at 2026-10-25 03:50:30.017309
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4]) == 2
    assert module_0.next_smallest([5, 1, 3, 2]) == 2
    assert module_0.next_smallest([1, 1, 2, 2]) == 2
    assert module_0.next_smallest([-1, -3, -2]) == -2
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([4, 4, 4]) is None
    assert module_0.next_smallest([]) is None

# Generated at 2026-10-25 03:50:34.525644
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 2, 3]) == 2
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([-5, -2, -3, -5]) == -3
    assert module_0.next_smallest([10, 10]) is None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([]) is None

# Generated at 2026-10-25 03:50:39.246583
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([3, 1, 2]) == 2
    assert module_0.next_smallest([1, 1, 2, 3]) == 2
    assert module_0.next_smallest([5, 5, 5]) is None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([-1, -3, -2]) == -2
    assert module_0.next_smallest([2, 2, 1, 1]) == 2