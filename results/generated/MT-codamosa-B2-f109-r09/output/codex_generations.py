

# Generated at 2026-11-02 20:01:12.248764
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array is trivially sorted
    assert module_0.move_one_ball([]) == True

    # Single element is always sorted
    assert module_0.move_one_ball([5]) == True
    assert module_0.move_one_ball([1]) == True

    # Already sorted arrays
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True
    assert module_0.move_one_ball([7]) == True

    # Arrays that are a rotation of a sorted array
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True
    assert module_0.move_one_ball([4, 5, 6, 7, 1, 2, 3]) == True

    # Arrays that cannot be sorted by one rotation
    assert module_0.move_one_ball([3, 1, 2, 5, 4]) == False
    assert module_0.move_one_ball([2, 1, 3]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([7, 5, 6, 1, 2, 3, 4]) == False

    # Arrays with duplicates
    assert module_0.move_one_ball([2, 1, 2]) == True
    assert module_0.move_one_ball([3, 1, 1]) == True
    assert module_0.move_one_ball([2, 2, 2]) == True
    assert module_0.move_one_ball([1, 3, 1]) == False

    # Negative numbers
    assert module_0.move_one_ball([-3, -2, -5, -4]) == True   # rotation of [-5, -4, -3, -2]
    assert module_0.move_one_ball([-1, -3, -2]) == True       # rotation of [-3, -2, -1]
    assert module_0.move_one_ball([-1, -2, -3]) == False

    # Two-element arrays
    assert module_0.move_one_ball([1, 2]) == True
    assert module_0.move_one_ball([2, 1]) == True  # rotation gives [1, 2]

# Generated at 2026-11-02 20:04:13.510337
# Unit test for function move_one_ball
def test_move_one_ball():import unittest


class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(module_0.move_one_ball([]))

    def test_single_element(self):
        self.assertTrue(module_0.move_one_ball([5]))

    def test_already_sorted(self):
        self.assertTrue(module_0.move_one_ball([1, 2, 3, 4, 5]))

    def test_can_be_rotated_to_sorted(self):
        self.assertTrue(module_0.move_one_ball([3, 4, 5, 1, 2]))

    def test_can_be_rotated_to_sorted_two(self):
        self.assertTrue(module_0.move_one_ball([5, 1, 2, 3, 4]))

    def test_cannot_be_rotated_to_sorted(self):
        self.assertFalse(module_0.move_one_ball([3, 1, 4, 5, 2]))

    def test_cannot_be_rotated_to_sorted_two(self):
        self.assertFalse(module_0.move_one_ball([2, 1, 3, 5, 4]))

    def test_two_elements_sorted(self):
        self.assertTrue(module_0.move_one_ball([1, 2]))

    def test_two_elements_rotated(self):
        self.assertTrue(module_0.move_one_ball([2, 1]))

    def test_with_duplicates(self):
        self.assertTrue(module_0.move_one_ball([1, 1, 2, 3]))

    def test_with_duplicates_rotated(self):
        self.assertTrue(module_0.move_one_ball([3, 1, 1, 2]))

    def test_all_same_elements(self):
        self.assertTrue(module_0.move_one_ball([7, 7, 7, 7]))

    def test_negative_numbers(self):
        self.assertTrue(module_0.move_one_ball([-3, -2, -1, -5]))

    def test_negative_numbers_false(self):
        self.assertFalse(module_0.move_one_ball([-1, -3, -2, -5]))

    def test_mixed_positive_negative(self):
        self.assertTrue(module_0.move_one_ball([1, -1, 2]))

    def test_reverse_sorted(self):
        self.assertFalse(module_0.move_one_ball([5, 4, 3, 2, 1]))

    def test_large_array_rotated(self):
        self.assertTrue(module_0.move_one_ball(list(range(10, 100)) + list(range(10))))

    def test_large_array_not_rotatable(self):
        self.assertFalse(module_0.move_one_ball([2, 1] + list(range(3, 100))))


if __name__ == '__main__':
    unittest.main()

# Generated at 2026-11-02 20:06:07.925879
# Unit test for function move_one_ball
def test_move_one_ball():import unittest


class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(module_0.move_one_ball([]))

    def test_single_element(self):
        self.assertTrue(module_0.move_one_ball([5]))

    def test_two_elements_sorted(self):
        self.assertTrue(module_0.move_one_ball([1, 2]))

    def test_two_elements_rotatable(self):
        self.assertTrue(module_0.move_one_ball([2, 1]))

    def test_already_sorted(self):
        self.assertTrue(module_0.move_one_ball([1, 2, 3, 4, 5]))

    def test_rotatable_array(self):
        self.assertTrue(module_0.move_one_ball([3, 4, 5, 1, 2]))

    def test_rotatable_array_with_min_in_middle(self):
        self.assertTrue(module_0.move_one_ball([7, 1, 2, 3, 4, 5, 6]))

    def test_non_rotatable_array(self):
        self.assertFalse(module_0.move_one_ball([3, 1, 2, 5, 4]))

    def test_reverse_sorted(self):
        self.assertFalse(module_0.move_one_ball([5, 4, 3, 2, 1]))

    def test_duplicates_rotatable(self):
        self.assertTrue(module_0.move_one_ball([2, 3, 1, 1, 2]))

    def test_duplicates_non_rotatable(self):
        self.assertFalse(module_0.move_one_ball([2, 1, 3, 1]))

    def test_all_same_elements(self):
        self.assertTrue(module_0.move_one_ball([4, 4, 4, 4]))

    def test_negative_numbers_rotatable(self):
        self.assertTrue(module_0.move_one_ball([-3, -2, -5, -1]))

    def test_negative_numbers_non_rotatable(self):
        self.assertFalse(module_0.move_one_ball([-1, -5, -3, -2]))

    def test_mixed_positive_negative(self):
        self.assertTrue(module_0.move_one_ball([2, -1, 0, 1]))

    def test_min_at_end(self):
        self.assertTrue(module_0.move_one_ball([2, 3, 4, 1]))

    def test_min_at_start(self):
        self.assertTrue(module_0.move_one_ball([1, 3, 5, 2]))

    def test_large_rotatable(self):
        self.assertTrue(module_0.move_one_ball(list(range(10, 100)) + list(range(10))))

    def test_large_non_rotatable(self):
        self.assertFalse(module_0.move_one_ball(list(range(50, 100)) + list(range(0, 49))))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 20:07:01.660447
# Unit test for function move_one_ball
def test_move_one_ball():import unittest


class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(module_0.move_one_ball([]))

    def test_single_element(self):
        self.assertTrue(module_0.move_one_ball([5]))

    def test_two_elements_sorted(self):
        self.assertTrue(module_0.move_one_ball([1, 2]))

    def test_two_elements_rotatable(self):
        self.assertTrue(module_0.move_one_ball([2, 1]))

    def test_already_sorted(self):
        self.assertTrue(module_0.move_one_ball([1, 2, 3, 4, 5]))

    def test_rotatable_array(self):
        self.assertTrue(module_0.move_one_ball([3, 4, 5, 1, 2]))

    def test_rotatable_array_variant(self):
        self.assertTrue(module_0.move_one_ball([5, 1, 2, 3, 4]))

    def test_not_rotatable(self):
        self.assertFalse(module_0.move_one_ball([2, 1, 3, 5, 4]))

    def test_reverse_sorted_not_rotatable(self):
        self.assertFalse(module_0.move_one_ball([5, 4, 3, 2, 1]))

    def test_with_duplicates_rotatable(self):
        self.assertTrue(module_0.move_one_ball([2, 3, 1, 1, 2]))

    def test_with_duplicates_not_rotatable(self):
        self.assertFalse(module_0.move_one_ball([3, 1, 2, 1]))

    def test_all_same_elements(self):
        self.assertTrue(module_0.move_one_ball([7, 7, 7, 7]))

    def test_negative_numbers_rotatable(self):
        self.assertTrue(module_0.move_one_ball([-3, -2, -5, -4]))

    def test_negative_numbers_not_rotatable(self):
        self.assertFalse(module_0.move_one_ball([-1, -3, -2, -5]))

    def test_mixed_positive_negative(self):
        self.assertTrue(module_0.move_one_ball([0, -1, 1]))

    def test_large_rotatable_array(self):
        self.assertTrue(module_0.move_one_ball(list(range(10, 100)) + list(range(10))))

    def test_large_not_rotatable(self):
        self.assertFalse(module_0.move_one_ball(list(range(50)) + [100] + list(range(50, 100))))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 20:08:13.104418
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array should return True
    assert module_0.move_one_ball([]) == True

    # Already sorted array should return True
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Single element array should return True
    assert module_0.move_one_ball([7]) == True

    # Array that can be rotated once to become sorted
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True

    # Array rotated multiple positions
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True

    # Array that cannot be sorted by one rotation
    assert module_0.move_one_ball([2, 1, 3, 5, 4]) == False

    # Array with duplicates that can be rotated
    assert module_0.move_one_ball([3, 4, 1, 1, 2]) == False

    # Array with duplicates that is sorted
    assert module_0.move_one_ball([1, 1, 2, 3]) == True

    # Reverse sorted array cannot be fixed with one rotation
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False

    # Two element array that can be rotated
    assert module_0.move_one_ball([2, 1]) == True

    # Two element sorted array
    assert module_0.move_one_ball([1, 2]) == True

    # Negative numbers, can be rotated
    assert module_0.move_one_ball([-3, -2, -1, -5, -4]) == True

    # Negative numbers, cannot be rotated to sorted
    assert module_0.move_one_ball([-1, -3, -2]) == False

    # Large rotation (n-1 shifts)
    assert module_0.move_one_ball([2, 3, 4, 5, 1]) == True

    # Array with all same elements
    assert module_0.move_one_ball([7, 7, 7, 7]) == True

    print("All test cases passed!")

# Run tests
test_move_one_ball()