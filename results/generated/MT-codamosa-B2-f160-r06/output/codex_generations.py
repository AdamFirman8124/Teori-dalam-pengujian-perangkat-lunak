

# Generated at 2026-11-01 20:42:07.527051
# Unit test for function do_algebra
def test_do_algebra():
    import random

    # Single operand, no operators -> returns the operand itself
    assert module_0.do_algebra([], [7]) == 7

    # Simple binary operations
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [2, 5]) == -3
    assert module_0.do_algebra(['*'], [4, 6]) == 24
    assert module_0.do_algebra(['//'], [7, 2]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Operator precedence: * binds tighter than +
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14   # 2 + 3*4

    # Left-to-right evaluation for same-precedence ops
    assert module_0.do_algebra(['-', '-'], [10, 3, 2]) == 5   # (10 - 3) - 2
    assert module_0.do_algebra(['//', '//'], [100, 5, 2]) == 10  # (100 // 5) // 2

    # Mixed chain respecting precedence
    assert module_0.do_algebra(['-', '+', '*'], [10, 2, 3, 4]) == 20  # 10 - 2 + 3*4

    # Multi-digit and negative operands
    assert module_0.do_algebra(['+'], [-2, 30]) == 28
    assert module_0.do_algebra(['*', '-'], [12, 34, 56]) == 12 * 34 - 56

    # Longer mixed expression
    assert module_0.do_algebra(['+', '*', '-', '**'], [2, 3, 4, 5, 2]) == 2 + 3 * 4 - 5 ** 2  # -7

    # Randomized cross-check against Python's own evaluation
    ops = ['+', '-', '*', '//']
    for _ in range(50):
        n = random.randint(1, 6)
        operand = [random.randint(1, 20) for _ in range(n + 1)]
        operator = [random.choice(ops) for _ in range(n)]
        expected = eval(str(operand[0]) + ''.join(
            o + str(v) for o, v in zip(operator, operand[1:])
        ))
        assert module_0.do_algebra(operator, operand) == expected

# Generated at 2026-11-01 20:42:43.574255
# Unit test for function do_algebra
def test_do_algebra():
    # Single operator tests
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    assert module_0.do_algebra(['*'], [3, 5]) == 15
    assert module_0.do_algebra(['//'], [10, 3]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Multiple operators
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 5  # 2 + 3*4 - 5 = 9? -> 2+12-5=9
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14          # 2 + 3*4 = 14
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10          # 2*3 + 4 = 10
    assert module_0.do_algebra(['-', '+', '*'], [6, 1, 2, 3]) == 11  # 6 - 1 + 2*3 = 11

    # Operator precedence respected (multiplication before addition)
    assert module_0.do_algebra(['+', '*', '*'], [1, 2, 3, 4]) == 25  # 1 + 2*3*4 = 25

    # Exponentiation and floor division combined
    assert module_0.do_algebra(['**', '//'], [2, 3, 4]) == 2         # 2**3 // 4 = 2

    # Negative results
    assert module_0.do_algebra(['-'], [3, 10]) == -7
    assert module_0.do_algebra(['-', '*'], [1, 2, 5]) == -9          # 1 - 2*5 = -9

    # Longer chain
    assert module_0.do_algebra(['+', '-', '*', '//'], [10, 2, 3, 4, 5]) == 3  # 10+2-3*4//5 = 10

    print("All test cases passed!")


test_do_algebra()

# Generated at 2026-11-01 20:43:40.197260
# Unit test for function do_algebra
def test_do_algebra():
    # Addition
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['+', '+'], [1, 2, 3]) == 6

    # Subtraction
    assert module_0.do_algebra(['-'], [5, 3]) == 2
    assert module_0.do_algebra(['-', '-'], [10, 4, 2]) == 4

    # Multiplication
    assert module_0.do_algebra(['*'], [4, 5]) == 20
    assert module_0.do_algebra(['*', '*'], [2, 3, 4]) == 24

    # Floor division
    assert module_0.do_algebra(['//'], [10, 3]) == 3
    assert module_0.do_algebra(['//', '//'], [100, 5, 2]) == 10

    # Exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8
    assert module_0.do_algebra(['**', '**'], [2, 2, 2]) == 16  # right-associative: 2**(2**2)

    # Operator precedence
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14        # 2 + 3*4
    assert module_0.do_algebra(['-', '+'], [2, 3, 4]) == 3         # 2 - 3 + 4 (left-to-right)
    assert module_0.do_algebra(['**', '*'], [2, 3, 4]) == 32       # (2**3) * 4
    assert module_0.do_algebra(['//', '*'], [10, 2, 3]) == 15      # (10//2) * 3
    assert module_0.do_algebra(['+', '*', '-', '//'], [3, 5, 2, 8, 3]) == 11  # 3 + 5*2 - 8//3

    # Negative operands
    assert module_0.do_algebra(['+'], [-2, 3]) == 1
    assert module_0.do_algebra(['*', '-'], [-2, 3, 4]) == -10      # -2*3 - 4
    assert module_0.do_algebra(['**'], [-2, 3]) == -8              # (-2)**3

    # Single operand (no operators)
    assert module_0.do_algebra([], [42]) == 42

    print("All tests passed!")


if __name__ == "__main__":
    test_do_algebra()

# Generated at 2026-11-01 20:44:28.633940
# Unit test for function do_algebra
def test_do_algebra():
# nonce:2ac40b02
    # Test addition
    assert module_0.do_algebra(['+'], [3, 5]) == 8

    # Test subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6

    # Test multiplication
    assert module_0.do_algebra(['*'], [6, 7]) == 42

    # Test floor division
    assert module_0.do_algebra(['//'], [10, 3]) == 3

    # Test modulo
    assert module_0.do_algebra(['%'], [10, 3]) == 1

    # Test exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Test operator precedence: multiplication before addition
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14  # 2 + 3*4

    # Test operator precedence: addition before multiplication result
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 10  # 2*3 + 4

    # Test mixed subtraction and addition (left-to-right)
    assert module_0.do_algebra(['-', '+'], [10, 4, 2]) == 8  # 10 - 4 + 2

    # Test multiple operators with precedence
    assert module_0.do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == -9  # 1 + 2 - 3*4

    # Test chained floor division and multiplication
    assert module_0.do_algebra(['//', '*'], [9, 2, 3]) == 12  # (9//2)*3

    # Test with negative result
    assert module_0.do_algebra(['-'], [3, 10]) == -7

    # Test with negative operands
    assert module_0.do_algebra(['+'], [-3, 5]) == 2
    assert module_0.do_algebra(['+', '-'], [-3, -2, -1]) == -4  # -3 + -2 - -1

    # Test single operand (no operators)
    assert module_0.do_algebra([], [42]) == 42

    # Test modulo with multiplication precedence
    assert module_0.do_algebra(['%', '*'], [10, 3, 2]) == 4  # 10 % (3*2)

    print("All tests passed!")

test_do_algebra()

# Generated at 2026-11-01 20:44:51.671998
# Unit test for function do_algebra
def test_do_algebra():
    # Test basic addition
    assert module_0.do_algebra(['+'], [3, 5]) == 8

    # Test basic subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6

    # Test basic multiplication
    assert module_0.do_algebra(['*'], [3, 4]) == 12

    # Test floor division
    assert module_0.do_algebra(['//'], [10, 3]) == 3

    # Test modulo
    assert module_0.do_algebra(['%'], [10, 3]) == 1

    # Test multiple operators
    assert module_0.do_algebra(['+', '-', '*'], [2, 3, 4, 5]) == 2 + 3 - 4 * 5  # -15

    # Test operator precedence (multiplication before addition)
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 2 + 3 * 4  # 14

    # Test negative result
    assert module_0.do_algebra(['-'], [3, 10]) == -7

    # Test single operand with no operators
    assert module_0.do_algebra([], [42]) == 42

    # Test complex expression with floor division
    assert module_0.do_algebra(['*', '+', '//'], [6, 7, 3, 2]) == 6 * 7 + 3 // 2  # 43

    # Test chain of additions
    assert module_0.do_algebra(['+', '+', '+'], [1, 2, 3, 4]) == 10

    # Test modulo with larger numbers
    assert module_0.do_algebra(['%'], [100, 7]) == 2

    # Test mixed division and subtraction
    assert module_0.do_algebra(['//', '-'], [20, 3, 2]) == 20 // 3 - 2  # 4

    # Test expression starting with negative operand
    assert module_0.do_algebra(['+'], [-5, 3]) == -2

    print("All tests passed!")


test_do_algebra()