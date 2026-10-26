

# Generated at 2026-10-25 07:02:55.970643
# Unit test for function solution
def test_solution():
    # Odd number at even index â included
    assert module_0.solution([1, 2, 3]) == 4          # 1 (idx 0) + 3 (idx 2)
    assert module_0.solution([5, 0, 3, 0, 7]) == 15   # 5 + 3 + 7

    # Odd number at odd index â excluded
    assert module_0.solution([0, 1, 0, 3]) == 0

    # Even numbers only â nothing included
    assert module_0.solution([2, 4, 6, 8]) == 0

    # Empty list
    assert module_0.solution([]) == 0

    # Negative odd numbers (x%2==1 works for negatives in Python: -3%2 == 1)
    assert module_0.solution([-3, 2, -5, 4, -7]) == -15  # -3 + -5 + -7

    # Single element
    assert module_0.solution([7]) == 7
    assert module_0.solution([8]) == 0

    print("All tests passed!")

test_solution()

# Generated at 2026-10-25 07:03:12.365481
# Unit test for function solution
def test_solution():
    assert module_0.solution([1, 2, 3, 4, 5]) == 9       # 1 + 3 + 5
    assert module_0.solution([2, 4, 6, 8]) == 0
    assert module_0.solution([1, 3, 5, 7]) == 6           # indices 0 and 2: 1 + 5
    assert module_0.solution([]) == 0
    assert module_0.solution([10, 11, 12, 13, 15]) == 15 # only index 4 qualifies

# Generated at 2026-10-25 07:03:14.785005
# Unit test for function solution

# Generated at 2026-10-25 07:03:17.200844
# Unit test for function solution

# Generated at 2026-10-25 07:03:19.790283
# Unit test for function solution

# Generated at 2026-10-25 07:03:22.206942
# Unit test for function solution

# Generated at 2026-10-25 07:03:24.623479
# Unit test for function solution

# Generated at 2026-10-25 07:03:27.042206
# Unit test for function solution

# Generated at 2026-10-25 07:03:29.459457
# Unit test for function solution

# Generated at 2026-10-25 07:03:31.874240
# Unit test for function solution

# Generated at 2026-10-25 07:03:34.287929
# Unit test for function solution