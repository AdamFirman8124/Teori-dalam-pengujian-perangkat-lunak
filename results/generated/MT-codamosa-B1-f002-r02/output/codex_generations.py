

# Generated at 2026-10-23 19:42:51.405893
# Unit test for function truncate_number
def test_truncate_number():
    assert math.isclose(module_0.truncate_number(3.14), 0.14)
    assert math.isclose(module_0.truncate_number(7.0), 0.0)
    assert math.isclose(module_0.truncate_number(0.85), 0.85)

# Generated at 2026-10-23 19:43:00.560961
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.14) == pytest.approx(0.14)
    assert module_0.truncate_number(7.0) == pytest.approx(0.0)
    assert module_0.truncate_number(0.75) == pytest.approx(0.75)

# Generated at 2026-10-23 19:43:09.837644
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(10.25) == 0.25
    assert module_0.truncate_number(7.0) == 0.0

# Generated at 2026-10-23 19:43:20.999472
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.14) == pytest.approx(0.14)
    assert module_0.truncate_number(10.0) == pytest.approx(0.0)
    assert module_0.truncate_number(0.75) == pytest.approx(0.75)
    assert module_0.truncate_number(12.999) == pytest.approx(0.999)

# Generated at 2026-10-23 19:43:31.341843
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.14) == 0.14
    assert module_0.truncate_number(10.0) == 0.0
    assert module_0.truncate_number(0.75) == 0.75
    assert module_0.truncate_number(-3.14) == 0.86