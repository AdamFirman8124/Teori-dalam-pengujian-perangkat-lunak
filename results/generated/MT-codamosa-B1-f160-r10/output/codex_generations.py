

# Generated at 2026-10-25 02:16:47.014816
# Unit test for function do_algebra

# Generated at 2026-10-25 02:16:49.550276
# Unit test for function do_algebra

# Generated at 2026-10-25 02:16:51.966109
# Unit test for function do_algebra

# Generated at 2026-10-25 02:17:04.819821
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+", "*"], [2, 3, 4]) == 14
    assert module_0.do_algebra(["-", "/"], [10, 4, 2]) == 3
    assert module_0.do_algebra(["*", "+"], [2, 3, 4]) == 10
    assert module_0.do_algebra(["/", "-"], [20, 5, 2]) == 2
    assert module_0.do_algebra([], [7]) == 7

# Generated at 2026-10-25 02:17:28.987100
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+"], [2, 3]) == 5
    assert module_0.do_algebra(["-"], [10, 4]) == 6
    assert module_0.do_algebra(["*"], [3, 5]) == 15
    assert module_0.do_algebra(["/"], [10, 4]) == pytest.approx(2.5)

    # Produces: 2 + 3 * 4
    assert module_0.do_algebra(["+", "*"], [2, 3, 4]) == 14

# Generated at 2026-10-25 02:17:40.557764
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+", "*"], [2, 3, 4]) == 14
    assert module_0.do_algebra(["-", "/"], [10, 4, 2]) == 3
    assert module_0.do_algebra(["**"], [2, 3]) == 8
    assert module_0.do_algebra(["+", "-", "*"], [10, 5, 2, 3]) == 9

# Generated at 2026-10-25 02:18:02.369978
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