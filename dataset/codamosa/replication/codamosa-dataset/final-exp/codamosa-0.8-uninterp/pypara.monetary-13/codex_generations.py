

# Generated at 2022-06-14 04:46:45.408906
# Unit test for method __eq__ of class Price
def test_Price___eq__():
    assert Price.of(ccy='USD', qty='10', dov='2018-12-01') == Price.of(ccy='USD', qty='10', dov='2018-12-01')
    assert Price.of(ccy='USD', qty='10', dov='2018-12-01') == Price.of(ccy='USD', qty='10.000', dov='2018-12-01')
    assert Price.of(ccy='USD', qty='10', dov='2018-12-01') != Price.of(ccy='INR', qty='10', dov='2018-12-01')

# Generated at 2022-06-14 04:46:56.695896
# Unit test for method __eq__ of class Price
def test_Price___eq__():
    some_price = Price.of(USD, Decimal("1"), datetime.date(2012, 1, 1))
    assert some_price == Price.of(USD, Decimal("1"), datetime.date(2012, 1, 1))
    assert some_price == Price.of(USD, 1, datetime.date(2012, 1, 1))

    assert some_price != Price.of(USD, Decimal("2"), datetime.date(2012, 1, 1))
    assert some_price != Price.of(EUR, Decimal("1"), datetime.date(2012, 1, 1))
    assert some_price != Price.of(USD, Decimal("1"), datetime.date(2013, 1, 1))
    assert some_price != Price.of(USD, Decimal("1"), datetime.date(2012, 2, 1))

# Generated at 2022-06-14 04:47:04.442703
# Unit test for method subtract of class Price
def test_Price_subtract():
    A1 = Price.of(CCY['AUD'], Decimal(10), date(2019,11,22))
    A2 = Price.of(CCY['AUD'], Decimal(20), date(2019,11,22))
    A3 = A2.subtract(A1)
    assert A3.defined == True
    assert A3.ccy.code == 'AUD'
    assert A3.qty == Decimal(10)
    assert A3.dov == date(2019,11,22)


# Generated at 2022-06-14 04:47:05.890280
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    return True


# Generated at 2022-06-14 04:47:10.088905
# Unit test for method with_dov of class NonePrice
def test_NonePrice_with_dov():
    """
    Test `with_dov` method of class `NonePrice`
    """
    d = NonePrice.with_dov(Date(21, 8, 2019))
    assert_equal(d, NoPrice)

# Generated at 2022-06-14 04:47:13.383366
# Unit test for method positive of class Money
def test_Money_positive():
    assert NoneMoney.positive() is NoneMoney
    assert NoMoney.positive() is NoMoney
    assert SomeMoney(ccy1, qty, dov).positive() == SomeMoney(ccy1, qty, dov)



# Generated at 2022-06-14 04:47:21.277099
# Unit test for method convert of class Price
def test_Price_convert():
    test_ccy = "USD"
    test_qty = Decimal('1.0')
    test_dov = Date(year = 2018, month = 2, day = 2)
    price_USD = SomePrice(test_ccy, test_qty, test_dov)
    price_USD_converted = price_USD.convert("EUR")
    assert price_USD_converted.ccy == "EUR"
    assert price_USD_converted.qty == Decimal('0.907793565991732')
    assert price_USD_converted.dov == test_dov

    test_qty = Decimal('0.0')
    price_USD = SomePrice(test_ccy, test_qty, test_dov)

# Generated at 2022-06-14 04:47:30.236013
# Unit test for method __ge__ of class Money
def test_Money___ge__():
    # Given
    ccy1 = Currency.USD
    a = Money.of(ccy1, Decimal('1.0'), Date.now())
    ccy2 = Currency.USD
    b = Money.of(ccy2, Decimal('1.0'), Date.now())
    ccy3 = Currency.GBP
    c = Money.of(ccy3, Decimal('1.0'), Date.now())

    # When
    result1 = a.__ge__(b)
    result2 = a.__ge__(c)

    # Then
    assert result1,'Money.__ge__: a >= b'
    assert result2, 'Money.__ge__: a >= c'

# Generated at 2022-06-14 04:47:32.276684
# Unit test for method positive of class Money
def test_Money_positive():
    m1 = Money.of(Currency.USD, 10, Date.today())
    a1 = Money.of(Currency.USD, 10, Date.today())
    assert m1.positive() == a1


# Generated at 2022-06-14 04:47:34.110528
# Unit test for method with_dov of class NonePrice
def test_NonePrice_with_dov():
    from datetime import date

    d = date(2020, 1, 1)
    p = NoPrice.with_dov(d)
    assert p.undefined


## Singleton instance:
NoPrice: Price = NonePrice()

# Generated at 2022-06-14 04:48:41.590228
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():
    """
    Tests method SomeMoney.round
    """

    ## We need to import the object first:
    from freight_money import SomeMoney

    ## Import some helpers:
    from freight_forwarder.utils import Money, dt_to_date
    from datetime import date

    ## Try some roundings:
    assert SomeMoney(Money.usd, 1, dt_to_date(date(2000, 1, 1))).round() == SomeMoney(Money.usd, 1, dt_to_date(date(2000, 1, 1)))
    assert SomeMoney(Money.usd, 1.1, dt_to_date(date(2000, 1, 1))).round() == SomeMoney(Money.usd, 1, dt_to_date(date(2000, 1, 1)))

# Generated at 2022-06-14 04:48:43.692829
# Unit test for method as_float of class Price
def test_Price_as_float():
    assert Price.of('USD', 100, Date(2018, 1, 1)).as_float() == float(100)



# Generated at 2022-06-14 04:48:56.021472
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    ## Data:
    p1: Decimal = Decimal("1.2")
    p2: Decimal = Decimal("5")
    p3: Decimal = Decimal("346.25")
    c1: Currency = Currency.parse("GBP")
    c2: Currency = Currency.parse("USD")
    c3: Currency = Currency.parse("EUR")
    date1: Date = Date(2018, 1, 11)
    date2: Date = Date(2018, 4, 22)
    date3: Date = Date(2000, 12, 24)

    ## Some prices:
    s1: SomePrice = SomePrice(c1, p1, date1)
    s2: SomePrice = SomePrice(c2, p2, date2)
    s3: SomePrice = SomePrice(c3, p3, date3)

# Generated at 2022-06-14 04:49:00.093185
# Unit test for method __add__ of class SomeMoney
def test_SomeMoney___add__():
    class TestDummy(object):
        pass
    dummy_instance = TestDummy()

    ## TODO: Complete.
    NotImplemented
    try:
        pass
    except:
        pass

# Generated at 2022-06-14 04:49:02.103392
# Unit test for method __int__ of class Price
def test_Price___int__():
    assert Price.of(USD, Decimal("1"), Date.now()) == Decimal("1")

# Generated at 2022-06-14 04:49:03.433400
# Unit test for method __neg__ of class Price
def test_Price___neg__():
    expected = Price.of(Currency.USD, Decimal("-0.10"))
    actual = -Price.of(Currency.USD, Decimal("+0.10"))
    assert expected == actual



# Generated at 2022-06-14 04:49:07.649568
# Unit test for method __lt__ of class SomePrice
def test_SomePrice___lt__():
    p1 = Price.of(USD, 1, Date.now()).reify()
    p2 = Price.of(USD, 2, Date.now()).reify()
    assert p1 < p2
    assert not (p1 < p1)

    p1 = Price.of(USD, 1, Date.now()).reify()
    p2 = Price.of(GBP, 2, Date.now()).reify()
    with pytest.raises(IncompatibleCurrencyError):
        p1 < p2

    assert not (NoPrice < NoPrice)
    assert not (NoPrice < p2)
    assert p2 > NoPrice
    assert p2 >= NoPrice

    p1 = Price.of(USD, 1, Date.now()).reify()
    assert p1 > NoPrice

# Generated at 2022-06-14 04:49:11.520746
# Unit test for method gt of class Money
def test_Money_gt():
    from .currencies import Currency
    from .commons.numbers import Zero

    assert(Money.of(Currency.USD, Zero, Date.now()) > Money.of(Currency.EUR, Zero, Date.now()))


# Generated at 2022-06-14 04:49:14.728134
# Unit test for method __bool__ of class Price
def test_Price___bool__():
    price = Price()
    price.ccy = Currency("USD")
    price.qty = Decimal("12.36")
    price.dov = Date.week(2017, 50)

    assert price.__bool__() is True



# Generated at 2022-06-14 04:49:27.160698
# Unit test for method multiply of class Price
def test_Price_multiply():
    assert Price.NA * 1 == Price.NA
    assert Price.NA * -1 == Price.NA
    assert Price.NA * 0 == Price.NA
    assert Price.NA * 0.0 == Price.NA
    assert Price.NA * Decimal() == Price.NA
    assert Price.NA * Decimal('0') == Price.NA
    assert Price.NA * Decimal('-1') == Price.NA
    assert Price.NA * Decimal('1') == Price.NA
    assert Currency('USD') * Price.NA == Price.NA
    assert Price.NA * Currency('USD') == Price.NA
    assert Price.NA * Price.NA == Price.NA

# Generated at 2022-06-14 04:49:57.023198
# Unit test for method __gt__ of class Price
def test_Price___gt__():
    """Test case for method __gt__ of class Price."""
    pass

# Generated at 2022-06-14 04:50:05.690243
# Unit test for method as_boolean of class Price
def test_Price_as_boolean():
    assert NoPrice.as_boolean() is False
    assert SomePrice(USD, Decimal(0), Date(1, 1, 1)).as_boolean() is False
    assert SomePrice(USD, Decimal(1), Date(1, 1, 1)).as_boolean() is True
    assert SomePrice(USD, Decimal(1.1), Date(1, 1, 1)).as_boolean() is True
    assert SomePrice(USD, Decimal("-100.100"), Date(1, 1, 1)).as_boolean() is False
    assert SomePrice(USD, Decimal("100.100"), Date(1, 1, 1)).as_boolean() is True
    assert SomePrice(USD, Decimal("-100.1"), Date(1, 1, 1)).as_boolean() is False

# Generated at 2022-06-14 04:50:16.289835
# Unit test for method __lt__ of class Price
def test_Price___lt__():

    btc = Currency.of("BTC")
    usd = Currency.of("USD")
    dov = Date.of(2019, 8, 19)

    # undefined, defined, defined
    assert Price.of(None, None, None) < Price.of(btc, Decimal("1"), dov)
    assert Price.of(None, None, None) < Price.of(btc, Decimal("1"), None)

    # defined, undefined, defined
    assert not Price.of(usd, Decimal("1"), dov) < Price.of(None, None, None)
    assert not Price.of(usd, Decimal("1"), None) < Price.of(None, None, None)

    # defined, defined, undefined

# Generated at 2022-06-14 04:50:25.476761
# Unit test for method is_equal of class Price
def test_Price_is_equal():
    assert Price.of(ccy=None, qty=None, dov=None).is_equal(CcyQty(ccy="EUR", qty=Decimal(100), dov=Date(2018, 12, 12))) == False
    assert Price.of(ccy=None, qty=None, dov=None).is_equal(CcyQty(ccy=None, qty=Decimal(100), dov=Date(2018, 12, 12))) == False
    assert Price.of(ccy=None, qty=None, dov=None).is_equal(CcyQty(ccy="EUR", qty=None, dov=Date(2018, 12, 12))) == False

# Generated at 2022-06-14 04:50:30.246086
# Unit test for method __truediv__ of class Price
def test_Price___truediv__():
    import pytest

    with pytest.raises(TypeError):
        NoPrice / SomeMoney

    with pytest.raises(TypeError):
        SomePrice / NoMoney

    with pytest.raises(TypeError):
        SomePrice / SomeMoney

    with pytest.raises(TypeError):
        SomeMoney / SomePrice

    actual = SomePrice.of(EUR, 1.0, Date.today()) / SomePrice.of(EUR, 2.0, Date.today())
    assert actual == SomePrice.of(EUR, 1.0 / 2.0, Date.today())



# Generated at 2022-06-14 04:50:32.858047
# Unit test for method __eq__ of class Price
def test_Price___eq__():
    price = Price()
    assert price == price



# Generated at 2022-06-14 04:50:43.441462
# Unit test for method __floordiv__ of class Price
def test_Price___floordiv__():
    from pricers.monetary import Price
    from datetime import date
    from datetime import datetime
    from datetime import timedelta
    from decimal import Decimal
    from enum import Enum
    from pricers.currencies import Currency

    class DataPoint(Enum):
        EMPTY = ()
        SOME = (Currency.CAD, '1.1', date.today())
        SOME_OTHER = (Currency.CAD, '1.1', date.today() + timedelta(days = 1))
        SOME_OTHER_YET = (Currency.USD, '1.1', date.today())
        SOME_OTHER_YET_AGAIN = (Currency.CAD, '2.1', date.today())

    for data_point in DataPoint:
        if data_point == DataPoint.EMPTY:
            price

# Generated at 2022-06-14 04:50:47.188317
# Unit test for method as_boolean of class Money
def test_Money_as_boolean():
    assert Money.NA.as_boolean() is False
    assert Money.NA.is_equal(Money.NA)
    assert Money.NA.as_boolean() == Money.NA.as_boolean()
    assert Money.NA != Money.of(Currency("USD"), Decimal("0.00"), Date(2016, 3, 30))


# Generated at 2022-06-14 04:50:51.048996
# Unit test for method __mul__ of class Money
def test_Money___mul__():
    # Money.__mul__(self, other):
    #
    # Note that undefined money object is returned as is.
    #
    money1 = Money.of("USD", 100)
    assert money1 * 10 == Money.of("USD", 1000)
    assert money1 * 0 == Money.of("USD", 0)



# Generated at 2022-06-14 04:50:54.756964
# Unit test for method with_qty of class Price
def test_Price_with_qty():
    assert NoPrice.with_qty(Decimal(1)) is NoPrice
    assert SomePrice(CAD, Decimal(1), Date(2015, 12, 31)).with_qty(Decimal(2)) == SomePrice(CAD, Decimal(2), Date(2015, 12, 31))




# Generated at 2022-06-14 04:52:14.236626
# Unit test for method __ge__ of class Money
def test_Money___ge__():
    '''
    Tests method __ge__ of class Money
    '''
    _fx_rate_service = None  # type: ignore
    _money_defined = SomeMoney(ccy=Currency('USD'), qty=Decimal(1), dov=Date(2016, 1, 1))
    _money_undefined = NoMoney
    _money_other = SomeMoney(ccy=Currency('USD'), qty=Decimal(1), dov=Date(2015, 1, 1))
    _money_other_incompatible = SomeMoney(ccy=Currency('EUR'), qty=Decimal(1), dov=Date(2015, 1, 1))

    assert not (_money_undefined >= _money_undefined)
    assert not (_money_undefined >= _money_other)

# Generated at 2022-06-14 04:52:19.687767
# Unit test for method with_qty of class Price
def test_Price_with_qty():
    import re
    import decimal
    import math

    someprice = SomePrice(Currency.USD, Decimal(0.0), Date(2019, 12, 31))
    assert someprice.with_qty(Decimal(1.2)).qty == Decimal(1.2)
    print("testing method with_qty of class Price succeeded")

if __name__ == "__main__":
    test_Price_with_qty()



# Generated at 2022-06-14 04:52:25.988924
# Unit test for method add of class Money
def test_Money_add():
    """
    Covers:

        Money(100, "USD", Date(01, 01, 2018)) +
        Money(100, "USD", Date(01, 01, 2018))
    """
    assert Money(100, "USD", Date(1, 1, 2018)) + Money(100, "USD", Date(1, 1, 2018)) == Money(200, "USD", Date(1, 1, 2018))



# Generated at 2022-06-14 04:52:26.647085
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    pass

# Generated at 2022-06-14 04:52:34.145106
# Unit test for method with_dov of class Price
def test_Price_with_dov():
    print("Testing Price.with_dov...", end="")
    assert Price.of(USD, 1, TODAY).with_dov(TOMORROW) == Price.of(USD, 1, TOMORROW)
    assert Price.of(USD, 1, TODAY).with_dov(None) == Price.of(USD, 1, TODAY)
    assert NoPrice.with_dov(TOMORROW) == NoPrice
    print("Passed.")



# Generated at 2022-06-14 04:52:44.697090
# Unit test for method gte of class Money
def test_Money_gte():
    class Money(Money):
        pass
    Money.NA = Money.of(None, None, None)

    assert Money.NA.gte(Money(Currency("TRY"), Decimal("10.00"), Date("2017-11-01")))

    assert Money(Currency("TRY"), Decimal("20.00"), Date("2017-11-01")).gte(Money.NA)

    with pytest.raises(IncompatibleCurrencyError):
        Money(Currency("TRY"), Decimal("20.00"), Date("2017-11-01")).gte(
            Money(Currency("USD"), Decimal("20.00"), Date("2017-11-01"))
        )


# Generated at 2022-06-14 04:52:50.283862
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():
    ccy = Currency("USD")
    s = SomeMoney(ccy, Decimal("1234567.89"), Date(2019, 12, 31))
    r = s.round()
    assert r.ccy == ccy
    assert r.qty == Decimal("1234568")
    assert r.dov == s.dov
    r = s.round(3)
    assert r.ccy == ccy
    assert r.qty == Decimal("1234567.890")
    assert r.dov == s.dov
    r = s.round(4)
    assert r.ccy == ccy
    assert r.qty == Decimal("1234567.8900")
    assert r.dov == s.dov
    r = s.round(-3)
    assert r.ccy == c

# Generated at 2022-06-14 04:52:56.329215
# Unit test for method is_equal of class Money
def test_Money_is_equal():
    from .currencies import USD
    from .commons.time import Date
    from .money import Money

    usd_1 = Money.of(USD, Decimal(1), Date(1, 1, 1))
    usd_2 = Money.of(USD, Decimal(1), Date(1, 1, 1))
    assert usd_1.is_equal(usd_2)



# Generated at 2022-06-14 04:53:04.321724
# Unit test for method with_dov of class Price
def test_Price_with_dov():
    # given
    ccyUSD = Currency.get_ccy_by_mnemonic("USD")
    ccyEUR = Currency.get_ccy_by_mnemonic("EUR")

    monUSD = Money.of(ccyUSD, Decimal("10"))
    monEUR = Money.of(ccyEUR, Decimal("10"))

    # when
    pUSD = Price.of(ccyUSD, Decimal("10"), Date("2018-08-21"))
    pEUR = Price.of(ccyEUR, Decimal("10"), Date("2018-08-21"))

    pUSD2 = pUSD.with_dov(Date("2018-08-24"))
    pEUR2 = pEUR.with_dov(Date("2018-08-24"))

    # then
    assert pUSD2.cc

# Generated at 2022-06-14 04:53:08.568725
# Unit test for method __le__ of class SomeMoney
def test_SomeMoney___le__():

    ## This is how to define undefined money:
    assert NoMoney.__le__(NoMoney)  # type: ignore

    ## This is how to define some money:
    some_money: Money = SomeMoney(USD, 100, TODAY)
    assert some_money.__le__(some_money)  # type: ignore

    ## If the right operand is undefined:
    assert not some_money.__le__(NoMoney)  # type: ignore

    ## If the right operand is a different currency:
    with pytest.raises(IncompatibleCurrencyError):
        some_money.__le__(SomeMoney(EUR, 100, TODAY))  # type: ignore

    ## If the right operand is the same currency:
    assert some_money.__le__(SomeMoney(USD, 200, TODAY))  # type: ignore


# Generated at 2022-06-14 04:53:42.311520
# Unit test for method convert of class Money
def test_Money_convert():
    """
    Unit test for method convert of class Money
    """
    some_usd = SomeMoney(currencies.USD, 4, Date(2020, 3, 2))
    some_usd.convert(currencies.USD, Date(2020, 3, 1))
    some_usd.convert(currencies.GBP, Date(2020, 3, 1))
    some_usd.convert(currencies.GBP, Date(2020, 3, 2))
    some_usd.convert(currencies.GBP, Date(2020, 3, 3))
    # Unit test for method is_equal of class Money
    def test_Money_is_equal():
        """
        Unit test for method is_equal of class Money
        """

# Generated at 2022-06-14 04:53:43.927936
# Unit test for method __ge__ of class Money
def test_Money___ge__(): pass    # Raises NotImplementedError

# Generated at 2022-06-14 04:53:50.582406
# Unit test for method lte of class Money
def test_Money_lte():
    import datetime
    assert (NoMoney <= NoMoney)
    assert (NoMoney <= SomeMoney(Currency("USD"), Decimal("100"), datetime.date(2017, 1, 1)))
    assert (SomeMoney(Currency("USD"), Decimal("100"), datetime.date(2017, 1, 1)) <= SomeMoney(Currency("USD"), Decimal("100"), datetime.date(2017, 1, 1)))

# Generated at 2022-06-14 04:53:57.967150
# Unit test for method add of class Money
def test_Money_add():
    assert (SomeMoney(USD, 100, DATE_2019_01_15) + SomeMoney(USD, 200, DATE_2019_01_10) == SomeMoney(USD, 300,
                                                                                                     DATE_2019_01_15))
    assert (SomeMoney(USD, 100, DATE_2019_01_15) + SomeMoney(EUR, 200, DATE_2019_01_10) == NoMoney)
    assert (SomeMoney(USD, 100, DATE_2019_01_15) + SomeMoney(EUR, 200, DATE_2019_01_10) == NoMoney)
    assert (SomeMoney(USD, 100, DATE_2019_01_15) + NoMoney == SomeMoney(USD, 100, DATE_2019_01_15))

# Generated at 2022-06-14 04:54:06.809872
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    assert SomePrice(GBP, 1, "2019-01-01").convert(USD) == SomePrice(USD, 1.3, "2019-01-01")
    with pytest.raises(IncompatibleCurrencyError):
        assert SomePrice(GBP, 1, "2019-01-01").convert(CHF, strict=True)
    with pytest.raises(FXRateLookupError):
        assert SomePrice(GBP, 1, "2019-01-01").convert(CHF, strict=True)


# Generated at 2022-06-14 04:54:12.878428
# Unit test for method convert of class Price
def test_Price_convert():
    curr = 'SGD'
    qty = Decimal('10')
    dov = Date(1,1,2020)
    prc = Price.of(curr, qty, dov)
    assert prc.convert('HBD') == NoPrice

# Generated at 2022-06-14 04:54:15.388589
# Unit test for method with_dov of class NonePrice
def test_NonePrice_with_dov():
    ## Test undefined price
    actual = NoPrice.with_dov(date(2019, 9, 5))
    assert actual == NoPrice

    ## Test defined price
    actual = SomePrice(eur, 10.0, date(2020, 1, 1)).with_dov(date(2019, 9, 5))
    assert actual == SomePrice(eur, 10.0, date(2019, 9, 5))



# Generated at 2022-06-14 04:54:18.272681
# Unit test for method __ge__ of class Money
def test_Money___ge__():
    """
    Unit test for method __ge__ of class Money
    """
    raise NotImplementedError()



# Generated at 2022-06-14 04:54:26.534770
# Unit test for method with_ccy of class Price
def test_Price_with_ccy():
    from xbbg.currencies import USD, EUR
    from xbbg.fields import PriceField
    from xbbg.core import Price, Money, Currency

    assert Price(USD, 1).with_ccy(EUR) == Price(EUR, 1)
    assert Price(USD, 1, 1).with_ccy(EUR) == Price(EUR, 1, 1)
    assert Price(USD, 1, 2).with_ccy(EUR) == Price(EUR, 1, 2)
    assert Price(USD, 1, 3).with_ccy(EUR) == Price(EUR, 1, 3)



# Generated at 2022-06-14 04:54:32.944568
# Unit test for method __le__ of class SomeMoney
def test_SomeMoney___le__():
    from quantumpay.banking.domain import fxrates

    with fxrates.register('EUR', 'USD', at=Date(2020, 5, 9), value=1.09):
        assert SomeMoney(EUR, Decimal('1'), asof=Date(2020, 6, 1)) <= SomeMoney(USD, Decimal('1'), asof=Date(2020, 6, 1))

