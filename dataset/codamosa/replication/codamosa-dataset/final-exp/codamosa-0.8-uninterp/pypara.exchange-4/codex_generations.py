

# Generated at 2022-06-14 04:34:33.759450
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:34:46.186583
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    class TestService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict = False):
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"] and asof == datetime.date.today():
                return FXRate(Currencies["USD"], Currencies["EUR"], asof, Decimal("0.7"))
        def queries(self, queries, strict = False):
            pass
    tservice = TestService()
    rate = tservice.query(Currencies["USD"], Currencies["EUR"], datetime.date.today())
    assert isinstance(rate, FXRate)
    assert rate.ccy1 == Currencies["USD"]
    assert rate.ccy

# Generated at 2022-06-14 04:34:58.801742
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime

    from decimal import Decimal

    from pypara.currencies import Currencies

    ## Create and initialize `FXRateService`:
    service = FXRateService()
    service.default = service

    ## Test the method:
    rate = service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today())
    assert rate is None

    rate = service.query(Currencies["USD"], Currencies["USD"], datetime.date.today())
    assert rate is None

    rate = service.query(Currencies["USD"], Currencies["EUR"], datetime.date.today(), strict=True)
    assert rate is None

    rate = service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today(), strict=True)
    assert rate is None



# Generated at 2022-06-14 04:35:01.314988
# Unit test for method query of class FXRateService
def test_FXRateService_query(): # noqa: D103
    """
    Unit test for method query of class FXRateService.
    """
    assert True == True


# Generated at 2022-06-14 04:35:09.613236
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.fxrates import FXRateServiceTest

    queries = [
        (Currencies["USD"], Currencies["EUR"], datetime.date(2019, 11, 1)),
        (Currencies["EUR"], Currencies["USD"], datetime.date(2019, 11, 1)),
        (Currencies["EUR"], Currencies["USD"], datetime.date(2019, 11, 2)),
        (Currencies["USD"], Currencies["TRY"], datetime.date(2019, 11, 1)),
        (Currencies["USD"], Currencies["TRY"], datetime.date(2019, 11, 3))
    ]

    service = FXRateServiceTest()
    rates = service.queries(queries)

# Generated at 2022-06-14 04:35:20.531987
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # Import system modules
    import time

    # Import custom modules
    from pypara.currencies import Currency, Currencies
    from pypara.fx.services import FXRateService, FXRateServiceFactory

    # Create FX rate service
    fx_rate_service = FXRateServiceFactory().default()

    # Get today's date
    today = time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday

    # Query EUR/USD FX rate
    fx_rate_eur_usd = fx_rate_service.query(Currencies["EUR"], Currencies["USD"], today)
    assert fx_rate_eur_usd.value > Currency.ZERO

    # Query EUR/GBP FX rate
    fx_rate_eur_gbp = fx_rate_service

# Generated at 2022-06-14 04:35:32.090592
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService
    from pypara.services import ServiceRegistry

    # Define various currencies:
    TRY = Currencies["TRY"]
    EUR = Currencies["EUR"]
    USD = Currencies["USD"]
    JPY = Currencies["JPY"]
    GBP = Currencies["GBP"]

    # Define some dates:
    xxx = Date(2000, 1, 1)
    d1 = Date(2012, 1, 1)
    d2 = Date(2012, 1, 2)
    d3 = Date(2012, 1, 3)
    d4 = Date(2012, 1, 4)

    # Define the default lookup error:

# Generated at 2022-06-14 04:35:42.565055
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    This test is designed to ensure the iterator returned by the `FXRateService.queries` method is properly closed.
    """
    import pytest

    class AlwaysClosingRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            with pytest.raises(AttributeError):
                yield None

    ars = AlwaysClosingRateService()
    with pytest.raises(AttributeError):
        next(ars.queries(()))

# Generated at 2022-06-14 04:35:52.616532
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .commons.temporal import Temporal
    from .commons.zeitgeist import Date
    from .currencies import Currency, Currencies
    from .currencies.currencies import Currencies
    from .fx import FXRateLookupError, FXRateService

    ## Define a mock FX rate service class:

# Generated at 2022-06-14 04:36:01.857957
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    #import unittest
    #from unittest import mock
    #class Test(unittest.TestCase):
    #    @mock.patch.object(FXRateService.default, "query")
    #    def test_query(self, mock_fx_rate_service_query):
    #        asof = Datetime()
    #        query = (Currencies["EUR"], Currencies["USD"], asof)
    #        fx_rate = FXRateService.default.query(query.ccy1, query.ccy2, query.asof, True)
    #        assert FXRateService.default.query == mock_fx_rate_service_query.query
    #unittest.main()
    pass

# Generated at 2022-06-14 04:36:15.186680
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currency

    ## Define a simple query:
    query = (Currency("EUR"), Currency("USD"), date(2019, 1, 1))

    ## Define the expected result:
    expected = FXRate(Currency("EUR"), Currency("USD"), date(2019, 1, 1), Decimal("2.0"))

    ## Define a test service:
    class TestService(FXRateService):
        """
        Provides a simple test service.
        """
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """

# Generated at 2022-06-14 04:36:27.556781
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: E305
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class Query(FXRateService):  # noqa: E701
        """
        Provides a foreign exchange rate service implementation for testing.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """

# Generated at 2022-06-14 04:36:29.913259
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """
    pass

# Generated at 2022-06-14 04:36:42.382198
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .commons.zeitgeist import Date

    class MyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof.date.year == 2019:
                return FXRate(Currencies["EUR"], Currencies["USD"], asof, Decimal("1.10"))
            else:
                return None

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            from itertools import starmap
            from operator import methodcaller


# Generated at 2022-06-14 04:36:55.663869
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """TODO: Implement unit test for :method:`FXRateService.queries`"""
    # import unittest
    # from unittest import mock
    # from unittest.mock import MagicMock
    # from pypara.fxrates import FXRateService, FXRateLookupError
    # from pypara.commons.zeitgeist import Date
    # from pypara.currencies import Currency
    #
    # class TestFXRateService(unittest.TestCase):
    #     """Provides unit test for :class:`FXRateService`."""
    #
    #     def test_queries(self):
    #         """Unit test for :method:`FXRateService.queries`"""
    #         ## Create the mocks:
    #         mock_fxrates = MagicMock()
   

# Generated at 2022-06-14 04:37:07.260685
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies
    from pypara.date import now, today, yesterday

    # Set the default FX rate service:
    from pypara.fx import InMemoryFXRateService

# Generated at 2022-06-14 04:37:17.293115
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Verifies the implementation and behavior of method queries of class FXRateService.
    """
    from datetime import date
    from decimal import Decimal
    from unittest import TestCase, mock

    from pypara.currencies import Currency
    from pypara.markets import FXRateService

    class TestFXRateService(FXRateService):
        """
        Defines an FX rate service for unit testing.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: date, strict: bool = False) -> Decimal:
            if (ccy1, ccy2, asof) not in self.rates:
                if strict:
                    raise FXRateLookupError(ccy1, ccy2, asof)
                else:
                    return None

# Generated at 2022-06-14 04:37:29.498768
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService, FXRate

    service = FXRateService()

    def nassert(expected, queries, strict=False):
        assert expected == [rate for rate in service.queries(queries, strict)]

    def assertq(ccy1, ccy2, asof, value):
        nassert([FXRate(ccy1, ccy2, asof, value)], [(ccy1, ccy2, asof)])

    ## No data
    assertq(Currencies["EUR"], Currencies["USD"], date(2017, 1, 1), Decimal("1.0"))

# Generated at 2022-06-14 04:37:40.595541
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies, Currency

    ## The parameters:
    asof = Date.today()
    usd = Currencies["USD"]
    eur = Currencies["EUR"]
    queries = ((usd, eur, asof), (eur, usd, asof))

    # Test with a service that provides FX rates:
    class GoodService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == usd and ccy2 == eur and asof == asof:
                return FXRate(usd, eur, asof, Decimal(2))

# Generated at 2022-06-14 04:37:51.700824
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test queries method of class FXRateService
    """
    import datetime as dt
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.currencies import Currencies as CCY
    from pypara.fx import FXRate

    # Define a unit test class:
    class FXRateServiceTest(FXRateService):
        """
        Test class for FXRateService.
        """
        def __init__(self, rates: Iterable[FXRate]):
            """
            Init.
            """
            self.rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Query.
            """

# Generated at 2022-06-14 04:38:07.375989
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """
    from unittest import TestCase
    import datetime

    from decimal import Decimal

    from pypara.currencies import Currency, Currencies
    from pypara.temporal import Date
    from pypara.timeutils import TimeUtils

    class MockService(FXRateService):
        """
        Provides a mock implementation of foreign exchange rate service.
        """


# Generated at 2022-06-14 04:38:20.889332
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    **Purpose**: Test method query of class FXRateService.

    **Assertion**: The method query of class FXRateService should not raise any errors.
    """
    # Create and register a dummy FX rate service:
    import pytest
    from .mocks import MockFXRateService
    from .currencies import Currency

    FXRateService.default = MockFXRateService()

    assert isinstance(FXRateService.default, MockFXRateService)
    assert FXRateService.default is not None

    # Test the foreign exchange rate query method with strict and non-strict mode:

# Generated at 2022-06-14 04:38:27.687038
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """
    ccy1 ="USD"
    ccy2 ="EUR"
    asof ="2018-01-01"
    strict = "False"

    ### Produce error by calling abstract method query
    with pytest.raises(TypeError):
        FXRateService().query(ccy1,ccy2,asof,strict)


# Generated at 2022-06-14 04:38:37.170939
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance import FXRate, FXRateService

    class FXRateServiceImpl(FXRateService):

        def query(self, ccy1, ccy2, asof, strict = False):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate.of(ccy1, ccy2, asof, Decimal("2"))
            else:
                return None

        def queries(self, queries, strict = False):
            for query in queries:
                yield self.query(query[0], query[1], query[2], strict)

    service = FXRateServiceImpl()

# Generated at 2022-06-14 04:38:47.262731
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService
    class TestRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False):
            if ccy1 == ccy2:
                return None
            return FXRate(ccy1, ccy2, datetime.date(year=2020,month=2,day=3), Decimal(2))
    from pypara.fxrates import FXRateService
    FXRateService.default = TestRateService()

    result = FXRateService.default.query(Currencies["EUR"], Currencies["EUR"], datetime.date(year=2020,month=2,day=3))

# Generated at 2022-06-14 04:38:59.750469
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from functools import partial
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.fxrates import FXRate, FXRateLookupError, FXRateService
    ## A simple implementation:
    class SimpleFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if Currency(ccy1) != Currency(ccy2):
                return FXRate(ccy1, ccy2, asof, Decimal(1.2))
            return FXRate(ccy1, ccy2, asof, Decimal(1))

# Generated at 2022-06-14 04:39:12.620859
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService
    from pypara.temporal import Temporal

    class LocalFXRateService(FXRateService):
        @staticmethod
        def query(ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == Temporal.today():
                return FXRate(Currencies["EUR"], Currencies["USD"], asof, Decimal("2"))
            return None

    service = LocalFXRateService()
    rate = service.query(Currencies["EUR"], Currencies["USD"], Temporal.today())

# Generated at 2022-06-14 04:39:22.170804
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    :return: A list of error messages.
    """
    from datetime import date
    from decimal import Decimal
    from unittest import TestCase
    from pypara.currencies import Currency
    from pypara.currencies import Currencies as C
    from pypara.commons.zeitgeist import Temporal

    ## Dummy FX rate service:
    class DummyFXRateService(FXRateService):
        def __init__(self):
            self.rates = [
                (C.EUR, C.USD, date(2017, 12, 29), Decimal("2")),
                (C.USD, C.EUR, date(2017, 12, 29), Decimal("0.5"))
            ]


# Generated at 2022-06-14 04:39:28.421320
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .fxtopics import HistoricalFXRates
    from .zeitgeist import Date
    from .commons.numbers import Decimal
    from decimal import Decimal
    import datetime
    queries = [
        (Currencies["USD"], Currencies["EUR"], Date(datetime.date(2019, 1, 1))),
        (Currencies["USD"], Currencies["EUR"], Date(datetime.date(2019, 12, 31))),
    ]
    rates = [r for r in HistoricalFXRates().queries(queries)]
    assert len(rates) == 2
    assert rates[0] == FXRate(Currencies["USD"], Currencies["EUR"], Date(datetime.date(2019, 1, 1)), Decimal("0.90"))
    assert rates[1] == FXRate

# Generated at 2022-06-14 04:39:29.612854
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass


# Generated at 2022-06-14 04:39:51.841518
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .temporal import Date
    from .currencies import Currencies
    from .markets.fx import FXSpotRateService
    import datetime
    service = FXSpotRateService()
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["EUR"]
    date = Date(datetime.date.today())
    queries = [(ccy1, ccy2, date)]
    results = service.queries(queries)
    rate = next(results)
    assert rate is not None

# Generated at 2022-06-14 04:40:03.600719
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .commons import Dates
    from .commons.numbers import DecimalTuple
    from .fxrates import FXRateServiceStub

    ## Build queries
    euro = Currencies['EUR']
    dollar = Currencies['USD']
    queries = [(euro, dollar, Dates.today("2018-01-01")),
               (dollar, euro, Dates.today("2018-01-01")),
               (dollar, dollar, Dates.today("2018-01-01"))]
    stub = FXRateServiceStub()

    ## Make a query:
    rates = stub.queries(queries, True)
    assert isinstance(rates, Iterable)
    assert all(rate is not None for rate in rates)

    ## Verify data:
    rates = DecimalTuple(*rates)
    assert rates

# Generated at 2022-06-14 04:40:15.936969
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Test for method query of class FXRateService
    """
    from unittest.mock import Mock
    from .currencies import Currency, Currencies
    from .rates import Rate, RateService
    from .temporals import date
    from .values import Value
    from . import rates
    from . import temporals
    from . import values

    ccy1: Currency = Currencies["USD"]
    ccy2: Currency = Currencies["EUR"]
    today: Date = date.date()

    fxrate: FXRate = FXRate(ccy1, ccy2, today, Decimal("0.5"))


# Generated at 2022-06-14 04:40:27.606309
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:40:36.967339
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the functionality provided by method queries of class FXRateService.
    """

    from .currencies import CCY1, CCY2, Currency
    from .currencies import Currencies
    from .temporals import Temporals
    from decimal import Decimal
    from unittest import TestCase, mock
    from unittest.mock import MagicMock

    ## Define the query tuple:
    TQuery = Tuple[Currency, Currency, Temporals.TTemporal]

    ## Define a foreign exchange rate:
    FXRATE = FXRate(CCY1, CCY2, Temporals.DATE, Decimal("2"))

    ## Define a strict and non-strict lookup:
    LOOKUP_STRICT = TQuery(CCY1, CCY2, Temporals.DATE)
    LOOK

# Generated at 2022-06-14 04:40:38.009816
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:40:47.096468
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.currencies import Currency
    from pypara.fxrates import FXRateLookupError as FXRateLookupError, FXRateService
    from pypara.temporal import Temporal

    # Define a query function:
    def query(ccy1: Currency, ccy2: Currency, asof: Temporal) -> Optional[Decimal]:
        if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
            if asof == datetime.date(2019, 4, 1):
                return Decimal("1.15")
            elif asof == datetime.date(2019, 4, 8):
                return Decimal("1.16")

# Generated at 2022-06-14 04:40:56.556982
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.utils.cache import Cache
    from pypara.fx.mocks import DummyFXRateService
    from pypara.currencies import Currencies  # noqa: F401
    from pypara.commons.zeitgeist import Date, Temporal  # noqa: F401

    svc = DummyFXRateService()

    # Service should not be cached:
    assert not isinstance(svc, Cache)

    # All queries should be satisfied:

# Generated at 2022-06-14 04:41:05.990283
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currency
    from pypara.fx.in_memory import InMemoryFXRateService
    from pypara.fx.utils import build_fx_dates
    from pypara.temporal import Temporal

    ## Create the service and the data:
    service = InMemoryFXRateService()
    rates = [
        FXRate(Currency("EUR"), Currency("USD"), Temporal.of_date(date), Decimal("1.23"))
        for date in build_fx_dates(Date(1, 1, 1900), Date(1, 1, 2000), 365)]

    ## Add the data to the service:
    for rate in rates:
        service.add(rate)

    ## Perform some queries:
    for rate in rates:
        assert service.query(rate[0], rate[1], rate[2])

# Generated at 2022-06-14 04:41:17.843094
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.mktdata.fx.services import DummyFXRateService

    service = DummyFXRateService()

    # Test with a valid ccy1, ccy2 and asof
    value = service.query(Currencies["USD"], Currencies["EUR"], datetime.date.today(), strict=False)

    # Verify the type of value
    assert type(value) is FXRate

    # Verify the value of value
    assert value == FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("2"))

    # Test with a invalid ccy1, ccy2 and asof

# Generated at 2022-06-14 04:41:59.102918
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:42:09.992821
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    # Import libraries:
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx.fx_rates import FXRate, FXRateService

    # Create an FX rate lookup service:

# Generated at 2022-06-14 04:42:22.323829
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.exchange import FXRateService

    ## Define a simple rate lookup:
    rates = {
        (Currencies["EUR"], Currencies["USD"], datetime.date(2019, 1, 1)): Decimal(1.214),
        (Currencies["EUR"], Currencies["USD"], datetime.date(2019, 1, 2)): Decimal(1.215),
        (Currencies["EUR"], Currencies["USD"], datetime.date(2019, 1, 3)): Decimal(1.214),
        (Currencies["EUR"], Currencies["USD"], datetime.date(2019, 1, 4)): Decimal(1.214),
    }

    ## Define a simple rate query service:
   

# Generated at 2022-06-14 04:42:23.962390
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:42:24.588742
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass

# Generated at 2022-06-14 04:42:32.806866
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    ## Create a query set:
    queries = [(Currencies["EUR"], Currencies["USD"], datetime.date(2017, 1, 1)),
               (Currencies["EUR"], Currencies["USD"], datetime.date(2017, 2, 1))]

    ## Create the FX rate service:
    class FXRateServiceMock(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            ## Check the date:
            if asof == datetime.date(2017, 1, 1):
                return FXRate(ccy1, ccy2, asof, Decimal("1.1"))
            elif asof == datetime.date(2017, 2, 1):
                return FXRate

# Generated at 2022-06-14 04:42:43.445172
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """

    from datetime import date
    from fractions import Fraction
    from .currencies import Currency, CurrencyPair
    from .services.cache import CacheMeta

    #
    # Defines a test foreign exchange rates service that finds rates in a given dictionary:
    #
    class TestFXRateService(FXRateService, metaclass=CacheMeta):
        """
        Defines a test foreign exchange rates service that finds rates in a given dictionary.
        """

        def __init__(self, rates: dict) -> None:
            """
            Initializes the FX rate provider dictionary.
            """
            self.rates = rates


# Generated at 2022-06-14 04:42:49.978594
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.currencies import Currency
    from pypara.currencies.converters import FXRateServiceConverter
    from pypara.fx import FXRateService, FXRate
    from pypara.temporal import Date

    class Mock(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            pass
        def queries(self, queries, strict=False):
            return iter(map(lambda x: FXRate(ccy1=x[0], ccy2=x[1], date=x[2], value=1), queries))

    ## Create a date and a mock:
    date = Date(2020, 1, 1)
    mock = Mock()
    converter = FXRateServiceConverter(mock)

    ## Run and assert:

# Generated at 2022-06-14 04:42:56.017913
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from unittest.mock import Mock, MagicMock

    from unittest import TestCase

    from .currencies.fxrateservice import FXRateServiceMemory

    class MockFXRateService(FXRateServiceMemory):
        def query(self, ccy1, ccy2, asof, strict=False):
            return self.lookup[(ccy1, ccy2, asof)]


# Generated at 2022-06-14 04:43:00.080966
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class FXRateServiceImpl(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date(2019, 1, 1):
                return FXRate.of(Currencies["EUR"], Currencies["USD"], asof, Decimal("1.1"))

# Generated at 2022-06-14 04:44:23.634061
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Verify that the queries method of the FXRateService class works as expected.
    """

    from .currencies import Currencies
    from .dates import Temporal
    from .fx import FXRateServiceImpl

    class FXRateServiceStub(FXRateServiceImpl):

        def query(self, ccy1, ccy2, asof, strict=False):
            if (ccy1, ccy2, asof) in [
                (Currencies["USD"], Currencies["EUR"], Temporal(2020, 1, 1)),
                (Currencies["USD"], Currencies["EUR"], Temporal(2020, 1, 2)),
            ]:
                return None
            return None

    ## Verify that we get the expected None results: