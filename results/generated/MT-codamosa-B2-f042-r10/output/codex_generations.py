

# Generated at 2026-11-02 16:54:12.536343
# Unit test for function incr_list
def test_incr_list():
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]
    assert module_0.incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert module_0.incr_list([]) == []
    assert module_0.incr_list([0]) == [1]
    assert module_0.incr_list([-1, -2, -3]) == [0, -1, -2]
    assert module_0.incr_list([-5, 0, 5]) == [-4, 1, 6]
    assert module_0.incr_list([1000000]) == [1000001]
    assert module_0.incr_list([1, 1, 1]) == [2, 2, 2]
    # Original list should not be modified
    original = [1, 2, 3]
    result = module_0.incr_list(original)
    assert original == [1, 2, 3]
    assert result == [2, 3, 4]
    print("All tests passed!")


class TestIncrList(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(module_0.incr_list([1, 2, 3]), [2, 3, 4])

    def test_empty(self):
        self.assertEqual(module_0.incr_list([]), [])

    def test_negatives(self):
        self.assertEqual(module_0.incr_list([-1, -2, -3]), [0, -1, -2])

    def test_mixed(self):
        self.assertEqual(module_0.incr_list([-5, 0, 5]), [-4, 1, 6])

    def test_duplicates(self):
        self.assertEqual(module_0.incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]),
                         [6, 4, 6, 3, 4, 4, 10, 1, 124])

    def test_input_not_mutated(self):
        original = [1, 2, 3]
        module_0.incr_list(original)
        self.assertEqual(original, [1, 2, 3])


if __name__ == "__main__":
    test_incr_list()
    unittest.main()

# Generated at 2026-11-02 16:55:27.030769
# Unit test for function incr_list
def test_incr_list():
    # Test with a basic list of positive integers
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]

    # Test with an empty list
    assert module_0.incr_list([]) == []

    # Test with negative numbers
    assert module_0.incr_list([-1, -2, -3]) == [0, -1, -2]

    # Test with a single element
    assert module_0.incr_list([0]) == [1]

    # Test with mixed positive, negative, and zero
    assert module_0.incr_list([0, -5, 10]) == [1, -4, 11]

    # Test with large numbers
    assert module_0.incr_list([1000000, 999999]) == [1000001, 1000000]

    # Test that original list is not modified
    original = [1, 2, 3]
    result = module_0.incr_list(original)
    assert original == [1, 2, 3]
    assert result == [2, 3, 4]

    # Test that returned object is a new list
    assert module_0.incr_list([1, 2]) is not None
    assert isinstance(module_0.incr_list([1, 2]), list)

    # Test with duplicates
    assert module_0.incr_list([5, 5, 5]) == [6, 6, 6]

    # Test with floats
    assert module_0.incr_list([1.5, 2.5]) == [2.5, 3.5]

    print("All tests passed!")


if __name__ == "__main__":
    test_incr_list()

# Generated at 2026-11-02 16:56:33.033793
# Unit test for function incr_list
def test_incr_list():
    # Test with a basic list
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]
    # Test with empty list
    assert module_0.incr_list([]) == []
    # Test with negative numbers
    assert module_0.incr_list([-1, -2, 0]) == [0, -1, 1]
    # Test with single element
    assert module_0.incr_list([5]) == [6]
    # Test with large numbers
    assert module_0.incr_list([1000, 999999]) == [1001, 1000000]
    # Test original list not modified
    original = [1, 2, 3]
    module_0.incr_list(original)
    assert original == [1, 2, 3]

# Generated at 2026-11-02 16:57:49.071673
# Unit test for function incr_list
def test_incr_list():
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]
    assert module_0.incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert module_0.incr_list([]) == []
    assert module_0.incr_list([-1, -2, -3]) == [0, -1, -2]
    assert module_0.incr_list([0]) == [1]
    assert module_0.incr_list([100, 200]) == [101, 201]

# Generated at 2026-11-02 16:59:09.873536
# Unit test for function incr_list
def test_incr_list():
    # Basic case
    assert module_0.incr_list([1, 2, 3]) == [2, 3, 4]
    # Empty list
    assert module_0.incr_list([]) == []
    # Negative numbers
    assert module_0.incr_list([-1, -2, -3]) == [0, -1, -2]
    # Zeros
    assert module_0.incr_list([0, 0, 0]) == [1, 1, 1]
    # Mixed positive/negative
    assert module_0.incr_list([-5, 0, 5]) == [-4, 1, 6]
    # Large numbers
    assert module_0.incr_list([999999, 1000000]) == [1000000, 1000001]
    # Single element
    assert module_0.incr_list([42]) == [43]
    # Original list is not mutated
    original = [1, 2, 3]
    module_0.incr_list(original)
    assert original == [1, 2, 3]
    print("All tests passed!")


if __name__ == "__main__":
    test_incr_list()