

# Generated at 2026-11-03 05:27:11.517232
# Unit test for function below_zero
def test_below_zero():
    # Balance drops below zero
    assert module_0.below_zero([1, 2, 3, -5]) == True

    # Balance never drops below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Empty list of operations
    assert module_0.below_zero([]) == False

    # Balance reaches exactly zero but not below
    assert module_0.below_zero([1, -1]) == False

    # Single negative operation immediately goes below zero
    assert module_0.below_zero([-1]) == True

    # Balance goes below zero then recovers (still True)
    assert module_0.below_zero([5, -10, 20]) == True

    # Multiple operations with balance hitting negative midway
    assert module_0.below_zero([10, -5, -5, -1]) == True

    # Large values
    assert module_0.below_zero([1000000, -1000001]) == True
    assert module_0.below_zero([1000000, -1000000]) == False

    # Alternating operations staying non-negative
    assert module_0.below_zero([1, -1, 1, -1, 1]) == False

# Generated at 2026-11-03 05:29:16.622581
# Unit test for function below_zero
def test_below_zero():import unittest


class TestBelowZero(unittest.TestCase):

    def test_never_below_zero(self):
        self.assertFalse(module_0.below_zero([1, 2, 3]))

    def test_goes_below_zero(self):
        self.assertTrue(module_0.below_zero([1, 2, -4, 5]))

    def test_empty_list(self):
        self.assertFalse(module_0.below_zero([]))

    def test_exactly_zero(self):
        # Balance reaching zero is not below zero
        self.assertFalse(module_0.below_zero([1, -1]))

    def test_single_negative(self):
        self.assertTrue(module_0.below_zero([-1]))

    def test_single_positive(self):
        self.assertFalse(module_0.below_zero([1]))

    def test_dips_below_then_recovers(self):
        self.assertTrue(module_0.below_zero([10, -15, 20]))

    def test_all_positive(self):
        self.assertFalse(module_0.below_zero([1, 2, 3, 4, 5]))

    def test_all_negative(self):
        self.assertTrue(module_0.below_zero([-1, -2, -3]))

    def test_stays_at_zero_then_negative(self):
        self.assertTrue(module_0.below_zero([5, -5, -1]))

    def test_large_numbers(self):
        self.assertFalse(module_0.below_zero([1000000, -999999]))
        self.assertTrue(module_0.below_zero([1000000, -1000001]))

    def test_alternating(self):
        self.assertFalse(module_0.below_zero([2, -1, 2, -1, 2, -1]))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 05:32:03.586756
# Unit test for function below_zero
def test_below_zero():
    # Case where balance goes below zero
    assert module_0.below_zero([1, 2, 3, -5]) == True

    # Case where balance never goes below zero
    assert module_0.below_zero([1, 2, 3]) == False

    # Empty list, no operations
    assert module_0.below_zero([]) == False

    # Balance exactly zero, should not trigger
    assert module_0.below_zero([5, -5]) == False

    # Starts below zero immediately
    assert module_0.below_zero([-1]) == True

    # Large positive then large negative
    assert module_0.below_zero([100, 50, -200]) == True

    # Negative then recovery, still dips below zero
    assert module_0.below_zero([10, -15, 100]) == True

    # Multiple operations staying positive
    assert module_0.below_zero([1, 1, 1, 1, 1]) == False

    # Mixed operations ending at positive but dipping negative
    assert module_0.below_zero([2, -4, 10, -3]) == True

    # Only positive operations
    assert module_0.below_zero([10, 20, 30]) == False

    # Single zero operation
    assert module_0.below_zero([0]) == False

    # Large numbers
    assert module_0.below_zero([1000000, -2000000]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_below_zero()

# Generated at 2026-11-03 05:33:38.813908
# Unit test for function below_zero
def test_below_zero():
    # Test with empty list - balance never goes below zero
    assert module_0.below_zero([]) == False

    # Test with single positive operation
    assert module_0.below_zero([1]) == False
    assert module_0.below_zero([100]) == False

    # Test with single negative operation - immediately below zero
    assert module_0.below_zero([-1]) == True
    assert module_0.below_zero([-100]) == True

    # Test with operations that never drop below zero
    assert module_0.below_zero([1, 2, 3]) == False
    assert module_0.below_zero([5, -3, 2]) == False  # balance: 5, 2, 4
    assert module_0.below_zero([10, -10, 5]) == False  # balance: 10, 0, 5

    # Test with operations that drop below zero at some point
    assert module_0.below_zero([1, 2, -4]) == True  # balance: 1, 3, -1
    assert module_0.below_zero([5, -3, -3]) == True  # balance: 5, 2, -1

    # Test where balance touches zero but never goes below
    assert module_0.below_zero([1, -1]) == False  # balance: 1, 0
    assert module_0.below_zero([3, -3, 3, -3]) == False  # balance: 3, 0, 3, 0

    # Test with first operation being zero
    assert module_0.below_zero([0, 1]) == False
    assert module_0.below_zero([0, -1]) == True

    # Test with large numbers
    assert module_0.below_zero([1000000, -2000000]) == True
    assert module_0.below_zero([1000000, -999999]) == False

    # Test negative result then recovery - still True since it dipped below zero
    assert module_0.below_zero([5, -10, 20]) == True  # balance: 5, -5, 15

# Generated at 2026-11-03 05:34:51.799567
# Unit test for function below_zero
def test_below_zero():
    # Test with empty list - balance never goes below zero
    assert module_0.below_zero([]) == False

    # Test with operations that go below zero
    assert module_0.below_zero([1, 2, -4]) == True

    # Test with operations that stay non-negative
    assert module_0.below_zero([1, 2, 3]) == False

    # Test with balance reaching exactly zero (not below)
    assert module_0.below_zero([1, 2, -3, 4]) == False

    # Test with single negative operation
    assert module_0.below_zero([-1]) == True

    # Test with single positive operation
    assert module_0.below_zero([5]) == False

    # Test with balance going negative mid-sequence
    assert module_0.below_zero([1, -2, 3]) == True

    # Test with large numbers
    assert module_0.below_zero([1000000, -2000000]) == True

    # Test with zeros only
    assert module_0.below_zero([0, 0, 0]) == False

    # Test with operations summing to exactly zero
    assert module_0.below_zero([5, -5]) == False


test_below_zero()
print("All tests passed!")