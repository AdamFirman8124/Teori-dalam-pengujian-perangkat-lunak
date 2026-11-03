

# Generated at 2026-11-02 18:48:21.503234
# Unit test for function valid_date
def test_valid_date():
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('06-06-2005') == True
    assert module_0.valid_date('21-31-2000') == False
    assert module_0.valid_date('04-12-2003') == True
    assert module_0.valid_date('04122003') == False
    assert module_0.valid_date('20030412') == False
    assert module_0.valid_date('2003-04') == False
    assert module_0.valid_date('2003-04-12') == False
    assert module_0.valid_date('04-2003') == False

# Generated at 2026-11-02 18:49:58.628143
# Unit test for function valid_date
def test_valid_date():
# nonce:bdc2e0ae
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('1-1-2012') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('02-29-2021') == True  # Feb 29 accepted (no leap-year check)
    assert module_0.valid_date(' 04-30-2020 ') == True  # surrounding whitespace stripped

    # Invalid months
    assert module_0.valid_date('00-01-2012') == False
    assert module_0.valid_date('13-01-2012') == False
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('2000-01-01') == False  # wrong field order -> month=2000

    # Invalid days
    assert module_0.valid_date('01-00-2012') == False
    assert module_0.valid_date('01-32-2012') == False
    assert module_0.valid_date('04-31-2012') == False  # April has 30 days
    assert module_0.valid_date('06-0-2012') == False
    assert module_0.valid_date('02-30-2012') == False  # Feb max 29
    assert module_0.valid_date('11-31-2012') == False  # November has 30 days

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('01-01') == False          # missing year
    assert module_0.valid_date('01-01-2012-05') == False  # too many fields
    assert module_0.valid_date('01/01/2012') == False     # wrong separator
    assert module_0.valid_date('abc-01-2012') == False    # non-numeric month
    assert module_0.valid_date('01-aa-2012') == False     # non-numeric day
    assert module_0.valid_date(None) == False             # not a string

    print("All test cases passed!")


if __name__ == "__main__":
    test_valid_date()

# Generated at 2026-11-02 18:51:13.842236
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('06-04-2020') == True
    assert module_0.valid_date('01-01-2007') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('1-1-2020') == True
    assert module_0.valid_date('02-29-2020') == True

    # Whitespace is stripped
    assert module_0.valid_date('  01-01-2020  ') == True

    # Invalid month
    assert module_0.valid_date('15-01-2012') == False
    assert module_0.valid_date('13-13-2011') == False
    assert module_0.valid_date('00-10-2020') == False

    # Invalid day
    assert module_0.valid_date('04-0-2040') == False
    assert module_0.valid_date('03-32-2011') == False
    assert module_0.valid_date('04-31-3000') == False
    assert module_0.valid_date('06-31-2020') == False
    assert module_0.valid_date('02-30-2021') == False
    assert module_0.valid_date('01-00-2020') == False

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('01/01/2020') == False
    assert module_0.valid_date('01-01') == False
    assert module_0.valid_date('01-01-2020-extra') == False
    assert module_0.valid_date('aa-bb-cccc') == False
    assert module_0.valid_date('2020-01-01') == False

# Generated at 2026-11-02 18:53:08.599584
# Unit test for function valid_date
def test_valid_date():
    # Valid dates
    assert module_0.valid_date("01-31-2023") == True
    assert module_0.valid_date("1-1-2023") == True
    assert module_0.valid_date("02-29-2023") == True
    assert module_0.valid_date("03-15-2023") == True
    assert module_0.valid_date("04-30-2023") == True
    assert module_0.valid_date("06-15-2023") == True
    assert module_0.valid_date("09-30-2021") == True
    assert module_0.valid_date("11-30-1999") == True
    assert module_0.valid_date("12-25-2023") == True
    assert module_0.valid_date(" 06-15-2023 ") == True  # surrounding whitespace is stripped
    assert module_0.valid_date("01-15-0000") == True    # year is not validated

    # Invalid month
    assert module_0.valid_date("00-10-2023") == False
    assert module_0.valid_date("13-01-2023") == False
    assert module_0.valid_date("99-01-2023") == False

    # Invalid day for 31-day months
    assert module_0.valid_date("01-32-2023") == False
    assert module_0.valid_date("01-00-2023") == False
    assert module_0.valid_date("03-45-2023") == False

    # Invalid day for 30-day months
    assert module_0.valid_date("04-31-2023") == False
    assert module_0.valid_date("06-31-2023") == False
    assert module_0.valid_date("09-31-2023") == False
    assert module_0.valid_date("11-31-2023") == False

    # Invalid day for February
    assert module_0.valid_date("02-30-2023") == False
    assert module_0.valid_date("02-31-2023") == False
    assert module_0.valid_date("02-00-2023") == False

    # Malformed input
    assert module_0.valid_date("") == False
    assert module_0.valid_date("01/15/2023") == False
    assert module_0.valid_date("01-15") == False
    assert module_0.valid_date("01-15-2023-extra") == False
    assert module_0.valid_date("abc-15-2023") == False
    assert module_0.valid_date("01-xy-2023") == False
    assert module_0.valid_date("01-15-abcd") == False

    # Non-string inputs trigger the except branch
    assert module_0.valid_date(None) == False
    assert module_0.valid_date(12345) == False
    assert module_0.valid_date(["01-15-2023"]) == False

# Generated at 2026-11-02 18:55:13.257658
# Unit test for function valid_date
def test_valid_date():
    # nonce:819610a9
    # Valid dates
    assert module_0.valid_date('03-11-2000') == True
    assert module_0.valid_date('01-31-2021') == True
    assert module_0.valid_date('12-31-2021') == True
    assert module_0.valid_date('02-29-2020') == True
    assert module_0.valid_date('04-30-2021') == True
    assert module_0.valid_date('06-15-2021') == True
    assert module_0.valid_date('09-28-2021') == True
    assert module_0.valid_date('11-30-2021') == True
    assert module_0.valid_date('3-11-2000') == True          # no zero padding
    assert module_0.valid_date('  03-11-2000  ') == True     # surrounding whitespace

    # Invalid months
    assert module_0.valid_date('00-10-2000') == False
    assert module_0.valid_date('13-01-2000') == False
    assert module_0.valid_date('99-01-2000') == False

    # Invalid days
    assert module_0.valid_date('01-00-2021') == False
    assert module_0.valid_date('01-32-2021') == False
    assert module_0.valid_date('04-31-2021') == False        # April has 30 days
    assert module_0.valid_date('06-31-2021') == False        # June has 30 days
    assert module_0.valid_date('09-31-2021') == False        # September has 30 days
    assert module_0.valid_date('11-31-2021') == False        # November has 30 days
    assert module_0.valid_date('02-00-2021') == False
    assert module_0.valid_date('02-30-2021') == False        # February max 29

    # Malformed input
    assert module_0.valid_date('') == False
    assert module_0.valid_date('abc') == False
    assert module_0.valid_date('a-b-c') == False
    assert module_0.valid_date('3-11') == False              # missing year
    assert module_0.valid_date('03/11/2000') == False        # wrong separator
    assert module_0.valid_date('03-11-2000a') == False       # non-numeric year

    print("All tests passed!")


if __name__ == '__main__':
    test_valid_date()