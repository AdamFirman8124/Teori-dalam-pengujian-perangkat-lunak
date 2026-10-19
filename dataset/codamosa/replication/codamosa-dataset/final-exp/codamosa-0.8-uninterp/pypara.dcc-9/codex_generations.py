

# Generated at 2022-06-14 04:34:52.569751
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    
    begin_date = Date(2010,9,1)
    end_date = Date(2012,10,1)
    date = Date(2011,8,1)
    freq = 1
    rate = 0.08
    
    def dcc_30E(start,asof,end,freq):
        if asof <= start or asof >= end:
            return ZERO

        s_day, s_month, s_year = start.day, start.month, start.year
        e_day, e_month, e_year = end.day, end.month, end.year
        a_day, a_month, a_year = asof.day, asof.month, asof.year


# Generated at 2022-06-14 04:35:03.621381
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:35:14.401010
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Test case for dcfc_30_360_us()
    """
    ## Parameters:
    d1 = datetime.date(2008, 1, 30)
    d2 = datetime.date(2008, 2, 29)
    d3 = datetime.date(2008, 3, 31)
    d4 = datetime.date(2008, 4, 30)

    ## Test:
    assert round(dcfc_30_360_us(start=d1, asof=d2, end=d2), 14) == Decimal('0.083333333333333')
    assert round(dcfc_30_360_us(start=d2, asof=d3, end=d3), 14) == Decimal('0.0861111111111111')

# Generated at 2022-06-14 04:35:19.032566
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert dcfc_act_act_icma(datetime.date(2002,1,1), datetime.date(2002,2,1), datetime.date(2002,3,1)) == Decimal(1)/Decimal(365)
    assert dcfc_act_act_icma(datetime.date(2002,1,1), datetime.date(2002,3,1), datetime.date(2003,1,1)) == Decimal('0.534246575342465753424657534')


# Generated at 2022-06-14 04:35:31.150071
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    This is the unit test for the dcfc_30_360_us function.
    """
    ## Set up:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    ## Execute:

# Generated at 2022-06-14 04:35:45.429618
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    assert round(dcc_factory("NL/365")(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == round(Decimal('0.16986301369863'), 14)
    assert round(dcc_factory("NL/365")(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == round(Decimal('0.16986301369863'), 14)

# Generated at 2022-06-14 04:35:52.786953
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    start = datetime.date(year=2007, month=12, day=28)
    asof = datetime.date(year=2008, month=2, day=29)
    end = datetime.date(year=2009, month=5, day=31)
    assert round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_e_plus_360(start=start, asof=datetime.date(2020, 4, 30), end=end), 14) == Decimal('12.3333333333333')

# Generated at 2022-06-14 04:36:00.073018
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) == Decimal('0.16986301369863')



# Generated at 2022-06-14 04:36:07.486348
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_us(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_us(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:36:15.140249
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():

    dcc_list = [datetime.date(2017, 1, 2), datetime.date(2017, 1, 3), datetime.date(2016, 12, 30)]
    dcc_period = datetime.timedelta(days=1)
    dcc_start = dcc_list[0]
    dcc_end = dcc_list[-1]
    dcc_fraction = ZERO
    for dcc_date in dcc_list:
        dcc_fraction += dcc_date.day_count_fraction(dcc_start, dcc_end)

    assert dcc_fraction == ONE



# Generated at 2022-06-14 04:36:53.015748
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    """Test function dcfc_act_act_icma"""
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    assert round(dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end), 10) == Decimal('0.5245901639')



# Generated at 2022-06-14 04:37:00.003529
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2016, 1, 29), datetime.date(2016, 12, 29)

# Generated at 2022-06-14 04:37:13.457017
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert dcfc_act_365_l(datetime.date(2012,1,1),datetime.date(2012,3,1),datetime.date(2012,3,1))==0.136986301369863
    assert dcfc_act_365_l(datetime.date(2012,1,1),datetime.date(2012,12,1),datetime.date(2012,12,1))==0.986301369863014
    assert dcfc_act_365_l(datetime.date(2012,1,1),datetime.date(2012,3,1),datetime.date(2013,3,1))==0.365753424657534


# Generated at 2022-06-14 04:37:26.192003
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 9, 10), end=datetime.date(2020, 3, 2)), 10) == 0.5245901639
    assert round(dcfc_act_act_icma(start=datetime.date(2025, 3, 2), asof=datetime.date(2025, 9, 10), end=datetime.date(2026, 3, 2)), 10) == 0.5245901639
    assert round(dcfc_act_act_icma(start=datetime.date(2032, 3, 2), asof=datetime.date(2032, 9, 10), end=datetime.date(2033, 3, 2)), 10) == 0.52459016

# Generated at 2022-06-14 04:37:31.360077
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert dcfc_30_360_isda(
        datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)
    ) == 0.16666666666667
    assert dcfc_30_360_isda(
        datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)
    ) == 0.16944444444444
    assert dcfc_30_360_isda(
        datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)
    ) == 1.08333333333333

# Generated at 2022-06-14 04:37:42.182694
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    """Test for the function dcfc_30_e_360."""
    assert abs((dcfc_30_e_360(start=datetime.date(2007, 12, 28),
                              asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) - 0.16666666666667) \
                                                                                                    / 0.16666666666667) \
           < 1e-14
    assert abs((dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29))
                - 0.16944444444444) / 0.16944444444444) < 1e-14

# Generated at 2022-06-14 04:37:52.322951
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    test1_start = datetime.date(2013, 4, 1)
    test1_asof = datetime.date(2013, 5, 2)
    print("Numer of days:", (test1_asof.day - test1_start.day) + 30 * (test1_asof.month - test1_start.month) + 360 * (test1_asof.year - test1_start.year))
    print("Day count fraction:", dcfc_30_e_plus_360(test1_start, test1_asof, test1_asof))

    test2_start = datetime.date(2013, 4, 1)
    test2_asof = datetime.date(2013, 5, 31)

# Generated at 2022-06-14 04:38:02.059699
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == _decimal(0.16666666666667)

# Generated at 2022-06-14 04:38:11.185265
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == round(Decimal('0.16666666666667'), 14)
    assert round

# Generated at 2022-06-14 04:38:15.291367
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    result = dcfc_act_act_icma(start = ex1_start, asof = ex1_asof, end = ex1_end, freq = None)
    expected = Decimal('0.5245901639')
    assert expected == result


# Generated at 2022-06-14 04:40:10.436828
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCRegistry["Actual/Actual"].calculate_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1), datetime.date(2017, 1, 1)) == 0.0
    assert DCCRegistry["Actual/Actual"].calculate_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 2), datetime.date(2017, 1, 2)) == 1.0
    assert DCCRegistry["Actual/Actual"].calculate_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 2), datetime.date(2017, 2, 1)) == 1.0
    

# Generated at 2022-06-14 04:40:23.045764
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    # test case 1
    assert(round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667'))

    # test case 2
    assert(round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444'))

    # test case 3

# Generated at 2022-06-14 04:40:34.293775
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    from .calendars import TARGET_HOLIDAYS
    # T-1
    start = Date(2019, 7, 15)
    asof = Date(2019, 12, 5)
    end = Date(2019, 12, 19)
    freq = Decimal(2)
    assert DCCRegistry.ACT_ACT_ISDA.calculate_daily_fraction(
        start, asof, end, freq
    ) == "0.0"

    # On the start date of the period
    start = Date(2019, 7, 15)
    asof = Date(2019, 12, 19)
    end = Date(2019, 12, 19)
    freq = Decimal(2)

# Generated at 2022-06-14 04:40:36.539331
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    """
    Unit test for method calculate_daily_fraction of class DCC
    """

# Generated at 2022-06-14 04:40:40.843006
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    start, asof, end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)
    assert round(dcfc_30_360_german(start, asof, end), 14) == Decimal('0.16666666666667')

    start, asof, end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 28)
    assert round(dcfc_30_360_german(start, asof, end), 14) == Decimal('0.16944444444444')

    start, asof, end = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)

# Generated at 2022-06-14 04:40:52.601329
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) == Decimal('0.16666666666667')
    assert dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)) == Decimal('0.16944444444444')
    assert dcfc_30_360_german(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:41:04.136782
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    
    print("Testing DCC.calculate_daily_fraction ...")
    
    from .enums import DCCs
    from .dates import date
    from .money import EUR

    names = [
        ("ACT_365", 0.0027397260273972602),
        ("ACT_360", 0.002777777777777778),
        ("ACT_ACT_ICMA", 0.002739726027397260),
        ("ACT_ACT_ISDA", 0.0027397260273972602),
    ]

    # test values are from http://www.daycountconvention.com/day_count_fraction/
    start = date("2012-7-1")
    asof = date("2012-7-2")
    end = date("2016-7-1")

   

# Generated at 2022-06-14 04:41:08.512615
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCCRegistry["ACT/365"].calculate_daily_fraction(
        datetime.date(2020, 7, 1),
        datetime.date(2020, 7, 30),
        datetime.date(2020, 7, 31),
    ) == Decimal("0.0383561643835616")
    assert DCCRegistry["ACT/365"].calculate_daily_fraction(
        datetime.date(2020, 6, 8),
        datetime.date(2020, 7, 31),
        datetime.date(2020, 9, 30),
    ) == Decimal("-0.0136986301369863")

# Generated at 2022-06-14 04:41:13.867567
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof) == Decimal('0.16666666666667')
    assert dcfc_30_360_us

# Generated at 2022-06-14 04:41:15.869227
# Unit test for method find of class DCCRegistryMachinery
def test_DCCRegistryMachinery_find():
    """
    Test method find of class DCCRegistryMachinery
    """
    test_obj = DCCRegistryMachinery()
    # Try to find a DCC that is not in the registry
    assert test_obj.find("anything") == None


# Generated at 2022-06-14 04:42:18.631694
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    print(dcfc_30_360_us(start=datetime.date(2019, 9, 30), asof=datetime.date(2020, 4, 10), end=datetime.date(2022, 6, 30)))
# End def


# Generated at 2022-06-14 04:42:30.686083
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2007, 9, 30), datetime.date(2008, 9, 29)
    ex6_start, ex6_asof = datetime.date(2008, 9, 30), dat

# Generated at 2022-06-14 04:42:41.272676
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    # Ex 1
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    assert round(dcfc_30_360_german(start, asof), 14) == Decimal('0.16666666666667')

    # Ex 2
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    assert round(dcfc_30_360_german(start, asof), 14) == Decimal('0.16944444444444')

    # Ex 3
    start, asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)

# Generated at 2022-06-14 04:42:48.781882
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:43:01.488392
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    assert round(dcfc_act_365_a(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14)==Decimal('0.16986301369863')
    assert round(dcfc_act_365_a(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14)==Decimal('0.17213114754098')
    assert round(dcfc_act_365_a(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 14)==Dec

# Generated at 2022-06-14 04:43:09.526674
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    '''
    This is the unit test for function dcfc_30_360_isda
    '''
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)
    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:43:19.585638
# Unit test for method interest of class DCC
def test_DCC_interest():
    rate = Decimal(0.03)
    m1 = Money(Decimal(100.0), Currencies.USD)
    sdate = datetime.date(2014,1,1)
    edate = datetime.date(2014,3,31)
    m2 = DCCRegistry.get('ACT/ACT').interest(m1, rate, sdate, edate)
    assert m2.amount == Decimal(2.5)
    assert m2.currency == Currencies.USD

    # Case 2:
    m1 = Money(Decimal(100.0), Currencies.USD)
    sdate = datetime.date(2014,1,1)
    edate = datetime.date(2014,3,31)

# Generated at 2022-06-14 04:43:27.776357
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    """
    Unit test for function dcfc_30_e_360()
    """
    # ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    # ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    # ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    # ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:43:34.327108
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    dccreg = DCCRegistryMachinery()
    dccreg.register(DCC("1", {"x"}, {"USD"}, DCFM("AFB")))
    assert dccreg.find("1").name == "1"
    assert dccreg.find("x").name == "1"
    assert dccreg.find("X").name == "1"
    assert DCC("2", {"y"}, {"USD"}, DCFM("AFB")) in dccreg.registry
    # __UnhandledException__
    try:
        dccreg.register(DCC("1", {"x"}, {"USD"}, DCFM("AFB")))
        assert False
    except TypeError:
        assert True


DCCRegistry: DCCRegistryMachinery = DCCRegistryMachinery()
"""
Provides the day count registry model.
"""

# Generated at 2022-06-14 04:43:43.092801
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    assert dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) == 0.16986301369863
    assert dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)) == 0.16986301369863
    assert dcfc_nl_365(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)) == 1.08219178082192