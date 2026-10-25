

# Generated at 2026-10-25 02:48:26.431517
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

# Generated at 2026-10-25 02:48:43.064454
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

# Generated at 2026-10-25 02:49:00.688315
# Unit test for function order_by_points

# Generated at 2026-10-25 02:49:03.102641
# Unit test for function order_by_points

# Generated at 2026-10-25 02:49:05.517922
# Unit test for function order_by_points

# Generated at 2026-10-25 02:49:07.932076
# Unit test for function order_by_points

# Generated at 2026-10-25 02:49:10.347641
# Unit test for function order_by_points

# Generated at 2026-10-25 02:49:12.763591
# Unit test for function order_by_points

# Generated at 2026-10-25 02:49:15.178874
# Unit test for function order_by_points

# Generated at 2026-10-25 02:49:17.592591
# Unit test for function order_by_points

# Generated at 2026-10-25 02:49:20.007767
# Unit test for function order_by_points