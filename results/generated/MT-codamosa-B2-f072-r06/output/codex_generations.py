

# Generated at 2026-10-24 22:01:35.575508
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 4) is True       # Palindrome, exact weight
    assert module_0.will_it_fly([1, 2, 1], 3) is False      # Too heavy
    assert module_0.will_it_fly([1, 2, 3], 10) is False     # Not a palindrome
    assert module_0.will_it_fly([1, 2, 2, 1], 6) is True    # Even-length palindrome
    assert module_0.will_it_fly([5], 5) is True             # Single element
    assert module_0.will_it_fly([5], 4) is False            # Single element, too heavy
    assert module_0.will_it_fly([], 0) is True              # Empty list

# Generated at 2026-10-24 22:01:48.783006
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome with sum below or equal to the limit
    assert module_0.will_it_fly([1, 2, 1], 5) is True
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome whose sum exceeds the limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Sum is valid, but the list is not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element and empty lists
    assert module_0.will_it_fly([5], 5) is True
    assert module_0.will_it_fly([5], 4) is False
    assert module_0.will_it_fly([], 0) is True

# Generated at 2026-10-24 22:01:54.518131
# Unit test for function will_it_fly
def test_will_it_fly():
    assert module_0.will_it_fly([1, 2, 1], 4) is True       # Palindrome, exact weight
    assert module_0.will_it_fly([1, 2, 1], 3) is False      # Exceeds weight
    assert module_0.will_it_fly([1, 2, 3], 10) is False     # Not a palindrome
    assert module_0.will_it_fly([5], 5) is True             # Single element
    assert module_0.will_it_fly([], 0) is True               # Empty list
    assert module_0.will_it_fly([1, 2, 2, 1], 6) is True    # Even-length palindrome

# Generated at 2026-10-24 22:02:00.866831
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome within the weight limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome exceeding the weight limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single element
    assert module_0.will_it_fly([5], 5) is True

    # Empty list
    assert module_0.will_it_fly([], 0) is True

# Generated at 2026-10-24 22:02:06.294395
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome within the weight limit
    assert module_0.will_it_fly([1, 2, 1], 4) is True

    # Palindrome exactly at the weight limit
    assert module_0.will_it_fly([1, 2, 2, 1], 6) is True

    # Palindrome exceeding the weight limit
    assert module_0.will_it_fly([1, 2, 1], 3) is False

    # Not a palindrome, despite being within the limit
    assert module_0.will_it_fly([1, 2, 3], 10) is False

    # Single-element list
    assert module_0.will_it_fly([5], 5) is True
    assert module_0.will_it_fly([5], 4) is False

    # Empty list
    assert module_0.will_it_fly([], 0) is True