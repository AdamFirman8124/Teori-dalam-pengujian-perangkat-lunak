

# Generated at 2022-06-14 04:49:22.511388
# Unit test for method scalar_add of class Money
def test_Money_scalar_add():
    """
    Checks if the method scalar_add works as expected.
    """
    from .currencies import Currency, USD
    from .pricing import Money, NoMoney
    from .exchange import FXRateService

    ## Define a simple FX rate service with an explicit FX rate between EUR and USD:
    fxs = FXRateService(dov="2019-01-01", rates={"EUR/USD": 1.2})

    ## Non-existent money should yield no money:
    assert (NoMoney.scalar_add(2) == NoMoney)
    assert (NoMoney.scalar_add(-1.0) == NoMoney)

    ## A money with 0 quantity should yield same money:
    m1 = Money.of(USD, 0, "1990-01-01")

# Generated at 2022-06-14 04:49:25.540351
# Unit test for method __add__ of class Price
def test_Price___add__():
    # Given
    price1 = Price.of(ccy=USD, qty=Decimal('5'), dov=Date(2013, 1, 1))
    price2 = Price.of(ccy=USD, qty=Decimal('10'), dov=Date(2013, 1, 1))

    # When
    result = price1.__add__(price2)

    # Then
    assert result == Price.of(USD, Decimal('15'), Date(2013, 1, 1))

# Generated at 2022-06-14 04:49:28.412829
# Unit test for method positive of class Money
def test_Money_positive():
    # Test for method positive of class Money
    sut = MoneyFactory.of("USD", 2.0)
    assert sut is sut.positive()

# Generated at 2022-06-14 04:49:38.640901
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    a = SomePrice(Currency.USD, Decimal('5'), Date(2020, 1, 20))
    b = SomePrice(Currency.USD, Decimal('3'), Date(2020, 1, 20))
    c = SomePrice(Currency.CAD, Decimal('3'), Date(2020, 1, 20))
    assert a.convert(Currency.USD) == a
    assert b.convert(Currency.USD) == b
    assert c.convert(Currency.CAD) == c
    assert a.convert(Currency.CAD) == None
    assert b.convert(Currency.CAD) == None
    assert c.convert(Currency.USD) == None
    assert a.convert(Currency.CAD, Date(2020,1,20), True) == None

# Generated at 2022-06-14 04:49:47.627622
# Unit test for method with_ccy of class Money
def test_Money_with_ccy():
    m1 = Money.of(Currency.USD, 0.10, Date(2020, 4, 1))
    # Calling with_ccy on defined money
    m2 = m1.with_ccy(Currency.GBP)
    assert m2.ccy == Currency.GBP
    assert m2.qty == 0.10
    assert str(m2.dov) == "2020-04-01"
    # Calling with_ccy on undefined money
    m3 = NoMoney.with_ccy(Currency.GBP)
    assert isinstance(m3, NoMoney)
    # Calling with_ccy with None values
    m4 = Money.of(Currency.USD, 0.10, Date(2020, 4, 1))
    m5 = m4.with_ccy(None)

# Generated at 2022-06-14 04:49:59.150519
# Unit test for method __int__ of class Price
def test_Price___int__():
    assert Price.of(ccy="USD", qty=Decimal("1.23"), dov=Date.ofEpochDay(0)).__int__() == 1
    assert Price.of(ccy="USD", qty=Decimal("1.23"), dov=Date.ofEpochDay(0)).__int__() == 1
    assert Price.of(ccy="USD", qty=-Decimal("1.23"), dov=Date.ofEpochDay(0)).__int__() == -1
    assert Price.of(ccy="USD", qty=Decimal("1.75"), dov=Date.ofEpochDay(0)).__int__() == 1

# Generated at 2022-06-14 04:50:11.883965
# Unit test for method lt of class Money
def test_Money_lt():
    assert Money.of(ccy="USD", qty=1.0, dov=Date(1, 1, 2000)) < Money.of(ccy="USD", qty=1.1, dov=Date(2, 1, 2000))
    assert Money.of(ccy="USD", qty=1.0, dov=Date(1, 1, 2000)) < Money.of(ccy="USD", qty=1.0, dov=Date(2, 1, 2000))
    assert Money.of(ccy="USD", qty=1.0, dov=Date(1, 1, 2000)) < Money.of(ccy="USD", qty=1.0, dov=Date(2, 1, 2000))

# Generated at 2022-06-14 04:50:16.389171
# Unit test for method __ge__ of class Money
def test_Money___ge__():
    from .currencies import USD
    from .money import Money
    from .zeitgeist import Date

    object_0 = Money.of(USD, 100, Date.today())
    object___ge__1 = object_0.__ge__(None)

    assert object___ge__1 == NotImplemented


# Generated at 2022-06-14 04:50:20.844926
# Unit test for method multiply of class Money
def test_Money_multiply():
    USD = Currency.of("USD")
    money = USD.money(10.0)
    
    assert money.multiply(2.0) == USD.money(20.0)
    assert money.multiply(Decimal(2.0)) == USD.money(20.0)

# Generated at 2022-06-14 04:50:22.865280
# Unit test for method __float__ of class Price
def test_Price___float__():
    assert float(Price.of(USDCur, Decimal("1.1"), Date(2020, 11, 1))) == 1.1

# Generated at 2022-06-14 04:51:59.705401
# Unit test for method as_integer of class Price
def test_Price_as_integer():
    for fp in (0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.9):
        assert Price.of(GBP, Decimal(fp), today).as_integer() == 1
        assert Price.of(GBP, Decimal(-fp), today).as_integer() == -1
        assert Price.of(USD, Decimal(fp), today).as_integer() == 1
        assert Price.of(USD, Decimal(-fp), today).as_integer() == -1
        assert Price.of(JPY, Decimal(fp), today).as_integer() == 0
        assert Price.of(JPY, Decimal(-fp), today).as_integer() == 0
    assert NoPrice.as_integer() == 0

# Unit tests for method as_float of class Price

# Generated at 2022-06-14 04:52:04.055332
# Unit test for method __eq__ of class Money
def test_Money___eq__():
    assert (
        SomeMoney(ccy=EUR, qty=100 * EUR.amount, dov=Date.today()) == Money.of(EUR, 100, Date.today())
    )


# Generated at 2022-06-14 04:52:10.044513
# Unit test for method convert of class SomeMoney
def test_SomeMoney_convert():
    from datetime import date

    from finx.currencies import AUD, NZD

    ## Construct a new SomeMoney object:
    x = SomeMoney(AUD, Decimal("1"), date(2020, 1, 1))

    ## Convert to NZD:
    y = x.convert(NZD, date(2020, 1, 2))

    assert y == SomeMoney(NZD, Decimal("1"), date(2020, 1, 2))

# Generated at 2022-06-14 04:52:13.513079
# Unit test for method __le__ of class Money
def test_Money___le__():
    assert Money.of(Currency.USD, Decimal(1), Date.today()) <= Money.of(Currency.USD, Decimal(2), Date.today())


# Generated at 2022-06-14 04:52:15.028800
# Unit test for method __gt__ of class Money
def test_Money___gt__():
    """
    Test method __gt__ of class Money
    """
    pass



# Generated at 2022-06-14 04:52:18.438292
# Unit test for method __pos__ of class Money
def test_Money___pos__():
    import pytest
    from money import Money
    
    # Call the __pos__ method
    money: Money = Money.of(None, None, None)
    returned = money.__pos__()
    assert bool(returned) is False


# Generated at 2022-06-14 04:52:29.869051
# Unit test for method is_equal of class Money
def test_Money_is_equal():
    """
    Runs the unit-tests for :func:`Money.is_equal` method.
    """
    import pytest

    from .currencies import Currency
    from .monetary import Money

    with pytest.raises(TypeError):
        Money.NA.is_equal(None)

    ## Null checks:
    assert Money.NA.is_equal(Money.NA)

    ## Non-null checks:
    x = Money.of(Currency("USD"), 1, Date.today())
    x2 = Money.of(Currency("USD"), 1, Date.today())
    assert x.is_equal(x2)
    assert x2.is_equal(x)

    ## Non-equal checks:
    x = Money.of(Currency("USD"), 1, Date.today())

# Generated at 2022-06-14 04:52:35.269272
# Unit test for method scalar_add of class Money
def test_Money_scalar_add():
    result = NoMoney.scalar_add(Decimal("12"))
    assert result == NoMoney

    result = SomeMoney(usd, Decimal("100"), Date.today()).scalar_add(Decimal("12"))
    assert result == SomeMoney(usd, Decimal("112"), Date.today())


# Generated at 2022-06-14 04:52:45.532362
# Unit test for method lt of class Money
def test_Money_lt():
    assert SomeMoney(CCY1,QTY1,DATE).lt(SomeMoney(CCY1,QTY1,DATE)) == False
    assert SomeMoney(CCY1,QTY1,DATE).lt(SomeMoney(CCY2,QTY2,DATE)) == False
    assert SomeMoney(CCY1,QTY1,DATE).lt(SomeMoney(CCY1,QTY2,DATE)) == True
    assert SomeMoney(CCY1,QTY1,DATE).lt(SomeMoney(CCY1,QTY1,DATE1)) == False
    assert SomeMoney(CCY1,QTY1,DATE).lt(SomeMoney(CCY1,QTY1,DATE2)) == True

# Generated at 2022-06-14 04:52:57.929012
# Unit test for method as_boolean of class Money
def test_Money_as_boolean():
    assert SomeMoney(Currency.USD, Decimal("0.0"), Date.today()) == False
    assert SomeMoney(Currency.USD, Decimal("-0.0"), Date.today()) == False
    assert SomeMoney(Currency.USD, Decimal("0.0000000001"), Date.today()) == True
    assert SomeMoney(Currency.USD, Decimal("-0.0000000001"), Date.today()) == True
    assert SomeMoney(Currency.USD, Decimal("1.0000000001"), Date.today()) == True
    assert SomeMoney(Currency.USD, Decimal("-1.0000000001"), Date.today()) == True
    assert SomeMoney(Currency.USD, Decimal("99999999999999999999999999"), Date.today()) == True