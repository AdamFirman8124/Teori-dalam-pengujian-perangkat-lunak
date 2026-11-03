

# Generated at 2026-11-02 12:07:37.272751
# Unit test for function derivative
def test_derivative():
    # Test basic polynomial: 3 + x + 2x^2 + 4x^3 + 5x^4 -> 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

    # Test simple polynomial: 1 + 2x + 3x^2 -> 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]

    # Test linear polynomial: 2 + 4x -> 4
    assert module_0.derivative([2, 4]) == [4]

    # Test constant polynomial -> empty list (derivative of constant is 0)
    assert module_0.derivative([5]) == []

    # Test empty list -> empty list
    assert module_0.derivative([]) == []

    # Test polynomial with all zero constant term: 0 + 0x + 0x^2 -> 0 + 0x
    assert module_0.derivative([0, 0, 0]) == [0, 0]

    # Test negative coefficients: -1 + 3x - 2x^2 -> 3 - 4x
    assert module_0.derivative([-1, 3, -2]) == [3, -4]

    # Test floating point coefficients: 1.5 + 2.0x -> 2.0
    assert module_0.derivative([1.5, 2.0]) == [2.0]

    # Test single-element list with zero
    assert module_0.derivative([0]) == []

    # Test longer polynomial: 0 + 0x + 1x^2 + 0x^3 + 3x^4 -> 0 + 2x + 0x^2 + 12x^3
    assert module_0.derivative([0, 0, 1, 0, 3]) == [0, 2, 0, 12]

# Generated at 2026-11-02 12:08:52.098563
# Unit test for function derivative
def test_derivative():
    # Standard polynomial: 3 + x + 2x^2 + 4x^3 + 5x^4 -> 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # 1 + 2x + 3x^2 -> 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Floats: 3.5 + 4.5x -> 4.5
    assert module_0.derivative([3.5, 4.5]) == [4.5]
    # 1.5 + 2.5x + 3.5x^2 -> 2.5 + 7x
    assert module_0.derivative([1.5, 2.5, 3.5]) == [2.5, 7.0]
    # Single constant -> derivative is empty
    assert module_0.derivative([5]) == []
    assert module_0.derivative([7]) == []
    # Empty input -> empty output
    assert module_0.derivative([]) == []
    # All zero coefficients
    assert module_0.derivative([0, 0, 0, 0]) == [0, 0, 0]
    # Negative coefficients: -1 - 2x - 3x^2 - 4x^3 -> -2 - 6x - 12x^2
    assert module_0.derivative([-1, -2, -3, -4]) == [-2, -6, -12]
    # Leading zero coefficient: 0 + 1x + 0x^2 + 2x^3 -> 1 + 0x + 6x^2
    assert module_0.derivative([0, 1, 0, 2]) == [1, 0, 6]
    # Large values
    assert module_0.derivative([10**6, 10**6, 10**6]) == [10**6, 2 * 10**6]

# Generated at 2026-11-02 12:10:36.234726
# Unit test for function derivative
def test_derivative():
    # Standard polynomial: 3 + 1*x + 2*x^2 + 4*x^3 + 5*x^4
    # Derivative: 1 + 4*x + 12*x^2 + 20*x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

    # Polynomial: 1 + 2*x + 3*x^2 -> derivative: 2 + 6*x
    assert module_0.derivative([1, 2, 3]) == [2, 6]

    # Single constant term -> derivative is empty
    assert module_0.derivative([5]) == []

    # Empty list -> derivative is empty
    assert module_0.derivative([]) == []

    # Polynomial with zero coefficients: 0 + 0*x + 1*x^2 -> derivative: 0 + 2*x
    assert module_0.derivative([0, 0, 1]) == [0, 2]

    # Negative coefficients: -1 - 2*x -> derivative: -2
    assert module_0.derivative([-1, -2]) == [-2]

    # Linear polynomial: 4 + 7*x -> derivative: 7
    assert module_0.derivative([4, 7]) == [7]

    # Higher-degree polynomial: 1 + 1*x + 1*x^2 + 1*x^3 -> derivative: 1 + 2*x + 3*x^2
    assert module_0.derivative([1, 1, 1, 1]) == [1, 2, 3]

    # Result length should be one less than input (for non-empty input)
    assert len(module_0.derivative([10, 20, 30, 40])) == 3

    print("All tests passed!")


if __name__ == "__main__":
    test_derivative()

# Generated at 2026-11-02 12:12:43.140603
# Unit test for function derivative
def test_derivative():
    # Standard polynomial: 3 + 1x + 2x^2 + 4x^3 + 5x^4 -> 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # 1 + 2x + 3x^2 -> 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Single constant: derivative is empty
    assert module_0.derivative([5]) == []
    # Empty input: derivative is empty
    assert module_0.derivative([]) == []
    # Zero coefficients
    assert module_0.derivative([0, 0, 0]) == [0, 0]
    # Negative coefficients: 2 - 3x + 4x^2 -> -3 + 8x
    assert module_0.derivative([2, -3, 4]) == [-3, 8]
    # Constant term ignored: c0 * 0 dropped by slicing
    assert module_0.derivative([7, 0, 1]) == [0, 2]
    print("All tests passed!")


test_derivative()

# Generated at 2026-11-02 12:13:44.056488
# Unit test for function derivative
def test_derivative():
    # Polynomial: 3 + 1*x + 2*x^2 + 4*x^3 + 5*x^4 -> derivative: 1 + 4*x + 12*x^2 + 20*x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # Polynomial: 1 + 2*x + 3*x^2 -> derivative: 2 + 6*x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Empty polynomial has empty derivative
    assert module_0.derivative([]) == []
    # Constant polynomial has zero module_0.derivative(empty coefficient list)
    assert module_0.derivative([5]) == []
    # Zero coefficients are preserved
    assert module_0.derivative([0, 0, 0]) == [0, 0]
    # Negative coefficients handled correctly
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]
    # Single linear term: 4*x -> derivative 4
    assert module_0.derivative([0, 4]) == [4]