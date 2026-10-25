

# Generated at 2026-10-24 04:37:04.901466
# Unit test for function do_algebra
def test_do_algebra():
    # Multiplication and division bind tighter than + and -
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 5   # 2 + 3*4 - 5
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8          # 7//3 * 4
    assert module_0.do_algebra(['-'], [10, 4]) == 6                  # 10 - 4
    assert module_0.do_algebra(['+'], [1, 2]) == 3                   # 1 + 2
    assert module_0.do_algebra(['*'], [5, 5]) == 25                  # 5 * 5
    assert module_0.do_algebra(['//'], [9, 2]) == 4                  # 9 // 2 (floor division)
    assert module_0.do_algebra(['**'], [2, 3]) == 8                  # 2 ** 3
    # Long chain with mixed precedence
    assert module_0.do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -7  # 1 + 2 - 3*4
    # Single operand, empty operator list
    assert module_0.do_algebra([], [42]) == 42
    # Multi-digit numbers must not be concatenated as digits
    assert module_0.do_algebra(['+'], [11, 22]) == 33                # not 1122
    print("All tests passed.")

test_do_algebra()

# Generated at 2026-10-24 04:37:06.220175
# Unit test for function do_algebra
def test_do_algebra():
    # Multiplication and division bind tighter than + and -
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 5   # 2 + 3*4 - 5
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8          # 7//3 * 4
    assert module_0.do_algebra(['-'], [10, 4]) == 6                  # 10 - 4
    assert module_0.do_algebra(['+'], [1, 2]) == 3                   # 1 + 2
    assert module_0.do_algebra(['*'], [5, 5]) == 25                  # 5 * 5
    assert module_0.do_algebra(['//'], [9, 2]) == 4                  # 9 // 2 (floor division)
    assert module_0.do_algebra(['**'], [2, 3]) == 8                  # 2 ** 3
    # Long chain with mixed precedence
    assert module_0.do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -7  # 1 + 2 - 3*4
    # Single operand, empty operator list
    assert module_0.do_algebra([], [42]) == 42
    # Multi-digit numbers must not be concatenated as digits
    assert module_0.do_algebra(['+'], [11, 22]) == 33                # not 1122
    print("All tests passed.")

test_do_algebra()

# Generated at 2026-10-24 04:37:07.529357
# Unit test for function do_algebra
def test_do_algebra():
    # Multiplication and division bind tighter than + and -
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 5   # 2 + 3*4 - 5
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8          # 7//3 * 4
    assert module_0.do_algebra(['-'], [10, 4]) == 6                  # 10 - 4
    assert module_0.do_algebra(['+'], [1, 2]) == 3                   # 1 + 2
    assert module_0.do_algebra(['*'], [5, 5]) == 25                  # 5 * 5
    assert module_0.do_algebra(['//'], [9, 2]) == 4                  # 9 // 2 (floor division)
    assert module_0.do_algebra(['**'], [2, 3]) == 8                  # 2 ** 3
    # Long chain with mixed precedence
    assert module_0.do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -7  # 1 + 2 - 3*4
    # Single operand, empty operator list
    assert module_0.do_algebra([], [42]) == 42
    # Multi-digit numbers must not be concatenated as digits
    assert module_0.do_algebra(['+'], [11, 22]) == 33                # not 1122
    print("All tests passed.")

test_do_algebra()

# Generated at 2026-10-24 04:37:08.872160
# Unit test for function do_algebra
def test_do_algebra():
    # Multiplication and division bind tighter than + and -
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 5   # 2 + 3*4 - 5
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8          # 7//3 * 4
    assert module_0.do_algebra(['-'], [10, 4]) == 6                  # 10 - 4
    assert module_0.do_algebra(['+'], [1, 2]) == 3                   # 1 + 2
    assert module_0.do_algebra(['*'], [5, 5]) == 25                  # 5 * 5
    assert module_0.do_algebra(['//'], [9, 2]) == 4                  # 9 // 2 (floor division)
    assert module_0.do_algebra(['**'], [2, 3]) == 8                  # 2 ** 3
    # Long chain with mixed precedence
    assert module_0.do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -7  # 1 + 2 - 3*4
    # Single operand, empty operator list
    assert module_0.do_algebra([], [42]) == 42
    # Multi-digit numbers must not be concatenated as digits
    assert module_0.do_algebra(['+'], [11, 22]) == 33                # not 1122
    print("All tests passed.")

test_do_algebra()

# Generated at 2026-10-24 04:37:10.178902
# Unit test for function do_algebra
def test_do_algebra():
    # Multiplication and division bind tighter than + and -
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 5   # 2 + 3*4 - 5
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8          # 7//3 * 4
    assert module_0.do_algebra(['-'], [10, 4]) == 6                  # 10 - 4
    assert module_0.do_algebra(['+'], [1, 2]) == 3                   # 1 + 2
    assert module_0.do_algebra(['*'], [5, 5]) == 25                  # 5 * 5
    assert module_0.do_algebra(['//'], [9, 2]) == 4                  # 9 // 2 (floor division)
    assert module_0.do_algebra(['**'], [2, 3]) == 8                  # 2 ** 3
    # Long chain with mixed precedence
    assert module_0.do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -7  # 1 + 2 - 3*4
    # Single operand, empty operator list
    assert module_0.do_algebra([], [42]) == 42
    # Multi-digit numbers must not be concatenated as digits
    assert module_0.do_algebra(['+'], [11, 22]) == 33                # not 1122
    print("All tests passed.")

test_do_algebra()