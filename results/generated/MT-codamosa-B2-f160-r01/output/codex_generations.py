

# Generated at 2026-11-02 14:48:28.603614
# Unit test for function do_algebra
def test_do_algebra():
    # Simple addition
    assert module_0.do_algebra(['+'], [3, 4]) == 7
    assert module_0.do_algebra(['+', '+'], [1, 2, 3]) == 6

    # Subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    assert module_0.do_algebra(['-', '-'], [10, 4, 2]) == 4

    # Multiplication
    assert module_0.do_algebra(['*'], [3, 4]) == 12
    assert module_0.do_algebra(['*', '*'], [2, 3, 4]) == 24

    # Division
    assert module_0.do_algebra(['//'], [10, 3]) == 3
    assert module_0.do_algebra(['/'], [10, 2]) == 5.0

    # Operator precedence: * and // bind tighter than + and -
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14          # 2 + 3*4
    assert module_0.do_algebra(['+', '*', '-'], [1, 2, 3, 4]) == 3   # 1 + 2*3 - 4

    # Mixed operations
    assert module_0.do_algebra(['+', '-', '*'], [2, 3, 4, 5]) == -15  # 2+3-4*5
    assert module_0.do_algebra(['*', '+'], [5, 6, 7]) == 37           # 5*6+7
    assert module_0.do_algebra(['-', '+', '//'], [20, 5, 3, 2]) == 16 # 20-5+3//2

    # Negative operands
    assert module_0.do_algebra(['+'], [-2, 3]) == 1
    assert module_0.do_algebra(['-'], [5, -2]) == 7
    assert module_0.do_algebra(['*', '-'], [-3, 4, 2]) == -14         # -3*4 - 2

    # Single operand, no operators
    assert module_0.do_algebra([], [42]) == 42

    # Longer chain
    assert module_0.do_algebra(['+', '*', '-', '*'], [1, 2, 3, 4, 5]) == 3  # 1+2*3-4*5

    print("All tests passed!")


test_do_algebra()

# Generated at 2026-11-02 14:49:44.536779
# Unit test for function do_algebra
def test_do_algebra():
    # Single operand, no operators
    assert module_0.do_algebra([], [5]) == 5

    # Simple addition
    assert module_0.do_algebra(['+'], [2, 3]) == 5

    # Simple subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6

    # Simple multiplication
    assert module_0.do_algebra(['*'], [3, 4]) == 12

    # Integer division
    assert module_0.do_algebra(['//'], [10, 3]) == 3

    # Modulo
    assert module_0.do_algebra(['%'], [10, 3]) == 1

    # Operator precedence: multiplication before addition
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Operator precedence: division before subtraction
    assert module_0.do_algebra(['-', '//'], [10, 4, 2]) == 8

    # Multiple mixed operators
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    # Negative result
    assert module_0.do_algebra(['-'], [3, 10]) == -7

    # Negative operand via subtraction chain
    assert module_0.do_algebra(['-', '-'], [1, 2, 3]) == 2

    # Modulo and multiplication combined
    assert module_0.do_algebra(['*', '%'], [4, 5, 3]) == 2

    # Long chain of additions
    assert module_0.do_algebra(['+', '+', '+', '+'], [1, 2, 3, 4, 5]) == 15

    # Long chain of multiplications
    assert module_0.do_algebra(['*', '*', '*'], [2, 3, 4, 5]) == 120

    # Division truncates toward negative infinity (floor division)
    assert module_0.do_algebra(['//'], [7, 2]) == 3
    assert module_0.do_algebra(['//'], [-7, 2]) == -4

    # Complex expression
    assert module_0.do_algebra(['+', '*', '//', '-'], [5, 3, 2, 4, 1]) == 6

    print("All test cases passed!")


test_do_algebra()

# Generated at 2026-11-02 14:50:03.845509
# Unit test for function do_algebra
def test_do_algebra():# Single operand, no operators
    assert module_0.do_algebra([], [5]) == 5

    # Basic addition
    assert module_0.do_algebra(['+'], [2, 3]) == 5

    # Basic subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6

    # Basic multiplication
    assert module_0.do_algebra(['*'], [3, 4]) == 12

    # Floor division
    assert module_0.do_algebra(['//'], [10, 3]) == 3

    # Modulo
    assert module_0.do_algebra(['%'], [10, 3]) == 1

    # Exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Operator precedence: 2 + 3*4 - 5 = 9
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    # Mixed multiplication and addition: 1*2 + 3 = 5
    assert module_0.do_algebra(['*', '+'], [1, 2, 3]) == 5

    # Sequential subtraction: 10 - 2 - 3 = 5
    assert module_0.do_algebra(['-', '-'], [10, 2, 3]) == 5

    # Negative operand: 5 + (-3) = 2
    assert module_0.do_algebra(['+'], [5, -3]) == 2

    # Negative first operand: -2 * 3 = -6
    assert module_0.do_algebra(['*'], [-2, 3]) == -6

    # Complex expression: 8 + 4*2//3 = 8 + 2 = 10
    assert module_0.do_algebra(['+', '*', '//'], [8, 4, 2, 3]) == 10

    # Exponent precedence: 2 * 3**2 = 18
    assert module_0.do_algebra(['*', '**'], [2, 3, 2]) == 18

    # Modulo chain: 10 % 4 % 3 = 2 % 3 = 2
    assert module_0.do_algebra(['%', '%'], [10, 4, 3]) == 2

    # Large numbers
    assert module_0.do_algebra(['**'], [2, 10]) == 1024

    print("All test cases passed!")


test_do_algebra()

# Generated at 2026-11-02 14:51:42.972281
# Unit test for function do_algebra
def test_do_algebra():
    # Basic addition
    assert module_0.do_algebra(['+'], [2, 3]) == 5

    # Basic subtraction
    assert module_0.do_algebra(['-'], [5, 3]) == 2

    # Basic multiplication
    assert module_0.do_algebra(['*'], [2, 3]) == 6

    # Integer division
    assert module_0.do_algebra(['//'], [7, 2]) == 3

    # Single operand, no operators
    assert module_0.do_algebra([], [5]) == 5

    # Operator precedence: 2 + 3*4 - 5 = 9
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    # Multiplication binds tighter than addition: 2*3 + 4 = 10
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10

    # Negative result: 3 - 5 = -2
    assert module_0.do_algebra(['-'], [3, 5]) == -2

    # Chained multiplications: 2*3*4 + 5 = 29
    assert module_0.do_algebra(['*', '*', '+'], [2, 3, 4, 5]) == 29

    # Mixed chain: 1 + 2*3 - 4 = 3
    assert module_0.do_algebra(['+', '*', '-'], [1, 2, 3, 4]) == 3

    print("All tests passed!")


test_do_algebra()

# Generated at 2026-11-02 14:52:45.677822
# Unit test for function do_algebra
def test_do_algebra():
    # Basic single-operator cases
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [10, 3]) == 7
    assert module_0.do_algebra(['*'], [4, 5]) == 20
    assert module_0.do_algebra(['//'], [10, 3]) == 3
    assert module_0.do_algebra(['%'], [10, 3]) == 1
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Multiple operators respecting precedence
    assert module_0.do_algebra(['**', '*', '+'], [2, 3, 4, 5]) == 37   # 2**3 * 4 + 5
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9     # 2 + 3*4 - 5
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8            # 7//3 * 4

    # Single operand, no operators
    assert module_0.do_algebra([], [42]) == 42

    # Longer chains
    assert module_0.do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10
    assert module_0.do_algebra(['*', '*', '*'], [1, 2, 3, 4]) == 24
    assert module_0.do_algebra(['-', '+'], [10, 4, 2]) == 8            # 10 - 4 + 2
    assert module_0.do_algebra(['%', '-'], [10, 3, 2]) == 0            # 10 % 3 - 2

    # Mixed operators with precedence
    assert module_0.do_algebra(['+', '**', '//'], [1, 2, 3, 4]) == 5   # 1 + 2**3 // 4

    print("All do_algebra tests passed!")