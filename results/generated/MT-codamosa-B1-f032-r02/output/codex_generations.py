

# Generated at 2026-10-25 06:18:56.699490
# Unit test for function find_zero

# Generated at 2026-10-25 06:18:59.101522
# Unit test for function find_zero

# Generated at 2026-10-25 06:19:05.595428
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: 2x - 3 = 0 -> root at 1.5
    xs1 = [2.0, -3.0]
    root1 = module_0.find_zero(xs1)
    assert abs(poly(xs1, root1)) < 1e-6

    # Quadratic polynomial: x^2 - 4 = 0 -> root at 2 or -2
    xs2 = [-4.0, 0.0, 1.0]
    root2 = module_0.find_zero(xs2)
    assert abs(poly(xs2, root2)) < 1e-6
    assert abs(abs(root2) - 2.0) < 1e-6

    # Cubic polynomial: (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6
    xs3 = [-6.0, 11.0, -6.0, 1.0]
    root3 = module_0.find_zero(xs3)
    assert abs(poly(xs3, root3)) < 1e-6

    # Polynomial with root at zero: 5x = 0 -> root at 0
    xs4 = [0.0, 5.0]
    root4 = module_0.find_zero(xs4)
    assert abs(root4) < 1e-6

# Generated at 2026-10-25 06:19:25.885569
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

# Generated at 2026-10-25 06:19:28.317539
# Unit test for function poly

# Generated at 2026-10-25 06:19:30.731409
# Unit test for function poly

# Generated at 2026-10-25 06:19:33.145267
# Unit test for function poly

# Generated at 2026-10-25 06:19:35.563644
# Unit test for function find_zero

# Generated at 2026-10-25 06:19:37.978114
# Unit test for function find_zero

# Generated at 2026-10-25 06:19:40.560852
# Unit test for function find_zero

# Generated at 2026-10-25 06:19:42.979581
# Unit test for function poly

# Generated at 2026-10-25 06:19:45.399152
# Unit test for function poly

# Generated at 2026-10-25 06:19:47.813825
# Unit test for function poly

# Generated at 2026-10-25 06:20:15.835052
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

# Generated at 2026-10-25 06:20:17.282379
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

# Generated at 2026-10-25 06:20:18.824084
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

# Generated at 2026-10-25 06:20:20.251427
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

# Generated at 2026-10-25 06:20:21.727552
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

# Generated at 2026-10-25 06:20:23.165975
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

# Generated at 2026-10-25 06:20:24.644866
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

# Generated at 2026-10-25 06:20:26.097427
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

# Generated at 2026-10-25 06:20:27.556345
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

# Generated at 2026-10-25 06:20:28.931888
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

# Generated at 2026-10-25 06:22:38.815196
# Unit test for function find_zero

# Generated at 2026-10-25 06:22:51.133061
# Unit test for function find_zero
def test_find_zero():assert abs(module_0.find_zero([-2, 1]) - 2.0) < 1e-9

# Generated at 2026-10-25 06:22:52.778257
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

# Generated at 2026-10-25 06:22:54.364255
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

# Generated at 2026-10-25 06:22:55.803487
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

# Generated at 2026-10-25 06:22:57.216097
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

# Generated at 2026-10-25 06:22:58.858458
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

# Generated at 2026-10-25 06:23:00.171869
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

# Generated at 2026-10-25 06:23:01.730038
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

# Generated at 2026-10-25 06:23:03.205587
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

# Generated at 2026-10-25 06:23:04.604796
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

# Generated at 2026-10-25 06:24:19.303352
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

# Generated at 2026-10-25 06:24:20.728988
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

# Generated at 2026-10-25 06:24:22.401823
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

# Generated at 2026-10-25 06:24:25.089686
# Unit test for function find_zero

# Generated at 2026-10-25 06:24:27.852877
# Unit test for function find_zero

# Generated at 2026-10-25 06:24:31.036335
# Unit test for function find_zero

# Generated at 2026-10-25 06:24:33.906864
# Unit test for function find_zero

# Generated at 2026-10-25 06:24:35.402197
# Unit test for function find_zero
def test_find_zero():
    # Linear polynomial: 2x - 3 = 0 -> root at 1.5
    xs1 = [2.0, -3.0]
    root1 = module_0.find_zero(xs1)
    assert abs(poly(xs1, root1)) < 1e-6

    # Quadratic polynomial: x^2 - 4 = 0 -> root at 2 or -2
    xs2 = [-4.0, 0.0, 1.0]
    root2 = module_0.find_zero(xs2)
    assert abs(poly(xs2, root2)) < 1e-6
    assert abs(abs(root2) - 2.0) < 1e-6

    # Cubic polynomial: (x-1)(x-2)(x-3) = x^3 - 6x^2 + 11x - 6
    xs3 = [-6.0, 11.0, -6.0, 1.0]
    root3 = module_0.find_zero(xs3)
    assert abs(poly(xs3, root3)) < 1e-6

    # Polynomial with root at zero: 5x = 0 -> root at 0
    xs4 = [0.0, 5.0]
    root4 = module_0.find_zero(xs4)
    assert abs(root4) < 1e-6

# Generated at 2026-10-25 06:24:37.139727
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

# Generated at 2026-10-25 06:24:38.641129
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

# Generated at 2026-10-25 06:24:40.160035
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

# Generated at 2026-10-25 06:24:41.740211
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

# Generated at 2026-10-25 06:24:43.470864
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

# Generated at 2026-10-25 06:26:17.935352
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:20.860767
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:23.454885
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:26.722563
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:29.326611
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:31.983054
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:34.961195
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:37.546141
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:40.551019
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:43.761358
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:46.262722
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:48.999090
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:51.782760
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:54.646125
# Unit test for function find_zero

# Generated at 2026-10-25 06:26:57.576987
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:00.375127
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:03.319853
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:06.068198
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:08.891933
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:11.850333
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:14.267286
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:16.903036
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:20.085365
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:22.600293
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:25.784205
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:28.230799
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:30.793985
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:33.385105
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:36.483920
# Unit test for function find_zero

# Generated at 2026-10-25 06:27:39.153880
# Unit test for function find_zero