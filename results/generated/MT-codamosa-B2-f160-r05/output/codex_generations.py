

# Generated at 2026-11-02 08:50:57.135222
# Unit test for function do_algebra
def test_do_algebra():
    # Test addition
    assert module_0.do_algebra(['+'], [3, 4]) == 7

    # Test subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6

    # Test multiplication
    assert module_0.do_algebra(['*'], [6, 7]) == 42

    # Test floor division
    assert module_0.do_algebra(['//'], [9, 2]) == 4

    # Test exponentiation
    assert module_0.do_algebra(['**'], [2, 5]) == 32

    # Test operator precedence: 2 + 3 * 4 = 14 (not 20)
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Test left-to-right evaluation for equal precedence: 8 - 3 + 2 = 7
    assert module_0.do_algebra(['-', '+'], [8, 3, 2]) == 7

    # Test mixed operators: 5 * 4 - 3 = 17
    assert module_0.do_algebra(['*', '-'], [5, 4, 3]) == 17

    # Test exponentiation precedence: 2 ** 3 * 4 = 32
    assert module_0.do_algebra(['**', '*'], [2, 3, 4]) == 32

    # Test complex chain: 2 * 3 + 4 ** 2 // 5 = 6 + 3 = 9
    assert module_0.do_algebra(['*', '+', '**', '//'], [2, 3, 4, 2, 5]) == 9

    # Test with zero operand
    assert module_0.do_algebra(['+'], [0, 5]) == 5
    assert module_0.do_algebra(['*'], [7, 0]) == 0

    # Test single-operand expression (no operators)
    assert module_0.do_algebra([], [42]) == 42

    # Test longer chain: 10 + 2 - 3 * 4 // 5 = 12 - 2 = 10
    assert module_0.do_algebra(['+', '-', '*', '//'], [10, 2, 3, 4, 5]) == 10

    # Test multiple multiplications: 2 * 3 * 4 = 24
    assert module_0.do_algebra(['*', '*'], [2, 3, 4]) == 24

    # Test chained exponentiation (right-assoc): 2 ** 3 ** 2 = 2 ** 9 = 512
    assert module_0.do_algebra(['**', '**'], [2, 3, 2]) == 512

    print("All tests passed!")


if __name__ == "__main__":
    test_do_algebra()

# Generated at 2026-11-02 08:51:14.245129
# Unit test for function do_algebra
def test_do_algebra():
    # Single operations
    assert module_0.do_algebra(['+'], [3, 4]) == 7
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    assert module_0.do_algebra(['*'], [3, 4]) == 12
    assert module_0.do_algebra(['//'], [10, 3]) == 3
    assert module_0.do_algebra(['%'], [10, 3]) == 1
    assert module_0.do_algebra(['**'], [2, 3]) == 8
    assert module_0.do_algebra(['**'], [10, 2]) == 100

    # Zero handling
    assert module_0.do_algebra(['*'], [0, 100]) == 0
    assert module_0.do_algebra(['+', '-'], [0, 5, 3]) == 2

    # Multiple operators with correct precedence
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9      # 2 + 3*4 - 5
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 14             # 2*3 + 4
    assert module_0.do_algebra(['//', '*'], [8, 4, 2]) == 4             # 8//4*2
    assert module_0.do_algebra(['**', '*'], [2, 3, 2]) == 16            # 2**3*2
    assert module_0.do_algebra(['-', '*', '+'], [5, 2, 3, 1]) == 0      # 5 - 2*3 + 1
    assert module_0.do_algebra(['**', '+', '-'], [2, 3, 4, 1]) == 11    # 2**3 + 4 - 1
    assert module_0.do_algebra(['+', '//', '*'], [10, 7, 3, 2]) == 14   # 10 + 7//3*2
    assert module_0.do_algebra(['%', '*'], [10, 3, 2]) == 2             # 10%3*2
    assert module_0.do_algebra(['%', '+'], [10, 3, 5]) == 6             # 10%3 + 5
    assert module_0.do_algebra(['*', '*'], [2, 3, 2]) == 12             # 2*3*2

    # Longer operator chain
    assert module_0.do_algebra(['+', '-', '*', '//'], [10, 2, 3, 4, 5]) == 10  # 10 + 2 - 3*4//5

    # Larger operands
    assert module_0.do_algebra(['+', '*'], [123, 456, 789]) == 123 + 456 * 789
    assert module_0.do_algebra(['-', '//'], [1000000, 999999, 1]) == 1

# Generated at 2026-11-02 08:51:26.442479
# Unit test for function do_algebra
def test_do_algebra():
# nonce:9066ee0c
    # Single operand, no operators
    assert module_0.do_algebra([], [5]) == 5

    # Basic operations
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    assert module_0.do_algebra(['*'], [4, 6]) == 24
    assert module_0.do_algebra(['//'], [10, 3]) == 3

    # Operator precedence: * before +
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Mixed operators
    assert module_0.do_algebra(['+', '-', '*'], [10, 5, 3, 2]) == 9

    # Exponentiation
    assert module_0.do_algebra(['**', '*', '+'], [2, 3, 4, 5]) == 37

    # Negative operands
    assert module_0.do_algebra(['+', '-'], [-1, -2, -3]) == 2

    # Longer chain
    assert module_0.do_algebra(['+', '+', '*', '-'], [1, 2, 3, 4, 5]) == 1 + 2 + 3 * 4 - 5

    print("All tests passed!")

# Generated at 2026-11-02 08:51:44.868154
# Unit test for function do_algebra
def test_do_algebra():
    # Basic addition
    assert module_0.do_algebra(['+'], [3, 4]) == 7
    # Basic subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    # Basic multiplication
    assert module_0.do_algebra(['*'], [3, 4]) == 12
    # Integer (floor) division
    assert module_0.do_algebra(['//'], [10, 3]) == 3
    # Exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8
    # Negative result
    assert module_0.do_algebra(['-'], [3, 10]) == -7
    # Negative operands
    assert module_0.do_algebra(['+', '-'], [-2, 3, 4]) == -3
    # Multiple operators, left-to-right with precedence
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    # Multiplication binds tighter than addition
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10
    # Chained subtraction
    assert module_0.do_algebra(['-', '-'], [10, 3, 2]) == 5
    # Floor division with negative operand (Python floor semantics)
    assert module_0.do_algebra(['//'], [-10, 3]) == -4
    # Mixed expression with precedence
    assert module_0.do_algebra(['+', '*', '//'], [10, 2, 3, 4]) == 11
    # Longer chain
    assert module_0.do_algebra(['+', '-', '*', '+'], [1, 2, 3, 4, 5]) == 1 + 2 - 3 * 4 + 5  # -4
    # Single operand, no operators
    assert module_0.do_algebra([], [42]) == 42
    # Power combined with multiplication
    assert module_0.do_algebra(['**', '*'], [2, 3, 4]) == 2 ** 3 * 4  # 32

# Generated at 2026-11-02 08:51:56.532612
# Unit test for function do_algebra
def test_do_algebra():
    # Single operation tests
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [5, 2]) == 3
    assert module_0.do_algebra(['*'], [4, 6]) == 24
    assert module_0.do_algebra(['//'], [9, 4]) == 2

    # Mixed operators respecting precedence
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9      # 2 + 3*4 - 5
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8             # 7//3 * 4
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10             # 2*3 + 4
    assert module_0.do_algebra(['+', '-', '*', '/'.replace('/', '//')], [1, 2, 3, 4, 5]) == 0  # 1+2-3*4//5

    # Chained same operators
    assert module_0.do_algebra(['+', '+', '+'], [1, 1, 1, 1]) == 4
    assert module_0.do_algebra(['-', '-'], [10, 3, 2]) == 5
    assert module_0.do_algebra(['*', '*'], [2, 3, 4]) == 24
    assert module_0.do_algebra(['//', '//'], [100, 5, 2]) == 10

    # Negative operands
    assert module_0.do_algebra(['+', '-'], [-5, 3, 2]) == -4            # -5 + 3 - 2
    assert module_0.do_algebra(['*', '-'], [3, -2, 5]) == -11           # 3*(-2) - 5

    # Single operand, no operators
    assert module_0.do_algebra([], [42]) == 42

    # Result may be negative
    assert module_0.do_algebra(['-'], [3, 10]) == -7