

# Generated at 2026-11-02 16:33:50.884148
# Unit test for function get_positive
def test_get_positive():import unittest


def module_0.get_positive(l: list):
    return [e for e in l if e > 0]


class TestGetPositive(unittest.TestCase):

    def test_basic_positive_numbers(self):
        self.assertEqual(module_0.get_positive([1, 2, 3]), [1, 2, 3])

    def test_mixed_numbers(self):
        self.assertEqual(module_0.get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_all_negative(self):
        self.assertEqual(module_0.get_positive([-1, -2, -3]), [])

    def test_empty_list(self):
        self.assertEqual(module_0.get_positive([]), [])

    def test_zero_excluded(self):
        self.assertEqual(module_0.get_positive([0, 1, -1, 0]), [1])

    def test_floats(self):
        self.assertEqual(module_0.get_positive([-1.5, 2.5, 3.0]), [2.5, 3.0])

    def test_duplicates_preserved(self):
        self.assertEqual(module_0.get_positive([3, 3, -3, 3]), [3, 3, 3])

    def test_large_numbers(self):
        self.assertEqual(module_0.get_positive([-1000000, 1000000]), [1000000])

    def test_order_preserved(self):
        self.assertEqual(module_0.get_positive([5, -5, 1, -1, 9]), [5, 1, 9])


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 16:35:20.351562
# Unit test for function get_positive
def test_get_positive():
    # Test with mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    
    # Test with all positive numbers
    assert module_0.get_positive([1, 2, 3, 4]) == [1, 2, 3, 4]
    
    # Test with all negative numbers
    assert module_0.get_positive([-1, -2, -3, -4]) == []
    
    # Test with empty list
    assert module_0.get_positive([]) == []
    
    # Test with zero (zero is not positive)
    assert module_0.get_positive([0, 1, -1, 0, 2]) == [1, 2]
    
    # Test with floats
    assert module_0.get_positive([-1.5, 2.5, -3.7, 0.1]) == [2.5, 0.1]
    
    # Test with duplicates
    assert module_0.get_positive([3, 3, -3, 3]) == [3, 3, 3]
    
    print("All tests passed!")


test_get_positive()

# Generated at 2026-11-02 16:36:37.844170
# Unit test for function get_positive
def test_get_positive():
    # Test with mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

    # Test with all positive numbers
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

    # Test with only negative numbers
    assert module_0.get_positive([-1, -2, -4, -5, -6]) == []

    # Test with empty list
    assert module_0.get_positive([]) == []

    # Test with zero included (zero is not positive)
    assert module_0.get_positive([0, 1, 0, 2]) == [1, 2]

    # Test with floats
    assert module_0.get_positive([-1.5, 2.5, -3.2, 0.1]) == [2.5, 0.1]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_positive()

# Generated at 2026-11-02 16:38:14.630432
# Unit test for function get_positive
def test_get_positive():
    # Mixed positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
    assert module_0.get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]

    # All positive numbers
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]

    # All negative numbers
    assert module_0.get_positive([-1, -2, -3]) == []

    # Zero is not positive
    assert module_0.get_positive([0, 0, 0]) == []
    assert module_0.get_positive([-1, 0, 1]) == [1]

    # Empty list
    assert module_0.get_positive([]) == []

    # Duplicates preserved
    assert module_0.get_positive([2, 2, -2, 2]) == [2, 2, 2]

    # Floats
    assert module_0.get_positive([-1.5, 2.5, -3.7, 0.1]) == [2.5, 0.1]

    # Order preserved
    assert module_0.get_positive([10, -5, 3, -1, 7]) == [10, 3, 7]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_positive()

# Generated at 2026-11-02 16:40:16.109659
# Unit test for function get_positive
def test_get_positive():
    # Test with a list containing positive and negative numbers
    assert module_0.get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]

    # Test with a list of only positive numbers
    assert module_0.get_positive([1, 2, 3]) == [1, 2, 3]

    # Test with a list of only negative numbers
    assert module_0.get_positive([-1, -2, -3]) == []

    # Test with an empty list
    assert module_0.get_positive([]) == []

    # Test with zero (zero is not positive)
    assert module_0.get_positive([0, 1, -1]) == [1]

    # Test with floats
    assert module_0.get_positive([-1.5, 2.5, -3.0, 4.1]) == [2.5, 4.1]

    # Test with duplicates
    assert module_0.get_positive([3, -3, 3, 7]) == [3, 3, 7]

    # Test preserves original order
    assert module_0.get_positive([5, -2, 1, -8, 9]) == [5, 1, 9]

    print("All test cases passed!")


if __name__ == "__main__":
    test_get_positive()