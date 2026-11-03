

# Generated at 2026-11-02 21:05:58.424308
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('02-29-2020') == True   # Feb 29 accepted by implementation

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('13-01-2020') == False
    assert module_0.valid_date('00-10-2020') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('01-00-2020') == False
    assert module_0.valid_date('02-30-2020') == False
    assert module_0.valid_date('04-31-2020') == False
    assert module_0.valid_date('06-31-2020') == False
    assert module_0.valid_date('11-31-2020') == False

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('junk') == False
    assert module_0.valid_date('03112000') == False
    assert module_0.valid_date('03-11-2000-extra') == False
    assert module_0.valid_date('ab-cd-efgh') == False
    assert module_0.valid_date('03/11/2000') == False

    # Whitespace around input is stripped
    assert module_0.valid_date('  03-11-2000  ') == True

    print("All tests passed!")


test_valid_date()

# Generated at 2026-11-02 21:07:13.601067
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('06-06-2005') == True
    assert module_0.valid_date('04-12-2003') == True
    assert module_0.valid_date('1-1-2011') == True
    assert module_0.valid_date('02-29-2020') == True
    assert module_0.valid_date('  01-01-2007  ') == True  # surrounding whitespace is stripped

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('21-31-2000') == False
    assert module_0.valid_date('00-01-2011') == False
    assert module_0.valid_date('13-01-2011') == False
    assert module_0.valid_date('2003-04-12') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('01-0-2011') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('01-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('02-30-2021') == False

    # Invalid format
    assert module_0.valid_date('') == False
    assert module_0.valid_date('04122003') == False
    assert module_0.valid_date('20030412') == False
    assert module_0.valid_date('2003-04') == False
    assert module_0.valid_date('04-2003') == False
    assert module_0.valid_date('abc-def-ghij') == False
    assert module_0.valid_date('03-11-2000-xyz') == False
    assert module_0.valid_date('03/11/2000') == False

# Generated at 2026-11-02 21:08:45.452767
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("03-11-2000") == True
    assert module_0.valid_date("06-04-2020") == True
    assert module_0.valid_date("02-29-2020") == True  # Feb 29 allowed by this implementation
    assert module_0.valid_date("12-31-1999") == True
    assert module_0.valid_date("1-1-2021") == True

    # Invalid month
    assert module_0.valid_date("15-01-2012") == False
    assert module_0.valid_date("00-01-2012") == False
    assert module_0.valid_date("13-01-2012") == False

    # Invalid day
    assert module_0.valid_date("04-31-2020") == False  # April has 30 days
    assert module_0.valid_date("06-31-2020") == False
    assert module_0.valid_date("09-31-2020") == False
    assert module_0.valid_date("11-31-2020") == False
    assert module_0.valid_date("02-30-2020") == False
    assert module_0.valid_date("02-31-2020") == False
    assert module_0.valid_date("01-32-2020") == False
    assert module_0.valid_date("01-00-2020") == False
    assert module_0.valid_date("01-0-2020") == False

    # Invalid formats / non-date strings
    assert module_0.valid_date("") == False
    assert module_0.valid_date("03-11-2000extra") == False
    assert module_0.valid_date("03/11/2000") == False
    assert module_0.valid_date("11-2000") == False
    assert module_0.valid_date("03-11-2000-01") == False
    assert module_0.valid_date("a-b-c") == False
    assert module_0.valid_date("ab-11-2000") == False
    assert module_0.valid_date("03-11-20x0") == False
    assert module_0.valid_date(None) == False

    # Whitespace handling (strip is applied)
    assert module_0.valid_date("  03-11-2000  ") == True

# Generated at 2026-11-02 21:08:58.453082
# Unit test for function valid_date
def test_valid_date():
# nonce:23ead0e2
    # Valid dates
    assert module_0.valid_date("03-04-2003") == True
    assert module_0.valid_date("  03-04-2003  ") == True   # whitespace is stripped
    assert module_0.valid_date("1-1-2020") == True          # single-digit month/day
    assert module_0.valid_date("12-31-2000") == True        # last day of a 31-day month
    assert module_0.valid_date("04-30-2001") == True        # last day of a 30-day month
    assert module_0.valid_date("02-29-2020") == True        # Feb 29 accepted (no leap-year check)

    # Invalid month
    assert module_0.valid_date("13-01-2000") == False
    assert module_0.valid_date("00-01-2000") == False

    # Invalid day
    assert module_0.valid_date("01-32-2000") == False       # day > 31
    assert module_0.valid_date("04-31-2001") == False       # day > 30 in a 30-day month
    assert module_0.valid_date("02-30-2000") == False       # day > 29 in February
    assert module_0.valid_date("01-00-2000") == False       # day < 1 in a 31-day month
    assert module_0.valid_date("04-00-2001") == False       # day < 1 in a 30-day month
    assert module_0.valid_date("02-00-2000") == False       # day < 1 in February

    # Malformed input
    assert module_0.valid_date("") == False
    assert module_0.valid_date("   ") == False
    assert module_0.valid_date("03-04") == False            # missing year
    assert module_0.valid_date("03/04/2003") == False       # wrong separator
    assert module_0.valid_date("ab-cd-efgh") == False       # non-numeric parts
    assert module_0.valid_date("03-04-2003-01") == False    # too many parts
    assert module_0.valid_date(20030304) == False           # non-string input (no .strip)

# Generated at 2026-11-02 21:09:28.215140
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('06-06-2005') == True
    assert module_0.valid_date('04-12-2003') == True

    # Whitespace should be stripped
    assert module_0.valid_date('  03-11-2000  ') == True

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('21-31-2000') == False
    assert module_0.valid_date('00-10-2000') == False
    assert module_0.valid_date('13-10-2000') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('02-30-2020') == False
    assert module_0.valid_date('06-31-2000') == False

    # Malformed input / wrong number of parts
    assert module_0.valid_date('') == False
    assert module_0.valid_date('04122003') == False
    assert module_0.valid_date('20030412') == False
    assert module_0.valid_date('2003-04') == False
    assert module_0.valid_date('2003-04-12') == False
    assert module_0.valid_date('04-2003') == False

    # Non-numeric components
    assert module_0.valid_date('03-aa-2000') == False
    assert module_0.valid_date('aa-11-2000') == False