

# Generated at 2026-11-02 22:48:37.002095
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 10) == 25.0
    assert module_0.triangle_area(6, 2) == 6.0

    # Floating point inputs
    assert math.isclose(module_0.triangle_area(2.5, 4), 5.0)
    assert math.isclose(module_0.triangle_area(1.5, 3.5), 2.625)
    assert math.isclose(module_0.triangle_area(7.2, 3.1), 7.2 * 3.1 / 2.0)

    # Results requiring division
    assert math.isclose(module_0.triangle_area(1, 3), 1.5)
    assert math.isclose(module_0.triangle_area(5, 1), 2.5)

    # Zero edge cases
    assert module_0.triangle_area(10, 0) == 0.0
    assert module_0.triangle_area(0, 7) == 0.0

    # Return type should be float
    assert isinstance(module_0.triangle_area(3, 4), float)

    print("test_triangle_area passed")


test_triangle_area()

# Generated at 2026-11-02 22:50:08.343246
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(10, 5) == 25.0

    # Float inputs
    assert module_0.triangle_area(5.0, 2.5) == 6.25
    assert abs(module_0.triangle_area(1.5, 3.7) - 2.775) < 1e-9

    # Zero values
    assert module_0.triangle_area(0, 10) == 0.0
    assert module_0.triangle_area(10, 0) == 0.0

    # Result is always a float
    result = module_0.triangle_area(4, 6)
    assert isinstance(result, float)
    assert result == 12.0

    # Larger values
    assert module_0.triangle_area(100, 200) == 10000.0

    print("All tests passed!")


test_triangle_area()

# Generated at 2026-11-02 22:51:41.219529
# Unit test for function triangle_area
def test_triangle_area():
    # Basic case: base 3, height 4 => area 6.0
    assert module_0.triangle_area(3, 4) == 6.0

    # Base 5, height 2 => area 5.0
    assert module_0.triangle_area(5, 2) == 5.0

    # Zero height => area 0.0
    assert module_0.triangle_area(10, 0) == 0.0

    # Zero base => area 0.0
    assert module_0.triangle_area(0, 10) == 0.0

    # Fractional values: base 2.5, height 4.0 => area 5.0
    assert math.isclose(module_0.triangle_area(2.5, 4.0), 5.0)

    # Fractional result: base 1, height 1 => area 0.5
    assert module_0.triangle_area(1, 1) == 0.5

    # Large values: base 1e6, height 1e6 => area 5e11
    assert math.isclose(module_0.triangle_area(1e6, 1e6), 5e11)

    # Consistency: result is always half of a*h
    a, h = 7, 13
    assert math.isclose(module_0.triangle_area(a, h), a * h / 2.0)

# Generated at 2026-11-02 22:55:45.239852
# Unit test for function triangle_area
def test_triangle_area():
    # Basic positive cases
    assert module_0.triangle_area(5, 3) == 7.5
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(6, 8) == 24.0
    assert module_0.triangle_area(1, 1) == 0.5

    # Floating point inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert math.isclose(module_0.triangle_area(0.1, 0.3), 0.015)

    # Zero base or height yields zero area
    assert module_0.triangle_area(0, 10) == 0.0
    assert module_0.triangle_area(10, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Negative inputs follow the arithmetic (no validation in function)
    assert module_0.triangle_area(-5, 3) == -7.5
    assert module_0.triangle_area(-5, -3) == 7.5

    # Large values
    assert module_0.triangle_area(1e6, 1e6) == 5e11

    # Result is always a float (true division)
    assert isinstance(module_0.triangle_area(4, 2), float)