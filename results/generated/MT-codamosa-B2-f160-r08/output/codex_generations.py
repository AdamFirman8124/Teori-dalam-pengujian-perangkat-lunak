

# Generated at 2026-11-02 11:42:18.016786
# Unit test for function do_algebra
def test_do_algebra():
    # Test addition only
    assert module_0.do_algebra(['+'], [3, 4]) == 7

    # Test subtraction only
    assert module_0.do_algebra(['-'], [10, 4]) == 6

    # Test multiplication only
    assert module_0.do_algebra(['*'], [5, 6]) == 30

    # Test floor division
    assert module_0.do_algebra(['//'], [7, 3]) == 2

    # Test true division
    assert module_0.do_algebra(['/'], [8, 2]) == 4.0

    # Test exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Test single operand with no operators
    assert module_0.do_algebra([], [42]) == 42

    # Test mixed operators with precedence: 2 + 3*4 - 5 = 9
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

    # Test precedence: 7//3*4 = 2*4 = 8
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8

    # Test exponentiation with multiplication: 2**3*4 = 32
    assert module_0.do_algebra(['**', '*'], [2, 3, 4]) == 32

    # Test negative result: 2 - 5 + 3 = 0
    assert module_0.do_algebra(['-', '+'], [2, 5, 3]) == 0

    # Test negative operands: -2 * 3 = -6
    assert module_0.do_algebra(['*'], [-2, 3]) == -6

    print("All tests passed!")


if __name__ == "__main__":
    test_do_algebra()

# Generated at 2026-11-02 11:43:35.800682
# Unit test for function do_algebra
def test_do_algebra():
    # Basic addition
    assert module_0.do_algebra(['+'], [2, 3]) == 5

    # Subtraction
    assert module_0.do_algebra(['-'], [5, 3]) == 2

    # Multiplication
    assert module_0.do_algebra(['*'], [4, 6]) == 24

    # Integer (floor) division
    assert module_0.do_algebra(['//'], [7, 2]) == 3

    # Exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Operator precedence: multiplication before addition
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Operator precedence: exponent before subtraction
    assert module_0.do_algebra(['-', '**'], [10, 2, 3]) == 2

    # Multiple operations, left-to-right for same precedence
    assert module_0.do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -3  # 1+2-3*4

    # Longer chain with mixed precedence
    assert module_0.do_algebra(['*', '+', '//'], [2, 3, 4, 2]) == 8  # 2*3 + 4//2

    # Single operand (no operators)
    assert module_0.do_algebra([], [42]) == 42

    # Zero handling
    assert module_0.do_algebra(['+', '*'], [0, 5, 3]) == 15

    # Large numbers with exponentiation
    assert module_0.do_algebra(['**', '*'], [2, 10, 3]) == 3072  # 2**10 * 3

    print("All tests passed!")


if __name__ == "__main__":
    test_do_algebra()

# Generated at 2026-11-02 11:45:05.599891
# Unit test for function do_algebra
def test_do_algebra():
    # Test basic addition
    assert module_0.do_algebra(['+'], [3, 4]) == 7

    # Test basic subtraction
    assert module_0.do_algebra(['-'], [10, 3]) == 7

    # Test basic multiplication
    assert module_0.do_algebra(['*'], [5, 6]) == 30

    # Test integer division
    assert module_0.do_algebra(['//'], [10, 3]) == 3

    # Test modulo
    assert module_0.do_algebra(['%'], [10, 3]) == 1

    # Test exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Test multiple operators with precedence: 2 + 3 * 4 = 14
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Test parentheses-free precedence: 2 * 3 + 4 = 10
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10

    # Test chain of operations: 5 - 3 + 2 = 4
    assert module_0.do_algebra(['-', '+'], [5, 3, 2]) == 4

    # Test exponent with multiplication: 2 ** 3 * 4 = 32
    assert module_0.do_algebra(['**', '*'], [2, 3, 4]) == 32

    # Test negative result: 3 - 10 = -7
    assert module_0.do_algebra(['-'], [3, 10]) == -7

    # Test with zero operand: 0 + 5 = 5
    assert module_0.do_algebra(['+'], [0, 5]) == 5

    # Test single operand (no operators)
    assert module_0.do_algebra([], [42]) == 42

    # Test complex mixed expression: 5 * 2 - 3 + 10 // 2 = 12
    assert module_0.do_algebra(['*', '-', '+', '//'], [5, 2, 3, 10, 2]) == 12

    # Test modulo with multiplication: 10 % 3 * 4 = 4
    assert module_0.do_algebra(['%', '*'], [10, 3, 4]) == 4

    # Test exponent chain (right associative): 2 ** 2 ** 2 = 16
    assert module_0.do_algebra(['**', '**'], [2, 2, 2]) == 16

    print("All test_do_algebra tests passed!")


test_do_algebra()

# Generated at 2026-11-02 11:46:48.676333
# Unit test for function do_algebra
def test_do_algebra():
    # Single operator tests
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    assert module_0.do_algebra(['*'], [6, 7]) == 42
    assert module_0.do_algebra(['//'], [9, 2]) == 4

    # Operator precedence: * and // bind tighter than + and -
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14    # 2 + 3*4
    assert module_0.do_algebra(['-', '*'], [10, 2, 3]) == 4    # 10 - 2*3
    assert module_0.do_algebra(['+', '//'], [5, 8, 3]) == 7    # 5 + 8//3

    # Multiple operators
    assert module_0.do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -9  # 1+2-3*4
    assert module_0.do_algebra(['*', '+'], [10, 20, 30]) == 230      # 10*20+30
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9   # 2+3*4-5

    # Chained floor division is left-associative
    assert module_0.do_algebra(['//', '//'], [100, 5, 2]) == 10  # (100//5)//2

    # Mixed // and * share precedence, evaluated left to right
    assert module_0.do_algebra(['//', '*'], [9, 2, 3]) == 12     # (9//2)*3

    # Zero and identity cases
    assert module_0.do_algebra(['+'], [0, 0]) == 0
    assert module_0.do_algebra(['*'], [123, 0]) == 0
    assert module_0.do_algebra(['+', '-'], [7, 7, 7]) == 7       # 7+7-7
    assert module_0.do_algebra(['-', '+'], [0, 5, 5]) == 0       # 0-5+5

    print("All tests passed!")


if __name__ == "__main__":
    test_do_algebra()