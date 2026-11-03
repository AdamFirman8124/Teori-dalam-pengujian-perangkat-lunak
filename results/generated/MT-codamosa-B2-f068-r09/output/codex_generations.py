

# Generated at 2026-11-02 21:09:06.518380
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []
    
    # No even values returns empty list
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([1, 3, 5]) == []
    
    # Single element cases
    assert module_0.pluck([0]) == [0, 0]
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1]) == []
    
    # Smallest even at the beginning
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([2, 4, 6]) == [2, 0]
    
    # Smallest even at the end
    assert module_0.pluck([6, 4, 2]) == [2, 2]
    
    # Smallest even in the middle
    assert module_0.pluck([8, 12, 10, 4, 6]) == [4, 3]
    
    # Duplicate smallest even value returns first index
    assert module_0.pluck([4, 2, 2, 6]) == [2, 1]
    assert module_0.pluck([2, 2, 4]) == [2, 0]
    
    # Array with only even numbers
    assert module_0.pluck([10, 8, 6, 4]) == [4, 3]
    
    # Zero is an even value
    assert module_0.pluck([5, 0, 3, 0, 7]) == [0, 1]
    assert module_0.pluck([1, 0, -2, 4]) == [-2, 2]
    
    # Negative even numbers
    assert module_0.pluck([-4, -2, 6, 2]) == [-4, 0]
    assert module_0.pluck([3, -6, -2, 8]) == [-6, 1]
    
    # Mixed odd and even, smallest even not global min consideration
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 8, 1]) == [0, 1]
    
    # Larger array
    assert module_0.pluck([7, 9, 2, 8, 4, 6, 10, 1]) == [2, 2]
    
    # All values the same even number
    assert module_0.pluck([6, 6, 6]) == [6, 0]
    
    # Even number larger than odd values present
    assert module_0.pluck([100, 3, 5]) == [100, 0]

test_pluck()
print("All tests passed!")

# Generated at 2026-11-02 21:09:33.568121
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even numbers
    assert module_0.pluck([1, 3, 5, 7]) == []

    # Single even number
    assert module_0.pluck([2]) == [2, 0]

    # Single odd number
    assert module_0.pluck([3]) == []

    # Mixed odds and evens
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 1, 6, 3]) == [4, 0]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Smallest even appears later in array
    assert module_0.pluck([8, 12, 4, 6]) == [4, 2]

    # Duplicate minimum evens - should return first occurrence index
    assert module_0.pluck([2, 4, 2, 6]) == [2, 0]
    assert module_0.pluck([4, 2, 3, 2]) == [2, 1]

    # All elements are the same even number
    assert module_0.pluck([6, 6, 6]) == [6, 0]

    # Negative numbers
    assert module_0.pluck([-4, -2, -6]) == [-6, 2]
    assert module_0.pluck([-3, -5, -7]) == []

    # Zero as minimum even
    assert module_0.pluck([5, 0, 7, 2]) == [0, 1]

    # Larger array
    assert module_0.pluck(list(range(1, 11))) == [2, 1]

    print("All test_pluck tests passed!")


test_pluck()

# Generated at 2026-11-02 21:09:47.877425
# Unit test for function pluck
def test_pluck():import unittest


def module_0.pluck(arr):
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]


# Unit test for function pluck
class TestPluck(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(module_0.pluck([]), [])

    def test_no_even_values(self):
        self.assertEqual(module_0.pluck([1, 3, 5, 7]), [])

    def test_single_even_element(self):
        self.assertEqual(module_0.pluck([4]), [4, 0])

    def test_single_odd_element(self):
        self.assertEqual(module_0.pluck([3]), [])

    def test_basic_case(self):
        self.assertEqual(module_0.pluck([4, 2, 3]), [2, 1])

    def test_smallest_even_at_end(self):
        self.assertEqual(module_0.pluck([1, 2, 3]), [2, 1])

    def test_multiple_evens_picks_smallest(self):
        self.assertEqual(module_0.pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_duplicate_smallest_returns_first_index(self):
        self.assertEqual(module_0.pluck([2, 4, 2, 6]), [2, 0])

    def test_negative_evens(self):
        self.assertEqual(module_0.pluck([-4, -2, 3]), [-4, 0])

    def test_all_even_values(self):
        self.assertEqual(module_0.pluck([8, 6, 4, 2]), [2, 3])

    def test_zero_is_even(self):
        self.assertEqual(module_0.pluck([1, 0, 5]), [0, 1])

    def test_large_values(self):
        self.assertEqual(module_0.pluck([1000000, 999998, 3]), [999998, 1])

    def test_even_and_odd_mixed(self):
        self.assertEqual(module_0.pluck([7, 1, 5, 3, 8, 9]), [8, 4])

    def test_result_format(self):
        result = module_0.pluck([2, 3, 4])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 21:10:02.015761
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []

    # Single even number
    assert module_0.pluck([2]) == [2, 0]

    # Single odd number
    assert module_0.pluck([3]) == []

    # Multiple even numbers, minimum at start
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    # Minimum even number not at start
    assert module_0.pluck([4, 2, 6]) == [2, 1]

    # Duplicate minimum even values -> index of first occurrence
    assert module_0.pluck([4, 2, 3, 2]) == [2, 1]

    # Mixed odd/even with zero as minimum
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]

    # Larger array with minimum even at the end
    assert module_0.pluck([7, 1, 9, 5, 8]) == [8, 4]

# Generated at 2026-11-02 21:10:15.618569
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == [], "Empty array should return empty list"
    assert module_0.pluck([1]) == [], "Array with no evens should return empty list"
    assert module_0.pluck([1, 2, 3]) == [2, 1], "Should return smallest even value and its index"
    assert module_0.pluck([2, 4, 3]) == [2, 0], "Should return smallest even value and its index"
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1], "Should return first occurrence of smallest even"
    assert module_0.pluck([1, 2, 3, 0, 5, 3]) == [0, 3], "Zero is even and smallest"
    assert module_0.pluck([3, 5, 7]) == [], "All odd numbers should return empty list"
    assert module_0.pluck([4, 2, 6, 2]) == [2, 1], "Duplicate minimum even should return first index"
    assert module_0.pluck([0]) == [0, 0], "Single even element"
    assert module_0.pluck([-2, -4, 3]) == [-4, 1], "Negative even numbers handled correctly"
    print("All tests passed!")


if __name__ == "__main__":
    test_pluck()