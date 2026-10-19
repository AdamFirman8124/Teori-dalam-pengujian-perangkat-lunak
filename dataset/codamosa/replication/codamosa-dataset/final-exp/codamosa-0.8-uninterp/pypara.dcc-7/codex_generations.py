

# Generated at 2022-06-14 04:35:12.028421
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_nl_365(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == round(Decimal('0.16986301369863'), 14)

# Generated at 2022-06-14 04:35:17.062759
# Unit test for method interest of class DCC
def test_DCC_interest():
    start = datetime.date(2014, 5, 1)
    asof = datetime.date(2014, 5, 30)
    end = datetime.date(2014, 7, 31)
    principal = Money(100, "USD")
    rate = Decimal(0.05)
    assert principal * rate * Decimal(".5") == DCC._30E360.interest(principal, rate, start, asof, end)


# Generated at 2022-06-14 04:35:29.114339
# Unit test for method find of class DCCRegistryMachinery
def test_DCCRegistryMachinery_find():
    ## Tests for the find method of DCCRegistryMachinery.
    ### We first register a simple dcc and find it:
    dcc1 = DCC("dcc1", [], set(), lambda s, a, e, f: 0, )
    dcc2 = DCC("dcc2", [], set(), lambda s, a, e, f: 0, )
    dcc3 = DCC("dcc3", [], set(), lambda s, a, e, f: 0, )

    ## Create a registry and register the dcc:
    registry = DCCRegistryMachinery()
    registry.register(dcc1)

    ### We can find it:
    assert registry.find("dcc1") is dcc1

    ### We can not find it by the alternative name:
    assert registry.find("dcc2") is None



# Generated at 2022-06-14 04:35:36.685213
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    ## Import needed class and methods.
    ## We are using the 30/360 specific code, but the 30/360 is
    ## already included in this module so we will use a stand-in.
    from .testing import dummy_dcc_30_360

    ## Define the principal and rates.
    principal = Money(10000, "USD")
    rate = Decimal(0.04)

    ## Define the dates for the test.
    start = datetime.datetime(2014, 1, 1).date()
    end = datetime.datetime(2014, 7, 1).date()

    ## Define the different dates used to calculate the daily interest

# Generated at 2022-06-14 04:35:49.416415
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    test_cases = (
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), 0.16986301369863),
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), 0.17213114754098),
        (datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), 1.08196721311475),
        (datetime.date(2008, 2, 1), datetime.date(2009, 5, 31), 1.32513661202186),
    )
    for case in test_cases:
        assert round(dcfc_act_365_a(start=case[0], asof=case[1], end=case[1]), 14) == case[2]
    return True

# Generated at 2022-06-14 04:36:03.449469
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    # Test 1:
    assert round(dcfc_30_360_us(start=datetime.date(2019, 1, 31), asof=datetime.date(2019, 2, 28), end=datetime.date(2019, 2, 28)), 14) == Decimal('0.083333333333333')
    # Test 2:
    assert round(dcfc_30_360_us(start=datetime.date(2019, 1, 31), asof=datetime.date(2019, 2, 28), end=datetime.date(2019, 2, 28)), 14) == Decimal('0.083333333333333')
    # Test 3:

# Generated at 2022-06-14 04:36:06.946320
# Unit test for method find of class DCCRegistryMachinery
def test_DCCRegistryMachinery_find():
    assert DCCRegistry.find("Act/Act") is not None



# Generated at 2022-06-14 04:36:20.604967
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    if dcfc_act_365_a(datetime.date(2020, 2, 1), datetime.date(2020, 3, 1), datetime.date(2020, 4, 1)) != 1 / 31:
        raise Exception("Unit test for function dcfc_act_365_a failed.")
    if dcfc_act_365_a(datetime.date(2020, 1, 1), datetime.date(2020, 3, 1), datetime.date(2020, 4, 1)) != 1 / 32:
        raise Exception("Unit test for function dcfc_act_365_a failed.")

# Generated at 2022-06-14 04:36:32.648607
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    #: Defines the name of the day count convention.
    name: str

    #: Defines a set of alternative names of the day count convention.
    altnames: Set[str]

    #: Defines a set of currencies which are known to use this convention by default.
    currencies: Set[Currency]

    #: Defines the day count fraction calculation method function.
    calculate_fraction_method: Callable[[Date, Date, Date, Optional[Decimal]], Decimal]
    principal = Money(10000, 'USD')
    rate = Decimal(0.02)
    start = Date(2019,1,1)
    asof = Date(2019,1,10)
    end = None
    freq = None
    start = datetime.date(2019, 1, 1)

# Generated at 2022-06-14 04:36:40.340615
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    # Test case 1:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    assert round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

    # Test case 2:
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    assert round(dcfc_30_360_isda(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')

    # Test case 3:


# Generated at 2022-06-14 04:37:00.830337
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 9, 10), end=datetime.date(2020, 3, 2)), 10) == Decimal('0.5245901639')
    assert round(dcfc_act_act_icma(start=datetime.date(2016, 3, 2), asof=datetime.date(2016, 9, 10), end=datetime.date(2017, 3, 2)), 10) == Decimal('0.5227272727')

# Generated at 2022-06-14 04:37:14.120679
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    import datetime

    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2007, 2, 28), datetime.date(2008, 2, 28)


# Generated at 2022-06-14 04:37:18.269857
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert dcfc_30_360_german(Date(1999,12,31), Date(2000,1,15), Date(2000,1,15)) == Decimal(0)
    assert dcfc_30_360_german(Date(2000,1,15), Date(2000,2,15), Date(2000,2,15)) == Decimal("0.083333333333333")
    assert dcfc_30_360_german(Date(2000,2,15), Date(2000,3,15), Date(2000,3,15)) == Decimal("0.083333333333333")
    assert dcfc_30_360_german(Date(2000,3,15), Date(2000,4,15), Date(2000,4,15)) == Decimal("0.1")
    assert dcfc_30_360

# Generated at 2022-06-14 04:37:22.004457
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCC.calculate_daily_fraction(datetime.date(2014,3,3),datetime.date(2014,3,3),datetime.date(2014,3,7))==0



# Generated at 2022-06-14 04:37:26.897845
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert round(dcfc_30_360_german(datetime.date(2013, 4, 30), datetime.date(2013, 7, 31), datetime.date(2013, 7, 31)), 14) == 0.25  # Actual/Actual, ISDA (2013)
    assert round(dcfc_30_360_german(datetime.date(2013, 4, 30), datetime.date(2013, 5, 31), datetime.date(2013, 7, 31)), 14) == 0.0833  # Actual/Actual, ISDA (2013)
    assert round(dcfc_30_360_german(datetime.date(2013, 7, 31), datetime.date(2013, 8, 30), datetime.date(2013, 10, 31)), 14) == 0.0833  # Actual/Actual, ISDA

# Generated at 2022-06-14 04:37:37.310269
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    for i in range(100):
        start = random_date()
        asof = random_date(start)
        end = random_date(asof)
        if i % 3 == 0:
            assert dcfc_act_365_a(start, asof, end) == dcfc_act_365_f(start, asof, end)
        else:
            assert dcfc_act_365_a(start, asof, end) <= dcfc_act_365_f(start, asof, end)


# Generated at 2022-06-14 04:37:40.894437
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    assert round(dcfc_act_365_a(start=datetime.date(2019, 1, 8), asof=datetime.date(2021, 1, 8), end=datetime.date(2021, 1, 8)), 6) == 0.874186

# Generated at 2022-06-14 04:37:45.224444
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    assert dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end) == 0.52459016393442621



# Generated at 2022-06-14 04:37:52.132334
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(start=datetime.date(2018, 2, 28),asof=datetime.date(2018, 10, 12),end=datetime.date(2018, 10, 12)),14) == Decimal('0.19722222222222'), "test_dcfc_30_e_360: test 1 failed"



# Generated at 2022-06-14 04:38:05.985798
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:38:29.983757
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    """
    Test case for function dcfc_act_act_icma
    """
    test_var_start_date = datetime.date(2019, 3, 2)
    test_var_asof_date = datetime.date(2019, 9, 10)
    test_var_end_date = datetime.date(2020, 3, 2)
    print(round(dcfc_act_act_icma(start=test_var_start_date, asof=test_var_asof_date, end=test_var_end_date), 10))



# Generated at 2022-06-14 04:38:38.879212
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14) == 0.16942884946478
    assert round(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14) == 0.17216108990194
    assert round(dcfc_act_act(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14) == 1.08243131970956

# Generated at 2022-06-14 04:38:48.168655
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    dcc = DCC(
        name="ACT/360",
        altnames={"A360", "ACT360", "ACT/360"},
        currencies=_as_ccys({"CHF", "EUR", "GBP", "HKD", "USD"}),
        calculate_fraction_method=_ACT360_method,
    )
    principal = Money(100, Currencies.USD)
    asof = datetime.date(2017, 2, 17)
    freq = Decimal(1)
    coupon = dcc.coupon(principal, Decimal(0.01), datetime.date(2017, 1, 15), asof, datetime.date(2017, 1, 15), freq)
    assert coupon.amount == Decimal(0.05) and coupon.ccy == Currencies.USD



# Generated at 2022-06-14 04:39:00.149679
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    from .currencies import Currencies
    assert DCC("BDA", {"BDA"}, {"TRY"} , _actual_actual_icma_fraction_method).calculate_fraction(datetime.date(2014, 10, 10), datetime.date(2014, 12, 31), datetime.date(2015, 12, 31), None) == Decimal("0.25")
    assert DCC("ACT360", {"ACT360"}, {"EUR"} , _actual_360_fraction_method).calculate_fraction(datetime.date(2010, 12, 31), datetime.date(2010, 12, 31), datetime.date(2011, 12, 31), None) == Decimal("0")

# Generated at 2022-06-14 04:39:13.011106
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    asof = datetime.date(2020, 4, 23)
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:39:23.965509
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    print("\n")
    print("---start test_DCC_calculate_daily_fraction---")

    day_count_fraction = DCC("test", set(), set(), lambda start, asof, end,freq: asof - start)
    if day_count_fraction.calculate_daily_fraction(start=datetime.date(2018,1,1),asof=datetime.date(2018,1,1),end=datetime.date(2018,1,1)) != 0:
        print("test_DCC_calculate_daily_fraction failed")


# Generated at 2022-06-14 04:39:30.078500
# Unit test for method interest of class DCC
def test_DCC_interest():
    instance = DCC('name', set('altnames'), _as_ccys(set('currencies')), calculate_fraction_method)
    instance.interest(principal='Money', rate='Decimal', start='Date', asof='Date', end='Optional[Date]', freq='Optional[Decimal]')

# Generated at 2022-06-14 04:39:39.585066
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    from dateutil.relativedelta import relativedelta
    from .monetary import Money
    from .currencies import Currencies
    bd = datetime.date(2016,8,15)
    ed = datetime.date(2017,2,15)
    principal = Money(100,Currencies.USD)
    rate = Decimal(0.01)
    start = datetime.date(2017, 1, 1)
    asof = datetime.date(2017, 5, 4)
    assert DCC.ACT_ICMA.calculate_daily_fraction(bd,asof,ed,1) == Decimal('0.006849315')
    assert DCC.BND_30_360.calculate_daily_fraction(bd,asof,ed,1) == Decimal('0.006849315')


# Generated at 2022-06-14 04:39:52.653312
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    """
    Unit test for function dcfc_30_360_isda
    """
    ex1_start, ex1_asof, ex1_end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof, ex2_end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof, ex3_end = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)

# Generated at 2022-06-14 04:40:01.957169
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    """
    Function dcfc_30_360_isda unit test implementation.
    """
    # Define specific unit test data sets:
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    end = asof
    assert round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14) == Decimal('0.16666666666667')
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    end = asof
    assert round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14) == Decimal('0.16944444444444')
    start, asof = dat

# Generated at 2022-06-14 04:41:41.547150
# Unit test for method find of class DCCRegistryMachinery

# Generated at 2022-06-14 04:41:46.592326
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert round(dcfc_act_365_l(datetime.date(2018, 12, 28), datetime.date(2019, 2, 28), datetime.date(2019, 2, 28)), 14) == Decimal('0.16939890710383')
    assert round(dcfc_act_365_l(datetime.date(2018, 12, 28), datetime.date(2019, 2, 29), datetime.date(2019, 2, 29)), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_l(datetime.date(2018, 12, 28), datetime.date(2019, 10, 31), datetime.date(2020, 11, 30)), 14) == Decimal('1.08196721311475')

# Generated at 2022-06-14 04:41:58.909776
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof) == 0.1666666666666666666666666667

# Generated at 2022-06-14 04:42:06.760271
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """Test the function dcfc_30_360_us"""
    assert round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:42:12.265548
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    if IS_TEST_EXECUTION:
        # Exhibit 1:
        ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
        # Exhibit 2:
        ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
        # Exhibit 3:
        ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
        # Exhibit 4:
        ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
        # Check:

# Generated at 2022-06-14 04:42:21.488239
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert (
        round(
            dcfc_30_360_isda(start=datetime.date(year=2007, month=12, day=28), asof=datetime.date(
                year=2008, month=2, day=28), end=datetime.date(year=2008, month=2, day=28)), 14) ==
        round(Decimal("0.16666666666667"), 14)
    )

# Generated at 2022-06-14 04:42:31.042942
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    convention = DCC("Convention", {'Conv'}, {Currencies.USD}, _DCC_M30_E360_ISDA)
    assert convention.calculate_daily_fraction(datetime.date(2015, 1, 1), datetime.date(2015, 1, 1), datetime.date(2015, 1, 2), None) == 0
    assert convention.calculate_daily_fraction(datetime.date(2015, 1, 1), datetime.date(2015, 1, 2), datetime.date(2015, 1, 2), None) == 1
    assert convention.calculate_daily_fraction(datetime.date(2015, 1, 1), datetime.date(2015, 1, 3), datetime.date(2015, 1, 3), None) == 1


# Generated at 2022-06-14 04:42:41.598414
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert dcc_helper.check_against_case_insensitive_value(dcfc_30_e_360, "30E/360", True), "case insensitive"
    assert dcc_helper.check_against_case_insensitive_value(dcfc_30_e_360, "30/360 European", True), "case insensitive"
    assert dcc_helper.check_against_case_insensitive_value(dcfc_30_e_360, "30/360 ISMA", True), "case insensitive"
    assert dcc_helper.check_against_case_insensitive_value(dcfc_30_e_360, "30S/360 Special German", True), "case insensitive"

    ## Case 1:

# Generated at 2022-06-14 04:42:48.896885
# Unit test for method find of class DCCRegistryMachinery

# Generated at 2022-06-14 04:42:52.895318
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    # For some reason - doctest is not working for this function..