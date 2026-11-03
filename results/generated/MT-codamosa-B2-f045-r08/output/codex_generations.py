

# Generated at 2026-11-02 00:08:11.619947
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert math.isclose(module_0.triangle_area(5, 3), 7.5)
    assert math.isclose(module_0.triangle_area(4, 2), 4.0)
    assert math.isclose(module_0.triangle_area(10, 8), 40.0)

    # Floating point inputs
    assert math.isclose(module_0.triangle_area(2.5, 4.0), 5.0)
    assert math.isclose(module_0.triangle_area(1.5, 2.5), 1.875)

    # Zero base or height yields zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Fractional results
    assert math.isclose(module_0.triangle_area(3, 7), 10.5)
    assert math.isclose(module_0.triangle_area(1, 1), 0.5)

    # Large values
    assert math.isclose(module_0.triangle_area(1000, 2000), 1000000.0)

# Generated at 2026-11-02 00:09:27.922778
# Unit test for function triangle_area
def test_triangle_area():
    # Basic positive values
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(10, 5) == 25.0
    
    # Floating point values
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert abs(module_0.triangle_area(1.5, 3.7) - 2.775) < 1e-9
    
    # Zero base or height yields zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0
    
    # Result is always a float
    assert isinstance(module_0.triangle_area(2, 3), float)
    
    # Large values
    assert module_0.triangle_area(1e6, 1e6) == 5e11
    
    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 00:10:15.542025
# Unit test for function triangle_area
def test_triangle_area():
    # Basic positive case
    assert module_0.triangle_area(1, 1) == 0.5
    assert module_0.triangle_area(2, 3) == 3.0
    assert module_0.triangle_area(4, 5) == 10.0

    # Floating point inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(0.1, 0.2) == 0.1 * 0.2 / 2.0

    # Zero input
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Negative inputs (mathematically signed area)
    assert module_0.triangle_area(-2, 3) == -3.0
    assert module_0.triangle_area(2, -3) == -3.0

    # Result is always a float
    assert isinstance(module_0.triangle_area(3, 4), float)

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 00:11:18.277190
# Unit test for function triangle_area
def test_triangle_area():
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 10) == 25.0
    assert module_0.triangle_area(0, 10) == 0.0
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(-3, 4) == -6.0
    assert module_0.triangle_area(1, 1) == 0.5
    assert isinstance(module_0.triangle_area(3, 4), float)
    print("All tests passed!")

test_triangle_area()

# Generated at 2026-11-02 00:12:08.164167
# Unit test for function triangle_area
def test_triangle_area():
    # Basic case: base and height
    assert module_0.triangle_area(5, 3) == 7.5
    assert module_0.triangle_area(4, 2) == 4.0
    assert module_0.triangle_area(10, 10) == 50.0

    # Zero base yields zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0

    # Fractional inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(1.5, 1.5) == 1.125

    # Result is always a float
    assert isinstance(module_0.triangle_area(2, 3), float)

    print("All tests passed!")