

# Generated at 2026-10-25 12:31:51.159147
# Unit test for function poly
def test_poly():
    assert module_0.poly([], 2.0) == 0
    assert module_0.poly([1], 100.0) == 1.0
    assert math.isclose(module_0.poly([1, 2, 3], 2.0), 17.0)  # 1 + 2*2 + 3*4
    assert math.isclose(module_0.poly([0, 1], 5.0), 5.0)      # x
    assert math.isclose(module_0.poly([2, -3, 1], 0.0), 2.0)  # constant term
    assert math.isclose(module_0.poly([0, 0, 1], 3.0), 9.0)   # x^2
    assert math.isclose(module_0.poly([1, 1], -1.0), 0.0)
    assert math.isclose(module_0.poly([-2, 0, 1, 1], 2.0), 10.0) # -2 + 4 + 8

# Generated at 2026-10-25 12:33:06.797168
# Unit test for function find_zero

# Generated at 2026-10-25 12:33:44.797685
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-0.5, 1.0])

# Generated at 2026-10-25 12:33:47.213401
# Unit test for function find_zero

# Generated at 2026-10-25 12:33:49.627674
# Unit test for function find_zero

# Generated at 2026-10-25 12:33:52.043159
# Unit test for function find_zero

# Generated at 2026-10-25 12:33:54.456164
# Unit test for function find_zero

# Generated at 2026-10-25 12:33:56.872855
# Unit test for function find_zero

# Generated at 2026-10-25 12:33:59.290813
# Unit test for function find_zero

# Generated at 2026-10-25 12:34:01.699640
# Unit test for function find_zero

# Generated at 2026-10-25 12:34:04.111179
# Unit test for function find_zero

# Generated at 2026-10-25 12:34:06.525263
# Unit test for function find_zero

# Generated at 2026-10-25 12:34:24.331201
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

# Generated at 2026-10-25 12:34:32.441058
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

# Generated at 2026-10-25 12:34:33.945960
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

# Generated at 2026-10-25 12:34:50.632542
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

# Generated at 2026-10-25 12:34:53.071140
# Unit test for function find_zero

# Generated at 2026-10-25 12:34:55.862949
# Unit test for function find_zero

# Generated at 2026-10-25 12:34:58.431793
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:01.068235
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:03.600988
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:06.176119
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:08.704018
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:11.352894
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:13.880669
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:16.464634
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:18.963038
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:21.562035
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:24.058112
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:26.600872
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:29.158904
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:31.718312
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:34.252787
# Unit test for function find_zero

# Generated at 2026-10-25 12:35:37.043375
# Unit test for function find_zero
def test_find_zero():assert abs(module_0.find_zero([-1, 1]) - 1.0) < 1e-9

# Generated at 2026-10-25 12:35:39.891028
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

# Generated at 2026-10-25 12:35:43.110494
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

# Generated at 2026-10-25 12:36:06.337823
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

# Generated at 2026-10-25 12:36:08.825468
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:11.345584
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:14.026269
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:16.704976
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:19.232566
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:21.756148
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:24.224408
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:26.775336
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:29.334499
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:31.823177
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:34.371979
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:36.919935
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:39.462666
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:42.053853
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:44.480999
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:47.011040
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:49.662598
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:52.345441
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:54.875110
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:57.427579
# Unit test for function find_zero

# Generated at 2026-10-25 12:36:59.919331
# Unit test for function find_zero

# Generated at 2026-10-25 12:37:36.235124
# Unit test for function find_zero
def test_find_zero():
    # Linear: 1 + 2x = 0 -> root at x = -0.5 (already inside [-1, 1])
    xs = [1, 2]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6
    assert abs(x - (-0.5)) < 1e-6

    # Linear: 3 - x = 0 -> root at x = 3 (forces bracket expansion to the right)
    xs = [3, -1]
    x = module_0.find_zero(xs)
    assert abs(poly(xs, x)) < 1e-6
    assert abs(x - 3.0) < 1e-6

    # Linear: -20 + x = 0 -> root at x = 20 (forces large bracket expansion)

# Generated at 2026-10-25 12:37:38.964222
# Unit test for function find_zero

# Generated at 2026-10-25 12:37:41.721858
# Unit test for function find_zero

# Generated at 2026-10-25 12:37:44.310107
# Unit test for function find_zero

# Generated at 2026-10-25 12:37:46.931315
# Unit test for function find_zero

# Generated at 2026-10-25 12:37:49.522189
# Unit test for function find_zero

# Generated at 2026-10-25 12:37:52.342133
# Unit test for function find_zero

# Generated at 2026-10-25 12:37:55.132082
# Unit test for function find_zero

# Generated at 2026-10-25 12:37:57.640378
# Unit test for function find_zero

# Generated at 2026-10-25 12:38:00.276019
# Unit test for function find_zero

# Generated at 2026-10-25 12:38:02.808521
# Unit test for function find_zero

# Generated at 2026-10-25 12:38:15.739886
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-4.0, 1.0])
assert abs(result - 4.0) < 1e-10

# Generated at 2026-10-25 12:38:32.263178
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

# Generated at 2026-10-25 12:38:40.341764
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

# Generated at 2026-10-25 12:38:43.107457
# Unit test for function find_zero

# Generated at 2026-10-25 12:38:45.720250
# Unit test for function find_zero

# Generated at 2026-10-25 12:38:48.197507
# Unit test for function find_zero

# Generated at 2026-10-25 12:38:51.071454
# Unit test for function find_zero

# Generated at 2026-10-25 12:38:53.435327
# Unit test for function find_zero

# Generated at 2026-10-25 12:38:56.161594
# Unit test for function find_zero

# Generated at 2026-10-25 12:38:58.741391
# Unit test for function find_zero

# Generated at 2026-10-25 12:39:01.259986
# Unit test for function find_zero

# Generated at 2026-10-25 12:39:03.824463
# Unit test for function find_zero

# Generated at 2026-10-25 12:40:57.653943
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:00.341750
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:03.247781
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:05.832457
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:08.378433
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:11.396221
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:14.274711
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:17.262873
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:19.881210
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:22.638693
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:25.095479
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:28.026464
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:30.762016
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:33.429991
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:36.080886
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:38.956171
# Unit test for function find_zero

# Generated at 2026-10-25 12:41:42.143567
# Unit test for function find_zero
def test_find_zero():
    assert abs(module_0.find_zero([-1.0, 1.0]) - 1.0) < 1e-6

# Generated at 2026-10-25 12:41:58.756478
# Unit test for function find_zero
def test_find_zero():
    # x - 2  -> root at 2
    xs = [-2.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(z - 2.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # x^2 - 1  -> roots at Â±1 (converges to -1)
    xs = [-1.0, 0.0, 1.0]
    z = module_0.find_zero(xs)
    assert abs(abs(z) - 1.0) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6

    # 2x + 1  -> root at -0.5
    xs = [1.0, 2.0]
    z = module_0.find_zero(xs)
    assert abs(z + 0.5) < 1e-6, z
    assert abs(poly(xs, z)) < 1e-6