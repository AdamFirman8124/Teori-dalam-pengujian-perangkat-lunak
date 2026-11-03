

# Generated at 2026-11-01 19:48:20.295887
# Unit test for function do_algebra
def test_do_algebra():
    # Addition
    assert module_0.do_algebra(['+'], [3, 4]) == 7
    assert module_0.do_algebra(['+'], [0, 0]) == 0

    # Subtraction
    assert module_0.do_algebra(['-'], [10, 5]) == 5
    assert module_0.do_algebra(['-'], [3, 10]) == -7

    # Multiplication
    assert module_0.do_algebra(['*'], [3, 4]) == 12
    assert module_0.do_algebra(['*'], [-2, 5]) == -10

    # Floor division
    assert module_0.do_algebra(['//'], [9, 2]) == 4

    # Operator precedence: * before +
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Mixed operators
    assert module_0.do_algebra(['-', '+', '*'], [10, 2, 3, 4]) == 20

    # Chained same operator
    assert module_0.do_algebra(['*', '*', '-'], [2, 3, 4, 5]) == 19
    assert module_0.do_algebra(['-', '-'], [5, 3, 2]) == 0

    print("All tests passed!")

test_do_algebra()

# Generated at 2026-11-01 19:48:46.252284
# Unit test for function do_algebra
def test_do_algebra():
    # Single addition
    assert module_0.do_algebra(['+'], [3, 5]) == 8

    # Single subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6

    # Single multiplication
    assert module_0.do_algebra(['*'], [6, 7]) == 42

    # Floor division
    assert module_0.do_algebra(['//'], [10, 3]) == 3

    # Modulo
    assert module_0.do_algebra(['%'], [10, 3]) == 1

    # Exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Operator precedence: multiplication before addition
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 2 + 3 * 4 == 14

    # Mixed operations with precedence
    assert module_0.do_algebra(['+', '-', '*'], [5, 3, 2, 8]) == 5 + 3 - 2 * 8

    # Chained additions
    assert module_0.do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

    # Chained subtractions
    assert module_0.do_algebra(['-', '-'], [20, 5, 3]) == 12

    # Complex mixed expression
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 2 + 3 * 4 - 5

    # Exponent combined with multiplication
    assert module_0.do_algebra(['**', '*'], [2, 3, 4]) == 2 ** 3 * 4

    # Result is an integer
    assert isinstance(module_0.do_algebra(['+', '*'], [1, 2, 3]), int)

    # Zero operand
    assert module_0.do_algebra(['*'], [0, 100]) == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_do_algebra()

# Generated at 2026-11-01 19:49:11.347783
# Unit test for function do_algebra
def test_do_algebra():
    # Single basic operations
    assert module_0.do_algebra(['+'], [1, 2]) == 3
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    assert module_0.do_algebra(['*'], [3, 5]) == 15
    assert module_0.do_algebra(['//'], [10, 3]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Operator precedence (eval semantics)
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9       # 2 + 3*4 - 5
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8              # 7//3 * 4
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10              # 2*3 + 4
    assert module_0.do_algebra(['+', '//'], [10, 5, 2]) == 12            # 10 + 5//2
    assert module_0.do_algebra(['**', '+'], [2, 3, 1]) == 9              # 2**3 + 1

    # Same-precedence left-to-right evaluation
    assert module_0.do_algebra(['+', '-'], [10, 5, 2]) == 13             # 10 + 5 - 2
    assert module_0.do_algebra(['-', '-'], [1, 2, 3]) == -4              # 1 - 2 - 3

    # Longer chains
    assert module_0.do_algebra(['+', '*', '//', '-'], [10, 2, 3, 4, 5]) == 6  # 10 + 2*3//4 - 5
    assert module_0.do_algebra(['*', '*', '+'], [2, 2, 2, 10]) == 18          # 2*2*2 + 10

    # Zeros and single operand
    assert module_0.do_algebra(['+', '*'], [0, 5, 3]) == 15              # 0 + 5*3
    assert module_0.do_algebra([], [42]) == 42

    print("All tests passed!")


if __name__ == "__main__":
    test_do_algebra()

# Generated at 2026-11-01 19:49:28.252850
# Unit test for function do_algebra
def test_do_algebra():
    # Test addition
    assert module_0.do_algebra(['+'], [3, 4]) == 7

    # Test subtraction
    assert module_0.do_algebra(['-'], [10, 3]) == 7

    # Test multiplication
    assert module_0.do_algebra(['*'], [3, 4]) == 12

    # Test integer division
    assert module_0.do_algebra(['//'], [10, 3]) == 3

    # Test modulo
    assert module_0.do_algebra(['%'], [10, 3]) == 1

    # Test operator precedence: multiplication before addition
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Test operator precedence: division before subtraction
    assert module_0.do_algebra(['-', '//'], [10, 6, 2]) == 7

    # Test multiple operators of same precedence (left-to-right)
    assert module_0.do_algebra(['+', '-', '+'], [1, 2, 3, 4]) == 4

    # Test chained multiplication and division
    assert module_0.do_algebra(['*', '//'], [8, 3, 4]) == 6

    # Test multi-digit operands
    assert module_0.do_algebra(['+', '*'], [12, 3, 45]) == 147

    # Test modulo with multiplication precedence
    assert module_0.do_algebra(['%', '*'], [10, 4, 2]) == 2

    # Test single operand with no operators
    assert module_0.do_algebra([], [42]) == 42

    # Test negative result
    assert module_0.do_algebra(['-'], [3, 10]) == -7

    # Test complex mixed expression
    assert module_0.do_algebra(['+', '*', '-'], [5, 2, 3, 1]) == 10

    print("All tests passed!")


test_do_algebra()

# Generated at 2026-11-01 19:49:41.353810
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8
    assert module_0.do_algebra(['+'], [5, 10]) == 15
    assert module_0.do_algebra(['-', '*'], [10, 5, 2]) == 0
    assert module_0.do_algebra(['**'], [2, 3]) == 8
    assert module_0.do_algebra(['*', '+', '//'], [4, 5, 6, 4]) == 26
    assert module_0.do_algebra(['-'], [100, 55]) == 45
    print("All tests passed!")

if __name__ == "__main__":
    test_do_algebra()