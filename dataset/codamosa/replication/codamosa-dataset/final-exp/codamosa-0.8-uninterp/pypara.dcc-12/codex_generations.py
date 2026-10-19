

# Generated at 2022-06-14 04:35:09.492422
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCs.ACT_ACT_ICMA.calculate_fraction(datetime.date(2016, 1, 1), datetime.date(2016, 2, 1), datetime.date(2016, 3, 1)) is not None


# Generated at 2022-06-14 04:35:11.442803
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():

    assert DCC.calculate_fraction(start, asof, end, freq) == principal * rate * self.calculate_fraction(start, asof, end, freq)


# Generated at 2022-06-14 04:35:18.689658
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Tests for function "dcfc_30_360_us".
    """
    print("Testing dcfc_30_360_us.")

    ## Simply check the formulae:
    days  = [datetime.date(2017,5,5), datetime.date(2017,5,1), datetime.date(2017,5,31), datetime.date(2017,7,31), datetime.date(2017,4,28), datetime.date(2017,4,30), datetime.date(2017,2,28), datetime.date(2017,2,30)]

# Generated at 2022-06-14 04:35:30.880586
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    '''
    Test dcfc_act_365_l function
    '''
    start_date = datetime.datetime(2020,1,1,0,0,0)
    end_date = datetime.datetime(2020,3,1,0,0,0)
    start_date2 = datetime.datetime(2020,1,1,0,0,0)
    end_date2 = datetime.datetime(2020,3,2,0,0,0)
    start_date3 = datetime.datetime(2020,1,1,0,0,0)
    end_date3 = datetime.datetime(2020,12,31,0,0,0)
    start_date4 = datetime.datetime(2020,1,1,0,0,0)
    end_date4

# Generated at 2022-06-14 04:35:37.316525
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    ## Get 30/360 dc:
    dc = _30360_dc

    ## Create some dates and check the daily fractions:
    assert dc.calculate_daily_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 2), datetime.date(2017, 1, 31)) == ONE / 30
    assert dc.calculate_daily_fraction(datetime.date(2017, 1, 2), datetime.date(2017, 1, 3), datetime.date(2017, 1, 31)) == ONE / 30
    assert dc.calculate_daily_fraction(datetime.date(2017, 1, 3), datetime.date(2017, 1, 4), datetime.date(2017, 1, 31)) == ONE / 30

# Generated at 2022-06-14 04:35:49.775851
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:36:03.504680
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Unit test for function dcfc_30_360_us.
    """
    assert dcfc_30_360_us(datetime.date(2017, 1, 1), datetime.date(2017, 2, 1), datetime.date(2017, 2, 1)) == Decimal('0.083333333333333')
    assert dcfc_30_360_us(datetime.date(2017, 1, 1), datetime.date(2017, 1, 31), datetime.date(2017, 1, 31)) == Decimal('0.083333333333333')
    assert dcfc_30_360_us(datetime.date(2013, 1, 31), datetime.date(2013, 2, 28), datetime.date(2013, 2, 28)) == Decimal('0.083333333333333')
    assert d

# Generated at 2022-06-14 04:36:15.099823
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    from .currencies import Currencies

    eur = Currencies["EUR"]
    aud = Currencies["AUD"]

    DCCRegistry.register(
        DCC(
            "ACT/365",
            {
                "A/365",
                "A365",
                "Actual/365",
                "Actual365",
                "ACT/365 Fixed",
                "ACT/365 (Fixed)",
                "ACT/365F",
                "ACT/365 (F)",
                "ACT/365 (NL)",
                "NL/365",
                "NL365",
            },
            {eur, aud},
            lambda start, asof, end, freq: _get_actual_day_count(start, asof) / Decimal(365)
        )
    )

    dcc = DCCRegistry["ACT/365"]

# Generated at 2022-06-14 04:36:19.090228
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    print("\ndcfc_act_365_a")
    assert round(dcfc_act_365_a(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14) == Decimal('1.08196721311475')
    assert round(dcfc_act_365_a(datetime.date(2008, 2, 1), datetime.date(2009, 5, 31), datetime.date(2009, 5, 31)), 14) == Decimal('1.32513661202186')


# Generated at 2022-06-14 04:36:27.639033
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    print("\n----- Testing dcfc_30_360_german")

    ## Ex 1:
    ex1_start, ex1_asof, ex1_end = datetime.date(2008, 1, 30), datetime.date(2008, 7, 31), datetime.date(2008, 7, 31)
    print("{:12s} :  {:15s} - {:15s} = {:12.14f}".format("30/360 German", ex1_asof, ex1_start, dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_end)))

# Generated at 2022-06-14 04:37:02.873536
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(datetime.date(2019, 4, 5), datetime.date(2019, 10, 14), datetime.date(2019, 12, 16)), 12) == Decimal('0.6338028169')
    assert round(dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)), 25) == Decimal('0.5245901639344262295081967')
    assert round(dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 3, 2), datetime.date(2020, 3, 2)), 14) == Decimal('0')

# Generated at 2022-06-14 04:37:15.483905
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:37:28.786957
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    from .monetary import Money
    from . import DCC

    dcc = DCC['ACT365F']
    start_date = Date(2016,1,1)
    asof_date = Date(2016,1,15)
    end_date = Date(2016,1,31)
    frequency = ONE

    assert dcc.calculate_fraction(start_date, asof_date, end_date, frequency) == Decimal('0.487671232876712')
    assert dcc.calculate_fraction(start_date, asof_date, end_date, ZERO) == Decimal('0.487671232876712')
    assert dcc.calculate_fraction(start_date, asof_date, end_date, None) == Decimal('0.487671232876712')



# Generated at 2022-06-14 04:37:37.083010
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    print('Testing function dcfc_30_360_isda...', end='')
    # The following tests ensure that dcfc_30_360_isda() produces the right output.
    # print(dcfc_30_360_isda(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)))
    # 0.16666666666667
    assert(abs(dcfc_30_360_isda(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) - Decimal('0.16666666666667')) < 1e-10)
    # print(dcfc_30_360_isda(datetime.date(2007, 12, 28), dat

# Generated at 2022-06-14 04:37:44.792961
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    """
    Unit test for function dcfc_act_365_a.
    
    NOTE:
    - This test passes.
    """
    ## Test case 1:
    # ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    # ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    # ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    # ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    # round(dcfc_act_365_a

# Generated at 2022-06-14 04:37:51.271092
# Unit test for method interest of class DCC
def test_DCC_interest():
    assertDCC = DCC('TestDCC', 'TestDCC', 'TestDCC', 1, 1)
    principal = Money('RUB', 1)
    rate = 2
    start = '2017-01-01'
    asof = '2017-01-01'
    end = '2017-01-01'
    freq = 1
    assert assertDCC.interest(principal, rate, start, asof, end, freq) == 1

# Generated at 2022-06-14 04:38:01.291797
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert round(dcfc_30_360_german(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_german(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_german(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:38:10.709270
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    """
    Unit test for method calculate_fraction of class DCC
    """
    start_date = Date(2018, 1, 1)
    asof_date = Date(2018, 1, 1)
    end_date = Date(2018, 1, 1)

    # when freq is None
    assert DCCRegistry["ACT/365"].calculate_fraction(start_date, asof_date, end_date) == 0.0
    assert DCCRegistry["ACT/360"].calculate_fraction(start_date, asof_date, end_date) == 0.0
    assert DCCRegistry["ACT/365.25"].calculate_fraction(start_date, asof_date, end_date) == 0.0
    assert DCCRegistry["ACT/ACT"].calculate

# Generated at 2022-06-14 04:38:22.913229
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    # Get the start, asof and end dates:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    # Test each example:
    assert dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof) == Dec

# Generated at 2022-06-14 04:38:33.908514
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCCRegistry["ACT/ACT"].calculate_daily_fraction(
            datetime.date(2017, 2, 1), datetime.date(2017, 3, 2), datetime.date(2018, 1, 31)) == Decimal("29.91509434")
    assert DCCRegistry["ACT/ACT"].calculate_daily_fraction(
            datetime.date(2017, 2, 1), datetime.date(2017, 3, 2), datetime.date(2018, 1, 31), Decimal("1")) == Decimal("29.91509434")

# Generated at 2022-06-14 04:39:29.255456
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    test = dcc("Act/Act", {"Actual/Actual", "Actual/Actual (ISDA)"})
    return test

# Generated at 2022-06-14 04:39:38.585213
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    print("Testing function dcfc_30_360_isda...", end="")

    # Tests are sorted by date

# Generated at 2022-06-14 04:39:52.068151
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(start=datetime.date(2007,12,28), asof=datetime.date(2008,2,28), end=datetime.date(2008,2,28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_isda(start=datetime.date(2007,12,28), asof=datetime.date(2008,2,29), end=datetime.date(2008,2,29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_isda(start=datetime.date(2007,10,31), asof=datetime.date(2008,11,30), end=datetime.date(2008,11,30)), 14) == Dec

# Generated at 2022-06-14 04:39:59.897143
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    """
    Unit test for method calculate_daily_fraction of class DCC
    This function tests that the function returns the correct daily fraction and that it raises an error when the user provides incorrect input.
    """
    from .currencies import Currencies
    from .monetary import Money
    from .tenors import Tenor
    usd = Currencies['USD']

    # The initial dates for which we want to calculate the daily fraction
    dcc2_start = datetime.date(2015, 1, 1)
    dcc2_asof = datetime.date(2015, 1, 2)
    dcc2_end = datetime.date(2015, 4, 30)
    dcc30_start = datetime.date(2015, 1, 1)
    dcc30_asof = datetime.date(2015, 1, 2)
    dcc

# Generated at 2022-06-14 04:40:08.495561
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_nl_365(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:40:21.573725
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    import unittest
    import unittest.mock

    from .currencies import USD
    from .monetary import Money

    ## Define the testing method:

# Generated at 2022-06-14 04:40:30.968376
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    
    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == round(Decimal('0.16666666666667'), 14)

# Generated at 2022-06-14 04:40:43.058892
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    """
    Tests the implementation of method calculate_daily_fraction of class DCC
    """
    try:
        test = DCC(
            name="test",
            altnames={"test1","test2"},
            currencies=_as_ccys({"USD","EUR"}),
            calculate_fraction_method=lambda x,y,z: Decimal(1))
        test.calculate_daily_fraction(
            datetime.date(2000,1,1),
            datetime.date(2000,1,3),
            datetime.date(2000,1,4))
    except Exception:
        print("error: test_DCC_calculate_daily_fraction")

# Generated at 2022-06-14 04:40:50.118782
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14)==Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14)==Decimal('0.16944444444444')

# Generated at 2022-06-14 04:41:01.588170
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    # Test data:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    # Function under test:

# Generated at 2022-06-14 04:42:07.410673
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCCRegistry["ACT/365L"].calculate_daily_fraction(datetime.date(2016, 4, 1), datetime.date(2016, 4, 6), datetime.date(2016, 10, 3)) == Decimal("0.0163")


# Generated at 2022-06-14 04:42:12.666099
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ## Test1:
    ex1_start, ex1_end, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)
    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

    ## Test2:
    ex2_start, ex2_end, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)

# Generated at 2022-06-14 04:42:24.281975
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:42:37.127551
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert dcfc_30_360_isda(datetime.date(2006,1,1), datetime.date(2006,2,1), datetime.date(2006,3,1)) == Decimal('0.08333333333333')
    assert dcfc_30_360_isda(datetime.date(2006,1,1), datetime.date(2006,2,1), datetime.date(2006,3,2)) == Decimal('0.08611111111111')
    assert dcfc_30_360_isda(datetime.date(2005,1,31), datetime.date(2005,5,31), datetime.date(2005,6,30)) == Decimal('0.16111111111111')

# Generated at 2022-06-14 04:42:49.699192
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)

# Generated at 2022-06-14 04:43:00.256805
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    expected = Decimal('0.5245901639')
    assert round(dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end), 10)==expected


# Generated at 2022-06-14 04:43:10.569864
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    The unit test for dcfc_30_360_german.
    """
    assert round(dcfc_30_360_german(datetime.date(2008, 1, 31), datetime.date(2008, 4, 1)), 14) == round(Decimal("0.083333333333333"), 14)
    assert round(dcfc_30_360_german(datetime.date(2008, 10, 31), datetime.date(2008, 11, 30)), 14) == round(Decimal("0.083333333333333"), 14)
    assert round(dcfc_30_360_german(datetime.date(2008, 1, 31), datetime.date(2008, 2, 29)), 14) == round(Decimal("0.077777777777778"), 14)

# Generated at 2022-06-14 04:43:20.455755
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
  assert dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) == 0.166666666666667
  assert dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)) == 0.1694444444444444
  assert dcfc_30_e_360(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)) == 1.083333333333333

# Generated at 2022-06-14 04:43:27.891060
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    start = datetime.date(2017, 1, 1)
    asof = datetime.date(2017, 1, 1)
    end = datetime.date(2017, 1, 2)

    dcc_30_360 = DCC('30/360', {'30-360'}, {Currencies['USD']}, calculate_fraction_30_360)
    assert dcc_30_360.calculate_daily_fraction(start, asof, end) == Decimal('0.0')

    asof = datetime.date(2017, 1, 2)
    assert dcc_30_360.calculate_daily_fraction(start, asof, end) == Decimal('0.0027777777777778')


# Generated at 2022-06-14 04:43:39.841456
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Unit test for function dcfc_30_360_us.
    """
    ####################################################################################################################
    ##                                                                                                                ##
    ##                                    EXECUTE UNIT TESTS FOR FUNCTION dcfc_30_360_us                              ##
    ##                                                                                                                ##
    ####################################################################################################################
    ## Example from http://en.wikipedia.org/wiki/Day_count_convention:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)