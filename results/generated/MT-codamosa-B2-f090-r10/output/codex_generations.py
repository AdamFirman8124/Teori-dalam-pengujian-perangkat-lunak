

# Generated at 2026-10-24 14:06:44.073035
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([1, 1, 1]) is None          # all duplicates -> 1 unique
    assert module_0.next_smallest([1, 1, 2]) == 2             # dupes collapse
    assert module_0.next_smallest([2, 2, 1, 1]) == 2
    assert module_0.next_smallest([]) is None                 # empty
    assert module_0.next_smallest([7]) is None                # single element
    assert module_0.next_smallest([-5, -1, -3]) == -3         # negatives
    assert module_0.next_smallest([0, -1]) == 0               # zero included

# Generated at 2026-10-24 14:06:45.403547
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([1, 1, 1]) is None          # all duplicates -> 1 unique
    assert module_0.next_smallest([1, 1, 2]) == 2             # dupes collapse
    assert module_0.next_smallest([2, 2, 1, 1]) == 2
    assert module_0.next_smallest([]) is None                 # empty
    assert module_0.next_smallest([7]) is None                # single element
    assert module_0.next_smallest([-5, -1, -3]) == -3         # negatives
    assert module_0.next_smallest([0, -1]) == 0               # zero included

# Generated at 2026-10-24 14:06:46.835286
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([1, 1, 1]) is None          # all duplicates -> 1 unique
    assert module_0.next_smallest([1, 1, 2]) == 2             # dupes collapse
    assert module_0.next_smallest([2, 2, 1, 1]) == 2
    assert module_0.next_smallest([]) is None                 # empty
    assert module_0.next_smallest([7]) is None                # single element
    assert module_0.next_smallest([-5, -1, -3]) == -3         # negatives
    assert module_0.next_smallest([0, -1]) == 0               # zero included

# Generated at 2026-10-24 14:06:48.155432
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([1, 1, 1]) is None          # all duplicates -> 1 unique
    assert module_0.next_smallest([1, 1, 2]) == 2             # dupes collapse
    assert module_0.next_smallest([2, 2, 1, 1]) == 2
    assert module_0.next_smallest([]) is None                 # empty
    assert module_0.next_smallest([7]) is None                # single element
    assert module_0.next_smallest([-5, -1, -3]) == -3         # negatives
    assert module_0.next_smallest([0, -1]) == 0               # zero included

# Generated at 2026-10-24 14:06:49.487109
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([1, 1, 1]) is None          # all duplicates -> 1 unique
    assert module_0.next_smallest([1, 1, 2]) == 2             # dupes collapse
    assert module_0.next_smallest([2, 2, 1, 1]) == 2
    assert module_0.next_smallest([]) is None                 # empty
    assert module_0.next_smallest([7]) is None                # single element
    assert module_0.next_smallest([-5, -1, -3]) == -3         # negatives
    assert module_0.next_smallest([0, -1]) == 0               # zero included