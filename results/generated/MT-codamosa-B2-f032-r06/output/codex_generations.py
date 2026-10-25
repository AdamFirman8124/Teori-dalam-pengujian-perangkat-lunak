

# Generated at 2026-10-25 01:38:38.202580
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([0.0, 1.0], 0.0),          # x = 0
        ([1.0, 1.0], -1.0),         # 1 + x = 0
        ([-6.0, 1.0], 6.0),         # -6 + x = 0
        ([-8.0, 0.0, 0.0, 1.0], 2.0),  # x^3 - 8 = 0
    ]

    for coefficients, expected in test_cases:
        root = module_0.find_zero(coefficients)

        assert math.isclose(root, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, root)) < 1e-8

# Generated at 2026-10-25 01:38:45.735594
# Unit test for function poly
def test_poly():
    assert module_0.poly([], 5.0) == 0
    assert module_0.poly([3], 10.0) == 3.0
    assert module_0.poly([1, 2, 3], 2.0) == 17.0       # 1 + 2Â·2 + 3Â·2Â²
    assert module_0.poly([1, -2, 1], 1.0) == 0.0       # 1 - 2x + xÂ²
    assert math.isclose(module_0.poly([0.1, 0.2], 0.3), 0.16)

# Generated at 2026-10-25 01:38:48.153011
# Unit test for function find_zero

# Generated at 2026-10-25 01:38:50.568693
# Unit test for function find_zero

# Generated at 2026-10-25 01:38:52.983672
# Unit test for function find_zero

# Generated at 2026-10-25 01:38:55.398764
# Unit test for function find_zero

# Generated at 2026-10-25 01:39:02.311762
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([0.0, 1.0])

# Generated at 2026-10-25 01:39:12.962400
# Unit test for function find_zero
def test_find_zero():
    # xÂ³ - 27 = 0; root is 3.
    # This also tests expansion of the initial [-1, 1] interval.
    xs = [-27, 0, 0, 1]

    root = module_0.find_zero(xs)

    assert math.isclose(root, 3.0, rel_tol=0.0, abs_tol=1e-9)
    assert abs(poly(xs, root)) < 1e-8

# Generated at 2026-10-25 01:39:34.456541
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([1, 2], -0.5),                 # 1 + 2x = 0
        ([-2, 1], 2.0),                 # -2 + x = 0
        ([2, 0, 0, 1], -2 ** (1 / 3)),  # 2 + xÂ³ = 0
        ([3, 0, 1], None),              # No real root; unsupported
    ]

    for coefficients, expected in test_cases:
        if expected is None:
            continue

        root = module_0.find_zero(coefficients)

        assert math.isclose(root, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, root)) < 1e-8

# Generated at 2026-10-25 01:39:44.778779
# Unit test for function find_zero
def test_find_zero():
    cases = [
        ([-2, 0, 0, 1], 2 ** (1 / 3)),  # xÂ³ - 2 = 0
        ([3, 1], -3.0),                  # x + 3 = 0
        ([0, 1], 0.0),                   # x = 0
    ]

    for coefficients, expected in cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 01:39:47.291886
# Unit test for function find_zero

# Generated at 2026-10-25 01:39:49.901962
# Unit test for function find_zero

# Generated at 2026-10-25 01:39:52.397123
# Unit test for function find_zero

# Generated at 2026-10-25 01:39:54.874282
# Unit test for function find_zero

# Generated at 2026-10-25 01:39:57.384989
# Unit test for function find_zero

# Generated at 2026-10-25 01:39:59.885889
# Unit test for function find_zero

# Generated at 2026-10-25 01:40:02.378381
# Unit test for function find_zero

# Generated at 2026-10-25 01:40:04.870709
# Unit test for function find_zero

# Generated at 2026-10-25 01:40:07.371935
# Unit test for function find_zero

# Generated at 2026-10-25 01:40:18.772874
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-1, 1], 1.0),          # x - 1
        ([1, 1], -1.0),          # x + 1
        ([-8, 0, 0, 1], 2.0),   # xÂ³ - 8
        ([8, 0, 0, 1], -2.0),   # xÂ³ + 8
        ([0, -4, 0, 1], 2.0),   # xÂ³ - 4x (may find one of its roots)
    ]

    for coefficients, expected_root in test_cases:
        root = module_0.find_zero(coefficients)

        # The returned value must be a root of the polynomial.
        assert abs(poly(coefficients, root)) < 1e-7

        # Check the expected root where the bisection path is deterministic.
        if coefficients != [0, -4, 0, 1]:
            assert math.isclose(root, expected_root, abs_tol=1e-9)

# Generated at 2026-10-25 01:40:30.763419
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        [1, 2],                # 1 + 2x = 0
        [-6, 11, -6, 1],      # roots: 1, 2, 3
        [0, 1],                # root: 0
        [8, 0, 0, 1],         # 8 + xÂ³ = 0
        [-1, 0, 0, 1],        # xÂ³ - 1 = 0
    ]

    for coefficients in test_cases:
        root = module_0.find_zero(coefficients)
        assert abs(poly(coefficients, root)) < 1e-7

# Generated at 2026-10-25 01:40:41.303864
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-1, 1], 1.0),          # x - 1
        ([3, 1], -3.0),          # x + 3
        ([-8, 0, 0, 1], 2.0),   # xÂ³ - 8
        ([8, 0, 0, 1], -2.0),   # xÂ³ + 8
    ]

    for coefficients, expected in test_cases:
        root = module_0.find_zero(coefficients)

        assert math.isclose(root, expected, abs_tol=1e-9)
        assert math.isclose(poly(coefficients, root), 0.0, abs_tol=1e-8)

# Generated at 2026-10-25 01:41:01.035313
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-2, 1], 2.0),          # x - 2
        ([3, 1], -3.0),          # x + 3
        ([-8, 0, 0, 1], 2.0),   # xÂ³ - 8
        ([0, 1], 0.0),           # x
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)
        assert math.isclose(result, expected, abs_tol=1e-9)
        assert math.isclose(poly(coefficients, result), 0.0, abs_tol=1e-8)

# Generated at 2026-10-25 01:41:10.163945
# Unit test for function find_zero
def test_find_zero():
    # p(x) = 2x - 4, whose zero is x = 2
    xs = [-4, 2]

    zero = module_0.find_zero(xs)

    assert math.isclose(zero, 2.0, abs_tol=1e-9)
    assert math.isclose(poly(xs, zero), 0.0, abs_tol=1e-9)

# Generated at 2026-10-25 01:41:20.518309
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-1.0, 2.0], 0.5),          # 2x - 1 = 0
        ([-3.0, 1.0], 3.0),          # x - 3 = 0 (tests interval expansion)
        ([-2.0, 0.0, 0.0, 1.0], math.pow(2.0, 1 / 3)),  # xÂ³ - 2 = 0
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert math.isclose(poly(coefficients, result), 0.0, abs_tol=1e-8)

# Generated at 2026-10-25 01:41:36.213990
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-2.0, 1.0], 2.0),                  # x - 2 = 0
        ([3.0, 1.0], -3.0),                  # x + 3 = 0
        ([-2.0, 0.0, 0.0, 1.0], 2 ** (1/3)) # xÂ³ - 2 = 0
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 01:41:44.565012
# Unit test for function find_zero
def test_find_zero():
    # xÂ³ - 2 = 0, whose real root is â2
    coefficients = [-2.0, 0.0, 0.0, 1.0]

    result = module_0.find_zero(coefficients)

    assert math.isclose(result, 2 ** (1 / 3), abs_tol=1e-9)
    assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 01:42:00.152492
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-2.0, 0.0, 0.0, 1.0], 2.0 ** (1.0 / 3.0)),  # x^3 - 2
        ([8.0, 0.0, 0.0, 1.0], -2.0),                 # x^3 + 8
        ([-125.0, 0.0, 0.0, 1.0], 5.0),               # x^3 - 125
        ([3.0, 1.0], -3.0),                            # x + 3
        ([0.0, 0.0, 0.0, 1.0], 0.0),                  # x^3
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert math.isclose(poly(coefficients, result), 0.0, abs_tol=1e-7)

# Generated at 2026-10-25 01:42:02.734833
# Unit test for function find_zero

# Generated at 2026-10-25 01:42:05.245109
# Unit test for function find_zero

# Generated at 2026-10-25 01:42:07.745447
# Unit test for function find_zero

# Generated at 2026-10-25 01:42:17.260145
# Unit test for function find_zero
def test_find_zero():
    # p(x) = xÂ³ - 6xÂ² + 11x - 6, with roots 1, 2, and 3
    coefficients = [-6.0, 11.0, -6.0, 1.0]

    root = module_0.find_zero(coefficients)

    assert math.isclose(root, 1.0, abs_tol=1e-8)
    assert abs(poly(coefficients, root)) < 1e-8

# Generated at 2026-10-25 01:42:26.260470
# Unit test for function find_zero
def test_find_zero():
    # Polynomial: xÂ³ - 2, whose real root is â2
    coefficients = [-2.0, 0.0, 0.0, 1.0]

    result = module_0.find_zero(coefficients)
    expected = 2.0 ** (1.0 / 3.0)

    assert math.isclose(result, expected, abs_tol=1e-9)
    assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 01:42:37.127642
# Unit test for function find_zero
def test_find_zero():
    # xÂ³ - 2 = 0, whose real root is â2
    coefficients = [-2, 0, 0, 1]

    result = module_0.find_zero(coefficients)
    expected = math.pow(2, 1 / 3)

    assert math.isclose(result, expected, abs_tol=1e-9)
    assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 01:42:48.591937
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-2, 1], 2.0),       # x - 2 = 0
        ([3, 1], -3.0),       # x + 3 = 0
        ([0, 1], 0.0),        # x = 0
        ([-4, 0, 1], -2.0),   # xÂ² - 4 = 0; algorithm finds -2
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 01:43:04.986812
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-0.5, 1.0], 0.5),                  # x - 0.5
        ([-6.0, 1.0], 6.0),                  # x - 6
        ([2.0, 0.0, 0.0, 1.0], -math.pow(2.0, 1 / 3)),  # x^3 + 2
    ]

    for coefficients, expected in test_cases:
        root = module_0.find_zero(coefficients)

        assert math.isclose(root, expected, abs_tol=1e-8)
        assert abs(poly(coefficients, root)) < 1e-7

# Generated at 2026-10-25 01:43:08.398564
# Unit test for function find_zero

# Generated at 2026-10-25 01:43:13.268225
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-1.0, 1.0])

# Generated at 2026-10-25 01:43:25.296988
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        [0.0, 1.0],             # x
        [-2.0, 1.0],            # x - 2
        [1.0, 1.0],             # x + 1
        [-1.0, 0.0, 0.0, 1.0], # xÂ³ - 1
        [1.0, 1.0, 0.0, 1.0],  # xÂ³ + x + 1
    ]

    for coefficients in test_cases:
        root = module_0.find_zero(coefficients)
        assert abs(poly(coefficients, root)) < 1e-8

# Generated at 2026-10-25 01:43:39.916170
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([0, 1], 0.0),                  # x = 0
        ([3, 2], -1.5),                 # 3 + 2x = 0
        ([-2, 0, 0, 1], 2 ** (1 / 3)), # xÂ³ - 2 = 0
        ([1, 0, 0, 1], -1.0),          # xÂ³ + 1 = 0
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, rel_tol=0.0, abs_tol=1e-8)
        assert abs(poly(coefficients, result)) < 1e-7

# Generated at 2026-10-25 01:43:50.292460
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([1.0, 2.0], -0.5),             # 1 + 2x = 0
        ([-8.0, 0.0, 0.0, 1.0], 2.0), # xÂ³ - 8 = 0
        ([6.0, 1.0, 0.0, 1.0], -2.0), # xÂ³ + x + 6 = 0
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)
        assert math.isclose(result, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 01:43:52.782099
# Unit test for function find_zero

# Generated at 2026-10-25 01:43:55.272645
# Unit test for function find_zero

# Generated at 2026-10-25 01:43:57.809603
# Unit test for function find_zero

# Generated at 2026-10-25 01:44:00.476613
# Unit test for function find_zero

# Generated at 2026-10-25 01:44:03.006365
# Unit test for function find_zero

# Generated at 2026-10-25 01:44:05.476197
# Unit test for function find_zero

# Generated at 2026-10-25 01:44:07.995893
# Unit test for function find_zero

# Generated at 2026-10-25 01:44:10.489416
# Unit test for function find_zero

# Generated at 2026-10-25 01:44:17.157953
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-1.0, 2.0])

# Generated at 2026-10-25 01:44:39.784531
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([1, 1], -1.0),          # 1 + x = 0
        ([4, -2], 2.0),          # 4 - 2x = 0
        ([1, 0, 0, 1], -1.0),   # 1 + x^3 = 0
        ([-8, 0, 0, 1], 2.0),   # x^3 - 8 = 0
        ([0, 1], 0.0),           # x = 0
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-8)
        assert abs(poly(coefficients, result)) < 1e-7

# Generated at 2026-10-25 01:44:50.858503
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-2, 1], 2.0),             # x - 2 = 0
        ([2, 1], -2.0),             # x + 2 = 0
        ([-2, 0, 0, 1], 2 ** (1/3)) # xÂ³ - 2 = 0
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert math.isclose(poly(coefficients, result), 0.0, abs_tol=1e-8)

# Generated at 2026-10-25 01:44:53.360501
# Unit test for function find_zero

# Generated at 2026-10-25 01:44:55.876385
# Unit test for function find_zero

# Generated at 2026-10-25 01:44:58.372162
# Unit test for function find_zero

# Generated at 2026-10-25 01:45:26.201522
# Unit test for function find_zero

# Generated at 2026-10-25 01:45:30.488721
# Unit test for function find_zero

# Generated at 2026-10-25 01:45:34.232972
# Unit test for function find_zero

# Generated at 2026-10-25 01:45:48.092724
# Unit test for function find_zero
def test_find_zero():
    cases = [
        ([-2.0, 1.0], 2.0),                    # x - 2 = 0
        ([2.0, 1.0], -2.0),                    # x + 2 = 0
        ([-2.0, 0.0, 0.0, 1.0], 2.0 ** (1 / 3)),  # xÂ³ - 2 = 0
    ]

    for coefficients, expected in cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 01:45:56.081373
# Unit test for function find_zero
def test_find_zero():
    # p(x) = xÂ³ - 2, whose real root is â2
    coefficients = [-2.0, 0.0, 0.0, 1.0]

    result = module_0.find_zero(coefficients)
    expected = math.pow(2.0, 1.0 / 3.0)

    assert math.isclose(result, expected, abs_tol=1e-9)
    assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 01:46:05.171943
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-2, 1], 2.0),          # x - 2 = 0
        ([2, 1], -2.0),          # x + 2 = 0
        ([0, 1], 0.0),           # x = 0
        ([-8, 0, 0, 1], 2.0),   # xÂ³ - 8 = 0
        ([1, 1, 0, 1], -1.0),   # xÂ³ + x + 1 = 0 (verify residual)
    ]

    for coefficients, expected in test_cases:
        root = module_0.find_zero(coefficients)

        # Every returned value must approximately satisfy the polynomial.
        assert abs(poly(coefficients, root)) < 1e-8

        # Check the exact expected root where one is known.
        if coefficients != [1, 1, 0, 1]:
            assert abs(root - expected) < 1e-8

# Generated at 2026-10-25 01:46:15.639571
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-2, 1], 2.0),              # x - 2
        ([-2, 0, 0, 1], 2 ** (1/3)), # xÂ³ - 2
        ([0, 1], 0.0),               # x
        ([1, 0, 1, 1], -1.465571231876768),  # xÂ³ + xÂ² + 1
    ]

    for coefficients, expected in test_cases:
        root = module_0.find_zero(coefficients)

        assert math.isclose(root, expected, abs_tol=1e-8)
        assert math.isclose(poly(coefficients, root), 0.0, abs_tol=1e-8)

# Generated at 2026-10-25 01:46:19.361350
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:22.577581
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:25.524460
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:28.916690
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:32.765991
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:36.095199
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:40.307808
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:43.531738
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:46.700313
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:49.485348
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:54.410015
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:56.800606
# Unit test for function find_zero

# Generated at 2026-10-25 01:46:59.540581
# Unit test for function find_zero

# Generated at 2026-10-25 01:47:03.289678
# Unit test for function find_zero

# Generated at 2026-10-25 01:47:10.752029
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-0.5, 1.0])