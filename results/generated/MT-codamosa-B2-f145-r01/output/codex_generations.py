

# Generated at 2026-11-02 10:04:40.869935
# Unit test for function order_by_points
def test_order_by_points():
    # Standard example: negatives have their first digit negated
    # 1->1, 11->2, -1->-1, -11->-1+1=0
    assert module_0.order_by_points([1, 11, -1, 11, -11]) == [-1, -11, 1, 11, 11]

    # All digit sums equal (10 each) -> stable sort preserves input order
    assert module_0.order_by_points([1234, 4231, 3421, 2341, 2413]) == [1234, 4231, 3421, 2341, 2413]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([7]) == [7]

    # All negatives: sums are -1, -2, -3
    assert module_0.order_by_points([-1, -2, -3]) == [-3, -2, -1]

    # Mixed positives, negatives, and zero
    assert module_0.order_by_points([0, -5, 5]) == [-5, 0, 5]

    # Ties keep original order (sort stability)
    assert module_0.order_by_points([56, 65]) == [56, 65]
    assert module_0.order_by_points([21, 12]) == [21, 12]

    # First-digit negation for negatives: -123 -> -1+2+3 = 4, -321 -> -3+2+1 = 0
    assert module_0.order_by_points([-123, -321]) == [-321, -123]

    # Larger mixed case: 9->9, -9->-9, 99->18, -99->-9+9=0
    assert module_0.order_by_points([9, -9, 99, -99]) == [-9, -99, 9, 99]

    # Positive ordering by digit sum: 100->1, 2->2, 11->2 (tie, stable)
    assert module_0.order_by_points([100, 11, 2]) == [100, 2, 11]


if __name__ == "__main__":
    test_order_by_points()
    print("All tests passed!")

# Generated at 2026-11-02 10:05:20.602418
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers
    assert module_0.order_by_points([12, 3, 45]) == [3, 12, 45]  # sums: 3, 3, 9 -> stable ties
    
    # Canonical example: negative first digit counts negatively
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    
    # Empty list
    assert module_0.order_by_points([]) == []
    
    # Single element
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([-123]) == [-123]
    
    # Negative vs positive with same magnitude
    assert module_0.order_by_points([-5, 5]) == [-5, 5]  # sums: -5, 5
    
    # Stability on ties (original order preserved)
    assert module_0.order_by_points([21, 12]) == [21, 12]  # both sum to 3
    assert module_0.order_by_points([56, 65, 12]) == [12, 56, 65]  # 56 and 65 tie (sum 11)
    
    # All negative numbers
    assert module_0.order_by_points([-21, -12]) == [-21, -12]  # sums: -1, 1
    
    # Duplicates
    assert module_0.order_by_points([3, 3, 3]) == [3, 3, 3]
    
    # Mixed large values
    assert module_0.order_by_points([99, -99, 100, -100]) == [-99, -100, 99, 100]
    # sums: 18, 0 (i.e., -9+9), 1, -1 -> order: -100(-1), -99(0), 100(1), 99(18)
    
    # Zero handling
    assert module_0.order_by_points([10, 0, 1]) == [0, 1, 10]  # sums: 1, 0, 1 -> 0 first, then 10/1 tie
    
    print("All order_by_points tests passed!")


if __name__ == "__main__":
    test_order_by_points()

# Generated at 2026-11-02 10:06:00.325561
# Unit test for function order_by_points
def test_order_by_points():
    # Basic example with mixed positive and negative numbers
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([42]) == [42]

    # All positive numbers
    assert module_0.order_by_points([56, 23, 9, 101]) == [101, 23, 9, 56]

    # Stability: equal keys preserve original order
    assert module_0.order_by_points([21, 12]) == [21, 12]
    assert module_0.order_by_points([0, 10, 100]) == [0, 10, 100]

    # Negative numbers: first digit is negated in the key
    assert module_0.order_by_points([-10, 12, 3]) == [-10, 12, 3]
    assert module_0.order_by_points([-123, 123]) == [-123, 123]
    assert module_0.order_by_points([-5, 5]) == [-5, 5]
    assert module_0.order_by_points([999, -999]) == [-999, 999]

    # Already sorted input remains unchanged
    assert module_0.order_by_points([-1, 0, 1, 2]) == [-1, 0, 1, 2]

    # Duplicates
    assert module_0.order_by_points([11, 11, 2]) == [2, 11, 11]

    print("All tests passed!")


if __name__ == "__main__":
    test_order_by_points()

# Generated at 2026-11-02 10:07:24.913530
# Unit test for function order_by_points
def test_order_by_points():
    # Mixed positive and negative numbers
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # Larger list; ties broken by original index (stable sort)
    assert module_0.order_by_points([1234, 423, 463, 145, 2, 423, 423, 53, 6, 37, 345, 431, 8, 87, 99]) == \
        [2, 6, 53, 431, 8, 423, 423, 423, 1234, 145, 37, 345, 463, 87, 99]
    # Empty list
    assert module_0.order_by_points([]) == []
    # Negatives with various digit sums
    assert module_0.order_by_points([1, -11, -32, 43, 23, -56, 43, -71, 44, -52, 10]) == \
        [-71, -52, -32, -11, 1, -56, 10, 23, 43, 43, 44]
    # Single element
    assert module_0.order_by_points([56]) == [56]
    # Zero and already-ordered case
    assert module_0.order_by_points([0, 10, 2]) == [0, 10, 2]
    # Negative single digits
    assert module_0.order_by_points([-5, 3, -1]) == [-5, -1, 3]
    print("test_order_by_points passed")

# Generated at 2026-11-02 10:08:20.884537
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers sorted by digit sum
    assert module_0.order_by_points([12, 3, 21]) == [3, 12, 21]  # sums: 3, 3, 3 (stable)
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([0]) == [0]
    assert module_0.order_by_points([0, 6, 6, -76, -21, 1]) == [-76, -21, 0, 1, 6, 6]
    # Negative single digits
    assert module_0.order_by_points([-1, -2, -3]) == [-3, -2, -1]
    # Mixed multi-digit values
    assert module_0.order_by_points([56, 65, 100, -100]) == [-100, 100, 56, 65]  # sums: 1, 1, 11, 11
    # Stability for equal keys
    assert module_0.order_by_points([23, 32, 14]) == [23, 32, 14]  # all sum to 5, order preserved
    # Single negative number
    assert module_0.order_by_points([-19]) == [-19]  # sum: -1 + 9 = 8