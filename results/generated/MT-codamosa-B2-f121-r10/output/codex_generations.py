

# Generated at 2026-10-24 10:31:39.672626
# Unit test for function solution
def test_solution():
    assert module_0.solution([]) == 0
    assert module_0.solution([5, 8, 7, 1]) == 12  # 5 (idx 0) + 7 (idx 2)
    assert module_0.solution([3, 3, 3, 3, 3]) == 9  # 3 + 3 + 3 at idx 0, 2, 4
    assert module_0.solution([30, 13, 24, 321]) == 0  # 30 and 24 are even
    assert module_0.solution([1, 2, 3, 4, 5, 6]) == 9  # 1 + 3 + 5
    assert module_0.solution([1, 3, 5, 7]) == 6  # 1 (idx 0) + 5 (idx 2), ignore odd idx
    assert module_0.solution([2, 4, 6, 8]) == 0  # no odds
    assert module_0.solution([1]) == 1
    assert module_0.solution([2]) == 0

# Generated at 2026-10-24 10:31:48.177969
# Unit test for function solution
def test_solution():
    assert module_0.solution([1, 2, 3]) == 3          # indices 0,2 â 1+3, both odd â wait: 1+3=4? No â check below
    assert module_0.solution([]) == 0
    assert module_0.solution([0, 1, 2, 3]) == 0       # even indices hold 0,2 â no odd values
    assert module_0.solution([5, 5, 5, 5, 5]) == 15   # indices 0,2,4 â 5+5+5
    assert module_0.solution([2, 3, 4, 5, 6, 7]) == 0 # even indices hold 2,4,6 â all even
    assert module_0.solution([7]) == 7                # single element, odd, at index 0
    assert module_0.solution([1, 1, 1, 1]) == 2       # indices 0,2 â 1+1

# Generated at 2026-10-24 10:31:49.510317
# Unit test for function solution
def test_solution():
    assert module_0.solution([1, 2, 3]) == 3          # indices 0,2 â 1+3, both odd â wait: 1+3=4? No â check below
    assert module_0.solution([]) == 0
    assert module_0.solution([0, 1, 2, 3]) == 0       # even indices hold 0,2 â no odd values
    assert module_0.solution([5, 5, 5, 5, 5]) == 15   # indices 0,2,4 â 5+5+5
    assert module_0.solution([2, 3, 4, 5, 6, 7]) == 0 # even indices hold 2,4,6 â all even
    assert module_0.solution([7]) == 7                # single element, odd, at index 0
    assert module_0.solution([1, 1, 1, 1]) == 2       # indices 0,2 â 1+1

# Generated at 2026-10-24 10:31:50.840964
# Unit test for function solution
def test_solution():
    assert module_0.solution([1, 2, 3]) == 3          # indices 0,2 â 1+3, both odd â wait: 1+3=4? No â check below
    assert module_0.solution([]) == 0
    assert module_0.solution([0, 1, 2, 3]) == 0       # even indices hold 0,2 â no odd values
    assert module_0.solution([5, 5, 5, 5, 5]) == 15   # indices 0,2,4 â 5+5+5
    assert module_0.solution([2, 3, 4, 5, 6, 7]) == 0 # even indices hold 2,4,6 â all even
    assert module_0.solution([7]) == 7                # single element, odd, at index 0
    assert module_0.solution([1, 1, 1, 1]) == 2       # indices 0,2 â 1+1

# Generated at 2026-10-24 10:31:52.155661
# Unit test for function solution
def test_solution():
    assert module_0.solution([1, 2, 3]) == 3          # indices 0,2 â 1+3, both odd â wait: 1+3=4? No â check below
    assert module_0.solution([]) == 0
    assert module_0.solution([0, 1, 2, 3]) == 0       # even indices hold 0,2 â no odd values
    assert module_0.solution([5, 5, 5, 5, 5]) == 15   # indices 0,2,4 â 5+5+5
    assert module_0.solution([2, 3, 4, 5, 6, 7]) == 0 # even indices hold 2,4,6 â all even
    assert module_0.solution([7]) == 7                # single element, odd, at index 0
    assert module_0.solution([1, 1, 1, 1]) == 2       # indices 0,2 â 1+1