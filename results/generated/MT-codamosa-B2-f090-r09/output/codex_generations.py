

# Generated at 2026-10-24 21:36:22.909183
# Unit test for function next_smallest

# Generated at 2026-10-24 21:36:27.009164
# Unit test for function next_smallest
def test_next_smallest():assert module_0.next_smallest([1, 2, 3, 4]) == 2

# Generated at 2026-10-24 21:36:28.334226
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

# Generated at 2026-10-24 21:36:29.668435
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

# Generated at 2026-10-24 21:36:31.013727
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

# Generated at 2026-10-24 21:36:32.347842
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