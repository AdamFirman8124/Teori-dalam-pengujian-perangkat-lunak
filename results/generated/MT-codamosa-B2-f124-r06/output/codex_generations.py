

# Generated at 2026-11-02 13:35:19.483487
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('02-29-2020') == True   # Feb 29 allowed
    assert module_0.valid_date('12-31-1999') == True   # 31-day month boundary
    assert module_0.valid_date(' 03-11-2000 ') == True # surrounding whitespace is stripped

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('13-06-2020') == False
    assert module_0.valid_date('00-10-2020') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False   # day 0
    assert module_0.valid_date('03-32-2011') == False  # day > 31
    assert module_0.valid_date('04-31-3000') == False  # 31 days in a 30-day month
    assert module_0.valid_date('02-30-2021') == False  # Feb 30 invalid

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('03-11') == False       # missing year
    assert module_0.valid_date('aa-bb-cccc') == False  # non-numeric
    assert module_0.valid_date('03/11/2000') == False  # wrong separator

# Generated at 2026-11-02 13:37:38.089148
# Unit test for function valid_date
def test_valid_date():# Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2021') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('02-29-2020') == True  # Feb allows up to 29
    assert module_0.valid_date(' 03-11-2000 ') == True  # whitespace stripped

    # Invalid month
    assert module_0.valid_date('13-11-2000') == False
    assert module_0.valid_date('00-11-2000') == False
    assert module_0.valid_date('15-01-2012') == False

    # Invalid day - 31-day months
    assert module_0.valid_date('01-32-2000') == False
    assert module_0.valid_date('01-00-2000') == False
    assert module_0.valid_date('12-31-2000') == True

    # Invalid day - 30-day months
    assert module_0.valid_date('04-31-2000') == False
    assert module_0.valid_date('04-30-2000') == True
    assert module_0.valid_date('06-00-2000') == False

    # Invalid day - February
    assert module_0.valid_date('02-30-2000') == False
    assert module_0.valid_date('02-00-2000') == False
    assert module_0.valid_date('02-29-2000') == True

    # Malformed inputs
    assert module_0.valid_date('') == False
    assert module_0.valid_date('   ') == False
    assert module_0.valid_date('3-11') == False
    assert module_0.valid_date('a-b-c') == False
    assert module_0.valid_date('3/11/2000') == False
    assert module_0.valid_date('3-11-2000-xyz') == False
    assert module_0.valid_date('03-11-twothousand') == False

# Generated at 2026-11-02 13:38:42.910271
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('11-30-2021') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('02-29-2020') == True
    assert module_0.valid_date('04-12-2003') == True

    # Leading/trailing whitespace is stripped
    assert module_0.valid_date(' 06-04-2020') == True
    assert module_0.valid_date('12-31-2021 ') == True

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('13-01-2012') == False
    assert module_0.valid_date('00-10-2020') == False
    assert module_0.valid_date('21-31-2000') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('01-00-2020') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('02-30-2021') == False
    assert module_0.valid_date('06-32-2020') == False

    # Malformed input (wrong format / non-numeric parts)
    assert module_0.valid_date('') == False
    assert module_0.valid_date('04122003') == False
    assert module_0.valid_date('20030412') == False
    assert module_0.valid_date('2003-04') == False
    assert module_0.valid_date('2003-04-12') == False
    assert module_0.valid_date('04-2003') == False
    assert module_0.valid_date('a-b-c') == False
    assert module_0.valid_date('12-31-year') == False

# Generated at 2026-11-02 13:39:40.254478
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('02-29-2020') == True   # Feb 29 accepted (max day 29)
    assert module_0.valid_date('1-1-2011') == True     # single-digit parts

    # Whitespace is stripped
    assert module_0.valid_date('  03-11-2000  ') == True

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('13-01-2020') == False
    assert module_0.valid_date('00-12-2012') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('06-00-2020') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False  # April has 30 days
    assert module_0.valid_date('11-31-2020') == False  # November has 30 days
    assert module_0.valid_date('02-30-2019') == False  # February max 29

    # Malformed input -> exception path returns False
    assert module_0.valid_date('') == False
    assert module_0.valid_date('03-11') == False       # missing year
    assert module_0.valid_date('06/04/2020') == False  # wrong separator
    assert module_0.valid_date('06-04-2020-extra') == False  # too many parts
    assert module_0.valid_date('abc') == False
    assert module_0.valid_date(None) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_valid_date()

# Generated at 2026-11-02 13:40:39.038646
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('01-15-2020') == True
    assert module_0.valid_date('12-31-2019') == True
    assert module_0.valid_date('02-29-2020') == True
    assert module_0.valid_date('06-30-2021') == True
    assert module_0.valid_date('  07-04-1776  ') == True   # surrounding whitespace is stripped
    assert module_0.valid_date('1-2-3') == True            # single-digit fields parse as ints

    # Invalid month
    assert module_0.valid_date('00-10-2020') == False
    assert module_0.valid_date('13-10-2020') == False
    assert module_0.valid_date('99-99-9999') == False

    # Invalid day
    assert module_0.valid_date('01-00-2020') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('05-32-2000') == False

    # Malformed / unparseable input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('15-01-2012') == False      # month out of range
    assert module_0.valid_date('04-0-2040') == False       # day zero
    assert module_0.valid_date('ab-cd-ef') == False        # non-numeric parts
    assert module_0.valid_date('1-1') == False             # too few parts
    assert module_0.valid_date('10-10-10-10') == False     # too many parts
    assert module_0.valid_date('01-15-') == False          # empty year
    assert module_0.valid_date(None) == False              # non-string input
    assert module_0.valid_date(12345) == False             # non-string input


if __name__ == '__main__':
    test_valid_date()
    print("All tests passed!")