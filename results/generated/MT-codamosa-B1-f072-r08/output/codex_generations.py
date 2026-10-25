

# Generated at 2026-10-24 07:05:45.641383
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome within the weight limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome exactly at the weight limit
    assert module_0.will_it_fly([3, 2, 3], 8) is True

    # Palindrome exceeding the weight limit
    assert module_0.will_it_fly([3, 2, 3], 7) is False

    # Weight is acceptable, but the list is not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element and empty lists
    assert module_0.will_it_fly([5], 5) is True
    assert module_0.will_it_fly([], 0) is True

# Generated at 2026-10-24 07:05:50.292191
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome with sum within the limit
    assert module_0.will_it_fly([1, 2, 1], 5) is True

    # Palindrome with sum equal to the limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome exceeding the limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Sum within the limit, but not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element list
    assert module_0.will_it_fly([5], 5) is True

    # Empty list
    assert module_0.will_it_fly([], 0) is True

# Generated at 2026-10-24 07:05:54.698985
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome within the weight limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome exceeding the weight limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Weight is acceptable, but the list is not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element list
    assert module_0.will_it_fly([5], 5) is True

    # Empty list
    assert module_0.will_it_fly([], 0) is True

# Generated at 2026-10-24 07:06:00.180453
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 4) is True      # Palindrome; sum equals limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False     # Sum exceeds limit
    assert module_0.will_it_fly([1, 2, 3], 10) is False    # Not a palindrome
    assert module_0.will_it_fly([5], 5) is True            # Single element
    assert module_0.will_it_fly([], 0) is True              # Empty list

# Generated at 2026-10-24 07:06:07.348968
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome within the weight limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome exactly at the weight limit
    assert module_0.will_it_fly([3, 2, 3], 8) is True

    # Palindrome exceeding the weight limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Weight is acceptable, but the list is not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element list
    assert module_0.will_it_fly([5], 5) is True
    assert module_0.will_it_fly([5], 4) is False

    # Empty list
    assert module_0.will_it_fly([], 0) is True

# Generated at 2026-10-24 07:06:12.632271
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 5) is True      # Palindrome, within limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True      # Exactly at limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False     # Exceeds limit
    assert module_0.will_it_fly([1, 2, 3], 10) is False    # Not a palindrome
    assert module_0.will_it_fly([5], 5) is True            # Single element
    assert module_0.will_it_fly([], 0) is True             # Empty list

# Generated at 2026-10-24 07:06:18.407640
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 4) is True       # Palindrome within weight
    assert module_0.will_it_fly([1, 2, 1], 3) is False      # Exceeds weight
    assert module_0.will_it_fly([1, 2, 3], 10) is False     # Not a palindrome
    assert module_0.will_it_fly([5], 5) is True             # Single element
    assert module_0.will_it_fly([5], 4) is False            # Single element exceeds weight
    assert module_0.will_it_fly([], 0) is True               # Empty list

# Generated at 2026-10-24 07:06:27.625991
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 4) is True     # Palindrome, sum <= w
    assert module_0.will_it_fly([1, 2, 1], 3) is False    # Sum exceeds w
    assert module_0.will_it_fly([1, 2, 3], 10) is False   # Not a palindrome
    assert module_0.will_it_fly([5], 5) is True           # Single element
    assert module_0.will_it_fly([], 0) is True             # Empty list
    assert module_0.will_it_fly([2, 2], 4) is True         # Sum equals w

# Generated at 2026-10-24 07:06:33.304885
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome within the weight limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome exactly at the weight limit
    assert module_0.will_it_fly([1, 2, 2, 1], 6) is True

    # Palindrome exceeding the weight limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Not a palindrome, despite being within the weight limit
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element list
    assert module_0.will_it_fly([5], 5) is True

# Generated at 2026-10-24 07:06:38.753167
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 4) is True       # Palindrome, exact weight
    assert module_0.will_it_fly([1, 2, 1], 3) is False      # Exceeds weight limit
    assert module_0.will_it_fly([1, 2, 3], 10) is False     # Not a palindrome
    assert module_0.will_it_fly([5], 5) is True             # Single element
    assert module_0.will_it_fly([], 0) is True               # Empty list
    assert module_0.will_it_fly([0, 0, 0], 0) is True       # Zero-weight palindrome

# Generated at 2026-10-24 07:06:45.197453
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 5) is True       # Palindrome, sum <= limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True       # Sum equals limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False      # Sum exceeds limit
    assert module_0.will_it_fly([1, 2, 3], 10) is False     # Not a palindrome
    assert module_0.will_it_fly([5], 5) is True             # Single element
    assert module_0.will_it_fly([5], 4) is False            # Single element exceeds limit
    assert module_0.will_it_fly([], 0) is True               # Empty list

# Generated at 2026-10-24 07:06:51.131373
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome within the weight limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome exactly at the weight limit
    assert module_0.will_it_fly([3, 2, 3], 8) is True

    # Palindrome exceeding the weight limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Within the weight limit but not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element and empty lists
    assert module_0.will_it_fly([5], 5) is True
    assert module_0.will_it_fly([], 0) is True

# Generated at 2026-10-24 07:06:56.091575
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome with sum within the weight limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True
    assert module_0.will_it_fly([3], 3) is True
    assert module_0.will_it_fly([], 0) is True

    # Palindrome exceeding the weight limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False
    assert module_0.will_it_fly([3, 3], 5) is False

    # Non-palindromes
    assert module_0.will_it_fly([1, 2, 3], 10) is False
    assert module_0.will_it_fly([1, 2], 3) is False

# Generated at 2026-10-24 07:07:02.034884
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 4) is True       # Palindrome, within weight
    assert module_0.will_it_fly([1, 2, 1], 3) is False      # Palindrome, overweight
    assert module_0.will_it_fly([1, 2, 3], 10) is False     # Not a palindrome
    assert module_0.will_it_fly([1], 1) is True             # Single element
    assert module_0.will_it_fly([], 0) is True              # Empty list
    assert module_0.will_it_fly([2, 2], 4) is True          # Exactly at weight limit

# Generated at 2026-10-24 07:07:07.971840
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 4) is True      # Palindrome, exact weight
    assert module_0.will_it_fly([1, 2, 1], 5) is True      # Palindrome, below limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False     # Exceeds weight limit
    assert module_0.will_it_fly([1, 2, 3], 10) is False    # Not a palindrome
    assert module_0.will_it_fly([5], 5) is True            # Single-element list
    assert module_0.will_it_fly([], 0) is True              # Empty list