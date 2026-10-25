

# Generated at 2026-10-24 06:52:43.605182
# Unit test for function order_by_points
def test_order_by_points():
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([1, 2, 3]) == [1, 2, 3]
    assert module_0.order_by_points([12, 10, 11]) == [10, 11, 12]
    assert module_0.order_by_points([-12, -2, 0, 1, 2]) == [-2, 0, -12, 1, 2]
    assert module_0.order_by_points([99, 100, 1]) == [100, 1, 99]

# Generated at 2026-10-24 06:53:13.210705
# Unit test for function order_by_points
def test_order_by_points():
    # empty / single
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([5]) == [5]
    assert module_0.order_by_points([0]) == [0]

    # basic: sort by sum of digits
    # 100->1, 12->3, 111->3, 5->5
    assert module_0.order_by_points([12, 5, 111, 100]) == [100, 12, 111, 5]

    # already sorted
    assert module_0.order_by_points([1, 11, 111]) == [1, 11, 111]

    # ties keep original order (Python sort is stable)
    # 19->10, 28->10, 11->2
    assert module_0.order_by_points([19, 28, 11]) == [11, 19, 28]

    # all same sum -> unchanged
    assert module_0.order_by_points([100, 10, 1]) == [100, 10, 1]
    assert module_0.order_by_points([1, 10, 100]) == [1, 10, 100]

    # zero
    # 0->0, 10->1, 1->1, 100->1
    assert module_0.order_by_points([10, 0, 1, 100]) == [0, 10, 1, 100]

    # negative handling in digits_sum:
    # -n negates first digit only, e.g. -32 -> -3+2 = -1
    assert module_0.order_by_points([-32]) == [-32]
    assert module_0.order_by_points([32, -32]) == [-32, 32]  # -1 < 5
    assert module_0.order_by_points([19, -19]) == [-19, 19]  # 8 < 10
    assert module_0.order_by_points([123, -123]) == [-123, 123]  # 4 < 6

    # -101 -> -1+0+1 = 0, same as 0
    assert module_0.order_by_points([-101, 0]) == [-101, 0]
    assert module_0.order_by_points([0, -101]) == [0, -101]

# Generated at 2026-10-24 06:53:29.683508
# Unit test for function order_by_points
def test_order_by_points():
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([1, 2, 3]) == [1, 2, 3]
    assert module_0.order_by_points([12, 10, 11]) == [10, 11, 12]
    assert module_0.order_by_points([-12, -2, 0, 1, 2]) == [-2, 0, -12, 1, 2]
    assert module_0.order_by_points([99, 100, 1]) == [100, 1, 99]

# Generated at 2026-10-24 06:53:32.100239
# Unit test for function order_by_points

# Generated at 2026-10-24 06:53:34.514733
# Unit test for function order_by_points

# Generated at 2026-10-24 06:53:36.933277
# Unit test for function order_by_points

# Generated at 2026-10-24 06:53:39.363389
# Unit test for function order_by_points

# Generated at 2026-10-24 06:53:41.768278
# Unit test for function order_by_points

# Generated at 2026-10-24 06:53:44.182379
# Unit test for function order_by_points