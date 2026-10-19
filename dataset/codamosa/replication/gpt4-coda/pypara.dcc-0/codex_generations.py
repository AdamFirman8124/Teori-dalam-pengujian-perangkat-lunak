

# Generated at 2024-03-18 07:01:30.193109
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    # Unit test for function dcfc_30_e_plus_360
    def test_dcfc_30_e_plus_360():
        assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
        assert round(dcfc_30_e_plus_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
        assert round(dcfc_30_e_plus_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2024-03-18 07:01:37.017350
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():    assert dcfc_30_360_isda(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == Decimal('0.16666666666667')

# Generated at 2024-03-18 07:01:38.072774
# Unit test for function dcfc_act_act

# Generated at 2024-03-18 07:01:46.965078
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():    # Create a DCC instance with a dummy calculation method
    dummy_calc_method = lambda start, asof, end, freq: Decimal((asof - start).days) / Decimal((end - start).days)
    dcc = DCC(name="30/360", altnames=set(), currencies=set(), calculate_fraction_method=dummy_calc_method)

    # Test cases

# Generated at 2024-03-18 07:01:52.529773
# Unit test for function dcfc_act_act
def test_dcfc_act_act():    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')

# Generated at 2024-03-18 07:01:58.829810
# Unit test for method interest of class DCC
def test_DCC_interest():    # Create a DCC instance with a simple day count fraction calculation method
    dcc = DCC(
        name="30/360",
        altnames={"30U/360", "Bond Basis"},
        currencies=_as_ccys({"USD", "EUR"}),
        calculate_fraction_method=lambda start, asof, end, freq: Decimal((asof - start).days) / Decimal(360)
    )

    # Define a principal amount of money
    principal = Money(amount=Decimal(1000), currency=Currencies.USD)

    # Define an interest rate
    rate = Decimal('0.05')  # 5%

    # Define start, asof, and end dates
    start = datetime.date(2021, 1, 1)
    asof = datetime.date(2021, 6, 30)
    end = datetime.date(2021, 12, 31)

    # Calculate the interest
   

# Generated at 2024-03-18 07:02:07.629688
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    # Test cases for dcfc_30_360_german
    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
    assert round(dcfc_30_360_german(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
    assert round(dcfc_30_360_german(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2024-03-18 07:02:14.877322
# Unit test for method interest of class DCC
def test_DCC_interest():    # Create a DCC instance with a simple day count fraction calculation method
    dcc = DCC(
        name="30/360",
        altnames={"30U/360", "Bond Basis"},
        currencies=_as_ccys({"USD", "EUR"}),
        calculate_fraction_method=lambda start, asof, end, freq: Decimal((end - start).days) / Decimal(360)
    )

    # Define a principal amount of money
    principal = Money(amount=Decimal(1000), currency=Currencies.USD)

    # Define an interest rate
    rate = Decimal('0.05')  # 5%

    # Define start, asof, and end dates
    start = datetime.date(2021, 1, 1)
    asof = datetime.date(2021, 6, 30)
    end = datetime.date(2021, 12, 31)

    # Calculate the expected interest

# Generated at 2024-03-18 07:02:21.447842
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    # Unit test for function dcfc_30_e_plus_360
    def test_dcfc_30_e_plus_360():
        assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
        assert round(dcfc_30_e_plus_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
        assert round(dcfc_30_e_plus_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2024-03-18 07:02:31.222504
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2024-03-18 07:03:15.934386
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():    # Test cases for the dcfc_act_365_a function
    def test_dcfc_act_365_a():
        assert dcfc_act_365_a(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == Decimal('0.16986301369863')
        assert dcfc_act_365_a(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) == Decimal('0.17213114754098')
        assert dcfc_act_365_a(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)) == Decimal('1.08196721311475')
        assert dcfc_act_365_a

# Generated at 2024-03-18 07:03:26.661843
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2024-03-18 07:03:40.916294
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():    assert dcfc_30_360_isda(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == Decimal('0.16666666666667')

# Generated at 2024-03-18 07:03:49.460088
# Unit test for function dcfc_nl_365
def test_dcfc_nl_365():    # Unit test for function dcfc_nl_365
    def test_dcfc_nl_365():
        assert round(dcfc_nl_365(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16986301369863')
        assert round(dcfc_nl_365(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16986301369863')
        assert round(dcfc_nl_365(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08219178082192')
        assert round(dcfc_nl_365(start=ex4_start, asof=ex4_asof, end=ex4_asof), 14) == Decimal('1.32602739726027')


# Generated at 2024-03-18 07:03:55.394352
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    # Unit test for function dcfc_30_e_plus_360
    def test_dcfc_30_e_plus_360():
        assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
        assert round(dcfc_30_e_plus_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
        assert round(dcfc_30_e_plus_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2024-03-18 07:04:04.015793
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2024-03-18 07:04:05.036672
# Unit test for method calculate_fraction of class DCC
def test_DCC_calculate_fraction():import unittest


# Generated at 2024-03-18 07:04:10.961159
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():    # Unit test for function dcfc_30_360_us
    def test_dcfc_30_360_us():
        assert round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16666666666667')
        assert round(dcfc_30_360_us(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 29), end=datetime.date(2008, 2, 29)), 14) == Decimal('0.16944444444444')

# Generated at 2024-03-18 07:04:25.012781
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2024-03-18 07:04:31.385329
# Unit test for function dcfc_act_act
def test_dcfc_act_act():    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')

# Generated at 2024-03-18 07:05:33.480848
# Unit test for function dcfc_30_360_german
def test_dcfc_30_360_german():    assert round(dcfc_30_360_german(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2024-03-18 07:05:42.891281
# Unit test for function dcfc_30_360_us
def test_dcfc_30_360_us():    # Unit test for function dcfc_30_360_us
    def test_dcfc_30_360_us():
        assert round(dcfc_30_360_us(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
        assert round(dcfc_30_360_us(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
        assert round(dcfc_30_360_us(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2024-03-18 07:05:43.553489
# Unit test for function dcfc_act_act

# Generated at 2024-03-18 07:05:51.715829
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():    # Test cases for the dcfc_act_365_a function
    def test_dcfc_act_365_a():
        assert dcfc_act_365_a(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == Decimal('0.16986301369863')
        assert dcfc_act_365_a(datetime.date(2007, 12, 28), datetime.date(2008, 2, 29), datetime.date(2008, 2, 29)) == Decimal('0.17213114754098')
        assert dcfc_act_365_a(datetime.date(2007, 10, 31), datetime.date(2008, 11, 30), datetime.date(2008, 11, 30)) == Decimal('1.08196721311475')
        assert dcfc_act_365_a

# Generated at 2024-03-18 07:05:58.069498
# Unit test for function dcfc_30_e_360
def test_dcfc_30_e_360():    assert round(dcfc_30_e_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')

# Generated at 2024-03-18 07:06:04.628015
# Unit test for method calculate_daily_fraction of class DCC
def test_DCC_calculate_daily_fraction():    # Create a DCC instance with a dummy calculation method
    dcc = DCC(
        name="30/360",
        altnames={"30U/360", "Bond Basis"},
        currencies=_as_ccys({"USD", "EUR"}),
        calculate_fraction_method=lambda start, asof, end, freq: Decimal((asof - start).days) / Decimal(360)
    )

    # Define test cases

# Generated at 2024-03-18 07:06:13.190109
# Unit test for function dcfc_act_365_a
def test_dcfc_act_365_a():    # Test cases for the dcfc_act_365_a function
    def test_dcfc_act_365_a():
        assert dcfc_act_365_a(Date(2007, 12, 28), Date(2008, 2, 28), Date(2008, 2, 28)) == Decimal('0.16986301369863')
        assert dcfc_act_365_a(Date(2007, 12, 28), Date(2008, 2, 29), Date(2008, 2, 29)) == Decimal('0.17213114754098')
        assert dcfc_act_365_a(Date(2007, 10, 31), Date(2008, 11, 30), Date(2008, 11, 30)) == Decimal('1.08196721311475')

# Generated at 2024-03-18 07:06:22.201867
# Unit test for function dcfc_30_e_plus_360
def test_dcfc_30_e_plus_360():    # Unit test for function dcfc_30_e_plus_360
    def test_dcfc_30_e_plus_360():
        assert round(dcfc_30_e_plus_360(start=ex1_start, asof=ex1_asof, end=ex1_asof), 14) == Decimal('0.16666666666667')
        assert round(dcfc_30_e_plus_360(start=ex2_start, asof=ex2_asof, end=ex2_asof), 14) == Decimal('0.16944444444444')
        assert round(dcfc_30_e_plus_360(start=ex3_start, asof=ex3_asof, end=ex3_asof), 14) == Decimal('1.08333333333333')

# Generated at 2024-03-18 07:06:28.357672
# Unit test for function dcfc_act_act
def test_dcfc_act_act():    assert round(dcfc_act_act(start=datetime.date(2007, 12, 28), asof=datetime.date(2008, 2, 28), end=datetime.date(2008, 2, 28)), 14) == Decimal('0.16942884946478')

# Generated at 2024-03-18 07:06:41.299087
# Unit test for function dcfc_30_360_isda
def test_dcfc_30_360_isda():    assert dcfc_30_360_isda(datetime.date(2007, 12, 28), datetime.date(2008, 2, 28), datetime.date(2008, 2, 28)) == Decimal('0.16666666666667')