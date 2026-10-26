

# Generated at 2026-10-25 11:33:22.801312
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

# Generated at 2026-10-25 11:33:25.352064
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:27.766117
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:30.180933
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:32.601470
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:35.296516
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:37.707638
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:40.124116
# Unit test for function poly

# Generated at 2026-10-25 11:33:42.537481
# Unit test for function poly

# Generated at 2026-10-25 11:33:44.954537
# Unit test for function poly

# Generated at 2026-10-25 11:33:47.366476
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:49.784079
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:52.196865
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:54.609538
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:57.024125
# Unit test for function find_zero

# Generated at 2026-10-25 11:33:59.439471
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:01.852860
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:04.268455
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:06.739859
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:09.106479
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:11.522181
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:13.936674
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:16.350066
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:18.767433
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:21.182312
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:23.597222
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:26.011634
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:28.425226
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:30.839008
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:33.258134
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:35.674609
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:38.100273
# Unit test for function find_zero

# Generated at 2026-10-25 11:34:47.774691
# Unit test for function find_zero
def test_find_zero():result = module_0.find_zero([-0.5, 1.0])

# Generated at 2026-10-25 11:35:04.278848
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

# Generated at 2026-10-25 11:35:06.694251
# Unit test for function find_zero

# Generated at 2026-10-25 11:35:09.301094
# Unit test for function find_zero

# Generated at 2026-10-25 11:35:11.717164
# Unit test for function find_zero

# Generated at 2026-10-25 11:35:14.134378
# Unit test for function find_zero

# Generated at 2026-10-25 11:35:16.556807
# Unit test for function find_zero

# Generated at 2026-10-25 11:35:18.968225
# Unit test for function find_zero

# Generated at 2026-10-25 11:35:58.192337
# Unit test for function find_zero

# Generated at 2026-10-25 11:36:00.658251
# Unit test for function find_zero

# Generated at 2026-10-25 11:36:03.321732
# Unit test for function find_zero

# Generated at 2026-10-25 11:36:05.833023
# Unit test for function find_zero

# Generated at 2026-10-25 11:36:08.748259
# Unit test for function find_zero
def test_find_zero():
    assert abs(module_0.find_zero([-1.0, 1.0]) - 1.0) < 1e-6

# Generated at 2026-10-25 11:36:12.892562
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

# Generated at 2026-10-25 11:36:15.659564
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

# Generated at 2026-10-25 11:36:32.188843
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

# Generated at 2026-10-25 11:37:53.839899
# Unit test for function find_zero

# Generated at 2026-10-25 11:37:56.343437
# Unit test for function find_zero

# Generated at 2026-10-25 11:37:58.870067
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:01.303710
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:03.812673
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:06.292498
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:08.973089
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:11.478968
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:14.012836
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:16.448363
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:18.983751
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:21.560689
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:24.234808
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:26.697021
# Unit test for function find_zero

# Generated at 2026-10-25 11:38:29.231311
# Unit test for function find_zero

# Generated at 2026-10-25 11:39:43.967742
# Unit test for function find_zero

# Generated at 2026-10-25 11:39:46.625992
# Unit test for function find_zero

# Generated at 2026-10-25 11:39:49.256674
# Unit test for function find_zero

# Generated at 2026-10-25 11:39:51.853142
# Unit test for function find_zero

# Generated at 2026-10-25 11:39:54.540106
# Unit test for function find_zero

# Generated at 2026-10-25 11:39:57.093900
# Unit test for function find_zero

# Generated at 2026-10-25 11:39:59.680322
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:02.649540
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:05.309982
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:08.006171
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:10.716799
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:13.348863
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:15.748894
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:18.360973
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:20.900997
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:23.469883
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:26.063774
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:28.594662
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:31.171148
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:33.743292
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:36.237065
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:38.901606
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:41.324988
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:43.911625
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:46.559679
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:49.053470
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:51.901320
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:54.358560
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:56.837473
# Unit test for function find_zero

# Generated at 2026-10-25 11:40:59.504272
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:25.122062
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:28.265110
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:30.744017
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:33.421389
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:36.263627
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:39.209430
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:41.638449
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:44.421929
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:47.102313
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:49.694913
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:52.148445
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:55.108359
# Unit test for function find_zero

# Generated at 2026-10-25 11:42:57.938285
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:00.730433
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:03.380736
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:06.115223
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:08.732505
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:11.403819
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:14.292179
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:16.924564
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:19.661962
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:22.312478
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:25.101468
# Unit test for function find_zero

# Generated at 2026-10-25 11:43:27.672559
# Unit test for function find_zero