

# Generated at 2022-06-14 04:34:37.437051
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency
    from .finance import FXRate
    from .temporal import Date
    from .finance import ZeroRateService

    class FXRateService(ZeroRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal("2.0")) if ccy1 == ccy2 else super().query(ccy1, ccy2, asof, strict)

    fxrate_service = FXRateService()
    fxrate = fxrate_service.query(Currency("USD"), Currency("USD"), Date("2018-01-01"))
    fxrate2 = fxrate_service.query(Currency("EUR"), Currency("USD"), Date("2018-01-01"))
    assert fxrate

# Generated at 2022-06-14 04:34:48.165261
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService.
    """
    from decimal import Decimal
    from decimal import InvalidOperation
    from pypara.currencies import Currency, CurrencyPair
    from pypara.fxtrading import FXRateService
    from pypara.temporal import Calendar, Date
    from pypara.temporal import TimeDelta
    from pypara.temporal import Temporal
    from pypara.testing import ResourceTestCase
    from unittest import TestCase

    ## Defines a dummy foreign exchange rate service:

    class DummyFXRateService(FXRateService):
        """
        Provides a dummy foreign exchange rate service.
        """

        def __init__(self, *rates: FXRate) -> None:
            """
            Initializes the dummy foreign exchange rate service.
            """
            self

# Generated at 2022-06-14 04:34:53.125694
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the :method:`FXRateService.queries` method.
    """
    from .currencies import Currency, EUR, USD
    from .fxrates import InMemoryFXRateService, FXRate
    from .commons.zeitgeist import Date

    ## Test whether an exception is raised for an invalid iterable:
    try:
        InMemoryFXRateService().queries(None)  # type: ignore
        assert False, "An exception should be raised for an invalid iterable."
    except ValueError:
        assert True

    ## Now test valid queries:
    queries = [(EUR, USD, Date.today())]

    ## Test the strict mode:

# Generated at 2022-06-14 04:35:02.531394
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test querying of an FX rate by passing a collection of queries to
    """
    from datetime import date
    from .currencies import Currencies
    from .services.fxrateservice import CachedFXRateService
    from .services.fxrateservice import DummyFXRateService

    ## Create a dummy FX rate service:
    service = DummyFXRateService()

    ## Prepare the query:
    query = (Currencies["EUR"], Currencies["USD"], date.today())

    ## Create a cached FX rate service:
    cached = CachedFXRateService(service)

    ## Execute the query:
    assert cached.queries([query]) == [service.query(*query)] * 3

# Generated at 2022-06-14 04:35:10.470093
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import TestCase

    class MockFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate.of(ccy1, ccy2, asof, Decimal(2))

        def queries(self, queries, strict=False):
            pass

    class MockCurrency(Currency):
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

        def __eq__(self, other):
            return self.name == other

        def __hash__(self):
            return hash(self.name)

    class Test(TestCase):
        def test_query_successful(self):
            fx_rate_service = MockFXRateService()
            ccy

# Generated at 2022-06-14 04:35:20.098264
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .currencies.exceptions import CurrencyLookupError
    from .currencies.registries import CurrencyRegistry
    from .temporals import Date
    from .temporals.exceptions import TemporalLookupError
    from .temporals.registries import DateRegistry
    from .temporals.units import DateUnit, Year

    # Define some test values:
    queries = (
        (Currency("EUR"), Currency("USD"), Date(2020, 1, 1)),
        (Currency("USD"), Currency("EUR"), Date(2020, 1, 1)),
        (Currency("USD"), Currency("EUR"), Date(2020, 1, 1))
    )

# Generated at 2022-06-14 04:35:31.811969
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # Import
    from decimal import Decimal
    from unittest.mock import MagicMock
    from .currencies import Currency, Currencies
    from .temporal import Temporal, Date
    from .fx import FXRate, FXRateService

    # Create a magic mock and query a single FX rate:
    service = MagicMock(spec=FXRateService)
    service.query.return_value = FXRate(Currencies["EUR"], Currencies["USD"], Date(2019, 3, 17), Decimal("1.1"))
    rate = service.query(Currencies["EUR"], Currencies["USD"], Date(2019, 3, 17))
    assert rate == FXRate(Currencies["EUR"], Currencies["USD"], Date(2019, 3, 17), Decimal("1.1"))

    # Create a magic mock and query multiple FX rates:


# Generated at 2022-06-14 04:35:45.535323
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from pypara.currencies import Currency, Currencies

    from .utils import FXRateServiceMock
    svc = FXRateServiceMock()

    ## Query for a single rate:
    assert (svc.query(Currencies["EUR"], Currencies["USD"], date(2018, 12, 31)) ==
             FXRate(ccy1=Currencies["EUR"], ccy2=Currencies["USD"], date=date(2018, 12, 31), value=1.1))

    ## Query for multiple rates:

# Generated at 2022-06-14 04:35:53.772871
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency

    class FXRateServiceMock(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal(1.0))

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (FXRate(ccy1, ccy2, asof, Decimal(1.0)) for (ccy1, ccy2, asof) in queries)

    from datetime import date
    from .currencies import Currencies
    from .fxrates import FXRateLookupError

    service = FXRateServiceMock()

# Generated at 2022-06-14 04:36:02.629879
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test queries method of FXRateService.
    """
    ## Define a class that can provide foreign exchange rates:
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.fxrates import FXRateService

    class QueryableFXRateService(FXRateService):

        def __init__(self, rates: Iterable[FXRate]) -> None:
            super().__init__()
            self._rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            for rate in self._rates:
                if rate.ccy1 == ccy1 and rate.ccy2 == ccy2 and rate.date == asof:
                    return rate

# Generated at 2022-06-14 04:36:20.435065
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test class FXRateService

    Test method queries of class FXRateService
    """

    from .currencies import Currencies
    from .commons.zeitgeist import Date
    import datetime as dt

    # Test 1
    asof1 = Date("2020-01-20")
    asof2 = Date("2020-01-21")

    rval1 = FXRate(Currencies["EUR"], Currencies["USD"], asof1, Decimal("1.25"))
    rval2 = FXRate(Currencies["EUR"], Currencies["USD"], asof2, Decimal("1.19"))

    rlist = [rval1, rval2]

    rlist2 = []
    for rval in rlist:
        rlist2.append(rval)

    rlist3 = []

# Generated at 2022-06-14 04:36:32.593609
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # test coverage: 100%
    """
    Tests query method.
    """
    from decimal import Decimal

    import datetime
    import unittest

    from pypara.currencies import Currencies

    class MockFXRateService(FXRateService):
        """
        Provides a mock FX rate service class.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate(ccy1, ccy2, asof, ONE)


# Generated at 2022-06-14 04:36:43.842092
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .utils import serialization
    from .zeitgeist import Temporal, Dates
    from . commans.numbers import ONE, ZERO
    from .commons.collections import Quantity

    from decimal import Decimal

    import datetime

    from fractions import Fraction

    from pypara.commons.collections import Quantity
    from pypara.fxrates import FXRate, FXRateLookupError, FXRateService
    from pypara.currencies import Currency
    from pypara.utils import serialization


# Generated at 2022-06-14 04:36:53.176883
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies

    EUR = Currencies["EUR"]
    USD = Currencies["USD"]
    GBP = Currencies["GBP"]
    TRL = Currencies["TRL"]

    from .time import TODAY

    rate = FXRate(EUR, USD, TODAY, Decimal("1.1"))

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == EUR and ccy2 == USD and asof == TODAY:
                return rate
            else:
                return None


# Generated at 2022-06-14 04:37:01.920859
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .temporal import Temporal, TimeDimensions
    from .currencies import Currency, Currencies

    ## Init the fx rate service:
    class FXRateServiceMock(FXRateService):
        def __init__(self):
            self.fx_rates = []

        def add_fx_rate(self, fx_rate: FXRate) -> None:
            self.fx_rates.append(fx_rate)


# Generated at 2022-06-14 04:37:12.655101
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:37:25.467447
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """
    # noinspection PyAbstractClass
    class FxRateService(FXRateService):
        """
        Provides an FX rate service for testing purposes.
        """

        def __init__(self, rates: Iterable[Tuple[Currency, Currency, Date, Decimal]]) -> None:
            """
            Initializes the FX rate service.
            """
            self.rates = list(map(lambda r: FXRate(*r), rates))

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Queries an FX rate.
            """

# Generated at 2022-06-14 04:37:37.477243
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests foreign exchange rate lookup by :method:`FXRateService.queries`.
    """
    import unittest
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRate, FXRateService

    class Mock(FXRateService):
        """Defines a mock foreign exchange rate service implementation."""

        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["EUR"]:
                if ccy2 == Currencies["USD"]:
                    return FXRate(ccy1, ccy2, asof, Decimal("2"))
                if ccy2 == Currencies["TRY"]:
                    return FXRate(ccy1, ccy2, asof, Decimal("6"))


# Generated at 2022-06-14 04:37:40.070607
# Unit test for method query of class FXRateService
def test_FXRateService_query(): # noqa: MC0001
    """
    Tests method :method:`FXRateService.query` of class :class:`FXRateService`.
    """
    pass

# Generated at 2022-06-14 04:37:51.438542
# Unit test for method queries of class FXRateService

# Generated at 2022-06-14 04:38:07.845554
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime

    from decimal import Decimal
    from pypara.currencies import Currencies

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate.of(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))


# Generated at 2022-06-14 04:38:21.270041
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    This function tests the method queries of class FXRateService.
    """
    ## Create some FX rate lookup inputs:
    from .currencies import Currencies
    from .temporal import DateTime
    from .utils import null
    inputs = [
        (Currencies["USD"], Currencies["EUR"], DateTime("2019-05-18")),
        (Currencies["EUR"], Currencies["USD"], DateTime("2019-05-18")),
        (Currencies["GBP"], Currencies["JPY"], DateTime("2019-05-18")),
        (Currencies["JPY"], Currencies["GBP"], DateTime("2019-05-18")),
        (Currencies["EUR"], Currencies["USD"], DateTime("2019-05-17")),
    ]

    ## Create a bogus FX rate service:

# Generated at 2022-06-14 04:38:32.173582
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance import FXRate, FXRateService
    from pypara.zeitgeist import Date

    # Define the FX rate for EUR/USD
    rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

    # Define a local FX rate service
    class LocalFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            # Check if we have the rate
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
                return rate

            # Raise an exception if we are in strict

# Generated at 2022-06-14 04:38:44.366481
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103
    from .currencies import Currency
    from .temporal import Date
    from .fxrates import FXRateService

    def dummy_query(ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
        return FXRate(ccy1, ccy2, asof, Decimal(1) if ccy1 == ccy2 else Decimal(2))

    class DummyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return dummy_query(ccy1=ccy1, ccy2=ccy2, asof=asof, strict=strict)


# Generated at 2022-06-14 04:38:56.760810
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class :class:`FXRateService`.
    """
    from datetime import date
    from unittest import TestCase
    from unittest.mock import NonCallableMock
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService
    from pypara.temporal import Temporal

    # Create the FXRateService mock:
    fxrate_service = NonCallableMock()

    # Define query responses:

# Generated at 2022-06-14 04:39:04.492000
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .services.rateservice import ExchangeRateService
    from .commons.zeitgeist import Date
    import decimal
    #: Defines the default foreign exchange rate service for the runtime.
    rates = ExchangeRateService.of()
    #: Returns the foreign exchange rate of a given currency pair as of a given date.
    rate = rates.query(Currencies['EUR'], Currencies['USD'], Date('2017-01-01'))
    assert rate.ccy1 == Currencies['EUR']
    assert rate.ccy2 == Currencies['USD']
    assert rate.date == Date('2017-01-01')
    assert rate.value == Decimal(1)
    #: Returns the foreign exchange rate of a given currency pair as of a given date.

# Generated at 2022-06-14 04:39:15.469592
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test the method `queries` of class :class:`FXRateService`
    """
    ## Import:
    import datetime
    #from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    ## Test class:
    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Optional[Date] = None, strict: bool = False) -> Optional[FXRate]:
            pass
        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (super().queries(queries))

    service = TestFXRateService()

# Generated at 2022-06-14 04:39:25.122065
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    from decimal import Decimal
    from typing import Iterable
    from unittest import TestCase

    from .currencies import Currencies
    from .temporal import Temporal

    from .finance.fxrates import FXRate, FXRateService

    class FXRateServiceMock(FXRateService):

        def __init__(self, rates: Iterable[Tuple[Currency, Currency, Temporal, Decimal]]):
            self._rates = {(ccy1, ccy2, date): rate for ccy1, ccy2, date, rate in rates}


# Generated at 2022-06-14 04:39:36.379014
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    from decimal import Decimal
    from pypara.currencies import Currencies

    class FXService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.

            :param ccy1: The first currency of foreign exchange rate.
            :param ccy2: The second currency of foreign exchange rate.
            :param asof: Temporal dimension the foreign exchange rate is effective as of.
            :param strict: Indicates if we should raise a lookup error if that the foreign exchange rate can not be found.
            :return: The foreign exhange rate as a :class:`Decimal` instance or None.
            """

# Generated at 2022-06-14 04:39:45.099033
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """
    from .quotes import FXQuote
    from .quoteset import FXQuoteSet

    ## Define queries:

# Generated at 2022-06-14 04:40:04.466490
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # Imports
    from decimal import Decimal

    from pypara.currencies import Currency
    from pypara.datetime import Datetime
    from pypara.services import FXRateService
    from pypara.services.ram_fx_rate_service \
        import RamFXRateService \
        as FRS

    # Setup the service with some dummy rates

# Generated at 2022-06-14 04:40:16.998348
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    # Unit test:
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate, FXRateLookupError, FXRateService, __all__

    # Create and return a mock FX rate service:
    class FXRateServiceMock(FXRateService):

        # Implement the query method:
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate.of(ccy1, ccy2, asof, Decimal("2"))

        # Implement the queries method:

# Generated at 2022-06-14 04:40:28.089014
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService
    import datetime
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return queries

    service = MockFXRateService()
    assert [*service.queries((Currencies['EUR'], Currencies['USD'], datetime.date.today()))] == [(Currencies['EUR'], Currencies['USD'], datetime.date.today())]

# Generated at 2022-06-14 04:40:37.443338
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .temporal import Day
    from .utils.fx import EUR_USD
    from .utils.fx_services import FXMemoryService

    ## Use the default FX rate service:
    eur_usd = FXRateService.default.query(Currencies["EUR"], Currencies["USD"], Day.today())
    assert eur_usd == FXRate(Currencies["EUR"], Currencies["USD"], Day.today(), EUR_USD)

    ## Create a new FX service:
    fxs = FXMemoryService(EUR_USD)
    eur_usd = fxs.query(Currencies["EUR"], Currencies["USD"], Day.today())
    assert eur_usd == FXRate(Currencies["EUR"], Currencies["USD"], Day.today(), EUR_USD)


# Unit test

# Generated at 2022-06-14 04:40:46.728973
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.enums import OnError
    from pypara.temporal import Temporal
    from pypara.typing import Date

    class FailingRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict = False):
            # We should be able to handle different types for temporal dimension
            if isinstance(asof, Temporal):
                asof = asof.date
            return None

    rate_service = FailingRateService()
    date = Date(2019, 12, 20)
    temporal = Temporal.from_date(date)
    currency = Currency.get_by_locale_code("TRL")


# Generated at 2022-06-14 04:40:47.468982
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    assert True

# Generated at 2022-06-14 04:40:55.967835
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency, Currencies
    import datetime as dt
    from decimal import Decimal
    from .fx_rates import FXRateService

    class Stub(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: dt.date, strict: bool = False) -> Optional[Decimal]:
            return Decimal("1.25")

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False):
            return []

    srv = Stub()
    assert srv.query(Currencies["EUR"], Currencies["USD"], dt.date.today()) == Decimal("1.25")


# Generated at 2022-06-14 04:41:05.630389
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the query method of :class:`FXRateService`.
    """
    from unittest import TestCase, mock
    from unittest.mock import call
    from pypara.currencies import Currencies
    from pypara.finance.fx.services.in_memory import InMemoryFXRateService
    from pypara.finance.fx.services.mock import MockFXRateService

    class FXRateServiceTest(TestCase):
        """
        Provides a test case for :class:`FXRateService`.
        """

        def test_query(self):
            """
            Tests the query method of the FX rate service.
            """
            ## Create the FX rate service:
            service = self.service(Currencies["EUR"], Currencies["USD"], 5)

            ## Query the FX rate service:
            rate

# Generated at 2022-06-14 04:41:16.748728
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.dates import Date

    from .commons.testing import assert_equal

    try:
        from .currencies import FXRateService as CurrenciesFXRateService
    except ImportError:
        print("CurrenciesFXRateService not implemented - skipping the test...")
        return

    ## Create a FX rate service instance and query a couple of rates:
    fxrate = CurrenciesFXRateService()
    rate = fxrate.query(Currencies["EUR"], Currencies["USD"], Date.today())
    assert_equal(rate, FXRate(Currencies["EUR"], Currencies["USD"], Date.today(), Decimal("1.24")))

# Generated at 2022-06-14 04:41:25.606564
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the method query of class FXRateService.
    """
    ## Imports
    from decimal import Decimal
    from pypara.commons.collections import DefaultDict
    from pypara.currencies import Currencies
    from pypara.commons.datetime import date_factory

    ## Fixtures
    rate = FXRate.of(Currencies["USD"], Currencies["TRY"], date_factory("2020-01-01"), Decimal("6"))

    class DummyFXRateService(FXRateService):
        """
        Provides a dummy foreign exchange rate service.
        """

        def __init__(self, **kwargs) -> None:
            """
            Initializes the dummy foreign exchange rate service.
            """
            self._dict = DefaultDict(lambda: None, **kwargs)


# Generated at 2022-06-14 04:41:58.985857
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate

    ## Define the test query table:
    query_table = [
        (Currencies["EUR"], Currencies["USD"], datetime.date(2017, 1, 1)),
        (Currencies["EUR"], Currencies["USD"], datetime.date(2017, 1, 2)),
        (Currencies["EUR"], Currencies["USD"], datetime.date(2017, 1, 3)),
    ]

    ## Define the expected rates:

# Generated at 2022-06-14 04:42:06.917588
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """

    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    ##
    ## Test 1:
    ##
    ## Test one query with a single foreign exchange rate:
    ##
    class TestFXRateService(FXRateService):
        """
        Provides a testing foreign exchange rate service
        """


# Generated at 2022-06-14 04:42:19.992225
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Checks the method queries of class FXRateService.
    """
    ## Create a dummy FX rate service:
    class DummyService(FXRateService):
        """
        Provides a dummy FX rate service.
        """
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if (ccy1.name, ccy2.name) == ("EUR", "USD"):
                from decimal import Decimal
                from .currencies import Currencies
                return FXRate(Currencies["EUR"], Currencies["USD"], asof, Decimal("1.1"))
            return None


# Generated at 2022-06-14 04:42:29.683638
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the method :method:`FXRateService.queries`.
    """
    ## Define an FX rate service stub:
    class FXRateServiceStub(FXRateService):
        """
        Provides a stub implementation of :class:`FXRateService`.
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

# Generated at 2022-06-14 04:42:30.686114
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D103
    pass


# Generated at 2022-06-14 04:42:41.273038
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import TestCase, main
    from pypara.currencies import Currency
    from pypara.temporal import Temporal
    from datetime import date
    from decimal import Decimal

    class QueryService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[Decimal]:
            return Decimal(1.0)

        def queries(self, queries: Iterable[Tuple[Currency, Currency, Temporal]], strict: bool = False) -> Iterable[Optional[Decimal]]:
            pass

    class TestFXRateService(TestCase):
        def test_query_non_strict_mode(self):
            sut = QueryService()

# Generated at 2022-06-14 04:42:44.146695
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests class FXRateService's method queries.
    """
    # TODO(v3): Complete this method.
    return None

# Generated at 2022-06-14 04:42:45.582084
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    unit test for method queries of class FXRateService
    """
    pass

# Generated at 2022-06-14 04:42:54.087807
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies
    from pypara.temporal import Temporals

    ## Test the argument type:
    try:
        FXRateService().query(1, Currencies["USD"], Temporals.today())
        assert False
    except TypeError:
        assert True

    ## Test the argument type:
    try:
        FXRateService().query(Currencies["EUR"], 1, Temporals.today())
        assert False
    except TypeError:
        assert True

    ## Test the argument type:
    try:
        FXRateService().query(Currencies["EUR"], Currencies["USD"], 1)
        assert False
    except TypeError:
        assert True

    ## Test the query:
    assert FXRateService().query(Currencies["EUR"], Currencies["USD"], Temporals.today())

# Generated at 2022-06-14 04:43:05.011687
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    sample_queries = [
        (Currency('EUR') , Currency('USD'), Date(2020, 7, 1)),
        (Currency('USD') , Currency('EUR'), Date(2020, 7, 1)),
        (Currency('EUR') , Currency('TRY'), Date(2020, 7, 1)),
        (Currency('USD') , Currency('TRY'), Date(2020, 7, 1)),
        (Currency('EUR') , Currency('USD'), Date(2020, 7, 2)),
        (Currency('USD') , Currency('EUR'), Date(2020, 7, 2)),
        (Currency('EUR') , Currency('TRY'), Date(2020, 7, 2)),
        (Currency('USD') , Currency('TRY'), Date(2020, 7, 2)),
    ]

# Generated at 2022-06-14 04:43:53.256734
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    class SampleService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            raise NotImplementedError("This is a unit test.")
        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            raise NotImplementedError("This is a unit test.")
    assert issubclass(SampleService, FXRateService)


# Generated at 2022-06-14 04:44:02.406858
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class MockFXRateService(FXRateService):

        def __init__(self):
            self._rates = []

        def query(self, ccy1, ccy2, asof, strict=False):
            for rate in self._rates:
                if rate[0] == ccy1 and rate[1] == ccy2 and rate[2] == asof:
                    return rate
            if strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            else:
                return None

        def queries(self, queries, strict=False):
            for q in queries:
                yield self.query(q[0], q[1], q[2], strict)

    mock = MockFXRateService()



# Generated at 2022-06-14 04:44:12.092768
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.currencies import Currencies
    from pypara.temporal import Date
    from pypara.finance.fx import FXRate, FXRateService
    from pypara.finance.fx.memory import MemoryFXRateService

    ## Create a random date:
    date = Date("2018-01-01")

    ## Create a random rate:
    rate = FXRate(Currencies["EUR"], Currencies["USD"], date, Decimal("1.22"))

    class QueryTestService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return rate


# Generated at 2022-06-14 04:44:23.145290
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from pypara.currencies import Currencies
    from .commons.zeitgeist import Zeitgeist
    from .fxrates import FXRateSource

    ## Prepare the queries:
    queries = (
        (Currencies["EUR"], Currencies["USD"], Zeitgeist.now().add_years(-1).date()),
        (Currencies["EUR"], Currencies["USD"], Zeitgeist.now().date()),
        (Currencies["USD"], Currencies["EUR"], Zeitgeist.now().date()),
    )

    ## Query the default FX rate source:
    rates = FXRateSource.default.queries(queries)
    rate = next(rates)
    assert rate is not None, "Rate cannot be None."
    assert rate.ccy1 == Currencies["EUR"], "Wrong currency 1."