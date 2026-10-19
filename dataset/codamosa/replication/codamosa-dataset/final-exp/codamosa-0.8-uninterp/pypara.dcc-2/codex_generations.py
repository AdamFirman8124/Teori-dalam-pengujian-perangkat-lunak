

# Generated at 2022-06-14 04:35:02.723912
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:35:13.903529
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    assert (round(dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end), 10) == Decimal('0.5245901639'))
# End of function test_dcfc_act_act_icma



# Generated at 2022-06-14 04:35:26.309774
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    np.testing.assert_allclose(
        dcfc_30_e_plus_360(datetime.date(2018,1,31),datetime.date(2018,2,28),datetime.date(2018,2,28)),
        0.083333333333333)
    np.testing.assert_allclose(
        dcfc_30_e_plus_360(datetime.date(2018,12,28),datetime.date(2019,2,28),datetime.date(2019,2,28)),
        0.086111111111111)


# Generated at 2022-06-14 04:35:35.496843
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    from .currencies import USD
    from .monetary import Money

    assert DCC_ACT.calculate_fraction(
        datetime.date(2017,  1,  1), datetime.date(2017,  1,  1), datetime.date(2017,  1,  2)) == ZERO
    assert DCC_ACT.calculate_fraction(
        datetime.date(2017,  1,  1), datetime.date(2017,  1,  1), datetime.date(2017,  1,  1)) == ZERO
    assert DCC_ACT.calculate_fraction(
        datetime.date(2017,  1,  1), datetime.date(2017,  1,  2), datetime.date(2017,  1,  2)) == ONE

# Generated at 2022-06-14 04:35:46.871358
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    from wolff.math.dcfc import dcfc_30_e_360
    assert(round(dcfc_30_e_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14)) == 0.16666666666667
    assert(round(dcfc_30_e_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14)) == 0.16944444444444
    assert(round(dcfc_30_e_360(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14)) == 1.08333333333333
   

# Generated at 2022-06-14 04:35:55.826021
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:36:05.571066
# Unit test for function dcfc_30_e_plus_360

# Generated at 2022-06-14 04:36:09.703862
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    # Set up test 1
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex1_dcfc = dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    # Set up test 2
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex2_dcfc = dcfc_act_365_a(start=ex2_start, asof=ex2_asof, end=ex2_asof)
    # Set up test 3

# Generated at 2022-06-14 04:36:12.839284
# Unit test for method find of class DCCRegistryMachinery
def test_DCCRegistryMachinery_find():
    name = "Act/Act"
    assert DCCRegistry.find(name) != None
    assert DCCRegistry.find(name).name == name


# Generated at 2022-06-14 04:36:25.815072
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    """
    Tests calculating the day count fraction.
    """
    ## AAPR:
    assert DCCs["AAPR"].calculate_fraction(datetime.date(2014, 1, 1), datetime.date(2014, 12, 31), datetime.date(2015, 1, 1)) == Decimal(1)

    ## ACT/365:
    assert DCCs["ACT/365"].calculate_fraction(datetime.date(2014, 1, 1), datetime.date(2014, 12, 31), datetime.date(2015, 1, 1)) == Decimal(1)

    ## ACT/360:

# Generated at 2022-06-14 04:37:15.048305
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    """
    Ensures that the function dfc_act_act_icma returns the expected results.
    """
    assert round(dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)),10)==Decimal('0.5245901639')


# Generated at 2022-06-14 04:37:22.291005
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    dcc = DCC('name', 'altnames', 'currencies', 'calculate_fraction_method')
    assert (dcc.calculate_fraction(start, asof, end, freq)) == \
           DCC.calculate_fraction_method(start, asof, end, freq)


# Generated at 2022-06-14 04:37:33.745831
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ## It should work if the start date is the end:
    assert dcfc_30_360_us(datetime.date(year=2008, month=2, day=28), datetime.date(year=2008, month=2, day=28), datetime.date(year=2008, month=2, day=28)) == Decimal("0.08333333333333")

    ## It should work for known examples:
    assert dcfc_30_360_us(datetime.date(year=2008, month=4, day=15), datetime.date(year=2008, month=10, day=15), datetime.date(year=2008, month=10, day=15)) == Decimal("0.5")

# Generated at 2022-06-14 04:37:47.188359
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478')

# Generated at 2022-06-14 04:37:57.401530
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    # Test case # 1: previous day is before start date, so return 0
    start_date = datetime.date(2017, 1, 1)
    previous_day = datetime.date(2016, 12, 31)
    asof = datetime.date(2017, 1, 1)
    end_date = datetime.date(2017, 1, 2)
    dcc = DCC('dcc', ['dcc'], _as_ccys({''}), dcc_actual_actual)
    assert dcc.calculate_daily_fraction(start_date, previous_day, end_date) == 0

    # Unit test for method calculate_daily_fraction of class DCC
    # Test case # 2: previous day is start date, so return 0
    start_date = datetime.date(2017, 1, 1)
    previous

# Generated at 2022-06-14 04:38:08.874523
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Runs unit tests for the :func:`dcfc_30_360_us` function.
    """
    # Imports
    import math

    # Unit-test #1
    dcf = dcfc_30_360_us(start=datetime.date(2013,1,2), asof=datetime.date(2013,1,31), end=datetime.date(2013,1,31))
    dcf_should_be = 30.0 / 360.0
    dcf_is_ok = abs(dcf - dcf_should_be)/dcf_should_be < 1e-12
    assert(dcf_is_ok == True)

    # Unit-test #2

# Generated at 2022-06-14 04:38:19.302636
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16942884946478')

# Generated at 2022-06-14 04:38:30.863125
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    '''
    This function tests the function dcfc_nl_365.
    We expect the function to return the correct day count fraction for each convention.
    '''
    # Assume
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)


# Generated at 2022-06-14 04:38:43.512109
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert round(dcfc_30_e_360(Date(1,1,1), Date(1,1,1), Date(1,1,1)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(Date(1,1,1), Date(1,1,1), Date(1,1,2)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(Date(1,1,1), Date(1,1,1), Date(1,1,30)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_e_360(Date(1,1,1), Date(1,1,1), Date(1,1,31)), 14) == Decimal

# Generated at 2022-06-14 04:38:50.561204
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert round(
        dcfc_30_360_german(start=datetime.date(2007, 1, 31), asof=datetime.date(2007, 1, 31), end=datetime.date(2007, 1, 31)), 14
    ) == Decimal('0.08333333333333')
    assert round(
        dcfc_30_360_german(start=datetime.date(2007, 1, 31), asof=datetime.date(2008, 1, 31), end=datetime.date(2008, 1, 31)), 14
    ) == Decimal('1.08333333333333')

# Generated at 2022-06-14 04:39:43.668123
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    '''
    Modification from the test from the "Act/365A" convention (in @dcc decorator):
        replace asof = asof with asof = asof + timedelta(days=1)
    '''
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28) + timedelta(days=1)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29) + timedelta(days=1)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30) + timedelta(days=1)
    ex4_start, ex4_asof = datetime.date

# Generated at 2022-06-14 04:39:54.993651
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:40:03.810654
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    ex1_start, ex1_asof, ex1_end, expected_result = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2), Decimal('0.5245901639')
    assert round(dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end), 10) == expected_result


# Generated at 2022-06-14 04:40:09.892121
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    # Setup
    test_start = datetime.date(year=2020, month=1, day=1)
    test_asof = datetime.date(year=2020, month=7, day=1)
    expected = 0.47671232876712

    # Exercise
    actual = dcfc_nl_365(test_start, test_asof, test_asof)

    # Verify
    assert round(actual, 14) == expected
    # Cleanup - none necessary



# Generated at 2022-06-14 04:40:22.549031
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_act_365_a(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')

# Generated at 2022-06-14 04:40:31.584523
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    '''
    Tests a version of the dcfc_30_e_plus_360 function with specific dates
    '''
    import datetime
    assert dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == 0.1666666666666666666666666666666666666666666666666666667
    assert dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) == 0.169444444444444444444444444444444444444444444444444444

# Generated at 2022-06-14 04:40:44.097816
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    # Test case 01
    start = datetime.date(2003, 8, 31)
    asof = datetime.date(2003, 10, 31)
    end = datetime.date(2003, 10, 31)
    freq = None
    assert round(dcfc_act_act(start, asof, end), 14) == Decimal('0.30668076109937')
    # Test case 02
    start = datetime.date(2015, 3, 23)
    asof = datetime.date(2015, 4, 24)
    end = datetime.date(2015, 4, 24)
    freq = None
    assert round(dcfc_act_act(start, asof, end), 14) == Decimal('0.31170483460559')



# Generated at 2022-06-14 04:40:48.653485
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    '''
    Unit test for function dcfc_30_e_plus_360
    '''

    # Tests date 1
    date_start = datetime.date(2007, 12, 28)
    date_asof = datetime.date(2008, 2, 28)
    assert round(dcfc_30_e_plus_360(start=date_start, asof=date_asof, end=date_asof), 14) == Decimal('0.16666666666667')

    # Tests date 2
    date_start = datetime.date(2007, 12, 28)
    date_asof = datetime.date(2008, 2, 29)
    assert round(dcfc_30_e_plus_360(start=date_start, asof=date_asof, end=date_asof), 14) == Dec

# Generated at 2022-06-14 04:40:57.460140
# Unit test for function dcfc_act_act

# Generated at 2022-06-14 04:41:06.506128
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    test = {
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)): Decimal('0.16942884946478'),
        (datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)): Decimal('0.17216108990194'),
        (datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)): Decimal('1.08243131970956'),
        (datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)): Decimal('1.32625945055768'),
    }
    for (start, asof), expected_output in test.items():
        result = dcfc_act_act(start, asof, asof)
        assert result

# Generated at 2022-06-14 04:42:50.808489
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    print(round(dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14))

# Generated at 2022-06-14 04:43:03.208656
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    """
    Test function dcfc_30_e_360.
    """

    # Test example 1:
    print("Test example 1:")
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    print("start=", ex1_start, "asof=", ex1_asof)
    print(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof))

    # Test example 2:
    print("Test example 2:")
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)

# Generated at 2022-06-14 04:43:06.261327
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCActualActual().calculate_fraction(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31), datetime.date(2018, 1, 1)) == Decimal('1.027397260273973')



# Generated at 2022-06-14 04:43:18.112583
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    assert(0 == dcfc_act_act_icma(datetime.date(2019, 1, 1), datetime.date(2019, 1, 1), datetime.date(2019, 1, 1)))
    assert(1 == dcfc_act_act_icma(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31), datetime.date(2019, 12, 31)))
    assert(dcfc_act_act_icma(datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)) < 0.5)



# Generated at 2022-06-14 04:43:23.435915
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    start, asof, end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)
    expected_output = Decimal('0.5245901639')
    assert round(dcfc_act_act_icma(start=start, asof=asof, end=end), 10) == expected_output



# Generated at 2022-06-14 04:43:37.173361
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert dcfc_30_360_us(datetime.date(2011,1,1), datetime.date(2011,1,1),datetime.date(2011,1,1)) == Decimal('0.0027777777777778')
    assert dcfc_30_360_us(datetime.date(2011,1,1), datetime.date(2011,1,31),datetime.date(2011,1,31)) == Decimal('0.083333333333333')
    assert dcfc_30_360_us(datetime.date(2011,1,1), datetime.date(2011,2,1),datetime.date(2011,2,1)) == Decimal('0.086111111111111')

# Generated at 2022-06-14 04:43:49.170945
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    dcc = DCC(name="30/360 ISDA", altnames=[], currencies=_as_ccys({}), calculate_fraction_method=dcc_actual360)
    assert dcc.calculate_daily_fraction(datetime.date(2014, 1, 1), datetime.date(2014, 2, 1), datetime.date(2014, 4, 1)) == Decimal(0.03055555555555556)
    assert dcc.calculate_daily_fraction(datetime.date(2014, 1, 1), datetime.date(2014, 3, 1), datetime.date(2014, 4, 1)) == Decimal(0.03055555555555556)

# Generated at 2022-06-14 04:43:55.502614
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2022-06-14 04:44:06.801997
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():

    global asof
    asof = datetime.date.today()

    def test(start: Date, asof: Date, end: Date, freq: Optional[Decimal] = None) -> Decimal:
        s = start.strftime("%Y-%m-%d")
        e = end.strftime("%Y-%m-%d")
        r = round(dcfc_act_act_icma(start=start, asof=asof, end=end, freq=freq), 12)
        print(f"{s} - {e}: {r}")
        return r

    test(datetime.date(2019, 3, 2), asof, datetime.date(2019, 9, 10), freq=Decimal(2))

# Generated at 2022-06-14 04:44:13.917990
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert dcfc_30_e_plus_360(datetime.date(2020, 6, 1), datetime.date(2020, 6, 30), datetime.date(2020, 6, 30)) == 1
    assert dcfc_30_e_plus_360(datetime.date(2020, 6, 30), datetime.date(2020, 7, 31), datetime.date(2020, 7, 31)) == 1
    assert dcfc_30_e_plus_360(datetime.date(2020, 1, 30), datetime.date(2020, 2, 17), datetime.date(2020, 2, 17)) == 0.4166666666666667