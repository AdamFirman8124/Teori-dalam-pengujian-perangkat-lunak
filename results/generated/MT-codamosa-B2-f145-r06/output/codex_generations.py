

# Generated at 2026-10-25 06:17:16.875419
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

# Generated at 2026-10-25 06:17:18.411168
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

# Generated at 2026-10-25 06:17:21.055797
# Unit test for function order_by_points

# Generated at 2026-10-25 06:17:23.830519
# Unit test for function order_by_points

# Generated at 2026-10-25 06:17:26.248467
# Unit test for function order_by_points

# Generated at 2026-10-25 06:17:28.663081
# Unit test for function order_by_points

# Generated at 2026-10-25 06:17:31.079452
# Unit test for function order_by_points

# Generated at 2026-10-25 06:17:33.510979
# Unit test for function order_by_points

# Generated at 2026-10-25 06:17:35.928135
# Unit test for function order_by_points

# Generated at 2026-10-25 06:17:38.343430
# Unit test for function order_by_points

# Generated at 2026-10-25 06:17:40.760948
# Unit test for function order_by_points