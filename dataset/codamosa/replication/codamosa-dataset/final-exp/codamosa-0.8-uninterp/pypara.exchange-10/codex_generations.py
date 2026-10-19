

# Generated at 2022-06-14 04:34:30.852947
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    from .currencies import Currencies

    from .commons.zeitgeist import Date

    from decimal import Decimal

    class MockFXRateService(FXRateService):

        def __init__(self, queries, rates):

            self._queries = queries
            self._rates = rates

        def query(self, ccy1, ccy2, asof, strict=False):

            query = (ccy1, ccy2, asof)

            if query not in self._queries:
                return None

            query_idx = self._queries.index(query)

            return self._rates[query_idx]

        def queries(self, queries, strict=False):

            return (self.query(ccy1, ccy2, asof) for ccy1, ccy2, asof in queries)


# Generated at 2022-06-14 04:34:43.182656
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import TestCase, main
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.temporals import Date

    class MockFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"]:
                return FXRate(Currencies["USD"], Currencies["EUR"], Date.of(2018, 9, 1), Decimal("0.88"))
            else:
                return None


# Generated at 2022-06-14 04:34:56.537380
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .currencies.extras import Currencies
    from .currencies.temporal import Temporal
    from .temporal import TemporalType, Date

    class MockRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal(1.2))

    service = MockRateService()
    rate1 = service.query(Currencies["EUR"], Currencies["USD"], Date(2000, 1, 1))
    rate2 = service.query(Currencies["EUR"], Currencies["USD"], Date(2000, 1, 2))
    rate3 = service.query(Currencies["EUR"], Currencies["USD"], Date(2000, 1, 3))
    rates = service.qu

# Generated at 2022-06-14 04:34:57.044771
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass

# Generated at 2022-06-14 04:35:07.778776
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    class Service(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return None

        def queries(self, queries, strict=False):
            return None

    # Test FXRateService.query()
    from decimal import Decimal
    from datetime import date
    service = Service()
    try:
        service.query(None, None, date.today())
        assert False
    except TypeError:
        assert True

    try:
        service.query(None, None, date.today(), strict=True)
        assert False
    except FXRateLookupError:
        assert True

    class Service(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return None


# Generated at 2022-06-14 04:35:18.678845
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """
    from decimal import Decimal
    from unittest import mock, TestCase
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    LOCAL_CCY1 = Currencies["USD"]
    LOCAL_CCY2 = Currencies["EUR"]
    OTHER_CCY1 = Currencies["EUR"]
    OTHER_CCY2 = Currencies["USD"]
    LOCAL_DATE = Date(2020, 1, 1)
    OTHER_DATE = Date(2019, 1, 1)
    LOCAL_RATE = Decimal("0.8")
    OTHER_RATE = Decimal("0.6")


# Generated at 2022-06-14 04:35:26.060595
# Unit test for constructor of class FXRateLookupError
def test_FXRateLookupError():
    from .currencies import Currencies
    from datetime import date

    error = FXRateLookupError(Currencies["USD"], Currencies["EUR"], date.today())
    assert error.ccy1 == Currencies["USD"]
    assert error.ccy2 == Currencies["EUR"]
    assert error.asof == date.today()
    assert str(error) == "Foreign exchange rate for USD/EUR not found as of %s" % date.today()



# Generated at 2022-06-14 04:35:35.348783
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """ Tests converting a currency to another one.
    """

    from decimal import Decimal
    from datetime import date
    from pypara.currencies import EUR, USD
    from pypara.fx.rates import FXRate, FXRateService

    class TestFXRateService(FXRateService):
        """ Provides a test FXRateService.
        """

        def __init__(self):
            self._rates = {FXRate(EUR, USD, date(2010, 5, 1), Decimal(1.3)): True,
                           FXRate(EUR, USD, date(2010, 8, 5), Decimal(1.4)): True,
                           FXRate(EUR, USD, date(2010, 8, 6), Decimal(1.5)): True}


# Generated at 2022-06-14 04:35:48.701604
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from pypara.commons.numbers import ONE, ZERO
    from pypara.currencies import Currencies
    from pypara.fx.fxrateservices import DummyFXRateService

    ## Test method query of class DummyFXRateService
    ## for an invalid currency pair:

    service = DummyFXRateService()
    try:
        service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today())
        assert False, "Expected a `ValueError`"
    except ValueError as e:
        assert str(e) == "Currency pair `EUR/USD` can not be found.", \
            "Expected a `ValueError` with message: `Currency pair `EUR/USD` can not be found.`"

    ## Test method query of class DummyFX

# Generated at 2022-06-14 04:35:59.706167
# Unit test for constructor of class FXRateLookupError
def test_FXRateLookupError():
    from unittest import TestCase, main

    from .currencies import Currencies

    class _T(TestCase):

        def test_init(self):
            with self.assertRaises(ValueError):
                FXRateLookupError(None, Currencies["USD"], Date.today())
            with self.assertRaises(ValueError):
                FXRateLookupError(Currencies["EUR"], None, Date.today())
            with self.assertRaises(ValueError):
                FXRateLookupError(Currencies["EUR"], Currencies["USD"], None)

    main(verbosity=2)

# Unit tests for methods of class FXRate

# Generated at 2022-06-14 04:36:15.099690
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the functionality of method queries of the :class:`FXRateService`.
    """
    from unittest.mock import Mock

    ## Mock the service:
    service = Mock()

    ## Create mock query results:
    rate1 = FXRate(Currency("EUR"), Currency("USD"), Date(2018, 1, 1), Decimal("2"))
    rate2 = FXRate(Currency("USD"), Currency("EUR"), Date(2018, 1, 1), Decimal("0.5"))
    rate3 = FXRate(Currency("EUR"), Currency("USD"), Date(2018, 1, 2), Decimal("2.1"))
    rate4 = FXRate(Currency("USD"), Currency("EUR"), Date(2018, 1, 2), Decimal("0.48"))

    ## Set mocks:
    service.query.side

# Generated at 2022-06-14 04:36:24.997834
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.temporal import Dt
    import datetime
    ccy1, ccy2 = Currencies["EUR"], Currencies["USD"]
    asof = Dt(datetime.date.today())
    rate = Decimal("2")
    queries = [(ccy1, ccy2, asof)]
    rates = [FXRate(ccy1, ccy2, asof, rate)]
    class MockQuery():
        def __init__(self, rate):
            self.rate = rate
    class MockFxRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return MockQuery(rate)

# Generated at 2022-06-14 04:36:26.695018
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103
    pass                          # noqa: D104


# Generated at 2022-06-14 04:36:36.625926
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():	
    ccy1 = "EUR"	
    ccy2 = "USD"	
    asof = "20190101"	
    rate = FXRate(ccy1,ccy2,asof,Decimal("2"))	
    rate2 = FXRate(ccy1,ccy2,asof,Decimal("2"))	
    strict = False	
    x = FXRate.queries([(ccy1,ccy2,asof),(ccy1,ccy2,asof)], strict)	
    assert x == [rate,rate2]

# Generated at 2022-06-14 04:36:47.345127
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Date
    from .fxrates import FXRateService, FXRateLookupError

    ## Define a non-strict mock fx rate service:
    class MockFXRateService(FXRateService):
        def __init__(self, rates: Iterable[FXRate]):
            self.rates = dict([(query, rate) for rate in rates for query in rate.queries])

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            query = (ccy1, ccy2, asof)
            return self.rates.get(query, None) if not strict else self.rates[query]


# Generated at 2022-06-14 04:36:59.047371
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    import unittest
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance.fxtransactions import FXRateService

    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
                return FXRate(Currencies["EUR"], Currencies["USD"], asof, Decimal("2"))
            elif ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"]:
                return FXRate(Currencies["USD"], Currencies["EUR"], asof, Decimal("0.5"))

# Generated at 2022-06-14 04:37:12.400746
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .finance.exchange import ExchangeRates

    for date in [Date(2020, 1, 1), Date(2019, 12, 25)]:
        for ccy1, ccy2 in [
            (Currencies["EUR"], Currencies["USD"]),
            (Currencies["USD"], Currencies["EUR"]),
        ]:
            rate = ExchangeRates.query(ccy1, ccy2, date)
            assert rate is not None
            assert rate.ccy1 == ccy1
            assert rate.ccy2 == ccy2
            assert rate.date == date
            assert rate.value > ZERO
            assert ~rate == ExchangeRates.query(ccy2, ccy1, date)



# Generated at 2022-06-14 04:37:12.979320
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    ...

# Generated at 2022-06-14 04:37:25.774736
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate, FXRateService

    class MockFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if (ccy1, ccy2, asof) == (Currencies["EUR"], Currencies["USD"], datetime.date.today()):
                return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
            else:
                return None


# Generated at 2022-06-14 04:37:37.857937
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests that the method queries of the class FXRateService works as expected.
    """
    from enum import Enum
    from collections import namedtuple
    from typing import Optional, Tuple
    from .commons.zeitgeist import Date
    from .currencies import Currency

    class State(Enum):
        """
        Defines simple states for unit testing.
        """
        empty = None
        lookup_error = False
        rate = True

    # Define FX rate query tuple.
    Query = namedtuple("Query", ["ccy1", "ccy2", "asof"])

    # Create FX rate service.

# Generated at 2022-06-14 04:37:53.098729
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # Imports
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies, Currency
    from pypara.finance.fx import FXRate

    # Define a foreign exchange rate service
    class TestFXRateService(FXRateService):
        def __init__(self, rates: Iterable[FXRate]):
            self._rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False):
            for rate in self._rates:
                if rate.ccy1 == ccy1 and rate.ccy2 == ccy2 and rate.date == asof:
                    return rate
            return None


# Generated at 2022-06-14 04:38:02.730608
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .zeitgeist import Time
    from .commons.numbers import Decimal

    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return None

    assert TestFXRateService.default is None

    FXRateService.default = TestFXRateService()
    assert FXRateService.default is not None

    assert FXRateService.default.query(Currencies["EUR"], Currencies["USD"], Time.today(), strict=False) is None


# Generated at 2022-06-14 04:38:11.592967
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from .currencies import Currencies
    from .fxrates import FXRateService
    from .temporal import Time

    class _FXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=True):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == time:
                return FXRate(ccy1, ccy2, asof.date, Decimal(2))
            elif strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            return None

        def queries(self, queries, strict=True):
            raise NotImplementedError

    time = Time(2017, 12, 31)
    service = _FXRateService()
    rate = service.query

# Generated at 2022-06-14 04:38:23.566553
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from collections import namedtuple
    from itertools import chain
    from pypara.currencies import Currencies
    from pypara.dated import Temporal

    ## Define the queries:
    Q = namedtuple("Q", ["ccy1", "ccy2", "date"])
    ques = [
        Q(Currencies["EUR"], Currencies["USD"], Temporal.now()),
        Q(Currencies["USD"], Currencies["EUR"], Temporal.now()),
    ]

    ## Define the service:

# Generated at 2022-06-14 04:38:34.219778
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests that FXRateService.queries works as expected.
    """
    # Create a dummy FX rate service:
    class DummyFXRateService(FXRateService):
        def __init__(self) -> None:
            # Cache results:
            self._rates = {}

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Lookup the query:
            q, r = self._rates.get((ccy1, ccy2, asof), (None, None))

            # Check if we have an exact match:
            if q == (ccy1, ccy2, asof):
                return r

            # Check if we have a match with opposite currencies:

# Generated at 2022-06-14 04:38:45.429665
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    queries = (
        (Currency["USD"], Currency["EUR"], Date(2018, 1, 1)),
        (Currency["USD"], Currency["EUR"], Date(2018, 1, 2)),
        (Currency["USD"], Currency["EUR"], Date(2018, 1, 3))
    )

    rates = (
        FXRate(Currency["USD"], Currency["EUR"], Date(2018, 1, 1), ONE),
        FXRate(Currency["USD"], Currency["EUR"], Date(2018, 1, 2), ONE),
        FXRate(Currency["USD"], Currency["EUR"], Date(2018, 1, 3), ONE)
    )

    lookup = {query: rate for query, rate in zip(queries, rates)}


# Generated at 2022-06-14 04:38:51.674088
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the method queries of class FXRateService.
    """
    from .currencies import TestCurrencyService

    ## Test a default foreign exchange service that queries a default currency service with USD, EUR, GBP and TRY:
    ccy_svc = TestCurrencyService.default()
    fx_svc = FXRateService.default()

    ## Test if the queries return the right rates:

# Generated at 2022-06-14 04:39:01.597262
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.exchange import MemoryFXRateService

    ## Create a test FX rate service:
    svc = MemoryFXRateService({
        (Currencies["EUR"], Currencies["USD"], datetime.date.today()): Decimal("2"),
        (Currencies["USD"], Currencies["EUR"], datetime.date.today()): Decimal("0.5")
    })

    ## Date/Time calculations:
    asof = datetime.date.today()
    tomorrow = asof + datetime.timedelta(days=1)
    day_after = asof + datetime.timedelta(days=2)

    ## Check EUR/USD:

# Generated at 2022-06-14 04:39:03.899561
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService.
    """
    assert True


# Generated at 2022-06-14 04:39:05.378569
# Unit test for method query of class FXRateService
def test_FXRateService_query():                                                 # noqa: D103
    pass


# Generated at 2022-06-14 04:39:26.893223
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from dateutil.parser import parse
    from pypara.currencies import Currencies
    from pypara.fx import FXRateLookupError

    class TestingRateService(FXRateService):

        """
        Provides a testing rate service.
        """

        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
                if asof == parse("2019-01-01"):
                    return FXRate(ccy1, ccy2, asof, Decimal("2"))
            if strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            return None


# Generated at 2022-06-14 04:39:37.047345
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class FXRateService
    """
    from pypara.currencies import Currencies

    class DummyRateService(FXRateService):
        """
        Dummy FX rate service for unit tests.
        """

        def __init__(self, rate: Optional[Decimal] = None) -> None:
            """
            Initializes the dummy FX rate service.
            """
            ## Keep the given rate:
            self.rate = rate

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            raise NotImplementedError


# Generated at 2022-06-14 04:39:49.975296
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    ## Given:
    ## Define a dummy service:
    class DummyFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Decimal:
            pass

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[Decimal]]:
            pass

    ## And: Define a dummy service with a non-iterable query argument.
    class DummyFailingFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Decimal:
            pass

        def queries(self, queries: str, strict: bool = False) -> Iterable[Optional[Decimal]]:
            pass



# Generated at 2022-06-14 04:40:02.542237
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.temporal import Date
    from pypara.currencies import Currencies
    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate.of(ccy1, ccy2, asof, ONE) if ccy1 == ccy2 else None
        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (self.query(ccy1, ccy2, asof) for ccy1, ccy2, asof in queries)
    fxrate = TestFXRateService()

# Generated at 2022-06-14 04:40:10.632594
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """
    pass

if __name__ == '__main__':
    import unittest
    import doctest
    unit_suite = unittest.TestLoader().loadTestsFromTestCase(test_FXRateService_query)
    doctest_suite = doctest.DocTestSuite(test_FXRateService_query)
    unittest.TextTestRunner().run(unit_suite)
    unittest.TextTestRunner().run(doctest_suite)

# Generated at 2022-06-14 04:40:23.135380
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    from .fxrates import FXRateServiceError

    # Test with an empty query and non-strict mode
    rate_service = TestFXRateService()
    assert list(rate_service.queries((), strict=False)) == []

    # Test with a non-empty query and non-strict mode
    rate_service = TestFXRateService()
    assert list(rate_service.queries(((Currencies["EUR"], Currencies["USD"], datetime.date.today()),), strict=False)) == [Decimal("2")]
    
    # Test with an empty query and strict mode
    rate_service = TestFXRateService()

# Generated at 2022-06-14 04:40:34.367983
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests that query method of :class:`FXRateService` works as expected.
    """
    from .currencies import Currencies
    from .commons.zeitgeist import Date
    from .market import FXRateService

    ##
    ## Create a memory-based FX rate service and put EUR/USD rate as of today:
    ##
    service = FXRateService.Memory(
        [FXRate(Currencies["EUR"], Currencies["USD"], Date.today(), Decimal("2"))]
    )

    ##
    ## Check that we can query EUR/USD as of today:
    ##
    rate = service.query(Currencies["EUR"], Currencies["USD"], Date.today())
    assert rate == FXRate(Currencies["EUR"], Currencies["USD"], Date.today(), Decimal("2"))

    ##
    ##

# Generated at 2022-06-14 04:40:38.914078
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .commons.zeitgeist import Temporal
    from .currencies import Currencies
    from .fx.static import StaticFXRateService
    from .fx.static.rates import DEFAULT_FX_RATES

    ## Ease typing:
    FXRateService = StaticFXRateService

    ## Test that the default foreign exchange rate service is empty:
    if FXRateService.default is not None:
        raise AssertionError("Default foreign exchange rate service must be empty.")

    ## Assign and test the default foreign exchange rate service:
    FXRateService.default = FXRateService(DEFAULT_FX_RATES)
    if FXRateService.default is None:
        raise AssertionError("Default foreign exchange rate service must be assigned.")

    ## Check the foreign exchange rate query:

# Generated at 2022-06-14 04:40:40.618162
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService.
    """
    pass



# Generated at 2022-06-14 04:40:51.797739
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.commons.zeitgeist import Date
    from pypara.rates.fx import FXRateService
    from pypara.rates.fx.repository import FXRateRepository
    
    ## Create a repository:
    repository = FXRateRepository()
    
    ## Create a service:
    service = FXRateService(repository)
    
    ## Test queries:
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]

# Generated at 2022-06-14 04:41:41.020073
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """Testing queries method of class FXRateService."""
    class MockRateService(FXRateService):

        def __init__(self) -> None:
            self.__rates = [(0, 1, 1), (0, 1, 2), (0, 1, 3), (0, 1, 4), (0, 1, 5), (0, 1, 6), (0, 1, 7)]

        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal(self.__rates[asof.date.toordinal() - 1][2]))


# Generated at 2022-06-14 04:41:49.455554
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import pytest
    import datetime

    from decimal import Decimal
    from pypara.currencies import Currencies

    class MyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
            else:
                return None

    svc = MyFXRateService()

    rate = svc.query(Currencies["EUR"], Currencies["USD"], datetime.date.today())
    assert isinstance(rate, FXRate)
    assert rate

# Generated at 2022-06-14 04:41:59.917699
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .commons.zeitgeist import Date
    from .currencies import Currency
    from .fxrates import FXRate, FXRateService

    from typing import Iterable, Tuple

    from decimal import Decimal

    from unittest import mock

    # Define an FX rate service that returns FX rates when queried:
    class MockedService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 != Currency("EUR"):
                return None
            elif ccy2.code != "USD" and ccy2.code != "TRY":
                return None
            elif asof != Date(2007, 5, 2):
                return None

# Generated at 2022-06-14 04:42:00.969719
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    assert False


# Generated at 2022-06-14 04:42:10.547482
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services import FXRateService

    class FXRateServiceImpl(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("0.5")) if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today() else None


# Generated at 2022-06-14 04:42:11.217295
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:42:23.565181
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .commons.zeitgeist import Date
    from .currencies import Currencies
    from .currencies import is_safe_to_create_FXRate

    class MockFXRateService(FXRateService):

        def __init__(self, rates: Iterable[FXRate]) -> None:
            super().__init__()
            self.rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            for rate in self.rates:
                if is_safe_to_create_FXRate(rate):
                    if rate.ccy1 == ccy1 and rate.ccy2 == ccy2 and rate.date == asof:
                        return rate
            return None


# Generated at 2022-06-14 04:42:32.159985
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): # noqa: D400
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    # Mocks:
    class Mock(FXRateService):
        def query(self, ccy1, ccy2, asof):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate(ccy1, ccy2, asof, Decimal("1"))
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["GBP"] and asof == datetime.date.today():
                return FXRate(ccy1, ccy2, asof, Decimal("2"))
            return None


# Generated at 2022-06-14 04:42:32.620046
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    assert True is True

# Generated at 2022-06-14 04:42:43.285655
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest.mock import patch
    from pypara.fx import FXRateService

    ## Create a mock FX rate service and set it as the default one:
    with patch.object(FXRateService, "default", spec=FXRateService) as mock:
        ## The mock should return a fixed value when queried:
        mock.return_value = "rate"

        ## The queries should return a fixed value each:
        mock.queries.side_effect = [["rate1", "rate2"], ["rate3", "rate4"]]

        ## The mock should return the value when queried:
        assert FXRateService.default.query(None, None, None) == "rate"

        ## The queries should return the correct values:

# Generated at 2022-06-14 04:44:02.658239
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import TestCase

    from .commons.dates import DateBuilder
    from .currencies import Currencies

    class LocalFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            pass

    svc = LocalFXRateService()
    ccy1: Currency = Currencies["EUR"]
    ccy2: Currency = Currencies["USD"]
    date: Date = DateBuilder.today()


# Generated at 2022-06-14 04:44:11.717246
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class :class:`FXRateService`
    """

    from unittest.mock import Mock

    from .currencies import Currency, Currencies
    from .temporal import Temporal, TimeScale

    qry = Mock(spec=str)
    qry.query = Mock(spec=str)
    qry.query.side_effect = [1, 2, 3, 4, 5]

    assert qry.querys([(Currencies["USD"], Currencies["EUR"], Temporal(TimeScale.D1))]) == [1]
    assert qry.querys([(Currencies["USD"], Currencies["EUR"], Temporal(TimeScale.D1))] * 2) == [1, 2]

# Generated at 2022-06-14 04:44:16.039824
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    :author: Qubit Technology <support@qubit-technology.com>
    Test in decorator
    """
    from unittest.mock import Mock
    class FxRateServiceMock(FXRateService):
        """
        Mocked FXRateService
        """
        def __init__(self, return_values):
            self.num_query = 0
            self.return_values = return_values

        def query(self, ccy1, ccy2, asof, strict=False):
            return_value = self.return_values[self.num_query]
            self.num_query += 1
            return return_value

        def queries(self, queries, strict=False):
            for query in queries:
                yield self.query(query[0], query[1], query[2], strict)
   