

# Generated at 2026-11-01 21:52:16.914892
# Unit test for function sum_squares
def test_sum_squares():
    import math

    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14  # 1 + 4 + 9

    # Test with floats that need ceiling
    assert module_0.sum_squares([1.5, 2.5]) == 13  # ceil(1.5)=2 -> 4, ceil(2.5)=3 -> 9

    # Test with negative floats
    assert module_0.sum_squares([-1.5, -2.5]) == 5  # ceil(-1.5)=-1 -> 1, ceil(-2.5)=-2 -> 4

    # Test with negative integers
    assert module_0.sum_squares([-1, -2, -3]) == 14  # 1 + 4 + 9

    # Test with mixed positive and negative values
    assert module_0.sum_squares([1.2, -3.7, 2.0]) == 18  # 4 + 9 + 4

    # Test with empty list
    assert module_0.sum_squares([]) == 0

    # Test with zero
    assert module_0.sum_squares([0]) == 0

    # Test with single element
    assert module_0.sum_squares([2.1]) == 9  # ceil(2.1)=3 -> 9

    # Test with large values
    assert module_0.sum_squares([100.1]) == 101**2  # ceil(100.1)=101 -> 10201

    print("All test cases passed!")


test_sum_squares()

# Generated at 2026-11-01 21:52:39.237852
# Unit test for function sum_squares
def test_sum_squares():
    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14

    # Test with empty list
    assert module_0.sum_squares([]) == 0

    # Test with single element
    assert module_0.sum_squares([5]) == 25

    # Test with floats that need ceiling
    assert module_0.sum_squares([1.5, 2.5]) == 13  # 2^2 + 3^2

    # Test with negative floats (ceiling rounds toward zero)
    assert module_0.sum_squares([-1.5]) == 1  # ceil(-1.5) = -1, (-1)^2 = 1

    # Test with negative integers
    assert module_0.sum_squares([-1, -2, -3]) == 14

    # Test with zeros
    assert module_0.sum_squares([0, 0, 0]) == 0

    # Test with mixed values
    assert module_0.sum_squares([1.1, 2, -3.7]) == 17  # 4 + 4 + 9

    # Test with large numbers
    assert module_0.sum_squares([100.1, 200.9]) == 90601  # 101^2 + 201^2

    # Test with fractional part close to next integer
    assert module_0.sum_squares([2.999]) == 9  # ceil(2.999) = 3

test_sum_squares()
print("All tests passed!")

# Generated at 2026-11-01 21:53:21.020030
# Unit test for function sum_squares
def test_sum_squares():
    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14  # 1 + 4 + 9
    
    # Test with floats (ceiling applied)
    assert module_0.sum_squares([1.4, 5.1, -4.0]) == 56  # ceil(1.4)=2, ceil(5.1)=6, ceil(-4.0)=-4 -> 4 + 36 + 16
    
    # Test with negative floats
    assert module_0.sum_squares([-1.4, 4.6, 6.3]) == 75  # ceil(-1.4)=-1, ceil(4.6)=5, ceil(6.3)=7 -> 1 + 25 + 49
    
    # Test with empty list
    assert module_0.sum_squares([]) == 0
    
    # Test with single element
    assert module_0.sum_squares([2]) == 4
    
    # Test with zero
    assert module_0.sum_squares([0]) == 0
    
    # Test with value between -1 and 0 (ceils to 0)
    assert module_0.sum_squares([-0.5]) == 0
    
    # Test with all negative integers
    assert module_0.sum_squares([-1, -2, -3]) == 14  # 1 + 4 + 9
    
    # Test with mixed large numbers
    assert module_0.sum_squares([10.9, -3.2]) == 134  # ceil(10.9)=11 -> 121, ceil(-3.2)=-3 -> 9

# Generated at 2026-11-01 21:54:04.907274
# Unit test for function sum_squares
def test_sum_squares():
    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14
    # Test with floats requiring ceiling
    assert module_0.sum_squares([1.5, 2.5]) == 13  # ceil(1.5)=2, ceil(2.5)=3 -> 4+9
    # Test with negative floats
    assert module_0.sum_squares([-1.5, -2.5]) == 5  # ceil(-1.5)=-1, ceil(-2.5)=-2 -> 1+4
    # Test with mixed values
    assert module_0.sum_squares([1, -2.7, 3.1]) == 15  # 1 + ceil(-2.7)^2 + ceil(3.1)^2 = 1+4+16... wait
    # Recompute: ceil(-2.7) = -2 -> 4; ceil(3.1) = 4 -> 16; total = 21
    assert module_0.sum_squares([1, -2.7, 3.1]) == 21
    # Test with empty list
    assert module_0.sum_squares([]) == 0
    # Test with single zero
    assert module_0.sum_squares([0]) == 0
    # Test with value just above an integer
    assert module_0.sum_squares([1.01]) == 4  # ceil(1.01) = 2
    # Test with negative fraction near zero
    assert module_0.sum_squares([-0.5]) == 0  # ceil(-0.5) = 0
    # Test with large numbers
    assert module_0.sum_squares([100.2, 200.8]) == 101**2 + 201**2  # 10201 + 40401 = 50602
    # Test with all identical elements
    assert module_0.sum_squares([2.1, 2.1, 2.1]) == 27  # 3 * 3^2

# Generated at 2026-11-01 21:54:44.694566
# Unit test for function sum_squares
def test_sum_squares():
    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1, 4, 9]) == 98

    # Test with floats (ceiling applied before squaring)
    assert module_0.sum_squares([1.4, 5.1, 2.0, 1.0, 4.5]) == 70
    assert module_0.sum_squares([1.0, 2.0, 3.0]) == 14

    # Test with negative numbers (ceil rounds toward positive infinity)
    assert module_0.sum_squares([-1.4, 4.2, 0]) == 26
    assert module_0.sum_squares([-1.5]) == 1
    assert module_0.sum_squares([-2.5, -3.5]) == 4 + 9

    # Test with zero
    assert module_0.sum_squares([0]) == 0
    assert module_0.sum_squares([0, 0, 0]) == 0

    # Test with empty list
    assert module_0.sum_squares([]) == 0

    # Test with single element
    assert module_0.sum_squares([2.5]) == 9
    assert module_0.sum_squares([10]) == 100

    # Test with mixed values
    assert module_0.sum_squares([1.1, -1.1, 2.2]) == 1 + 1 + 9

    # Test with large numbers
    assert module_0.sum_squares([100.1, 200.9]) == 101**2 + 201**2

    print("All tests passed!")


if __name__ == "__main__":
    test_sum_squares()