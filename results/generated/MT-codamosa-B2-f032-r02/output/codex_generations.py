

# Generated at 2026-11-01 19:46:25.047684
# Unit test for function poly
def test_poly():# Test linear polynomial: 2x + 3
    assert module_0.poly([2.0, 3.0], 0.0) == 3.0
    assert module_0.poly([2.0, 3.0], 1.0) == 5.0
    assert module_0.poly([2.0, 3.0], -1.0) == 1.0

    # Test quadratic polynomial: x^2 - 2x + 1 = (x-1)^2
    assert math.isclose(module_0.poly([1.0, -2.0, 1.0], 1.0), 0.0, abs_tol=1e-9)
    assert math.isclose(module_0.poly([1.0, -2.0, 1.0], 2.0), 1.0, abs_tol=1e-9)
    assert math.isclose(module_0.poly([1.0, -2.0, 1.0], -1.0), 4.0, abs_tol=1e-9)

    # Test cubic polynomial: x^3 + x^2 + x + 1 at x = 2 -> 15
    assert math.isclose(module_0.poly([1.0, 1.0, 1.0, 1.0], 2.0), 15.0, abs_tol=1e-9)

    # Test constant polynomial
    assert module_0.poly([5.0], 100.0) == 5.0

    # Test with float coefficients
    assert math.isclose(module_0.poly([0.5, -0.25], 4.0), 1.0, abs_tol=1e-9)

    # Test with integer coefficient evaluated at 0
    assert module_0.poly([1, 2, 3], 0) == 1

    print("test_poly passed")


if __name__ == "__main__":
    test_poly()

# Generated at 2026-11-01 19:46:49.416762
# Unit test for function poly
def test_poly():
    # Linear polynomial: p(x) = 1 + 2x
    assert abs(module_0.poly([1, 2], 0) - 1) < 1e-9
    assert abs(module_0.poly([1, 2], 3) - 7) < 1e-9
    assert abs(module_0.poly([1, 2], -1.5) - (-2.0)) < 1e-9

    # Cubic polynomial: p(x) = -6 + 11x - 6x^2 + x^3
    assert abs(module_0.poly([-6, 11, -6, 1], 0) - (-6)) < 1e-9
    assert abs(module_0.poly([-6, 11, -6, 1], 1) - 0) < 1e-9
    assert abs(module_0.poly([-6, 11, -6, 1], 4) - 6) < 1e-9

    # Empty coefficient list evaluates to 0
    assert module_0.poly([], 5) == 0

    # All-zero coefficients
    assert abs(module_0.poly([0, 0, 0], 100)) < 1e-12

    # Constant polynomial ignores x
    assert abs(module_0.poly([5], 123.456) - 5) < 1e-9

    # Fractional x value
    assert abs(module_0.poly([1, 1], 0.5) - 1.5) < 1e-9


# Unit test for function find_zero
def test_find_zero():
    # Linear: 1 + 2x = 0 -> x = -0.5
    root = find_zero([1, 2])
    assert abs(root - (-0.5)) < 1e-8

    # Cubic with roots 1, 2, 3
    xs = [-6, 11, -6, 1]
    root = find_zero(xs)
    assert abs(module_0.poly(xs, root)) < 1e-8

    # Quadratic x^2 - 4: either root satisfies p(x) ~ 0
    xs = [-4, 0, 1]
    root = find_zero(xs)
    assert abs(module_0.poly(xs, root)) < 1e-8

    # Random-ish higher-degree polynomial still yields near-zero evaluation
    xs = [3.5, -2.1, 0.7, -4.4, 1.3]
    root = find_zero(xs)
    assert abs(module_0.poly(xs, root)) < 1e-6


if __name__ == "__main__":
    test_poly()
    test_find_zero()
    print("All tests passed.")

# Generated at 2026-11-01 19:47:21.368054
# Unit test for function find_zero
def test_find_zero():
    # nonce:bc738452
    # Linear: 1 + 2x has a zero at x = -0.5
    xs1 = [1, 2]
    assert abs(poly(xs1, module_0.find_zero(xs1))) < 1e-6
    assert abs(module_0.find_zero(xs1) + 0.5) < 1e-6

    # Linear: -1 + x has a zero at x = 1
    xs2 = [-1, 1]
    assert abs(poly(xs2, module_0.find_zero(xs2))) < 1e-6
    assert abs(module_0.find_zero(xs2) - 1.0) < 1e-6

    # Linear through origin: 2x has a zero at x = 0
    xs3 = [0, 2]
    assert abs(module_0.find_zero(xs3)) < 1e-6

    # Quadratic: x^2 - 4 has a zero in the search interval
    xs4 = [-4, 0, 1]
    assert abs(poly(xs4, module_0.find_zero(xs4))) < 1e-6

    # Cubic: (x - 0.5)(x - 2)(x + 3) = x^3 + 0.5x^2 - 6.5x + 3
    # Only root in [-1, 1] is x = 0.5
    xs5 = [3, -6.5, 0.5, 1]
    assert abs(poly(xs5, module_0.find_zero(xs5))) < 1e-6
    assert abs(module_0.find_zero(xs5) - 0.5) < 1e-6

    # Result should always satisfy poly(xs, zero) ~ 0
    for xs in [xs1, xs2, xs3, xs4, xs5]:
        assert abs(poly(xs, module_0.find_zero(xs))) < 1e-6

# Generated at 2026-11-01 19:47:36.989491
# Unit test for function poly
def test_poly():import unittest


class TestPoly(unittest.TestCase):
    def test_linear(self):
        # p(x) = 2x + 3
        self.assertAlmostEqual(module_0.poly([3, 2], 1.0), 5.0)

    def test_constant(self):
        # p(x) = 7
        self.assertAlmostEqual(module_0.poly([7], 10.0), 7.0)

    def test_quadratic(self):
        # p(x) = x^2 - 4
        self.assertAlmostEqual(module_0.poly([-4, 0, 1], 2.0), 0.0)

    def test_cubic(self):
        # p(x) = x^3 + 2x^2 + 3x + 4 at x = 2 => 8 + 8 + 6 + 4 = 26
        self.assertAlmostEqual(module_0.poly([4, 3, 2, 1], 2.0), 26.0)

    def test_negative_x(self):
        # p(x) = x^2 at x = -3 => 9
        self.assertAlmostEqual(module_0.poly([0, 0, 1], -3.0), 9.0)

    def test_zero_x(self):
        # p(x) = 5x^2 - 3x + 2 at x = 0 => 2
        self.assertAlmostEqual(module_0.poly([2, -3, 5], 0.0), 2.0)

    def test_fractional_x(self):
        # p(x) = 2x + 1 at x = 0.5 => 2
        self.assertAlmostEqual(module_0.poly([1, 2], 0.5), 2.0)

    def test_find_zero_linear(self):
        # p(x) = x - 3, zero at x = 3
        self.assertAlmostEqual(find_zero([1, -3]), 3.0, places=5)

    def test_find_zero_quadratic(self):
        # p(x) = 2x^2 - 8, zero at x = 2
        self.assertAlmostEqual(find_zero([-8, 0, 2]), 2.0, places=5)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 19:48:15.979110
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: x + 2 = 0 -> root at -2... wait, coeff order: [2, 1] => 2 + x, root = -2
    xs = [2, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6, f"Linear: poly at root should be ~0, got {poly(xs, result)}"

    # Another linear: 1 + 2x -> root at -0.5
    xs = [1, 2]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6, f"Linear 2: got {poly(xs, result)}"
    assert abs(result - (-0.5)) < 1e-6, f"Expected root -0.5, got {result}"

    # Quadratic: -6 + 11x - 6x^2 -> roots at 1, 2, 3 (bisection finds one of them)
    xs = [-6, 11, -6]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6, f"Quadratic: got {poly(xs, result)}"

    # Cubic: -12 + 2x + 4x^2 + x^3 -> root at x = 2 (approx)
    xs = [-12, 2, 4, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6, f"Cubic: got {poly(xs, result)}"

    # Polynomial with root at zero: x^2 -> root at 0
    xs = [0, 0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6, f"x^2: got {poly(xs, result)}"

    # Verify result lies within the searched bracket bounds (finite check)
    xs = [5, -3]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6, f"Bracketed: got {poly(xs, result)}"

    print("All find_zero tests passed!")


if __name__ == "__main__":
    test_find_zero()

# Generated at 2026-11-01 19:48:39.426267
# Unit test for function find_zero
def test_find_zero():
# nonce:898bd466
    # Linear polynomial: 2 - 3x = 0  =>  x = 2/3
    assert abs(module_0.find_zero([2, -3]) - 2.0 / 3.0) < 1e-6

    # Linear polynomial: 1 + 2x = 0  =>  x = -0.5
    assert abs(module_0.find_zero([1, 2]) - (-0.5)) < 1e-6

    # Linear polynomial: 5 - x = 0  =>  x = 5 (requires search range expansion)
    assert abs(module_0.find_zero([5, -1]) - 5.0) < 1e-6

    # Cubic (x-1)(x-2)(x-3) = -6 + 11x - 6x^2 + x^3
    # Should converge to one of its roots
    xs = [-6, 11, -6, 1]
    z = module_0.find_zero(xs)
    assert abs(poly(xs, z)) < 1e-6
    assert round(z, 2) in (1.0, 2.0, 3.0)

    # Negative leading coefficient cubic: -(x-2)(x-3)(x-4)
    xs = [-24, 26, -9, 1]
    z = module_0.find_zero(xs)
    assert abs(poly(xs, z)) < 1e-6
    assert round(z, 2) in (2.0, 3.0, 4.0)

    # Root far outside initial [-1, 1] window: 1 + 100x = 0 => x = -0.01
    assert abs(module_0.find_zero([1, 100]) + 0.01) < 1e-6

    # Root inside initial window: 1 - 2x = 0 => x = 0.5
    assert abs(module_0.find_zero([1, -2]) - 0.5) < 1e-6

# Generated at 2026-11-01 19:49:03.564433
# Unit test for function find_zero
def test_find_zero():
    # Linear: 1 + 2x = 0 -> zero at x = -0.5
    xs = [1, 2]
    assert abs(module_0.find_zero(xs) - (-0.5)) < 1e-6

    # Linear: -3 + x = 0 -> zero at x = 3 (requires search interval expansion)
    xs = [-3, 1]
    root = module_0.find_zero(xs)
    assert abs(root - 3.0) < 1e-6
    assert abs(poly(xs, root)) < 1e-6

    # Quadratic: x^2 - 4 -> zeros at x = -2 or x = 2
    xs = [-4, 0, 1]
    root = module_0.find_zero(xs)
    assert abs(abs(root) - 2.0) < 1e-6
    assert abs(poly(xs, root)) < 1e-6

    # Cubic: (x-1)(x-2)(x-3) = -6 + 11x - 6x^2 + x^3
    xs = [-6, 11, -6, 1]
    root = module_0.find_zero(xs)
    assert any(abs(root - r) < 1e-4 for r in (1.0, 2.0, 3.0))
    assert abs(poly(xs, root)) < 1e-4

    # Linear: -4 + x = 0 -> zero at x = 4
    xs = [-4, 1]
    root = module_0.find_zero(xs)
    assert abs(root - 4.0) < 1e-6
    assert abs(poly(xs, root)) < 1e-6


test_find_zero()
print("All tests passed!")

# Generated at 2026-11-01 19:49:25.029895
# Unit test for function find_zero
def test_find_zero():
    import math

    # Linear polynomial: 1 + 2x = 0  ->  x = -0.5
    xs = [1, 2]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6, f"Expected zero for {xs}, got poly={poly(xs, x)} at x={x}"
    assert abs(x - (-0.5)) < 1e-6

    # Quadratic polynomial: -6 + 11x - 6x^2 + x^3 (roots 1, 2, 3)
    xs = [-6, 11, -6, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6, f"Expected zero for {xs}, got poly={poly(xs, x)} at x={x}"
    assert round(x, 6) in (1.0, 2.0, 3.0)

    # Polynomial: x^2 - 4 (roots -2, 2)
    xs = [-4, 0, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6, f"Expected zero for {xs}, got poly={poly(xs, x)} at x={x}"
    assert abs(abs(x) - 2.0) < 1e-6

    # Constant zero polynomial: poly is always 0, loop exits immediately
    xs = [0]
    x = module_0.find_zero(xs)
    assert poly(xs, x) == 0

    # Polynomial with root at 0: 5x = 0
    xs = [0, 5]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6
    assert abs(x) < 1e-6

    # Polynomial: 2 - 3x (root at 2/3)
    xs = [2, -3]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6
    assert abs(x - (2.0 / 3.0)) < 1e-6

    # Higher-degree polynomial: x^4 - 1 (roots -1, 1)
    xs = [-1, 0, 0, 0, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6
    assert abs(abs(x) - 1.0) < 1e-6

    # Polynomial with large coefficients: 1000 + 1x (root at -1000)
    xs = [1000, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-3, f"Expected zero for {xs}, got poly={poly(xs, x)} at x={x}"
    assert abs(x - (-1000.0)) < 1e-3

    print("All tests passed!")


if __name__ == "__main__":
    test_find_zero()

# Generated at 2026-11-01 19:49:38.588330
# Unit test for function find_zero
def test_find_zero():
    # Test 1: linear polynomial x + 2 -> zero at -0.5
    assert abs(module_0.find_zero([1, 2]) - (-0.5)) < 1e-6, "Test 1 failed"

    # Test 2: linear polynomial 2x + 1 -> zero at -0.5
    assert abs(module_0.find_zero([2, 1]) - (-0.5)) < 1e-6, "Test 2 failed"

    # Test 3: linear polynomial x - 1 -> zero at 1.0
    assert abs(module_0.find_zero([1, -1]) - 1.0) < 1e-6, "Test 3 failed"

    # Test 4: cubic polynomial with root at 1.0: x^3 - 6x^2 + 11x - 6
    result = module_0.find_zero([-6, 11, -6, 1])
    assert abs(poly([-6, 11, -6, 1], result)) < 1e-6, "Test 4 failed"

    # Test 5: polynomial 5 + 8x -> zero at -0.625
    assert abs(module_0.find_zero([5, 8]) - (-0.625)) < 1e-6, "Test 5 failed"

    # Test 6: quadratic x^2 - 4 -> zero at 2.0 (or -2.0)
    result = module_0.find_zero([-4, 0, 1])
    assert abs(poly([-4, 0, 1], result)) < 1e-6, "Test 6 failed"

    # Test 7: polynomial with root at 0: x -> zero near 0.0
    result = module_0.find_zero([0, 1])
    assert abs(poly([0, 1], result)) < 1e-6, "Test 7 failed"

    # Test 8: verify returned value is a zero for a general polynomial
    xs = [3, -4, 1]  # x^2 - 4x + 3, roots at 1 and 3
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6, "Test 8 failed"

    # Test 9: polynomial with large coefficients: 100x + 50 -> zero at -0.5
    assert abs(module_0.find_zero([100, 50]) - (-0.5)) < 1e-6, "Test 9 failed"

    # Test 10: result lies within reasonable bounds (bisection sanity check)
    result = module_0.find_zero([1, 0, -1])  # x^2 - 1, roots at -1 and 1
    assert -1.0 <= result <= 1.0, "Test 10 failed"

    print("All test_find_zero tests passed!")


if __name__ == "__main__":
    test_find_zero()

# Generated at 2026-11-01 19:50:01.932913
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: f(x) = 1 + 2x -> zero at x = -0.5
    xs = [1, 2]
    assert abs(module_0.find_zero(xs) - (-0.5)) < 1e-6

    # Linear polynomial: f(x) = 2 - x -> zero at x = 2
    xs = [2, -1]
    assert abs(module_0.find_zero(xs) - 2.0) < 1e-6

    # Linear polynomial: f(x) = x - 3 -> zero at x = 3
    xs = [-3, 1]
    assert abs(module_0.find_zero(xs) - 3.0) < 1e-6

    # Cubic: f(x) = (x-1)(x-2)(x-3) = -6 + 11x - 6x^2 + x^3
    xs = [-6, 11, -6, 1]
    zero = module_0.find_zero(xs)
    assert any(abs(zero - r) < 1e-4 for r in (1.0, 2.0, 3.0))
    assert abs(poly(xs, zero)) < 1e-4

    # Quadratic: f(x) = x^2 - 5x = x(x - 5), roots at 0 and 5
    xs = [0, -5, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6

    # Quadratic: f(x) = x^2 - 3x + 2 = (x-1)(x-2)
    xs = [2, -3, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6

    # General check: returned value should nearly zero the polynomial
    for xs in ([3, 1], [0, -5, 1], [2, -3, 1], [-6, 11, -6, 1]):
        z = module_0.find_zero(xs)
        assert abs(poly(xs, z)) < 1e-4


if __name__ == "__main__":
    test_find_zero()
    print("All tests passed.")

# Generated at 2026-11-01 19:51:09.684622
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: 1 + 2x = 0 at x = -0.5
    assert abs(module_0.find_zero([1, 2]) - (-0.5)) < 1e-8
    assert abs(poly([1, 2], module_0.find_zero([1, 2]))) < 1e-8

    # Linear polynomial whose root lies outside the initial [-1, 1] bracket:
    # 2 + x = 0 at x = -2 (bracket must expand)
    assert abs(module_0.find_zero([2, 1]) - (-2.0)) < 1e-8
    assert abs(poly([2, 1], module_0.find_zero([2, 1]))) < 1e-8

    # Cubic: x^3 - 6x^2 + 11x - 6 has roots 1, 2, 3
    xs = [-6, 11, -6, 1]
    root = module_0.find_zero(xs)
    assert abs(poly(xs, root)) < 1e-6
    assert any(abs(root - r) < 1e-6 for r in (1.0, 2.0, 3.0))

    # Quadratic: x^2 - 1 has roots at -1 and 1 (boundary of initial bracket)
    xs2 = [-1, 0, 1]
    root2 = module_0.find_zero(xs2)
    assert abs(poly(xs2, root2)) < 1e-6
    assert abs(abs(root2) - 1.0) < 1e-6

    # Zero polynomial: product check is 0 immediately, bisection still terminates
    assert module_0.find_zero([0]) == -1.0

# Generated at 2026-11-01 19:51:54.059779
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: 1 + 2*x = 0 -> x = -0.5
    assert abs(module_0.find_zero([1, 2]) + 0.5) < 1e-4

    # Linear polynomial: -6 + 12*x = 0 -> x = 0.5
    assert abs(module_0.find_zero([-6, 12]) - 0.5) < 1e-4

    # Quadratic polynomial: -6 + 11*x - 6*x^2 = 0 -> roots at 1, 2, 3
    xs = [-6, 11, -6]
    root = module_0.find_zero(xs)
    assert abs(poly(xs, root)) < 1e-8

    # Cubic polynomial: -12 + 22*x - 12*x^2 + 2*x^3 -> roots at 1, 2, 3
    xs = [-12, 22, -12, 2]
    root = module_0.find_zero(xs)
    assert abs(poly(xs, root)) < 1e-8

    # Constant sign change search: verify returned value is actually a root
    xs = [5, -3, 1]
    root = module_0.find_zero(xs)
    assert abs(poly(xs, root)) < 1e-6

    # Result should lie within a reasonable bracket
    xs = [2, -4]
    root = module_0.find_zero(xs)
    assert -100 <= root <= 100
    assert abs(root - 0.5) < 1e-4

# Generated at 2026-11-01 19:52:31.234592
# Unit test for function find_zero
def test_find_zero():
    # Linear: 1 + 2x = 0 -> root at -0.5 (found within initial bracket)
    assert abs(module_0.find_zero([1, 2]) - (-0.5)) < 1e-6

    # Linear: 7 - 14x = 0 -> root at 0.5
    assert abs(module_0.find_zero([7, -14]) - 0.5) < 1e-6

    # Linear: -5 + 3x = 0 -> root at 5/3 (requires bracket expansion)
    assert abs(module_0.find_zero([-5, 3]) - 5.0 / 3.0) < 1e-6

    # Linear: -4 + 2x = 0 -> root at 2 (requires bracket expansion)
    assert abs(module_0.find_zero([-4, 2]) - 2.0) < 1e-6

    # Cubic (x-1)(x-2)(x-3) = -6 + 11x - 6x^2 + x^3
    xs = [-6, 11, -6, 1]
    z = module_0.find_zero(xs)
    # Returned point must be an actual zero of the polynomial
    assert abs(poly(xs, z)) < 1e-6
    # Bisection starting from [-1, 1] converges to the root at x = 1
    assert abs(z - 1.0) < 1e-6

    # Cubic x^3 - 1 -> root at 1
    xs = [-1, 0, 0, 1]
    z = module_0.find_zero(xs)
    assert abs(z - 1.0) < 1e-6
    assert abs(poly(xs, z)) < 1e-6

    # Higher-degree: 2x^3 - 3x^2 + 0x + 1 has a root in [-1, 1]
    xs = [1, 0, -3, 2]
    z = module_0.find_zero(xs)
    assert abs(poly(xs, z)) < 1e-6

    print("test_find_zero passed")


if __name__ == "__main__":
    test_find_zero()

# Generated at 2026-11-01 19:53:29.500187
# Unit test for function find_zero
def test_find_zero():# Linear polynomial: 1 + 2x has root at x = -0.5
    result = module_0.find_zero([1, 2])
    assert abs(poly([1, 2], result)) < 1e-7

    # Quadratic: x^2 - 4 has roots ±2; bisection should land on one of them
    result = module_0.find_zero([-4, 0, 1])
    assert abs(abs(result) - 2.0) < 1e-6

    # Cubic with roots 1, 2, 3: -6 + 11x - 6x^2 + x^3
    xs = [-6, 11, -6, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6

    # Constant-zero-free check: odd-degree polynomial always crosses zero
    xs = [1, 0, 0, -1]  # 1 - x^3 has root at x = 1
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-6

    # Root far from origin: 512 + x^9 has root near -2
    xs = [512, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    result = module_0.find_zero(xs)
    assert abs(poly(xs, result)) < 1e-4

    # Result returned is a float within reasonable bounds
    result = module_0.find_zero([1, 2])
    assert isinstance(result, float)

test_find_zero()
print("All tests passed.")

# Generated at 2026-11-01 19:54:46.714513
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: 1 + 2x = 0 -> x = -0.5
    assert abs(module_0.find_zero([1, 2]) - (-0.5)) < 1e-6

    # Quadratic polynomial: 1 + 3x - 4x^2 = 0 -> roots at 1 and -0.25
    xs = [1, 3, -4]
    assert abs(poly(xs, module_0.find_zero(xs))) < 1e-6

    # Cubic polynomial: -6 + 11x - 6x^2 + x^3 = 0 -> root at 1.0
    xs = [-6, 11, -6, 1]
    assert abs(poly(xs, module_0.find_zero(xs))) < 1e-6

    # Polynomial with symmetric roots: -1 + x^2 = 0
    xs = [-1, 0, 1]
    assert abs(poly(xs, module_0.find_zero(xs))) < 1e-6

    # Result returned by find_zero must lie within a small neighborhood of a true root
    xs = [2, -3, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6
    assert isinstance(zero, float)

    print("All tests passed!")

# Generated at 2026-11-01 19:55:45.946263
# Unit test for function find_zero
def test_find_zero():
    # Linear: 1 + 2x = 0 -> x = -0.5
    xs = [1, 2]
    res = module_0.find_zero(xs)
    assert abs(res - (-0.5)) < 1e-6
    assert abs(poly(xs, res)) < 1e-6

    # Linear with large slope: 1 + 100x = 0 -> x = -0.01
    xs = [1, 100]
    res = module_0.find_zero(xs)
    assert abs(res - (-0.01)) < 1e-6
    assert abs(poly(xs, res)) < 1e-6

    # Quadratic: -6 + 11x - 6x^2 = -(x-2)(x-3) -> roots 2 and 3
    xs = [-6, 11, -6]
    res = module_0.find_zero(xs)
    assert abs(poly(xs, res)) < 1e-6
    assert 1.9 <= res <= 3.1

    # Quadratic: 4 + 2x - 4x^2 -> roots approx -0.7808 and 1.2808
    xs = [4, 2, -4]
    res = module_0.find_zero(xs)
    assert abs(poly(xs, res)) < 1e-6

    # Cubic: -6 + 11x - 6x^2 + x^3 = (x-1)(x-2)(x-3) -> roots 1, 2, 3
    xs = [-6, 11, -6, 1]
    res = module_0.find_zero(xs)
    assert abs(poly(xs, res)) < 1e-6
    assert 0.9 <= res <= 3.1

    # Quartic with root near 0: 1 - 4x^2 -> roots -0.5 and 0.5
    xs = [1, 0, -4]
    res = module_0.find_zero(xs)
    assert abs(poly(xs, res)) < 1e-6