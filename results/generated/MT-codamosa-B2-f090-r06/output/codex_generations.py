

# Generated at 2026-10-25 03:26:07.006130
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4]) == 2
    assert module_0.next_smallest([5, 1, 3, 2, 4]) == 2
    assert module_0.next_smallest([1, 1, 2, 2]) == 2
    assert module_0.next_smallest([-1, -5, -3]) == -3
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([7, 7, 7]) is None
    assert module_0.next_smallest([]) is None

# Generated at 2026-10-25 03:26:11.733796
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4]) == 2
    assert module_0.next_smallest([4, 2, 1, 3]) == 2
    assert module_0.next_smallest([1, 1, 2, 3]) == 2
    assert module_0.next_smallest([-5, -2, -10, 0]) == -5
    assert module_0.next_smallest([1]) is None
    assert module_0.next_smallest([7, 7, 7]) is None
    assert module_0.next_smallest([]) is None

# Generated at 2026-10-25 03:26:15.742859
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 3, 2, 4]) == 2
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([-5, -1, -3]) == -3
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([7, 7, 7]) is None
    assert module_0.next_smallest([]) is None

# Generated at 2026-10-25 03:26:20.845026
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3
    assert module_0.next_smallest([1]) is None
    assert module_0.next_smallest([1, 1, 1]) is None
    assert module_0.next_smallest([]) is None

# Generated at 2026-10-25 03:26:25.775263
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([2, 2, 3, 3, 1]) == 2
    assert module_0.next_smallest([-1, -5, -3]) == -3
    assert module_0.next_smallest([1, 1, 1]) is None
    assert module_0.next_smallest([1]) is None
    assert module_0.next_smallest([]) is None