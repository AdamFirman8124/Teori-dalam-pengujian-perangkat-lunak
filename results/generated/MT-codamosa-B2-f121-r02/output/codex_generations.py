

# Generated at 2026-11-02 09:41:00.257357
# Unit test for function solution
def test_solution():
    # Basic case: odd numbers at even indices
    assert module_0.solution([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5

def test_solution_empty():
    # Empty list should return 0
    assert module_0.solution([]) == 0

def test_solution_no_odd_at_even_idx():
    # No odd numbers at even indices
    assert module_0.solution([2, 3, 4, 5, 6]) == 0

def test_solution_all_odd():
    # All odd numbers at even indices
    assert module_0.solution([1, 1, 1, 1]) == 2  # indices 0 and 2

def test_solution_single_element():
    # Single odd element at index 0
    assert module_0.solution([7]) == 7

def test_solution_single_even_element():
    # Single even element at index 0
    assert module_0.solution([8]) == 0

def test_solution_negative_numbers():
    # Negative odd numbers at even indices
    assert module_0.solution([-1, 2, -3, 4, -5]) == -9

def test_solution_odd_at_odd_idx():
    # Odd numbers at odd indices should be ignored
    assert module_0.solution([2, 1, 2, 3, 2, 5]) == 0

def test_solution_zero():
    # Zero is even, should be ignored
    assert module_0.solution([0, 1, 0, 3]) == 0

def test_solution_large_numbers():
    # Works with larger numbers
    assert module_0.solution([101, 2, 103, 4, 105]) == 309

def test_solution_mixed():
    # Mixed case
    assert module_0.solution([3, 3, 3, 3, 3, 3]) == 9  # indices 0, 2, 4

# Generated at 2026-11-02 09:42:23.716392
# Unit test for function solution
def test_solution():
    # nonce:6413f74d
    # Basic case: odd values at even indices
    assert module_0.solution([5, 15, 0, 4, 31]) == 36  # 5 + 31
    assert module_0.solution([1, 2, 3, 4]) == 4        # 1 + 3
    # Empty list
    assert module_0.solution([]) == 0
    # No odd values at even indices
    assert module_0.solution([2, 4, 6]) == 0
    assert module_0.solution([2, 1, 4, 3]) == 0
    # All odd values at even indices
    assert module_0.solution([3, 3, 3, 3]) == 6        # 3 + 3
    assert module_0.solution([1, 2, 5, 4, 7, 6]) == 13 # 1 + 5 + 7
    # Odd value at odd index should be ignored
    assert module_0.solution([0, 1, 0, 3]) == 0
    # Single element list
    assert module_0.solution([7]) == 7
    assert module_0.solution([8]) == 0
    # Negative odd values
    assert module_0.solution([-3, 2, -5, 4]) == -8     # -3 + -5
    # Zero is even, should be ignored
    assert module_0.solution([0, 1, 0, 1]) == 0

# Generated at 2026-11-02 09:43:30.313546
# Unit test for function solution
def test_solution():
    assert module_0.solution([5, 8, 6, 4]) == 5
    assert module_0.solution([1, 2, 3, 4]) == 4
    assert module_0.solution([2, 4, 6]) == 0
    assert module_0.solution([]) == 0
    assert module_0.solution([3, 3, 3, 3, 3]) == 9
    assert module_0.solution([0, 1, 2, 3, 4, 5]) == 0
    assert module_0.solution([7]) == 7
    assert module_0.solution([1, 100, 3, 100, 5]) == 9
    assert module_0.solution([2, 2, 2, 2, 2]) == 0
    assert module_0.solution([-1, -3, -5, -7]) == -6
    assert module_0.solution([10, 3, 20, 5, 30, 7]) == 60
    assert module_0.solution([0]) == 0

# Generated at 2026-11-02 09:44:46.257077
# Unit test for function solution
def test_solution():
    # Basic case: odd numbers at even indices
    assert module_0.solution([1, 2, 3]) == 4  # 1 (idx 0) + 3 (idx 2)
    assert module_0.solution([1, 5, 3]) == 4
    assert module_0.solution([5, 4, 3, 2, 1]) == 9  # 5 (idx 0) + 3 (idx 2) + 1 (idx 4)

    # No odd numbers at even indices
    assert module_0.solution([2, 1, 4, 3, 6]) == 0
    assert module_0.solution([0, 1, 2, 3, 4, 5]) == 0

    # All even numbers
    assert module_0.solution([2, 4, 6, 8]) == 0

    # All odd numbers
    assert module_0.solution([1, 1, 1, 1]) == 2  # idx 0 and idx 2
    assert module_0.solution([3, 3, 3, 3, 3]) == 9  # idx 0, 2, 4

    # Empty list
    assert module_0.solution([]) == 0

    # Single element: odd
    assert module_0.solution([7]) == 7

    # Single element: even
    assert module_0.solution([4]) == 0

    # Odd numbers only at odd indices should not count
    assert module_0.solution([2, 3, 2, 5, 2]) == 0

    # Negative numbers: -1 % 2 == 1 in Python, so negatives count as odd
    assert module_0.solution([-1, 2, -3]) == -4
    assert module_0.solution([-2, -1, -4, -3]) == 0  # odd values at odd indices only

    # Larger mixed list
    assert module_0.solution([1, 2, 3, 4, 5, 6, 7]) == 16  # 1 + 3 + 5 + 7

    # Zero in list
    assert module_0.solution([0, 0, 0]) == 0

    # Duplicates
    assert module_0.solution([9, 9, 9]) == 18  # idx 0 and 2

    print("All test_solution tests passed!")


if __name__ == "__main__":
    test_solution()

# Generated at 2026-11-02 09:46:03.137927
# Unit test for function solution
def test_solution():
    # Basic cases: odd values at even indices
    assert module_0.solution([5, 8, 6, 1]) == 5          # only 5 at idx 0 qualifies
    assert module_0.solution([3, 13, 2, 9]) == 3         # only 3 at idx 0 qualifies
    assert module_0.solution([1, 2, 3, 4]) == 4          # 1 (idx 0) + 3 (idx 2)
    assert module_0.solution([1, 1, 1, 1, 1]) == 3       # 1 + 1 + 1 at idx 0, 2, 4

    # Edge cases
    assert module_0.solution([]) == 0                    # empty list
    assert module_0.solution([7]) == 7                   # single odd element at idx 0
    assert module_0.solution([4]) == 0                   # single even element
    assert module_0.solution([2, 3, 4, 5, 6, 7]) == 0    # even values at even indices
    assert module_0.solution([2, 1, 4, 3]) == 0          # odd values only at odd indices

    # Negative numbers (Python: -3 % 2 == 1, so negative odds qualify)
    assert module_0.solution([-3, 2, -5, 4]) == -8       # -3 (idx 0) + -5 (idx 2)
    assert module_0.solution([-2, -1, -4, -3]) == 0      # even values at even indices

    # Larger mixed case
    assert module_0.solution([1, 0, 1, 0, 9, 0, 7]) == 17  # 1 + 1 + 9 + 7