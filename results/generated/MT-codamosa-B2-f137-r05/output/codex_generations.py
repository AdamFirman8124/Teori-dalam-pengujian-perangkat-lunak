

# Generated at 2026-10-24 15:46:37.574983
# Unit test for function compare_one
def test_compare_one():
    # int vs int
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(5, 3) == 5
    assert module_0.compare_one(1, 1) is None

    # float vs float
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(3.2, 1.1) == 3.2
    assert module_0.compare_one(2.0, 2.0) is None

    # int vs float - equal values return None
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(5, 2.5) == 5
    assert module_0.compare_one(1, 1.0) is None

    # numeric strings with dot
    assert module_0.compare_one("1.5", "2.5") == "2.5"
    assert module_0.compare_one("5.0", 4) == "5.0"
    assert module_0.compare_one(4, "5.0") == "5.0"
    assert module_0.compare_one("1", "1.0") is None

    # numeric strings with comma as decimal separator
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("1,5", 1.4) == "1,5"
    assert module_0.compare_one("1,2", 1.5) == 1.5
    assert module_0.compare_one("1,0", "1.0") is None
    assert module_0.compare_one("1,0", 1) is None

    # returns original value, not converted temp value
    assert module_0.compare_one("1,9", 2) == 2
    result = module_0.compare_one(5, "6,0")
    assert result == "6,0" and isinstance(result, str)

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -1.4) == -1.4

# Generated at 2026-10-24 15:47:06.040479
# Unit test for function compare_one
def test_compare_one():
    # int vs int
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(5, 3) == 5
    assert module_0.compare_one(1, 1) is None

    # float vs float
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(3.2, 1.1) == 3.2
    assert module_0.compare_one(2.0, 2.0) is None

    # int vs float - equal values return None
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(5, 2.5) == 5
    assert module_0.compare_one(1, 1.0) is None

    # numeric strings with dot
    assert module_0.compare_one("1.5", "2.5") == "2.5"
    assert module_0.compare_one("5.0", 4) == "5.0"
    assert module_0.compare_one(4, "5.0") == "5.0"
    assert module_0.compare_one("1", "1.0") is None

    # numeric strings with comma as decimal separator
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("1,5", 1.4) == "1,5"
    assert module_0.compare_one("1,2", 1.5) == 1.5
    assert module_0.compare_one("1,0", "1.0") is None
    assert module_0.compare_one("1,0", 1) is None

    # returns original value, not converted temp value
    assert module_0.compare_one("1,9", 2) == 2
    result = module_0.compare_one(5, "6,0")
    assert result == "6,0" and isinstance(result, str)

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -1.4) == -1.4

# Generated at 2026-10-24 15:48:03.591571
# Unit test for function compare_one
def test_compare_one():
    # int vs int
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(5, 3) == 5
    assert module_0.compare_one(1, 1) is None

    # float vs float
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(3.2, 1.1) == 3.2
    assert module_0.compare_one(2.0, 2.0) is None

    # int vs float - equal values return None
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(5, 2.5) == 5
    assert module_0.compare_one(1, 1.0) is None

    # numeric strings with dot
    assert module_0.compare_one("1.5", "2.5") == "2.5"
    assert module_0.compare_one("5.0", 4) == "5.0"
    assert module_0.compare_one(4, "5.0") == "5.0"
    assert module_0.compare_one("1", "1.0") is None

    # numeric strings with comma as decimal separator
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("1,5", 1.4) == "1,5"
    assert module_0.compare_one("1,2", 1.5) == 1.5
    assert module_0.compare_one("1,0", "1.0") is None
    assert module_0.compare_one("1,0", 1) is None

    # returns original value, not converted temp value
    assert module_0.compare_one("1,9", 2) == 2
    result = module_0.compare_one(5, "6,0")
    assert result == "6,0" and isinstance(result, str)

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -1.4) == -1.4

# Generated at 2026-10-24 15:48:50.079100
# Unit test for function compare_one
def test_compare_one():
    # int vs int
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(5, 3) == 5
    assert module_0.compare_one(1, 1) is None

    # float vs float
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(3.2, 1.1) == 3.2
    assert module_0.compare_one(2.0, 2.0) is None

    # int vs float - equal values return None
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(5, 2.5) == 5
    assert module_0.compare_one(1, 1.0) is None

    # numeric strings with dot
    assert module_0.compare_one("1.5", "2.5") == "2.5"
    assert module_0.compare_one("5.0", 4) == "5.0"
    assert module_0.compare_one(4, "5.0") == "5.0"
    assert module_0.compare_one("1", "1.0") is None

    # numeric strings with comma as decimal separator
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("1,5", 1.4) == "1,5"
    assert module_0.compare_one("1,2", 1.5) == 1.5
    assert module_0.compare_one("1,0", "1.0") is None
    assert module_0.compare_one("1,0", 1) is None

    # returns original value, not converted temp value
    assert module_0.compare_one("1,9", 2) == 2
    result = module_0.compare_one(5, "6,0")
    assert result == "6,0" and isinstance(result, str)

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -1.4) == -1.4

# Generated at 2026-10-24 15:48:51.512336
# Unit test for function compare_one
def test_compare_one():
    # int vs int
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(5, 3) == 5
    assert module_0.compare_one(1, 1) is None

    # float vs float
    assert module_0.compare_one(1.5, 2.5) == 2.5
    assert module_0.compare_one(3.2, 1.1) == 3.2
    assert module_0.compare_one(2.0, 2.0) is None

    # int vs float - equal values return None
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(5, 2.5) == 5
    assert module_0.compare_one(1, 1.0) is None

    # numeric strings with dot
    assert module_0.compare_one("1.5", "2.5") == "2.5"
    assert module_0.compare_one("5.0", 4) == "5.0"
    assert module_0.compare_one(4, "5.0") == "5.0"
    assert module_0.compare_one("1", "1.0") is None

    # numeric strings with comma as decimal separator
    assert module_0.compare_one("1,5", "2,5") == "2,5"
    assert module_0.compare_one("1,5", 1.4) == "1,5"
    assert module_0.compare_one("1,2", 1.5) == 1.5
    assert module_0.compare_one("1,0", "1.0") is None
    assert module_0.compare_one("1,0", 1) is None

    # returns original value, not converted temp value
    assert module_0.compare_one("1,9", 2) == 2
    result = module_0.compare_one(5, "6,0")
    assert result == "6,0" and isinstance(result, str)

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -1.4) == -1.4