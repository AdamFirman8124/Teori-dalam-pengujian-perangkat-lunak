

# Generated at 2026-11-02 17:52:37.996243
# Unit test for function valid_date
def test_valid_date():
    # nonce:90cc0e79
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('02-29-2020') == True  # Feb allows up to 29
    assert module_0.valid_date('  03-11-2000  ') == True  # whitespace stripped

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('00-10-2012') == False
    assert module_0.valid_date('13-01-2012') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('02-30-2020') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('06-31-2021') == False

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('03-11') == False
    assert module_0.valid_date('03-11-2000-extra') == False
    assert module_0.valid_date('abc-def-ghij') == False
    assert module_0.valid_date('03/11/2000') == False
    assert module_0.valid_date('a-b-c') == False

# Generated at 2026-11-02 17:55:15.791927
# Unit test for function valid_date
def test_valid_date():# Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('12-31-2022') == True
    assert module_0.valid_date('11-30-2022') == True
    assert module_0.valid_date('08-31-2022') == True
    assert module_0.valid_date('07-31-2022') == True
    assert module_0.valid_date('02-29-2020') == True   # Feb 29 accepted (no leap-year check)
    assert module_0.valid_date('2-3-2011') == True     # single-digit month/day
    assert module_0.valid_date('  01-15-2022  ') == True  # surrounding whitespace stripped

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('13-01-2022') == False
    assert module_0.valid_date('00-01-2022') == False
    assert module_0.valid_date('-1-01-2022') == False
    assert module_0.valid_date('2000-01-01') == False  # month out of range

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('01-00-2022') == False
    assert module_0.valid_date('12-00-2022') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('01-32-2022') == False
    assert module_0.valid_date('01--1-2022') == False  # negative day

    # Day out of range for 30-day months
    assert module_0.valid_date('04-31-2022') == False
    assert module_0.valid_date('06-31-2022') == False
    assert module_0.valid_date('09-31-2022') == False
    assert module_0.valid_date('11-31-2022') == False

    # February bounds
    assert module_0.valid_date('02-30-2022') == False
    assert module_0.valid_date('02-30-2021') == False
    assert module_0.valid_date('02-0-2022') == False

    # Malformed input -> caught by except
    assert module_0.valid_date('') == False
    assert module_0.valid_date('01-01') == False
    assert module_0.valid_date('01-01-2022-01') == False
    assert module_0.valid_date('ab-01-2022') == False
    assert module_0.valid_date('01-ab-2022') == False
    assert module_0.valid_date('01-01-abcd') == False
    assert module_0.valid_date(None) == False
    assert module_0.valid_date(123) == False

    # Year is not validated by the implementation
    assert module_0.valid_date('01-01-99999') == True

    print("test_valid_date passed")

# Generated at 2026-11-02 17:56:45.811579
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('06-06-2005') == True
    assert module_0.valid_date('08-04-2045') == True
    assert module_0.valid_date('02-29-2020') == True    # February allows up to 29 days
    assert module_0.valid_date(' 01-01-2020 ') == True  # leading/trailing whitespace is stripped

    # Invalid month values
    assert module_0.valid_date('15-01-1999') == False
    assert module_0.valid_date('21-11-2000') == False
    assert module_0.valid_date('13-01-2020') == False
    assert module_0.valid_date('00-10-2020') == False

    # Invalid day values
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('04-0-1234') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('06-88-2010') == False
    assert module_0.valid_date('04-31-3000') == False   # April has at most 30 days
    assert module_0.valid_date('02-30-2020') == False   # February has at most 29 days

    # Malformed input / exceptions
    assert module_0.valid_date('') == False
    assert module_0.valid_date('abc-01-2020') == False
    assert module_0.valid_date('01-01') == False
    assert module_0.valid_date('01/01/2020') == False
    assert module_0.valid_date(None) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_valid_date()

# Generated at 2026-11-02 17:59:54.363863
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('06-06-2005') == True
    assert module_0.valid_date('04-12-2003') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('02-29-2020') == True   # Feb 29 allowed (no leap-year check)
    assert module_0.valid_date('3-4-2020') == True     # single-digit month/day accepted
    assert module_0.valid_date('  04-12-2003  ') == True  # surrounding whitespace stripped

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('21-31-2000') == False
    assert module_0.valid_date('00-01-2021') == False
    assert module_0.valid_date('13-01-2021') == False
    assert module_0.valid_date('2003-04-12') == False  # wrong field order

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('11-31-2020') == False
    assert module_0.valid_date('02-30-2021') == False
    assert module_0.valid_date('02-00-2021') == False

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('04122003') == False
    assert module_0.valid_date('111011') == False
    assert module_0.valid_date('1101104') == False
    assert module_0.valid_date('04-12') == False
    assert module_0.valid_date('04-12-2003-01') == False
    assert module_0.valid_date('abc-def-ghij') == False
    assert module_0.valid_date('04-12-20x3') == False
    assert module_0.valid_date('04--2003') == False

    print("All test_valid_date tests passed!")

# Generated at 2026-11-02 18:01:00.057884
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('1-1-2020') == True
    assert module_0.valid_date('  12-31-1999  ') == True  # leading/trailing whitespace stripped
    assert module_0.valid_date('02-29-2020') == True      # Feb 29 allowed
    assert module_0.valid_date('04-30-2021') == True

    # Invalid month
    assert module_0.valid_date('00-01-2012') == False
    assert module_0.valid_date('13-05-2020') == False
    assert module_0.valid_date('15-01-2012') == False

    # Invalid day
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('06-00-2020') == False
    assert module_0.valid_date('04-31-2011') == False     # April has 30 days
    assert module_0.valid_date('02-30-2011') == False

    # Malformed input / exception paths
    assert module_0.valid_date('03-11-2000x') == False    # non-integer year
    assert module_0.valid_date('a-11-2000') == False      # non-integer month
    assert module_0.valid_date('03/11/2000') == False     # wrong separator -> wrong split count
    assert module_0.valid_date('') == False
    assert module_0.valid_date('03-11') == False          # missing year -> ValueError
    assert module_0.valid_date('2000-03-11') == False     # month out of range after split

    # Non-string input triggers exception handler
    assert module_0.valid_date(None) == False
    assert module_0.valid_date(123) == False