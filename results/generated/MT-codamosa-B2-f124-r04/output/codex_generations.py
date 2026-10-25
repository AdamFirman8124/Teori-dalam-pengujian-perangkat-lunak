

# Generated at 2026-10-24 23:19:32.532199
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

# Generated at 2026-10-24 23:19:43.569506
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2023") is True
    assert module_0.valid_date("12-31-2023") is True
    assert module_0.valid_date("04-30-2023") is True
    assert module_0.valid_date(" 06-15-2023 ") is True
    assert module_0.valid_date("02-29-2024") is True  # Leap year

    # Invalid months and days
    assert module_0.valid_date("00-10-2023") is False
    assert module_0.valid_date("13-10-2023") is False
    assert module_0.valid_date("01-00-2023") is False
    assert module_0.valid_date("01-32-2023") is False
    assert module_0.valid_date("04-31-2023") is False
    assert module_0.valid_date("02-30-2023") is False

    # Invalid formats
    assert module_0.valid_date("") is False
    assert module_0.valid_date("01/01/2023") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01-01") is False

# Generated at 2026-10-24 23:19:55.968847
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("1-1-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("4-30-2024") is True
    assert module_0.valid_date("2-29-2024") is True
    assert module_0.valid_date(" 6-15-2024 ") is True

    # Invalid month/day combinations
    assert module_0.valid_date("0-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("1-0-2024") is False
    assert module_0.valid_date("1-32-2024") is False
    assert module_0.valid_date("4-31-2024") is False
    assert module_0.valid_date("2-30-2024") is False

    # Invalid input formats
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:20:06.851104
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True
    assert module_0.valid_date("02-29-2024") is True  # Leap year

    # Invalid days and months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats
    assert module_0.valid_date("2024-01-01") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

    # Non-leap year
    assert module_0.valid_date("02-29-2023") is False

# Generated at 2026-10-24 23:20:09.270838
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:11.910658
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:14.335309
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:16.873933
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:19.287516
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:21.704435
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:24.310261
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:26.729025
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:29.305561
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:31.730217
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:34.147015
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:36.562906
# Unit test for function valid_date

# Generated at 2026-10-24 23:20:48.490978
# Unit test for function valid_date
def test_valid_date():
    valid_dates = [
        "01-01-2024",
        "01-31-2024",
        "04-30-2024",
        "02-29-2024",
        "12-31-2024",
        " 06-15-2024 ",
    ]

    invalid_dates = [
        "00-15-2024",
        "13-15-2024",
        "01-32-2024",
        "04-31-2024",
        "02-30-2024",
        "01-00-2024",
        "not-a-date",
        "",
        None,
    ]

    for date in valid_dates:
        assert module_0.valid_date(date) is True

    for date in invalid_dates:
        assert module_0.valid_date(date) is False

# Generated at 2026-10-24 23:21:02.418172
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024")
    assert module_0.valid_date("12-31-2024")
    assert module_0.valid_date("04-30-2024")
    assert module_0.valid_date(" 06-15-2024 ")
    assert module_0.valid_date("02-29-2024")  # Leap year
    assert module_0.valid_date("02-29-2000")  # Divisible by 400

    # Invalid months
    assert not module_0.valid_date("00-10-2024")
    assert not module_0.valid_date("13-10-2024")

    # Invalid days
    assert not module_0.valid_date("01-00-2024")
    assert not module_0.valid_date("01-32-2024")
    assert not module_0.valid_date("04-31-2024")
    assert not module_0.valid_date("02-30-2024")

    # Invalid leap-year dates
    assert not module_0.valid_date("02-29-2023")
    assert not module_0.valid_date("02-29-1900")

    # Invalid years and formats
    assert not module_0.valid_date("01-01-0")
    assert not module_0.valid_date("not-a-date")
    assert not module_0.valid_date("01/01/2024")
    assert not module_0.valid_date("01-01")
    assert not module_0.valid_date("")
    assert not module_0.valid_date(None)

# Generated at 2026-10-24 23:21:14.193682
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 06-15-2023 ") is True

    # Invalid days
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("02-29-2023") is False
    assert module_0.valid_date("01-00-2024") is False

    # Invalid months and input formats
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:21:23.924513
# Unit test for function valid_date

# Generated at 2026-10-24 23:21:26.346301
# Unit test for function valid_date

# Generated at 2026-10-24 23:21:28.763916
# Unit test for function valid_date

# Generated at 2026-10-24 23:21:31.179768
# Unit test for function valid_date

# Generated at 2026-10-24 23:21:33.601861
# Unit test for function valid_date

# Generated at 2026-10-24 23:21:36.019086
# Unit test for function valid_date

# Generated at 2026-10-24 23:21:38.436409
# Unit test for function valid_date

# Generated at 2026-10-24 23:21:40.851173
# Unit test for function valid_date

# Generated at 2026-10-24 23:21:43.450437
# Unit test for function valid_date

# Generated at 2026-10-24 23:21:55.179779
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024")
    assert module_0.valid_date("12-31-2024")
    assert module_0.valid_date("04-30-2024")
    assert module_0.valid_date("02-29-2024")       # Leap year
    assert module_0.valid_date(" 06-15-2023 ")     # Surrounding whitespace

    # Invalid dates
    assert not module_0.valid_date("13-01-2024")   # Invalid month
    assert not module_0.valid_date("00-10-2024")
    assert not module_0.valid_date("04-31-2024")   # April has 30 days
    assert not module_0.valid_date("02-30-2024")
    assert not module_0.valid_date("02-29-2023")   # Not a leap year
    assert not module_0.valid_date("01-00-2024")
    assert not module_0.valid_date("not-a-date")
    assert not module_0.valid_date("")
    assert not module_0.valid_date(None)

# Generated at 2026-10-24 23:22:07.460762
# Unit test for function valid_date
def test_valid_date():
    valid_dates = [
        "01-01-2024",
        "1-1-2024",
        "12-31-2024",
        "04-30-2024",
        "02-29-2024",
        "  06-15-2020  ",
    ]

    invalid_dates = [
        "00-10-2024",   # Invalid month
        "13-10-2024",
        "01-00-2024",   # Invalid day
        "01-32-2024",
        "04-31-2024",
        "02-30-2024",
        "not-a-date",
        "01/01/2024",
        "01-01",
        "",
        None,
    ]

    for date in valid_dates:
        assert module_0.valid_date(date) is True, f"Expected {date!r} to be valid"

    for date in invalid_dates:
        assert module_0.valid_date(date) is False, f"Expected {date!r} to be invalid"

# Generated at 2026-10-24 23:22:21.574947
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True
    assert module_0.valid_date("02-29-2024") is True  # Leap year

    # Invalid months and days
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats
    assert module_0.valid_date("2024-01-01") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("invalid") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

    # Non-leap year
    assert module_0.valid_date("02-29-2023") is False

# Generated at 2026-10-24 23:22:29.325082
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
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("January-01-2024") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:22:41.337030
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

    # Invalid formats
    assert module_0.valid_date("01/15/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:22:43.757522
# Unit test for function valid_date

# Generated at 2026-10-24 23:22:52.601608
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("01-31-2024") is True

# Generated at 2026-10-24 23:23:08.373780
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 06-15-2023 ") is True

    # Invalid months and days
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False

    # February and leap-year cases
    assert module_0.valid_date("02-29-2023") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("02-29-1900") is False
    assert module_0.valid_date("02-29-2000") is True

    # Invalid formats and values
    assert module_0.valid_date("2024-01-01") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:23:20.043628
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

    # Invalid months and input formats
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:23:30.875973
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True
    assert module_0.valid_date("02-29-2024") is True

    # Invalid months and days
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid formats
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

    # Leap-year validation
    assert module_0.valid_date("02-29-2023") is False

# Generated at 2026-10-24 23:23:33.294616
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:35.712900
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:38.323748
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:40.842479
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:43.259527
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:45.675768
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:48.093097
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:50.507038
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:52.925694
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:55.348062
# Unit test for function valid_date

# Generated at 2026-10-24 23:23:57.952693
# Unit test for function valid_date

# Generated at 2026-10-24 23:24:04.304196
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("01-31-2024") is True

# Generated at 2026-10-24 23:24:15.424855
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
    assert module_0.valid_date("02-29-2023") is False

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid input
    assert module_0.valid_date("") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:24:24.044037
# Unit test for function valid_date
def test_valid_date():import pytest

@pytest.mark.parametrize("date", [
    "01-01-2024",
    "12-31-2024",
    "04-30-2024",
    "02-29-2024",  # Leap year
    " 06-15-2023 ",
])
def test_valid_date(date):
    assert module_0.valid_date(date) is True


@pytest.mark.parametrize("date", [
    "00-10-2024",
    "13-10-2024",
    "01-00-2024",
    "01-32-2024",
    "04-31-2024",
    "02-30-2024",
    "02-29-2023",  # Not a leap year
    "not-a-date",
    "01/01/2024",
    "",
    None,
])
def test_invalid_date(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 23:24:34.851352
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("01-15-2024") is True

# Generated at 2026-10-24 23:24:45.240785
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
    assert module_0.valid_date("02-29-2023") is False
    assert module_0.valid_date("02-30-2024") is False
    assert module_0.valid_date("05-00-2024") is False

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid formats and types
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:24:58.062007
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 06-15-2024 ") is True

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Invalid months
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False

    # Invalid formats and values
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("invalid") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:25:08.697292
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

    # Invalid formats and values
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:25:26.406325
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("01-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-28-2023") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 12-31-2024 ") is True

    # Invalid days
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Leap-year cases
    assert module_0.valid_date("02-29-2023") is False
    assert module_0.valid_date("02-29-1900") is False
    assert module_0.valid_date("02-29-2000") is True

    # Invalid months and years
    assert module_0.valid_date("00-15-2024") is False
    assert module_0.valid_date("13-15-2024") is False
    assert module_0.valid_date("01-01-0000") is False

    # Invalid formats and types
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("01-01") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:25:37.995554
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
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

    # Malformed input
    assert module_0.valid_date("") is False
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/15/2024") is False
    assert module_0.valid_date("01-15") is False
    assert module_0.valid_date(None) is False

# Generated at 2026-10-24 23:25:51.706284
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-01-2024") is True
    assert module_0.valid_date("12-31-2024") is True
    assert module_0.valid_date("04-30-2024") is True
    assert module_0.valid_date("02-29-2024") is True
    assert module_0.valid_date(" 06-15-2023 ") is True

    # Invalid month/day combinations
    assert module_0.valid_date("00-10-2024") is False
    assert module_0.valid_date("13-10-2024") is False
    assert module_0.valid_date("01-00-2024") is False
    assert module_0.valid_date("01-32-2024") is False
    assert module_0.valid_date("04-31-2024") is False
    assert module_0.valid_date("02-30-2024") is False

    # Leap-year validation
    assert module_0.valid_date("02-29-2023") is False

    # Malformed input
    assert module_0.valid_date("not-a-date") is False
    assert module_0.valid_date("01/01/2024") is False
    assert module_0.valid_date("") is False
    assert module_0.valid_date(None) is False