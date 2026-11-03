

# Generated at 2026-11-03 01:12:47.936095
# Unit test for function add
def test_add():
    # nonce:1deae6c8
    # Basic case from problem description
    assert module_0.add([4, 2, 6, 7]) == 2, "Expected 2 for [4, 2, 6, 7]"
    
    # Empty list
    assert module_0.add([]) == 0, "Expected 0 for empty list"
    
    # Single element list (no odd indices)
    assert module_0.add([2]) == 0, "Expected 0 for [2]"
    
    # No even elements at odd indices
    assert module_0.add([1, 3, 5, 7]) == 0, "Expected 0 for [1, 3, 5, 7]"
    
    # All even elements at odd indices
    assert module_0.add([1, 2, 3, 4, 5, 6]) == 12, "Expected 12 for [1, 2, 3, 4, 5, 6]"
    
    # Even element at odd index mixed with odd
    assert module_0.add([0, 2, 1, 3, 9, 8]) == 10, "Expected 10 for [0, 2, 1, 3, 9, 8]"
    
    # Two elements, even at index 1
    assert module_0.add([1, 4]) == 4, "Expected 4 for [1, 4]"
    
    # Two elements, odd at index 1
    assert module_0.add([1, 5]) == 0, "Expected 0 for [1, 5]"
    
    # Negative even numbers at odd indices
    assert module_0.add([1, -2, 3, -4]) == -6, "Expected -6 for [1, -2, 3, -4]"
    
    # Zero is even
    assert module_0.add([1, 0, 2, 0]) == 0, "Expected 0 for [1, 0, 2, 0]"
    
    print("All tests passed!")

test_add()

# Generated at 2026-11-03 01:13:38.930765
# Unit test for function add
def test_add():
    # nonce:2d27cbac
    # Even elements at odd indices are summed
    assert module_0.add([4, 2, 6, 7]) == 2      # only lst[1]=2 is even at odd index
    assert module_0.add([1, 2, 3, 4]) == 6      # lst[1]=2, lst[3]=4
    assert module_0.add([0, 4, 1, 8, 5, 10]) == 22  # 4 + 8 + 10

    # No even elements at odd indices
    assert module_0.add([1, 3, 5, 7]) == 0
    assert module_0.add([2, 1, 4, 3, 6, 5]) == 0

    # Empty list
    assert module_0.add([]) == 0

    # Single element (no odd indices)
    assert module_0.add([2]) == 0

    # Zero is even
    assert module_0.add([1, 0, 3, 0]) == 0

    # Negative numbers
    assert module_0.add([-1, -4, -3, -6]) == -10
    assert module_0.add([-1, -3, -2]) == 0

    # Longer list
    assert module_0.add(list(range(10))) == 2 + 4 + 6 + 8  # 20

    print("All tests passed!")


if __name__ == "__main__":
    test_add()

# Generated at 2026-11-03 01:14:39.443155
# Unit test for function add
def test_add():
    # Even elements at odd indices are summed
    assert module_0.add([1, 2, 3, 4, 5, 6]) == 12  # 2 + 4 + 6
    assert module_0.add([1, 4, 3, 8, 5, 12]) == 24  # 4 + 8 + 12
    assert module_0.add([1, 2]) == 2
    # No even elements at odd indices
    assert module_0.add([2, 3, 4, 5]) == 0
    assert module_0.add([7, 7, 7, 7]) == 0
    # Empty list
    assert module_0.add([]) == 0
    # Single element (no odd indices)
    assert module_0.add([2]) == 0
    # Zero counts as even
    assert module_0.add([1, 0, 3, 0]) == 0
    # Negative even numbers at odd indices
    assert module_0.add([1, -2, 3, -4]) == -6

# Generated at 2026-11-03 01:15:14.676848
# Unit test for function add
def test_add():import unittest


class TestAdd(unittest.TestCase):
    def test_basic_mixed(self):
        # 2 at index 1 is even -> included; 4 at index 3 is even -> included
        self.assertEqual(module_0.add([1, 2, 3, 4]), 6)

    def test_mixed_even_odd_indices(self):
        # indices 1,3,5: values 2, 5, 4 -> only 2 and 4 are even
        self.assertEqual(module_0.add([1, 2, 4, 5, 6, 4]), 6)

    def test_no_even_at_odd_indices(self):
        self.assertEqual(module_0.add([1, 3, 5, 7]), 0)

    def test_all_even_at_odd_indices(self):
        self.assertEqual(module_0.add([1, 2, 3, 4, 5, 6]), 12)

    def test_empty_list(self):
        self.assertEqual(module_0.add([]), 0)

    def test_single_element(self):
        self.assertEqual(module_0.add([2]), 0)

    def test_two_elements_even_at_index_one(self):
        self.assertEqual(module_0.add([1, 4]), 4)

    def test_two_elements_odd_at_index_one(self):
        self.assertEqual(module_0.add([1, 3]), 0)

    def test_with_zero(self):
        # 0 is even
        self.assertEqual(module_0.add([1, 0, 2, 0]), 0)

    def test_negative_numbers(self):
        # -2 and -4 are even
        self.assertEqual(module_0.add([1, -2, 3, -4]), -6)

    def test_large_list(self):
        lst = [0] * 10
        lst[1] = 2
        lst[3] = 4
        lst[5] = 5  # odd, excluded
        lst[7] = 6
        lst[9] = 8
        self.assertEqual(module_0.add(lst), 20)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-03 01:16:06.379749
# Unit test for function add
def test_add():import pytest


def test_add_basic():
    # Even elements at odd indices: lst[1]=2, lst[3]=4 → 2+4=6
    assert module_0.add([1, 2, 3, 4]) == 6


def test_add_mixed():
    # Odd indices: lst[1]=2 (even), lst[3]=1 (odd), lst[5]=4 (even) → 2+4=6
    assert module_0.add([1, 2, 4, 1, 5, 4]) == 6


def test_add_empty():
    assert module_0.add([]) == 0


def test_add_single_element():
    assert module_0.add([2]) == 0  # Only index 0, not included


def test_add_no_even_at_odd_indices():
    assert module_0.add([1, 3, 5, 7, 9]) == 0


def test_add_all_even_at_odd_indices():
    # lst[1]=2, lst[3]=4, lst[5]=6, lst[7]=8 → 20
    assert module_0.add([0, 2, 0, 4, 0, 6, 0, 8]) == 20


def test_add_negative_numbers():
    # lst[1]=-2 (even), lst[3]=-4 (even) → -6
    assert module_0.add([1, -2, 3, -4]) == -6


def test_add_zero_at_odd_index():
    # lst[1]=0 is even → 0
    assert module_0.add([1, 0]) == 0


def test_add_large_list():
    # Odd indices 1,3,5: values 2, 4, 6 → 12
    assert module_0.add([1, 2, 3, 4, 5, 6]) == 12