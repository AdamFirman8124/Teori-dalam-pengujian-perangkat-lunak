

# Generated at 2026-10-24 15:05:14.769890
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

# Generated at 2026-10-24 15:05:16.202676
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

# Generated at 2026-10-24 15:05:17.554197
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

# Generated at 2026-10-24 15:05:18.914771
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

# Generated at 2026-10-24 15:05:20.266322
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