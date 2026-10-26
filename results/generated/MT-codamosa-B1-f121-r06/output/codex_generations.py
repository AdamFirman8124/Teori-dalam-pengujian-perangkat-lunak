

# Generated at 2026-10-25 08:48:42.061991
# Unit test for function solution
def test_solution():
    # empty list
    assert module_0.solution([]) == 0
    # single element
    assert module_0.solution([1]) == 1
    assert module_0.solution([2]) == 0
    # odd numbers at even indices are summed
    assert module_0.solution([1, 2, 3]) == 4  # 1 + 3
    assert module_0.solution([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5
    # odd numbers at odd indices are ignored
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 0
    assert module_0.solution([2, 3, 4, 5]) == 0
    # all odd, only even indices count
    assert module_0.solution([5, 5, 5, 5, 5]) == 15  # 5 + 5 + 5
    # even numbers at even indices are ignored
    assert module_0.solution([0, 1, 2]) == 0
    # negative odds: in Python -1 % 2 == 1
    assert module_0.solution([-1, -2, -3]) == -4  # -1 + -3

# Generated at 2026-10-25 08:48:44.470195
# Unit test for function solution

# Generated at 2026-10-25 08:48:46.900624
# Unit test for function solution

# Generated at 2026-10-25 08:48:49.318156
# Unit test for function solution

# Generated at 2026-10-25 08:48:51.735005
# Unit test for function solution

# Generated at 2026-10-25 08:48:54.151390
# Unit test for function solution

# Generated at 2026-10-25 08:48:56.567785
# Unit test for function solution

# Generated at 2026-10-25 08:48:58.987961
# Unit test for function solution

# Generated at 2026-10-25 08:49:01.408633
# Unit test for function solution

# Generated at 2026-10-25 08:49:03.827972
# Unit test for function solution

# Generated at 2026-10-25 08:49:06.249053
# Unit test for function solution

# Generated at 2026-10-25 08:49:08.670543
# Unit test for function solution

# Generated at 2026-10-25 08:49:11.083116
# Unit test for function solution