

# Generated at 2026-11-02 09:20:39.339396
# Unit test for function poly
def test_poly():
# nonce:abf2e89d
    # Constant polynomial
    assert module_0.poly([5], 3) == 5
    assert module_0.poly([0], 10) == 0
    # Empty coefficient list evaluates to 0
    assert module_0.poly([], 4) == 0
    # Linear polynomial
    assert module_0.poly([1, 2], 3) == 7
    assert module_0.poly([-2, 1], 2) == 0
    # Quadratic polynomial
    assert module_0.poly([1, 2, 3], 2) == 17
    assert module_0.poly([1, 2, 3], -2) == 9
    # Evaluation at zero returns the constant term
    assert module_0.poly([1, 2, 3], 0) == 1
    # Negative coefficients
    assert module_0.poly([1, -2, 3], -2) == 17
    # Floating point coefficients and inputs
    assert abs(module_0.poly([0.5, 0.25, 1.5], 2.0) - 7.0) < 1e-9
    # Higher degree term only
    assert module_0.poly([0, 0, 0, 1], 2) == 8


# Unit test for function find_zero
def test_find_zero():
    # Linear: 2x - 4 = 0 -> x = 2
    assert abs(find_zero([-4, 2]) - 2.0) < 1e-6
    # Linear: 3 + x = 0 -> x = -3
    assert abs(find_zero([3, 1]) + 3.0) < 1e-6
    # Linear: 1 + 2x = 0 -> x = -0.5
    assert abs(find_zero([1, 2]) + 0.5) < 1e-6
    # Cubic (x-1)(x-2)(x-3); boundary root at x = 1 is found
    assert abs(find_zero([-6, 11, -6, 1]) - 1.0) < 1e-6
    # Returned value should be (near) an actual root
    for coeffs in [[1, 2], [3, 1], [-6, 11, -6, 1]]:
        assert abs(module_0.poly(coeffs, find_zero(coeffs))) < 1e-6

# Generated at 2026-11-02 09:22:39.146367
# Unit test for function find_zero
def test_find_zero():
    # Linear: x + 2 = 0 -> root at -0.5
    xs = [1, 2]
    result = module_0.find_zero(xs)
    assert isinstance(result, float)
    assert abs(poly(xs, result)) < 1e-8
    assert abs(result - (-0.5)) < 1e-6

    # Linear: 1 - 2x = 0 -> root at 0.5
    xs = [1, -2]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8
    assert abs(result - 0.5) < 1e-6

    # Linear: 5 + 4x = 0 -> root at -1.25 (requires interval expansion)
    xs = [5, 4]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8
    assert abs(result - (-1.25)) < 1e-6

    # Cubic: (x - 1)(x - 2)(x - 3) -> converges to root at x = 1
    xs = [-6, 11, -6, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6
    assert abs(result - 1.0) < 1e-6

    # Quadratic: x^2 - 4 -> root at -2 (requires interval expansion)
    xs = [-4, 0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8
    assert abs(result - (-2.0)) < 1e-6

    # Quadratic: x^2 - 1 -> root at boundary x = -1
    xs = [-1, 0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8

    # Cubic: x^3 - 10 -> root at 10^(1/3), requires multiple expansions
    xs = [-10, 0, 0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8
    assert abs(result - math.pow(10, 1.0 / 3.0)) < 1e-6

    # Zero polynomial: every point is a root
    xs = [0]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8


test_find_zero()

# Generated at 2026-11-02 09:24:57.724370
# Unit test for function poly
def test_poly():
    assert module_0.poly([1.0, 2.0], 0.0) == 1.0
    assert module_0.poly([-6.0, 11.0, -6.0, 1.0], -1.0) == -24.0
    assert module_0.poly([], 5.0) == 0.0
    assert module_0.poly([3.0], 2.0) == 3.0
    assert module_0.poly([1.0, 0.0, 1.0], 2.0) == 5.0
    assert abs(module_0.poly([1.0, 1.0], 1.0) - 2.0) < 1e-9
    assert abs(module_0.poly([0.5, -2.0, 1.0], 3.0) - 3.5) < 1e-9
    assert module_0.poly([1.0, -1.0], 1.0) == 0.0


# Unit test for function find_zero
def test_find_zero():
    assert abs(find_zero([1.0, 2.0]) - (-0.5)) < 1e-8
    assert abs(find_zero([-6.0, 11.0, -6.0, 1.0]) - ((1 + math.sqrt(3)) / 2)) < 1e-8
    assert abs(find_zero([-4.0, 1.0]) - 4.0) < 1e-8
    assert abs(find_zero([5.0, 3.0, -5.0]) - 0.778539) < 1e-4
    assert abs(find_zero([1.0, -1.0]) - 1.0) < 1e-8
    assert abs(module_0.poly(find_zero([-6.0, 11.0, -6.0, 1.0]),
                    find_zero([-6.0, 11.0, -6.0, 1.0]))) < 1e-8


if __name__ == "__main__":
    test_poly()
    test_find_zero()
    print("All tests passed!")

# Generated at 2026-11-02 09:27:27.402887
# Unit test for function find_zero
def test_find_zero():
    # nonce:11efd7f2
    # Linear: f(x) = 1 + 2x, zero at x = -0.5
    x = module_0.find_zero([1, 2])
    assert isinstance(x, float)
    assert abs(x - (-0.5)) < 1e-6
    assert abs(poly([1, 2], x)) < 1e-6

    # Linear: f(x) = -1 + x, zero at x = 1
    assert abs(module_0.find_zero([-1, 1]) - 1.0) < 1e-6

    # Linear: f(x) = 2 + x, zero at x = -2
    assert abs(module_0.find_zero([2, 1]) - (-2.0)) < 1e-6

    # Linear with large root, exercises the bracket-doubling loop:
    # f(x) = 100 + x, zero at x = -100
    assert abs(module_0.find_zero([100, 1]) - (-100.0)) < 1e-6

    # Cubic: f(x) = x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)
    xs = [-6, 11, -6, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6
    assert -4.0 <= x <= 4.0

    # Cubic: f(x) = x^3 + x^2 - 3x + 5, single real root between -3 and -2
    xs = [5, -3, 1, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6
    assert -4.0 <= x <= -1.0