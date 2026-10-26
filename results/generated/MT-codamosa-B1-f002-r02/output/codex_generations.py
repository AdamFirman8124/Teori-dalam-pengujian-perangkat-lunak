

# Generated at 2026-10-25 08:31:42.748042
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

# Generated at 2026-10-25 08:31:44.086313
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

# Generated at 2026-10-25 08:31:46.507186
# Unit test for function truncate_number

# Generated at 2026-10-25 08:31:48.922833
# Unit test for function truncate_number

# Generated at 2026-10-25 08:31:51.340568
# Unit test for function truncate_number

# Generated at 2026-10-25 08:31:54.115455
# Unit test for function truncate_number

# Generated at 2026-10-25 08:31:56.397497
# Unit test for function truncate_number

# Generated at 2026-10-25 08:31:58.815037
# Unit test for function truncate_number

# Generated at 2026-10-25 08:32:01.233497
# Unit test for function truncate_number

# Generated at 2026-10-25 08:32:03.785447
# Unit test for function truncate_number

# Generated at 2026-10-25 08:32:06.200778
# Unit test for function truncate_number