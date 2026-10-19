

# Generated at 2022-06-14 04:34:57.202560
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert dcfc_30_e_360(start=start, end=end) == 0.20833333333333
    assert round(dcfc_30_e_360(start=datetime.date(2012, 9, 15), end=datetime.date(2013, 9, 15)), 14) == Decimal('1.00078703703704')
    assert round(dcfc_30_e_360(start=datetime.date(2012, 9, 15), end=datetime.date(2013, 9, 30)), 14) == Decimal('1.00277777777778')
    assert round(dcfc_30_e_360(start=datetime.date(2012, 9, 30), end=datetime.date(2013, 9, 15)), 14) == Decimal('0.99861111111111')
    assert round

# Generated at 2022-06-14 04:35:07.960461
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof, ex1_end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof, ex2_end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof, ex3_end = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)

# Generated at 2022-06-14 04:35:12.768565
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    assert round(dcfc_act_365_a(datetime.date(2018, 6, 30), datetime.date(2018, 7, 1), end=datetime.date(2018, 7, 1)), 14) == Decimal('0.0027397260273973')
    assert round(dcfc_act_365_a(datetime.date(2018, 6, 29), datetime.date(2018, 7, 1), end=datetime.date(2018, 7, 1)), 14) == Decimal('0.0054794520547945')
    assert round(dcfc_act_365_a(datetime.date(2019, 6, 30), datetime.date(2019, 7, 1), end=datetime.date(2019, 7, 1)), 14) == Decimal('0.0027397260273973')


# Generated at 2022-06-14 04:35:22.710818
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    """
    Test the calculation of a day count fraction of a given date range.
    """

    # Set up initial dates and frequencies
    start = datetime.date(2008, 7, 7)
    asof = datetime.date(2008, 8, 7)
    end = datetime.date(2008, 8, 7)
    freq = Decimal(2)

    # Create a DCC
    DCC1 = DCC("30/360", "30/360", "30/360", set(), set(), set(), set())
    DCC1.calculate_fraction_method = calculate_fraction

    # Calculate the day count fraction and compare to expected value
    assert DCC1.calculate_fraction(
        start, asof, end, freq
        ) == Decimal(1) / Decimal(4)

   

# Generated at 2022-06-14 04:35:24.461956
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)) == Decimal('0.5245901639')



# Generated at 2022-06-14 04:35:31.460073
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ## Unit tests:
    assert round(dcfc_30_360_us(datetime.date(2007, 5, 31), datetime.date(2008, 6, 30), datetime.date(2008, 6, 30)), 14) == Decimal('1.08333333333333')
    assert round(dcfc_30_360_us(datetime.date(2007, 5, 31), datetime.date(2008, 6, 30), datetime.date(2008, 6, 30)), 14) == Decimal('1.08333333333333')
    assert round(dcfc_30_360_us(datetime.date(2007, 11, 30), datetime.date(2008, 6, 30), datetime.date(2008, 6, 30)), 14) == Decimal('0.66666666666667')

# Generated at 2022-06-14 04:35:42.524196
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    assert round(dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end), 10) == Decimal('0.5245901639')

    ex2_start, ex2_asof, ex2_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 3)

# Generated at 2022-06-14 04:35:49.426145
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    from pypfopt.utilities import month_days
    start_date = datetime.date(2007, 1, 1)
    n_steps = 120
    for d in range(1,32):
        for m in range(1,13):
            end_date = datetime.date(2007 + n_steps // month_days(m), m, d)
            assert (dcfc_30_e_plus_360(start_date, end_date, end_date) - dcfc_30_e_360(start_date, end_date, end_date)) < 0.000001


# Generated at 2022-06-14 04:36:03.450653
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    '''
    Unit test for method coupon of class DCC
    '''
    for i in range(10):
       principal = Money(1, 'USD')
       rate = Decimal(1)
       start = datetime.date(2014,  1,  1)
       asof = datetime.date(2015, 12, 31)
       end = datetime.date(2015, 12, 31)
       freq = Union[int, Decimal]
       eom = Optional[int] = None
       dcc = DCC(name='DCC', altnames=dict, currencies=dict, calculate_fraction_method=DCFC)
       assert dcc.coupon(principal, rate, start, asof, end, freq, eom) == Decimal(0.25)
       break
    else:
       raise RuntimeError

# Generated at 2022-06-14 04:36:16.360731
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    print('Testing function dcfc_30_e_360')
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_e_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:36:49.041186
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    """
    Unit test for function dcfc_act_act_icma.
    """
    ## Define test cases:
    test_cases = [
        # Start date, accrual date, maturity date, expected result
        (datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2), Decimal("0.5245901639")),
        (datetime.date(2019, 3, 2), datetime.date(2020, 3, 2), datetime.date(2021, 3, 2), Decimal("1")),
        (datetime.date(2020, 3, 2), datetime.date(2020, 3, 2), datetime.date(2021, 3, 2), Decimal("0")),
    ]

    ## Iterate over test cases:


# Generated at 2022-06-14 04:36:54.727896
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    # 30/360 ISDA
    start = datetime.date(2017, 1, 1)
    asof = datetime.date(2017, 1, 3)
    end = datetime.date(2017, 1, 31)
    freq = Decimal(1)
    dcc = DCCRegistry["30/360"]
    assert dcc.calculate_daily_fraction(start, asof, end, freq) == Decimal("0.000277777777777778")
    # 30/360 ISMA
    dcc = DCCRegistry["30/360 ISMA"]
    assert dcc.calculate_daily_fraction(start, asof, end, freq) == Decimal("0.000277777777777778")
    # 30E/360

# Generated at 2022-06-14 04:37:05.064973
# Unit test for method find of class DCCRegistryMachinery
def test_DCCRegistryMachinery_find():
    # Arrange
    principal = Money.of(Currencies["USD"], Decimal(1000000), datetime.date.today())
    start = datetime.date(2007, 12, 28)
    end = datetime.date(2008, 2, 28)
    rate = Decimal(0.01)
    dcc = DCCRegistry.find("Act/Act")
    # Act
    result = dcc.calculate_fraction(start, end, end)
    # Assert
    assert round(result, 14) == Decimal('0.16942884946478')


# Generated at 2022-06-14 04:37:16.489569
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert dcfc_30_e_360(datetime.date(2011, 5, 9),  datetime.date(2012, 3, 31),  datetime.date(2012, 3, 31))  == Decimal('0.3375')
    assert dcfc_30_e_360(datetime.date(2011, 3, 15), datetime.date(2012, 3, 31),  datetime.date(2012, 3, 31))  == Decimal('1.30277777777778')
    assert dcfc_30_e_360(datetime.date(2012, 3, 15), datetime.date(2012, 3, 31),  datetime.date(2012, 3, 31))  == Decimal('0.47222222222222')

# Generated at 2022-06-14 04:37:29.437363
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCACT_360.calculate_fraction(datetime.date(2008,7,7), datetime.date(2015,10,6), datetime.date(2021,10,6)) == Decimal('1308/360')
    assert DCCACT_360.calculate_fraction(datetime.date(2008,7,7), datetime.date(2015,10,6), datetime.date(2021,10,6), 4) == Decimal('1308/360')
    assert DCCACT_365_FIXED.calculate_fraction(datetime.date(2008,7,7), datetime.date(2015,10,6), datetime.date(2021,10,6)) == Decimal('1303/365')
    assert DCCACT_365_FIXED.calculate_fraction

# Generated at 2022-06-14 04:37:36.923852
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 2) == Decimal('0.17')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 2) == Decimal('0.17')
    assert round(dcfc_act_act(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 2) == Decimal('1.08')

# Generated at 2022-06-14 04:37:41.980525
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 9, 10), end=datetime.date(2020, 3, 2)), 10)==Decimal('0.5245901639')


# Generated at 2022-06-14 04:37:46.151362
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    start_date, asof_date = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    assert dcfc_nl_365(start_date, asof_date, end=asof_date) == Decimal(0.16986301369863)
    start_date, asof_date = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    assert dcfc_nl_365(start_date, asof_date, end=asof_date) == Decimal(0.16986301369863)
    start_date, asof_date = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)

# Generated at 2022-06-14 04:37:54.168402
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    start = Date(2018, 3, 1)
    asof = Date(2018, 3, 31)
    end = Date(2018, 6, 30)
    dcc_act_360 = DCC(
        name="ACT/360",
        altnames=set(),
        currencies=set(),
        calculate_fraction_method=calculate_fraction_act_360,
    )
    assert dcc_act_360.calculate_fraction(start, asof, end) == Decimal("0.5")

# Generated at 2022-06-14 04:38:06.574526
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    dcc = DCCRegistry["ACT/365"]
    assert dcc.calculate_fraction(datetime.date(2012, 12, 11), datetime.date(2013, 1, 2), datetime.date(2013, 1, 2)) == Decimal('0.118082188')
    assert dcc.calculate_fraction(datetime.date(2012, 12, 11), datetime.date(2013, 1, 2), datetime.date(2013, 2, 3)) == Decimal('1.116438356')
    assert dcc.calculate_fraction(datetime.date(2012, 12, 11), datetime.date(2013, 1, 2), datetime.date(2013, 1, 3)) == Decimal('1.118082188')


# Generated at 2022-06-14 04:39:17.390019
# Unit test for method interest of class DCC
def test_DCC_interest():
    Currencies.register("KWD", "Kuwaiti Dinar", "KD", Decimal("1000.000"))
    DCCRegistry.register(
        DCC(
            name="30E/360",
            altnames={"0E/360", "ISMA"},
            currencies={Currencies.KWD},
            calculate_fraction_method=DCF360(periods_method=_periods_method_30E_360),
        )
    )
    assert DCCRegistry.get("30E/360").interest(Money(Decimal('100'),Currencies.KWD),Decimal(0.05),Date(2017,1,1),Date(2018,1,1))==Money(Decimal('5'),Currencies.KWD)


# Generated at 2022-06-14 04:39:19.552958
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    import doctest
    doctest.testmod()



# Generated at 2022-06-14 04:39:30.286268
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    _act = DCC(
        "Actual / actual", set(), _as_ccys({}), lambda s, x, y, z: Decimal(_get_actual_day_count(x, y))
    )

    ## Make sure that we calculate properly for the edge cases:
    assert _act.calculate_daily_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1), datetime.date(2017, 1, 1)) == ZERO
    assert _act.calculate_daily_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 2), datetime.date(2017, 1, 2)) == ONE

# Generated at 2022-06-14 04:39:40.127997
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    #print(ex1_start, ex1_asof, ex1_end)
    #print(ex2_start, ex2_asof, ex2_end)
    #print(ex3_start, ex3_asof, ex3

# Generated at 2022-06-14 04:39:52.963702
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Test function dcfc_30_360_german.
    """
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2008, 2, 29), datetime.date(2009, 5, 31)
    ex6

# Generated at 2022-06-14 04:40:02.404193
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    assert round(dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end), 10) == Decimal('0.5245901639')
test_dcfc_act_act_icma()



# Generated at 2022-06-14 04:40:10.533155
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    start = datetime.date(2017, 10, 18)
    asof = datetime.date(2017, 11, 18)
    end = datetime.date(2018, 1, 18)
    DCC_30E_360 = DCC(name='30E/360', altnames={'ThirtyE360'}, currencies={}, calculate_fraction_method=DCF.ACT_360)
    DCC_30E_360.calculate_fraction(start, asof, end) == Decimal('0.0833333')


# Generated at 2022-06-14 04:40:21.619421
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert isclose(
        [round(dcfc_30_e_plus_360(start=start, asof=asof, end=end), 14) for start, asof, end in pairs],
        [Decimal('0.16666666666667'), Decimal('0.16944444444444'), Decimal('1.08333333333333'), Decimal('1.33333333333333')]
    )
    print("Unit test for function `dcfc_30_e_plus_360(start: Date, asof: Date, end: Date, freq: Optional[Decimal] = None) -> Decimal` passed.")


# Generated at 2022-06-14 04:40:30.998684
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """Tests that the function dcfc_30_360_us works as expected."""
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2007, 12, 28), datetime.date(2009, 2, 28)

    ##

# Generated at 2022-06-14 04:40:36.352091
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 14) == Dec

# Generated at 2022-06-14 04:41:40.358347
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert round(dcfc_act_365_l(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16939890710383')
    assert round(dcfc_act_365_l(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_l(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 14) == Decimal

# Generated at 2022-06-14 04:41:46.986197
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_e_plus_360(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30)), 14) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:41:58.950645
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    import pandas as pd
    import pandas.util.testing as pdt


# Generated at 2022-06-14 04:42:06.789088
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """Tests for function dcfc_30_360_us"""
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Dec

# Generated at 2022-06-14 04:42:19.991919
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Tests the dcfc_30_360_us function.
    """
    assert round(dcfc_30_360_us(start=datetime.date(2005, 1, 1), asof=datetime.date(2005, 1, 31), end=datetime.date(2005, 1, 31)), 14) == Decimal('0.08333333333333')
    assert round(dcfc_30_360_us(start=datetime.date(2005, 1, 1), asof=datetime.date(2005, 2, 1), end=datetime.date(2005, 2, 1)), 14) == Decimal('0.08333333333333')

# Generated at 2022-06-14 04:42:29.687358
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    start = Date(2019, 4, 4)
    asof = Date(2019, 5, 6)
    end = Date(2019, 5, 7)
    assert round(dcfc_30_360_us(start=start, asof=asof, end=end), 14) == Decimal('0.097222222222222')

    start = Date(2019, 4, 30)
    asof = Date(2019, 5, 30)
    end = Date(2019, 6, 30)
    assert round(dcfc_30_360_us(start=start, asof=asof, end=end), 14) == Decimal('1.0000000000000000')

    start = Date(2019, 4, 30)
    asof = Date(2019, 5, 31)
    end = Date(2019, 6, 30)
    assert round

# Generated at 2022-06-14 04:42:36.262943
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCs["ACT/360"].calculate_fraction(
        start = datetime.date(2018,  1,  1),
        asof = datetime.date(2018,  3, 31),
        end = datetime.date(2018,  3, 31),
        freq = None
    ) == Decimal('0.08333333')
    assert DCCs["ACT/365"].calculate_fraction(
        start = datetime.date(2018,  1,  1),
        asof = datetime.date(2018,  3, 31),
        end = datetime.date(2018,  3, 31),
        freq = None
    ) == Decimal('0.08767123')

# Generated at 2022-06-14 04:42:45.711590
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194')

# Generated at 2022-06-14 04:42:54.114258
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 14) == Dec

# Generated at 2022-06-14 04:43:05.083872
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    ex3_start = datetime.date(2007, 10, 31)
    ex3_asof = datetime.date(2008, 11, 30)
    ex4_start = datetime.date(2008, 2, 1)
    ex4_asof = datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:44:13.808633
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    con = DCC(name="TEST",
              altnames=set(),
              currencies=set(),
              calculate_fraction_method=lambda start, asof, end, freq: ONE)

    assert con.calculate_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1), datetime.date(2017, 2, 1)) == ONE
    assert con.calculate_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 2, 1), datetime.date(2017, 3, 1)) == ONE

    assert con.calculate_fraction(datetime.date(2016, 2, 28), datetime.date(2016, 2, 28), datetime.date(2016, 3, 1)) == ONE