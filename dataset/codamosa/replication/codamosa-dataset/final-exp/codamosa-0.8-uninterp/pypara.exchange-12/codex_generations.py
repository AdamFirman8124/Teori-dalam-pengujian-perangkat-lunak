

# Generated at 2022-06-14 04:34:35.172811
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method :method:`FXRateService.query` on class :class:`FXRateService`.
    """
    from unittest.mock import Mock
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    ## Create a service and an FX rate:
    service: FXRateService = Mock()
    fxrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

    ## Create a mock query:
    service.query.return_value = fxrate

    ## Test:
    assert service.query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) == fxrate



# Generated at 2022-06-14 04:34:45.593367
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    from unittest import TestCase
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class _(TestCase):
        def test_when_values_are_not_inverted(self):
            nrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("5"))
            rrate = FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.2"))
            self.assertEqual(~nrate, rrate)

    _().test_when_values_are_not_inverted()


# Generated at 2022-06-14 04:34:58.735633
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """
    # Imports
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.fx.rates import FXRateService
    from pypara.temporal import Temporal

    # Helper class
    class FXRateServiceImpl(FXRateService):
        """
        Dummy implementation of class FXRateServiceImpl
        """

        def __init__(self) -> None:
            """
            Initialize the dummy implementation of class FXRateServiceImpl
            """
            # References

# Generated at 2022-06-14 04:34:59.969587
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    pass


# Generated at 2022-06-14 04:35:13.581827
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx_rates.services import DummyFXRateService

    ## Service test:
    fx_service = DummyFXRateService()
    assert fx_service.query(Currencies["USD"], Currencies["GBP"], datetime.date.today(), strict=False) is None

    ## Full query test:
    fx_rate = fx_service.query(Currencies["USD"], Currencies["GBP"], datetime.date.today(), strict=True)
    assert fx_rate.ccy1 == Currencies["USD"]
    assert fx_rate.ccy2 == Currencies["GBP"]
    assert fx_rate.date == datetime.date.today()

# Generated at 2022-06-14 04:35:24.341399
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    import datetime
    import pytest

    from decimal import Decimal
    from pypara.currencies import Currencies

    ## Instantiate the FX rate:
    nrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))

    ## Check the invert:
    assert (~nrate).value == Decimal("0.5")
    assert (~nrate)[0] == Currencies["USD"]
    assert (~nrate)[1] == Currencies["EUR"]
    assert (~nrate)[2] == datetime.date.today()

    ## Check the invert of the inverted rate:
    assert ~~nrate == nrate


# Generated at 2022-06-14 04:35:28.637536
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    #
    # >>> import datetime
    # >>> from decimal import Decimal
    # >>> from pypara.currencies import Currencies
    #
    # Query with EUR/USD
    # >>> FXRateService().query(Currencies["EUR"], Currencies["USD"], datetime.date.today())
    #
    pass

# Generated at 2022-06-14 04:35:36.481289
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test the FXRateService.queries method.
    """
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.dummy import FXRateDummyService
    from pypara.temporal.zeitgeist import Date

    ## Ensure the dummy service is loaded:
    FXRateDummyService.load()

    ## Check the type:
    assert isinstance(FXRateService.default, FXRateDummyService)

    ## Query a few rates:

# Generated at 2022-06-14 04:35:39.683577
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    from pypara.currencies import Currencies
    assert not ~FXRate(Currencies["EUR"], Currencies["USD"], Date.today, 1)


# Generated at 2022-06-14 04:35:51.132168
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime

    from decimal import Decimal

    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    ## Define a test FX rate service:
    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 is Currencies["USD"] and ccy2 is Currencies["EUR"] and asof is Date("2016-12-31"):
                return FXRate(Currencies["USD"], Currencies["EUR"], Date("2016-12-31"), Decimal("0.9637"))
            else:
                return None


# Generated at 2022-06-14 04:35:56.587044
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    '''
    Testing the method query of class FXRateService.
    '''
    pass


# Generated at 2022-06-14 04:36:02.003403
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the query method of the FXRateService class.
    """
    from unittest import mock

    ccy1 = mock.Mock()
    ccy2 = mock.Mock()
    asof = mock.Mock()
    strict = mock.Mock()
    fxrateservice = FXRateService()

    try:
        fxrateservice.query(ccy1, ccy2, asof, strict)
        assert False, "Should not get here."
    except NotImplementedError:
        pass


# Generated at 2022-06-14 04:36:10.646164
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    import datetime

    from decimal import Decimal

    from pypara.currencies import Currencies

    nrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    rrate = FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.5"))

    assert ~nrate == rrate, f"The inverted version of {nrate} must be {rrate}."


# Unit tests for method of of class FXRate

# Generated at 2022-06-14 04:36:15.354542
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    """
    Tests the ~ operator on FXRate.
    """
    from .currencies import Currencies
    import datetime
    from decimal import Decimal
    nrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    rrate = FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.5"))
    assert ~nrate == rrate


# Generated at 2022-06-14 04:36:24.714387
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    urate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    ifr = ~urate
    assert ifr.ccy1 == urate.ccy2
    assert ifr.ccy2 == urate.ccy1
    assert ifr.date == urate.date
    assert ifr.value == urate.value ** -1
    assert ~ifr == urate

# Generated at 2022-06-14 04:36:32.287267
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    ## Setup
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    nrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    rrate = FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.5"))

    assert ~nrate == rrate

# Generated at 2022-06-14 04:36:43.672240
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .dates import Date
    from .temporal import Temporal
    from .temporal.lookupservices import HistoricalTemporalLookupService

    class MockRateService(FXRateService):
        def __init__(self) -> None:
            self.rates = []
            for ccy1 in (Currency.USD, Currency.GBP, Currency.CHF):
                for ccy2 in (Currency.USD, Currency.GBP, Currency.CHF):
                    self.rates.append(FXRate(ccy1, ccy2, Date.of_date(2000, 1, 1), Decimal(2)))


# Generated at 2022-06-14 04:36:50.388456
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    import datetime

    from decimal import Decimal

    from pypara.currencies import Currencies

    nrate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    rrate = ~nrate
    assert rrate.ccy1 == Currencies["USD"]
    assert rrate.ccy2 == Currencies["EUR"]
    assert rrate.date == nrate.date
    assert rrate.value == Decimal("0.5")


# Generated at 2022-06-14 04:36:58.659450
# Unit test for method __invert__ of class FXRate
def test_FXRate___invert__():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    rate = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    assert rate[0] == Currencies["EUR"]
    assert rate[1] == Currencies["USD"]
    assert rate[2] == datetime.date.today()
    assert rate[3] == Decimal("2")
    assert ~rate == FXRate(Currencies["USD"], Currencies["EUR"], datetime.date.today(), Decimal("0.5"))


# Generated at 2022-06-14 04:37:12.592974
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    """
    Unit test for method queries of class FXRateService
    """

    import datetime

    from pypara.currencies import Currency, Currencies
    from pypara.date_time import Date

    # Create a dummy FX rate service:
    class DummyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return []

    # Create a dummy FX rate service:

# Generated at 2022-06-14 04:37:33.087363
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the `queries` method of :class:`FXRateService`.
    """
    from unittest.mock import patch
    from .commons.temporal import DateRange
    from .currencies import Currency, Currencies

    ## Patch `query`:
    with patch.object(FXRateService, "query") as query:
        query.return_value = None

        ## Create a range:
        range_ = DateRange(Date(2018, 1, 1), Date(2019, 1, 1))

        ## Create a service:
        service = FXRateService()

        ## Query:
        service.queries(
            ((Currencies["EUR"], Currencies["USD"], date) for date in range_), strict=True)

        ## Verify that the query method was called with the right arguments:
        query.assert_called_with

# Generated at 2022-06-14 04:37:34.572673
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:37:47.291353
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import pytest
    from pypara.currencies import Currencies
    from pypara.temporal import Temporal
    from datetime import date

    class Impl(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Temporal, strict: bool = False) -> Optional[FXRate]:
            pass
        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            for ccy1, ccy2, asof in queries:
                yield None

    assert list(Impl().queries([(Currencies["USD"], Currencies["EUR"], date.today())])) == [None]

# Generated at 2022-06-14 04:37:57.471219
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx.rates import FXRate
    from pypara.fx.services import FXRateService

    class MockService(FXRateService):
        """
        Provides a mock implementation for :class:`FXRateService` for unit-testing purpose.
        """

        #: Defines the supported foreign exchange rates.

# Generated at 2022-06-14 04:37:59.344165
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # todo: Add test cases
    pass


# Generated at 2022-06-14 04:38:07.432329
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx.services import FXRateService
    from pypara.fx.services.memory import MemoryFXRateService

    ## Create a mock service:
    service = MemoryFXRateService()
    rate1 = FXRate(Currencies["EUR"], Currencies["USD"], datetime.date.today(), Decimal("2"))
    rate2 = FXRate(Currencies["GBP"], Currencies["EUR"], datetime.date.today(), Decimal("2"))
    service.put(rate1)
    service.put(rate2)

    ## Create the queries:
    query1 = Currencies["EUR"], Currencies["USD"], datetime.date.today()
    query2 = Currencies["GBP"], Currencies["USD"], dat

# Generated at 2022-06-14 04:38:19.132271
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .commons.zeitgeist import Date
    from .currencies import Currency

    class DummyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return None

        def queries(self, queries: Iterable[FXRateService.TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return ()

    ## Create a service instance:
    subject = DummyFXRateService()

    ## Query a rate:
    assert subject.query(Currency.EUR, Currency.USD, Date.today) is None



# Generated at 2022-06-14 04:38:27.721310
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest.mock import Mock
    from pypara.currencies import Currencies
    from pypara.temporal import Dates
    from ..temporal import date

    ## Define the mock object:
    mock = Mock(spec=FXRateService)

    ## Define the queries:

# Generated at 2022-06-14 04:38:33.747340
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .temporal import Dates
    from .fx_rates import FXRates
    assert [rate for rate in FXRateService.default.queries(
        [(Currencies["EUR"], Currencies["USD"], Dates.today()),
         (Currencies["EUR"], Currencies["USD"], Dates.today())])] == \
           [FXRates.eurusd(Dates.today()), FXRates.eurusd(Dates.today())]

# Generated at 2022-06-14 04:38:45.149628
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """

    ## Test FX rate service:
    class TestFXRateService(FXRateService):
        """
        Test FX rate service.
        """

        def __init__(self, rates: Iterable[FXRate]) -> None:
            """
            Initializes the test FX rate service.
            """
            self.__rates = dict(rates)

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, stict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            return self.__rates.get((ccy1, ccy2, asof))


# Generated at 2022-06-14 04:39:11.872187
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currency, Currencies
    from .commons.zeitgeist import Date
    from decimal import Decimal
    from pypara.fx.rates import FXRate

    # Create the pair of currencies and the temporal dimension:
    ccy1 = Currencies["USD"]
    ccy2 = Currencies["TRY"]
    asof = Date.today()

    # Create the fxrate object
    fxrate = FXRate(ccy1, ccy2, asof, Decimal(6.3))

    # Test
    def query(sself, ccy1, ccy2, asof):
        return fxrate


    # Test
    def queries(sself, qs, strict):
        # Return an iterable of fxrates
        return [fxrate]

    # Create a service:
    service = type

# Generated at 2022-06-14 04:39:12.913549
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    impo

# Generated at 2022-06-14 04:39:22.626759
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.rates.fxrates import FXRateService, FXRateServiceError, FXRate

    ## Dummy FXRateService service:
    class DummyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == datetime.date.today():
                return FXRate(ccy1, ccy2, asof, Decimal("2"))

            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return

# Generated at 2022-06-14 04:39:35.363785
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class :class:`FXRateService`.
    """
    import pandas as pd
    import pandas.util.testing as tm

    class _FXRateService(FXRateService):
        """
        Provides an implementation of the FX rate service interface with a fixed foreign exchange rate table.
        """

        #: Foreign exchange rate table.
        table: pd.DataFrame = pd.DataFrame(
            {"CCY1": ["EUR", "EUR", "EUR"], "CCY2": ["USD", "JPY", "EUR"], "ASOF": ["2019-07-17", "2019-07-17", "2019-07-17"], "VALUE": ["1.11", "120.50", "1"]}
        )


# Generated at 2022-06-14 04:39:47.859781
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currencies
    from .commons.zeitgeist import Date

    class TestService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, ONE)

        def queries(self, queries: Iterable[FXRateService.TQuery]):
            for query in queries:
                yield self.query(*query)

    ## Query for some random exchange rates
    service = TestService()

# Generated at 2022-06-14 04:39:57.428054
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests :meth:`FXRateService.queries`
    """
    # Import required modules
    import datetime

    from decimal import Decimal

    from pypara.currencies import Currencies

    # Create a query sequence

# Generated at 2022-06-14 04:40:07.287360
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService
    """
    ## Define a dummy service:
    class DummyService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return None

    ## Define a dummy FX rate:
    from pypara.currencies import Currencies
    from .commons.zeitgeist import dates
    from .commons.numbers import ONE
    from .fx import FXRate

    dummy_rate = FXRate(Currencies["USD"], Currencies["GBP"], dates.today(), ONE)

    ## Define a dummy service (with a function):

# Generated at 2022-06-14 04:40:20.038030
# Unit test for method query of class FXRateService
def test_FXRateService_query(): # noqa: E501
    import datetime
    import decimal
    import pytest
    from pypara.currencies import Currencies

    class Foo():
        def __init__(self, ccy1, ccy2, asof, value):
            self.ccy1 = ccy1
            self.ccy2 = ccy2
            self.asof = asof
            self.value = value

    class FooService(FXRateService):
        def __init__(self, rates: Iterable[Foo]):
            self.rates = []
            for rate in rates:
                self.rates.append((rate.ccy1, rate.ccy2, rate.asof, rate.value))


# Generated at 2022-06-14 04:40:30.140155
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class FXRateService
    """
    from pypara.currencies import Currencies
    class FXServiceStub(FXRateService):
        """
        Provides a stub that simulates FX rate service
        """
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns the foreign exchange rate of a given currency pair as of a given date.
            """
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == Date(2020, 5, 19):
                return FXRate(Currencies["EUR"], Currencies["USD"], Date(2020, 5, 19), Decimal("2"))
            return None

# Generated at 2022-06-14 04:40:39.864446
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .temporal import Temporal
    from .temporals import Temporals
    from .fxrates import FXRates

    ## Create and check the query iterable:
    queries = ((Currency("USD"), Currency("EUR")), (Currency("EUR"), Currency("USD")))
    asof = Temporals.now().date
    rates = FXRates.default.queries(queries, asof)
    assert rates[0].ccy1 == Currency("USD")
    assert rates[0].ccy2 == Currency("EUR")
    assert rates[0].date == asof
    assert rates[0].value > 1
    assert rates[1].ccy1 == Currency("EUR")
    assert rates[1].ccy2 == Currency("USD")

# Generated at 2022-06-14 04:41:23.264696
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRate, FXRateService
    from pypara.temporal import Today
    ##
    class FXRateServiceMock(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == date.today():
                return FXRate.of(Currencies["EUR"], Currencies["USD"], date.today(), Decimal("1.2"))
            else:
                return None

# Generated at 2022-06-14 04:41:31.475198
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the query method of FXRateService.
    """
    from decimal import Decimal
    from unittest import TestCase
    from pypara.currencies import Currency, Currencies
    from pypara.exchange.rates import FXRate, FXRateService
    from pypara.temporals import Temporals

    # Some ISO 4217 currencies
    class Ccy:
        AUD = Currencies["AUD"]
        CAD = Currencies["CAD"]
        CHF = Currencies["CHF"]
        EUR = Currencies["EUR"]
        GBP = Currencies["GBP"]
        SEK = Currencies["SEK"]
        TRY = Currencies["TRY"]
        USD = Currencies["USD"]

    # Some unit test cases

# Generated at 2022-06-14 04:41:37.533048
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService
    ## The class under test:
    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return FXRate(ccy1, ccy2, asof, Decimal("0.5"))
        def queries(self, queries, strict=False):
            for query in queries:
                yield self.query(*query)
    ## Initialize the service:
    service = TestFXRateService()
    ## Run the query method:

# Generated at 2022-06-14 04:41:48.198209
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    ## import modules:
    import unittest

    ## import packages:
    from pypara.currencies import Currency
    from pypara.time import Date

    ## test the non-strict case:
    class FXRateServiceStub:
        """
        Provides a stub implementation of the :class:`FXRateService` class.
        """

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Returns an FX rate for the specified query.
            """

# Generated at 2022-06-14 04:41:59.350670
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit testing of method queries of class FXRateService.
    """
    from .commons.zeitgeist import Date
    from .currencies import Currencies
    from .services import DatedFXRateService
    from ..finance import USD, EUR, GBP
    from ..utils import close_enough

    ## Generate the FX rates:

# Generated at 2022-06-14 04:42:10.109108
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from .currencies import Currencies
    from .commons.zeitgeist import Date
    from .fx import FXRate, FXRateService
    from decimal import Decimal

    class BogusFXRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict=False):
            if ccy1 == Currencies["EUR"] and ccy2 == Currencies["USD"] and asof == Date.todays(Date.ISO):
                return FXRate(Currencies["EUR"], Currencies["USD"], asof, Decimal("2"))

# Generated at 2022-06-14 04:42:22.425089
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from pypara.currencies import Currencies
    from pypara.datetime import Date, Days
    from pypara.exchange import FXRateService
    import datetime
    from decimal import Decimal

    class DummyFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currencies["USD"] and ccy2 == Currencies["EUR"] and asof == Date(datetime.date.today()):
                return FXRate(Currencies["USD"], Currencies["EUR"], Date(datetime.date.today()), Decimal("0.8"))

# Generated at 2022-06-14 04:42:31.409176
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Checks the implementation of :method:`FXRateService.queries`
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance.fx import FXRateService

    ## Define the query collection:
    queries = [(Currencies["EUR"], Currencies["USD"], datetime.date.today())]

    ## Define and create the service:
    service = type("Service", (FXRateService,), dict(
        queries = lambda self, requests, strict = False: [FXRate.of(ccy1, ccy2, date, Decimal("2")) for ccy1, ccy2, date in requests]
    ))()

    ## Check the input validation:

# Generated at 2022-06-14 04:42:37.380786
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method FXRateService.queries.
    """

    # Imports:
    from datetime import date

    from .currencies import Currency, Currencies

    # Test case 1:
    # Test a strict FX rate service:
    class MyFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if asof == date(2017, 1, 1):
                return FXRate(ccy1, ccy2, asof, ONE)
            else:
                return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return (self.query(*query) for query in queries)

    service = MyFXRate

# Generated at 2022-06-14 04:42:49.698187
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for method query of class FXRateService
    """
    import datetime
    from decimal import Decimal
    from pypara.base.fxtrades import FXTrade
    from pypara.currencies import Currencies

    ## Define two FX trades:
    ft1 = FXTrade(Currencies["USD"], Currencies["EUR"], datetime.datetime.now(), Decimal("2"), Decimal("2"), Decimal("1000"))
    ft2 = FXTrade(Currencies["EUR"], Currencies["USD"], datetime.datetime.now(), Decimal("1"), Decimal("1"), Decimal("1000"))

    ## Create a rate service:
    from pypara.currencies.rateservices import FXRateServiceMemory

# Generated at 2022-06-14 04:44:12.185569
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    #
    # Test method query when an FX rate service is given and it supports the foreign exchange rate lookup.
    #

    # First, let's create a mock FX rate service:
    class MockFXRateService(FXRateService):
        def query(self, ccy1, ccy2, dtime, strict):
            assert ccy1 == Currency("EUR")
            assert ccy2 == Currency("USD")
            assert dtime == Date(2012, 12, 31)
            assert strict == False
            return FXRate(Currency("EUR"), Currency("USD"), Date(2012, 12, 31), Decimal("2"))

        def queries(self, queries, strict):
            assert len(queries) == 1
            assert queries[0] == (Currency("EUR"), Currency("USD"), Date(2012, 12, 31))
            assert strict == False

# Generated at 2022-06-14 04:44:23.175705
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the :method:`FXRateService.query` method.
    """
    import unittest

    from pypara.currencies import Currencies
    from pypara.temporal import Dates

    ## Create a dummy class:
    class Dummy(FXRateService):
        _data = {
            (Currencies["EUR"], Currencies["USD"], Dates.today()): FXRate(Currencies["EUR"], Currencies["USD"], Dates.today(), 2)
        }

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self._data[(ccy1, ccy2, asof)]
