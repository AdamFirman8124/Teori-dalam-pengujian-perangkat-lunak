

# Generated at 2026-10-24 14:38:25.862555
# Unit test for function triangle_area
def test_triangle_area():
    assert module_0.triangle_area(10, 5) == 25.0
    assert module_0.triangle_area(4, 3) == 6.0
    assert module_0.triangle_area(7, 2) == 7.0

# Generated at 2026-10-24 14:38:27.285470
# Unit test for function triangle_area
def test_triangle_area():
    # integers
    assert module_0.triangle_area(4, 6) == 12.0
    # floats
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    # zero base or height -> zero area
    assert module_0.triangle_area(0, 10) == 0.0
    assert module_0.triangle_area(10, 0) == 0.0
    # result is float even for even integer products
    assert isinstance(module_0.triangle_area(3, 3), float)
    # order doesn't matter
    assert module_0.triangle_area(6, 4) == module_0.triangle_area(4, 6)
    # large values
    assert module_0.triangle_area(1e6, 2e6) == 1e12

# Generated at 2026-10-24 14:38:28.608834
# Unit test for function triangle_area
def test_triangle_area():
    # integers
    assert module_0.triangle_area(4, 6) == 12.0
    # floats
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    # zero base or height -> zero area
    assert module_0.triangle_area(0, 10) == 0.0
    assert module_0.triangle_area(10, 0) == 0.0
    # result is float even for even integer products
    assert isinstance(module_0.triangle_area(3, 3), float)
    # order doesn't matter
    assert module_0.triangle_area(6, 4) == module_0.triangle_area(4, 6)
    # large values
    assert module_0.triangle_area(1e6, 2e6) == 1e12

# Generated at 2026-10-24 14:38:30.049935
# Unit test for function triangle_area
def test_triangle_area():
    # integers
    assert module_0.triangle_area(4, 6) == 12.0
    # floats
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    # zero base or height -> zero area
    assert module_0.triangle_area(0, 10) == 0.0
    assert module_0.triangle_area(10, 0) == 0.0
    # result is float even for even integer products
    assert isinstance(module_0.triangle_area(3, 3), float)
    # order doesn't matter
    assert module_0.triangle_area(6, 4) == module_0.triangle_area(4, 6)
    # large values
    assert module_0.triangle_area(1e6, 2e6) == 1e12

# Generated at 2026-10-24 14:38:31.484874
# Unit test for function triangle_area
def test_triangle_area():
    # integers
    assert module_0.triangle_area(4, 6) == 12.0
    # floats
    assert module_0.triangle_area(2.5, 4.0) == 5.0
    # zero base or height -> zero area
    assert module_0.triangle_area(0, 10) == 0.0
    assert module_0.triangle_area(10, 0) == 0.0
    # result is float even for even integer products
    assert isinstance(module_0.triangle_area(3, 3), float)
    # order doesn't matter
    assert module_0.triangle_area(6, 4) == module_0.triangle_area(4, 6)
    # large values
    assert module_0.triangle_area(1e6, 2e6) == 1e12