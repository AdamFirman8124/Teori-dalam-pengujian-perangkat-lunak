

# Generated at 2026-11-02 13:12:56.558243
# Unit test for function triangle_area
def test_triangle_area():
    # Test with basic positive integers
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(10, 5) == 25.0
    
    # Test with floats
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(1.5, 2.5) == 1.875
    
    # Test with zero base
    assert module_0.triangle_area(0, 10) == 0.0
    
    # Test with zero height
    assert module_0.triangle_area(10, 0) == 0.0
    
    # Test with both zero
    assert module_0.triangle_area(0, 0) == 0.0
    
    # Test with large numbers
    assert module_0.triangle_area(1000000, 2000000) == 1000000000000.0
    
    # Test result is always a float
    assert isinstance(module_0.triangle_area(3, 4), float)
    
    # Test with fractional result
    assert module_0.triangle_area(1, 1) == 0.5
    assert module_0.triangle_area(3, 1) == 1.5
    
    # Test floating point precision
    assert abs(module_0.triangle_area(0.1, 0.2) - 0.01) < 1e-9
    
    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 13:14:29.102866
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(10, 5) == 25.0

    # Float inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(1.5, 2.5) == 1.875

    # Base or height of zero yields zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0

    # Result is always a float due to division by 2.0
    assert isinstance(module_0.triangle_area(3, 4), float)

    # Large values
    assert module_0.triangle_area(1e6, 1e6) == 5e11

    # Negative inputs follow the formula directly
    assert module_0.triangle_area(-3, 4) == -6.0

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 13:16:29.814675
# Unit test for function triangle_area
def test_triangle_area():
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 10) == 25.0
    assert module_0.triangle_area(2.5, 4) == 5.0
    assert module_0.triangle_area(0, 10) == 0.0
    assert module_0.triangle_area(1, 1) == 0.5
    assert module_0.triangle_area(7, 3) == 10.5
    assert module_0.triangle_area(10, 0.5) == 2.5

# Generated at 2026-11-02 13:20:09.578648
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 3) == 7.5
    assert module_0.triangle_area(10, 2) == 10.0

    # Float inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(0.5, 0.5) == 0.125

    # Zero base or height yields zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(7, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Fractional results
    assert module_0.triangle_area(1, 1) == 0.5
    assert module_0.triangle_area(3, 1) == 1.5

    # Large values
    assert module_0.triangle_area(1000, 2000) == 1000000.0

    # Result is always a float
    assert isinstance(module_0.triangle_area(4, 2), float)

    print("All tests passed!")


test_triangle_area()