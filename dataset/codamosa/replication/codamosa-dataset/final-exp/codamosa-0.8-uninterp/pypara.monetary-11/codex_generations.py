

# Generated at 2022-06-14 04:49:48.624584
# Unit test for method __bool__ of class Money
def test_Money___bool__():
    ## Premise:
    m1 = Money.of(USD, 3, Date.now())
    m2 = Money.of(USD, 0, Date.now())
    m3 = NoMoney

    ## Exercise:
    assert bool(m1) is True
    assert bool(m2) is False
    assert bool(m3) is False


# Generated at 2022-06-14 04:49:50.608177
# Unit test for method __eq__ of class Price
def test_Price___eq__():
    with pytest.raises(NotImplementedError):
        Price.__eq__(None, None)

# Generated at 2022-06-14 04:50:01.831817
# Unit test for method with_qty of class Money
def test_Money_with_qty():
    from .currencies import EUR
    from .dates import Jan01_2020, Jan02_2020, Jan03_2020
    from .markets import FxCross
    from .money import Money, Price, SomeMoney, SomePrice

    EUR_1p = Money.of(EUR, Decimal("0.01"), Jan01_2020)
    EUR_1 = Money.of(EUR, Decimal("1"), Jan01_2020)
    EUR_1p_FX = EUR_1p.with_qty(Decimal("0.01"))
    EUR_1_FX = EUR_1.with_qty(Decimal("1"))
    assert EUR_1_FX == EUR_1
    assert EUR_1p_FX == EUR_1p
    EUR_2_FX = EUR_1.with_qty(Decimal("2"))

# Generated at 2022-06-14 04:50:09.357480
# Unit test for method is_equal of class Price
def test_Price_is_equal():
    assert SomePrice(USD, Decimal('1.0'), Date(2019, 3, 1)).is_equal(SomePrice(USD, Decimal('1.0'), Date(2019, 3, 1))) is True
    assert SomePrice(USD, Decimal('1.0'), Date(2019, 3, 1)).is_equal(SomePrice(USD, Decimal('0.0'), Date(2019, 3, 1))) is False
    assert NoPrice.is_equal(NoPrice) is True

# Generated at 2022-06-14 04:50:19.566202
# Unit test for method __sub__ of class Money
def test_Money___sub__():
    # Test with a defined money
    ccy = Currency.of("USD")
    qty = Decimal("100")
    dov = Date.today()
    m1 = Money.of(ccy, qty, dov)
    m2 = Money.of(ccy, Decimal("50"), dov)
    res = m1 - m2
    assert res == Money.of(ccy, Decimal("50"), dov)

    # Test with an undefined money
    m1 = NoMoney
    m2 = Money.of(ccy, Decimal("50"), dov)
    res = m1 - m2
    assert res == m1
    res = m2 - m1
    assert res == m2

    # Test with an incompatible currency

# Generated at 2022-06-14 04:50:27.323237
# Unit test for method __bool__ of class Price
def test_Price___bool__():
    price = Money.of(Currency.of("JPY"), 1000000, Date.from_str("2020-07-16")) \
        .as_price(Currency.of("USD"), Date.from_str("2020-07-16"))
    assert price
    assert price.as_boolean()
    assert bool(price)

    price = Money.of(Currency.of("JPY"), 0, Date.from_str("2020-07-16")) \
        .as_price(Currency.of("USD"), Date.from_str("2020-07-16"))
    assert not price
    assert not price.as_boolean()
    assert not bool(price)


# Generated at 2022-06-14 04:50:36.446008
# Unit test for method __lt__ of class Price
def test_Price___lt__():
    p1 = Price.of(USD, s(1), today)
    p2 = Price.of(USD, s(2), today)
    p3 = Price.of(EUR, s(1), today)
    assert not p1 < p1
    assert p1 < p2
    with pytest.raises(IncompatibleCurrencyError):
        assert p1 < p3
    assert not NoPrice < p1
    assert NoPrice < p2
    assert not p1 < NoPrice
    assert p2 < NoPrice



# Generated at 2022-06-14 04:50:47.862314
# Unit test for method floor_divide of class Price
def test_Price_floor_divide():
    # Price.floor_divide
    assert Price.NA.floor_divide(6.0) == Price.NA
    assert Price.of(USD, 3.0, today()).floor_divide(6.0) == Price.of(USD, 0.0, today())
    assert Price.of(USD, 6.0, today()).floor_divide(3.0) == Price.of(USD, 2.0, today())
    assert Price.of(USD, 6.0, today()).floor_divide(6.0) == Price.of(USD, 1.0, today())
    assert Price.of(USD, 7.0, today()).floor_divide(6.0) == Price.of(USD, 1.0, today())
    # Unit test for method multiply of class Price

# Generated at 2022-06-14 04:50:53.863577
# Unit test for method __ge__ of class Money
def test_Money___ge__():
    from .currencies import USD
    from .zeitgeist import Date
    from .money import Money, SomeMoney

    money = Money.of(USD, 100, Date.today())
    money_other = Money.of(USD, 101, Date.today())

    # case: self > other
    assert money > money_other
    assert not money >= money_other

    # case: self > other
    assert not money > money_other

    # case: self == other
    assert money_other >= money
    assert money_other <= money

    # case: self and other undefined
    assert SomeMoney(USD, Decimal('0.00'), Date.today()) == NoMoney

    # case: self is undefined
    assert NoMoney < money_other

    # case: other is undefined
    assert money > NoMoney

# Generated at 2022-06-14 04:50:59.961327
# Unit test for method __ge__ of class SomePrice
def test_SomePrice___ge__():
    x = SomePrice(Currency("EUR"), Decimal("1"), Date(2011, 1, 1))
    assert x >= x.with_qty(Decimal("1"))
    assert x >= x.with_qty(Decimal("0"))
    assert not x >= x.with_qty(Decimal("-1"))

# Generated at 2022-06-14 04:52:27.797147
# Unit test for method __sub__ of class Money
def test_Money___sub__():
    _m1 = Money.of(Currency.USD, Decimal("100.00"), Date.today())
    _m2 = Money.of(Currency.USD, Decimal("-100.00"), Date.today())
    assert (_m1 - _m1) == _m2



# Generated at 2022-06-14 04:52:40.464661
# Unit test for method gte of class Money
def test_Money_gte():
    assert SomeMoney(USD, Decimal("1"), "2018-01-01") >= SomeMoney(USD, Decimal("1"), "2018-01-01")
    assert SomeMoney(USD, Decimal("1"), "2018-01-01") >= SomeMoney(USD, Decimal("1"), "2018-01-01")
    assert SomeMoney(USD, Decimal("100"), "2018-01-01") <= SomeMoney(USD, Decimal("100"), "2018-01-01")
    assert SomeMoney(USD, Decimal("100"), "2018-01-01") >= SomeMoney(USD, Decimal("100"), "2018-01-01")
    assert NoMoney >= SomeMoney(USD, Decimal("100"), "2018-01-01")
    assert SomeMoney(USD, Decimal("100"), "2018-01-01") >= NoMoney
   

# Generated at 2022-06-14 04:52:43.015536
# Unit test for method __ge__ of class SomePrice
def test_SomePrice___ge__():
    Price.of("USD", Decimal("3.00"), Date.today()) >= Price.of("USD", Decimal("2.00"), Date.today())



# Generated at 2022-06-14 04:52:55.563887
# Unit test for method scalar_add of class Money
def test_Money_scalar_add():
    # A no-money object + a scalar should yield a no-money object
    assert NoMoney.scalar_add(10) == NoMoney
    
    # A money object + a scalar should yield a money object with the sum
    money = Money.of(Currency.USD, Decimal('0.0'), Date(2020, 9, 8))
    res = money.scalar_add(10)
    assert res.ccy == Currency.USD
    assert res.qty == Decimal('10.0')
    assert res.dov == Date(2020, 9, 8)
    
    # A money object + a scalar should yield a money object with the sum
    money = Money.of(Currency.USD, Decimal('0.0'), Date(2020, 9, 8))

# Generated at 2022-06-14 04:52:58.562947
# Unit test for method as_integer of class Money
def test_Money_as_integer():
    mny = Money(Currency.of("USD"), 123.45, Date.today())
    assert mny.as_integer() == 123



# Generated at 2022-06-14 04:53:00.996101
# Unit test for method scalar_add of class Money
def test_Money_scalar_add():
    # TODO: implement test case for method Money.scalar_add
    raise ProgrammingError("Test is not implemented.")

# Generated at 2022-06-14 04:53:05.373907
# Unit test for method with_ccy of class Price
def test_Price_with_ccy():
    assert Price.NA.with_ccy(USD) == Price.NA
    assert SomePrice(USD, Decimal(1.23), today()).with_ccy(JPY) == SomePrice(JPY, Decimal(1.23), today())

# Generated at 2022-06-14 04:53:14.920271
# Unit test for method floor_divide of class Price
def test_Price_floor_divide():
    
    from datetime import date, datetime
    from pytz import UTC
    
    from finx.datamodel.money import Money, Price
    from finx.datamodel.currency import Currency
    from nose.tools import assert_equal, assert_true, assert_false, assert_is_none, assert_raises, assert_is_instance
    
    USD = Currency.USD
    GBP = Currency.GBP
    EUR = Currency.EUR
    JPY = Currency.JPY
    ZAR = Currency.ZAR
    
    # Test case where the monetary value is None
    #-------------------------
    x = Price.of(None, None, None)
    y = x.floor_divide(10)
    assert_true(y.undefined)
    
    # Test case where the monetary value is defined


# Generated at 2022-06-14 04:53:17.572380
# Unit test for method with_ccy of class Price
def test_Price_with_ccy():
    assert NoPrice.with_ccy(USD) == NoPrice

    assert (
        SomePrice(USD, Decimal("100"), Date.today()).with_ccy(EUR)
        == SomePrice(EUR, Decimal("100"), Date.today())
    )



# Generated at 2022-06-14 04:53:18.628445
# Unit test for method __bool__ of class Money
def test_Money___bool__():
    result = Money.NA.__bool__()
    assert isinstance(result, bool)
