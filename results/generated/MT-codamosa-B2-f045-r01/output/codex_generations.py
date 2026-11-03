

# Generated at 2026-11-02 17:38:09.379149
# Unit test for function triangle_area
def test_triangle_area():
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 10) == 25.0
    assert module_0.triangle_area(0, 7) == 0.0
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert module_0.triangle_area(1, 1) == 0.5
    assert module_0.triangle_area(10, 3) == 15.0
    with pytest.raises(TypeError):
        module_0.triangle_area("a", 2)

# Generated at 2026-11-02 17:38:57.983808
# Unit test for function triangle_area
def test_triangle_area():
    # Basic positive values
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 10) == 25.0
    assert module_0.triangle_area(1, 1) == 0.5

    # Float inputs
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    assert abs(module_0.triangle_area(1.2, 3.7) - 2.22) < 1e-9

    # Zero base or height yields zero area
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(7, 0) == 0.0

    # Large values
    assert module_0.triangle_area(1e6, 1e6) == 5e11

    # Result is always a float
    assert isinstance(module_0.triangle_area(2, 3), float)

    # Symmetry: swapping arguments gives same area
    assert module_0.triangle_area(4, 6) == module_0.triangle_area(6, 4)

    print("All tests passed!")


if __name__ == "__main__":
    test_triangle_area()

# Generated at 2026-11-02 17:39:58.484939
# Unit test for function triangle_area
def test_triangle_area():
    # Basic integer inputs
    assert module_0.triangle_area(3, 4) == 6.0
    assert module_0.triangle_area(5, 8) == 20.0

    # Fractional results
    assert module_0.triangle_area(1, 3) == 1.5
    assert module_0.triangle_area(7, 3) == 10.5

    # Floating point inputs
    assert math.isclose(module_0.triangle_area(2.5, 4.0), 5.0)
    assert math.isclose(module_0.triangle_area(1.2, 3.7), 2.22)

    # Zero dimensions
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0

    # Result should always be a float (division by 2.0)
    assert isinstance(module_0.triangle_area(3, 4), float)
    assert isinstance(module_0.triangle_area(2, 2), float)

# Generated at 2026-11-02 17:41:26.465142
# Unit test for function triangle_area
def test_triangle_area():
    # Basic case: base 5, height 4 -> area 10.0
    assert module_0.triangle_area(5, 4) == 10.0

    # Base 3, height 2 -> area 3.0
    assert module_0.triangle_area(3, 2) == 3.0

    # Base 10, height 6 -> area 30.0
    assert module_0.triangle_area(10, 6) == 30.0

    # Floating point values: 2.5 * 4 / 2 = 5.0
    assert module_0.triangle_area(2.5, 4) == 5.0

    # Zero base -> area 0.0
    assert module_0.triangle_area(0, 5) == 0.0

    # Zero height -> area 0.0
    assert module_0.triangle_area(7, 0) == 0.0

    # Result is always a float due to division by 2.0
    result = module_0.triangle_area(4, 2)
    assert isinstance(result, float)

    # Fractional result: 1 * 1 / 2 = 0.5
    assert module_0.triangle_area(1, 1) == 0.5

    # Large numbers
    assert module_0.triangle_area(1000000, 2000000) == 1000000000000.0

    print("All triangle_area tests passed!")

# Generated at 2026-11-02 17:43:25.920220
# Unit test for function triangle_area
def test_triangle_area():
# nonce:6b4f1daa
    # Basic positive cases
    assert module_0.triangle_area(5, 3) == 7.5
    assert module_0.triangle_area(10, 4) == 20.0
    assert module_0.triangle_area(1, 1) == 0.5

    # Float inputs
    assert module_0.triangle_area(2.5, 4) == 5.0
    assert module_0.triangle_area(3.2, 1.5) == 2.4

    # Zero edge case
    assert module_0.triangle_area(0, 5) == 0.0
    assert module_0.triangle_area(5, 0) == 0.0

    # Result should always be a float
    assert isinstance(module_0.triangle_area(3, 2), float)

    # Symmetry: swapping base and height yields same area
    assert module_0.triangle_area(6, 4) == module_0.triangle_area(4, 6)