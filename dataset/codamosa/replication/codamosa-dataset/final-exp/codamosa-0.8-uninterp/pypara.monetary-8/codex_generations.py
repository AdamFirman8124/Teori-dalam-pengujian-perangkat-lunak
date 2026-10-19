

# Generated at 2022-06-14 04:51:01.989349
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    from money import Currency
    from money import Money
    from money import Price
    from money import SomeMoney
    from money import SomePrice
    from money import fxrates

    with fxrates.test_db:
        p = SomePrice(Currency("EUR"), 33, "2018-01-01")
        assert p.convert(Currency("USD"), "2018-01-02") == SomePrice(Currency("USD"), 40.5, "2018-01-02")
        assert p.convert(Currency("GBP"), "2018-01-03") == SomePrice(Currency("GBP"), 30.0, "2018-01-03")
        assert p.convert(Currency("USD"), "2018-01-04") == SomePrice(Currency("USD"), 40.5, "2018-01-04")

# Generated at 2022-06-14 04:51:04.274420
# Unit test for method __bool__ of class Price
def test_Price___bool__():
    assert NoPrice.__bool__() is False
    assert SomePrice(USD, Decimal("1"), Date(2020, 1, 1)).__bool__() is True
    assert SomePrice(USD, Decimal("0"), Date(2020, 1, 1)).__bool__() is False

# Generated at 2022-06-14 04:51:13.110212
# Unit test for method gte of class Price
def test_Price_gte():
    assert Price.of('USD', 10, date(2020, 1, 1)).gte(Price.of('USD', 20, date(2020, 1, 1)))

    assert Price.of('USD', 10, date(2020, 1, 1)).gte(Price.of('USD', 0, date(2020, 1, 1)))

    assert Price.of('USD', 10, date(2020, 1, 1)).gte(Price.of('USD', 10, date(2020, 1, 1)))

    assert Price.of('USD', 10, date(2020, 1, 1)).gte(Price.of('USD', -10, date(2020, 1, 1)))

    assert Price.of('USD', 0, date(2020, 1, 1)).gte(Price.of('USD', -10, date(2020, 1, 1)))



# Generated at 2022-06-14 04:51:20.682441
# Unit test for method with_dov of class Price
def test_Price_with_dov():
    # given
    price = Price.of(EUR, 100, TODAY)

    # when
    another = price.with_dov(TOMORROW)

    # then
    assert price.is_equal(Price.of(EUR, 100, TODAY))
    assert another.is_equal(Price.of(EUR, 100, TOMORROW))
    assert price is not another
    assert price.ccy is not another.ccy
    assert price.qty is not another.qty
    assert price.dov is not another.dov

# Generated at 2022-06-14 04:51:29.283704
# Unit test for method with_dov of class Price
def test_Price_with_dov():
    """
    Unit test for method with_dov of class Price

    """
    a = Price.of(ccy=usd, qty=Decimal("2.34"), dov=Date.from_ymd(2020, 5, 9))
    assert a.with_dov(Date.from_ymd(2020, 5, 10)).dov == Date.from_ymd(2020, 5, 10)
    assert isinstance(a.with_dov(Date.from_ymd(2020, 5, 10)), Price)


# Generated at 2022-06-14 04:51:37.412416
# Unit test for method __floordiv__ of class Price
def test_Price___floordiv__():
    _1 = Money.of(Currency.USD, Decimal('100'), Date.today())
    _2 = Money.of(Currency.USD, Decimal('10'), Date.today())
    _3 = Money.of(Currency.USD, Decimal('10.01'), Date.today())

    _4 = Money.of(Currency.USD, Decimal('10.2'), Date.today())
    _5 = Money.of(Currency.USD, Decimal('10.3'), Date.today())
    _6 = Money.of(Currency.USD, Decimal('10.9'), Date.today())

    assert (_1 // 1) == Money.of(Currency.USD, Decimal('100'), Date.today())
    assert (_1 // 10) == Money.of(Currency.USD, Decimal('10'), Date.today())

# Generated at 2022-06-14 04:51:48.103026
# Unit test for method convert of class SomeMoney
def test_SomeMoney_convert():
    from datetime import date
    from financepy.products.funding.FinFXForward import FinFXForward
    from financepy.finutils.FinGlobalTypes import FinSwapTypes
    from financepy.finutils.FinDate import FinDate
    from financepy.finutils.FinGlobalVariables import gDaysInYear
    from financepy.finutils.FinError import FinError
    from financepy.finutils.FinGlobalVariables import gDaysInYear
    from financepy.finutils.FinDayCount import FinDayCountTypes
    from financepy.finutils.FinMath import ONE_MILLION
    from financepy.market.curves.FinDiscountCurveFlat import FinDiscountCurveFlat
    from financepy.market.curves.FinDiscountCurveZeros import FinDiscountCurveZeros

# Generated at 2022-06-14 04:51:59.902428
# Unit test for method __floordiv__ of class SomePrice
def test_SomePrice___floordiv__():
    """
    Test case for method __floordiv__ of class SomePrice.
    """

    ## Successful:
    p1 = SomePrice(GBP, Decimal(10), Date(2020, 1, 3))
    p2 = Decimal(2)
    p3 = SomePrice(GBP, Decimal(5), Date(2020, 1, 3))
    assert p1 // p2 == p3

    ## Division by zero:
    p1 = SomePrice(GBP, Decimal(10), Date(2020, 1, 3))
    p2 = Decimal(0)
    assert p1 // p2 is NoPrice

    ## For __future__.division (not supported):
    p1 = SomePrice(GBP, Decimal(10), Date(2020, 1, 3))
    p2 = Decimal(2)
    p3

# Generated at 2022-06-14 04:52:11.373699
# Unit test for method divide of class Price
def test_Price_divide():
    from pymoneris.core import Pair
    
    NA = NoPrice
    
    test_cases = [
        ((Pair(AUD,CAD), 1.012345,),
        (1.0,),
        1.012345),
        ((Pair(AUD,CAD), 1.012345,),
        (0.0,),
        NA)
    ]
    errors = []
    for (arg1, arg2), expected_output, expected_no_exception in test_cases:
        try:
            assert (arg1.divide(arg2) == expected_output) == expected_no_exception
        except:
            errors.append('input: ({}, {}) expected output: ({}, {})'.format(arg1, arg2, expected_output, expected_no_exception))

# Generated at 2022-06-14 04:52:21.479426
# Unit test for method __bool__ of class Price
def test_Price___bool__():
    assert bool(NoPrice) == False, "bool(NoPrice) == False"
    assert bool(NoPrice.with_ccy(USD)) == False, "bool(NoPrice.with_ccy(USD)) == False"
    assert bool(Price.of(USD, '0', Date.today())) == False, "bool(NoPrice.of(USD, '0', Date.today())) == False"
    assert bool(Price.of(USD, '0.0', Date.today())) == False, "bool(NoPrice.of(USD, '0.0', Date.today())) == False"
    assert bool(Price.of(USD, Decimal('0'), Date.today())) == False, "bool(NoPrice.of(USD, Decimal('0'), Date.today())) == False"

# Generated at 2022-06-14 04:53:09.029818
# Unit test for method gte of class Money
def test_Money_gte():
    assert NoMoney >= NoMoney
    assert SomeMoney(Currency.USD, 1, Date(2018, 10, 1)) >= SomeMoney(Currency.USD, 1, Date(2018, 10, 1))
    assert SomeMoney(Currency.USD, 1, Date(2018, 10, 1)) >= SomeMoney(Currency.USD, 1, Date(2018, 10, 1))
    assert NoMoney >= SomeMoney(Currency.USD, 1, Date(2018, 10, 1))
    assert SomeMoney(Currency.USD, 1, Date(2018, 10, 1)) >= NoMoney
    assert SomeMoney(Currency.USD, 1, Date(2018, 10, 1)) >= NoMoney

# Generated at 2022-06-14 04:53:15.651335
# Unit test for method __add__ of class Price
def test_Price___add__():
    p1 = Price.of(EUR, Decimal(40), Date.today())
    p2 = Price.of(EUR, Decimal(40), Date.today())
    assert p1 + p2 == Price.of(EUR, Decimal(80), Date.today())
    assert p1 + 40 == Price.of(EUR, Decimal(80), Date.today())
    assert 40 + p1 == Price.of(EUR, Decimal(80), Date.today())
    assert p1 + None == Price.of(EUR, Decimal(40), Date.today())


# Generated at 2022-06-14 04:53:20.972649
# Unit test for method with_dov of class SomeMoney
def test_SomeMoney_with_dov():
    ccy = Currency.default()
    qty = Decimal(1)
    dov = Date.today()
    money = SomeMoney(ccy, qty, dov)
    assert money.ccy is ccy
    assert money.qty == qty
    assert money.dov == dov
    dov += timedelta(days=100)
    another_money = money.with_dov(dov)
    assert another_money.ccy is ccy
    assert another_money.qty == qty
    assert another_money.dov == dov

# Generated at 2022-06-14 04:53:31.729396
# Unit test for method __truediv__ of class SomeMoney
def test_SomeMoney___truediv__():
    from pyfin.exceptions import DivisionByZero, ProgrammingError
    from pyfin.model.money import Money, NoMoney, SomeMoney
    from pyfin.model.types import Currency

    SomeMoney.convert = lambda cls, *args: ValueError("I am broken!")

    ccy = Currency.of("USD")

    assert NoMoney / 1 == NoMoney
    assert 1 / NoMoney == NoMoney

    assert ccy.money(1) / 1 == ccy.money(1)
    assert 1 / ccy.money(1) == ccy.money(1)

    assert ccy.money(None) / 1 == NoMoney
    assert None / ccy.money(None) == NoMoney

    assert ccy.money(1) / None == NoMoney
    assert None / ccy.money(1) == NoMoney


# Generated at 2022-06-14 04:53:42.546335
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():
    from money.common import CNY, TWD
    m = SomeMoney(TWD, Decimal('1000.000'), None)
    assert m.round().as_integer() == 1000
    assert m.round().ccy == TWD
    assert m.round(2).as_float() == 1000.0
    assert m.round(2).ccy == TWD
    assert m.round(3).as_float() == 1000.0
    assert m.round(3).ccy == TWD
    assert m.round(4).as_float() == 1000.0
    assert m.round(4).ccy == TWD
    assert m.round(0) == m
    assert m.round(2) == m.round(3)

# Generated at 2022-06-14 04:53:44.004568
# Unit test for method __abs__ of class Price
def test_Price___abs__():
  pass



# Generated at 2022-06-14 04:53:54.212395
# Unit test for method convert of class SomePrice
def test_SomePrice_convert():
    fxrateservice_default = FXRateService.default
    FXRateService.default = Mock()

    ccy = Currency("USD")

    FXRateService.default.query.return_value = SomeFXRate(ccy, ccy, AsAt(Date(2021, 1, 2)), 1.00)

    assert SomePrice(ccy, 1.00, AsAt(Date(2021, 1, 1))).convert(Currency("USD")) == \
           SomePrice(ccy, 1.00, AsAt(Date(2021, 1, 2)))

    FXRateService.default = fxrateservice_default

## NOTE: Unit test for method convert of class SomePrice
## TODO: IMPLEMENT THIS (see above)

# Generated at 2022-06-14 04:53:55.013017
# Unit test for method __eq__ of class SomeMoney
def test_SomeMoney___eq__():
    pass

# Generated at 2022-06-14 04:54:07.317313
# Unit test for method with_dov of class SomeMoney
def test_SomeMoney_with_dov():
    from datetime import date
    from .currency import AED
    from .date import Date
    from .money import SomeMoney
    assert SomeMoney(None, None, None).with_dov(Date(None, None, None)).dov == Date(None, None, None)
    assert SomeMoney(AED, Decimal('1.234'), date(2019, 1, 1)).with_dov(Date(None, None, None)).dov == Date(None, None, None)
    assert SomeMoney(AED, Decimal('1.234'), date(2019, 1, 1)).with_dov(Date(None, None, None)).ccy == AED

# Generated at 2022-06-14 04:54:15.041960
# Unit test for method with_qty of class Price
def test_Price_with_qty():
    p1 = SomePrice(USD, Decimal(1), Date(2019, 3, 31))
    p2 = p1.with_qty(Decimal(2))

    assert type(p1) == SomePrice
    assert type(p2) == SomePrice

    assert p1 != p2
    assert p2 == SomePrice(USD, Decimal(2), Date(2019, 3, 31))

test_Price_with_qty() 