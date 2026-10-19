

# Generated at 2022-06-14 04:35:27.301941
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert round(dcfc_30_360_german(datetime.date(2010,3,31), datetime.date(2010,4,30), datetime.date(2010,4,30)), 14) == Decimal("0.30555555555556")
    assert round(dcfc_30_360_german(datetime.date(2010,2,28), datetime.date(2010,3,31), datetime.date(2010,3,31)), 14) == Decimal("0.30277777777778")
    assert round(dcfc_30_360_german(datetime.date(2010,1,31), datetime.date(2010,2,28), datetime.date(2010,2,28)), 14) == Decimal("0.29444444444444")


# Generated at 2022-06-14 04:35:34.293652
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194')

# Generated at 2022-06-14 04:35:41.057710
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Unit test of dcfc_30_360_german and related functions.
    """
    ## Test whether function dcfc_30_360_german yields the correct result for the example of ISDA 1999.

# Generated at 2022-06-14 04:35:51.854345
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:36:02.492967
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14) == Decimal("0.16942884946478")
    assert round(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14) == Decimal("0.17216108990194")
    assert round(dcfc_act_act(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14) == Decimal("1.08243131970956")

# Generated at 2022-06-14 04:36:08.725453
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:36:21.945307
# Unit test for method find of class DCCRegistryMachinery
def test_DCCRegistryMachinery_find():
    start = datetime.date(2008, 12, 28)
    end = datetime.date(2009, 2, 28)
    rate = Decimal(0.01)
    expected_calculate_fraction_result_1 = Decimal('0.16942884946478')
    expected_calculate_fraction_result_2 = Decimal('0.15846839742282')
    expected_calculate_fraction_result_3 = Decimal('0.15846839742282')
    expected_calculate_fraction_result_4 = Decimal('0.15846839742282')
    expected_calculate_fraction_result_5 = Decimal('0.15846839742282')
    expected_interest = Decimal('1694.29')

# Generated at 2022-06-14 04:36:33.413483
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:36:38.523213
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    assert round(dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16986301369863')
    assert round(dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:36:43.562162
# Unit test for method calculate_fraction of class DCC

# Generated at 2022-06-14 04:37:10.784984
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    """
    Tests the day count fraction calculator for the "Act/365A" convention.
    """
    ## Test cases:
    ex_start, ex_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    assert round(dcfc_act_365_a(start=ex_start, asof=ex_asof, end=ex_asof), 14) == Decimal("0.16986301369863")

    ex_start, ex_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    assert round(dcfc_act_365_a(start=ex_start, asof=ex_asof, end=ex_asof), 14) == Decimal("0.17213114754098")



# Generated at 2022-06-14 04:37:19.053925
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    dcc = DCC('ACT360', {'ACT360'}, {Currencies["USD"]}, identity)
    assert dcc.coupon(Money(1, Currencies["USD"]), Decimal(0.01), Date(2018, 4, 1), Date(2018, 5, 1), Date(2018, 6, 1), 2) == Money(0.0006944444444444445, Currencies["USD"])



# Generated at 2022-06-14 04:37:24.872617
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ## Test 1:
    start, asof = datetime.date(2018, 4, 30), datetime.date(2018, 5, 31)
    end = datetime.date(2018, 12, 28)
    assert 0.10958333333333333333333333333333333333333333333333 == dcfc_30_360_german(start, asof, end)

    ## Test 2:
    start, asof = datetime.date(2018, 2, 28), datetime.date(2018, 5, 31)
    end = datetime.date(2018, 12, 28)
    assert 0.31666666666666666666666666666666666666666666666667 == dcfc_30_360_german(start, asof, end)

    ## Test 3:

# Generated at 2022-06-14 04:37:30.284777
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    print("test_dcfc_30_360_us")

    with unittest.TestCase() as testcase:
        testcase.assertEqual(round(dcfc_30_360_us(datetime.date(2014, 12, 1), datetime.date(2015, 4, 30), datetime.date(2015, 4, 30)), 14), Decimal('0.44444444444444'))
        testcase.assertEqual(round(dcfc_30_360_us(datetime.date(2014, 12, 1), datetime.date(2015, 4, 30), datetime.date(2015, 5, 30)), 14), Decimal('0.47777777777778'))

# Generated at 2022-06-14 04:37:41.363195
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:37:53.477273
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    ex1_start, ex1_asof = date(2007, 12, 28), date(2008, 2, 28)
    ex2_start, ex2_asof = date(2007, 12, 28), date(2008, 2, 29)
    ex3_start, ex3_asof = date(2007, 10, 31), date(2008, 11, 30)
    ex4_start, ex4_asof = date(2008, 2, 1), date(2009, 5, 31)
    assert round(dcfc_act_365_l(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16939890710383')

# Generated at 2022-06-14 04:38:00.480914
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 9, 10), end=datetime.date(2020, 3, 2)), 10) == Decimal('0.5245901639')



# Generated at 2022-06-14 04:38:10.301139
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    """Test function dcfc_30_e_360."""
    # Arrange
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 27), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 12, 30), datetime.date(2008, 2, 29)
    ex4_start, ex4_asof = datetime.date(2007, 12, 28), datetime.date(2008, 3, 31)
    ex5_start, ex5_asof = datetime.date(2007, 12, 29), datetime.date(2008, 3, 31)
    ex6

# Generated at 2022-06-14 04:38:16.419559
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    import datetime
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 9, 10), end=datetime.date(2020, 3, 2)), 10) == 0.5245901639
    assert round(dcfc_act_act_icma(start=datetime.date(2020, 3, 2), asof=datetime.date(2020, 9, 10), end=datetime.date(2021, 3, 2)), 10) == 0.5245901639
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 3, 3), end=datetime.date(2020, 3, 2)), 10) == 0.0027397

# Generated at 2022-06-14 04:38:20.589770
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    # Set the global variable of year_start to check if it is reset with the default value
    global year_start
    year_start = 2011
    ## test case 1
    # Set up the input dates
    start = datetime.date(2011,1,1)
    asof = datetime.date(2011,2,28) 
    end = datetime.date(2011,12,31)
    # Set up the expected output result
    result_except = 0.090410958904109
    # Get the actual result 
    result_actual = dcfc_act_365_l(start, asof, end)
    # Check if the actual result and the expected result are the same
    assert result_actual == result_except, " The actual result or the expected result is wrong!"
    
    ## test case 2
    # Set up the

# Generated at 2022-06-14 04:39:05.816946
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)) == Decimal(0.16666666666667)
    assert dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)) == Decimal(0.16944444444444)
    assert dcfc_30_e_plus_360(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)) == Decimal(1.08333333333333)
    assert dcfc_30_e_plus_360(datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)) == Decimal(1.33333333333333)
    assert dcfc

# Generated at 2022-06-14 04:39:12.398448
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    dcc = DCC('name', {'altname1', 'altname2'}, {Currencies['EUR'], Currencies['USD']}, lambda a, b, c, d: Decimal('0.5'))
    assert dcc.calculate_daily_fraction(datetime.date(2014, 1, 1), datetime.date(2014, 1, 2), datetime.date(2014, 1, 3)) == Decimal(0.5)


# Generated at 2022-06-14 04:39:23.453380
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    # check DCC._USE_EOM_MONTHS
    assert DCC.calculate_daily_fraction(datetime.date(2014,12,31), datetime.date(2015,1,3), datetime.date(2015,1,3), Decimal('1.00')) == ONE
    assert DCC.calculate_daily_fraction(datetime.date(2014,12,31), datetime.date(2015,1,2), datetime.date(2015,1,3), Decimal('1.00')) == Decimal('0.04')

# Generated at 2022-06-14 04:39:35.707679
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    '''
    Test method calculate_daily_fraction of class DCC
    :return:
    '''
    ## Get the tests:

# Generated at 2022-06-14 04:39:44.634564
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    '''
    This function performs unit tests on function dcfc_30_e_360
    '''

    # Define module to be tested
    from financepy.finutils import *

    ## Create some data in a dataframe
    import pandas as pd
    from datetime import date,timedelta

    startDate  = date(2017,1,1)
    endDate    = date(2017,12,31)
    numDays    = (endDate - startDate).days
    numMonths  = numDays/30
    numYears   = numDays/365

    dates = pd.date_range(startDate,endDate)
    df = pd.DataFrame(index = dates)
    df["Date"]  = df.index
    df["Month"] = df.index.month
    df["Day"]   = df

# Generated at 2022-06-14 04:39:55.674119
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    print(round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14))

# Generated at 2022-06-14 04:40:06.307370
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    """
    Test function dcfc_act_act().
    """
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194')

# Generated at 2022-06-14 04:40:12.126667
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    '''
    Unit test for function dcfc_30_360_german
    Covers all possible cases
    '''
    asof = datetime.date(2008, 2, 29)
    end = datetime.date(2008, 2, 29)
    assert round(dcfc_30_360_german(start=datetime.date(2008, 2, 1), asof=asof, end=end), 14)==round(Decimal('0.16666666666667'),14)
    assert round(dcfc_30_360_german(start=datetime.date(2008, 2, 10), asof=asof, end=end), 14)==round(Decimal('0.13888888888889'),14)

# Generated at 2022-06-14 04:40:23.830598
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    bdc = DCCRegistry["30/360"]
    assert bdc.calculate_daily_fraction(datetime.date(2015, 1, 1), datetime.date(2015, 1, 1), datetime.date(2015, 2, 1)) == 0
    assert bdc.calculate_daily_fraction(datetime.date(2015, 1, 1), datetime.date(2015, 1, 2), datetime.date(2015, 2, 1)) == 1/360
    assert bdc.calculate_daily_fraction(datetime.date(2015, 1, 1), datetime.date(2015, 1, 6), datetime.date(2015, 2, 1)) == 5/360

# Generated at 2022-06-14 04:40:32.403227
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert (round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667'))

# Generated at 2022-06-14 04:41:46.867920
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert dcfc_30_360_german(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == Decimal("0.16666666666667")
    assert dcfc_30_360_german(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) == Decimal("0.16944444444444")
    assert dcfc_30_360_german(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)) == Decimal("1.08333333333333")

# Generated at 2022-06-14 04:41:58.951709
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ## In his paper 'The Definition of the Accrual Period for Interest Paying Bonds',
    ## Richard Sarnoff (the creator of the 30/360 US day count convention) provides
    ## the following examples:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    ## The caclulations for those examples are

# Generated at 2022-06-14 04:42:06.389220
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    dcc = DCC('my', {'my1', 'my2'}, {'USD', 'EUR'}, lambda a, b, c, d: Decimal(0))
    DCCRegistry.register(dcc)
    assert dcc.name == 'my'
    assert dcc.altnames == {'my1', 'my2'}
    assert dcc.currencies == {'USD', 'EUR'}



# Generated at 2022-06-14 04:42:12.044793
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    from datetime import date
    assert dcfc_30_360_german(date(2017, 1, 31), date(2017, 2, 28), date(2017, 2, 28)) == 0.0833333333333333
    assert dcfc_30_360_german(date(2017, 1, 31), date(2017, 2, 28), date(2017, 2, 28)) == 0.0833333333333333
    assert dcfc_30_360_german(date(2017, 1, 31), date(2017, 1, 31), date(2017, 1, 31)) == 1
    assert dcfc_30_360_german(date(2017, 1, 30), date(2017, 1, 30), date(2017, 1, 30)) == 1

# Generated at 2022-06-14 04:42:24.153666
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    start = datetime.date(2017,1,1)
    asof = datetime.date(2017,1,10)
    end = datetime.date(2017,1,20)
    freq = Decimal(2)
    dcc = DCC(name = "ACT/365", altnames = {}, currencies = _as_ccys(Currencies.codes()), calculate_fraction_method=ACT365)
    assert dcc.calculate_fraction(start, asof, end, freq) == Decimal(9/365)
    assert dcc.calculate_fraction(end, asof, end, freq) == Decimal(0)
    assert dcc.calculate_fraction(start, start, start, freq) == Decimal(0)

# Generated at 2022-06-14 04:42:30.110794
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

    result = round(dcfc_30_e_360(start=start, asof=asof, end=asof), 14)

    assert result == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:42:36.196773
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    assert round(dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16986301369863')
    assert round(dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:42:36.678411
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    pass

# Generated at 2022-06-14 04:42:46.222896
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():

    start_date = date(2010, 1, 25)
    end_date   = date(2010, 9, 25)

    assert(round(dcfc_30_e_360(start_date, end_date, end_date), 14) == 0.27777777777778)
    assert(round(dcfc_30_e_360(start_date, end_date, end_date), 14) == round(0.27777777777777778, 14))



# Generated at 2022-06-14 04:42:54.283998
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    import unittest
    from decimal import Decimal
    import datetime

# Generated at 2022-06-14 04:43:22.087474
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    dcc_registry = DCCRegistry()
    dcc = DCC(name="test", altnames={"test_alt"}, currencies={Currencies['USD']}, calculate_fraction_method=dcf_act_act)
    dcc_registry.register(dcc)
    assert dcc_registry._buffer_main["test"] == dcc
    assert dcc_registry._buffer_altn["test_alt"] == dcc



# Generated at 2022-06-14 04:43:26.223271
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    start = Date(2013,1,1)
    asof = Date(2013,1,2)
    end = Date(2013,1,5)
    dcf = DCC.ACT_360.calculate_daily_fraction(start, asof, end)
    assert dcf == Decimal("0.00277777777777778")

# Generated at 2022-06-14 04:43:38.713735
# Unit test for method calculate_daily_fraction of class DCC

# Generated at 2022-06-14 04:43:47.640358
# Unit test for method interest of class DCC
def test_DCC_interest():
    start_date = datetime.date(2017,11,1)
    asof_date = datetime.date(2018,11,1)
    end_date = datetime.date(2018,11,1)
    principal = Money(123.0, Currencies.USD)
    rate = Decimal(0.1)
    interest = principal * rate * (end_date - start_date).days / 360
    assert DCCRegistry.get("ACT/360").interest(principal, rate, start_date, asof_date, end_date) == interest



# Generated at 2022-06-14 04:43:51.689077
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) == 0.16942884946478
    assert dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)) ==0.17216108990194
    assert dcfc_act_act(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)) == 1.08243131970956

# Generated at 2022-06-14 04:44:01.523388
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    ## Define the dcc:
    dcc = DCC("Act/Act", {"ACTUAL/ACTUAL", "ACTUAL365", "ACT/ACT", "ACT/365", "ACT/365L", "ACT/365F"}, {Currencies['USD']}, DCFC.ACTUAL_ACTUAL)
    ## Register the dcc:
    DCCRegistry.register(dcc)
    ## Checks if registered:
    assert DCCRegistry.find("ACT/ACT") == dcc
    assert DCCRegistry.find("ACT/365") == dcc
    assert DCCRegistry.find("ACT/365L") == dcc
    assert DCCRegistry.find("ACT/365F") == dcc
    ## Attempt to re-register:

# Generated at 2022-06-14 04:44:09.342798
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    # data for test :
    dcc = DCC(
        'Actual/360',
        {'Act/360', 'ACT/360'},
        {Currencies['USD']},
        _actual_360
    )
    #  test for method calculate_daily_fraction
    assert dcc.calculate_daily_fraction(datetime.date(2013, 6, 1), datetime.date(2013, 6, 2), datetime.date(2013, 6, 3)) == Decimal('0.00277777')


# Generated at 2022-06-14 04:44:19.901099
# Unit test for method interest of class DCC
def test_DCC_interest():
    start = datetime.date(2017, 1, 1)
    asof = datetime.date(2017, 1, 2)
    end = datetime.date(2017, 1, 3)
    principal = Money(10, Currencies.EUR)
    rate = Decimal(0.5)
    dcc = DCCRegistry.DCC_ACTUAL_365
    result = dcc.interest(principal, rate, start, asof, end)
    print('result = ', result)
    return result == Money(0.036986301369863, Currencies.EUR)
