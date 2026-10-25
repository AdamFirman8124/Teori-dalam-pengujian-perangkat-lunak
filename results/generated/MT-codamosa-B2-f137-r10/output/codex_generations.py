

# Generated at 2026-10-24 11:25:02.647943
# Unit test for function compare_one
def test_compare_one():
    # Different types, numeric comparison
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1", 1) is None          # equal values, different types
    assert module_0.compare_one(2, 2) is None            # equal integers
    assert module_0.compare_one("1.0", "1,0") is None    # equal after comma normalization

    # Negative numbers
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

    # Zero vs negative
    assert module_0.compare_one(0, -1) == 0

    # Original types are preserved (string stays string, int stays int)
    assert isinstance(module_0.compare_one("2,5", 3), str)
    assert isinstance(module_0.compare_one(3, "2,5"), int)

    print("All compare_one tests passed.")


test_compare_one()

# Generated at 2026-10-24 11:25:04.081154
# Unit test for function compare_one
def test_compare_one():
    # Different types, numeric comparison
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1", 1) is None          # equal values, different types
    assert module_0.compare_one(2, 2) is None            # equal integers
    assert module_0.compare_one("1.0", "1,0") is None    # equal after comma normalization

    # Negative numbers
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

    # Zero vs negative
    assert module_0.compare_one(0, -1) == 0

    # Original types are preserved (string stays string, int stays int)
    assert isinstance(module_0.compare_one("2,5", 3), str)
    assert isinstance(module_0.compare_one(3, "2,5"), int)

    print("All compare_one tests passed.")


test_compare_one()

# Generated at 2026-10-24 11:25:05.482838
# Unit test for function compare_one
def test_compare_one():
    # Different types, numeric comparison
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1", 1) is None          # equal values, different types
    assert module_0.compare_one(2, 2) is None            # equal integers
    assert module_0.compare_one("1.0", "1,0") is None    # equal after comma normalization

    # Negative numbers
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

    # Zero vs negative
    assert module_0.compare_one(0, -1) == 0

    # Original types are preserved (string stays string, int stays int)
    assert isinstance(module_0.compare_one("2,5", 3), str)
    assert isinstance(module_0.compare_one(3, "2,5"), int)

    print("All compare_one tests passed.")


test_compare_one()

# Generated at 2026-10-24 11:25:06.946438
# Unit test for function compare_one
def test_compare_one():
    # Different types, numeric comparison
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1", 1) is None          # equal values, different types
    assert module_0.compare_one(2, 2) is None            # equal integers
    assert module_0.compare_one("1.0", "1,0") is None    # equal after comma normalization

    # Negative numbers
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

    # Zero vs negative
    assert module_0.compare_one(0, -1) == 0

    # Original types are preserved (string stays string, int stays int)
    assert isinstance(module_0.compare_one("2,5", 3), str)
    assert isinstance(module_0.compare_one(3, "2,5"), int)

    print("All compare_one tests passed.")


test_compare_one()

# Generated at 2026-10-24 11:25:08.277437
# Unit test for function compare_one
def test_compare_one():
    # Different types, numeric comparison
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("1", 1) is None          # equal values, different types
    assert module_0.compare_one(2, 2) is None            # equal integers
    assert module_0.compare_one("1.0", "1,0") is None    # equal after comma normalization

    # Negative numbers
    assert module_0.compare_one(-2, -1) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

    # Zero vs negative
    assert module_0.compare_one(0, -1) == 0

    # Original types are preserved (string stays string, int stays int)
    assert isinstance(module_0.compare_one("2,5", 3), str)
    assert isinstance(module_0.compare_one(3, "2,5"), int)

    print("All compare_one tests passed.")


test_compare_one()