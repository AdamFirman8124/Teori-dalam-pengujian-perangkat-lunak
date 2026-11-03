

# Generated at 2026-11-02 14:52:35.024913
# Unit test for function find_zero
def test_find_zero():
    # nonce:bb6288a5
    import random

    # Test case 1: Linear polynomial 2x + 1, zero at x = -0.5
    result = module_0.find_zero([2, 1])
    assert abs(poly([2, 1], result)) < 1e-8, f"Expected zero, got poly = {poly([2, 1], result)}"
    assert abs(result - (-0.5)) < 1e-6, f"Expected -0.5, got {result}"

    # Test case 2: Linear polynomial -6x + 12, zero at x = 2
    result = module_0.find_zero([-6, 12])
    assert abs(poly([-6, 12], result)) < 1e-8, f"Expected zero, got poly = {poly([-6, 12], result)}"
    assert abs(result - 2.0) < 1e-6, f"Expected 2.0, got {result}"

    # Test case 3: Quadratic polynomial x^2 - 4, zero at x = 2 (or -2)
    result = module_0.find_zero([1, 0, -4])
    assert abs(poly([1, 0, -4], result)) < 1e-8, f"Expected zero, got poly = {poly([1, 0, -4], result)}"
    assert abs(abs(result) - 2.0) < 1e-6, f"Expected ±2.0, got {result}"

    # Test case 4: Polynomial x^2 + x, zero at x = 0 (or -1)
    result = module_0.find_zero([1, 1, 0])
    assert abs(poly([1, 1, 0], result)) < 1e-8, f"Expected zero, got poly = {poly([1, 1, 0], result)}"

    # Test case 5: Polynomial x - 5, zero at x = 5
    result = module_0.find_zero([1, -5])
    assert abs(poly([1, -5], result)) < 1e-8, f"Expected zero, got poly = {poly([1, -5], result)}"
    assert abs(result - 5.0) < 1e-6, f"Expected 5.0, got {result}"

    # Randomized testing: verify that poly evaluated at returned value is near zero
    for _ in range(50):
        ncoeff = random.randint(1, 5)
        coeffs = [random.uniform(-10, 10) for _ in range(ncoeff)]
        coeffs[-1] = random.choice([1, -1])  # ensure nonzero leading coeff -> guaranteed sign change somewhere
        result = module_0.find_zero(coeffs)
        assert abs(poly(coeffs, result)) < 1e-6, (
            f"find_zero failed for coefficients {coeffs}: "
            f"poly({result}) = {poly(coeffs, result)}"
        )

    print("All test_find_zero tests passed!")


if __name__ == "__main__":
    test_find_zero()

# Generated at 2026-11-02 14:53:10.703936
# Unit test for function poly
def test_poly():
    # Constant polynomial
    assert module_0.poly([5], 0.0) == 5.0
    assert module_0.poly([5], 10.0) == 5.0

    # Linear polynomial: 2x + 3
    assert module_0.poly([3, 2], 0.0) == 3.0
    assert module_0.poly([3, 2], 1.0) == 5.0
    assert module_0.poly([3, 2], 2.0) == 7.0

    # Quadratic polynomial: 1 + 2x + 3x^2 at x=2 -> 1 + 4 + 12 = 17
    assert module_0.poly([1, 2, 3], 2.0) == 17.0

    # Cubic polynomial: 1 + 2x + 3x^2 + 4x^3 at x=1 -> 10
    assert module_0.poly([1, 2, 3, 4], 1.0) == 10.0

    # Zero coefficients
    assert module_0.poly([0, 0, 0], 5.0) == 0.0

    # Negative coefficients: -x^2 + 4 at x=2 -> 0
    assert module_0.poly([4, 0, -1], 2.0) == 0.0

    # Negative x value: 1 + x at x=-1 -> 0
    assert module_0.poly([1, 1], -1.0) == 0.0

    # Fractional x: 2x at x=0.5 -> 1
    assert module_0.poly([0, 2], 0.5) == 1.0

    # Floating point tolerance check
    assert math.isclose(module_0.poly([1, 2, 3], 1.5), 1 + 3 + 6.75)

    print("test_poly passed")


test_poly()

# Generated at 2026-11-02 14:54:40.648923
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: 1 + 2x = 0 -> root at -0.5
    assert abs(module_0.find_zero([1, 2]) - (-0.5)) < 1e-8

    # Linear polynomial: 1 - 2x = 0 -> root at 0.5
    assert abs(module_0.find_zero([1, -2]) - 0.5) < 1e-8

    # Root lies outside the initial [-1, 1] bracket: 3 + x = 0 -> root at -3
    root = module_0.find_zero([3, 1])
    assert abs(root - (-3.0)) < 1e-8
    assert abs(poly([3, 1], root)) < 1e-8

    # Cubic (x-1)(x-2)(x-3): poly(1) == 0 so bracketing stops immediately,
    # bisection converges to the root at x = 1
    xs = [-6, 11, -6, 1]
    root = module_0.find_zero(xs)
    assert abs(root - 1.0) < 1e-6

# Generated at 2026-11-02 14:55:32.808550
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: x + 2 = 0 -> root at -0.5
    assert abs(module_0.find_zero([1, 2]) - (-0.5)) < 1e-8

    # Linear polynomial: 2x - 4 = 0 -> root at 2.0
    assert abs(module_0.find_zero([2, -4]) - 2.0) < 1e-8

    # Linear polynomial: x - 3 = 0 -> root at 3.0
    assert abs(module_0.find_zero([-3, 1]) - 3.0) < 1e-8

    # Quadratic: x^2 - 4 = 0 -> verify returned point is a root
    xs = [-4, 0, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6

    # Cubic with roots 1, 2, 3: verify returned point is a root
    xs = [-6, 11, -6, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6

    # Cubic with triple root at 1: (x-1)^3 = -1 + 3x - 3x^2 + x^3
    assert abs(module_0.find_zero([-1, 3, -3, 1]) - 1.0) < 1e-6

    # Verify result is a root for a higher-degree polynomial
    # (x - 5)(x + 2)(x - 0.5) expanded with leading coefficient 1
    xs = [5.0, -26.5, 3.0, 1.0]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6

    print("All find_zero tests passed!")


if __name__ == "__main__":
    test_find_zero()

# Generated at 2026-11-02 14:56:13.585883
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: x - 2, root at x = 2
    assert abs(module_0.find_zero([-2, 1]) - 2) < 1e-5

    # Cubic with roots 1, 2, 3: x^3 - 6x^2 + 11x - 6
    xs = [-6, 11, -6, 1]
    zero = module_0.find_zero(xs)
    assert abs(zero - 1) < 1e-5
    assert abs(poly(xs, zero)) < 1e-6

    # Generic check: returned value is (near) a root of the polynomial
    xs = [-5, 2, -3, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6
# nonce:50563a57

# Generated at 2026-11-02 14:57:07.005366
# Unit test for function find_zero
def test_find_zero():
    # Linear: 1 + 2x = 0 -> root at x = -0.5
    xs = [1, 2]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6
    assert result == pytest.approx(-0.5, abs=1e-6)

    # Linear: 3 + x = 0 -> root at x = -3 (requires search range doubling)
    xs = [3, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6
    assert result == pytest.approx(-3, abs=1e-6)

    # Quadratic: x^2 - 4 -> roots at +/-2; bisection converges to -2
    xs = [-4, 0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6
    assert result == pytest.approx(-2, abs=1e-6)

    # Quadratic: 2 - 3x + x^2 = (x-1)(x-2) -> bisection converges to x = 1
    xs = [2, -3, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6
    assert result == pytest.approx(1, abs=1e-6)

    # Cubic: -1 + x^3 -> only real root at x = 1
    xs = [-1, 0, 0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6
    assert result == pytest.approx(1, abs=1e-6)

    # Round-trip: returned value should nearly zero the polynomial
    xs = [-5, 3, 7]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-4

# Generated at 2026-11-02 14:57:43.359311
# Unit test for function find_zero
def test_find_zero():
    # Test linear polynomial: 1 + 2x = 0 -> zero at x = -0.5
    xs = [1, 2]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8, f"Expected zero, got poly={poly(xs, result)}"
    assert abs(result - (-0.5)) < 1e-6, f"Expected -0.5, got {result}"

    # Test linear polynomial: 1 - 2x = 0 -> zero at x = 0.5
    xs = [1, -2]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8, f"Expected zero, got poly={poly(xs, result)}"
    assert abs(result - 0.5) < 1e-6, f"Expected 0.5, got {result}"

    # Test cubic polynomial: -6 + 11x - 6x^2 + x^3, roots at 1, 2, 3
    xs = [-6, 11, -6, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6, f"Expected zero, got poly={poly(xs, result)}"

    # Test quadratic polynomial: x^2 - 4, root at 2 (or -2)
    xs = [-4, 0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8, f"Expected zero, got poly={poly(xs, result)}"
    assert abs(abs(result) - 2) < 1e-6, f"Expected root near +/-2, got {result}"

    # Test polynomial with larger coefficients: 100 + 50x = 0 -> zero at x = -2
    xs = [100, 50]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6, f"Expected zero, got poly={poly(xs, result)}"
    assert abs(result - (-2)) < 1e-6, f"Expected -2, got {result}"

    # Test result is within a reasonable range (bisection guarantees begin bound)
    xs = [3, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-8, f"Expected zero, got poly={poly(xs, result)}"
    assert abs(result - (-3)) < 1e-6, f"Expected -3, got {result}"

    print("All tests passed!")


if __name__ == "__main__":
    test_find_zero()

# Generated at 2026-11-02 14:58:42.549833
# Unit test for function find_zero
def test_find_zero():
    # nonce:a095cb5d
    # Linear: 1 + 2x = 0  =>  x = -0.5
    root = module_0.find_zero([1, 2])
    assert abs(poly([1, 2], root)) < 1e-6
    assert abs(root - (-0.5)) < 1e-6

    # Linear: -4 + x = 0  =>  x = 4
    root = module_0.find_zero([-4, 1])
    assert abs(root - 4.0) < 1e-6

    # Quadratic: -1 + x^2 = 0  =>  roots at x = -1 or x = 1
    root = module_0.find_zero([-1, 0, 1])
    assert abs(poly([-1, 0, 1], root)) < 1e-6
    assert abs(abs(root) - 1.0) < 1e-6

    # Cubic: -6 + 11x - 6x^2 + x^3  =>  roots at 1, 2, 3
    coeffs = [-6, 11, -6, 1]
    root = module_0.find_zero(coeffs)
    assert abs(poly(coeffs, root)) < 1e-6

    # Higher-degree: 5x^3 - 2x + 1 has a real root; verify residual is ~0
    coeffs = [1, -2, 0, 5]
    root = module_0.find_zero(coeffs)
    assert abs(poly(coeffs, root)) < 1e-6


if __name__ == "__main__":
    test_find_zero()
    print("All tests passed.")

# Generated at 2026-11-02 14:59:27.439983
# Unit test for function find_zero
def test_find_zero():
    # nonce:8f85d254

    # Helper sanity checks for poly
    assert poly([1, 2], 0.5) == 2.0
    assert poly([3, -1], 2.0) == 1.0
    assert poly([1, 2, 3], 0.0) == 1.0
    assert poly([], 5.0) == 0

    # Linear polynomial: root of 1 + 2x is x = -0.5
    assert abs(module_0.find_zero([1, 2]) - (-0.5)) < 1e-8

    # Linear polynomial with root outside initial [-1, 1] range: 2 - x -> root = 2
    assert abs(module_0.find_zero([2, -1]) - 2.0) < 1e-8

    # Linear polynomial with fractional root: 5 + 3x -> root = -5/3
    assert abs(module_0.find_zero([5, 3]) - (-5.0 / 3.0)) < 1e-8

    # Cubic polynomial x^3 - 6x^2 + 11x - 6 has roots 1, 2, 3;
    # bisection from [-1, 1] converges to root at 1
    assert abs(module_0.find_zero([-6, 11, -6, 1]) - 1.0) < 1e-6

    # Root found should actually evaluate close to zero
    xs = [1, 2]
    assert abs(poly(xs, module_0.find_zero(xs))) < 1e-8

    xs = [-6, 11, -6, 1]
    assert abs(poly(xs, module_0.find_zero(xs))) < 1e-6

# Generated at 2026-11-02 15:00:17.545272
# Unit test for function find_zero
def test_find_zero():
    # Test linear polynomial: 1 + 2x = 0 -> x = -0.5
    xs = [1, 2]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6

    # Test quadratic polynomial: -6 + 11x - 6x^2 + x^3, roots at 1, 2, 3
    xs = [-6, 11, -6, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6

    # Test another simple linear: -4 + 2x = 0 -> x = 2
    xs = [-4, 2]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6

    # Test constant-free case: x (root at 0)
    xs = [0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6

    # Test polynomial with root near zero: x^2 - 1 (roots at -1, 1)
    xs = [-1, 0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6

    # Ensure returned value is a float
    assert isinstance(module_0.find_zero([1, 2]), float)