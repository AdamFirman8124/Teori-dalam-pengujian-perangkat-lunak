

# Generated at 2022-06-14 04:48:52.121874
# Unit test for method floor_divide of class Price
def test_Price_floor_divide():
    assert NoPrice.floor_divide(2) == NoPrice
    assert SomePrice(USD, Decimal('10'), Date(2020, 1, 1)).floor_divide(2) == SomePrice(USD, Decimal('5'), Date(2020, 1, 1))
    with pytest.raises(MonetaryOperationException):
        SomePrice(USD, Decimal('10.10'), Date(2020, 1, 1)).floor_divide(2)

# Generated at 2022-06-14 04:49:02.356459
# Unit test for method __le__ of class Price
def test_Price___le__():
    m1 = Money.of(USD, 100.0)
    m2 = Money.of(USD, 200.0)
    m3 = Money.of(USD, 100.0)
    m4 = Money.of(EUR, 100.0)
    m5 = Money.of(CHF, 100.0)
    m6 = Money.of(GBP, 100.0)
    assert not m1.__le__(m2)
    assert m1.__le__(m3)
    assert m1.__lt__(m2)
    assert not m1.__lt__(m3)
    assert not m1.__lt__(m4)
    assert not m1.__lt__(m5)
    assert not m1.__lt__(m6)

# Generated at 2022-06-14 04:49:12.484194
# Unit test for method gt of class Money
def test_Money_gt():
    # Undefined money objects are never greater than or equal to ``other`` if ``other`` is defined
    assert (Money.of('GBP', 3.55, Date.today()) > NoMoney) == True
    # Defined money objects are always greater than ``other`` if other is undefined
    assert (Money.of(None, 3.55, Date.today()) > NoMoney) == False
    # :class:`IncompatibleCurrencyError` is raised when comparing two defined money 
    # objects with different currencies.
    with pytest.raises(IncompatibleCurrencyError):
        Money.of('GBP', 3.55, Date.today()) > Money.of('EUR', 3.55, Date.today())


# Generated at 2022-06-14 04:49:23.469600
# Unit test for method gt of class Money
def test_Money_gt():
    from .currencies import USD, EUR
    from .commons.zeitgeist import yesterday, today
    m1 = Money.of(USD, 10, today)
    m2 = Money.of(USD, 10, today)
    m3 = Money.of(EUR, 10, today)
    m4 = Money.of(USD, 20, today)
    m5 = Money.of(USD, 10, yesterday)
    assert m1 == m2
    assert m1.gt(m2) is False
    assert m2.gt(m1) is False
    assert m1.gt(m3) is True
    assert m1.gt(m4) is False
    assert m1.gt(m5) is True


# Generated at 2022-06-14 04:49:35.214507
# Unit test for method lt of class Price
def test_Price_lt():
    print('Test method lt of class Price')
    tst = Money.of('EUR', 30, Date.new(2018, 12, 31))
    tst2 = Money.of('CHF', 10, Date.new(2018, 12, 31))
    assert not tst.lt(tst2), "method lt of class Money should return priceobject is not less than other"
    tst = Money.of('EUR', 30, Date.new(2018, 12, 31))
    tst2 = Money.of('EUR', 30, Date.new(2018, 12, 31))
    assert not tst.lt(tst2), "method lt of class Money should return priceobject is not less than other"
    tst = Money.of('EUR', 0, Date.new(2018, 12, 31))

# Generated at 2022-06-14 04:49:39.486558
# Unit test for method __mul__ of class Money
def test_Money___mul__():
    monetary = tcc.money("1.25", "USD")
    assert monetary.__mul__(2) == tcc.money("2.50", "USD")
from tcc.contrib import lmx



# Generated at 2022-06-14 04:49:47.980231
# Unit test for method floor_divide of class Price
def test_Price_floor_divide():
    # Defined price object.
    price1 = Price.of(ccy=Currency.USD,qty=Decimal('1.517'),dov=date(2019, 1, 1))
    price2 = Price.of(ccy=Currency.USD,qty=Decimal('2.1'),dov=date(2019, 1, 1))
    assert price1.floor_divide(Decimal('1.500')) == Price.of(ccy=Currency.USD,qty=Decimal('1'),dov=date(2019, 1, 1))
    assert price2.floor_divide(Decimal('1.500')) == Price.of(ccy=Currency.USD,qty=Decimal('1'),dov=date(2019, 1, 1))
    # Undefined currency.

# Generated at 2022-06-14 04:49:59.535969
# Unit test for method as_integer of class Money
def test_Money_as_integer():
    """
    Unit test for the method as_integer of class Money
    """
    import pytest
    
    undefined_money1 = Money.NA
    undefined_money2 = NoMoney
    some_money_USD = Money.of(Currency.USD, 10, Date.today())
    undefined_money3 = SomeMoney(Currency.USD, None, None)
    some_money_GBP = Money.of(Currency.GBP, 10, Date.today())
    
    def test_undefined_money1():
        with pytest.raises(MonetaryOperationException):
            undefined_money1.as_integer()
    
    def test_undefined_money2():
        with pytest.raises(MonetaryOperationException):
            undefined_money2.as_integer()
    

# Generated at 2022-06-14 04:50:05.872603
# Unit test for method is_equal of class Money
def test_Money_is_equal():
    # Case.1
    ccy = Currency.get("USD")
    qty = Decimal("100.50")
    dov = Date.today()
    usd_amt_1 = SomeMoney(ccy, ccy.quantize(qty), dov)
    usd_amt_2 = SomeMoney(ccy, ccy.quantize(qty), dov)
    assert usd_amt_1.is_equal(usd_amt_2) is True

    # Case.2
    other = "USD 100.50"
    assert usd_amt_1.is_equal(other) is False



# Generated at 2022-06-14 04:50:13.446496
# Unit test for method times of class Price
def test_Price_times():
    fx_rate = FXRate(Currency.USD, Currency.EUR, Decimal(1.2), Date(2020, 1, 4))

    # Not enough argument test
    try:
        Price.times()
    except TypeError as err:
        assert err.__str__() == "times() missing 2 required positional arguments: 'self' and 'other'"

    # Regular test
    assert Price.of(Currency.USD, Decimal(10), Date(2020, 1, 4)).times(Price.of(Currency.EUR, Decimal(10), Date(2020, 1, 4))).as_float() == 200.00

    # Undefined price test

# Generated at 2022-06-14 04:51:27.598237
# Unit test for method lt of class Price
def test_Price_lt():
    assert NoPrice.lt(SomePrice(Currency.USD, Decimal("1.0"), Date(19, 8, 24)))
    assert SomePrice(Currency.USD, Decimal("0.1"), Date(19, 8, 24)).lt(SomePrice(Currency.USD, Decimal("1.0"), Date(19, 8, 24)))
    assert not SomePrice(Currency.USD, Decimal("1.0"), Date(19, 8, 24)).lt(SomePrice(Currency.USD, Decimal("0.1"), Date(19, 8, 24)))
    assert not SomePrice(Currency.USD, Decimal("1.0"), Date(19, 8, 24)).lt(SomePrice(Currency.USD, Decimal("1.0"), Date(19, 8, 24)))



# Generated at 2022-06-14 04:51:33.058092
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    # given
    m = Money.of(Currency.EUR, 100, Date.today())

    # when
    actual = m.floor_divide(2)

    # then
    assert isinstance(actual, Money)
    assert actual.ccy == Currency.EUR
    assert actual.qty == 50
    assert actual.dov == Date.today()
Money



# Generated at 2022-06-14 04:51:46.173769
# Unit test for method __mul__ of class Money
def test_Money___mul__():
    """
    SomeMoney * Numeric -> SomeMoney
    (SomeMoney * Numeric) -> SomeMoney
    SomeMoney * SomeMoney -> MonetaryOperationException
    SomeMoney * NoMoney -> NoMoney
    NoMoney * SomeMoney -> NoMoney
    NoMoney * NoMoney -> NoMoney
    """
    m1 = SomeMoney(Currency.USD, 1234.4567, Date.today())
    m2 = SomeMoney(Currency.TRY, 123.456, Date.today())
    assert m1 * 3 == SomeMoney(
        Currency.USD, 1234.4567 * 3, Date.today()
    )  # SomeMoney * Numeric -> SomeMoney
    assert (m1 * 3) == SomeMoney(
        Currency.USD, 1234.4567 * 3, Date.today()
    )  # (SomeMoney * Numeric) -> Some

# Generated at 2022-06-14 04:51:57.789100
# Unit test for method positive of class Price
def test_Price_positive():
    assert NoPrice.positive() == NoPrice
    assert SomePrice(ccy=USD, qty=Decimal("0"), dov=Date.today()).positive() == SomePrice(ccy=USD, qty=Decimal("0"), dov=Date.today())
    assert SomePrice(ccy=USD, qty=Decimal("10"), dov=Date.today()).positive() == SomePrice(ccy=USD, qty=Decimal("10"), dov=Date.today())
    assert SomePrice(ccy=USD, qty=Decimal("-10"), dov=Date.today()).positive() == SomePrice(ccy=USD, qty=Decimal("10"), dov=Date.today())


# Generated at 2022-06-14 04:52:10.122583
# Unit test for method __add__ of class Price
def test_Price___add__():
    #
    # __add__, 1
    #
    m1_1 = Money(10, Currency.USD.code, Date(2020, 3, 3))
    m2_1 = Money(20, Currency.USD.code, Date(2020, 2, 1))
    p1_1 = Price(m1_1, m2_1, Date(2020, 3, 3))

    m3_1 = Money(20, Currency.USD.code, Date(2020, 2, 2))
    m4_1 = Money(40, Currency.USD.code, Date(2020, 1, 1))
    p2_1 = Price(m3_1, m4_1, Date(2020, 3, 3))

    m5_1 = Money(30, Currency.USD.code, Date(2020, 3, 3))

# Generated at 2022-06-14 04:52:14.803149
# Unit test for method __neg__ of class Money
def test_Money___neg__():
    """
    Makes sure that class:`MonetrayOperationException` is raised if call-site attempts to negate an
    undefined money.
    """
    mo = NoMoney
    with pytest.raises(MonetaryOperationException):
        assert -mo


## Unit test for method __pos__ of class Money

# Generated at 2022-06-14 04:52:25.432347
# Unit test for method add of class Price
def test_Price_add():
    firstPrice = Price.of(None, None, None)
    secondPrice = Price.of(None, None, None)
    resultPrice = firstPrice.add(secondPrice)
    assert resultPrice.undefined is True
    assert resultPrice.defined is False

    firstPrice = Price.of('USD', 100, '2020-02-01')
    secondPrice = Price.of('USD', 10, '2020-02-01')
    resultPrice = firstPrice.add(secondPrice)
    assert resultPrice.undefined is False
    assert resultPrice.defined is True
    assert resultPrice.ccy == 'USD'
    assert resultPrice.qty == 110
    assert resultPrice.dov == '2020-02-01'

    firstPrice = Price.of('USD', 100, '2020-02-01')
    secondPrice = Price.of

# Generated at 2022-06-14 04:52:33.128734
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    assert Round(USD(0.01) + 12) == USD(12.01)
    assert (USD(0.01) + 12) == USD(12.01)
    assert USD(0.01) + 12 == USD(12.01)
    assert 12 + USD(0.01) == USD(12.01)
    assert USD(0.01) + Round(12) == USD(12.01)
    assert Round(USD(0.01) + 12.0) == USD(12.01)

# Generated at 2022-06-14 04:52:44.077538
# Unit test for method __sub__ of class Money
def test_Money___sub__():
    from tests.mop.money import money1, money2
    m1 = money1
    m2 = money2
    res = m1.__sub__(m2)
    assert res is not money1
    assert res is not money2
    assert isinstance(res, Money) is True
    assert bool(money1) is True
    assert bool(money2) is True
    assert bool(res) is True
    assert type(res.ccy) == Currency
    assert type(res.qty) == Decimal
    assert res.defined is True
    assert res.undefined is False
    assert money1.is_equal(res) is False
    assert money2.is_equal(res) is False
    assert res.is_equal(Money.of(res.ccy, res.qty, res.dov)) is True


# Generated at 2022-06-14 04:52:50.557812
# Unit test for method __floordiv__ of class Money
def test_Money___floordiv__():
    from .currencies import Currency

    ccy = Currency("USD")

    m1 = SomeMoney(ccy, Decimal("2.00"), Date.today())

    assert (m1 / 2) == SomeMoney(ccy, Decimal("1.00"), Date.today())
    assert (m1 // 2) == SomeMoney(ccy, Decimal("1.00"), Date.today())



# Generated at 2022-06-14 04:53:16.974906
# Unit test for method lte of class Money
def test_Money_lte():
    class Test:
        def setUp(self):
            self.ccy = Currency.USD
            self.ccy2 = Currency.EUR
            self.m1 = Money.of(None,1,None)
            self.m2 = Money.of(self.ccy,1,None)
            self.m3 = Money.of(self.ccy2,2,None)
            self.m4 = Money.of(self.ccy,2,None)
            self.m5 = Money.of(self.ccy,1,None)
            self.m6 = Money.of(self.ccy,1,None)
        def test_when_none_then_return_true(self):
            self.assertTrue(self.m1.lte(self.m1))

# Generated at 2022-06-14 04:53:28.701496
# Unit test for method __int__ of class Money
def test_Money___int__():
    """
    Tests method __int__ of class Money
    """
    assert int(SomeMoney('USD', Decimal("1.0"), Date("2020-12-10"))) == 1
    assert int(SomeMoney('USD', Decimal("1"), Date("2020-12-10"))) == 1
    assert int(SomeMoney('USD', 1, Date("2020-12-10"))) == 1
    assert int(SomeMoney('USD', Decimal("1.5"), Date("2020-12-10"))) == 1
    assert int(SomeMoney('USD', Decimal("1.9"), Date("2020-12-10"))) == 1

    assert int(NoMoney) == 0

# Generated at 2022-06-14 04:53:32.882641
# Unit test for method as_integer of class Money
def test_Money_as_integer():
    # pylint: disable=unused-variable,expression-not-assigned
    with NoMoney as money:
        assert money.as_integer() == 0

    with SomeMoney(ccy=Currency.USD, qty=1, dov=Date.today()) as money:
        assert money.as_integer() == 1

# Generated at 2022-06-14 04:53:41.556827
# Unit test for method lte of class Money
def test_Money_lte():
    money = Money.of("USD", 100.1, Date.today())
    assert money.lte(money) is True
    assert (money <= Money.of("USD", 100, Date.today())) is False
    assert (money <= Money.of("USD", 100.1, Date.today())) is True
    assert (money <= Money.of("USD", 100.15, Date.today())) is True
    assert (money <= Money.of("EUR", 100, Date.today())) is True
    with pytest.raises(IncompatibleCurrencyError):
        money <= Money.of("USD", 100.1, Date.one_month_after(Date.today()))
    assert (money <= NoMoney) is False
    assert (money <= NoMoney) is False
    assert (NoMoney <= NoMoney) is True

# Generated at 2022-06-14 04:53:49.024527
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():

    with pytest.raises(CurrencyError):
        assert SomeMoney("USD", Decimal("0.01234567891234"), None).round()

    assert SomeMoney("USD", Decimal("0.01234567891234"), None).round() == SomeMoney("USD", Decimal("0.012346"), None)
    assert SomeMoney("CAD", Decimal("0.01234567891234"), None).round() == SomeMoney("CAD", Decimal("0.012346"), None)
    assert SomeMoney("USD", Decimal("0.01234567891234"), None).round() != SomeMoney("CAD", Decimal("0.012346"), None)

# Generated at 2022-06-14 04:53:55.207293
# Unit test for method as_boolean of class Price
def test_Price_as_boolean():
    print("Testing as_boolean of class Price")
    #Test when it is defined
    assert SomePrice(EUR, Decimal(20.5), date(2019, 1, 3)).as_boolean()
    #Test when quantity is zero
    assert not SomePrice(EUR, Decimal(0), date(2019, 1, 3)).as_boolean()
    #Test when it is undefined
    assert not NoPrice.as_boolean()

test_Price_as_boolean()


# Generated at 2022-06-14 04:53:58.021107
# Unit test for method add of class Money
def test_Money_add():
    money1 = Money.of(ccy=Currency(), qty=1, dov=Date())
    money2 = Money.of(ccy=Currency(), qty=1, dov=Date())
    assert (money1 + money2) == Money.of(ccy=Currency(), qty=2, dov=Date())


# Generated at 2022-06-14 04:54:01.767735
# Unit test for method as_boolean of class Money
def test_Money_as_boolean():
    assert Money.NA.as_boolean() == False
    assert SomeMoney(None, None, None).as_boolean() == False
    assert SomeMoney(Currency.EUR, Decimal(0), Date.today).as_boolean() == False
    assert SomeMoney(Currency.EUR, Decimal(5), Date.today).as_boolean() == True
    
    

# Generated at 2022-06-14 04:54:04.449128
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    from cq.money import Money
    from cq.currencies import CNY
    from cq.zeitgeist.datetime import Date

    now = Date.now()
    m = Money.of(CNY, 1, now)
    assert m.dov == now
    assert m.with_dov(now + 1).dov == now + 1


# Generated at 2022-06-14 04:54:14.658497
# Unit test for method __sub__ of class Money
def test_Money___sub__():
    assert NoneMoney == Money.NA - Money.NA
    assert NoneMoney == NoneMoney - NoneMoney
    assert NoneMoney == NoneMoney - SomeMoney(ccy=Currency.EUR, qty=Decimal("1.0"), dov=Date.now())
    assert NoneMoney == SomeMoney(ccy=Currency.EUR, qty=Decimal("1.0"), dov=Date.now()) - NoneMoney
    assert SomeMoney(ccy=Currency.EUR, qty=Decimal("0"), dov=Date.now()) == SomeMoney(ccy=Currency.EUR, qty=Decimal("1.0"), dov=Date.now()) - SomeMoney(ccy=Currency.EUR, qty=Decimal("1.0"), dov=Date.now())