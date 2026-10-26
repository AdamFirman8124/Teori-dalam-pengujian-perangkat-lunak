

# Generated at 2026-10-25 10:14:18.918469
# Unit test for function find_zero

# Generated at 2026-10-25 10:14:21.332979
# Unit test for function find_zero

# Generated at 2026-10-25 10:14:23.748387
# Unit test for function find_zero

# Generated at 2026-10-25 10:14:26.162240
# Unit test for function find_zero

# Generated at 2026-10-25 10:14:28.577416
# Unit test for function find_zero

# Generated at 2026-10-25 10:14:30.991754
# Unit test for function find_zero

# Generated at 2026-10-25 10:14:33.408847
# Unit test for function poly

# Generated at 2026-10-25 10:14:35.825474
# Unit test for function poly

# Generated at 2026-10-25 10:14:38.240883
# Unit test for function poly

# Generated at 2026-10-25 10:14:49.571590
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

# Generated at 2026-10-25 10:15:56.944783
# Unit test for function find_zero

# Generated at 2026-10-25 10:16:08.240872
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-2.0, 1.0])

# Generated at 2026-10-25 10:16:39.457090
# Unit test for function find_zero
def test_find_zero():assert math.isclose(module_0.find_zero([-0.25, 1.0]), 0.25, abs_tol=1e-9)

# Generated at 2026-10-25 10:17:16.332635
# Unit test for function find_zero
def test_find_zero():assert abs(module_0.find_zero([-2.0, 1.0]) - 2.0) < 1e-9

# Generated at 2026-10-25 10:18:02.512780
# Unit test for function find_zero

# Generated at 2026-10-25 10:18:39.966264
# Unit test for function find_zero
def test_find_zero():
    assert abs(module_0.find_zero([-1.0, 1.0]) - 1.0) < 1e-6

# Generated at 2026-10-25 10:18:42.443069
# Unit test for function find_zero

# Generated at 2026-10-25 10:18:44.933360
# Unit test for function find_zero

# Generated at 2026-10-25 10:18:47.410779
# Unit test for function find_zero

# Generated at 2026-10-25 10:19:05.480530
# Unit test for function find_zero

# Generated at 2026-10-25 10:19:08.491517
# Unit test for function find_zero
def test_find_zero():
    assert abs(module_0.find_zero([-1.0, 1.0]) - 1.0) < 1e-6

# Generated at 2026-10-25 10:19:13.060485
# Unit test for function find_zero

# Generated at 2026-10-25 10:19:16.122616
# Unit test for function find_zero
def test_find_zero():
    assert abs(module_0.find_zero([-1.0, 1.0]) - 1.0) < 1e-6

# Generated at 2026-10-25 10:19:22.875954
# Unit test for function find_zero

# Generated at 2026-10-25 10:19:31.292132
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-3.0, 1.0])

# Generated at 2026-10-25 10:19:49.229368
# Unit test for function find_zero

# Generated at 2026-10-25 10:19:51.736631
# Unit test for function find_zero

# Generated at 2026-10-25 10:19:54.214933
# Unit test for function find_zero

# Generated at 2026-10-25 10:20:34.763048
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

# Generated at 2026-10-25 10:20:57.810465
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

# Generated at 2026-10-25 10:21:33.591825
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:36.106188
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:38.635838
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:41.242381
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:43.747926
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:46.443056
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:49.046171
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:51.603678
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:54.149308
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:56.729608
# Unit test for function find_zero

# Generated at 2026-10-25 10:21:59.268379
# Unit test for function find_zero

# Generated at 2026-10-25 10:22:01.820426
# Unit test for function find_zero

# Generated at 2026-10-25 10:22:04.357013
# Unit test for function find_zero

# Generated at 2026-10-25 10:22:20.368628
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-2.0, 1.0])

# Generated at 2026-10-25 10:22:36.942253
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

# Generated at 2026-10-25 10:22:53.475698
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

# Generated at 2026-10-25 10:23:37.677620
# Unit test for function find_zero
def test_find_zero():assert math.isclose(module_0.find_zero([-2.0, 1.0]), 2.0, abs_tol=1e-9)

# Generated at 2026-10-25 10:23:55.541508
# Unit test for function find_zero

# Generated at 2026-10-25 10:23:58.283189
# Unit test for function find_zero

# Generated at 2026-10-25 10:24:00.881721
# Unit test for function find_zero

# Generated at 2026-10-25 10:24:03.386292
# Unit test for function find_zero

# Generated at 2026-10-25 10:24:05.989771
# Unit test for function find_zero

# Generated at 2026-10-25 10:24:08.791251
# Unit test for function find_zero