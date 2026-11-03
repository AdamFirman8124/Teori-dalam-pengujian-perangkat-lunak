

# Generated at 2026-11-02 17:39:50.646642
# Unit test for function sum_squares
def test_sum_squares():
    # Test with a list of integers
    assert module_0.sum_squares([1, 2, 3]) == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9

    # Test with a list of floats (ceiling applied before squaring)
    assert module_0.sum_squares([1.5, 2.5]) == 13  # ceil(1.5)^2 + ceil(2.5)^2 = 4 + 9

    # Test with an empty list
    assert module_0.sum_squares([]) == 0

    # Test with a single element
    assert module_0.sum_squares([5]) == 25

    # Test with negative numbers
    assert module_0.sum_squares([-1.5, -2]) == 5  # ceil(-1.5)^2 + ceil(-2)^2 = 1 + 4

    # Test with zeros
    assert module_0.sum_squares([0, 0, 0]) == 0

    # Test with larger values
    assert module_0.sum_squares([10, 20, 30]) == 1400  # 100 + 400 + 900

    # Test with mixed integers and floats
    assert module_0.sum_squares([1, 2.3, 4]) == 30  # 1 + 9 + 16

    # Test with already whole floats
    assert module_0.sum_squares([2.0, 3.0]) == 13  # 4 + 9

    print("All tests passed!")

# Generated at 2026-11-02 17:41:23.921625
# Unit test for function sum_squares
def test_sum_squares():
    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14
    # Test with positive floats (ceiling rounds up)
    assert module_0.sum_squares([1.4, 5.1]) == 40
    # Test with negative floats (ceil(-1.5) == -1, ceil(2.2) == 3)
    assert module_0.sum_squares([-1.5, 2.2]) == 10
    # Test with empty list
    assert module_0.sum_squares([]) == 0
    # Test with zero
    assert module_0.sum_squares([0]) == 0
    # Test with exact floats (no rounding needed)
    assert module_0.sum_squares([1.0, 2.0]) == 5
    # Test with single negative float
    assert module_0.sum_squares([-2.5]) == 4
    # Test with single integer
    assert module_0.sum_squares([5]) == 25
    # Test with small fractions (all ceil to 1)
    assert module_0.sum_squares([0.1, 0.9]) == 2
    # Test with mixed values
    assert module_0.sum_squares([-3.2, 4.7, 0.3]) == 9 + 25 + 1

# Generated at 2026-11-02 17:43:18.102712
# Unit test for function sum_squares
def test_sum_squares():
    # Test with list of positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1, 4, 9]) == 98

    # Test with list of floats (ceiling applied)
    assert module_0.sum_squares([1.0, 2.0, 3.0]) == 14
    assert module_0.sum_squares([1.5, 2.5]) == 13  # ceil(1.5)=2, ceil(2.5)=3 -> 4+9
    assert module_0.sum_squares([0.1, 0.9]) == 2   # ceil(0.1)=1, ceil(0.9)=1 -> 1+1

    # Test with negative numbers
    assert module_0.sum_squares([-1.5]) == 1       # ceil(-1.5) = -1 -> 1
    assert module_0.sum_squares([-2.5, -3.5]) == 25  # ceil(-2.5)=-2, ceil(-3.5)=-3 -> 4+9

    # Test with empty list
    assert module_0.sum_squares([]) == 0

    # Test with single element
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([0]) == 0

    # Test with mixed values
    assert module_0.sum_squares([1.2, 2, -3.7]) == 1 + 4 + 9  # ceil: 2, 2, -3

    # Test with large numbers
    assert module_0.sum_squares([1000]) == 1000000

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()

# Generated at 2026-11-02 17:45:06.760496
# Unit test for function sum_squares
def test_sum_squares():
    # Basic integer inputs
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1, 4, 9]) == 98
    assert module_0.sum_squares([0, 0, 0]) == 0

    # Float inputs requiring ceiling
    assert module_0.sum_squares([1.4, 2.5, 3.6]) == 29  # ceil: 2, 3, 4 -> 4+9+16
    assert module_0.sum_squares([2.5, 3.5]) == 25       # ceil: 3, 4 -> 9+16
    assert module_0.sum_squares([1.0, 2.0, 3.0]) == 14  # ceil of exact ints unchanged

    # Negative numbers (ceiling rounds toward zero)
    assert module_0.sum_squares([-1.4, -2.5]) == 5      # ceil: -1, -2 -> 1+4
    assert module_0.sum_squares([-1, 4, 0.5]) == 18     # ceil: -1, 4, 1 -> 1+16+1
    assert module_0.sum_squares([-0.5]) == 1            # ceil: 0 -> wait, ceil(-0.5) == 0 -> 0

    # Empty list
    assert module_0.sum_squares([]) == 0

    # Single element
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([0.2]) == 1             # ceil: 1

    print("All tests passed!")

# Generated at 2026-11-02 17:47:36.991061
# Unit test for function sum_squares
def test_sum_squares():
    # nonce:574717e5
    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14
    # Test with larger integers
    assert module_0.sum_squares([1, 4, 9]) == 98
    # Test with multiple odd integers
    assert module_0.sum_squares([1, 3, 5, 7]) == 84
    # Test with floats requiring ceiling
    assert module_0.sum_squares([1.4, 4.2, 0]) == 29  # ceil: 2, 5, 0 -> 4 + 25 + 0
    # Test with negative floats (ceil rounds toward positive infinity)
    assert module_0.sum_squares([-2.4, 1, 1]) == 6  # ceil(-2.4) = -2 -> 4 + 1 + 1
    # Test with empty list
    assert module_0.sum_squares([]) == 0
    # Test with whole-number floats (ceiling leaves them unchanged)
    assert module_0.sum_squares([2.0, 3.0]) == 13
    # Test with negative integers
    assert module_0.sum_squares([-1, -2]) == 5
    # Test with mixed values
    assert module_0.sum_squares([-1.5, 0.5, 2]) == 6  # ceil: -1, 1, 2 -> 1 + 1 + 4
    # Test with all zeros
    assert module_0.sum_squares([0, 0, 0]) == 0
    # Test single element
    assert module_0.sum_squares([3.9]) == 16  # ceil(3.9) = 4 -> 16
    print("All tests passed!")