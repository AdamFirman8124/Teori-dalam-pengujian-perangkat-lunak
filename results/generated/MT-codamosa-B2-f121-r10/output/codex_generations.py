

# Generated at 2026-11-01 20:04:56.816647
# Unit test for function solution
def test_solution():
    # Empty list -> sum is 0
    assert module_0.solution([]) == 0

    # Single element cases
    assert module_0.solution([5]) == 5          # even index, odd value
    assert module_0.solution([4]) == 0          # even index, even value
    assert module_0.solution([0]) == 0

    # Provided-style examples
    assert module_0.solution([5, 8, 6, 4]) == 5
    assert module_0.solution([15, 31, 32, 20]) == 15
    assert module_0.solution([30, 46, 42, 24]) == 0

    # Mixed values: only even-indexed odd numbers count
    assert module_0.solution([1, 2, 3, 4]) == 4       # 1 (idx 0) + 3 (idx 2)
    assert module_0.solution([1, 3, 5, 7, 9]) == 15   # all odd, even indices 0,2,4
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 10  # 2+4+6 at even indices (all even)

    # Odd values at odd indices must be ignored
    assert module_0.solution([0, 1, 0, 3, 0, 5]) == 0

    # Negative numbers: -1 % 2 == 1 in Python, so it counts as odd
    assert module_0.solution([-1, 2, -3]) == -4       # -1 (idx 0) + -3 (idx 2)
    assert module_0.solution([-2, -3, -4]) == -6      # -2 + -4 at even indices

    # Larger list
    assert module_0.solution(list(range(100))) == sum(x for x in range(100) if x % 2 == 1 and x % 2 != 0 and False or (x % 2 == 1 and x % 2 == 1)) if False else solution_check_helper()

# Generated at 2026-11-01 20:05:18.016868
# Unit test for function solution
def test_solution():
    # Typical cases: sum of odd elements at even indices
    assert module_0.solution([5, 8, 6, 4]) == 5
    assert module_0.solution([1, 2, 3, 4]) == 4          # 1 + 3
    assert module_0.solution([0, 1, 2, 3, 4]) == 6       # 0 + 2 + 4
    assert module_0.solution([3, 3, 3, 3]) == 6          # indices 0 and 2: 3 + 3

    # Empty list
    assert module_0.solution([]) == 0

    # Single element
    assert module_0.solution([7]) == 7
    assert module_0.solution([8]) == 0                   # even element at even index

    # Odd elements only at odd indices contribute nothing
    assert module_0.solution([2, 5, 4, 7]) == 0

    # Negative odd numbers
    assert module_0.solution([-3, 2, -5, 4]) == -8       # -3 + -5

    # Mixed signs
    assert module_0.solution([1, -1, 3, -3]) == 4        # 1 + 3

    # Larger list
    assert module_0.solution(list(range(10))) == 20      # 1 + 3 + 5 + 7 + 9

    # Duplicates and zeros
    assert module_0.solution([0, 0, 0, 0]) == 0
    assert module_0.solution([9, 9, 9]) == 18            # indices 0 and 2

# Generated at 2026-11-01 20:05:40.132211
# Unit test for function solution
def test_solution():
    # Test with empty list
    assert module_0.solution([]) == 0
    
    # Test with single element - odd value at even index
    assert module_0.solution([1]) == 1
    
    # Test with single element - even value at even index
    assert module_0.solution([2]) == 0
    
    # Test with mixed values
    assert module_0.solution([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5
    
    # Test with all odd values at even indices
    assert module_0.solution([3, 3, 3, 3, 3]) == 9  # 3 + 3 + 3
    
    # Test with all even values
    assert module_0.solution([2, 4, 6, 8]) == 0
    
    # Test where odd values only appear at odd indices
    assert module_0.solution([2, 3, 4, 5, 6]) == 0
    
    # Test with negative numbers
    assert module_0.solution([-1, 2, -3, 4, -5]) == -9  # -1 + (-3) + (-5)
    
    # Test with zero values
    assert module_0.solution([0, 1, 0, 3, 0]) == 0
    
    # Test with larger list
    assert module_0.solution(list(range(10))) == 20  # 1 + 3 + 5 + 7 + 9
    
    print("All tests passed!")

if __name__ == "__main__":
    test_solution()

# Generated at 2026-11-01 20:06:09.214137
# Unit test for function solution
def test_solution():
    # Empty list returns 0
    assert module_0.solution([]) == 0

    # Single element, odd value at even index
    assert module_0.solution([1]) == 1

    # Single element, even value at even index
    assert module_0.solution([2]) == 0

    # Classic example: indices 0 and 2 are even, values 1 and 3 are odd
    assert module_0.solution([1, 2, 3]) == 4

    # All elements odd, but only even indices count
    assert module_0.solution([3, 3, 3, 3]) == 6

    # Odd values at odd indices should be ignored
    assert module_0.solution([5, 8, 2, 1]) == 5

    # Even values at even indices contribute nothing
    assert module_0.solution([0, 1, 2]) == 0

    # Negative odd numbers count as odd
    assert module_0.solution([-1, 4, -3, 6]) == -4

    # No odd values at all
    assert module_0.solution([2, 4, 6, 8]) == 0

    # Mixed list with larger values
    assert module_0.solution([7, 2, 9, 4, 11]) == 27

    # Zero values ignored (0 is even)
    assert module_0.solution([0, 0, 0]) == 0

# Generated at 2026-11-01 20:06:31.947510
# Unit test for function solution
def test_solution():
    # Odd elements at even indices are summed
    assert module_0.solution([1, 2, 3]) == 4          # 1 + 3
    assert module_0.solution([3, 3, 3, 3, 3]) == 9    # indices 0, 2, 4
    assert module_0.solution([5, 0, 3, 0, 1]) == 9    # 5 + 3 + 1

    # No odd elements at even indices
    assert module_0.solution([2, 1, 4, 3, 6]) == 0    # evens at even indices
    assert module_0.solution([1, 1, 1, 1]) == 2       # odds only at odd indices
    assert module_0.solution([]) == 0                 # empty list

    # Single element cases
    assert module_0.solution([7]) == 7
    assert module_0.solution([8]) == 0

    # Negative numbers
    assert module_0.solution([-3, 2, -5]) == -8       # -3 + -5

    # Zero is even, should be excluded
    assert module_0.solution([0, 1, 0]) == 0

    # Larger example
    assert module_0.solution([1, 4, 9, 16, 25, 36, 49]) == 84  # 1 + 9 + 25 + 49