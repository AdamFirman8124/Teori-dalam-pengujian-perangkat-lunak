

# Generated at 2026-10-24 04:02:43.591166
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert module_0.mean_absolute_deviation([1, 2, 3, 4, 5]) == pytest.approx(1.2)
    assert module_0.mean_absolute_deviation([10]) == pytest.approx(0.0)
    assert module_0.mean_absolute_deviation([-2, 0, 2]) == pytest.approx(4 / 3)
    assert module_0.mean_absolute_deviation([5, 5, 5]) == pytest.approx(0.0)

# Generated at 2026-10-24 04:02:53.102247
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    tolerance = 1e-9

    assert abs(module_0.mean_absolute_deviation([1, 2, 3]) - (2 / 3)) < tolerance
    assert abs(module_0.mean_absolute_deviation([-2, 0, 2]) - (4 / 3)) < tolerance
    assert abs(module_0.mean_absolute_deviation([1, 2, 4, 8]) - 2.25) < tolerance
    assert module_0.mean_absolute_deviation([5, 5, 5]) == 0
    assert module_0.mean_absolute_deviation([7]) == 0

# Generated at 2026-10-24 04:02:59.336717
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert isclose(module_0.mean_absolute_deviation([1, 2, 3]), 2 / 3)
    assert isclose(module_0.mean_absolute_deviation([5, 5, 5]), 0.0)
    assert isclose(module_0.mean_absolute_deviation([-2, 0, 2]), 4 / 3)
    assert isclose(module_0.mean_absolute_deviation([1.5, 2.5]), 0.5)
    assert isclose(module_0.mean_absolute_deviation([10]), 0.0)

# Generated at 2026-10-24 04:03:07.324408
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert math.isclose(
        module_0.mean_absolute_deviation([1, 2, 3, 4, 5]),
        1.2,
    )
    assert math.isclose(
        module_0.mean_absolute_deviation([10, 10, 10]),
        0.0,
    )
    assert math.isclose(
        module_0.mean_absolute_deviation([5]),
        0.0,
    )

# Generated at 2026-10-24 04:03:14.197373
# Unit test for function mean_absolute_deviation
def test_mean_absolute_deviation():
    assert math.isclose(
        module_0.mean_absolute_deviation([1, 2, 3, 4, 5]),
        1.2,
    )
    assert math.isclose(
        module_0.mean_absolute_deviation([-2, -1, 0, 1, 2]),
        1.2,
    )
    assert module_0.mean_absolute_deviation([5]) == 0.0
    assert module_0.mean_absolute_deviation([3, 3, 3]) == 0.0