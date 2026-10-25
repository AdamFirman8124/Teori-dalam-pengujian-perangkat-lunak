

# Generated at 2026-10-25 02:54:03.838803
# Unit test for function is_simple_power
def test_is_simple_power():
    assert module_0.is_simple_power(1, 5) is True      # Any positive n^0 equals 1
    assert module_0.is_simple_power(1, 1) is True
    assert module_0.is_simple_power(8, 2) is True       # 2^3
    assert module_0.is_simple_power(81, 3) is True      # 3^4
    assert module_0.is_simple_power(12, 2) is False
    assert module_0.is_simple_power(8, 3) is False
    assert module_0.is_simple_power(2, 1) is False

# Generated at 2026-10-25 02:54:09.881854
# Unit test for function is_simple_power
def test_is_simple_power():
    assert module_0.is_simple_power(1, 1) is True
    assert module_0.is_simple_power(1, 5) is True       # 5^0
    assert module_0.is_simple_power(8, 2) is True       # 2^3
    assert module_0.is_simple_power(27, 3) is True      # 3^3
    assert module_0.is_simple_power(16, 4) is True      # 4^2

    assert module_0.is_simple_power(0, 2) is False
    assert module_0.is_simple_power(10, 2) is False
    assert module_0.is_simple_power(12, 3) is False
    assert module_0.is_simple_power(2, 1) is False

# Generated at 2026-10-25 02:54:15.511424
# Unit test for function is_simple_power
def test_is_simple_power():
    assert module_0.is_simple_power(1, 1) is True
    assert module_0.is_simple_power(1, 5) is True
    assert module_0.is_simple_power(8, 2) is True
    assert module_0.is_simple_power(27, 3) is True
    assert module_0.is_simple_power(12, 2) is False
    assert module_0.is_simple_power(0, 2) is False

# Generated at 2026-10-25 02:54:24.728622
# Unit test for function is_simple_power
def test_is_simple_power():
    assert module_0.is_simple_power(1, 1)
    assert module_0.is_simple_power(1, 5)
    assert module_0.is_simple_power(8, 2)
    assert module_0.is_simple_power(81, 3)

    assert not module_0.is_simple_power(12, 2)
    assert not module_0.is_simple_power(80, 3)
    assert not module_0.is_simple_power(2, 1)

# Generated at 2026-10-25 02:54:27.148190
# Unit test for function is_simple_power

# Generated at 2026-10-25 02:54:29.684619
# Unit test for function is_simple_power

# Generated at 2026-10-25 02:54:32.102845
# Unit test for function is_simple_power