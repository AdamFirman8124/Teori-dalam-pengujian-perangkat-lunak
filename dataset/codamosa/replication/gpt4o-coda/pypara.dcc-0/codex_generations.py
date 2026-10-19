

# Generated at 2024-06-03 03:14:59.455126
# Unit test for method coupon of class DCC
def test_DCC_coupon():    # Define a sample DCC instance with a simple day count fraction calculation method
    dcc = DCC(
        name="30/360",
        altnames=set(),
        currencies=set(),
        calculate_fraction_method=lambda start, asof, end, freq: Decimal((asof - start).days) / Decimal(360)
    )

    # Define test parameters
    principal = Money(Decimal('1000'), Currency('USD'))
    rate = Decimal('0.05')
    start = datetime.date(2020, 1, 1)
    asof = datetime.date(2020, 6, 30)
    end = datetime.date(2021, 1, 1)
    freq = Decimal('2')  # Semi-annual
    eom = None

    # Calculate the coupon
    coupon = dcc.coupon(principal, rate, start, asof, end, freq, eom)

    #

# Generated at 2024-06-03 03:15:04.107790
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:15:08.329518
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:15:11.563949
# Unit test for function dcfc_act_act
def test_dcfc_act_act():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:15:15.339523
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():    dcc = DCC(
        name="30/360",
        altnames={"30U/360", "360/360"},
        currencies=_as_ccys({"USD", "EUR"}),
        calculate_fraction_method=lambda start, asof, end, freq: Decimal((asof - start).days) / Decimal(360)
    )


# Generated at 2024-06-03 03:15:18.890283
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:15:22.205972
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:15:27.669600
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:15:30.826332
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():    # Define a mock calculation method
    def mock_calculate_fraction_method(start, asof, end, freq):
        return Decimal((end - start).days) / Decimal(365)

    # Create a DCC instance with the mock method
    dcc = DCC(
        name="MockDCC",
        altnames=set(),
        currencies=set(),
        calculate_fraction_method=mock_calculate_fraction_method
    )

    # Test cases
    start = datetime.date(2020, 1, 1)
    asof = datetime.date(2020, 6, 1)
    end = datetime.date(2020, 12, 31)

    # Test when dates are in order
    assert dcc.calculate_fraction(start, asof, end) == Decimal(365 - 1) / Decimal(365)

    # Test when asof is before start
    assert dcc.calculate_fraction(asof, start, end)

# Generated at 2024-06-03 03:15:34.461487
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:16:31.754061
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:16:36.043627
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:16:39.875430
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:16:43.286737
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():    # Define a mock calculation method
    def mock_calculate_fraction_method(start, asof, end, freq):
        return Decimal((asof - start).days) / Decimal((end - start).days)

    # Create a DCC instance with the mock method
    dcc = DCC(
        name="MockDCC",
        altnames=set(),
        currencies=set(),
        calculate_fraction_method=mock_calculate_fraction_method
    )

    # Define test dates
    start = datetime.date(2023, 1, 1)
    asof = datetime.date(2023, 1, 2)
    end = datetime.date(2023, 1, 10)

    # Calculate daily fraction
    daily_fraction = dcc.calculate_daily_fraction(start, asof, end)

    # Assert the expected result

# Generated at 2024-06-03 03:16:45.259038
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)

# Generated at 2024-06-03 03:16:49.071836
# Unit test for method interest of class DCC
def test_DCC_interest():    # Define a sample DCC instance with a simple day count fraction calculation method
    dcc = DCC(
        name="30/360",
        altnames={"30U/360", "Bond Basis"},
        currencies=_as_ccys({"USD", "EUR"}),
        calculate_fraction_method=lambda start, asof, end, freq: Decimal((asof - start).days) / Decimal(360)
    )

    # Define test parameters
    principal = Money(Decimal("1000"), Currency("USD"))
    rate = Decimal("0.05")
    start = datetime.date(2023, 1, 1)
    asof = datetime.date(2023, 7, 1)
    end = datetime.date(2023, 12, 31)

    # Calculate expected interest
    expected_interest = principal * rate * Decimal((asof - start).days) / Decimal(360)

    # Assert the interest calculation


# Generated at 2024-06-03 03:16:52.354888
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:16:56.320907
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:16:59.842822
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():    # Define a mock calculation method
    def mock_calculate_fraction_method(start, asof, end, freq):
        return Decimal((end - start).days) / Decimal(365)

    # Create a DCC instance with the mock method
    dcc = DCC(
        name="MockDCC",
        altnames=set(),
        currencies=set(),
        calculate_fraction_method=mock_calculate_fraction_method
    )

    # Test cases
    start = datetime.date(2020, 1, 1)
    asof = datetime.date(2020, 6, 1)
    end = datetime.date(2020, 12, 31)

    # Case 1: Normal case
    assert dcc.calculate_fraction(start, asof, end) == Decimal('0.9972602739726027397260273973')

    # Case 2: asof before start

# Generated at 2024-06-03 03:17:03.175433
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:18:57.078164
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:19:00.452740
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:19:04.725019
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:19:08.376862
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():    # Define a mock calculation method
    def mock_calculate_fraction_method(start, asof, end, freq):
        return Decimal((end - start).days) / Decimal(365)

    # Create a DCC instance with the mock method
    dcc = DCC(
        name="MockDCC",
        altnames=set(),
        currencies=set(),
        calculate_fraction_method=mock_calculate_fraction_method
    )

    # Test cases
    start = datetime.date(2020, 1, 1)
    asof = datetime.date(2020, 6, 1)
    end = datetime.date(2020, 12, 31)

    # Case 1: Normal case
    assert dcc.calculate_fraction(start, asof, end) == Decimal('0.9972602739726027397260273973')

    # Case 2: asof before start

# Generated at 2024-06-03 03:19:13.607003
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:19:16.503396
# Unit test for method interest of class DCC
def test_DCC_interest():    # Create a mock DCC instance with a simple day count fraction calculation method
    mock_dcc = DCC(
        name="MockDCC",
        altnames=set(),
        currencies=set(),
        calculate_fraction_method=lambda start, asof, end, freq: Decimal((asof - start).days) / Decimal(365)
    )

    # Define test parameters
    principal = Money(Decimal('1000'), Currency('USD'))
    rate = Decimal('0.05')
    start = datetime.date(2023, 1, 1)
    asof = datetime.date(2023, 7, 1)
    end = datetime.date(2023, 12, 31)

    # Calculate expected interest
    expected_interest = principal * rate * Decimal((asof - start).days) / Decimal(365)

    # Assert the interest calculation

# Generated at 2024-06-03 03:19:19.480299
# Unit test for function dcfc_act_365_l
def test_dcfc_act_365_l():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:19:22.983644
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:19:27.072302
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():    # Define a mock day count fraction calculation method
    def mock_calculate_fraction_method(start, asof, end, freq):
        return Decimal((asof - start).days) / Decimal((end - start).days)

    # Create a DCC instance with the mock method
    dcc = DCC(
        name="MockDCC",
        altnames=set(),
        currencies=set(),
        calculate_fraction_method=mock_calculate_fraction_method
    )

    # Test cases
    start = datetime.date(2023, 1, 1)
    asof = datetime.date(2023, 6, 1)
    end = datetime.date(2023, 12, 31)

    # Case 1: Normal case
    assert dcc.calculate_fraction(start, asof, end) == Decimal('0.4166666666666666666666666667')

    # Case 2: asof is the same as

# Generated at 2024-06-03 03:19:31.073066
# Unit test for function dcfc_act_act
def test_dcfc_act_act():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:21:42.493630
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:21:45.621973
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:21:48.796770
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:21:51.826699
# Unit test for function dcfc_act_act_icma
def test_dcfc_act_act_icma():    ex1_start, ex1_asof, ex1_end = datetime.date(2019, 3, 2), datetime.date(2019, 9, 10), datetime.date(2020, 3, 2)

# Generated at 2024-06-03 03:21:55.992249
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:21:59.259262
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:22:02.293739
# Unit test for function dcfc_act_act
def test_dcfc_act_act():    assert round(dcfc_act_act(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')

# Generated at 2024-06-03 03:22:05.354025
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:22:08.588584
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)

# Generated at 2024-06-03 03:22:11.975157
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():    ex1_start, ex1_asof = datetime.date(2007, 12, 28), datetime.date(2008, 2, 28)