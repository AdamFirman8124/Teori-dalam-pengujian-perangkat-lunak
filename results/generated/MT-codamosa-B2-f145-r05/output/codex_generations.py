

# Generated at 2026-11-02 16:00:25.146316
# Unit test for function order_by_points
def test_order_by_points():
    # Sorts by digit sum; for negatives the leading digit is negated
    # Keys: 1->1, 11->2, -1->-1, -11->0, -12->1
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Keys: 1234->10, 4231->10, 2211->6, 654->15, 999->27, 69->15
    assert module_0.order_by_points([1234, 4231, 2211, 654, 999, 69]) == [2211, 1234, 4231, 654, 69, 999]

    # Keys: 1->1, -11->0, -32->-1, 43->7, 54->9, -6->-6, -7->-7
    assert module_0.order_by_points([1, -11, -32, 43, 54, -6, -7]) == [-7, -6, -32, -11, 1, 43, 54]

    # Empty and single-element lists
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([5]) == [5]

    # All negative single digits
    assert module_0.order_by_points([-5, -3, -1]) == [-5, -3, -1]

    # Zero handling: -10 -> -1, 0 -> 0, 10 -> 1
    assert module_0.order_by_points([0, -10, 10]) == [-10, 0, 10]

    # Stability: 12, 21, 3 all have digit sum 3, original order preserved
    assert module_0.order_by_points([12, 21, 3]) == [12, 21, 3]

    # Duplicates preserved
    assert module_0.order_by_points([2, 2, -2]) == [-2, 2, 2]

    # Input list is not mutated
    nums = [3, -1, 2]
    module_0.order_by_points(nums)
    assert nums == [3, -1, 2]

# Generated at 2026-11-02 16:02:33.740462
# Unit test for function order_by_points
def test_order_by_points():
    # Basic example from spec: digit sums [1, 2, -1, 0, 1] with stable tie-breaking
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Simple positive numbers: digit sums [11, 11, 7, 3, 2, 17]
    assert module_0.order_by_points([56, 65, 34, 12, 11, 98]) == [11, 12, 34, 56, 65, 98]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Stability: equal digit sums keep original order (56 and 65 both sum to 11)
    assert module_0.order_by_points([56, 65]) == [56, 65]

    # All negatives: digit sums [-12 -> 1, -3 -> -3, -21 -> -1]
    assert module_0.order_by_points([-12, -3, -21]) == [-3, -21, -12]

    # Contains zero: digit sums [10 -> 1, 0 -> 0, 1 -> 1], stable tie between 10 and 1
    assert module_0.order_by_points([10, 0, 1]) == [0, 10, 1]

    # Multi-digit sums: [1234 -> 10, 4231 -> 10, 2211 -> 6], stable tie between 1234 and 4231
    assert module_0.order_by_points([1234, 4231, 2211]) == [2211, 1234, 4231]

    # Digit sums [99 -> 18, 100 -> 1, 9 -> 9]
    assert module_0.order_by_points([99, 100, 9]) == [100, 9, 99]

    # Duplicates
    assert module_0.order_by_points([3, 3, 3]) == [3, 3, 3]

    print("All tests passed!")


test_order_by_points()

# Generated at 2026-11-02 16:04:36.380307
# Unit test for function order_by_points
def test_order_by_points():
# nonce:0f8efbea
    # Sort by sum of digits, ascending
    assert module_0.order_by_points([1234, 423, 463, 65, 110, 134]) == [110, 134, 423, 1234, 65, 463]

    # Negative numbers: sign applies only to the leading digit
    assert module_0.order_by_points([1, 11, -1, -11, 2]) == [-1, -11, 1, 11, 2]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Ties keep original (stable) order
    assert module_0.order_by_points([12, 3, 21]) == [12, 3, 21]
    assert module_0.order_by_points([56, 65, 11]) == [11, 56, 65]

    # All-negative input
    assert module_0.order_by_points([-9, -18, -3]) == [-9, -3, -18]

    # Mixed multi-digit negatives and positives
    assert module_0.order_by_points([-56, -65, 12]) == [-65, -56, 12]

    # Zero handling
    assert module_0.order_by_points([10, 0, 1]) == [0, 10, 1]

    # Input list is not mutated
    original = [3, -1, 2]
    module_0.order_by_points(original)
    assert original == [3, -1, 2]

# Generated at 2026-11-02 16:05:33.733698
# Unit test for function order_by_points
def test_order_by_points():
    # Mixed positives/negatives (classic case)
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Equal digit sums: stable sort preserves original order
    assert module_0.order_by_points([12, 3, 21]) == [12, 3, 21]
    assert module_0.order_by_points([56, 65]) == [56, 65]

    # Negatives: first digit negated, rest positive
    assert module_0.order_by_points([-3, -12, 4]) == [-3, -12, 4]
    assert module_0.order_by_points([-123, 123]) == [-123, 123]

    # Zero and sign boundaries
    assert module_0.order_by_points([0, -1, 1]) == [-1, 0, 1]

    # Multi-digit sums
    assert module_0.order_by_points([99, 18, 90]) == [18, 90, 99]

    # Larger mixed example
    assert module_0.order_by_points([120, -91, 34, -5, 7]) == [-91, -5, 120, 34, 7]

    # Input with duplicates
    assert module_0.order_by_points([-11, -11, 2]) == [-11, -11, 2]

    # Already sorted input stays sorted
    assert module_0.order_by_points([-9, 0, 9]) == [-9, 0, 9]

# Generated at 2026-11-02 16:07:01.030825
# Unit test for function order_by_points
def test_order_by_points():
    # Mixed positives and negatives
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # Larger numbers
    assert module_0.order_by_points([1234567, 123, 545, -5644, 4567]) == [123, -5644, 545, 4567, 1234567]
    # Empty list
    assert module_0.order_by_points([]) == []
    # Single element
    assert module_0.order_by_points([0]) == [0]
    # Simple positives/negatives
    assert module_0.order_by_points([0, 1, -1]) == [-1, 0, 1]
    # Stability for equal digit sums (12 -> 3, 21 -> 3)
    assert module_0.order_by_points([12, 21]) == [12, 21]
    # Negative leading digit handling (-100 -> -1, -1 -> -1, stable order kept)
    assert module_0.order_by_points([-100, 10, -1]) == [-100, -1, 10]
    # All negatives
    assert module_0.order_by_points([-34, -23, -12]) == [-12, -23, -34]