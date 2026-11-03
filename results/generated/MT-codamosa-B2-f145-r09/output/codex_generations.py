

# Generated at 2026-11-02 12:22:50.067429
# Unit test for function order_by_points
def test_order_by_points():
    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Positive numbers, distinct digit sums
    assert module_0.order_by_points([56, 65, 43, 12, 4]) == [12, 4, 43, 56, 65]

    # Mixed positive and negative numbers
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Ties on digit sum resolved by stability (input order preserved)
    assert module_0.order_by_points([1234, 423, 46]) == [423, 1234, 46]

    # All elements share the same digit sum
    assert module_0.order_by_points([11, 20, 2]) == [11, 20, 2]

    # Negative single number (first digit negated)
    assert module_0.order_by_points([-5]) == [-5]

    # Zeros
    assert module_0.order_by_points([0, 0, 0]) == [0, 0, 0]

# Generated at 2026-11-02 12:23:51.382791
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers sorted by digit sum
    assert module_0.order_by_points([1234, 4231, 2211, 2141]) == [2211, 2141, 1234, 4231]

    # Negative numbers: first digit carries the negative sign
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Mixed positive and negative numbers
    assert module_0.order_by_points([12, -3, 30, -21, 5]) == [-21, -3, 12, 30, 5]

    # Single element
    assert module_0.order_by_points([42]) == [42]

    # Empty list
    assert module_0.order_by_points([]) == []

    # All negative numbers
    assert module_0.order_by_points([-15, -6, -100, -32]) == [-100, -15, -6, -32]

    # Ties keep original order (stable sort): 12 and 21 both sum to 3
    assert module_0.order_by_points([21, 12, 3]) == [3, 21, 12]

    # Zero handled correctly
    assert module_0.order_by_points([0, -10, 1]) == [0, -10, 1]

    # Large numbers
    assert module_0.order_by_points([999999, 1000000, -999999]) == [-999999, 999999, 1000000]

    print("All tests passed!")


test_order_by_points()

# Generated at 2026-11-02 12:24:57.732901
# Unit test for function order_by_points
def test_order_by_points():
    # Mixed positive and negative numbers (first digit of negatives counts as negative)
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # Empty list
    assert module_0.order_by_points([]) == []
    # Single element
    assert module_0.order_by_points([56]) == [56]
    # All negative numbers
    assert module_0.order_by_points([-1, -11, -2]) == [-2, -1, -11]
    # Equal digit sums preserve original order (stable sort)
    assert module_0.order_by_points([1, 10, 100]) == [1, 10, 100]
    assert module_0.order_by_points([123, 321, 213]) == [123, 321, 213]
    # Zero handling
    assert module_0.order_by_points([0, 12, -12]) == [0, -12, 12]
    # Multi-digit comparisons
    assert module_0.order_by_points([99, 100, 101]) == [100, 101, 99]
    # Negative leading digit dominates ordering
    assert module_0.order_by_points([-123, 45, -6]) == [-6, -123, 45]
    assert module_0.order_by_points([-100, 121, 3]) == [-100, 121, 3]
    print("All test cases passed!")

# Generated at 2026-11-02 12:26:27.638815
# Unit test for function order_by_points
def test_order_by_points():
    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Mixed positive and negative numbers (digit sum of negatives negates first digit)
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Negative numbers only
    assert module_0.order_by_points([-56, -99, -1]) == [-1, -99, -56]

    # Zero, duplicates, and multi-digit positives
    assert module_0.order_by_points([0, 6, 6, -6, 90]) == [-6, 0, 6, 6, 90]

    # All equal digit sums -> stable sort preserves original order
    assert module_0.order_by_points([1234, 4231, 2341, 2413]) == [1234, 4231, 2341, 2413]

    # Already sorted by digit sum
    assert module_0.order_by_points([10, 2, 3]) == [10, 2, 3]

    # Larger mixed case
    assert module_0.order_by_points([3, -44, 21, -2, 100]) == [-2, 3, -44, 100, 21]


if __name__ == "__main__":
    test_order_by_points()
    print("All tests passed!")

# Generated at 2026-11-02 12:27:27.953905
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers sorted by digit sum
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # Digit sums: 10, 10, 6, 3 -> stability keeps 1234 before 4231
    assert module_0.order_by_points([1234, 4231, 2211, 3]) == [3, 2211, 1234, 4231]
    # Empty list
    assert module_0.order_by_points([]) == []
    # Single element
    assert module_0.order_by_points([56]) == [56]
    # Negative numbers: first digit negated
    assert module_0.order_by_points([0, -10, 10]) == [-10, 0, 10]
    assert module_0.order_by_points([-99, -19, 9]) == [-19, -99, 9]
    # Same digit sum -> original (stable) order preserved
    assert module_0.order_by_points([12, 21]) == [12, 21]
    # Mixed large values
    assert module_0.order_by_points([56, 65, 100, -100]) == [-100, 100, 56, 65]
    print("test_order_by_points passed")

test_order_by_points()