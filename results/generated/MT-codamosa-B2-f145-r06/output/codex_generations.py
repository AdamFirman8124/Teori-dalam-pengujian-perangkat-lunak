

# Generated at 2026-11-03 00:24:23.947740
# Unit test for function order_by_points
def test_order_by_points():
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert module_0.order_by_points([1234567, 1234567]) == [1234567, 1234567]
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([1, -11]) == [-11, 1]
    assert module_0.order_by_points([123432, 1234321]) == [1234321, 123432]
    assert module_0.order_by_points([0, 10, -10]) == [0, -10, 10]
    assert module_0.order_by_points([56, 65]) == [56, 65]
    assert module_0.order_by_points([-5, 5]) == [-5, 5]
    assert module_0.order_by_points([99, 18, -99]) == [-99, 18, 99]

test_order_by_points()
print("All tests passed!")

# Generated at 2026-11-03 00:25:25.185244
# Unit test for function order_by_points
def test_order_by_points():
    # nonce:34fd660d
    # Mixed positive/negative numbers
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # Negative numbers have first digit negated in digit sum
    assert module_0.order_by_points([1, -11, -32, 43, 54, -98, 2, -3]) == [-3, -32, -98, -11, 1, 2, 43, 54]
    # Ascending input with large numbers
    assert module_0.order_by_points([1234, 423, 463, 145, 2, 423, 423, 53, 6, 37, 3457, 3, 56, 0, 46]) == \
        [0, 2, 3, 6, 53, 423, 423, 423, 1234, 145, 37, 46, 56, 463, 3457]
    # Descending input
    assert module_0.order_by_points([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert module_0.order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -100]) == [-100, 1, 10, 2, 3, 4, 5, 6, 7, 8, 9]
    # Empty list
    assert module_0.order_by_points([]) == []
    # Single element
    assert module_0.order_by_points([-5]) == [-5]
    assert module_0.order_by_points([0]) == [0]
    # Stability: equal digit sums preserve original order
    assert module_0.order_by_points([21, 12, 3]) == [21, 12, 3]
    assert module_0.order_by_points([10, 1]) == [10, 1]  # both digit sum 1

# Generated at 2026-11-03 00:26:29.589745
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers
    assert module_0.order_by_points([56, 65, 12]) == [12, 56, 65]
    
    # Mixed positive and negative numbers
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    
    # Multiple elements with ties (stable sort preserves input order)
    assert module_0.order_by_points([1234, 423, 463, 145, 2, 423, 423]) == [2, 423, 423, 423, 1234, 145, 463]
    
    # Negative numbers with digit sums determining order
    assert module_0.order_by_points([1, -11, -32, 43, 54, -6, 7]) == [-6, -32, -11, 1, 43, 7, 54]
    
    # Empty list
    assert module_0.order_by_points([]) == []
    
    # Single element
    assert module_0.order_by_points([5]) == [5]
    
    # Contains zero
    assert module_0.order_by_points([0, 10, 1]) == [0, 10, 1]
    
    # All negative numbers
    assert module_0.order_by_points([-12, -3, -21]) == [-3, -21, -12]
    
    # Negative sign only affects first digit
    assert module_0.order_by_points([-1, -2, -3]) == [-3, -2, -1]
    
    # Already sorted by digit sum
    assert module_0.order_by_points([100, 20, 3]) == [100, 20, 3]

# Generated at 2026-11-03 00:27:39.733973
# Unit test for function order_by_points
def test_order_by_points():
    # Classic mixed-sign case with digit-sum ties (stable sort)
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # Multiple elements with equal digit sums keep original relative order
    assert module_0.order_by_points([1234, 423, 463, 145, 2, 423, 423]) == [2, 423, 423, 423, 1234, 145, 463]
    # Empty list
    assert module_0.order_by_points([]) == []
    # Single elements
    assert module_0.order_by_points([5]) == [5]
    assert module_0.order_by_points([-5]) == [-5]
    # Zero, positive, negative
    assert module_0.order_by_points([0, 1, -1]) == [-1, 0, 1]
    # All tie on digit sum -> stability preserves input order
    assert module_0.order_by_points([21, 12, 3]) == [21, 12, 3]
    # Negatives: first digit negated (-12 -> -1+2=1, -11 -> -1+1=-2)
    assert module_0.order_by_points([-12, -11]) == [-11, -12]
    assert module_0.order_by_points([-99, -10]) == [-10, -99]
    # Ascending digit sums
    assert module_0.order_by_points([100, 20, 3]) == [100, 20, 3]
    # Ties among positives resolved stably
    assert module_0.order_by_points([56, 65, 11]) == [11, 56, 65]
    # Mixed signs interleaved
    assert module_0.order_by_points([-3, 12, -12, 21]) == [-3, -12, 12, 21]
    # Input list must not be mutated
    nums = [3, 1]
    module_0.order_by_points(nums)
    assert nums == [3, 1]

# Generated at 2026-11-03 00:28:49.777576
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers
    assert module_0.order_by_points([12, 10]) == [10, 12]
    # Negative numbers sort by negated first digit
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    # Increasing digit sums
    assert module_0.order_by_points([12345, 1234, 123, 12, 1]) == [1, 12, 123, 1234, 12345]
    # Empty list
    assert module_0.order_by_points([]) == []
    # Mixed values with duplicates and stability
    assert module_0.order_by_points([0, 6, 6, -76, -76, 123]) == [-76, -76, 0, 6, 6, 123]
    # Single element
    assert module_0.order_by_points([5]) == [5]
    # All negative
    assert module_0.order_by_points([-1, -2, -3]) == [-3, -2, -1]
    # Zero
    assert module_0.order_by_points([0, -10, 1]) == [-10, 0, 1]