

# Generated at 2026-10-24 13:55:19.549328
# Unit test for function valid_date

# Generated at 2026-10-24 13:55:21.965526
# Unit test for function valid_date

# Generated at 2026-10-24 13:55:50.241585
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("6-15-2020") == True

# Generated at 2026-10-24 13:56:17.278028
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:56:19.820623
# Unit test for function valid_date

# Generated at 2026-10-24 13:56:22.368101
# Unit test for function valid_date

# Generated at 2026-10-24 13:56:24.784525
# Unit test for function valid_date

# Generated at 2026-10-24 13:56:27.209145
# Unit test for function valid_date

# Generated at 2026-10-24 13:56:46.875041
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("6-15-2020") == True

# Generated at 2026-10-24 13:56:48.303232
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:56:49.631520
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:56:50.955226
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:56:52.400252
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:56:53.728975
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:56:55.180468
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:56:56.500378
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:56:57.818147
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:56:59.271887
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:00.693175
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:02.127145
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:04.645196
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:07.060172
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:09.474888
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:11.889872
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:14.313372
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:16.874456
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:19.292334
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:21.702834
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:24.133751
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:26.554467
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:28.972059
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:31.393850
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:33.809293
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:36.225672
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:38.640259
# Unit test for function valid_date

# Generated at 2026-10-24 13:57:40.045647
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:41.366133
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:42.688156
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:44.008742
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:45.357793
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:46.663328
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:47.970140
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:49.297810
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:50.606993
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:51.950632
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:53.273440
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:54.664331
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:56.084907
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:57.469088
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:57:58.783105
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:00.278970
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:01.611792
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:02.992261
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:04.346992
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:05.735390
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:07.053450
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:08.379811
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:09.813497
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:11.134691
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:12.444872
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 13:58:15.916973
# Unit test for function valid_date

# Generated at 2026-10-24 13:58:18.330460
# Unit test for function valid_date

# Generated at 2026-10-24 13:58:20.751897
# Unit test for function valid_date

# Generated at 2026-10-24 13:58:23.160455
# Unit test for function valid_date

# Generated at 2026-10-24 13:58:25.575472
# Unit test for function valid_date

# Generated at 2026-10-24 13:58:27.993633
# Unit test for function valid_date

# Generated at 2026-10-24 13:58:30.408803
# Unit test for function valid_date

# Generated at 2026-10-24 13:58:32.914502
# Unit test for function valid_date

# Generated at 2026-10-24 13:58:35.328938
# Unit test for function valid_date

# Generated at 2026-10-24 13:58:37.742004
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:15.965348
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:18.384713
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:20.963047
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:23.514070
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:25.927219
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:28.340631
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:30.752133
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:33.166702
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:35.583289
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:37.992650
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:40.405610
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:42.818872
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:45.232429
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:47.647376
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:50.060987
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:52.478272
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:54.886815
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:57.300275
# Unit test for function valid_date

# Generated at 2026-10-24 13:59:59.713463
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:02.127483
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:05.814685
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:07.131373
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:08.532277
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:09.850799
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:11.204405
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:12.591028
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:13.902970
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:15.214747
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:16.547730
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:17.863717
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:00:25.895992
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:28.483885
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:30.897219
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:33.310830
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:35.723796
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:38.543110
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:40.959899
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:43.374610
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:45.787762
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:48.199706
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:50.614346
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:53.223644
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:55.637452
# Unit test for function valid_date

# Generated at 2026-10-24 14:00:58.052519
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:00.463860
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:02.879876
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:05.293258
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:07.705380
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:25.740899
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:43.625603
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("6-15-2020") == True

# Generated at 2026-10-24 14:01:46.184998
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:48.798225
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:51.210734
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:53.623866
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:56.037490
# Unit test for function valid_date

# Generated at 2026-10-24 14:01:58.670142
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:01.083676
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:03.501577
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:05.910914
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:18.056674
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:20.469133
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:22.883573
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:25.295539
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:27.707341
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:30.120308
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:32.533732
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:34.945899
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:37.360256
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:39.771644
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:42.185165
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:44.599330
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:47.015351
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:49.435184
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:51.859544
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:54.282085
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:56.696523
# Unit test for function valid_date

# Generated at 2026-10-24 14:02:59.117118
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:01.996704
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:19.920363
# Unit test for function valid_date
def test_valid_date():assert module_0.valid_date("6-15-2020") == True

# Generated at 2026-10-24 14:03:21.251726
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:03:22.646854
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:03:24.030867
# Unit test for function valid_date
def test_valid_date():import pytest

# paste your valid_date above, or: from solution import valid_date

VALID = [
    "1-1-2020", "01-01-2020", " 12-31-1999 ", "2-29-2020", "2-29-2000",
    "4-30-2020", "12-31-2020", "1-31-2021",
]

INVALID = [
    "0-01-2020",      # month < 1
    "13-01-2020",     # month > 12
    "1-0-2020",       # day < 1
    "1-32-2020",      # day > 31
    "4-31-2020",      # April has 30
    "6-31-2020",      # June has 30
    "2-30-2020",      # Feb never has 30
    "2-29-2019",      # 2019 not a leap year
    "2-29-1900",      # 1900 is a century non-leap year
    "2020-01-01",     # wrong field order
    "1-1",            # missing field
    "1-1-2020-5",     # extra field
    "",               # empty
    "abc",            # garbage
    "1/1/2020",       # wrong separator
]

@pytest.mark.parametrize("date", VALID)
def test_accepts_valid(date):
    assert module_0.valid_date(date) is True

@pytest.mark.parametrize("date", INVALID)
def test_rejects_invalid(date):
    assert module_0.valid_date(date) is False

# Generated at 2026-10-24 14:03:37.609317
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:40.021159
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:42.433426
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:44.847294
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:47.266278
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:49.681662
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:52.098633
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:54.514608
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:56.932024
# Unit test for function valid_date

# Generated at 2026-10-24 14:03:59.486993
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:01.902796
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:04.317377
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:06.733307
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:09.150655
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:11.564842
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:13.980364
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:16.397490
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:18.814713
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:21.233300
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:23.652085
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:26.073062
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:28.484037
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:30.897815
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:33.311718
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:35.720617
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:38.134815
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:40.547686
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:42.966064
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:45.378887
# Unit test for function valid_date

# Generated at 2026-10-24 14:04:47.793442
# Unit test for function valid_date

# Generated at 2026-10-24 14:05:07.626693
# Unit test for function valid_date

# Generated at 2026-10-24 14:05:10.042901
# Unit test for function valid_date

# Generated at 2026-10-24 14:05:12.455484
# Unit test for function valid_date

# Generated at 2026-10-24 14:05:14.870921
# Unit test for function valid_date

# Generated at 2026-10-24 14:05:17.283322
# Unit test for function valid_date

# Generated at 2026-10-24 14:05:19.696318
# Unit test for function valid_date