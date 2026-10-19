

# Generated at 2022-06-14 04:34:22.968370
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    assert False


# Generated at 2022-06-14 04:34:34.899472
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Performs unit tests for method queries.
    """
    # Setup
    class TestFXRateService(FXRateService):
        """
        TestFXRateService for the purpose of unit testing.
        """
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Implements the fall back foreign exchange rate to a given currency pair as of a given date.
            """
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            """
            Implements the fall back foreign exchange rates to a given currency pairs as of a given dates.
            """
            return super().queries(queries, strict)

    import random
    import string


# Generated at 2022-06-14 04:34:46.894530
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """
    import datetime
    import random
    import unittest
    from decimal import Decimal
    from pypara.currencies import Currencies

    ## Define the currency pairs and asof dates to generate FX rate queries from:
    ccypairs = [("EUR", "USD"), ("USD", "JPY"), ("EUR", "USD"), ("EUR", "USD")]
    asofs = [
        datetime.date(2019, 4, 14),
        datetime.date(2019, 7, 14),
        datetime.date(2019, 8, 14),
        datetime.date(2021, 2, 14),
    ]

    ## Define the FX rates:

# Generated at 2022-06-14 04:34:59.032899
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime as dt

    from decimal import Decimal as D

    from .currencies import Currency as C

    class FXRateServiceStub(FXRateService):
        def __init__(self):
            self.rates = {
                (C["EUR"], C["USD"], dt.date(2019, 2, 1)): D("1.1414"),
                (C["EUR"], C["USD"], dt.date(2019, 2, 2)): D("1.1414"),
                (C["USD"], C["EUR"], dt.date(2019, 2, 1)): D("0.8765"),
                (C["USD"], C["EUR"], dt.date(2019, 2, 2)): D("0.8765"),
            }


# Generated at 2022-06-14 04:35:12.592623
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies, Currency
    from pypara.currencies.money import Money
    from pypara.temporal import Temporal, Temporals, Dates
    from pypara.fx import FXRateService, FXRateLookupError, FXRate
    from pypara.fx.fixerio import FixerioFXRateService # noqa: F401
    from decimal import Decimal
    import unittest
    import datetime
    import os

    ## Create the class under test (CUT).
    cut = FixerioFXRateService(os.environ["FIXERIO_ACCESS_KEY"]) # noqa: S106

    ## Create the test case.

# Generated at 2022-06-14 04:35:19.590792
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():  # noqa: D103
    from .commons.temporal import Date
    from .currencies import Currency
    from .services import DummyFXRateService
    from .utils.convert import convert

    service = DummyFXRateService()

    ## Query the rates:
    rates = list(
        service.queries([
            (Currency("EUR"), Currency("TRY")),
            (Currency("TRY"), Currency("SAR"), Date()),
        ])
    )

    ## Make sure that the results are in the right order:
    assert convert(Currency("EUR"), Currency("TRY"), service=service) == rates[0]
    assert convert(Currency("TRY"), Currency("SAR"), service=service, asof=Date()) == rates[1]


# A test fixture case for FXRateService.queries

# Generated at 2022-06-14 04:35:31.736060
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency, Currencies
    from .refdata import FXRateService

    eur = Currencies["EUR"]
    usd = Currencies["USD"]
    nzd = Currencies["NZD"]
    queries = [(eur, usd, Date.today()), (nzd, usd, Date.today())]

    rate_service = FXRateService()
    rates = rate_service.queries(queries)
    assert isinstance(rates, list)
    assert len(rates) == 2
    assert isinstance(rates[0], FXRate)
    assert isinstance(rates[1], FXRate)

    rates = rate_service.queries(queries, strict = True)
    assert isinstance(rates, list)
    assert len(rates) == 2
    assert isinstance(rates[0], FXRate)

# Generated at 2022-06-14 04:35:45.536879
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == ccy2:
                return FXRate(ccy1, ccy2, asof, ONE)
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            pass

    from .currencies import Countries

    svc = TestFXRateService()
    assert svc.query(Countries["TR"], Countries["TR"], Date.now()) == FXRate(Countries["TR"], Countries["TR"],
                                                                             Date.now(), ONE)

# Generated at 2022-06-14 04:35:52.832575
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """
    # Mocking this class with `unittest` fails due to its abstract nature.
    # Hence, we are using the `mock` library.
    # See: https://stackoverflow.com/questions/38841926/python-urllib-request-is-not-callable-in-unit-test
    # see: https://stackoverflow.com/questions/37000600/how-to-mock-an-abstract-method
    from unittest import TestCase
    from unittest.mock import MagicMock, call

    # Create a dummy class
    class DummyClass(FXRateService, metaclass=ABCMeta):
        TQuery = Tuple[Currency, Currency, Date]


# Generated at 2022-06-14 04:36:02.123780
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the foreign exchange rate lookup functionality.
    """

    ## No setup required.

    ## Define the currencies:
    ccy1, ccy2 = "EUR", "USD"
    ## Define the temporal dimension:
    asof = Date()

    ## Test the default service:
    assert FXRateService.default is not None
    ## Test the default service query:
    assert FXRateService.default.query(ccy1, ccy2, asof) is not None
    ## Test the default service queries:
    assert len(list(FXRateService.default.queries([[ccy1, ccy2, asof]]))) == 1


if __name__ == "__main__":
    test_FXRateService_query()

# Generated at 2022-06-14 04:36:06.796971
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:36:20.434447
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    ## Import required modules:
    from unittest.mock import MagicMock
    from unittest import TestCase
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.forex import FXRateService, FXRate

    ## Define a mock class:
    class FXMock(FXRateService):
        """
        Defines a mock FX rate service.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("2"))


# Generated at 2022-06-14 04:36:32.593122
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test case for method queries of class FXRateService.
    """
    from .currencies import Currency
    from .temporal import Date

    ## Test for the following sequence of FXRateService.queries:
    # - call queries once
    # - yield once
    # - call queries once
    # - yield once
    # - call queries once
    # - yield once
    # - call queries once
    # - yield once
    # - call queries once

# Generated at 2022-06-14 04:36:43.840733
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test the queries method of FXRateService class
    """
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies


# Generated at 2022-06-14 04:36:53.189036
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest.mock import MagicMock, create_autospec, patch
    from pypara.currencies import Currencies

    # Setting up the mocks
    # Mocks: FXRateService
    fxrs_mock = MagicMock(
        spec_set=FXRateService,
        default_side_effect=FXRateService.query(Currencies['EUR'], Currencies['USD'], Date())
    )

    # Mocks: FXRate
    fxr_mock = MagicMock(
        spec_set=FXRate,
        spec_set_class=True
    )
    fxr_mock.ccy1 = Currencies['EUR']
    fxr_mock.ccy2 = Currencies['USD']
    fxr_mock.date = Date()
    f

# Generated at 2022-06-14 04:37:01.920493
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class :class:`FXRateService`.
    """
    from .currencies import Currency
    from .temporal import Date
    from .fxrates import FXRate, FXRateService

    class SimpleFXRateService(FXRateService):
        """
        Provides a simple foreign exchange rate service.
        """

        ## Define a lookup function:
        __lookup = {
            (Currency("AUD"), Currency("BRL")): FXRate(Currency("AUD"), Currency("BRL"), Date(2019, 1, 1), Decimal("0.5")),
            (Currency("BRL"), Currency("AUD")): FXRate(Currency("BRL"), Currency("AUD"), Date(2019, 1, 1), Decimal("2")),
        }


# Generated at 2022-06-14 04:37:14.970008
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """Unit test for method queries of class FXRateService."""
    from .datalayer.fx_rates import FXRatesDataLayer
    from .service_layer.fx_rates import FXRateServiceLayer
    fx_rate_service = FXRateServiceLayer(FXRatesDataLayer("test/data/fx_rates.csv"))
    base = fx_rate_service.resolve("EUR", "TRY", Date.today())
    ccy1 = "USD"
    ccy2 = "TRY"
    asof = Date.today()
    ccy1, ccy2 = "TRY", "USD"
    ccy1, ccy2 = "USD", "TRY"
    ccy1, ccy2 = "TRY", "EUR"
    ccy1, ccy2 = "EUR", "TRY"
    ccy1

# Generated at 2022-06-14 04:37:28.629659
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.rates import FXRateService

    class DummyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, ONE)

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return map(self.query, *zip(*queries))


# Generated at 2022-06-14 04:37:30.231327
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:37:41.288900
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency

    ## Reference implementation:
    class Reference(FXRateService):
        """
        Provides a reference implementation for testing.
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
            for query in queries:
                yield self.query(*query, strict=strict)

    ## Check the query

# Generated at 2022-06-14 04:37:58.026478
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.temporal import Temporals
    import datetime

    class TestFXRateService(FXRateService):
        def __init__(self, rates):
            self.rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            for rate in self.rates:
                if (rate[0] == ccy1) and (rate[1] == ccy2) and (rate[2] <= asof):
                    return rate

            if strict:
                raise FXRateLookupError(ccy1, ccy2, asof)
            else:
                return None


# Generated at 2022-06-14 04:38:09.165807
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService.

    **Note:** Implementation is of the abstract class :class:`FXRateService`.
    """
    from decimal import Decimal
    from pypara.currencies import Currency

    class MockFXRateService(FXRateService):
        """
        Provides a mock foreign exchange rate service.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Tests method query of class FXRateService.
            """
            from .fxrates import FXRates


# Generated at 2022-06-14 04:38:19.352919
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService, FXRate
    from unittest.mock import Mock

    ## Define a simple FX rate lookup service:
    class SimpleFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1.5")) if (ccy1, ccy2, asof) in [(Currencies["EUR"], Currencies["USD"], datetime.date.today())] else None


# Generated at 2022-06-14 04:38:28.153445
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.currencies.exchange_rates import EURFXRateService

    ## Create the FX rate service:
    fx_service = EURFXRateService()

    ## Retrieve the EUR/USD rate as of today:
    rate = fx_service.query(Currencies["EUR"], Currencies["USD"], Date.today())

    print(f"Today's EUR/USD rate is {rate.value}")
    assert rate.value >= Decimal("1.1")



# Generated at 2022-06-14 04:38:37.550016
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the function query_rates of class FXRateService.
    """

    from decimal import Decimal
    from pypara.currencies import Currencies

    from .commons import Temporal
    from .fxrates import FXRateService, FXRateLookupError

    class TestFXRateService(FXRateService):
        """
        Test FX rate service.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Queries an FX rate.
            """
            ## Create a key:
            key = (ccy1.code, ccy2.code, asof)

            ## Check if we have a hit:

# Generated at 2022-06-14 04:38:47.360524
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the query method of class FXRateService.
    """
    from pypara.currencies import Currency, Currencies
    from pypara.fx import BISFXRateService
    from pypara.temporal import Temporal, Temporals
    from pypara.testing.doubles import FakeFXRateService
    from pypara.testing.helper import stamp

    ## Create a fake FX rate service to use in tests:
    fx = FakeFXRateService()

    ## Check behaviour when dates are invalid:
    date = Temporal.of(2020, 2, 29)
    assert fx.query(Currencies["EUR"], Currencies["USD"], date) is None

    ## Check behaviour on invalid FX rate queries:
    date1 = Temporal.of(2020, 1, 31)
    date2 = Temporal.of

# Generated at 2022-06-14 04:38:59.788227
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.date import Today
    from pypara.fx import FXRateService
    from pypara.fx.sources import InMemoryRateService
    from pypara.markets.ccys import CCYMarket
    from pypara.markets.markets import MarketService

    # Create an FXRateService instance and register it as default:
    rate_service = InMemoryRateService()
    FXRateService.default = rate_service

    # Create a market service and register a currency market:
    market_service = MarketService()
    market_service.register(CCYMarket.EURUSD, Currencies["EUR"], Currencies["USD"], "FX rate EUR/USD")

    # Register EUR/USD currency pair market:

# Generated at 2022-06-14 04:39:02.451454
# Unit test for method query of class FXRateService
def test_FXRateService_query():
  pass


# Generated at 2022-06-14 04:39:03.897680
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # Fixture
    from pypara.currencies import Currencies


# Generated at 2022-06-14 04:39:14.957399
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    @dataclass
    class FXRateService(pypara.finance.FXRateService):
        rates: Dict[tuple, pypara.finance.FXRate]

        def query(self, ccy1: pypara.currencies.Currency, ccy2: pypara.currencies.Currency, asof: pypara.commons.zeitgeist.Date, strict: bool = False) -> Optional[pypara.finance.FXRate]:
            return self.rates.get((ccy1, ccy2, asof), None)


# Generated at 2022-06-14 04:39:34.147637
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    from .currencies import USD
    from .temporal import Date, Today

    from .fxrates import FXRateSource

    ## Define the service:
    service = FXRateSource.of(USD, Today)

    ## Query the service:
    assert service.query(USD, USD, Date.of(2018, 12, 1)) == FXRate(USD, USD, Date.of(2018, 12, 1), 1.0)

# Generated at 2022-06-14 04:39:44.114992
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.temporal import Temporal

    class FXRateServiceImpl(FXRateService):

        foo = {"EUR": {"USD": [Temporal(Date(2018, 9, 1), Date(2018, 9, 30), Decimal("1.2"))]}}

        def query(self, ccy1, ccy2, asof, strict=False):
            try:
                rates = self.foo[str(ccy1)][str(ccy2)]
                return list(rate for rate in rates if asof in rate)[0].value
            except (IndexError, KeyError):
                if strict:
                    raise FXRateLookupError(ccy1, ccy2, asof)
                return None


# Generated at 2022-06-14 04:39:55.275704
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    unit test for method queries of class FXRateService
    """

    from .sources.fxquotes import FXQuotes
    from .currencies import Currencies

    ## Create test FXQuoteService
    fxq = FXQuotes()
    
    ## Prepare queries
    queries = [
        (Currencies["USD"], Currencies["EUR"], datetime.date(2018, 1, 1)),
        (Currencies["USD"], Currencies["EUR"], datetime.date(2018, 1, 2)),
        (Currencies["USD"], Currencies["EUR"], datetime.date(2018, 1, 3))
        ]

    ## Execute method queries
    rates = fxq.queries(queries)

    ## Check the results
    assert(len(rates) == 3)

# Generated at 2022-06-14 04:40:03.852356
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return iter(())

    tfxr = TestFXRateService()
    assert tuple(tfxr.queries(iter((None,)))) == ()
    assert tuple(tfxr.queries(iter(()))) == ()

# Generated at 2022-06-14 04:40:16.072403
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from .commons.zeitgeist import Date
    from .finance.money import Money
    from .fxrates.ecb import ECBFXRateService

    asof = Date.today()
    eur_usd = Money(Currencies["USD"], Decimal("2.0000"))
    eur_gbp = Money(Currencies["GBP"], Decimal("0.9000"))
    fx_eur_usd = FXRate(Currencies["EUR"], Currencies["USD"], asof, Decimal("2.0000"))
    fx_eur_gbp = FXRate(Currencies["EUR"], Currencies["GBP"], asof, Decimal("0.9000"))

    #: Queries list:

# Generated at 2022-06-14 04:40:27.651242
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.temporal import Date
    from pypara.finance.fx import FXRateService

    class FrozenFXRateService(FXRateService):

        def __init__(self, rates):
            super().__init__()
            self._rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict=False) -> Optional[FXRate]:
            for c1, c2, date, value in self._rates:
                if (ccy1, ccy2, asof) == (c1, c2, date):
                    return FXRate(c1, c2, date, value)

# Generated at 2022-06-14 04:40:37.005658
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates.sources import SimpleFXRateSource

    # Define the source and the service:

# Generated at 2022-06-14 04:40:48.339016
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from ..currencies.currencies import Currency, Currencies
    import datetime
    from decimal import Decimal
    class MockFXRateService(FXRateService):
        def __init__(self):
            self.rates = {
                (Currencies.EUR, Currencies.USD, datetime.date.today()-datetime.timedelta(1)): Decimal("1.1")
            }
        def query(self, ccy1: Currency, ccy2: Currency, asof: datetime.date, strict: bool = False) -> Optional[Decimal]:
            try: return (self.rates)[(ccy1, ccy2, asof)]
            except (KeyError): return None

# Generated at 2022-06-14 04:40:52.641322
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency

    assert FXRateService.query(Currency("EUR"),Currency("USD"),Date.today()) == None
    assert FXRateService.query(Currency("USD"),Currency("EUR"),Date.today()) == None


# Generated at 2022-06-14 04:41:04.140138
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """
    import datetime

    from decimal import Decimal

    from pypara.currencies import Currencies

    class _FXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for ccy1, ccy2, asof in queries:
                yield FXRate(ccy1, ccy2, asof, Decimal("1"))

    date = datetime.date.today()


# Generated at 2022-06-14 04:41:44.861910
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:41:50.937003
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx.services import InMemoryFXRateService

    ## Create a service with few FX rates:
    service = InMemoryFXRateService()

    ## Populate some rates:
    service.update(FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("1.1")))
    service.update(FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.9")))
    service.update(FXRate(Currencies["AED"], Currencies["TRY"], datetime.date.today(), Decimal("2.2")))

# Generated at 2022-06-14 04:41:51.603598
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass

# Generated at 2022-06-14 04:42:01.355612
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    # Method query of class FXRateService should raise ValueError if ccy1 is None
    srv = FXRateService()
    ccy1 = None
    ccy2 = Currency.of("USD")
    asof = Date.of(2020, 1, 1)
    strict = True
    expected = ValueError
    actual = None
    try:
        srv.query(ccy1=ccy1, ccy2=ccy2, asof=asof, strict=strict)
    except ValueError as exception:
        actual = exception
    msg = "Method query of class FXRateService should raise ValueError if ccy1 is None"
    assert type(actual) == expected, msg

    # Method query of class FXRateService should raise ValueError if ccy2 is None
    srv = FXRateService()
    ccy1 = Currency

# Generated at 2022-06-14 04:42:10.716041
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .commons.temporal import Temporal
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currency, Currencies
    class TestService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> FXRate:
            return FXRate.of(ccy1, ccy2, asof, Decimal(ccy1.code + ccy2.code + str(asof.year) + str(asof.month) + str(asof.day)))

# Generated at 2022-06-14 04:42:23.051441
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .temporal import Temporal
    from .commons import now
    from .fxrates import FXRateService, FXRate
    from .fxrates.dummy import DummyFXRateService

    ## ------------------------------------------------------------------------------------------------------------
    ## Test if the method works correctly:
    ## ------------------------------------------------------------------------------------------------------------
    service = DummyFXRateService()

    assert service.query(Currencies["EUR"], Currencies["USD"], Temporal(now())) == FXRate(
        Currencies["EUR"], Currencies["USD"], Temporal.of(now()), Decimal("1.25"))

    assert service.query(Currencies["USD"], Currencies["KRW"], Temporal(now())) == FXRate(
        Currencies["USD"], Currencies["KRW"], Temporal.of(now()), Decimal("1.2"))

   

# Generated at 2022-06-14 04:42:31.835706
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .time import Days, temporal
    from .values import Money

    ## Initialize data:
    money1 = Money("1000000", Currencies["EUR"]) # 1000000 EUR
    money2 = Money("2000000", Currencies["USD"]) # 2000000 USD

    ## Service:
    class TestFXRateService(FXRateService):  # noqa: E301
        """
        A foreign exchange rate service for testing purpose.
        """

# Generated at 2022-06-14 04:42:42.693875
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("2"))
    service = MockFXRateService()
    rate = service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today())
    ccy1, ccy2, date, value = rate
    assert ccy1 == Currencies["EUR"]
    assert ccy2 == Currencies["USD"]
    assert date == datetime.date.today()
    assert value == Decimal("2")


# Generated at 2022-06-14 04:42:49.919769
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    query = FXRateService.TQuery
    date = datetime.date.today()
    assert FXRateService.default.query(Currencies["EUR"], Currencies["USD"], date) == FXRate.of(
        Currencies["EUR"], Currencies["USD"], date, Decimal("1.095")
    )
    assert FXRateService.default.query(*query(Currencies["EUR"], Currencies["USD"], date)) == FXRate.of(
        Currencies["EUR"], Currencies["USD"], date, Decimal("1.095")
    )

# Generated at 2022-06-14 04:43:02.979695
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from functools import partial
    from unittest.mock import Mock
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            pass

    ## Test the lookup error:
    strict_fx_rate_service = TestFXRateService()
    strict_fx_rate_service.query = partial(
        FXRateService.query,
        strict=True
    )

    assert strict_fx_rate_