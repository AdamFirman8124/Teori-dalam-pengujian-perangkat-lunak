

# Generated at 2026-11-02 22:12:03.755347
# Unit test for function find_zero
def test_find_zero():import math
import unittest


class TestFindZero(unittest.TestCase):
    def test_find_zero(self):
        # Test with polynomial x^2 - 1, roots at -1 and 1
        result = module_0.find_zero([1, 0, -2])
        self.assertAlmostEqual(poly([1, 0, -2], result), 0, places=6)

        # Test with linear polynomial 2x - 4, root at 2
        result = module_0.find_zero([-4, 2])
        self.assertAlmostEqual(poly([-4, 2], result), 0, places=6)

        # Test with polynomial x^3 + x^2 + x + 1, root at -1
        result = module_0.find_zero([1, 1, 1, 1])
        self.assertAlmostEqual(poly([1, 1, 1, 1], result), 0, places=6)

        # Test with polynomial -6 + 11x - 6x^2 + x^3, roots at 1, 2, 3
        result = module_0.find_zero([-6, 11, -6, 1])
        self.assertAlmostEqual(poly([-6, 11, -6, 1], result), 0, places=6)


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 22:14:24.341136
# Unit test for function find_zero
def test_find_zero():
    # --- poly helper checks ---
    assert poly([1, 2, 3], 2.0) == 17.0          # 1 + 2*2 + 3*4
    assert poly([5], 100.0) == 5.0               # constant polynomial
    assert poly([], 3.0) == 0.0                  # empty coefficients
    assert abs(poly([0, -2, 1], 3.0) - 3.0) < 1e-9  # x^2 - 2x at x=3

    # --- find_zero: linear 2x + 1 = 0 -> x = -0.5 ---
    xs = [1, 2]
    x = module_0.find_zero(xs)
    assert abs(x + 0.5) < 1e-4
    assert abs(poly(xs, x)) < 1e-6

    # --- find_zero: linear 11x - 6 = 0 -> x = 6/11 ---
    xs = [-6, 11]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6
    assert abs(x - 6.0 / 11.0) < 1e-4

    # --- find_zero: cubic x^3 - 6x^2 + 11x - 6 (roots 1, 2, 3) ---
    xs = [-6, 11, -6, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-4
    assert any(abs(x - r) < 1e-3 for r in (1.0, 2.0, 3.0))

    # --- find_zero: quadratic x^2 - 4 (roots -2, 2) ---
    xs = [-4, 0, 1]
    x = module_0.find_zero(xs)
    assert abs(abs(x) - 2.0) < 1e-3
    assert abs(poly(xs, x)) < 1e-4

    # --- find_zero: quadratic x^2 - x - 2 (roots -1, 2) ---
    xs = [-2, -1, 1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-4
    assert any(abs(x - r) < 1e-3 for r in (-1.0, 2.0))

    # --- find_zero: root lying outside initial bracket [-1, 1] ---
    # 5x - 20 = 0 -> x = 4, bracket must expand
    xs = [-20, 5]
    x = module_0.find_zero(xs)
    assert abs(x - 4.0) < 1e-4
    assert abs(poly(xs, x)) < 1e-6

    # --- find_zero: negative root outside bracket ---
    # 5x + 20 = 0 -> x = -4
    xs = [20, 5]
    x = module_0.find_zero(xs)
    assert abs(x + 4.0) < 1e-4
    assert abs(poly(xs, x)) < 1e-6

# Generated at 2026-11-02 22:16:45.280284
# Unit test for function find_zero
def test_find_zero():
    # nonce:a16edd3c
    # Linear: 1 - 2x = 0 -> root at 0.5
    assert abs(module_0.find_zero([1, -2]) - 0.5) < 1e-6

    # Linear: 1 + 2x = 0 -> root at -0.5
    assert abs(module_0.find_zero([1, 2]) + 0.5) < 1e-6

    # Residual check: poly at the found root is ~ 0
    xs = [1, -2]
    assert abs(poly(xs, module_0.find_zero(xs))) < 1e-6

    # Cubic (x-1)(x-2)(x-3) = -6 + 11x - 6x^2 + x^3 -> bisection converges to 1.0
    assert abs(module_0.find_zero([-6, 11, -6, 1]) - 1.0) < 1e-6

    # Residual check for the cubic
    xs = [-6, 11, -6, 1]
    assert abs(poly(xs, module_0.find_zero(xs))) < 1e-6

# Generated at 2026-11-02 22:18:45.193054
# Unit test for function find_zero
def test_find_zero():
    # nonce:2e770205

    # Linear polynomial: 2 - 3x = 0 -> x = 2/3
    xs = [2, -3]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6, f"linear failed: poly({zero})={poly(xs, zero)}"

    # Quadratic: x^2 - 3x + 2 = (x-1)(x-2), bisection should converge to root 1
    xs = [1, -3, 2]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6, f"quadratic failed: poly({zero})={poly(xs, zero)}"
    assert abs(zero - 1.0) < 1e-6, f"expected root near 1.0, got {zero}"

    # Cubic: -6 + 11x - 6x^2 + x^3 = (x-1)(x-2)(x-3)
    xs = [-6, 11, -6, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6, f"cubic failed: poly({zero})={poly(xs, zero)}"

    # Root outside [-1, 1]: 5 - 4x = 0 -> x = 1.25 (requires interval expansion)
    xs = [5, -4]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6, f"expanded interval failed: poly({zero})={poly(xs, zero)}"
    assert abs(zero - 1.25) < 1e-6, f"expected root near 1.25, got {zero}"

    # Negative root outside [-1, 1]: 2 + 3x = 0 -> x = -2/3 (inside), use 1 + 2x -> x = -0.5
    xs = [1, 2]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6, f"negative root failed: poly({zero})={poly(xs, zero)}"
    assert abs(zero - (-0.5)) < 1e-6, f"expected root near -0.5, got {zero}"

    # Zero polynomial edge case: poly is 0 everywhere
    assert abs(poly([0], module_0.find_zero([0]))) < 1e-6

    print("test_find_zero passed")


if __name__ == "__main__":
    test_find_zero()

# Generated at 2026-11-02 22:20:12.746877
# Unit test for function find_zero
def test_find_zero():
    # nonce:a30d63a2

    # Linear: 1 + 2x = 0 -> root at -0.5
    xs = [1, 2]
    zero = module_0.find_zero(xs)
    assert abs(zero - (-0.5)) < 1e-6, f"expected -0.5, got {zero}"
    assert abs(poly(xs, zero)) < 1e-6

    # Linear: -5 + 10x = 0 -> root at 0.5
    xs = [-5, 10]
    zero = module_0.find_zero(xs)
    assert abs(zero - 0.5) < 1e-6, f"expected 0.5, got {zero}"
    assert abs(poly(xs, zero)) < 1e-6

    # Quadratic: 2 - 3x + x^2 = (x - 1)(x - 2) -> roots at 1 and 2
    xs = [2, -3, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6
    assert abs(zero - 1.0) < 1e-3 or abs(zero - 2.0) < 1e-3, f"root not near 1 or 2, got {zero}"

    # Cubic: -6 + 11x - 6x^2 + x^3 = -(x - 1)(x - 2)(x - 3) -> roots at 1, 2, 3
    xs = [-6, 11, -6, 1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6

    # Polynomial 1 - x^2 -> roots at -1 and 1
    xs = [1, 0, -1]
    zero = module_0.find_zero(xs)
    assert abs(poly(xs, zero)) < 1e-6

    print("test_find_zero passed")


if __name__ == "__main__":
    test_find_zero()