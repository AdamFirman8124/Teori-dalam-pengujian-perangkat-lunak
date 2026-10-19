

# Generated at 2022-06-14 04:34:20.467456
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:34:32.379386
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    ## Import packages:
    import datetime

    ## Import modules:
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.fxrates import FXRateService, FXRate

    ## Initialize a foreign exchange rate service:
    service = FXRateService()
    service.query = lambda ccy1, ccy2, asof, strict: FXRate(ccy1, ccy2, asof, Decimal(1))

    ## Make sure that the query is working fine:
    today = datetime.date.today()
    rate = service.query(Currencies["EUR"], Currencies["USD"], today)
    assert rate == FXRate(Currencies["EUR"], Currencies["USD"], today, Decimal(1))
    assert rate.value == Decimal(1)
    assert rate.cc

# Generated at 2022-06-14 04:34:45.288273
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest import mock, TestCase

    from .currencies import Currency, Currencies

    class Mock(FXRateService):
        @classmethod
        def _mock(cls, ccy1: Currency, ccy2: Currency, asof: Date) -> float:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof.date == asof.date:
                return 0.1
            raise FXRateLookupError(ccy1, ccy2, asof)


# Generated at 2022-06-14 04:34:58.503667
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate, FXRateService

    ## Create a stub FX rate service:
    eur_usd = Decimal("2")
    class Stub(FXRateService):
        """
        Provides a stub foreign exchange (FX) rate service.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False):
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            if ccy2 == Currencies["USD"] and ccy1 == Currencies["EUR"]:
                return FXRate(ccy1, ccy2, asof, eur_usd)

            return None


# Generated at 2022-06-14 04:35:12.135198
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """

    ## Import required packages:
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.currencies import Currency
    from pypara.currencies import FxRates
    from pypara.currencies import FXRateService
    from pypara.currencies import Temporal

    ## Prepare the query:
    queries = [
        (Currencies["EUR"], Currencies["USD"], datetime.date.today()),
        (Currencies["EUR"], Currencies["USD"], datetime.date.today()),
        (Currencies["EUR"], Currencies["USD"], datetime.date.today())
    ]

    ## Prepare the mocks:

# Generated at 2022-06-14 04:35:20.235338
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import TestCase, main
    from unittest.mock import Mock, call
    from pypara.currencies import Currency
    from .currencies.temporal import LocalDate

    testee = Mock(spec=FXRateService)
    result = testee.query(Currency("EUR"), Currency("USD"), LocalDate(2019, 1, 1))
    assert bool(result) is True
    assert testee.mock_calls == [call.query(Currency("EUR"), Currency("USD"), LocalDate(2019, 1, 1), strict=False)]

    main()



# Generated at 2022-06-14 04:35:31.915312
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currencies
    queries = ((Currencies["EUR"], Currencies["USD"], Date.today()),
               (Currencies["USD"], Currencies["EUR"], Date.today()))
    rates = [FXRate(ccy1=Currencies["EUR"], ccy2=Currencies["USD"], date=Date.today(), value=Decimal("1.5"))]
    fx_rate_service = FXRateServiceMock((queries[0],), rates)
    results = list(fx_rate_service.queries(queries))
    assert len(results) == len(queries)
    for index, query in enumerate(queries):
        assert results[index] is None
    for index, rate in enumerate(rates):
        assert results[index] == rate


# Generated at 2022-06-14 04:35:39.366151
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import TestCase, mock
    from pypara.currencies import Currencies
    from pypara.temporals import Date


# Generated at 2022-06-14 04:35:49.462707
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    # Imports:
    import datetime
    import unittest
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curves.fxrates import FXRateService

    # Test Case:
    class Case(unittest.TestCase):

        def test_fx_rate_service(self):

            # Define a foreign exchange rate service:
            class TestFXRateService(FXRateService):
                def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
                    pass
                def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
                    pass

            # Create a test service:
            testService = TestFXRateService

# Generated at 2022-06-14 04:36:03.451930
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class LocalFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict):
            if ccy1 != Currencies["EUR"]:
                return None
            if ccy2 != Currencies["USD"]:
                return None
            if asof != date:
                return None
            return FXRate(Currencies["EUR"], Currencies["USD"], date, Decimal("2"))

    date = datetime.date.today()
    fxrs = LocalFXRateService()
    rate = fxrs.query(Currencies["EUR"], Currencies["USD"], date)
    assert rate == FXRate.of(Currencies["EUR"], Currencies["USD"], date, Decimal("2"))

# Generated at 2022-06-14 04:36:19.440665
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService
    """
    from .currencies import Currency
    from .fxrates import FXRateService
    from .temporal import Date

    class MockFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, 0.5)

    service = MockFXRateService()
    assert service.query(Currency("ABC"), Currency("XYZ"), Date("2019-01-01")) == FXRate(Currency("ABC"),
                                                                                          Currency("XYZ"),
                                                                                          Date("2019-01-01"),
                                                                                          0.5)


# Generated at 2022-06-14 04:36:27.636551
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    from pypara.currencies import Currency
    from pypara.markets import FXRate
    from pypara.markets.services import InMemoryFXRateService

    EUR = Currency("EUR")
    USD = Currency("USD")
    GBP = Currency("GBP")
    JPY = Currency("JPY")
    CAD = Currency("CAD")
    CNY = Currency("CNY")


# Generated at 2022-06-14 04:36:41.316842
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curves import FXRateCurve
    from pypara.curves.interpolators import Interpolator
    from pypara.temporals.timeutils import asdate

    # Create an FX rate curve
    curve = FXRateCurve(Interpolator("linear"))

    # Populate the FX rate curve with some FX rates
    curve.add(Currencies["EUR"], Currencies["USD"], asdate("20070101"), Decimal("1.3"))
    curve.add(Currencies["EUR"], Currencies["USD"], asdate("20080101"), Decimal("1.5"))
    curve.add(Currencies["EUR"], Currencies["USD"], asdate("20090101"), Decimal("1.4"))

# Generated at 2022-06-14 04:36:54.486090
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from .temporal import Temporal
    from .impl.memory_fxrates import MemoryFXRateService

    # Prepare example data:
    fxrates = {
        (Currencies['USD'], Currencies['EUR'], datetime.date(2018, 10, 5)): Decimal('0.88'),
        (Currencies['EUR'], Currencies['USD'], datetime.date(2018, 10, 6)): Decimal('1.13'),
        (Currencies['JPY'], Currencies['USD'], datetime.date(2018, 10, 7)): Decimal('0.009'),
    }

    # Create FX rate service:
    fxrservice = MemoryFXRateService(fxrates)

    # Convert EUR to USD

# Generated at 2022-06-14 04:37:02.307601
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:37:15.183410
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.markets.fx import FXRate, FXRateService

    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if strict:
                if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                    return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
                else:
                    raise FXRateLookupError(ccy1, ccy2, asof)

# Generated at 2022-06-14 04:37:28.683004
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies
    from pypara.temporals import Temporals
    from pypara.testing.fxrates import BaseFXRateService

    # Create an FX rate service:
    service = BaseFXRateService()

    # Prepare the queries:
    queries = (
        (Currencies["EUR"], Currencies["USD"], Temporals.today),
        (Currencies["USD"], Currencies["EUR"], Temporals.today),
        (Currencies["EUR"], Currencies["USD"], Temporals.today + 1)
    )

    # Query:
    results = service.queries(queries)

# Generated at 2022-06-14 04:37:30.663466
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:37:41.655081
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .temporals import Date
    from .fx import FXRateService
    from .fakes import FakeFXRateService
    fx = FakeFXRateService()
    fx.rates.append(FXRate(Currencies["EUR"], Currencies["USD"], Date(2018, 1, 1), Decimal("1.15")))
    fx.rates.append(FXRate(Currencies["EUR"], Currencies["USD"], Date(2014, 11, 30), Decimal("1")))
    fx.rates.append(FXRate(Currencies["EUR"], Currencies["USD"], Date(2017, 1, 1), Decimal("1.23")))

# Generated at 2022-06-14 04:37:52.126391
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService
    from pypara.temporal import now, TPlus

    class TestRateService(FXRateService):
        def __init__(self):
            self.rate = FXRate(Currencies["EUR"], Currencies["USD"], now(), Decimal("1.25"))

        def query(self, ccy1, ccy2, asof, strict=False):
            if self.rate[0] == ccy1 and self.rate[1] == ccy2 and self.rate[2] == asof:
                return self.rate
            else:
                raise FXRateLookupError(ccy1, ccy2, asof)


# Generated at 2022-06-14 04:38:09.408664
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from itertools import product
    from .currencies import Currencies
    from .commons.zeitgeist import AsOf

    ## Let's create a list of all currency pairs:
    ## ccys = list(product(CCys, CCys))
    ccys = [
        (Currencies["EUR"], Currencies["USD"]),
        (Currencies["USD"], Currencies["EUR"]),
        (Currencies["USD"], Currencies["USD"]),
    ]

    ## Let's create a list of dates:
    dates = [AsOf.today(), AsOf.yesterday()]

    ## Define pairs of query and result:

# Generated at 2022-06-14 04:38:12.074701
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    assert False


# Generated at 2022-06-14 04:38:17.139674
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.currencies.ics.currency_service import ICService

    # IC
    ic = ICService()
    currency = ic.query("USD")
    date = ic.query("GBP")
    rate = FXRate.of(currency, date, date.now(), Decimal("2"))
    assert True

# Generated at 2022-06-14 04:38:29.520460
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate, FXRateLookupError, FXRateService

    ## Define a mock FX rate service class:
    class _MockFXRateService(FXRateService):

        def __init__(self, rates: Tuple[FXRate, ...]) -> None:
            self.rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            for rate in self.rates:
                if rate.ccy1 == ccy1 and rate.ccy2 == ccy2 and rate.date == asof:
                    return rate

# Generated at 2022-06-14 04:38:32.687543
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method FXRateService.query of class FXRateService.
    """

    pass # TODO: Implement test.



# Generated at 2022-06-14 04:38:44.643928
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from unittest import TestCase
    from pypara.currencies import Currencies
    from pypara.temporal import Date
    from pypara.finance.fx import FXRate, FXRateService

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == Date(2017, 12, 31):
                return FXRate(ccy1, ccy2, asof, Decimal("1.2"))
            return None

    fxrate_service = TestFXRateService()

# Generated at 2022-06-14 04:38:51.278026
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """Unit test for method queries of class FXRateService"""
    from unittest.mock import MagicMock
    from .currencies import Currencies
    from .commons.zeitgeist import Date

    FXRateService.default = MagicMock()
    FXRateService.default.queries.return_value = [
        FXRate(Currencies["EUR"], Currencies["TRY"], Date(day = 1, month = 1, year = 2000), Decimal("2")),
        FXRate(Currencies["EUR"], Currencies["TRY"], Date(day = 2, month = 2, year = 2020), Decimal("3")),
    ]

# Generated at 2022-06-14 04:39:01.322792
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates.in_memory import InMemoryFXRateService

    fxrates = [
        FXRate(Currencies["EUR"], Currencies["USD"], date(2020, 5, 15), Decimal("2")),
        FXRate(Currencies["EUR"], Currencies["USD"], date(2020, 5, 16), Decimal("2.5")),
        FXRate(Currencies["EUR"], Currencies["USD"], date(2020, 5, 17), Decimal("2.5")),
        FXRate(Currencies["EUR"], Currencies["USD"], date(2020, 5, 18), Decimal("3")),
    ]

    rateservice = InMemoryFXRateService(fxrates)

# Generated at 2022-06-14 04:39:13.247052
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test the functionality of method queries of class FXRateService
    """
    from unittest import TestCase, mock
    from pypara.currencies import Currencies
    from pypara.finance import Date

    queries = [(Currencies["EUR"], Currencies["USD"], Date.of(2020, 1, 1)),
               (Currencies["USD"], Currencies["EUR"], Date.of(2020, 1, 1)),
               (Currencies["EUR"], Currencies["USD"], Date.of(2020, 1, 2)),
               (Currencies["USD"], Currencies["EUR"], Date.of(2020, 1, 2))]


# Generated at 2022-06-14 04:39:22.894223
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    """
    from pypara.currencies import Currencies
    from pypara.services.fixed_fx_rate_service import FixedFXRateService

    ## Local services:

# Generated at 2022-06-14 04:39:44.538148
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import mock
    import decimal
    import datetime
    from pypara.currencies import Currency
    from pypara.fx import FXRateService
    from pypara.temporal import Date
    context = mock.MagicMock()
    service = FXRateService(context)
    service.query = mock.MagicMock()
    service.query.side_effect = [decimal.Decimal(3), decimal.Decimal(2), decimal.Decimal(9)]
    ccy1 = Currency.of("EUR")
    ccy2 = Currency.of("USD")
    ccy3 = Currency.of("GBP")
    date1 = Date.of(2011, 4, 4)
    date2 = Date.of(2012, 5, 5)
    date3 = Date.of(2013, 6, 6)
    result = service

# Generated at 2022-06-14 04:39:55.596292
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .currencies.temporal import CurrencyRate
    from .fx import FXRateService
    from datetime import date
    import unittest
    class FXRateServiceTest(FXRateService):
        def query(self, ccy1, ccy2, asof, strict):
            return CurrencyRate.TRANSLATED.get((ccy1, ccy2, asof))
        def queries(self, queries, strict):
            return (self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries)
        def test_query_single(self):
            self.query(Currency("EUR"), Currency("USD"), date(2019, 1, 1), False)

# Generated at 2022-06-14 04:39:57.519154
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:40:07.322124
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRate, FXRateService
    from pypara.temporal import Date, DateTime
    from pypara.testing import TestCase

    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: DateTime, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("2") if ccy1 == Currencies["USD"] and ccy2 == Currencies["TRY"] else None)


# Generated at 2022-06-14 04:40:14.280340
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class FXRateService.
    """
    ## Find the test module:
    import sys, os
    import unittest
    import pypara as pp

    ## Discover the tests:
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.discover(os.path.dirname(__file__)))

# Generated at 2022-06-14 04:40:25.955653
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from decimalfp import Decimal
    from pypara.currencies import Currencies

    class StaticFXRateService(FXRateService):
        """
        Provides a static FX rate service implementation.
        """


# Generated at 2022-06-14 04:40:35.842782
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService
    from pypara.temporal import Dates

    ## Create a dummy FX rate service:
    default = FXRateService()

    ## Define a dummy function:
    def query(ccy1, ccy2, asof, strict=False):
        if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
            if asof == Dates[2019][1][1]:
                return FXRate(Currencies["EUR"], Currencies["USD"], asof, ONE)
            elif asof == Dates[2019][1][2]:
                return FXRate(Currencies["EUR"], Currencies["USD"], asof, ONE)

# Generated at 2022-06-14 04:40:37.007775
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:40:48.339706
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .temporal import Temporal
    from .zeitgeist import Date
    import datetime
    from decimal import Decimal
    from pypara.fx import FXRate

    ## Define a dummy FX rate service:
    class DummyFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1.00"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for query in queries:
                yield FXRate(query[0], query[1], query[2], Decimal("1.00"))

    ## Create

# Generated at 2022-06-14 04:40:57.240874
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    ## Check that maps is defined and is a builtin function:
    assert callable(map)
    assert map.__module__ == "builtins"

    ## Define an FX rate service:
    class MyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("2.3"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return map(lambda q: self.query(q[0], q[1], q[2], strict), queries)

    ## Check if the implementation works as expected:
    import datetime

# Generated at 2022-06-14 04:41:46.130127
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # Given:
    from .currencies import Currencies
    from .temporal import DateTime
    from .temporal import Period
    from .temporal import Schedule

    from decimal import Decimal as D

    from unittest import TestCase
    from unittest.mock import MagicMock
    from unittest.mock import patch

    class TestFXRateService(FXRateService):

        def __init__(self, rates: dict, duration: int = 0, strict: bool = True) -> None:
            self.rates = rates
            self.duration = duration
            self.strict = strict

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if strict != self.strict:
                raise ValueError(strict)

           

# Generated at 2022-06-14 04:41:51.420186
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Temporal
    from decimal import Decimal
    from typing import Iterable
    from unittest import TestCase

    class MyService(FXRateService):
        def __init__(self, rates: Iterable[FXRate]):
            self.rates = {(rate[0], rate[1], rate[2]): rate for rate in rates}

        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[FXRate]:
            try:
                return self.rates[(ccy1, ccy2, asof)]
            except KeyError:
                if strict:
                    raise FXRateLookupError(ccy1, ccy2, asof)
                else:
                    return None


# Generated at 2022-06-14 04:42:01.171553
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the query method of the :class:`FXRateService` class.
    """
    import datetime
    from decimal import Decimal
    from unittest.mock import Mock
    from pypara.currencies import Currencies

    class MockRateService(FXRateService):
        """
        Provides a mock FX rate service.
        """


# Generated at 2022-06-14 04:42:09.109921
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict = False):
            return FXRate(ccy1, ccy2, asof, Decimal("2"))
    test = TestFXRateService()
    assert test.query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) == FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))


# Generated at 2022-06-14 04:42:21.119219
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies
    from pypara.datasources.memory import InMemoryDataSource
    from pypara.datasources.query import Query
    from pypara.times import Temporal

    ## Prepare test data:
    queries = [
        (Currencies["EUR"], Currencies["USD"], Temporal(datetime.date(2018, 1, 1))),
        (Currencies["EUR"], Currencies["USD"], Temporal(datetime.date(2019, 1, 1)))
    ]

# Generated at 2022-06-14 04:42:22.478311
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:42:31.440950
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.datetimes import Date, Temporal
    from pypara.fx.services import FXRateService

    class MyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1.5"))

        def queries(self, queries: Iterable[Tuple[Currency, Currency, Temporal]], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [FXRate(ccy1, ccy2, date, Decimal("1.5")) for ccy1, ccy2, date in queries]

    fx

# Generated at 2022-06-14 04:42:33.218436
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)

# Generated at 2022-06-14 04:42:38.416710
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    import datetime

    class FXRateServiceTestImpl(FXRateService):

        def __init__(self, rates: Iterable[FXRate]):
            self._rates = {(rate[0], rate[1], rate[2]): rate[3] for rate in rates}


# Generated at 2022-06-14 04:42:50.386087
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """
    import unittest
    import datetime
    from decimal import Decimal
    from pypara.fxrates import FXRateService
    from pypara.currencies import Currencies

    class StubFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [None] * len(queries)

    class TestFXRateService(unittest.TestCase):

        def setUp(self):
            self.rate_service = StubFXRateService()


# Generated at 2022-06-14 04:44:03.740427
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    class Service0(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal("1.2"))

    class Service1(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return super().query(ccy1, ccy2, asof, strict)

        def queries(self, queries, strict=False):
            return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

    ## Create a service

# Generated at 2022-06-14 04:44:12.802195
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finmath.fx import FXRateService
    from pypara.services import Services

    rates = [("EUR", "USD", datetime.date.today(), Decimal("2")),
             ("EUR", "USD", datetime.date.today() + datetime.timedelta(days=1), Decimal("2.5")),
             ("EUR", "USD", datetime.date.today() + datetime.timedelta(days=2), Decimal("3"))]


# Generated at 2022-06-14 04:44:23.496326
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Days

    class StubFXRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            if (ccy1 == Currencies['USD'] and ccy2 == Currencies['USD'] and asof ==
                    datetime.date(2020, 1, 1)):
                return None
            elif (ccy1 == Currencies['EUR'] and ccy2 == Currencies['USD'] and asof ==
                  datetime.date(2020, 1, 1)):
                return FXRate(Currencies['EUR'], Currencies['USD'], datetime.date(2020, 1, 1), 2)