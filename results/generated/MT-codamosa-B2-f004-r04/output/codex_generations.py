

# Generated at 2026-10-25 08:09:13.844351
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

# Generated at 2026-10-25 08:09:15.266599
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

# Generated at 2026-10-25 08:09:16.643325
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

# Generated at 2026-10-25 08:09:18.031653
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

# Generated at 2026-10-25 08:09:19.477563
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