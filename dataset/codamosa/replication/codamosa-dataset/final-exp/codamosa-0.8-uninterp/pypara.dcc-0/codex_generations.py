

# Generated at 2022-06-14 04:34:57.039373
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

    assert abs(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof) - 0.16666666666667) < 1.0e-14

# Generated at 2022-06-14 04:35:10.308025
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    Unit test for function dcfc_30_360_german
    """
    print("Test function dcfc_30_360_german")

    # Start date
    ex1_start, ex2_start, ex3_start, ex4_start = datetime.date(2007, 12, 28), datetime.date(2007, 12, 28), datetime.date(2007, 10, 31), datetime.date(2008, 2, 1)

    # As of date
    ex1_asof, ex2_asof, ex3_asof, ex4_asof = datetime.date(2008, 2, 28), datetime.date(2008, 2, 29), datetime.date(2008, 11, 30), datetime.date(2009, 5, 31)

    # Test 1
    res = dcfc_30

# Generated at 2022-06-14 04:35:19.827503
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    ex1_start, ex1_asof = (datetime.date(2007, 12, 28), datetime.date(2008, 2, 28))
    ex2_start, ex2_asof = (datetime.date(2007, 12, 28), datetime.date(2008, 2, 29))
    ex3_start, ex3_asof = (datetime.date(2007, 10, 31), datetime.date(2008, 11, 30))
    ex4_start, ex4_asof = (datetime.date(2008, 2, 1), datetime.date(2009, 5, 31))
    assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
   

# Generated at 2022-06-14 04:35:31.672495
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():
    assert dcfc_30_e_360(start=Date(2019, 3, 29), asof=Date(2019, 5, 30), end=Date(2020, 5, 30)) == 0.08333333333333333
    assert dcfc_30_e_360(start=Date(2019, 3, 29), asof=Date(2019, 5, 31), end=Date(2020, 5, 30)) == 0.08333333333333333
    assert dcfc_30_e_360(start=Date(2019, 3, 30), asof=Date(2019, 5, 30), end=Date(2020, 5, 30)) == 0.08333333333333333
    assert dcfc_30_e_360(start=Date(2019, 3, 30), asof=Date(2019, 5, 31), end=Date(2020, 5, 30))

# Generated at 2022-06-14 04:35:42.893742
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    ## Test data:
    ex1_start, ex1_asof = datetime.date(2014, 12, 31), datetime.date(2015, 1, 31)
    ex2_start, ex2_asof = datetime.date(2014, 12, 30), datetime.date(2015, 1, 31)
    ex3_start, ex3_asof = datetime.date(2014, 12, 31), datetime.date(2015, 1, 30)
    ex4_start, ex4_asof = datetime.date(2014, 1, 1), datetime.date(2014, 2, 1)
    ex5_start, ex5_asof = datetime.date(2014, 1, 31), datetime.date(2014, 2, 28)

# Generated at 2022-06-14 04:35:51.079479
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert(0.16666666666667 == round(dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14))
    assert(0.16944444444444 == round(dcfc_30_e_plus_360(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14))
    assert(1.08333333333333 == round(dcfc_30_e_plus_360(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14))

# Generated at 2022-06-14 04:36:03.724341
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    assert round(dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_german(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_german(start=datetime.date(2007, 10, 31), asof=datetime.date(2008, 11, 30), end=datetime.date(2008, 11, 30)), 14) == Dec

# Generated at 2022-06-14 04:36:11.163191
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    assert DCCRegistry.ACT_360.calculate_daily_fraction(
        start=datetime.date(year=2000, month=1, day=1),
        asof=datetime.date(year=2000, month=1, day=2),
        end=datetime.date(year=2000, month=12, day=31),
    ) == Decimal("0.00277777777")



# Generated at 2022-06-14 04:36:15.476715
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    # This function uses the doctest module.
    import doctest
    doctest.testmod(verbose=False)
test_dcfc_30_360_german()


# Generated at 2022-06-14 04:36:27.761367
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    assert DCCRegistry['30/360 ICMA'].calculate_fraction(
        datetime.date(2017, 1, 1), datetime.date(2017, 1, 1), datetime.date(2017, 1, 2)) == Decimal('0.0027777777777777777777777777777777777777')
    assert DCCRegistry['30/360 ICMA'].calculate_fraction(
        datetime.date(2017, 1, 1), datetime.date(2017, 1, 1), datetime.date(2017, 1, 1)) == Decimal('0.0')

# Generated at 2022-06-14 04:36:47.814779
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    assert DCCRegistry.ACT_360.coupon(Money(100, 'USD'), .05, datetime.date(2020, 1, 1), datetime.date(2020, 2, 1), datetime.date(2020, 3, 1), freq = 2) == Money(2.5, 'USD')
    assert DCCRegistry.ACT_360.coupon(Money(100, 'USD'), .05, datetime.date(2020, 1, 1), datetime.date(2020, 2, 1), datetime.date(2020, 3, 1), freq = 2) == Money(2.5, 'USD')

# Generated at 2022-06-14 04:36:52.789153
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    # Start date
    start = datetime.date(2020, 1, 1)

    # Fixing date
    fixing = datetime.date(2020, 2, 1)

    # End date
    end = datetime.date(2021, 1, 1)

    # Setup DCC
    calc_fraction_method = lambda start, fixing, end, freq: ONE
    dcc = DCC('name', {'altname'}, {Currencies['USD']}, calc_fraction_method)

    # Calculate daily fraction
    fraction = dcc.calculate_daily_fraction(start, fixing, end, 1)

    # Assert that daily fraction is one
    assert(fraction == ONE)



# Generated at 2022-06-14 04:36:55.140248
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    result = dcfc_30_e_plus_360(datetime.date(2013, 11, 30), datetime.date(2014, 3, 31), datetime.date(2014, 3, 31))
    assert result == Decimal('0.16111111111111')



# Generated at 2022-06-14 04:37:07.260297
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert abs(0.16666666666667 - dcfc_30_e_plus_360.func(
        start=datetime.date(2007, 12, 28),
        asof=datetime.date(2008, 2, 28),
        end=datetime.date(2008, 2, 28),
        freq=None
    )) < 1.e-10
    assert abs(0.16944444444444 - dcfc_30_e_plus_360.func(
        start=datetime.date(2007, 12, 28),
        asof=datetime.date(2008, 2, 29),
        end=datetime.date(2008, 2, 29),
        freq=None
    )) < 1.e-10

# Generated at 2022-06-14 04:37:19.804301
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert dcfc_30_360_us(
        datetime.date(2018, 2, 28),
        datetime.date(2018, 3, 31),
        datetime.date(2018, 3, 31)) == Decimal("0.17777777777778")
    assert dcfc_30_360_us(
        datetime.date(2018, 2, 28),
        datetime.date(2018, 3, 30),
        datetime.date(2018, 3, 30)) == Decimal("0.15555555555556")
    assert dcfc_30_360_us(
        datetime.date(2018, 2, 28),
        datetime.date(2018, 4, 30),
        datetime.date(2018, 4, 30)) == Decimal("0.33333333333333")
    assert dcf

# Generated at 2022-06-14 04:37:29.578171
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():
    # Given
    ex1_start: datetime.date = datetime.date(2019, 3, 2)
    ex1_asof: datetime.date = datetime.date(2019, 9, 10)
    ex1_end: datetime.date = datetime.date(2020, 3, 2)
    # When
    actual: Decimal = dcfc_act_act_icma(start=ex1_start, asof=ex1_asof, end=ex1_end, freq=Decimal(4))
    # Then
    assert actual == Decimal("0.1311454040")

# Generated at 2022-06-14 04:37:40.681126
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    """
    Ensure that the daily fraction is calculated as expected.
    """
    start = datetime.date(2017, 1, 1)
    asof = datetime.date(2017, 1, 5)
    end = datetime.date(2017, 1, 7)


# Generated at 2022-06-14 04:37:51.727192
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    assert DCCRegistry.find("act/act afb").coupon(Money(1000, "EUR"), Decimal(0.1), datetime.date(2014, 1, 1), datetime.date(2014, 1, 2), datetime.date(2014, 1, 10), Decimal(1)) == Money(10, "EUR")
    assert DCCRegistry.find("act/act isda").coupon(Money(1000, "EUR"), Decimal(0.1), datetime.date(2014, 1, 1), datetime.date(2014, 1, 2), datetime.date(2014, 1, 10), Decimal(1)) == Money(10, "EUR")

# Generated at 2022-06-14 04:38:01.694057
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    test_cases = (((datetime.date(2007,12,28),datetime.date(2008,2,28)), 0.166666666666667),
                  ((datetime.date(2007,12,28),datetime.date(2008,2,29)), 0.169444444444444),
                  ((datetime.date(2007,10,31),datetime.date(2008,11,30)), 1.08333333333333),
                  ((datetime.date(2008,2,1),datetime.date(2009,5,31)), 1.33333333333333))
    for test_case in test_cases:
        actual = round(dcfc_30_360_isda(*test_case[0]), 14)
        expected = test_case[1]

# Generated at 2022-06-14 04:38:08.490025
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    assert dcfc_30_360_isda(start=datetime.date(1998, 7, 31), asof=datetime.date(1998, 12, 31), end=datetime.date(1998, 12, 31)) == Decimal("0.16666666666667")
    assert dcfc_30_360_isda(start=datetime.date(1998, 7, 31), asof=datetime.date(1998, 12, 31), end=datetime.date(1998, 12, 30)) == Decimal("0.16666666666667")
    assert dcfc_30_360_isda(start=datetime.date(1998, 12, 30), asof=datetime.date(1999, 1, 15), end=datetime.date(1999, 1, 15)) == Decimal("0.08333333333333")
    assert dcf

# Generated at 2022-06-14 04:38:56.334136
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    # Init
    machinery = DCCRegistryMachinery()
    dcc = DCC(name="Act/Act", altnames=set(), currencies=set(), calculate_fraction_method=lambda x, y, z, w: Decimal(1))
    # Check
    machinery.register(dcc)
    assert dcc in machinery.registry

# Generated at 2022-06-14 04:39:00.986034
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    # Define the end date
    end = datetime.date(2018, 2, 28)

    # Define a list of start dates
    start_dates = [
        datetime.date(2018, 1, 30),
        datetime.date(2018, 2, 1),
        datetime.date(2017, 3, 5),
        datetime.date(2017, 3, 31),
        datetime.date(2017, 5, 30),
        datetime.date(2017, 12, 31),
    ]

    # Compute the expected day count fractions

# Generated at 2022-06-14 04:39:13.195559
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """Performs unit tests for dcfc_30_360_german."""

    # Define test data:
    start_day, asof_day = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    start_month_end, asof_month_end = datetime.date(2007, 12, 31), datetime.date(2008, 2, 29)
    start_leap_year_end, asof_leap_year_end = datetime.date(2012, 2, 29), datetime.date(2012, 3, 31)
    start_end, asof_end = datetime.date(2007, 12, 31), datetime.date(2008, 3, 31)

    # Perform tests:

# Generated at 2022-06-14 04:39:22.857452
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    # Basic test
    assert dcfc_30_360_us(datetime.date(2017, 1, 1), datetime.date(2017, 1, 1), datetime.date(2017, 1, 1)) == Decimal('0')
    assert dcfc_30_360_us(datetime.date(2017, 1, 1), datetime.date(2017, 1, 2), datetime.date(2017, 1, 2)) == Decimal('1/360')
    assert dcfc_30_360_us(datetime.date(2017, 1, 1), datetime.date(2017, 2, 1), datetime.date(2017, 2, 1)) == Decimal('1/12')

# Generated at 2022-06-14 04:39:35.640001
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():
    """
    unit test for function dcfc_30_360_german
    """
    import unittest
    class TestDCFC(unittest.TestCase):
        def test1(self):
            self.assertEqual(
                round(dcfc_30_360_german(
                    start=datetime.date(year=2007, month=12, day=28),
                    asof=datetime.date(year=2008, month=2, day=28),
                    end=datetime.date(year=2008, month=2, day=28)), 14),
                Decimal('0.16666666666667'))

# Generated at 2022-06-14 04:39:48.247913
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    # Create the test object
    dccrm = DCCRegistryMachinery()
    # Create the test object
    dcc = DCC("Act/365", {"ACT/365", "ACT/365F", "ACT365", "ACT365F", "A365"}, {"EUR", "USD"})
    # Register the DCC
    dccrm.register(dcc)
    # Check the returned values
    assert dccrm._is_registered("Act/365") == True
    assert dccrm._is_registered("ACT/365") == True
    assert dccrm._is_registered("ACT/365F") == True
    assert dccrm._is_registered("ACT365") == True
    assert dccrm._is_registered("ACT365F") == True
    assert dccrm._is_registered("A365") == True


################

# Generated at 2022-06-14 04:39:57.646033
# Unit test for function dcfc_act_act
def test_dcfc_act_act():
    # Test Option 1
    ex1_start = datetime.date(2007, 12, 28)
    ex1_asof = datetime.date(2008, 2, 28)
    expected_result = Decimal('0.16942884946478')
    actual_result = dcfc_act_act(start=ex1_start, asof=ex1_asof, end=ex1_asof)
    assert round(actual_result, 14) == expected_result
    # Test Option 2
    ex2_start = datetime.date(2007, 12, 28)
    ex2_asof = datetime.date(2008, 2, 29)
    expected_result = Decimal('0.17216108990194')

# Generated at 2022-06-14 04:40:08.726415
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    dcfc_30_360_isda(start=ex1_start, asof=ex1_asof, end=ex1_asof)

# Generated at 2022-06-14 04:40:20.300168
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():
    """
    Unit test for function dcfc_nl_365
    """
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)
    assert round(dcfc_nl_365(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Dec

# Generated at 2022-06-14 04:40:30.373751
# Unit test for method coupon of class DCC
def test_DCC_coupon():
    """
    Test coupon method of class DCC.
    """
    from ..currencies import add_currency
    from ..currencies import CURRENCIES
    from ..currencies import Currencies
    add_currency("XAU", "Gold", "XAU", gold=True)
    add_currency("XAG", "Silver", "XAG", silver=True)
    xau = Currencies("XAU")
    xag = Currencies("XAG")
    CURRENCIES.XAU.precision = 4
    CURRENCIES.XAG.precision = 4
    print("\ntesting coupon method of DCC class:")
    print("test_0")

# Generated at 2022-06-14 04:41:17.511524
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    # The following examples are based on dcfc_30_e_360, with the difference that for dcfc_30_e_plus_360 the
    # "asof" date was added by one day.
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 3, 1)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 31)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 6, 1)

    # Test example 1 with dcfc

# Generated at 2022-06-14 04:41:23.039808
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():
    assert round(dcfc_act_365_l(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2007, 12, 28)), 14) == Decimal('0.16939890710383')
    assert round(dcfc_act_365_l(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2007, 12, 28)), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_l(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2007, 10, 31)), 14) == Decimal('1.08196721311475')

# Generated at 2022-06-14 04:41:34.693617
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():
    assert round(dcfc_30_e_plus_360(start=date(2007, 12, 28), asof=date(2008, 2, 28), end=date(2008, 2, 28)), 14) == 0.16666666666667
    assert round(dcfc_30_e_plus_360(start=date(2007, 12, 28), asof=date(2008, 2, 29), end=date(2008, 2, 29)), 14) == 0.16944444444444
    assert round(dcfc_30_e_plus_360(start=date(2007, 10, 31), asof=date(2008, 11, 30), end=date(2008, 11, 30)), 14) == 1.08333333333333

# Generated at 2022-06-14 04:41:46.794066
# Unit test for method interest of class DCC
def test_DCC_interest():
    dcc = DCC("30/360 ISMA", {"ISMA", "30U/360", "30E/360"}, {Currencies.USD}, DCCRegistry.d30_360_isma)
    principal = Money(100, Currencies.USD)
    rate = Decimal("0.05")
    start = Date(2019, 10, 1)
    asof = Date(2019, 10, 1)
    assert str(dcc.interest(principal, rate, start, asof)) == "-1.67"
    asof = Date(2019, 10, 2)
    assert str(dcc.interest(principal, rate, start, asof)) == "-1.67"
    asof = Date(2019, 10, 3)

# Generated at 2022-06-14 04:41:58.949516
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():
    assert round(dcfc_act_365_a(start=datetime.date(2007,12,28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008,2,28)), 14) == Decimal('0.16986301369863')
    assert round(dcfc_act_365_a(start=datetime.date(2007,12,28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008,2,29)), 14) == Decimal('0.17213114754098')
    assert round(dcfc_act_365_a(start=datetime.date(2007,10,31), asof=datetime.date(2008,11,30), end=datetime.date(2008,11,30)), 14) == Dec

# Generated at 2022-06-14 04:42:09.930573
# Unit test for method register of class DCCRegistryMachinery
def test_DCCRegistryMachinery_register():
    principal = Money.of(Currencies['USD'], Decimal(1000000), datetime.date.today())
    start = datetime.date(2007, 12, 28)
    end = datetime.date(2008, 2, 28)
    rate = Decimal(0.01)
    dcc = DCC('Act/Act', frozenset({'ACT/ACT', 'Actual/Actual', 'Act/Actual', 'Actual/Act', 'ACTUAL/ACTUAL'}), frozenset({Currencies['USD']}), _day_count_fraction_act_act)
    try:
        DCCRegistry.register(dcc)
    except:
        pass
    assert DCCRegistry.register(dcc) == None

# Generated at 2022-06-14 04:42:22.272759
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    """
    Unit Test for dcfc_30_360_us
    """
    # Test data:
    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)
    ex2_start, ex2_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 29)
    ex3_start, ex3_asof = datetime.date(2007, 10, 31), datetime.date(2008, 11, 30)
    ex4_start, ex4_asof = datetime.date(2008, 2, 1), datetime.date(2009, 5, 31)

# Generated at 2022-06-14 04:42:31.345092
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():
    assert round(dcfc_30_360_us(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14) == Decimal("0.16666666666667")
    assert round(dcfc_30_360_us(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)), 14) == Decimal("0.16944444444444")
    assert round(dcfc_30_360_us(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)), 14) == Decimal("1.08333333333333")

# Generated at 2022-06-14 04:42:42.615621
# Unit test for method interest of class DCC

# Generated at 2022-06-14 04:42:52.496431
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    from .currencies import USD
    from .monetary import Money
    from .quantity import units

    start = Date(2004, 12, 5)
    end = Date(2005, 4, 5)
    pm = Money(1, USD)
    rate = Decimal("0.03")
    f1 = DCCs[0].calculate_fraction(start, Date(2014, 4, 1), end)
    print(f"Days between {start} and {end}: {end.day_count(start)}. Fraction: {f1}.")
    f2 = DCCs[0].calculate_fraction(start, Date(2005, 3, 5), end)
    print(f"Days between {start} and {end}: {end.day_count(start)}. Fraction: {f2}.")


# Generated at 2022-06-14 04:44:03.889115
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    from .currencies import Currency, Currencies
    from .monetary import Money
    ccy = Currencies["USD"]
    day_count = DCCRegistry.find("30E/360M")
    print(day_count.calculate_daily_fraction(datetime.date(2016, 8, 1), datetime.date(2016, 10, 2), datetime.date(2016, 11, 30)))
    print(day_count.interest(Money(100, ccy), Decimal(0.05), datetime.date(2016, 8, 1), datetime.date(2016, 10, 2), datetime.date(2016, 11, 30)))
    
    day_count = DCCRegistry.find("ACT/360")

# Generated at 2022-06-14 04:44:11.716127
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():
    import datetime
    print("Testing function calculate_daily_fraction of class DCC")
    for day_count in DCCRegistry.DAY_COUNTS:
        print("\tTesting", day_count.name, "...")
        start, asof, end = datetime.date(2014, 1, 1), datetime.date(2014, 2, 1), datetime.date(2014, 3, 1)
        assert day_count.calculate_daily_fraction(start, asof, end) == day_count.calculate_fraction(start, asof, end)
    print("PASSED")



# Generated at 2022-06-14 04:44:22.956693
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():
    # checks if dates are provided properly:
    assert DCC(name='', altnames=set(), currencies=set(), calculate_fraction_method=lambda start, asof, end, freq: None)[3](
        start = datetime.date(2019, 1, 1), 
        asof = datetime.date(2019, 1, 2), 
        end = datetime.date(2019, 1, 1), 
        freq = None
    ) == ZERO