

# Generated at 2022-06-14 04:34:37.179881
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies

    import datetime
    from decimal import Decimal

    class LocalFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
            else:
                return None

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for (ccy1, ccy2, asof) in queries:
                yield self

# Generated at 2022-06-14 04:34:48.081592
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.forex import FXRateService

    ## Create a test FX rate service:
    class TestFXRateService(FXRateService):
        @staticmethod
        def query(ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            import datetime
            from decimal import Decimal
            from pypara.forex import FXRate
            from pypara.currencies import Currencies

            if ccy1 is Currencies["EUR"] and ccy2 is Currencies["USD"] and asof is datetime.date.today():
                return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

            return

# Generated at 2022-06-14 04:34:59.532681
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class FXRateServiceStub(FXRateService):
        def __init__(self, rates: FXRate):
            self.rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self.rates

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return iter(self.rates)

    r = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    s = FXRateServiceStub(r)

# Generated at 2022-06-14 04:35:11.138779
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService
    class FXRateServiceStub(FXRateService):
        def query(self, ccy1, ccy2, asof):
            return None
        def queries(self, queries, strict=False):
            for query in queries:
                yield self.query(*query, strict=strict)
    fx_service = FXRateServiceStub()
    result = fx_service.queries([(Currencies["EUR"], Currencies["USD"], datetime.date.today())])
    for actual, expected in zip(result, [None]):
        assert actual == expected

# Generated at 2022-06-14 04:35:21.671791
# Unit test for method query of class FXRateService
def test_FXRateService_query(): # pragma: no cover
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    # Create fx rate service:
    class MyService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            if (ccy1, ccy2, asof) in self.rates:
                return self.rates[(ccy1, ccy2, asof)]
            elif not strict:
                return None
            else:
                raise FXRateLookupError(ccy1, ccy2, asof)

        def queries(self, queries, strict=False):
            return map(lambda q: self.query(*q, strict=strict), queries)

    # Create service and provide with some rates:
    service = MyService()
    service

# Generated at 2022-06-14 04:35:30.583681
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

    class FXRateServiceMock(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return rate

    assert FXRateServiceMock().query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) == rate


# Generated at 2022-06-14 04:35:38.838496
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:35:50.750711
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    class DummyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1.2"))

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            raise NotImplementedError()

    import datetime as dt


# Generated at 2022-06-14 04:35:56.842789
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Make sure that the queries of class FXRateService works as expected.
    """
    from .currencies import Currencies
    from .dates import Temporals
    from .exchanges import LocalDateTime
    from decimal import Decimal
    from typing import List
    from unittest import TestCase

    class QueryService(FXRateService):
        """
        Provides a test FX rate service implementation.
        """

        #
        # Private constants:
        #

# Generated at 2022-06-14 04:36:06.420071
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    This module provides definitions and functionality related to foreign-exchange conversions.
    """

    # Imports:
    from datetime import date
    from decimal import Decimal
    from unittest import TestCase
    from pypara.currencies import Currency, Currencies
    from pypara.fx import FXRate, FXRateService
    from pypara.temporal import Date

    # Create a mock service class:
    class MockFXRateService(FXRateService):
        """
        Provides a mock FX rate service implementation.
        """


# Generated at 2022-06-14 04:36:11.487984
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:36:24.903808
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:36:38.342884
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import InMemoryFXRateService
    from pypara.zeitgeist import Date

    ## Create the service:
    service = InMemoryFXRateService({
        # Source: https://www.x-rates.com/calculator/?from=EUR&to=USD&amount=1
        FXRate(Currencies["EUR"], Currencies["USD"], Date(2019,1,1), Decimal("1.1381"))
    })

    ## Fetch the foreign exchange rate:
    fx = service.query(Currencies["EUR"], Currencies["USD"], Date(2019,1,1))

    ## Check the result:
    assert fx
    assert fx.ccy1 == Currencies["EUR"]

# Generated at 2022-06-14 04:36:48.490564
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.currencies import Currencies
    from pypara.date import Date as Temporal
    from pypara.fxrates.memory import FXRateMemory
    from pypara.fxrates.historic import FXRateHistoric

    ## Setup the test:
    ccy1 = Currencies["EUR"]
    ccy2 = ccy3 = ccy4 = ccy5 = ccy6 = ccy7 = ccy8 = ccy9 = ccy10 = Currencies["USD"]
    temporal1 = Temporal.of(2017, 1, 1)
    temporal2 = Temporal.of(2017, 1, 2)
    temporal3 = Temporal.of(2017, 1, 3)
    temporal4 = Temporal.of(2017, 1, 4)

    ## Test a service with a single source:
    source = FXRateMemory

# Generated at 2022-06-14 04:36:59.150495
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the :method:`FXRateService.query` method
    """
    from random import random
    from unittest import TestCase
    from .commons.containers import Pipelined

    ## We want to test a pipelined FX rate service:
    class FXRateServiceDummy(FXRateService):
        def __init__(self, *rates: FXRate) -> None:
            self.__rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> FXRate:
            for rate in self.__rates:
                if ccy1 == rate.ccy1 and ccy2 == rate.ccy2 and asof == rate.date:
                    return rate


# Generated at 2022-06-14 04:37:12.882387
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    class DummyRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            return None

        def queries(self, queries, strict=False):
            for query in queries:
                for ccy in query:
                    if ccy == Currency.NONE:
                        yield None
                        break
                else:
                    yield FXRate(query[0], query[1], query[2], Decimal("1"))

    ## Create a dummy FX rate service:
    service = DummyRateService()

    ## Define some FX rate queries:

# Generated at 2022-06-14 04:37:14.993530
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the FXRateService.query method.
    """
    pass

# Generated at 2022-06-14 04:37:28.575710
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date

    from currency_settings import CurrencySettings

    from .commons.enums import Temporals
    from .commons.temporals import Temporal

    from .currencies.currency import Currency
    from .currencies.cached_service import CachedFXRateService
    from .currencies.fixed_service import FixedFXRateService

    """
    >>> import time
    >>> start = time.time()
    """

    ## Create a foreign exchange rate service:

# Generated at 2022-06-14 04:37:35.597811
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .commons.zeitgeist import Dates
    from pypara.currencies.conversions import FXConversionService
    from pypara.fxrates.services import FXRateService

    service = FXConversionService(FXRateService.default)
    assert service.query(Currencies["EUR"], Currencies["USD"], Dates.today()) == Decimal('1.17')

    service = FXConversionService(None)
    assert service.query(Currencies["TRY"], Currencies["USD"], Dates.today()) is None

# Generated at 2022-06-14 04:37:48.033228
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    import datetime
    from decimal import Decimal
    from unittest.mock import patch
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    class Service(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            pass

        def queries(self, queries, strict=False):
            pass

    with patch.object(Service, "query", return_value=None) as query:
        service = Service()
        assert service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today(), strict=True) is None
        query.assert_called_with(Currencies["EUR"], Currencies["USD"], datetime.date.today(), strict=True)


# Generated at 2022-06-14 04:38:07.566700
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests :method:`~test_FXRateService.queries` of class :class:`~test_FXRateService`.
    """
    ##
    from decimal import Decimal
    import datetime
    from pypara.currencies import Currencies

    ##
    from .commons.zeitgeist import Date

    ##
    class EmptyFXRateService(FXRateService):
        """
        Provides a simple implementation of an empty foreign exchange rate service.
        """

        def __init__(self):
            """
            Initializes the empty foreign exchange rate service.
            """
            pass


# Generated at 2022-06-14 04:38:20.947112
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Runs unit test for method queries of class FXRateService.
    """
    from pypara.currencies import Currencies
    from pypara.temporal import Temporal

    queries = [
        (Currencies["TRY"], Currencies["USD"], Temporal.of(2018, 1, 1)),
        (Currencies["TRY"], Currencies["USD"], Temporal.of(2018, 1, 1)),
        (Currencies["CAD"], Currencies["USD"], Temporal.of(2018, 1, 1)),
        (Currencies["CAD"], Currencies["USD"], Temporal.of(2018, 1, 1)),
        (Currencies["TRY"], Currencies["USD"], Temporal.of(2018, 1, 1)),
        (Currencies["TRY"], Currencies["USD"], Temporal.of(2018, 1, 1)),
    ]

   

# Generated at 2022-06-14 04:38:31.942114
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    import pytest
    from decimal import Decimal

    from pypara.commons.numbers import ZERO
    from pypara.currencies import Currency, Currencies
    from pypara.core.temporal import Date

    curr_service = FXRateService()

    ## Test 1:

# Generated at 2022-06-14 04:38:44.165257
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime 
    from decimal import Decimal
    from pypara.currencies import Currencies
    ddate = datetime.date.today()
    oo = currency=Currencies["USD"], currency=Currencies["USD"], date=ddate
    oe = currency=Currencies["USD"], currency=Currencies["EUR"], date=ddate
    eo = currency=Currencies["EUR"], currency=Currencies["USD"], date=ddate
    ee = currency=Currencies["EUR"], currency=Currencies["EUR"], date=ddate
    #queries = [oo, oe, eo, ee]
    queries = [oo, oe]
    results = [decimal.Decimal("1"), decimal.Decimal("2")]
    for query, result in zip(queries, results):
        assert query

# Generated at 2022-06-14 04:38:45.655877
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class :class:`FXRateService`.
    """
    assert 1 == 1

# Generated at 2022-06-14 04:38:58.427067
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies
    from pypara.pricing.fxrates import FXRate, FXRateService, FXRateLookupError

    ## Implements the foreign exchange rate service:
    class CustomFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == ccy2:
                return FXRate.of(ccy1, ccy2, asof, 1)
            elif ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
                return FXRate.of(ccy1, ccy2, asof, 2)
            else:
                return None


# Generated at 2022-06-14 04:39:01.695887
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    queries = [
        (Currency('AAA'), Currency('BBB'), Date(1993, 2, 12)),
        (Currency('AAA'), Currency('BBB'), Date(1994, 2, 10))
    ]

    fxs = FXRateService()

    fxs.queries(queries, strict=True)



# Generated at 2022-06-14 04:39:05.383912
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Temporals
    FXRateService().queries([
        (Currencies["USD"], Currencies["EUR"], Temporals["2018-01-01"]),
        (Currencies["EUR"], Currencies["USD"], Temporals["2018-01-01"]),
        (Currencies["USD"], Currencies["CHF"], Temporals["2018-01-01"]),
    ])

# Generated at 2022-06-14 04:39:16.220941
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    from pypara.currencies import Currencies
    import datetime
    from decimal import Decimal

    class FXRateService_Test(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1.0"))

    rates = FXRateService_Test().queries(((Currencies["USD"], Currencies["EUR"], datetime.date(2017, 1, 1)),
                                          (Currencies["EUR"], Currencies["USD"], datetime.date(2017, 1, 2)),
                                          (Currencies["EUR"], Currencies["USD"], datetime.date(2017, 1, 3))))

# Generated at 2022-06-14 04:39:25.121627
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Note that this is an unit test for method query of class FXRateService.
    """
    from decimal import Decimal
    from pypara.currencies import Currencies
    from .temporals import TimePoint, today

    assert FXRateService.query(Currencies['USD'], Currencies['EUR'], today(), strict=True) == Decimal('0.5')
    try:
        FXRateService.query(Currencies['USD'], Currencies['EUR'], TimePoint(2018, 1, 1))
    except FXRateLookupError as err:
        assert err.args == ('Foreign exchange rate for USD/EUR not found as of 2018-01-01',)
    else:
        raise AssertionError('LookupError not raised')



# Generated at 2022-06-14 04:39:46.700064
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .commons import temporal
    from .fx import InMemoryFXRateService

    service = InMemoryFXRateService()
    service.rates.append(FXRate(Currencies["EUR"], Currencies["USD"], temporal.today, Decimal("2")))
    service.rates.append(FXRate(Currencies["USD"], Currencies["JPY"], temporal.today, Decimal("200")))
    service.rates.append(FXRate(Currencies["TRY"], Currencies["USD"], temporal.today, Decimal("0.2")))
    service.rates.append(FXRate(Currencies["TRY"], Currencies["EUR"], temporal.today, Decimal("1")))

    # noinspection PyTypeChecker

# Generated at 2022-06-14 04:39:52.653882
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    import datetime
    from decimal import Decimal
    from .commons.zeitgeist import Date

    q = Currencies["EUR"], Currencies["USD"], Date(2018, 12, 20)
    r = FXRateService.default.query(*q)
    assert r
    assert isinstance(r.value, Decimal)
    assert r.value > 1.0


# Generated at 2022-06-14 04:39:53.750968
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103
    pass

# Generated at 2022-06-14 04:39:54.387233
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:40:05.511879
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    from .currencies import Currencies
    from .commons.zeitgeist import Date

    class FXRateSession(FXRateService):
        """
        A mock foreign exchange rate service for FXRateService.query test.
        """


# Generated at 2022-06-14 04:40:06.582587
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:40:19.488041
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.memory import MemoryFXRateService

    service = MemoryFXRateService()

    rates = [
        FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    ]

    for rate in rates:
        service.update(rate.ccy1, rate.ccy2, rate.date, rate.value)

    rate = rates[0]

    qrate = service.query(rate.ccy1, rate.ccy2, rate.date)

    assert rate == qrate, "There should be a match."

    qrates = service.queries([(rate.ccy1, rate.ccy2, rate.date)])

    assert rate in qrates

# Generated at 2022-06-14 04:40:31.197759
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of FXRateService.
    """
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.issuances import AssetType
    from pypara.timeseries import Timeseries

    ## Create a timeseries:
    fxrates = Timeseries(
        "FXRATES",
        AssetType.FXRATE,
        (
            (date(2018, 9, 1), Decimal("0.86")),
            (date(2018, 9, 2), Decimal("0.85")),
            (date(2018, 9, 3), Decimal("0.87")),
        )
    )

    ## Create a test instance:
    class TestService(FXRateService):
        """
        Test FXRateService implementation
        """
       

# Generated at 2022-06-14 04:40:44.020440
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .commons.temporal import Date, DatePointSet
    from .currencies import Currency
    
    ## Prepare the test:
    qry = [
        (Currency('USD'), Currency('EUR'), Date.of(2018, 12, 31)),
        (Currency('USD'), Currency('TRY'), Date.of(2018, 12, 31)),
        (Currency('USD'), Currency('EUR'), Date.of(2018, 12, 31))
    ]
    
    ## Execute the test:
    def dummy_query(ccy1, ccy2, asof):
        if ccy1 == ccy2:
            return FXRate(ccy1, ccy2, asof, 1.0000)

# Generated at 2022-06-14 04:40:54.098168
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.foreign_exchange import FXRateService

    queries_in = [(Currencies["EUR"], Currencies["USD"], datetime.date.today()),
                  (Currencies["USD"], Currencies["EUR"], datetime.date.today()),
                  (Currencies["EUR"], Currencies["TRY"], datetime.date.today())]

    queries_out = [FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2")),
                   FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.5")),
                   None]


# Generated at 2022-06-14 04:41:45.722782
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    queries = [
        ("EUR", "USD", "2020-01-01"),
        ("USD", "EUR", "2020-01-01"),
        ("EUR", "USD", "2020-01-02"),
        ("USD", "EUR", "2020-01-02")
    ]
    rates = [
        ("EUR", "USD", "2020-01-01", Decimal("1.1")),
        ("USD", "EUR", "2020-01-01", Decimal("0.9")),
        ("EUR", "USD", "2020-01-02", Decimal("1.07")),
        ("USD", "EUR", "2020-01-02", Decimal("0.93")),
    ]


# Generated at 2022-06-14 04:41:51.282525
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from unittest import mock

    #: Defines a foreign exchange rate service.
    class FXRateServiceEx(FXRateService):

        def __init__(self):
            super().__init__()


# Generated at 2022-06-14 04:42:01.049434
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): # pragma: no cover
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currencies
    from pypara.finance.forex import FXRate, FXRateService
    class SampleFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False) -> Optional[FXRate]:
            if ccy1 == Currencies['EUR'] and ccy2 == Currencies['USD'] and asof == date(2020, 1, 1):
                return FXRate(Currencies['EUR'], Currencies['USD'], date(2020, 1, 1), Decimal('1.25'))
            else:
                return None

# Generated at 2022-06-14 04:42:10.570978
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService.
    """
    import datetime

    class FXRateServiceImpl(FXRateService):
        """
        Provides an implementation of :class:`FXRateService`.
        """

        def __init__(self, rates: Iterable[FXRate]):
            """
            Initializes the FX rate service implementation.
            """
            self.rates = dict(((rate[0], rate[1], rate[2]), rate) for rate in rates)

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            if strict:
                return self.rates[ccy1, ccy2, asof]


# Generated at 2022-06-14 04:42:22.909190
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal as D
    from pypara.currencies import Currencies
    from pypara.exchange import FXRateLookupError, FXRateService
    from pypara.services.memory import MemoryFXRateService

    ## Initialize the memory FX rate service:
    fx = MemoryFXRateService().with_quotes(
        (Currencies["EUR"], Currencies["USD"], datetime.date.today(), D("2")),
        (Currencies["USD"], Currencies["EUR"], datetime.date.today(), D("0.5"))
    )

    ## Test the fx rate service:
    eur_usd = fx.query(Currencies["EUR"], Currencies["USD"], datetime.date.today())

# Generated at 2022-06-14 04:42:31.737677
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    from unittest.mock import Mock  # noqa: E402
    from .currencies import Currency  # noqa: E402
    from .temporals import Date  # noqa: E402

    ## Create the mock:
    service = FXRateService()

    ## Assert default value of strict argument:
    assert service.query(Currency("EUR"), Currency("USD"), Date.today()) is not None

    ## Assert explicit strict argument:
    assert service.query(Currency("EUR"), Currency("USD"), Date.today(), strict=True) is not None

    ## Assert overriding strict argument:
    assert service.query(Currency("EUR"), Currency("USD"), Date.today(), strict=False) is not None

    ## Assert default value of strict argument:

# Generated at 2022-06-14 04:42:32.197338
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    ...

# Generated at 2022-06-14 04:42:42.069479
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from itertools import chain
    from pypara.commons import Temporals
    from pypara.currencies import Currencies
    from pypara.currencies.nifty import NiftyFXRateService

    nfxrate = NiftyFXRateService()

# Generated at 2022-06-14 04:42:52.058984
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currency
    from pypara.finance.commons.zeitgeist import Date
    from pypara.services.memory import MemoryFXRateService
    import datetime

    ## Create a currency pair and date:
    ccy1 = Currency.of("EUR")
    ccy2 = Currency.of("USD")
    asof = Date.today()

    # Test to provide a strict FX rate query
    service = MemoryFXRateService()
    fxrate = service.query(ccy1, ccy2, asof, strict=True)

    assert fxrate.ccy1 == ccy1
    assert fxrate.ccy2 == ccy2
    assert fxrate.date == asof
    assert isinstance(fxrate.value, Decimal)

    # Test to not provide a strict

# Generated at 2022-06-14 04:43:03.639886
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.currencies import Currencies
    from pypara.fx.in_memory import InMemoryFXRateService
    from pypara.temporal import Date

    ## Setup the FX rate service:
    rates = (
        (Currencies["USD"], Currencies["EUR"], Date("2018-01-01"), Decimal("2")),
        (Currencies["USD"], Currencies["EUR"], Date("2018-01-02"), Decimal("3")),
        (Currencies["USD"], Currencies["EUR"], Date("2018-01-03"), Decimal("4")),
    )
    svc = InMemoryFXRateService()
    svc.load(*(FXRate(*r) for r in rates))

    ## Query the service: