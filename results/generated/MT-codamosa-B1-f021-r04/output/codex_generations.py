

# Generated at 2026-10-25 07:51:20.638186
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

# Generated at 2026-10-25 07:51:23.165354
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 07:51:25.784046
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 07:51:28.201941
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 07:51:30.658573
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 07:52:24.588001
# Unit test for function rescale_to_unit
def test_rescale_to_unit():assert module_0.rescale_to_unit([0, 5, 10]) == [0.0, 0.5, 1.0]

# Generated at 2026-10-25 07:52:27.145368
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 07:52:29.571895
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 07:52:31.988929
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 07:52:34.405329
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 07:52:36.817334
# Unit test for function rescale_to_unit

# Generated at 2026-10-25 07:52:39.234154
# Unit test for function rescale_to_unit