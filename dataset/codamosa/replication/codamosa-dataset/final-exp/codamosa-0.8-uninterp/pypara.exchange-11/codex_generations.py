

# Generated at 2022-06-14 04:34:32.683798
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Call the method queries and validate the result.
    """
    class TestFXRateService(FXRateService):
        """
        Provides a dummy FX rate service.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            return FXRate(ccy1, ccy2, asof, Decimal("2"))

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            """
            Returns foreign exchange rates for a given collection of currency pairs and dates.
            """

# Generated at 2022-06-14 04:34:45.406020
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies
    from pypara.temporals import Date
    
    class Test(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass
        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [
                FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2")),
                FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("4"))
            ]

    ## Set the default FX rate service:
    FXRateService.default

# Generated at 2022-06-14 04:34:58.602191
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Date

    class MockFXRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            from .currencies import Currency
            from .temporal import Date
            import datetime
            from decimal import Decimal
            from .fxrates import FXRate

            if (ccy1, ccy2, asof) in ((Currency.of("EUR"), Currency.of("USD"), Date.of(datetime.date.today())),
                                      (Currency.of("USD"), Currency.of("EUR"), Date.of(datetime.date.today()))):
                return FXRate(Currency.of("EUR"), Currency.of("USD"), Date.of(datetime.date.today()), Decimal("2"))


# Generated at 2022-06-14 04:35:12.194203
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import unittest
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class _FXRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict = False):
            return FXRate.of(ccy1, ccy2, asof, Decimal(2.0))

        def queries(self, queries, strict = False):

            for ccy1, ccy2, asof in queries:
                yield FXRate.of(ccy1, ccy2, asof, Decimal(2.0))


# Generated at 2022-06-14 04:35:13.407942
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    assert True is True


# Generated at 2022-06-14 04:35:25.544409
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import TestCase
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance.curves import Curve
    from pypara.finance.curves import CurveId

    from pypara.finance.fx import FXRateLookupError, FXRateService

    class DummyFXRateService(FXRateService):
        def __init__(self):
            self.__rates = {}

        def add(self, ccy1: Currency, ccy2: Currency, date: Date, value: Decimal) -> None:
            self.__rates[(ccy1, ccy2, date)] = FXRate(ccy1, ccy2, date, value)


# Generated at 2022-06-14 04:35:26.689197
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:35:27.435400
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass

# Generated at 2022-06-14 04:35:35.979333
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from collections import namedtuple
    from unittest import TestCase
    from unittest.mock import MagicMock
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.markets.temporal import Date, Dates
    from pypara.markets.foreign_exchange import FXRateService

    class MockFXRateService(FXRateService):
        def __init__(self):
            self.query_mock = MagicMock()

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self.query_mock(self, ccy1, ccy2, asof, strict)


# Generated at 2022-06-14 04:35:37.482429
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:35:51.285220
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .commons.zeitgeist import Dates
    from .services.dbrates import DBFXRateService

    fxrsvc = DBFXRateService(DEFAULT_FX_RATES_DB)

    rate = fxrsvc.query(Currencies["EUR"], Currencies["USD"], Dates["2002-01-01"])
    assert rate.ccy1 == Currencies["EUR"]
    assert rate.ccy2 == Currencies["USD"]
    assert rate.date == Dates["2002-01-01"]
    assert rate.value == Decimal("1.06")

    rate = fxrsvc.query(Currencies["USD"], Currencies["EUR"], Dates["2002-01-01"])
    assert rate.ccy1 == Currencies["USD"]

# Generated at 2022-06-14 04:36:03.763387
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    from pypara.currencies import Currencies
    from pypara.temporal import Temporal

    # Mock FXRateService:
    class FXRateServiceMock(FXRateService):

        # Overrides base class method:
        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == ccy2:
                return FXRate(ccy1, ccy2, asof, 1)
            else:
                return FXRate(ccy1, ccy2, asof, 2)

        # Overrides base class method:
        def queries(self, queries, strict=False):
            yield from (self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries)

    # Create the mock FX rate service:


# Generated at 2022-06-14 04:36:16.673686
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.currencies import Currencies
    from pypara.currencies.rates.mock import MockFXRateService

    ## Query a single FX rate using a tuple:
    fxrs = MockFXRateService()
    rate = fxrs.queries([(Currencies["EUR"], Currencies["USD"], Date.now())])
    assert fxrs[0] == rate[0]

    ## Query a single FX rate using the query method:
    rate = fxrs.query(Currencies["EUR"], Currencies["USD"], Date.now())
    assert fxrs[0] == rate

    ## Query two FX rates:

# Generated at 2022-06-14 04:36:26.034656
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .contrib.currencies import ECBFXRateService
    from .commons.zeitgeist import LocalDate
    service = ECBFXRateService()
    rates = list(service.queries([
        (Currency["USD"], Currency["EUR"], LocalDate.parse("2019-01-01")),
        (Currency["USD"], Currency["EUR"], LocalDate.parse("2019-04-03")),
        (Currency["USD"], Currency["EUR"], LocalDate.parse("2019-04-02"))
    ]))
    assert len(rates) == 3


# Generated at 2022-06-14 04:36:39.251873
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103

    from .env import Env
    from .scheduled import Scheduler

    Env.set(Scheduler(Date(2018, 1, 1)))
    svc = FXRateService._create()
    assert svc.query(Currency("EUR"), Currency("USD"), Date(2018, 1, 1)) == FXRate(
        Currency("EUR"), Currency("USD"), Date(2018, 1, 1), Decimal("1.03097")
    )
    assert svc.query(Currency("USD"), Currency("EUR"), Date(2018, 1, 1)) == FXRate(
        Currency("USD"), Currency("EUR"), Date(2018, 1, 1), Decimal("0.96724")
    )

# Generated at 2022-06-14 04:36:52.422652
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from random import choice
    from string import ascii_lowercase
    import datetime
    from pypara.currencies import Currency
    from pypara.services.forex import FXRateService

    def random_string(length: int) -> str:
        return "".join(choice(ascii_lowercase) for _ in range(length))

    # setup:
    date = datetime.date.today()
    expected = [
        (Currency(random_string(5)), Currency(random_string(5)), date),
        (Currency(random_string(5)), Currency(random_string(5)), date),
        (Currency(random_string(5)), Currency(random_string(5)), date),
        (Currency(random_string(5)), Currency(random_string(5)), date),
    ]


# Generated at 2022-06-14 04:36:53.652870
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    return 0


# Generated at 2022-06-14 04:37:02.131587
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date, timedelta
    from decimal import Decimal
    from typing import Iterable, Tuple
    from .currencies import Currency
    from .currencies import Currencies
    from .fx import FXRateService

    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: date, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            filtered = [query for query in queries if date.today() - timedelta(days=1) <= query[2] <= date.today()]

# Generated at 2022-06-14 04:37:15.112259
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxtypes import FXRateLookupError, FXRateService

    # Create an FXRateService implementation
    class StubFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date(2018, 12, 15):
                return FXRate(ccy1, ccy2, asof, Decimal("2.0"))

# Generated at 2022-06-14 04:37:28.682106
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    class DemoForeignExchangeRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) \
                -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal(1.0))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(ccy1, ccy2, asof, strict) for (ccy1, ccy2, asof) in queries]

    from .currencies import Currencies

    fes = DemoForeignExchangeRateService()

    rates = fes.queries([(Currencies["EUR"], Currencies["USD"], Date.today())])


# Generated at 2022-06-14 04:37:48.306924
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currencies 
    from pypara.temporals import Date
    class Service(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal(1))

        def queries(self, queries, strict=False):
            return [self.query(ccy1, ccy2, asof) for (ccy1, ccy2, asof) in queries]

    service = Service()

# Generated at 2022-06-14 04:37:58.137063
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # Local imports
    import pytest
    from pypara.currencies import Currencies
    from pypara.temporal import Temporal, Temporals

    class TestFXRateService(FXRateService):
        # Local imports
        from decimal import Decimal

        #: Defines the FX rates in the test service.

# Generated at 2022-06-14 04:38:09.235746
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency
    from .currencies import CurrencyIso
    from .currencies import CurrencyIsoLatinA
    from .currencies import CurrencyIsoLatinB
    from .currencies import CurrencyIsoNum
    from .currencies import CurrencyIsoNum3
    from .currencies import CurrencyIsoNum3Letter
    from .currencies import CurrencySymbol
    from .currencies import CurrencySymbolLatin
    from .currencies import CurrencySymbolLatinA
    from .currencies import CurrencySymbolLatinB
    from .currencies import CurrencySymbolLatinC
    from .currencies import CurrencySymbolLatinD
    from .currencies import CurrencyUnit
    from .currencies import CurrencyUnitLatinA
    from datetime import date
    from decimal import Decimal

# Generated at 2022-06-14 04:38:19.355615
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    class DummyRateService(FXRateService):

        def query(self,  ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for ccy1, ccy2, asof in queries:
                yield self.query(ccy1, ccy2, asof)

    service = DummyRateService()

# Generated at 2022-06-14 04:38:30.851600
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Performs unit tests on method queries of class FXRateService.
    """
    ## Define a dummy FX rate service for unit testing:
    class DummyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for r in (None for _ in queries):
                yield r

    ## Test that we get the same result no matter we use
    ## query method or queries method with a single query:
    service = DummyFXRateService()
    single = next(service.queries([(None, None, None)], False))

# Generated at 2022-06-14 04:38:31.758879
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:38:44.001798
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of the fxRateService class.
    """
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.datetime import now
    from pypara.fxrates.services import InMemoryFXRateService

    # Create a service instance:
    service = InMemoryFXRateService(
        [
            FXRate(ccy1=Currencies["EUR"], ccy2=Currencies["USD"], date=now().date(), value=Decimal("1.2")),
            FXRate(ccy1=Currencies["USD"], ccy2=Currencies["EUR"], date=now().date(), value=Decimal("0.83")),
        ]
    )

    # Query the rates:

# Generated at 2022-06-14 04:38:56.206981
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .commons.zeitgeist import Date
    from .currencies import Currency
    from .exchanges import Exchange
    from .finance import ExchangeRate
    from .markets import Market
    from decimal import Decimal
    import datetime
    ccys = Currency["EUR", "USD"]
    date = Date(datetime.date(2016, 4, 4))
    exchange = Exchange.of("XType", Market.of("XMarket"))
    rate = ExchangeRate(date, exchange, ccys[0], ccys[1], Decimal(1.123), Decimal(2.123))
    service = exchange.service
    assert service.query(ccys[0], ccys[1], date) == FXRate(ccys[0], ccys[1], date, rate.value)

# Generated at 2022-06-14 04:39:04.156125
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    class MockFXRateService(FXRateService):

        def __init__(self):
            self.queries = []  # type: List[FXRateService.TQuery]
            self.strict = False  # type: bool

        def query(self, ccy1, ccy2, asof, strict=False):
            self.queries.append((ccy1, ccy2, asof))
            self.strict = strict

    ## Create the mock:
    service = MockFXRateService()

    ## Assert argument passing:
    date = datetime.date.today()
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["EUR"]


# Generated at 2022-06-14 04:39:15.215269
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the method query of class FXRateService through a custom FXRateService class.
    """
    # Import stuff:
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    ### Define a custom FXRateService class:
    class Custom(FXRateService):
        """
        A custom foreign exchange rate service provided for unit testing.
        """

        #: Defines the mapping of queries to FX rates.
        _rates = {
            (Currencies["EUR"], Currencies["USD"], datetime.date.today()): Decimal("2.0"),
            (Currencies["USD"], Currencies["EUR"], datetime.date.today()): Decimal("0.5")
        }


# Generated at 2022-06-14 04:39:39.065220
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRate, FXRateService

    assert issubclass(FXRateService, FXRateService)

    class FXRateServiceImpl(FXRateService):
        def query(self, ccy1, ccy2, asof, strict = False):
            assert isinstance(ccy1, Currencies)
            assert isinstance(ccy2, Currencies)
            assert isinstance(asof, datetime.date)
            assert isinstance(strict, bool)
            return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal(2))

        def queries(self, queries, strict = False):
            assert isinstance(ccy1, Currencies)

# Generated at 2022-06-14 04:39:46.680741
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class FXRateService.
    """
    from unittest import TestCase, mock
    from unittest.mock import Mock

    # Define a fake FXRateService instance:
    fx_service = Mock()
    fx_service.query.side_effect = [
        FXRate(Currency("EUR"), Currency("USD"), "2018-01-01", 1.2345),
        FXRate(Currency("EUR"), Currency("USD"), "2018-01-02", 1.2346)
    ]

    # Define a query:
    query = [
        (Currency("EUR"), Currency("USD"), "2018-01-01"),
        (Currency("EUR"), Currency("USD"), "2018-01-02")
    ]

    # Run the queries method:

# Generated at 2022-06-14 04:39:56.860997
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .temporals import Date
    from decimal import Decimal
    from pypara.asset.fxrates import FXRate

    # Define a mock rate:
    asof = Date(2020, 1, 1)
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
    rate = FXRate(ccy1, ccy2, asof, Decimal("2.0"))

    # Define a mock service:
    class MockService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            assert ccy1 == rate.ccy1
            assert ccy2 == rate.ccy2
            assert asof == rate.date
           

# Generated at 2022-06-14 04:40:05.589614
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """
    # noinspection PyProtectedMember
    from pypara.finance._marketdata import _DEBUG_FX_RATE_SERVICE
    from pypara.currencies import Currencies
    from pypara.time import Date

    queries = [
        (Currencies["EUR"], Currencies["USD"], Date("2019-01-01")),
        (Currencies["USD"], Currencies["EUR"], Date("2019-01-01"))
    ]

    assert all(_DEBUG_FX_RATE_SERVICE.queries(queries))
    assert all(_DEBUG_FX_RATE_SERVICE.queries(queries, strict=True))

# Generated at 2022-06-14 04:40:18.455377
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .services import FXRateServiceInMemory
    from .temporals import Temporals

    # Create a service with a hard-coded FX rate for EUR/USD as of today:
    service = FXRateServiceInMemory()  # type: FXRateService
    service.add_rate(Currencies["EUR"], Currencies["USD"], Temporals.today(), 0.89)

    # Create some queries:
    q1 = (Currencies["EUR"], Currencies["USD"], Temporals.today())  # Query 1
    q2 = (Currencies["USD"], Currencies["EUR"], Temporals.today())  # Query 2
    q3 = (Currencies["EUR"], Currencies["USD"], Temporals.today() - 1)  # Query 3

# Generated at 2022-06-14 04:40:19.487619
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:40:29.659226
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate, FXRateLookupError, FXRateService

    class TestService(FXRateService):
        def __init__(self, strict: bool = False):
            self.rates = [
                FXRate(Currencies["EUR"], Currencies["USD"], date.today(), Decimal("2")),
                FXRate(Currencies["USD"], Currencies["EUR"], date.today(), Decimal("1/2"))
            ]
            self.strict = strict


# Generated at 2022-06-14 04:40:39.465199
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.temporals.date import Date
    from pypara.currencies import Currencies
    from testing.mocking.fxrateservice import MockFXRateService
    from decimal import Decimal
    from datetime import date
    queries = [
        (Currencies.EUR, Currencies.USD, Date(date(2017, 1, 1))),
        (Currencies.EUR, Currencies.USD, Date(date(2018, 1, 1))),
        (Currencies.EUR, Currencies.USD, Date(date(2019, 1, 1)))
    ]
    rates = (
        Decimal('1.0000'), Decimal('0.9051'), Decimal('1.1638')
    )
    service = MockFXRateService()

# Generated at 2022-06-14 04:40:50.765324
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.curves import InterpolationCurve
    from pypara.services.curves import LinearInterpolationMethod

# Generated at 2022-06-14 04:40:58.272346
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests :method:`FXRateService.queries` method.
    """

    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    ## Define the FX rate service:
    class FXRateServiceImpl(FXRateService):

        def __init__(self, rates: Iterable[FXRate]) -> None:
            self.rates = {
                (rate.ccy1, rate.ccy2, rate.date): rate
                for rate in rates
            }

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if strict:
                return self.rates[(ccy1, ccy2, asof)]

# Generated at 2022-06-14 04:41:49.181732
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .exchangerates import FXRateService as FRS
    from .temporal import Temporal
    from decimal import Decimal
    from datetime import date

    ## Prepare an FX rate service:
    fxrates = [
        FXRate(Currencies["EUR"], Currencies["USD"], date(2019, 1, 1), Decimal("2")),
        FXRate(Currencies["EUR"], Currencies["USD"], date(2019, 2, 1), Decimal("2")),
        FXRate(Currencies["EUR"], Currencies["USD"], date(2019, 3, 1), Decimal("2")),
    ]


# Generated at 2022-06-14 04:41:59.916748
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency, Currencies
    from .temporal import Temporal, Date
    from .commons.numbers import ZERO, ONE

    class DummyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False):
            if ccy1 == ccy2:
                return FXRate(ccy1, ccy2, asof, ONE)

    # Create a dummy service
    service = DummyFXRateService()

    # Query for EUR/USD
    qry = service.query(Currencies["EUR"], Currencies["USD"], Temporal.now())
    assert qry is None, "Should be `None`"

    # Query for EUR/EUR

# Generated at 2022-06-14 04:42:07.759540
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import unittest

    from dataclasses import dataclass

    from .currencies import Currencies

    from . import temps

    ## Define a service:
    @dataclass
    class MyService(FXRateService):
        @staticmethod
        def query(ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == temps.Date(2017, 12, 15):
                return FXRate(Currencies["EUR"], Currencies["USD"], temps.Date(2017, 12, 15), 1.23)
            return None

        @staticmethod
        def queries(queries: Iterable[TQuery], strict: bool = False) -> None:
            pass

# Generated at 2022-06-14 04:42:20.126975
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies

    class FXRS(FXRateService):
        def __init__(self):
            pass

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1.1")) if (ccy1, ccy2, asof) in self.queries else None


# Generated at 2022-06-14 04:42:29.807288
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies
    from pypara.temporal import CurrentDate
    from .services.fx import MemoryFXRateService

    ## We will not define all rates, but only one:
    rates = [
        FXRate.of(Currencies["USD"], Currencies["TRY"], CurrentDate.get().date(), Decimal("6.0"))
    ]

    ## Create service:
    service = MemoryFXRateService(rates)

    ## Query for all combinations of USD/TRY and TRY/USD:
    assert service.query(Currencies["USD"], Currencies["TRY"], CurrentDate.get().date()) == rates[0]
    assert service.query(Currencies["TRY"], Currencies["USD"], CurrentDate.get().date()) == rates[0] ** -1

    ## When strict, we should raise an error when the rate is not

# Generated at 2022-06-14 04:42:40.476754
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the query method of the FXRateService class.
    """
    # Import packages:
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    # Create a new FXRateService:
    class TestFXRateService(FXRateService):
        """
        Provides an FX rate service for testing purposes.
        """

        # noinspection PyPep8Naming,PyShadowingBuiltins

# Generated at 2022-06-14 04:42:48.389764
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof):
            raise NotImplementedError()

        def queries(self, queries, strict):
            rates = [None]
            return rates

    queries = [
        [Currency("EUR"), Currency("USD"), Date(2017, 5, 8)],
        [Currency("EUR"), Currency("USD"), Date(2017, 5, 9)],
        [Currency("EUR"), Currency("USD"), Date(2017, 5, 10)]
    ]

    fx_rate_service = TestFXRateService()
    rates = fx_rate_service.queries(queries)

    assert rates is not None

    assert len(rates) == len(queries)

    from decimal import Decimal

# Generated at 2022-06-14 04:43:00.847381
# Unit test for method query of class FXRateService
def test_FXRateService_query(): # noqa: D103
    import pytest
    from decimal import Decimal
    import datetime
    from pypara.currencies import Currency
    from pypara.currencies import Currencies
    from pypara.fx_rates import FXRate
    from pypara.fx_rates import FXRateService

    currency = Currencies["USD"]
    date = datetime.date.today()
    rate = Decimal("1.25")

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: datetime.date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == currency and ccy2 == currency and asof == date:
                return FXRate(ccy1, ccy2, asof, rate)


# Generated at 2022-06-14 04:43:08.037138
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    service = FXRateService()

    ## Test default implementation (should return None):
    rate = service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today(), strict=False)
    assert rate is None

    ## Test default implementation (should raise FXRateLookupError):
    with pytest.raises(FXRateLookupError) as error:
        rate = service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today(), strict=True)


# Generated at 2022-06-14 04:43:18.600491
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest import TestCase, mock
    from pypara.foreign_exchange import FXRateService

    class MockService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return ccy1, ccy2, asof

    service = MockService()
    queries = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

    with mock.patch('pypara.foreign_exchange.FXRateService.query') as mocked_query:
        mocked_query.return_value = (1, 2, 3)
        ret = service.queries(queries)
        assert ret == [(1, 2, 3)] * 3
