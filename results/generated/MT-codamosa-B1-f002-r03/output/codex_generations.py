

# Generated at 2026-10-25 01:48:24.492177
# Unit test for function truncate_number
def test_truncate_number():
    # positive values
    assert module_0.truncate_number(3.75) == pytest.approx(0.75)
    assert module_0.truncate_number(0.5) == pytest.approx(0.5)

    # whole numbers
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # negative values: % returns a POSITIVE remainder in Python
    assert module_0.truncate_number(-1.5) == pytest.approx(0.5)   # not -0.5
    assert module_0.truncate_number(-0.25) == pytest.approx(0.75)  # not -0.25

    # result is always in [0, 1)
    for x in (1e-9, 1.999, 42.0, 1e12 + 0.5):
        assert 0.0 <= module_0.truncate_number(x) < 1.0

    # infinity is undefined for % 1.0
    assert math.isnan(module_0.truncate_number(math.inf))

# Generated at 2026-10-25 01:48:25.825870
# Unit test for function truncate_number
def test_truncate_number():
    # positive values
    assert module_0.truncate_number(3.75) == pytest.approx(0.75)
    assert module_0.truncate_number(0.5) == pytest.approx(0.5)

    # whole numbers
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # negative values: % returns a POSITIVE remainder in Python
    assert module_0.truncate_number(-1.5) == pytest.approx(0.5)   # not -0.5
    assert module_0.truncate_number(-0.25) == pytest.approx(0.75)  # not -0.25

    # result is always in [0, 1)
    for x in (1e-9, 1.999, 42.0, 1e12 + 0.5):
        assert 0.0 <= module_0.truncate_number(x) < 1.0

    # infinity is undefined for % 1.0
    assert math.isnan(module_0.truncate_number(math.inf))

# Generated at 2026-10-25 01:48:27.142683
# Unit test for function truncate_number
def test_truncate_number():
    # positive values
    assert module_0.truncate_number(3.75) == pytest.approx(0.75)
    assert module_0.truncate_number(0.5) == pytest.approx(0.5)

    # whole numbers
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # negative values: % returns a POSITIVE remainder in Python
    assert module_0.truncate_number(-1.5) == pytest.approx(0.5)   # not -0.5
    assert module_0.truncate_number(-0.25) == pytest.approx(0.75)  # not -0.25

    # result is always in [0, 1)
    for x in (1e-9, 1.999, 42.0, 1e12 + 0.5):
        assert 0.0 <= module_0.truncate_number(x) < 1.0

    # infinity is undefined for % 1.0
    assert math.isnan(module_0.truncate_number(math.inf))

# Generated at 2026-10-25 01:48:28.470668
# Unit test for function truncate_number
def test_truncate_number():
    # positive values
    assert module_0.truncate_number(3.75) == pytest.approx(0.75)
    assert module_0.truncate_number(0.5) == pytest.approx(0.5)

    # whole numbers
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # negative values: % returns a POSITIVE remainder in Python
    assert module_0.truncate_number(-1.5) == pytest.approx(0.5)   # not -0.5
    assert module_0.truncate_number(-0.25) == pytest.approx(0.75)  # not -0.25

    # result is always in [0, 1)
    for x in (1e-9, 1.999, 42.0, 1e12 + 0.5):
        assert 0.0 <= module_0.truncate_number(x) < 1.0

    # infinity is undefined for % 1.0
    assert math.isnan(module_0.truncate_number(math.inf))

# Generated at 2026-10-25 01:48:29.798287
# Unit test for function truncate_number
def test_truncate_number():
    # positive values
    assert module_0.truncate_number(3.75) == pytest.approx(0.75)
    assert module_0.truncate_number(0.5) == pytest.approx(0.5)

    # whole numbers
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # negative values: % returns a POSITIVE remainder in Python
    assert module_0.truncate_number(-1.5) == pytest.approx(0.5)   # not -0.5
    assert module_0.truncate_number(-0.25) == pytest.approx(0.75)  # not -0.25

    # result is always in [0, 1)
    for x in (1e-9, 1.999, 42.0, 1e12 + 0.5):
        assert 0.0 <= module_0.truncate_number(x) < 1.0

    # infinity is undefined for % 1.0
    assert math.isnan(module_0.truncate_number(math.inf))