

# Generated at 2026-11-02 16:55:40.656896
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('06-06-2005') == True
    assert module_0.valid_date('04-12-2003') == True
    assert module_0.valid_date(' 12-31-2021 ') == True  # whitespace stripped

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('21-31-2000') == False
    assert module_0.valid_date('00-10-2020') == False
    assert module_0.valid_date('13-01-2020') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('02-30-2021') == False
    assert module_0.valid_date('11-31-2020') == False

    # February allowed up to 29 (leap years not checked)
    assert module_0.valid_date('02-29-2020') == True
    assert module_0.valid_date('02-29-2021') == True

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('04122003') == False
    assert module_0.valid_date('20030412') == False
    assert module_0.valid_date('2003-04') == False
    assert module_0.valid_date('2003-04-12') == False
    assert module_0.valid_date('04-2003') == False
    assert module_0.valid_date('ab-cd-efgh') == False
    assert module_0.valid_date('03-11-2000-01') == False

# Generated at 2026-11-02 16:56:42.101953
# Unit test for function valid_date
def test_valid_date():
    # nonce:50cccd17
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('12-31-2020') == True
    assert module_0.valid_date('02-29-2020') == True   # Feb 29 accepted (no leap-year check)
    assert module_0.valid_date('1-1-2020') == True     # single-digit month/day ok
    assert module_0.valid_date('  03-11-2000  ') == True  # surrounding whitespace stripped

    # Invalid months
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('13-01-2020') == False
    assert module_0.valid_date('00-10-2020') == False

    # Invalid days
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('01-00-2020') == False
    assert module_0.valid_date('02-30-2021') == False
    assert module_0.valid_date('04-31-3000') == False  # April has only 30 days
    assert module_0.valid_date('06-31-2020') == False  # June has only 30 days

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('abc') == False
    assert module_0.valid_date('03-11') == False       # missing year
    assert module_0.valid_date('03/11/2000') == False  # wrong separator
    assert module_0.valid_date('aa-bb-cccc') == False  # non-numeric parts

    print("All tests passed!")


test_valid_date()

# Generated at 2026-11-02 16:58:05.129101
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('04-12-2003') == True
    assert module_0.valid_date('06-06-2005') == True
    assert module_0.valid_date('02-29-2000') == True  # Feb allows up to 29

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('00-10-2000') == False
    assert module_0.valid_date('13-01-2012') == False
    assert module_0.valid_date('21-31-2000') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False  # April has 30 days
    assert module_0.valid_date('02-30-2000') == False  # Feb > 29
    assert module_0.valid_date('01-00-2000') == False

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('04122003') == False
    assert module_0.valid_date('20030412') == False
    assert module_0.valid_date('2003-04') == False
    assert module_0.valid_date('2003-04-12') == False
    assert module_0.valid_date('04-2003') == False
    assert module_0.valid_date('03/11/2000') == False
    assert module_0.valid_date('abc-def-ghi') == False
    assert module_0.valid_date('03-11') == False
    assert module_0.valid_date('aa-bb-cccc') == False

    # Whitespace handling (strip is applied)
    assert module_0.valid_date(' 01-01-2007 ') == True
    assert module_0.valid_date('  03-11-2000') == True
    assert module_0.valid_date('  15-01-2012  ') == False

# Generated at 2026-11-02 16:59:20.060272
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('06-06-2005') == True
    assert module_0.valid_date('04-12-2003') == True

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('21-31-2000') == False
    assert module_0.valid_date('00-10-2020') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('02-30-2021') == False

    # Invalid formats
    assert module_0.valid_date('') == False
    assert module_0.valid_date('04122003') == False
    assert module_0.valid_date('2003-04-12') == False
    assert module_0.valid_date('03-11') == False
    assert module_0.valid_date('03-11-2000-01') == False
    assert module_0.valid_date('ab-cd-efgh') == False
    assert module_0.valid_date('1-1-2000 ') == True  # trailing whitespace is stripped

# Generated at 2026-11-02 17:00:42.818594
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('02-29-2020') == True

    # Valid date with surrounding whitespace (stripped)
    assert module_0.valid_date('  03-11-2000  ') == True

    # Invalid format / unparseable input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('03-11-2000-') == False
    assert module_0.valid_date('03-11 2000') == False
    assert module_0.valid_date('a-b-c') == False
    assert module_0.valid_date('03-11') == False

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('00-01-2012') == False
    assert module_0.valid_date('13-01-2021') == False

    # Invalid days
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('06-31-2021') == False
    assert module_0.valid_date('02-30-2021') == False
    assert module_0.valid_date('01-0-2021') == False
    assert module_0.valid_date('12-0-2021') == False

    print("All tests passed!")

# Generated at 2026-11-02 17:03:55.957328
# Unit test for function valid_date
def test_valid_date():# Valid dates
    assert module_0.valid_date("01-15-2023") == True
    assert module_0.valid_date("03-31-2023") == True
    assert module_0.valid_date("04-30-2023") == True
    assert module_0.valid_date("02-29-2023") == True   # no leap-year check in function
    assert module_0.valid_date("12-31-1999") == True
    assert module_0.valid_date("1-1-2020") == True     # single digits accepted
    assert module_0.valid_date("  06-15-2021  ") == True  # surrounding whitespace stripped

    # Invalid month
    assert module_0.valid_date("00-10-2023") == False
    assert module_0.valid_date("13-10-2023") == False
    assert module_0.valid_date("-5-10-2023") == False

    # Invalid day
    assert module_0.valid_date("01-00-2023") == False   # day < 1 for 31-day month
    assert module_0.valid_date("01-32-2023") == False   # day > 31
    assert module_0.valid_date("04-31-2023") == False   # day > 30 for 30-day month
    assert module_0.valid_date("04-00-2023") == False   # day < 1 for 30-day month
    assert module_0.valid_date("02-30-2023") == False   # day > 29 for February
    assert module_0.valid_date("02-00-2023") == False   # day < 1 for February

    # Malformed input -> exception path returns False
    assert module_0.valid_date("") == False                 # cannot unpack
    assert module_0.valid_date("01-15") == False            # too few parts
    assert module_0.valid_date("01-15-2023-extra") == False # too many parts
    assert module_0.valid_date("aa-bb-cccc") == False       # non-numeric
    assert module_0.valid_date("01/15/2023") == False       # wrong separator
    assert module_0.valid_date("-1-15-2023") == False       # leading '-' creates extra part

    print("All valid_date tests passed!")