

# Generated at 2022-06-14 04:48:45.581480
# Unit test for method gte of class Money
def test_Money_gte():
    assert Money.of(ccy=Usd, qty=1, dov=Date.today()) >= Money.of(ccy=Usd, qty=0, dov=Date.today())
    assert Money.of(ccy=Usd, qty=1, dov=Date.today()) >= Money.of(ccy=Usd, qty=1, dov=Date.today())
    assert Money.of(ccy=Eur, qty=1, dov=Date.today()) >= Money.of(ccy=Eur, qty=0, dov=Date.today())
    assert Money.of(ccy=Eur, qty=1, dov=Date.today()) >= Money.of(ccy=Eur, qty=1, dov=Date.today())

# Generated at 2022-06-14 04:48:47.531385
# Unit test for method __floordiv__ of class Money
def test_Money___floordiv__():
    # self = Money = NoMoney
    # self = Money = SomeMoney
    pass


# Generated at 2022-06-14 04:48:53.543109
# Unit test for method __pos__ of class Price
def test_Price___pos__():
    assert is_equal(SomePrice(CCY_USD, Decimal("+1.23"), Date.create(2019, 1, 1)).positive(), SomePrice(CCY_USD, Decimal("+1.23"), Date.create(2019, 1, 1)))
    assert is_equal(SomePrice(CCY_USD, Decimal("-1.23"), Date.create(2019, 1, 1)).positive(), SomePrice(CCY_USD, Decimal("+1.23"), Date.create(2019, 1, 1)))
    assert NoPrice.positive() is NoPrice

# Generated at 2022-06-14 04:49:02.007343
# Unit test for method multiply of class Money
def test_Money_multiply():
    """
    Test case for method multiply of class Money
    """
    ## Define the data:
    m1 = Money.of(USD, Decimal(100), Date(2019, 12, 31))
    m2 = Money.of(USD, Decimal(100), Date(2019, 12, 31))
    m3 = Money.NA
    ## Define the expected results:
    ## Test:
    assert m1.multiply(2) == m2
    assert m1.multiply(-2) == -m2
    assert m1.multiply(2) != m3
    ## Test the exception:
    try:
        m1.multiply(m1)
    except Exception as err:
        assert isinstance(err, TypeError)


# Generated at 2022-06-14 04:49:04.102370
# Unit test for method __floordiv__ of class SomeMoney
def test_SomeMoney___floordiv__():
    # simple
    assert SomeMoney(USD, 10, Date("2019-01-01")) // 2 == SomeMoney(USD, 5, Date("2019-01-01"))
    try:
        SomeMoney(USD, 10, Date("2019-01-01")) // 0
        assert False
    except (InvalidOperation, DivisionByZero):
        pass



# Generated at 2022-06-14 04:49:15.091057
# Unit test for method __ge__ of class SomeMoney
def test_SomeMoney___ge__():
    ##
    ## Example 1:
    ##
    a = SomeMoney(CAD, 10, "2020-01-01")
    b = SomeMoney(CAD, 10, "2020-01-01")

    assert a >= b

    ##
    ## Example 2:
    ##
    a = SomeMoney(CAD, 10, "2020-01-01")
    b = SomeMoney(CAD, 20, "2020-01-01")

    assert not (a >= b)

    ##
    ## Example 3:
    ##
    a = SomeMoney(CAD, 10, "2020-01-01")
    b = NoMoney

    assert a >= b

    ##
    ## Example 4:
    ##
    a = SomeMoney(CAD, 10, "2020-01-01")

# Generated at 2022-06-14 04:49:18.905184
# Unit test for method __float__ of class Money
def test_Money___float__():
    assert float(Money.of(Currency("USD"), Decimal("10.10"), Date(2016, 1, 1))) == 10.10  # type: ignore


# Generated at 2022-06-14 04:49:22.459405
# Unit test for method negative of class Price
def test_Price_negative():
    assert Price.of(USD, Decimal('-1.23'), TODAY) == Price.of(USD, Decimal('1.23'), TODAY).negative()
## Unit test for method scalar_subtract of class Price

# Generated at 2022-06-14 04:49:31.885354
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    # Arrange
    ccy = Currency.of("EUR")
    qty = 1
    dov = Date.today()
    money = SomeMoney(ccy, qty, dov)
    expected_dov = Date.of("2020-06-01")
    # Act
    new_money = money.with_dov(expected_dov)
    # Assert
    assert new_money.ccy == money.ccy
    assert new_money.qty == money.qty
    assert new_money.dov == expected_dov
    assert new_money != money

test_Money_with_dov()



# Generated at 2022-06-14 04:49:38.175112
# Unit test for method add of class Money
def test_Money_add():
    m = Money(ccy=eur, date=dt, qty=2.1)
    m2 = Money(ccy=eur, date=dt, qty=2.1)
    assert m.add(m2)== Money(ccy=eur, date=dt, qty=4.2)
    # Test different currency
    m3 = Money(ccy=usd,date=dt,qty=2.1)
    assert m.add(m3)==TypeError

# Generated at 2022-06-14 04:50:23.694213
# Unit test for method __sub__ of class Money
def test_Money___sub__():
    # Python does not support tuple comparison at the moment
    # (https://bugs.python.org/issue14208)
    if ( ... , ) < ( ... , ... , ... , ):
        raise Exception("Implementation of __sub__ is not as expected!")
    # Python does not support tuple comparison at the moment
    # (https://bugs.python.org/issue14208)
    if ( ... , ) < ( ... , ... , ... , ):
        raise Exception("Implementation of __sub__ is not as expected!")
    # Python does not support tuple comparison at the moment
    # (https://bugs.python.org/issue14208)
    if ( ... , ) < ( ... , ... , ... , ):
        raise Exception("Implementation of __sub__ is not as expected!")
    # Python does not support tuple comparison at the moment
    # (https

# Generated at 2022-06-14 04:50:29.683856
# Unit test for method positive of class Money
def test_Money_positive():
    from pyleri import Choice, Grammar

    class MoneyGrammar(Grammar):
        money = Choice(Money)

    g = MoneyGrammar()
    m = g.parse(Money.of(ccy=Currency('EUR'), qty=Decimal(36), dov=Date(2017, 12, 31)))
    assert m.value.positive() == Money.of(ccy=Currency('EUR'), qty=Decimal(36), dov=Date(2017, 12, 31)) # noqa: E501
    assert m.value.positive().positive() == Money.of(ccy=Currency('EUR'), qty=Decimal(36), dov=Date(2017, 12, 31)) # noqa: E501

# Generated at 2022-06-14 04:50:30.594376
# Unit test for method __gt__ of class Price
def test_Price___gt__():
    assert True



# Generated at 2022-06-14 04:50:40.485257
# Unit test for method __gt__ of class SomeMoney
def test_SomeMoney___gt__():
    some_money_1 = SomeMoney(JPY, Decimal(1), Date(2019, 11, 28))
    some_money_2 = SomeMoney(JPY, Decimal(10), Date(2020, 11, 28))
    some_money_3 = SomeMoney(JPY, Decimal(100), Date(2020, 11, 28))
    some_money_4 = SomeMoney(JPY, Decimal(100), Date(2020, 11, 29))
    some_money_5 = SomeMoney(EUR, Decimal(100), Date(2020, 11, 30))

    assert not some_money_1.gt(some_money_1)
    assert some_money_2.gt(some_money_1)
    assert some_money_3.gt(some_money_1)

# Generated at 2022-06-14 04:50:48.851025
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():

    m1 = SomeMoney(EUR, 42.99999999, Date.today())
    assert m1.round() == SomeMoney(EUR, 43, Date.today())

    m2 = SomeMoney(EUR, 42.555, Date.today())
    assert m2.round() == SomeMoney(EUR, 43, Date.today())

    m3 = SomeMoney(EUR, 42.99, Date.today())
    assert m3.round() == SomeMoney(EUR, 43, Date.today())

    m4 = SomeMoney(EUR, 42.55, Date.today())
    assert m4.round() == SomeMoney(EUR, 43, Date.today())

    m4 = SomeMoney(EUR, 42.55, Date.today())

# Generated at 2022-06-14 04:51:00.318507
# Unit test for method __lt__ of class Money
def test_Money___lt__():
    from .currencies import USD
    from .dates import TODAY
    from .enums import RoundingMethod

    assert SomeMoney(USD, +10, TODAY) < SomeMoney(USD, +11, TODAY)
    assert SomeMoney(USD, +11, TODAY) > SomeMoney(USD, +10, TODAY)
    assert NoMoney < SomeMoney(USD, +1, TODAY)
    assert SomeMoney(USD, +1, TODAY) > NoMoney

    assert SomeMoney(USD, +10.1, TODAY) < SomeMoney(USD, +10.11, TODAY)
    assert SomeMoney(USD, +10.11, TODAY) > SomeMoney(USD, +10.1, TODAY)

    assert SomeMoney(USD, +10.0, TODAY) < SomeMoney(USD, +10.01, TODAY)

# Generated at 2022-06-14 04:51:07.027773
# Unit test for method with_qty of class Money
def test_Money_with_qty():
    # Test result TypeError: '>' not supported between instances of 'NoMoney' and 'NoMoney'
    assert NoMoney.with_qty(1) is NoMoney
    assert NoMoney.with_qty(Decimal(0.0)) is NoMoney
    assert NoMoney.with_qty(Decimal(1.1)) is NoMoney
Money.NA = NoneMoney



# Generated at 2022-06-14 04:51:12.778357
# Unit test for method __neg__ of class Money
def test_Money___neg__():
    # Lazy initialization
    # Local variables: ccy, qty, dov
    # Local variable ccy has a default value of:
    ccy = GBP
    # Local variable qty has a default value of:
    qty = 1
    # Local variable dov has a default value of:
    dov = Date.of(2020, 3, 14)
    # Block body
    return -SomeMoney(ccy, qty, dov)

# Generated at 2022-06-14 04:51:22.304517
# Unit test for method scalar_subtract of class Money
def test_Money_scalar_subtract():
    assert Money(ccy=Currency("USD"), qty=Decimal("100"), dov=Date(2015, 3, 27)) - 1 == Money(ccy=Currency("USD"), qty=Decimal("99"), dov=Date(2015, 3, 27))
    assert Money(ccy=Currency("USD"), qty=Decimal("100"), dov=Date(2015, 3, 27)) - Decimal("1") == Money(ccy=Currency("USD"), qty=Decimal("99"), dov=Date(2015, 3, 27))
    assert Money(ccy=Currency("USD"), qty=Decimal("100"), dov=Date(2015, 3, 27)) - float(1) == Money(ccy=Currency("USD"), qty=Decimal("99"), dov=Date(2015, 3, 27))


# Generated at 2022-06-14 04:51:27.508593
# Unit test for method __abs__ of class Money
def test_Money___abs__():
    from .currencies import USD

    assert abs(USD(5)) == USD(5)
    assert abs(USD(-5)) == USD(5)

    assert abs(USD(5, 1)) == USD(5, 1)
    assert abs(USD(-5, 1)) == USD(5, 1)

