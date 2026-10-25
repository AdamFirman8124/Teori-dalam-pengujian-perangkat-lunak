

# Generated at 2026-10-24 22:24:43.101910
# Unit test for function valid_date

# Generated at 2026-10-24 22:24:45.521326
# Unit test for function valid_date

# Generated at 2026-10-24 22:24:47.937817
# Unit test for function valid_date

# Generated at 2026-10-24 22:25:04.005268
# Unit test for function valid_date
def test_valid_date():
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("02-29-2024") is True      # leap year
    assert module_0.valid_date("02-29-2023") is False     # not a leap year
    assert module_0.valid_date("02-29-1900") is False     # century, not leap
    assert module_0.valid_date("02-29-2000") is True      # 400-year leap
    assert module_0.valid_date("04-31-2024") is False     # April has 30 days
    assert module_0.valid_date("13-01-2024") is False     # bad month
    assert module_0.valid_date("00-10-2024") is False     # bad month
    assert module_0.valid_date("01-00-2024") is False     # bad day
    assert module_0.valid_date("01-32-2024") is False     # bad day
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01-01-2024-05") is False
    assert module_0.valid_date(None) is False
    print("all tests passed")


test_valid_date()

# Generated at 2026-10-24 22:25:15.152904
# Unit test for function valid_date
def test_valid_date():import pytest

@pytest.mark.parametrize("date", [
    "01-01-2024",
    "12-31-2024",
    "04-30-2024",
    "02-29-2024",
    " 06-15-2024 ",
])
def test_valid_date_accepts_valid_dates(date):
    assert module_0.valid_date(date) is True


@pytest.mark.parametrize("date", [
    "00-10-2024",  # invalid month
    "13-10-2024",  # invalid month
    "01-00-2024",  # invalid day
    "01-32-2024",  # too many days
    "04-31-2024",  # April has 30 days
    "02-30-2024",  # February has at most 29 days
    "not-a-date",
    "01/01/2024",
    "",
    None,
])
def test_valid_date_rejects_invalid_dates(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 22:25:26.633764
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("02-29-2024") is True

    # Invalid calendar dates
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("01-00-2024") is False

    # Non-leap-year date
    assert module_0.valid_date("02-29-2023") is False

    # Malformed input
    assert module_0.valid_date("") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("01-01") is False
    assert module_0.valid_date(None) is False

    # Surrounding whitespace
    assert module_0.valid_date(" 01-01-2024 ") is True

# Generated at 2026-10-24 22:25:37.579584
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 06-15-2023 ") is True

    # Invalid days
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("05-00-2024") is False

    # Invalid months
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False

    # Invalid formats and values
    assert module_0.valid_date("01/15/2024") is False
    assert module_0.valid_date("January-15-2024") is False
    assert module_0.valid_date("01-15") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:25:48.333439
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True  # Leap year
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid days
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("02-29-2023") is False  # Not a leap year
    assert module_0.valid_date("01-00-2024") is False

    # Invalid months and malformed input
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:25:57.341894
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid months
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats and values
    assert module_0.valid_date("01/31/2024") is False
    assert module_0.valid_date("January-31-2024") is False
    assert module_0.valid_date("01-31") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:26:08.295616
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("1-1-2023") is True
    assert module_0.valid_date("12-31-2023") is True
    assert module_0.valid_date("4-30-2023") is True
    assert module_0.valid_date(" 6-15-2023 ") is True

    # Month boundaries
    assert module_0.valid_date("0-10-2023") is False
    assert module_0.valid_date("13-10-2023") is False

    # Day boundaries
    assert module_0.valid_date("1-0-2023") is False
    assert module_0.valid_date("1-32-2023") is False
    assert module_0.valid_date("4-31-2023") is False
    assert module_0.valid_date("2-30-2023") is False

    # Leap years
    assert module_0.valid_date("2-29-2024") is True
    assert module_0.valid_date("2-29-2023") is False

    # Malformed input
    assert module_0.valid_date("") is False
    assert module_0.valid_date("1/1/2023") is False
    assert module_0.valid_date("January-1-2023") is False
    assert module_0.valid_date("1-1") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:26:19.255165
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2023") is True
    assert module_0.valid_date("04-30-2023") is True
    assert module_0.valid_date("02-28-2023") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2023 ") is True

    # Invalid dates
    assert module_0.valid_date("00-10-2023") is False
    assert module_0.valid_date("13-10-2023") is False
    assert module_0.valid_date("04-31-2023") is False
    assert module_0.valid_date("02-29-2023") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:26:30.724137
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("01-30-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Malformed inputs
    assert module_0.valid_date("") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("January-01-2024") is False
    assert module_0.valid_date("01-01") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:26:33.248928
# Unit test for function valid_date

# Generated at 2026-10-24 22:26:35.670032
# Unit test for function valid_date

# Generated at 2026-10-24 22:26:38.087999
# Unit test for function valid_date

# Generated at 2026-10-24 22:26:40.505835
# Unit test for function valid_date

# Generated at 2026-10-24 22:26:42.921308
# Unit test for function valid_date

# Generated at 2026-10-24 22:26:45.482230
# Unit test for function valid_date

# Generated at 2026-10-24 22:26:47.903228
# Unit test for function valid_date

# Generated at 2026-10-24 22:26:50.321540
# Unit test for function valid_date

# Generated at 2026-10-24 22:27:06.552174
# Unit test for function valid_date

# Generated at 2026-10-24 22:27:23.562134
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Malformed input
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:27:38.001299
# Unit test for function valid_date
def test_valid_date():import pytest

@pytest.mark.parametrize(
    "value, expected",
    [
        ("01-01-2024", True),
        ("12-31-2023", True),
        ("04-30-2024", True),
        ("02-29-2024", True),   # Leap year
        (" 06-15-2024 ", True),

        ("00-10-2024", False),
        ("13-10-2024", False),
        ("01-00-2024", False),
        ("01-32-2024", False),
        ("04-31-2024", False),
        ("02-30-2024", False),
        ("02-29-2023", False),  # Not a leap year
        ("01/01/2024", False),
        ("not-a-date", False),
        ("", False),
        (None, False),
    ],
)
def test_valid_date(value, expected):
    assert module_0.valid_date(value) is expected

# Generated at 2026-10-24 22:27:40.424067
# Unit test for function valid_date

# Generated at 2026-10-24 22:27:42.940291
# Unit test for function valid_date

# Generated at 2026-10-24 22:27:45.359514
# Unit test for function valid_date

# Generated at 2026-10-24 22:27:47.776922
# Unit test for function valid_date

# Generated at 2026-10-24 22:27:50.194044
# Unit test for function valid_date

# Generated at 2026-10-24 22:27:52.610444
# Unit test for function valid_date

# Generated at 2026-10-24 22:27:55.141032
# Unit test for function valid_date

# Generated at 2026-10-24 22:28:00.016480
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("01-01-2024") is True

# Generated at 2026-10-24 22:28:10.564846
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024")
    assert module_0.valid_date("12-31-2024")
    assert module_0.valid_date("04-30-2024")
    assert module_0.valid_date("02-29-2024")       # Leap year
    assert module_0.valid_date(" 06-15-2023 ")     # Surrounding whitespace

    # Invalid dates
    assert not module_0.valid_date("00-10-2024")
    assert not module_0.valid_date("13-10-2024")
    assert not module_0.valid_date("04-31-2024")
    assert not module_0.valid_date("02-30-2024")
    assert not module_0.valid_date("02-29-2023")   # Not a leap year
    assert not module_0.valid_date("01-00-2024")
    assert not module_0.valid_date("not-a-date")
    assert not module_0.valid_date("")
    assert not module_0.valid_date(None)

# Generated at 2026-10-24 22:28:24.084661
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid days
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("01-00-2024") is False

    # Invalid months
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False

    # Invalid formats and values
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/15/2024") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:28:36.882075
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid days
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("03-00-2024") is False

    # Invalid months
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False

    # Invalid formats and types
    assert module_0.valid_date("01/15/2024") is False
    assert module_0.valid_date("January-15-2024") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:28:48.469730
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("1-1-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("4-30-2024") is True
    assert module_0.valid_date("2-29-2024") is True
    assert module_0.valid_date(" 6-15-2023 ") is True

    # Invalid days and months
    assert module_0.valid_date("0-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("1-0-2024") is False
    assert module_0.valid_date("1-32-2024") is False
    assert module_0.valid_date("4-31-2024") is False
    assert module_0.valid_date("2-30-2024") is False

    # Leap-year validation
    assert module_0.valid_date("2-29-2023") is False
    assert module_0.valid_date("2-29-2000") is True
    assert module_0.valid_date("2-29-1900") is False

    # Invalid formats and input types
    assert module_0.valid_date("2024-01-01") is False
    assert module_0.valid_date("1/1/2024") is False
    assert module_0.valid_date("invalid") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:28:50.890349
# Unit test for function valid_date

# Generated at 2026-10-24 22:28:53.307582
# Unit test for function valid_date

# Generated at 2026-10-24 22:28:55.837436
# Unit test for function valid_date

# Generated at 2026-10-24 22:29:08.115550
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats and values
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:29:17.739927
# Unit test for function valid_date

# Generated at 2026-10-24 22:29:24.191330
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("12-31-2024") is True

# Generated at 2026-10-24 22:29:40.267212
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024")
    assert module_0.valid_date("12-31-2024")
    assert module_0.valid_date("04-30-2024")
    assert module_0.valid_date("02-29-2024")       # Leap year
    assert module_0.valid_date(" 06-15-2023 ")     # Surrounding whitespace

    # Invalid days
    assert not module_0.valid_date("01-32-2024")
    assert not module_0.valid_date("04-31-2024")
    assert not module_0.valid_date("02-30-2024")
    assert not module_0.valid_date("02-29-2023")   # Not a leap year
    assert not module_0.valid_date("00-10-2024")
    assert not module_0.valid_date("13-10-2024")

    # Invalid formats and values
    assert not module_0.valid_date("2024-01-01")
    assert not module_0.valid_date("01/01/2024")
    assert not module_0.valid_date("not-a-date")
    assert not module_0.valid_date("")
    assert not module_0.valid_date(None)

# Generated at 2026-10-24 22:29:42.907375
# Unit test for function valid_date

# Generated at 2026-10-24 22:29:45.441322
# Unit test for function valid_date

# Generated at 2026-10-24 22:29:47.860795
# Unit test for function valid_date

# Generated at 2026-10-24 22:29:50.374750
# Unit test for function valid_date

# Generated at 2026-10-24 22:29:52.791070
# Unit test for function valid_date

# Generated at 2026-10-24 22:29:55.329165
# Unit test for function valid_date

# Generated at 2026-10-24 22:29:57.747133
# Unit test for function valid_date

# Generated at 2026-10-24 22:30:06.378991
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("01-01-2024") is True

# Generated at 2026-10-24 22:30:18.663573
# Unit test for function valid_date
def test_valid_date():from datetime import date as Date


def module_0.valid_date(value):
    try:
        month, day, year = map(int, value.strip().split("-"))
        Date(year, month, day)
        return True
    except (AttributeError, TypeError, ValueError):
        return False

# Generated at 2026-10-24 22:30:31.159314
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True

    # Invalid months
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats
    assert module_0.valid_date("2024-01-01") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False

# Generated at 2026-10-24 22:30:43.625967
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2024")
    assert module_0.valid_date("04-30-2024")
    assert module_0.valid_date("02-29-2024")  # Leap year
    assert module_0.valid_date(" 12-25-2024 ")

    # Invalid days
    assert not module_0.valid_date("01-32-2024")
    assert not module_0.valid_date("04-31-2024")
    assert not module_0.valid_date("02-30-2024")
    assert not module_0.valid_date("02-29-2023")  # Not a leap year
    assert not module_0.valid_date("01-00-2024")

    # Invalid months
    assert not module_0.valid_date("00-15-2024")
    assert not module_0.valid_date("13-15-2024")

    # Invalid formats and values
    assert not module_0.valid_date("2024-01-31")
    assert not module_0.valid_date("01/31/2024")
    assert not module_0.valid_date("not-a-date")
    assert not module_0.valid_date("")
    assert not module_0.valid_date(None)

# Generated at 2026-10-24 22:30:56.582092
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:30:59.219187
# Unit test for function valid_date
def test_valid_date():
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("02-29-2024") is True      # leap year
    assert module_0.valid_date("02-29-2023") is False     # not a leap year
    assert module_0.valid_date("02-29-1900") is False     # century, not leap
    assert module_0.valid_date("02-29-2000") is True      # 400-year leap
    assert module_0.valid_date("04-31-2024") is False     # April has 30 days
    assert module_0.valid_date("13-01-2024") is False     # bad month
    assert module_0.valid_date("00-10-2024") is False     # bad month
    assert module_0.valid_date("01-00-2024") is False     # bad day
    assert module_0.valid_date("01-32-2024") is False     # bad day
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01-01-2024-05") is False
    assert module_0.valid_date(None) is False
    print("all tests passed")


test_valid_date()

# Generated at 2026-10-24 22:31:10.174402
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True

    # Invalid days
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("01-00-2024") is False

    # Invalid months
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False

    # Invalid formats
    assert module_0.valid_date("01/15/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:31:21.764464
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats and values
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("01-01") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:31:32.192075
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid days
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("01-00-2024") is False

    # Invalid months and formats
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False
    assert module_0.valid_date("01/15/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:31:43.056484
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid days
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("02-29-2023") is False  # Not a leap year
    assert module_0.valid_date("01-00-2024") is False

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid formats and values
    assert module_0.valid_date("2024-01-01") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:31:55.435578
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True

    # Invalid months
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("January-01-2024") is False
    assert module_0.valid_date("01-01") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:31:57.856076
# Unit test for function valid_date

# Generated at 2026-10-24 22:32:00.437960
# Unit test for function valid_date

# Generated at 2026-10-24 22:32:08.334765
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("01-01-2024") is True

# Generated at 2026-10-24 22:32:21.445908
# Unit test for function valid_date
def test_valid_date():
    valid_dates = [
        "01-01-2024",
        "12-31-2024",
        "04-30-2024",
        "02-29-2024",       # Leap year
        " 06-15-2023 ",     # Surrounding whitespace
    ]

    invalid_dates = [
        "00-10-2024",
        "13-10-2024",
        "01-00-2024",
        "04-31-2024",
        "02-30-2024",
        "02-29-2023",       # Not a leap year
        "12-32-2024",
        "not-a-date",
        "01/01/2024",
        "",
        None,
    ]

    for value in valid_dates:
        assert module_0.valid_date(value), f"Expected {value!r} to be valid"

    for value in invalid_dates:
        assert not module_0.valid_date(value), f"Expected {value!r} to be invalid"

# Generated at 2026-10-24 22:32:28.426734
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("01-01-2024") is True

# Generated at 2026-10-24 22:32:40.495207
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid days
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-29-2023") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("01-00-2024") is False

    # Invalid months and years
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("01-10-0") is False

    # Invalid formats
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/10/2024") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:32:52.577137
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("1-1-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("4-30-2024") is True
    assert module_0.valid_date(" 6-15-2024 ") is True
    assert module_0.valid_date("2-29-2024") is True  # Leap year

    # Invalid months and days
    assert module_0.valid_date("0-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("1-0-2024") is False
    assert module_0.valid_date("1-32-2024") is False
    assert module_0.valid_date("4-31-2024") is False
    assert module_0.valid_date("2-30-2024") is False
    assert module_0.valid_date("2-29-2023") is False  # Not a leap year

    # Malformed input
    assert module_0.valid_date("") is False
    assert module_0.valid_date("1/1/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("1-1") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:32:54.999837
# Unit test for function valid_date

# Generated at 2026-10-24 22:32:57.417068
# Unit test for function valid_date

# Generated at 2026-10-24 22:32:59.835176
# Unit test for function valid_date

# Generated at 2026-10-24 22:33:02.251692
# Unit test for function valid_date

# Generated at 2026-10-24 22:33:04.830945
# Unit test for function valid_date

# Generated at 2026-10-24 22:33:12.214738
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("01-31-2024") is True

# Generated at 2026-10-24 22:33:24.524755
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("1-1-2024")
    assert module_0.valid_date("01-31-2024")
    assert module_0.valid_date("4-30-2024")
    assert module_0.valid_date("2-29-2024")
    assert module_0.valid_date(" 12-25-2024 ")

    # Invalid months
    assert not module_0.valid_date("0-10-2024")
    assert not module_0.valid_date("13-10-2024")

    # Invalid days
    assert not module_0.valid_date("1-0-2024")
    assert not module_0.valid_date("1-32-2024")
    assert not module_0.valid_date("4-31-2024")
    assert not module_0.valid_date("2-30-2024")

    # Invalid formats
    assert not module_0.valid_date("2024-01")
    assert not module_0.valid_date("January-1-2024")
    assert not module_0.valid_date("")
    assert not module_0.valid_date(None)

# Generated at 2026-10-24 22:33:35.891305
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid calendar dates
    assert module_0.valid_date("02-29-2023") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("13-01-2024") is False
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("01-00-2024") is False

    # Invalid formats and types
    assert module_0.valid_date("2024-01-31") is False
    assert module_0.valid_date("01/31/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:33:46.975008
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats and values
    assert module_0.valid_date("01/15/2024") is False
    assert module_0.valid_date("January-15-2024") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:33:58.521757
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True

    # Invalid month/day combinations
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats and values
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("January-01-2024") is False
    assert module_0.valid_date("01-01") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 22:34:00.945116
# Unit test for function valid_date

# Generated at 2026-10-24 22:34:03.367613
# Unit test for function valid_date

# Generated at 2026-10-24 22:34:05.906128
# Unit test for function valid_date

# Generated at 2026-10-24 22:34:18.601447
# Unit test for function valid_date
def test_valid_date():month == 2 and day < 1 or day > 29

# Generated at 2026-10-24 22:34:31.198823
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("1-1-2024") is True
    assert module_0.valid_date("1-31-2024") is True
    assert module_0.valid_date("4-30-2024") is True
    assert module_0.valid_date("2-29-2024") is True
    assert module_0.valid_date(" 12-25-2024 ") is True

    # Invalid months
    assert module_0.valid_date("0-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid days
    assert module_0.valid_date("1-0-2024") is False
    assert module_0.valid_date("1-32-2024") is False
    assert module_0.valid_date("4-31-2024") is False
    assert module_0.valid_date("2-30-2024") is False

    # Invalid formats
    assert module_0.valid_date("") is False
    assert module_0.valid_date("January-1-2024") is False
    assert module_0.valid_date("1/1/2024") is False
    assert module_0.valid_date("1-1") is False
    assert module_0.valid_date("1-1-2024-extra") is False

# Generated at 2026-10-24 22:34:43.781663
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date("02-29-2000") is True
    assert module_0.valid_date(" 12-25-2023 ") is True

    # Invalid days
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("01-00-2024") is False

    # Leap-year cases
    assert module_0.valid_date("02-29-2023") is False
    assert module_0.valid_date("02-29-1900") is False

    # Invalid months and malformed input
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/31/2024") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False