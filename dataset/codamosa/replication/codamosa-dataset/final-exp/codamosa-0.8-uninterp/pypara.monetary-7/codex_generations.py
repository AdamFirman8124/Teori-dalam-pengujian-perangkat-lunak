

# Generated at 2022-06-14 04:47:36.363033
# Unit test for method __pos__ of class Price
def test_Price___pos__():
    # Arrange
    pay_date = date(2019, 11, 22)
    p1 = Price.of("EUR", Decimal("2.0"), pay_date)
    p2 = Price.of("EUR", Decimal("-2.0"), pay_date)
    p3 = Price.of("EUR", Decimal("0"), pay_date)
    p4 = Price.NA

    # Act
    p1_pos = p1.__pos__()
    p2_pos = p2.__pos__()
    p3_pos = p3.__pos__()
    p4_pos = p4.__pos__()

    # Assert
    assert p1_pos.ccy == "EUR"
    assert p1_pos.qty == Decimal("2.0")
    assert p1_pos

# Generated at 2022-06-14 04:47:40.722372
# Unit test for method __int__ of class Money
def test_Money___int__():
    assert int(-SomeMoney('EUR', Decimal('1'), Date(2020, 1, 3))) == -1
    assert int(SomeMoney('JPY', Decimal('2'), Date(2020, 1, 3))) == 2


# Generated at 2022-06-14 04:47:41.794792
# Unit test for method __floordiv__ of class SomePrice
def test_SomePrice___floordiv__():
    # Test not implemented
    return

# Generated at 2022-06-14 04:47:54.778932
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    from .currencies import USD
    from .commons.numbers import ZDecimal
    from .exchange import NoFXRate

    class MockFXRateService(FXRateService):

        def get(self, ccy1: Currency, ccy2: Currency, asof: Date) -> Optional[Decimal]:
            return None

    mUSD = Money.of(USD, ZDecimal("10.00"), Date("2019-01-01"))

    r = mUSD.convert(USD, asof=None, strict=True)  # No fx-rate from USD to USD.
    assert isinstance(r, NoMoney)

    r = mUSD.convert(USD, asof=Date("2019-01-02"), strict=True)  # No fx-rate from USD to USD.
    assert isinstance(r, NoMoney)

   

# Generated at 2022-06-14 04:48:06.048551
# Unit test for method add of class Money
def test_Money_add():
    a = Money.of(Currency.of('EUR'), 1, Date.today())
    b = Money.of(Currency.of('EUR'), 2, Date.today())
    c = Money.of(Currency.of('USD'), 2, Date.today())
    assert b == a.add(b)
    assert b == a.scalar_add(1)
    assert a == b.subtract(b)
    assert a == b.scalar_subtract(1)
    assert c == a.add(c)
    assert c == a.scalar_add(2)
    assert b == c.subtract(c)
    assert b == c.scalar_subtract(1)

# Generated at 2022-06-14 04:48:11.523814
# Unit test for method __pos__ of class Price
def test_Price___pos__():
    assert Money.of(CAD, 20) == +Money.of(CAD, -20)
    assert Money.of(CAD, -20) == +Money.of(CAD, -20)
    assert NoMoney == +NoMoney


# Generated at 2022-06-14 04:48:15.581625
# Unit test for method __floordiv__ of class Money
def test_Money___floordiv__():
    money = Money.of("USD", Decimal("1000"), Date.today())
    assert money.__floordiv__(Decimal("10")) == 100.0

# Generated at 2022-06-14 04:48:24.130542
# Unit test for method __neg__ of class Price
def test_Price___neg__():
    # Test method docstring defined.
    assert Price.__neg__.__doc__ is not None
    # Test method arguments count.
    assert Price.__neg__.__func__.__code__.co_argcount == 1
    # Test NoPrice as operand.
    assert not NoPrice
    assert NoPrice == NoPrice
    assert NoPrice.__neg__() == NoPrice
    # Test SomePrice as operand.
    assert SomePrice(1, 1, 2) == SomePrice(1, 1, 2)
    assert SomePrice(1, 1, 2).__neg__() == SomePrice(-1, -1, 2)

# Generated at 2022-06-14 04:48:34.874125
# Unit test for method convert of class SomeMoney
def test_SomeMoney_convert():
    import mypackage.testdata as tds
    usd = tds.usd
    eur = tds.eur
    date1 = tds.date1
    date2 = tds.date2
    date3 = tds.date3
    date4 = tds.date4
    date5 = tds.date5

    ## Setup service:
    register_fx_rate_service("my_service", tds.MyFxRateService("my_service"))

    ## And service:
    assert get_fx_rate_service("my_service") is not None

    ## Setup default service:
    set_fx_rate_provider("my_service")

    ## Check default:
    assert FXRateService.default is not None

    ## Check undefined money object:

# Generated at 2022-06-14 04:48:40.032288
# Unit test for method round of class Price
def test_Price_round():
    Price.of(USD, Decimal("10.00"), Date.today())
    Price.of(USD, Decimal("10.25"), Date.today())
    Price.of(USD, Decimal("10.75"), Date.today())
    Price.of(USD, Decimal("10.50"), Date.today())

# Generated at 2022-06-14 04:52:03.085348
# Unit test for method __eq__ of class Price
def test_Price___eq__():
    """Test for method .__eq__ of class Price"""

    # Case A: Bad case
    # None object should not be compared with another object
    # Except AssertionError
    with raises(AssertionError):
        assert (None == Money.of(Currency.USD, 10, Date.current()))

    # Case B: Good case
    # Empty price object should be compared to another empty price object
    assert (Price.of(Currency.USD, None, None) == Price.of(Currency.USD, None, None))
    # Equal price objects should be equal
    assert (Price.of(Currency.USD, Decimal(10), Date.current()) ==
            Price.of(Currency.USD, Decimal(10), Date.current()))
    # Unequal price objects should not be equal

# Generated at 2022-06-14 04:52:14.348885
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    from .currencies import Currency
    from .money import Money
    from .prices import Price
    from .usd import USD

    # UNIT TEST: Test undefined money:
    assert Money.NA.floor_divide(USD(5)) == Money.NA

    # UNIT TEST: Test floor divide:
    m1 = USD(6)
    assert m1.floor_divide(USD(5)) == USD(1)
    assert m1.floor_divide(USD(3)) == USD(2)
    assert m1.floor_divide(USD(1.5)) == USD(4)
    assert m1.floor_divide(USD(0.5)) == USD(12)
    assert m1.floor_divide(USD(0.1)) == USD(60)

# Generated at 2022-06-14 04:52:24.595182
# Unit test for method __int__ of class Price
def test_Price___int__():
    def test_factory(sign: int, _ccy: Currency, _qty: Decimal, _dov: Date) -> Price:
        return Price.of(_ccy, _qty, _dov)

    # Define test cases with tuples of:
    # * input arguments,
    # * expected return values/exceptions.

# Generated at 2022-06-14 04:52:29.428506
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    from .currencies import Currency
    from .money import Money
    from .exchange import DummyFXRateService

    m1 = Money.of(Currency.USD, 12.5, Date.now())
    m2 = m1.floor_divide(2)
    print(m2)



# Generated at 2022-06-14 04:52:38.407635
# Unit test for method as_boolean of class Price
def test_Price_as_boolean():
    assert Price.of(None, 10, today()).as_boolean() == True
    assert Price.of(None, 0, today()).as_boolean() == False
    assert Price.of(None, None, today()).as_boolean() == False
    assert Price.of(None, 10, today()).as_boolean() == True
    assert Price.of(None, 0, today()).as_boolean() == False
    assert Price.of(None, None, today()).as_boolean() == False
    
## noinspection PyShadowingBuiltins

# Generated at 2022-06-14 04:52:42.567526
# Unit test for method as_integer of class Price
def test_Price_as_integer():
    x = Price.of("USD", 100, "2020-11-01")
    assert(x.as_integer() == 100)
    assert(Price.of("USD", 1.21, "2020-11-01").as_integer() == 1)

# Generated at 2022-06-14 04:52:55.333585
# Unit test for method is_equal of class Price
def test_Price_is_equal():
    assert Price.of(EUR, 1.0, None).is_equal(Price.of(EUR, 1.0, None))
    assert not Price.of(EUR, 1.0, None).is_equal(Price.of(GBP, 1.0, None))
    assert not Price.of(GBP, 1.0, None).is_equal(Price.of(EUR, 1.0, None))
    assert not Price.of(GBP, 1.2, None).is_equal(Price.of(GBP, 1.0, None))
    assert not Price.of(GBP, 1.0, "2019-11-10").is_equal(Price.of(GBP, 1.0, "2019-11-11"))

# Generated at 2022-06-14 04:53:08.325157
# Unit test for method abs of class Price
def test_Price_abs():
  assert Price.of(ccy='USD', qty=Decimal('-10.000000'),dov=date(2020,1,1)).abs()== Price.of(ccy='USD', qty=Decimal('10.000000'),dov=date(2020,1,1))
  assert Price.of(ccy='EUR', qty=Decimal('-10.000000'),dov=date(2020,1,1)).abs()== Price.of(ccy='EUR', qty=Decimal('10.000000'),dov=date(2020,1,1))

# Generated at 2022-06-14 04:53:16.743997
# Unit test for method __eq__ of class Price
def test_Price___eq__():
    # Setup
    p1 = Price.of(EUR, Decimal(4.4), Date.today())
    p2 = Price.of(EUR, Decimal(4.4), Date.today())
    p3 = Price.of(EUR, Decimal(4.4), Date.today())
    p4 = Price.of(EUR, Decimal(4.4), Date.today())
    
    # Exercise
    r1 = p1 == p2
    r2 = p1 == p3
    r3 = p1 == p4
    # Verify
    assert p1 == p2
    assert p2 == p3
    assert p3 == p4
    assert p1 == p3
    assert p2 == p4
    assert p2 == p1
    assert p3 == p2
    assert p4 == p3

# Generated at 2022-06-14 04:53:22.281658
# Unit test for method as_float of class Money
def test_Money_as_float():
    assert NoneMoney.as_float() == 0.
    assert SomeMoney(Currency.USD, Decimal("0.01"), Date.now()).as_float() == 0.01
