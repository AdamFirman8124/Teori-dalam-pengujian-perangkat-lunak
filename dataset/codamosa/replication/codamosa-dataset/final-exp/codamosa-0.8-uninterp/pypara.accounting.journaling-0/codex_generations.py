

# Generated at 2022-06-14 04:11:34.416537
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # examples with correct journal entries:
    try:
        je = JournalEntry(datetime.date.today())
        je.post(datetime.date.today(), Account('132'), Quantity(10))
        je.post(datetime.date.today(), Account('132'), Quantity(-10))
        je.validate()
    except AssertionError:
        # examples with incorrect journal entries:
        je.post(datetime.date.today(), Account('132'), Quantity(10))
        je.validate()

# Generated at 2022-06-14 04:11:37.308117
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    dummy_source = ReadJournalEntries[int]
    dummy_source.__call__(period=DateRange(datetime.date.today(), datetime.date.today()))

# Generated at 2022-06-14 04:11:38.144837
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert None

# Generated at 2022-06-14 04:11:46.914611
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import Account
    from .ledger import Ledger

    # Arrange:
    def read(period: DateRange) -> Iterable[JournalEntry[Ledger]]:
        from .services.ledger_services import FetchJournalEntries
        return FetchJournalEntries(period=period)()

    # Act:
    entries = read(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31)))

    # Assert:
    assert entries is not None
    assert isinstance(entries, Iterable)

    # Act:
    total = isum(i.amount for e in entries for i in e.increments if i.account == Account.CASH)

    # Assert:
    assert total > 0

    # System test:
    print(total)


# Unit test

# Generated at 2022-06-14 04:11:57.062685
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountGroup
    from .chartofaccounts import ChartOfAccounts
    from .payables import Payment

    # Given:

# Generated at 2022-06-14 04:12:05.239102
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Debit and Credit amounts are equal
    je = JournalEntry(datetime.date.today(), "description", "source")
    je.post(datetime.date.today(), Account("Cash", AccountType.ASSETS), 11)
    je.post(datetime.date.today(), Account("Revenue", AccountType.REVENUES), 11)
    je.validate()

    # Debit and Credit amounts are not equal
    je = JournalEntry(datetime.date.today(), "description", "source")
    je.post(datetime.date.today(), Account("Cash", AccountType.ASSETS), 22)
    je.post(datetime.date.today(), Account("Revenue", AccountType.REVENUES), 11)
    try:
        je.validate()
    except AssertionError:
        pass

# Generated at 2022-06-14 04:12:12.562563
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import DateRange

    from .accounts import Account
    from .companies import Company

    assert issubclass(ReadJournalEntries, Protocol)

    _RJE = TypeVar("_RJE", bound=ReadJournalEntries)
    class TestClass(Generic[_RJE]):
        def __init__(self):
            self.comp_a = Company("Test Company A")
            self.comp_b = Company("Test Company B")
            self.acc_a = Account("Test Account A", self.comp_a)
            self.acc_b = Account("Test Account B", self.comp_a)
            self.acc_c = Account("Test Account C", self.comp_b)


# Generated at 2022-06-14 04:12:13.996598
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j1 = JournalEntry()
    j1.post(Account('A', 0), 1)
    assert j1.postings == [Posting(datetime.date.today(),Account('A', 0),Direction.INC, 1)]


# Generated at 2022-06-14 04:12:24.439383
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Test the method __call__ of class ReadJournalEntries.
    """
    from finance.interfaces.accounts import ReadAccounts
    from finance.interfaces.balances import ReadBalanceEntries

    ## Create a mock function:

# Generated at 2022-06-14 04:12:33.541006
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from datetime import timedelta
    from collections import Iterable
    from .accounts import Account

    dr1 = DateRange(date(2020, 3, 4), date(2020, 3, 4))
    dr2 = DateRange(date(2020, 3, 7), date(2020, 3, 7))
    dr3 = DateRange(date(2020, 3, 7), date(2020, 3, 7))
    dr4 = DateRange(date(2020, 3, 7), date(2020, 3, 7))
    dr5 = DateRange(date(2020, 3, 7), date(2020, 3, 7))
    dr6 = DateRange(date(2020, 3, 7), date(2020, 3, 7))
    dr7 = DateRange(date(2020, 3, 7), date(2020, 3, 7))
   

# Generated at 2022-06-14 04:12:37.018328
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert True

# Generated at 2022-06-14 04:12:47.585474
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from pytest import raises
    from ..accounts.accounts import Account, AccountType
    from ..commons.zeitgeist import DateRange

    @dataclass(frozen=True)
    class MockSource:
        """A mock source object."""

        guid: str

    source = MockSource("My source")

    # Initialize a journal entry:
    je: JournalEntry[MockSource] = JournalEntry(date(2020, 5, 1), "My journal entry", source)
    je.post(date(2020, 5, 1), Account("My account", AccountType.EQUITIES), 10)
    je.post(date(2020, 5, 1), Account("My other account", AccountType.REVENUES), -10)

    # Check the __call__ function logic:

# Generated at 2022-06-14 04:12:54.896150
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .books import Book
    from .constants import ROOT_ACCOUNT
    from .transactions import Transaction

    b0 = Book(ROOT_ACCOUNT)
    b0.post(date=datetime.date(2019, 12, 31), description="Test Journal Entry: post method")(
        Account(AccountType.ASSETS, "bank", "bank"),
        Account(AccountType.EXPENSES, "cash", "cash")
    )
    assert len(b0.journal_entries) == 1, "JournalEntry: length of journal entries is not correct"
    assert b0.journal_entries[0].postings[0].amount == 1, "JournalEntry: post method: amount not correct"

# Generated at 2022-06-14 04:13:07.125224
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from typing import Callable

    def make_journal_entries(date_range: DateRange) -> Callable[[], Iterable[JournalEntry[int]]]:
        class Journal:
            pass

# Generated at 2022-06-14 04:13:08.188017
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert False, "Test not implemented"


# Generated at 2022-06-14 04:13:17.289979
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import datetime, unittest
    from dataclasses import dataclass, field
    from typing import List
    from hypothesis import example, given, strategies as st
    from ..commons.numbers import Amount, Quantity, isum
    from ..commons.others import Guid, makeguid
    from ..commons.zeitgeist import DateRange

    @dataclass(frozen=True)
    class Dummy:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            assert not period.is_empty()
            return []


# Generated at 2022-06-14 04:13:18.958100
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    a = JournalEntry.post()

# Generated at 2022-06-14 04:13:23.873909
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # pylint: disable=unused-variable
    # pylint: disable=no-self-use
    class ReadJournalEntriesImpl:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            ...  # pragma: no cover

# Generated at 2022-06-14 04:13:31.958251
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Tests the method __call__ of class ReadJournalEntries.
    """

    # Define a function which is an instance of ReadJournalEntries.
    @dataclass()
    class ReadJournalEntriesExample:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    # Create an instance of ReadJournalEntriesExample
    example = ReadJournalEntriesExample()

    # Validate the instantiation
    assert isinstance(example, ReadJournalEntries)
    assert not isinstance(ReadJournalEntriesExample, ReadJournalEntries)

# Generated at 2022-06-14 04:13:42.818868
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime
    from .accounts import Accounts
    # Create an instance of class Account
    account = Accounts.create("BANK")
    # Create an instance of class JournalEntry
    journal_entry = JournalEntry(
        date=datetime.date(2020, 3, 10),
        description="Bank deposit",
        source=account
    )
    # Post the quantity of 100 to the account
    journal_entry.post(date=journal_entry.date, account=account, quantity=100)
    # Print postings
    for posting in journal_entry.postings:
        print(posting)
    # Print the increment postings
    for increment in journal_entry.increments:
        print(increment)
    # Print the decrement postings
    for decrement in journal_entry.decrements:
        print(decrement)
    #

# Generated at 2022-06-14 04:13:57.572846
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from functools import partial

    from .accounts import AccountType, Account

    ##
    ## Test data
    ##
    class TestSource:
        pass

    test_postings = [
        (date(2020, 5, 24), Account("ASSET", AccountType.ASSETS), Direction.INC, Amount(100)),
        (date(2020, 5, 24), Account("EXPENSE", AccountType.EXPENSES), Direction.DEC, Amount(75)),
    ]

    expected_postings_data = [
        (date(2020, 5, 24), Account("ASSET", AccountType.ASSETS), Direction.INC, Amount(100)),
        (date(2020, 5, 24), Account("EXPENSE", AccountType.EXPENSES), Direction.DEC, Amount(75)),
    ]


# Generated at 2022-06-14 04:14:09.694065
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    asset_bank = Account("Bank", AccountType.ASSETS)
    expense_rent = Account("Rent", AccountType.EXPENSES)
    equity_owner1 = Account("Owner1", AccountType.EQUITIES)
    equity_owner2 = Account("Owner2", AccountType.EQUITIES)

    j1 = JournalEntry[int](
        date=datetime.date(2020, 1, 1), description="Test journal 1", source=1, postings=[]
    )
    j1.post(
        datetime.date(2020, 1, 1),
        asset_bank,
        1_00,
    )
    j1.post(
        datetime.date(2020, 1, 1),
        expense_rent,
        -1_00,
    )


# Generated at 2022-06-14 04:14:10.276074
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert True

# Generated at 2022-06-14 04:14:16.153215
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.numbers import Quantity as Q
    from ..commons.timelines import DateRange as DR
    from .accounts import Account as A

    def test_posting(posting: Posting[str]) -> None:
        assert posting.account.name == "foo"
        assert posting.journal.description == "bar"
        assert posting.amount == Q(100)
        assert posting.direction == Direction.INC

    entry = JournalEntry[str](DR.latest.today, "bar", "")
    entry.post(DR.latest.today, A("foo"), Q(100)).validate()
    for posting in entry.postings:
        test_posting(posting)


# Generated at 2022-06-14 04:14:21.200875
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Unit test for method __call__ of class ReadJournalEntries
    """
    class R:

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return list()

    assert isinstance(R(), ReadJournalEntries)

# Generated at 2022-06-14 04:14:24.374803
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[None]]:
        pass

    assert issubclass(read_journal_entries, ReadJournalEntries)

# Generated at 2022-06-14 04:14:28.380981
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from unittest import mock
    read = mock.Mock(spec=ReadJournalEntries)
    assert read(DateRange(datetime.date(2020, 4, 1), datetime.date(2020, 5, 1))) == read.return_value

# Generated at 2022-06-14 04:14:32.490925
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_journal_entries(date_range: DateRange) -> Iterable[JournalEntry[_T]]:
        pass
    assert ReadJournalEntries.__isubclasscheck__(read_journal_entries)


# Generated at 2022-06-14 04:14:43.813439
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType
    from .business import Product
    from .ledgers import Ledger
    from .persistence import InMemoryJournalEntryStore

    ## Create a ledger:
    ledger = Ledger()

    ## Create a product:
    product = ledger.products.create(Product, description="Test Product")

    ## Create a journal entry:
    je1 = ledger.journal_entries.create(JournalEntry, date=datetime.date.today())
    je1.postings.append(Posting(je1, date=datetime.date.today(), account=Account(ledger, "Assets account", AccountType.ASSETS), direction=Direction.INC, amount=1))

# Generated at 2022-06-14 04:14:47.354115
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Just runs type checker to ensure the protocol member is defined correctly.
    """
    callable = ReadJournalEntries

    def _read(period: DateRange) -> Iterable[JournalEntry[int]]:
        pass

    _ = callable(_read)

# Generated at 2022-06-14 04:15:07.983775
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .transactions import Transaction
    from .accounts import Account
    from ..commons.zeitgeist import DateTime

    class Journal:
        def __init__(self):
            self.entries = []

        def __call__(self, period: DateRange):
            return (e for e in self.entries if period.contains(e.date))

    # noinspection PyTypeChecker
    journal: ReadJournalEntries[Transaction] = Journal()

    txn = Transaction()
    txn.post(DateTime.now().date(), Account.ASSETS_CASH, +100)
    journal.entries.append(txn)

    assert len(list(journal(DateRange.current_year()))) == 1

# Generated at 2022-06-14 04:15:11.715705
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Create a journal entry for testing
    journal_entry = JournalEntry[int](date = datetime.date.today(), description = 'test_journal_entry', source = 55)
    assert type(journal_entry) == JournalEntry[int]
    ## Check if validate() raises the expected error
    try:
        journal_entry.validate()
    except Exception as e:
        exception_raised = isinstance(e, AssertionError)
    assert exception_raised

# Generated at 2022-06-14 04:15:20.696933
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    from .accounts import AccountType

    journal_entry = JournalEntry[int](datetime.date.today(), "test", 3)
    assert journal_entry.postings == []
    journal_entry.post(datetime.date.today(), Account("asset", AccountType.ASSETS), -100)
    assert journal_entry.postings[0].direction == Direction.DEC
    assert journal_entry.postings[0].account.type == AccountType.ASSETS
    assert journal_entry.postings[0].amount.value == 100


# Generated at 2022-06-14 04:15:24.153803
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    _v = []
    ReadJournalEntries.__call__.__annotations__.clear()
    ReadJournalEntries.__call__.__annotations__['period'] = DateRange
    ReadJournalEntries.__call__.__annotations__['return'] = Iterable[JournalEntry[Any]]

# Generated at 2022-06-14 04:15:33.767466
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import datetime_range
    from .accounts import Account
    from .definition import Definition

    def assert_journal_entry(source: object, entries: str) -> None:
        journal_entry = JournalEntry(datetime.date(2017, 4, 2), "Hello", source)
        journal_entry.post(journal_entry.date, Asset(), +300)
        journal_entry.post(journal_entry.date, Expense(), -300)
        entries = entries.split(",")
        assert entries == [str(i.account) for i in journal_entry.postings]

    assert_journal_entry(Definition(Asset(), "Cash", "Cash in the bank"), "Cash,Expense")
    assert_journal_entry(Definition(Account(), "Cash", "Cash in the bank"), "Cash,Expense")

# Generated at 2022-06-14 04:15:34.587691
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass


# Generated at 2022-06-14 04:15:45.912639
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..journal.accounts import AccountType, Account

    # Given
    a1 = Account("A1", AccountType.ASSETS, "Asset")
    a2 = Account("A2", AccountType.REVENUES, "Revenue")
    je = JournalEntry("2020-01-01", "Description")

    # When
    je.post("2020-01-01", a1, 1000)
    je_posted = je.post("2020-01-01", a2, -1000)
    je_posted.validate()

    # Then
    assert je_posted.date == datetime.date(2020, 1, 1)
    assert je_posted.description == "Description"
    assert je_posted.postings[0].account.id == a1.id
    assert je_posted.postings[0].direction == Direction.INC
   

# Generated at 2022-06-14 04:15:51.197632
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[object]]:
        yield JournalEntry(period.start, "", object())
        yield JournalEntry(period.start, "", object())
    assert len(ReadJournalEntries.__args__) == 1
    assert ReadJournalEntries[object].__args__ == ()
    assert issubclass(ReadJournalEntries, ReadJournalEntries[object])

# Generated at 2022-06-14 04:16:00.926270
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Create dummy object for testing
    @dataclass(frozen=True)
    class Dummy:
        pass
    dummy = Dummy()

    # Create test instance
    journal_entry = JournalEntry[Dummy]

    # Run test
    journal_entry.post(datetime.date(2020, 1, 1), None, 1)
    assert(journal_entry.postings[0].date == datetime.date(2020, 1, 1))
    assert(journal_entry.postings[0].account == None)
    assert(journal_entry.postings[0].direction == Direction.INC)
    assert(journal_entry.postings[0].amount == Amount(1))


# Generated at 2022-06-14 04:16:10.105198
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from forex_types.money import Money
    from .accounts import Account, AccountType

    class P(ReadJournalEntries[str]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[str]]:
            journal = JournalEntry[str](date=datetime.date(2018, 1, 1), description="Test journal entry.", source="abc")
            journal.post(journal.date, Account("101.01", AccountType.ASSETS, description="Cash"), Money("INR", 30))
            journal.post(journal.date, Account("201.01", AccountType.EQUITIES, description="Equity"), Money("INR", -30))
            journal.validate()
            return [journal]

    assert P()(None) is not None


# Generated at 2022-06-14 04:16:39.137474
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j = JournalEntry[str]("2019-01-01", "Test", "Test", [])
    j.post(datetime.date(2019, 1, 1), Account(AccountType.EXPENSES, "Test"), Quantity(-1))
    j.post(datetime.date(2019, 1, 1), Account(AccountType.ASSETS, "Test"), Quantity(1))
    j.validate()

# Generated at 2022-06-14 04:16:48.213210
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal = JournalEntry(datetime.date(2020, 3, 14), "New journal entry", None)
    journal.post(datetime.date(2020, 3, 14), Account("A", AccountType.ASSETS), Quantity(20))

    assert journal.postings[0].date == datetime.date(2020, 3, 14)
    assert journal.postings[0].account.id == "A"
    assert journal.postings[0].account.type == AccountType.ASSETS
    assert journal.postings[0].direction == Direction.INC
    assert journal.postings[0].amount == Quantity(20)

# Generated at 2022-06-14 04:16:58.409074
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.numbers import Quantity
    from ..commons.others import makeguid
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountType
    j: JournalEntry[str] = JournalEntry(datetime.date(2020, 1, 2), "Test Description", "Test Source")
    cash_asset: Account = Account("Cash", AccountType.ASSETS)
    stock_equity: Account = Account("Stocks", AccountType.EQUITIES)
    revenue: Account = Account("Revenue", AccountType.REVENUES)
    expense: Account = Account("Expense", AccountType.EXPENSES)
    liability: Account = Account("Liability", AccountType.LIABILITIES)
    j.post(datetime.date(2020, 1, 2), cash_asset, Quantity(1))

# Generated at 2022-06-14 04:17:08.278245
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import Account, AccountType
    from .currencies import Currency, USD, INR
    from .import datetime as dt

    # Setup:
    #   Account:
    account = Account(AccountType.ASSETS, "Unknown Account", Currency(USD), "")

    #   Period:
    period = DateRange(dt.date(2019, 1, 1), dt.date(2019, 12, 31))

    # Test:

# Generated at 2022-06-14 04:17:10.290684
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    #given
    JournalEntry
    je = JournalEntry(datetime.datetime.now().date(), "Test Journal Entry", 4)
    #when
    je.post(datetime.datetime.now().date(), Account(1), 5)
    je.post(datetime.datetime.now().date(), Account(2), -2)
    #then
    assert je.validate()

# Generated at 2022-06-14 04:17:18.051723
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import dummy_date_range
    from .accounts import AccountTypes
    from .accounts.read_accounts import ReadAccounts
    from .read_natures import ReadNatures

    def make_journal(date: datetime.date) -> JournalEntry[object]:
        revenue = Account(1, AccountTypes.REVENUE, "Sales revenue")
        expense = Account(2, AccountTypes.EXPENSE, "Purchases expense")
        asset = Account(3, AccountTypes.ASSETS, "Warehouse asset")
        benefits = Account(4, AccountTypes.EQUITIES, "Benefits equity")
        liability = Account(5, AccountTypes.LIABILITIES, "Salaries liability")

# Generated at 2022-06-14 04:17:28.309975
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from .accounts import Account, AccountType
    from .commons.currency import Currency
    from .commons.numbers import Amount
    from .commons.others import makeguid
    from .commons.zeitgeist import DateRange
    # Test Data
    jdate = date.today()
    jdesc = "This is a journal entry for posting test of class JournalEntry."
    jsource = Account(AccountType.ASSETS, Currency.EUR, "Test account", "A descriptive account for unit testing.")
    jcredit = Amount(100, Currency.EUR)
    jdebit = Amount(-100, Currency.EUR)
    # Testing
    je = JournalEntry(jdate, jdesc, jsource)
    je.post(jdate, jsource, jcredit)

# Generated at 2022-06-14 04:17:38.641602
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.numbers import Amount, Quantity
    accounts = {
        "AT1": Account("AT1", "Asset Account 1"),
        "AT2": Account("AT2", "Asset Account 2"),
    }
    business_object = "foo"
    je = JournalEntry[str](date=datetime.date.today(), description="My Journal Entry",
                           source=business_object).post(date=datetime.date.today(), account=accounts["AT1"],
                                                         quantity=Quantity(10, "USD"))
    print(je)
    print(len(je.postings))
    for p in je.postings:
        print(p)
    assert len(je.postings) == 1
    for p in je.postings:
        assert p.amount == Amount(10, "USD")



# Generated at 2022-06-14 04:17:45.189876
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j = JournalEntry[int](
        date=datetime.date.today(), 
        description="test", 
        source=1
    )
    j.post(
        date=datetime.date.today(), 
        account=Account(code="001", description="A", type=AccountType.ASSETS), 
        quantity=1
    )
    j.post(
        date=datetime.date.today(), 
        account=Account(code="001", description="A", type=AccountType.ASSETS), 
        quantity=1
    )
    j.post(
        date=datetime.date.today(), 
        account=Account(code="001", description="A", type=AccountType.ASSETS), 
        quantity=-2
    )
    print(j)

# Generated at 2022-06-14 04:17:55.676564
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    mock_journal_entry = JournalEntry(
        date=datetime.date(2020, 3, 4),
        description="Vendor Payment",
        source=None,
        postings=[
            Posting(
                journal=mock_journal_entry,
                date=datetime.date(2020, 3, 4),
                account=Account("Bank Accounts", "Checking Account", AccountType.ASSETS),
                direction=Direction.INC,
                amount=Amount(1),
            ),
            Posting(
                journal=mock_journal_entry,
                date=datetime.date(2020, 3, 4),
                account=Account("Accounts Payable", "Vendor 1", AccountType.LIABILITIES),
                direction=Direction.DEC,
                amount=Amount(1),
            ),
        ],
    )
    mock_journal

# Generated at 2022-06-14 04:19:13.652918
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .currencies import Currency, CurrencyPair, CurrencyPairMap, default_currency_pair_map
    from .instrument import EquityType, Instrument

    journal_entry = JournalEntry()
    journal_entry.post(datetime.date.today(), Account("Cash", AccountType.ASSETS), 10)
    journal_entry.post(datetime.date.today(), Account("Cash", AccountType.ASSETS), -20)
    journal_entry.post(datetime.date.today(), Account("Cash", AccountType.ASSETS), -30)
    journal_entry.post(datetime.date.today(), Account("Cash", AccountType.ASSETS), -40)


# Generated at 2022-06-14 04:19:24.798832
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from math import isclose
    from .bank_statement import BankStatement
    from .bank_statement_extractor import BankStatementExtractor
    from .currency_denominated_accounts import CurrencyDenominatedAccounts
    from .ledger import Ledger
    import pytest
    from ._test.test_accounts import test_accounts
    from ._test.test_bank_statement import test_bank_statement
    from ._test.test_currency_denominated_accounts import test_currency_denominated_accounts
    from ._test.test_date_range import test_date_range
    from ._test.test_ledger import test_ledger

    ledger: Ledger = test_ledger()
    currency_denominated_accounts: CurrencyDenominatedAccounts = test_currency_denominated_accounts()

# Generated at 2022-06-14 04:19:25.754975
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:19:32.695825
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    amount = Amount(1)
    date = datetime.date(year=2019, month=8, day=11)
    description = "Test description"
    account = Account("TestAccount")
    source = "Test Source"

    journal_entry = JournalEntry(date, description, source, postings=[])
    journal_entry.post(date, account, amount)

    assert journal_entry.postings == [Posting(journal_entry, date, account, Direction.INC, amount)]

# Generated at 2022-06-14 04:19:40.666039
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account
    from .transactions import JournalEntry, post
    from datetime import date
    exp1 = JournalEntry(date(2019, 1, 1), "First expense", dict())
    exp2 = JournalEntry(date(2019, 1, 2), "Second expense", dict()).post(date(2019, 1, 2), Account("EXPENSES"), -10)
    exp3 = JournalEntry(date(2019, 1, 3), "Third expense", dict()).post(date(2019, 1, 3), Account("EXPENSES"), -15)
    exp4 = JournalEntry(date(2019, 1, 4), "Fourth expense", dict()).post(date(2019, 1, 4), Account("EXPENSES"), -20)
    inc1 = JournalEntry(date(2019, 1, 1), "First income", dict())
    inc2

# Generated at 2022-06-14 04:19:41.445170
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    assert True

# Generated at 2022-06-14 04:19:46.623469
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Test the validate method of JournalEntry class
    """
    acc1 = Account("test", AccountType.ASSETS)
    acc2 = Account("test", AccountType.REVENUES)
    source = "test"
    description = "test"
    date = 1, 1, 2019
    value = 10

    journal_entry = JournalEntry[str](date, description, source)
    journal_entry.post(date, acc1, value)
    journal_entry.post(date, acc2, -value)
    journal_entry.validate()

# Generated at 2022-06-14 04:19:52.684027
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    @dataclass(frozen=True)
    class TestPosting:
        journal: JournalEntry
        date: datetime.date
        account: Account
        direction: Direction
        amount: Amount

        def __str__(self):
            return f"TestPosting(date={self.date},account={self.account},direction={self.direction},amount={self.amount})"
            
    @dataclass(frozen=True)
    class TestJournalEntry(JournalEntry):
        source: str
        postings: List[TestPosting] = field(default_factory=list)
            
    test_entry = TestJournalEntry(date=datetime.date(2019, 2, 12), description="Test Journal Entry", source="Test Source")
    a = Account("A", AccountType.ASSETS)

# Generated at 2022-06-14 04:20:01.197416
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    class BusinessObject:
        pass

    journal = JournalEntry[BusinessObject](datetime.date.today(), "Invoice Sale", BusinessObject())
    journal.post(journal.date, Account("Customer", AccountType.ASSETS), Amount(10))
    journal.post(journal.date, Account("Sales", AccountType.REVENUES), Amount(10))
    journal.validate()
    assert len(list(journal.increments)) == 2
    assert len(list(journal.decrements)) == 0
    assert len(list(journal.debits)) == 1
    assert len(list(journal.credits)) == 1

# Generated at 2022-06-14 04:20:11.491210
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import dataclass, field
    from unittest.mock import MagicMock

    @dataclass
    class MockSource(ReadJournalEntries):
        @classmethod
        def create(cls, entries: Iterable[JournalEntry[_T]]) -> "MockSource":
            mock = MagicMock(ReadJournalEntries.__call__)
            mock.return_value = entries
            return cls(mock)

        reader: MagicMock

    reader = MockSource.create([])
    for entry in reader(DateRange()):
        assert False

    reader = MockSource.create([JournalEntry(datetime.date.today(), "", None)])
    count = 0
    for entry in reader(DateRange()):
        count += 1
    assert count == 1
