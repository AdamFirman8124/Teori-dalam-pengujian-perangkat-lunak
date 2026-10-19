

# Generated at 2022-06-14 04:34:57.108270
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == dcfc_30EPlus360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28))
    assert dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) == dcfc_30EPlus360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) 

# Generated at 2022-06-14 04:35:07.887778
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert compare_with_expected_value(dcfc_30_e_plus_360(datetime.date(2020,3,31), datetime.date(2020,4,30)), 0.16666666666666666)
    assert compare_with_expected_value(dcfc_30_e_plus_360(datetime.date(2019,2,28), datetime.date(2019,3,31)), 0.16666666666666666)
    assert compare_with_expected_value(dcfc_30_e_plus_360(datetime.date(2018,1,31), datetime.date(2018,2,28)), 0.16666666666666666)

# Generated at 2022-06-14 04:35:16.692547
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    A unit test for the function, dcfc_30_360_us

    :return: None.
    """
    ## Example 1:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex1_dcfc = round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)
    print(ex1_dcfc)
    assert ex1_dcfc == Decimal('0.16666666666667')

    ## Example 2:
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)

# Generated at 2022-06-14 04:35:22.576291
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    cal_DCC = DCC("my_name", {'altName'}, {Currencies.USD}, calculate_fraction_method)
    cal_DCC.calculate_fraction(datetime.date(2017, 8, 8),datetime.date(2018, 8, 8),datetime.date(2019, 8, 8),2) == Decimal("1") 

# Generated at 2022-06-14 04:35:34.615774
# Unit test for method interest of class DCC
def test_DCC_interest():
    ## Checks if dates are provided properly:
    assert DCCRegistry.get("30/360").interest(Money(0), 0.1, datetime.date(2014, 4, 4), datetime.date(2014, 4, 4)) == Money(0)
    assert DCCRegistry.get("30/360").interest(Money(0), 0.1, datetime.date(2014, 4, 6), datetime.date(2014, 4, 5)) == Money(0)
    assert DCCRegistry.get("30/360").interest(Money(1000), 0.1, datetime.date(2014, 4, 5), datetime.date(2014, 4, 4)) == Money(0)
    ## Cool, we can proceed with calculation based on the methodology:

# Generated at 2022-06-14 04:35:41.279305
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    dcf1 = round(dcfc_act_365_l(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)

# Generated at 2022-06-14 04:35:50.026321
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(start=datetime.date(2019, 4, 29), asof=datetime.date(2019, 7, 30), end=datetime.date(2019, 7, 30)), 14) == Decimal('0.083333333333333')
    assert round(dcfc_30_360_us(start=datetime.date(2019, 4, 29), asof=datetime.date(2019, 7, 31), end=datetime.date(2019, 7, 31)), 14) == Decimal('0.083333333333333')

# Generated at 2022-06-14 04:36:03.711490
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.17216108990194')
    assert round(dcfc_act_act(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08243131970956')

# Generated at 2022-06-14 04:36:09.530677
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    # Test 1
    ex_start = datetime.date(2007, 12, 28)
    ex_asof = datetime.date(2008, 2, 28)
    exp_dcfc = Decimal('0.16666666666667')
    act_dcfc = dcfc_30_e_plus_360(ex_start, ex_asof)
    assert exp_dcfc == act_dcfc, "Error: Expected day count fraction: %.14f, got: %.14f" % (exp_dcfc, act_dcfc)

    # Test 2
    ex_start = datetime.date(2007, 12, 28)
    ex_asof = datetime.date(2008, 2, 29)
    exp_dcfc = Decimal('0.16944444444444')
    act

# Generated at 2022-06-14 04:36:23.010299
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    myDCC = DCC ('Actual/365 (Fixed)', {"Actual/365 (Fixed)"}, {'USD', 'GBP'}, _actual_365_fixed)
    assert myDCC.calculate_daily_fraction(datetime.date(2019, 1, 1),
                                          datetime.date(2019, 1, 1),
                                          datetime.date(2019, 1, 2),
                                          Decimal(1)) == ONE
    assert myDCC.calculate_daily_fraction(datetime.date(2019, 1, 1),
                                          datetime.date(2019, 1, 1),
                                          datetime.date(2019, 1, 1),
                                          Decimal(1)) == ZERO

# Generated at 2022-06-14 04:36:58.132824
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:37:00.459939
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    pass



# Generated at 2022-06-14 04:37:07.317839
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert dcfc_30_e_plus_360(start=datetime.date(2016,12,30), asof=datetime.date(2018,2,28), end=datetime.date(2018,2,28)) == 0.16666666666666666



# Generated at 2022-06-14 04:37:19.843975
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    ## Case 1
    ## Case 1.0
    principal = Money(10000, Currencies.USD)
    rate = Decimal(0.1)
    start = datetime.date(2014, 1, 1)
    asof = datetime.date(2015, 12, 31)
    end = datetime.date(2015, 12, 31)
    freq = Decimal(1)
    eom = None
    dcc = DCC("ACT/365", set({"ACT/365"}), set({Currencies.USD}), DCF_ACT_365)
    assert dcc.coupon(principal, rate, start, asof, end, freq, eom) == Money(1000, Currencies.USD)

    ## Case 1.1
    principal = Money(10000, Currencies.USD)

# Generated at 2022-06-14 04:37:31.978817
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start = datetime.date(2007, 12, 28)
    ex2_start = datetime.date(2007, 12, 28)
    ex3_start = datetime.date(2007, 10, 31)
    ex4_start = datetime.date(2008, 2, 1)

    ex1_asof = datetime.date(2008, 2, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    ex3_asof = datetime.date(2008, 11, 30)
    ex4_asof = datetime.date(2009, 5, 31)

    ex1_end = ex1_asof
    ex2_end = ex2_asof
    ex3_end = ex3_asof
    ex4_end = ex4_asof


# Generated at 2022-06-14 04:37:42.654176
# Unit test for method register of class DCCRegistryMachinery

# Generated at 2022-06-14 04:37:50.369853
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    test_start = datetime.date(2015, 3, 31)
    test_asof = datetime.date(2015, 5, 21)
    dcfc = dcfc_30_e_360(test_start, test_asof, test_asof)
    assert dcfc == Decimal('0.17222222222222')
    # TODO:  Check this test



# Generated at 2022-06-14 04:38:02.138651
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCRegistry.get("30/360 PS").calculate_fraction(start=datetime.date(2017, 10, 10),
                                                           asof=datetime.date(2017, 10, 10),
                                                           end=datetime.date(2017, 10, 10)) == Decimal(0)
    assert DCCRegistry.get("30/360 PS").calculate_fraction(start=datetime.date(2017, 10, 10),
                                                           asof=datetime.date(2017, 10, 11),
                                                           end=datetime.date(2017, 10, 11)) == Decimal(1) / Decimal(360)



# Generated at 2022-06-14 04:38:08.757808
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)),14) == \
        Decimal('0.16666666666667')
    assert round(dcfc_30_360_isda(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)),14) == \
        Decimal('0.16944444444444')
    assert round(dcfc_30_360_isda(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)),14) == \
        Decimal('1.08333333333333')

# Generated at 2022-06-14 04:38:19.328747
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    print("\n\nUnit test for method calculate_daily_fraction of class DCC")
    # Define a day count convention
    myDCC = DCC(
        'ACT/360', {'ACT/360', 'ACT360', '30/360 US'}, {Currencies['USD']},
        lambda start, asof, end, freq: _get_actual_day_count(start, asof) / 360
    )

    assert (
        myDCC.calculate_daily_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1), datetime.date(2017, 1, 2)) ==
        Decimal('0')
    )

# Generated at 2022-06-14 04:39:00.223767
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    assert dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)) == Decimal('0.16986301369863')
    assert dcfc_nl_365(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)) == Decimal('0.16986301369863')
    assert dcfc_nl_365(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)) == Decimal('1.08219178082192')
    assert dcfc

# Generated at 2022-06-14 04:39:13.011354
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    """
    Unit test for function dcfc_30_e_plus_360
    """
    import sys

    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    

# Generated at 2022-06-14 04:39:23.966690
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ## Expected values:
    ex1 = Decimal("0.16666666666667")
    ex2 = Decimal("0.16944444444444")
    ex3 = Decimal("1.08333333333333")
    ex4 = Decimal("1.33333333333333")

    ## Get start and asof dates:
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)

    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)

    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)


# Generated at 2022-06-14 04:39:35.795904
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28))) == 0.166666666666667
    assert round(dcfc_30_360_us(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29))) == 0.169444444444444
    assert round(dcfc_30_360_us(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30))) == 1.08333333333333

# Generated at 2022-06-14 04:39:48.366565
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    print(round(dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14))

# Generated at 2022-06-14 04:39:57.735079
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478')

# Generated at 2022-06-14 04:40:07.514779
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    round(test_dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)

# Generated at 2022-06-14 04:40:20.269774
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194')

# Generated at 2022-06-14 04:40:30.336156
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:40:35.931386
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2008, 2, 28), datetime.date(2008, 6, 30)
    ex6_start, ex6_asof = datetime.date(2008, 2, 29), dat

# Generated at 2022-06-14 04:42:13.352578
# Unit test for method find of class DCCRegistryMachinery
def test_DCCRegistryMachinery_find():
    """
    Test Method for DCCRegistryMachinery_find
    """
    assert DCCRegistryMachinery._find_strict({"name": "Act/360"}) == None



# Generated at 2022-06-14 04:42:24.081802
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    fun = dcfc_act_act
    start, asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

    # Bad start and end dates:
    with pytest.raises(ValueError, match="start and end dates must be"):
        fun(start=asof, asof=asof, end=asof)
    with pytest.raises(ValueError, match="start and end dates must be"):
        fun(start=start, asof=start, end=start)

    # Date range:
    assert fun(start=start, asof=asof, end=asof) == Decimal("0.16942884946478")

    # Non-business day:

# Generated at 2022-06-14 04:42:32.523850
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ## Get the new start date, if required:
    if start.day == 31:
        new_start = datetime.date(start.year, start.month, 30)
    asof = datetime.date(2016, 12, 30)
    start = datetime.date(2016, 1, 31)
    (asof.day - start.day) + 30 * (asof.month - start.month) + 360 * (asof.year - start.year)
    nod = (asof.day - start.day) + 30 * (asof.month - start.month) + 360 * (asof.year - start.year)


# Generated at 2022-06-14 04:42:43.199790
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Test cases for the dcfc_30_360_german function:
    """
    # Testcase 1:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex1_nod = dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert ex1_nod == Decimal('0.16666666666667')

    # Testcase 2:
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)

# Generated at 2022-06-14 04:42:52.812759
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    """
    Unit Test for DCC.coupon
    """
    assert DCCRegistry["ACT/ACT"].coupon(Money(1, "USD"), 0.01, datetime.date(2014,  1,  1), datetime.date(2014,  7,  1), datetime.date(2014,  7,  1), 2)==Money(0.005, "USD")
    assert DCCRegistry["ACT/ACT"].coupon(Money(1, "USD"), 0.01, datetime.date(2014,  1,  1), datetime.date(2014,  6, 30), datetime.date(2014,  7,  1), 2)==Money(0.007142857142857143, "USD")

# Generated at 2022-06-14 04:43:04.083863
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    #
    test_date_list = pd.date_range('2010-01-01','2015-12-31').tolist()
    for i in range(len(test_date_list)):
        if i+1<len(test_date_list):
            test_start = test_date_list[i]
            test_asof = test_date_list[i+1]
            if dcfc_30_e_360(test_start, test_asof, test_asof) != ((test_asof-test_start).days/360):
                print("Test failed!")
                print("Given start:", test_start, "Given asof:", test_asof)
                print("Expected result:", ((test_asof-test_start).days/360))

# Generated at 2022-06-14 04:43:15.703096
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    """
    DCC.calculate_daily_fraction(self, start: Date, asof: Date, end: Date, freq: Optional[Decimal] = None) -> Decimal
    """
    #
    # When asof is exactly start or end date
    #

    # _construct_date()
    # _get_actual_day_count()
    # _has_leap_day()
    # _is_last_day_of_month()
    # _last_payment_date()
    # _next_payment_date()
    # Date
    # DCC
    # DCCRegistry
    # Decimal
    # Money
    # ONE
    # ZERO
    # datetime
    # relativedelta()
    #

    from .commons.numbers import ONE, ZERO

# Generated at 2022-06-14 04:43:27.347259
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    from datetime import date
    from decimal import Decimal
    from financepy.finutils.FinDate import FinDate
    from financepy.products.funding.FinDCC import DCC
    from financepy.products.funding.FinDCC import DCCRegistry
    startDate = FinDate(1, 1, 2018)
    endDate = FinDate(1, 1, 2019)
    asofDate = FinDate(1, 1, 2019)
    freq = 2
    actf = DCCRegistry.ACT_365_FIXED.calculate_fraction(startDate, asofDate, endDate, Decimal(freq))
    assert actf == Decimal('0.5')

# Generated at 2022-06-14 04:43:39.677099
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Test that the dcfc_30_360_us function is behaving correctly.
    """
    ## Try a variety of dates:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    ## assert() a correct result

# Generated at 2022-06-14 04:43:50.480598
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == round(Decimal('0.16666666666667'), 14)
    assert round