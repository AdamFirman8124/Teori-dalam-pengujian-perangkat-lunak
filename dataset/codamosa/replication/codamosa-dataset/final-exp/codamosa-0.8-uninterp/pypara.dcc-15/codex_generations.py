

# Generated at 2022-06-14 04:35:16.064060
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:35:26.295128
# Unit test for method interest of class DCC
def test_DCC_interest():
    t_dcc = DCC(
        name='Actual360',
        altnames={'30/360 US', 'Eurobondbasis'},
        currencies=_as_ccys(
            {'AUD', 'BEF', 'CAD', 'CHF', 'EUR', 'GBP', 'JPY', 'NZD', 'USD'}),
        calculate_fraction_method=Actual360().calculate_fraction)
    assert t_dcc.interest(Money('10', 'USD'), Decimal('0.1'), datetime.date(2014, 1, 1), datetime.date(2014, 2, 28)) == Money('0.3', 'USD')

# Generated at 2022-06-14 04:35:35.468657
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:35:48.948494
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():

    assert round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)),14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)),14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:35:56.311371
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:36:01.370671
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    """
    Unit test for function dcfc_30_360_isda.
    """

    ## Data used for the unit tests:
    start = datetime.date(2007, 12, 28)
    asof = datetime.date(2008, 2, 28)
    end = datetime.date(2008, 2, 29)
    result = Decimal(0.16666666666667)

    ## Unit test:
    assert round(dcfc_30_360_isda(start=start, asof=asof, end=end), 14) == result



# Generated at 2022-06-14 04:36:08.168781
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():

    ## These are test cases provided here:
    ## http://www.isda.org/c_and_a/pdf/mktc1198.pdf
    ## Note that the day count fraction must be multiplied by
    ## the length of the period (in years), i.e.:
    ## 
    ##     >>> ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ##     >>> ex1_end = datetime.date(2009, 12, 28)
    ##     >>> dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof) * ex1_end.year
    ##     Decimal('1.00000000000001')


    ex1_start, ex1_

# Generated at 2022-06-14 04:36:11.521570
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    import datetime
    start = datetime.date(1999, 2, 28)
    asof = datetime.date(1999, 3, 15)
    assert dcfc_30_e_360(start=start, asof=asof, end=asof) == Decimal('0.04166666666667')



# Generated at 2022-06-14 04:36:22.934922
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    print("Testing function dcfc_30_360_german ...")
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)

# Generated at 2022-06-14 04:36:33.988142
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:37:16.272007
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert dcfc_30_e_plus_360(start=datetime.date(2018,3,30),asof=datetime.date(2018,6,29),end=datetime.date(2018,6,29)) == Decimal("0.08333333333333")+Decimal("0.08333333333333")+Decimal("0.08333333333333")
    assert dcfc_30_e_plus_360(start=datetime.date(2018,4,30),asof=datetime.date(2018,6,29),end=datetime.date(2018,6,29)) == Decimal("0.08333333333333")+Decimal("0.08333333333333")

# Generated at 2022-06-14 04:37:29.223233
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194')

# Generated at 2022-06-14 04:37:32.708384
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    assert( round(dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end), 10) == Decimal('0.5245901639') )
# Test function test_dcfc_act_act_icma()
test_dcfc_act_act_icma()



# Generated at 2022-06-14 04:37:46.652005
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    # ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    # ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    # ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    # ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2017, 2, 28), datetime.date(2017, 3, 31)
    import math

# Generated at 2022-06-14 04:37:55.143799
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 9, 10), end=datetime.date(2020, 3, 2)), 10) == Decimal('0.5245901639')


# Generated at 2022-06-14 04:38:01.103029
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    """
    :return: Nothing.
    """
    import doctest
    doctest.testmod(extraglobs=dict(dcfc_30_e_360=dcfc_30_e_360))
    return



# Generated at 2022-06-14 04:38:08.182867
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=ex1_asof), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=ex2_asof), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:38:21.433896
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007,12,28), asof=datetime.date(2008,2,28), end=datetime.date(2008,2,28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007,12,28), asof=datetime.date(2008,2,29), end=datetime.date(2008,2,29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:38:32.325795
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    """
    Test Cases for function dcfc_act_act
    """
    assert dcfc_act_act(datetime.date(2007, 12, 28),datetime.date(2008, 2, 28),datetime.date(2008, 2, 28))==0.16942884946478
    assert dcfc_act_act(datetime.date(2007, 12, 28),datetime.date(2008, 2, 29),datetime.date(2008, 2, 29))==0.17216108990194
    assert dcfc_act_act(datetime.date(2007, 10, 31),datetime.date(2008, 11, 30),datetime.date(2008, 11, 30))==1.08243131970956

# Generated at 2022-06-14 04:38:40.380976
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:39:18.581322
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    start_date = datetime.date(2017, 11, 10)
    asof_date = datetime.date(2017, 11, 10)
    end_date = datetime.date(2017, 11, 20)
    freq = Decimal(2)
    dcc_func = DCCRegistry.get("30e/360 ISDA")

    actual_result = dcc_func.calculate_fraction(start_date, asof_date, end_date, freq)
    expected_result = Decimal(0.1111111111111111)

    assert actual_result == expected_result
    print("Test for method calculate_fraction of class DCC passed")


# Generated at 2022-06-14 04:39:26.454076
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(datetime.date(2008, 10, 30), datetime.date(2009, 2, 28), datetime.date(2009, 2, 28)), 14)  == Decimal('0.16666666666667')
    assert round(dcfc_30_360_us(datetime.date(2008, 10, 31), datetime.date(2009, 2, 28), datetime.date(2009, 2, 28)), 14)  == Decimal('0.16666666666667')
    assert round(dcfc_30_360_us(datetime.date(2008, 10, 31), datetime.date(2009, 2, 28), datetime.date(2009, 2, 28)), 14)  == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:39:31.085850
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert Decimal(round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)) == Decimal('0.16666666666667')
    assert Dec

# Generated at 2022-06-14 04:39:36.090943
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    """[summary]
    """
    dcc_30e360_with_leap = DCC(
        "30E/360 With Leap",
        {"30E/360WL", "30/360WL", "30WD/360WL", "ACT/360WL", "ACT/360"},
        _as_ccys({"AUD", "CHF", "CNY", "EUR", "GBP", "JPY", "USD", "XAG", "XAU"}),
        lambda s, a, e, f: Decimal(_get_actual_day_count(min(max(s, a), e), max(s, e))) / Decimal(360),
    )

# Generated at 2022-06-14 04:39:48.743148
# Unit test for method interest of class DCC
def test_DCC_interest():
    from .money import Money
    from .currencies import Currencies
    from .commons.zeitgeist import Date
    from .rates import Rate

    test_obj = DCC("A","A","B",rate)
    assert type(test_obj.interest(Money(1,Currencies.USD),1,Date(2013,12,31),Date(2014,12,31),Date(2014,12,31),1)) == Money
    assert test_obj.interest(Money(1,Currencies.USD),1,Date(2013,12,31),Date(2014,12,31),Date(2014,12,31),1).amount == 1
    assert test_obj.interest(Money(1,Currencies.USD),1,Date(2013,12,31),Date(2014,12,31),Date(2014,12,31),1).currency == Cur

# Generated at 2022-06-14 04:39:57.945077
# Unit test for method find of class DCCRegistryMachinery
def test_DCCRegistryMachinery_find():
    # Create an instance of DCCRegistryMachinery
    registry = DCCRegistryMachinery()

    # Create an instance of DCC, passing "Test" to the name parameter and an empty set to the altnames parameter
    dcc = DCC("Test", set(), set(), DCFC(lambda x, y, z, w: Decimal(0)))

    # Register dcc to registry
    registry.register(dcc)

    # Get the value of the result variable by accessing the find method of registry, passing the string "Test" to the name parameter
    result = registry.find("Test")

    # Check if the result variable is equal to dcc
    assert result == dcc

    # Get the value of the result variable by accessing the find method of registry, passing the string "test" to the name parameter
    result = registry.find("test")

    # Check if

# Generated at 2022-06-14 04:40:07.577875
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    # This function tests the function dcfc_30_e_360()
    # Creating a list of example dates
    example_start_dates = [datetime.date(2007, 12, 28), datetime.date(2007, 12, 28), datetime.date(2007, 10, 31),
                           datetime.date(2008, 2, 1)]
    example_as_of_dates = [datetime.date(2008, 2, 28), datetime.date(2008, 2, 29), datetime.date(2008, 11, 30),
                           datetime.date(2009, 5, 31)]
    example_end_dates = example_as_of_dates

# Generated at 2022-06-14 04:40:20.322078
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = (datetime.date(2007, 12, 28), datetime.date(2008, 2, 28))
    ex2_start, ex2_asof = (datetime.date(2007, 12, 28), datetime.date(2008, 2, 29))
    ex3_start, ex3_asof = (datetime.date(2007, 10, 31), datetime.date(2008, 11, 30))
    ex4_start, ex4_asof = (datetime.date(2008, 2, 1), datetime.date(2009, 5, 31))
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal(
        '0.16942884946478')


# Generated at 2022-06-14 04:40:26.974653
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    start = datetime.date(2005, 9, 1)
    asof = datetime.date(2005, 9, 28)
    dcf_30_360_isda = dcfc_30_360_isda(start, asof)
    assert round(dcf_30_360_isda, 14) == Decimal('0.28888888888889')



# Generated at 2022-06-14 04:40:30.520648
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(
        start=datetime.date(2019, 3, 2), 
        asof=datetime.date(2019, 9, 10), 
        end=datetime.date(2020, 3, 2), 
        freq=Decimal(2)),
        10
    ) == Decimal('0.5245901639')



# Generated at 2022-06-14 04:43:22.564243
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(datetime.date(2012,1,1), datetime.date(2012,12,31), datetime.date(2012,12,31), None),14) == Decimal('1.15277777777778')
    assert round(dcfc_30_e_plus_360(datetime.date(2013,1,1), datetime.date(2013,12,31), datetime.date(2013,12,31), None),14) == Decimal('1.15277777777778')

# Generated at 2022-06-14 04:43:26.879080
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    start = datetime.date(2019, 11, 20)
    asof = datetime.date(2019, 12, 31)
    assert round(dcfc_30_360_isda(start=start, asof=asof, end=asof), 14) == Decimal('0.047222222222222')



# Generated at 2022-06-14 04:43:39.217880
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(datetime.date(2020, 1, 31), datetime.date(2020, 2, 29), datetime.date(2020, 2, 29)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_us(datetime.date(2020, 1, 31), datetime.date(2020, 3, 31), datetime.date(2020, 3, 31)), 14) == Decimal('0.33333333333333')
    assert round(dcfc_30_360_us(datetime.date(2020, 1, 31), datetime.date(2020, 3, 30), datetime.date(2020, 3, 30)), 14) == Decimal('0.33333333333333')

# Generated at 2022-06-14 04:43:50.116620
# Unit test for function dcfc_30_360_german

# Generated at 2022-06-14 04:44:00.781904
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    from .currencies import Currency
    from .locales import Locales
    from .monetary import Money

    #  Case 1. Coupon calculation in EUR currency
    principal = Money(10000, Currencies.EUR, Locales.DEFAULT)
    rate = Decimal('0.02')
    StartDate = Date(1, 12, 2017)
    EndDate = Date(1, 6, 2019)
    freq = Decimal(2)
    eom = 30

    expected = Money(-533.73, Currencies.EUR, Locales.DEFAULT)

    actual = DCCs.ACT_360.coupon(principal, rate, StartDate, EndDate, EndDate, freq, eom)

    assert actual == expected

    #  Case 2. Coupon calculation in JPY currency

# Generated at 2022-06-14 04:44:11.191629
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCCRegistry.get('30/360ISDA').calculate_daily_fraction(datetime.date(2018,11,15),datetime.date(2018,12,4),datetime.date(2019,12,4),Decimal(2.0)) == Decimal('0.001388888888888888888888888888888')
    assert DCCRegistry.get('ACT/360').calculate_daily_fraction(datetime.date(2015,9,29),datetime.date(2015,12,4),datetime.date(2016,1,21),Decimal(2.0)) == Decimal('0.01111111111111111111111111111111')

# Generated at 2022-06-14 04:44:22.745462
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    cases = {
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)): 0.16986301369863,
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)): 0.17213114754098,
        (datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)): 1.08196721311475,
        (datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)): 1.32513661202186,
    }
    for dates, expected_dcf in cases.items():
        assert round(dcfc_act_365_a(*dates, *dates), 14) == round(expected_dcf, 14)

