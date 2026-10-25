

# Generated at 2026-10-24 06:25:55.914210
# Unit test for function compare_one
def test_compare_one():import pytest
from your_module import compare_one  # replace with real module name


@pytest.mark.parametrize("a, b, expected", [
    # plain numbers
    (1, 2, 2),
    (2, 1, 2),
    (1, 1, None),
    (1.5, 1.5, None),
    (-1, -2, -1),
    # comma-decimal strings
    ("1,5", "1.5", None),
    ("2,5", "1,5", "2,5"),
    ("1,5", "2.5", "2.5"),
    # mixed types â returns the ORIGINAL argument, not a float
    ("3", 2, "3"),
    (1, "1.0", None),
    ("0,5", 0.5, None),
])
def test_compare_one(a, b, expected):
    assert module_0.compare_one(a, b) == expected


def test_compare_one_returns_original_object():
    a, b = "2,5", "1,5"
    assert module_0.compare_one(a, b) is a  # not a converted float


def test_compare_one_does_not_mutate_inputs():
    a, b = "1,5", "2,5"
    module_0.compare_one(a, b)
    assert (a, b) == ("1,5", "2,5")

# Generated at 2026-10-24 06:26:00.457214
# Unit test for function compare_one
def test_compare_one():assert module_0.compare_one(10, 5) == 10

# Generated at 2026-10-24 06:26:01.746282
# Unit test for function compare_one
def test_compare_one():import pytest
from your_module import compare_one  # replace with real module name


@pytest.mark.parametrize("a, b, expected", [
    # plain numbers
    (1, 2, 2),
    (2, 1, 2),
    (1, 1, None),
    (1.5, 1.5, None),
    (-1, -2, -1),
    # comma-decimal strings
    ("1,5", "1.5", None),
    ("2,5", "1,5", "2,5"),
    ("1,5", "2.5", "2.5"),
    # mixed types â returns the ORIGINAL argument, not a float
    ("3", 2, "3"),
    (1, "1.0", None),
    ("0,5", 0.5, None),
])
def test_compare_one(a, b, expected):
    assert module_0.compare_one(a, b) == expected


def test_compare_one_returns_original_object():
    a, b = "2,5", "1,5"
    assert module_0.compare_one(a, b) is a  # not a converted float


def test_compare_one_does_not_mutate_inputs():
    a, b = "1,5", "2,5"
    module_0.compare_one(a, b)
    assert (a, b) == ("1,5", "2,5")

# Generated at 2026-10-24 06:26:05.744436
# Unit test for function compare_one
def test_compare_one():assert module_0.compare_one(10, 5) == 10

# Generated at 2026-10-24 06:26:07.178583
# Unit test for function compare_one
def test_compare_one():import pytest
from your_module import compare_one  # replace with real module name


@pytest.mark.parametrize("a, b, expected", [
    # plain numbers
    (1, 2, 2),
    (2, 1, 2),
    (1, 1, None),
    (1.5, 1.5, None),
    (-1, -2, -1),
    # comma-decimal strings
    ("1,5", "1.5", None),
    ("2,5", "1,5", "2,5"),
    ("1,5", "2.5", "2.5"),
    # mixed types â returns the ORIGINAL argument, not a float
    ("3", 2, "3"),
    (1, "1.0", None),
    ("0,5", 0.5, None),
])
def test_compare_one(a, b, expected):
    assert module_0.compare_one(a, b) == expected


def test_compare_one_returns_original_object():
    a, b = "2,5", "1,5"
    assert module_0.compare_one(a, b) is a  # not a converted float


def test_compare_one_does_not_mutate_inputs():
    a, b = "1,5", "2,5"
    module_0.compare_one(a, b)
    assert (a, b) == ("1,5", "2,5")

# Generated at 2026-10-24 06:26:09.785134
# Unit test for function compare_one

# Generated at 2026-10-24 06:26:12.227863
# Unit test for function compare_one

# Generated at 2026-10-24 06:26:14.619322
# Unit test for function compare_one

# Generated at 2026-10-24 06:26:17.034010
# Unit test for function compare_one

# Generated at 2026-10-24 06:26:19.449027
# Unit test for function compare_one

# Generated at 2026-10-24 06:26:21.866994
# Unit test for function compare_one

# Generated at 2026-10-24 06:26:24.281888
# Unit test for function compare_one

# Generated at 2026-10-24 06:26:26.695151
# Unit test for function compare_one