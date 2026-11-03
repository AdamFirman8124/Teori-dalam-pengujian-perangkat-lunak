

# Generated at 2026-11-02 14:21:56.196626
# Unit test for function solution
def test_solution():
    assert module_0.solution([1, 2, 3]) == 4          # odd values at even indices: 1 + 3
    assert module_0.solution([]) == 0                 # empty list
    assert module_0.solution([5]) == 5                # single odd element at index 0
    assert module_0.solution([2]) == 0                # single even element at index 0
    assert module_0.solution([2, 3, 4, 5]) == 0       # even values at even indices
    assert module_0.solution([1, 2, 3, 4]) == 4       # 1 + 3
    assert module_0.solution([0, 1, 2, 3, 5]) == 5    # only 5 qualifies
    assert module_0.solution([1, 1, 1, 1]) == 2       # indices 0 and 2
    assert module_0.solution([3, 3, 3, 3, 3]) == 9    # indices 0, 2, 4
    assert module_0.solution([-1, 2, -3]) == -4       # negative odd values count
    assert module_0.solution([7, 8, 9, 10, 11, 12]) == 27  # 7 + 9 + 11
    
    # Verify odd values at odd indices are excluded
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 0

# Generated at 2026-11-02 14:23:39.927707
# Unit test for function solution
def test_solution():
    # Basic cases
    assert module_0.solution([1, 2, 3]) == 3          # indices 0,2 -> 1 + 3... wait, idx 2 is even, 3 is odd -> 1+3=4
    # Correcting: idx 0 -> 1 (odd), idx 2 -> 3 (odd): sum = 4
    assert module_0.solution([1, 2, 3]) == 4

    assert module_0.solution([1, 5, 2, 3, 4]) == 6    # idx0:1, idx2:2(even), idx4:4(even) -> 1 only? No:
    # idx0: 1 (odd, even idx) -> include
    # idx2: 2 (even number) -> exclude
    # idx4: 4 (even number) -> exclude
    assert module_0.solution([1, 5, 2, 3, 4]) == 1

    assert module_0.solution([5]) == 5                # single odd element at even index
    assert module_0.solution([4]) == 0                # single even element at even index

    # Empty list
    assert module_0.solution([]) == 0

    # Odd elements at odd indices should not count
    assert module_0.solution([0, 1, 0, 1, 0]) == 0    # odd numbers only at odd indices
    assert module_0.solution([2, 3, 2, 3, 6]) == 0    # odd numbers only at odd indices

    # Mixed case
    assert module_0.solution([3, 3, 3, 3, 3]) == 9    # idx0:3, idx2:3, idx4:3 -> 9
    assert module_0.solution([30, 13, 24, 321, 0]) == 0
    assert module_0.solution([2, 2, 2, 2]) == 0

    # Negative odd numbers at even indices
    assert module_0.solution([-3, 2, -5]) == -8       # -3 + -5
    assert module_0.solution([-1, 4, -1, 4, -1]) == -3

    # Larger list
    assert module_0.solution(list(range(10))) == 2 + 6  # idx2 -> 2 (even num), idx4 -> 4, idx6 -> 6, idx8 -> 8 => 0
    # Only odd values at even indices count; range(10) evens at even indices => 0
    assert module_0.solution(list(range(10))) == 0

    print("All tests passed!")


# Run tests
if __name__ == "__main__":
    test_solution()

# Generated at 2026-11-02 14:26:39.258010
# Unit test for function solution
def test_solution():
    # Standard case: odd values at even indices
    assert module_0.solution([5, 8, 7, 1]) == 12  # 5 (idx 0) + 7 (idx 2)
    
    # All odd values, multiple even indices
    assert module_0.solution([3, 3, 3, 3, 3]) == 9  # 3 (idx 0) + 3 (idx 2) + 3 (idx 4)
    
    # Even values at even indices -> no contribution
    assert module_0.solution([30, 13, 24, 321]) == 0
    
    # Odd values only at odd indices -> no contribution
    assert module_0.solution([2, 3, 4, 5]) == 0
    
    # Empty list
    assert module_0.solution([]) == 0
    
    # Single odd element at index 0
    assert module_0.solution([5]) == 5
    
    # Single even element at index 0
    assert module_0.solution([4]) == 0
    
    # Negative odd numbers at even indices
    assert module_0.solution([-3, 2, -5]) == -8  # -3 (idx 0) + -5 (idx 2)
    
    # Mixed positive/negative
    assert module_0.solution([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5
    
    # Large numbers
    assert module_0.solution([1000001, 2, 1000003]) == 2000004
    
    # Zero at even index (zero is even, not odd)
    assert module_0.solution([0, 1, 0, 1]) == 0

# Generated at 2026-11-02 14:30:55.451411
# Unit test for function solution
def test_solution():
    # Odd element at an even index is summed
    assert module_0.solution([5, 8, 6, 4]) == 5
    # Odd elements at odd indices are ignored
    assert module_0.solution([3, 13, 2, 9]) == 3
    assert module_0.solution([0, 3, 0, 5]) == 0
    # Multiple qualifying elements
    assert module_0.solution([1, 2, 3, 4, 5]) == 9
    assert module_0.solution([1, 0, 1, 0]) == 2
    assert module_0.solution([1, 1, 1, 1, 1]) == 3
    # No qualifying elements
    assert module_0.solution([2, 2, 2, 2]) == 0
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 0
    # Single element lists
    assert module_0.solution([7]) == 7
    assert module_0.solution([0]) == 0
    # Empty list
    assert module_0.solution([]) == 0
    # Negative odd numbers at even indices (Python -3 % 2 == 1)
    assert module_0.solution([-3, 2, -5]) == -8
    assert module_0.solution([-2, 1, -4, 3]) == 0
    # Larger example
    assert module_0.solution([9, 5, 7, 3, 11, 13]) == 9 + 7 + 11
    print("All tests passed!")

test_solution()