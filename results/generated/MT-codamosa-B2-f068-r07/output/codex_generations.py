

# Generated at 2026-11-02 10:52:52.179767
# Unit test for function pluck
def test_pluck():import unittest


class TestPluck(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(module_0.pluck([]), [])

    def test_no_evens(self):
        self.assertEqual(module_0.pluck([1, 3, 5, 7]), [])

    def test_single_even(self):
        self.assertEqual(module_0.pluck([4]), [4, 0])

    def test_single_odd(self):
        self.assertEqual(module_0.pluck([3]), [])

    def test_basic_example(self):
        self.assertEqual(module_0.pluck([4, 2, 3]), [2, 1])

    def test_multiple_evens_min_selected(self):
        self.assertEqual(module_0.pluck([1, 2, 3, 4, 5, 6]), [2, 1])

    def test_min_even_not_first_even(self):
        self.assertEqual(module_0.pluck([8, 12, 4, 6]), [4, 2])

    def test_tie_returns_first_index(self):
        self.assertEqual(module_0.pluck([2, 4, 2, 6]), [2, 0])

    def test_even_at_end(self):
        self.assertEqual(module_0.pluck([1, 3, 5, 0]), [0, 3])

    def test_negative_evens(self):
        self.assertEqual(module_0.pluck([1, -2, 3, -4]), [-4, 3])

    def test_zero_is_even(self):
        self.assertEqual(module_0.pluck([5, 0, 3]), [0, 1])

    def test_all_evens(self):
        self.assertEqual(module_0.pluck([10, 2, 8, 2]), [2, 1])

    def test_large_values(self):
        self.assertEqual(module_0.pluck([1000000, 999998, 999997]), [999998, 1])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 10:54:42.425875
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    
    # No even values
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []
    
    # Single even element
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([0]) == [0, 0]
    
    # Single odd element
    assert module_0.pluck([3]) == []
    
    # Basic cases with smallest even in middle/end
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 4, 3, 2]) == [2, 3]
    
    # Smallest even value appears multiple times -> first index
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([2, 4, 2, 6]) == [2, 0]
    
    # All even values
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]
    assert module_0.pluck([2, 2, 2]) == [2, 0]
    
    # Contains zero
    assert module_0.pluck([1, 0, 5, 2]) == [0, 1]
    
    # Negative even numbers
    assert module_0.pluck([-4, -2, 3, 6]) == [-4, 0]
    assert module_0.pluck([3, -2, -8, 4]) == [-8, 2]
    
    # Larger values
    assert module_0.pluck([100, 101, 102, 99]) == [100, 0]
    
    # Odd smallest overall but even needed
    assert module_0.pluck([1, 3, 2, 5, 4]) == [2, 2]

    print("All test_pluck tests passed!")


if __name__ == "__main__":
    test_pluck()

# Generated at 2026-11-02 10:55:54.398133
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even numbers
    assert module_0.pluck([1, 3, 5, 7]) == []

    # Single even number
    assert module_0.pluck([2]) == [2, 0]

    # Smallest even appears first
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    # Smallest even appears last
    assert module_0.pluck([4, 6, 2]) == [2, 2]

    # Duplicate minimum evens — should return first occurrence index
    assert module_0.pluck([4, 2, 3, 2, 5]) == [2, 1]

    # Mixed odd and even values
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Negative even numbers included
    assert module_0.pluck([-4, 3, -2, 7]) == [-4, 0]

    # Negative smaller than positive
    assert module_0.pluck([3, 6, -8, 10]) == [-8, 2]

    # All odds with negatives
    assert module_0.pluck([-3, -1, 5]) == []

    # Zero counts as even
    assert module_0.pluck([1, 0, 3]) == [0, 1]

    # Larger example
    assert module_0.pluck([7, 9, 2, 4, 6, 8, 2]) == [2, 2]

    print("All test_pluck tests passed!")


test_pluck()

# Generated at 2026-11-02 10:58:43.658053
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    
    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []
    
    # Single even number
    assert module_0.pluck([4]) == [4, 0]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    
    # Multiple evens, smallest at various positions
    assert module_0.pluck([2, 4, 6]) == [2, 0]
    assert module_0.pluck([6, 4, 2]) == [2, 2]
    assert module_0.pluck([1, 5, 8, 3, 10]) == [8, 2]
    
    # Duplicate minimum even values -> first occurrence index
    assert module_0.pluck([4, 2, 3, 2]) == [2, 1]
    assert module_0.pluck([2, 2, 2]) == [2, 0]
    
    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([0, -2, 4]) == [-2, 1]
    
    # Zero is even
    assert module_0.pluck([5, 0, 3, 0]) == [0, 1]
    
    # Mixed odds and evens
    assert module_0.pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert module_0.pluck([9, 7, 5, 3]) == []

# Generated at 2026-11-02 11:01:26.670001
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even values
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([7]) == []

    # Single even element
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([0]) == [0, 0]

    # Smallest even in the middle
    assert module_0.pluck([4, 2, 3]) == [2, 1]

    # Smallest even at the end
    assert module_0.pluck([5, 3, 1, 8]) == [8, 3]

    # Smallest even at the start
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    # Duplicate smallest evens -> first occurrence index
    assert module_0.pluck([1, 2, 3, 2]) == [2, 1]
    assert module_0.pluck([2, 4, 2]) == [2, 0]

    # All zeros
    assert module_0.pluck([0, 0, 0]) == [0, 0]

    # Zero counts as even
    assert module_0.pluck([1, 0, 3]) == [0, 1]

    # Negative even values
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]
    assert module_0.pluck([3, -6, 5, -6]) == [-6, 1]

    # Mixed odd and even values
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]

    print("All pluck tests passed!")


if __name__ == "__main__":
    test_pluck()