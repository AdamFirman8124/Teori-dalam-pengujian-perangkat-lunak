

# Generated at 2026-11-02 11:30:06.154425
# Unit test for function multiply
def test_multiply():
    # Basic positive numbers
    assert module_0.multiply(12, 3) == 6
    assert module_0.multiply(148, 412) == 16
    assert module_0.multiply(19, 28) == 72
    assert module_0.multiply(2020, 1851) == 0

    # Single digit numbers
    assert module_0.multiply(3, 4) == 12
    assert module_0.multiply(9, 9) == 81

    # Zero cases
    assert module_0.multiply(10, 5) == 0
    assert module_0.multiply(0, 7) == 0
    assert module_0.multiply(0, 0) == 0
    assert module_0.multiply(100, 100) == 0

    # Negative numbers (Python modulo: -n % 10 is positive, abs is a no-op there)
    assert module_0.multiply(-1, 3) == 27      # abs(-1 % 10) == 9
    assert module_0.multiply(-12, 3) == 24     # abs(-12 % 10) == 8
    assert module_0.multiply(4, -15) == 20     # abs(-15 % 10) == 5
    assert module_0.multiply(-14, -15) == 30   # abs(-14 % 10) == 6, abs(-15 % 10) == 5

    # Floats
    assert module_0.multiply(2.5, 4) == 10.0   # abs(2.5 % 10) * abs(4 % 10)

    print("All tests passed!")


if __name__ == "__main__":
    test_multiply()

# Generated at 2026-11-02 11:32:48.133999
# Unit test for function multiply
def test_multiply():
    # Positive multi-digit numbers: product of last digits
    assert module_0.multiply(12, 33) == 6
    assert module_0.multiply(148, 412) == 16
    assert module_0.multiply(123, 456) == 18

    # Single digit numbers
    assert module_0.multiply(4, 5) == 20
    assert module_0.multiply(5, 5) == 25

    # Numbers ending in zero
    assert module_0.multiply(10, 20) == 0
    assert module_0.multiply(100, 7) == 0

    # Zero input
    assert module_0.multiply(0, 7) == 0
    assert module_0.multiply(0, 0) == 0

    # Negative numbers (Python modulo: -12 % 10 == 8, -33 % 10 == 7)
    assert module_0.multiply(-12, 33) == 24
    assert module_0.multiply(12, -33) == 14
    assert module_0.multiply(-12, -33) == 56

    # Large numbers
    assert module_0.multiply(999999, 888888) == 72

    print("test_multiply: all assertions passed")

# Generated at 2026-11-02 11:36:10.490191
# Unit test for function multiply
def test_multiply():
    # Positive numbers
    assert module_0.multiply(148, 412) == 16, "Expected 16 for module_0.multiply(148, 412)"
    assert module_0.multiply(19, 28) == 72, "Expected 72 for module_0.multiply(19, 28)"
    assert module_0.multiply(2020, 1851) == 0, "Expected 0 for module_0.multiply(2020, 1851)"
    assert module_0.multiply(14, -15) == 20, "Expected 20 for module_0.multiply(14, -15)"

    # Single digit numbers
    assert module_0.multiply(3, 4) == 12, "Expected 12 for module_0.multiply(3, 4)"
    assert module_0.multiply(0, 5) == 0, "Expected 0 for module_0.multiply(0, 5)"
    assert module_0.multiply(5, 0) == 0, "Expected 0 for module_0.multiply(5, 0)"
    assert module_0.multiply(0, 0) == 0, "Expected 0 for module_0.multiply(0, 0)"

    # Negative numbers
    assert module_0.multiply(-3, 4) == 12, "Expected 12 for module_0.multiply(-3, 4)"
    assert module_0.multiply(3, -4) == 12, "Expected 12 for module_0.multiply(3, -4)"
    assert module_0.multiply(-3, -4) == 12, "Expected 12 for module_0.multiply(-3, -4)"
    assert module_0.multiply(-1, -1) == 1, "Expected 1 for module_0.multiply(-1, -1)"

    # Numbers ending in zero
    assert module_0.multiply(10, 20) == 0, "Expected 0 for module_0.multiply(10, 20)"
    assert module_0.multiply(-10, 5) == 0, "Expected 0 for module_0.multiply(-10, 5)"

    # Large numbers
    assert module_0.multiply(123456, 789012) == 12, "Expected 12 for module_0.multiply(123456, 789012)"
    assert module_0.multiply(999999, 999999) == 81, "Expected 81 for module_0.multiply(999999, 999999)"

    # Negative numbers with last digit handling
    assert module_0.multiply(-148, 412) == 16, "Expected 16 for module_0.multiply(-148, 412)"
    assert module_0.multiply(148, -412) == 16, "Expected 16 for module_0.multiply(148, -412)"
    assert module_0.multiply(-148, -412) == 16, "Expected 16 for module_0.multiply(-148, -412)"

    print("All tests passed!")


if __name__ == "__main__":
    test_multiply()

# Generated at 2026-11-02 11:38:13.669176
# Unit test for function multiply
def test_multiply():
# nonce:8d7f0a9b
    # Test with positive multi-digit numbers
    assert module_0.multiply(123, 456) == 18, "Expected 3 * 6 = 18"
    assert module_0.multiply(12, 34) == 8, "Expected 2 * 4 = 8"

    # Test with single-digit numbers
    assert module_0.multiply(3, 4) == 12, "Expected 3 * 4 = 12"
    assert module_0.multiply(9, 9) == 81, "Expected 9 * 9 = 81"

    # Test with negative numbers
    assert module_0.multiply(-15, 27) == 35, "Expected 5 * 7 = 35"
    assert module_0.multiply(-7, -3) == 21, "Expected 7 * 3 = 21"

    # Test with zero
    assert module_0.multiply(0, 5) == 0, "Expected 0 * 5 = 0"
    assert module_0.multiply(0, 0) == 0, "Expected 0 * 0 = 0"

    # Test with numbers ending in zero
    assert module_0.multiply(10, 20) == 0, "Expected 0 * 0 = 0"
    assert module_0.multiply(100, 5) == 0, "Expected 0 * 5 = 0"

    # Test with large numbers
    assert module_0.multiply(123456, 789012) == 12, "Expected 6 * 2 = 12"

    print("All tests passed!")

if __name__ == "__main__":
    test_multiply()