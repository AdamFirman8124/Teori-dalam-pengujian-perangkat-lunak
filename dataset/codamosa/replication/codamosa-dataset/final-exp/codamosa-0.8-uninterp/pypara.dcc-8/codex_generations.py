

# Generated at 2022-06-14 04:35:09.431832
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    assert DCC.__dict__['coupon'].__doc__ == '''
        Calculates the accrued interest for the coupon payment.

        This method is primarily used for bond coupon accruals which assumes the start date to be the first of regular
        payment schedules.
    '''
    assert DCC('Act/Act AFB', set(), set(),
               DCFC(lambda : 0)).coupon(Money(0, Currencies['USD']), 0,
                                        datetime.date(2014, 1, 1), datetime.date(2014, 1, 1)) == Money(0, Currencies['USD'])

# Generated at 2022-06-14 04:35:18.220058
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    """
    Unit test for method coupon of class DCC
    """

# Generated at 2022-06-14 04:35:27.964586
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    """
    Unit test for method coupon of class DCC
    """
    dcc = DCC('30/360', '30/360', {}, None)
    m = Money(100, Currencies.USD)
    r = Decimal(0.005)
    start = Date(2017, 1, 1)
    asof = Date(2017, 5, 10)
    end = Date(2017, 7, 1)
    freq = Decimal(2)
    assert abs(dcc.coupon(m, r, start, asof, end, freq) - Money(0.0833, Currencies.USD)) < ONE



# Generated at 2022-06-14 04:35:36.210139
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    # create dummy object 
    dummy_object = DCC(
            name='name', altnames=set(), currencies=set(), calculate_fraction_method=lambda x, y, z, freq: Decimal(x),
        )
    # define start, asof, end and freq as datetime objects
    start = datetime.date(2014, 4, 1)
    asof = datetime.date(2014, 5, 31)
    end = datetime.date(2014, 5, 31)
    freq = Decimal(3)
    # define dummy rate
    rate = Decimal(3)

    test_answer = dummy_object.calculate_daily_fraction(start, asof, end, freq)

    correct_answer = Decimal(1) / Decimal(191)

# Generated at 2022-06-14 04:35:46.915239
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    assert(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof)==.1666666666666666666666666666666666)

# Generated at 2022-06-14 04:35:54.157706
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)
    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)
    assert dcfc_act_act(ex1_start, ex1_asof, ex1_asof) == Decimal('0.16942884946478')

# Generated at 2022-06-14 04:36:04.942275
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """Tests all examples from http://www.isda.org/c_and_a/docs/30-360.pdf"""
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:36:18.141015
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert type(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof)) is Decimal

# Generated at 2022-06-14 04:36:30.858116
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert round(dcfc_act_365_l(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == round(Decimal('0.16939890710383'),14)
   

# Generated at 2022-06-14 04:36:33.831536
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    _equal(dcfc_30_360_german, get_test_data("30_360_german.json"))



# Generated at 2022-06-14 04:36:49.881640
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    """
    Test function dcfc_30_360_isda
    """
    start = datetime.date(2007, 12, 28)
    asof = datetime.date(2008, 2, 28)
    end = datetime.date(2008, 2, 28)
    assert round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14) == Decimal('0.16666666666667')
    start = datetime.date(2007, 12, 28)
    asof = datetime.date(2008, 2, 29)
    end = datetime.date(2008, 2, 29)
    assert round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:36:55.427057
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    print("Calculate the day count fraction based on the underlying methodology after performing some general checks.")
    dcc = DCC("name" ,{'altnames'} ,{'currencies'}, calculate_fraction_method)
    principal = Money(1, 'USD')
    rate = Decimal(2)
    start = datetime.date(2017 ,4 ,4)
    asof = datetime.date(2017 ,4 ,4)
    end = datetime.date(2017 ,4 ,4)
    freq = Decimal(2)
    print(dcc.calculate_fraction(start, asof, end, freq))
    start = datetime.date(2017 ,4 ,4)
    asof = datetime.date(2017 ,4 ,4)
    end = datetime.date(2017 ,4 ,4)


# Generated at 2022-06-14 04:37:07.298838
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():    
    """
    Unit test for method calculate_fraction of class DCC.
    """
    # Import needed packages
    import datetime
    import unittest
    
    # Import needed modules
    from kcrv.curves import AFRCurve
    from kcrv.curves.calibration import calibration_values
    from kcrv.curves.exchange.models import NewZealand
    from kcrv.definitions import DCC
    
    # Define curve data set and calibration values
    data_set = NewZealand.NZRCurve
    calibration_data = calibration_values(data_set)
    
    # Define curve
    curve = AFRCurve(data_set, calibration_data)
    
    # Define dates
    start = datetime.date(2015, 2, 20)


# Generated at 2022-06-14 04:37:17.331943
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    """ Unit test for function dcfc_30_360_isda """

    ## Test data:
    test_dates = [
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), Decimal('0.16666666666667')),
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), Decimal('0.16944444444444')),
        (datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), Decimal('1.08333333333333')),
        (datetime.date(2008, 2, 1), datetime.date(2009, 5, 31), Decimal('1.33333333333333')),
    ]

    ## Test data:
    for date_pair in test_dates:
        start

# Generated at 2022-06-14 04:37:23.738925
# Unit test for function dcfc_30_360_isda

# Generated at 2022-06-14 04:37:29.192617
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    # Example 1
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    # Example 2
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    # Example 3

# Generated at 2022-06-14 04:37:40.380281
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert(round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667'))

# Generated at 2022-06-14 04:37:50.979584
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    assert round(dcfc_30_360_german(start=start, asof=asof, end=asof), 14) == Decimal('0.16666666666667')
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    assert round(dcfc_30_360_german(start=start, asof=asof, end=asof), 14) == Decimal('0.16944444444444')
    start, asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)

# Generated at 2022-06-14 04:38:04.775518
# Unit test for method interest of class DCC
def test_DCC_interest():
    curr = Currencies['EUR']
    test_start = Date(2021,1,1)
    test_asof = Date(2021,2,2)
    test_end = Date(2022,1,1)
    test_freq = Decimal(2)
    import numpy as np
    for i in range(100):
        rate = np.random.rand()
        principal = Money(round(np.random.rand()*100000000),curr)
        test = DCCs['ACT/360'].interest(principal, rate, test_start, test_asof, test_end, test_freq)
        ans = principal * rate * DCCs['ACT/360'].calculate_fraction(test_start, test_asof, test_end, test_freq)

# Generated at 2022-06-14 04:38:12.912731
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    """
    Tests function dcfc_30_e_360 for two sets of data
    """
    test_data = [
        datetime.date(2007, 12, 28), datetime.date(2008, 2, 28),
        datetime.date(2007, 12, 28), datetime.date(2008, 2, 29),
        datetime.date(2007, 10, 31), datetime.date(2008, 11, 30),
        datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)]
    expected_vals = [
        Decimal('0.16666666666667'),
        Decimal('0.16944444444444'),
        Decimal('1.08333333333333'),
        Decimal('1.33055555555556')]

# Generated at 2022-06-14 04:38:55.221206
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), None), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), None), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_e_plus_360(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), None), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:39:03.656986
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    # test cases
    # case 1:
    start_date = datetime.date(2017, 1, 15)
    end_date = datetime.date(2017, 2, 15)
    asof = datetime.date(2017, 2, 1)
    actual_result = DCC(
        'DCC', {'DCC'}, {Currencies['USD']},
        lambda start, asof, end, freq: (
            ZERO
            if asof < start
            else ONE if asof == end
            else Decimal(asof.day) / Decimal(end.day) if end.day > 0 else ZERO
        )
    ).calculate_daily_fraction(start_date, asof, end_date)
    expected_result = Decimal('0.0642857142857143')

# Generated at 2022-06-14 04:39:05.975143
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    lDCCR = DCCRegistryMachinery()
    lDCCR.register(lDCC)
    try:
        lDCCR.register(lDCC)
    except TypeError:
        pass
    else:
        raise AssertionError

# Generated at 2022-06-14 04:39:16.626213
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
  ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
  ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
  ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
  ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
  assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:39:25.377625
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    assert round(dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14)==Decimal('0.16986301369863')
    assert round(dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14)==Decimal('0.16986301369863')

# Generated at 2022-06-14 04:39:36.414992
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    import pandas as pd
    from pandas.testing import assert_series_equal
    from result import Ok

    # Test function properly
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:39:49.170464
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)
    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:40:01.248318
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """Test the dcfc_30_360_german() function."""
    from dcc import dcfc_30_360_german
    ## Test data:
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ans = Decimal('0.16666666666667')
    assert(round(dcfc_30_360_german(start, asof, asof), 14) == ans)
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ans = Decimal('0.16944444444444')
    assert(round(dcfc_30_360_german(start, asof, asof), 14) == ans)
    start, asof = datetime.date

# Generated at 2022-06-14 04:40:09.255564
# Unit test for function dcfc_nl_365

# Generated at 2022-06-14 04:40:20.365179
# Unit test for method interest of class DCC
def test_DCC_interest():
    expected_result = Money(36.0, 'EUR')
    initial_accrual_money = Money(200, 'EUR')
    initial_accrual_rate = Decimal(0.18)
    start_date = datetime.date(2011, 1, 1)
    asof_date = datetime.date(2012, 3, 1)
    end_date = datetime.date(2012, 3, 1)
    freq = Decimal(1)
    result = DCCRegistry['act/360'].interest(initial_accrual_money, initial_accrual_rate, start_date, asof_date, end_date, freq)
    assert result == expected_result

