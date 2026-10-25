

# Generated at 2026-10-24 22:42:45.581778
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+"], [2, 3]) == 5
    assert module_0.do_algebra(["-", "*"], [10, 2, 3]) == 4
    assert module_0.do_algebra(["+", "*"], [2, 3, 4]) == 14
    assert module_0.do_algebra(["/"], [8, 2]) == 4
    assert module_0.do_algebra(["**"], [2, 3]) == 8
    assert module_0.do_algebra([], [7]) == 7

# Generated at 2026-10-24 22:42:52.646796
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+"], [2, 3]) == 5
    assert module_0.do_algebra(["-"], [10, 4]) == 6
    assert module_0.do_algebra(["*"], [3, 5]) == 15
    assert module_0.do_algebra(["/"], [10, 2]) == 5.0
    assert module_0.do_algebra(["+", "*"], [2, 3, 4]) == 14  # Operator precedence
    assert module_0.do_algebra([], [7]) == 7

# Generated at 2026-10-24 22:42:59.501574
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+"], [2, 3]) == 5
    assert module_0.do_algebra(["-"], [10, 4]) == 6
    assert module_0.do_algebra(["*"], [3, 5]) == 15
    assert module_0.do_algebra(["/"], [10, 2]) == 5

    # Verifies normal operator precedence: 2 + (3 * 4) - 5
    assert module_0.do_algebra(["+", "*", "-"], [2, 3, 4, 5]) == 9

    # A single operand requires no operators
    assert module_0.do_algebra([], [7]) == 7

# Generated at 2026-10-24 22:43:06.569492
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra([], [5]) == 5
    assert module_0.do_algebra(["+"], [2, 3]) == 5
    assert module_0.do_algebra(["-", "*"], [10, 2, 3]) == 4
    assert module_0.do_algebra(["+", "*"], [2, 3, 4]) == 14
    assert module_0.do_algebra(["/"], [8, 2]) == 4

# Generated at 2026-10-24 22:43:13.535648
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+"], [2, 3]) == 5
    assert module_0.do_algebra(["-"], [10, 4]) == 6
    assert module_0.do_algebra(["*"], [3, 5]) == 15
    assert module_0.do_algebra(["/"], [8, 2]) == 4
    assert module_0.do_algebra(["+", "*"], [2, 3, 4]) == 14  # Operator precedence