

# Generated at 2026-11-02 14:20:21.487184
# Unit test for function derivative
def test_derivative():
    # Polynomial 3 + 1*x + 2*x^2 + 4*x^3 + 5*x^4
    # Derivative: 1 + 4*x + 12*x^2 + 20*x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

    # Polynomial 1 + 2*x + 3*x^2
    # Derivative: 2 + 6*x
    assert module_0.derivative([1, 2, 3]) == [2, 6]

    # Constant polynomial has zero-length derivative
    assert module_0.derivative([5]) == []

    # Empty polynomial
    assert module_0.derivative([]) == []

    # Zero coefficients
    assert module_0.derivative([0, 0, 0]) == [0, 0]

    # Negative coefficients
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]

    # Linear polynomial: derivative is constant
    assert module_0.derivative([4, 7]) == [7]

    # Result length is always one less than input (for non-empty input)
    xs = [1, 2, 3, 4, 5, 6]
    assert len(module_0.derivative(xs)) == len(xs) - 1

    print("All derivative tests passed!")


if __name__ == "__main__":
    test_derivative()

# Generated at 2026-11-02 14:21:16.569740
# Unit test for function derivative
def test_derivative():
    # Polynomial 3 + x + 2x^2 + 4x^3 + 5x^4 -> 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # Polynomial 1 + 2x + 3x^2 -> 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Constant polynomial -> derivative is empty
    assert module_0.derivative([4]) == []
    # Zero polynomial of higher degree -> zeros
    assert module_0.derivative([0, 0, 0]) == [0, 0]
    # Negative coefficients
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]

# Generated at 2026-11-02 14:22:25.203632
# Unit test for function derivative
def test_derivative():
    # nonce:550d7b47
    # Polynomial 3 + x + 2x^2 + 4x^3 + 5x^4 -> derivative 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # Polynomial 1 + 2x + 3x^2 -> derivative 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Constant polynomial -> derivative is empty (constant term drops off)
    assert module_0.derivative([5]) == []
    # All-zero coefficients
    assert module_0.derivative([0, 0, 0]) == [0, 0]
    # Linear polynomial with zero slope term -> derivative is [0]
    assert module_0.derivative([7, 0]) == [0]
    # Negative coefficients
    assert module_0.derivative([-3, -1, -2]) == [-1, -4]
    # Float coefficients
    assert module_0.derivative([1.5, 2.5]) == [2.5]
    # Empty input
    assert module_0.derivative([]) == []

# Generated at 2026-11-02 14:24:33.374908
# Unit test for function derivative
def test_derivative():
    # nonce:34c9a3e5
    # Standard polynomial: 3 + 1*x + 2*x^2 + 4*x^3 + 5*x^4 -> 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # 1 + 2x + 3x^2 -> 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Empty polynomial -> empty derivative
    assert module_0.derivative([]) == []
    # Constant polynomial -> derivative is empty (zero polynomial)
    assert module_0.derivative([5]) == []
    assert module_0.derivative([7]) == []
    # Zero coefficients preserved
    assert module_0.derivative([0, 0, 0]) == [0, 0]
    assert module_0.derivative([1, 0, 3]) == [0, 6]
    # Negative coefficients
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]
    # Float coefficients
    assert module_0.derivative([2.5, -1.5, 4.0]) == [-1.5, 8.0]
    # Linear polynomial: c0 + c1*x -> [c1]
    assert module_0.derivative([10, 3]) == [3]

    print("All derivative tests passed!")


if __name__ == "__main__":
    test_derivative()

# Generated at 2026-11-02 14:27:42.261089
# Unit test for function derivative
def test_derivative():
    # Basic polynomial: 3 + 1x + 2x^2 + 4x^3 + 5x^4 -> 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # Polynomial: 1 + 2x + 3x^2 -> 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Polynomial: 3 + 2x + 1x^2 -> 2 + 2x
    assert module_0.derivative([3, 2, 1]) == [2, 2]
    # Constant polynomial has derivative []
    assert module_0.derivative([5]) == []
    # Empty input
    assert module_0.derivative([]) == []
    # Zero coefficients are preserved
    assert module_0.derivative([0, 0, 0]) == [0, 0]
    # Negative coefficients
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]
    # Single linear term: 4x -> 4
    assert module_0.derivative([0, 4]) == [4]
    # Long polynomial with mixed values
    assert module_0.derivative([1, 0, 0, 7]) == [0, 0, 21]