

# Generated at 2026-10-25 06:18:30.398915
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

# Generated at 2026-10-25 06:18:32.814333
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:35.229155
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:37.686980
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:40.091883
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:42.506780
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:45.032945
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:47.430375
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:49.848174
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:52.261359
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:54.677637
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:57.091582
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:18:59.494556
# Unit test for function will_it_fly

# Generated at 2026-10-25 06:19:10.514417
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

# Generated at 2026-10-25 06:19:11.980229
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

# Generated at 2026-10-25 06:19:13.415754
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

# Generated at 2026-10-25 06:19:14.743933
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

# Generated at 2026-10-25 06:19:16.105519
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

# Generated at 2026-10-25 06:19:17.578642
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

# Generated at 2026-10-25 06:19:19.028613
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

# Generated at 2026-10-25 06:19:20.386629
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

# Generated at 2026-10-25 06:19:21.904521
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

# Generated at 2026-10-25 06:19:23.304193
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