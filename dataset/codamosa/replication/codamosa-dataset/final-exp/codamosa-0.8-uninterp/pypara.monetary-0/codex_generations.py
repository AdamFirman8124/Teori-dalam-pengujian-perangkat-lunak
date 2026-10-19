

# Generated at 2022-06-14 04:48:17.475166
# Unit test for method __eq__ of class Price
def test_Price___eq__():
    import pytest

    NoPrice = Price.NA
    SomePrice = Price.of

    # Test for __eq__ of class Price
    #
    # Test with other as None
    assert NoPrice == None  # type: ignore

    # Test with other as a defined price object with value in the same currency
    assert SomePrice(GBP, '1', '2020-01-01') == SomePrice(GBP, '1', '2020-01-01')

    # Test with other is a defined price object with value in a different currency
    assert None == SomePrice(EUR, '1', '2020-01-01')

    # Test with other is not a price object
    with pytest.raises(TypeError):
        SomePrice(GBP, '1', '2020-01-01') == 1

    # Test with other is a price object with

# Generated at 2022-06-14 04:48:26.788860
# Unit test for method scalar_subtract of class Money
def test_Money_scalar_subtract():
    """
    Test method scalar_subtract of class Money.
    """
    assert Money.of(Currency.of("EUR"), Decimal("1.0"), Date.today()) > Money.of(Currency.of("EUR"), Decimal("0.1"), Date.today())
    assert Money.of(Currency.of("EUR"), Decimal("0.5"), Date.today()) > Money.of(Currency.of("EUR"), Decimal("0.1"), Date.today())
    assert Money.of(Currency.of("EUR"), Decimal("0.5"), Date.today()) >= Money.of(Currency.of("EUR"), Decimal("0.5"), Date.today())
    assert Money.of(Currency.of("EUR"), Decimal("0.5"), Date.today()) <= Money.of

# Generated at 2022-06-14 04:48:28.641932
# Unit test for method positive of class Price
def test_Price_positive():
  # Assume
  positive = 1

  # Act

  # Assert
  assert positive.positive() == positive



# Generated at 2022-06-14 04:48:33.827123
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():
    sm = SomeMoney(Currency("EUR"), Decimal("1.234567890"), Date("2018-09-15"))  # type: ignore
    round_sm = sm.round()
    assert round_sm == SomeMoney(Currency("EUR"), Decimal("1.23456789"), Date("2018-09-15"))  # type: ignore


# Generated at 2022-06-14 04:48:45.093891
# Unit test for method with_ccy of class Price
def test_Price_with_ccy():
    # Uncommenting lines below will cause the test to fail
    # with TypeError.
    # Money.NA.with_ccy(EUR)
    # Money.NA.with_ccy('EUR')
    # EUR(None).with_ccy(USD)
    # EUR(None).with_ccy('USD')
    x = EUR(Decimal(1))
    assert x.with_ccy(EUR) == x
    assert x.with_ccy(USD) == EUR(Decimal(1), ccy=USD)
    assert x.with_ccy(Decimal(1)) == EUR(Decimal(1), ccy='1')
    assert x.with_ccy('USD') == EUR(Decimal(1), ccy=USD)

# Generated at 2022-06-14 04:48:56.922716
# Unit test for method as_boolean of class Money
def test_Money_as_boolean():
    assert bool(SomeMoney.of(Currency.USD, 1, Date.today())) is True
    assert bool(SomeMoney.of(Currency.USD, -1, Date.today())) is True
    assert bool(SomeMoney.of(Currency.USD, 0, Date.today())) is False
    assert bool(SomeMoney.of(Currency.USD, None, Date.today())) is False
    assert bool(SomeMoney.of(None, 1, Date.today())) is False
    assert bool(SomeMoney.of(Currency.USD, 1, None)) is False
    assert bool(SomeMoney.of(None, None, None)) is False
    assert bool(SomeMoney.of(Currency.USD, None, None)) is False
    assert bool(NoMoney) is False



# Generated at 2022-06-14 04:48:58.729871
# Unit test for method __truediv__ of class SomePrice
def test_SomePrice___truediv__():
    assert SomePrice('SEK', Decimal('1'), Date(2018, 4, 2)) / Decimal('0') == NoPrice
    assert SomePrice('SEK', Decimal('1'), Date(2018, 4, 2)) / '0' == NoPrice

# Generated at 2022-06-14 04:49:07.357395
# Unit test for method __int__ of class Money
def test_Money___int__():
    """
    Test that monetary value is properly converted to integer as expected.
    """
    ## Test with simple money:
    m = SomeMoney("EUR", 100.0, "2019-09-05")
    assert isinstance(int(m), int)  # noqa: E712
    assert int(m) == 100

    ## Test with undefined money:
    assert isinstance(int(NoMoney), int)  # noqa: E712
    assert int(NoMoney) == 0



# Generated at 2022-06-14 04:49:18.045392
# Unit test for method __le__ of class SomeMoney
def test_SomeMoney___le__():
    #
    # [E] Money e;
    #     Money > e;
    #     Money < e;
    #     Money >= e;
    #     Money <= e;
    #     Money != e;
    #     Money == e;
    #
    assert SomeMoney(USD, 10) > SomeMoney(USD, 5)
    assert SomeMoney(USD, 5) < SomeMoney(USD, 10)
    assert SomeMoney(USD, 10) >= SomeMoney(USD, 5)
    assert SomeMoney(USD, 5) <= SomeMoney(USD, 10)
    assert SomeMoney(USD, 5) != SomeMoney(USD, 10)
    assert SomeMoney(USD, 5) == SomeMoney(USD, 5)

# Generated at 2022-06-14 04:49:23.190657
# Unit test for method multiply of class Price
def test_Price_multiply():
    result = Money.of(Currency.of('USD'), 50).multiply(2)
    assert result.ccy.code == 'USD'
    assert result.qty == 100
    assert result.dov == Date.today()
    assert result.as_boolean() is True

# Generated at 2022-06-14 04:50:50.491990
# Unit test for method lt of class Price
def test_Price_lt():
    x = Price.of(SEK, 15.0, LocalDate.parse("2020-01-01"))
    y = Price.of(NOK, 20.0, LocalDate.parse("2020-01-01"))
    assert (x.lt(y))


# Generated at 2022-06-14 04:51:02.291112
# Unit test for method __floordiv__ of class SomePrice
def test_SomePrice___floordiv__():
    # TODO: add more tests!
    assert SomePrice(AED, Decimal("2.5"), date(2018, 5, 1)) // Decimal(2) == SomePrice(AED, Decimal("1"), date(2018, 5, 1))
    assert SomePrice(AED, Decimal("2.5"), date(2018, 5, 1)) // 2 == SomePrice(AED, Decimal("1"), date(2018, 5, 1))
    assert SomePrice(AED, Decimal("2.5"), date(2018, 5, 1)) // 2.0 == SomePrice(AED, Decimal("1"), date(2018, 5, 1))

# Generated at 2022-06-14 04:51:14.110189
# Unit test for method lte of class Price
def test_Price_lte():
    aapl_info = pd.read_csv('data/aapl.csv', index_col='Date', parse_dates=True)

    aapl_info['Open'].astype(float).head()
    #aapl_info['Open'].astype(float).head()
    my_list = list(aapl_info['Open'].astype(float))
    my_list = my_list[0:10]
    my_list.sort()
    my_list = [round(x, 2) for x in my_list]
    tmp_list =[10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
    for i in tmp_list:
        my_list.append(i)


# Generated at 2022-06-14 04:51:18.053241
# Unit test for method __lt__ of class SomePrice
def test_SomePrice___lt__():
    assert SomePrice(US_DOLLAR, Decimal("1.00"), Date(2019, 1, 1)) < SomePrice(US_DOLLAR, Decimal("2.00"), Date(2019, 1, 1))

# Generated at 2022-06-14 04:51:29.629529
# Unit test for method scalar_subtract of class Price
def test_Price_scalar_subtract():
    usd = Currency.get("USD")
    x = Price.of(usd, Decimal("100"), None)
    y = x.scalar_subtract(Decimal("10"))
    assert isinstance(y, Price)
    assert y.ccy == usd
    assert y.qty == Decimal("90")

    # Test for undefined price object
    x = Price.of(usd, None, None)
    y = x.scalar_subtract(Decimal("10"))
    assert y is NoPrice
    assert not y.defined
    assert not y.undefined

    # Test for undefined price object
    x = Price.of(usd, None, None)
    y = x.scalar_subtract(None)
    assert y is NoPrice
    assert not y.defined
   

# Generated at 2022-06-14 04:51:40.672258
# Unit test for method __add__ of class SomeMoney
def test_SomeMoney___add__():

    from math import nan
    from numbers import Number

    from pygear.core.error import IncompatibleCurrencyError
    from pygear.core.types import Currency, Date, SomeMoney

    ## Set up test:
    ccy = Currency("USD")
    dov = Date.today()

    ## Test:
    assert (SomeMoney(ccy, 100, dov) + SomeMoney(ccy, 200, dov)) == SomeMoney(ccy, 300, dov)

    with raises(TypeError):
        SomeMoney(ccy, 100, dov) + nan

    with raises(TypeError):
        SomeMoney(ccy, 100, dov) + None

    with raises(TypeError):
        SomeMoney(ccy, 100, dov) + "hello"


# Generated at 2022-06-14 04:51:46.683257
# Unit test for method __gt__ of class Price
def test_Price___gt__():
    
    # Arrange
    p1 = Price.of(Currency.USD, Decimal(10), Date.now())
    p2 = Price.of(Currency.USD, Decimal(1), Date.now())
    
    # Act
    result = p1.__gt__(p2)
    
    # Assert
    assert(result == True)
    
test_Price___gt__()




# Generated at 2022-06-14 04:51:58.922939
# Unit test for method is_equal of class Price
def test_Price_is_equal():
    ## Arrange ##
    eur_100 = SomeMoney(Currency("EUR"), 100)
    gbp_100 = SomeMoney(Currency("GBP"), 100)
    eur_price = SomePrice(Currency("EUR"), Decimal("1.1"), Date.of("20180405"))
    usd_price = SomePrice(Currency("USD"), Decimal("1.1"), Date.of("20180405"))
    eur_price_1 = SomePrice(Currency("EUR"), Decimal("1.1"), Date.of("20180405"))

    ## Act ##
    ## Assert ##
    assert not eur_price.is_equal(None)
    assert eur_price.is_equal(eur_price_1)
    assert not eur_price.is_equal(eur_100)

# Generated at 2022-06-14 04:52:05.546189
# Unit test for method __lt__ of class SomePrice
def test_SomePrice___lt__():
    # We need to know if this is Python 3 or 2:
    import sys
    if sys.version_info[0] > 2:
        from unittest.mock import MagicMock
        from unittest import mock
    else:
        from mock import MagicMock
        from mock import mock

    # Set up mock FX rate service:
    from quantdsl.domain.services.fxrateservice import FXRateService
    FXRateService.default = mock.MagicMock(**{"query.return_value": None})

    # Set up mocks:
    USD = MagicMock(**{"__str__.return_value": "USD"})
    GBP = MagicMock(**{"__str__.return_value": "GBP"})

# Generated at 2022-06-14 04:52:06.911512
# Unit test for method __floordiv__ of class SomeMoney
def test_SomeMoney___floordiv__():
    s = SomeMoney(USD, Decimal('100'), "today")
    r = SomeMoney(USD, Decimal('100'), "today")
    assert s.__floordiv__(r) == NoMoney



# Generated at 2022-06-14 04:52:53.675186
# Unit test for method __bool__ of class Price
def test_Price___bool__():
    # Create some prices with different quantities to test __bool__
    assert CashPrice(Currency.EUR, Decimal(0.00)) == NoPrice
    assert CashPrice(Currency.EUR, Decimal(5.00)) != NoPrice


# Generated at 2022-06-14 04:52:57.687707
# Unit test for method __lt__ of class Price
def test_Price___lt__():
    assert Price(ccy="USD", qty=Decimal("2.0"), dov=Date.today()).__lt__(Price(ccy="USD", qty=Decimal("3.0"), dov=Date.today()))

# Generated at 2022-06-14 04:53:00.368025
# Unit test for method lte of class Price
def test_Price_lte():
    assert Price.of(CAD, 10, date.today()).lte(Price.of(CAD, 100, date.today()))

# Generated at 2022-06-14 04:53:11.683840
# Unit test for method with_ccy of class Price
def test_Price_with_ccy():
    EGP = Currency.of("EGP")
    USD = Currency.of("USD")

    assert Price.of(USD, 10.0, Date(2013, 1, 23)).with_ccy(EGP) == Price.of(USD, 10.0, Date(2013, 1, 23))
    assert Price.of(USD, 10.0, Date(2013, 1, 23)).with_ccy(USD) == Price.of(USD, 10.0, Date(2013, 1, 23))
    assert Price.of(USD, 10.0, Date(2013, 1, 23)).with_ccy(None) == Price.of(USD, 10.0, Date(2013, 1, 23))

# Generated at 2022-06-14 04:53:15.297033
# Unit test for method with_qty of class Price
def test_Price_with_qty():
    
    assert Price.of(USDCurr, 100, Date.from_str("2020-04-01")).with_qty(200) == Price.of(USDCurr, 200, Date.from_str("2020-04-01"))
    assert Price.NA.with_qty(200) == Price.NA
    

# Generated at 2022-06-14 04:53:20.868161
# Unit test for method times of class Price
def test_Price_times():
    # Test that the correct results are returned for valid inputs
    # Test that the correct exceptions are thrown for invalid inputs
    assert Price.of(USD, Decimal(10), date(2019, 9, 2)).times(2) == Money.of(USD, Decimal(20), date(2019, 9, 2))
    assert Price.of(USD, Decimal(10), date(2019, 9, 2)).times(0) == Money.of(USD, Decimal(0), date(2019, 9, 2))
    assert Price.of(USD, Decimal(10), date(2019, 9, 2)).times(-1) == Money.of(USD, Decimal(-10), date(2019, 9, 2))

# Generated at 2022-06-14 04:53:25.308406
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    amount = Money.of("USD", 100)
    rate = Price.of("USD", 1.5)
    new_rate = rate.scalar_add(1)
    assert new_rate.qty == 2.5
    assert new_rate.ccy == "USD"



# Generated at 2022-06-14 04:53:31.301431
# Unit test for method times of class Price
def test_Price_times():
    print("Unit test for method times of class Price.")
    ccy = Currency.USD
    qty = Decimal(1)
    dov = datetime.date(2015, 1, 1)
    price = Price.of(ccy, qty, dov)
    assert price.times(1) == Money.of(ccy, qty, dov)
    assert price.times(-1) == Money.of(ccy, -qty, dov)
test_Price_times()


# Generated at 2022-06-14 04:53:37.999068
# Unit test for method with_ccy of class Price
def test_Price_with_ccy():
  # simple with_ccy (test if ccy is equal)
  price = Price.of('EUR', 100, '01-01-2020')
  assert (price.with_ccy('EUR').ccy == 'EUR')
  # with_ccy (test if ccy is not equal)
  assert (price.with_ccy('GBP').ccy != 'EUR')
  # test if it returns undefined when undefined is given
  assert (NoPrice.with_ccy('GBP') == NoPrice)


# Generated at 2022-06-14 04:53:42.107614
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    assert SomePrice(USD, 1, today).convert(USD, today, False).as_float() == 1.0
    assert SomePrice(USD, 1, today).convert(EUR, today, False).is_undefined()
    assert SomePrice(USD, 1, today).convert(EUR, today, True).is_undefined()
    assert SomePrice(USD, 1, today).convert(EUR, tomorrow, False).as_float() > -1
    assert SomePrice(USD, 1, today).convert(EUR, tomorrow, True).as_float() < -1
    assert SomePrice(USD, 1, today).convert(JPY, tomorrow, False).as_float() == 100
    assert SomePrice(USD, 1, today).convert(JPY, tomorrow, True).as_float() == 100