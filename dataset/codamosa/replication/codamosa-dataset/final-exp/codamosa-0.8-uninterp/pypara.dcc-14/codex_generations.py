

# Generated at 2022-06-14 04:35:06.368740
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    """
    Tests the calculate_daily_fraction method of class DCC.
    """
    # TODO: This unit test should be moved under a .tests module.
    #
    #
    # Get the Act/Act convention:
    aa = DCCRegistry["Act/Act"]

    # Tests for daily fraction between two different years:
    assert aa.calculate_daily_fraction(datetime.date(2016, 8, 1), datetime.date(2016, 8, 1), datetime.date(2016, 8, 2), Decimal(1)) == ONE
    assert aa.calculate_daily_fraction(datetime.date(2016, 8, 1), datetime.date(2016, 8, 1), datetime.date(2016, 8, 2), Decimal(1)) == ONE
    assert aa.calcul

# Generated at 2022-06-14 04:35:18.510489
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    ## Create a DCC:
    dcc = DCC("AAA", set(), set(), lambda s, a, e, f: Decimal("0.01"))

    ## Calculate fraction:
    assert dcc.calculate_fraction(datetime.date(2014, 1, 1), datetime.date(2014, 1, 2), datetime.date(2014, 1, 3)) == Decimal("0.01")
    assert dcc.calculate_fraction(datetime.date(2014, 1, 1), datetime.date(2014, 1, 2), datetime.date(2014, 1, 3), 1) == Decimal("0.01")

    ## Calculate fraction with invalid dates:

# Generated at 2022-06-14 04:35:30.642646
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCRegistry['30/360'].calculate_fraction(datetime.date(2010, 1, 1), datetime.date(2010, 1, 1), datetime.date(2010, 1, 31)) == 0
    assert DCCRegistry['30/360'].calculate_fraction(datetime.date(2010, 1, 1), datetime.date(2010, 2, 1), datetime.date(2010, 3, 1)) == Decimal('0.086')
    assert DCCRegistry['30/360'].calculate_fraction(datetime.date(2010, 1, 1), datetime.date(2010, 2, 1), datetime.date(2010, 3, 15)) == Decimal('0.117')

# Generated at 2022-06-14 04:35:38.944221
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    """Unit test for function: dcfc_30_360_isda"""
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_isda(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:35:44.335495
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert round(dcfc_30_360_isda(start=datetime.date(2007,12,28), asof=datetime.date(2008,2,28), end=datetime.date(2008,2,28)),14) == Decimal('0.16666666666667'), "dcfc_30_360_isda 1 failed"
    assert round(dcfc_30_360_isda(start=datetime.date(2007,12,28), asof=datetime.date(2008,2,29), end=datetime.date(2008,2,29)),14) == Decimal('0.16944444444444'), "dcfc_30_360_isda 2 failed"

# Generated at 2022-06-14 04:35:48.682567
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)

# Generated at 2022-06-14 04:36:01.969012
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Performs unit test.

    :return: None.
    """
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)


# Generated at 2022-06-14 04:36:08.465593
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(datetime.date(2012, 9, 1), datetime.date(2012, 10, 1), datetime.date(2012, 10, 1)), 14) == Decimal('0.0833333333333333')
    assert round(dcfc_30_360_us(datetime.date(2012, 9, 1), datetime.date(2012, 9, 30), datetime.date(2012, 9, 30)), 14) == Decimal('0.0833333333333333')
    assert round(dcfc_30_360_us(datetime.date(2012, 9, 30), datetime.date(2012, 12, 31), datetime.date(2012, 12, 31)), 14) == Decimal('0.333333333333333')

# Generated at 2022-06-14 04:36:16.513177
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert dcfc_30_e_plus_360(datetime.date(2007,12,28), datetime.date(2008,2,28),datetime.date(2008,2,28))  == Decimal('0.16666666666667')
    assert dcfc_30_e_plus_360(datetime.date(2007,12,28), datetime.date(2008,2,29),datetime.date(2008,2,29))  == Decimal('0.16944444444444')
    assert dcfc_30_e_plus_360(datetime.date(2007,10,31), datetime.date(2008,11,30),datetime.date(2008,11,30)) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:36:28.445522
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCRegistry.__default_registry__.get_instance(DCCRegistry.__default_registry__.ACTUAL_ACTUAL).calculate_fraction(
        Date(2012,1,1), Date(2012,1,31), Date(2012,2,1)
    ) == Decimal('31') / Decimal('31')
    assert DCCRegistry.__default_registry__.get_instance(DCCRegistry.__default_registry__.ACTUAL_ACTUAL).calculate_fraction(
        Date(2012,1,1), Date(2012,2,1), Date(2012,2,29)
    ) == Decimal('28') / Decimal('59')

# Generated at 2022-06-14 04:37:16.041813
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28))
    dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29))
    dcfc_30_e_plus_360(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30))
    dcfc_30_e_plus_360(datetime.date(2008, 2, 1), datetime.date(2009, 5, 31), datetime.date(2009, 5, 31))



# Generated at 2022-06-14 04:37:28.838899
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')
    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.17216108990194')

# Generated at 2022-06-14 04:37:39.066278
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    # Arrange
    dcc0 = DCC("NAME", {"N", "NA", "NAM"}, {Currencies["USD"], Currencies["GBP"]}, _dcfc_act_act)
    dcc1 = DCC("NAME", {"N", "NA", "NAM"}, {Currencies["USD"], Currencies["GBP"]}, _dcfc_act_act)
    sut = DCCRegistryMachinery()
    # Act
    sut.register(dcc0)
    # Assert
    assert sut._is_registered("NAME")
    # Act
    sut.register(dcc1)
    # Assert
    assert sut._is_registered("NAME")



# Generated at 2022-06-14 04:37:50.837977
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    assert isclose(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)),
                   Decimal('0.16942884946478'))
    assert isclose(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)),
                   Decimal('0.17216108990194'))
    assert isclose(dcfc_act_act(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)),
                   Decimal('1.08243131970956'))

# Generated at 2022-06-14 04:38:04.597540
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    """
    Exact dcfc_30_e_plus_360 tests
    """
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:38:12.800146
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    """
    Unit test for method calculate_daily_fraction of class DCC
    """
    import dtcc.dcc as dcc
    # Initialize required variables
    start=datetime.date(2017, 8, 8)
    asof=datetime.date(2017, 8, 10)
    end=datetime.date(2017, 8, 12)
    freq=Decimal(0.5)
    # Execute the code to be tested
    result = DCC._make(['', '', '', dcc.act_360]).calculate_daily_fraction(start, asof, end, freq)
    # Verify the result

# Generated at 2022-06-14 04:38:15.335367
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert round(dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)), 10) == Decimal('0.5245901639')
# Test suite for function dcfc_act_act_icma

# Generated at 2022-06-14 04:38:18.568692
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    # TODO: Add unit test for function dcfc_act_act
    pass



# Generated at 2022-06-14 04:38:30.750365
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    ex5_start, ex5_asof = datetime.date(2008, 11, 30), datetime.date(2010, 2, 28)


# Generated at 2022-06-14 04:38:43.428749
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    print('Testing function dcfc_30_360_german...')
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14)

# Generated at 2022-06-14 04:39:22.731727
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    start_date = datetime.datetime(2020, 11, 10)
    end_date = datetime.datetime(2021, 11, 10)
    as_of_date = datetime.datetime(2020, 11, 19)
    dcc = DCC('ACT/360', None, None, None)
    assert dcc.calculate_fraction(start_date, as_of_date, end_date, None) == Decimal(0.027)


# Generated at 2022-06-14 04:39:28.756010
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:39:34.172868
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    from dateutil import parser
    from dateutil.tz import tzlocal
    from .monetary import Money

    start = parser.parse("2019-01-01 00:00:00", tzinfos=tzlocal())
    asof = parser.parse("2019-01-01 00:00:00", tzinfos=tzlocal())
    end = parser.parse("2019-01-31 00:00:00", tzinfos=tzlocal())
    freq = 1

    principal = Money("USD 1,000")
    rate = 0.1

    dcc_name = "ACT/360"
    dcc = DCCRegistry[dcc_name]

    ## Calculate the accrued interest
    result = dcc.interest(principal, rate, start, asof, end, freq)

# Generated at 2022-06-14 04:39:45.166180
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    dcc = DCCRegistry.find("Act/Act")
    start = datetime.date(2007, 12, 28)
    asof = datetime.date(2008, 2, 28)
    end = datetime.date(2008, 2, 28)
    freq = None
    assert dcc.calculate_fraction(start, asof, end, freq) == dcc.calculate_fraction_method(start, asof, end, freq)
    assert dcc.calculate_fraction_method(start, asof, end, freq) == dcfc_act_act(start, asof, end, freq)
    assert round(dcfc_act_act(start=start, asof=asof, end=end), 14) == Decimal('0.16942884946478')

# Generated at 2022-06-14 04:39:56.033434
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    start, asof, end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)
    tolerance = Decimal("0.0000000000000000")
    assert (dcfc_30_360_german(start, asof, end) - Decimal("0.16666666666667")).abs() < tolerance
    start, asof, end = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)
    tolerance = Decimal("0.0000000000000000")
    assert (dcfc_30_360_german(start, asof, end) - Decimal("0.16944444444444")).abs() < tolerance

# Generated at 2022-06-14 04:40:06.302804
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Unit test for function dcfc_30_360_german
    """
    # Check value of function:
    assert round(dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008,  2, 28), end=datetime.date(2008,  2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008,  2, 29), end=datetime.date(2008,  2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2022-06-14 04:40:19.190235
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert (
        round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) ==
        Decimal('0.16666666666667')
    )
    assert (
        round(dcfc_30_e_360(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) ==
        Decimal('0.16944444444444')
    )

# Generated at 2022-06-14 04:40:22.180581
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    # Test example
    assert round(dcfc_act_act_icma(start=datetime.date(2019, 3, 2), asof=datetime.date(2019, 9, 10),
                                   end=datetime.date(2020, 3, 2), freq=Decimal(2)), 10) == Decimal('0.5245901639')



# Generated at 2022-06-14 04:40:31.352957
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    assert dcfc_act_365_a(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == 0.16986301369863
    assert dcfc_act_365_a(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) == 0.17213114754098
    assert dcfc_act_365_a(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)) == 1.08196721311475

# Generated at 2022-06-14 04:40:44.098973
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    from .currencies import CUR
    from .enums import PeriodType
    from .numbers import one_half, one_third

    assert DCC.ACT_ACT.calculate_fraction(
        start=Date(2017, 1, 1),
        asof=Date(2017, 6, 30),
        end=Date(2017, 12, 31),
    ) == Decimal('0.5')
    assert DCC.ACT_ACT.calculate_daily_fraction(
        start=Date(2017, 1, 1),
        asof=Date(2017, 6, 30),
        end=Date(2017, 12, 31),
    ) == Decimal('0.5') / Decimal('365')