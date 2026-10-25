

# Generated at 2026-10-24 21:08:16.020972
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 branch
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(8, 1) == False

    # exact powers
    assert module_0.is_simple_power(1, 2) == True    # 2^0
    assert module_0.is_simple_power(2, 2) == True    # 2^1
    assert module_0.is_simple_power(8, 2) == True    # 2^3
    assert module_0.is_simple_power(3, 3) == True    # 3^1
    assert module_0.is_simple_power(27, 3) == True   # 3^3
    assert module_0.is_simple_power(16, 4) == True   # 4^2
    assert module_0.is_simple_power(1, 100) == True  # any n^0

    # not powers
    assert module_0.is_simple_power(5, 2) == False
    assert module_0.is_simple_power(6, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(15, 4) == False

    print("All tests passed!")


test_is_simple_power()

# Generated at 2026-10-24 21:08:17.337788
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 branch
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(8, 1) == False

    # exact powers
    assert module_0.is_simple_power(1, 2) == True    # 2^0
    assert module_0.is_simple_power(2, 2) == True    # 2^1
    assert module_0.is_simple_power(8, 2) == True    # 2^3
    assert module_0.is_simple_power(3, 3) == True    # 3^1
    assert module_0.is_simple_power(27, 3) == True   # 3^3
    assert module_0.is_simple_power(16, 4) == True   # 4^2
    assert module_0.is_simple_power(1, 100) == True  # any n^0

    # not powers
    assert module_0.is_simple_power(5, 2) == False
    assert module_0.is_simple_power(6, 3) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(15, 4) == False

    print("All tests passed!")


test_is_simple_power()

# Generated at 2026-10-24 21:08:19.857059
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:08:22.272481
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:08:24.692667
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:08:27.110776
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:08:29.525975
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:08:31.942075
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:08:34.359905
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:08:36.779996
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:08:47.918897
# Unit test for function is_simple_power
def test_is_simple_power():assert module_0.is_simple_power(1, 1) is True