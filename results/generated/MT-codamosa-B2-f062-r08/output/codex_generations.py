

# Generated at 2026-11-03 03:40:11.071681
# Unit test for function derivative
def test_derivative():
    # Standard polynomial: 3 + 1x + 2x^2 + 4x^3 + 5x^4
    # Derivative: 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

    # Simple quadratic: 1 + 2x + 3x^2 -> 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]

    # Another case: 3 + 2x + 1x^2 -> 2 + 2x
    assert module_0.derivative([3, 2, 1]) == [2, 2]

    # Float coefficients
    assert module_0.derivative([3.5, 1, 2, 4, 5]) == [1, 4, 12, 20]

    # Linear polynomial: 5 + 7x -> 7
    assert module_0.derivative([5, 7]) == [7]

    # Constant polynomial -> derivative is empty
    assert module_0.derivative([5]) == []

    # Empty input
    assert module_0.derivative([]) == []

    # Negative coefficients: -1 - 4x - 3x^2 -> -4 - 6x
    assert module_0.derivative([-1, -4, -3]) == [-4, -6]

    # Zero coefficients: 0 + 0x + 5x^2 -> 0 + 10x
    assert module_0.derivative([0, 0, 5]) == [0, 10]

    print("All tests passed!")


if __name__ == "__main__":
    test_derivative()

# Generated at 2026-11-03 03:41:22.341635
# Unit test for function derivative
def test_derivative():
# nonce:116fd280
    # Standard polynomial: 3 + x + 2x^2 + 4x^3 + 5x^4 -> 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # Simple polynomial: 1 + 2x + 3x^2 -> 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Constant polynomial -> derivative is empty
    assert module_0.derivative([5]) == []
    # Empty input
    assert module_0.derivative([]) == []
    # Zero coefficients
    assert module_0.derivative([0, 0, 0]) == [0, 0]
    # Negative coefficients
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]
    # Leading zero: 0 + 4x -> derivative [4]
    assert module_0.derivative([0, 4]) == [4]
    # Single-degree: 7x -> derivative [7]
    assert module_0.derivative([0, 7]) == [7]
    # Mixed positive/negative
    assert module_0.derivative([2, -3, 4, -5]) == [-3, 8, -15]

# Generated at 2026-11-03 03:42:19.910608
# Unit test for function derivative
def test_derivative():
    # nonce:257495ef
    # Basic cases: coefficients of polynomial, derivative computed term-by-term
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert module_0.derivative([1, 2, 3]) == [2, 6]

    # Single-element list (constant polynomial) -> derivative is empty
    assert module_0.derivative([5]) == []

    # Empty list -> empty derivative
    assert module_0.derivative([]) == []

    # Zero coefficients are preserved (scaled by index)
    assert module_0.derivative([0, 0, 0]) == [0, 0]

    # Negative coefficients
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]

    # Two-element list (linear polynomial) -> slope only
    assert module_0.derivative([7, 4]) == [4]

# Generated at 2026-11-03 03:43:09.878457
# Unit test for function derivative
def test_derivative():
    # Derivative of 3 + x + 2x^2 + 4x^3 + 5x^4 is 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # Derivative of 1 + 2x + 3x^2 is 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Derivative of 3 + 2x + x^2 is 2 + 2x
    assert module_0.derivative([3, 2, 1]) == [2, 2]
    # Derivative of a constant is an empty list
    assert module_0.derivative([5]) == []
    assert module_0.derivative([0]) == []
    # Derivative of an empty polynomial is an empty list
    assert module_0.derivative([]) == []
    # Derivative of 1 + x^2 is 2x
    assert module_0.derivative([1, 0, 1]) == [0, 2]
    # Derivative with negative coefficients
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]
    # Derivative of linear function
    assert module_0.derivative([0, 7]) == [7]
    print("All derivative tests passed!")


if __name__ == "__main__":
    test_derivative()

# Generated at 2026-11-03 03:44:24.513719
# Unit test for function derivative
def test_derivative():
    # Polynomial: 3 + 1*x + 2*x^2 + 4*x^3 + 5*x^4
    # Derivative: 1 + 4*x + 12*x^2 + 20*x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

    # Polynomial: 1 + 2*x + 3*x^2
    # Derivative: 2 + 6*x
    assert module_0.derivative([1, 2, 3]) == [2, 6]

    # Constant polynomial has derivative 0 (empty list of remaining coefficients)
    assert module_0.derivative([5]) == []

    # Empty polynomial
    assert module_0.derivative([]) == []

    # Polynomial with negative coefficients: -2 + 4*x
    # Derivative: 4
    assert module_0.derivative([-2, 4]) == [4]

    # Zero coefficients
    assert module_0.derivative([0, 0, 0]) == [0, 0]

    print("All tests passed!")


test_derivative()