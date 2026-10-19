

# Generated at 2022-06-14 04:46:56.266921
# Unit test for method with_ccy of class Price
def test_Price_with_ccy():

    ccy = Currency("USD")
    qty = Decimal("100")
    dov = Date("2017-01-01")
    price = Price.of(ccy, qty, dov)

    new_ccy = Currency("EUR")
    new_price = price.with_ccy(new_ccy)

    assert new_price.defined
    assert new_price.ccy == Currency("EUR")
    assert new_price.qty == Decimal("100")
    assert new_price.dov == Date("2017-01-01")

    new_price = NoPrice.with_ccy(new_ccy)

    assert new_price.undefined

test_Price_with_ccy()

# Generated at 2022-06-14 04:47:03.382785
# Unit test for method __le__ of class SomePrice
def test_SomePrice___le__():
    assert (SomePrice("USD", Decimal("10.0"), Date("2018-01-01")) <= \
            SomePrice("USD", Decimal("11.0"), Date("2018-01-02"))) == True
    assert (SomePrice("USD", Decimal("10.0"), Date("2018-01-01")) <= \
            NoPrice) == True
    assert (NoPrice <= \
            SomePrice("USD", Decimal("11.0"), Date("2018-01-02"))) == False
    assert (SomePrice("USD", Decimal("10.0"), Date("2018-01-01")) <= \
            SomePrice("USD", Decimal("10.0"), Date("2018-01-02"))) == True

# Generated at 2022-06-14 04:47:10.801045
# Unit test for method is_equal of class Price
def test_Price_is_equal():
    ccy_nzd = Currency.of('NZD')
    ccy_aud = Currency.of('AUD')
    price1 = Price.of(ccy_nzd, 10, Date(2020, 4, 1))
    price2 = Price.of(ccy_nzd, 10, Date(2020, 4, 1))
    price3 = Price.of(ccy_nzd, 10, Date(2020, 4, 2))
    price4 = Price.of(ccy_aud, 10, Date(2020, 4, 1))
    price5 = Price.of(ccy_nzd, 20, Date(2020, 4, 1))
    price6 = Price.of(ccy_nzd, 10, Date(2020, 4, 1))
    assert price1.is_equal(price2) is True
    assert price2.is_

# Generated at 2022-06-14 04:47:14.769210
# Unit test for method lt of class Money
def test_Money_lt():
    from .commons.types import NA
    from .currencies import USD
    assert NoneMoney.lt(NoneMoney) is NA
    assert SomeMoney(USD, 1, Date.today()).lt(NoneMoney) is NA
    assert NoneMoney.lt(SomeMoney(USD, 1, Date.today())) is False

# Generated at 2022-06-14 04:47:19.766519
# Unit test for method __floordiv__ of class Money
def test_Money___floordiv__():
    from .currencies import USD
    
    money = USD(5.80)
    
    assert (money / 2.0) == USD(2.9)
    assert (money // 2.0) == USD(2.0)
    assert (money // 2) == USD(2.0)

# Generated at 2022-06-14 04:47:22.997901
# Unit test for method __floordiv__ of class Price
def test_Price___floordiv__():
    ccy = Currency.of("USD")
    qty = Decimal("0.10")
    price = Price.of(ccy, qty, TODAY)
    assert price / Decimal("0.01") == Price.of(ccy, Decimal("10.0"), TODAY)

    price = Price.of(ccy, qty, TODAY)
    assert price / 10 == Price.of(ccy, Decimal("0.1"), TODAY)



# Generated at 2022-06-14 04:47:30.685905
# Unit test for method multiply of class Money
def test_Money_multiply():

    # Calculate the profit of a single transaction.
    # We will sell USD for EUR and then buy EUR for USD.
    # In the end, we expect to have the same amount of USD.
    #
    # First, we define some values:
    #
    # * purchase_price = cost to buy EUR 1
    # * exchange_rate = USD/EUR FXRate
    # * margin = profit margin
    #
    # Then, profit can be computed as:
    #
    # * `profit = purchase_price * exchange_rate * (1.0 + margin)`
    #
    # If margin is zero, then there should be no profit.
    #
    # Note that the purchase price and profit is computed in USD.

    from math import isclose

    from .currencies import USD, EUR


# Generated at 2022-06-14 04:47:35.366915
# Unit test for method __pos__ of class Price
def test_Price___pos__():
    # Test 1 - identity operation
    m1 = Money.of(USD, 100)
    assert m1 == +m1
    # Test 2 - undefined identity
    m1 = Money.of(USD, None)
    assert m1 == +m1

# Generated at 2022-06-14 04:47:46.606265
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    # NOQA
    assert Money.of(Currency("USD"), Decimal("1.234"), Date("2020-09-01")).with_dov(Date("2020-10-01")) == \
        Money.of(Currency("USD"), Decimal("1.234"), Date("2020-10-01"))
    assert Money.of(Currency("USD"), Decimal("1.234"), Date("2020-09-01")).with_dov(Date("2020-10-01")) != \
        Money.of(Currency("USD"), Decimal("1.234"), Date("2020-09-01"))
    assert Money.NA.with_dov(Date("2020-10-01")) == Money.NA

# Generated at 2022-06-14 04:47:50.235804
# Unit test for method __sub__ of class Price
def test_Price___sub__():
    a = SomePrice('USD', Decimal('-10000000000000.00'), date(2014, 10, 10))
    b = SomePrice('USD', Decimal('10000000000000.00'), date(2014, 10, 10))
    assert a - b == NoPrice
    a = SomePrice('USD', Decimal('-10.00'), date(2014, 10, 9))
    b = SomePrice('USD', Decimal('10.00'), date(2014, 10, 10))
    c = a - b
    assert c.ccy == 'USD'
    assert c.qty == Decimal('0.00')
    assert c.dov == date(2014, 10, 10)

# Generated at 2022-06-14 04:49:23.190974
# Unit test for method with_dov of class Price
def test_Price_with_dov():
#
# Method with_dov
#
    # Tested method is a pure function, it has no side effects.
#
# Test case 1.
    #
    #
    # Values for test case:
    #
    # date = date(2000,1,1
    #
    #
#
    # Test whether the method returns the expected result:
    #
    assert Price.NA.with_dov(date(2000,1,1)) == Price.NA
#
# Test case 2.
    #
    #
    # Values for test case:
    #
    # date = date(2000,1,1
    #
    #
#
    # Test whether the method returns the expected result:
    #

# Generated at 2022-06-14 04:49:30.613654
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    from decimal import Decimal
    from datetime import date
    from zoopy.currency import USD
    from zoopy.money import Money
    from zoopy.price import Price

    assert (
        Price.of(USD, Decimal('5'), date(2020, 3, 2))
            .scalar_add(Decimal('3'))
            .money
            == Money.of(USD, Decimal('8'), date(2020, 3, 2))
    )

    # Unit test for method scalar_subtract of class Price

# Generated at 2022-06-14 04:49:39.823718
# Unit test for method lt of class Price
def test_Price_lt():
    p1 = Price.of(ccy="USD",qty=30,dov=Date.of(2017,10,31))
    p2 = Price.of(ccy="USD",qty=10,dov=Date.of(2017,10,31))
    if p1.lt(p2):
        print(p1.lt(p2))
    else:
        print(p2.lt(p1))
    p3 = Price.of(ccy="USD",qty=None,dov=Date.of(2017,10,31))
    p4 = Price.of(ccy="USD",qty=10,dov=Date.of(2017,10,31))
    if p3.lt(p4):
        print(p3.lt(p4))

# Generated at 2022-06-14 04:49:46.324280
# Unit test for method __eq__ of class Money
def test_Money___eq__():
    from . import Money, SomeMoney
    from .currencies import USD, GBP, EUR

    # Some money objects:
    gbp = SomeMoney(GBP, 100)
    usd = SomeMoney(USD, 100)
    eur = SomeMoney(EUR, 100)
    unknown = SomeMoney(None, 100)

    # Object equivalence:
    assert gbp == gbp
    assert usd == usd
    assert eur == eur
    assert unknown == unknown

    # Non-object equivalence:
    assert gbp != gbp.ccy
    assert usd != usd.ccy
    assert eur != eur.ccy
    assert unknown != unknown.ccy

    # Equivalence check with NoneMoney:
    assert gbp != None
    assert usd != None
    assert eur != None
   

# Generated at 2022-06-14 04:49:49.331653
# Unit test for method __abs__ of class Price
def test_Price___abs__():
    instance, expected = Price(), Price()
    result = instance.__abs__()
    assert isinstance(result, type(expected))

# Generated at 2022-06-14 04:49:57.742525
# Unit test for method gt of class Price
def test_Price_gt():
    expected_result = True

    result = Price(100, Currency("USD"), Date("1500-01-01")) > Price(1, Currency("USD"), Date("1500-01-01"))
    assert expected_result == result

    result = Price(1, Currency("USD"), Date("1500-01-01")) > Price(100, Currency("USD"), Date("1500-01-01"))
    assert not result

    result = Price(100, Currency("USD"), Date("1500-01-01")) > Price(100, Currency("USD"), Date("1500-01-01"))
    assert not result


# Generated at 2022-06-14 04:50:06.109667
# Unit test for method with_qty of class Money
def test_Money_with_qty():
    class Mock(Money):
        __slots__ = ("ccy", "qty", "dov")
        NA: "Money"
        ccy: Currency
        qty: Decimal
        dov: Date
        defined: bool
        undefined: bool

        def __init__(self, ccy: Currency, qty: Decimal, dov: Date):
            self.ccy = ccy
            self.qty = qty
            self.dov = dov

        def is_equal(self, other: Any) -> bool:
            return False  # pragma: no cover

        def as_boolean(self) -> bool:
            return False  # pragma: no cover

        def as_float(self) -> float:
            return float(self.qty)  # pragma: no cover


# Generated at 2022-06-14 04:50:09.400638
# Unit test for method subtract of class Price
def test_Price_subtract():
    assert Price.of(usd, 100, dt).subtract(Price.of(usd, 25, dt)) == Price.of(usd, 75, dt)



# Generated at 2022-06-14 04:50:10.905450
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():
    pass
    # c, q, d = self
    # dec = c.decimals
    # return SomeMoney(c, q.__round__(ndigits if ndigits < dec else dec), d)

# Generated at 2022-06-14 04:50:14.374019
# Unit test for method gt of class Money
def test_Money_gt():
    """
    Unit test for method gt of class Money
    """
    obj = Money(12,"USD", "2019-07-07")
    obj2 = Money(10,"USD", "2019-07-07")
    obj.gt(obj2)==True
    

# Generated at 2022-06-14 04:51:02.832801
# Unit test for method add of class Price
def test_Price_add():
    import docdifferent.acl as acl
    import docdifferent.money as money

    acl.set_system_date(datetime.datetime(2018, 12, 28, 0, 0))  # Needed for runnning this particular test.

    # scenario 1
    m1 = money.Money.of(Currency("GBP"), 100, Date("2018-12-31"))
    m2 = money.Money.of(Currency("GBP"), 200, Date("2018-12-31"))

    # expectations
    expect = money.Money.of(Currency("GBP"), 300, Date("2018-12-31"))
    assert m1.add(m2) == expect

    # scenario 2
    m1 = money.Money.of(Currency("GBP"), 100, Date("2018-12-31"))
    m2 = money.Money

# Generated at 2022-06-14 04:51:05.752420
# Unit test for method __lt__ of class Money
def test_Money___lt__():
    assert Money(ccy=None, qty=None, dov=None) < Money(ccy=None, qty=None, dov=None)



# Generated at 2022-06-14 04:51:14.397986
# Unit test for method convert of class SomeMoney
def test_SomeMoney_convert():
    from cashflow.currency import Currency, CurrencyConversionError
    from cashflow.date import Date
    from cashflow.service import EXTERNAL_WEB_SERVICE_IMPLEMENTATION
    from cashflow.service.web import WebServiceError
    from cashflow.service.web import web_service as fxr_service

    ## Default currency conversion:
    c = Currency.USD
    d = Date.today()
    m = SomeMoney(ccy=c, qty=1, dov=d)
    assert m.convert(Currency.USD, d) == SomeMoney(ccy=Currency.USD, qty=1, dov=d)

# Generated at 2022-06-14 04:51:15.988733
# Unit test for method gt of class Price
def test_Price_gt():
    assert (Price.NA > Price.NA) == False


# Generated at 2022-06-14 04:51:16.855910
# Unit test for method __gt__ of class SomeMoney
def test_SomeMoney___gt__():
    pass


# Generated at 2022-06-14 04:51:27.833640
# Unit test for method negative of class Money
def test_Money_negative():
    assert Money.NA.negative() == Money.NA
    assert Money.of(Currency.USD, 100, Date(2018, 1, 1)).negative().ccy is Currency.USD
    assert Money.of(Currency.USD, -100, Date(2018, 1, 1)).negative().ccy is Currency.USD
    assert Money.of(Currency.USD, 100, Date(2018, 1, 1)).negative().qty == -100
    assert Money.of(Currency.USD, -100, Date(2018, 1, 1)).negative().qty == 100
    assert Money.of(Currency.USD, 100, Date(2018, 1, 1)).negative().dov is Date(2018, 1, 1)

# Generated at 2022-06-14 04:51:36.785430
# Unit test for method __sub__ of class Price
def test_Price___sub__():
    """Unit test for method __sub__ of class Price"""
    assert Price(Currency('EUR'), Decimal('1'), Date('2018-01-01')) - Price(Currency('EUR'), Decimal('1'), Date('2018-01-01')) == Price(Currency('EUR'), Decimal('0'), Date('2018-01-01'))
    assert Price(Currency('EUR'), Decimal('1'), Date('2018-01-01')) - Price(Currency('USD'), Decimal('3'), Date('2018-01-01')) == Price(Currency('EUR'), Decimal('-2'), Date('2018-01-01'))
    assert NonePrice() - Price(Currency('EUR'), Decimal('1'), Date('2018-01-01')) == NonePrice()

# Generated at 2022-06-14 04:51:44.075043
# Unit test for method __le__ of class Money
def test_Money___le__():
    """
    Tests :py:meth:`Money.__le__` method.
    """
    assert SomeMoney(GBP, 1, TODAY) <= SomeMoney(GBP, 1, TODAY)
    assert SomeMoney(GBP, 1, TODAY) <= SomeMoney(GBP, 2, TODAY)
    with raises(IncompatibleCurrencyError):
        SomeMoney(GBP, 1, TODAY) <= SomeMoney(USD, 1, TODAY)



# Generated at 2022-06-14 04:51:51.019777
# Unit test for method divide of class Money
def test_Money_divide():
    import decimal
    import pytest
    from pytest_mock import MockerFixture
    from datetime import datetime

    from financepy.products.funding.Money import Money
    from financepy.products.funding.Currencies import Currency
    from financepy.products.funding.EuroDollarFutures import EuroDollarFutures
    from financepy.products.funding.EuroDollarFutures import EuroDollarContract

    from financepy.products.funding.FXRates import FXRates
    from financepy.products.funding.FXRate import FXRate
    from financepy.products.funding.EuroDollarFutures import EuroDollarFutures
    from financepy.products.funding.EuroDollarFutures import EuroDollarContract
    from financepy.finutils.FinDate import FinDate


# Generated at 2022-06-14 04:51:55.822638
# Unit test for method with_qty of class Price
def test_Price_with_qty():
    p = Price.of(Currency.USD, Decimal('1.0'), Date.today())
    assert p == p.with_qty(Decimal('1.0'))
    assert p != p.with_qty(Decimal('1.000'))

