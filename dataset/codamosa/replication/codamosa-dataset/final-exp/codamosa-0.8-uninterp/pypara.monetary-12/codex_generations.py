

# Generated at 2022-06-14 04:49:47.184158
# Unit test for method convert of class Money
def test_Money_convert():
    x1 = Money(Currency('JPY'), 100)
    x2 = Money(Currency('USD'), 100)
    assert x1.convert(Currency('USD'), Date(2020,1,1)) == x2



# Generated at 2022-06-14 04:49:59.067503
# Unit test for method __lt__ of class Money
def test_Money___lt__():
    from dataclasses import InitVar
    from .currencies import EUR

    class Money(Money):
        """
        Provides an implementation for the abstract Money class above.
        """

        NA: "Money" = NoneMoney

        ccy: Currency
        qty: Decimal
        dov: Date

        def __init__(
            self, ccy: Currency, qty: Optional[Decimal] = None, dov: Optional[Date] = None,
        ) -> None:
            self.ccy = ccy
            self.qty = ccy.quantize(qty or 0)
            self.dov = dov or Date.today()

        def is_equal(self, other: Any) -> bool:
            return isinstance(other, Money) and self.ccy == other.ccy and self.qty == other.q

# Generated at 2022-06-14 04:50:11.836577
# Unit test for method gte of class Money
def test_Money_gte():
    from .currencies import USD, TRY
    from .exchange import FXRateLookupError
    from .money import Money, NoMoney, SomeMoney

    assert Money.of(None, None, None) >= Money.of(None, None, None)
    assert Money.of(None, None, None) >= SomeMoney(TRY, 100, "2018-12-01")
    assert SomeMoney(TRY, 100, "2018-12-01") >= Money.of(None, None, None)
    assert SomeMoney(TRY, 100, "2018-12-01") >= SomeMoney(USD, 100, "2018-12-01") is False
    assert SomeMoney(TRY, 100, "2018-12-01") >= SomeMoney(TRY, 99, "2018-12-01") is True

# Generated at 2022-06-14 04:50:21.579293
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    from es_common.model.currencies import Currency
    from es_common.model.types.date import Date

    # Test for convert on Price object with currency "USD" and quantity 100.0 on valid asof date
    price = Price.of(Currency.USD, Decimal(100.0), Date.of(2020, 1, 1))
    assert isinstance(price, SomePrice)
    assert price.convert(Currency.CAD, Date.of(2020, 1, 1), True) == Price.of(Currency.CAD, Decimal(1.32),
                                                                              Date.of(2020, 1, 1))

    # Test for convert on Price object with currency "USD" and quantity 100.0 on invalid asof date

# Generated at 2022-06-14 04:50:28.491283
# Unit test for method scalar_subtract of class Price
def test_Price_scalar_subtract():
    from hamcrest import assert_that, is_

    p = Price.of(USD, 1, D1)
    assert_that(p.scalar_subtract(1), is_(NoPrice))
    assert_that(p.scalar_subtract(Decimal("0")), is_(p))

    p = Price.of(USD, Decimal("1.222"), D1)
    assert_that(p.scalar_subtract(0), is_(p))
    assert_that(p.scalar_subtract(Decimal("1.22")), is_(Price.of(USD, Decimal("0.002"), D1)))

# Generated at 2022-06-14 04:50:30.065014
# Unit test for method __int__ of class Money
def test_Money___int__():
    money = Money.of(Currency.USD, Decimal("100"), Date(2020, 1, 1))

    int(money)



# Generated at 2022-06-14 04:50:32.578217
# Unit test for method as_integer of class Money
def test_Money_as_integer():
    from .currencies import USD
    from .commons.zeitgeist import Now

    assert SomeMoney(USD, Decimal(1.23), Now()).as_integer() == 1

# Generated at 2022-06-14 04:50:42.525762
# Unit test for method __sub__ of class SomeMoney
def test_SomeMoney___sub__():
    #simple object
    inst = SomeMoney(ccy=Currency.NONE, qty=Decimal(10), dov=Date.TODAY)
    #positive scenario
    #undefined other -> return self
    assert inst.__sub__(NoMoney) == inst
    #defined object, same currency
    other = SomeMoney(ccy=Currency.NONE, qty=Decimal(20), dov=Date.TODAY)
    assert inst.__sub__(other) == SomeMoney(ccy=Currency.NONE, qty=Decimal(-10), dov=Date.TODAY)
    #defined object, different currency => raise IncompatibleCurrencyError
    other = SomeMoney(ccy=Currency.GBP, qty=Decimal(20), dov=Date.TODAY)

# Generated at 2022-06-14 04:50:48.197798
# Unit test for method is_equal of class Money
def test_Money_is_equal():
    from pyts.markets.currencies import USD, EUR

    a = Money.of(USD, 1.0, Date(2017, 1, 1))
    b = Money.of(USD, 1.0, Date(2017, 1, 1))
    assert a.is_equal(b)

    c = Money.of(EUR, 1.0, Date(2017, 1, 1))
    assert not a.is_equal(c)

    d = Money.of(None, None, None)
    assert not a.is_equal(d)


# Generated at 2022-06-14 04:50:59.255519
# Unit test for method lte of class Money
def test_Money_lte():
    assert Money.of('USD', 10, '2000-01-01').lte(Money.of('USD', 10, '2001-01-01'))
    assert Money.of('USD', 10, '2000-01-01').lte(Money.of('USD', 10, '2000-01-01'))
    assert Money.of('USD', 10, '2000-01-01').lte(Money.of('USD', 11, '2000-01-01'))
    assert not Money.of('USD', 10, '2000-01-01').lte(Money.of('USD', 9, '2000-01-01'))
    assert not Money.of('USD', 10, '2000-01-01').lte(Money.of('JPY', 10, '2000-01-01'))

# Generated at 2022-06-14 04:51:38.954429
# Unit test for method convert of class Money
def test_Money_convert():
    """Unit test for method convert of class Money"""
    # fix rate for AUDUSD
    CcyPair = NamedTuple("CcyPair", [("ccy1", Currency),("ccy2", Currency)])
    Rate = NamedTuple("Rate", [("ccy_pair", CcyPair),("bid", float),("ask", float)])
    rates = [Rate(CcyPair("AUD","USD"), 0.7067, 0.7071)]
    def lookup(ccy1,ccy2,asof):
        if asof.day == 2:
            rate = Rate(CcyPair("USD","AUD"), 0.7075, 0.7079)
        else:
            rate = Rate(CcyPair("AUD","USD"), 0.7067, 0.7071)

# Generated at 2022-06-14 04:51:46.049566
# Unit test for method with_ccy of class Money
def test_Money_with_ccy():
    """
    Unit test for method with_ccy of class Money
    """
    m1 = Money.of(Currency.USD, 100.00, Date.today())
    m2 = m1.with_ccy(Currency.EUR)

    assert m2.ccy == Currency.EUR
    assert m2.qty == Decimal(100)
    assert m2 == Money.of(Currency.EUR, 100.00, Date.today())



# Generated at 2022-06-14 04:51:58.565420
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    assert SomePrice(AUD, 100, TODAY).convert(USD, TODAY, strict=False) == SomePrice(USD, 100 / 50, TODAY)
    assert SomePrice(AUD, 100, TODAY).convert(USD, TODAY, strict=True) == SomePrice(USD, 100 / 50, TODAY)
    assert SomePrice(AUD, 100, TODAY).convert(USD, TODAY + 10, strict=True) == SomePrice(USD, 100 / 50, TODAY + 10)
    assert SomePrice(AUD, 100, TODAY).convert(USD, TODAY, strict=False).convert(AUD, TODAY, strict=False) == \
        SomePrice(AUD, 100, TODAY)
    assert SomePrice(AUD, 100, TODAY).convert(USD, TODAY + 10, strict=True) == SomePrice(USD, 100 / 50, TODAY + 10)

# Generated at 2022-06-14 04:52:05.357241
# Unit test for method __lt__ of class Money
def test_Money___lt__():
    NoneMoney.__lt__(NoMoney)
    SomeMoney(Currency.USD, Decimal(0), Date.today()).__lt__(SomeMoney(Currency.USD, Decimal(1), Date.today()))
    assert SomeMoney(Currency.USD, Decimal(0), Date.today()).__lt__(SomeMoney(Currency.USD, Decimal(1), Date.today())) == True
    assert SomeMoney(Currency.USD, Decimal(0.3), Date.today()).__lt__(SomeMoney(Currency.USD, Decimal(0.4), Date.today())) == True
    assert SomeMoney(Currency.EUR, Decimal(0), Date.today()).__lt__(SomeMoney(Currency.EUR, Decimal(1), Date.today())) == True
    assert SomeMoney

# Generated at 2022-06-14 04:52:15.444883
# Unit test for method gt of class Money
def test_Money_gt():
    ccy1 = Currency("USD")
    m1 = Money.of(ccy1, Decimal("5.7"), Date.today())
    m2 = Money.of(ccy1, Decimal("5.8"), Date.today())
    m3 = Money.of(ccy1, Decimal("5.7"), Date.today())
    m_1 = Money.of(ccy1, Decimal("-5.7"), Date.today())
    m_2 = Money.of(ccy1, Decimal("-5.8"), Date.today())
    assert m2.gt(m1) 
    assert m1.gt(m_1) 
    assert m2.gt(m_2) 
    assert m1.gt(m_2) 
    assert m_2.gt(m_1) 


# Generated at 2022-06-14 04:52:26.501373
# Unit test for method __eq__ of class Money
def test_Money___eq__():
    assert NoneMoney == NoneMoney
    assert SomeMoney(Currency.USD, Decimal("10.00"), Date.today()).__eq__(SomeMoney(Currency.USD, Decimal("10.00"), Date.today())), "MMoney.__eq__(SomeMoney)"
    assert not SomeMoney(Currency.USD, Decimal("10.00"), Date.today()).__eq__(SomeMoney(Currency.USD, Decimal("11.00"), Date.today())), "MMoney.__eq__(SomeMoney)"
    assert not SomeMoney(Currency.USD, Decimal("10.00"), Date.today()).__eq__(SomeMoney(Currency.EUR, Decimal("10.00"), Date.today())), "MMoney.__eq__(SomeMoney)"

# Generated at 2022-06-14 04:52:29.965208
# Unit test for method __ge__ of class SomeMoney
def test_SomeMoney___ge__():
    assert SomeMoney.of(USD, 100, Date(2020, 1, 1)) >= SomeMoney.of(USD, 100, Date(2020, 1, 1))

# Generated at 2022-06-14 04:52:31.176462
# Unit test for method __pos__ of class Money
def test_Money___pos__():
    Money.NA.positive()



# Generated at 2022-06-14 04:52:34.295711
# Unit test for method as_integer of class Money
def test_Money_as_integer():
    print("testing method as_integer of class Money")
    assert Money.of("USD", 2, Date.now()).as_integer() == 2



# Generated at 2022-06-14 04:52:43.675855
# Unit test for method __eq__ of class Money
def test_Money___eq__():
    assert NoMoney == NoMoney
    assert SomeMoney(Currency("USD"), 100.0, Date.today()) == SomeMoney(Currency("USD"), 100.0, Date.today())
    assert SomeMoney(Currency("USD"), 100.0, Date.today()) != SomeMoney(Currency("EUR"), 100.0, Date.today())
    assert SomeMoney(Currency("EUR"), 100.0, Date.today()) != SomeMoney(Currency("EUR"), 200.0, Date.today())
    assert SomeMoney(Currency("EUR"), 200.0, Date.today()) != SomeMoney(Currency("EUR"), 200.0, Date.today() - 1)
    



# Generated at 2022-06-14 04:54:38.178754
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    x=SomePrice(Currency("EUR"),Decimal("1"),date(2020, 7, 30))
    assert x.convert(Currency("USD"),date(2020,7,30),strict=True)==NoPrice
    assert x.convert(Currency("USD"),date(2020,7,30))==NoPrice
    assert x.convert(Currency("USD"),date(2020,7,29))==NoPrice
    assert x.convert(Currency("USD"),date(2020,7,31))==NoPrice
    assert x.convert(Currency("JPY"),date(2020,7,30))==SomePrice(Currency("JPY"), Decimal("120.99"), date(2020, 7, 30))

# Generated at 2022-06-14 04:54:47.865508
# Unit test for method __gt__ of class Money
def test_Money___gt__():
    results = dict()
    for m in Money.__subclasses__():
        for n in Money.__subclasses__():
            results[(m,n)] = Money.of(Currency('GBp'),1,Date.today()).__gt__(Money.of(Currency('GBp'),1,Date.today()))
    assert results == {
        (SomeMoney, SomeMoney): True,
        (SomeMoney, NoneMoney): True,
        (SomeMoney, NoMoney): True,
        (NoneMoney, SomeMoney): True,
        (NoneMoney, NoneMoney): True,
        (NoneMoney, NoMoney): True,
        (NoMoney, SomeMoney): True,
        (NoMoney, NoneMoney): True,
        (NoMoney, NoMoney): True
    }
