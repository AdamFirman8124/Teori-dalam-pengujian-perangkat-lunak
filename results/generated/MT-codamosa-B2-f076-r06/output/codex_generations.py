

# Generated at 2026-10-24 20:59:13.037828
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:15.456804
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:17.876439
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:20.292848
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:22.712135
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:25.129966
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:27.548298
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:29.967243
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:32.386342
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:34.805375
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:37.224161
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:39.640968
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:42.057759
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:44.472771
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:46.889008
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:49.308707
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:51.721582
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:54.137609
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:56.555510
# Unit test for function is_simple_power

# Generated at 2026-10-24 20:59:58.971294
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:00:01.388121
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:00:03.804064
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:00:06.220120
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:00:08.636748
# Unit test for function is_simple_power

# Generated at 2026-10-24 21:00:14.797394
# Unit test for function is_simple_power
def test_is_simple_power():
    # x == 1 cases
    assert module_0.is_simple_power(1, 1) == True
    assert module_0.is_simple_power(1, 2) == True
    assert module_0.is_simple_power(1, 10) == True

    # n == 1 cases (only x == 1 is a power of 1)
    assert module_0.is_simple_power(5, 1) == False
    assert module_0.is_simple_power(2, 1) == False

    # exact powers
    assert module_0.is_simple_power(8, 2) == True      # 2^3
    assert module_0.is_simple_power(3, 2) == True      # 2^0 = 1? no: 3 is not... corrected below

# Generated at 2026-10-24 21:00:16.124119
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

# Generated at 2026-10-24 21:00:17.555864
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

# Generated at 2026-10-24 21:00:19.815725
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

# Generated at 2026-10-24 21:00:21.856496
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

# Generated at 2026-10-24 21:00:23.187758
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

# Generated at 2026-10-24 21:00:24.514903
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