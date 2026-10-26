

# Generated at 2026-10-25 12:31:24.741691
# Unit test for function compare_one
def test_compare_one():
    # int vs float
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2

    # equal values -> None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(1.0, 1) is None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one("1.0", "1,0") is None
    assert module_0.compare_one("5,1", "5.1") is None

    # strings with '.' vs ','
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("5,1", "6,0") == "6,0"
    assert module_0.compare_one("1,2", 1.1) == "1,2"
    assert module_0.compare_one("1.2", 1.1) == "1.2"

    # preserves original type / value
    assert module_0.compare_one("5", 3) == "5"
    assert module_0.compare_one(10, "9.9") == 10

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

# Generated at 2026-10-25 12:31:31.204154
# Unit test for function compare_one
def test_compare_one():
    # int vs float
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2

    # equal values -> None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(1.0, 1) is None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one("1.0", "1,0") is None
    assert module_0.compare_one("5,1", "5.1") is None

    # strings with '.' vs ','
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("5,1", "6,0") == "6,0"
    assert module_0.compare_one("1,2", 1.1) == "1,2"
    assert module_0.compare_one("1.2", 1.1) == "1.2"

    # preserves original type / value
    assert module_0.compare_one("5", 3) == "5"
    assert module_0.compare_one(10, "9.9") == 10

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

# Generated at 2026-10-25 12:31:32.705556
# Unit test for function compare_one
def test_compare_one():
    # int vs float
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2

    # equal values -> None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(1.0, 1) is None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one("1.0", "1,0") is None
    assert module_0.compare_one("5,1", "5.1") is None

    # strings with '.' vs ','
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("5,1", "6,0") == "6,0"
    assert module_0.compare_one("1,2", 1.1) == "1,2"
    assert module_0.compare_one("1.2", 1.1) == "1.2"

    # preserves original type / value
    assert module_0.compare_one("5", 3) == "5"
    assert module_0.compare_one(10, "9.9") == 10

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

# Generated at 2026-10-25 12:31:35.773419
# Unit test for function compare_one
def test_compare_one():
    # int vs float
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2

    # equal values -> None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(1.0, 1) is None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one("1.0", "1,0") is None
    assert module_0.compare_one("5,1", "5.1") is None

    # strings with '.' vs ','
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("5,1", "6,0") == "6,0"
    assert module_0.compare_one("1,2", 1.1) == "1,2"
    assert module_0.compare_one("1.2", 1.1) == "1.2"

    # preserves original type / value
    assert module_0.compare_one("5", 3) == "5"
    assert module_0.compare_one(10, "9.9") == 10

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"

# Generated at 2026-10-25 12:31:37.384761
# Unit test for function compare_one
def test_compare_one():
    # int vs float
    assert module_0.compare_one(1, 2.5) == 2.5
    assert module_0.compare_one(2.5, 1) == 2.5
    assert module_0.compare_one(1, 2) == 2
    assert module_0.compare_one(2, 1) == 2

    # equal values -> None
    assert module_0.compare_one(1, 1) is None
    assert module_0.compare_one(1.0, 1) is None
    assert module_0.compare_one("1", 1) is None
    assert module_0.compare_one("1.0", "1,0") is None
    assert module_0.compare_one("5,1", "5.1") is None

    # strings with '.' vs ','
    assert module_0.compare_one(1, "2,3") == "2,3"
    assert module_0.compare_one("5,1", "6") == "6"
    assert module_0.compare_one("5,1", "6,0") == "6,0"
    assert module_0.compare_one("1,2", 1.1) == "1,2"
    assert module_0.compare_one("1.2", 1.1) == "1.2"

    # preserves original type / value
    assert module_0.compare_one("5", 3) == "5"
    assert module_0.compare_one(10, "9.9") == 10

    # negatives
    assert module_0.compare_one(-1, -2) == -1
    assert module_0.compare_one("-1,5", -2) == "-1,5"