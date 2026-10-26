

# Generated at 2026-10-25 14:18:33.113844
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(1234, 10) == "1234"
    assert module_0.change_base(255, 16) == "1515"   # digits aren't lettered: 15 then 15
    assert module_0.change_base(0, 2) == ""          # current behavior: empty string for 0

# Generated at 2026-10-25 14:18:42.819275
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(15, 8) == "17"
    assert module_0.change_base(100, 10) == "100"
    assert module_0.change_base(0, 2) == "0"
    assert module_0.change_base(-10, 2) == "-1010"

# Generated at 2026-10-25 14:18:56.666695
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(1, 2) == "1"
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(25, 2) == "11001"
    assert module_0.change_base(10, 10) == "10"
    assert module_0.change_base(123, 10) == "123"
    assert module_0.change_base(100, 5) == "400"

# Generated at 2026-10-25 14:19:12.187083
# Unit test for function change_base
def test_change_base():import pytest


def module_0.change_base(x: int, base: int):
    ret = ""

    while x > 0:
        ret = str(x % base) + ret
        x //= base

    return ret


@pytest.mark.parametrize(
    "x, base, expected",
    [
        (10, 2, "1010"),
        (10, 3, "101"),
        (10, 10, "10"),
        (255, 10, "255"),
        (1, 2, "1"),
    ],
)
def test_change_base(x, base, expected):
    assert module_0.change_base(x, base) == expected

# Generated at 2026-10-25 14:19:21.241234
# Unit test for function change_base
def test_change_base():
    assert module_0.change_base(10, 2) == "1010"
    assert module_0.change_base(25, 3) == "221"
    assert module_0.change_base(42, 5) == "132"
    assert module_0.change_base(7, 10) == "7"
    assert module_0.change_base(0, 2) == "0"