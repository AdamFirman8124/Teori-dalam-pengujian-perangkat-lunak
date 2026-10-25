

# Generated at 2026-10-24 00:53:21.943731
# Unit test for function simplify
def test_simplify():
    assert module_0.simplify("1/2", "2/1") is True      # 2/2 = 1
    assert module_0.simplify("3/4", "2/3") is False     # 6/12 = 0.5
    assert module_0.simplify("5/6", "3/5") is False     # 15/30 = 0.5
    assert module_0.simplify("2/3", "3/2") is True      # 6/6 = 1
    assert module_0.simplify("0/5", "2/7") is True      # 0/35 = 0

# Generated at 2026-10-24 00:53:36.822990
# Unit test for function simplify
def test_simplify():
    assert module_0.simplify("1/2", "2/1") is True
    assert module_0.simplify("3/4", "4/3") is True
    assert module_0.simplify("2/3", "3/2") is True

    assert module_0.simplify("1/2", "1/2") is False
    assert module_0.simplify("2/3", "3/4") is False
    assert module_0.simplify("5/6", "2/5") is False

# Generated at 2026-10-24 00:53:52.105790
# Unit test for function simplify
def test_simplify():import pytest


def module_0.simplify(x, n):
    a, b = x.split("/")
    c, d = n.split("/")

    numerator = int(a) * int(c)
    denom = int(b) * int(d)

    return numerator % denom == 0


@pytest.mark.parametrize(
    "x, n, expected",
    [
        ("1/2", "2/1", True),   # 1/2 Ã 2/1 = 1
        ("2/3", "3/2", True),   # 2/3 Ã 3/2 = 1
        ("1/2", "1/2", False),  # 1/4 is not an integer
        ("3/4", "2/3", False),  # 1/2 is not an integer
        ("4/5", "5/2", True),   # 2 is an integer
    ],
)
def test_simplify(x, n, expected):
    assert module_0.simplify(x, n) is expected

# Generated at 2026-10-24 00:54:19.297359
# Unit test for function simplify
def test_simplify():
    # Result is a whole number
    assert module_0.simplify("1/2", "2/1") == True      # 1/2 * 2 = 1
    assert module_0.simplify("1/3", "3/1") == True      # 1/3 * 3 = 1
    assert module_0.simplify("2/4", "2/1") == True      # 1/2 * 2 = 1
    assert module_0.simplify("3/2", "2/3") == True      # 1
    assert module_0.simplify("5/1", "1/5") == True      # 1

    # Result is a fraction
    assert module_0.simplify("1/2", "1/2") == False     # 1/4
    assert module_0.simplify("1/3", "1/3") == False     # 1/9
    assert module_0.simplify("2/3", "3/4") == False     # 1/2

    # Zero and negatives
    assert module_0.simplify("0/1", "1/2") == True      # 0 is whole
    assert module_0.simplify("-1/2", "2/1") == True     # -1 is whole
    assert module_0.simplify("-1/2", "1/2") == False    # -1/4

    # Large numbers (float division would fail here)
    assert module_0.simplify("1000003/7", "7/1000003") == True
    assert module_0.simplify("999999999/2", "2/3") == False

    print("All tests passed!")

test_simplify()

# Generated at 2026-10-24 00:54:32.906841
# Unit test for function simplify
def test_simplify():
    assert module_0.simplify("2/3", "3/2") is True    # 1
    assert module_0.simplify("4/5", "5/2") is True    # 2
    assert module_0.simplify("1/2", "1/3") is False   # 1/6
    assert module_0.simplify("2/3", "3/4") is False   # 1/2