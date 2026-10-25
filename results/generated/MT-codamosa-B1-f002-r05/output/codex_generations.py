

# Generated at 2026-10-24 11:40:58.535307
# Unit test for function truncate_number
def test_truncate_number():
    # Positive floats: fractional part is returned
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(1.25) == 0.25
    assert module_0.truncate_number(0.75) == 0.75

    # Whole numbers: fractional part is zero
    assert module_0.truncate_number(4.0) == 0.0
    assert module_0.truncate_number(100) == 0.0

    # Less than one
    assert module_0.truncate_number(0.123) == 0.123

    # Negative numbers: Python's % keeps the sign of the divisor,
    # so results are in [0, 1) even for negatives
    assert module_0.truncate_number(-1.5) == 0.5
    assert module_0.truncate_number(-3.25) == 0.75

    # Large value
    assert module_0.truncate_number(123456.789) == 0.789

# Generated at 2026-10-24 11:41:07.366817
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(5.75) == pytest.approx(0.75)
    assert module_0.truncate_number(10.0) == pytest.approx(0.0)
    assert module_0.truncate_number(0.42) == pytest.approx(0.42)
    assert module_0.truncate_number(-3.7) == pytest.approx(0.3)

# Generated at 2026-10-24 11:41:09.882805
# Unit test for function truncate_number

# Generated at 2026-10-24 11:41:12.297496
# Unit test for function truncate_number

# Generated at 2026-10-24 11:41:14.715554
# Unit test for function truncate_number

# Generated at 2026-10-24 11:41:17.300617
# Unit test for function truncate_number

# Generated at 2026-10-24 11:41:19.721393
# Unit test for function truncate_number

# Generated at 2026-10-24 11:41:22.133880
# Unit test for function truncate_number

# Generated at 2026-10-24 11:41:24.556122
# Unit test for function truncate_number

# Generated at 2026-10-24 11:41:26.965424
# Unit test for function truncate_number

# Generated at 2026-10-24 11:41:29.380140
# Unit test for function truncate_number