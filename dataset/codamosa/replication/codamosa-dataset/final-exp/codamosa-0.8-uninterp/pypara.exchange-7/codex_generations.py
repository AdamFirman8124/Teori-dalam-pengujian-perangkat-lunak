

# Generated at 2022-06-14 04:34:36.674430
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curves import CurveService
    from pypara.curves.curve import CurveLookupError
    from pypara.exchanges import Exchanges
    from pypara.exchanges.exchange import ExchangeLookupError
    from pypara.timeseries import TimeSeriesLookupError

    ## Create the curve service, which is used by the FX rate service below to determine the FX rates:
    cs = CurveService.default

    ## Create a set of queries:

# Generated at 2022-06-14 04:34:47.791978
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """
    from decimal import Decimal
    from unittest import TestCase
    from unittest.mock import Mock, call
    from .currencies import Currency

    ## Defines a foreign exchange rate service for testing:
    class MockFXRateService(FXRateService):
        def __init__(self) -> None:
            self.query_mock = Mock(return_value=None)
            self.query_mock.side_effect = lambda c, l, a: {(Currency("EUR"), Currency("USD"), Date("20180101")): FXRate(Currency("EUR"), Currency("USD"), Date("20180101"), Decimal("0.5"))}.get((c, l, a))


# Generated at 2022-06-14 04:34:52.825097
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test code for queries method.
    """
    ## Import package:
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    ## Set up a dummy FX rate service:
    class MockFXRateService(FXRateService):

        ## Defines a dummy FX rate for EUR/USD:
        rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date(2017, 1, 1), Decimal("1.0"))

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass


# Generated at 2022-06-14 04:35:03.137230
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .dates import Dates
    from .fxrates import FXRateService

    from decimal import Decimal

    # A service that return a single FX rate:
    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(Currencies["EUR"], Currencies["USD"], Dates.min, Decimal("2"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            raise NotImplementedError()

    # Setup a test service:
    test_service = TestFXRateService()

    # Query a single rate:

# Generated at 2022-06-14 04:35:15.831777
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency, Currencies
    from .temporal import Date, now, today

    class TestService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1.254")) if ccy1 == ccy2 else None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            r = []
            for ccy1, ccy2, asof in queries:
                r.append(self.query(ccy1, ccy2, asof))
            return r

    ts = TestService()

# Generated at 2022-06-14 04:35:28.035127
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import datetime
    from decimal import Decimal
    import sys
    import tempfile
    import unittest
    from os.path import join
    from pypara.calendars import Temporal
    from pypara.currencies import Currencies
    from pypara.commons.monads import Some, NoneType
    from pypara.marketdata.fxrate import FXRateService
    from pypara.marketdata.fxrates.xrate import XRate

    ## Create the test class:
    class Test(unittest.TestCase):

        ## The FX Rate service
        fxrs = None

        ## The temporal dimensions/dates for the rates:
        dates = [datetime(2019,1,1), datetime(2019,1,2), datetime(2019,1,3)]

        ## The FX rates:
       

# Generated at 2022-06-14 04:35:28.737241
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:35:36.528260
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance import FXRate

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"]:
                if asof == datetime.date(2018, 12, 1):
                    return FXRate(Currencies["USD"], Currencies["EUR"], datetime.date(2018, 12, 1), Decimal("0.5"))

# Generated at 2022-06-14 04:35:49.294038
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curve import Curve
    from pypara.fx import FXRateService
    from pypara.time import Temporal

    class FXRateServiceMock(FXRateService):
        def __init__(self):
            super().__init__()
            self.fx_rates = Curve("fx_rates")
            self.fx_rates.set(
                Temporal("2001-01-01"), Decimal("1.1"), Currencies["EUR"], Currencies["USD"])
            self.fx_rates.set(
                Temporal("2001-01-01"), Decimal("1.2"), Currencies["EUR"], Currencies["GBP"])

# Generated at 2022-06-14 04:36:02.787877
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    print("Executing test_FXRateService_query")

    from decimal import Decimal
    from pypara.temporal import DATE_TODAY
    from pypara.currencies import Currencies
    from pypara.exchange import FXRates
    from pypara.exchange import FXRateService

    fxrate = FXRate(Currencies["EUR"], Currencies["USD"], DATE_TODAY, Decimal("2"))
    fxrates = FXRates()
    fxrates.register(fxrate)
    service = FXRateService.from_FXRates(fxrates)
    rate = service.query(Currencies["EUR"], Currencies["USD"], DATE_TODAY)

    assert fxrate == rate


# Generated at 2022-06-14 04:36:20.190661
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .services.dummy import DummyFXRateService
    from .currencies import Currencies
    from .zeitgeist import Date

    ## Create a dummy FX rate service:
    service = DummyFXRateService()

    ## Create the queries:
    q1 = (Currencies["USD"], Currencies["TRY"], Date.from_isoformat("2019-10-01"))
    q2 = (Currencies["USD"], Currencies["TRY"], Date.from_isoformat("2019-10-02"))
    q3 = (Currencies["USD"], Currencies["TRY"], Date.from_isoformat("2019-10-03"))
    queries = [q1, q2, q3]

    ## Query for FX rates:

# Generated at 2022-06-14 04:36:23.264387
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the functionality of the method `query` of class :class:`FXRateService`.
    """
    # TODO: Implement unit test.
    pass

# Generated at 2022-06-14 04:36:34.177867
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currency, Currencies
    from pypara.rates.fx import FXRateService
    class FXRateService(FXRateService):
        queries = FXRateService.queries
        def query(self, ccy1: Currency, ccy2: Currency, asof: date, strict: bool = False) -> Optional[FXRate]:
            if (ccy1, ccy2, asof) == (Currencies["EUR"], Currencies["USD"], date(2020, 1, 1)):
                return FXRate(ccy1, ccy2, asof, Decimal("1.3333"))
            if (ccy1, ccy2, asof) == (Currencies["EUR"], Currencies["USD"], date(2020, 3, 26)):
                return

# Generated at 2022-06-14 04:36:45.259131
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.forex import FXRateLookupError, FXRateService

    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return ccy1 + ccy2

        def queries(self, queries, strict=False):
            values = []
            for ccy1, ccy2, asof in queries:
                values.append(self.query(ccy1, ccy2, asof))
            return values

    test_fx_service = TestFXRateService()
    currencies = [Currencies["EUR"], Currencies["USD"]]
    dates = [datetime.date.today()]
    rates = test_fx_service.qu

# Generated at 2022-06-14 04:36:55.431511
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    # Arrange
    service = FXRateService()  # This is not a concrete class.
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
    asof = datetime.date(2020, 1, 1)

    # Act
    rate = service.query(ccy1, ccy2, asof)

    # Assert
    assert rate is None



# Generated at 2022-06-14 04:37:04.682746
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from unittest.mock import MagicMock
    service = FXRateService()
    service.query = MagicMock(return_value = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2")))
    assert service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) == FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

# Generated at 2022-06-14 04:37:16.102518
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # A simple dummy class:
    class MyFxService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            return ccy1.is_ccy_same(ccy2) and ccy2.is_ccy_same(ccy1) and ccy1.is_ccy_same(ccy1)

        def queries(self, queries, strict=False):
            for ccy1, ccy2, asof in queries:
                yield ccy1.is_ccy_same(ccy2) and ccy2.is_ccy_same(ccy1) and ccy1.is_ccy_same(ccy1)

    # Create a fx rate service:
    service = MyFxService()

    # Create a fx rate query:

# Generated at 2022-06-14 04:37:28.685738
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.temporal import Date

    class TestRatePair(NamedTuple):
        """
        Defines a test rate pair for testing FXRateService.queries
        """

        ccy1: Currency
        ccy2: Currency
        asof: Date
        rate: Decimal

    class TestFXRateService(FXRateService):
        """
        Defines a test foreign exchange rate service for testing FXRateService.queries
        """


# Generated at 2022-06-14 04:37:36.865661
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests if method queries works as expected.
    """

    ## Import required packages:
    import datetime
    import unittest
    import warnings
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    ## Define the test case:
    class TestFXRateService(unittest.TestCase):

        """
        Defines a test case for method queries of class FXRateService.
        """

        def setUp(self):
            """
            Sets up the test.
            """
            ## Suppress the runtime warning for a missing FX rate:
            warnings.filterwarnings("ignore")

            ## Define the collection of queries:

# Generated at 2022-06-14 04:37:49.089392
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency, Currencies
    from .market import Market
    from .temporal import Date
    from .utils import TestCase

    from decimal import Decimal

    from datetime import date

    class FXRateServiceMock(FXRateService):

        def __init__(self, rates: Iterable[FXRate]) -> None:
            self.rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass


# Generated at 2022-06-14 04:38:08.265825
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.commons.zeitgeist import Date

    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal(2.0))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return map(lambda x: self.query(x[0], x[1], x[2], strict), queries)

    fxr = TestFXRateService()


# Generated at 2022-06-14 04:38:21.489192
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class Mock(FXRateService):

        @staticmethod
        def query(ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["EUR"]:
                if ccy2 == Currencies["USD"]:
                    return FXRate(ccy1, ccy2, asof, Decimal("2"))
                if ccy2 == Currencies["GBP"]:
                    return FXRate(ccy1, ccy2, asof, Decimal("0.8"))
            elif ccy1 == Currencies["USD"]:
                if ccy2 == Currencies["EUR"]:
                    return FXRate(ccy1, ccy2, asof, Decimal("0.5"))

# Generated at 2022-06-14 04:38:32.362909
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Ensures all queries are resolved correctly.
    """
    from .currencies import EUR, USD, GBP  # noqa: E402
    from .temporal import Date  # noqa: E402
    import datetime  # noqa: E402
    from .tools.decorators import lazy  # noqa: E402

    from unittest.mock import Mock, patch  # noqa: E402
    from typing import Iterable  # noqa: E402

    class MockedFXRateService(FXRateService):

        @lazy
        def _fx_rates(self) -> Iterable[FXRate]:
            import datetime  # noqa: E402


# Generated at 2022-06-14 04:38:44.447286
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """
    # pylint: disable=attribute-defined-outside-init
    from decimal import Decimal
    from unittest.mock import Mock, patch
    from .currencies import Currency

    from .currencies import Currencies as C

    from . import financial


# Generated at 2022-06-14 04:38:47.190868
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    try:
        FXRateService().query(FxRateService.Currency.EUR, FxRateService.Currency.USD, FxRateService.Temporal.today())
    except TypeError:
        pass


# Generated at 2022-06-14 04:38:59.704688
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from typing import Iterable, Optional, Tuple
    from pypara.currencies import Currencies
    from pypara.times.date import Date
    from pypara.money import Decimal
    from pypara.fxrates import FXRate, FXRateService

    class FXRateServiceImpl(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
                return FXRate(Currencies["EUR"], Currencies["USD"], asof, Decimal("1.1"))

# Generated at 2022-06-14 04:39:06.194505
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.rates import FXRate, FXRateService

    ## Define a service to use for test:
    class DummyService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == ccy2:
                return FXRate(ccy1, ccy2, date, Decimal(1))

            if ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"]:
                if asof == date:
                    return FXRate(ccy1, ccy2, asof, Decimal(1))
                else:
                    return FXRate(ccy1, ccy2, asof, Decimal(2))


# Generated at 2022-06-14 04:39:11.551516
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies

    from .commons.zeitgeist import Date

    # Test empty FXRateService:
    fxsvc = FXRateService()
    empty_rate = fxsvc.query(Currencies["EUR"], Currencies["USD"], Date())
    assert empty_rate is None



# Generated at 2022-06-14 04:39:22.840621
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService
    """
    from abc import ABC, abstractmethod
    from argparse import ArgumentParser
    from datetime import date
    from decimal import Decimal
    from functools import partial
    from typing import List
    from unittest import TestCase

    from pypara.currencies import Currency
    from pypara.temporal import Temporal
    from pypara.utils.dates import to_date

    class MockFXRateService(FXRateService):
        """
        Provides a mock foreign exchange rate service.
        """

        #: Defines the foreign exchange rates.
        rates: List[FXRate]

        #: Defines the foreign exchange rate queries.
        queries: List[MockFXRateService.TQuery]


# Generated at 2022-06-14 04:39:35.641919
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import DummyFXRateService
    fx_service = DummyFXRateService()

    ## Define test cases:

# Generated at 2022-06-14 04:39:58.378432
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService

    class TestService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate(ccy1, ccy2, asof, Decimal("2"))
            else:
                return None

        def queries(self, queries, strict):
            for query in queries:
                yield self.query(*query)


# Generated at 2022-06-14 04:40:07.785698
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the FXRateService method queries.
    """
    from .calendars import SystemCalendar
    from .currencies import Currency
    from .currencies import Currencies
    from .core import LocalDateTime
    from .temporals import Temporals
    from .temporals import Temporal
    from .zeitgeist import Date
    from .zeitgeist import IOS_DATE_FORMAT
    from collections import namedtuple
    from datetime import date
    from decimal import Decimal
    import logging
    import unittest

    ## The service log:
    log = logging.getLogger(__name__)
    log.addHandler(logging.NullHandler())

    ## The test calendar:
    calendar = SystemCalendar()

    ## Test class:

# Generated at 2022-06-14 04:40:08.908107
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:40:20.259666
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """
    from unittest import TestCase
    from unittest.mock import Mock
    from pypara.currencies import Currency
    from pypara.markets.fxtr import FXRateService, FXRateLookupError

    # Test:
    class Test(TestCase):

        def setUp(self):
            self._fxservice = FXRateService()
            self._fxservice.query = Mock()

        def test_FXRateService_query(self):
            self._fxservice.query(ccy1=Currency("TRY"), ccy2=Currency("USD"), asof="asof")

# Generated at 2022-06-14 04:40:30.297634
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Runs unit tests for the method queries of the class FXRateService.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.exchanges import GroupedFXRateService
    from pypara.temporal import Temporal
    from pypara.temporals import Temporals

    ## Define the service:

# Generated at 2022-06-14 04:40:39.974534
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    from .currencies import Currency
    from .commons.zeitgeist import Date
    from .currencies.fx.forward import ForwardFXRateService
    from .currencies.fx.pairs import FXRatePair, FXRatePairService

    ## Create an FX rate pair service:
    fxrate_pairs = [
        FXRatePair(Currency("EUR"), Currency("USD"), Date(2018, 1, 1), 4),
        FXRatePair(Currency("EUR"), Currency("USD"), Date(2018, 1, 2), 4),
        FXRatePair(Currency("EUR"), Currency("USD"), Date(2018, 1, 3), 4),
        FXRatePair(Currency("EUR"), Currency("USD"), Date(2018, 1, 4), 4),
    ]
    fxpair_service = FXRatePair

# Generated at 2022-06-14 04:40:51.254952
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """
    class FXRateServiceMock(FXRateService):
        """
        Provides a mock implementation of foreign exchange rate service.
        """

        def __init__(self, fxrates: Iterable[FXRate]) -> None:
            """
            Initializes the foreign exchange rate service mock.
            """
            self._rates = dict(((rate[0], rate[1], rate[2]), rate) for rate in fxrates)

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """

# Generated at 2022-06-14 04:40:58.528492
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test FX rate queries in a single-thread environment.
    """
    import datetime
    from decimal import Decimal

    from pypara.currencies import Currencies
    from .services import SingleThreadFXRateService

    ## Create a service instance:
    service = SingleThreadFXRateService()

    ## Try with empty queries:
    assert list(service.queries([])) == []

    ## Try with queries:
    assert list(service.queries([(Currencies["EUR"], Currencies["USD"], datetime.date.today())])) == [
        FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("1.1389"))
        ]

    ## Try with queries:

# Generated at 2022-06-14 04:41:03.061176
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from collections import namedtuple
    from pypara.currencies import Currencies

    class _SimpleFXRateService(FXRateService): # noqa: W0212
        def __init__(self):
            self._rates = {(Currencies["EUR"], Currencies["USD"]): Decimal("2")}

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            rate = self._rates.get((ccy1, ccy2))
            if rate is not None:
                return FXRate(ccy1, ccy2, asof, rate)
            if strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            return None


# Generated at 2022-06-14 04:41:03.887896
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query.
    """
    pass


# Generated at 2022-06-14 04:41:47.080401
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the query method of FXRateService.
    """
    pass



# Generated at 2022-06-14 04:41:52.119931
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.currencies.fx import SimpleFXRateService

    # Create the FX rate service
    service = SimpleFXRateService()

    # Add a rate
    service.add(Currencies["EUR"], Currencies["USD"], date = "2018-07-04", value = Decimal("1.18"))

    # And query the same rate
    rate = service.query(Currencies["EUR"], Currencies["USD"], date = "2018-07-04")

    # Test result
    assert isinstance(rate, FXRate)
    assert rate.ccy1 == Currencies["EUR"]
    assert rate.ccy2 == Currencies["USD"]
    assert rate.date == "2018-07-04"

# Generated at 2022-06-14 04:42:01.754411
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    import datetime
    from decimal import Decimal
    from unittest import TestCase, main
    from unittest.mock import Mock
    from pypara.time.temporal import Temporal

    ## Define the test service:
    class MyService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            assert len(queries) == 6
            return [None] * 6

    ## Create a mock to be used as Temporal
    temporal_mock = Mock(spec=Temporal)

# Generated at 2022-06-14 04:42:10.871179
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests :method:`FXRateService.queries` method.
    """
    ### Define the FX rate service:
    class __MockFXRateService(FXRateService):
        """
        Provides a mock implementation of :class:`FXRateService`.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, ONE) if ccy1 == ccy2 else None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for query in queries:
                yield self.query(*query)

    ### Create the service and define the queries:
    service = __MockFXRateService

# Generated at 2022-06-14 04:42:11.990638
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass



# Generated at 2022-06-14 04:42:24.153031
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from ..currencies import Currencies
    from ..temporal import Temporal
    from .commons.numbers import ONE
    import datetime
    from decimal import Decimal

    class EURUSD(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Decimal:
            if asof.date == datetime.date(2019, 1, 6):
                if ccy1 == Currencies["EUR"] \
                        and ccy2 == Currencies["USD"]:
                    return Decimal("1.13")
                elif ccy1 == Currencies["USD"] \
                        and ccy2 == Currencies["EUR"]:
                    return ONE / Decimal("1.13")

# Generated at 2022-06-14 04:42:32.584700
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest.mock import Mock

    from pypara.currencies import Currencies

    ## Create a mocked service:
    service = Mock(spec=FXRateService)
    expected_rates = [
        FXRate(Currencies["EUR"], Currencies["USD"], Date("2017-06-30"), Decimal("1.6")),
        FXRate(Currencies["USD"], Currencies["EUR"], Date("2017-06-30"), Decimal("0.6")),
        FXRate(Currencies["USD"], Currencies["GBP"], Date("2017-06-30"), Decimal("0.75")),
        FXRate(Currencies["GBP"], Currencies["USD"], Date("2017-06-30"), Decimal("1.33"))
    ]
    service.queries.return_value = expected_rates

    ## Create a collection

# Generated at 2022-06-14 04:42:43.245064
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    # Test no implementation
    try:
        # Test no implementation
        FXRateService.default.query(Currency.of("EUR"), Currency.of("USD"), Date.today(is_holiday=True))

    except TypeError as e:
        key = "query"
        assert key in str(e)

    # Test implementation
    class FXRateServiceBaby(FXRateService):

        #: Defines the default foreign exchange rate service for the runtime.
        default: Optional["FXRateServiceBaby"] = None

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate.of(ccy1, ccy2, asof, Decimal("1.0000"))


# Generated at 2022-06-14 04:42:52.843568
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.exchange import FXRateLookupError
    import datetime

    class FXRateServiceMock(FXRateService):
        def __init__(self):
            self._rates = {
                ("EUR", "USD", datetime.date(2018, 9, 1)): Decimal("1.2"),
                ("EUR", "USD", datetime.date(2018, 9, 3)): Decimal("1.3"),
                ("EUR", "USD", datetime.date(2018, 9, 5)): Decimal("1.4"),
            }


# Generated at 2022-06-14 04:43:04.136893
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate
    from pypara.fxrates.services import InMemoryFXRateService

    ## Initialize the service:
    service = InMemoryFXRateService()

    ## Insert rates:
    for ccy1 in Currencies:
        for ccy2 in Currencies:
            service.insert(FXRate(ccy1, ccy2, datetime.date.today(), Decimal("2")))

    ## Query the service: