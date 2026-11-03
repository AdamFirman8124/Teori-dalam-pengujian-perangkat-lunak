

# Generated at 2026-11-02 09:57:31.707073
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case: multiple unique elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 3, 1, 4, 2]) == 2

    # Unsorted input with duplicates
    assert module_0.next_smallest([4, 1, 3, 2, 4, 1]) == 2
    assert module_0.next_smallest([7, 7, 7, 3, 3, 5]) == 5

    # Duplicates of the smallest value
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2

    # Negative numbers and mixed values
    assert module_0.next_smallest([-5, -1, -3, 0, 2]) == -3
    assert module_0.next_smallest([-2, -2, -1]) == -1

    # Two unique elements
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 10

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    # Fewer than two unique elements -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None
    assert module_0.next_smallest([7, 7, 7, 7]) is None

    # Large list
    assert module_0.next_smallest(list(range(100, 0, -1))) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 09:58:13.586497
# Unit test for function next_smallest
def test_next_smallest():
    # Normal case with distinct integers
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Unsorted input
    assert module_0.next_smallest([5, 3, 1, 4, 2]) == 2
    # Duplicates present
    assert module_0.next_smallest([5, 1, 4, 3, 2, 1]) == 2
    # Negative numbers
    assert module_0.next_smallest([-1, -2, -3]) == -2
    # Two elements only
    assert module_0.next_smallest([1, 2]) == 2
    assert module_0.next_smallest([2, 1]) == 2
    # Empty list
    assert module_0.next_smallest([]) is None
    # Single element
    assert module_0.next_smallest([1]) is None
    # All elements identical
    assert module_0.next_smallest([7, 7, 7]) is None
    # Mixed floats and ints
    assert module_0.next_smallest([1.5, 2, 3]) == 2
    # Large numbers
    assert module_0.next_smallest([1000000, 999999, 1000001]) == 1000000
    # Duplicates of the smallest value
    assert module_0.next_smallest([1, 1, 2, 3]) == 2
    print("All tests passed!")

test_next_smallest()

# Generated at 2026-11-02 09:59:26.848200
# Unit test for function next_smallest
def test_next_smallest():
    # Basic cases with distinct elements
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 4, 3, 2, 1]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2

    # Lists with duplicates (duplicates should be ignored)
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([2, 2, 1, 1, 3, 3]) == 2
    assert module_0.next_smallest([1, 1, 1, 1]) is None  # all same -> None

    # Edge cases: empty and single-element lists
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([7]) is None

    # Exactly two elements
    assert module_0.next_smallest([1, 2]) == 2
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20

    # Negative numbers
    assert module_0.next_smallest([-1, -2, -3]) == -2
    assert module_0.next_smallest([-5, 0, 5]) == 0
    assert module_0.next_smallest([-1, -1, -2]) == -1

    # Mixed positive/negative and zero
    assert module_0.next_smallest([3, -1, 0, 2]) == 0

    # Floats
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5

    # Large values
    assert module_0.next_smallest([1000000, 999999, 1000001]) == 1000000

# Generated at 2026-11-02 10:00:21.934669
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case: sorted list of unique integers
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2

    # Unsorted list
    assert module_0.next_smallest([5, 3, 1, 4, 2]) == 2

    # List with duplicates
    assert module_0.next_smallest([1, 1, 2, 3]) == 2
    assert module_0.next_smallest([3, 3, 1, 1, 2]) == 2

    # Two elements only
    assert module_0.next_smallest([2, 1]) == 2
    assert module_0.next_smallest([1, 2]) == 2

    # Single element -> None
    assert module_0.next_smallest([1]) is None

    # Empty list -> None
    assert module_0.next_smallest([]) is None

    # All identical elements -> None
    assert module_0.next_smallest([7, 7, 7]) is None
    assert module_0.next_smallest([0, 0, 0, 0]) is None

    # Negative numbers
    assert module_0.next_smallest([-1, -5, -3]) == -3
    assert module_0.next_smallest([-10, 0, 10]) == 0

    # Mixed positive and negative
    assert module_0.next_smallest([3, -1, 2, 0]) == 0

    # Floats and ints mixed
    assert module_0.next_smallest([1.5, 1, 2.5]) == 1.5

    # Large list
    assert module_0.next_smallest(list(range(100, 0, -1))) == 2

    # Two identical elements -> None
    assert module_0.next_smallest([5, 5]) is None

    print("All tests passed!")


if __name__ == "__main__":
    test_next_smallest()

# Generated at 2026-11-02 10:01:39.001870
# Unit test for function next_smallest
def test_next_smallest():
    # Typical case with distinct integers
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    # Unsorted input
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    # Duplicates should be ignored (unique values only)
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([3, 3, 3, 1, 1, 5, 5]) == 3
    # Negative numbers
    assert module_0.next_smallest([-5, -1, -3, -2]) == -3
    assert module_0.next_smallest([-2, -4, -6]) == -4
    # Mixed positive and negative
    assert module_0.next_smallest([0, -1, 1]) == 0
    # Fewer than 2 unique values -> None
    assert module_0.next_smallest([7]) is None
    assert module_0.next_smallest([4, 4, 4, 4]) is None
    # Empty list -> None
    assert module_0.next_smallest([]) is None
    # Two unique values
    assert module_0.next_smallest([10, 20]) == 20
    assert module_0.next_smallest([20, 10]) == 20
    # Floats
    assert module_0.next_smallest([1.5, 2.5, 0.5]) == 1.5
    # Duplicates of the smallest value
    assert module_0.next_smallest([2, 2, 1, 1, 3]) == 2


# Nonce-based test class for unittest runner
class TestNextSmallest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(module_0.next_smallest([1, 2, 3, 4, 5]), 2)

    def test_unsorted(self):
        self.assertEqual(module_0.next_smallest([5, 3, 1, 4, 2]), 2)

    def test_duplicates(self):
        self.assertEqual(module_0.next_smallest([1, 1, 2, 2, 3]), 2)

    def test_all_same(self):
        self.assertIsNone(module_0.next_smallest([7, 7, 7]))

    def test_single_element(self):
        self.assertIsNone(module_0.next_smallest([42]))

    def test_empty(self):
        self.assertIsNone(module_0.next_smallest([]))

    def test_negatives(self):
        self.assertEqual(module_0.next_smallest([-1, -5, -3]), -3)

    def test_two_unique(self):
        self.assertEqual(module_0.next_smallest([9, 3]), 9)

    def test_floats(self):
        self.assertEqual(module_0.next_smallest([2.5, 1.5, 3.5]), 2.5)


if __name__ == "__main__":
    test_next_smallest()
    print("test_next_smallest passed")
    unittest.main()