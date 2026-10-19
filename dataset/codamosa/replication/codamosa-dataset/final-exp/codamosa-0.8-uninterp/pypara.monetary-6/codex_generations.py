

# Generated at 2022-06-14 04:46:59.731064
# Unit test for method __eq__ of class Price
def test_Price___eq__():
    from .currency import Currency
    from .currency import EUR
    from .currency import USD
    from .date import Date
    from .money import Money
    from .money import NoMoney
    from .price import Maybe
    from .price import NoPrice
    from .price import Price
    from .price import SomePrice
    from .util import Decimal


# Generated at 2022-06-14 04:47:05.536093
# Unit test for method scalar_add of class Price
def test_Price_scalar_add():
    assert Price.of(USD, Decimal(1), Date(2020, 6, 14)).scalar_add(1) == Price.of(USD, Decimal(2), Date(2020, 6, 14))
    assert Price.of(None, Decimal(1), Date(2020, 6, 14)).scalar_add(1) == Price.of(None, Decimal(1), Date(2020, 6, 14))

# Generated at 2022-06-14 04:47:16.008045
# Unit test for method __floordiv__ of class SomeMoney
def test_SomeMoney___floordiv__():
    c = Currency
    d = Date
    assert SomeMoney(c('EUR'), Decimal('1.3'), d(2013, 10, 14)).__floordiv__(Decimal('0.1')) == SomeMoney(c('EUR'), Decimal('13'), d(2013, 10, 14))
    assert SomeMoney(c('EUR'), Decimal('1.3'), d(2013, 10, 14)).__floordiv__(Decimal('0.9')) == SomeMoney(c('EUR'), Decimal('1'), d(2013, 10, 14))
    assert SomeMoney(c('EUR'), Decimal('1.3'), d(2013, 10, 14)).__floordiv__(Decimal('1.3')) == SomeMoney(c('EUR'), Decimal('1'), d(2013, 10, 14))
    assert Some

# Generated at 2022-06-14 04:47:17.190634
# Unit test for method __int__ of class Money
def test_Money___int__():
    assert int(Money.of("USD", 2.0, "2019-01-01")) == 2

# Generated at 2022-06-14 04:47:21.524619
# Unit test for method round of class Money
def test_Money_round():
    assert SomeMoney('USD', Decimal('1.55'), Date.today()).round() == Money.of('USD', Decimal('2'), Date.today())
    assert SomeMoney('USD', Decimal('1.54'), Date.today()).round() == Money.of('USD', Decimal('2'), Date.today())
    assert SomeMoney('USD', Decimal('1.54'), Date.today()).round() == Money.of('USD', Decimal('2'), Date.today())
    assert SomeMoney('USD', Decimal('1.45'), Date.today()).round() == Money.of('USD', Decimal('1'), Date.today())
    assert SomeMoney('USD', Decimal('1.54'), Date.today()).round(1) == Money.of('USD', Decimal('1.5'), Date.today())

# Generated at 2022-06-14 04:47:26.830891
# Unit test for method __lt__ of class SomePrice
def test_SomePrice___lt__():
    assert SomePrice(ccy="GBP", qty=Decimal("100"), dov=Date("2020-01-01")) < SomePrice(ccy="GBP", qty=Decimal("200"), dov=Date("2020-01-01"))



# Generated at 2022-06-14 04:47:39.033429
# Unit test for method positive of class Price
def test_Price_positive():
    assert Price.NA.positive() == Price.NA
    assert Price(0.0, USD, Date.today()).positive() == Price(0.0, USD, Date.today())
    assert Price(1.0, USD, Date.today()).positive() == Price(1.0, USD, Date.today())
    assert Price(-1.0, USD, Date.today()).positive() == Price(1.0, USD, Date.today())
    assert Price(100.0, USD, Date.today()).positive() == Price(100.0, USD, Date.today())
    assert Price(-100.0, USD, Date.today()).positive() == Price(100.0, USD, Date.today())
    assert Price(1.5, USD, Date.today()).positive() == Price(1.5, USD, Date.today())


# Generated at 2022-06-14 04:47:51.822888
# Unit test for method with_dov of class SomePrice
def test_SomePrice_with_dov():
    from datetime import date
    from moneyed import GBP
    from numpy import nan
    from pandas import DataFrame, date_range
    from decimal import Decimal
    from datacode.models.pipeline import Pipeline
    from datacode.models.variables import Variable
    from datacode.models.dtypes.price import PriceType
    from datacode.models.dtypes.numeric import NumericType

    df = DataFrame({
        'price': [10, nan, 30.00, 40],
        'date': [date(2020, 1, 1), date(2020, 1, 1), date(2020, 1, 1), date(2020, 1, 1)]
    })

    var_price = Variable('price', PriceType(GBP), 'Price')

# Generated at 2022-06-14 04:47:53.814645
# Unit test for method gt of class Price
def test_Price_gt():
    assert (SomePrice.of(Currency('USD'), 100, as_date('2012-01-01')) > NoneMoney()) == False
    assert (NonePrice() > NoneMoney()) == False
    assert (NonePrice() > SomePrice.of(Currency('USD'), 100, as_date('2012-01-01'))) == False

# Generated at 2022-06-14 04:48:01.361254
# Unit test for method __add__ of class Money
def test_Money___add__():
    from .currencies import USD
    from datetime import date
    from .commons.numbers import Decimal

    assert NoneMoney + NoneMoney == NoneMoney
    assert NoneMoney + SomeMoney(USD, Decimal("1.00"), date.today()) == NoMoney
    assert NoneMoney + SomeMoney(USD, Decimal("1.00"), date.today()) == NoMoney

    m1 = SomeMoney(USD, Decimal("1.00"), date.today())
    m2 = SomeMoney(USD, Decimal("2.00"), date.today())
    assert m1 + m2 == SomeMoney(USD, Decimal("3.00"), date.today())
    assert m1 + NoneMoney == m1
    assert m1 + NoMoney == m1


# Generated at 2022-06-14 04:52:08.969638
# Unit test for method abs of class Money
def test_Money_abs():
    some_money = Money.of(Currency.USD, Decimal(100), Date(2001, 12, 31))
    assert some_money.abs().qty == 100
    assert some_money.negative().abs().ccy == some_money.ccy
    assert some_money.negative().abs().dov == some_money.dov
    assert some_money.negative().abs().qty == 100

# Generated at 2022-06-14 04:52:13.384203
# Unit test for method divide of class Money
def test_Money_divide():
    m = Money.of(Currency.USD, 1, Date.today())
    assert (m.divide(2) == m.with_qty(0.5))
    assert (m.divide(-2) == m.with_qty(-0.5))



# Generated at 2022-06-14 04:52:16.258833
# Unit test for method __abs__ of class Money
def test_Money___abs__():
    # Arrange
    someMoney = SomeMoney(Currency.of("USD"), Decimal("12.34"), Date.today())

    # Act
    actual = abs(someMoney)

    # Assert
    assert actual.qty == Decimal("12.34")



# Generated at 2022-06-14 04:52:27.560630
# Unit test for method lte of class Price
def test_Price_lte():
    assert SomePrice(USD, Decimal(2), date(2020, 1, 1)).lte(SomePrice(USD, Decimal(3), date(2020, 1, 1)))
    assert SomePrice(USD, Decimal(1), date(2020, 1, 1)).lte(SomePrice(USD, Decimal(1), date(2020, 1, 1)))
    assert SomePrice(USD, Decimal(4), date(2020, 1, 1)).lte(SomePrice(USD, Decimal(2), date(2020, 1, 1)))
    assert SomePrice(USD, Decimal(1), date(2020, 1, 1)).lte(SomePrice(USD, Decimal(3), date(2020, 1, 1)))

# Generated at 2022-06-14 04:52:40.422324
# Unit test for method __mul__ of class Money
def test_Money___mul__():
    ccy_usd = Currency.of("USD")
    ccy_eur = Currency.of("EUR")
    ccy_trn = Currency.of("TRY")
    date_today = Date.today()
    date_tomorrow = date_today.tomorrow()
    date_yesterday = date_today.yesterday()

    usd10_today = Money.of(ccy_usd, 10, date_today)
    eur20_today = Money.of(ccy_eur, 20, date_today)
    try10_today = Money.of(ccy_trn, 10, date_today)

    usd10_tomorrow = Money.of(ccy_usd, 10, date_tomorrow)

# Generated at 2022-06-14 04:52:48.024669
# Unit test for method __add__ of class SomePrice
def test_SomePrice___add__():
    assert SomePrice(Currency.USD, 1, today) + SomePrice(Currency.USD, 2, today) == SomePrice(Currency.USD, 3, today)
    assert SomePrice(Currency.USD, 1, today).__add__(SomePrice(Currency.USD, 2, today)) == SomePrice(Currency.USD, 3, today)
    assert SomePrice(Currency.USD, 1, today).__add__(SomePrice(Currency.USD, 2, yesterday)) == SomePrice(Currency.USD, 3, today)
    assert SomePrice(Currency.USD, 1, yesterday).__add__(SomePrice(Currency.USD, 2, today)) == SomePrice(Currency.USD, 3, today)

# Generated at 2022-06-14 04:53:00.421069
# Unit test for method multiply of class Money
def test_Money_multiply():
    """
    Test Money.multiply function
    :return: None
    """
    from .currencies import USD, EUR, CHF

    from .exchange import FXRateService
    from .exchange.mock import MockFXRateService
    from .exchange.historical import HistoricalFXRateService

    m1 = Money.of(USD, 100, Date.today())
    m2 = Money.of(USD, 10, Date.today())
    m3 = Money.of(EUR, 100, Date.today())
    m4 = m1.multiply(10)
    m5 = m1.multiply(Decimal(10))
    m6 = m1 / 10
    m7 = m1 + m2
    m8 = m3.convert(USD, Date.today(), True)
    m9 = m3

# Generated at 2022-06-14 04:53:07.970599
# Unit test for method __floordiv__ of class Price
def test_Price___floordiv__():
    assert Price.of(Currency.of('USD'), 100, Date.today()) // 1 == Price.of(Currency.of('USD'), 100, Date.today())
    assert Price.of(Currency.of('USD'), 100, Date.today()) // 2 == Price.of(Currency.of('USD'), 50, Date.today())
    assert NoPrice // 1 == NoPrice
    assert NoPrice // 2 == NoPrice


# Generated at 2022-06-14 04:53:16.445666
# Unit test for method __eq__ of class Money
def test_Money___eq__():
    from decimal import Decimal

    from .currencies import Currency, USD

    from .money import Money, SomeMoney

    assert Money.NA.is_equal(Money.NA) is True
    assert Money.of(USD, Decimal("100"), Date.today()).is_equal(Money.of(USD, Decimal("100"), Date.today())) is True

    assert Money.NA.is_equal(None) is False
    assert Money.NA.is_equal(USD) is False
    assert Money.NA.is_equal(Money.of(USD, Decimal("100"), Date.today())) is False
    assert Money.NA.is_equal(SomeMoney(USD, Decimal("100"), Date.today())) is False

    assert Money.of(USD, Decimal("100"), Date.today()).is_equal(None) is False


# Generated at 2022-06-14 04:53:29.863455
# Unit test for method floor_divide of class Price
def test_Price_floor_divide():
  # Quantize - 1 decimal
  # 3.2 => 3.2; 3.5 => 3.5; 3.7 => 3.7; 3.17 => 3.1; 3.15 => 3.1; 3.12 => 3.1
  # Remainder value will be 0 if not the last digit
  A = Price.of('USD', Decimal('3.17'), Date.today())
  B = A.floor_divide(Decimal('2'))
  assert B.qty == Decimal('1.58')
  B = A.floor_divide(Decimal('3'))
  assert B.qty == Decimal('1.05')
  B = A.floor_divide(Decimal('1.58'))
  assert B.qty == Decimal('2')