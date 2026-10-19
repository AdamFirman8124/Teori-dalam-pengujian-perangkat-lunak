

# Generated at 2022-06-14 04:48:41.819080
# Unit test for method __lt__ of class SomePrice
def test_SomePrice___lt__():
    assert NoPrice < NoPrice
    assert SomePrice("USD", Decimal("10.0"), Date.today() - Date(1)) < SomePrice("USD", Decimal("20.0"), Date.today() - Date(2))
    assert not SomePrice("USD", Decimal("20.0"), Date.today() - Date(2)) < SomePrice("USD", Decimal("10.0"), Date.today() - Date(1))
    assert not SomePrice("USD", Decimal("10.0"), Date.today() - Date(1)) < SomePrice("USD", Decimal("10.0"), Date.today() - Date(1))
    

# Generated at 2022-06-14 04:48:46.628912
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():
    money = SomeMoney(Currency.of('USD'), Decimal('100'), Date.of(2020, 3, 3))
    assert money.round() == SomeMoney(Currency.of('USD'), Decimal('100'), Date.of(2020, 3, 3))
    assert money.round(2) == SomeMoney(Currency.of('USD'), Decimal('100.00'), Date.of(2020, 3, 3))


# Generated at 2022-06-14 04:48:54.575474
# Unit test for method __floordiv__ of class Price
def test_Price___floordiv__():
    # Imports
    import pybtex.database as pybtex

    # Setup
    from io import StringIO
    from pypipegraph.readers import BibTexReader
    from pypipegraph.unit_test_helpers import make_simple_pipegraph
    from itertools import groupby
    from typing import Dict, Iterator, List, Tuple

    # Execution
    source, target = StringIO(), StringIO()
    source.write('@article{Armstrong2012,\n')
    source.write('  author = {Armstrong, L and Friend, P},\n')
    source.write('  title = {Dynamic transcriptional response of Pseudomonas fluorescens SBW25 to aerobic and anaerobic growth},\n')
    source.write('  journal = {BMC Genomics},\n')

# Generated at 2022-06-14 04:48:57.658039
# Unit test for method round of class Price
def test_Price_round():
    from birgitta.schema.bq_types.types_price import Price
    price = Price(ccy='USD', qty=0.56, dov='2020-04-26')
    rounded = price.round()
    assert rounded == 1


# Generated at 2022-06-14 04:49:10.231219
# Unit test for method floor_divide of class Price
def test_Price_floor_divide():
    from dateutil.parser import parse
    from pymoneyed import Money
    from pandas.util.testing import assert_frame_equal
    import pandas as pd
    import numpy as np

    # Case: price is defined
    qty = 0.15
    ccy = 'USD'
    dov = parse('2019-12-31')
    price = Price.of(ccy, qty, dov)
    validate_price(price)

    # Case: operand is numeric
    operand = 2
    res = price.floor_divide(operand)
    validate_price(res, qty=0, ccy=ccy, dov=dov)

    # Case: operand is money
    res = price.floor_divide(Money(operand, ccy))

# Generated at 2022-06-14 04:49:12.193239
# Unit test for method positive of class Price
def test_Price_positive():
    with pytest.raises(AttributeError):
        Price().positive()

# Generated at 2022-06-14 04:49:15.059661
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    assert Money.of(USD, 1, Date.today()).with_dov(Date.today() + 1) == Money.of(USD, 1, Date.today() + 1)


# Generated at 2022-06-14 04:49:24.956512
# Unit test for method __gt__ of class Price
def test_Price___gt__():
    import datetime
    from pymonad.Maybe import Just, Nothing
    from pymonad.Reader import curry
    from arepl_dump import dump
    from pymonad.Either import Left, Right
    def gt(x,y):
        return x > y
    x = gt(Price.of(Currency.of('USD'), Decimal(10), Date(2012, 4, 8)), Price.of(Currency.of('USD'), Decimal(10), Date(2012, 4, 8)))
    print(repr(x))
    assert x == False
    dump.dumpEval(x)

# Generated at 2022-06-14 04:49:34.552906
# Unit test for method __neg__ of class Money
def test_Money___neg__():
    """
    Unit test for method __neg__ of class Money
    """

    class MoneyStub(Money):

        __slots__ = ()

        def is_equal(self, other: Any) -> bool:
            raise NotImplementedError

        def as_boolean(self) -> bool:
            raise NotImplementedError

        def as_float(self) -> float:
            raise NotImplementedError

        def as_integer(self) -> int:
            raise NotImplementedError

        def abs(self) -> "Money":
            raise NotImplementedError

        def negative(self) -> "Money":
            raise NotImplementedError

        def positive(self) -> "Money":
            raise NotImplementedError

        def round(self, ndigits: int = 0) -> "Money":
            raise Not

# Generated at 2022-06-14 04:49:38.879975
# Unit test for method __float__ of class Money
def test_Money___float__():
    assert float(SomeMoney(EUR, 1, TODAY)) == 1.0

    try:
        float(NoMoney)
        raise AssertionError("NoMoney can not be converted to float.")
    except MonetaryOperationException:
        pass

# Generated at 2022-06-14 04:51:38.799875
# Unit test for method convert of class Money
def test_Money_convert():
    assert Money.of(Currency.USD, 100, Date.today()).convert(Currency.TRY) == Money.of(Currency.TRY, 100, Date.today())

# Generated at 2022-06-14 04:51:41.847797
# Unit test for method round of class SomeMoney
def test_SomeMoney_round():
    expected = Money.of(EUR, 5, TODAY)
    assert SomeMoney(EUR,1, TODAY).round(2) == expected



# Generated at 2022-06-14 04:51:49.109085
# Unit test for method is_equal of class Money
def test_Money_is_equal():
    from decimal import Decimal
    from datetime import date
    from .currencies import USD

    a = USD(Decimal("100"), date(2016, 1, 1))
    b = USD(Decimal("100"), date(2016, 1, 1))
    c = USD(Decimal("0"), date(2016, 1, 1))

    assert a.is_equal(b)
    assert not a.is_equal(c)
    assert not Money.NA.is_equal(a)
    assert not a.is_equal(Money.NA)
    assert Money.NA.is_equal(Money.NA)



# Generated at 2022-06-14 04:51:49.905156
# Unit test for method __floordiv__ of class Money
def test_Money___floordiv__():
    pass

# Generated at 2022-06-14 04:52:01.116674
# Unit test for method as_integer of class Money
def test_Money_as_integer():

    from decimal import Decimal

    from .currencies import Currency

    ## NoMoney object should raise MoneyOperationException
    def test_Money_as_integer_nomoney():
        from ..money import Money
        try:
            assert Money.NA.as_integer() == 0
        except MonetaryOperationException as e:
            assert str(e) == "undefined monetary value is encountered"

    test_Money_as_integer_nomoney()

    ## SomeMoney object with negative quantity should raise MoneyOperationException
    def test_Money_as_integer_negative_number():
        from ..money import Money
        money = Money.of(Currency.of('USD'), Decimal('-1.23'), Date.today())

# Generated at 2022-06-14 04:52:04.980138
# Unit test for method __sub__ of class SomePrice
def test_SomePrice___sub__():
    """Unit test for method __sub__ of class SomePrice
    """
    ## TODO: Implement unit test for __sub__.

    pass



# Generated at 2022-06-14 04:52:15.067328
# Unit test for method __floordiv__ of class SomeMoney
def test_SomeMoney___floordiv__():
    with pytest.raises(ValueError, match="^money is missing currency$"):
        SomeMoney(None, 1, Date.today()).__floordiv__(1)
    with pytest.raises(ValueError, match="^money is missing value date$"):
        SomeMoney(EUR, 1, None).__floordiv__(1)
    with pytest.raises(ValueError, match="^money is missing quantity$"):
        SomeMoney(EUR, None, Date.today()).__floordiv__(1)
    assert SomeMoney(EUR, 1, Date.today()).__floordiv__(1) == SomeMoney(EUR, 1, Date.today())
    assert SomeMoney(EUR, 1.1, Date.today()).__floordiv__(2) == SomeMoney.of

# Generated at 2022-06-14 04:52:25.895485
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    assert Money.of(Currency.USD, 5, Date.today()).floor_divide(3) == Money.of(Currency.USD, 1, Date.today())
    assert Money.of(Currency.USD, 5, Date.today()).floor_divide(2) == Money.of(Currency.USD, 2, Date.today())
    assert Money.of(Currency.USD, 4.5, Date.today()).floor_divide(2) == Money.of(Currency.USD, 2, Date.today())
    assert Money.of(Currency.USD, 1.7, Date.today()).floor_divide(2) == Money.of(Currency.USD, 0, Date.today())

# Generated at 2022-06-14 04:52:27.192694
# Unit test for method __gt__ of class Money
def test_Money___gt__():
    expected = False
    actual = Money.of(None, None, None).__gt__(Money.of(None, None, None))
    assert expected == actual

# Generated at 2022-06-14 04:52:33.435690
# Unit test for method round of class Money
def test_Money_round():
    # Given
    money = Money.of('eur', 0.01, Date(2020, 1, 1))
    # When
    rounded = round(money)
    # Then
    assert rounded == money.round()
    assert rounded.ccy.code == money.ccy.code
    assert rounded.qty == 1
    assert rounded.dov == Date(2020,1,1)



# Generated at 2022-06-14 04:52:52.726411
# Unit test for method as_integer of class Money
def test_Money_as_integer():
    assert SomeMoney("USD", 1, Date.today()).as_integer() == 1


# Generated at 2022-06-14 04:53:04.848773
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    '''
    Unittest for method with_dov of class Money
    '''
    from datetime import date
    from ..currency import Currency
    from ..money import Money

    USD = Currency.of('USD')
    EUR = Currency.of('EUR')

    m0 = Money.of(USD, 5, date(2018, 1, 5))
    m1 = Money.of(USD, 5, date(2018, 1, 6))
    m2 = m0.with_dov(date(2018, 1, 10))
    m3 = m0.with_dov(None)

    assert m2 == Money.of(USD, 5, date(2018, 1, 10))
    assert m3 == Money.of(USD, 5, date(2018, 1, 5))

    #Test for inconsistent currency

# Generated at 2022-06-14 04:53:14.672845
# Unit test for method with_dov of class SomePrice
def test_SomePrice_with_dov():
    from arez.serialize import from_object
    from arez.serialize import to_object
    from arez.serialize import to_json
    from datetime import date
    from decimal import Decimal
    from pony.orm import db_session
    from stresstest import StressTest
    from typing import Optional
    from typing import Union
    from typing import cast
    assert isinstance(StressTest.PRICE, SomePrice)
    s: SomePrice = cast(SomePrice, StressTest.PRICE)
    assert isinstance(StressTest.PRICE, Optional[Price])
    assert isinstance(s, Optional[Price])
    assert isinstance(s.with_dov(date(2019, 2, 21)), Optional[Price])

# Generated at 2022-06-14 04:53:20.498553
# Unit test for method abs of class Money
def test_Money_abs():
  # Retrieve the method to be tested.
  method = Money.abs

  # Test case 1:
  actual = method(NoMoney)
  assert actual is NoMoney, "Test case 1: Failed: Returned {0} for None instead of None.".format(actual)

  # Test case 2:
  actual = method(NoneMoney)
  assert actual is NoneMoney, "Test case 2: Failed: Returned {0} for None instead of None.".format(actual)

  # Test case 3:
  expected = SomeMoney(Currency.USD, Decimal(1.0), Date.today())
  actual = method(expected)
  assert actual is expected, "Test case 3: Failed: Returned {0} for {1} instead of {1}.".format(actual, expected)

  # Test case 4:

# Generated at 2022-06-14 04:53:30.892953
# Unit test for method floor_divide of class Money
def test_Money_floor_divide():
    from .currencies import USD, JPY
    from .datetime import Date, DateTime
    from .exchange import FXRateLookupError, FXRateService, FixedFXRateService
    from decimal import Decimal
    m1 = Money(USD, Decimal(10))
    m2 = Money(USD, Decimal(2))
    assert m1.floor_divide(m2) == Money(USD, Decimal(5))
    m1 = Money(USD, Decimal(10))
    m2 = Money(USD, Decimal(3))
    assert m1.floor_divide(m2) == Money(USD, Decimal(3))
    m1 = Money(USD, Decimal(10))
    m2 = Money(USD, Decimal(0))
    assert m1.floor_divide(m2) == NoMoney


# Generated at 2022-06-14 04:53:36.587281
# Unit test for method __floordiv__ of class Money
def test_Money___floordiv__():
    """
    Tests regular division of monetary values.
    """
    i = Money.of(EUR, 100, TODAY)
    j = Money.of(USD, 102, TODAY)

    assert (i / 10) == Money.of(EUR, 10, TODAY)
    assert (i / j) == Money.of(EUR, Decimal(100) / Decimal(102), TODAY)

# Generated at 2022-06-14 04:53:41.473843
# Unit test for method __truediv__ of class Money
def test_Money___truediv__():
    from decimal import Decimal
    from .currencies import Currency
    from .money import Money
    from .zeitgeist import Date
    test_subject_1: Money = Money.of(Currency("EUR"), Decimal("1.23456"), Date("2020-02-11"))
    assert test_subject_1 / 1 == test_subject_1
    assert test_subject_1 / None is test_subject_1
    assert test_subject_1 / True == test_subject_1



# Generated at 2022-06-14 04:53:42.015529
# Unit test for method __ge__ of class SomePrice
def test_SomePrice___ge__():
    pass

# Generated at 2022-06-14 04:53:53.864390
# Unit test for method with_dov of class Money
def test_Money_with_dov():
    import datetime
    # In:       Money.of(ccy, qty, dov)
    #                 ccy  qty   dov
    money = Money.of(Currency.AUD, 10, Date.of("2012-12-05"))
    # Out:     SomeMoney(ccy=AUD, qty=10, dov=datetime.date(2012, 12, 5))
    assert money.with_dov(Date.of("2012-12-06")) == SomeMoney(ccy=Currency.AUD, qty=10, dov=datetime.date(2012, 12, 6))
    # In:       NoMoney.with_dov(Date.of("2012-12-06"))
    # Out:     NoMoney
    assert NoMoney.with_dov(Date.of("2012-12-06")) == No

# Generated at 2022-06-14 04:54:06.352914
# Unit test for method convert of class SomeMoney

# Generated at 2022-06-14 04:54:57.032200
# Unit test for method multiply of class Money
def test_Money_multiply():
    """
    Tests the method :meth:`multiply` of :class:`Money`.
    """
    assert SomeMoney(ccy=USD, qty=30.50, dov=Date.today()) * 10 == SomeMoney(
        ccy=USD, qty=305, dov=Date.today()
    )
    assert SomeMoney(ccy=USD, qty=30.50, dov=Date.today()) * (-10) == SomeMoney(
        ccy=USD, qty=-305, dov=Date.today()
    )
    assert SomeMoney(ccy=USD, qty=30.50, dov=Date.today()) * 0 == SomeMoney(
        ccy=USD, qty=0, dov=Date.today()
    )
