

# Generated at 2026-10-25 07:13:16.827659
# Unit test for function will_it_fly

# Generated at 2026-10-25 07:13:19.245939
# Unit test for function will_it_fly

# Generated at 2026-10-25 07:13:21.660930
# Unit test for function will_it_fly

# Generated at 2026-10-25 07:13:24.075167
# Unit test for function will_it_fly

# Generated at 2026-10-25 07:13:26.491829
# Unit test for function will_it_fly

# Generated at 2026-10-25 07:13:28.906817
# Unit test for function will_it_fly

# Generated at 2026-10-25 07:13:31.441781
# Unit test for function will_it_fly

# Generated at 2026-10-25 07:13:37.010847
# Unit test for function will_it_fly
def test_will_it_fly():
    # Balanced (palindrome) and light enough -> flies
    assert module_0.will_it_fly([3, 2, 3], 9) is True
    assert module_0.will_it_fly([1, 2], 5) is False      # not a palindrome
    assert module_0.will_it_fly([3, 2, 3], 1) is False   # too heavy (sum=8 > 1)
    assert module_0.will_it_fly([3, 2, 3], 8) is True    # exactly at weight limit
    assert module_0.will_it_fly([5], 5) is True          # single element, palindrome
    assert module_0.will_it_fly([5], 4) is False         # single element too heavy
    assert module_0.will_it_fly([], 10) is True          # empty list: palindrome, sum=0 <= w
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 9) is True   # odd-length palindrome
    assert module_0.will_it_fly([1, 2, 2, 1], 6) is True      # even-length palindrome
    assert module_0.will_it_fly([1, 2, 3, 4, 5], 100) is False  # not a palindrome

# Generated at 2026-10-25 07:13:38.855281
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

# Generated at 2026-10-25 07:13:40.192691
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