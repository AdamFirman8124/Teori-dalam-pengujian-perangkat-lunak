

# Generated at 2026-11-03 05:02:18.456788
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert module_0.triangle_area(10, 5) == 25.0
    assert module_0.triangle_area(4, 3) == 6.0

    # Float inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(7.2, 3.5) == 12.6
    assert abs(module_0.triangle_area(1.0 / 3, 3) - 0.5) < 1e-9

    # Base or height of zero yields zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0
    assert module_0.triangle_area(0, 0) == 0.0

    # Result should always be a float
    assert isinstance(module_0.triangle_area(2, 3), float)

    # Large values
    assert module_0.triangle_area(1e6, 1e6) == 5e11

    # Fractional result check
    assert module_0.triangle_area(3, 3) == 4.5
    assert module_0.triangle_area(1, 1) == 0.5

    # Verify against known geometric values
    assert module_0.triangle_area(6, 8) == 24.0
    assert module_0.triangle_area(12, 10) == 60.0

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-03 05:03:55.248858
# Unit test for function triangle_area
def test_triangle_area():
    # Basic cases
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 10) == 25.0
    assert module_0.triangle_area(1, 1) == 0.5

    # Floating point inputs
    assert math.isclose(module_0.triangle_area(2.5, 4.0), 5.0)
    assert math.isclose(module_0.triangle_area(7.2, 3.5), 12.6)

    # Zero height yields zero area
    assert module_0.triangle_area(10, 0) == 0.0

    # Result is always a float
    assert isinstance(module_0.triangle_area(3, 4), float)

    # Property check: area scales linearly with base and height
    assert math.isclose(module_0.triangle_area(4, 5), 2 * module_0.triangle_area(2, 5))
    assert math.isclose(module_0.triangle_area(4, 5), 5 * module_0.triangle_area(4, 1))

    # Large values
    assert math.isclose(module_0.triangle_area(1e6, 1e6), 5e11)

# Generated at 2026-11-03 05:06:37.885958
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert module_0.triangle_area(3, 4) == 6.0
    # Base and height of 1
    assert module_0.triangle_area(1, 1) == 0.5
    # Floating point inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    # Zero height yields zero area
    assert module_0.triangle_area(5, 0) == 0.0
    # Zero base yields zero area
    assert module_0.triangle_area(0, 5) == 0.0
    # Larger values
    assert module_0.triangle_area(10, 20) == 100.0
    # Result is always a float
    assert isinstance(module_0.triangle_area(2, 3), float)
    # Approximate check for non-trivial division
    assert abs(module_0.triangle_area(1, 3) - 1.5) < 1e-9
    assert abs(module_0.triangle_area(7, 3) - 10.5) < 1e-9

# Generated at 2026-11-03 05:10:12.210827
# Unit test for function triangle_area
def test_triangle_area():
    # Basic case: base and height are positive integers
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 2) == 5.0

    # Floats
    assert module_0.triangle_area(2.5, 4.0) == 5.0

    # Zero base/height yields zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0

    # Large values
    assert module_0.triangle_area(1e6, 1e6) == 1e6 * 1e6 / 2.0

    # Result is always a float (division by 2.0)
    assert isinstance(module_0.triangle_area(3, 4), float)