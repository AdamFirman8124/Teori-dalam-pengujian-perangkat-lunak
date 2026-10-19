

# Generated at 2022-06-14 04:48:23.670335
# Unit test for method __mul__ of class Money
def test_Money___mul__():
    # ccy1, ccy2 = currency_code_set  # type: ignore
    ccy1, ccy2 = (
        Currency.of('USD'),
        Currency.of('EUR')
    )  # type: ignore
    ccy1 = Currency.of('USD')
    ccy2 = Currency.of('EUR')
    # Test cases
    # Case quantize(Numeric)
    
    
    # Case $12.34 * 2
    assert SomeMoney.of(ccy1, 12.34, Date.of(2000, 1, 1)).__mul__(2) == SomeMoney.of(ccy1, 24.68, Date.of(2000, 1, 1))
    
    
    # Case $12.34 * Decimal(2)

# Generated at 2022-06-14 04:48:34.774863
# Unit test for method __floordiv__ of class Money
def test_Money___floordiv__():
    from . import EURNOK, Money, NoneMoney, SomeMoney

    # Case 1: NoneMoney
    m1 = NoneMoney
    m2 = Money.of(EURNOK, qty=7, dov="2018-01-01")
    m3 = m1 // m2
    m4 = m1 // 2
    m5 = m1 // 2.0
    assert m3 == NoneMoney
    assert m4 == NoneMoney
    assert m5 == NoneMoney

    # Case 2: SomeMoney
    m1 = SomeMoney(EURNOK, 20.1036, "2018-01-01")
    m2 = Money.of(EURNOK, qty=7, dov="2018-01-01")
    m3 = m1 // m2
    m4 = m1 // 2
    m5 = m1 // 2.

# Generated at 2022-06-14 04:48:45.473364
# Unit test for method lt of class Money

# Generated at 2022-06-14 04:48:57.249071
# Unit test for method __lt__ of class SomePrice
def test_SomePrice___lt__():
    import finance.domain.price as module
    import money.money as money
    rate = module.NoPrice
    left = module.SomePrice(money.Currency.USD, 3, 'dov')
    right = module.SomePrice(money.Currency.USD, 3, 'dov')
    assert not left.__lt__(right)
    right = module.SomePrice(money.Currency.USD, 3 + 1e-10, 'dov')
    assert not left.__lt__(right)
    right = module.SomePrice(money.Currency.USD, 2, 'dov')
    assert left.__lt__(right)
    right = module.SomePrice(money.Currency.EUR, 3, 'dov')
    assert not left.__lt__(right)
    ## TODO: Test undefined case.


# Generated at 2022-06-14 04:49:06.748869
# Unit test for method with_ccy of class Money
def test_Money_with_ccy():
    assert SomeMoney.of(ccy=USD, qty=10, dov=dov).with_ccy(CAD) == SomeMoney.of(ccy=CAD, qty=10, dov=dov)
    assert SomeMoney.of(ccy=USD, qty=10, dov=dov).with_ccy(None) == NoMoney
    assert NoMoney.with_ccy(CAD) == NoMoney
    assert NoneMoney.with_ccy(CAD) == NoneMoney


# Generated at 2022-06-14 04:49:16.377053
# Unit test for method add of class Price
def test_Price_add():
    # All cases of None
    actual = Price().add(Price())
    expected = Price()
    assert actual == expected
    # Both defined
    actual = Price.of(Currency.USD,Decimal("7.432"),Date("2013-10-01")).add(Price.of(Currency.USD,Decimal("4.321"),Date("2013-10-01")))
    expected = Price.of(Currency.USD,Decimal("11.753"),Date("2013-10-01"))
    assert actual == expected
    # One defined
    actual = Price.of(Currency.USD,Decimal("7.432"),Date("2013-10-01")).add(Price())
    expected = Price.of(Currency.USD,Decimal("7.432"),Date("2013-10-01"))
    assert actual == expected
    # Different

# Generated at 2022-06-14 04:49:20.138883
# Unit test for method gt of class Price
def test_Price_gt():
    assert Price.of(ccy=None, qty=None, dov=None).gt(None) is False


# Generated at 2022-06-14 04:49:27.331369
# Unit test for method subtract of class Money
def test_Money_subtract():
    """
    Tests ``Money.subtract`` method for correct operation.
    """
    from dateutil.tz import tzutc
    from ..monetization import Money, Price
    from ..currencies import CurrencySet

    assert Money.of(CurrencySet.get_currency("USD"), 0.0, Date.today(tzutc())) - Price.of(CurrencySet.get_currency("USD"), 0.0, 0.0) == Money.NA



# Generated at 2022-06-14 04:49:37.824817
# Unit test for method __int__ of class Price
def test_Price___int__():
    _test_Price___int__(NoPrice, raises=TypeError)
    _test_Price___int__(SomePrice(ccy=None, qty=None, dov=None))
    _test_Price___int__(SomePrice(ccy=None, qty=Decimal("1"), dov=None))
    _test_Price___int__(SomePrice(ccy=None, qty=None, dov=Date.today()))
    _test_Price___int__(SomePrice(ccy=None, qty=Decimal("1"), dov=Date.today()))
    _test_Price___int__(SomePrice(ccy="EUR", qty=None, dov=None))

# Generated at 2022-06-14 04:49:41.103901
# Unit test for method divide of class Price
def test_Price_divide():
    # Prerequisites
    price = Price.of(Currency.get('USD'), Decimal(100), Date(1, 1, 1))

    # Test
    price = price.divide(Decimal(2))

    # Assert
    assert price == Price.of(Currency.get('USD'), Decimal(50), Date(1, 1, 1))
    assert type(price) == SomePrice



# Generated at 2022-06-14 04:50:12.907087
# Unit test for method lte of class Price
def test_Price_lte():
    assert repr(NoPrice) == repr(Price.NA)
    assert repr(NoPrice) == repr(NoPrice.NA)
    assert repr(SomePrice(CAD, Decimal('2.55'), '2020-10-10')) == repr(Price.of(CAD, Decimal('2.55'), '2020-10-10'))
    assert repr(SomePrice(CAD, Decimal('2.55'), '2020-10-10')) == repr(Money.of(CAD, Decimal('2.55'), '2020-10-10').price)
    assert repr(SomePrice(CAD, Decimal('2.55'), '2020-10-10')) == repr(Money.of(CAD, Decimal('2.55'), '2020-10-10').price)

# Generated at 2022-06-14 04:50:21.731499
# Unit test for method __eq__ of class Money
def test_Money___eq__():
    assert NoneMoney == NoneMoney
    assert SomeMoney(Currency("TRY"), Decimal("1.23"), Date(20010101)) == SomeMoney(
        Currency("TRY"), Decimal("1.23"), Date(20010101)
    )
    assert SomeMoney(Currency("USD"), Decimal("1.23"), Date(20010101)) == SomeMoney(
        Currency("USD"), Decimal("1.23"), Date(20010101)
    )
    assert not NoneMoney == SomeMoney(Currency("USD"), Decimal("1.23"), Date(20010101))
    assert not SomeMoney(Currency("USD"), Decimal("1.23"), Date(20010101)) == NoneMoney



# Generated at 2022-06-14 04:50:23.659373
# Unit test for method __le__ of class Price
def test_Price___le__():
    pass  # Don't need to test that here...

# Generated at 2022-06-14 04:50:29.546242
# Unit test for method __lt__ of class Price
def test_Price___lt__():
    import tests.fixtures as fixtures
    obj = fixtures.fx_rates
    obj_2 = fixtures.fx_rates_2

    assert Price.of(USD, Decimal("9.99999"), Date(2018, 12, 10)) < Price.of(USD, Decimal("10"), Date(2018, 12, 10))
    assert Price.of(USD, Decimal("-10"), Date(2018, 12, 10)) < Price.of(USD, Decimal("-9.99999"), Date(2018, 12, 10))

    assert Price.of(USD, Decimal("10"), Date(2018, 12, 10)) >= Price.of(USD, Decimal("10"), Date(2018, 12, 10))

# Generated at 2022-06-14 04:50:33.493484
# Unit test for method as_float of class Price
def test_Price_as_float():
    assert Price.of(Currency.of("GBP"), Decimal("123.45"), Date.of(2019, 5, 1)).as_float() == 123.45
    assert Price.of(Currency.of("GBP"), Decimal("123"), Date.of(2019, 5, 1)).as_float() == 123.0


# Generated at 2022-06-14 04:50:35.759256
# Unit test for method as_float of class Money
def test_Money_as_float():
    assert (1.0 == SomeMoney.of(ccy=USD, qty=1.0, dov=Date.now()).as_float())

# Generated at 2022-06-14 04:50:46.538552
# Unit test for method __add__ of class Price
def test_Price___add__():
    # Test for undefined price.
    a = NoPrice
    b = NoMoney
    c = NoAmount
    d = NoCurrency
    e = NoPrice
    f = Price(CURRENCIES["USD"], Decimal("1"), TODAY)
    assert a + b == a
    assert a + c == a
    assert a + d == a
    assert a + e == a
    assert a + f == f
    # Test for defined price.
    a = Price(CURRENCIES["USD"], Decimal("1"), TODAY)
    b = Price(CURRENCIES["EUR"], Decimal("1"), TODAY)
    c = Money(CURRENCIES["USD"], Decimal("1"), TODAY)
    d = Money(CURRENCIES["EUR"], Decimal("1"), TODAY)

# Generated at 2022-06-14 04:50:57.534891
# Unit test for method __add__ of class SomePrice
def test_SomePrice___add__():
    from app.pricing.domain.money import SomeMoney
    from app.pricing.domain.money import Money
    from app.pricing.domain.pricing import Price
    from decimal import Decimal
    from datetime import date
    from app.pricing.domain.currency import Currency

    ## Some prices:
    p1 = SomePrice(Currency("USD"), Decimal("1.3"), date(2020, 1, 15))
    p2 = SomePrice(Currency("USD"), Decimal("2.5"), date(2020, 1, 20))

    ## These two prices should sum up to a price that has the maximum date of value.
    assert isinstance(p1 + p2, Price)
    assert p1 + p2 == SomePrice(Currency("USD"), Decimal("3.8"), date(2020, 1, 20))

    ## Sum

# Generated at 2022-06-14 04:51:04.460398
# Unit test for method scalar_add of class Money
def test_Money_scalar_add():
    m1 = Money(Currency.USD, 1, Date.today())
    m2 = Money(Currency.USD, 2, Date.today())
    assert m1.scalar_add(2) == Money(Currency.USD, 3, Date.today())
    assert m2.scalar_add(1) == Money(Currency.USD, 3, Date.today())

# Generated at 2022-06-14 04:51:07.682308
# Unit test for method as_float of class Price
def test_Price_as_float():

    # Test a defined price
    price = Price.of(Currency.USD, 100.00, today)
    assert price.as_float() == 100.0

    # Test an undefined price
    price = Price.NA
    with raises(MonetaryOperationException):
        price.as_float()

# Generated at 2022-06-14 04:52:11.245431
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    assert Money.of(
        Currency.of("TRY"), Decimal("10"), Date.today()
    ).floor_divide(Decimal("2")) == Money.of(Currency.of("TRY"), 5, Date.today())

    assert Money.of(
        Currency.of("TRY"), Decimal("10"), Date.today()
    ).floor_divide(Decimal("3")) == Money.of(Currency.of("TRY"), 3, Date.today())

    assert Money.of(
        Currency.of("TRY"), Decimal("10"), Date.today()
    ).floor_divide(0) == Money.of(Currency.of("TRY"), 10, Date.today())

    assert Money.of(
        Currency.of("TRY"), Decimal("0"), Date.today()
    ).floor_divide(0) == Money.of

# Generated at 2022-06-14 04:52:14.879948
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    m = Money.of("USD", Decimal("1.00"), Date(2020, 1, 1))
    assert m.dov == Date(2020, 1, 1) and m.dov.is_date



# Generated at 2022-06-14 04:52:18.996352
# Unit test for method negative of class Money
def test_Money_negative():
    if not (SomeMoney(Currency('GBP'), Decimal('100.00'), Date(2020, 5, 10)).negative()
            == SomeMoney(Currency('GBP'), Decimal('-100.00'), Date(2020, 5, 10))):
        raise AssertionError()



# Generated at 2022-06-14 04:52:30.462114
# Unit test for method __truediv__ of class Money
def test_Money___truediv__():
    """
    Tests the method __truediv__ of class Money
    """
    import random
    import pytest

    from bot.monetary import currencies, money

    CURRENCIES = [currencies.ZAR, currencies.USD, currencies.CAD]

    ZEROS = (0, 0.0, 0j)
    INTS = (1, -1, 100, -100, 1000, -1000, 1000000, -1000000, 1000000)
    FLOATS = (
        0.1,
        -0.1,
        1.0,
        -1.0,
        1.1,
        0.3,
        -0.3,
        0.01,
        -0.01,
        -1.1,
        -1.11,
        -12.23,
    )
   

# Generated at 2022-06-14 04:52:34.433229
# Unit test for method __truediv__ of class Money
def test_Money___truediv__():
    """
    Tests the method Money.__truediv__
    """

    tester = Money()
    other = Money()

    result = tester.__truediv__(other)
    assert result is None



# Generated at 2022-06-14 04:52:35.822495
# Unit test for method gt of class Price
def test_Price_gt():
    assert Price.NA.gt(Price.NA) is False



# Generated at 2022-06-14 04:52:36.841384
# Unit test for method __floordiv__ of class Price
def test_Price___floordiv__():

    pass # No test needed



# Generated at 2022-06-14 04:52:40.708900
# Unit test for method scalar_add of class Money
def test_Money_scalar_add():
    money = Money.of(Money.CCY, Money.QTY, Money.DOV)
    money.scalar_add(1)
    assert True



# Generated at 2022-06-14 04:52:45.169168
# Unit test for method scalar_subtract of class Money
def test_Money_scalar_subtract():
    x=Money.of(Currency.of('AUD'),Decimal(5.6),Date.today())
    y=Money.of(Currency.of('AUD'),Decimal(1.10),Date.today())
    x.scalar_subtract(y.qty)==Money.of(Currency.of('AUD'),Decimal(4.5),Date.today())

# Generated at 2022-06-14 04:52:57.432072
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():

    """
    Unit test for testing class:`Money` method :meth:`floor_divide` in ./src/models/money.py
    """

    ## Imports:
    import pytest
    from decimal import Decimal

    from money import Money, NoMoney, SomeMoney

    ## Define:
    EUR = Money.EUR
    USD = Money.USD
    EUR_1000 = SomeMoney(EUR, Decimal(1000.0), Date.now())
    USD_2000 = SomeMoney(USD, Decimal(2000.0), Date.now())
    NONE = Money.NA

    ## Test with defined money:
    assert EUR_1000.floor_divide(Decimal(0.1)) == SomeMoney(EUR, Decimal(10000.0), Date.now())

# Generated at 2022-06-14 04:53:55.709806
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    # type: () -> None
    assert Money.of(Currency.USD, 10.5, Date.today()).floor_divide(3) == Money.of(Currency.USD, 3, Date.today())
    assert Money.of(Currency.USD, 10.5, Date.today()).floor_divide(3.5) == Money.of(Currency.USD, 3, Date.today())
    assert Money.of(Currency.USD, 10.5, Date.today()).floor_divide(Decimal('3.5')) == Money.of(Currency.USD, 3, Date.today())
    assert Money.of(Currency.USD, 10.5, Date.today()).floor_divide(Decimal('3.51')) == Money.of(Currency.USD, 3, Date.today())
   

# Generated at 2022-06-14 04:53:57.301822
# Unit test for method __int__ of class Money
def test_Money___int__():
    assert int(NoneMoney) == 0
    assert int(SomeMoney(USD, 3.14, "2019-10-13")) == 3

# Generated at 2022-06-14 04:54:00.551986
# Unit test for method as_float of class Price
def test_Price_as_float():
    assert Price.NA.as_float() == float(0)
    assert Price.of(USD, Decimal('1.0'), date(2020, 1, 1)).as_float() == float(1)
    assert Price.of(USD, Decimal('1.23'), date(2020, 1, 1)).as_float() == float(1.23)


# Generated at 2022-06-14 04:54:02.811427
# Unit test for method __lt__ of class Money
def test_Money___lt__():
    # Test KnownValue_NoneMoney_NoneMoney
    # Setup
    m1 = NoMoney
    m2 = NoMoney

    # Exercise
    actual = m1 < m2

    # Verify
    assert actual == False


# Generated at 2022-06-14 04:54:10.514676
# Unit test for method scalar_subtract of class Price
def test_Price_scalar_subtract():
    assert Price.of(Currency('GBP'), 1.5, Date('2018-06-05')).scalar_subtract(1.3) == Price.of(Currency('GBP'), 0.2, Date('2018-06-05'))
    assert Price.of(Currency('AED'), 5.0, Date('2018-06-05')).scalar_subtract(0.5) == Price.of(Currency('AED'), 4.5, Date('2018-06-05'))
    assert Price.of(Currency('USD'), 2.5, Date('2018-06-05')).scalar_subtract(0.0) == Price.of(Currency('USD'), 2.5, Date('2018-06-05'))


# Generated at 2022-06-14 04:54:20.920697
# Unit test for method __mul__ of class Price
def test_Price___mul__():
    class TestCase(unittest.TestCase):
        def test_some(self):
            m1 = Price.of(USD, 10, Date(2018, 12, 1))
            m2 = m1 * 0.5
            self.assertEqual(m2.ccy, USD)
            self.assertEqual(m2.qty, 5)
            self.assertEqual(m2.dov, Date(2018, 12, 1))

        def test_other_none(self):
            m1 = Price.of(USD, 0, Date(2018, 12, 1))
            m2 = m1 * None
            self.assertEqual(m2, NoPrice)

    return unittest.TestLoader().loadTestsFromTestCase(TestCase)



# Generated at 2022-06-14 04:54:29.445159
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    import decimal as decimal
    import money.money as money
    price = money.Price.of("USD", decimal.Decimal("125.25"), "2018-10-23")
    assert isinstance(price.scalar_add(3), money.Price)
    assert price.scalar_add(3) == money.Price.of("USD", decimal.Decimal("128.25"), "2018-10-23")
    assert price.scalar_add(3.65) == money.Price.of("USD", decimal.Decimal("128.90"), "2018-10-23")
    assert price.scalar_add("25") == money.Price.of("USD", decimal.Decimal("150.25"), "2018-10-23")

# Generated at 2022-06-14 04:54:36.897356
# Unit test for method __ge__ of class Price
def test_Price___ge__():
    assert (SomePrice.of(USD, Decimal('1'), as_date('2019-01-01')) >= SomePrice.of(USD, Decimal('1'), as_date('2019-01-01'))) is True
    assert (NoPrice >= SomePrice.of(USD, Decimal('1'), as_date('2019-01-01'))) is False
    assert (SomePrice.of(USD, Decimal('1'), as_date('2019-01-01')) >= NoPrice) is True
    assert (SomePrice.of(USD, Decimal('1'), as_date('2019-01-01')) >= SomePrice.of(EUR, Decimal('1'), as_date('2019-01-01'))) is True

# Generated at 2022-06-14 04:54:39.217499
# Unit test for method __eq__ of class Money
def test_Money___eq__():
    func = Money.__eq__
    cls  = type(NoMoney)
    return func.__qualname__, cls

# Generated at 2022-06-14 04:54:48.082602
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    ccy1 = Currency("EUR", "978")
    qty1 = Decimal("1.0")
    dov1 = Date(day=12, month=3, year=2017)
    ccy2 = Currency("USD", "840")
    dov2 = Date(day=13, month=3, year=2017)
    sp1 = SomePrice(ccy=ccy1, qty=qty1, dov=dov1)
    class FXRateMock:
        value = Decimal("10.0")
    class FXRateServiceMock:
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool=False) -> Optional[FXRate]:
            return FXRateMock()
    FXRateService.default = FXRateServiceMock()
    expected_result