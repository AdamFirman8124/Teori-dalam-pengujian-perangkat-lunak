

# Generated at 2022-06-14 04:34:53.791570
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)==Decimal('0.16942884946478')

# Generated at 2022-06-14 04:34:58.253991
# Unit test for method calculate_fraction of class DCC

# Generated at 2022-06-14 04:35:04.845018
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    start = datetime.date(2019, 5, 20)
    asof = datetime.date(2019, 5, 24)
    end = datetime.date(2019, 5, 25)
    freq = Decimal('1')
    result = DCC("name", {"altname"}, {"currency"}, None).calculate_fraction(start, asof, end, freq)
    assert result == Decimal('0.25')



# Generated at 2022-06-14 04:35:09.586844
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    print(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)))
    print(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 28)))
    print(dcfc_act_act(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 2, 28)))
    print(dcfc_act_act(datetime.date(2008, 2, 1), datetime.date(2009, 5, 31), datetime.date(2008, 2, 28)))


# Generated at 2022-06-14 04:35:17.337023
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(datetime.date(2007, 12, 28), datetime.date(2009, 5, 31), datetime.date(2009, 5, 31)), 14) == Decimal("1.33333333333333")
    assert round(dcfc_30_360_us(datetime.date(2007, 12, 28), datetime.date(2009, 5, 31), datetime.date(2009, 5, 31)), 14) == Decimal("1.33333333333333")
    assert round(dcfc_30_360_us(datetime.date(2007, 12, 28), datetime.date(2009, 6, 30), datetime.date(2009, 6, 30)), 14) == Decimal("1.33333333333333")

# Generated at 2022-06-14 04:35:21.478350
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == Decimal('0.16942884946478')
    assert dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) == Decimal('0.17216108990194')
    assert dcfc_act_act(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)) == Decimal('1.08243131970956')

# Generated at 2022-06-14 04:35:28.674384
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    ## Setup
    DCC = DCCRegistry['B30/360']
    start = Date(2017,1,1)
    asof = Date(2017,1,2)
    end = Date(2017,1,3)
    freq = Decimal(1)
    # Test
    dcc = DCC(start,asof,end,freq)
    # Assert
    assert dcc == Decimal('0.00277777777777778')


# Generated at 2022-06-14 04:35:38.660808
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194')

# Generated at 2022-06-14 04:35:50.684458
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) ==Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) ==Decimal('0.17216108990194')
    assert round(dcfc_act_act(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) ==Decimal('1.08243131970956')

# Generated at 2022-06-14 04:35:58.797933
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert abs((0.16666666666667 - dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28))).tovalue()) < 0.00000000000001



# Generated at 2022-06-14 04:36:28.004676
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    res = DCC.coupon(Money(1000, 'RUB'), 
                     Decimal(0.12), 
                     Date(datetime(2018, 4, 23)), 
                     Date(datetime(2018, 6, 23)), 
                     Date(datetime(2018, 7, 1)), 
                     2)
    assert res.amount == 16.0
    assert res.currency.code == 'RUB'


# Generated at 2022-06-14 04:36:41.637200
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert abs(dcfc_30_360_us(datetime.date(1999, 12, 31),datetime.date(2000, 1, 31)) - Decimal('0.1666666666666666666666666667')) < 0.000000001
    assert abs(dcfc_30_360_us(datetime.date(1999, 12, 31),datetime.date(2000, 2, 29)) - Decimal('0.16944444444444444444444444444')) < 0.000000001
    assert abs(dcfc_30_360_us(datetime.date(1999, 12, 30),datetime.date(2000, 1, 31)) - Decimal('0.1666666666666666666666666667')) < 0.000000001

# Generated at 2022-06-14 04:36:46.514783
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    assert(DCCRegistry.resolve("ACT/ACT").coupon(Money(100, "USD"), 0.1, datetime.date(2019, 5, 20), datetime.date(2019, 5, 30), datetime.date(2019, 6, 1), 2)) == Money(1.439, "USD")
    assert(DCCRegistry.resolve("ACT/ACT").coupon(Money(100, "USD"), 0.1, datetime.date(2019, 5, 20), datetime.date(2019, 5, 30), datetime.date(2019, 6, 1), 2)) == Money(1.439, "USD")

# Generated at 2022-06-14 04:36:58.558547
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:37:12.460078
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert dcfc_act_365_l(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) == Decimal('0.16939890710383')
    assert dcfc_act_365_l(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)) == Decimal('0.17213114754098')
    assert dcfc_act_365_l(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)) == Decimal('1.08196721311475')

# Generated at 2022-06-14 04:37:25.298266
# Unit test for method find of class DCCRegistryMachinery
def test_DCCRegistryMachinery_find():
    if DCCRegistry.find("test") is None:
        raise RuntimeError("Unexpected")
    if DCCRegistry.find("test").name != "test":
        raise RuntimeError("Unexpected")
    if DCCRegistry.find("test-test") is not None:
        raise RuntimeError("Unexpected")
    if DCCRegistry.find("TEST") is None:
        raise RuntimeError("Unexpected")
    if DCCRegistry.find("TEST").name != "test":
        raise RuntimeError("Unexpected")
    if DCCRegistry.find("TEST-TEST") is not None:
        raise RuntimeError("Unexpected")
    if DCCRegistry.find("TEST - TEST") is None:
        raise RuntimeError("Unexpected")

# Generated at 2022-06-14 04:37:29.647207
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert round(dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_german(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 14) == Dec

# Generated at 2022-06-14 04:37:34.035230
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Run unit test for the dcfc_30_360_german function.
    """
    assert math.isclose(dcfc_30_360_german(datetime.date(2020, 1, 1), datetime.date(2020, 1, 1), datetime.date(2020, 1, 1)), 0.0)
    assert math.isclose(dcfc_30_360_german(datetime.date(2020, 2, 29), datetime.date(2020, 2, 29), datetime.date(2020, 2, 29)), 1.0)
    assert math.isclose(dcfc_30_360_german(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31), datetime.date(2020, 12, 31)), 11.9722222222)

# Generated at 2022-06-14 04:37:38.227804
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    assert round(dcfc_nl_365(datetime.date(2016, 1, 1), datetime.date(2016, 1, 1)), 14) == Decimal(0)
    assert round(dcfc_nl_365(datetime.date(2016, 1, 1), datetime.date(2016, 2, 1)), 14) == Decimal(1 / 365.)
    assert round(dcfc_nl_365(datetime.date(2016, 12, 31), datetime.date(2017, 1, 1)), 14) == Decimal(0)
    assert round(dcfc_nl_365(datetime.date(2016, 1, 1), datetime.date(2017, 1, 1)), 14) == Decimal(1)

# Generated at 2022-06-14 04:37:50.288731
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == 0.16942884946478
    assert dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) == 0.17216108990194
    assert dcfc_act_act(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)) == 1.08243131970956

# Generated at 2022-06-14 04:39:17.402406
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    start = datetime.date(2019, 2, 28)
    asof =  datetime.date(2019, 3, 31)
    dcfc = dcfc_30_e_plus_360(start, asof)

# Generated at 2022-06-14 04:39:22.540410
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    assert round(dcfc_act_365_a(start = datetime.date(2007,12,28), asof = datetime.date(2008,2,28), end = datetime.date(2008,2,28)),14) == Decimal('0.16986301369863')
    assert round(dcfc_act_365_a(start = datetime.date(2007,12,28), asof = datetime.date(2008,2,29), end = datetime.date(2008,2,29)),14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_a(start = datetime.date(2007,10,31), asof = datetime.date(2008,11,30), end = datetime.date(2008,11,30)),14) == Dec

# Generated at 2022-06-14 04:39:35.243968
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert dcfc_30_360_isda(datetime.date(2017, 4, 15), datetime.date(2018, 6, 30), datetime.date(2018, 6, 30)) == Decimal("0.166666666666666666666667")
    assert dcfc_30_360_isda(datetime.date(2017, 9, 30), datetime.date(2018, 6, 30), datetime.date(2018, 6, 30)) == Decimal("0.833333333333333333333333")
    assert dcfc_30_360_isda(datetime.date(2017, 9, 30), datetime.date(2017, 12, 31), datetime.date(2017, 12, 31)) == Decimal("0.333333333333333333333333")

# Generated at 2022-06-14 04:39:44.500907
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2009, 2, 28), datetime.date(2009, 3, 31)
    ex6_start, ex6_asof = datetime.date(2009, 2, 28), dat

# Generated at 2022-06-14 04:39:55.596688
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(datetime.date(2014,11,30), datetime.date(2015,6,1), datetime.date(2015,6,1)),14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_plus_360(datetime.date(2014,12,31), datetime.date(2015,6,1), datetime.date(2015,6,1)),14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_plus_360(datetime.date(2015,1,31), datetime.date(2015,6,1), datetime.date(2015,6,1)),14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:40:06.265268
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert(round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478'))

# Generated at 2022-06-14 04:40:19.138339
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    from dateutil.relativedelta import relativedelta
    from datetime import date
    from math import isclose

    dcc = DCC(
        name="TestDCC",
        altnames=set(["t1", "t2"]),
        currencies={Currencies["USD"]},
        calculate_fraction_method=(lambda start, asof, end, freq: (asof - start).days / (end - start).days)
    )

    # Test for a range of dates
    s = date(2017, 1, 1)
    e = date(2017, 3, 1)
    dcf = dcc.calculate_daily_fraction(s, e, e)
    assert isclose(dcf, 2 / 29, abs_tol=0.001)

    # Test for just a single day

# Generated at 2022-06-14 04:40:28.044375
# Unit test for method interest of class DCC
def test_DCC_interest():
    from .monetary import Money
    import datetime
    from decimal import Decimal
    start = datetime.date(2020, 1, 1)
    end = datetime.date(2021, 1, 1)
    principal = Money(100, "USD")
    rate = Decimal(.02)
    dcc_actual_365 = DCC(name='DCC_ACTUAL_365', altnames={'ACT/365', 'ACT/365'}, currencies=set(), calculate_fraction_method=calculate_fraction_method)
    assert principal.amount*rate*dcc_actual_365.calculate_fraction(start, end, end) == 2



# Generated at 2022-06-14 04:40:34.615612
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:40:44.563309
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof) == Decimal('0.16666666666667')
    assert dcfc_30_e_360

# Generated at 2022-06-14 04:42:44.429467
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert round(dcfc_30_360_german(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_german(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_german(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:42:53.459379
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert round(dcfc_30_360_german(datetime.date(2010, 5, 12), datetime.date(2011, 2, 1), datetime.date(2011, 2, 1)), 14) == Decimal('0.28472222222222')
    assert round(dcfc_30_360_german(datetime.date(2010, 5, 12), datetime.date(2010, 12, 30), datetime.date(2010, 12, 30)), 14) == Decimal('0.76944444444444')
    assert round(dcfc_30_360_german(datetime.date(2010, 5, 12), datetime.date(2011, 2, 28), datetime.date(2011, 2, 28)), 14) == Decimal('0.79166666666667')

# Generated at 2022-06-14 04:43:04.564512
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) == Decimal('0.16666666666667')
    assert dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)) == Decimal('0.16944444444444')
    assert dcfc_30_360_us(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)) == Decimal('1.08333333333333')
    assert dcfc

# Generated at 2022-06-14 04:43:08.862058
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    assert round(dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16986301369863')
    assert round(dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:43:19.205120
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    from datetime import date
    from decimal import Decimal
    from financepy.products.funding.CurveBuilding.YieldCurveModel import YieldCurveModel
    from financepy.markets.curves.FinDiscountCurveFlat import FinDiscountCurveFlat
    from financepy.markets.curves.FinDiscountCurve import FinDiscountCurveTypes
    
    startDate = date(2019, 9, 30)
    settleDate = date(2019, 10, 4)
    maturityDate = date(2020, 1, 15)

    dayCountType = FinDiscountCurveTypes.DISCOUNT_CURVE_ACT365
    discountCurve = FinDiscountCurveFlat(settledate, 0.05, dayCountType)
    yieldCurve = YieldCurveModel(settledate, discountCurve)
   

# Generated at 2022-06-14 04:43:27.521328
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)  == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:43:32.781562
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert dcfc_30_360_isda(start=datetime.date(2007, 12, 28),
                            asof=datetime.date(2008, 2, 28),
                            end=datetime.date(2008, 2, 28)) == 0.1666666666666667
    assert dcfc_30_360_isda(start=datetime.date(2007, 12, 28),
                            asof=datetime.date(2008, 2, 29),
                            end=datetime.date(2008, 2, 29)) == 0.1694444444444444
    assert dcfc_30_360_isda(start=datetime.date(2007, 10, 31),
                            asof=datetime.date(2008, 11, 30),
                            end=datetime.date(2008, 11, 30)) == 1.

# Generated at 2022-06-14 04:43:42.476883
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    from datetime import date
    from pyxir.portfolio import DCC
    from pyxir.currencies import Currencies

    start = date(2017, 1, 1)
    asof = date(2018, 1, 31)
    end = date(2018, 7, 1)
    dcc = DCC["ACT/365"]

    principal = 1000
    rate = 0.1

    interest = 200
    assert dcc.coupon(principal, rate, start, asof, end, 2, 15) == interest

    interest = 200
    assert dcc.coupon(principal, rate, start, asof, end, 2) == interest

    interest = 200
    assert dcc.coupon(principal * Currencies["USD"], rate, start, asof, end, 2) == interest

    interest = 200

# Generated at 2022-06-14 04:43:51.912781
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:44:01.617654
# Unit test for method calculate_daily_fraction of class DCC