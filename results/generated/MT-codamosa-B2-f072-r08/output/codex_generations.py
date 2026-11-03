

# Generated at 2026-11-03 01:13:21.188213
# Unit test for function will_it_fly
def test_will_it_fly():import unittest


class TestWillItFly(unittest.TestCase):

    def test_too_heavy(self):
        # Sum exceeds weight limit
        self.assertFalse(module_0.will_it_fly([3, 2, 3], 7))
        self.assertFalse(module_0.will_it_fly([1, 2], 1))
        self.assertFalse(module_0.will_it_fly([5], 4))

    def test_not_palindromic(self):
        # Weight is fine but object is not balanced
        self.assertFalse(module_0.will_it_fly([1, 2], 5))
        self.assertFalse(module_0.will_it_fly([3, 2, 1], 10))
        self.assertFalse(module_0.will_it_fly([1, 2, 3, 4], 20))

    def test_palindromic_and_light(self):
        # Balanced and within weight limit
        self.assertTrue(module_0.will_it_fly([3, 2, 3], 9))
        self.assertTrue(module_0.will_it_fly([1, 2], 5))
        self.assertTrue(module_0.will_it_fly([3], 5))

    def test_exact_weight_boundary(self):
        # Sum equals weight exactly -> should fly
        self.assertTrue(module_0.will_it_fly([3, 2, 3], 8))
        self.assertTrue(module_0.will_it_fly([5], 5))

    def test_empty_list(self):
        # Empty object is trivially balanced and weightless
        self.assertTrue(module_0.will_it_fly([], 0))
        self.assertTrue(module_0.will_it_fly([], 10))

    def test_single_element(self):
        # Single element is always palindromic
        self.assertTrue(module_0.will_it_fly([1], 1))
        self.assertTrue(module_0.will_it_fly([0], 0))
        self.assertFalse(module_0.will_it_fly([1], 0))

    def test_even_length_palindrome(self):
        self.assertTrue(module_0.will_it_fly([2, 2], 4))
        self.assertTrue(module_0.will_it_fly([1, 2, 2, 1], 10))
        self.assertFalse(module_0.will_it_fly([1, 2, 2, 1], 5))

    def test_negative_numbers(self):
        # Negative values reduce the sum
        self.assertTrue(module_0.will_it_fly([-1, 1], 0))
        self.assertFalse(module_0.will_it_fly([-1, 1], -1))

    def test_both_conditions_fail(self):
        # Too heavy AND not palindromic -> still False
        self.assertFalse(module_0.will_it_fly([1, 2, 3], 3))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 01:14:20.304997
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome and weight sufficient -> True
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([1, 2], 5) == False  # Not a palindrome
    assert module_0.will_it_fly([3], 5) == True  # Single element palindrome
    assert module_0.will_it_fly([3], 2) == False  # Sum exceeds weight
    assert module_0.will_it_fly([], 0) == True  # Empty list is palindrome, sum 0
    assert module_0.will_it_fly([1, 2, 1], 5) == True
    assert module_0.will_it_fly([1, 2, 1], 3) == True  # Sum equals weight exactly
    assert module_0.will_it_fly([1, 2, 3], 1) == False  # Sum exceeds weight
    assert module_0.will_it_fly([1, 2, 3], 6) == False  # Not a palindrome
    assert module_0.will_it_fly([5, 5, 5, 5], 20) == True  # Sum equals weight
    assert module_0.will_it_fly([5, 5, 5, 5], 19) == False  # Sum exceeds weight
    assert module_0.will_it_fly([0, 0], 0) == True  # Zero sum with zero weight
    assert module_0.will_it_fly([7, 7, 7], 100) == True
    assert module_0.will_it_fly([2, 3, 2], 7) == True
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 9) == True
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 8) == False  # Sum exceeds weight
    assert module_0.will_it_fly([4, 4], 100) == True
    assert module_0.will_it_fly([4, 5], 100) == False  # Not a palindrome
    print("All test cases passed!")

test_will_it_fly()

# Generated at 2026-11-03 01:15:08.154946
# Unit test for function will_it_fly
def test_will_it_fly():
    # Balanced and light -> should fly
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    # Balanced but too heavy -> should not fly
    assert module_0.will_it_fly([3, 2, 3], 6) == False
    # Sum equals weight exactly -> should fly
    assert module_0.will_it_fly([3, 2, 3], 8) == True
    # Unbalanced (not a palindrome) -> should not fly
    assert module_0.will_it_fly([1, 2], 5) == False
    # Unbalanced and too heavy -> should not fly
    assert module_0.will_it_fly([5, 1, 4], 5) == False
    # Single element within weight -> should fly
    assert module_0.will_it_fly([1], 1) == True
    # Single element exceeding weight -> should not fly
    assert module_0.will_it_fly([2], 1) == False
    # Empty list is balanced and weighs 0 -> should fly
    assert module_0.will_it_fly([], 0) == True
    # All elements the same -> palindrome -> should fly
    assert module_0.will_it_fly([4, 4, 4, 4], 16) == True
    # Odd-length palindrome -> should fly
    assert module_0.will_it_fly([1, 2, 1], 4) == True
    # Palindrome but sum just over weight -> should not fly
    assert module_0.will_it_fly([2, 3, 2], 6) == False
    # Negative weight capacity -> should not fly
    assert module_0.will_it_fly([1], -1) == False
    # Longer palindrome
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 10) == True
    # Near-palindrome (one mismatch) -> should not fly
    assert module_0.will_it_fly([1, 2, 3, 4, 1], 20) == False

# Generated at 2026-11-03 01:15:58.909409
# Unit test for function will_it_fly
def test_will_it_fly():
    # Object is balanced and light enough -> True
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([3], 5) == True
    assert module_0.will_it_fly([1, 2], 5) == False  # Not balanced

    # Object is balanced but too heavy -> False
    assert module_0.will_it_fly([3, 2, 3], 1) == False
    assert module_0.will_it_fly([1, 2, 1], 4) == True  # sum == w, exactly at limit
    assert module_0.will_it_fly([1, 2, 1], 3) == False  # sum > w

    # Single element cases
    assert module_0.will_it_fly([5], 5) == True
    assert module_0.will_it_fly([5], 4) == False

    # Empty list is trivially balanced with sum 0
    assert module_0.will_it_fly([], 0) == True
    assert module_0.will_it_fly([], 10) == True

    # Even-length palindromes
    assert module_0.will_it_fly([4, 4], 8) == True
    assert module_0.will_it_fly([4, 4], 7) == False
    assert module_0.will_it_fly([2, 3, 3, 2], 10) == True

    # Odd-length non-palindromes
    assert module_0.will_it_fly([1, 2, 3], 100) == False

    # Negative numbers and zeros
    assert module_0.will_it_fly([0, 0], 0) == True
    assert module_0.will_it_fly([-1, -1], -2) == True
    assert module_0.will_it_fly([-1, -1], -3) == False

    # Longer palindrome
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 9) == True
    assert module_0.will_it_fly([1, 2, 3, 2, 1], 8) == False

# nonce:d1e67fb7

# Generated at 2026-11-03 01:16:41.023935
# Unit test for function will_it_fly
def test_will_it_fly():
    # Palindrome and weight sufficient -> flies
    assert module_0.will_it_fly([3, 2, 3], 9) == True
    assert module_0.will_it_fly([3, 2, 3], 8) == False  # too heavy
    assert module_0.will_it_fly([1, 2], 5) == False     # not a palindrome
    assert module_0.will_it_fly([3], 5) == True         # single element palindrome

    # Edge cases
    assert module_0.will_it_fly([], 0) == True          # empty object, zero weight
    assert module_0.will_it_fly([], 10) == True
    assert module_0.will_it_fly([1, 1], 2) == True      # sum equals weight exactly
    assert module_0.will_it_fly([1, 1], 1) == False     # sum exceeds weight
    assert module_0.will_it_fly([1, 2, 1], 5) == True
    assert module_0.will_it_fly([1, 2, 3], 100) == False  # palindrome check fails
    assert module_0.will_it_fly([5, 5, 5, 5], 20) == True
    assert module_0.will_it_fly([5, 5, 5, 5], 19) == False
    assert module_0.will_it_fly([7], 7) == True         # single element, exact weight
    assert module_0.will_it_fly([7], 6) == False
    assert module_0.will_it_fly([1, 2, 2, 1], 6) == True
    assert module_0.will_it_fly([1, 2, 3, 1], 100) == False  # not palindrome
    assert module_0.will_it_fly([0], 0) == True
    assert module_0.will_it_fly([0, 0], 0) == True

    print("All tests passed!")


# Run tests
test_will_it_fly()