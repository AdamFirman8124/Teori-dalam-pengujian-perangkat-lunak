

# Generated at 2026-10-25 10:53:24.356588
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

# Generated at 2026-10-25 10:53:40.882182
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

# Generated at 2026-10-25 10:53:58.966518
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

# Generated at 2026-10-25 10:54:17.090179
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

# Generated at 2026-10-25 10:54:33.680348
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