

# Generated at 2026-11-01 21:43:45.936917
# Unit test for function derivative
def test_derivative():
    from solution import derivative

    # Test with a polynomial having multiple coefficients
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

    # Test with a simple linear polynomial
    assert module_0.derivative([1, 2, 3]) == [2, 6]

    # Test with two coefficients
    assert module_0.derivative([4, 7]) == [7]

    # Test with a single coefficient (constant) -> derivative is empty
    assert module_0.derivative([5]) == []

    # Test with an empty list
    assert module_0.derivative([]) == []

    # Test with negative coefficients
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]

    # Test with mixed positive/negative/zero coefficients
    assert module_0.derivative([0, -4, 0, 6, 1]) == [-4, 0, 18, 4]

    # Test with zero polynomial coefficients
    assert module_0.derivative([0, 0, 0]) == [0, 0]

    print("All tests passed!")

# Generated at 2026-11-01 21:44:09.046856
# Unit test for function derivative
def test_derivative():
    # Standard polynomial: 3 + 1x + 2x^2 + 4x^3 + 5x^4 -> 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]

    # Linear polynomial: 2 + 3x -> 3
    assert module_0.derivative([2, 3]) == [3]

    # Constant polynomial -> empty list (derivative is zero)
    assert module_0.derivative([5]) == []

    # Empty input list
    assert module_0.derivative([]) == []

    # Single coefficient zero
    assert module_0.derivative([0]) == []

    # Negative coefficients: -1 + -2x + -3x^2 -> -2 + -6x
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]

    # Zero constant term: 0 + 1x + 2x^2 -> 1 + 4x
    assert module_0.derivative([0, 1, 2]) == [1, 4]

    # Large coefficients
    assert module_0.derivative([1000000, 2000000]) == [2000000]

    # Floating point coefficients
    assert module_0.derivative([1.5, 2.5, 3.5]) == [2.5, 7.0]

    # Verify length: derivative of n coefficients has n-1 coefficients
    xs = [i for i in range(10)]
    assert len(module_0.derivative(xs)) == len(xs) - 1

    # Verify each element matches i * xs[i] shifted by one
    result = module_0.derivative(xs)
    expected = [i * x for i, x in enumerate(xs)][1:]
    assert result == expected

# Generated at 2026-11-01 21:44:47.682227
# Unit test for function derivative
def test_derivative():
    # Polynomial 3 + 1x + 2x^2 + 4x^3 + 5x^4 -> 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # Polynomial 1 + 2x + 3x^2 -> 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # Polynomial 3 + 2x + 1x^2 -> 2 + 2x
    assert module_0.derivative([3, 2, 1]) == [2, 2]
    # Empty polynomial
    assert module_0.derivative([]) == []
    # Single constant term -> derivative is empty
    assert module_0.derivative([5]) == []
    assert module_0.derivative([0]) == []
    # All zero coefficients
    assert module_0.derivative([0, 0, 0]) == [0, 0]
    # Negative coefficients
    assert module_0.derivative([-3, 2, -1]) == [2, -2]
    # Float coefficients
    assert module_0.derivative([1.5, 2.0, 3.0]) == [2.0, 6.0]
    # Two elements
    assert module_0.derivative([7, 4]) == [4]

# Generated at 2026-11-01 21:45:15.227728
# Unit test for function derivative
def test_derivative():
    # Standard polynomial cases (coefficients of increasing powers)
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    assert module_0.derivative([3, 2, 1]) == [2, 2]

    # Edge cases: single element and empty list
    assert module_0.derivative([5]) == []
    assert module_0.derivative([]) == []

    # Zero coefficients preserved at correct positions
    assert module_0.derivative([0, 0, 0, 0]) == [0, 0, 0]
    assert module_0.derivative([1, 0, 3, 0, 2, 7]) == [0, 6, 0, 8, 35]

    # Descending coefficients
    assert module_0.derivative([6, 5, 4, 3, 2, 1]) == [5, 8, 9, 8, 5]

    # Negative coefficients
    assert module_0.derivative([-1, -2, -3]) == [-2, -6]

    # Float coefficients
    assert module_0.derivative([2.5, 1.5, 3.0]) == [1.5, 6.0]

# Generated at 2026-11-01 21:45:45.128055
# Unit test for function derivative
def test_derivative():
    # derivative of 3 + 1x + 2x^2 + 4x^3 + 5x^4 is 1 + 4x + 12x^2 + 20x^3
    assert module_0.derivative([3, 1, 2, 4, 5]) == [1, 4, 12, 20]
    # derivative of 1 + 2x + 3x^2 is 2 + 6x
    assert module_0.derivative([1, 2, 3]) == [2, 6]
    # derivative of constant 5 is empty (dropped leading 0)
    assert module_0.derivative([5]) == []
    # derivative of empty polynomial is empty
    assert module_0.derivative([]) == []
    # derivative of 3 + 2x + 1x^2 is 2 + 2x
    assert module_0.derivative([3, 2, 1]) == [2, 2]
    # works with floats
    assert module_0.derivative([6.5, 2.0]) == [2.0]
    # derivative of linear polynomial ax + b is [a]
    assert module_0.derivative([-7, 4]) == [4]
    # longer polynomial check
    assert module_0.derivative([0, 0, 0, 7]) == [0, 0, 21]
    # result preserves numeric types
    result = module_0.derivative([1, 2, 3, 4])
    assert isinstance(result, list) and len(result) == 3