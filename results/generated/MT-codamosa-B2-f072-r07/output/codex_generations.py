

# Generated at 2026-11-02 16:32:28.884048
# Unit test for function will_it_fly
def test_will_it_fly():
    # Object is balanced (palindrome) and light enough -> True
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([1, 2], 5) == False   # not a palindrome
    assert module_0.will_it_fly([3], 5) == True       # single element, light enough
    assert module_0.will_it_fly([3], 2) == False      # single element, too heavy
    assert module_0.will_it_fly([3, 2, 3], 1) == False  # palindrome but too heavy
    assert module_0.will_it_fly([], 5) == True        # empty list is balanced and light
    assert module_0.will_it_fly([], 0) == True        # empty list with zero weight
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 10) == True   # odd-length palindrome
    assert module_0.will_it_fly([1, 2, 2, 1], 6) == True       # even-length palindrome
    assert module_0.will_it_fly([1, 2, 3], 100) == False       # not a palindrome
    assert module_0.will_it_fly([5, 5, 5, 5], 20) == True      # exactly at weight limit
    assert module_0.will_it_fly([5, 5, 5, 5], 19) == False     # just over weight limit
    assert module_0.will_it_fly([1], 1) == True                # single element at limit
    assert module_0.will_it_fly([2, 1, 1, 2], 6) == True       # palindrome at limit
    assert module_0.will_it_fly([0, 0], 0) == True             # zeros with zero weight
    assert module_0.will_it_fly([1, 2, 1], 4) == True          # palindrome under limit
    assert module_0.will_it_fly([1, 2, 3, 4], 100) == False    # ascending, not palindrome
    assert module_0.will_it_fly([4, 3, 3, 4], 14) == True      # even palindrome at limit
    print("All tests passed!")


if __name__ == "__main__":
    test_will_it_fly()

# Generated at 2026-11-02 16:33:36.288255
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome with sum <= w -> True
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([3, 2, 3], 8) == False  # sum > w
    assert module_0.will_it_fly([1, 2], 5) == False     # not palindrome
    assert module_0.will_it_fly([3], 5) == True
    assert module_0.will_it_fly([], 0) == True          # empty is palindrome
    assert module_0.will_it_fly([], 1) == True
    assert module_0.will_it_fly([1, 2, 1], 4) == True
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum > w
    assert module_0.will_it_fly([5, 5, 5, 5], 20) == True
    assert module_0.will_it_fly([5, 5, 5, 5], 19) == False
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 10) == True
    assert module_0.will_it_fly([1, 2, 3, 4, 1], 100) == False  # not palindrome
    assert module_0.will_it_fly([0, 0], 0) == True
    assert module_0.will_it_fly([7], 7) == True
    assert module_0.will_it_fly([7], 6) == False
    assert module_0.will_it_fly([1, 1, 1, 1], 4) == True
    assert module_0.will_it_fly([2, 1, 1, 2], 6) == True
    assert module_0.will_it_fly([2, 1, 2], 4) == False  # sum > w
    assert module_0.will_it_fly([1, 3, 1], 5) == True
    assert module_0.will_it_fly([4, 4], 8) == True
    assert module_0.will_it_fly([4, 4], 7) == False
    assert module_0.will_it_fly([9, 9, 9], 27) == True
    assert module_0.will_it_fly([9, 9, 9], 26) == False
    assert module_0.will_it_fly([1, 2, 3, 3, 2, 1], 12) == True
    assert module_0.will_it_fly([1, 2, 3, 3, 1, 2], 100) == False  # not palindrome
    print("All tests passed!")

test_will_it_fly()

# Generated at 2026-11-02 16:34:53.384619
# Unit test for function will_it_fly
def test_will_it_fly():
    # nonce:06275c25
    # Balanced (palindrome) and light -> True
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([1, 2], 5) == False   # not a palindrome
    assert module_0.will_it_fly([3], 5) == True       # single element, light
    assert module_0.will_it_fly([1, 2, 3], 1) == False  # palindrome but too heavy
    assert module_0.will_it_fly([1, 2, 3], 6) == False  # heavy and not palindrome
    assert module_0.will_it_fly([], 0) == True        # empty list is balanced and light
    assert module_0.will_it_fly([5, 5, 5, 5], 20) == True   # even-length palindrome, exactly at weight
    assert module_0.will_it_fly([5, 5, 5, 5], 19) == False  # even-length palindrome, one over weight
    assert module_0.will_it_fly([4, 4], 8) == True    # even-length palindrome, exactly at limit
    assert module_0.will_it_fly([1, 2, 1], 0) == False  # palindrome but weight limit is zero
    assert module_0.will_it_fly([0], 0) == True       # zero weight object, zero limit
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 100) == True  # odd-length palindrome, light
    print("All tests passed!")

if __name__ == "__main__":
    test_will_it_fly()

# Generated at 2026-11-02 16:36:10.977900
# Unit test for function will_it_fly
def test_will_it_fly():
    # Balanced and light -> flies
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    # Balanced but too heavy -> does not fly
    assert module_0.will_it_fly([3, 2, 3], 1) == False
    # Not balanced but light -> does not fly
    assert module_0.will_it_fly([1, 2], 5) == False
    # Not balanced and heavy -> does not fly
    assert module_0.will_it_fly([3, 2, 1], 1) == False
    # Single element, within weight -> flies
    assert module_0.will_it_fly([1], 1) == True
    # Single element, exceeds weight -> does not fly
    assert module_0.will_it_fly([5], 1) == False
    # Empty list, weight >= 0 -> flies
    assert module_0.will_it_fly([], 0) == True
    # Empty list, negative weight -> does not fly
    assert module_0.will_it_fly([], -1) == False
    # Palindrome with even length -> flies
    assert module_0.will_it_fly([2, 2], 4) == True
    # Sum exactly equal to weight -> flies
    assert module_0.will_it_fly([1, 2, 1], 4) == True
    # Sum one over weight -> does not fly
    assert module_0.will_it_fly([1, 2, 2], 4) == False
    # Negative numbers, palindrome, within weight -> flies
    assert module_0.will_it_fly([-1, 0, -1], 0) == True
    # Long palindrome -> flies
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 9) == True
    # Almost palindrome -> does not fly
    assert module_0.will_it_fly([1, 2, 3, 4, 1], 100) == False

    print("All test cases passed!")

if __name__ == "__main__":
    test_will_it_fly()

# Generated at 2026-11-02 16:37:48.774693
# Unit test for function will_it_fly
def test_will_it_fly():
    # Balanced and light enough -> flies
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([1, 2], 5) == False  # Not balanced (palindrome check fails)
    assert module_0.will_it_fly([3], 5) == True      # Single element, light enough
    assert module_0.will_it_fly([3], 2) == False     # Single element, too heavy
    assert module_0.will_it_fly([1, 2, 1], 100) == True
    assert module_0.will_it_fly([1, 2, 3], 6) == False   # Not a palindrome
    assert module_0.will_it_fly([1, 2, 3], 2) == False   # Too heavy and not palindrome
    assert module_0.will_it_fly([5, 5, 5, 5], 20) == True   # Exactly at weight limit
    assert module_0.will_it_fly([5, 5, 5, 5], 19) == False  # Just over weight limit
    assert module_0.will_it_fly([], 0) == True              # Empty object flies
    assert module_0.will_it_fly([], 1) == True
    assert module_0.will_it_fly([0], 0) == True             # Zero weight element
    assert module_0.will_it_fly([2, 2], 4) == True
    assert module_0.will_it_fly([2, 2], 3) == False
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 10) == True
    assert module_0.will_it_fly([1, 2, 3, 4, 1], 100) == False  # Not palindrome
    # Non-integer values
    assert module_0.will_it_fly(['a', 'b', 'a'], 10) == True if False else None  # skip type issue
    print("All tests passed!")


if __name__ == "__main__":
    test_will_it_fly()