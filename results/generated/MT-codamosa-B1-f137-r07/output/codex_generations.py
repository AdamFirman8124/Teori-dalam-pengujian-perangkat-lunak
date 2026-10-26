

# Generated at 2026-10-25 07:34:05.229151
# Unit test for function compare_one

# Generated at 2026-10-25 07:34:07.700936
# Unit test for function compare_one

# Generated at 2026-10-25 07:34:10.062943
# Unit test for function compare_one

# Generated at 2026-10-25 07:34:12.475077
# Unit test for function compare_one

# Generated at 2026-10-25 07:34:14.891382
# Unit test for function compare_one

# Generated at 2026-10-25 07:34:25.785581
# Unit test for function compare_one
def test_compare_one():assert module_0.compare_one(1, 2) == 2

# Generated at 2026-10-25 07:34:55.588704
# Unit test for function compare_one
def test_compare_one():
    # ints / floats
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(5, 3) == 5
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(2.5, 2.5) is None

    # numeric strings
    assert module_0.compare_one("1", "2") == "2"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1.5", "2.5") == "2.5"

    # comma vs dot are equal
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one("1,0", "1.0") is None
    assert module_0.compare_one("1,5", "1.5") is None

    # mixed types, returns original value/type
    assert module_0.compare_one(1, "2,3") == "2,3"

# Generated at 2026-10-25 07:34:58.007313
# Unit test for function compare_one

# Generated at 2026-10-25 07:35:00.421757
# Unit test for function compare_one

# Generated at 2026-10-25 07:35:02.839554
# Unit test for function compare_one

# Generated at 2026-10-25 07:35:05.256427
# Unit test for function compare_one

# Generated at 2026-10-25 07:35:07.669988
# Unit test for function compare_one

# Generated at 2026-10-25 07:35:10.086034
# Unit test for function compare_one