

# Generated at 2026-10-24 13:28:57.119076
# Unit test for function triangle_area
def test_triangle_area():
    # valid triangles
    assert module_0.triangle_area(3, 4, 5) == pytest.approx(6.0)
    assert module_0.triangle_area(6, 8, 10) == pytest.approx(24.0)
    assert module_0.triangle_area(5, 5, 6) == pytest.approx(12.0)
    assert module_0.triangle_area(3, 3, 3) == pytest.approx(3.9)      # 3.897...
    assert module_0.triangle_area(1, 1, 1) == pytest.approx(0.43)     # 0.4330...
    assert module_0.triangle_area(2, 2, 3) == pytest.approx(1.98)     # 1.9843...

    # degenerate (sum == third side) -> -1
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(3, 3, 6) == -1
    assert module_0.triangle_area(0, 0, 0) == -1

    # impossible (sum < third side) -> -1
    assert module_0.triangle_area(1, 1, 5) == -1
    assert module_0.triangle_area(10, 1, 1) == -1

    # negative sides -> -1 (always fails one inequality)
    assert module_0.triangle_area(-1, 5, 5) == -1
    assert module_0.triangle_area(10, 10, -1) == -1

    # result is rounded to 2 decimals
    assert module_0.triangle_area(2, 2, 3) == round(module_0.triangle_area(2, 2, 3), 2)

# Generated at 2026-10-24 13:28:58.438647
# Unit test for function triangle_area
def test_triangle_area():
    # valid triangles
    assert module_0.triangle_area(3, 4, 5) == pytest.approx(6.0)
    assert module_0.triangle_area(6, 8, 10) == pytest.approx(24.0)
    assert module_0.triangle_area(5, 5, 6) == pytest.approx(12.0)
    assert module_0.triangle_area(3, 3, 3) == pytest.approx(3.9)      # 3.897...
    assert module_0.triangle_area(1, 1, 1) == pytest.approx(0.43)     # 0.4330...
    assert module_0.triangle_area(2, 2, 3) == pytest.approx(1.98)     # 1.9843...

    # degenerate (sum == third side) -> -1
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(3, 3, 6) == -1
    assert module_0.triangle_area(0, 0, 0) == -1

    # impossible (sum < third side) -> -1
    assert module_0.triangle_area(1, 1, 5) == -1
    assert module_0.triangle_area(10, 1, 1) == -1

    # negative sides -> -1 (always fails one inequality)
    assert module_0.triangle_area(-1, 5, 5) == -1
    assert module_0.triangle_area(10, 10, -1) == -1

    # result is rounded to 2 decimals
    assert module_0.triangle_area(2, 2, 3) == round(module_0.triangle_area(2, 2, 3), 2)

# Generated at 2026-10-24 13:28:59.779638
# Unit test for function triangle_area
def test_triangle_area():
    # valid triangles
    assert module_0.triangle_area(3, 4, 5) == pytest.approx(6.0)
    assert module_0.triangle_area(6, 8, 10) == pytest.approx(24.0)
    assert module_0.triangle_area(5, 5, 6) == pytest.approx(12.0)
    assert module_0.triangle_area(3, 3, 3) == pytest.approx(3.9)      # 3.897...
    assert module_0.triangle_area(1, 1, 1) == pytest.approx(0.43)     # 0.4330...
    assert module_0.triangle_area(2, 2, 3) == pytest.approx(1.98)     # 1.9843...

    # degenerate (sum == third side) -> -1
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(3, 3, 6) == -1
    assert module_0.triangle_area(0, 0, 0) == -1

    # impossible (sum < third side) -> -1
    assert module_0.triangle_area(1, 1, 5) == -1
    assert module_0.triangle_area(10, 1, 1) == -1

    # negative sides -> -1 (always fails one inequality)
    assert module_0.triangle_area(-1, 5, 5) == -1
    assert module_0.triangle_area(10, 10, -1) == -1

    # result is rounded to 2 decimals
    assert module_0.triangle_area(2, 2, 3) == round(module_0.triangle_area(2, 2, 3), 2)

# Generated at 2026-10-24 13:29:01.118207
# Unit test for function triangle_area
def test_triangle_area():
    # valid triangles
    assert module_0.triangle_area(3, 4, 5) == pytest.approx(6.0)
    assert module_0.triangle_area(6, 8, 10) == pytest.approx(24.0)
    assert module_0.triangle_area(5, 5, 6) == pytest.approx(12.0)
    assert module_0.triangle_area(3, 3, 3) == pytest.approx(3.9)      # 3.897...
    assert module_0.triangle_area(1, 1, 1) == pytest.approx(0.43)     # 0.4330...
    assert module_0.triangle_area(2, 2, 3) == pytest.approx(1.98)     # 1.9843...

    # degenerate (sum == third side) -> -1
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(3, 3, 6) == -1
    assert module_0.triangle_area(0, 0, 0) == -1

    # impossible (sum < third side) -> -1
    assert module_0.triangle_area(1, 1, 5) == -1
    assert module_0.triangle_area(10, 1, 1) == -1

    # negative sides -> -1 (always fails one inequality)
    assert module_0.triangle_area(-1, 5, 5) == -1
    assert module_0.triangle_area(10, 10, -1) == -1

    # result is rounded to 2 decimals
    assert module_0.triangle_area(2, 2, 3) == round(module_0.triangle_area(2, 2, 3), 2)

# Generated at 2026-10-24 13:29:02.455981
# Unit test for function triangle_area
def test_triangle_area():
    # valid triangles
    assert module_0.triangle_area(3, 4, 5) == pytest.approx(6.0)
    assert module_0.triangle_area(6, 8, 10) == pytest.approx(24.0)
    assert module_0.triangle_area(5, 5, 6) == pytest.approx(12.0)
    assert module_0.triangle_area(3, 3, 3) == pytest.approx(3.9)      # 3.897...
    assert module_0.triangle_area(1, 1, 1) == pytest.approx(0.43)     # 0.4330...
    assert module_0.triangle_area(2, 2, 3) == pytest.approx(1.98)     # 1.9843...

    # degenerate (sum == third side) -> -1
    assert module_0.triangle_area(1, 2, 3) == -1
    assert module_0.triangle_area(3, 3, 6) == -1
    assert module_0.triangle_area(0, 0, 0) == -1

    # impossible (sum < third side) -> -1
    assert module_0.triangle_area(1, 1, 5) == -1
    assert module_0.triangle_area(10, 1, 1) == -1

    # negative sides -> -1 (always fails one inequality)
    assert module_0.triangle_area(-1, 5, 5) == -1
    assert module_0.triangle_area(10, 10, -1) == -1

    # result is rounded to 2 decimals
    assert module_0.triangle_area(2, 2, 3) == round(module_0.triangle_area(2, 2, 3), 2)