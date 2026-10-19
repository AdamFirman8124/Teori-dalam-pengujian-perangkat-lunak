

# Generated at 2022-06-14 04:34:38.920841
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .commons.numbers import ONE
    from .commons.zeitgeist import today
    from .currencies import Currencies

    class DemoFXRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == today():
                return FXRate(Currencies["EUR"], Currencies["USD"], asof, ONE)
            return None

        def queries(self, queries, strict=False):
            for query in queries:
                yield self.query(*query, strict=strict)

    from decimal import Decimal

    fx = DemoFXRateService()
    rate = fx.query(Currencies["EUR"], Currencies["USD"], today())

# Generated at 2022-06-14 04:34:48.861695
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.datasources.fx import FXRateService as DummyFXRateService, FXRateLookupError
    from pypara.currencies import Currencies

    ## Create the dummy FX rate service:
    service = DummyFXRateService()

    ## Query the service:
    assert service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) == FXRate(
        Currencies["EUR"],
        Currencies["USD"],
        datetime.date.today(),
        Decimal(1) / Decimal(1.14),
    )

# Generated at 2022-06-14 04:34:50.680604
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    :return:
    """
    ## OK:
    assert True

# Generated at 2022-06-14 04:35:00.501548
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Test method query of class FXRateService
    """
    import datetime
    from pypara.currencies import Currency
    from pypara.finance.fx import FXRateService

    class FXRateService(FXRateService):
        """
        Provides a stub implementation of FXRateService
        """

        def __init__(self):
            super().__init__()
            self.rate_dict = {}

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self.rate_dict.get((ccy1, ccy2, asof))


# Generated at 2022-06-14 04:35:01.996051
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """
    pass



# Generated at 2022-06-14 04:35:10.136600
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # pylint: disable=W0212
    from unittest.mock import patch, Mock
    from collections import namedtuple

    from pypara.currencies import Currencies
    from pypara.datetime import Dates
    from pypara.exchange.fx.services import FXRateService, FXRateLookupError

    with patch.multiple(
        FXRateService,
        name="FXRateService",
        spec=True,
        abstractmethods=list(),
        autospec=True
    ) as mock:
        service = mock["name"]
        # pylint: disable=W0706

# Generated at 2022-06-14 04:35:19.472376
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    This is a unit test for method :method:`FXRateService.queries`.
    """

    ## Needed imports:
    from .currencies import Currency, Currencies
    from .temporal import Date, Temporal

    ## Create the FX rate service:
    class MockFXRateService(FXRateService):
        def __init__(self) -> None:
            #: Defines the FX rate dictionary.
            self.__rates = {
                (Currencies["USD"], Currencies["EUR"], Date(2000, 1, 1)): Decimal("0.5")
            }

        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[Decimal]:
            query = (ccy1, ccy2, Date.of(asof))

# Generated at 2022-06-14 04:35:31.414159
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class Service(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal(2)) if ccy1 == ccy2 else None

        def queries(self, queries, strict=False):
            return (self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries)

    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
    asof = datetime.date.today()
    svc = Service()

# Generated at 2022-06-14 04:35:33.514774
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:35:34.709029
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:35:41.127293
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # type: () -> None
    """
    Tests method query of class FXRateService.
    """
    pass



# Generated at 2022-06-14 04:35:51.897598
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    import pytest

    from pypara.currencies import Currencies
    from pypara.curves import FXRateService


# Generated at 2022-06-14 04:36:03.809991
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Executes unit tests on method query of class FXRateService.

    :return: True if all tests passed
    :rtype: bool
    """
    ## Test query method:
    import datetime
    from decimal import Decimal
    from pypara.fx import FXRateService
    from pypara.currencies import Currencies

    ## Create a dummy rate provider:
    class Provider(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 != Currencies["USD"] or ccy2 != Currencies["EUR"] or asof != datetime.date.today():
                return None
            return FXRate(ccy1, ccy2, asof, Decimal("2"))


# Generated at 2022-06-14 04:36:16.736035
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .storages import FXRateInMemoryStorage
    from .temporals import asdate, today

    # Setup the storage:
    storage = FXRateInMemoryStorage()
    storage.add(Currencies["EUR"], Currencies["USD"], today(), Decimal("2"))

    # Setup the service:
    service = storage.service()

    # Query the FX rate:
    rate = service.query(Currencies["EUR"], Currencies["USD"], today())
    assert rate is not None
    assert FXRate(Currencies["EUR"], Currencies["USD"], today(), Decimal("2")) == rate
    assert rate.ccy1 == Currencies["EUR"]
    assert rate.ccy2 == Currencies["USD"]
    assert rate.date == today()

# Generated at 2022-06-14 04:36:22.749212
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currencies
    fxrate = FXRateService.default.query(Currencies["USD"], Currencies["TRY"], date.today(), strict=True)
    assert fxrate.value > Decimal("0")

# Generated at 2022-06-14 04:36:33.872399
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .exchanges.rates import _FXRateServiceStatic

    ## Try to get a rate for an unexpected currency pair as of an unexpected date:
    with (_FXRateServiceStatic(), Currencies["HUF"], Currencies["YEN"], Date(2018, 6, 30)) as (service, ccy1, ccy2, asof):
        rate = service.query(ccy1, ccy2, asof)
        assert rate is None

    ## Try to get a rate for a supported currency pair as of an unexpected date:
    with (_FXRateServiceStatic(), Currencies["EUR"], Currencies["USD"], Date(2018, 6, 30)) as (service, ccy1, ccy2, asof):
        rate = service.query(ccy1, ccy2, asof)
        assert rate is None

   

# Generated at 2022-06-14 04:36:45.069351
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from .exchanges.memory import FXMemoryExchange

    ## Create a memory exchange:
    exchange = FXMemoryExchange()

    ## Create a foreign exchange rate:
    rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

    ## Check that the memory exchange is empty:
    assert exchange.query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) is None

    ## Save the foreign exchange rate to the memory exchange:
    exchange.save(rate)

    ## Check that the memory exchange contains the saved item:
    assert rate == exchange.query(Currencies["EUR"], Currencies["USD"], datetime.date.today())



# Generated at 2022-06-14 04:36:53.877881
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests query method of FX rate service.

    :return: ``None``
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.rates.redis import RedisFXRateService

    ## Clone the Redis client:
    rdsp = RedisFXRateService()

    ## Push a rate:
    rdsp.put(FXRate(Currencies["EUR"], Currencies["USD"], datetime.date(2017, 1, 1), Decimal("1.5")))

    ## Query a rate:
    rate = rdsp.query(Currencies["EUR"], Currencies["USD"], datetime.date(2017, 1, 1))
    if rate is None:
        raise AssertionError("FX rate for EUR/USD must exist.")

# Generated at 2022-06-14 04:37:02.207246
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    import pytest

    ## Initialize the fixture:
    class CustomFXRateService(FXRateService):
        def __init__(self):
            self._rate = FXRate(Currencies["EUR"], Currencies["USD"], date(2019, 1, 1), Decimal("1.2"))

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self._rate if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == date(2019, 1, 1) else None


# Generated at 2022-06-14 04:37:15.149228
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.finance.fxrates import FXRateService

    class MockFXRateService(FXRateService):
        def __init__(self):
            self.rates = []

        def add_rates(self, ccy1: Currency, ccy2: Currency, date: date, value: Decimal) -> None:
            self.rates.append((ccy1, ccy2, date, value))

        def query(self, ccy1: Currency, ccy2: Currency, asof: date, strict: bool = False) -> Optional[FXRate]:
            for c, d, v in self.rates:
                if c == ccy1 and d == ccy2 and v == asof:
                    return v
            return None



# Generated at 2022-06-14 04:37:33.827249
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    ## import built-in modules:
    import contextlib
    from datetime import date, timedelta
    from decimal import Decimal
    from io import StringIO

    ## import third-party modules:
    from pytest import raises

    ## import pypara modules:
    from .commons import Temporal
    from .currencies import Currency
    from .exchange import FXRateService
    from .exchange.fx import FXRate

    ## Note that we use `Currency` class instead of `Currencies` mapping:
    ccy1 = Currency("EUR")
    ccy2 = Currency("USD")
    temporal = Temporal(date.today() - timedelta(days=1), date.today())

    ## Create a mock query service:

# Generated at 2022-06-14 04:37:47.176887
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # Given a foreign exchange rate service
    class MockFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict):
            return FXRate(ccy1, ccy2, asof, Decimal(1.1))

        def queries(self, queries, strict):
            return FxRateService.queries(queries, strict)

    service = MockFXRateService()

    # When
    #    I query for foreign exchange rates for a given collection of currency pairs and dates
    import datetime
    from pypara.currencies import Currencies

# Generated at 2022-06-14 04:37:57.365161
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import DateRange
    from .fxrates import ListFXRateService
    from pypara.commons.numbers import ZERO

    # A list of currencies to work with:
    CCYS = [ccy for ccy in Currencies.values() if ccy.code != "XTS" and ccy != Currencies["XXX"]]

    # A list of exchange rates to work with:
    FXS = []
    for i in range(0, 10):
        date = DateRange.now(minus_days=i)
        for ccy in CCYS:
            FXS.append(FXRate.of(ccy, Currencies["USD"], date, ONE))
            FXS.append(FXRate.of(Currencies["USD"], ccy, date, ONE))

    # Create the exchange rate

# Generated at 2022-06-14 04:38:08.841929
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx.services import FixedFXRateService
    from pypara.persistence import get_temporal_key    

    # Create the FX rate service.
    fx_rate_service = FixedFXRateService({"EURUSD": {"2020-06-17": Decimal(1.1), "2020-06-18": Decimal(1.2)}},
                                         None)

    # Test the queries.
    query_1 = (Currencies["EUR"], Currencies["USD"], datetime.date(2020, 6, 17))
    query_2 = (Currencies["EUR"], Currencies["USD"], datetime.date(2020, 6, 18))

# Generated at 2022-06-14 04:38:21.708062
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService
    """
    # Create FXRateService
    import unittest.mock
    mock_FXRateService = unittest.mock.MagicMock(spec=FXRateService)

    # Create arguments
    mock_ccy1 = unittest.mock.MagicMock(spec=Currency)
    mock_ccy2 = unittest.mock.MagicMock(spec=Currency)
    mock_asof = unittest.mock.MagicMock(spec=Date)
    mock_strict = None

    # Call method
    result = mock_FXRateService.query(mock_ccy1, mock_ccy2, mock_asof, mock_strict)

    # Check method call
    mock_FXRateService.query.assert_called_

# Generated at 2022-06-14 04:38:32.506701
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies
    from pypara.util.date import today
    from pypara.util.fx import FXRate, FXRateService

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["USD"]:
                if ccy2 == Currencies["USD"]:
                    return FXRate.of(Currencies["USD"], Currencies["USD"], asof, Decimal("1"))
                elif ccy2 == Currencies["EUR"]:
                    return FXRate.of(Currencies["USD"], Currencies["EUR"], asof, Decimal("2"))

            return None

    usd

# Generated at 2022-06-14 04:38:33.094221
# Unit test for method query of class FXRateService
def test_FXRateService_query():
   pass

# Generated at 2022-06-14 04:38:45.027624
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Today

    class TestService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate.of(ccy1, ccy2, asof.date, Decimal("1.5"))

        def queries(self, queries, strict=False):
            return (self.query(q[0],q[1],q[2]) for q in queries)


# Generated at 2022-06-14 04:38:51.441983
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests :method:`FXRateService.query` method.
    """
    import datetime

    from decimal import Decimal
    from .currencies import Currencies

    ## Create a test foreign exchange rate service:
    class TestFXRateService(FXRateService):
        """
        Provides a test class for :class:`FXRateService`.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            ## Base case:
            if ccy1 is None or ccy2 is None or asof is None:
                return None

            ## The foreign exchange rate:
            rate: Optional[FXRate] = None

            ## Test for

# Generated at 2022-06-14 04:39:01.462277
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.fx_rates import FXRate, FXRateService
    class TestService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate.of(ccy1, ccy2, asof, ONE)

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (FXRate.of(ccy1, ccy2, asof, ONE) for ccy1, ccy2, asof in queries)

    s = TestService()

# Generated at 2022-06-14 04:39:25.354626
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of the FXRateService Abstract Base Class.
    """
    from .currencies import Currencies
    from .exchanges import ExchangeRateService
    
    ## Prepare the queries and assert the results are the same for both method 
    ## implementations:

# Generated at 2022-06-14 04:39:36.414774
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    import datetime
    import unittest
    from decimal import Decimal
    from pypara.currencies import Currencies

    class MockFXRateService(FXRateService):

        def __init__(self) -> None:
            self.query_calls = []

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            self.query_calls.append((ccy1, ccy2, asof))
            return FXRate.of("EUR", "USD", asof=datetime.date(2020, 1, 1), value=Decimal("1.0001"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            fx_rates = []
           

# Generated at 2022-06-14 04:39:45.134982
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests that :method:`FXRateService.queries` function properly.
    """
    # Create a query and a dummy service:
    from .currencies import Currencies
    from .commons.zeitgeist import Date

# Generated at 2022-06-14 04:39:54.138423
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    date = datetime.date.today()
    ccy1, ccy2 = Currencies["EUR"], Currencies["USD"]
    rate = FXRate.of(ccy1, ccy2, date, Decimal("2"))

    class FXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return rate

    svc = FXRateService()

    assert rate is svc.query(ccy1, ccy2, date)


# Generated at 2022-06-14 04:40:05.355406
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies
    from pypara.time import Date, Temporals

    # First we need a pipe line of queries
    queries = ((Currencies["EUR"], Currencies["USD"], Temporals["2019-08-01"]),
               (Currencies["EUR"], Currencies["USD"], Temporals["2019-08-02"]))

    # Now we create a mock object for it
    from unittest import mock
    rates = iter((FXRate(Currencies["EUR"], Currencies["USD"], Temporals["2019-08-01"], Decimal("1.5")),
                  FXRate(Currencies["EUR"], Currencies["USD"], Temporals["2019-08-02"], Decimal("2.5"))))
    mock_service = mock.Mock()

# Generated at 2022-06-14 04:40:18.403666
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.fx.services import FXRateService
    from pypara.currencies import Currencies
    from pypara.primitives import Temporal

    from datetime import date

    class SUT(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=True):
            return 1.0

        def queries(self, queries, strict=True):
            yield None


# Generated at 2022-06-14 04:40:28.800759
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency, Currencies
    from .commons.zeitgeist import Date
    from .fxrates import FXRateService

    class _F:
        """
        Defines a dummy foreign exchange service.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False):
            return FXRate(ccy1, ccy2, asof, Decimal("1.0"))

    f = _F()
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["EUR"]
    asof = Date.today()
    rate = f.query(ccy1, ccy2, asof)
    assert rate.ccy1 == ccy1
    assert rate.ccy2 == ccy2
    assert rate.date == asof

# Generated at 2022-06-14 04:40:38.004595
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Test method query of class FXRateService.
    """
    # This part is for test; do not delete:
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currency, Currencies

    class TestFXRateService(FXRateService):
        """
        Test service to serve foreign exchange rates.
        """

        #: Defines the supported currency pairs.

# Generated at 2022-06-14 04:40:49.586486
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies

    rusd = FXRate(Currencies["USD"], Currencies["RUB"], date(2016, 12, 31), Decimal("66.1913"))
    rate = FXRateService.default.query(Currencies["USD"], Currencies["RUB"], date(2016, 12, 31))
    assert rate == rusd

    eur = FXRate(Currencies["EUR"], Currencies["EUR"], date(2016, 12, 31), Decimal("1"))
    rate = FXRateService.default.query(Currencies["EUR"], Currencies["EUR"], date(2016, 12, 31))
    assert rate == eur


# Generated at 2022-06-14 04:40:57.839849
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.fxrates import FXRateService, FXRateLookupError
    from pypara.temporals import Temporal

    class TestService(FXRateService):
        def __init__(self):
            self.rates = [
                FXRate(Currency("EUR"), Currency("USD"), Temporal(datetime.date(2020, 1, 1)), Decimal("1.23")),
                FXRate(Currency("EUR"), Currency("USD"), Temporal(datetime.date(2020, 1, 2)), Decimal("1.24"))
            ]


# Generated at 2022-06-14 04:41:49.674037
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:41:50.725871
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:41:59.846429
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Demonstrates the usage of :method:`FXRateService.queries` method.

    >>> from decimal import Decimal
    >>> from pypara.currencies import Currencies
    >>> from pypara.services.fx.services import FXRateService
    >>> fxrate_service = FXRateService()
    >>> fxrate_service.queries([
    ...     (Currencies["EUR"], Currencies["USD"], date(2015, 1, 1)),
    ...     (Currencies["USD"], Currencies["EUR"], date(2015, 1, 1)),
    ...     (Currencies["USD"], Currencies["EUR"], date(2015, 2, 1)),
    ... ])
    [None, None, None]
    """



# Generated at 2022-06-14 04:42:00.924960
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:42:10.521623
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    # Define a mock FX rate service
    class MockFXRateService(FXRateService):

        # Query
        def query(self, ccy1, ccy2, asof, strict = False):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today() :
                return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

            return None

        # Queries
        def queries(self, queries, strict = False):
            return [self.query(ccy1, ccy2, asof, strict) for (ccy1,ccy2,asof) in queries]

    # Define

# Generated at 2022-06-14 04:42:22.909047
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    This unit test tests :method:`FXRateService.queries` method of :class:`FXRateService`.
    """
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currencies

    # Define the base FX rate service:
    class BaseFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # If we are not strict, return None:
            if not strict:
                return None

            # Otherwise, raise a lookup error:
            raise FXRateLookupError(ccy1, ccy2, asof)


# Generated at 2022-06-14 04:42:31.703978
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, 1)

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return super().queries(queries)

    import pytest
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currency, Currencies

    service = TestFXRateService()

    with pytest.raises(TypeError):
        next(service.queries([(Currencies["EUR"], Currencies["USD"], date.today(), 1)]))


# Generated at 2022-06-14 04:42:37.586889
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    class Dummy(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> FXRate:
            return FXRate.of(ccy1, ccy2, asof, Decimal(str(asof.year)))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return list(map(lambda q: self.query(q[0], q[1], q[2]), queries))

    import datetime
    from pypara.currencies import Currencies

    s = Dummy()
    t = datetime.date.today()

# Generated at 2022-06-14 04:42:49.740294
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103
    from .currencies import Currencies
    from .temporal.date_time import DateTime
    from .temporal.date_vector import DateVector

    # Create the FX rate service:
    class TestRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == DateTime("2020-12-31").date:
                return FXRate(ccy1, ccy2, asof, Decimal("2"))

# Generated at 2022-06-14 04:43:02.736797
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest import TestCase, main
    from pypara.currencies import Currencies
    from pypara.temporals import Date
    import sys

    class Test(TestCase):
        def test(self):
            class Dummy(FXRateService):
                def query(dummy, ccy1, ccy2, asof, strict):
                    queries.append((ccy1, ccy2, asof))
                    return None

                def queries(dummy, queries, strict):
                    return iter(queries)

            ## The target to test:
            target = Dummy()

            ## An empty collection:
            queries = []
            self.assertListEqual(list(target.queries(queries)), [])

            ## An iterator with items: