

# Generated at 2022-06-14 04:34:38.088829
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # Test query for invalid query arguments.
    #
    # Define a simple FX rate service.
    class Svc(FXRateService):

        def __init__(self):
            self.__rates = {}

        def add(self, ccy1: Currency, ccy2: Currency, asof: Date, rate: FXRate):
            self.__rates[(ccy1, ccy2, asof)] = rate

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self.__rates.get((ccy1, ccy2, asof))

    # Create the FX rate service.
    svc = Svc()

    # Add a EUR/USD FX rate.
    from decimal import Decimal
    from datetime import date

# Generated at 2022-06-14 04:34:39.232933
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:34:48.998603
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .services.dummy_fxrate_service import DummyFXRateService
    from .temporal import Temporal

    _service = DummyFXRateService()
    assert _service.query(Currencies["EUR"], Currencies["USD"], Temporal.today()) == FXRate(Currencies["EUR"], Currencies["USD"], Temporal.today(), Decimal("1.10"))
    assert _service.query(Currencies["USD"], Currencies["EUR"], Temporal.today(), True) == FXRate(Currencies["USD"], Currencies["EUR"], Temporal.today(), Decimal("1.10"))
    try:
        _service.query(Currencies["XXX"], Currencies["YYY"], Temporal.today(), True)
        assert False
    except FXRateLookupError:
        assert True




# Generated at 2022-06-14 04:34:59.842179
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest import TestCase, mock
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currencies

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: date, strict: bool = False) -> Optional[FXRate]:
            if (ccy1, ccy2) == (Currencies["EUR"], Currencies["USD"]):
                return FXRate(ccy1, ccy2, asof, Decimal("2"))
            return None

        def queries(self, queries: Iterable[Tuple[Currency, Currency, date]], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for query in queries:
                yield self.query(*query)

    service = TestFXRateService

# Generated at 2022-06-14 04:35:08.404402
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    import datetime
    from decimal import Decimal
    from .currencies import Currency
    from .temporal import Temporal
    from .fx.rates import FXRateLookupError, FXRateService

    ### Mock the FX rate service:
    class MockFXRateService(FXRateService):

        def _query(self, ccy1: Currency, ccy2: Currency, asof: Temporal) -> Optional[Decimal]:
            if ccy1.code == "EUR" and ccy2.code == "USD" and asof.truncate() == datetime.date(2018, 1, 1):
                return Decimal("2")


# Generated at 2022-06-14 04:35:19.705281
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    import datetime
    from decimal import Decimal

    class MockFXRateService(FXRateService):
        def __init__(self, _rates):
            self.__rates = _rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date = None, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for ccy1, ccy2, asof in queries:
                yield self.__rates.get((ccy1, ccy2, asof))


# Generated at 2022-06-14 04:35:31.859316
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.exchange import FXRateService
    from pypara.zeitgeist import Date

    class DummyRateService(FXRateService):
        """
        Dummy FX rate service for unit test purposes.
        """


# Generated at 2022-06-14 04:35:33.621093
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    This unit test checks method query for class FXRateService.
    """


# Generated at 2022-06-14 04:35:43.562257
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import CurrencyContext
    from .currencies import Currencies
    import datetime
    from decimal import Decimal

    context = CurrencyContext(date=datetime.date.today(), fx_service=None)
    rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    context.fx_service = FXRateService()
    context.fx_service.query = lambda ccy1, ccy2, asof, strict: rate
    assert context.fx_service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) == rate

# Generated at 2022-06-14 04:35:53.049950
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency, Currencies # noqa: F401
    from .fxrates import FXRateService, TEmptyService # noqa: F401
    from decimal import Decimal # noqa: F401
    from numpy.testing import assert_array_equal # noqa: F401
    from random import choice # noqa: F401
    from unittest import TestCase # noqa: F401

    _currency = lambda: [x[1] for x in sorted(Currencies.items())]


# Generated at 2022-06-14 04:35:57.490250
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass

# Generated at 2022-06-14 04:36:07.136681
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:36:15.867738
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests :method:`FXRateService.queries` method.
    """
    ## Import required modules:
    import datetime

    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance.fx import FXRate, FXRateService


# Generated at 2022-06-14 04:36:28.004903
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Performs the unit test for method query of class :class:`FXRateService`.
    """
    from unittest import TestCase, mock
    from unittest.mock import Mock, patch

    from pypara.currencies import Currency
    from pypara.fxrates import FXRate, FXRateLookupError

    class TestFXRateService(FXRateService):
        """
        Defines a concrete `FXRateService` class for testing.
        """

        @mock.patch("pypara.fxrates.FXRateService.query")
        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return FXRateService.query(self, **dict(queries[0]), strict=strict)


# Generated at 2022-06-14 04:36:41.598218
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Temporal
    from .fxrates.static import StaticFXRateService

    service = StaticFXRateService()
    assert list(service.queries([(Currencies["USD"], Currencies["EUR"], Temporal.of("2018-01-01"))]))[0] == FXRate(
        Currencies["USD"], Currencies["EUR"], Temporal.of("2018-01-01"), Decimal("0.89775")
    )
    assert list(service.queries([(Currencies["EUR"], Currencies["USD"], Temporal.of("2018-01-01"))]))[0] == FXRate(
        Currencies["EUR"], Currencies["USD"], Temporal.of("2018-01-01"), Decimal("1.1177")
    )

# Generated at 2022-06-14 04:36:54.783566
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateLookupError, FXRateService
    from pypara.temporal import Temporal
    from pypara.utils import DateUtils
    from unittest import TestCase

    class MockFxRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            if (ccy1, ccy2, asof) in self.queries:
                return self.queries[(ccy1, ccy2, asof)]
            if strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            return None


# Generated at 2022-06-14 04:37:07.139050
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .commons.dateutils import Dates
    from .fxrates.static import StaticFXRateService
    import pytest

    usd_eur_rate = StaticFXRateService.load_text("USD,EUR,2019-01-01,0.8")
    queries = [(Currency("USD"), Currency("EUR"), Dates["2019-01-01"]),
               (Currency("EUR"), Currency("USD"), Dates["2019-01-01"])]

    fxrates = usd_eur_rate.queries(queries)

    fxrate = next(fxrates)
    assert fxrate.ccy1 == Currency("USD")
    assert fxrate.ccy2 == Currency("EUR")
    assert fxrate.date == Dates["2019-01-01"]
    assert fxrate

# Generated at 2022-06-14 04:37:17.236434
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests functionality of `query` method of class `FXRateService`
    """
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from .test_enum import enum_test
    from .test_str import str_test
    
    # Test Abstract FXRateService
    class TestFXRateService(FXRateService):
        
        def query(self, ccy1, ccy2, asof, strict=False):
            return None
        
        def queries(self, queries, strict=False):
            return []
    
    enum_test(TestFXRateService, "default", FXRateService.default, isinstance(TestFXRateService().query(Currencies["EUR"], Currencies["USD"], date.today()), FXRate))
    
    # Test FXRateService


# Generated at 2022-06-14 04:37:29.223251
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.commons.temporal import Temporals
    from pypara.currencies import Currencies
    from pypara.finance.currencies import FXRate
    import datetime
    import pytest
    import os

    # Get path:
    path = os.path.join(os.path.dirname(__file__), "resources", "fx", "rates.csv")

    # Create FX rate service:
    FXRateService.default = FXRateFileService(path)

    # Test simple rate:

# Generated at 2022-06-14 04:37:40.379338
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:37:57.603525
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.temporal import Date

    class SimpleFXRateService(FXRateService):

        query_rate = dict((
            ((Currency("EUR"), Currency("USD"), Date.of(2018, 1, 1)), Decimal("10")),
            ((Currency("EUR"), Currency("USD"), Date.of(2018, 1, 2)), Decimal("20")),
            ((Currency("USD"), Currency("EUR"), Date.of(2018, 1, 1)), Decimal("0.1")),
            ((Currency("USD"), Currency("EUR"), Date.of(2018, 1, 2)), Decimal("0.2")),
        ))


# Generated at 2022-06-14 04:38:06.692716
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():  ## noqa: D102
    from unittest import TestCase
    from pytest import raises
    from datetime import date
    from decimal import Decimal

    from pypara.currencies import Currency, Currencies
    from pypara.finance.commons import Temporal

    class TestQuery(TestCase):
        """
        Provides a unit test for method queries of class FXRateService.
        """

        class TestFXRateService(FXRateService):
            """
            Provides an FX rate service for performing unit tests.
            """


# Generated at 2022-06-14 04:38:18.472220
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    import datetime

    from decimal import Decimal

    from pypara.currencies import Currencies

    from .commons.zeitgeist import UTCDate

    from .fxrates.memory import FXRateMemory

    queries = [
        (Currencies["EUR"], Currencies["USD"], UTCDate.of(datetime.date(2010, 1, 1))),
        (Currencies["USD"], Currencies["EUR"], UTCDate.of(datetime.date(2010, 1, 1))),
        (Currencies["EUR"], Currencies["USD"], UTCDate.of(datetime.date(2010, 1, 2))),
        (Currencies["USD"], Currencies["EUR"], UTCDate.of(datetime.date(2010, 1, 2)))
    ]


# Generated at 2022-06-14 04:38:30.702528
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .commons.zeitgeist import now
    from .currencies import Currencies
    from .services import FXRateService

    class FixedRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if strict:
                raise FXRateLookupError(ccy1, ccy2, asof)

            return FXRate(ccy1, ccy2, asof, Decimal("1.1"))

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(*q, strict=strict) for q in queries]

    # Create a rate service instance:
    rsvc = FixedRateService()

# Generated at 2022-06-14 04:38:39.293619
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .fx.fx_rate_service import InMemoryFXRateService
    from .values import Temporal

    EUR = Currency("EUR", "EUR", "978", is_fund=True)
    USD = Currency("USD", "USD", "840", is_fund=True)


# Generated at 2022-06-14 04:38:48.210012
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from itertools import chain
    from unittest import TestCase, main
    from pypara.currencies import Currency, Currencies
    from pypara.temporal import Temporal, Date


# Generated at 2022-06-14 04:39:00.149625
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class Service(FXRateService):
        def __init__(self):
            self.rates = [
                FXRate(Currencies["EUR"], Currencies["USD"], datetime.date(2018, 1, 1), Decimal("1.21")),
                FXRate(Currencies["USD"], Currencies["EUR"], datetime.date(2018, 1, 1), Decimal("0.82")),
            ]

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            for rate in self.rates:
                if rate.ccy1 == ccy1 and rate.ccy2 == ccy2 and rate.date == asof:
                    return

# Generated at 2022-06-14 04:39:13.012625
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the :method:`FXRateService.queries` method.
    """
    ## Basic behavior
    assert list(FXRateService.queries(None, False)) == list()  # noqa: E711
    assert list(FXRateService.queries([], False)) == list()
    assert list(FXRateService.queries([(0, 1, 2), (3, 4, 5)], False)) == list()  # noqa: E721
    assert list(FXRateService.queries([(0, 1, 2), (3, 4, 5)], True)) == list()  # noqa: E721

    ## Representation
    service = _TestService()

# Generated at 2022-06-14 04:39:14.047390
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:39:23.440905
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies
    from pypara.services import FXRateService

    ## Define the base currency:
    baseccy = Currencies["EUR"]

    ## Define a special FX rate service:
    class MockFXRateService(FXRateService):
        """Provides a mock FX rate service."""

        def __init__(self) -> None:
            """Initializes the mock FX rate service."""

# Generated at 2022-06-14 04:39:51.055767
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService
    from .commons.zeitgeist import Date

    class AtDateRateService(FXRateService):
        """
        Provides a simple foreign exchange rate service that returns rates as of a specified date.
        """


# Generated at 2022-06-14 04:40:02.495924
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    # Imports
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    # Arrange
    service = FXRateService()

    # Act
    result = service.queries([(Currencies["USD"], Currencies["GBP"], datetime.date.today()),
                              (Currencies["USD"], Currencies["GBP"], datetime.date.today())])
    result = list(result)

    # Assert
    assert result[0].ccy1 == Currencies['USD']
    assert result[0].ccy2 == Currencies['GBP']
    assert result[0].date == datetime.date.today()
    assert result[0].value == Decimal("0.5")


# Generated at 2022-06-14 04:40:14.855848
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .temporals import date
    from .types import Temporals

    from .fx import FXRateService

    class MockFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("2"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for ccy1, ccy2, asof in queries:
                yield self.query(ccy1, ccy2, asof)

    fxService = MockFXRateService()

# Generated at 2022-06-14 04:40:26.510484
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Correclty retrieve fx rate by query.
    """
    ## Mock the abstract class:
    class MockFXRateService(FXRateService):

        def __init__(self):
            self.fxrates = {}

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            key = (ccy1, ccy2, asof)
            return self.fxrates[key] if key in self.fxrates else None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(*query) for query in queries]

    ## Build the test data:
    from decimal import Decimal
    from pypara.currencies import Currencies

# Generated at 2022-06-14 04:40:35.884190
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    # Define a service:
    class TestService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate.of(ccy1, ccy2, asof, Decimal("2"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (self.query(q[0], q[1], q[2]) for q in queries)

    # Test:
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    service = TestService()

# Generated at 2022-06-14 04:40:47.236041
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests functionality of the queries method of class FXRateService.
    """
    
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate, FXRateLookupError, FXRateService, test_FXRate
    
    
    class FakeFXRateService(FXRateService):
        """
        Provides a fake foreign exchange rate service class.
        """
        
        def __init__(self, rates: Iterable[FXRate]):
            """
            Initializes the fake foreign exchange rate service.
            """
            self._rates = dict(((rate.ccy1, rate.ccy2, rate.asof), rate) for rate in rates)
        

# Generated at 2022-06-14 04:40:56.550568
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.exchange import FXRate

    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            rate = FXRate(ccy1, ccy2, date=asof, value=Decimal("1.56"))
            return rate

    service = MockFXRateService()
    usd = Currencies["USD"]
    gbp = Currencies["GBP"]
    asof = datetime.date.today()
    rate = service.query(ccy1=usd, ccy2=gbp, asof=asof, strict=False)

# Generated at 2022-06-14 04:41:05.960166
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from unittest import TestCase
    from pypara.currencies import Currencies
    from pypara.market.fx import FXRateService

    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate.of(ccy1, ccy2, asof, Decimal("2.5"))

# Generated at 2022-06-14 04:41:17.805851
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test that all the queries are carried out even if the strict flag is set.
    """

    # Define a query tuple:
    TQuery = FXRateService.TQuery

    # Define some value tuples:
    TValue = Tuple[Currency, Currency, Date, Optional[FXRate]]
    values = [
        TValue(Currency("EUR"), Currency("USD"), Date("2018-01-01"), FXRate("EUR", "USD", "2018-01-01", Decimal("1"))),
        TValue(
            Currency("EUR"),
            Currency("USD"),
            Date("2018-01-01"),
            FXRate("EUR", "USD", "2018-01-01", Decimal("1.25")),
        ),
    ]

    # Define the dummy rate service:

# Generated at 2022-06-14 04:41:24.477208
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class :class:`FXRateService`
    """
    # local imports:
    from para.commons.zeitgeist import Date

    # create a mock class:
    class Mock(FXRateService):
        """
        Provides a mock service for foreign exchange rates.
        """
        def _query(self, ccy1, ccy2, asof):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == Date(1999, 12, 31):
                return FXRate(Currencies["EUR"], Currencies["USD"], Date(1999, 12, 31), Decimal("2.0000000"))
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"] and asof == Date(1999, 12, 31):
                return

# Generated at 2022-06-14 04:42:10.278463
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Test for method query of class FXRateService.
    """
    from .currencies import Currency
    from .fxrates import FXRateService
    from .zeitgeist import Date
    from .zeitgeist import today
    
    asof = today()
    ccy1 = Currency("EUR")
    ccy2 = Currency("USD")
    assert ((ccy1, ccy2) not in FXRateService.default.oracle)
    
    rate = FXRateService.default.query(ccy1, ccy2, asof)
    assert rate == None
    assert ((ccy1, ccy2) in FXRateService.default.oracle)
    
    rate = FXRateService.default.query(ccy1, ccy2, asof)
    assert rate == None

# Generated at 2022-06-14 04:42:14.837143
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    r = FXRate(Currency.EUR, Currency.USD, Date(2010, 1, 1), Decimal(1.5))
    assert FXRateService().query(Currency.EUR, Currency.USD, Date(2010, 1, 1)) == r

# Generated at 2022-06-14 04:42:25.961288
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """
    from unittest import TestCase
    from pypara.currencies import Currencies as Currencies
    from pypara.trade import Temporals as Temporals

    def test_case(self):
        for query in self.queries:
            self.assertIsNotNone(self.rate_service.query(*query, strict=self.strict))

    class MockRateService(FXRateService):
        def __init__(self, queries):
            self.queries = queries

        def query(self, *query, **kwargs):
            return next((rate for rate in self.queries if rate[0:3] == query), None)


# Generated at 2022-06-14 04:42:38.051387
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .times import get_today

    class _Test(FXRateService):

        def query(
                self,
                ccy1: Currency,
                ccy2: Currency,
                asof: Date,
                strict: bool = False,
        ) -> Optional[FXRate]:
            if (ccy1, ccy2, asof) == (Currencies["AED"], Currencies["USD"], get_today()) or \
                    (ccy1, ccy2, asof) == (Currencies["USD"], Currencies["AED"], get_today()):
                return FXRate(Currencies["AED"], Currencies["USD"], get_today(), Decimal(0.2722))

# Generated at 2022-06-14 04:42:50.080842
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies
    from pypara.currencies import Currency
    from pypara.currencies.queries import CurrencyPairQuery
    from pypara.fx.memservices import InMemoryFXRateService

    ## Create an in-memory FX rate service that
    ## has "EUR/USD" rates for everyday from 2009/1/1 to 2009/12/31:

# Generated at 2022-06-14 04:43:03.135014
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies, CurrenciesLookupError
    from pypara.fx import FXRate, FXRateLookupError
    from pypara.fx.services import DatedFXRateService

    ## Set the base currency:
    base_ccy = Currencies["USD"]

    ## Rate sample:

# Generated at 2022-06-14 04:43:03.685056
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass

# Generated at 2022-06-14 04:43:15.209098
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest import TestCase, main

    from .commons.temporal import Days

    from .currencies import Currencies

    from .fxrates.sources import CachedFXRateSource, InMemoryFXRateSource

    class FXRateServiceTestCase(TestCase):

        def test_FXRateService_queries(self):
            ## Create a sample FX rate service:
            service = CachedFXRateSource(InMemoryFXRateSource(
                FXRate(Currencies["EUR"], Currencies["USD"], Days[-1].date, Decimal(1.1)),
                FXRate(Currencies["EUR"], Currencies["USD"], Days[-2].date, Decimal(1.2)),
            ))

            ## Check that we can extract FX rates:

# Generated at 2022-06-14 04:43:23.822862
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.currencies import Currencies
    from pypara.commons.zeitgeist import Date
    from pypara.finance.fx import FXRate, FXRateService

    ## Check abstract class:
    with pytest.raises(TypeError):
        FXRateService.query(None, Currencies["EUR"], Currencies["USD"], Date.today())

    ## Check non-strict non-required rate:
    class NullFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

    service = NullFXRateService()

# Generated at 2022-06-14 04:43:24.669900
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass
