

# Generated at 2026-10-25 10:36:48.587160
# Unit test for function order_by_points
def test_order_by_points():
    # basic ascending order by digit sum
    assert module_0.order_by_points([1, -1, 2, -2, 3, -3]) == [-3, -2, -1, 1, 2, 3]

    # first digit of a negative number is negated before summing
    assert module_0.order_by_points([11, -11, 12, -12]) == [-11, -12, 11, 12]

    # a negative can sort after a positive when its digit sum is larger
    assert module_0.order_by_points([-19, 1]) == [1, -19]

    # edge cases
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([]) == []

    # input list must not be mutated
    nums = [10, -10]
    module_0.order_by_points(nums)
    assert nums == [10, -10]

# Generated at 2026-10-25 10:36:50.049113
# Unit test for function order_by_points
def test_order_by_points():
    # basic ascending order by digit sum
    assert module_0.order_by_points([1, -1, 2, -2, 3, -3]) == [-3, -2, -1, 1, 2, 3]

    # first digit of a negative number is negated before summing
    assert module_0.order_by_points([11, -11, 12, -12]) == [-11, -12, 11, 12]

    # a negative can sort after a positive when its digit sum is larger
    assert module_0.order_by_points([-19, 1]) == [1, -19]

    # edge cases
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([]) == []

    # input list must not be mutated
    nums = [10, -10]
    module_0.order_by_points(nums)
    assert nums == [10, -10]

# Generated at 2026-10-25 10:36:51.439632
# Unit test for function order_by_points
def test_order_by_points():
    # basic ascending order by digit sum
    assert module_0.order_by_points([1, -1, 2, -2, 3, -3]) == [-3, -2, -1, 1, 2, 3]

    # first digit of a negative number is negated before summing
    assert module_0.order_by_points([11, -11, 12, -12]) == [-11, -12, 11, 12]

    # a negative can sort after a positive when its digit sum is larger
    assert module_0.order_by_points([-19, 1]) == [1, -19]

    # edge cases
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([]) == []

    # input list must not be mutated
    nums = [10, -10]
    module_0.order_by_points(nums)
    assert nums == [10, -10]

# Generated at 2026-10-25 10:36:52.785279
# Unit test for function order_by_points
def test_order_by_points():
    # basic ascending order by digit sum
    assert module_0.order_by_points([1, -1, 2, -2, 3, -3]) == [-3, -2, -1, 1, 2, 3]

    # first digit of a negative number is negated before summing
    assert module_0.order_by_points([11, -11, 12, -12]) == [-11, -12, 11, 12]

    # a negative can sort after a positive when its digit sum is larger
    assert module_0.order_by_points([-19, 1]) == [1, -19]

    # edge cases
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([]) == []

    # input list must not be mutated
    nums = [10, -10]
    module_0.order_by_points(nums)
    assert nums == [10, -10]

# Generated at 2026-10-25 10:36:54.245347
# Unit test for function order_by_points
def test_order_by_points():
    # basic ascending order by digit sum
    assert module_0.order_by_points([1, -1, 2, -2, 3, -3]) == [-3, -2, -1, 1, 2, 3]

    # first digit of a negative number is negated before summing
    assert module_0.order_by_points([11, -11, 12, -12]) == [-11, -12, 11, 12]

    # a negative can sort after a positive when its digit sum is larger
    assert module_0.order_by_points([-19, 1]) == [1, -19]

    # edge cases
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([]) == []

    # input list must not be mutated
    nums = [10, -10]
    module_0.order_by_points(nums)
    assert nums == [10, -10]