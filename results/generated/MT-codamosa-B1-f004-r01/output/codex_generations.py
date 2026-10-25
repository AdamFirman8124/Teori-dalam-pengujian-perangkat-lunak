

# Generated at 2026-10-25 02:17:49.160237
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.2)
    assert module_0.mean_absolute_deviation([10, 10, 10]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-1, 0, 1]) == pytest.approx(2 / 3)
    assert module_0.mean_absolute_deviation([5]) == pytest.approx(0.0)

# Generated at 2026-10-25 02:17:54.587662
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3]) == pytest.approx(2 / 3)
    assert module_0.mean_absolute_deviation([-2, 0, 2]) == pytest.approx(4 / 3)
    assert module_0.mean_absolute_deviation([5, 5, 5]) == 0
    assert module_0.mean_absolute_deviation([10]) == 0

    with pytest.raises(ZeroDivisionError):
        module_0.mean_absolute_deviation([])

# Generated at 2026-10-25 02:18:00.742934
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert isclose(module_0.mean_absolute_deviation([1, 2, 3]), 2 / 3)
    assert isclose(module_0.mean_absolute_deviation([1, 1, 1]), 0.0)
    assert isclose(module_0.mean_absolute_deviation([-2, 0, 2]), 4 / 3)
    assert isclose(module_0.mean_absolute_deviation([5]), 0.0)
    assert isclose(module_0.mean_absolute_deviation([1.5, 2.5, 3.5]), 2 / 3)

# Generated at 2026-10-25 02:18:06.232535
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert abs(module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) - 1.2) < 1e-9
    assert abs(module_0.mean_absolute_deviation([-1, 0, 1]) - (2 / 3)) < 1e-9
    assert module_0.mean_absolute_deviation([5, 5, 5]) == 0.0
    assert module_0.mean_absolute_deviation([42]) == 0.0

# Generated at 2026-10-25 02:18:12.609366
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.2)
    assert module_0.mean_absolute_deviation([10, 10, 10]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-2, 0, 2]) == pytest.approx(4 / 3)
    assert module_0.mean_absolute_deviation([7]) == pytest.approx(0.0)

    with pytest.raises(ZeroDivisionError):
        module_0.mean_absolute_deviation([])