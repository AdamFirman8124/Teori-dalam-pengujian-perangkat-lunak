

# Generated at 2026-10-25 11:39:42.385889
# Unit test for function rescale_to_unit
def test_rescale_to_unit():
    # 1. Basic increasing list
    result = module_0.rescale_to_unit([1.0, 2.0, 3.0])
    assert len(result) == 3
    assert math.isclose(result[0], 0.0)
    assert math.isclose(result[1], 0.5)
    assert math.isclose(result[2], 1.0)

    # 2. Unsorted with negatives and duplicates
    result = module_0.rescale_to_unit([0, -10, 10, 0])
    # min=-10, max=10 -> [(0+10)/20, 0, 1, 0.5]
    assert math.isclose(result[0], 0.5)
    assert math.isclose(result[1], 0.0)
    assert math.isclose(result[2], 1.0)
    assert math.isclose(result[3], 0.5)

    # 3. Floats: min and max map to 0 and 1
    result = module_0.rescale_to_unit([2.5, 3.5, 5.0])
    assert min(result) == 0.0
    assert max(result) == 1.0

    # 4. Two elements
    assert module_0.rescale_to_unit([5, 10]) == [0.0, 1.0]

    # 5. Edge cases of current implementation:
    # empty list -> min() raises ValueError
    try:
        module_0.rescale_to_unit([])
        assert False, "should raise ValueError for []"
    except ValueError:
        pass

    # all equal / single element -> division by zero
    try:
        module_0.rescale_to_unit([5.0, 5.0, 5.0])
        assert False, "should raise ZeroDivisionError for equal values"
    except ZeroDivisionError:
        pass

# Generated at 2026-10-25 11:39:44.925026
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:39:47.440640
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:39:49.854707
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:39:52.270498
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:39:54.973028
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:39:57.386692
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:39:59.800770
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:40:02.603203
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:40:05.015854
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:40:07.429516
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:40:09.847443
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 11:40:12.260229
# Unit test for function rescale_to_unit