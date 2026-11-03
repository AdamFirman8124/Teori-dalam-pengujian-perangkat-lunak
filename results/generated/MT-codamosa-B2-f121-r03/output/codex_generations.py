

# Generated at 2026-11-02 23:07:40.512194
# Unit test for function solution
def test_solution():
    # Odd values at even indices are summed
    assert module_0.solution([1, 2, 3]) == 4          # 1 (idx 0) + 3 (idx 2)
    assert module_0.solution([1, 2]) == 1             # 1 (idx 0)
    assert module_0.solution([5, 0, 3, 0, 5]) == 13   # 5 + 3 + 5

    # Even values at even indices are excluded
    assert module_0.solution([2, 3, 4, 5]) == 0       # 2 and 4 are even
    assert module_0.solution([0, 1, 2, 3]) == 0

    # Odd values at odd indices are excluded
    assert module_0.solution([2, 1, 2, 1]) == 0

    # Edge cases
    assert module_0.solution([]) == 0                 # empty list
    assert module_0.solution([7]) == 7                # single odd element
    assert module_0.solution([8]) == 0                # single even element

    # Negative numbers
    assert module_0.solution([-1, 2, -3]) == -4       # -1 + -3
    assert module_0.solution([-2, -3, -4]) == 0       # negatives at even idx are even

    # Longer list
    assert module_0.solution([1, 1, 1, 1, 1]) == 3    # indices 0, 2, 4

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()

# Generated at 2026-11-02 23:10:26.810151
# Unit test for function solution
def test_solution():
    # Empty list
    assert module_0.solution([]) == 0

    # Odd values at even indices
    assert module_0.solution([1, 2, 3]) == 4  # 1 + 3
    assert module_0.solution([1, 3, 5, 7]) == 6  # 1 + 5

    # Even values at even indices (should be excluded)
    assert module_0.solution([2, 4, 8]) == 0
    assert module_0.solution([0, 1, 2, 3]) == 0

    # Odd values only at odd indices (should be excluded)
    assert module_0.solution([2, 3, 4, 5]) == 0
    assert module_0.solution([0, 1]) == 0

    # Single element list
    assert module_0.solution([5]) == 5
    assert module_0.solution([4]) == 0

    # Negative numbers
    assert module_0.solution([-3, 2, -5]) == -8  # -3 + -5
    assert module_0.solution([-2, -3, -4]) == 0

    # Mixed values
    assert module_0.solution([3, 2, 1, 4, 7]) == 11  # 3 + 1 + 7
    assert module_0.solution([5, 5, 5, 5, 5, 5]) == 15  # 5 + 5 + 5 at indices 0, 2, 4

    # Larger list
    assert module_0.solution(list(range(10))) == 20  # 1 + 5 + 9 + 13 + ... wait, indices 0,2,4,6,8: 0,2,4,6,8 all even
    # Recomputed: even indices 0,2,4,6,8 -> values 0,2,4,6,8 -> all even -> sum 0
    # Correct value:
    assert module_0.solution(list(range(10))) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()

# Generated at 2026-11-02 23:12:43.309684
# Unit test for function solution
def test_solution():
    # Basic case: odd numbers at even indices
    assert module_0.solution([1, 2, 3]) == 4  # 1 + 3

    # Odd numbers at even and odd indices
    assert module_0.solution([1, 5, 3]) == 4  # 1 + 3 (5 is at odd index, excluded)

    # All even numbers - sum should be 0
    assert module_0.solution([2, 4, 6]) == 0

    # Empty list
    assert module_0.solution([]) == 0

    # Single odd element at index 0
    assert module_0.solution([5]) == 5

    # Single even element at index 0
    assert module_0.solution([4]) == 0

    # Odd numbers only at odd indices
    assert module_0.solution([2, 3, 4, 5]) == 0

    # All odd numbers
    assert module_0.solution([1, 3, 5, 7]) == 6  # 1 + 5 (indices 0 and 2)

    # Mixed even/odd with larger list
    assert module_0.solution([3, 3, 3, 3, 3]) == 9  # indices 0, 2, 4

    # Zeros in the list
    assert module_0.solution([0, 1, 0, 1, 1]) == 1  # only index 4 has odd value

    # Negative odd numbers (Python: -3 % 2 == 1)
    assert module_0.solution([-1, 2, -3, 4]) == -4  # -1 + -3

    # Negative even numbers excluded
    assert module_0.solution([-2, 1, -4, 3]) == 0

    # Large numbers
    assert module_0.solution([1000001, 2, 1000003]) == 2000004

    # Verify return type is int
    assert isinstance(module_0.solution([1, 2, 3]), int)

# Generated at 2026-11-02 23:13:53.946422
# Unit test for function solution
def test_solution():
    # Classic example: even indices 0 and 2 hold odd values 1 and 3
    assert module_0.solution([1, 2, 3]) == 4
    # No odd values at even indices
    assert module_0.solution([2, 4, 6]) == 0
    # Empty list
    assert module_0.solution([]) == 0
    # Single odd element at index 0
    assert module_0.solution([5]) == 5
    # Single even element at index 0
    assert module_0.solution([4]) == 0
    # Odd value at odd index should be ignored
    assert module_0.solution([2, 3, 4]) == 0
    assert module_0.solution([1, 1, 1, 1]) == 2  # only indices 0 and 2 count
    # Negative odd values count too
    assert module_0.solution([-1, 2, -3]) == -4
    # Mixed list with multiple qualifying values
    assert module_0.solution([1, 2, 3, 4, 5, 6, 7]) == 1 + 3 + 5 + 7
    # Zero is even, should not count
    assert module_0.solution([0, 1, 0]) == 0