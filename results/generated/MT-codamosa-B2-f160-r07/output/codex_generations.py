

# Generated at 2026-11-02 14:43:09.970859
# Unit test for function do_algebra
def test_do_algebra():
    # nonce:24b994de
    # Addition
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    # Subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    # Multiplication
    assert module_0.do_algebra(['*'], [4, 5]) == 20
    # Floor division
    assert module_0.do_algebra(['//'], [10, 3]) == 3
    # Modulo
    assert module_0.do_algebra(['%'], [10, 3]) == 1
    # Operator precedence: multiplication before addition
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14
    # Multiple mixed operators with precedence
    assert module_0.do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -9  # 1+2-3*4
    # Single operand, no operators
    assert module_0.do_algebra([], [42]) == 42
    # Negative operands
    assert module_0.do_algebra(['+', '-'], [5, -3, 2]) == 0
    # Subtraction of a negative operand
    assert module_0.do_algebra(['-'], [5, -3]) == 8
    # Repeated same operator
    assert module_0.do_algebra(['*'], [2, 3, 4]) == 24
    # Floor division with negative dividend (Python semantics)
    assert module_0.do_algebra(['//'], [-7, 2]) == -4
    # Modulo with negative dividend (Python semantics)
    assert module_0.do_algebra(['%'], [-7, 3]) == 2
    # Complex expression
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9  # 2+3*4-5
    # Larger numbers
    assert module_0.do_algebra(['*', '+'], [100, 200, 300]) == 20300
    # Zero handling
    assert module_0.do_algebra(['+', '*'], [0, 5, 3]) == 15
    print("All tests passed!")

# Generated at 2026-11-02 14:45:34.935692
# Unit test for function do_algebra
def test_do_algebra():
    # Single operand, no operators
    assert module_0.do_algebra([], [5]) == 5

    # Basic addition
    assert module_0.do_algebra(['+'], [2, 3]) == 5

    # Basic subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6

    # Basic multiplication
    assert module_0.do_algebra(['*'], [3, 4]) == 12

    # Integer division
    assert module_0.do_algebra(['//'], [7, 2]) == 3

    # Exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Operator precedence: 2 + 3 * 4 = 14
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Left-to-right for same precedence: 2 - 3 + 4 = 3
    assert module_0.do_algebra(['-', '+'], [2, 3, 4]) == 3

    # Exponentiation is right-associative: 2 ** 3 ** 2 = 512
    assert module_0.do_algebra(['**', '**'], [2, 3, 2]) == 512

    # Negative operands: -1 + -2 - -3 = 0
    assert module_0.do_algebra(['+', '-'], [-1, -2, -3]) == 4

    # Mixed: 5 * 3 - 2 = 13
    assert module_0.do_algebra(['*', '-'], [5, 3, 2]) == 13

    # Longer chain with precedence: 1 + 2 * 3 - 4 // 2 = 5
    assert module_0.do_algebra(['+', '*', '-', '//'], [1, 2, 3, 4, 2]) == 5

    # Floor division with negative operand: -7 // 2 = -4
    assert module_0.do_algebra(['//'], [-7, 2]) == -4

    # Exponentiation with negative base: -2 ** 3 = -8
    assert module_0.do_algebra(['**'], [-2, 3]) == -8

    # Zero operand: 5 * 0 + 3 = 3
    assert module_0.do_algebra(['*', '+'], [5, 0, 3]) == 3

    print("All do_algebra tests passed!")

# Generated at 2026-11-02 14:47:33.056785
# Unit test for function do_algebra
def test_do_algebra():
    # Single operand, no operators
    assert module_0.do_algebra([], [5]) == 5

    # Basic binary operations
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    assert module_0.do_algebra(['*'], [6, 7]) == 42
    assert module_0.do_algebra(['//'], [9, 2]) == 4
    assert module_0.do_algebra(['%'], [10, 3]) == 1

    # Operator precedence: * // % bind tighter than + -
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14
    assert module_0.do_algebra(['-', '//'], [20, 7, 2]) == 17
    assert module_0.do_algebra(['*', '%'], [5, 4, 3]) == 2

    # Longer expressions
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert module_0.do_algebra(['//', '*', '+'], [100, 5, 3, 2]) == 62
    assert module_0.do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10
    assert module_0.do_algebra(['*', '*', '*'], [2, 3, 4, 5]) == 120

    # Negative result
    assert module_0.do_algebra(['-'], [3, 10]) == -7

    # Modulo combined with other operations
    assert module_0.do_algebra(['%', '+'], [10, 4, 6]) == 12
# nonce:f2fb52b4

# Generated at 2026-11-02 14:48:50.348402
# Unit test for function do_algebra
def test_do_algebra():
    # Single operator cases
    assert module_0.do_algebra(['+'], [3, 5]) == 8
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    assert module_0.do_algebra(['*'], [6, 7]) == 42
    assert module_0.do_algebra(['//'], [9, 2]) == 4
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Multiple operators with precedence
    assert module_0.do_algebra(['+', '-', '*'], [2, 3, 4, 5]) == -15
    assert module_0.do_algebra(['+', '*'], [1, 2, 3]) == 7      # 1 + (2*3)
    assert module_0.do_algebra(['**', '*'], [2, 3, 4]) == 32    # (2**3) * 4
    assert module_0.do_algebra(['//', '-'], [7, 3, 4]) == -2    # (7//3) - 4
    assert module_0.do_algebra(['*', '-'], [5, 3, 2]) == 13     # (5*3) - 2

    # Longer chains
    assert module_0.do_algebra(['+', '+', '*'], [1, 2, 3, 4]) == 15  # 1 + 2 + (3*4)
    assert module_0.do_algebra(['//', '//'], [100, 5, 2]) == 10      # (100//5)//2

    print("All tests passed!")

# Generated at 2026-11-02 14:50:35.808686
# Unit test for function do_algebra
def test_do_algebra():
    # Single basic operations
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [5, 3]) == 2
    assert module_0.do_algebra(['*'], [4, 6]) == 24
    assert module_0.do_algebra(['//'], [7, 2]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Operator precedence: 2 + 3 * 4 = 14
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Same precedence, left-to-right: 10 - 3 - 2 = 5
    assert module_0.do_algebra(['-', '-'], [10, 3, 2]) == 5

    # Mixed operators: 2 * 3 + 4 - 5 = 5
    assert module_0.do_algebra(['*', '+', '-'], [2, 3, 4, 5]) == 5

    # Exponentiation binds tighter: 2 ** 3 * 4 = 32
    assert module_0.do_algebra(['**', '*'], [2, 3, 4]) == 32

    # 2 + 3 ** 2 = 11
    assert module_0.do_algebra(['+', '**'], [2, 3, 2]) == 11

    # Classic combination: 2 ** 3 * 4 // 5 = 6
    assert module_0.do_algebra(['**', '*', '//'], [2, 3, 4, 5]) == 6

    # Negative operands
    assert module_0.do_algebra(['+'], [3, -2]) == 1
    assert module_0.do_algebra(['*'], [3, -2]) == -6
    assert module_0.do_algebra(['-', '*'], [5, -3, 2]) == 11

    # Longer chains
    assert module_0.do_algebra(['+', '+', '+', '+'], [1, 2, 3, 4, 5]) == 15
    assert module_0.do_algebra(['*', '*', '*'], [2, 2, 2, 2]) == 16
    assert module_0.do_algebra(['+', '-', '*', '//'], [10, 2, 3, 4, 5]) == 12

    # Single operand, no operators
    assert module_0.do_algebra([], [42]) == 42

    # Result type check for floor division
    assert isinstance(module_0.do_algebra(['//'], [10, 3]), int)