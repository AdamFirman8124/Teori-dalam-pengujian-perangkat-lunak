

# Generated at 2026-10-25 03:16:33.406874
# Unit test for function compare_one

# Generated at 2026-10-25 03:16:35.818773
# Unit test for function compare_one

# Generated at 2026-10-25 03:16:38.242539
# Unit test for function compare_one

# Generated at 2026-10-25 03:16:40.658138
# Unit test for function compare_one

# Generated at 2026-10-25 03:16:43.070103
# Unit test for function compare_one

# Generated at 2026-10-25 03:16:48.370702
# Unit test for function compare_one
def test_compare_one():assert module_0.compare_one("1,5", 2) == 2

# Generated at 2026-10-25 03:16:54.522909
# Unit test for function compare_one
def test_compare_one():import pytest

def module_0.compare_one(a, b):
    temp_a, temp_b = a, b

    if isinstance(temp_a, str):
        temp_a = temp_a.replace(',', '.')
    if isinstance(temp_b, str):
        temp_b = temp_b.replace(',', '.')

    if float(temp_a) == float(temp_b):
        return None

    return a if float(temp_a) > float(temp_b) else b


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (10, 5, 10),
        (5, 10, 10),
        (5, 5, None),
        ("10", "5", "10"),
        ("5", "10", "10"),
        ("1,5", "1.2", "1,5"),
        ("1,5", 1.5, None),
        (-2, -5, -2),
        (0, "0,0", None),
    ],
)
def test_compare_one(a, b, expected):
    assert module_0.compare_one(a, b) == expected


def test_compare_one_invalid_value():
    with pytest.raises(ValueError):
        module_0.compare_one("not-a-number", 10)

# Generated at 2026-10-25 03:17:00.305940
# Unit test for function compare_one
def test_compare_one():
    assert module_0.compare_one(10, 5) == 10
    assert module_0.compare_one(3, 8) == 8
    assert module_0.compare_one(4, 4) is None

    # Numeric strings with decimal commas
    assert module_0.compare_one("2,5", "3,1") == "3,1"
    assert module_0.compare_one("7,5", "2,5") == "7,5"

    # Mixed types and equal numeric values
    assert module_0.compare_one("10", 5) == "10"
    assert module_0.compare_one("4,0", 4) is None

    # Negative values
    assert module_0.compare_one(-2, -5) == -2

# Generated at 2026-10-25 03:17:05.975606
# Unit test for function compare_one
def test_compare_one():
    # Returns the larger original value
    assert module_0.compare_one(10, 5) == 10
    assert module_0.compare_one(3, 8) == 8

    # Equal values return None
    assert module_0.compare_one(4, 4) is None
    assert module_0.compare_one("2.5", "2,5") is None

    # Supports numeric strings with dots and commas
    assert module_0.compare_one("3,5", "2.9") == "3,5"
    assert module_0.compare_one("1.5", "2,5") == "2,5"

    # Supports comparisons between strings and numbers
    assert module_0.compare_one("10,5", 10) == "10,5"
    assert module_0.compare_one(7, "8.0") == "8.0"
    assert module_0.compare_one("5,0", 5) is None