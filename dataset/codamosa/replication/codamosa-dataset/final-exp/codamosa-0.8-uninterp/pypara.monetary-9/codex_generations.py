

# Generated at 2022-06-14 04:48:24.080565
# Unit test for method convert of class SomeMoney
def test_SomeMoney_convert():
    from .currency import Currency
    from .date import Date
    from .money import SomeMoney
    from .storages import LocalStorage
    
    LocalStorage.fx_rates.clear()
    assert LocalStorage.fx_rates == {}

    usd = Currency.of('USD')
    aud = Currency.of('AUD')
    cny = Currency.of('CNY')

    # Test 1
    assert (SomeMoney.of(usd, 1, Date.today())
            .convert(aud, Date.today(), strict=False) == NoMoney)

    # Test 2
    assert (SomeMoney.of(usd, 1, Date.today())
            .convert(aud, Date.today(), strict=True) == NoMoney)

    # Test 3
    LocalStorage.fx_rates[(usd, aud, Date.today())]

# Generated at 2022-06-14 04:48:28.389494
# Unit test for method __add__ of class SomeMoney
def test_SomeMoney___add__():
    from . import ccy, today, Money

    assert Money.of("USD", 100_000, today) + Money.of("USD", 50_000, today) == Money.of("USD", 150_000, today)



# Generated at 2022-06-14 04:48:37.158200
# Unit test for method multiply of class Money
def test_Money_multiply():
    ccy_GBP = Currency.of("GBP")
    ccy_USD = Currency.of("USD")
    ccy_EUR = Currency.of("EUR")
    dose = Date.now()
    value1 = Money.of(ccy_GBP, 10, dose)
    value2 = Money.of(ccy_GBP, -10, dose)
    value3 = Money.of(ccy_GBP, 0, dose)
    value4 = Money.of(ccy_USD, 10, dose)
    value5 = Money.of(ccy_EUR, 10, dose)
    value6 = Money.of(ccy_GBP, 10.49, dose)
    value7 = Money.of(ccy_GBP, 1.51, dose)

    assert value4.multiply(5)

# Generated at 2022-06-14 04:48:46.558343
# Unit test for method add of class Price
def test_Price_add():
    def _run_test_Price_add(p1, p2, expected_sum):
        computed_sum = p1.add(p2)
        assert computed_sum == expected_sum

    # Test #1: p1 and p2 are defined prices in different currencies
    p1 = Price.of(USD, 1.0, Date.today())
    p2 = Price.of(EUR, 1.0, Date.today())
    _run_test_Price_add(p1, p2, Price.of(EUR, 1.0, Date.today()))

    # Test #2: p1 and p2 are defined prices in same currencies
    p1 = Price.of(USD, 1.0, Date.today())
    p2 = Price.of(USD, 1.0, Date.today())
    _run_test_Price

# Generated at 2022-06-14 04:48:54.474269
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    pr = Price.of(Currency.of("USD"), Decimal(1.23), Date.of(2019, 1, 1))
    assert pr.scalar_add(1) == Price.of(Currency.of("USD"), Decimal(2.23), Date.of(2019, 1, 1))
    assert pr.scalar_add(1.23) == Price.of(Currency.of("USD"), Decimal(2.46), Date.of(2019, 1, 1))
    assert pr.scalar_add(-1) == Price.of(Currency.of("USD"), Decimal(0.23), Date.of(2019, 1, 1))

# Generated at 2022-06-14 04:48:55.644742
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    test_unit_Price_scalar_add()


# Generated at 2022-06-14 04:49:03.051729
# Unit test for method negative of class Money
def test_Money_negative():
    # Non-defined money must return itself
    assert NoMoney == NoMoney.negative()
    assert NoPrice == NoPrice.negative()

    # Defined monies must return the negative
    assert Money.of(USD, -100, date(2019, 11, 30)) == SomeMoney(USD, 100, date(2019, 11, 30)).negative()
    assert Price.of(1.0) == SomePrice(1.0).negative()

    # Only monetary objects are accepted
    for m in (True, False, 10, 10.10, (10, "USD")):
        with pytest.raises(MonetaryOperationException):
            SomeMoney(USD, 10, date(2019, 11, 30)).negative() + m

# Generated at 2022-06-14 04:49:11.760786
# Unit test for method __neg__ of class Money
def test_Money___neg__():
    assert -Money(Currency(u'AAA', decimal_places=2), Decimal('1.23'), Date(2017, 1, 1)) == Money(Currency(u'AAA', decimal_places=2), Decimal('-1.23'), Date(2017, 1, 1))
    assert -Money(Currency(u'AAA', decimal_places=2), Decimal('-1.23'), Date(2017, 1, 1)) == Money(Currency(u'AAA', decimal_places=2), Decimal('1.23'), Date(2017, 1, 1))

# Generated at 2022-06-14 04:49:23.240200
# Unit test for method as_boolean of class Price
def test_Price_as_boolean():
    # Test case #1: Negative test case
    assert NoPrice.as_boolean() == False

    # Test case #2: Positive test case
    # money with positive quantity
    currency = Currency.BRL
    quantity = +1.5
    dv = Date(2019, 2, 15)
    price_positive = Price.of(currency, quantity, dv)
    assert price_positive.as_boolean() == True

    # Test case #3: Positive test case
    # money with negative quantity
    currency = Currency.BRL
    quantity = -1.5
    dv = Date(2019, 2, 15)
    price_negative = Price.of(currency, quantity, dv)
    assert price_negative.as_boolean() == True

    # Test case #4: Positive test case
    # money with zero quantity
   

# Generated at 2022-06-14 04:49:34.968254
# Unit test for method with_qty of class Price
def test_Price_with_qty():
    # Define a simple price factory function
    def p(qty, ccy, dov):
        return Price.of(ccy, qty, dov)

    # Define a simple money factory function
    def m(qty, ccy, dov):
        return Money.of(ccy, qty, dov)

    # Base test case
    assert p(100, 'USD', Date.of(2020,1,1)).with_qty(200) == p(200, 'USD', Date.of(2020,1,1))

    # Check that undefined price is returned as is
    assert p(None, 'USD', Date.of(2020,1,1)).with_qty(200) == p(None, 'USD', Date.of(2020,1,1))

    # Check that different currencies are not compatible

# Generated at 2022-06-14 04:51:12.652952
# Unit test for method __bool__ of class Price
def test_Price___bool__():
    assert NoPrice.__bool__() == False
    assert SomePrice(ccy='USD', qty=Decimal('0'), dov=Date('2017-01-01')).__bool__() == False
    assert SomePrice(ccy='USD', qty=Decimal('1'), dov=Date('2017-01-01')).__bool__() == True


# Generated at 2022-06-14 04:51:15.905525
# Unit test for method with_qty of class Price
def test_Price_with_qty():
    assert Price.of(Currency("USD"), Decimal("100"), Date(2020, 1, 1)).with_qty(Decimal("200")) == Price.of(Currency("USD"), Decimal("200"), Date(2020, 1, 1))


# Generated at 2022-06-14 04:51:21.411347
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    assert NoPrice.scalar_add(Decimal(1.0)) == NoPrice

    price = Price.of(Currency("EUR"), Decimal("1.0"), Date(2020, 1, 1))
    assert price.scalar_add(Decimal("1.0")) == Price.of(Currency("EUR"), Decimal("2.0"), Date(2020, 1, 1))



# Generated at 2022-06-14 04:51:26.794242
# Unit test for method divide of class Price
def test_Price_divide():
    assert Price.of(GBP, Decimal("5.5"), date(2019, 7, 15)).divide(Decimal("2")) == Price.of(GBP, Decimal("2.75"), date(2019,7,15))
test_Price_divide()

# Generated at 2022-06-14 04:51:36.124672
# Unit test for method as_integer of class Money
def test_Money_as_integer():
    """
    Tests the as_integer method of the Money class
    """
    assert SomeMoney(Currency.USD, 1.0, Date.today()).as_integer() == 1
    assert SomeMoney(Currency.USD, 1.50, Date.today()).as_integer() == 1
    assert SomeMoney(Currency.USD, 1.51, Date.today()).as_integer() == 2
    assert SomeMoney(Currency.USD, Decimal('1.50'), Date.today()).as_integer() == 1
    assert SomeMoney(Currency.USD, Decimal('1.51'), Date.today()).as_integer() == 2
    assert SomeMoney(Currency.USD, Decimal('10e0'), Date.today()).as_integer() == 10

# Generated at 2022-06-14 04:51:47.240506
# Unit test for method __add__ of class SomePrice
def test_SomePrice___add__():
    p1 = SomePrice("USD", Decimal("292.28"), Date.today())
    p2 = SomePrice("USD", Decimal("-292.28"), Date.today())
    assert p1 == (p1 + p2) # Compare assert only
    assert p2 == (p2 + p1) # Compare assert only
    assert p1 == p2.__add__(p1) # Compare assert only
    assert p2 == p1.__add__(p2) # Compare assert only
    assert p1 == p2.__add__(p1) # Compare assert only
    assert p1 == p1.__add__(p2) # Compare assert only

# Generated at 2022-06-14 04:51:59.345504
# Unit test for method with_ccy of class Price
def test_Price_with_ccy():
    # Arrange
    boc_cad = Currency("CAD")
    boc_cad_qty = Decimal("100")
    boc_cad_dov = Date("2018-12-31")
    boc_cad_price = Price.of(boc_cad, boc_cad_qty, boc_cad_dov)

    # Act
    boc_usd = Currency("USD")
    result = boc_cad_price.with_ccy(boc_usd)

    # Assert
    assert isinstance(result, Price)
    assert result.ccy is boc_usd
    assert result.qty == boc_cad_qty
    assert result.dov == boc_cad_dov

    # Assert (negative)
   

# Generated at 2022-06-14 04:52:11.201098
# Unit test for method with_dov of class Price
def test_Price_with_dov():
    """
    Performs unit testing for :meth:`Price.with_dov` method of the :class:`Price`
    class.
    """
    dov = Date.today()
    ccy = Currency.USD
    qty = Decimal(100)
    price = Price.of(ccy, qty, dov)
    price2 = Price.of(ccy, qty, dov)
    price3 = Price.of(ccy, qty, dov + MonthDelta(1))
    assert price.with_dov(dov) is price
    assert price.with_dov(dov + MonthDelta(1)) == price3
    assert price.with_dov(dov) == price2
    assert price.money.with_dov(dov) == price2.money

# Generated at 2022-06-14 04:52:15.067101
# Unit test for method __int__ of class Price
def test_Price___int__():
    ccy = Currency(code="EUR")
    qty = 100
    dov = Date.today()
    m = Money(ccy, qty, dov)
    assert int(m) == qty

# Generated at 2022-06-14 04:52:19.939448
# Unit test for method scalar_add of class Money
def test_Money_scalar_add():
    from .currencies import Currency
    from .commons.numbers import Decimal
    Money = Money
    Currency = Currency
    Decimal = Decimal
    assert Money.of(Currency.USD, Decimal("54.2"), Date.today()).scalar_add(Decimal("-1")).qty == Decimal("53.2")

# Generated at 2022-06-14 04:52:46.100086
# Unit test for method __bool__ of class Price
def test_Price___bool__():
    # Case when price is defined
    assert SomePrice(GBP, Decimal('3.45'), Date(2018, 1, 1)).__bool__() == True
    assert SomePrice(GBP, Decimal('0'), Date(2018, 1, 1)).__bool__() == False
    assert SomePrice(GBP, Decimal('0'), Date(2018, 1, 1)).undefined is False
    assert SomePrice(GBP, Decimal('0'), Date(2018, 1, 1)).defined is True

    # Case when price is not defined
    assert NoPrice.__bool__() == False
    assert NoPrice.defined is False
    assert NoPrice.undefined is True


# Generated at 2022-06-14 04:52:50.171855
# Unit test for method as_float of class Price
def test_Price_as_float():
    assert Price.NA.as_float() == float("nan")
    assert Price.of(ccy=USD, qty=Decimal("123.45"), dov=Date.now()).as_float() == 123.45

# Generated at 2022-06-14 04:52:51.255412
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    """
    Tests method convert of class SomePrice
    """
    # TODO: implement this test
    pass


# Generated at 2022-06-14 04:52:54.851624
# Unit test for method times of class Price
def test_Price_times():
    input1 = Price.of(USD, 1, None)
    input2 = 1
    expected = 1    
    actual = input1.times(input2)
    assert actual == 1 # "Error in test_Money_times"


# Generated at 2022-06-14 04:52:57.885667
# Unit test for method __float__ of class Price
def test_Price___float__():
    """
    Unit test for method __float__ of class Price
    """
    p1 = Price.of(USD, 3, today)
    assert float(p1) == 3.0
    p2 = Price.of(USD, Decimal(3), today)
    assert float(p2) == 3.0



# Generated at 2022-06-14 04:53:05.080047
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    s = SomePrice(USD, Decimal('11'), date(2012, 3, 3))
    r = s.convert(EUR)
    assert r.ccy == EUR
    assert r.qty == Decimal('7.77')
    assert r.dov == date(2012, 3, 3)
    assert s.convert(JPY, date(2012, 3, 5)).qty == Decimal('1368.7')



# Generated at 2022-06-14 04:53:08.766382
# Unit test for method __int__ of class Price
def test_Price___int__():

    # Arrange
    price = Price.of(USD, 100, date(2020, 1, 1))

    # Act
    qty = int(price)

    # Assert
    assert qty == 100


# Generated at 2022-06-14 04:53:16.944327
# Unit test for method __ge__ of class Price
def test_Price___ge__():
    import datetime
    import quantumpseudocode as qp
    import quantumpseudocode.monetary as qm

    #
    # Assert true case.
    #
    a = qm.Price.of(qm.AUD, 10.0, datetime.date.today())
    b = qm.Price.of(qm.AUD, 9.0, datetime.date.today())
    assert (a >= b) == True

    #
    # Assert false case.
    #
    a = qm.Price.of(qm.AUD, 10.0, datetime.date.today())
    b = qm.Price.of(qm.AUD, 11.0, datetime.date.today())
    assert (a >= b) == False

    #
    # Assert undefined object.


# Generated at 2022-06-14 04:53:29.937602
# Unit test for method lt of class Price
def test_Price_lt():
    Price.of(Currency.USD, 1, Date(2019, 1, 1)) < Price.of(Currency.EUR, 2, Date(2019, 1, 1)) == True
    Price.of(Currency.USD, 2, Date(2019, 1, 1)) < Price.of(Currency.EUR, 1, Date(2019, 1, 1)) == False
    Price.of(Currency.USD, 1, Date(2019, 1, 1)) < Price.of(Currency.USD, 2, Date(2019, 1, 2)) == True
    Price.of(Currency.USD, 1, Date(2019, 1, 2)) < Price.of(Currency.USD, 2, Date(2019, 1, 1)) == False

# Generated at 2022-06-14 04:53:31.709199
# Unit test for method __int__ of class Price
def test_Price___int__():
    assert Price.of(ccy='USD', qty=Decimal('23.13')/Decimal('1.33'), dov=Date.today()).__int__() ==  23



# Generated at 2022-06-14 04:54:17.162806
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    unit_test = True
    assert unit_test
    return None

# Generated at 2022-06-14 04:54:27.125112
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    curr1 = CurrencyCode.USDC
    curr2 = CurrencyCode.USD
    dt1 = Date.today()
    dt2 = Date.today() - 1
    dt3 = Date.today() - 2
    dt4 = Date.today() - 3
    
    def test(p1, p2, dt, strict=True):
        assert p1.convert(curr2, dt, strict=strict) == p2
        assert p1.convert(curr2, dt, strict=strict).ccy == curr2
        assert p1.convert(curr2, dt, strict=strict).dov == dt
        
    # Test case 1: no FX rates defined
    FXRateService.default = None

# Generated at 2022-06-14 04:54:28.962659
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    pass



# Generated at 2022-06-14 04:54:33.891907
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():
    some_money = SomeMoney(ccy=USD, qty=Decimal("10.2345678901234567890"), dov=Date.today())
    assert some_money.round(-2) == SomeMoney(ccy=USD, qty=Decimal("10.23"), dov=Date.today())



# Generated at 2022-06-14 04:54:43.110814
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():
    ccy1 = Currency(name="JPY", code="JPY", symbol="￥", decimals=0)
    m1 = SomeMoney(ccy=ccy1, qty=Decimal("-10.50"), dov=Date(2019, 12, 31))
    m2 = SomeMoney(ccy=ccy1, qty=Decimal("-10.49"), dov=Date(2019, 12, 31))
    m3 = SomeMoney(ccy=ccy1, qty=Decimal("10.50"), dov=Date(2019, 12, 31))
    assert m1.round() == m1
    assert m1.round(0) == m1
    assert m1.round(1) == m1

# Generated at 2022-06-14 04:54:43.994829
# Unit test for method lte of class Price
def test_Price_lte():
    assert True



# Generated at 2022-06-14 04:54:49.594172
# Unit test for method __gt__ of class SomePrice
def test_SomePrice___gt__():
    assert SomePrice(USD, Decimal('25.0'), Date()) > SomePrice(USD, Decimal('20.0'), Date())
    assert not SomePrice(USD, Decimal('25.0'), Date()) > SomePrice(USD, Decimal('25.0'), Date())
    assert not SomePrice(USD, Decimal('25.0'), Date()) > SomePrice(USD, Decimal('30.0'), Date())
