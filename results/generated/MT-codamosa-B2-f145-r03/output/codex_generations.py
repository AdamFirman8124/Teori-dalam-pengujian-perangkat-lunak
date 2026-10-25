

# Generated at 2026-10-24 14:54:41.431808
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers â sorted by digit sum
    assert module_0.order_by_points([12, 10, 11]) == [10, 11, 12]          # sums: 1, 2, 3

    # Same digit sum â original order preserved (stable sort)
    assert module_0.order_by_points([21, 12]) == [21, 12]                  # both sum to 3

    # Negative numbers: first digit of |n| is negated
    # -12 â -1+2 = 1;  12 â 3;  -3 â -3;  0 â 0
    assert module_0.order_by_points([12, -12, -3, 0]) == [-3, -12, 0, 12]  # sums: -3, 1, 0, 3

    # Mixed positives and negatives
    # -21 â -2+1 = -1;  3 â 3;  -4 â -4;  111 â 3
    assert module_0.order_by_points([-21, 3, -4, 111]) == [-4, -21, 3, 111]

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Duplicates
    assert module_0.order_by_points([1, 1, 1]) == [1, 1, 1]

    # Multi-digit negatives
    # -123 â -1+2+3 = 4;  -100 â -1+0+0 = -1;  22 â 4
    assert module_0.order_by_points([-123, -100, 22]) == [-100, -123, 22]

    print("All tests passed!")


test_order_by_points()

# Generated at 2026-10-24 14:54:42.854616
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers â sorted by digit sum
    assert module_0.order_by_points([12, 10, 11]) == [10, 11, 12]          # sums: 1, 2, 3

    # Same digit sum â original order preserved (stable sort)
    assert module_0.order_by_points([21, 12]) == [21, 12]                  # both sum to 3

    # Negative numbers: first digit of |n| is negated
    # -12 â -1+2 = 1;  12 â 3;  -3 â -3;  0 â 0
    assert module_0.order_by_points([12, -12, -3, 0]) == [-3, -12, 0, 12]  # sums: -3, 1, 0, 3

    # Mixed positives and negatives
    # -21 â -2+1 = -1;  3 â 3;  -4 â -4;  111 â 3
    assert module_0.order_by_points([-21, 3, -4, 111]) == [-4, -21, 3, 111]

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Duplicates
    assert module_0.order_by_points([1, 1, 1]) == [1, 1, 1]

    # Multi-digit negatives
    # -123 â -1+2+3 = 4;  -100 â -1+0+0 = -1;  22 â 4
    assert module_0.order_by_points([-123, -100, 22]) == [-100, -123, 22]

    print("All tests passed!")


test_order_by_points()

# Generated at 2026-10-24 14:54:44.159097
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers â sorted by digit sum
    assert module_0.order_by_points([12, 10, 11]) == [10, 11, 12]          # sums: 1, 2, 3

    # Same digit sum â original order preserved (stable sort)
    assert module_0.order_by_points([21, 12]) == [21, 12]                  # both sum to 3

    # Negative numbers: first digit of |n| is negated
    # -12 â -1+2 = 1;  12 â 3;  -3 â -3;  0 â 0
    assert module_0.order_by_points([12, -12, -3, 0]) == [-3, -12, 0, 12]  # sums: -3, 1, 0, 3

    # Mixed positives and negatives
    # -21 â -2+1 = -1;  3 â 3;  -4 â -4;  111 â 3
    assert module_0.order_by_points([-21, 3, -4, 111]) == [-4, -21, 3, 111]

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Duplicates
    assert module_0.order_by_points([1, 1, 1]) == [1, 1, 1]

    # Multi-digit negatives
    # -123 â -1+2+3 = 4;  -100 â -1+0+0 = -1;  22 â 4
    assert module_0.order_by_points([-123, -100, 22]) == [-100, -123, 22]

    print("All tests passed!")


test_order_by_points()

# Generated at 2026-10-24 14:54:45.476091
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers â sorted by digit sum
    assert module_0.order_by_points([12, 10, 11]) == [10, 11, 12]          # sums: 1, 2, 3

    # Same digit sum â original order preserved (stable sort)
    assert module_0.order_by_points([21, 12]) == [21, 12]                  # both sum to 3

    # Negative numbers: first digit of |n| is negated
    # -12 â -1+2 = 1;  12 â 3;  -3 â -3;  0 â 0
    assert module_0.order_by_points([12, -12, -3, 0]) == [-3, -12, 0, 12]  # sums: -3, 1, 0, 3

    # Mixed positives and negatives
    # -21 â -2+1 = -1;  3 â 3;  -4 â -4;  111 â 3
    assert module_0.order_by_points([-21, 3, -4, 111]) == [-4, -21, 3, 111]

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Duplicates
    assert module_0.order_by_points([1, 1, 1]) == [1, 1, 1]

    # Multi-digit negatives
    # -123 â -1+2+3 = 4;  -100 â -1+0+0 = -1;  22 â 4
    assert module_0.order_by_points([-123, -100, 22]) == [-100, -123, 22]

    print("All tests passed!")


test_order_by_points()

# Generated at 2026-10-24 14:54:48.080740
# Unit test for function order_by_points

# Generated at 2026-10-24 14:54:50.494584
# Unit test for function order_by_points

# Generated at 2026-10-24 14:54:52.908121
# Unit test for function order_by_points