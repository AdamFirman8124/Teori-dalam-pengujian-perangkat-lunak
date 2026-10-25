

# Generated at 2026-10-24 07:01:26.054434
# Unit test for function add_elements
def test_add_elements():
    # all single-digit, all included
    assert module_0.add_elements([1, 2, 3, 4], 4) == 10
    # 100 has 3 digits -> excluded
    assert module_0.add_elements([10, 20, 30, 100], 4) == 60
    # 111 and 4000 excluded
    assert module_0.add_elements([111, 21, 3, 4000], 4) == 24
    # only first k elements considered
    assert module_0.add_elements([1, 2, 3, 10, 20], 3) == 6
    # boundary 99 included, 100 excluded
    assert module_0.add_elements([99, 100, 9, 10], 4) == 118
    # negative: str(-10) = "-10" len 3 -> excluded, str(-2) = "-2" len 2 -> included
    assert module_0.add_elements([5, -10, 15, -2], 4) == 18
    # k = 0 -> empty sum
    assert module_0.add_elements([1, 2, 3], 0) == 0
    # k > len(arr) -> whole array
    assert module_0.add_elements([1, 22, 333], 10) == 23
    # empty array
    assert module_0.add_elements([], 0) == 0

# Generated at 2026-10-24 07:01:27.590202
# Unit test for function add_elements
def test_add_elements():
    # all single-digit, all included
    assert module_0.add_elements([1, 2, 3, 4], 4) == 10
    # 100 has 3 digits -> excluded
    assert module_0.add_elements([10, 20, 30, 100], 4) == 60
    # 111 and 4000 excluded
    assert module_0.add_elements([111, 21, 3, 4000], 4) == 24
    # only first k elements considered
    assert module_0.add_elements([1, 2, 3, 10, 20], 3) == 6
    # boundary 99 included, 100 excluded
    assert module_0.add_elements([99, 100, 9, 10], 4) == 118
    # negative: str(-10) = "-10" len 3 -> excluded, str(-2) = "-2" len 2 -> included
    assert module_0.add_elements([5, -10, 15, -2], 4) == 18
    # k = 0 -> empty sum
    assert module_0.add_elements([1, 2, 3], 0) == 0
    # k > len(arr) -> whole array
    assert module_0.add_elements([1, 22, 333], 10) == 23
    # empty array
    assert module_0.add_elements([], 0) == 0

# Generated at 2026-10-24 07:01:29.124440
# Unit test for function add_elements
def test_add_elements():
    # all single-digit, all included
    assert module_0.add_elements([1, 2, 3, 4], 4) == 10
    # 100 has 3 digits -> excluded
    assert module_0.add_elements([10, 20, 30, 100], 4) == 60
    # 111 and 4000 excluded
    assert module_0.add_elements([111, 21, 3, 4000], 4) == 24
    # only first k elements considered
    assert module_0.add_elements([1, 2, 3, 10, 20], 3) == 6
    # boundary 99 included, 100 excluded
    assert module_0.add_elements([99, 100, 9, 10], 4) == 118
    # negative: str(-10) = "-10" len 3 -> excluded, str(-2) = "-2" len 2 -> included
    assert module_0.add_elements([5, -10, 15, -2], 4) == 18
    # k = 0 -> empty sum
    assert module_0.add_elements([1, 2, 3], 0) == 0
    # k > len(arr) -> whole array
    assert module_0.add_elements([1, 22, 333], 10) == 23
    # empty array
    assert module_0.add_elements([], 0) == 0

# Generated at 2026-10-24 07:01:30.659356
# Unit test for function add_elements
def test_add_elements():
    # all single-digit, all included
    assert module_0.add_elements([1, 2, 3, 4], 4) == 10
    # 100 has 3 digits -> excluded
    assert module_0.add_elements([10, 20, 30, 100], 4) == 60
    # 111 and 4000 excluded
    assert module_0.add_elements([111, 21, 3, 4000], 4) == 24
    # only first k elements considered
    assert module_0.add_elements([1, 2, 3, 10, 20], 3) == 6
    # boundary 99 included, 100 excluded
    assert module_0.add_elements([99, 100, 9, 10], 4) == 118
    # negative: str(-10) = "-10" len 3 -> excluded, str(-2) = "-2" len 2 -> included
    assert module_0.add_elements([5, -10, 15, -2], 4) == 18
    # k = 0 -> empty sum
    assert module_0.add_elements([1, 2, 3], 0) == 0
    # k > len(arr) -> whole array
    assert module_0.add_elements([1, 22, 333], 10) == 23
    # empty array
    assert module_0.add_elements([], 0) == 0

# Generated at 2026-10-24 07:01:32.068066
# Unit test for function add_elements
def test_add_elements():
    # all single-digit, all included
    assert module_0.add_elements([1, 2, 3, 4], 4) == 10
    # 100 has 3 digits -> excluded
    assert module_0.add_elements([10, 20, 30, 100], 4) == 60
    # 111 and 4000 excluded
    assert module_0.add_elements([111, 21, 3, 4000], 4) == 24
    # only first k elements considered
    assert module_0.add_elements([1, 2, 3, 10, 20], 3) == 6
    # boundary 99 included, 100 excluded
    assert module_0.add_elements([99, 100, 9, 10], 4) == 118
    # negative: str(-10) = "-10" len 3 -> excluded, str(-2) = "-2" len 2 -> included
    assert module_0.add_elements([5, -10, 15, -2], 4) == 18
    # k = 0 -> empty sum
    assert module_0.add_elements([1, 2, 3], 0) == 0
    # k > len(arr) -> whole array
    assert module_0.add_elements([1, 22, 333], 10) == 23
    # empty array
    assert module_0.add_elements([], 0) == 0