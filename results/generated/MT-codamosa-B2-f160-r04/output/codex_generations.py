

# Generated at 2026-11-02 09:33:05.011307
# Unit test for function do_algebra
def test_do_algebra():
    # Basic single operations
    assert module_0.do_algebra(['+'], [3, 4]) == 7
    assert module_0.do_algebra(['-'], [10, 3]) == 7
    assert module_0.do_algebra(['*'], [3, 4]) == 12
    assert module_0.do_algebra(['//'], [10, 3]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Mixed operations respecting operator precedence
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14          # 2 + 3*4
    assert module_0.do_algebra(['*', '-'], [2, 3, 4]) == 2           # 2*3 - 4
    assert module_0.do_algebra(['+', '-', '*'], [5, 3, 2, 4]) == 0   # 5+3-2*4
    assert module_0.do_algebra(['+', '*'], [1, 2, 3]) == 7           # 1 + 2*3

    # Multi-digit numbers
    assert module_0.do_algebra(['+'], [123, 456]) == 579
    assert module_0.do_algebra(['-', '*'], [100, 20, 3]) == 40       # 100 - 20*3

    # Exponentiation precedence
    assert module_0.do_algebra(['**', '+'], [2, 3, 1]) == 9          # 2**3 + 1
    assert module_0.do_algebra(['+', '**'], [1, 2, 3]) == 9          # 1 + 2**3

    # True division
    assert module_0.do_algebra(['/', '*'], [8, 2, 3]) == 12.0        # 8/2*3
    assert module_0.do_algebra(['/', '+'], [9, 3, 1]) == 4.0         # 9/3 + 1

    # Longer chains
    assert module_0.do_algebra(['+', '*', '-'], [1, 2, 3, 4]) == 3   # 1 + 2*3 - 4

    print("All tests passed!")


# nonce:218acb33
test_do_algebra()

# Generated at 2026-11-02 09:36:52.855703
# Unit test for function do_algebra
def test_do_algebra():
    # Test single addition
    assert module_0.do_algebra(['+'], [1, 2]) == 3

    # Test single subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6

    # Test single multiplication
    assert module_0.do_algebra(['*'], [3, 5]) == 15

    # Test single floor division
    assert module_0.do_algebra(['//'], [7, 2]) == 3

    # Test single exponentiation
    assert module_0.do_algebra(['**'], [2, 3]) == 8

    # Test multiple additions
    assert module_0.do_algebra(['+', '+'], [1, 2, 3]) == 6

    # Test mixed operators respecting precedence
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9   # 2 + 3*4 - 5
    assert module_0.do_algebra(['**', '*', '+'], [2, 3, 4, 5]) == 37 # 2**3 * 4 + 5
    assert module_0.do_algebra(['//', '*'], [7, 3, 4]) == 8          # 7//3 * 4

    # Test negative intermediate results
    assert module_0.do_algebra(['-', '+'], [1, 5, 2]) == -2          # 1 - 5 + 2

    # Test larger operand chain
    assert module_0.do_algebra(['+', '-', '*', '//'], [10, 2, 3, 4, 5]) == 14  # 10+2-3*4//5

# Generated at 2026-11-02 09:39:38.647367
# Unit test for function do_algebra
def test_do_algebra():
    # Basic addition
    assert module_0.do_algebra(['+'], [3, 4]) == 7
    assert module_0.do_algebra(['+'], [0, 0]) == 0
    assert module_0.do_algebra(['+'], [-1, 5]) == 4

    # Basic subtraction
    assert module_0.do_algebra(['-'], [10, 4]) == 6
    assert module_0.do_algebra(['-'], [4, 10]) == -6
    assert module_0.do_algebra(['-'], [5, -3]) == 8  # 5 - (-3)

    # Basic multiplication
    assert module_0.do_algebra(['*'], [3, 4]) == 12
    assert module_0.do_algebra(['*'], [0, 100]) == 0
    assert module_0.do_algebra(['*'], [-2, 6]) == -12

    # Integer (floor) division
    assert module_0.do_algebra(['//'], [9, 2]) == 4
    assert module_0.do_algebra(['//'], [100, 10]) == 10
    assert module_0.do_algebra(['//'], [7, 3]) == 2

    # Operator precedence: multiplication before addition
    assert module_0.do_algebra(['+', '*'], [2, 3, 4]) == 14  # 2 + 3*4
    assert module_0.do_algebra(['*', '+'], [2, 3, 4]) == 14  # 2*3 + 4

    # Subtraction before division
    assert module_0.do_algebra(['-', '//'], [20, 8, 3]) == 17  # 20 - 8//3

    # Multiple operators, mixed precedence
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 5  # 2 + 3*4 - 5
    assert module_0.do_algebra(['//', '*'], [12, 3, 4]) == 16       # 12//3 * 4

    # Longer chains
    assert module_0.do_algebra(['+', '+', '-'], [1, 2, 3, 4]) == 2  # 1+2+3-4
    assert module_0.do_algebra(['*', '*', '+'], [2, 3, 4, 5]) == 29 # 2*3*4+5

    # Negative operands
    assert module_0.do_algebra(['+'], [-5, -5]) == -10
    assert module_0.do_algebra(['*', '-'], [-2, -3, -4]) == -10  # (-2*-3) - -4 = 6+4

    # Single operand (no operators)
    assert module_0.do_algebra([], [42]) == 42

    print("All tests passed!")


if __name__ == "__main__":
    test_do_algebra()