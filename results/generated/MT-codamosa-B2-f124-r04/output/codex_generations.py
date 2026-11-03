

# Generated at 2026-11-02 13:42:10.147888
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('11-30-2021') == True
    assert module_0.valid_date('12-31-2022') == True
    assert module_0.valid_date('02-29-2020') == True
    assert module_0.valid_date('1-1-2021') == True
    assert module_0.valid_date('  03-11-2000  ') == True  # whitespace stripped

    # Invalid month
    assert module_0.valid_date('15-01-2019') == False
    assert module_0.valid_date('00-01-2019') == False
    assert module_0.valid_date('13-01-2019') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('04-31-2021') == False  # April has 30 days
    assert module_0.valid_date('06-31-2021') == False  # June has 30 days
    assert module_0.valid_date('09-31-2021') == False  # September has 30 days
    assert module_0.valid_date('02-30-2021') == False  # February has max 29 days
    assert module_0.valid_date('03-32-2021') == False
    assert module_0.valid_date('01-32-2021') == False

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('06/04/2020') == False
    assert module_0.valid_date('06-04-2020extra') == False
    assert module_0.valid_date('abc-def-ghij') == False
    assert module_0.valid_date('1-1') == False
    assert module_0.valid_date('06-04') == False
    assert module_0.valid_date('06-04-2020-01') == False

# Generated at 2026-11-02 13:42:44.126666
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-15-2019') == True
    assert module_0.valid_date('02-29-2020') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('1-1-2011') == True

    # Leading/trailing whitespace is stripped
    assert module_0.valid_date('  03-11-2000  ') == True

    # Invalid month
    assert module_0.valid_date('15-01-2019') == False
    assert module_0.valid_date('00-01-2019') == False
    assert module_0.valid_date('13-01-2019') == False

    # Invalid day
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('02-30-2021') == False
    assert module_0.valid_date('02-00-2021') == False

    # Malformed input caught by exception handling
    assert module_0.valid_date('') == False
    assert module_0.valid_date('abc') == False
    assert module_0.valid_date('03/11/2000') == False
    assert module_0.valid_date('03-11') == False
    assert module_0.valid_date('03-11-20a0') == False
    assert module_0.valid_date('03-11-2000-extra') == False

# Generated at 2026-11-02 13:43:14.484416
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('12-31-2020') == True
    assert module_0.valid_date('01-01-1999') == True
    assert module_0.valid_date('04-30-2021') == True
    assert module_0.valid_date('02-29-2020') == True
    assert module_0.valid_date('  06-15-2025  ') == True  # extra whitespace

    # Invalid month
    assert module_0.valid_date('13-11-2000') == False
    assert module_0.valid_date('00-11-2000') == False
    assert module_0.valid_date('99-11-2000') == False

    # Invalid day
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('03-00-2011') == False
    assert module_0.valid_date('04-31-2011') == False  # April has 30 days
    assert module_0.valid_date('02-30-2021') == False  # February max 29
    assert module_0.valid_date('06-32-2022') == False

    # Invalid format / unparseable input
    assert module_0.valid_date('2000-03-11') == False   # wrong order
    assert module_0.valid_date('03/11/2000') == False   # wrong separator
    assert module_0.valid_date('month-4-2044') == False # non-numeric
    assert module_0.valid_date('') == False             # empty string
    assert module_0.valid_date('03-11') == False        # missing year
    assert module_0.valid_date('abc') == False          # no separators
    assert module_0.valid_date('03-11-2000-01') == False  # too many parts

    print("All test_valid_date tests passed!")


if __name__ == "__main__":
    test_valid_date()

# Generated at 2026-11-02 13:44:54.935077
# Unit test for function valid_date
def test_valid_date():# Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('12-31-1999') == True
    assert module_0.valid_date('02-29-2020') == True      # Feb 29 accepted (no leap-year check)
    assert module_0.valid_date('1-1-2020') == True        # single-digit month/day are fine
    assert module_0.valid_date('  05-15-2021  ') == True  # surrounding whitespace is stripped

    # Invalid month
    assert module_0.valid_date('00-10-2020') == False
    assert module_0.valid_date('13-05-2020') == False
    assert module_0.valid_date('15-01-2012') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False      # day 0
    assert module_0.valid_date('03-32-2011') == False     # 31-day month overflow
    assert module_0.valid_date('04-31-3000') == False     # April has 30 days
    assert module_0.valid_date('11-31-2020') == False     # November has 30 days
    assert module_0.valid_date('06-00-2020') == False     # day 0 in 30-day month
    assert module_0.valid_date('02-30-2020') == False     # February has at most 29 days

    # Malformed input / exceptions
    assert module_0.valid_date('') == False
    assert module_0.valid_date('2020/01/01') == False     # wrong separator
    assert module_0.valid_date('abc-def-ghij') == False   # non-numeric parts
    assert module_0.valid_date('03-11') == False          # too few parts
    assert module_0.valid_date('03-11-2000-extra') == False  # too many parts
    assert module_0.valid_date(123) == False              # non-string input
    assert module_0.valid_date(None) == False             # None input

    print("All tests passed!")

# Generated at 2026-11-02 13:45:33.007449
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('11-30-2011') == True
    assert module_0.valid_date('1-1-2020') == True
    assert module_0.valid_date('01-15-2021') == True
    assert module_0.valid_date('12-31-1999') == True
    assert module_0.valid_date('04-30-2021') == True
    assert module_0.valid_date('02-29-2020') == True
    assert module_0.valid_date('02-28-2021') == True

    # Whitespace handling
    assert module_0.valid_date('  06-18-2020  ') == True

    # Invalid month
    assert module_0.valid_date('00-15-2020') == False
    assert module_0.valid_date('13-06-2020') == False
    assert module_0.valid_date('99-01-2020') == False

    # Invalid day
    assert module_0.valid_date('01-32-2020') == False
    assert module_0.valid_date('01-0-2020') == False
    assert module_0.valid_date('06-31-2011') == False  # April has 30 days
    assert module_0.valid_date('04-31-2021') == False
    assert module_0.valid_date('09-31-2021') == False
    assert module_0.valid_date('11-31-2021') == False
    assert module_0.valid_date('02-30-2020') == False
    assert module_0.valid_date('02-31-2020') == False

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('   ') == False
    assert module_0.valid_date('01-01') == False
    assert module_0.valid_date('01-01-2020-extra') == False
    assert module_0.valid_date('01/01/2020') == False
    assert module_0.valid_date('abc-01-2000') == False
    assert module_0.valid_date('01-ab-2000') == False
    assert module_0.valid_date('01-01-abcd') == False
    assert module_0.valid_date(None) == False

    # Note: leap years are not validated; Feb 29 always accepted
    assert module_0.valid_date('02-29-2021') == True