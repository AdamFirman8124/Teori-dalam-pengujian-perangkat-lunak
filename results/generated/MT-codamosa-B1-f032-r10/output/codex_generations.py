

# Generated at 2026-10-25 11:50:31.753501
# Unit test for function poly

# Generated at 2026-10-25 11:50:34.311686
# Unit test for function poly

# Generated at 2026-10-25 11:50:37.037994
# Unit test for function poly

# Generated at 2026-10-25 11:50:39.460135
# Unit test for function poly

# Generated at 2026-10-25 11:50:42.254757
# Unit test for function poly

# Generated at 2026-10-25 11:50:44.676962
# Unit test for function poly

# Generated at 2026-10-25 11:50:47.088832
# Unit test for function poly

# Generated at 2026-10-25 11:50:53.984766
# Unit test for function poly
def test_poly():assert module_0.poly([1.0, 2.0, 3.0], 2.0) == 17.0

# Generated at 2026-10-25 11:50:55.701095
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

# Generated at 2026-10-25 11:51:00.683756
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

# Generated at 2026-10-25 11:51:20.140906
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

# Generated at 2026-10-25 11:51:39.474695
# Unit test for function find_zero

# Generated at 2026-10-25 11:51:41.889042
# Unit test for function find_zero

# Generated at 2026-10-25 11:51:44.364116
# Unit test for function find_zero

# Generated at 2026-10-25 11:51:46.733327
# Unit test for function find_zero

# Generated at 2026-10-25 11:51:49.148512
# Unit test for function find_zero

# Generated at 2026-10-25 11:51:51.561704
# Unit test for function find_zero

# Generated at 2026-10-25 11:51:53.975988
# Unit test for function find_zero

# Generated at 2026-10-25 11:51:56.388819
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:08.408195
# Unit test for function find_zero
def test_find_zero():assert abs(module_0.find_zero([-1, 1]) - 1.0) < 1e-9

# Generated at 2026-10-25 11:52:09.874186
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

# Generated at 2026-10-25 11:52:31.415194
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

# Generated at 2026-10-25 11:52:33.831383
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:36.245561
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:38.660045
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:41.073559
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:43.487800
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:45.936430
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:48.350601
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:50.765201
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:53.179578
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:55.593593
# Unit test for function find_zero

# Generated at 2026-10-25 11:52:58.039942
# Unit test for function find_zero

# Generated at 2026-10-25 11:53:00.420434
# Unit test for function find_zero

# Generated at 2026-10-25 11:53:39.852590
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

# Generated at 2026-10-25 11:53:41.419627
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

# Generated at 2026-10-25 11:53:42.816963
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

# Generated at 2026-10-25 11:53:44.531877
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

# Generated at 2026-10-25 11:53:45.988133
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

# Generated at 2026-10-25 11:53:47.392284
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

# Generated at 2026-10-25 11:53:50.125343
# Unit test for function find_zero

# Generated at 2026-10-25 11:53:52.585123
# Unit test for function find_zero

# Generated at 2026-10-25 11:53:55.276699
# Unit test for function find_zero

# Generated at 2026-10-25 11:53:57.753678
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:00.279000
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:03.122687
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:05.860025
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:08.360285
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:10.832297
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:13.339927
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:15.826003
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:18.318990
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:21.249929
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:23.745180
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:26.335169
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:28.813263
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:31.298671
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:33.823890
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:36.307425
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:38.780253
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:41.280919
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:43.767133
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:46.244857
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:48.747922
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:51.231355
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:53.819110
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:56.289285
# Unit test for function find_zero

# Generated at 2026-10-25 11:54:58.813325
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:01.301915
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:03.778952
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:06.280649
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:08.778861
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:11.297742
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:13.760290
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:16.244575
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:18.734060
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:21.233286
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:23.716005
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:26.184931
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:28.678141
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:31.166585
# Unit test for function find_zero

# Generated at 2026-10-25 11:55:33.675745
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:05.162085
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:07.647228
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:10.146524
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:12.665742
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:15.176552
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:17.692458
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:20.146360
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:22.694789
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:25.126443
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:27.656247
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:30.238246
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:32.919532
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:35.300736
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:37.797701
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:40.292153
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:42.834033
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:45.283588
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:47.810156
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:50.283673
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:52.742567
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:55.270762
# Unit test for function find_zero

# Generated at 2026-10-25 11:56:57.768038
# Unit test for function find_zero

# Generated at 2026-10-25 11:57:00.225310
# Unit test for function find_zero

# Generated at 2026-10-25 11:57:02.792057
# Unit test for function find_zero

# Generated at 2026-10-25 11:57:05.261497
# Unit test for function find_zero

# Generated at 2026-10-25 11:57:07.776351
# Unit test for function find_zero

# Generated at 2026-10-25 11:57:10.314256
# Unit test for function find_zero

# Generated at 2026-10-25 11:57:12.804839
# Unit test for function find_zero

# Generated at 2026-10-25 11:57:15.291777
# Unit test for function find_zero

# Generated at 2026-10-25 11:57:17.776339
# Unit test for function find_zero