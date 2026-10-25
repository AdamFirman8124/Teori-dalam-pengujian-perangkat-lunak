

# Generated at 2026-10-24 22:35:02.293779
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    assert module_0.rescale_to_unit([2.0, 4.0, 6.0]) == [0.0, 0.5, 1.0]
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == [0.0, 0.5, 1.0]
    assert module_0.rescale_to_unit([10.0, 0.0, 5.0]) == [1.0, 0.0, 0.5]

# Generated at 2026-10-24 22:35:07.640302
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]

    assert module_0.rescale_to_unit(numbers) == expected

# Generated at 2026-10-24 22:35:12.863330
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    numbers = [1.0, 2.0, 3.0]
    expected = [0.0, 0.5, 1.0]

    assert module_0.rescale_to_unit(numbers) == expected

# Generated at 2026-10-24 22:35:18.791067
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0]) == pytest.approx(
        [0.0, 0.5, 1.0]
    )
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == pytest.approx(
        [0.0, 0.5, 1.0]
    )
    assert module_0.rescale_to_unit([10.0, 0.0, 5.0]) == pytest.approx(
        [1.0, 0.0, 0.5]
    )
    assert module_0.rescale_to_unit([2.0, 4.0]) == pytest.approx(
        [0.0, 1.0]
    )

# Generated at 2026-10-24 22:35:25.356848
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    assert module_0.rescale_to_unit([1.0, 2.0, 3.0]) == pytest.approx(
        [0.0, 0.5, 1.0]
    )
    assert module_0.rescale_to_unit([-5.0, 0.0, 5.0]) == pytest.approx(
        [0.0, 0.5, 1.0]
    )
    assert module_0.rescale_to_unit([10.0, 5.0, 0.0]) == pytest.approx(
        [1.0, 0.5, 0.0]
    )