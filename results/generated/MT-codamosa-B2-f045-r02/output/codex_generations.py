

# Generated at 2026-11-02 21:28:32.417576
# Unit test for function triangle_area
def test_triangle_area():
    # Basic case: base and height as integers
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(10, 5) == 25.0

    # Base and height as floats
    assert math.isclose(module_0.triangle_area(2.5, 4.0), 5.0)
    assert math.isclose(module_0.triangle_area(1.2, 3.4), 2.04)

    # Zero values
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Fractional result (checks float division, not integer division)
    assert math.isclose(module_0.triangle_area(1, 1), 0.5)
    assert math.isclose(module_0.triangle_area(3, 1), 1.5)

    # Large values
    assert math.isclose(module_0.triangle_area(1e6, 1e6), 5e11)

    # Result type should be float
    assert isinstance(module_0.triangle_area(3, 4), float)

    print("All tests passed!")

# Generated at 2026-11-02 21:29:26.643624
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 2) == 5.0
    assert module_0.triangle_area(10, 10) == 50.0

    # Zero base gives zero area
    assert module_0.triangle_area(0, 5) == 0.0

    # Zero height gives zero area
    assert module_0.triangle_area(5, 0) == 0.0

    # Fractional inputs
    assert module_0.triangle_area(2.5, 4) == 5.0
    assert module_0.triangle_area(7.5, 2) == 7.5

    # Small values
    assert module_0.triangle_area(1, 1) == 0.5
    assert module_0.triangle_area(3, 3) == 4.5

    # Result is always a float
    assert isinstance(module_0.triangle_area(3, 4), float)

    # Large values
    assert module_0.triangle_area(1000, 2000) == 1000000.0

    print("All triangle_area tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 21:31:36.510661
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert math.isclose(module_0.triangle_area(5, 3), 7.5), "Expected 7.5 for base=5, height=3"
    assert math.isclose(module_0.triangle_area(10, 8), 40.0), "Expected 40.0 for base=10, height=8"

    # Floating point inputs
    assert math.isclose(module_0.triangle_area(2.5, 4.0), 5.0), "Expected 5.0 for base=2.5, height=4.0"
    assert math.isclose(module_0.triangle_area(1.5, 2.5), 1.875), "Expected 1.875 for base=1.5, height=2.5"

    # Zero base or height
    assert math.isclose(module_0.triangle_area(0, 5), 0.0), "Expected 0.0 for base=0"
    assert math.isclose(module_0.triangle_area(5, 0), 0.0), "Expected 0.0 for height=0"

    # Result is always a float
    assert isinstance(module_0.triangle_area(4, 3), float), "Result should be a float"

    # Large values
    assert math.isclose(module_0.triangle_area(1e6, 1e6), 5e11), "Expected 5e11 for large inputs"

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 21:33:45.389747
# Unit test for function triangle_area
def test_triangle_area():
    # Basic positive values
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(10, 5) == 25.0
    assert module_0.triangle_area(1, 1) == 0.5

    # Float inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(0.5, 0.5) == 0.125

    # Zero base or height gives zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(7, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Result is always a float
    assert isinstance(module_0.triangle_area(3, 4), float)

    # Large values
    assert module_0.triangle_area(1e6, 1e6) == 5e11

    # Consistency check
    assert module_0.triangle_area(6, 8) == module_0.triangle_area(8, 6)

# Generated at 2026-11-02 21:36:32.392120
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 2) == 5.0
    assert module_0.triangle_area(10, 8) == 40.0

    # Result should always be a float (division by 2.0)
    assert isinstance(module_0.triangle_area(3, 4), float)

    # Floating point inputs
    assert module_0.triangle_area(2.5, 4.0) == pytest.approx(5.0)
    assert module_0.triangle_area(1.5, 3.5) == pytest.approx(2.625)

    # Zero dimensions
    assert module_0.triangle_area(0, 10) == 0.0
    assert module_0.triangle_area(10, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Very small values (precision check)
    assert module_0.triangle_area(1e-10, 1e-10) == pytest.approx(5e-21)

    # Very large values
    assert module_0.triangle_area(1e6, 2e6) == pytest.approx(1e12)

    # Negative inputs (function computes signed area)
    assert module_0.triangle_area(-4, 5) == pytest.approx(-10.0)
    assert module_0.triangle_area(4, -5) == pytest.approx(-10.0)
    assert module_0.triangle_area(-4, -5) == pytest.approx(10.0)

    # Non-integer half results
    assert module_0.triangle_area(7, 3) == pytest.approx(10.5)
    assert module_0.triangle_area(1, 1) == pytest.approx(0.5)