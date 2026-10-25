# file: project/f124/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18], "branches": [[7, 8], [7, 9], [9, 10], [9, 11], [11, 12], [11, 13], [13, 14], [13, 18]]}

from f124 import valid_date


def test_valid_dates_return_true():
    assert valid_date("01-15-2020") is True
    assert valid_date("04-15-2020") is True
    assert valid_date("02-15-2020") is True
    assert valid_date("02-29-2020") is True
    assert valid_date("12-29-2020") is True


def test_strip_and_whitespace():
    assert valid_date("  01-15-2020  ") is True
    assert valid_date("\t02-15-2020\n") is True
    assert valid_date("  04-15-2020 ") is True


def test_month_out_of_range():
    assert valid_date("00-15-2020") is False
    assert valid_date("13-15-2020") is False
    assert valid_date("00-00-2020") is False


def test_31_day_month_branch():
    # month in [1,3,5,7,8,10,12] and day < 1 -> False
    assert valid_date("01-00-2020") is False
    assert valid_date("12-00-2020") is False
    # day > 31 with month in list -> False
    assert valid_date("01-32-2020") is False
    assert valid_date("07-40-2020") is False
    # day > 31 with month NOT in list -> False (covers A=False, C=True)
    assert valid_date("04-32-2020") is False
    assert valid_date("02-32-2020") is False
    # pass-through cases (condition False)
    assert valid_date("01-15-2020") is True
    assert valid_date("04-15-2020") is True


def test_30_day_month_branch():
    # month in [4,6,9,11] and day < 1 -> False
    assert valid_date("04-00-2020") is False
    assert valid_date("06-00-2020") is False
    assert valid_date("09-00-2020") is False
    assert valid_date("11-00-2020") is False
    # day > 30 -> False
    assert valid_date("04-31-2020") is False
    assert valid_date("06-31-2020") is False
    # day > 30 with month NOT in list -> False (covers A=False, C=True)
    assert valid_date("01-31-2020") is False
    assert valid_date("02-31-2020") is False
    # pass-through cases
    assert valid_date("04-15-2020") is True
    assert valid_date("01-15-2020") is True
    assert valid_date("02-15-2020") is True


def test_february_branch():
    # month == 2 and day < 1 -> False
    assert valid_date("02-00-2020") is False
    # day > 29 with month == 2 -> False
    assert valid_date("02-30-2020") is False
    # day > 29 with month != 2 -> False (covers first part False, second True)
    assert valid_date("01-30-2020") is False
    assert valid_date("04-30-2020") is False
    assert valid_date("01-31-2020") is False
    # pass-through cases
    assert valid_date("02-15-2020") is True
    assert valid_date("02-29-2020") is True
    assert valid_date("02-01-2020") is True


def test_day_boundary_postconditions():
    # due to `or day > 31 / or day > 30 / or day > 29` any day > 29 is False
    assert valid_date("01-29-2020") is True
    assert valid_date("01-30-2020") is False
    assert valid_date("01-31-2020") is False
    assert valid_date("01-32-2020") is False
    assert valid_date("04-29-2020") is True
    assert valid_date("04-30-2020") is False


def test_exceptions_return_false():
    assert valid_date(None) is False
    assert valid_date(123) is False
    assert valid_date(3.14) is False
    assert valid_date("") is False
    assert valid_date("   ") is False
    assert valid_date("bad") is False
    assert valid_date("01-15") is False
    assert valid_date("01-15-2020-extra") is False
    assert valid_date("01.15.2020") is False
    assert valid_date("aa-bb-cccc") is False
    assert valid_date("01-xx-2020") is False
    assert valid_date("xx-15-2020") is False
    assert valid_date("01-15-yyyy") is False
    assert valid_date("--") is False
    assert valid_date("01--15-2020") is False
