

# Generated at 2026-10-24 14:30:28.549343
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:31.116440
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:33.531676
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:35.945605
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:38.359738
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:40.771934
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:43.184966
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:45.598061
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:48.010992
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:50.424113
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:52.837478
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:55.250354
# Unit test for function order_by_points

# Generated at 2026-10-24 14:30:57.664382
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:00.077191
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:02.493518
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:04.906706
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:07.322478
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:09.733798
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:33.483913
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:42.393169
# Unit test for function order_by_points
def test_order_by_points():assert module_0.order_by_points([]) == []

# Generated at 2026-10-24 14:31:44.894132
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:47.308386
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:49.720749
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:52.134033
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:54.546140
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:56.959536
# Unit test for function order_by_points

# Generated at 2026-10-24 14:31:59.372266
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:01.786051
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:04.199047
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:06.846467
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:09.259544
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:11.672622
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:14.085609
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:38.135291
# Unit test for function order_by_points
def test_order_by_points():assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

# Generated at 2026-10-24 14:32:47.723676
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

# Generated at 2026-10-24 14:32:50.237192
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:52.655271
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:55.067607
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:57.482005
# Unit test for function order_by_points

# Generated at 2026-10-24 14:32:59.899806
# Unit test for function order_by_points

# Generated at 2026-10-24 14:33:02.315512
# Unit test for function order_by_points