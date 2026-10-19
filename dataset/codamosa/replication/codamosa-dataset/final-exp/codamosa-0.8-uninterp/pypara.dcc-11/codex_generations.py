

# Generated at 2022-06-14 04:35:00.745548
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    _asof = datetime.date(2015, 2, 17)
    _start = datetime.date(2015, 2, 1)
    _end = datetime.date(2015, 2, 28)
    _freq = None
    _test_data = [
        (datetime.date(2015, 2, 16), ZERO),
        (datetime.date(2015, 2, 17), ONE / Decimal('28'))
    ]
    _dcc = DCC(
        name='Actual/360',
        altnames={'Act/360', 'A/360'},
        currencies={Currencies['AT']},
        calculate_fraction_method=lambda s, a, e, f: Decimal(_get_actual_day_count(s, a) * 360) / Decimal('360')
    )

# Generated at 2022-06-14 04:35:06.047678
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert dcfc_30_e_360(datetime.date(2013, 12, 31), datetime.date(2014, 1, 17), datetime.date(2014, 1, 17)) == 0.0494 
    assert dcfc_30_e_360(datetime.date(2013, 12, 31), datetime.date(2014, 1, 17), datetime.date(2014, 1, 17)) == 0.0494 

# Generated at 2022-06-14 04:35:16.730160
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    """
    Registers a few day count conventions and checks if it does not raise any error.
    """
    ## Create a registry:
    registry = DCCRegistryMachinery()

    ## Register a convention:
    registry.register(
        DCC(
            name="Actual/360",
            altnames={"ACT/360", "Act/360", "Act/Act", "Act", "a/360", "a", "ACT/365_FIXED", "ACT/365F", "ACT/365", "ACT/365F", "ACT/365L", "ACT/365LF"},
            currencies={"USD", "TRY"},
            calculate_fraction_method=_act_act_dcc,
        ))



# Generated at 2022-06-14 04:35:28.720743
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    from datetime import date
    ex1_start, ex1_asof = date(2007, 12, 28), date(2008, 2, 28)
    ex2_start, ex2_asof = date(2007, 12, 28), date(2008, 2, 29)
    ex3_start, ex3_asof = date(2007, 10, 31), date(2008, 11, 30)
    ex4_start, ex4_asof = date(2008, 2, 1), date(2009, 5, 31)
    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:35:37.007869
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert round(dcfc_act_365_l(datetime.date(2017, 2, 1), datetime.date(2017, 2, 28), datetime.date(2017, 2, 28)), 14) == Decimal('0.19178082191781')

    try:
        dcfc_act_365_l(datetime.date(2017, 2, 1), datetime.date(2017, 2, 28), datetime.date(2017, 2, 28), freq=1)
    except TypeError:
        pass
    else:
        assert False



# Generated at 2022-06-14 04:35:43.042948
# Unit test for function dcfc_30_360_german

# Generated at 2022-06-14 04:35:52.839327
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert_equals(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), Decimal('0.16666666666667'))
    assert_equals(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), Decimal('0.16944444444444'))

# Generated at 2022-06-14 04:35:59.761214
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    dcc = DCC("Act/Act ISDA", {"ActAct", "ActActISDA"}, {"TRY"}, calculate)
    DCCRegistry.register(dcc)
    assert DCCRegistry._buffer_main["Act/ActISDA"] == dcc
    assert DCCRegistry._buffer_altn["ActAct"] == dcc
    assert DCCRegistry._buffer_altn["ActActISDA"] == dcc

# Generated at 2022-06-14 04:36:04.586253
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    import unittest

    # Defines the unit tests
    class DCCTestCase(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_default_day_count_fraction_calculation(self):
            # Calculate the default day count fraction
            default_dcf = DCC.default().calculate_fraction(
                start=datetime.date(2017, 1, 1),
                asof=datetime.date(2017, 1, 1),
                end=datetime.date(2017, 1, 2),
            )
            # Check the day count fraction is equal to 1
            self.assertEqual(default_dcf, ONE)


# Generated at 2022-06-14 04:36:15.128636
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCRegistry.ACT_360.calculate_fraction(datetime.date(2017, 1, 29), datetime.date(2017, 5, 1), datetime.date(2017, 5, 1)) == Decimal('0')
    assert DCCRegistry.ACT_360.calculate_fraction(datetime.date(2017, 2, 28), datetime.date(2017, 5, 1), datetime.date(2017, 5, 1)) == Decimal('0.083333333333333333333333333333333333333333333333333333333333')

# Generated at 2022-06-14 04:36:48.881959
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    """
    The test cases for the dcfc_nl_365 function

    :return: None
    """
    # Declare the start and end dates for which we need the day count fraction
    start = datetime.date(2008, 2, 29)
    asof = datetime.date(2008, 4, 28)
    end = datetime.date(2008, 4, 28)

    # Declare the expected and actual day count fraction
    expected = Decimal('0.164383561643836')
    actual = dcfc_nl_365(start, asof, end)

    # Check that the expected and actual day count fraction are the same
    assert actual == expected



# Generated at 2022-06-14 04:36:54.554245
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert dcfc_30_360_german(date(2007, 12, 28), date(2008, 2, 28), date(2008, 2, 28)) == Decimal("0.16666666666667")
    assert dcfc_30_360_german(date(2007, 12, 28), date(2008, 2, 29), date(2008, 2, 29)) == Decimal("0.16944444444444")
    assert dcfc_30_360_german(date(2007, 10, 31), date(2008, 11, 30), date(2008, 11, 30)) == Decimal("1.08333333333333")
    assert dcfc_30_360_german(date(2008, 2, 1), date(2009, 5, 31), date(2009, 5, 31)) == Decimal("1.33055555555556")

# Generated at 2022-06-14 04:37:03.758109
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    start = datetime.date(2017, 1, 1)
    asof = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 1, 1)
    dcc = DCC("0", {'0', '3'}, set(), lambda start, asof, end, freq: ZERO)
    assert dcc.calculate_daily_fraction(start, asof, end) == 0

    asof = datetime.date(2017, 1, 2)
    dcc = DCC("0", {'0', '3'}, set(), lambda start, asof, end, freq: ZERO)
    assert dcc.calculate_daily_fraction(start, asof, end) == 0

    asof = datetime.date(2017, 12, 31)
    dcc = D

# Generated at 2022-06-14 04:37:15.672248
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Tests the function dcfc_30_360_us
    """
    ## Ex: 1
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    assert round(dcfc_30_360_us(start=start, asof=asof, end=asof), 14) == 0.166666666666667

    ## Ex: 2
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    assert round(dcfc_30_360_us(start=start, asof=asof, end=asof), 14) == 0.169444444444444

    ## Ex: 3

# Generated at 2022-06-14 04:37:28.278037
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_us(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_us(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:37:32.449213
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194')

# Generated at 2022-06-14 04:37:46.534248
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    # dcfc_30_e_360 test
    assert round(dcfc_30_e_360(start=datetime.date(2017, 12, 29), asof=datetime.date(2018, 12, 31), end=datetime.date(2018, 12, 31)), 14) == Decimal('1.0')
    assert round(dcfc_30_e_360(start=datetime.date(2017, 12, 29), asof=datetime.date(2018, 12, 30), end=datetime.date(2018, 12, 30)), 14) == Decimal('0.99444444444444')

# Generated at 2022-06-14 04:37:56.972864
# Unit test for method interest of class DCC
def test_DCC_interest():
    principal = Money(1, 'USD')
    rate = 1
    start = datetime.date(2020, 1, 1)
    asof = datetime.date(2020, 2, 1)
    freq = 1
    end = datetime.date(2020, 3, 1)
    moneyInterest = Money(0.08333333333333333, 'USD')
    assert DCCRegistry.Actual360.interest(principal, rate, start, asof, end, freq) == moneyInterest
    assert DCCRegistry.Actual360.interest(principal, rate, start, asof, end) == moneyInterest
    assert DCCRegistry.Actual365Fixed.interest(principal, rate, start, asof, end, freq) == moneyInterest

# Generated at 2022-06-14 04:38:05.241919
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    """Test function dcfc_30_e_360
    """
    DCF = dcfc_30_e_360(start=datetime.date(2008, 2, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29))
    assert DCF == Decimal('0.16944444444444')

## The following day count conventions are based on the actual number of days, but with a fixed denominator:

# Generated at 2022-06-14 04:38:17.487782
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(datetime.date(2020, 9, 20), datetime.date(2020, 10, 20)), 14) == Decimal('1')
    assert round(dcfc_30_e_360(datetime.date(2020, 9, 20), datetime.date(2020, 10, 21)), 14) == Decimal('1.02777777777778')
    assert round(dcfc_30_e_360(datetime.date(2020, 9, 20), datetime.date(2020, 12, 20)), 14) == Decimal('1.36666666666667')
    assert round(dcfc_30_e_360(datetime.date(2020, 9, 20), datetime.date(2020, 12, 21)), 14) == Decimal('1.39444444444444')

# Generated at 2022-06-14 04:43:03.831929
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(start = datetime.date(2007, 12, 28), asof = datetime.date(2008, 2, 28), end = datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(start = datetime.date(2007, 12, 28), asof = datetime.date(2008, 2, 29), end = datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:43:09.441444
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert dcfc_act_365_l(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == Decimal('0.16939890710383')
    assert dcfc_act_365_l(datetime.date(2008, 2, 1), datetime.date(2009, 5, 31), datetime.date(2009, 5, 31)) == Decimal('1.32876712328767')



# Generated at 2022-06-14 04:43:19.508256
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:43:31.800966
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    print("Testing dcfc_30_e_360...", end="")
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:43:37.344657
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    r1 = round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)

# Generated at 2022-06-14 04:43:49.396979
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:43:55.651807
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():

    for (year, month, day) in [
            (2005,1,30),
            (2005,2,28),
            (2005,2,1),
            (2005,2,2),
            (2005,3,30),
            (2005,3,31),
            (2005,3,1),
            (2005,3,2),
            (2005,4,30),
            (2005,4,1),
            (2005,5,31),
            (2005,6,30),
            (2005,7,31),
            (2005,8,31),
            (2005,9,30),
            (2005,10,31),
            (2005,11,30),
            (2005,12,30) ]:

        start = datetime.date(year, month, day)


# Generated at 2022-06-14 04:44:03.535079
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert_almost_equal(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 0.16942884946478, 14)
    assert_almost_equal(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 0.17216108990194, 14)
    assert_almost_equal(dcfc_act_act(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 1.08243131970956, 14)

# Generated at 2022-06-14 04:44:12.749466
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    """
    Unit test for dcfc_30_360_isda().
    """
    # ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    # ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    # ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    # ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:44:15.481328
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    # TODO: Write unit tests for dcfc_30_e_plus_360
    assert None

