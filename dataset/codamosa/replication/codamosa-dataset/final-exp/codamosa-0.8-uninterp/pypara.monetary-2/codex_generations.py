

# Generated at 2022-06-14 04:51:50.500233
# Unit test for method __mul__ of class Price
def test_Price___mul__():
    from xone.money import Price
    from xone.money import Money
    from xone.money import Currency
    from xone.money import NoPrice
    from xone.money import NoMoney
    from xone.money import SomePrice
    from xone.money import SomeMoney
    from datetime import date

    # Case 1 - multiply a defined price with a positive quantity
    ccy = Currency.of('USD')
    price1 = SomePrice(ccy, 5.5, date(2020, 5, 9))
    assert price1 * 4 == SomePrice(ccy, 22, date(2020, 5, 9))
    assert price1 * 4.5 == SomePrice(ccy, 24.75, date(2020, 5, 9))

    # Case 2 - multiply a defined price with a negative quantity

# Generated at 2022-06-14 04:51:54.952936
# Unit test for method with_dov of class Price
def test_Price_with_dov():
    with raises(NotImplementedError):
        Price()

    with raises(NotImplementedError):
        Price().with_dov

    with raises(NotImplementedError):
        Price().with_dov(None)



# Generated at 2022-06-14 04:51:59.863214
# Unit test for method gte of class Price
def test_Price_gte():
    # Arrange
    price1 = Price.of(Currency.USD, Decimal(1), Date(2018, 1, 1))

    # Act
    is_greater_than_or_equal_to = price1.gte(price1)

    # Assert
    assert is_greater_than_or_equal_to is True


# Generated at 2022-06-14 04:52:07.878752
# Unit test for method with_dov of class SomeMoney
def test_SomeMoney_with_dov():
    from pymonies.currencies import Currency
    from pymonies.money import SomeMoney
    import datetime
    def test_impl():
        m1 = SomeMoney(Currency.usd(), 10, datetime.date(2007, 12, 15))
        m2 = m1.with_dov(datetime.date(2008, 1, 1))
        assert m2.dov == datetime.date(2008, 1, 1)
    test_impl()

# Generated at 2022-06-14 04:52:08.696529
# Unit test for method __le__ of class SomeMoney
def test_SomeMoney___le__():
    pass


# Generated at 2022-06-14 04:52:11.330095
# Unit test for method __truediv__ of class SomeMoney
def test_SomeMoney___truediv__():
    # AssertionError: Undefined monetary value
    with raises(AssertionError):
        SomeMoney(USD, Decimal('12.34'), Date(2019, 4, 12)) / None  # type: ignore

# Generated at 2022-06-14 04:52:21.430598
# Unit test for method __mul__ of class Price
def test_Price___mul__():
    p1 = Price.of(EUR, 10, today)
    x = Money(EUR, 99)
    p2 = p1 * 100
    assert p2.is_equal(Price(EUR, 1000, today))
    assert isinstance(p2, SomePrice)
    p3 = p1 * NoPrice
    assert p3.is_equal(NoPrice)
    assert isinstance(p3, NoPrice)
    p4 = p1 * x
    assert p4.is_equal(Price(EUR, 990, today))
    assert isinstance(p4, SomePrice)
    p5 = p1 * "100"
    assert p5.is_equal(Price(EUR, 1000, today))
    assert isinstance(p5, SomePrice)
    p6 = p1 * None

# Generated at 2022-06-14 04:52:28.213893
# Unit test for method with_qty of class Price
def test_Price_with_qty():
    # Setup
    ccy1 = Currency('USD')
    qty1 = 100
    dov1 = Date(2020, 3, 31)

    price1 = Price.of(ccy1, qty1, dov1)
    assert price1.qty == qty1

    price2 = price1.with_qty(1000)
    
    assert price2.qty == 1000
    assert price2 is not price1



# Generated at 2022-06-14 04:52:40.834504
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    c1 = CurrencyService.register_usd
    c2 = CurrencyService.register_cny
    c3 = CurrencyService.register_nok
    c4 = CurrencyService.register_chf
    c5 = CurrencyService.register_gbp
    c6 = CurrencyService.register_cad
    c7 = CurrencyService.register_aud
    c8 = CurrencyService.register_sek
    c9 = CurrencyService.register_nzd
    c10 = CurrencyService.register_eur
    c11 = CurrencyService.register_jpy

    ## US to US (1.0):
    assert SomePrice(c1, 1, DateService.now()).convert(c1, DateService.now()) == SomePrice(c1, 1, DateService.now())

    ## Real case (USD to CNY):

# Generated at 2022-06-14 04:52:48.184921
# Unit test for method convert of class Price
def test_Price_convert():
    assert Price.of(USD, Decimal("1"), Date.today()).convert(EUR, Date.today()) == Price.of(EUR, Decimal("1"), Date.today())
    assert Price.of(EUR, Decimal("1"), Date.today()).convert(USD, Date.today()) == Price.of(USD, Decimal("0.89508950895089"), Date.today())
    assert Price.of(USD, Decimal("1"), Date.today()).convert(GBP, Date.today()).qty == Price.of(GBP, Decimal("0.79458945894589"), Date.today()).qty
    assert Price.of(USD, None, Date.today()).convert(USD, Date.today()) == NoPrice 
    # assert Price.of(GBP, Dec

# Generated at 2022-06-14 04:53:17.455353
# Unit test for method __truediv__ of class SomeMoney
def test_SomeMoney___truediv__():
    """
    Tests the __truediv__ method of the SomeMoney class
    """
    a = SomeMoney(Currency.USD, Decimal(1), Date(1,1,2000))
    b = SomeMoney(Currency.USD, Decimal(2), Date(1,1,2000))
    assert a.__truediv__(2) == b

test_SomeMoney___truediv__()

# Generated at 2022-06-14 04:53:30.008895
# Unit test for method __truediv__ of class SomeMoney
def test_SomeMoney___truediv__():
    from decimal import Decimal as D
    from finance.models import Money
    from finance.models.currency import Currency as C
    from datetime import date as Date
    from finance.models.price import Price as P


    USD= C('USD')
    GBP= C('GBP')
    EUR= C('EUR')

    assert Money.of(USD, D('1.00'),Date(2020,12,2))/D('1.5') == Money.of(USD, D('0.6667'),Date(2020,12,2))
    assert Money.of(USD, D('1.00'),Date(2020,12,2))/D('-1.5') == Money.of(USD, D('-0.6667'),Date(2020,12,2))

# Generated at 2022-06-14 04:53:38.217126
# Unit test for method with_dov of class SomeMoney
def test_SomeMoney_with_dov():
    ccy = Currency.USD
    qty = Decimal("1.0")
    dov = Date(2017, 1, 1)
    sm = SomeMoney(ccy, qty, dov)

    dov_to = Date(2016, 1, 1)
    sm_to = sm.with_dov(dov_to)

    assert (sm != sm_to)
    assert (sm_to.ccy == ccy and sm_to.qty == qty and sm_to.dov == dov_to)


# Generated at 2022-06-14 04:53:46.229301
# Unit test for method __lt__ of class SomeMoney
def test_SomeMoney___lt__():
    ## SomeMoney.__lt__()
    # Raises IncompatibleCurrencyError when comparing two defined money objects with different currencies:
    with pytest.raises(IncompatibleCurrencyError):
        SomeMoney(USD, Decimal("1.0"), date(2017, 1, 1)) < SomeMoney(GBP, Decimal("1.0"), date(2017, 1, 1))

    # Returns true when comparing two defined money objects of same currency and quantity of right-hand money is greater than
    # that of left-hand:
    assert SomeMoney(USD, Decimal("1.0"), date(2017, 1, 1)) < SomeMoney(USD, Decimal("1.1"), date(2017, 1, 1))

    # Returns false when comparing two defined money objects of same currency and quantity of right-hand money is less than
    # that of left-hand:


# Generated at 2022-06-14 04:53:54.890770
# Unit test for method with_dov of class SomePrice
def test_SomePrice_with_dov():
    ccy, qty, dov = Currency.of('EUR'), Decimal('.1111'), Date.of(2018, 2, 1)
    price = SomePrice(ccy, qty, dov)
    new_dov = Date.of(2018, 2, 15)
    assert price.with_dov(new_dov).dov is new_dov
    assert price.with_dov(new_dov) is not price
    assert price.with_dov(dov) is price
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tests for class SomePrice
# Single ccy conversion test

# Generated at 2022-06-14 04:53:59.107551
# Unit test for method gte of class Price
def test_Price_gte():
    s = Price.of(USD, 100, dov)
    t = Price.of(USD, 100, dov)
    u = Price.of(USD, 1000, dov)
    v = Price.of(EUR, 500, dov)
    assert s.__ge__(t) == True
    assert s.__ge__(u) == False
    assert u.__ge__(v) == True
    assert v.__ge__(s) == False
    return True


# Generated at 2022-06-14 04:54:03.910119
# Unit test for method __eq__ of class Price
def test_Price___eq__():
    assert SomePrice(CCCY_EUR, Decimal(0), TODAY) == SomeMoney(CCCY_EUR, Decimal(0), TODAY)
    assert SomePrice(CCCY_EUR, Decimal('4.99'), TODAY) == SomeMoney(CCCY_EUR, Decimal('4.9900'), TODAY)
    assert SomePrice(CCCY_USD, Decimal('4.99'), TODAY) == SomeMoney(CCCY_USD, Decimal('4.99'), TODAY)
    assert SomePrice(CCCY_USD, Decimal('4.99'), TODAY) != SomeMoney(CCCY_EUR, Decimal('4.99'), TODAY)



# Generated at 2022-06-14 04:54:06.561722
# Unit test for method gte of class Price
def test_Price_gte():
    assert(Price.NA.gte(Price.NA) == True)
    assert(Price.NA.gte(Price.of('USD', 10, Date.from_str('2019-01-01'))) == False)
    assert(Price.of('USD', 10, Date.from_str('2019-01-01')).gte(Price.NA) == True)


# Generated at 2022-06-14 04:54:12.662476
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    ## SomePrice.convert
    # ==================
    #
    # Test the behaviour of method convert of class SomePrice.
    #
    # Setup
    # -----
    #
    # Create an instance of SomePrice as a test subject.
    #
    subject = SomePrice(Currency("EUR"), Decimal("1.8"), posix_epoch)
    #
    # Exercise
    # --------
    #
    # Attempt to convert the test subject from EUR to GBP, with a value date of 2010-01-01.
    #
    result = subject.convert(to=Currency("GBP"), asof=Date("2010-01-01"))  # type: ignore
    #
    # Verify
    # ------
    #
    # Check that the expected result is returned.
    #

# Generated at 2022-06-14 04:54:20.647175
# Unit test for method __float__ of class Price
def test_Price___float__():
    # Note: We do not test for the special case where the price is defined but qty is None. This is because
    # of the way class SomeMoney is implemented.
    some_price = Price.of(Currency.USD, Decimal('0.95'), Date.today())
    assert float(some_price) == 0.95

    # Note: We do not test for the special case where the price is defined but qty is None. This is because
    # of the way class SomeMoney is implemented.
    none_price = NoPrice
    with pytest.raises(MonetaryOperationException):
        float(none_price)