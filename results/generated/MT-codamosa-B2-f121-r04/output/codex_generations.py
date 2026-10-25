

# Generated at 2026-10-24 15:33:41.819086
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

# Generated at 2026-10-24 15:33:43.192079
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

# Generated at 2026-10-24 15:33:44.645864
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

# Generated at 2026-10-24 15:33:46.070251
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

# Generated at 2026-10-24 15:33:53.829393
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