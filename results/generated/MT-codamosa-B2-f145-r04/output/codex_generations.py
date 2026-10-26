

# Generated at 2026-10-25 09:46:06.632659
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:09.264392
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:11.680971
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:14.094184
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:16.624226
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:18.999549
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:21.414641
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:23.830780
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:26.248620
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:28.659908
# Unit test for function order_by_points

# Generated at 2026-10-25 09:46:41.550314
# Unit test for function order_by_points
def test_order_by_points():assert module_0.order_by_points([12, 21, 101, -12, 0]) == [0, -12, 101, 12, 21]

# Generated at 2026-10-25 09:46:43.168642
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