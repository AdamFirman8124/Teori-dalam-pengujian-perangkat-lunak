

# Generated at 2026-10-25 09:00:33.449647
# Unit test for function do_algebra

# Generated at 2026-10-25 09:00:35.867296
# Unit test for function do_algebra

# Generated at 2026-10-25 09:00:38.552336
# Unit test for function do_algebra

# Generated at 2026-10-25 09:00:50.309156
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14
    assert module_0.do_algebra(['**', '*'], [2, 3, 2]) == 16
    assert module_0.do_algebra(['//', '+'], [7, 3, 2]) == 4
    assert module_0.do_algebra(['-', '+'], [10, 5, 3]) == 8
    assert module_0.do_algebra([], [42]) == 42

# Generated at 2026-10-25 09:01:06.196624
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [5, 3]) == 2
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14  # 2 + (3 * 4)
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9  # 2 + 3*4 - 5
    assert module_0.do_algebra(['//'], [7, 2]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8
    assert module_0.do_algebra(['**', '*'], [2, 3, 2]) == 16  # (2**3)*2
    assert module_0.do_algebra([], [42]) == 42

# Generated at 2026-10-25 09:01:20.941021
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [5, 3]) == 2
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14  # 2 + (3 * 4)
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9  # 2 + 3*4 - 5
    assert module_0.do_algebra(['//'], [7, 2]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8
    assert module_0.do_algebra(['**', '*'], [2, 3, 2]) == 16  # (2**3)*2
    assert module_0.do_algebra([], [42]) == 42

# Generated at 2026-10-25 09:01:22.490308
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [5, 3]) == 2
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14  # 2 + (3 * 4)
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9  # 2 + 3*4 - 5
    assert module_0.do_algebra(['//'], [7, 2]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8
    assert module_0.do_algebra(['**', '*'], [2, 3, 2]) == 16  # (2**3)*2
    assert module_0.do_algebra([], [42]) == 42