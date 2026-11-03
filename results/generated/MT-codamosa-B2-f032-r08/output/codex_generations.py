

# Generated at 2026-11-03 01:54:55.286321
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: 2x + 3 -> zero at x = -1.5
    xs = [3, 2]
    assert abs(poly(xs, module_0.find_zero(xs))) < 1e-6

    # Quadratic polynomial: x^2 - 4 -> zero at x = 2 (or -2)
    xs = [-4, 0, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6
    assert abs(abs(zero) - 2.0) < 1e-6

    # Cubic polynomial: x^3 - 8 -> zero at x = 2
    xs = [-8, 0, 0, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6
    assert abs(zero - 2.0) < 1e-5

    # Polynomial: x - 1 -> zero at x = 1
    xs = [-1, 1]
    assert abs(module_0.find_zero(xs) - 1.0) < 1e-6

    # Polynomial: 5x - 10 -> zero at x = 2
    xs = [-10, 5]
    assert abs(module_0.find_zero(xs) - 2.0) < 1e-6

    # Polynomial with negative leading coefficient: -x + 4 -> zero at x = 4
    xs = [4, -1]
    assert abs(module_0.find_zero(xs) - 4.0) < 1e-6

    # Larger interval expansion: 1000x - 1 -> zero at x = 0.001
    xs = [-1, 1000]
    assert abs(poly(xs, module_0.find_zero(xs))) < 1e-6

    # Verify returned value is a float
    xs = [2, 1]
    assert isinstance(module_0.find_zero(xs), float)

    # Polynomial: x^2 + 3x - 10 -> roots at x = 2 and x = -5
    xs = [-10, 3, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6

# Generated at 2026-11-03 01:56:37.483905
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: 1 + 2x = 0 has root x = -0.5
    assert abs(module_0.find_zero([1, 2]) - (-0.5)) < 1e-6

    # poly evaluated at the returned zero should be close to zero
    assert abs(poly([1, 2], module_0.find_zero([1, 2]))) < 1e-6

    # Cubic: -6 + 11x - 6x^2 + x^3 has roots 1, 2, 3
    assert abs(poly([-6, 11, -6, 1], module_0.find_zero([-6, 11, -6, 1]))) < 1e-6

    # Quadratic: -4 + x^2 has roots -2 and 2
    assert abs(poly([-4, 0, 1], module_0.find_zero([-4, 0, 1]))) < 1e-6

    # Result should be a float
    assert isinstance(module_0.find_zero([1, 2]), float)

# Generated at 2026-11-03 01:57:13.526708
# Unit test for function poly
def test_poly():
    # Constant polynomial
    assert module_0.poly([5], 0) == 5
    assert module_0.poly([5], 100.0) == 5

    # Linear polynomial: 2x + 3
    assert math.isclose(module_0.poly([3, 2], 0), 3)
    assert math.isclose(module_0.poly([3, 2], 1), 5)
    assert math.isclose(module_0.poly([3, 2], -2), -1)

    # Quadratic polynomial: 1 + 2x + 3x^2
    assert math.isclose(module_0.poly([1, 2, 3], 0), 1)
    assert math.isclose(module_0.poly([1, 2, 3], 2), 1 + 2 * 2 + 3 * 4)
    assert math.isclose(module_0.poly([1, 2, 3], -1), 1 - 2 + 3)

    # Cubic polynomial with known root: x^3 - 6x^2 + 11x - 6 = (x-1)(x-2)(x-3)
    xs = [-6, 11, -6, 1]
    assert math.isclose(module_0.poly(xs, 1), 0)
    assert math.isclose(module_0.poly(xs, 2), 0)
    assert math.isclose(module_0.poly(xs, 3), 0)
    assert math.isclose(module_0.poly(xs, 0.5), 0.5 ** 3 - 6 * 0.25 + 11 * 0.5 - 6)

    # Negative x values
    assert math.isclose(module_0.poly([0, 1], -2), -2)
    assert math.isclose(module_0.poly([0, 0, 1], -3), 9)

    # Empty coefficient list evaluates to 0
    assert module_0.poly([], 42.0) == 0

    # Fractional x
    assert math.isclose(module_0.poly([1, 1], 0.5), 1.5)


# Unit test for function find_zero
def test_find_zero():
    # Zero of 2x + 1 is -0.5
    assert math.isclose(find_zero([1, 2]), -0.5, abs_tol=1e-8)

    # Zero of -6 + 11x - 6x^2 + x^3 = (x-1)(x-2)(x-3), bracketing finds one root
    root = find_zero([-6, 11, -6, 1])
    assert any(math.isclose(root, r, abs_tol=1e-6) for r in (1.0, 2.0, 3.0))

    # Zero of x is 0
    assert math.isclose(find_zero([0, 1]), 0.0, abs_tol=1e-8)


if __name__ == "__main__":
    test_poly()
    test_find_zero()
    print("All tests passed.")

# Generated at 2026-11-03 01:58:14.772103
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: 2x + 3, root at x = -1.5
    xs1 = [3, 2]
    root1 = module_0.find_zero(xs1)
    assert abs(poly(xs1, root1)) < 1e-6

    # Quadratic polynomial: x^2 - 4, roots at x = -2 and x = 2
    xs2 = [-4, 0, 1]
    root2 = module_0.find_zero(xs2)
    assert abs(poly(xs2, root2)) < 1e-6

    # Cubic polynomial: x^3 - 1, root at x = 1
    xs3 = [-1, 0, 0, 1]
    root3 = module_0.find_zero(xs3)
    assert abs(poly(xs3, root3)) < 1e-6

    # Cubic polynomial: (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6
    xs4 = [-6, 11, -6, 1]
    root4 = module_0.find_zero(xs4)
    assert abs(poly(xs4, root4)) < 1e-6

    # Polynomial with no sign change within [-1, 1] initially:
    # 5x + 1, root at x = -0.2
    xs5 = [1, 5]
    root5 = module_0.find_zero(xs5)
    assert abs(poly(xs5, root5)) < 1e-6

    # Verify the found root brackets correctly: sign of polynomial near root ~ 0
    assert poly(xs1, root1 - 0.1) * poly(xs1, root1 + 0.1) <= 0

    print("All tests passed for find_zero!")


test_find_zero()

# Generated at 2026-11-03 01:59:17.645420
# Unit test for function poly
def test_poly():
    assert module_0.poly([1, 2, 3], 2) == 17.0
    assert module_0.poly([1, 2], 3) == 7.0
    assert module_0.poly([5], 10) == 5.0
    assert module_0.poly([1, 2, 3, 4], 0) == 1.0
    assert module_0.poly([-1, 1], 1) == 0.0
    assert module_0.poly([2, -6, 2], -3) == 38.0
    assert module_0.poly([0, 0, 1], 5) == 25.0
    assert module_0.poly([1.5, 2.5], 2.0) == 6.5
    assert module_0.poly([], 1) == 0
    assert module_0.poly([-3, 0, 2], 2) == 5.0


# Unit test for function find_zero
def test_find_zero():
    assert abs(find_zero([-6, 11, -6, 1]) - 1.0) < 1e-4        # roots 1, 2, 3
    assert abs(find_zero([-4, 1]) - 4.0) < 1e-4                # root 4
    assert abs(find_zero([2, -3]) - (2 / 3)) < 1e-4            # root 2/3
    assert abs(find_zero([-1, 0, 1]) - 1.0) < 1e-4             # roots -1, 1
    assert abs(module_0.poly([find_zero([1, 0, -2])], find_zero([1, 0, -2]))) < 1e-4  # root of x^2 - 2
    assert abs(find_zero([5, -5]) - 1.0) < 1e-4                # root 1
    assert abs(find_zero([0, 1]) - 0.0) < 1e-4                 # root 0
    assert abs(find_zero([-10, 0, 1]) - math.sqrt(10)) < 1e-4  # root sqrt(10)

# Generated at 2026-11-03 02:00:17.695320
# Unit test for function find_zero
def test_find_zero():
    # Test 1: linear polynomial 2x + 3 = 0 -> root at x = -1.5
    result = module_0.find_zero([3, 2])
    assert math.isclose(poly([3, 2], result), 0, abs_tol=1e-6), \
        f"Expected poly value near 0, got {poly([3, 2], result)}"
    assert math.isclose(result, -1.5, abs_tol=1e-6), \
        f"Expected root near -1.5, got {result}"

    # Test 2: linear polynomial x - 4 = 0 -> root at x = 4.0
    result = module_0.find_zero([-4, 1])
    assert math.isclose(result, 4.0, abs_tol=1e-6), \
        f"Expected root near 4.0, got {result}"

    # Test 3: quadratic (x - 1)(x - 2) = x^2 - 3x + 2 -> root at 1.0 or 2.0
    result = module_0.find_zero([2, -3, 1])
    assert math.isclose(poly([2, -3, 1], result), 0, abs_tol=1e-6), \
        f"Expected poly value near 0, got {poly([2, -3, 1], result)}"

    # Test 4: quadratic with root at 0.5: 2x - 1 = 0
    result = module_0.find_zero([-1, 2])
    assert math.isclose(result, 0.5, abs_tol=1e-6), \
        f"Expected root near 0.5, got {result}"

    # Test 5: polynomial with larger coefficients: -6 + 11x - 6x^2
    # roots at 1, 2, 3
    result = module_0.find_zero([-6, 11, -6])
    assert math.isclose(poly([-6, 11, -6], result), 0, abs_tol=1e-6), \
        f"Expected poly value near 0, got {poly([-6, 11, -6], result)}"

    # Test 6: cubic x^3 - 8 = 0 -> root at x = 2.0
    result = module_0.find_zero([-8, 0, 0, 1])
    assert math.isclose(result, 2.0, abs_tol=1e-6), \
        f"Expected root near 2.0, got {result}"

    # Test 7: result should be a float
    result = module_0.find_zero([1, 1])
    assert isinstance(result, float), f"Expected float, got {type(result)}"

    # Test 8: symmetric check around known root x = 0.25 for 4x - 1
    result = module_0.find_zero([-1, 4])
    assert abs(result - 0.25) < 1e-8, \
        f"Expected root near 0.25, got {result}"

    print("All tests passed!")


if __name__ == "__main__":
    test_find_zero()

# Generated at 2026-11-03 02:01:27.682708
# Unit test for function find_zero
def test_find_zero():
    # Linear: 1 + 2x = 0 -> x = -0.5
    assert abs(module_0.find_zero([1, 2]) + 0.5) < 1e-6
    # Linear: 5 + 4x = 0 -> x = -1.25 (requires interval doubling)
    assert abs(module_0.find_zero([5, 4]) + 1.25) < 1e-6
    # Linear: -3 + x = 0 -> x = 3 (zero found outside initial [-1, 1])
    assert abs(module_0.find_zero([-3, 1]) - 3.0) < 1e-6
    # Cubic: (x-1)(x-2)(x-3), bisection converges to root at x = 1
    assert abs(module_0.find_zero([-6, 11, -6, 1]) - 1.0) < 1e-6
    # Quadratic: (x-1)(x-2), bisection converges to root at x = 1
    assert abs(module_0.find_zero([2, -3, 1]) - 1.0) < 1e-6