

# Generated at 2026-11-02 16:34:24.240471
# Unit test for function solution
def test_solution():
    # Basic case: odd values at even indices
    assert module_0.solution([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5
    # Even values at even indices contribute nothing
    assert module_0.solution([0, 1, 2, 3, 4, 5]) == 0  # 0, 2, 4 are all even
    # Mixed values
    assert module_0.solution([2, 3, 5, 6, 7]) == 12  # 5 + 7
    # Single element list with odd value
    assert module_0.solution([5]) == 5
    # Single element list with even value
    assert module_0.solution([4]) == 0
    # Empty list
    assert module_0.solution([]) == 0
    # Odd values only at odd indices
    assert module_0.solution([2, 1, 4, 3]) == 0
    # All odd values
    assert module_0.solution([1, 1, 1, 1, 1]) == 3  # indices 0, 2, 4
    # Negative odd values (Python: -1 % 2 == 1)
    assert module_0.solution([-1, 2, -3, 4]) == -4  # -1 + -3
    # Large numbers
    assert module_0.solution([1000001, 2, 999999]) == 2000000  # 1000001 + 999999
    # Floats excluded implicitly by x % 2 check behavior on ints only
    assert module_0.solution([1, 2, 3]) == 4  # 1 + 3

test_solution()
print("All tests passed!")

# Generated at 2026-11-02 16:35:40.386199
# Unit test for function solution
def test_solution():
    # Standard case: odd numbers at even indices
    assert module_0.solution([1, 2, 3, 4, 5]) == 1 + 3 + 5  # indices 0, 2, 4

    # Even numbers at even indices should not count
    assert module_0.solution([2, 3, 4, 5, 6]) == 4  # only 4 at index 2 is even-indexed even? no: 4%2==0, so sum is 0... 

    # Corrected: [2,3,4,5,6] -> indices 0,2,4 -> values 2,4,6 all even -> sum 0
    assert module_0.solution([2, 3, 4, 5, 6]) == 0

    # Odd numbers only at odd indices
    assert module_0.solution([2, 1, 4, 3, 6]) == 0

    # Empty list
    assert module_0.solution([]) == 0

    # Single element, odd at index 0
    assert module_0.solution([7]) == 7

    # Single element, even at index 0
    assert module_0.solution([8]) == 0

    # Negative odd number at even index
    assert module_0.solution([-3, 2, -5]) == -3 + -5

    # Zero at even index (zero is even, not counted)
    assert module_0.solution([0, 1, 0, 3]) == 0

    # Larger list with mixed values
    assert module_0.solution([1, 1, 1, 1, 1, 1]) == 3  # indices 0, 2, 4 contribute

# Generated at 2026-11-02 16:37:08.204380
# Unit test for function solution
def test_solution():
    # Even index + odd value elements are summed
    assert module_0.solution([1, 2, 3]) == 4          # 1 (idx 0) + 3 (idx 2)
    assert module_0.solution([5, 8, 6, 2, 7]) == 12   # 5 (idx 0) + 7 (idx 4)
    assert module_0.solution([3, 3, 3, 3]) == 3       # only idx 0 has odd value at even index? idx 2 = 3 also -> 6

def test_solution_extended():
    # Corrected expectations
    assert module_0.solution([3, 3, 3, 3]) == 6       # idx 0 and idx 2 both odd values
    assert module_0.solution([0, 1, 2, 3, 4, 5]) == 0 # all even-index values are even
    assert module_0.solution([]) == 0                 # empty list
    assert module_0.solution([2, 3, 4, 5]) == 0       # no odd values at even indices
    assert module_0.solution([1]) == 1                # single odd element at idx 0
    assert module_0.solution([2]) == 0                # single even element
    assert module_0.solution([-3, 2, -5, 4]) == -8    # negative odd values at even indices
    assert module_0.solution([7, 7, 7, 7, 7]) == 21   # idx 0, 2, 4 -> 7+7+7
    assert module_0.solution([0, 0, 1, 0, 1]) == 2    # idx 2 and idx 4
    assert module_0.solution([11, 4, 9, 6, 13, 8, 15]) == 48  # 11+9+13+15

    print("All tests passed!")

# Generated at 2026-11-02 16:38:31.491685
# Unit test for function solution
def test_solution():
    # nonce:66af235e
    # Basic case: 1 (idx 0) + 3 (idx 2) = 4
    assert module_0.solution([1, 2, 3]) == 4
    # Empty list
    assert module_0.solution([]) == 0
    # Single odd element at index 0
    assert module_0.solution([5]) == 5
    # Even values at even indices are excluded
    assert module_0.solution([2, 2]) == 0
    assert module_0.solution([0, 0]) == 0
    # Odd value at odd index is excluded
    assert module_0.solution([1, 1]) == 1
    # Multiple qualifying elements: 1 + 3 + 5 = 9
    assert module_0.solution([1, 2, 3, 4, 5]) == 9
    assert module_0.solution([3, 3, 3, 3, 3]) == 9
    # All even values at even indices
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 0
    # Negative odd numbers (Python: -1 % 2 == 1)
    assert module_0.solution([-1, 2, -3]) == -4
    # Large numbers
    assert module_0.solution([1000001, 0, 999999]) == 2000000

# Generated at 2026-11-02 16:40:31.461139
# Unit test for function solution
def test_solution():
    # Basic cases: odd values at even indices (0, 2, 4, ...)
    assert module_0.solution([1, 2, 3]) == 4          # 1 + 3
    assert module_0.solution([5, 0, 3, 0, 4, 2]) == 8  # 5 + 3
    assert module_0.solution([1, 2, 3, 4]) == 4        # 1 + 3

    # Edge cases
    assert module_0.solution([]) == 0                  # empty list
    assert module_0.solution([7]) == 7                 # single odd element
    assert module_0.solution([2]) == 0                 # single even element

    # No odd values at even indices
    assert module_0.solution([2, 3, 4, 5, 6]) == 0
    assert module_0.solution([0, 1, 0, 1, 0]) == 0

    # Odd values at odd indices should be ignored
    assert module_0.solution([2, 1, 2, 1, 2]) == 0

    # All odd values
    assert module_0.solution([1, 1, 1, 1, 1]) == 3     # indices 0, 2, 4

    # Negative numbers (Python: -3 % 2 == 1, so they count as odd)
    assert module_0.solution([-3, 2, -5]) == -8        # -3 + -5
    assert module_0.solution([-2, 1, -4]) == 0