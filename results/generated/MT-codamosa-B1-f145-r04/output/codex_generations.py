

# Generated at 2026-10-24 22:56:57.753614
# Unit test for function order_by_points
def test_order_by_points():
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([4, 2, 1, 3]) == [1, 2, 3, 4]

    # Digit sums: -32=-1, -98=-1, -87=-1, -11=0,
    #              1=1, 43=7, 54=9, 76=13
    assert module_0.order_by_points(
        [1, -11, -32, 43, 54, -98, 76, -87]
    ) == [-32, -98, -87, -11, 1, 43, 54, 76]

    # Equal digit sums retain their original order.
    assert module_0.order_by_points([12, 21, 30]) == [12, 21, 30]

# Generated at 2026-10-24 22:57:06.819766
# Unit test for function order_by_points
def test_order_by_points():
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([5]) == [5]
    assert module_0.order_by_points([32, 3, 1, 21]) == [1, 3, 21, 32]

    # Equal digit sums preserve the original order (stable sort)
    assert module_0.order_by_points([21, 3, 12, 30]) == [21, 3, 12, 30]

    # Includes zero and negative numbers
    assert module_0.order_by_points([-15, -12, -99, 0, 10, 2, 11]) == [
        -99, 0, -12, 10, 2, 11
    ]

# Generated at 2026-10-24 22:57:13.829198
# Unit test for function order_by_points
def test_order_by_points():
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [
        -1, -11, 1, -12, 11
    ]
    assert module_0.order_by_points([123, 45, -123, -45, 0]) == [
        0, -45, -123, 123, 45
    ]
    # Equal digit sums preserve the original order.
    assert module_0.order_by_points([12, 21, 3]) == [12, 21, 3]

# Generated at 2026-10-24 22:57:21.917950
# Unit test for function order_by_points
def test_order_by_points():
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([42]) == [42]

    # Positive numbers, preserving original order for equal digit sums
    assert module_0.order_by_points([56, 65, 74, 100, 99, 12]) == [
        100, 12, 56, 65, 74, 99
    ]

    # Negative numbers: the sign applies to the first digit
    assert module_0.order_by_points([-12, -21, -99, 0, 11]) == [
        -99, 0, -12, -21, 11
    ]

    # Mixed values
    assert module_0.order_by_points([12, -12, 3, -30, 21]) == [
        -30, -12, 12, 3, 21
    ]

    # Equal point totals retain their original order
    assert module_0.order_by_points([12, 30, 21, 3]) == [12, 30, 21, 3]

# Generated at 2026-10-24 22:57:29.803776
# Unit test for function order_by_points
def test_order_by_points():
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([5]) == [5]
    assert module_0.order_by_points([12, 3, 21, 4]) == [12, 3, 21, 4]
    assert module_0.order_by_points([12, -12, 0, 21, -99, -1, 99, -10]) == [
        -1, -10, 0, -99, -12, 12, 21, 99
    ]
    # Equal digit sums preserve their original order.
    assert module_0.order_by_points([21, 12, 30]) == [21, 12, 30]