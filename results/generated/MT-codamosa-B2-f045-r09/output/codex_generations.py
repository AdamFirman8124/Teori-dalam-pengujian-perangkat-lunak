

# Generated at 2026-11-02 06:59:43.192179
# Unit test for function triangle_area
def test_triangle_area():
    # Basic positive cases
    assert module_0.triangle_area(5, 3) == 7.5
    assert module_0.triangle_area(10, 4) == 20.0
    assert module_0.triangle_area(1, 1) == 0.5
    assert module_0.triangle_area(7, 2) == 7.0

    # Zero dimensions yield zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(3, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Float inputs
    assert module_0.triangle_area(2.5, 4) == 5.0
    assert module_0.triangle_area(1.5, 1.5) == 1.125

    # Result is always a float
    assert isinstance(module_0.triangle_area(4, 3), float)
    assert isinstance(module_0.triangle_area(2, 2), float)

    # Negative base computes algebraically
    assert module_0.triangle_area(-4, 3) == -6.0

    # Approximate check for values with floating-point representation
    assert abs(module_0.triangle_area(0.1, 0.3) - 0.015) < 1e-9

# Generated at 2026-11-02 07:01:25.883733
# Unit test for function triangle_area
def test_triangle_area():
    import math

    # Basic integer inputs
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(10, 5) == 25.0
    assert module_0.triangle_area(1, 1) == 0.5

    # Float inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(7.2, 3.5) == 12.6
    assert math.isclose(module_0.triangle_area(1.5, 2.5), 1.875)

    # Zero values
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Large values
    assert module_0.triangle_area(1e6, 1e6) == 5e11

    # Small values
    assert math.isclose(module_0.triangle_area(1e-6, 1e-6), 5e-13)

    # Result is always a float
    assert isinstance(module_0.triangle_area(3, 4), float)

    # Negative inputs (mathematically signed area)
    assert module_0.triangle_area(-3, 4) == -6.0
    assert module_0.triangle_area(-3, -4) == 6.0

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 07:02:48.752615
# Unit test for function triangle_area
def test_triangle_area():
    # Basic positive case
    assert module_0.triangle_area(3, 4) == 6.0
    # Float inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    # Zero height gives zero area
    assert module_0.triangle_area(5, 0) == 0.0
    # Zero base gives zero area
    assert module_0.triangle_area(0, 5) == 0.0
    # Larger values
    assert module_0.triangle_area(10, 20) == 100.0
    # Fractional result
    assert module_0.triangle_area(1, 1) == 0.5
    assert module_0.triangle_area(3, 5) == 7.5
    # Result is always a float
    assert isinstance(module_0.triangle_area(3, 4), float)

# Generated at 2026-11-02 07:03:50.181328
# Unit test for function triangle_area
def test_triangle_area():
    # Basic cases
    assert module_0.triangle_area(1, 1) == 0.5
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(10, 5) == 25.0

    # Floating point base/height
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(0.5, 0.5) == 0.125

    # Use approximate comparison for non-exact floats
    assert module_0.triangle_area(1.1, 2.2) == pytest.approx(1.21)

    # Zero values
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0

    # Large values
    assert module_0.triangle_area(1e6, 1e6) == 5e11

    # Result is always a float
    assert isinstance(module_0.triangle_area(2, 3), float)

# Generated at 2026-11-02 07:05:19.488423
# Unit test for function triangle_area
def test_triangle_area():
    # Basic case
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 10) == 25.0

    # Floating point inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert abs(module_0.triangle_area(1.5, 3.7) - 2.775) < 1e-9

    # Zero height yields zero area
    assert module_0.triangle_area(10, 0) == 0.0
    assert module_0.triangle_area(0, 10) == 0.0

    # Result is always a float
    assert isinstance(module_0.triangle_area(4, 5), float)

    # Symmetry in arguments
    assert module_0.triangle_area(6, 8) == module_0.triangle_area(8, 6)

    # Larger values
    assert module_0.triangle_area(1000, 2000) == 1000000.0

    print("All tests passed!")


test_triangle_area()