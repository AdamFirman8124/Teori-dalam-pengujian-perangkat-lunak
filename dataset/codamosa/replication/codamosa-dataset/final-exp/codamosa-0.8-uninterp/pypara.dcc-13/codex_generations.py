

# Generated at 2022-06-14 04:35:20.923548
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    print( round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14))

# Generated at 2022-06-14 04:35:25.945762
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    assert(round(dcfc_act_365_a(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16986301369863'))
    assert(round(dcfc_act_365_a(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17213114754098'))

# Generated at 2022-06-14 04:35:31.261530
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
# Test for function dcfc_30_360_isda
test_dcfc_30_360_isda()


# Generated at 2022-06-14 04:35:45.535682
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert dcfc_30_e_360('20181109', '20181110', '20181109') == 1.0 / float(360)
    assert dcfc_30_e_360('20181109', '20181110', '20181109') == 1.0 / float(360)
    assert dcfc_30_e_360('20181109', '20181130', '20181109') == 21.0 / float(360)
    assert dcfc_30_e_360('20181109', '20181231', '20181109') == 52.0 / float(360)
    assert dcfc_30_e_360('20181109', '20190128', '20181109') == 83.0 / float(360)


# Generated at 2022-06-14 04:35:53.317985
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Test function dcfc_30_360_german
    """

    def _test_dcfc_30_360_german(d1,d2,res):
        assert abs(dcfc_30_360_german(d1, d2, d2) - res) < 1e-12
        assert abs(dcfc_30_360_german(d2, d1, d1) - res) < 1e-12

    # Examples taken from https://www.quantstart.com/articles/Basics-of-Financial-Mathematics-Interest-and-Annuities-Certain
    d1 = datetime.date(2000,1,31)
    d2 = datetime.date(2001,1,31)

# Generated at 2022-06-14 04:35:57.108547
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    assert DCC.coupon(Decimal(1000),Decimal(0.05),Date(2017,1,1),Date(2017,1,1),Date(2017,1,1),Decimal(1),None) == Decimal(0)
    assert DCC.coupon(Decimal(1000),Decimal(0.05),Date(2017,1,1),Date(2018,1,1),Date(2018,1,1),Decimal(1),None) == Decimal(50)
    assert DCC.coupon(Decimal(1000),Decimal(0.05),Date(2017,1,1),Date(2018,7,1),Date(2018,7,1),Decimal(2),None) == Decimal(25)



# Generated at 2022-06-14 04:36:06.462772
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    # Test case 1:
    d1 = datetime.date(2012, 10, 30)
    d2 = datetime.date(2012, 11, 30)
    d3 = datetime.date(2013, 1, 31)
    d4 = datetime.date(2014, 12, 31)
    assert dcfc_30_360_german(d1, d2, d2) == Decimal('0.08333333333333')
    assert dcfc_30_360_german(d1, d3, d3) == Decimal(1)
    assert dcfc_30_360_german(d2, d3, d3) == Decimal('0.08333333333333')

# Generated at 2022-06-14 04:36:13.115447
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 10, 1), asof=datetime.date(2012, 2, 29), end=datetime.date(2012, 2, 29)), 14) == Decimal('4.4166666667')
#


# Generated at 2022-06-14 04:36:25.991326
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_e_360(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:36:30.233202
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    ex2_start, ex2_asof, ex2_end = datetime.date(2019, 3, 2), datetime.date(2020, 3, 2), datetime.date(2020, 9, 10)
    ex3_start, ex3_asof, ex3_end = datetime.date(2008, 1, 31), datetime.date(2008, 7, 31), datetime.date(2009, 1, 31)

# Generated at 2022-06-14 04:37:17.601774
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    date1 = datetime.date (2019, 12, 25)
    date2 = datetime.date (2019, 12, 26)
    date3 = datetime.date (2019, 12, 27)
    assert(DCC.calculate_fraction(ACT360, date1, date2, date3) == ONE/(360))
    assert(DCC.calculate_fraction(ACT365, date1, date2, date3) == ONE/(365))


# Generated at 2022-06-14 04:37:26.678552
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(
        dcfc_act_act_icma(
            start=datetime.date(2019, 3, 2),
            asof=datetime.date(2019, 9, 10),
            end=datetime.date(2020, 3, 2)), 10) == Decimal('0.5245901639')
    print("test_dcfc_act_act_icma() passed!")

test_dcfc_act_act_icma()


# Generated at 2022-06-14 04:37:38.692450
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ## Additional test case:
    assert dcfc_30_360_us(datetime.date(2010,3,31), datetime.date(2010,4,30), datetime.date(2010, 4, 30)) == Decimal("1.0")
    assert dcfc_30_360_us(datetime.date(2010,3,31), datetime.date(2010,3,31), datetime.date(2010, 3, 31)) == Decimal("0.0")
    assert dcfc_30_360_us(datetime.date(2010,3,31), datetime.date(2010,4,30), datetime.date(2010, 4, 30)) == Decimal("1.0")

# Generated at 2022-06-14 04:37:46.738604
# Unit test for function dcfc_30_360_german

# Generated at 2022-06-14 04:37:57.089036
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:38:08.701769
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    """
    Test function dcfc_act_365_a()
    """
    print(dcfc_act_365_a(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)))  # Expected result: 0.16986301369863
    print(dcfc_act_365_a(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)))  # Expected result: 0.17213114754098
    print(dcfc_act_365_a(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)))  # Expected result: 1.081967

# Generated at 2022-06-14 04:38:15.099748
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    dcc = DCC('test', [], set(), lambda start, asof, end, freq: ONE)
    assert dcc.calculate_daily_fraction(Date(2018, 1, 1), Date(2018, 1, 2), Date(2018, 1, 2)) == Decimal('1')



# Generated at 2022-06-14 04:38:25.297743
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:38:35.675323
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    from .currencies import Currencies
    from .commons.zeitgeist import Date
    from .enums import DayCountConvention
    dcc = DayCountConvention.ACT_360.dcc
    assert dcc.calculate_daily_fraction(
        Date(2018, 3, 22), Date(2018, 3, 25), Date(2018, 12, 22),
        freq=Decimal(1)) == Decimal('0.0027777777777778')
    assert dcc.calculate_daily_fraction(
        Date(2018, 3, 22), Date(2018, 3, 22), Date(2018, 3, 22),
        freq=Decimal(1)) == Decimal('0')

# Generated at 2022-06-14 04:38:46.379007
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    yield dcfc_30_e_plus_360(datetime.date(2014, 8, 25), datetime.date(2014, 8, 25), datetime.date(2014, 8, 25)) == 0
    yield dcfc_30_e_plus_360(datetime.date(2014, 8, 25), datetime.date(2014, 9, 25), datetime.date(2014, 9, 25)) == 1
    yield dcfc_30_e_plus_360(datetime.date(2014, 8, 25), datetime.date(2014, 8, 26), datetime.date(2014, 8, 25)) == 1 / 360
    yield dcfc_30_e_plus_360(datetime.date(2014, 8, 25), datetime.date(2014, 9, 25), datetime.date(2014, 8, 25))

# Generated at 2022-06-14 04:40:25.956168
# Unit test for method interest of class DCC
def test_DCC_interest():
    DCC1 = DCC(name='DCC1',altnames={"DCC1"} ,currencies= Currencies['USD'],calculate_fraction_method= lambda x,y,z,t: 10)
    principal = Money(1,Currencies['USD'])
    rate = Decimal(0.5)
    start = Date(1,1,2020)
    asof = Date(1,1,2021)
    end = None
    freq = None
    
    assert DCC1.interest(principal,rate,start,asof,end,freq) == Money(5,Currencies['USD'])


# Generated at 2022-06-14 04:40:28.863768
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    from .utils import assert_decimal
    assert_decimal(dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)), 0.5245901639)



# Generated at 2022-06-14 04:40:38.039075
# Unit test for function dcfc_nl_365

# Generated at 2022-06-14 04:40:49.587701
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    cf = DCCRegistry['Act/Act ISDA']
    assert cf.calculate_daily_fraction(datetime.date(2017, 2, 15), datetime.date(2017, 2, 20), datetime.date(2017, 2, 20)) == Decimal('0.0416666666666667')
    assert cf.calculate_daily_fraction(datetime.date(2017, 2, 15), datetime.date(2017, 2, 20), datetime.date(2017, 2, 20), Decimal(1)) == Decimal('0.0416666666666667')
    assert cf.calculate_daily_fraction(datetime.date(2017, 2, 15), datetime.date(2017, 2, 20), datetime.date(2017, 2, 22)) == Decimal('0.0416666666666667')

# Generated at 2022-06-14 04:40:57.841364
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCs["ACT/ACT"].calculate_fraction(datetime.date(2008, 7, 7), datetime.date(2008, 7, 7), datetime.date(2008, 7, 7)) == Decimal(0)
    assert DCCs["ACT/ACT"].calculate_fraction(datetime.date(2008, 7, 7), datetime.date(2008, 7, 8), datetime.date(2008, 7, 8)) == Decimal(1)
    assert DCCs["ACT/ACT"].calculate_fraction(datetime.date(2008, 7, 7), datetime.date(2008, 7, 8), datetime.date(2008, 7, 9)) == Decimal(2)

# Generated at 2022-06-14 04:41:06.614029
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    from datetools.utils import assert_eq
    assert_eq(dcfc_act_365_a(start=Date(day=28, month=12, year=2007), asof=Date(day=28, month=2, year=2008), end=Date(day=28, month=2, year=2008)), 0.16986301369863)
    assert_eq(dcfc_act_365_a(start=Date(day=28, month=12, year=2007), asof=Date(day=29, month=2, year=2008), end=Date(day=29, month=2, year=2008)), 0.17213114754098)

# Generated at 2022-06-14 04:41:11.906182
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCCRegistry["ACT/ACT"].calculate_daily_fraction(datetime.date(2014, 1, 1), datetime.date(2014, 1, 2), datetime.date(2014, 1, 3)) == datetime.date(2014, 1, 1)



# Generated at 2022-06-14 04:41:16.192433
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    dcfc_30_360_isda(start=datetime.date(2006, 10, 16), asof=datetime.date(2006, 12, 19), end=datetime.date(2006, 12, 19))
    dcfc_30_360_isda(start=datetime.date(2015, 10, 16), asof=datetime.date(2016, 2, 15), end=datetime.date(2016, 2, 15))



# Generated at 2022-06-14 04:41:21.672310
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    # Check whether the day count fraction are calculated correctly
    assert round(dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')
    assert round(dcfc_act_365_a(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_a(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08196721311475')

# Generated at 2022-06-14 04:41:34.579593
# Unit test for method interest of class DCC
def test_DCC_interest():
    dcc = DCC(
        "act/360",
        {"ACT/360"},
        _as_ccys({"USD", "EUR", "GBP", "CHF", "CAD"}),
        lambda a, b, c, d: b.days_in_year(c) * Decimal(b - a) / Decimal(c - a),
    )
    principal = Money(100, Currencies.USD)
    rate = 0.05
    start = Date(2017, 1, 1)
    asof = Date(2017, 12, 31)
    end = Date(2018, 1, 1)
    freq = Decimal(1)
    assert dcc.interest(principal, rate, start, asof, end, freq) == Money(5, Currencies.USD)
    # Uncomment these lines to see

# Generated at 2022-06-14 04:42:26.525988
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    a = datetime.date(2017,  1,  1)
    j = datetime.date(2017,  2,  1)
    b = datetime.date(2017, 12, 31)
    _ = DCC('ACT/365', {}, set(), lambda x, y, z, f: Decimal(y.toordinal()-x.toordinal())/Decimal(z.toordinal()-x.toordinal())*Decimal(365))
    assert _.calculate_daily_fraction(a, a, b) == ZERO
    assert _.calculate_daily_fraction(a, a+datetime.timedelta(days=1), b) == ONE/Decimal(365)
    assert _.calculate_daily_fraction(a, b, b) == ONE
    assert _

# Generated at 2022-06-14 04:42:30.176728
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 9, 10), end=datetime.date(2020, 3, 2)),10) == 0.5245901639



# Generated at 2022-06-14 04:42:40.807200
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Test for function dcfc_30_360_us

    Test data is taken from the book:
    * Generation and Valuation of Cash Flows, v1.0, October 3, 2013, p.68-69

    :return: None
    """
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)

# Generated at 2022-06-14 04:42:42.661290
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    """
    Method coupon of class DCC
    """
    assert DCC.coupon() == None


# Generated at 2022-06-14 04:42:49.920241
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert  0==dcfc_30_e_plus_360(start=datetime.date(2007, 2, 28), asof=datetime.date(2007, 3, 31), end=datetime.date(2008, 2, 28))
    assert  0==dcfc_30_e_plus_360(start=datetime.date(2007, 2, 28), asof=datetime.date(2007, 3, 30), end=datetime.date(2008, 2, 28))
    assert  0==dcfc_30_e_plus_360(start=datetime.date(2007, 2, 28), asof=datetime.date(2007, 3, 30), end=datetime.date(2008, 2, 29))

# Generated at 2022-06-14 04:42:56.001630
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    ## Define a DC30E360 function:
    def dcc_30e360_fraction_method(start: Date, asof: Date, end: Date, freq: Optional[Decimal]) -> Decimal:
        """
        Calculates the day count fraction using ISDA 30E360.
        """
        ## Get the actual number of days:
        actual = _get_actual_day_count(start, end)

        ## Get the actual number of months:
        mcount = ((end.year - start.year) * 12) + (end.month - start.month)

        ## Get the number of days for the period:
        if start.day == 31:
            dcount = 30
        else:
            dcount = ((mcount - 1) * 30) + 30 - start.day + end.day

        ## Get the year count:

# Generated at 2022-06-14 04:43:05.845317
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:43:12.887041
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCC_ACTUAL_ACTUAL_ISDA._calculate_daily_fraction(start=datetime.date(2019, 6, 21), asof=datetime.date(2019, 6, 22), end=datetime.date(2020, 6, 21), freq=Decimal(1)) == Decimal('0.00488839285714286')

# Generated at 2022-06-14 04:43:21.863468
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCC("", set(), set(), lambda start, asof, end, freq: Decimal(10)).calculate_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1), datetime.date(2017, 1, 1)) == Decimal(10)
    assert DCC("", set(), set(), lambda start, asof, end, freq: Decimal(10)).calculate_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 2), datetime.date(2017, 1, 2)) == Decimal(10)

# Generated at 2022-06-14 04:43:29.386364
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) == 0.16666666666666666)
    assert(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)) == 0.16666666666666666)
    assert(dcfc_30_360_us(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)) == 1.0833333333333333)