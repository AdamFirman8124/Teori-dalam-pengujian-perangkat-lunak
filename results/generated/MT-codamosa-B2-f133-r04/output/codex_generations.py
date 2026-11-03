

# Generated at 2026-11-02 16:01:15.043813
# Unit test for function sum_squares
def test_sum_squares():
    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14, "Expected 14 for [1, 2, 3]"
    
    # Test with floats (ceiling applied)
    assert module_0.sum_squares([1.0, 2.5, 3.2]) == 26, "Expected 26 for [1.0, 2.5, 3.2]"
    
    # Test with empty list
    assert module_0.sum_squares([]) == 0, "Expected 0 for empty list"
    
    # Test with negative numbers
    assert module_0.sum_squares([-1.5, -2]) == 5, "Expected 5 for [-1.5, -2]"
    
    # Test with zero
    assert module_0.sum_squares([0]) == 0, "Expected 0 for [0]"
    
    # Test with mixed values
    assert module_0.sum_squares([2.1, 3.9, -0.5]) == 19, "Expected 19 for [2.1, 3.9, -0.5]"
    
    print("All tests passed!")

# Generated at 2026-11-02 16:04:08.338170
# Unit test for function sum_squares
def test_sum_squares():
    # Test with integers
    assert module_0.sum_squares([1, 2, 3]) == 14  # 1 + 4 + 9

    # Test with floats requiring ceiling
    assert module_0.sum_squares([1.4, 2.5, 3.6]) == 29  # ceil: 2, 3, 4 -> 4 + 9 + 16

    # Test with empty list
    assert module_0.sum_squares([]) == 0

    # Test with negative floats (ceiling rounds toward positive infinity)
    assert module_0.sum_squares([-1.5, -2.2]) == 5  # ceil: -1, -2 -> 1 + 4

    # Test with single element
    assert module_0.sum_squares([5]) == 25

    # Test with zero
    assert module_0.sum_squares([0]) == 0

    # Test with mixed positive and negative values
    assert module_0.sum_squares([-1, 2.7, 3.1]) == 14  # ceil: -1, 3, 4 -> 1 + 9 + 16

    # Test with large numbers
    assert module_0.sum_squares([100.1]) == 10201  # ceil: 101 -> 101^2

    # Test with all negative integers
    assert module_0.sum_squares([-2, -3]) == 13  # 4 + 9

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-02 16:05:10.898828
# Unit test for function sum_squares
def test_sum_squares():
    # Test with positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14
    assert module_0.sum_squares([1, 4, 9]) == 98
    assert module_0.sum_squares([1, 3, 5, 7]) == 84

    # Test with floats (ceiling applied before squaring)
    assert module_0.sum_squares([1.5, 2.2]) == 13   # ceil(1.5)=2, ceil(2.2)=3 -> 4+9
    assert module_0.sum_squares([1.4, 4.2, 0]) == 29  # ceil(1.4)=2, ceil(4.2)=5, ceil(0)=0

    # Test with negative numbers (ceiling rounds toward zero)
    assert module_0.sum_squares([-1.5]) == 1        # ceil(-1.5) = -1 -> 1
    assert module_0.sum_squares([-2.4, 1, 1]) == 6  # ceil(-2.4) = -2 -> 4+1+1
    assert module_0.sum_squares([-3, -4]) == 25     # 9+16

    # Test with empty list
    assert module_0.sum_squares([]) == 0

    # Test with zero
    assert module_0.sum_squares([0]) == 0
    assert module_0.sum_squares([0, 0, 0]) == 0

    # Test with single element
    assert module_0.sum_squares([5]) == 25
    assert module_0.sum_squares([2.1]) == 9         # ceil(2.1)=3

    # Test with large numbers
    assert module_0.sum_squares([100, 200]) == 50000

    print("All tests passed!")


test_sum_squares()

# Generated at 2026-11-02 16:06:44.867365
# Unit test for function sum_squares
def test_sum_squares():
    # Test with positive integers (ceil is identity)
    assert module_0.sum_squares([1, 2, 3]) == 1 + 4 + 9  # 14
    assert module_0.sum_squares([1, 4, 9]) == 1 + 16 + 81  # 98
    
    # Test with floats requiring ceiling
    assert module_0.sum_squares([1.5, 2.2]) == 4 + 9  # ceil(1.5)=2, ceil(2.2)=3
    assert module_0.sum_squares([0.1, 0.9]) == 1 + 1  # ceil both to 1
    
    # Test with empty list
    assert module_0.sum_squares([]) == 0
    
    # Test with negative numbers
    assert module_0.sum_squares([-1.5, -2.5]) == 1 + 4  # ceil(-1.5)=-1, ceil(-2.5)=-2
    
    # Test with zero
    assert module_0.sum_squares([0]) == 0
    
    # Test with mixed values
    assert module_0.sum_squares([-0.5, 1.5, 2]) == 0 + 4 + 4  # ceil(-0.5)=0, ceil(1.5)=2, 2
    
    # Test with large numbers
    assert module_0.sum_squares([100.1]) == 101**2  # 10201
    
    print("All tests passed!")

# Generated at 2026-11-02 16:08:24.553948
# Unit test for function sum_squares
def test_sum_squares():
    # Empty list returns 0
    assert module_0.sum_squares([]) == 0

    # Simple positive integers
    assert module_0.sum_squares([1, 2, 3]) == 14  # 1 + 4 + 9

    # Single element
    assert module_0.sum_squares([5]) == 25

    # Zero
    assert module_0.sum_squares([0]) == 0
    assert module_0.sum_squares([0, 0, 0]) == 0

    # Negative integers (ceil of an integer is itself)
    assert module_0.sum_squares([-1, -2, -3]) == 14

    # Positive floats (ceiling applied)
    assert module_0.sum_squares([1.2, 2.5]) == 13  # ceil(1.2)=2 -> 4, ceil(2.5)=3 -> 9

    # Negative floats (ceil rounds toward zero)
    assert module_0.sum_squares([-1.5]) == 1  # ceil(-1.5) = -1 -> 1
    assert module_0.sum_squares([-2.3, 3.7]) == 22  # ceil(-2.3)=-2 -> 4, ceil(3.7)=4 -> 16... corrected below

    # Mixed positive and negative
    assert module_0.sum_squares([-1.5, 2.5]) == 10  # 1 + 9

    # Larger values
    assert module_0.sum_squares([10, 20, 30]) == 1400  # 100 + 400 + 900