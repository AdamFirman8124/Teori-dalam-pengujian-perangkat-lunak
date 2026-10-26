

# Generated at 2026-10-25 10:18:26.794142
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # mean = 3, (2+1+0+1+2)/5 = 1.2
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2

    # single element -> 0 deviation
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # all identical -> 0 deviation
    assert module_0.mean_absolute_deviation([2, 2, 2, 2]) == 0.0

    # mean = 15, (5+5)/2 = 5.0
    assert module_0.mean_absolute_deviation([10, 20]) == 5.0

    # mean = 0, (1+0+1)/3 = 0.666...
    assert abs(module_0.mean_absolute_deviation([-1, 0, 1]) - 2/3) < 1e-9

# Generated at 2026-10-25 10:18:28.165222
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # mean = 3, (2+1+0+1+2)/5 = 1.2
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2

    # single element -> 0 deviation
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # all identical -> 0 deviation
    assert module_0.mean_absolute_deviation([2, 2, 2, 2]) == 0.0

    # mean = 15, (5+5)/2 = 5.0
    assert module_0.mean_absolute_deviation([10, 20]) == 5.0

    # mean = 0, (1+0+1)/3 = 0.666...
    assert abs(module_0.mean_absolute_deviation([-1, 0, 1]) - 2/3) < 1e-9

# Generated at 2026-10-25 10:18:29.585209
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # mean = 3, (2+1+0+1+2)/5 = 1.2
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2

    # single element -> 0 deviation
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # all identical -> 0 deviation
    assert module_0.mean_absolute_deviation([2, 2, 2, 2]) == 0.0

    # mean = 15, (5+5)/2 = 5.0
    assert module_0.mean_absolute_deviation([10, 20]) == 5.0

    # mean = 0, (1+0+1)/3 = 0.666...
    assert abs(module_0.mean_absolute_deviation([-1, 0, 1]) - 2/3) < 1e-9

# Generated at 2026-10-25 10:18:31.086062
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # mean = 3, (2+1+0+1+2)/5 = 1.2
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2

    # single element -> 0 deviation
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # all identical -> 0 deviation
    assert module_0.mean_absolute_deviation([2, 2, 2, 2]) == 0.0

    # mean = 15, (5+5)/2 = 5.0
    assert module_0.mean_absolute_deviation([10, 20]) == 5.0

    # mean = 0, (1+0+1)/3 = 0.666...
    assert abs(module_0.mean_absolute_deviation([-1, 0, 1]) - 2/3) < 1e-9

# Generated at 2026-10-25 10:18:32.517114
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    # mean = 3, (2+1+0+1+2)/5 = 1.2
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == 1.2

    # single element -> 0 deviation
    assert module_0.mean_absolute_deviation([5.0]) == 0.0

    # all identical -> 0 deviation
    assert module_0.mean_absolute_deviation([2, 2, 2, 2]) == 0.0

    # mean = 15, (5+5)/2 = 5.0
    assert module_0.mean_absolute_deviation([10, 20]) == 5.0

    # mean = 0, (1+0+1)/3 = 0.666...
    assert abs(module_0.mean_absolute_deviation([-1, 0, 1]) - 2/3) < 1e-9