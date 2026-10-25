

# Generated at 2026-10-24 14:37:16.619922
# Unit test for function solution

# Generated at 2026-10-24 14:37:19.032574
# Unit test for function solution

# Generated at 2026-10-24 14:37:21.445407
# Unit test for function solution

# Generated at 2026-10-24 14:37:23.860187
# Unit test for function solution

# Generated at 2026-10-24 14:37:26.272297
# Unit test for function solution

# Generated at 2026-10-24 14:37:39.576685
# Unit test for function solution
def test_solution():assert module_0.solution([1, 2, 3, 4, 5]) == 9

# Generated at 2026-10-24 14:37:52.980229
# Unit test for function solution
def test_solution():
    # empty list
    assert module_0.solution([]) == 0

    # basic: 5 (idx 0) + 7 (idx 2) = 12, idx 1 and 3 ignored
    assert module_0.solution([5, 8, 7, 1]) == 12

    # odd at even indices only
    assert module_0.solution([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5
    assert module_0.solution([1, 2, 3]) == 4  # 1 + 3

    # odd at odd index ignored
    assert module_0.solution([2, 1]) == 0
    assert module_0.solution([2, 3, 4]) == 0

    # no odds at even indices
    assert module_0.solution([2, 4, 6]) == 0
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 0

    # single element
    assert module_0.solution([1]) == 1
    assert module_0.solution([2]) == 0

    # zeros
    assert module_0.solution([0, 1, 0, 1, 0]) == 0

    # negative odds (in Python -1 % 2 == 1, -3 % 2 == 1)
    assert module_0.solution([-1, -2, -3, -4, -5]) == -9  # -1 + -3 + -5

# Generated at 2026-10-24 14:37:55.745245
# Unit test for function solution
def test_solution():
    # empty list
    assert module_0.solution([]) == 0

    # basic: 5 (idx 0) + 7 (idx 2) = 12, idx 1 and 3 ignored
    assert module_0.solution([5, 8, 7, 1]) == 12

    # odd at even indices only
    assert module_0.solution([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5
    assert module_0.solution([1, 2, 3]) == 4  # 1 + 3

    # odd at odd index ignored
    assert module_0.solution([2, 1]) == 0
    assert module_0.solution([2, 3, 4]) == 0

    # no odds at even indices
    assert module_0.solution([2, 4, 6]) == 0
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 0

    # single element
    assert module_0.solution([1]) == 1
    assert module_0.solution([2]) == 0

    # zeros
    assert module_0.solution([0, 1, 0, 1, 0]) == 0

    # negative odds (in Python -1 % 2 == 1, -3 % 2 == 1)
    assert module_0.solution([-1, -2, -3, -4, -5]) == -9  # -1 + -3 + -5

# Generated at 2026-10-24 14:37:58.525490
# Unit test for function solution
def test_solution():
    # empty list
    assert module_0.solution([]) == 0

    # basic: 5 (idx 0) + 7 (idx 2) = 12, idx 1 and 3 ignored
    assert module_0.solution([5, 8, 7, 1]) == 12

    # odd at even indices only
    assert module_0.solution([1, 2, 3, 4, 5]) == 9  # 1 + 3 + 5
    assert module_0.solution([1, 2, 3]) == 4  # 1 + 3

    # odd at odd index ignored
    assert module_0.solution([2, 1]) == 0
    assert module_0.solution([2, 3, 4]) == 0

    # no odds at even indices
    assert module_0.solution([2, 4, 6]) == 0
    assert module_0.solution([2, 1, 4, 3, 6, 5]) == 0

    # single element
    assert module_0.solution([1]) == 1
    assert module_0.solution([2]) == 0

    # zeros
    assert module_0.solution([0, 1, 0, 1, 0]) == 0

    # negative odds (in Python -1 % 2 == 1, -3 % 2 == 1)
    assert module_0.solution([-1, -2, -3, -4, -5]) == -9  # -1 + -3 + -5