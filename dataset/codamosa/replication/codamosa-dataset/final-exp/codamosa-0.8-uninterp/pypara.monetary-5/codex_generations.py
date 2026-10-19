

# Generated at 2022-06-14 04:48:06.785694
# Unit test for method multiply of class Money
def test_Money_multiply():
    ccy = Currency.of("USD")
    money = Money.of(ccy, 100, Date.now())
    
    assert money.multiply(2) == Money.of(ccy, 200, Date.now())
    assert money.multiply(0.5) == Money.of(ccy, 50, Date.now())
    assert money.multiply(0) == Money.of(ccy, 0, Date.now())
    
    
    


# Generated at 2022-06-14 04:48:15.977391
# Unit test for method __ge__ of class SomeMoney
def test_SomeMoney___ge__():
    r = Money.of(USD, Decimal('100'), Date(2018, 1, 1)).__ge__(Money.of(USD, Decimal('100'), Date(2018, 1, 1)))
    assert r == True
    r = Money.of(USD, Decimal('100'), Date(2018, 1, 1)).__ge__(Money.of(USD, Decimal('100'), Date(2018, 1, 1)))
    assert r == True
    r = Money.of(USD, Decimal('100'), Date(2018, 1, 1)).__ge__(Money.of(USD, Decimal('101'), Date(2018, 1, 1)))
    assert r == False

# Generated at 2022-06-14 04:48:25.490787
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
# Test for method scalar_add of class Price for undefined case
    import datetime
    from finance.currency import Currency
    from finance.money import Money
    from finance.price import Price

    price = Price.of(Currency("GBP"), 0, datetime.date(2019, 1, 1))
    res = price.scalar_add(5)
    assert res.undefined
    assert res.ccy.is_equal(Currency("GBP"))
    assert res.qty is None and res.dov is None
    assert res.with_qty(1).undefined
    assert res.with_ccy(Currency("USD")).undefined

    price = Price.of(Currency("GBP"), 1, datetime.date(2019, 1, 1))
    res = price.scalar_add(5)


# Generated at 2022-06-14 04:48:34.630517
# Unit test for method scalar_subtract of class Money
def test_Money_scalar_subtract():
    money = Money.of('USD', 10, date(2016, 1, 1))
    assert money.scalar_subtract(5) == Money.of('USD', 5, date(2016, 1, 1))
    assert money.scalar_subtract(money) == Money.of('USD', 0, date(2016, 1, 1))
    assert money.scalar_subtract(None) == Money.NA
    assert money.scalar_subtract(NonMoney) == Money.NA
    assert Money.NA.scalar_subtract(5) == Money.NA
    assert Money.NA.scalar_subtract(Money.NA) == Money.NA



# Generated at 2022-06-14 04:48:38.783345
# Unit test for method __truediv__ of class SomeMoney
def test_SomeMoney___truediv__():
    assert (SomeMoney.of(USD, Decimal("-0.00123456"), Date(2002, 1, 1)) / 3).quantity == Decimal("-0.00041152")



# Generated at 2022-06-14 04:48:47.509478
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    """
    Unit test for method floor_divide of class Money
    """
    eur = Currency.of("EUR")
    jpy = Currency.of("JPY")
    usd = Currency.of("USD")
    date = Date.today()
    EUR_2_USD = 1.2
    EUR_2_JPY = 120.0
    usd_price = Price(usd, EUR_2_USD, date)
    jpy_price = Price(jpy, EUR_2_JPY, date)
    mny_1 = Money.of(eur, 100, date)
    assert mny_1.floor_divide(usd_price) == mny_1.with_ccy(usd).floor_divide(EUR_2_USD)

# Generated at 2022-06-14 04:48:49.465025
# Unit test for method __floordiv__ of class Money
def test_Money___floordiv__():
    # TODO: Implement
    raise NotImplementedError()

# Generated at 2022-06-14 04:48:59.803302
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    assert Money.of(None, None, None).floor_divide(0) == Money.of(None, None, None)
    assert Money.of(Currency.usd, None, None).floor_divide(0) == Money.of(Currency.usd, None, None)
    assert Money.of(None, 0, None).floor_divide(0) == Money.of(None, None, None)
    assert Money.of(Currency.usd, 0, None).floor_divide(0) == Money.of(Currency.usd, None, None)
    assert Money.of(None, None, Date.today()).floor_divide(0) == Money.of(None, None, None)

# Generated at 2022-06-14 04:49:09.367694
# Unit test for method as_float of class Price
def test_Price_as_float():
    """
    Unit test for method as_float of class Price.
    """
    # This is a mock.
    # It will replace the pd.as_float function,
    # and we will be able to check if it is called properly.
    def mock_price_as_float(x: float) -> float:
        return x

    price = Price.of(usd, 7.5, today)
    assert price.as_float() == 7.5

    with patch.object(pd, "as_float", new=mock_price_as_float):
        assert price.as_float() == 7.5



# Generated at 2022-06-14 04:49:20.139700
# Unit test for method __lt__ of class SomeMoney
def test_SomeMoney___lt__():
    ## Set up:
    m1 = Money.of("USD", Decimal("100.00"), Date.today())
    m2 = Money.of("USD", Decimal("200.00"), Date.today())
    m3 = Money.of("USD", Decimal("200.00"), Date.today())
    
    ## Test:
    assert not m1 < m1
    assert m1 < m2
    assert not m2 < m1
    
    assert m1 < m3
    assert not m3 < m1
    assert not m2 < m3
    assert not m3 < m2
    
    assert not m1 < NoMoney
    assert not NoMoney < m1
    
    assert not NoMoney < NoMoney

# Generated at 2022-06-14 04:49:39.539190
# Unit test for method __ge__ of class Money
def test_Money___ge__():  # noqa: D103
    pass  # For now...



# Generated at 2022-06-14 04:49:43.715495
# Unit test for method __gt__ of class SomeMoney
def test_SomeMoney___gt__():
    with raises(KeyError):
        SomeMoney(
            Currency.as_default("USD"),
            Decimal(100)
        ) > SomeMoney(
            Currency.as_default("DKK"),
            Decimal(100),
            Date.today()
        )



# Generated at 2022-06-14 04:49:48.013239
# Unit test for method scalar_subtract of class Money
def test_Money_scalar_subtract():
    assert Money.of(USD, 100, None) - 100 == Money.of(USD, 0, None)
    assert 100 - Money.of(USD, 100, None) == Money.of(USD, 0, None)

    # Non-numeric values cannot be subtracted from a money object.
    assert Money.of(USD, 10, None) - None is None
    assert Money.of(USD, 10, None) - "xyz" == Money.of(USD, 10, None)

    # Undefined money object simply returns itself, without throwing any error.
    assert Money.of(None, None, None) - 100 == Money.of(None, None, None)

test_Money_scalar_subtract()



# Generated at 2022-06-14 04:49:50.119521
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    assert 1 + NoPrice == NoPrice
    assert 1 + SomePrice(USD, Decimal(1), Date(datetime(2019, 12, 12))) == SomePrice(USD, Decimal(2), Date(datetime(2019, 12, 12)))

# Generated at 2022-06-14 04:49:57.379680
# Unit test for method __add__ of class Money
def test_Money___add__():
    # Arrange
    jpy = Currency.ccy("JPY")
    usd = Currency.ccy("USD")
    dov = Date.today()
    m1 = Money.of(jpy, Decimal(1), dov)
    m2 = Money.of(usd, Decimal(1), dov)

    # Act
    m = m1 + m2

    # Assert
    assert isinstance(m, NoMoney)

# Generated at 2022-06-14 04:50:01.755068
# Unit test for method __lt__ of class Price
def test_Price___lt__():
    p1 = Price.of(USD, Decimal(100), Date(2020, Month.SEPTEMBER, 2))
    p2 = Price.of(USD, Decimal(100), Date(2020, Month.SEPTEMBER, 2))
    assert not p1.__lt__(p2)

# Generated at 2022-06-14 04:50:13.032430
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    """
    Unit test for method convert of class SomePrice
    """
    ## Test fixture
    FXRateService.default = FXRateService()
    ## Test the code
    c = Currency("USD")
    q = Decimal(0.123)
    d = Date(2020, 4, 16)
    obj1 = SomePrice(c, q, d)
    ### Test attribute FXRateService is missing
    with raises(ProgrammingError) as err:
        obj2 = obj1.convert(to=c, asof=d, strict=False)
    assert exc_info()[0] == ProgrammingError
    assert exc_info()[1].args[0] == "Did you implement and set the default FX rate service?"
    assert exc_info()[1].__cause__ is None

# Generated at 2022-06-14 04:50:23.197394
# Unit test for method multiply of class Money
def test_Money_multiply():
    from decimal import Decimal as D
    from datetime import date
    from operator import mul, truediv, floordiv
    from fx.currencies import Currency
    from fx.money import Money
    Money(Currency("USD"), D(123.45), date(2020, 8, 12)).multiply(D(2)) is Money(Currency("USD"), D(123.45) * D(2), date(2020, 8, 12))
    Money(Currency("USD"), D(123.45), date(2020, 8, 12)).multiply(2) is Money(Currency("USD"), D(123.45) * D(2), date(2020, 8, 12))

# Generated at 2022-06-14 04:50:27.982814
# Unit test for method gt of class Money
def test_Money_gt():
    my_money = Money.of(Currency.DEM, 1.0, Date('2018-01-01'))
    other_money = Money.of(Currency.EUR, 2.0, Date('2018-01-01'))
    assert not my_money.gt(other_money)
    assert not my_money.gt(NoneMoney)
    assert not my_money.gt(NoMoney)
    assert my_money.gt(Money.of(Currency.DEM, 0.0, Date('2018-01-01')))


# Generated at 2022-06-14 04:50:28.718509
# Unit test for method __sub__ of class SomePrice
def test_SomePrice___sub__():
    pass


# Generated at 2022-06-14 04:51:40.928143
# Unit test for method __ge__ of class Money
def test_Money___ge__():
    assert NoneMoney >= NoneMoney


# Generated at 2022-06-14 04:51:46.491503
# Unit test for method lt of class Price
def test_Price_lt():
    asset_val = Money.of("USD", 10)
    asset_val2 = Money.of("EUR", 200)
    price = Price.of("EUR", 10)
    assert price.lt(asset_val) == False
    assert price.lt(asset_val2) == False
    assert price.lt(1) == True
    assert price.lt(0) == False

# Generated at 2022-06-14 04:51:52.030811
# Unit test for method __int__ of class Price

# Generated at 2022-06-14 04:51:55.947040
# Unit test for method __ge__ of class Price
def test_Price___ge__():
    try:
        from dtocean_core.utils.common import _Price___ge__
        assert _Price___ge__ is not None
        assert callable(_Price___ge__)
    except ImportError:
        pass




# Generated at 2022-06-14 04:52:03.485547
# Unit test for method with_ccy of class Money
def test_Money_with_ccy():
    m1 = Money.of(Currency.of("EUR"), Decimal("100"), Date(2020, 1, 1))
    m2 = m1.with_ccy(Currency.of("USD"))
    m3 = m1.with_ccy(Currency.of("EUR"))
    assert m2.ccy == Currency.of("USD")
    assert m2.qty == Decimal("100")
    assert m2.dov == Date(2020, 1, 1)
    assert m3.ccy == Currency.of("EUR")
    assert m3.qty  == Decimal("100")
    assert m3.dov == Date(2020, 1, 1)


# Generated at 2022-06-14 04:52:14.612855
# Unit test for method convert of class SomeMoney
def test_SomeMoney_convert():
    """
    Function to test the method convert of class SomeMoney
    """
    # Set the global value of FXRateService
    FXRateService.default = FXRateService.in_memory()
    from datetime import date
    from .currency import USD, GBP, EUR
    from .fxrates import FXRate, USD_GBP_2020_01_01, USD_EUR_2020_01_01
    asof = date(2020, 1, 1)
    money = Money.of(USD, 100, asof)
    money.convert(GBP).qty == 75
    FXRateService.default.add(USD_GBP_2020_01_01)
    money.convert(GBP).qty == Decimal("75.00")
    FXRateService.default.add(USD_EUR_2020_01_01)


# Generated at 2022-06-14 04:52:16.017059
# Unit test for method __int__ of class Price
def test_Price___int__():
    assert SomePrice(USD, 1.0, TODAY).__int__() == 1



# Generated at 2022-06-14 04:52:27.187102
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    """
    Tests the scalar_add method with Price instances.
    """

    assert Price.of("USD", decimal_value(1), TODAY).scalar_add(decimal_value(1)) == Price.of("USD", decimal_value(2), TODAY)

    assert Price.of("USD", decimal_value(1), TODAY).scalar_add(decimal_value(10.5)) == Price.of("USD", decimal_value(11.5), TODAY)

    assert Price.of(None, decimal_value(1), None).scalar_add(decimal_value(1)) == Price.of(None, decimal_value(2), None)


# Generated at 2022-06-14 04:52:39.923537
# Unit test for method __le__ of class SomePrice
def test_SomePrice___le__():
    """
    Test method __le__ of class SomePrice
    """
    # unit test for method SomePrice.__le__(other)
    from datetime import date
    from tumdlr.model.pricing import SomePrice,NoPrice,IncompatibleCurrencyError
    import tumdlr.model.currency as curr
    test1 = SomePrice(curr.USD,1,date(2020,1,1))
    test2 = SomePrice(curr.USD,1,date(2020,1,1))
    test3 = SomePrice(curr.USD,0,date(2020,1,1))
    test4 = SomePrice(curr.USD,2,date(2020,1,1))
    test5 = SomePrice(curr.GBP,1,date(2020,1,1))
    test6 = NoPrice


# Generated at 2022-06-14 04:52:47.751323
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    # this is an autogenerated function, please do not modify
    assert SomePrice(Currency.USD, Decimal('0.10'), Date('2019-01-02')).convert(Currency.USD, None, False) == SomePrice(Currency.USD, Decimal('0.10'), Date('2019-01-02'))
    assert SomePrice(Currency.EUR, Decimal('100.00'), Date('2019-01-02')).convert(Currency.USD, Date('2019-01-02'), False) == SomePrice(Currency.USD, Decimal('112.00'), Date('2019-01-02'))
    assert SomePrice(Currency.EUR, Decimal('100.00'), Date('2019-01-02')).convert(Currency.USD, Date('2019-01-04'), False) == SomePrice