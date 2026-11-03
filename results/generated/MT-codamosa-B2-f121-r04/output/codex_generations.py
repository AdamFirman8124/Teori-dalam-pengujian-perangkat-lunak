

# Generated at 2026-11-02 14:19:07.144133
# Unit test for function solution
def test_solution():
    # Basic case: odd values at even indices
    assert module_0.solution([5, 8, 6, 4]) == 5
    assert module_0.solution([1, 2, 3, 4]) == 4  # 1 + 3
    assert module_0.solution([3, 3, 3, 3, 3]) == 9  # 3 + 3 + 3 (indices 0, 2, 4)

    # No odd values at even indices
    assert module_0.solution([2, 4, 6]) == 0
    assert module_0.solution([0, 6, 4, 4]) == 0

    # Empty list
    assert module_0.solution([]) == 0

    # Single element cases
    assert module_0.solution([7]) == 7
    assert module_0.solution([8]) == 0

    # Odd values at odd indices should be ignored
    assert module_0.solution([2, 1, 4, 3]) == 0

    # Negative odd numbers
    assert module_0.solution([-1, 2, -3, 4]) == -4  # -1 + -3

    # Larger mixed list
    assert module_0.solution([30, 46, 43, 34, 15, 98, 9]) == 67  # 43 + 15 + 9

# Generated at 2026-11-02 14:20:43.851713
# Unit test for function solution
def test_solution():
    assert module_0.solution([1, 2, 3]) == 4          # odd values at even indices: 1 + 3
    assert module_0.solution([1, 5, 2, 3]) == 5       # odd values at even indices: 1 + 5... -> 1 (idx0), 2 (idx2) -> 1 only? no: 1 + 5? idx1 is odd index
    assert module_0.solution([3, 3, 3, 3]) == 6       # indices 0 and 2 hold 3 each
    assert module_0.solution([30, 13, 24, 321]) == 0  # even-index values 30, 24 are even
    assert module_0.solution([5, 8]) == 5             # only index 0
    assert module_0.solution([2, 4, 6]) == 0          # all even values
    assert module_0.solution([]) == 0                 # empty list
    assert module_0.solution([1]) == 1                # single odd element at index 0
    assert module_0.solution([2]) == 0                # single even element
    assert module_0.solution([0, 1, 2, 3, 4, 5]) == 0 # even-index values 0, 2, 4 are all even
    assert module_0.solution([1, 3, 5, 7, 9]) == 15   # indices 0, 2, 4 -> 1 + 5 + 9
    assert module_0.solution([-1, 2, -3]) == -4       # negative odd values at even indices
    assert module_0.solution([7, 7, 7, 7, 7, 7]) == 21  # indices 0, 2, 4 -> 7 * 3

# Generated at 2026-11-02 14:21:49.744811
# Unit test for function solution
def test_solution():
    # Basic cases: odd elements at even indices
    assert module_0.solution([1, 2, 3]) == 1          # idx 0: 1 (odd, counted), idx 2: 3 (odd, counted)
    assert module_0.solution([3, 3, 3, 3, 3]) == 9    # idx 0, 2, 4 -> 3+3+3
    assert module_0.solution([0, 1, 2, 3, 4, 5]) == 0 # even values at even indices
    assert module_0.solution([5, 0, 5, 0, 5]) == 15   # odd values at even indices
    assert module_0.solution([1, 1, 1, 1]) == 2       # idx 0 and 2 -> 1+1

    # Odd values at odd indices should not be counted
    assert module_0.solution([2, 1, 2, 1, 2]) == 0    # odd values only at odd indices

    # Empty list
    assert module_0.solution([]) == 0

    # Single element list
    assert module_0.solution([1]) == 1
    assert module_0.solution([2]) == 0
    assert module_0.solution([0]) == 0

    # Negative numbers
    assert module_0.solution([-1, 2, -3]) == -4       # -1 and -3 are odd, at even indices
    assert module_0.solution([-2, -1, -4, -3]) == 0   # no odd values at even indices

    # Larger list
    assert module_0.solution(list(range(10))) == 1 + 5 + 9  # idx 0,2,4,6,8 -> 1+5+9
    assert module_0.solution([7] * 6) == 21                 # idx 0,2,4 -> 7*3

    # Mixed values
    assert module_0.solution([1, 2, 4, 5, 7, 8, 9]) == 17  # idx 0:1, idx 4:7, idx 6:9

    print("All tests passed!")

if __name__ == "__main__":
    test_solution()

# Generated at 2026-11-02 14:23:32.113258
# Unit test for function solution
def test_solution():import unittest


class TestSolution(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(module_0.solution([1, 2, 3]), 4)  # 1 (idx 0) + 3 (idx 2)

    def test_all_odd_at_even_indices(self):
        self.assertEqual(module_0.solution([1, 5, 3, 7, 9]), 13)  # 1 + 3 + 9

    def test_no_odd_at_even_indices(self):
        self.assertEqual(module_0.solution([2, 1, 4, 3, 6]), 0)

    def test_empty_list(self):
        self.assertEqual(module_0.solution([]), 0)

    def test_single_element_odd(self):
        self.assertEqual(module_0.solution([5]), 5)

    def test_single_element_even(self):
        self.assertEqual(module_0.solution([4]), 0)

    def test_odd_values_at_odd_indices_ignored(self):
        self.assertEqual(module_0.solution([0, 1, 0, 3]), 0)  # odds only at odd indices

    def test_mixed_values(self):
        self.assertEqual(module_0.solution([3, 3, 3, 3, 3]), 9)  # indices 0, 2, 4

    def test_even_values_at_even_indices_ignored(self):
        self.assertEqual(module_0.solution([2, 2, 2, 2]), 0)

    def test_negative_numbers(self):
        # In Python, -1 % 2 == 1, so negative odds count
        self.assertEqual(module_0.solution([-1, 2, -3]), -4)  # -1 + -3

    def test_zero_value(self):
        self.assertEqual(module_0.solution([0, 1, 2]), 0)  # 0 is even, not counted

    def test_large_list(self):
        lst = list(range(100))  # even indices: 0,2,...,98 -> odd values only 1,3,...,97
        self.assertEqual(module_0.solution(lst), sum(range(1, 100, 2)))  # 1+3+...+97 = 2401

    def test_returns_int(self):
        self.assertIsInstance(module_0.solution([1, 2, 3]), int)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 14:26:28.726323
# Unit test for function solution
def test_solution():
# nonce:2bd12fa9
    assert module_0.solution([1, 2, 3]) == 4          # 1 (idx 0) + 3 (idx 2)
    assert module_0.solution([3, 3, 3, 3, 3]) == 9    # 3 + 3 + 3 at indices 0, 2, 4
    assert module_0.solution([30, 13, 24, 321]) == 0  # even values at even indices
    assert module_0.solution([]) == 0                 # empty list
    assert module_0.solution([1]) == 1                # single odd element at idx 0
    assert module_0.solution([2]) == 0                # single even element at idx 0
    assert module_0.solution([5, 0, -4, 1, 3]) == 8   # 5 (idx 0) + 3 (idx 4)
    assert module_0.solution([2, 2, 2, 2]) == 0       # no odd values
    assert module_0.solution([0, 1, 0, 1, 0]) == 0    # odd values only at odd indices
    assert module_0.solution([1, 1, 1, 1, 1]) == 3    # 1 + 1 + 1 at indices 0, 2, 4
    assert module_0.solution([-3, -3, -3]) == -6      # negative odd values: -3 + -3