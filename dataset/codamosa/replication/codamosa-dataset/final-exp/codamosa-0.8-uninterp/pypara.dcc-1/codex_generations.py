

# Generated at 2022-06-14 04:35:06.151041
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Unit test for function dcfc_30_360_german.
    """

    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:35:14.143585
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    def testfunc(dcc: DCC) -> None:
        registry = DCCRegistryMachinery()
        registry.register(dcc)
    test_cases = (DCC("Act/365F", {"act/365f"}, {}, calculate_dcf_act365f),)
    for test_case in test_cases:
        do_test(test_case, testfunc, None)

# Generated at 2022-06-14 04:35:15.038222
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    unittest.main()

# Generated at 2022-06-14 04:35:27.905952
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 14) == Dec

# Generated at 2022-06-14 04:35:35.741469
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex1 = round(dcfc_nl_365(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)

# Generated at 2022-06-14 04:35:42.137782
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert(DCCRegistry['act/act'].calculate_fraction(datetime.date(2014, 2, 1), datetime.date(2014, 2, 1), datetime.date(2014, 12, 31)) == 0)
    assert(DCCRegistry['act/act'].calculate_fraction(datetime.date(2014, 2, 1), datetime.date(2014, 3, 1), datetime.date(2014, 12, 31)) == Decimal(29/366))
    assert(DCCRegistry['act/act'].calculate_fraction(datetime.date(2016, 2, 1), datetime.date(2016, 3, 1), datetime.date(2016, 12, 31)) == Decimal(29/365))

# Generated at 2022-06-14 04:35:51.649886
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    """
    Test function dcfc_30_e_360
    """
    actual = round(dcfc_30_e_360(start = datetime.date(2007,12,28), asof = datetime.date(2009,5,31)), 14)
    expected = Decimal('1.33055555555556')
    assert(actual == expected)
    actual = round(dcfc_30_e_360(start = datetime.date(2007,12,28), asof = datetime.date(2008,6,1)), 14)
    expected = Decimal('0.16666666666667')
    assert(actual == expected)
    actual = round(dcfc_30_e_360(start = datetime.date(2008,2,1), asof = datetime.date(2009,5,31)), 14)

# Generated at 2022-06-14 04:36:01.321294
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    """Test for the function dcfc_30_e_plus_360()."""

    # Start the unit test
    tgroup = "test_dcfc_30_e_plus_360"
    print_test_header(
        group=tgroup,
        text="Test dcfc_30_e_plus_360 function.",
        underline=True)

    # Test 1: ISDA spec example
    print_test_header(group=tgroup, text="ISDA spec examples")
    ex01_start = Date(day=31, month=12, year=2007)
    ex01_asof = Date(day=30, month=4, year=2008)

# Generated at 2022-06-14 04:36:08.132427
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof = datetime.date(2007,12,28), datetime.date(2008,2,28)
    ex2_start, ex2_asof = datetime.date(2007,12,28), datetime.date(2008,2,29)
    ex3_start, ex3_asof = datetime.date(2007,10,31), datetime.date(2008,11,30)
    ex4_start, ex4_asof = datetime.date(2008,2,1), datetime.date(2009,5,31)
    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal(str(0.16666666666667))
    assert round

# Generated at 2022-06-14 04:36:15.920301
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    print('Testing dcfc_30_360_us...')
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:36:41.437003
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == round(Decimal('0.16666666666667'), 14)
    assert round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == round(Decimal('0.16944444444444'), 14)

# Generated at 2022-06-14 04:36:46.282398
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    """
    Unit test for method calculate_daily_fraction of class DCC.
    """
    ## Act

# Generated at 2022-06-14 04:36:51.716951
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCC(
        name=None,
        altnames=None,
        currencies=set(),
        calculate_fraction_method=None
    ).calculate_daily_fraction(
        start=datetime.date(2020, 3, 13),
        asof=datetime.date(2020, 3, 13),
        end= datetime.date(2020, 5, 4)
    ) == 0

    assert DCC(
        name=None,
        altnames=None,
        currencies=set(),
        calculate_fraction_method=None
    ).calculate_daily_fraction(
        start=datetime.date(2020, 3, 13),
        asof=datetime.date(2020, 3, 14),
        end= datetime.date(2020, 5, 4)
    ) == 0

    assert D

# Generated at 2022-06-14 04:36:57.122768
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    dcc = '30/360 German'
    start = datetime.date(2003, 5, 26)
    asof = datetime.date(2004, 5, 26)
    end = datetime.date(2004, 5, 26)
    freq = Decimal(1) / Decimal(2)
    output = dcfc_30_360_german(start, asof, end, freq)
    expected = Decimal('1.5')
    assert_almost_equal(output, expected, places=14, msg=f'Test failed for dcfc ({dcc}).')
    start = datetime.date(2003, 5, 31)
    asof = datetime.date(2004, 5, 31)
    end = datetime.date(2004, 5, 31)
    freq = Decimal(1) / Decimal

# Generated at 2022-06-14 04:37:03.259187
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    """
    Unit test for function dcfc_act_act
    """
    ex1_start, ex1_asof = date(2007, 12, 28), date(2008, 2, 28)
    ex2_start, ex2_asof = date(2007, 12, 28), date(2008, 2, 29)
    ex3_start, ex3_asof = date(2007, 10, 31), date(2008, 11, 30)
    ex4_start, ex4_asof = date(2008, 2, 1), date(2009, 5, 31)
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478')

# Generated at 2022-06-14 04:37:09.591395
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478')



# Generated at 2022-06-14 04:37:16.337865
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    start = datetime.date(2014, 1, 1)
    end = datetime.date(2014, 4, 1)
    asof = datetime.date(2014, 3, 1)
    freq = Decimal(2)
    print("End date: ", end)
    print(DCCRegistry["ACT_360"].calculate_fraction(start,asof,end,freq))


# Generated at 2022-06-14 04:37:24.110406
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 9, 10), end=datetime.date(2020, 3, 2)), 10) == Decimal('0.5245901639')


# Generated at 2022-06-14 04:37:34.946663
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:37:40.128685
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCC("one", (), (), lambda x,y,z,q: ONE).calculate_daily_fraction(
        datetime.date(2017,1,1),
        datetime.date(2017,1,1),
        datetime.date(2018,1,1)
    ) == ONE



# Generated at 2022-06-14 04:38:07.805407
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert round(dcfc_act_365_l(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14) == Decimal('0.16939890710383')
    assert round(dcfc_act_365_l(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_l(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14) == Decimal('1.08196721311475')

# Generated at 2022-06-14 04:38:21.271691
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:38:29.069791
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:38:35.556106
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)), 10) == Decimal('0.5245901639')



# Generated at 2022-06-14 04:38:46.306758
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:38:59.023281
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    """
    Unit test for function dcfc_30_e_plus_360

    >>> ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    >>> round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)
    Decimal('0.16666666666667')

    """
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    print(round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14))

## Unit test for function

# Generated at 2022-06-14 04:39:02.048040
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    DCC_obj= DCC(name="name", altnames="altnames", currencies="currencies",calculate_fraction_method="calculate_fraction_method")
    start = datetime.date(2017,1,1)
    asof = datetime.date(2017,1,2)
    end = datetime.date(2017,1,3)
    freq = None
    result = DCC_obj.calculate_fraction(start, asof, end, freq)
    assert result == 0

# Generated at 2022-06-14 04:39:13.377835
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    start_dates = [datetime.date(2007, 12, 28), datetime.date(2007, 12, 28), datetime.date(2007, 10, 31), datetime.date(2008, 2, 1)]
    asof_dates = [datetime.date(2008, 2, 28), datetime.date(2008, 2, 29), datetime.date(2008, 11, 30), datetime.date(2009, 5, 31)]
    end_dates = [datetime.date(2008, 2, 28), datetime.date(2008, 2, 29), datetime.date(2008, 11, 30), datetime.date(2009, 5, 31)]
    freqs = [None, None, None, None]

# Generated at 2022-06-14 04:39:22.963629
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:39:34.026112
# Unit test for method interest of class DCC
def test_DCC_interest():
    from .monetary import Money
    from .currencies import Currencies
    principal = Money(100, Currencies.USD)
    rate = Decimal('0.05')
    start = Date(2017,1,1)
    asof = Date(2017,3,31)
    end = Date(2017,12,31)
    freq = Decimal('2')
    a = DCC('ACT/360', {'act360'}, {Currencies.USD}, calculate_fraction_method=None)
    assert a.interest(principal, rate, start, asof, end, freq) == Money(5, Currencies.USD)

# Generated at 2022-06-14 04:40:33.054898
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Unit test for function dcfc_30_360_german.
    """

    assert round(dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal("0.16666666666667")
    assert round(dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal("0.16944444444444")

# Generated at 2022-06-14 04:40:35.375630
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert round(dcfc_30_360_german(datetime.date(2020, 1, 31), datetime.date(2020, 2, 29), datetime.date(2020, 2, 29)), 14) == 0.16666666666667



# Generated at 2022-06-14 04:40:45.056828
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    print(__dcfc_30_e_360_doc__)
    d0 = datetime.date(2007, 12, 28)
    d1 = datetime.date(2008, 2, 28)
    d2 = datetime.date(2008, 2, 29)
    d3 = datetime.date(2007, 10, 31)
    d4 = datetime.date(2008, 11, 30)
    d5 = datetime.date(2008, 2, 1)
    d6 = datetime.date(2009, 5, 31)
    print("Example 1: %f" % dcfc_30_e_360(d0, d1, d1))
    print("Example 2: %f" % dcfc_30_e_360(d0, d2, d2))

# Generated at 2022-06-14 04:40:50.250282
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert("calculate_fraction" in dir(DCCRegistry["ACT/365"]))
    assert isinstance(DCCRegistry["ACT/365"].calculate_fraction(datetime.date(2017, 6, 28), datetime.date(2017, 6, 29), datetime.date(2017, 6, 30), None), Decimal)


# Generated at 2022-06-14 04:41:01.725231
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    import unittest

    class TestDcfc30EPlus360(unittest.TestCase):
        def test_dcfc_30_e_plus_360(self):
            ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
            ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
            ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
            ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:41:08.943104
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194')

# Generated at 2022-06-14 04:41:19.322765
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    start_date = datetime.date(2012, 12, 15)
    asof_date = datetime.date(2015, 12, 31)
    end_date = datetime.date(2016, 1, 6)
    freq = Decimal(2)

    ACT_365 = DCC("Actual/365", {"Actual/365", "Act/365", "actual/365", "act/365"}, _as_ccys({"EUR", "USD", "PLN", "RUB", "GBP"}),
                  lambda s, a, e, f: Decimal((a - s).days) / Decimal(365))

# Generated at 2022-06-14 04:41:20.144900
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    pass



# Generated at 2022-06-14 04:41:22.920641
# Unit test for method interest of class DCC
def test_DCC_interest():
    assert DCCRegistry["ACT/365"].interest(Money(1, "EUR"), Decimal(0.05), Date(datetime.date(2019, 5, 30)),Date(datetime.date(2019, 6, 28))).amount == Decimal('0.0016086956')


# Generated at 2022-06-14 04:41:34.069076
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    """
    Test cases for method register of class DCCRegistryMachinery.
    """
    ## Define a dummy DCC model:
    dcc = DCC(
        "Dummy",
        set(),
        set(),
        lambda start, asof, end, freq: ZERO
    )

    ## Create a DCC registry and register the DCC:
    registry = DCCRegistryMachinery()
    registry.register(dcc)

    ## Check if it returns the right thing:
    assert registry.find("Dummy") == dcc

## Holds the registry machinery:
_dccregistry: DCCRegistryMachinery = DCCRegistryMachinery()


DCCRegistry = _dccregistry



# Generated at 2022-06-14 04:42:38.850559
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(datetime.date(2007,12,28),datetime.date(2008,2,28),datetime.date(2008,2,28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(datetime.date(2007,12,28),datetime.date(2008,2,29),datetime.date(2008,2,29)), 14) == Decimal('0.17216108990194')
    assert round(dcfc_act_act(datetime.date(2007,10,31),datetime.date(2008,11,30),datetime.date(2008,11,30)), 14) == Decimal('1.08243131970956')

# Generated at 2022-06-14 04:42:50.732217
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    import unittest
    import inspect
    import pprint
    

# Generated at 2022-06-14 04:42:52.592314
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    """
    Unit test for function dcfc_30_360_isda
    :return:
    """
    import doctest
    doctest.testmod(verbose=True)

# Generated at 2022-06-14 04:43:04.008233
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:43:15.625055
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2008, 2, 29), datetime.date(2009, 2, 28)
    ex6_start, ex6_asof = datetime.date(2007, 2, 28), dat

# Generated at 2022-06-14 04:43:24.240060
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert round(dcfc_act_365_l(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end= datetime.date(2008, 2, 28)), 14) == Decimal('0.16939890710383')
    assert round(dcfc_act_365_l(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end= datetime.date(2008, 2, 29)), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_l(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end= datetime.date(2008, 11, 30)), 14) == Decimal

# Generated at 2022-06-14 04:43:37.528328
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    assert round(
        dcfc_nl_365(
            start=datetime.date(2007, 12, 28),
            asof=datetime.date(2008, 2, 28),
            end=datetime.date(2008, 2, 28)
        ),
        14
    ) == Decimal('0.16986301369863')
    assert round(
        dcfc_nl_365(
            start=datetime.date(2007, 12, 28),
            asof=datetime.date(2008, 2, 29),
            end=datetime.date(2008, 2, 29)
        ),
        14
    ) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:43:49.626152
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Doing a unit test for the function dcfc_30_360_german
    """

    ex1_start, ex1_asof, ex1_end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 29)
    ex2_start, ex2_asof, ex2_end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 3, 1)
    ex3_start, ex3_asof, ex3_end  = datetime.date(2007, 12, 31), datetime.date(2008, 2, 29), datetime.date(2008, 3, 1)
    ex4_start, ex4_asof, ex4_end  = datetime

# Generated at 2022-06-14 04:43:55.834091
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:44:07.504286
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():

    assert dcfc_30_360_german(datetime.date(2007,12,28), datetime.date(2008,2,28)) == 0.166666666666667
    assert dcfc_30_360_german(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)) == 0.169444444444444
    assert dcfc_30_360_german(datetime.date(2007,10,31), datetime.date(2008,11,30)) == 1.08333333333333
    assert dcfc_30_360_german(datetime.date(2008,2,1), datetime.date(2009,5,31)) == 1.33055555555556
