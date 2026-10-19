

# Generated at 2022-06-14 04:34:38.418399
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """
    from .__init__ import _decimals
    from .currencies import Currencies
    from datetime import date
    from decimal import Decimal
    import unittest
    import warnings

    # noinspection PyUnusedLocal
    class _TestFXRateService(FXRateService):
        """
        Provides a test foreign exchange rate service class.
        """


# Generated at 2022-06-14 04:34:39.501501
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:34:47.790436
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """Unit test for method FXRateService.queries"""

    from .currencies import Currencies
    from .temporal import Date
    from .services.memory import MemoryFXRateService
    from .services.downloaders import ECBFXRateDownloader

    ## Initialize parameters:
    date = Date.today()
    query = (Currencies["USD"], Currencies["EUR"], date)

    ## Prepare the service:
    service = MemoryFXRateService(ECBFXRateDownloader())

    ## Execute the query:
    rates = list(service.queries([query]))
    assert len(rates) == 1


# Generated at 2022-06-14 04:34:58.226142
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    from pypara.currencies import Currencies
    from pypara.temporals import Date

    from . import InMemoryFXRateService
    from .fxrates import FXRate

    service = InMemoryFXRateService(
        FXRate(Currencies["USD"], Currencies["EUR"], Date(2018, 1, 1), Decimal("0.8"))
    )

    rate = service.query(Currencies["USD"], Currencies["EUR"], Date(2018, 1, 1))

    assert rate == FXRate(Currencies["USD"], Currencies["EUR"], Date(2018, 1, 1), Decimal("0.8"))


# Generated at 2022-06-14 04:35:11.847693
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curves import FlatCurve

    class FXRateServiceTmp(FXRateService):
        """
        Temporary FX rate service for testing.
        """

        #: The FX rates.

# Generated at 2022-06-14 04:35:21.497333
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currencies
    from pypara.fx.services.memory import MemoryFXRateService
    svc = MemoryFXRateService()
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["EUR"]
    rate = FXRate(ccy1, ccy2, date.today(), Decimal("0.8"))
    assert svc.query(ccy1, ccy2, date.today()) is None
    svc.upload(rate)
    assert svc.query(ccy1, ccy2, date.today()) is not None
    assert svc.query(ccy1, ccy2, date.today()) == rate

# Generated at 2022-06-14 04:35:32.596348
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.time import Temporal
    from pypara.currencies import Currency
    from pypara.services.fx import FXRateService

    ## Define a test implementation of a service:
    class TestService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[FXRate]:
            print(f"Query: {ccy1}, {ccy2}, {asof}, {strict}")
            return FXRate(ccy1, ccy2, asof, Decimal("1"))


# Generated at 2022-06-14 04:35:38.837683
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D302
    from .temporal import Date
    from .currencies import Currencies
    from .fx import FXRateService
    FXRateService.default = None
    try:
        FXRateService.default.query(Currencies["EUR"], Currencies["USD"], Date.today(), strict=True)
        raise AssertionError("Not raised.")
    except RuntimeError:
        pass
    except ValueError:
        raise AssertionError("Wrong exception.")


# Generated at 2022-06-14 04:35:48.936122
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test that the queries method of `FXRateService` class works as expected.
    """

    from unittest.mock import Mock, patch
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies

    ## Check the case where there is a call for an invalid query.
    #
    # Create the test instance:
    rate_service = FXRateService()

    # This should be wrapped in a context manager:

# Generated at 2022-06-14 04:35:56.270242
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    import datetime as dt
    import unittest

    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateLookupError, FXRateService

    class TestFXRateService(FXRateService, unittest.TestCase):
        """
        Implements a minimal foreign exchange rate service for testing purposes.
        """

        def __init__(self) -> None:
            """
            Initializes the foreign exchange rate service.
            """
            ## Populate the rates:
            self.rates = []
            self.rates.append(FXRate(Currencies["EUR"], Currencies["USD"], dt.date(2018, 3, 31), Decimal("1.230")))

# Generated at 2022-06-14 04:36:11.935355
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    from decimal import Decimal

    from pypara.currencies import Currency, Currencies

    class _FXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            ## Mock to return a fixed rate:
            return FXRate(ccy1, ccy2, asof, Decimal("1"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            raise NotImplementedError()


# Generated at 2022-06-14 04:36:21.152399
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Temporal

    queries = [(Currencies["USD"], Currencies["EUR"], Temporal.today()),
               (Currencies["EUR"], Currencies["USD"], Temporal.today()),
               (Currencies["USD"], Currencies["EUR"], Temporal.today()),
               (Currencies["EUR"], Currencies["USD"], Temporal.today()),]

    assert FXRateService.default.queries(queries)
    assert FXRateService.default.queries(queries, strict=True)

# Generated at 2022-06-14 04:36:30.539238
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .services import FXRateServices

    ## Define the query:
    ccy1 = Currency("EUR")
    ccy2 = Currency("USD")
    date = Date(2019, 1, 1)

    ## Create the service and query:
    service = FXRateServices.default
    rate = service.query(ccy1, ccy2, date)

    ## Check the response:
    assert isinstance(rate, FXRate)
    assert rate.ccy1 == ccy1
    assert rate.ccy2 == ccy2
    assert rate.date == date
    assert rate.value > ZERO



# Generated at 2022-06-14 04:36:40.751184
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime

    from decimal import Decimal
    from pypara.currencies import Currencies

    rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("0.5"))

    class FXRateServiceMock(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return rate

    assert FXRateServiceMock().query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) == rate


# Generated at 2022-06-14 04:36:53.414233
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .dates import Dates
    from .finance import FXRate, FXRateService

    class MyFXRateService(FXRateService):
        def __init__(self, rates: Iterable[FXRate]) -> None:
            ## Keep the rates:
            self.rates = [r for r in rates]

        def query(self, ccy1, ccy2, asof, strict=False) -> Optional[FXRate]:
            for rate in self.rates:
                if rate.ccy1 == ccy1 and rate.ccy2 == ccy2 and rate.date == asof:
                    return rate

            raise FXRateLookupError(ccy1, ccy2, asof)


# Generated at 2022-06-14 04:36:59.490427
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103
    from .currencies import Currencies
    from .temporal import today
    from .exchange.rates import fx_rates
    rate = fx_rates.query(Currencies["EUR"], Currencies["USD"], today)
    assert rate.ccy1 == Currencies["EUR"]
    assert rate.ccy2 == Currencies["USD"]
    assert rate.date == today
    assert rate.value > 1


# Generated at 2022-06-14 04:37:12.941367
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Does the method queries of class FXRateService work as expected?
    """
    ## Import:
    from unittest import TestCase, mock

    ## Mocks:
    from .commons import Temporals
    from .currencies import Currencies
    from .fxrates import FXRate

    ## Test case:
    class Test(TestCase):
        """
        Test case for method queries.
        """

        def setUp(self) -> None:
            """
            Sets up the test fixture.
            """
            self.CCY_1 = Currencies["USD"]
            self.CCY_2 = Currencies["EUR"]
            self.TMP = Temporals.today()
            self.QUERY = (self.CCY_1, self.CCY_2, self.TMP)

# Generated at 2022-06-14 04:37:25.730000
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from pypara.currencies import Currencies

    class MockFXRateService(FXRateService):
        def __init__(self):
            from iterable_collections import collect
            self._rates = collect(
                FXRate(Currencies["EUR"], Currencies["USD"], date(2019, 1, 1), 1.5),
                FXRate(Currencies["USD"], Currencies["EUR"], date(2019, 1, 1), 0.5),
                FXRate(Currencies["EUR"], Currencies["USD"], date(2019, 1, 2), 1.6),
                FXRate(Currencies["USD"], Currencies["EUR"], date(2019, 1, 2), 0.6),
            ).to_dict(key=lambda x: (x[0], x[1], x[2]))


# Generated at 2022-06-14 04:37:37.803350
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class FXRateService.
    """
    from pypara.currencies import Currencies
    from pypara.dates import dates

    class DummyFXRateService(FXRateService):
        """
        Provides a dummy FX rate service.
        """

        def query(self, ccy1, ccy2, asof, strict=False):  # noqa: N802
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            return FXRate(ccy1, ccy2, asof, Decimal(1))

        def queries(self, queries, strict=False):  # noqa: N802
            """
            Returns foreign exchange rates for a given collection of currency pairs and dates.
            """

# Generated at 2022-06-14 04:37:49.965301
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:38:08.559826
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.fxtrades import FXRateService
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    fxr1 = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    fxr2 = FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.5"))
    fxr3 = FXRate(Currencies["EUR"], Currencies["EUR"], datetime.date.today(), Decimal("1"))
    fxr4 = FXRate(Currencies["USD"], Currencies["USD"], datetime.date.today(), Decimal("1"))

    fxrates = [fxr1, fxr2, fxr3, fxr4]



# Generated at 2022-06-14 04:38:21.707948
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:38:32.507450
# Unit test for method query of class FXRateService

# Generated at 2022-06-14 04:38:40.498434
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests `queries` method of class :class:`FXRateService`.
    """

    from .currencies import Currencies

    from .curves import Curve, CurveService, PolynomialCurve, YieldCurveType
    from .curves.tests.test_curve_service import RandomCurveService

    from pypara.commons import Temporal

    # Prepare a test yield curve service:
    curve_service = CurveService.default or RandomCurveService()

    # Prepare a test FX rate service:

# Generated at 2022-06-14 04:38:48.806817
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .temporal import Temporal
    from ..currencies import Currencies
    from .rates.calendars import Calendar
    from .rates.services import FXRateService as FXRateServiceImpl
    service = FXRateServiceImpl()

    class TemporalStub(Temporal):
        def __init__(self, date: Date) -> None:
            self.date = date

    calendar = Calendar.of(4444)

    assert tuple(service.queries(
        ((Currencies["EUR"], Currencies["USD"], TemporalStub(calendar.day(1))),),
        strict=True,
    )) == (FXRate.of(Currencies["EUR"], Currencies["USD"], calendar.day(1), Decimal("0.858")),)


# Generated at 2022-06-14 04:38:50.375535
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:39:01.214419
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    ## Class FXRateService queries:

    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal(1)) if ccy1 == ccy2 else None

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (FXRate(ccy1, ccy2, asof, Decimal(1)) if ccy1 == ccy2 else None for ccy1, ccy2, asof in queries)

    ## Positive test

# Generated at 2022-06-14 04:39:03.051100
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:39:14.180281
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest import TestCase, mock
    from datetime import date, datetime
    from pypara.currencies import Currency
    from pypara.finance.fx import FXRateService
    from pypara.finance.fx.fxlib import FXLib
    from pypara.zeitgeist import Temporal

    class MockFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[FXRate]:
            return None

    class Test_query(TestCase):

        def test_should_make_a_query_for_each_item_in_the_iterator(self):
            service = MockFXRateService()

# Generated at 2022-06-14 04:39:25.058449
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # Test helper
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    nrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("0.5"))
    rrate = FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("2"))
    fxrates = {
        (Currencies["EUR"], Currencies["USD"], datetime.date.today()): nrate,
        (Currencies["USD"], Currencies["EUR"], datetime.date.today()): rrate,
    }


# Generated at 2022-06-14 04:39:51.751165
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # setup
    from .currencies import Currency, Currencies
    from .temporal import Date, DATE
    from .services.bloomberg import BloombergFXRateService
    from .services.memory import MemoryFXRateService
    from .services.yahoo import YahooFXRateService
    from .services.service import Service
    from . import services
    from itertools import chain
    from dateutil.parser import parse

    # arrange
    def to_query(ccy1: Currency, ccy2: Currency, date: Date):
        return (ccy1, ccy2, date, )


# Generated at 2022-06-14 04:40:03.515752
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():          # noqa: D103
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService, FXRate

    class MockRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal("1"))

        def queries(self, queries, strict=False):
            for ccy1, ccy2, asof in queries:
                yield FXRate(ccy1, ccy2, asof, Decimal("1"))

    rate_service = MockRateService()

# Generated at 2022-06-14 04:40:05.032949
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():  # noqa: E305
    """
    Tests method queries of class FXRateService.
    """
    pass

# Generated at 2022-06-14 04:40:06.330503
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # TODO: Implement unit test
    pass

# Generated at 2022-06-14 04:40:09.969322
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests :method:`FXRateService.queries` method.
    """
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies

    from .commons.mocks import FXRateServiceMock

    # Define a set of queries:
    queries = [
        (Currencies["EUR"], Currencies["USD"], date(2018, 5, 1)),
        (Currencies["USD"], Currencies["EUR"], date(2018, 5, 2)),
        (Currencies["USD"], Currencies["EUR"], date(2018, 5, 1)),
        (Currencies["EUR"], Currencies["USD"], date(2018, 5, 2)),
    ]

    # Define a set of expected rates:

# Generated at 2022-06-14 04:40:22.595860
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.dates import Temporals
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    class MockService(FXRateService):
        """
        Provides a mock implementation of class :class:`FXRateService`.
        """

        def query(self, ccy1, ccy2, asof, strict=False):
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            asof = Temporals.to_date(asof)
            if not isinstance(ccy1, Currency):
                raise ValueError("CCY1 must be of type `Currency`.")
            if not isinstance(ccy2, Currency):
                raise ValueError("CCY2 must be of type `Currency`.")

# Generated at 2022-06-14 04:40:33.930761
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from itertools import product
    from datetime import date
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService, FXRateLookupError

    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"] and asof == date(2018, 9, 18):
                return FXRate(ccy1, ccy2, asof, Decimal("0.75"))
            else:
                return None

        def queries(self, queries, strict=False):
            for ccy1, ccy2, asof in queries:
                yield self.query(ccy1, ccy2, asof, strict)


# Generated at 2022-06-14 04:40:39.677347
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import unittest
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.temporal import Temporal
    
    class FXRateService_query(unittest.TestCase):
        def test_query(self):
            ...
    unittest.main(module="test_FXRateService_query")


# Generated at 2022-06-14 04:40:40.693337
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass # TODO: Implement unit test

# Generated at 2022-06-14 04:40:50.887245
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Ccy
    from .factory import FXRateServiceFactory
    from .temporal import AsOf

    ## Get service from the factory:
    service = FXRateServiceFactory().register("ECB", "eurofxref-hist.xml").create()

    ## Query "EUR/USD" FX rate as of 2017-05-23:
    rate = service.query(Ccy("EUR"), Ccy("USD"), AsOf("2017-05-23"))

    ## Assert correct result:
    assert rate.ccy1 == Ccy("EUR")
    assert rate.ccy2 == Ccy("USD")
    assert rate.date == AsOf("2017-05-23")
    assert rate.value == 1.0939

# Generated at 2022-06-14 04:41:37.997468
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    queries = [
        (Currencies["USD"], Currencies["TRY"], datetime.date(2004, 5, 23)),
        (Currencies["USD"], Currencies["TRY"], datetime.date(2004, 5, 24)),
        (Currencies["USD"], Currencies["TRY"], datetime.date(2004, 5, 25)),
        (Currencies["USD"], Currencies["TRY"], datetime.date(2004, 5, 30)),
        (Currencies["USD"], Currencies["TRY"], datetime.date(2004, 6, 1))
    ]

# Generated at 2022-06-14 04:41:39.391694
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:41:48.821595
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from itertools import chain
    from unittest_data_provider import data_provider

    from .currencies import Currencies
    from .temporals import Temporals

    class TestFXRateService(FXRateService):
        # noinspection PyMethodMayBeStatic
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            yield from super().queries(queries, strict=strict)


# Generated at 2022-06-14 04:41:59.671407
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # Imports
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import (
        FXRate,
        FXRateService,
    )
    # End - Imports
    # Local Variables
    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"]:
                return FXRate.of(Currencies["EUR"], Currencies["USD"], asof, Decimal("2"))
            elif ccy1 == Currencies["USD"]:
                return FXRate.of(Currencies["USD"], Currencies["EUR"], asof, Decimal("0.5"))
            else:
                return None


# Generated at 2022-06-14 04:42:10.250563
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .commons.zeitgeist import Date
    from .fx.local import LocalFXRateService

    ## Define the FX rate service:
    service = LocalFXRateService.load(["../tests/fx/fxrates.csv"])  # type: FXRateService

    ## Define the queries:

# Generated at 2022-06-14 04:42:11.311313
# Unit test for method query of class FXRateService
def test_FXRateService_query():
        pass


# Generated at 2022-06-14 04:42:23.607933
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.currencies import Currencies
    from pypara.temporal import Date, Dates
    from pypara.fx.dummy import DummyFXRateService

    service = DummyFXRateService()

# Generated at 2022-06-14 04:42:32.191554
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class MockFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal("1"))
        def queries(self, queries, strict=False):
            for q in queries:
                yield self.query(*q)

    service = MockFXRateService()
    queries = [
        (Currencies["USD"], Currencies["EUR"], datetime.date(2018, 1, 1)),
        (Currencies["USD"], Currencies["GBP"], datetime.date(2018, 1, 2))
    ]
    rates = [i for i in service.queries(queries)]

# Generated at 2022-06-14 04:42:37.858857
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests :method:`FXRateService.queries` method of :class:`FXRateService` class
    """

    from datetime import date
    from unittest import TestCase
    from unittest.mock import Mock
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    class _TestCase(TestCase):

        def setUp(self):
            self.eurusd1 = FXRate.of(Currencies["EUR"], Currencies["USD"], date(2019, 11, 1), Decimal("1.5"))
            self.eurusd2 = FXRate.of(Currencies["EUR"], Currencies["USD"], date(2019, 11, 2), Decimal("1.6"))

# Generated at 2022-06-14 04:42:49.918543
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest.mock import MagicMock, patch

    from .currencies import Currencies

    ## Set the scope:
    scope = {"FxRateService": FXRateService}

    ## Patch the class:
    with patch.multiple(FXRateService, query=MagicMock()) as mocks:
        ## Prepare the reference:
        ref = mocks["query"].return_value = MagicMock()

        ## Evaluate the test-case:
        exec("from pypara.fx import FXRateService\n"
             "r = FxRateService().queries([(Currencies['EUR'], Currencies['USD'], Date())])", scope)

        ## Check the output:
        assert list(scope["r"]) == [ref]

        ## Check the calls:
        mocks["query"].assert_called_once_

# Generated at 2022-06-14 04:44:10.959519
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import EUR, USD
    from .temporal import Date
    from .temporal.zeitgeist import Dates
    from .futures import Future

    fxs = Future.of(USD, Dates.today(), 100) * 2
    queries = (
        (EUR, USD, Dates.today()),
        (USD, EUR, Dates.today()),
        (USD, USD, Dates.today()),
    )

    class LocalFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            if (ccy1, ccy2, asof) in queries:
                return FXRate(ccy1, ccy2, asof, 1)


# Generated at 2022-06-14 04:44:22.594476
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """
    from pypara.currencies import Currency
    from .currencies.providers import CurrenciesProvider
    from .fxrates.services import LocalFXRateService
    from .fxrates.providers import LocalFXRateProvider
    from .time.services import RealTimeService

    ## Prepare a FX rate service:
    provider = LocalFXRateProvider()
    service = LocalFXRateService(
        provider,
        CurrenciesProvider(),
        RealTimeService()
    )

    ## Prepare the sample query:
    query = (Currency("EUR", "EUR"), Currency("USD", "USD"), None)

    ## Grab the results:
    results = service.queries([query], strict=True)

    ## Assert the first result:
    result = results[0]

   