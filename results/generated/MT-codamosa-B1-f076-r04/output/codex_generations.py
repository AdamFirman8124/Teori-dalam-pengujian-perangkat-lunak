

# Generated at 2026-10-25 12:25:04.195386
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 special case: only 1 is a power of 1
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # 1 is a simple power (n**0) of any n
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 3) == True
    assert module_0.is_simple_power(1, 100) == True

    # powers of 2
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(12, 2) == False

    # powers of 3
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(8, 3) == False
    assert module_0.is_simple_power(10, 3) == False

    # other bases
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(1000, 10) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(50, 10) == False

    # 0 and negative x are not simple powers
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-4, 2) == False

# Generated at 2026-10-25 12:25:05.778230
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 special case: only 1 is a power of 1
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # 1 is a simple power (n**0) of any n
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 3) == True
    assert module_0.is_simple_power(1, 100) == True

    # powers of 2
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(12, 2) == False

    # powers of 3
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(8, 3) == False
    assert module_0.is_simple_power(10, 3) == False

    # other bases
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(1000, 10) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(50, 10) == False

    # 0 and negative x are not simple powers
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-4, 2) == False

# Generated at 2026-10-25 12:25:11.977118
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 special case: only 1 is a power of 1
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # 1 is a simple power (n**0) of any n
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 3) == True
    assert module_0.is_simple_power(1, 100) == True

    # powers of 2
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(12, 2) == False

    # powers of 3
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(8, 3) == False
    assert module_0.is_simple_power(10, 3) == False

    # other bases
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(1000, 10) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(50, 10) == False

    # 0 and negative x are not simple powers
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-4, 2) == False

# Generated at 2026-10-25 12:25:16.690235
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 special case: only 1 is a power of 1
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # 1 is a simple power (n**0) of any n
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 3) == True
    assert module_0.is_simple_power(1, 100) == True

    # powers of 2
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(12, 2) == False

    # powers of 3
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(8, 3) == False
    assert module_0.is_simple_power(10, 3) == False

    # other bases
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(1000, 10) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(50, 10) == False

    # 0 and negative x are not simple powers
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-4, 2) == False

# Generated at 2026-10-25 12:25:23.102195
# Unit test for function is_simple_power
def test_is_simple_power():
    # n == 1 special case: only 1 is a power of 1
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(2, 1) == False
    assert module_0.is_simple_power(0, 1) == False

    # 1 is a simple power (n**0) of any n
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 3) == True
    assert module_0.is_simple_power(1, 100) == True

    # powers of 2
    assert module_0.is_simple_power(2, 2) == True
    assert module_0.is_simple_power(4, 2) == True
    assert module_0.is_simple_power(8, 2) == True
    assert module_0.is_simple_power(16, 2) == True
    assert module_0.is_simple_power(3, 2) == False
    assert module_0.is_simple_power(6, 2) == False
    assert module_0.is_simple_power(10, 2) == False
    assert module_0.is_simple_power(12, 2) == False

    # powers of 3
    assert module_0.is_simple_power(3, 3) == True
    assert module_0.is_simple_power(9, 3) == True
    assert module_0.is_simple_power(27, 3) == True
    assert module_0.is_simple_power(8, 3) == False
    assert module_0.is_simple_power(10, 3) == False

    # other bases
    assert module_0.is_simple_power(16, 4) == True
    assert module_0.is_simple_power(125, 5) == True
    assert module_0.is_simple_power(1000, 10) == True
    assert module_0.is_simple_power(100, 10) == True
    assert module_0.is_simple_power(50, 10) == False

    # 0 and negative x are not simple powers
    assert module_0.is_simple_power(0, 2) == False
    assert module_0.is_simple_power(-4, 2) == False