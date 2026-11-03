

# Generated at 2026-11-02 00:29:24.873906
# Unit test for function order_by_points
def test_order_by_points():
    # Basic case: sort by digit sum
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # digits: 1->1, 11->2, -1->-1, -11->0, -12->(-1+2)=1

    # Negative numbers: first digit is negated
    assert module_0.order_by_points([-12, -11]) == [-11, -12]  # keys: 0, 1
    assert module_0.order_by_points([-1, 1]) == [-1, 1]        # keys: -1, 1

    # Ties preserve original (stable) order
    assert module_0.order_by_points([56, 65]) == [56, 65]                  # both key 11
    assert module_0.order_by_points([12, 21, 3]) == [12, 21, 3]            # all key 3
    assert module_0.order_by_points([123456789, 987654321]) == [123456789, 987654321]  # both key 45

    # Sorting actually changes order
    assert module_0.order_by_points([56, 65, 7]) == [7, 56, 65]            # keys: 11, 11, 7
    assert module_0.order_by_points([0, 30, 12]) == [0, 12, 30]            # keys: 0, 3, 3

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Zero and mixed values
    assert module_0.order_by_points([0, -5, 14]) == [-5, 14, 0]            # keys: 0, -5, 5

    # Larger mixed example
    assert module_0.order_by_points([99, -99, 100, -100]) == [-100, -99, 100, 99]
    # keys: 99->18, -99->0, 100->1, -100->-1

    # Original list is not modified (sorted returns new list)
    nums = [3, 1, 2]
    module_0.order_by_points(nums)
    assert nums == [3, 1, 2]

# Generated at 2026-11-02 00:30:04.297386
# Unit test for function order_by_points
def test_order_by_points():
    # Basic ordering by digit sum (negative numbers: first digit negated)
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Simple positive numbers
    assert module_0.order_by_points([12, 3, 21]) == [3, 12, 21]  # sums: 3, 3, 3 -> stable
    assert module_0.order_by_points([56, 65, 12, -45]) == [-45, 12, 56, 65]  # 11,11,3,1

    # Empty and single-element lists
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([5]) == [5]
    assert module_0.order_by_points([-7]) == [-7]  # -7 -> -7

    # Stability: ties keep original relative order
    assert module_0.order_by_points([12, 21, 3]) == [12, 21, 3]  # all digit sums = 3
    assert module_0.order_by_points([99, 18, 27]) == [18, 27, 99]  # 18,9,9 -> 18 before 27

    # Mixed negatives and positives
    assert module_0.order_by_points([0, 6, 6, -76, -22, 9]) == [-76, 0, -22, 6, 6, 9]
    assert module_0.order_by_points([-99, 97]) == [-99, 97]  # 0 vs 16

    # Multi-digit values
    assert module_0.order_by_points([1234, 12345, 12]) == [12, 1234, 12345]  # 10, 15, 3
    assert module_0.order_by_points([123456, 65, 55]) == [55, 65, 123456]    # 21, 11, 10

    # Zero handled correctly
    assert module_0.order_by_points([0, -0]) == [0, 0]

    # Input list is not mutated (sorted returns a new list)
    original = [3, 1, 2]
    module_0.order_by_points(original)
    assert original == [3, 1, 2]

    # Result is a list
    assert isinstance(module_0.order_by_points([2, 1]), list)

# Generated at 2026-11-02 00:30:48.226355
# Unit test for function order_by_points
def test_order_by_points():
    # Basic example: negative numbers have their first digit negated
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Ties preserve original order (stable sort)
    assert module_0.order_by_points([21, 12]) == [21, 12]
    assert module_0.order_by_points([56, 65]) == [56, 65]
    assert module_0.order_by_points([100, 10, 1]) == [100, 10, 1]

    # Negative multi-digit numbers
    assert module_0.order_by_points([-123, -321]) == [-321, -123]

    # Mixed positives and negatives
    assert module_0.order_by_points([12, -10, 2, -3, 1]) == [-3, -10, 1, 2, 12]

    # Zero and small values
    assert module_0.order_by_points([0, -1, 1]) == [-1, 0, 1]

    # Already sorted input stays sorted
    assert module_0.order_by_points([3, 12, 30]) == [3, 12, 30]

    # Two-digit negatives with same absolute digit sum
    assert module_0.order_by_points([-21, -12]) == [-21, -12]


if __name__ == "__main__":
    test_order_by_points()
    print("All tests passed.")

# Generated at 2026-11-02 00:31:28.515157
# Unit test for function order_by_points
def test_order_by_points():
    # Sort by digit sum, ascending
    assert module_0.order_by_points([123, 45, 9]) == [123, 45, 9]
    # Negative numbers: leading digit is negated
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert module_0.order_by_points([12, -10, 100, -30]) == [-30, -10, 100, 12]
    # Mixed signs
    assert module_0.order_by_points([0, 1, -1]) == [-1, 0, 1]
    # Empty and single-element lists
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([5]) == [5]
    assert module_0.order_by_points([0]) == [0]
    # Equal keys: stable sort preserves input order
    assert module_0.order_by_points([56, 65]) == [56, 65]
    assert module_0.order_by_points([56, 65, 100, 10]) == [100, 10, 56, 65]
    assert module_0.order_by_points([1, 10, 100]) == [1, 10, 100]
    # Larger multi-digit values
    assert module_0.order_by_points([1234, 4231, 1111]) == [1111, 1234, 4231]
    # All negative values
    assert module_0.order_by_points([-5, -3, -8]) == [-8, -5, -3]

# Generated at 2026-11-02 00:31:59.499917
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers sorted by digit sum
    assert module_0.order_by_points([56, 11, 45]) == [11, 56, 45]  # sums: 11->2, 56->11, 45->9

    # Classic example with negatives (first digit negated)
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([0]) == [0]

    # Mixed positives and negatives
    assert module_0.order_by_points([1234, 423, 463, 145, 123, 44, 23, 1, -44]) == \
        [-44, 1, 23, 123, 44, 423, 1234, 145, 463]

    # Stability: equal digit sums preserve original order
    assert module_0.order_by_points([56, 65]) == [56, 65]
    assert module_0.order_by_points([21, 12, 3]) == [3, 21, 12]  # 3->3, 21->3, 12->3

    # Negative numbers where leading digit dominates
    assert module_0.order_by_points([-99, -100, 5]) == [-100, -99, 5]  # -1, 0, 5

    # All zeros
    assert module_0.order_by_points([0, 0, 0]) == [0, 0, 0]

    # Larger negative values
    assert module_0.order_by_points([-123, 321]) == [321, -123]  # -123 -> -1+2+3=4, 321->6