

# Generated at 2022-06-14 04:35:17.876497
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    import datetime
    from decimal import Decimal
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:35:20.733732
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    print(round(dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end), 10))

# Generated at 2022-06-14 04:35:25.720536
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478')
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    assert round(dcfc_act_act(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.17216108990194')
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime

# Generated at 2022-06-14 04:35:30.211627
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert(round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478'))
    assert(round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194'))

# Generated at 2022-06-14 04:35:40.484627
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:35:49.930725
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert round(dcfc_act_365_l(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16939890710383')
    assert round(dcfc_act_365_l(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_l(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 14) == Decimal

# Generated at 2022-06-14 04:36:03.665767
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_e_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:36:16.621536
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ##============================================
    ## Example 1
    ##============================================
    ex1_start = datetime.date(2016, 2, 29)
    ex1_asof = datetime.date(2016, 3, 1)
    ex1_end = datetime.date(2016, 3, 1)

    assert ex1_start.day == 29
    assert ex1_asof.day == 1
    assert ex1_end.day == 1

    ex1_nod = dcfc_30_360_us(ex1_start, ex1_asof, ex1_end)
    assert ex1_nod == Decimal(1) / Decimal(360)

    ##============================================
    ## Example 2
    ##============================================
    ex2_start = datetime.date(2016, 2, 29)
    ex2_asof = dat

# Generated at 2022-06-14 04:36:28.483266
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)

    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)

    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)

    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)

    assert dcfc_act_365_a(ex1_start, ex1_asof, ex1_asof) == Decimal('0.16986301369863')
    assert dcfc_act

# Generated at 2022-06-14 04:36:38.824372
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360(): 
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:37:16.271034
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(
        start=datetime.date(2020, 2, 28),
        asof=datetime.date(2020, 3, 1),
        end=datetime.date(2020, 3, 1),
    ), 14) == round(Decimal('0.0055555555555556'), 14)

    assert round(dcfc_30_360_isda(
        start=datetime.date(2020, 2, 29),
        asof=datetime.date(2020, 3, 1),
        end=datetime.date(2020, 3, 1),
    ), 14) == round(Decimal('0.0083333333333333'), 14)


# Generated at 2022-06-14 04:37:22.623383
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    eps = 1e-8
    func = dcfc_act_365_l
    assert (func(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) - 0.16939890710383) < eps
    assert (func(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) - 0.17213114754098) < eps
    assert (func(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)) - 1.08196721311475) < eps

# Generated at 2022-06-14 04:37:23.410940
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    pass



# Generated at 2022-06-14 04:37:34.350948
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    print("DCC.calculate_daily_fraction")
    dcc = DCC("a", {"b", "c"}, {Currencies["USD"]}, lambda s, a, e, f: Decimal('1.0'))
    assert dcc.calculate_daily_fraction(datetime.date(2013, 4, 6), datetime.date(2013, 4, 6), datetime.date(2013, 4, 6)) == Decimal('1.0')
    assert dcc.calculate_daily_fraction(datetime.date(2013, 4, 6), datetime.date(2013, 4, 7), datetime.date(2013, 4, 6)) == Decimal('0.0')

# Generated at 2022-06-14 04:37:43.704910
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    # Initialize start date, as of date, and end date
    start = datetime.date(2018, 10, 16)
    asof = datetime.date(2018, 10, 20)
    end = datetime.date(2018, 10, 20)

    # Initialize DCC object
    dcc = DCC("DCC", {"DCC"}, set(), lambda s, a, e, f: (e - a).days)

    # Check calculate_fraction output
    assert dcc.calculate_fraction(start, asof, end) == (end - asof).days

# Generated at 2022-06-14 04:37:55.917187
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:38:08.079622
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_e_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:38:21.434438
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478')
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    assert round(dcfc_act_act(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.17216108990194')
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime

# Generated at 2022-06-14 04:38:29.239087
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    from datetime import date

    ex1_start, ex1_asof = date(2019, 1, 31), date(2019, 3, 28)
    ex2_start, ex2_asof = date(2019, 1, 31), date(2019, 3, 29)
    ex3_start, ex3_asof = date(2019, 1, 31), date(2019, 3, 31)
    ex4_start, ex4_asof = date(2019, 2, 28), date(2019, 3, 28)
    ex5_start, ex5_asof = date(2019, 2, 28), date(2019, 3, 29)
    ex6_start, ex6_asof = date(2019, 2, 28), date(2019, 3, 31)

# Generated at 2022-06-14 04:38:42.686375
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_isda(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_isda(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:39:20.581399
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)==Decimal('0.16666666666667')

# Generated at 2022-06-14 04:39:31.972398
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    ###
    DCC_calculate_fraction=DCC('name','altnames','currencies',_actual_365_fraction)
    start=datetime.date(2019, 1, 1)
    asof=datetime.date(2019, 1, 1)
    end=datetime.date(2019, 1, 1)
    assert DCC_calculate_fraction.calculate_fraction(start,asof,end) == 0

###
    start=datetime.date(2019, 1, 1)
    asof=datetime.date(2019, 1, 2)
    end=datetime.date(2019, 1, 2)
    assert DCC_calculate_fraction.calculate_fraction(start,asof,end) == 1



# Generated at 2022-06-14 04:39:36.852381
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    principal = Money.of(Currencies['USD'], Decimal(1000000), datetime.date.today())
    start = datetime.date(2007, 12, 28)
    end = datetime.date(2008, 2, 28)
    rate = Decimal(0.01)
    assert True, 'Example-1: Act/Act'
    dcc = DCCRegistry.find('Act/Act')
    assert round(dcc.calculate_fraction(start, end, end), 14) == Decimal('0.16942884946478')
    assert dcc.interest(principal, rate, start, end, end).qty == Decimal('1694.29')
    assert dcc.interest(principal, rate, end, start, start).qty == Decimal('0.00')

# Generated at 2022-06-14 04:39:49.693696
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof, ex1_end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof, ex2_end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)

    assert dcfc_act_act(ex1_start, ex1_asof, ex1_end) == Decimal('0.16942884946478')
    assert dcfc_act_act(ex2_start, ex2_asof, ex2_end) == Decimal('0.17216108990194')



# Generated at 2022-06-14 04:40:02.228443
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    '''
    Computes the day count fraction for "Act/Act (ICMA)" convention.

    :param start: The start date of the period.
    :param asof: The date which the day count fraction to be calculated as of.
    :param end: The end date of the period (a.k.a. termination date).
    :return: Day count fraction.

    >>> ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    >>> round(dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end), 10)
    Decimal('0.5245901639')
    '''
    



# Generated at 2022-06-14 04:40:14.571136
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof) == Decimal('0.16666666666667')
    assert dcfc_30_360_us

# Generated at 2022-06-14 04:40:20.269550
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    assert DCC("ACT/365", {"ACT/365"}, set(), day_count_fraction_method).coupon("100", "0.05", "2012-06-01", "2012-06-05", "2012-07-01") == Money("2.04")  # pylint: disable=no-member

# Generated at 2022-06-14 04:40:28.002210
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    dcc = DCC('name', set(), set(), lambda start, asof, end, freq: Decimal(1))
    assert dcc.calculate_daily_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1), datetime.date(2017, 1, 1)) == Decimal(0)
    assert dcc.calculate_daily_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 2), datetime.date(2017, 1, 2)) == Decimal(1)


# Generated at 2022-06-14 04:40:32.229476
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    dcc = DCC('name', {'altnames'}, {'currencies'}, DCCRegistry.ACT_360)
    dcc.calculate_fraction(datetime.date(2017,4,10), datetime.date(2017,4,15), datetime.date(2017,4,15))


# Generated at 2022-06-14 04:40:44.136693
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert dcfc_30_e_360(datetime.date(2017, 2, 28),
                         datetime.date(2017, 3, 31),
                         datetime.date(2017, 3, 31)) == Decimal('0.08333333333333')
    assert dcfc_30_e_360(datetime.date(2017, 1, 31),
                         datetime.date(2017, 2, 28),
                         datetime.date(2017, 2, 28)) == Decimal('0.09722222222222')
    assert dcfc_30_e_360(datetime.date(2016, 12, 30),
                         datetime.date(2017, 1, 31),
                         datetime.date(2017, 1, 31)) == Decimal('0.10555555555556')
    assert dcfc_30_e_

# Generated at 2022-06-14 04:42:28.777724
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert dcfc_30_e_plus_360(Date(1,1,1), Date(1,1,1), Date(1,1,1)) == 0
    assert dcfc_30_e_plus_360(Date(1,1,1), Date(1,1,2), Date(1,1,1)) == Decimal(1/360)
    assert dcfc_30_e_plus_360(Date(1,1,1), Date(1,2,1), Date(1,1,1)) == Decimal(30/360)
    assert dcfc_30_e_plus_360(Date(1,1,1), Date(1,2,2), Date(1,1,1)) == Decimal(31/360)

# Generated at 2022-06-14 04:42:39.822400
# Unit test for method interest of class DCC
def test_DCC_interest():
    # Test 1
    principal = Money(100.00, Currencies.USD)
    rate = Decimal(0.03)
    start = datetime.date(2018, 1, 1)
    asof = datetime.date(2018, 2, 1)
    end = datetime.date(2019, 1, 1)
    freq = Decimal(1)
    result = DCC.interest(principal, rate, start, asof, end, freq)
    print('interest:', result)
    assert result.amount == Decimal('3.00')
    assert result.currency == Currencies.USD
    # Test 2
    principal = Money(100.00, Currencies.USD)
    rate = Decimal(0.03)
    start = datetime.date(2017, 7, 1)

# Generated at 2022-06-14 04:42:48.018045
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 14) == Dec

# Generated at 2022-06-14 04:43:00.079013
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    # Testing of function dcfc_act_act_icma
    assert testhelp.close(dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 5, 8), datetime.date(2019, 8, 16), freq=Decimal('4')), Decimal('0.182795698924731'))
    assert testhelp.close(dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 5, 8), datetime.date(2019, 8, 16), freq=Decimal('2')), Decimal('0.365604116370987'))

# Generated at 2022-06-14 04:43:10.370744
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)

# Generated at 2022-06-14 04:43:20.414827
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert round(dcfc_act_365_l(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14) == Decimal('0.16939890710383')
    assert round(dcfc_act_365_l(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_l(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14) == Decimal('1.08196721311475')

# Generated at 2022-06-14 04:43:24.351113
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    dt_start = datetime.date(2007, 12, 31)
    dt_asof = datetime.date(2008, 2, 29)
    assert dcfc_30_360_german(dt_start, dt_asof, dt_asof) == Decimal("0.18055555555556")

# Generated at 2022-06-14 04:43:28.135196
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    from test_dcf import test_dcf
    test_dcf(lambda start, asof, freq: dcfc_30_e_360(start, asof, asof, freq), "dcfc_30_e_360")


# Generated at 2022-06-14 04:43:34.572900
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_365_l(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16939890710383')

# Generated at 2022-06-14 04:43:36.573554
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert round(dcfc_act_365_l(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28),
                                end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16939890710383')
# Unit tests.