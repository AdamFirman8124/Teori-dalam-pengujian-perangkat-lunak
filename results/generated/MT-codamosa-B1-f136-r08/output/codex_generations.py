

# Generated at 2026-10-24 11:55:20.049519
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():import pytest

def module_0.largest_smallest_integers(lst):
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


@pytest.mark.parametrize("lst, expected", [
    # mixed: closest-to-zero negative, smallest positive
    ([1, -2, 3, -4], (-2, 1)),
    # only positives -> no negative
    ([1, 2, 3, 4], (None, 1)),
    # only negatives -> no positive
    ([-1, -2, -3, -4], (-1, None)),
    # empty list
    ([], (None, None)),
    # zeros are neither negative nor positive
    ([0], (None, None)),
    ([0, -1, 2, 0], (-1, 2)),
    # duplicates
    ([-5, -5, 5, 5], (-5, 5)),
    # single element each way
    ([-7], (-7, None)),
    ([7], (None, 7)),
])
def test_largest_smallest_integers(lst, expected):
    assert module_0.largest_smallest_integers(lst) == expected

# Generated at 2026-10-24 11:55:22.467373
# Unit test for function largest_smallest_integers

# Generated at 2026-10-24 11:55:33.329878
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():assert module_0.largest_smallest_integers([1, 2, -1, -2, 0]) == (-1, 1)

# Generated at 2026-10-24 11:55:34.713737
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():import pytest

def module_0.largest_smallest_integers(lst):
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


@pytest.mark.parametrize("lst, expected", [
    # mixed: closest-to-zero negative, smallest positive
    ([1, -2, 3, -4], (-2, 1)),
    # only positives -> no negative
    ([1, 2, 3, 4], (None, 1)),
    # only negatives -> no positive
    ([-1, -2, -3, -4], (-1, None)),
    # empty list
    ([], (None, None)),
    # zeros are neither negative nor positive
    ([0], (None, None)),
    ([0, -1, 2, 0], (-1, 2)),
    # duplicates
    ([-5, -5, 5, 5], (-5, 5)),
    # single element each way
    ([-7], (-7, None)),
    ([7], (None, 7)),
])
def test_largest_smallest_integers(lst, expected):
    assert module_0.largest_smallest_integers(lst) == expected

# Generated at 2026-10-24 11:55:36.330475
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():import pytest

def module_0.largest_smallest_integers(lst):
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


@pytest.mark.parametrize("lst, expected", [
    # mixed: closest-to-zero negative, smallest positive
    ([1, -2, 3, -4], (-2, 1)),
    # only positives -> no negative
    ([1, 2, 3, 4], (None, 1)),
    # only negatives -> no positive
    ([-1, -2, -3, -4], (-1, None)),
    # empty list
    ([], (None, None)),
    # zeros are neither negative nor positive
    ([0], (None, None)),
    ([0, -1, 2, 0], (-1, 2)),
    # duplicates
    ([-5, -5, 5, 5], (-5, 5)),
    # single element each way
    ([-7], (-7, None)),
    ([7], (None, 7)),
])
def test_largest_smallest_integers(lst, expected):
    assert module_0.largest_smallest_integers(lst) == expected

# Generated at 2026-10-24 11:55:37.710272
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():import pytest

def module_0.largest_smallest_integers(lst):
    smallest = list(filter(lambda x: x < 0, lst))
    largest = list(filter(lambda x: x > 0, lst))
    return (max(smallest) if smallest else None, min(largest) if largest else None)


@pytest.mark.parametrize("lst, expected", [
    # mixed: closest-to-zero negative, smallest positive
    ([1, -2, 3, -4], (-2, 1)),
    # only positives -> no negative
    ([1, 2, 3, 4], (None, 1)),
    # only negatives -> no positive
    ([-1, -2, -3, -4], (-1, None)),
    # empty list
    ([], (None, None)),
    # zeros are neither negative nor positive
    ([0], (None, None)),
    ([0, -1, 2, 0], (-1, 2)),
    # duplicates
    ([-5, -5, 5, 5], (-5, 5)),
    # single element each way
    ([-7], (-7, None)),
    ([7], (None, 7)),
])
def test_largest_smallest_integers(lst, expected):
    assert module_0.largest_smallest_integers(lst) == expected