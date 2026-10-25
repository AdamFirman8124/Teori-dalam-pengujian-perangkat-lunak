

# Generated at 2026-10-25 05:15:39.908527
# Unit test for function poly
def test_poly():
    assert module_0.poly([], 5.0) == 0
    assert module_0.poly([5.0], 999.0) == 5.0
    assert module_0.poly([1.0, 2.0, 3.0], 2.0) == 17.0      # 1 + 2*2 + 3*2^2
    assert module_0.poly([1.0, 0.0, -1.0], 2.0) == -3.0     # 1 - x^2
    assert module_0.poly([2.0, 3.0], -1.0) == -1.0
    assert module_0.poly([1.0, 1.0], 0.0) == 1.0
    assert math.isclose(module_0.poly([0.5, 0.5], 0.5), 0.75)
    print("test_poly passed")


if __name__ == "__main__":
    test_poly()

# Generated at 2026-10-25 05:15:41.314447
# Unit test for function poly
def test_poly():
    assert module_0.poly([], 5.0) == 0
    assert module_0.poly([5.0], 999.0) == 5.0
    assert module_0.poly([1.0, 2.0, 3.0], 2.0) == 17.0      # 1 + 2*2 + 3*2^2
    assert module_0.poly([1.0, 0.0, -1.0], 2.0) == -3.0     # 1 - x^2
    assert module_0.poly([2.0, 3.0], -1.0) == -1.0
    assert module_0.poly([1.0, 1.0], 0.0) == 1.0
    assert math.isclose(module_0.poly([0.5, 0.5], 0.5), 0.75)
    print("test_poly passed")


if __name__ == "__main__":
    test_poly()

# Generated at 2026-10-25 05:16:23.140877
# Unit test for function find_zero
def test_find_zero():
    # xÂ³ - 2 = 0, whose real root is â2
    coefficients = [-2, 0, 0, 1]

    root = module_0.find_zero(coefficients)
    expected = 2 ** (1 / 3)

    assert math.isclose(root, expected, rel_tol=0.0, abs_tol=1e-9)
    assert abs(poly(coefficients, root)) < 1e-9

# Generated at 2026-10-25 05:16:34.431684
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-0.5, 1.0], 0.5),          # x - 0.5
        ([3.0, 1.0], -3.0),          # x + 3
        ([-8.0, 0.0, 0.0, 1.0], 2.0)  # x^3 - 8
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, rel_tol=0.0, abs_tol=1e-9)
        assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 05:16:43.718977
# Unit test for function find_zero
def test_find_zero():
    # xÂ³ - 2 = 0, whose real root is â2
    coefficients = [-2.0, 0.0, 0.0, 1.0]

    result = module_0.find_zero(coefficients)
    expected = math.pow(2.0, 1.0 / 3.0)

    assert math.isclose(result, expected, abs_tol=1e-9)
    assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 05:16:46.149744
# Unit test for function find_zero

# Generated at 2026-10-25 05:16:48.786223
# Unit test for function find_zero

# Generated at 2026-10-25 05:16:51.250519
# Unit test for function find_zero

# Generated at 2026-10-25 05:16:53.678521
# Unit test for function find_zero

# Generated at 2026-10-25 05:16:56.447138
# Unit test for function find_zero

# Generated at 2026-10-25 05:16:58.887167
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:01.749192
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:03.893468
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:06.312976
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:08.750581
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:11.168204
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:13.587025
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:16.006754
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:18.427517
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:20.847214
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:23.267104
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:25.685800
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:28.103223
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:30.522238
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:32.940254
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:35.359594
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:37.780286
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:40.197451
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:42.617203
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:45.035329
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:47.453711
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:49.872738
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:52.290875
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:54.710440
# Unit test for function find_zero

# Generated at 2026-10-25 05:17:57.127504
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:04.905045
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:07.427387
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:09.910621
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:12.400550
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:14.861460
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:17.335517
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:19.816872
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:22.367663
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:24.826300
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:27.321084
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:29.812280
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:32.309030
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:34.800379
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:37.300293
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:39.793316
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:42.248639
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:44.749182
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:47.250641
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:49.737629
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:52.231674
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:54.721583
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:57.232354
# Unit test for function find_zero

# Generated at 2026-10-25 05:18:59.709052
# Unit test for function find_zero

# Generated at 2026-10-25 05:19:02.215993
# Unit test for function find_zero

# Generated at 2026-10-25 05:19:05.087336
# Unit test for function find_zero
def test_find_zero():cases = [
        ([1, 2], -0.5),          # 1 + 2x
        ([-6, 11, -6, 1], 1.0),  # (x-1)(x-2)(x-3)
        ([-2, 1], 2.0),          # x - 2
    ]

# Generated at 2026-10-25 05:19:17.503079
# Unit test for function find_zero
def test_find_zero():
    # p(x) = xÂ³ - 2, whose real root is â2
    xs = [-2.0, 0.0, 0.0, 1.0]

    result = module_0.find_zero(xs)
    expected = math.pow(2.0, 1.0 / 3.0)

    assert math.isclose(result, expected, abs_tol=1e-9)
    assert abs(poly(xs, result)) < 1e-8

# Generated at 2026-10-25 05:20:30.301336
# Unit test for function find_zero

# Generated at 2026-10-25 05:20:33.089567
# Unit test for function find_zero

# Generated at 2026-10-25 05:20:36.053942
# Unit test for function find_zero

# Generated at 2026-10-25 05:20:38.596166
# Unit test for function find_zero

# Generated at 2026-10-25 05:20:41.410505
# Unit test for function find_zero

# Generated at 2026-10-25 05:20:43.998041
# Unit test for function find_zero

# Generated at 2026-10-25 05:20:46.724036
# Unit test for function find_zero

# Generated at 2026-10-25 05:20:49.907657
# Unit test for function find_zero

# Generated at 2026-10-25 05:20:52.729101
# Unit test for function find_zero

# Generated at 2026-10-25 05:20:55.751496
# Unit test for function find_zero
def test_find_zero():cases = [
        ([1, 2], -0.5),          # 1 + 2x
        ([-6, 11, -6, 1], 1.0),  # (x-1)(x-2)(x-3)
        ([-2, 1], 2.0),          # x - 2
    ]

# Generated at 2026-10-25 05:21:13.754844
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([1.0, 2.0], -0.5),                  # 1 + 2x = 0
        ([-4.0, 1.0], 4.0),                  # x - 4 = 0
        ([-2.0, 0.0, 0.0, 1.0], 2 ** (1/3)), # x^3 - 2 = 0
        ([0.0, 1.0], 0.0),                   # x = 0
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 05:21:26.350976
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-3, 1], 3.0),                 # x - 3 = 0
        ([3, 1], -3.0),                 # x + 3 = 0
        ([0, 1], 0.0),                  # x = 0
        ([-2, 0, 0, 1], 2 ** (1 / 3)), # xÂ³ - 2 = 0
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 05:21:36.588165
# Unit test for function find_zero
def test_find_zero():
    test_cases = [
        ([-3, 2], 1.5),          # 2x - 3 = 0
        ([-2, 0, 0, 1], 2 ** (1 / 3)),  # x^3 - 2 = 0
        ([0, 1], 0.0),           # x = 0
        ([8, 0, 0, 1], -2.0),   # x^3 + 8 = 0
    ]

    for coefficients, expected in test_cases:
        result = module_0.find_zero(coefficients)

        assert math.isclose(result, expected, abs_tol=1e-9)
        assert abs(poly(coefficients, result)) < 1e-8

# Generated at 2026-10-25 05:21:39.576253
# Unit test for function find_zero

# Generated at 2026-10-25 05:21:42.520684
# Unit test for function find_zero

# Generated at 2026-10-25 05:21:45.461046
# Unit test for function find_zero

# Generated at 2026-10-25 05:21:48.566009
# Unit test for function find_zero

# Generated at 2026-10-25 05:21:51.299320
# Unit test for function find_zero

# Generated at 2026-10-25 05:21:53.952039
# Unit test for function find_zero

# Generated at 2026-10-25 05:21:57.195177
# Unit test for function find_zero

# Generated at 2026-10-25 05:22:04.384244
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-2.0, 1.0])