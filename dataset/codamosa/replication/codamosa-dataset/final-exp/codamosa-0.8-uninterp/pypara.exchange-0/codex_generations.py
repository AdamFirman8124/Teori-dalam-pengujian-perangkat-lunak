

# Generated at 2022-06-14 04:34:29.842091
# Unit test for constructor of class FXRateLookupError
def test_FXRateLookupError():
    import datetime
    from pypara.currencies import Currencies
    error = FXRateLookupError(Currencies["EUR"], Currencies["USD"], datetime.date.today())
    assert error.ccy1 == Currencies["EUR"]
    assert error.ccy2 == Currencies["USD"]
    assert error.asof == datetime.date.today()
    assert error.args == (f"Foreign exchange rate for EUR/USD not found as of {datetime.date.today()}",)


# Unit tests for class FXRate

# Generated at 2022-06-14 04:34:40.650693
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx.rates import FXRate, FXRateService
    
    
    
    class FXRateStore(FXRateService):
    
        def __init__(self, rates: Iterable[FXRate]) -> None:
            self._rates = {
                (rate.ccy1, rate.ccy2, rate.date): rate
                for rate in rates
            }
    
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == ccy2:
                return FXRate(ccy1, ccy2, asof, ONE)

# Generated at 2022-06-14 04:34:49.612754
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest import TestCase, main
    from pypara.currencies import Currencies
    from pypara.dates import Date

    class TestFXRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"] and asof == Date.today():
                return FXRate(ccy1, ccy2, asof, ONE)
            return None

        def queries(self, queries, strict=False):
            fxrates = [self.query(ccy1, ccy2, asof) for ccy1, ccy2, asof in queries]
            return fxrates

    service = TestFXRateService()

# Generated at 2022-06-14 04:34:54.853588
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """

    from .currencies import Currency
    from .temporal import Date
    from decimal import Decimal
    from pypara.finance.fxrateservice import FXRateService

    class MockService(FXRateService):
        """
        Provides a mock implementation of the FXRateSerivce abstract class.
        """

        def __init__(self, rates: dict) -> None:
            """
            Initializes the mock.
            """
            self.__rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[Decimal]:
            """
            Returns an FX rate from the mock.
            """
            ## Prepare a key for the FX rate:

# Generated at 2022-06-14 04:34:59.851393
# Unit test for constructor of class FXRateLookupError
def test_FXRateLookupError():
    from .currencies import Currencies
    from .zeitgeist import Date
    try:
        raise FXRateLookupError(Currencies["EUR"], Currencies["USD"], Date.today())
    except FXRateLookupError as error:
        print(error)


# Generated at 2022-06-14 04:35:02.095802
# Unit test for constructor of class FXRateLookupError
def test_FXRateLookupError():
    from decimal import Decimal
    from pypara.currencies import Currency

    ccy1 = Currency("EUR")
    ccy2 = Currency("TRY")
    asof = Date(datetime.date.today())
    rate = FXRate(ccy1, ccy2, asof, Decimal("2"))

    print(rate)
    print(~rate)

# Generated at 2022-06-14 04:35:10.166110
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService.
    """
    from .currencies import Currency
    from .fx import FXRateService
    from .temporal import Temporal
    from .types import Kind

    class MockRateService(FXRateService):
        """
        Provides a mock FX rate service
        """


# Generated at 2022-06-14 04:35:13.456375
# Unit test for constructor of class FXRateLookupError
def test_FXRateLookupError():
    from .currencies import Currencies

    try:
        raise FXRateLookupError(Currencies["EUR"], Currencies["USD"], Date.today())
    except FXRateLookupError as e:
        assert str(e) == "Foreign exchange rate for EUR/USD not found as of today"
    except:
        assert False, "Unexpected exception was raised."


# Generated at 2022-06-14 04:35:18.447600
# Unit test for constructor of class FXRateLookupError
def test_FXRateLookupError():
    """
    Tests constructor of class FXRateLookupError.
    """
    import datetime
    from pypara.currencies import Currencies
    err = FXRateLookupError(Currencies["GBP"], Currencies["USD"], datetime.datetime.now())
    assert str(err)[:15] == "Foreign exchange"

# Generated at 2022-06-14 04:35:30.583880
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests for :method:`FXRateService.queries` method.
    """

    from .currencies import Currencies
    from .temporal import Date, Temporal

    import datetime

    ## Create a sample set of queries:

# Generated at 2022-06-14 04:35:37.933677
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:35:50.186700
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .mocks.fxrate import DummyFXRateService
    from .currencies import EUR, USD
    from .temporal import Date

    svc = DummyFXRateService(EUR, USD, 1.333, Date(2019, 1, 1))

    assert svc.query(EUR, USD, Date(2019, 1, 1)) == FXRate(EUR, USD, Date(2019, 1, 1), 1.333)
    assert svc.query(USD, EUR, Date(2021, 2, 2)) == FXRate(USD, EUR, Date(2019, 1, 1), 1 / 1.333)
    assert svc.query(EUR, USD, Date(2021, 2, 2)) == None
    assert svc.query(USD, EUR, Date(2021, 2, 2), strict=True) is None

#

# Generated at 2022-06-14 04:36:03.661902
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Performs unit test for method query of class FXRateService.
    """
    import unittest
    import datetime

    from decimal import Decimal

    from pypara.currencies import Currencies

    ## Anonymous subclass for the unit test:
    class T(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal("2"))

    ## Setup the test:
    fx = T()

    ## Define the test cases:

# Generated at 2022-06-14 04:36:15.100413
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    from pypara.currencies import Currencies
    from pypara.tools import FXRateService

    ##
    class MyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional["FXRate"]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
                if asof == date(2019, 1, 1): return FXRate(Currencies["EUR"], Currencies["USD"], date(2019, 1, 1), Decimal("1.1"))

# Generated at 2022-06-14 04:36:27.514548
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    import unittest
    import os
    import csv
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.rates.fx import FXRateService

    ## Define a test dataset:

    ## ... an iterable of rate queries:
    queries = (
        (Currencies["EUR"], Currencies["USD"], datetime.date(year=2017, month=12, day=31)),
        (Currencies["EUR"], Currencies["USD"], datetime.date(year=2018, month=12, day=31)),
        (Currencies["EUR"], Currencies["USD"], datetime.date(year=2019, month=12, day=31)),
    )

    ## ... an iterable of expected results:

# Generated at 2022-06-14 04:36:30.821881
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the query method of the :class:`FXRateService` class.
    """
    pass


# Generated at 2022-06-14 04:36:38.056372
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.fxtypes.fxrateservices import InMemoryFXRateService


    fx_rate_service = InMemoryFXRateService({("EUR", "USD", Date("2018-12-20")): Decimal("1.14")})
    assert fx_rate_service.query("EUR", "USD", Date("2018-12-20")) == Decimal("1.14")


# Generated at 2022-06-14 04:36:48.294318
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method `queries` of class `FXRateService`.
    """
    from datetime import date
    from decimal import Decimal
    from unittest import TestCase
    from pypara.currencies import Currency, Currencies
    from pypara.fx import FXRateService

    ## The test rates:

# Generated at 2022-06-14 04:36:59.591014
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currency("EUR") and ccy2 == Currency("USD") and asof == Date(2019, 11, 1):
                return FXRate(ccy1, ccy2, asof, Decimal("2"))
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for ccy1, ccy2, asof in queries:
                yield self.query(ccy1, ccy2, asof)

    service = TestFXRateService()

# Generated at 2022-06-14 04:37:13.054819
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.ccys.fx import FXRateService

    ## Local service that provides EUR/USD rate as of 2019-12-02:
    class LocalService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date(2019, 12, 2):
                return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date(2019, 12, 2), Decimal("1.10"))

        def queries(self, queries, strict=False):
            pass

    ## Local service that provides EUR/USD rate as of 2019-12-01:
   

# Generated at 2022-06-14 04:37:32.198421
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import unittest

    from .currencies import Currencies
    from .temporal import Temporal
    from .utils import run_test

    # noinspection PyUnusedLocal
    @run_test
    class TestFXRateService_queries(unittest.TestCase):
        """
        Tests :method:`FXRateService.queries`.
        """

        class MockFXRateService(FXRateService):
            """
            Provides a mock FX rate service.
            """

            # noinspection PyMethodMayBeStatic
            def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
                return None


# Generated at 2022-06-14 04:37:33.649032
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # TODO: Implement.
    pass


# Generated at 2022-06-14 04:37:46.653264
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporals import Temporals, TimePoint
    from .finance.fxrates import FXRateService

    class DummyFXRateService(FXRateService):
        """
        Dummy FX rate service class for unit testing.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return list(None for _ in queries)

    assert(list(DummyFXRateService().queries([(Currencies["EUR"], Currencies["USD"], Date.today())])) == [None])

# Generated at 2022-06-14 04:37:57.049326
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.portfolio import FXRate

    ## Create the test instance:
    class Test(FXRateService):
        """
        Provides an FX rate service for testing purposes.
        """

# Generated at 2022-06-14 04:38:06.178699
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from ...currencies import Currency, Currencies
    from ...temporal import Date

    class CurrencyRateFXService(FXRateService):
        """
        Defines a foreign exchange rate service that provides a constant FX rate.

        **Implementation Note:**

        The reason for defining this class is to unit test method query of class FXRateService.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 != Currencies["EUR"]:
                raise ValueError("ccy1 must be EUR.")
            if ccy2 != Currencies["USD"]:
                raise ValueError("ccy2 must be USD.")
            return FXRate(Currencies["EUR"], Currencies["USD"], asof, Decimal(1.5))


# Generated at 2022-06-14 04:38:11.768577
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies
    from pypara.temporal import Dates

    assert FXRateService().query(Currencies["USD"], Currencies["EUR"], Dates.today(), True) == None

# Generated at 2022-06-14 04:38:19.669113
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests if method queries of class FXRateService works as expected.
    """
    # Ensure a default FX rate provider has been set:
    if FXRateService.default is None:
        raise AssertionError("Default FX rate provider has not been set.")

    # Ensure the natural EUR/USD FX rate is found:
    result = next(iter(FXRateService.default.queries(((Currency("EUR"), Currency("USD"), Date.today()),))))
    assert isinstance(result, FXRate)
    assert result.ccy1 == Currency("EUR")
    assert result.ccy2 == Currency("USD")
    assert result.date == Date.today()
    assert result.value > ONE

    # Ensure an inverted EUR/USD FX rate is found:

# Generated at 2022-06-14 04:38:30.901992
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import pytest
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies
    from pypara.exchanges import FXRate
    from pypara.sources import MemoryFXRateService

    ## Create a memory FX rate service:
    service = MemoryFXRateService()

    ## Extend the service with data:
    service.bootstrap(
        [
            FXRate(Currencies["USD"], Currencies["EUR"], Date(2012, 6, 1), Decimal("0.8")),
            FXRate(Currencies["USD"], Currencies["EUR"], Date(2012, 7, 1), Decimal("0.81")),
        ]
    )

    ## Validate our results:

# Generated at 2022-06-14 04:38:43.552914
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.temporals import Date
    from unittest import TestCase
    from unittest.mock import MagicMock

    # Local imports:
    from pypara.services.fx_rates.base import FXRateLookupError, FXRateService

    # Mock a foreign exchange rate service:
    mock_service = MagicMock(spec=FXRateService)
    mock_service.query.side_effect = [None, FXRate(Currencies["EUR"], Currencies["USD"], Date.today(), Decimal("2"))]

    # Null response:
    assert mock_service.query(Currencies["EUR"], Currencies["USD"], Date.today(), True) is None

# Generated at 2022-06-14 04:38:55.560144
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """
    from decimal import Decimal, ROUND_HALF_UP
    import datetime
    from pypara.currencies import Currency
    from pypara.exchanges.rates import FXRate, FXRateLookupError, FXRateService
    from pypara.temporal import Date

    class TestFXRateService(FXRateService):
        """
        Provides a test FX rate service.
        """

        def __init__(self):
            # Define some FX rates
            self.eurjpy = FXRate(Currency.of("EUR"), Currency.of("JPY"), Date.of(datetime.date(2020, 1, 1)), Decimal("13.0000"))

# Generated at 2022-06-14 04:39:19.032980
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import TestCase, skip
    from pypara.services.timeaware import TestTimeAwareService
    from pypara.services.stub import FXRateStubService

    class Test(TestCase):
        def test_FXRateStubService_query(self):
            service = FXRateStubService()
            rate = service.query("CAD", "USD", "2020-01-01")
            assert(rate.value == Decimal("0.95"))

        @skip("TODO")
        def test_FXRateService_query(self):
            pass

    # Run tests:
    t = Test()
    t.test_FXRateStubService_query()
    t.test_FXRateService_query()

# Generated at 2022-06-14 04:39:26.834768
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.currencies import Currencies
    from pypara.dates import Date
    from pypara.fx.lookup import FXRateLookup
    from pypara.fx.sqlite3 import SQLite3FXRateService
    from pypara.paths import Files
    from decimal import Decimal

    fxrate = SQLite3FXRateService(Files["fx-rates"])
    rate = fxrate.query(Currencies["EUR"], Currencies["USD"], Date.today(), strict=False)
    assert rate.value != Decimal(0.0)

    rates = fxrate.queries([(Currencies["EUR"], Currencies["USD"], Date.today()), (Currencies["USD"], Currencies["EUR"], Date.today())])
    assert len(rates) == 2

    rates = FXRateLookup

# Generated at 2022-06-14 04:39:37.011541
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest.mock import MagicMock
    # Build the FX rate service mocker:
    mock_fxrate_service = MagicMock(FXRateService)
    # Build the FX rate mocker:
    mock_fxrate = MagicMock(FXRate)
    # Build the FX rate query mocker:
    mock_query = MagicMock(FXRateService.TQuery)
    # Set the query expectations:
    mock_fxrate_service.queries.side_effect = [[mock_fxrate, None]]
    # Run the queries method:
    rates = mock_fxrate_service.queries(iter([mock_query]))
    # Assert the side-effect is called with the correct argument:

# Generated at 2022-06-14 04:39:45.534827
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .datetime import Date
    from .fxrates import FXRate, FXRateService
    from .math import Decimal

    class MockFXRateService(FXRateService):
        def __init__(self):
            self.ccy1, self.ccy2, self.asof, self.rate = Currencies["USD"], Currencies["EUR"], Date.today(), Decimal("1.1")
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(self.ccy1, self.ccy2, self.asof, self.rate) if (ccy1 == self.ccy1 and ccy2 == self.ccy2 and asof == self.asof) else None



# Generated at 2022-06-14 04:39:56.652894
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """
    ## Define the lookup service:
    class FXRateLookupService(FXRateService):
        """
        Provides an FX rate lookup service.
        """

        def __init__(self, rates: Iterable[FXRate]) -> None:
            """
            Initializes the FX rate lookup service.
            """
            self.rates = rates


# Generated at 2022-06-14 04:40:06.336434
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from collections import namedtuple
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx.services import QueryTarget, FXRateDictService

    # Given a FX rate service
    ccy1, ccy2, ccy3 = Currencies["EUR"], Currencies["USD"], Currencies["TRY"]

# Generated at 2022-06-14 04:40:19.250842
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.fxrates import FXRate
    from pypara.fxrates.services import FXRateService

    class __TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal(2))


    service = __TestFXRateService()
    assert service.query(Currency("EUR"), Currency("USD"), Date(2018,1,1)) == FXRate(Currency("EUR"), Currency("USD"), Date(2018,1,1), Decimal(2))

# Generated at 2022-06-14 04:40:21.524924
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test case for method queries of class FXRateService
    """
    # Test the method under test
    assert True

# Generated at 2022-06-14 04:40:23.088206
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    assert True



# Generated at 2022-06-14 04:40:34.293827
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests a method to query multiple foreign exchange rates concurrently.
    """
    #
    # Imports:
    #
    import decimal
    import datetime
    #
    # Local imports:
    #
    from pypara.currencies import Currencies
    from pypara.finance import FXRate, FXRateService

    #
    # FX rate service:
    #
    class FXRateServiceImpl(FXRateService):
        #
        # Constructor:
        #
        def __init__(self, rates: Iterable[FXRate]) -> None:
            self.rates = dict(((x.ccy1, x.ccy2, x.date), x) for x in rates)

        #
        # FX rate query:
        #

# Generated at 2022-06-14 04:41:17.769355
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the method query of class FXRateService.
    """
    # Define a foreign exchange rate service:
    class FXRateServiceExample(FXRateService):
        """
        A sample implementation of foreign exchange rate service.
        """
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, 1.0)

        def queries(self, queries, strict=False):
            for query in queries:
                yield self.query(*query)

    from pypara.currencies import Currencies
    from pypara.date import Date

    # Define a foreign exchange rate service:
    service = FXRateServiceExample()
    # Define a currency pair:
    a = Currencies["EUR"]
    b = Currencies["USD"]

# Generated at 2022-06-14 04:41:24.454259
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance.fxrates import FXRate, FXRateService
    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
                return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
            return None

# Generated at 2022-06-14 04:41:34.951426
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Performs unit tests on the method `FXRateService.query` of the class :class:`FXRateService`.
    """
    ## Instance:
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate
    from pypara.fxrateservices import FXRateService

    ## Date:
    today = datetime.date.today()

    ## FX rates:
    eur_usd = FXRate(Currencies["EUR"], Currencies["USD"], today, Decimal("2"))
    eur_try = FXRate(Currencies["EUR"], Currencies["TRY"], today, Decimal("5.5"))

# Generated at 2022-06-14 04:41:46.830797
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """
    from decimal import Decimal
    from itertools import starmap
    from pypara.currencies import Currency, Currencies
    from pypara.datetime import Date, Temporal
    from pypara.fx.services import FXRateService, FXRateServiceCache
    from unittest import TestCase

    ## Mocks an external service:
    class FXRateServiceMock(FXRateService):
        """
        Mocks an external foreign exchange rate service.
        """


# Generated at 2022-06-14 04:41:58.952193
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .temporal import Temporal

    from datetime import date

    from decimal import Decimal

    from pypara.currencies.fx import FXRateService

    class TestService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[Decimal]:
            assert ccy1 == Currencies["EUR"]
            assert ccy2 == Currencies["USD"]
            assert asof.date == date(2020, 1, 1)
            return Decimal("2")

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[Decimal]]:
            rates = []

# Generated at 2022-06-14 04:42:09.929969
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit testing test_FXRateService_queries
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService

    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            if (ccy1, ccy2, asof) == (Currencies['EUR'], Currencies['USD'], datetime.date(2019, 1, 1)):
                return FXRate.of(Currencies['EUR'], Currencies['USD'], datetime.date(2019, 1, 1), Decimal('1.5'))

# Generated at 2022-06-14 04:42:10.528211
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass

# Generated at 2022-06-14 04:42:22.915313
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Years

    ## Empty query list:
    rate_service = lambda: None
    rate_service.queries = lambda self, queries, strict: iter(())
    assert list(rate_service().queries([], strict=False)) == []
    assert list(rate_service().queries([], strict=True)) == []

    ## Populated query list, with no result:
    rate_service = lambda: None
    rate_service.queries = lambda self, queries, strict: iter([None, None])
    assert list(rate_service().queries([(Currencies["USD"], Currencies["TRY"], Years.now()),
                                        (Currencies["TRY"], Currencies["USD"], Years.now())], strict=False)) == [None, None]

# Generated at 2022-06-14 04:42:23.569975
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:42:35.636517
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    from pypara.fx import MockFXRateService
    from pypara.currencies import Currencies
    from pypara.commons.numbers import ZERO

    # Populate the mock:
    mocksvc = MockFXRateService()
    mocksvc.append("EUR", "USD", "2019-01-01", 1.1111)
    mocksvc.append("USD", "EUR", "2019-01-01", 0.9)
    mocksvc.append("EUR", "USD", "2019-01-02", 1.2222)
    mocksvc.append("USD", "EUR", "2019-01-02", 0.8)

    # Check for USD/EUR
    assert mocksvc.query(Currencies["USD"], Currencies["EUR"], Date("2019-01-01")) == FXRate

# Generated at 2022-06-14 04:43:52.100436
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.commons.zeitgeist import Date
    from pypara.currencies import Currencies
    from pypara.data.fxrates import FXRate, FXRateService

    class TestFXRateService(FXRateService):
        """
        Provides an implementation of :class:`FXRateService` that returns predetermined data.
        """

        _rates = {}

        @classmethod
        def register(cls, rate: FXRate) -> None:
            cls._rates[(rate.ccy1, rate.ccy2, rate.date)] = rate


# Generated at 2022-06-14 04:44:01.700906
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """Test case for query method of class FXRateService."""
    from decimal import Decimal  # noqa: E402
    from datetime import date  # noqa: E402
    import pytest  # noqa: E402


    class TestFXRateService(FXRateService):
        """Provides an implementation of abstract class FXRateService."""

        _FXRATES = {
            ("EUR", "USD", date(2020, 1, 1)): Decimal("1.2000"),
            ("USD", "EUR", date(2020, 1, 1)): Decimal("0.8333"),
            ("EUR", "USD", date(2020, 1, 2)): Decimal("1.2100"),
            ("USD", "EUR", date(2020, 1, 2)): Decimal("0.8259"),
        }


# Generated at 2022-06-14 04:44:11.683974
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the :class:`FXRateService`:method:`query` method.
    """
    from datetime import date
    from decimal import Decimal, InvalidOperation
    from pypara.currencies import Currencies
    from pypara.exchangerates import FXRateService
    from pypara.exchangerates.eurofxref import EuroFXRefService

    ## Test the default foreign exchange rate service:
    FXRateService.default = EuroFXRefService("http://www.ecb.europa.eu/stats/eurofxref")

    ## Test validity:
    assert FXRateService.default.query(Currencies["EUR"], Currencies["USD"], date(2005, 9, 1)) == FXRate(Currencies["EUR"], Currencies["USD"], date(2005, 9, 1), Decimal("1.2069"))


# Generated at 2022-06-14 04:44:22.917502
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies as c
    from .commons.zeitgeist import Date as d

    class _TestService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate.of(ccy1, ccy2, asof, Decimal("2"))

        def queries(self, queries: Iterable["FXRateService.TQuery"], strict: bool = False) -> Iterable[Optional[FXRate]]:
            yield from (FXRate.of(ccy1, ccy2, asof, Decimal("2")) for ccy1, ccy2, asof in queries)

    assert isinstance(FXRateService.default, FXRateService)