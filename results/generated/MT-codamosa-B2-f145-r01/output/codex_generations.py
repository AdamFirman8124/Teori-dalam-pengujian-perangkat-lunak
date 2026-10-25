

# Generated at 2026-10-24 11:05:25.688713
# Unit test for function order_by_points
def test_order_by_points():
    # Basic ordering by digit sum
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Digit sums: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> -2, -12 -> -3
    # Sorted ascending: -1(-1), -11(-2)... wait check: -12 -> -(1+2) = -3, so order: -12, -11, -1, 1, 11
    # Corrected expectation:
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-12, -11, -1, 1, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Same digit sum -> stable order preserved
    assert module_0.order_by_points([21, 12, 3]) == [21, 12, 3]  # all sum to 3

    # All negative
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -23, -9]
    # -56 -> -11, -23 -> -5, -9 -> -9 => order: -56, -9, -23
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -9, -23]

    # Zero
    assert module_0.order_by_points([0, -10, 10]) == [-10, 0, 10]
    # -10 -> -1, 0 -> 0, 10 -> 1

    print("All tests passed!")

# Generated at 2026-10-24 11:05:26.999652
# Unit test for function order_by_points
def test_order_by_points():
    # Basic ordering by digit sum
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Digit sums: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> -2, -12 -> -3
    # Sorted ascending: -1(-1), -11(-2)... wait check: -12 -> -(1+2) = -3, so order: -12, -11, -1, 1, 11
    # Corrected expectation:
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-12, -11, -1, 1, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Same digit sum -> stable order preserved
    assert module_0.order_by_points([21, 12, 3]) == [21, 12, 3]  # all sum to 3

    # All negative
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -23, -9]
    # -56 -> -11, -23 -> -5, -9 -> -9 => order: -56, -9, -23
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -9, -23]

    # Zero
    assert module_0.order_by_points([0, -10, 10]) == [-10, 0, 10]
    # -10 -> -1, 0 -> 0, 10 -> 1

    print("All tests passed!")

# Generated at 2026-10-24 11:05:28.306275
# Unit test for function order_by_points
def test_order_by_points():
    # Basic ordering by digit sum
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Digit sums: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> -2, -12 -> -3
    # Sorted ascending: -1(-1), -11(-2)... wait check: -12 -> -(1+2) = -3, so order: -12, -11, -1, 1, 11
    # Corrected expectation:
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-12, -11, -1, 1, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Same digit sum -> stable order preserved
    assert module_0.order_by_points([21, 12, 3]) == [21, 12, 3]  # all sum to 3

    # All negative
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -23, -9]
    # -56 -> -11, -23 -> -5, -9 -> -9 => order: -56, -9, -23
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -9, -23]

    # Zero
    assert module_0.order_by_points([0, -10, 10]) == [-10, 0, 10]
    # -10 -> -1, 0 -> 0, 10 -> 1

    print("All tests passed!")

# Generated at 2026-10-24 11:05:29.635697
# Unit test for function order_by_points
def test_order_by_points():
    # Basic ordering by digit sum
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Digit sums: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> -2, -12 -> -3
    # Sorted ascending: -1(-1), -11(-2)... wait check: -12 -> -(1+2) = -3, so order: -12, -11, -1, 1, 11
    # Corrected expectation:
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-12, -11, -1, 1, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Same digit sum -> stable order preserved
    assert module_0.order_by_points([21, 12, 3]) == [21, 12, 3]  # all sum to 3

    # All negative
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -23, -9]
    # -56 -> -11, -23 -> -5, -9 -> -9 => order: -56, -9, -23
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -9, -23]

    # Zero
    assert module_0.order_by_points([0, -10, 10]) == [-10, 0, 10]
    # -10 -> -1, 0 -> 0, 10 -> 1

    print("All tests passed!")

# Generated at 2026-10-24 11:05:30.948699
# Unit test for function order_by_points
def test_order_by_points():
    # Basic ordering by digit sum
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Digit sums: 1 -> 1, 11 -> 2, -1 -> -1, -11 -> -2, -12 -> -3
    # Sorted ascending: -1(-1), -11(-2)... wait check: -12 -> -(1+2) = -3, so order: -12, -11, -1, 1, 11
    # Corrected expectation:
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-12, -11, -1, 1, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Same digit sum -> stable order preserved
    assert module_0.order_by_points([21, 12, 3]) == [21, 12, 3]  # all sum to 3

    # All negative
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -23, -9]
    # -56 -> -11, -23 -> -5, -9 -> -9 => order: -56, -9, -23
    assert module_0.order_by_points([-56, -23, -9]) == [-56, -9, -23]

    # Zero
    assert module_0.order_by_points([0, -10, 10]) == [-10, 0, 10]
    # -10 -> -1, 0 -> 0, 10 -> 1

    print("All tests passed!")