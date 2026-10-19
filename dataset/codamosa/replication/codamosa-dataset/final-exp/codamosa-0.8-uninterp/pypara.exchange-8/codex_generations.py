

# Generated at 2022-06-14 04:34:33.923125
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from decimal import Decimal
    from datetime import date
    from pypara.currencies import Currency, Currencies
    from pypara.quotes.fxrates import FXRateService

    class FxRateService(FXRateService):
        def __init__(self):
            pass

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if (ccy1==Currencies["USD"] and ccy2==Currencies["EUR"] and asof==date(2019,10,1)):
                return FXRate(Currencies["USD"], Currencies["EUR"], date(2019, 10, 1), Decimal("1.1"))
            else:
                return None


# Generated at 2022-06-14 04:34:36.201211
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    #pylint: disable=E1133
    #pylint: disable=C0330
    pass

# Generated at 2022-06-14 04:34:47.554120
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .commons.zeitgeist import now
    from .currencies import Currencies

    class StubFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, asof.day)

        def queries(self, queries: Iterable[Tuple[Currency, Currency, Date]], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return super().queries(queries, strict)

    rate_service = StubFXRateService()

# Generated at 2022-06-14 04:34:59.344615
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from unittest import TestCase, main
    from unittest.mock import patch
    from .currencies import Currency

    from .fxrates import FXRateService
    from .fxrates.fxrates import FXRateService as FXRateServiceImpl

    class TestCaseImpl(TestCase):

        def test_query_exception(self):
            with patch.object(FXRateServiceImpl, "query", side_effect=LookupError):
                with self.assertRaises(LookupError):
                    FXRateService.query(Currency.of("USD"), Currency.of("TRY"), Date.now())


# Generated at 2022-06-14 04:35:12.952278
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies


# Generated at 2022-06-14 04:35:19.614300
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRate
    from pypara.fxservices.inmemory import InMemoryFXRateService
    from pypara.temporals import Period
    import unittest

    class TestFXRateService(InMemoryFXRateService):
        """
        Provides a test class for reviewing the method queries of class FXRateService.
        """

        @staticmethod
        def _get_date(date: datetime.date, period: Period) -> datetime.date:
            """
            Returns a date that exists in a given period.

            :param date: The reference date.
            :param period: The period.
            :return: A date that exists in a given period.
            """

# Generated at 2022-06-14 04:35:20.248721
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    pass

# Generated at 2022-06-14 04:35:32.241488
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class FXRateService.
    """
    import datetime
    from decimal import Decimal
    from unittest.mock import MagicMock, Mock
    from pypara.currencies import Currencies
    from pypara.fxrates import FXRateService, FXRate

    ## Mock the query function of the FXRateService:
    FXRateService.query = MagicMock()

    ## Create a mock service:
    service = Mock(spec=FXRateService)

    ## Create a mock iterator:
    asof = datetime.date.today()

# Generated at 2022-06-14 04:35:45.591263
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .identities import Identity

    from .currencies import Currencies
    from .temporal import Temporal

    from .exchange import FXRateServiceMock
    from .exchange import FXRateServiceProxy

    fx_rate_service = FXRateServiceMock()
    fx_rate_service_proxy = FXRateServiceProxy(fx_rate_service)

    ## Run the queries:

# Generated at 2022-06-14 04:35:52.859411
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    # Fixtures:
    from datetime import date
    from pypara.currencies import Currencies  # noqa: E402

    # Setting up the FX rate factory:
    FXRateFactory = FXRate.of

    # Setting up the example FX rate:
    EUR_USD = FXRateFactory(Currencies["EUR"], Currencies["USD"], date.today(), Decimal("2"))
    USD_EUR = FXRateFactory(Currencies["USD"], Currencies["EUR"], date.today(), Decimal("0.5"))

    # Setting up the FX rate service:
    class ExampleFXRateService(FXRateService):
        """
        An example FX rate service.
        """


# Generated at 2022-06-14 04:36:05.799655
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class MyFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate.of(ccy1, ccy2, date, Decimal("{0}".format(date.year % 1000)))

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return map(lambda q: self.query(*q, strict=strict), queries)

    service = MyFXRateService()

    date = datetime.date.today()

    query1 = (Currencies["CHF"], Currencies["EUR"], date)
    query

# Generated at 2022-06-14 04:36:15.283903
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from .currencies import Currency
    from .temporal import Temporal
    from .rates import ZERORateService
    from .fxrates import FXRateService
    from .fxrates import FXRate
    from datetime import date
    from decimal import Decimal

    # Create a foreign exchange rate service around the zero rate service:
    service = FXRateService.from_rates(ZERORateService())

    # Create a bunch of queries:
    queries = [
        (Currency("EUR"), Currency("USD"), date(2020, 1, 1)),
        (Currency("EUR"), Currency("USD"), date(2020, 1, 2)),
        (Currency("EUR"), Currency("USD"), date(2020, 1, 3)),
    ]

    # Query the service:
    results = tuple(service.queries(queries))

    # Check the

# Generated at 2022-06-14 04:36:25.409358
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    # class Fx(FXRateService):  # noqa: WPS211
    #     def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
    #         return FXRate(ccy1, ccy2, asof, Decimal("1"))

    # fx = Fx()
    # fx.query(Currencies["EUR"], Currencies["USD"], datetime.date.today(), strict=False)


# Generated at 2022-06-14 04:36:38.620996
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of the FXRateService class. Note that this test method uses the built-in
    module 'unittest'.

    **Usage**

    In order to run this test module, you can simply type the following command in the root folder of the library::

        $ python -m unittest pypara.rates.test_FXRateService_queries

    If you are using the terminal, you can also use the following command::

        $ python -m unittest discover -s pypara.rates -t pypara/rates
    """
    import unittest
    import datetime
    from decimal import Decimal
    from pypara.currencies.currencies import Currencies
    from pypara.rates.fx_rate_service import FXRateService
    from pypara.temporal.date import Date


# Generated at 2022-06-14 04:36:48.682582
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    class TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, 1.0)

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(ccy1, ccy2, asof) for ccy1, ccy2, asof in queries]

    service = TestFXRateService()
    assert len(list(service.queries([]))) == 0
    assert len(list(service.queries([(1, 2, 3)]))) == 1

# Generated at 2022-06-14 04:36:59.780427
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests the queries method of class FXRateService.
    """
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx import FXRateService

    class TestFXRateService(FXRateService):
        """
        Provides a test class for FXRateService.
        """
        def __init__(self):
            self.rates = {
                (Currencies["USD"], Currencies["EUR"], datetime.date.today()): Decimal("0.5")
            }


# Generated at 2022-06-14 04:37:13.242502
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.services.fxrates import FXRateService

    class MyFXRateService(FXRateService):

        def __init__(self):
            self._rates = {
                (Currencies["EUR"], Currencies["USD"], datetime.date.today()): Decimal("2"),
                (Currencies["USD"], Currencies["EUR"], datetime.date.today()): Decimal("1.5")
            }

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            try:
                return self._rates[(ccy1, ccy2, asof)]
            except KeyError:
                if strict:
                    raise FX

# Generated at 2022-06-14 04:37:14.939585
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    assert __doc__


# Generated at 2022-06-14 04:37:28.531314
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """

    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.time import today

    class FXRateServiceStub(FXRateService):
        """
        A stub class for testing the queries method of the FXRateService class.
        """

        def __init__(self):
            """
            Initializes an FXRateServiceStub instance.
            """

# Generated at 2022-06-14 04:37:39.984086
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    from unittest import TestCase, main
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curves.time import Temporal  # noqa: F401

    class TestFXRateService(FXRateService):

        def __init__(self):
            super().__init__()
            self._rates = {(Currencies["EUR"], Currencies["USD"], Temporal.of("2019-01-01", False)): Decimal("1.00")}

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return self._rates.get((ccy1, ccy2, asof), None)


# Generated at 2022-06-14 04:37:57.121497
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService.
    """

    ## Initialize FX rate service
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies

    class MyFXRateService(FXRateService):  # pragma: no cover
        """
        Provides a mock foreign exchange rate service.
        """

        def __init__(self):
            self.rates = {
                (Currencies["EUR"], Currencies["USD"], datetime.date.today()): Decimal("1.2"),
                (Currencies["USD"], Currencies["EUR"], datetime.date.today()): Decimal("0.8333"),
            }


# Generated at 2022-06-14 04:38:06.244258
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.currencies.conversions import FXRate, FXRateService

# Generated at 2022-06-14 04:38:18.085872
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Verifies if the queries method of class FXRateService works as expected.
    """
    # Define the unit under test:
    uut = FXRateService()

    # Get the number of abstract methods:
    abstract_methods_len = len(uut.__abstractmethods__)

    # Define a query:
    query = (
        (Currency("EUR"), Currency("USD"), Date.today()),
        (Currency("USD"), Currency("EUR"), Date.today()),
        (Currency("USD"), Currency("TRY"), Date.today()))

    # Check that the method is abstract:
    assert len(uut.__abstractmethods__) == abstract_methods_len

    # Check the results:

# Generated at 2022-06-14 04:38:30.524492
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.exchanges import FXRateService, FXRate

    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False):
            return None

    queries = [
        (Currencies["USD"], Currencies["TRY"], datetime.date.today()),
        (Currencies["GBP"], Currencies["TRY"], datetime.date.today()),
        (Currencies["EUR"], Currencies["TRY"], datetime.date.today()),
    ]

    fxService = TestFXRateService()
    fxRates = fxService.queries(queries)

    for fxRate in fxRates:
        assert(fxRate is None)

# Generated at 2022-06-14 04:38:39.214636
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the query method of class FXRateService.
    """
    from decimal import Decimal
    from unittest import TestCase, TestSuite, TextTestRunner
    from pypara.currencies import Currencies
    from pypara.time import Date

    class TestFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict = False):
            return FXRate(ccy1, ccy2, asof, Decimal("1.1"))

        def queries(self, queries, strict = False):
            return tuple([self.query(query[0], query[1], query[2]) for query in queries])

    class TestFXRateServiceTestCase(TestCase):
        def test_query_with_currency_pair_and_date(self):
            service = TestFXRate

# Generated at 2022-06-14 04:38:46.718959
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    from collections import deque
    from datetime import date

    from pypara.currencies import EUR, USD
    from unittest import mock

    ## Create and initialize fx_rates:
    fx_rates = deque()
    fx_rates.append(FXRate(EUR, USD, date(2018, 1, 1), Decimal(1.25)))
    fx_rates.append(FXRate(EUR, USD, date(2018, 1, 2), Decimal(1.26)))
    fx_rates.append(FXRate(EUR, USD, date(2018, 1, 3), Decimal(1.27)))

    ## Mocking query method:

# Generated at 2022-06-14 04:38:59.321595
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Unit test for method queries of class FXRateService
    """

    # Import packages:
    import datetime
    import locale
    import pytest
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance.fx import FXRate

    # Set the locale:
    locale.setlocale(locale.LC_ALL, 'en_US')

    # Define the FX rate service:
    class TestFXRateService(FXRateService):
        """
        Test FX rate service class.
        """

        #: Defines the rate model.
        TModel = Tuple[Currency, Currency, datetime.date, Decimal]

        #: Defines the in-memory rates.

# Generated at 2022-06-14 04:39:12.072718
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    '''
        This is a unit test for method query of class FXRateService.
        Given two different currencies, i.e. EUR and USD as ccy1 and ccy2,
        and an arbitrary asof date, the method should return the foreign exchange rate of a given currency pair as of
        a given date
    '''

    # Given
    class FXRateServiceTest(FXRateService):
        def query(self, ccy1, ccy2, asof, strict = False):
            return FXRate(ccy1, ccy2, asof, Decimal("2"))

    # When
    actual = FXRateServiceTest().query(Currency("EUR"), Currency("USD"), Date(2020, 6, 26))

    # Then

# Generated at 2022-06-14 04:39:21.793154
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.currencies import Currencies
    from pypara.temporal import Date
    from pypara.fxrates import FXRate, FXRateService

    class FXRateServiceImpl(FXRateService):
        def __init__(self, fxrates: Iterable[FXRate]) -> None:
            self.fxrates = {(rate[0], rate[1], rate[2]): rate[3] for rate in fxrates}

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[Decimal]:
            def lookup(ccy1: Currency, ccy2: Currency, asof: Date) -> Decimal:
                assert ccy1 in Currencies.collection and ccy

# Generated at 2022-06-14 04:39:28.259486
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():  # noqa: D103
    from datetime import date
    from decimal import Decimal
    from pypara.currencies import Currency
    from pypara.fxrates.services import MemoryFXRateService

    # Build the FX rates:

# Generated at 2022-06-14 04:39:53.891691
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from datetime import date
    import pytest
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.fx.services import ArrayFXRateService

    # Check FXRateService.query(ccy1, ccy2, asof, strict)
    ## Create a rate service:
    with pytest.raises(TypeError):
        FXRateService()
    service = ArrayFXRateService()
    assert isinstance(service, FXRateService)

    ## Check FXRateService.query(ccy1, ccy2, asof, strict)
    assert service.query(Currencies["EUR"], Currencies["USD"], date.today(), False) == None

# Generated at 2022-06-14 04:40:00.593914
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    assert FXRateService().query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) is None
    assert FXRateService(strict=True).query(Currencies["EUR"], Currencies["USD"], datetime.date.today()) is None



# Generated at 2022-06-14 04:40:08.878642
# Unit test for method query of class FXRateService
def test_FXRateService_query(): # noqa: D103
    from unittest.mock import MagicMock, patch
    from .currencies import Currency
    from .zeitgeist import Date
    from .commons import Decimal

    ## Patch `query_impl` method:
    with patch.object(FXRateService, "query_impl") as mock_query_impl:
        ## Create the mock implementation:
        mock_rate1_impl  = MagicMock(spec=FXRate)
        mock_rate2_impl  = MagicMock(spec=FXRate)
        mock_query_impl.side_effect = [mock_rate1_impl, mock_rate2_impl]

        ## Create the service:
        service = FXRateService()

        ## Mock the FX rates:
        mock_rate1 = MagicMock(spec=FXRate)
        mock_rate2

# Generated at 2022-06-14 04:40:21.854706
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Test method queries of class FXRateService
    """
    from .currencies import Currency as Currency

    class Test_FXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            if ccy1 == Currency.USD and ccy2 == Currency.EUR:
                return FXRate(ccy1, ccy2, asof, Decimal("2"))
            elif ccy1 == Currency.EUR and ccy2 == Currency.USD:
                return FXRate(ccy1, ccy2, asof, Decimal("0.5"))
            else:
                return None


# Generated at 2022-06-14 04:40:28.749225
# Unit test for method query of class FXRateService
def test_FXRateService_query():

    # The tested class (may provide a mock service):
    class _FXRateService(FXRateService):

        def query(self, ccy1, ccy2, asof, strict):
            return None

    # The tested FX rate service:
    service = _FXRateService()

    # The FX rate service must not be none:
    assert service is not None


# Generated at 2022-06-14 04:40:34.689111
# Unit test for method query of class FXRateService

# Generated at 2022-06-14 04:40:45.997165
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService.
    """
    ## Create an empty FX rate service:
    class EmptyFXRateService(FXRateService):
        """
        Provides an empty FX rate service.
        """

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            """
            Returns foreign exchange rates for a given collection of currency pairs and dates.

            :param queries: An iterable of :class:`Currency`, :class:`Currency` and :class:`Temporal` tuples.
            :param strict: Indicates if we should raise a lookup error if that the foreign exchange rate can not be found.
            :return: An iterable of rates.
            """
            return iter([])

    ## Check if the method correctly handles empty queries:

# Generated at 2022-06-14 04:40:55.811560
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method queries of class FXRateService
    """
    from .commons.zeitgeist import Date, Temporal
    from .currencies import Currency
    from datetime import date
    from unittest import TestCase
    from typing import Iterator, Iterable, NamedTuple
    from unittest.mock import MagicMock, patch, ANY
    from pypara.fxrates import FXRateService
    from pypara.fxrates import FXRateLookupError
    from typing import Tuple
    from decimal import Decimal
    class MockFXRateService(FXRateService):
        def query(self, ccy1, ccy2, asof, strict=False) -> Optional[FXRate]:
            pass

# Generated at 2022-06-14 04:40:58.522390
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests the query method of the FXRateService class.
    """
    # TODO: Implement unit test



# Generated at 2022-06-14 04:41:07.068117
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.curves import Curve
    from pypara.temporals import DateSequence, Frequency

    ccy1 = Currencies["USD"]
    ccy2 = Currencies["EUR"]
    curve = Curve(DateSequence(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31), Frequency.MONTHLY),
                  (Decimal(x) for x in range(1, 13)))

    def FXRateService_from_curve(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False
                                 ) -> Optional[FXRate]:
        return FXRate(ccy1, ccy2, asof, curve.get(asof))



# Generated at 2022-06-14 04:41:59.244494
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():

    from .currencies import Currency
    from .temporal import Temporal
    from .values import Value

    from .enums import Units
    from .enums.units import Currencies

    ##
    # The currency we want to convert to
    TARGET_CCY = Currencies["USD"]

    ##
    # The as of date we want to convert
    TARGET_ASOF = Temporal.today()

    ##
    # An FX rate service with fixed FX rates
    class Service(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("1.23"))


# Generated at 2022-06-14 04:42:01.103412
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:42:10.595295
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    Tests method *queries* of class *FXRateService*.
    """
    # We know where this is going:
    import unittest
    import unittest.mock

    # Setup a mock service
    class MockService(FXRateService):
        """
        Provides a mock foreign exchange rate service.
        """

        def __init__(self):
            ## Set the queries:
            self.queries = []

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            """
            Collects the query for future inspection.
            """
            self.queries.append((ccy1, ccy2, asof))
            return None


# Generated at 2022-06-14 04:42:22.959053
# Unit test for method query of class FXRateService

# Generated at 2022-06-14 04:42:31.770431
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    import datetime
    from decimal import Decimal
    from pypara.currencies import Currencies
    from pypara.finance.fx import FXRateService

    class TestFXRateService(FXRateService):

        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            rate = FXRate(ccy1, ccy2, asof, Decimal(2))
            return rate

        def queries(self, queries: Iterable[TQuery], strict: bool = False) -> Iterable[Optional[FXRate]]:
            return [self.query(ccy1, ccy2, asof) for (ccy1, ccy2, asof) in queries]

    date = datetime.date.today()
    fxr1 = TestFX

# Generated at 2022-06-14 04:42:42.655396
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Tests method query of class FXRateService.
    """
    import pytest
    from decimal import Decimal
    from pypara.currencies import Currencies
    class _TestFXRateService(FXRateService):
        def query(self, ccy1: Currency, ccy2: Currency, asof: Date, strict: bool = False) -> Optional[FXRate]:
            return FXRate(ccy1, ccy2, asof, Decimal("2"))

    ## Invertibility:
    rate = _TestFXRateService().query(Currencies["EUR"], Currencies["USD"], Date.today())
    assert rate and FXRate(Currencies["USD"], Currencies["EUR"], Date.today(), Decimal("0.5")) == ~rate

    ## Lookup error:

# Generated at 2022-06-14 04:42:52.496450
# Unit test for method queries of class FXRateService
def test_FXRateService_queries(): 
    from datetime import date
    from pypara.currencies import Currencies
    from .commons.numbers import ONE
    from .currencies import Currency

    class TestFXRateService(FXRateService): 
        def __init__(self, rates: Iterable[FXRate]): 
            self._rates = rates

        def query(self, ccy1: Currency, ccy2: Currency, asof: date, strict: bool = False): 
            for rate in self._rates: 
                if rate.ccy1 == ccy1 and rate.ccy2 == ccy2 and rate.date == asof: 
                    return rate
            return None

        def queries(self, queries: Iterable[TQuery], strict: bool = False):
            results = []

# Generated at 2022-06-14 04:42:55.332586
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    from decimal import Decimal
    # TODO: Add unit tests
    pass


# Generated at 2022-06-14 04:42:56.458817
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    pass


# Generated at 2022-06-14 04:42:58.822106
# Unit test for method queries of class FXRateService
def test_FXRateService_queries():
    """
    TODO: Fill in [pypara.fx.FXRateService.queries]
    """

    pass

# Generated at 2022-06-14 04:44:20.917893
# Unit test for method query of class FXRateService
def test_FXRateService_query():
    """
    Unit test for the query method of the FXRateService class.
    """
    from unittest import TestCase, mock
    from .currencies import Currencies
    from .commons.zeitgeist import Date

    # Mock an FX rate service
    with mock.patch.object(FXRateService, "query") as mock_query:
        mock_query.return_value = None
        svc = FXRateService()
        assert svc.query(Currencies["EUR"], Currencies["USD"], Date.today()) == None
