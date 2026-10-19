

# Generated at 2022-06-14 04:34:34.033631
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import USD, EUR
    from .temporal import Date
    from .fx import FXRateService

    class MockService(FXRateService):
        def __init__(self, queries: Iterable[Tuple[Currency, Currency, Date]], strict: bool = False):
            self.queries = queries
            self.strict = strict
            super().__init__()

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if strict and self.strict:
                return None
            for query in self.queries:
                if (ccy1, ccy2, asof) == query:
                    return FXRate(ccy1, ccy2, asof, 1)
            return None


# Generated at 2022-06-14 04:34:46.370842
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test of method query of class FXRateService.
    """

    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx.services.qrates import QRatesFXRateService

    ## Create a dummy FX rate service:
    fx = QRatesFXRateService()

    ## Test for the case where we are looking for the same currency pair:
    rate = fx.query(Currencies["USD"], Currencies["USD"], datetime.date.today())
    assert rate == FXRate.of(Currencies["USD"], Currencies["USD"], datetime.date.today(), Decimal("1"))

    ## Test for the case where we are looking for an existing currency pair:

# Generated at 2022-06-14 04:34:58.801348
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.core.fxrates import FXRate, FXRateService

    # Mock FX rate service class:
    class MockFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            pass

        def queries(self, queries: Iterable[Tuple[Currency, Currency, Date]], strict: bool = False) -> Iterable[
            Optional[FXRate]]:
            pass

    # Create an instance of a mock FX rate service:
    svc: FXRateService = MockFXRateService()

    # A valid FX rate query is of type Currency, Currency and Temporal:
    ccy1: Currency = Currencies["EUR"]

# Generated at 2022-06-14 04:35:12.422992
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime

    from decimal import Decimal
    from pypara.currencies import Currencies

    # Params:
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]
    asof = datetime.date.today()
    rate = Decimal("2")

    # Create the service:
    class Service(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate.of(ccy1, ccy2, asof, rate)

        def queries(self, queries, strict=False):
            return [self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries]

    # Create the service instance:
    service = Service()

    # Test query

# Generated at 2022-06-14 04:35:22.528988
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    class FXRateServiceImpl(FXRateService):
        def __init__(self) -> None:
            super().__init__()
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            pass

# Generated at 2022-06-14 04:35:34.580963
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .demo import DemoFXRateService
    from .currencies import Currencies
    from .commons.zeitgeist import Date
    from datetime import date
    from decimal import Decimal
    x = DemoFXRateService()

# Generated at 2022-06-14 04:35:35.345843
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:35:48.701175
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies, CurrenciesLookupError
    from .commons.zeitgeist import Date
    from decimal import Decimal

    is_not_exist = False
    is_strict = False

    class FXRateServiceMock(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            nonlocal is_not_exist
            nonlocal is_strict
            is_strict = strict
            is_not_exist = not is_not_exist
            if is_not_exist:
                return None
            else:
                return FXRate(ccy1, ccy2, asof, Decimal("2"))


# Generated at 2022-06-14 04:36:01.981817
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService

    class Test(FXRateService):

        def query(self, ccy1, ccy2, asof, **kwargs):
            if ccy1 == Currencies['USD'] and ccy2 == Currencies['EUR'] and asof == datetime.date(2018, 12, 31):
                return FXRate(ccy1, ccy2, asof, Decimal('0.8'))
            if ccy1 == Currencies['EUR'] and ccy2 == Currencies['USD'] and asof == datetime.date(2018, 12, 31):
                return FXRate(ccy1, ccy2, asof, Decimal('1.25'))

# Generated at 2022-06-14 04:36:14.560368
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """
    from .currencies import Cryptocurrency, Currencies
    from .temporal.zeitgeist import Date, Weekdays

    ccy1 = Cryptocurrency.lookup("BTC")
    ccy2 = Currencies["USD"]
    date = Date(2013, 10, 25)  # Friday

    assert date.weekday == Weekdays.friday

    # Long
    queries = [
        (ccy1, ccy2, date),
        (ccy2, ccy1, date),
    ]
    rates = FXRateService.default.queries(queries)
    for rate in rates:
        assert isinstance(rate, FXRate)

    # Short

# Generated at 2022-06-14 04:36:30.901517
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currency
    from pypara.finance.commons.zeitgeist import Date
    from decimal import Decimal

    class TestService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1"))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [FXRate(ccy1, ccy2, asof, Decimal("1")) for ccy1, ccy2, asof in queries]

    service = TestService()

# Generated at 2022-06-14 04:36:42.868845
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    import unittest
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.uncertainties import Dist
    from pypara.utilities.distributions import Normal

    class MockFXRateService(FXRateService):
        def __init__(self):
            self.rates = {
                (Currencies["EUR"], Currencies["USD"]): {
                    datetime.date(2019, 3, 1): Dist(Normal(Decimal("1.1235"), Decimal("0.0004")))
                }
            }


# Generated at 2022-06-14 04:36:56.132502
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    service = object()
    service.queries = lambda *args, **kwargs: (
        FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2")),
        FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("3")),
    )
    response = tuple(service.queries([(Currencies["EUR"], Currencies["USD"], datetime.date.today())]))
    assert response[0].ccy1 == Currencies["EUR"]
    assert response[1].ccy1 == Currencies["EUR"]
    assert response[0].ccy2 == Currencies["USD"]

# Generated at 2022-06-14 04:37:02.913400
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    from .currencies import Currency
    from .temporal import Date, Temporal

    def fx_rate_service() -> FXRateService:

        from .currency_conversion import FXRateService

        class MockFXRateService(FXRateService):

            def __init__(self, data: dict = None) -> None:
                super().__init__()
                self.rates_: dict = data or {}

            def __contains__(self, item):
                return item[0:-1] in self.rates_.keys()

            def __getitem__(self, item):
                return self.rates_[item[0:-1]][0]


# Generated at 2022-06-14 04:37:15.515432
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from unittest import TestCase
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService, FXRateLookupError
    from pypara.commons.zeitgeist import Date

    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date(2019, 1, 1):
                return FXRate(ccy1, ccy2, asof, Decimal("1.0"))

# Generated at 2022-06-14 04:37:28.733814
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .temporal import Temporal
    from .fxrates import FXRateService, FXRate
    
    from datetime import date
    from decimal import Decimal
    from unittest import TestCase
    
    
    class Dummy(FXRateService):
        """
        Provides a dummy implementation for the FX rate service.
        """
    
        #: Defines the dummy FX rate service singleton.
        instance: "Dummy" = None
    
        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the dummy foreign exchange rate.
            """
            return FXRate(ccy1, ccy2, asof, Decimal("0.5"))
    

# Generated at 2022-06-14 04:37:36.887336
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService, FXRate
    # TODO: Add a test for queries method
    q1 = (Currencies["EUR"], Currencies["USD"], datetime.date.today())
    q2 = (Currencies["USD"], Currencies["TRY"], datetime.date.today())
    queries = [q1, q2]
    class MockFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            usd_eur = FXRate.of(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal(0.9))
            eur_

# Generated at 2022-06-14 04:37:49.143417
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.time import Date
    class MockService(FXRateService):
        def query(self, ccy1, ccy2, date, strict=False):
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["TRY"] and date == Date(date(2020, 3, 1)):
                return FXRate(Currencies["USD"], Currencies["TRY"], date, Decimal("5.50"))
            else:
                return None
        def queries(self, queries, strict=False):
            for ccy1, ccy2, date in queries:
                yield self.query(ccy1, ccy2, date, strict)
    service = MockService()

# Generated at 2022-06-14 04:37:58.492580
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from datetime import date
    from itertools import zip_longest
    from pypara.currencies import Currencies
    from pypara.fx import InMemoryFXRateService

    fxrs = InMemoryFXRateService()
    queries = [
        (Currencies["EUR"], Currencies["USD"], date(2020, 1, 1)),
        (Currencies["EUR"], Currencies["USD"], date(2020, 2, 1)),
        (Currencies["EUR"], Currencies["USD"], date(2020, 3, 1)),
        (Currencies["EUR"], Currencies["USD"], date(2020, 4, 1)),
        (Currencies["EUR"], Currencies["USD"], date(2020, 5, 1))
    ]

# Generated at 2022-06-14 04:38:07.344234
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .fx import BaseFXRateService
    from .temporal import Period
    from datetime import date
    from decimal import Decimal
    from typing import Callable

    ## Create a rate lookup function for the fixture:
    def rate_lookup(ccy1: Currency, ccy2: Currency, asof: date) -> Decimal:
        ccy_pair = (ccy1, ccy2)
        if ccy_pair == (Currencies["USD"], Currencies["EUR"]):
            return Decimal("0.5")

        elif ccy_pair == (Currencies["EUR"], Currencies["USD"]):
            return Decimal("2")

        elif ccy_pair == (Currencies["JPY"], Currencies["USD"]):
            return Decimal("0.009")

       

# Generated at 2022-06-14 04:38:24.933955
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService.
    """
    ## Imports:
    from pypara.currencies import Currencies
    from pypara.commons.zeitgeist import Date
    from pypara.finmath.fx import FXRateService

    ## Source and target currencies:
    ccy1 = Currencies["EUR"]
    ccy2 = Currencies["USD"]

    ## Define the FX rate service:
    class Service(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[Decimal]:
            return None

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[Decimal]]:
            return None

    ## Create the service

# Generated at 2022-06-14 04:38:35.359842
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    ## Create a mock service
    class MockService(FXRateService):
        def __init__(self, rates: Iterable[Optional[FXRate]]):
            self.rates = list(rates)

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self.rates[0]

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return self.rates

    ## Create a query and a rate:
    from .currencies import Currencies
    from decimal import Decimal

    import datetime
    query = (Currencies["USD"], Currencies["EUR"], datetime.date.today())

# Generated at 2022-06-14 04:38:46.111774
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of the FXRateService class.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    class _MyService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal("1.1")) if (ccy1, ccy2, asof) == (Currencies["EUR"], Currencies["USD"], datetime.date(2020, 1, 1)) else None

        def queries(self, queries, strict=False):
            return (self.query(ccy1, ccy2, asof, strict) for ccy1, ccy2, asof in queries)



# Generated at 2022-06-14 04:38:58.853424
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest.mock import MagicMock
    from pypara.currencies import Currencies
    from pypara.curves.datasets import CurveDataset, CurveDatasets
    from pypara.curves.repos import CurveRepo
    from pypara.rates.repos import CurveBasedFXRateService

    # This is a singleton unittest:
    if CurveBasedFXRateService.default:
        return

    # Setup the FX rate service:
    repo = MagicMock(CurveRepo)
    repo.dates = MagicMock(return_value=CurveDatasets.dates())
    repo.query = MagicMock(return_value=CurveDataset.of(Currencies["USD"], ZERO, ZERO))
    service = CurveBasedFXRateService(repo)
    FX

# Generated at 2022-06-14 04:39:05.720698
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): # noqa: D103
    import datetime
    from decimal import Decimal
    from collections import OrderedDict
    from pypara.currencies import Currencies
    from pypara.temporal import Temporal
    from pypara.util.fxrate import FXRateService

    ## Define the test data:

# Generated at 2022-06-14 04:39:16.439636
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    ## We need to have FXRateService here as it is abstract and we can not instantiate it directly.
    from .services.defaults import FXRateService as FXRateServiceImpl

    service = FXRateServiceImpl()

    # Factories:
    def create_query(from_: Currency, to: Currency, asof: Date) -> FXRateService.TQuery:
        return (from_, to, asof)

    ## We need Currency and Date to be able to create queries:
    from .currencies import Currency as CurrencyImpl
    from .commons.zeitgeist import Date as DateImpl

    USD = CurrencyImpl("USD")
    EUR = CurrencyImpl("EUR")
    AED = CurrencyImpl("AED")
    GBP = CurrencyImpl("GBP")

    today = DateImpl.today()

    ## Generic query:
    query = create_

# Generated at 2022-06-14 04:39:18.980273
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    ## Check that the method fails with invalid arguments:
    with raises(ValueError, match="Invalid arguments!"):
        FXRateService.query()



# Generated at 2022-06-14 04:39:26.835365
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the method queries from class FXRateService.
    """
    from itertools import chain
    from unittest import TestCase, mock

    from pypara.commons import Temporal
    from pypara.currencies import Currency

    ## Mock the foreign exchange rate service:
    rate_service = mock.Mock()
    rate_service.query.side_effect = lambda ccy1, ccy2, asof, strict: FXRate(ccy1, ccy2, asof, Decimal(1))

    ## Test a single query:
    rate = FXRateService.queries(rate_service, ((Currency.BASE, Currency.BASE, Temporal.BASE),), False)

# Generated at 2022-06-14 04:39:32.367704
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    def test_fx_rate_service() -> FXRateService:
        class TestFXRateService(FXRateService):
            def query(self, ccy1, ccy2, asof, strict=False) -> Optional[FXRate]:
                return None

            def queries(self, queries: Iterable[TQuery], strict=False) -> Iterable[Optional[FXRate]]:
                return [None for _ in queries]
        return TestFXRateService()

    assert list(test_fx_rate_service().queries([])) == []
    assert list(test_fx_rate_service().queries([(None, None, None)])) == [None]
    assert list(test_fx_rate_service().queries([(None, None, None), (None, None, None)])) == [None, None]

# Generated at 2022-06-14 04:39:34.799883
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Runs unit tests for method :method:`pypara.finance.fx.FXRateService.query`.
    """
    pass



# Generated at 2022-06-14 04:39:58.089426
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.fxrates import FXRateService

    # Defines a class for testing the query
    class FooRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            nrate = FXRate.of(ccy1, ccy2, asof, Decimal("2"))
            rrate = FXRate.of(ccy2, ccy1, asof, Decimal("0.5"))
            date = datetime.date.today()
            urate = FXRate.of(Currencies["EUR"], Currencies["USD"], date, Decimal("2"))

# Generated at 2022-06-14 04:40:07.638658
# Unit test for method query of class FXRateService

# Generated at 2022-06-14 04:40:18.323816
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Temporal
    from .curves import CurvePoint
    from .fx_rates import FXRateService
    class _FXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable["FXRateService.TQuery"], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return super().queries(queries, strict)

    ## Define the queries:

# Generated at 2022-06-14 04:40:18.984154
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass

# Generated at 2022-06-14 04:40:29.293657
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    # Check if an exception is raised when the arguments are not passed
    try:
        class RateService(FXRateService):
            def query(self):
                pass
        rate_service = RateService()
        rate_service.query()
        return False
    except TypeError as error:
        assert str(error) == "query() missing 3 required positional arguments: 'self', 'ccy1', and 'ccy2'"

    # Check if an exception is raised when the arguments are not passed

# Generated at 2022-06-14 04:40:39.078766
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies

    class MockFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(Currencies["EUR"], Currencies["USD"], asof, Decimal("1.25"))

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [FXRate(Currencies["EUR"], Currencies["USD"], date.today(), Decimal("1.25"))]

    rate = MockFXRateService().query(Currencies["EUR"], Currencies["USD"], date.today())
    assert rate.ccy1

# Generated at 2022-06-14 04:40:50.382620
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """
    class FakeFXRateService(FXRateService):
        """
        Fake FXRateService
        """

# Generated at 2022-06-14 04:40:57.537936
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # import datetime
    from .currencies import Currency

    class FXRateServiceStub(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for ccy1, ccy2, asof in queries:
                yield self.query(ccy1, ccy2, asof, strict)

    service = FXRateServiceStub()
    assert list(service.queries([(Currency("EUR"), Currency("USD"), Date.MIN)])) == [None]

# Generated at 2022-06-14 04:41:06.542369
# Unit test for method query of class FXRateService
def test_FXRateService_query():  # noqa: D102
    """
    Tests FXRateService.query method.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curves import CurveService, LocalCurveService
    from pypara.finance import Finance
    Finance.curve_service = CurveService.default = LocalCurveService()


# Generated at 2022-06-14 04:41:18.135812
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from unittest import TestCase
    from pypara.currencies import Currencies
    from pypara.temporal import Temporal

    from .commons.types import TestData
    from .fixtures.fx_rates import fx_rates_test_data

    fx_rates = fx_rates_test_data()

    class TestableFXRateService(FXRateService):
        def __init__(self, test_data):
            self.test_data = test_data

        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[Decimal]:
            return self.test_data.get((ccy1, ccy2, Date.of(asof)), None)


# Generated at 2022-06-14 04:42:09.259329
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from pypara.commons.zeitgeist import Date
    from pypara.currencies import Currency
    from unittest.mock import Mock
    queries = Mock()
    fxRateService = Mock()
    fxRateService.queries = queries
    fxRateService.queries([(Currency.of("EUR"), Currency.of("USD"), Date.of("2019-01-01")),
                           (Currency.of("EUR"), Currency.of("USD"), Date.of("2019-01-02"))], strict=True)

# Generated at 2022-06-14 04:42:21.297289
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class :class:`FXRateService`.
    """
    # Imports:
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    # Define a foreign exchange rate service:
    class MockFXRateService(FXRateService):
        """
        Defines a mock foreign exchange rate service.
        """


# Generated at 2022-06-14 04:42:30.853680
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from dateutil.parser import parse as date_parse
    from pypara.currencies import Currencies
    from pypara.market import FXRateService


# Generated at 2022-06-14 04:42:41.438467
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    test_query = FXRateService.TQuery(Currencies["EUR"], Currencies["USD"], datetime.date.today())
    test_result = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    test_service = FXRateService()
    try:
        test_service.query(*test_query, strict=True)
        raise AssertionError("Failed to raise `NotImplementedError`.")
    except NotImplementedError:
        pass

# Generated at 2022-06-14 04:42:51.671410
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Test the query function of FXRateService
    """
    import datetime

    from decimal import Decimal

    from pypara.currencies import Currencies

    class FXRateServiceSubClass(FXRateService):
        """
        Subclass of FXRateService
        """
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("2"))

        def queries(self, queries: Iterable[str], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [FXRate(ccy1, ccy2, asof, Decimal("2")) for ccy1, ccy2, asof in queries]


# Generated at 2022-06-14 04:43:03.316090
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    # Import
    from datetime import date
    from decimal import Decimal
    from math import isclose
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    # Create a class implementing the desired functionality
    class MockFXRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"]:
                return FXRate.of(ccy1, ccy2, asof, Decimal('1.18'))
            else:
                return None


# Generated at 2022-06-14 04:43:14.829518
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from .commons.zeitgeist import Date

    class FXRateServiceMock(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal('123.456'))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return []

    fxratesvc = FXRateServiceMock()
    fxrate = fxratesvc.query(Currencies['USD'], Currencies['JPY'], Date(date(2020, 12, 11)))

    assert fxrate
    assert isinstance(fxrate, FXRate)

# Generated at 2022-06-14 04:43:23.551836
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests FX rate collection lookup of an abstract FX rate service.
    """
    from .currencies import Currencies
    from .temporals import Date

    from unittest import mock

    class MockService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False):
            return None

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False):
            return mock.DEFAULT

    ## Arrange:
    service = MockService()

    ## Act:
    queries = [
        (Currencies["EUR"], Currencies["USD"], Date(2018, 12, 31)),
        (Currencies["JPY"], Currencies["GBP"], Date(2019, 1, 1))
    ]

    ## Assert:


# Generated at 2022-06-14 04:43:37.175590
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():  # noqa: D103
    from .currencies import Currency, Currencies
    from .temporal import Temporal, Date
    from decimal import Decimal
    try:
        from hypothesis import given, example
        from hypothesis.strategies import tuples, integers, lists
    except ImportError:
        pass

# Generated at 2022-06-14 04:43:49.134000
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class TestFXRateService(FXRateService):

        def __init__(self, queries: Iterable[FXRateService.TQuery] = None) -> None:
            self.queries = queries or []

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            for query in self.queries:
                if query != (ccy1, ccy2, asof):
                    continue
                return FXRate(ccy1, ccy2, asof, ONE)
            return None
