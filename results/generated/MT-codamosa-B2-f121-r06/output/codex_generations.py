

# Generated at 2026-11-02 14:05:46.175043
# Unit test for function solution
def test_solution():
    assert module_0.solution([5, 8, 6, 4]) == 5
    assert module_0.solution([1, 2, 3, 4]) == 1 + 3
    assert module_0.solution([3, 3, 3, 3, 3]) == 9
    assert module_0.solution([30, 13, 24, 321]) == 0
    assert module_0.solution([5, 5, 5]) == 10
    assert module_0.solution([]) == 0
    assert module_0.solution([0, 1, 2, 3, 4, 5]) == 0 + 4
    assert module_0.solution([2, 4, 6, 8]) == 0
    assert module_0.solution([1]) == 1
    assert module_0.solution([2]) == 0
    assert module_0.solution([-1, -2, -3]) == -1 + (-3)
    assert module_0.solution([7, 2, 9, 4, 1, 6]) == 7 + 9 + 1

# Generated at 2026-11-02 14:07:01.503064
# Unit test for function solution
def test_solution():
    # Test with mixed odd/even numbers at even and odd indices
    assert module_0.solution([1, 2, 3, 4]) == 4  # indices 0 (1) and 2 (3), both odd: 1+3=4
    
    # Test with all even numbers
    assert module_0.solution([2, 4, 6, 8]) == 0
    
    # Test with all odd numbers
    assert module_0.solution([1, 3, 5, 7]) == 1 + 5  # only even indices contribute
    
    # Test with empty list
    assert module_0.solution([]) == 0
    
    # Test with single element (odd at index 0)
    assert module_0.solution([5]) == 5
    
    # Test with single element (even at index 0)
    assert module_0.solution([4]) == 0
    
    # Test with negative odd numbers at even indices
    assert module_0.solution([-1, 2, -3, 4]) == -1 + (-3)
    
    # Test with zeros
    assert module_0.solution([0, 1, 0, 3]) == 0
    
    # Test edge case: odd numbers only at odd indices
    assert module_0.solution([2, 3, 4, 5]) == 0
    
    # Test larger list
    assert module_0.solution([1, 1, 1, 1, 1]) == 3  # indices 0, 2, 4 contribute
    
    # Test with negative even numbers
    assert module_0.solution([-2, 3, -4, 5, -6, 7]) == 0  # no odd at even indices
    
    print("All tests passed!")

# nonce:93728047

# Generated at 2026-11-02 14:08:45.008972
# Unit test for function solution
def test_solution():
    # Elements at even indices that are odd values are summed
    assert module_0.solution([1, 2, 3]) == 4          # 1 (idx 0) + 3 (idx 2)
    assert module_0.solution([5, 8, 7, 1]) == 12      # 5 (idx 0) + 7 (idx 2)
    assert module_0.solution([3, 3, 3, 3, 3]) == 9    # 3 (idx 0) + 3 (idx 2) + 3 (idx 4)
    assert module_0.solution([30, 13, 24, 321]) == 0  # even-index elements are even
    assert module_0.solution([]) == 0                 # empty list
    assert module_0.solution([2, 4, 6]) == 0          # all even values
    assert module_0.solution([1]) == 1                # single odd element at idx 0
    assert module_0.solution([0, 1, 0, 1, 0]) == 0    # even values at even indices
    assert module_0.solution([7, 2, 9, 4, 1, 6, 3]) == 20  # 7 + 9 + 1 + 3
    assert module_0.solution([-1, 2, -3]) == -4       # negative odd values at even indices

# Generated at 2026-11-02 14:10:31.686200
# Unit test for function solution
def test_solution():
    # Odd elements at even indices are summed
    assert module_0.solution([1, 2, 3]) == 4          # 1 + 3
    assert module_0.solution([1, 5, 3, 1]) == 4       # 1 + 3 (odd indices skipped)
    assert module_0.solution([1, 2, 3, 4, 5, 6, 7]) == 16  # 1 + 3 + 5 + 7

    # Odd element only at odd index contributes nothing
    assert module_0.solution([2, 3, 4]) == 0
    assert module_0.solution([0, 1, 2, 3, 4, 5]) == 0      # even values at even indices

    # All even numbers
    assert module_0.solution([2, 4, 6, 8]) == 0

    # All odd numbers
    assert module_0.solution([3, 3, 3, 3, 3]) == 9         # indices 0, 2, 4

    # Single element list
    assert module_0.solution([5]) == 5
    assert module_0.solution([4]) == 0

    # Empty list
    assert module_0.solution([]) == 0

    # Negative odd numbers (Python: -1 % 2 == 1)
    assert module_0.solution([-1, -2, -3]) == -4           # -1 + -3
    assert module_0.solution([-1, 1, -1, 1]) == -2

# Generated at 2026-11-02 14:12:02.493291
# Unit test for function solution
def test_solution():
    # nonce:47dffc13
    # Empty list
    assert module_0.solution([]) == 0

    # Odd elements at even indices
    assert module_0.solution([1, 2, 3]) == 4          # 1 + 3
    assert module_0.solution([1, 3, 5]) == 6          # 1 + 5
    assert module_0.solution([3, 3, 3, 3, 3]) == 9    # 3 + 3 + 3 (indices 0, 2, 4)

    # Even elements at even indices contribute nothing
    assert module_0.solution([0, 1, 2, 3]) == 0
    assert module_0.solution([2, 4, 6, 8]) == 0

    # Odd elements at odd indices are ignored
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 0

    # Mixed case
    assert module_0.solution([5, 8, 7, 1]) == 12      # 5 + 7
    assert module_0.solution([10, 9, 8, 7, 6, 5]) == 8  # 8 (index 2) is even... wait

    # Recompute: indices 0,2,4 -> 10, 8, 6 all even -> 0
    assert module_0.solution([10, 9, 8, 7, 6, 5]) == 0

    # Negative odd numbers at even indices
    assert module_0.solution([-1, 2, -3]) == -4       # -1 + -3
    assert module_0.solution([-2, 1, -4, 3]) == 0

    # Single element list
    assert module_0.solution([7]) == 7
    assert module_0.solution([8]) == 0

    # Zero is even, contributes nothing
    assert module_0.solution([0]) == 0

    # Larger example
    assert module_0.solution([1, 2, 3, 4, 5, 6, 7]) == 16  # 1 + 3 + 5 + 7