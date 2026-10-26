

# Generated at 2026-10-25 06:23:35.140492
# Unit test for function do_algebra

# Generated at 2026-10-25 06:23:37.553544
# Unit test for function do_algebra

# Generated at 2026-10-25 06:23:39.967842
# Unit test for function do_algebra

# Generated at 2026-10-25 06:23:42.381637
# Unit test for function do_algebra

# Generated at 2026-10-25 06:23:44.796778
# Unit test for function do_algebra

# Generated at 2026-10-25 06:23:47.212630
# Unit test for function do_algebra

# Generated at 2026-10-25 06:23:49.625794
# Unit test for function do_algebra

# Generated at 2026-10-25 06:23:52.040726
# Unit test for function do_algebra

# Generated at 2026-10-25 06:23:54.454568
# Unit test for function do_algebra

# Generated at 2026-10-25 06:24:09.944301
# Unit test for function do_algebra
def test_do_algebra():assert module_0.do_algebra(["+"], [2, 3]) == 5

# Generated at 2026-10-25 06:24:11.340828
# Unit test for function do_algebra
def test_do_algebra():
    # Basic operations
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [2, 3]) == -1
    assert module_0.do_algebra(['*'], [2, 3]) == 6
    assert module_0.do_algebra(['//'], [7, 2]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Operator precedence: * before +
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14  # 2 + 3*4

    # Multi-operator chain
    assert module_0.do_algebra(['+', '-', '*'], [2, 3, 4, 5]) == -9  # 2 + 3 - 4*5

    # Exponentiation binds tightest
    assert module_0.do_algebra(['+', '**'], [1, 2, 3]) == 9  # 1 + 2**3

    # Integer division with precedence
    assert module_0.do_algebra(['//', '*'], [9, 2, 3]) == 12  # 9 // 2 * 3 -> 4*3

    # Single operand, no operators
    assert module_0.do_algebra([], [42]) == 42

    # Zero handling
    assert module_0.do_algebra(['*'], [0, 5]) == 0

    print("All tests passed!")


test_do_algebra()