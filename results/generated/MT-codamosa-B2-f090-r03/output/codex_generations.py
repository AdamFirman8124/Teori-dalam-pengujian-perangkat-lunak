

# Generated at 2026-10-24 15:22:00.342022
# Unit test for function next_smallest

# Generated at 2026-10-24 15:22:02.757941
# Unit test for function next_smallest

# Generated at 2026-10-24 15:22:05.167119
# Unit test for function next_smallest

# Generated at 2026-10-24 15:22:07.582087
# Unit test for function next_smallest

# Generated at 2026-10-24 15:22:09.994096
# Unit test for function next_smallest

# Generated at 2026-10-24 15:22:20.782463
# Unit test for function next_smallest
def test_next_smallest():assert module_0.next_smallest([3, 1, 2]) == 2

# Generated at 2026-10-24 15:22:22.177982
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

# Generated at 2026-10-24 15:22:23.627124
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

# Generated at 2026-10-24 15:22:25.087906
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