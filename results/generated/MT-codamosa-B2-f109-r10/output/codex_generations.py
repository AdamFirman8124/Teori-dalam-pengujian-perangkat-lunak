

# Generated at 2026-11-02 15:48:38.496458
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
        self.assertFalse(module_0.move_one_ball([3, 1, 2, 5, 4]))

    def test_reverse_sorted(self):
        self.assertFalse(module_0.move_one_ball([5, 4, 3, 2, 1]))

    def test_duplicates_rotatable(self):
        self.assertTrue(module_0.move_one_ball([2, 2, 3, 1, 2]))

    def test_all_duplicates(self):
        self.assertTrue(module_0.move_one_ball([7, 7, 7, 7]))

    def test_negative_numbers(self):
        self.assertTrue(module_0.move_one_ball([-3, -2, -5, -4]))

    def test_mixed_signs_not_rotatable(self):
        self.assertFalse(module_0.move_one_ball([1, -1, 2, -2]))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 15:50:09.514612
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array is considered sorted
    assert module_0.move_one_ball([]) == True

    # Already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Single element array
    assert module_0.move_one_ball([7]) == True

    # Two elements, rotated
    assert module_0.move_one_ball([2, 1]) == True
    assert module_0.move_one_ball([1, 2]) == True

    # Rotated sorted arrays (achievable via right shifts)
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True
    assert module_0.move_one_ball([4, 5, 1, 2, 3]) == True
    assert module_0.move_one_ball([2, 3, 1]) == True

    # Arrays that cannot be sorted by rotations
    assert module_0.move_one_ball([3, 5, 4, 1, 2]) == False
    assert module_0.move_one_ball([1, 3, 2]) == False
    assert module_0.move_one_ball([2, 1, 4, 3]) == False
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False

    # Arrays with duplicates
    assert module_0.move_one_ball([2, 2, 1]) == True
    assert module_0.move_one_ball([1, 1, 1]) == True
    assert module_0.move_one_ball([2, 1, 2]) == True

    # Negative numbers
    assert module_0.move_one_ball([-1, -5, -3]) == True
    assert module_0.move_one_ball([-3, -1, -5]) == False

    print("All tests passed!")

# Generated at 2026-11-02 15:51:59.805614
# Unit test for function move_one_ball
def test_move_one_ball():import unittest


class TestMoveOneBall(unittest.TestCase):

    def test_empty_array(self):
        self.assertTrue(module_0.move_one_ball([]))

    def test_single_element(self):
        self.assertTrue(module_0.move_one_ball([7]))

    def test_two_elements_sorted(self):
        self.assertTrue(module_0.move_one_ball([1, 2]))

    def test_two_elements_rotated(self):
        self.assertTrue(module_0.move_one_ball([2, 1]))

    def test_already_sorted(self):
        self.assertTrue(module_0.move_one_ball([1, 2, 3, 4, 5]))

    def test_rotated_once(self):
        self.assertTrue(module_0.move_one_ball([5, 1, 2, 3, 4]))

    def test_rotated_multiple(self):
        self.assertTrue(module_0.move_one_ball([3, 4, 5, 1, 2]))

    def test_not_sortable(self):
        self.assertFalse(module_0.move_one_ball([2, 3, 4, 1, 5]))

    def test_reverse_sorted(self):
        self.assertFalse(module_0.move_one_ball([5, 4, 3, 2, 1]))

    def test_all_duplicates(self):
        self.assertTrue(module_0.move_one_ball([1, 1, 1, 1]))

    def test_duplicates_rotatable(self):
        self.assertTrue(module_0.move_one_ball([2, 2, 1, 2]))

    def test_duplicates_not_rotatable(self):
        self.assertFalse(module_0.move_one_ball([2, 1, 2, 1]))

    def test_negative_numbers(self):
        self.assertTrue(module_0.move_one_ball([-3, -2, -5, -4, -1]) is False)
        self.assertTrue(module_0.move_one_ball([-5, -4, -3, -2, -1]))

    def test_mixed_signs_rotatable(self):
        self.assertTrue(module_0.move_one_ball([2, 3, -1, 0, 1]))

    def test_mixed_signs_not_rotatable(self):
        self.assertFalse(module_0.move_one_ball([3, -1, 2, 0, 1]))

    def test_large_rotated_array(self):
        self.assertTrue(module_0.move_one_ball(list(range(50, 100)) + list(range(0, 50))))

    def test_large_unsorted_array(self):
        self.assertFalse(module_0.move_one_ball(list(range(50, 100)) + list(range(0, 49)) + [99]))

    def test_rotation_at_last_position(self):
        self.assertTrue(module_0.move_one_ball([2, 3, 4, 5, 1]))

    def test_min_at_middle_breaks_order(self):
        self.assertFalse(module_0.move_one_ball([1, 5, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 15:53:45.796288
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array should return True
    assert module_0.move_one_ball([]) == True

    # Single element array should return True
    assert module_0.move_one_ball([5]) == True

    # Already sorted array should return True
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Array that can be sorted with one right shift
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True

    # Array that can be sorted with one right shift (rotation at end)
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True

    # Array that cannot be sorted with one right shift
    assert module_0.move_one_ball([3, 1, 2, 5, 4]) == False

    # Array with duplicates that can be sorted
    assert module_0.move_one_ball([2, 3, 1, 1, 2]) == False

    # Array with all identical elements should return True
    assert module_0.move_one_ball([7, 7, 7, 7]) == True

    # Two element array - sortable
    assert module_0.move_one_ball([2, 1]) == True

    # Two element array - already sorted
    assert module_0.move_one_ball([1, 2]) == True

    # Unsorted array with multiple inversions
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False

    # Array rotated multiple positions
    assert module_0.move_one_ball([4, 5, 1, 2, 3]) == True

    # Negative numbers - sortable rotation
    assert module_0.move_one_ball([-3, -2, -5, -4]) == False

    # Negative numbers - already sorted
    assert module_0.move_one_ball([-5, -4, -3, -2]) == True

    # Mixed positive and negative numbers
    assert module_0.move_one_ball([-1, 0, 1, -2]) == False

    # Large array that is a valid rotation of sorted array
    assert module_0.move_one_ball([8, 9, 10, 1, 2, 3, 4, 5, 6, 7]) == True

    # Large array that is not a valid rotation
    assert module_0.move_one_ball([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False

    print("All tests passed!")

test_move_one_ball()

# Generated at 2026-11-02 15:57:39.032448
# Unit test for function move_one_ball
def test_move_one_ball():
    # Empty array
    assert module_0.move_one_ball([]) == True

    # Single element
    assert module_0.move_one_ball([5]) == True

    # Already sorted array
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Rotated sorted array (one right shift)
    assert module_0.move_one_ball([5, 1, 2, 3, 4]) == True

    # Rotated sorted array (multiple shifts)
    assert module_0.move_one_ball([3, 4, 5, 1, 2]) == True

    # Rotated sorted array (full rotation back to sorted)
    assert module_0.move_one_ball([1, 2, 3, 4, 5]) == True

    # Two elements in reverse (can be sorted with one shift)
    assert module_0.move_one_ball([2, 1]) == True

    # Array that cannot be sorted by rotations
    assert module_0.move_one_ball([3, 1, 2, 5, 4]) == False

    # Array with multiple inversions
    assert module_0.move_one_ball([2, 3, 1, 5, 4]) == False

    # Array with duplicates that is a valid rotation
    assert module_0.move_one_ball([3, 3, 1, 2, 3]) == True

    # Array with duplicates that cannot be sorted by rotation
    assert module_0.move_one_ball([2, 1, 3, 1, 2]) == False

    # Descending order array (only sortable if length <= 2)
    assert module_0.move_one_ball([5, 4, 3, 2, 1]) == False
    assert module_0.move_one_ball([2, 1]) == True

    # Negative numbers, valid rotation
    assert module_0.move_one_ball([-2, -1, 0, -4, -3]) == True

    # Negative numbers, invalid rotation
    assert module_0.move_one_ball([-1, -3, -2, 0, -4]) == False

    # Array where min value appears multiple times
    assert module_0.move_one_ball([1, 1, 2, 3, 1]) == True

    # Large array rotated
    assert module_0.move_one_ball(list(range(50, 100)) + list(range(0, 50))) == True

    # Large array not rotatable
    assert module_0.move_one_ball(list(range(0, 50)) + [99] + list(range(51, 99))) == False