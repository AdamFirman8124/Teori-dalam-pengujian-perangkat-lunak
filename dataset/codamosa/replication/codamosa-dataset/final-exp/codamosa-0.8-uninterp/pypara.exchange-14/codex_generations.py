

# Generated at 2022-06-14 04:34:36.409676
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    import datetime

    # Import test currency provider:
    from pypara.currencies.providers.test import TestCurrencyProvider

    # Use test provider:
    TestCurrencyProvider.default()

    # Import test FX rate provider:
    from pypara.fxrates.providers.test import TestFXRateProvider

    # Create FX rate provider:
    provider = TestFXRateProvider()

    # Get today's date
    date = datetime.date.today()

    # Test query method:
    assert provider.query(Currency("USD"), Currency("EUR"), date) == FXRate(Currency("USD"), Currency("EUR"), date, Decimal("0.9"))

# Generated at 2022-06-14 04:34:47.638985
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService.
    """

    class Dummy(FXRateService):
        """
        Dummy implementation of the FX rate service.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            return FXRate(ccy1, ccy2, asof, Decimal("2"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            """
            Returns foreign exchange rates for a given collection of currency pairs and dates.
            """
            pass

    dummy = Dummy()

# Generated at 2022-06-14 04:34:59.370947
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime as dt
    from decimal import Decimal
    from pypara.currencies import Currencies

    from pypara.fx import FXRateService

    ## Define the query:
    query = [
        (Currencies["EUR"], Currencies["USD"], dt.date.today()),
        (Currencies["EUR"], Currencies["EUR"], dt.date.today()),
        (Currencies["USD"], Currencies["EUR"], dt.date.today()),
        (Currencies["USD"], Currencies["USD"], dt.date.today()),
    ]

    ## Define the rates to be expected:

# Generated at 2022-06-14 04:35:00.108280
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    assert True

# Generated at 2022-06-14 04:35:13.692630
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """
    # noinspection PyPackageRequirements
    import unittest
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies
    from pypara.zeitgeist import LocalDate
    from pypara.fx import FXRateService

    class FXRateServiceStub(FXRateService):
        """
        Provides a dummy implementation of the FX rate service.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """

# Generated at 2022-06-14 04:35:25.946854
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency
    from .time import Date
    from .temporal import Temporal
    from .forex.ecb import ECBRateService

    ## Setup reference currency and temporal for testing:
    ccy_usd = Currency("USD")
    ccy_eur = Currency("EUR")
    ccy_gbp = Currency("GBP")
    ccy_chf = Currency("CHF")
    temporal = Temporal()

    ## Setup FX rate service:
    rate_service = ECBRateService(ccy_eur, temporal)
    FXRateService.default = rate_service

    ## Test query method with different currency pairs:
    rate = rate_service.query(ccy_eur, ccy_usd, Date.today())
    assert rate is not None


# Generated at 2022-06-14 04:35:36.175405
# Unit test for method query of class FXRateService

# Generated at 2022-06-14 04:35:47.471401
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test: pypara.finmath.fx.FXRateService.queries
    """
    ## Arrange ##

    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currencies

    class DummyFXRateService(FXRateService):
        def __init__(self, fx_rates: Optional[Iterable[FXRate]] = None):
            if fx_rates is None:
                self.rates = iter((
                    FXRate(Currencies["USD"], Currencies["EUR"], date(2019, 6, 1), Decimal("1.1234")),
                    FXRate(Currencies["EUR"], Currencies["USD"], date(2019, 6, 1), Decimal("0.8900"))))
            else:
                self.rates = iter(fx_rates)


# Generated at 2022-06-14 04:35:54.036875
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import pytest
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.temporals import Temporals
    from pypara.fx.fxrateservices import FXRateService, FXRateLookupError

    class MockService(FXRateService):
        """
        Provides a mock FX rate service.
        """

        def __init__(self, rates: Iterable[FXRate]) -> None:
            self.rates = dict(zip(((rate.ccy1, rate.ccy2, rate.date) for rate in rates), rates))


# Generated at 2022-06-14 04:36:03.504330
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    print("test_FXRateService_queries")
    test_results_list = []
    def add_result(result):
        test_results_list.append(result)
    # Test an empty sequence
    add_result(list(FXRateService.queries([])) == [])
    # Test a sequence of query tuples with different lengths
    add_result(list(FXRateService.queries([
        (None, None, None),
        (None, None),
        (None, None, None, None)
    ])) == [None] * 3)
    assert all(test_results_list)
    print("    passed")

# Generated at 2022-06-14 04:36:20.493920
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the :method:`FXRateService.queries` method.
    """
    try:
        from decimal import Decimal
        from unittest import TestCase
        from pypara.currencies import Currency, Currencies
        from pypara.utils.zeitgeist import Date
    except ImportError:
        return

    class TestedService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal(1))

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return FXRateService.queries(self, queries, strict)

# Generated at 2022-06-14 04:36:32.654953
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest.mock import MagicMock
    from typing import List  # noqa: F401 (import only used in type hints)

    # Initialize an FX rate service:
    service = MagicMock(FXRateService)

    # Create an FX rate service mock:
    @service.queries.side_effect
    def mock_queries(queries: List[FXRateService.TQuery], strict: bool) -> List[Optional[FXRate]]:
        return [None for _ in queries]

    # Define a reference query:
    from .currencies import Currencies
    from .commons.zeitgeist import now
    ref_query = (Currencies["EUR"], Currencies["USD"], now())

    # Invoke the method:
    rates = service.queries(queries=[ref_query])

    # Check the results

# Generated at 2022-06-14 04:36:43.877773
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Test for method query of class `FXRateService`.
    """

    ## Import libraries:
    import unittest
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies  # noqa: E402
    from pypara.temporal import Date

    ## Define a rate:
    rate = FXRate(Currencies["EUR"], Currencies["USD"], Date.today(), Decimal("2"))

    ## Define a FX rate service:
    class Test(FXRateService):
        """
        Defines a test foreign exchange rate service.
        """

        def query(self, ccy1, ccy2, asof, strict=False):
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """

# Generated at 2022-06-14 04:36:53.207719
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRate

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == date(2019, 1, 1):
                return FXRate(Currencies["EUR"], Currencies["USD"], date(2019, 1, 1), Decimal("1.2500"))

# Generated at 2022-06-14 04:36:55.838021
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 04:37:02.806920
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests :method:`FXRateService.queries`.
    """
    from collections import namedtuple

    from .currencies import Currencies

    from datetime import date

    from decimal import Decimal

    from unittest import mock
    from unittest.mock import MagicMock

    ## Create a dummy FX rate service
    class DummyService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict: bool = False):
            pass

        def queries(self, queries: Iterable[TQuery], strict: bool = False):
            return queries

    service = DummyService()

    ## Create some currency pairs and dates:
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
    asof = date.today()

    ## Test the queries

# Generated at 2022-06-14 04:37:15.451058
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate, FXRateLookupError, FXRateService

    class ForeignExchangeRateService(FXRateService):
        """
        Provides an implementation of the foreign exchange rate service.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            """
            Returns foreign exchange rates for a given collection of currency pairs and dates.
            """
            return []

   

# Generated at 2022-06-14 04:37:18.286083
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:37:29.223548
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.rates.amsr import AbstractMarketServiceRate
    from pypara.rates.fxrateservices import DefaultFXRateService
    s = DefaultFXRateService.instance("pypara.rates.amsr.AbstractMarketServiceRate")
    r = s.query(Currencies["EUR"], Currencies["USD"], datetime.date.today(), strict=False)
    assert r.ccy1 == AbstractMarketServiceRate.EUR
    assert r.ccy2 == AbstractMarketServiceRate.USD
    assert r.date == datetime.date.today()
    assert r.value == Decimal("1.1843")


# Generated at 2022-06-14 04:37:30.959854
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the method query of the abstract class FXRateService.
    """
    pass


# Generated at 2022-06-14 04:37:40.187288
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the implementation of method queries of class FXRateService.
    """
    ## TODO: Write unit test
    pass


# Generated at 2022-06-14 04:37:51.499048
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest.mock import MagicMock, PropertyMock, call

    fx = MagicMock(spec=FXRateService)
    q1 = (Currency("EUR"), Currency("USD"), Date.today())
    q2 = (Currency("USD"), Currency("EUR"), Date.today())
    q3 = (Currency("GBP"), Currency("USD"), Date.today())
    type(fx).queries = MagicMock(side_effect=[(1, 2, 3), (4, 5, 6)])

    result = fx.queries([q1, q2, q3], False)
    fx.queries.assert_has_calls([
        call([q1, q2, q3], False),
        call([q3], False)])

# Generated at 2022-06-14 04:38:05.300269
# Unit test for method query of class FXRateService
def test_FXRateService_query():

        from pypara.currencies import Currencies
        from pypara.currencies import Currency
        from pypara.currencies import CurrencyMismatchError
        from pypara.currencies import FXRateService
        from pypara.currencies import FXRateLookupError
        from pypara.currencies import ONE
        from pypara.currencies import TEN
        from pypara.currencies import ZERO
        from pypara.currencies import Date
        from pypara.currencies import Decimal

        class TestingFXRateService(FXRateService):

            def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
                if ccy1 != ccy2:
                    raise NotImplementedError
                else:
                    return FXRate

# Generated at 2022-06-14 04:38:13.264530
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import os

    from decimal import Decimal
    from dateutil.parser import parse as parse_date
    from pypara.currencies import Currencies
    from pypara.external.fxrates import FXRateService, FXRateServiceFactory

    FACTORY = FXRateServiceFactory()

    ## Get the test data:
    with open(os.path.dirname(__file__) + "/testdata/fxrates.csv", "r") as file:
        test_data = [line.rstrip() for line in file]
        test_data.pop(0)

    ## Get the exchange rate service:
    service = FACTORY.get_service("FIXING")

    # Run the test
    for line in test_data:
        ccy1, ccy2, asof, value = line.split(",")
        rate1 = service

# Generated at 2022-06-14 04:38:16.898460
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency

    # Test constructors
    assert FXRateService().query(Currency("USD"), Currency("EUR"), Date(1)) == None, "default implementation"

# Generated at 2022-06-14 04:38:26.391484
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class TestFXRateService(FXRateService):
        """
        Provides a test implementation of the :class:`FXRateService`.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """

# Generated at 2022-06-14 04:38:36.209600
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.currencies.conversions import FXRateService as BaseFXRateService
    from pypara.currencies.conversions import FXRate

    ## Define a dummy FX rate service:
    class FXRateService(BaseFXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies['EUR'] and ccy2 == Currencies['USD'] and asof == date.today():
                return FXRate(ccy1, ccy2, asof, Decimal('2'))
            else:
                return None


# Generated at 2022-06-14 04:38:38.914781
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .fxrates import FXRateServiceDummy
    assert FXRateServiceDummy().query(None, None, None) == None


# Generated at 2022-06-14 04:38:46.038550
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from typing import List, Iterable
    from pypara.currencies import Currencies
    from pypara.finance.defaults import DefaultFXRateService as FXRS

    ## Setup
    queries: List[FXRateService.TQuery] = [
        (Currencies["EUR"], Currencies["USD"], datetime.date.today()),
        (Currencies["USD"], Currencies["EUR"], datetime.date.today()),
        (Currencies["USD"], Currencies["USD"], datetime.date.today()),
        (Currencies["TRY"], Currencies["EUR"], datetime.date.today()),
    ]  # type: List[FXRateService.TQuery]
    rates: Iterable[Optional[FXRate]] = FXRS.queries(queries)

    ##

# Generated at 2022-06-14 04:38:58.809656
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.core.fxrates import FXRate, FXRateService


# Generated at 2022-06-14 04:39:21.907281
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """
    from .exchange import FXRateServices

    ## Pairs and dates:
    ccy12_ = list(zip(["USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD", "USD"], ["JPY", "EUR", "USD", "TRY", "CNY", "AUD", "GBP", "MXN", "CAD", "CZK"]))

# Generated at 2022-06-14 04:39:28.333557
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the query method of FXRateService
    """
    from decimal import Decimal

    from pypara.currencies import Currency
    from pypara.currencies.ccy_codes import CCYCodes
    from pypara.currencies.temporal import Temporal
    from pypara.service_providers.fx_rates import FXRateService

    # Define FX rate queries:
    queries = [
        (Currency(CCYCodes.USD), Currency(CCYCodes.EUR), Temporal.now()),
        (Currency(CCYCodes.EUR), Currency(CCYCodes.USD), Temporal.now())
    ]
    # Define FX rates:

# Generated at 2022-06-14 04:39:37.687009
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the fx rate service query method.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.currencies.exchange.rates import FXRateService

    ## Define some local objects:
    urate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

    ## Define a mocker:
    class Mocker(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return urate

    ## Test the query():
    foo = Mocker()
    assert foo.query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) == urate

# Generated at 2022-06-14 04:39:45.954897
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.dates import Temporal
    from .services import FXRateService as FX, FXRateServices


# Generated at 2022-06-14 04:39:56.068211
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103
    """
    Tests the method :method:`FXRateService.query`.
    """
    ## Define some currencies:
    from .currencies import Currency
    ccy1 = Currency("EUR")
    ccy2 = Currency("USD")
    asof = Date("2019-01-01")
    strict = True
    rate = FXRate(ccy1, ccy2, asof, Decimal("2"))

    ## Define the service:
    class FXRS(FXRateService):

        def query(self, ccy1, ccy2, asof, strict = False):
            return rate
    service = FXRS()

    ## Run unit test:
    assert service.query(ccy1, ccy2, asof, strict) == rate


# Generated at 2022-06-14 04:40:06.532892
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Verifies that the method ``query`` of class :class:`FXRateService` works as expected.
    """
    from datetime import date
    from unittest import mock, TestCase, TestSuite, TextTestRunner
    from unittest.mock import Mock, call

    from pypara.currencies import Currencies
    from pypara.temporal import Date

    def create_FXRateService_subclass_no_query_stub(*args, **kwargs) -> FXRateService:
        """
        Creates a subclass of :class:`FXRateService` without the ``query`` method implemented.
        """
        class FXRateServiceSubclass(FXRateService):
            """
            Defines a subclass of :class:`FXRateService`
            """

        return FXRateServiceSubclass()


# Generated at 2022-06-14 04:40:15.526956
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import mock
    from pypara.currencies import Currency, Currencies
    from pypara.finance import FXRateService
    from pypara.temporal import Date

    instance = mock.MagicMock(spec=FXRateService)
    instance.query(Currencies["USD"], Currencies["JPY"], Date(2019, 1, 1))
    instance.query.assert_called_with(Currencies["USD"], Currencies["JPY"], Date(2019, 1, 1), strict=False)
    instance.query.assert_called_once()


# Generated at 2022-06-14 04:40:27.250725
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
            else:
                return None

        def queries(
            self,
            queries: Iterable[Tuple[Currency, Currency, Date]],
            strict: bool = False,
        ) -> Iterable[Optional[FXRate]]:
            pass

    service = TestFX

# Generated at 2022-06-14 04:40:36.674552
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest import TestCase, mock

    from pypara.currencies import Currencies
    from pypara.temporal import Dates

    class MockFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, 1)

    # test with strict=True
    with TestCase.assertRaises(TestCase, FXRateLookupError):
        queries = [(Currencies["EUR"], Currencies["USD"], Dates.bad), (Currencies["EUR"], Currencies["USD"], Dates.today)]
        MockFXRateService().queries(queries, strict=True)

    # test with strict=False

# Generated at 2022-06-14 04:40:45.887144
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import pytest
    from pypara.currencies import Currencies
    from pypara.temporals import AsOf
    from .rates import InMemoryFXRateService

    ## Create an iterable of queries:
    queries = [
        (Currencies["EUR"], Currencies["USD"], AsOf(2017, 1, 3)),
        (Currencies["USD"], Currencies["EUR"], AsOf(2017, 1, 3)),
        (Currencies["EUR"], Currencies["USD"], AsOf(2017, 1, 1)),
        (Currencies["USD"], Currencies["EUR"], AsOf(2017, 1, 1)),
        (Currencies["EUR"], Currencies["USD"], AsOf(2017, 1, 2)),
        (Currencies["USD"], Currencies["EUR"], AsOf(2017, 1, 2))
    ]

    ##

# Generated at 2022-06-14 04:41:27.172613
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # Pass a bogus service to test :meth:`FXRateService.query`:
    class BogusService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

    # Should raise a :class:`LookupError` exception:
    if FXRateService.default is not None:
        try:
            FXRateService.default.query(
                Currency("EUR"),
                Currency("USD"),
                Date.today(),
                True
            )
            assert False
        except LookupError:
            assert True
        except Exception:  # noqa: E722
            assert False  # pragma: no cover

# Generated at 2022-06-14 04:41:36.517552
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class FXRateService.
    """

    ## Import in local scope:
    from decimal import Decimal
    from unittest import TestCase, mock
    from pypara.currencies import Currencies

    class _TestableFXRateService(FXRateService):
        """
        This class is used for testing :class:`FXRateService`.
        """

        def __init__(self):
            """
            Initializes testable FX rate service.
            """
            self.rate = FXRate.of(Currencies["EUR"], Currencies["USD"], Date(2017, 12, 31), Decimal("1.13"))


# Generated at 2022-06-14 04:41:47.638345
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Provides unit test for the method ``queries`` of the class :class:`FXRateService`.
    """

    from .instruments.interest_rate import TTemporal
    from .utils import nullable
    
    class DummyService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return next(self.queries(((ccy1, ccy2, asof),)))


# Generated at 2022-06-14 04:41:59.097893
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries for class FXRateService.
    """
    # pylint: disable=too-few-public-methods, no-init

    from unittest.mock import MagicMock

    from .commons.zeitgeist import Date

    from .currencies import Currency

    from .fxrates import FXRate, FXRateService

    # Define the default FX rate service
    FXRateService.default = MagicMock(FXRateService)

    # Define the expected values
    eur = Currency("EUR", 0)
    usd = Currency("USD", 1)

    today = Date.today()

    eur_usd = FXRate.of(eur, usd, today, Decimal("1.5"))

    # Define the mock behavior

# Generated at 2022-06-14 04:42:09.992368
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curves import CurveService

    class MyFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict: bool = False):
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"] and asof == datetime.date.today():
                return FXRate(ccy1, ccy2, asof, Decimal("2"))
            return None

        def queries(self, queries, strict: bool = False):
            import datetime
            from decimal import Decimal
            from pypara.currencies import Currencies

            currencies = [tup[0] for tup in queries]

# Generated at 2022-06-14 04:42:22.323547
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService
    """
    import datetime
    from decimal import Decimal
    from unittest import mock
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService
    from pypara.fxrates.busas import BusaFXRateService

    # Test with an empty query
    ccy1 = Currencies["AED"]
    ccy2 = Currencies["AUD"]
    asof = datetime.date.today()
    strict = True
    fxrate = BusaFXRateService().query(ccy1, ccy2, asof, strict)
    assert (fxrate is None) == True

    # Test with a non-empty query
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
   

# Generated at 2022-06-14 04:42:31.377000
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): # noqa: D102
    from .currencies import Currencies
    from .zeitgeist import Date
    ## Should return an empty iterable for an empty input:
    assert list(FXRateService.default.queries([])) == []
    ## Should return None for missing rates:
    assert tuple(FXRateService.default.queries(
        [(Currencies["USD"], Currencies["USD"], Date.today())])) == (None,)
    ## Should return the exact rates:

# Generated at 2022-06-14 04:42:37.358367
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curves import NullTemporal
    from pypara.temporal import Date

    ## Create a dummy FX rate service:

# Generated at 2022-06-14 04:42:49.699528
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .commons.zeitgeist import now
    from .currencies import Currencies
    from .services import FOREX
    assert FOREX.query(Currencies["EUR"], Currencies["USD"], now()).value > Decimal(0)
    assert FOREX.query(Currencies["EUR"], Currencies["USD"], now(), strict=True).value > Decimal(0)
    try:
        FOREX.query(Currencies["EUR"], Currencies["USD"], now() + 100)
        assert False, "Query of FXRateService must return None if the foreign exchange rate is not found."
    except FXRateLookupError:
        assert True

# Generated at 2022-06-14 04:43:02.696544
# Unit test for method queries of class FXRateService