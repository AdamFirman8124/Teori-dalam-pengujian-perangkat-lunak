

# Generated at 2026-10-25 04:51:03.763689
# Unit test for function is_simple_power

# Generated at 2026-10-25 04:51:06.225342
# Unit test for function is_simple_power

# Generated at 2026-10-25 04:51:08.611130
# Unit test for function is_simple_power

# Generated at 2026-10-25 04:51:11.026617
# Unit test for function is_simple_power

# Generated at 2026-10-25 04:51:13.443566
# Unit test for function is_simple_power

# Generated at 2026-10-25 04:51:15.869960
# Unit test for function is_simple_power

# Generated at 2026-10-25 04:51:18.299894
# Unit test for function is_simple_power

# Generated at 2026-10-25 04:51:20.716475
# Unit test for function is_simple_power

# Generated at 2026-10-25 04:51:23.133997
# Unit test for function is_simple_power

# Generated at 2026-10-25 04:51:31.757070
# Unit test for function is_simple_power
def test_is_simple_power():
    assert module_0.is_simple_power(1, 1) is True
    assert module_0.is_simple_power(1, 2) is True   # 2**0
    assert module_0.is_simple_power(8, 2) is True   # 2**3
    assert module_0.is_simple_power(9, 3) is True   # 3**2
    assert module_0.is_simple_power(16, 4) is True  # 4**2

    assert module_0.is_simple_power(2, 1) is False
    assert module_0.is_simple_power(10, 2) is False
    assert module_0.is_simple_power(15, 3) is False

# Generated at 2026-10-25 04:51:36.866409
# Unit test for function is_simple_power
def test_is_simple_power():
    assert module_0.is_simple_power(1, 1) is True
    assert module_0.is_simple_power(1, 5) is True
    assert module_0.is_simple_power(8, 2) is True
    assert module_0.is_simple_power(81, 3) is True
    assert module_0.is_simple_power(12, 2) is False
    assert module_0.is_simple_power(80, 3) is False