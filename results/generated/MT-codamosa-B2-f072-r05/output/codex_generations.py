

# Generated at 2026-10-25 14:11:28.151974
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome and sum(q) <= w
    assert module_0.will_it_fly([1, 2, 1], 5) == True   # sum=4 <= 5, palindrome
    assert module_0.will_it_fly([1, 2, 1], 4) == True   # sum=4 == w, palindrome
    assert module_0.will_it_fly([3, 2, 3], 9) == True   # sum=8 <= 9, palindrome
    assert module_0.will_it_fly([2, 2], 4) == True      # even-length palindrome
    assert module_0.will_it_fly([5], 5) == True        # single element is palindrome
    assert module_0.will_it_fly([], 0) == True         # sum=0 <= 0, vacuously palindrome

    # False: palindrome but too heavy sum(q) > w
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum=4 > 3
    assert module_0.will_it_fly([3, 2, 3], 7) == False  # sum=8 > 7
    assert module_0.will_it_fly([5], 4) == False        # sum=5 > 4
    assert module_0.will_it_fly([2, 2], 3) == False     # sum=4 > 3

    # False: light enough but not palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) == False # sum=6 <= 10, not palindrome
    assert module_0.will_it_fly([1, 2], 5) == False     # sum=3 <= 5, not palindrome
    assert module_0.will_it_fly([2, 3], 5) == False     # sum=5 <= 5, not palindrome

    # False: both too heavy and not palindrome
    assert module_0.will_it_fly([1, 2, 3], 5) == False  # sum=6 > 5, not palindrome

# Generated at 2026-10-25 14:11:44.126514
# Unit test for function will_it_fly
def test_will_it_fly():import pytest


def module_0.will_it_fly(q, w):
    if sum(q) > w:
        return False

    i, j = 0, len(q) - 1
    while i < j:
        if q[i] != q[j]:
            return False
        i += 1
        j -= 1

    return True


@pytest.mark.parametrize(
    "q, w, expected",
    [
        ([1, 2, 1], 5, True),      # Palindrome and within weight
        ([1, 2, 2, 1], 6, True),    # Even-length palindrome
        ([1, 2, 3], 10, False),    # Not a palindrome
        ([1, 2, 1], 3, False),      # Palindrome but too heavy
        ([5], 5, True),            # Single element, exact weight
        ([5], 4, False),            # Single element, too heavy
        ([], 0, True),             # Empty list
        ([2, 0, 2], 4, True),       # Palindrome with zero
    ],
)
def test_will_it_fly(q, w, expected):
    assert module_0.will_it_fly(q, w) == expected

# Generated at 2026-10-25 14:12:00.713819
# Unit test for function will_it_fly
def test_will_it_fly():
    # True: palindrome, sum <= w
    assert module_0.will_it_fly([1, 2, 1], 4) is True
    assert module_0.will_it_fly([1, 2, 2, 1], 6) is True

    # False: palindrome, sum > w
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # False: not palindrome, sum <= w
    assert module_0.will_it_fly([1, 2, 3], 10) is False
    assert module_0.will_it_fly([1, 2, 3, 1], 10) is False

    # Edge cases
    assert module_0.will_it_fly([], 0) is True
    assert module_0.will_it_fly([5], 5) is True
    assert module_0.will_it_fly([5], 4) is False

    print("All tests passed")

# Generated at 2026-10-25 14:12:22.639714
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome whose sum is within the limit
    assert module_0.will_it_fly([1, 2, 1], 5) is True

    # Palindrome whose sum equals the limit
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 9) is True

    # Sum exceeds the limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Sum is within the limit, but the list is not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element and empty lists
    assert module_0.will_it_fly([5], 5) is True
    assert module_0.will_it_fly([], 0) is True

# Generated at 2026-10-25 14:12:28.423058
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome with sum within the limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome exceeding the weight limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Within the weight limit, but not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element list
    assert module_0.will_it_fly([5], 5) is True

    # Empty list
    assert module_0.will_it_fly([], 0) is True