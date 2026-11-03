

# Generated at 2026-11-02 21:49:57.288270
# Unit test for function order_by_points
def test_order_by_points():
    # Basic case with positive and negative numbers
    # digit sums: 1->1, 11->2, -1->-1, -11->0, -12->1
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([42]) == [42]

    # Positive numbers, stable order for equal digit sums
    # digit sums: 56->11, 65->11, 12->3, 3->3
    assert module_0.order_by_points([56, 65, 12, 3]) == [12, 3, 56, 65]

    # All equal digit sums preserves original order
    assert module_0.order_by_points([21, 12, 30, 3]) == [21, 12, 30, 3]

    # All negative single digits
    assert module_0.order_by_points([-5, -3, -8]) == [-8, -5, -3]

    # Duplicates
    assert module_0.order_by_points([12, 21, 12]) == [12, 21, 12]

    # Larger numbers, equal digit sums stay stable
    # digit sums: 99->18, 18->9, 90->9
    assert module_0.order_by_points([99, 18, 90]) == [18, 90, 99]

    # Zero handling
    assert module_0.order_by_points([0, 10, 1]) == [0, 10, 1]

    # Mixed: negative leads to smaller key even with more digits
    # digit sums: -99->-18, 9->9, 18->9
    assert module_0.order_by_points([9, 18, -99]) == [-99, 9, 18]


if __name__ == "__main__":
    test_order_by_points()
    print("All tests passed.")

# Generated at 2026-11-02 21:51:27.085035
# Unit test for function order_by_points
def test_order_by_points():
    # Basic case: digit sums are 1, 2, -1, 0, 1 (stable sort keeps 1 before -12)
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([123]) == [123]

    # Mixed positives/negatives with ties (stability: -76 stays before -21)
    assert module_0.order_by_points([0, 6, 6, -76, -21, 1, 2]) == [-76, -21, 0, 1, 2, 6, 6]

    # All equal digit sums -> original order preserved
    assert module_0.order_by_points([12, 21, 3]) == [12, 21, 3]

    # Negative first digit lowers the key: -34 -> -3+4 = 1
    assert module_0.order_by_points([-34, 7]) == [-34, 7]

    # Multi-digit comparisons: keys are 18, 1, 2
    assert module_0.order_by_points([99, 100, 11]) == [100, 11, 99]

    # Negative number with single digit: -5 -> -5
    assert module_0.order_by_points([-5, 5, 0]) == [-5, 0, 5]


if __name__ == "__main__":
    test_order_by_points()
    print("All tests passed!")

# Generated at 2026-11-02 21:52:37.217702
# Unit test for function order_by_points
def test_order_by_points():
    # Basic positive numbers sorted by digit sum
    assert module_0.order_by_points([56, 65, 34, 12, 8]) == [12, 8, 34, 56, 65]

    # Mixed positive and negative numbers
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Zero handling
    assert module_0.order_by_points([0, 10, 100]) == [0, 10, 100]

    # Duplicates preserved
    assert module_0.order_by_points([2, 2, 2]) == [2, 2, 2]

    # Stability: equal digit sums keep original order
    assert module_0.order_by_points([21, 12]) == [21, 12]

    # Negative single digit
    assert module_0.order_by_points([-5, 5]) == [-5, 5]

    # Larger numbers
    assert module_0.order_by_points([99, 123, 456, 789]) == [123, 456, 789, 99]

    # Negative multi-digit with carry-over behavior
    assert module_0.order_by_points([-19, 10]) == [-19, 10]

    print("All tests passed!")


test_order_by_points()

# Generated at 2026-11-02 21:54:08.714148
# Unit test for function order_by_points
def test_order_by_points():
    # Already sorted by digit sum
    assert module_0.order_by_points([123, 456, 789]) == [123, 456, 789]

    # Unsorted positives: sums are 11, 5, 9
    assert module_0.order_by_points([56, 32, 9]) == [32, 9, 56]

    # Negative numbers: first digit negated (from problem example)
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Mixed positive and negative
    assert module_0.order_by_points([12, -5, 30]) == [-5, 12, 30]

    # All negatives: sums -3, -1, -2
    assert module_0.order_by_points([-3, -1, -2]) == [-3, -2, -1]

    # Empty list
    assert module_0.order_by_points([]) == []

    # Single element
    assert module_0.order_by_points([5]) == [5]

    # Zero and negatives around zero
    assert module_0.order_by_points([0, 10, -10]) == [-10, 0, 10]

    # Equal digit sums: stable sort preserves original order
    assert module_0.order_by_points([11, 2]) == [11, 2]
    assert module_0.order_by_points([2, 11]) == [2, 11]
    assert module_0.order_by_points([21, 12, 3]) == [21, 12, 3]

    # Duplicates
    assert module_0.order_by_points([5, 5, 5]) == [5, 5, 5]

    # Multi-digit negatives mixed with positives
    assert module_0.order_by_points([-99, 18, -7, 45]) == [-99, -7, 18, 45]

    print("All tests passed!")


test_order_by_points()

# Generated at 2026-11-02 21:57:31.124424
# Unit test for function order_by_points
def test_order_by_points():
    assert module_0.order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert module_0.order_by_points([]) == []
    assert module_0.order_by_points([56, 65, 3]) == [3, 56, 65]
    assert module_0.order_by_points([0, 12, -3]) == [-3, 0, 12]
    assert module_0.order_by_points([123, -456, 789]) == [-456, 123, 789]
    assert module_0.order_by_points([5]) == [5]
    assert module_0.order_by_points([10, 1]) == [10, 1]
    assert module_0.order_by_points([-123, 321, -321, 123]) == [-321, -123, 123, 321]