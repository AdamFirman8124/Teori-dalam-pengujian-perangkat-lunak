

# Generated at 2022-06-14 04:11:23.356504
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Set up
    from .books import Book

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[Book]]:
        return []

    # Exercise
    read_journal_entries(period=DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 31)))

# Generated at 2022-06-14 04:11:29.071318
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from giotto.controllers import command
    @command
    class OpenBankAccount:
        pass
    jo = JournalEntry(date=datetime.date(2019, 10, 1), description="Open Bank Account", source=OpenBankAccount())
    jo.post(date=jo.date, account=Account("1100", AccountType.ASSETS), quantity=1000)
    assert len(jo.postings) == 1

# Generated at 2022-06-14 04:11:31.853341
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Can not create a JournalEntry object, because it is an abstract class
    # Method validate of class JournalEntry seems to not have been defined.
    pass


# Generated at 2022-06-14 04:11:32.707221
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass

# Generated at 2022-06-14 04:11:43.239527
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # pylint: disable=too-many-locals
    """ Test `validate` method of `JournalEntry` class. """
    # Define test cases:

# Generated at 2022-06-14 04:11:49.998116
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Test: Increment
    je = JournalEntry(
        datetime.date(2019, 1, 1), "Test", None, []).post(
        datetime.date(2019, 2, 1), Account.of("Revenue", "Advertising"), 1)
    assert je
    assert je.postings[0].date == datetime.date(2019, 2, 1)
    assert je.postings[0].account.full_name == "Revenue:Advertising"
    assert je.postings[0].direction == Direction.INC
    assert je.postings[0].amount.value == 1
    
    assert len(je.postings) == 1
    # Test: Decrement

# Generated at 2022-06-14 04:11:54.618593
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import datetime
    from pigit.accounts import AccountType
    from pigit.accounts import AccountKey
    from pigit.accounts import Account
    from pigit.journal import Direction
    from pigit.journal import Posting
    
    @dataclass(frozen=True)
    class Transaction:
        #: Date of transaction.
        date: datetime.date
        #: Transaction code.
        code: int
        #: Transaction name
        name: str
        #: Source account.
        source: Account
        #: Destination account.
        destination: Account
        #: Transaction amount.
        amount: Amount
        #: Globally unique, ephemeral identifier.
        guid: Guid = field(default_factory=makeguid, init=False)
    

# Generated at 2022-06-14 04:12:00.301891
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from datetime import timedelta

    # https://stackoverflow.com/questions/28238531/generate-a-range-of-dates-in-python
    def date_range(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    class Source:
        pass

    class JournalEntryImpl(JournalEntry[Source]):
        pass

    class PostingImpl(Posting[Source]):
        pass

    source = Source()

# Generated at 2022-06-14 04:12:07.177020
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Arrange
    je = JournalEntry[str]()
    a1 = Account()
    a2 = Account()
    a3 = Account()
    a4 = Account()
    # Act
    je.post(datetime.date(2018, 1, 1), a1, 100)
    je.post(datetime.date(2018, 1, 1), a2, 200)
    je.post(datetime.date(2018, 1, 1), a3, 300)
    je.post(datetime.date(2018, 1, 1), a4, -600)
    # Assert

# Generated at 2022-06-14 04:12:13.440896
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from ..accounting.accounts import AccountType
    from ..accounting.accounts import Account
    from ..accounting.accounts import Name
    from ..accounting.accounts import Number
    from ..accounting.values import Amount
    from ..accounting.numbers import Quantity

    date_today = date.today()
    date_yesterday = date.today() - datetime.timedelta(days=1)
    date_tomorrow = date.today() + datetime.timedelta(days=1)
    # test journal entry

    def test_journal_entry(desc, journal_date, post_date, account, quantity, is_debit, is_credit):
        journal = JournalEntry(journal_date, desc, None)
        post = journal.post(post_date, account, quantity)
       

# Generated at 2022-06-14 04:12:20.908992
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.types import Function
    assert issubclass(Function[DateRange, Iterable[JournalEntry[_T]]], ReadJournalEntries)

# Generated at 2022-06-14 04:12:30.773133
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    account1 = Account("1", "account1", AccountType.ASSETS)
    account2 = Account("2", "account2", AccountType.REVENUES)
    post1: Posting = JournalEntry(datetime.date.today(), "Posting 1", None).post(datetime.date.today(), account1, 1000).postings[0]
    post2: Posting = JournalEntry(datetime.date.today(), "Posting 1", None).post(datetime.date.today(), account1, -1000).postings[0]
    post3: Posting = JournalEntry(datetime.date.today(), "Posting 1", None).post(datetime.date.today(), account2, 1000).postings[0]

# Generated at 2022-06-14 04:12:37.285551
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Tests method validate of class JournalEntry
    """
    # Set date
    date = datetime.date.today()
    # Create journal entry
    entry = JournalEntry(date, 'description', 'source')
    # Create assets account
    assets = Account('Assets', AccountType.ASSETS)
    # Create liabilities account
    liabilities = Account('Liabilities', AccountType.LIABILITIES)
    # Create revenues account
    revenues = Account('Revenues', AccountType.REVENUES)
    # Create expenses account
    expenses = Account('Expenses', AccountType.EXPENSES)
    # Create equities account
    equities = Account('Equities', AccountType.EQUITIES)
    entry.post(date, assets, -100)
    entry.post(date, revenues, +100)
    entry.validate() # should not

# Generated at 2022-06-14 04:12:47.748286
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    journal1 = JournalEntry[str](datetime.date(2020, 4, 12), "test", "test", [])
    journal1.validate()

    journal2 = JournalEntry[str](datetime.date(2020, 4, 12), "test", "test", [])
    journal2.post(datetime.date(2020, 4, 12), Account("revenue", AccountType.REVENUES), Quantity(10))
    journal2.post(datetime.date(2020, 4, 12), Account("expense", AccountType.EXPENSES), Quantity(-10))
    journal2.validate()

    journal3 = JournalEntry[str](datetime.date(2020, 4, 12), "test", "test", [])

# Generated at 2022-06-14 04:12:56.049907
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .journal import JournalEntry, Posting
    je = JournalEntry("1", "2", 3)
    Day = datetime.date
    a1 = Account("a1", AccountType.ASSETS, 4)
    a2 = Account("a2", AccountType.EQUITIES, 4)
    a3 = Account("a3", AccountType.REVENUES, 4)
    je.post(Day(2020,1,1), a1, 5)
    je.post(Day(2020,1,2), a2, 6)
    je.post(Day(2020,1,3), a3, 7)
    je.post(Day(2020,1,4), a3, 0)
    assert len(je.postings) == 3

# Generated at 2022-06-14 04:13:07.734428
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Setup:
    from .accounts import Account
    from .readjournalentries import read_journal_entries
    from .testutils import JournalEntryBuilder
    from .testutils import MockAccounts
    from .testutils import mock_perihelion

    period = mock_perihelion()
    account_a = MockAccounts(name="A")
    account_b = MockAccounts(name="B")
    account_c = MockAccounts(name="C")
    journal_a = JournalEntryBuilder(date=period.start)
    journal_b = JournalEntryBuilder(date=period.start)
    journal_c = JournalEntryBuilder(date=period.end)
    journal_a.post(account_a, +1).post(account_b, -1)

# Generated at 2022-06-14 04:13:17.060990
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..charts import Account as ChartAccount

    Account.charts.__setitem__(ChartAccount(name="Oakeshott"),[])
    Account.charts.__setitem__(ChartAccount(name="Family"),[])
    Account.charts.__setitem__(ChartAccount(name="Salary"),[])
    Account.charts.__setitem__(ChartAccount(name="Bank"),[])
    Account.charts.__setitem__(ChartAccount(name="Liabilities"),[])
    Account.charts.__setitem__(ChartAccount(name="Expenses"),[])
    Account.charts.__setitem__(ChartAccount(name="Legal"),[])
    Account.charts.__setitem__(ChartAccount(name="Services"),[])

# Generated at 2022-06-14 04:13:28.515763
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from unittest import TestCase

    @dataclass
    class Ob(Generic[_T]):
        def __init__(self, o: _T, p: DateRange):
            self.o = o
            self.p = p

    res = list(ReadJournalEntries[Ob]({date(2020, 1, 1), date(2020, 1, 2)}).map(lambda e: e.o))
    TestCase().assertListEqual(res, [Ob(1, {date(2020, 1, 1), date(2020, 1, 2)}), Ob(2, {date(2020, 1, 1), date(2020, 1, 2)})])

# Generated at 2022-06-14 04:13:36.834157
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Since ReadJournalEntries is a protocol, we use Protocol.__call__ as its implementation.

    # A sample journal entry.
    _date = datetime.date(2020, 4, 1)
    _source = "dummy"
    _journal = JournalEntry[str](
        date=_date,
        description="Dummy Journal Entry",
        source=_source,
    ).post(date=_date, account="Assets:Bank:Current Account", quantity=10)

    # Test with 3 different callables.
    def _callable0(period: DateRange) -> Iterable[JournalEntry[str]]:
        return []  # type: ignore

    def _callable1(period: DateRange) -> Iterable[JournalEntry[str]]:
        yield _journal  # type: ignore


# Generated at 2022-06-14 04:13:43.038287
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType
    from .commons.zeitgeist import now

    account1 = Account(AccountType.ASSETS, "Cash")
    account2 = Account(AccountType.REVENUES, "Revenue")

    # Create a journal entry
    j = JournalEntry[str](now.today(), "Test", "Tester")
    assert not j.postings

    # Post some entries
    j.post(now.today(), account1, Quantity(10))
    j.post(now.today(), account2, Quantity(-10))
    assert len(j.postings)

    # Check
    j.validate()

# Generated at 2022-06-14 04:13:59.482065
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType, ReadAccounts
    from .commons.system import System

    # Setup
    system = System.make_test_env()
    accounts: ReadAccounts = system.services.accounts
    journals = system.services.journal_entries

    sal1 = JournalEntry(datetime.date.today(), "Salary of Jan.")
    sal1.post(date=datetime.date(year=2020, month=1, day=1), account=accounts.get(Account.CASH), quantity=+1000)
    sal1.post(date=datetime.date(year=2020, month=1, day=1), account=accounts.get(Account.EXPENSE), quantity=-1000)

    # Test
    assert sal1.postings[0].direction == Direction.INC
    assert sal1.post

# Generated at 2022-06-14 04:14:10.239217
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from typing import Any
    from ..commons.zeitgeist import DateRange

    # Any journal entry
    journal: JournalEntry[Any] = JournalEntry(date=date(2019, 1, 1), description="A Journal Entry", source=None, guid=None)

    # Any read_journal_entries function.
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[Any]]:
        return [journal]

    # Read using the read_journal_entries function.
    entries = read_journal_entries(DateRange(start=date(2019, 1, 1), end=date(2019, 12, 31)))

    # Check
    assert [journal] == [next(entries)]

# Generated at 2022-06-14 04:14:17.606845
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import datetime
    from budget.commons.data import AssetAccount
    # Set up
    j = JournalEntry[str]('2018-06-01', 'Add a test function', "I am a source", [])
    # Exercise
    r = j.post(datetime.now(), AssetAccount.of('Bank'), 1000)
    # Verify
    assert r.postings[0].direction == Direction.INC
    assert r.postings[0].amount == 1000
    # Clean up

# Generated at 2022-06-14 04:14:25.425266
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountRepository
    from .ledgers import GeneralLedger
    from .test_ledgers import InMemoryLedger
    from .test_accounts import InMemoryAccounts

    journal_entries = GeneralLedger(
        InMemoryLedger(),
        AccountRepository(InMemoryAccounts()),
        [],
        [],
        JournalEntryFactory(),
    ).read_journal_entries
    assert callable(journal_entries)

    # noinspection PyTypeChecker
    journal_entries.__call__(DateRange())

# Generated at 2022-06-14 04:14:28.060174
# Unit test for method __call__ of class ReadJournalEntries

# Generated at 2022-06-14 04:14:28.642085
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:14:29.664221
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    ReadJournalEntries


# Generated at 2022-06-14 04:14:41.775093
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from typing import Dict
    
    from ..commons.zeitgeist import DateRange
        
    from .accounts import Account
    from .source import Source
    from .journal import JournalEntry, Posting, ReadJournalEntries
        
    @dataclass(frozen=True)
    class Entry(JournalEntry[Source]):
        date: date
        description: str
        source: Source

    def get_journal_entry(source: Source, date: date, amount: int) -> Entry:
        return Entry(date, source.description, source).post(date, source.account, amount)

    accounts: Dict[str, Account] = {}

# Generated at 2022-06-14 04:14:46.007179
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def is_consistent(je: JournalEntry[_T]) -> bool:
        try:
            je.validate()
            return True
        except AssertionError:
            return False

    assert all(is_consistent(je) for je in read_journal_entries(DateRange.years(2000, 2002)))



# Generated at 2022-06-14 04:14:57.651145
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    entries = [JournalEntry(datetime.date(2019, 7, 1), "Transaction 1", None), JournalEntry(
        datetime.date(2019, 7, 8), "Transaction 2", None)]

    def _ReadJournalEntries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        yield from (e for e in entries if period.contains(e.date))

    assert list(_ReadJournalEntries(DateRange(datetime.date(2019, 7, 1), datetime.date(2019, 7, 10)))) == entries
    assert list(_ReadJournalEntries(DateRange(datetime.date(2019, 7, 1), datetime.date(2019, 7, 30)))) == entries
    assert list(_ReadJournalEntries(DateRange(datetime.date(2019, 6, 1), datetime.date(2019, 7, 31))))

# Generated at 2022-06-14 04:15:11.110033
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert True

# Generated at 2022-06-14 04:15:17.755639
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from datetime import date
    from ..accounts import Account as _Account
    je = JournalEntry[None](date(2020,1,1), "test journal entry", None)
    je.post(date(2020,1,1), _Account("Assets"), 1)
    je.post(date(2020,1,1), _Account("Expenses"), 1)
    je.validate()

# Generated at 2022-06-14 04:15:19.094756
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert isinstance(ReadJournalEntries.__call__, property)


# Generated at 2022-06-14 04:15:29.264022
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType, Account, AccountProtocol, AccountKind
    from .business import BusinessProtocol, Business, Stock, Book
    from .accounting import AccountingProtocol, Accounting, AccountingFactory
    from datetime import date
    from typing import List
    import os
    import pickle

    AccountingProtocol.register(Accounting)

    # Account protocol
    AccountProtocol.register(Account)
    @dataclass(frozen=True)
    class _Account(Account):
        asset_account: Account = Account("Cash", AccountType.ASSETS, AccountKind.BALANCE_SHEET)
        equity_account: Account = Account("Retained Earnings", AccountType.EQUITIES, AccountKind.BALANCE_SHEET)

# Generated at 2022-06-14 04:15:31.066631
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class MyReadJournalEntries(ReadJournalEntries[_T]):
        pass
    assert issubclass(MyReadJournalEntries, ReadJournalEntries)

# Generated at 2022-06-14 04:15:41.777462
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..books.model import Book
    book = Book(name="Test Book")
    journal_entry = book.post_journal_entry(datetime.date(year=2019, month=1, day=1), "Test Journal Entry")
    journal_entry.post(datetime.date(year=2019, month=1, day=1), book.equity, -100.00)
    journal_entry.post(datetime.date(year=2019, month=1, day=1), book.asset, 100.00)
    journal_entry.validate()

# Generated at 2022-06-14 04:15:42.390349
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert True

# Generated at 2022-06-14 04:15:50.154842
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j = JournalEntry(date=datetime.date(2020, 1, 1), description='asd')
    a = Account(name="ABC", type=AccountType.EQUITIES)
    j.post(date=datetime.date(2020, 1, 1), account=a, quantity=100)
    j.post(date=datetime.date(2020, 1, 1), account=a, quantity=-50)
    print(j.increments)
    print(j.decrements)
    print(j.debits)
    print(j.credits)
    assert(True)

# Generated at 2022-06-14 04:16:01.009856
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime as dt
    from pytest import raises
    from ..commons.numbers import Amount, Quantity

    class Tester:
        def __init__(self):
            self.journal = JournalEntry[Tester]()


# Generated at 2022-06-14 04:16:02.195695
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass  # Does nothing.

# Generated at 2022-06-14 04:16:41.194276
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    print("test_JournalEntry_post")

    from datetime import date
    from ..commons.numbers import Quantity
    from ..commons.others import makeguid
    from .accounts import Account, AccountType

    # Create an instance of class Account
    account = Account("0000", "Cash", AccountType.ASSETS)

    # Create an instance of class JournalEntry
    journal_entry = JournalEntry(date.today(), "Deposit from Bank", makeguid(), [])

    journal_entry.post(date.today(), account, Quantity(100))

    print(journal_entry)

    journal_entry.validate()


# Generated at 2022-06-14 04:16:50.386586
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Arrange
    class SomeSource:
        pass

    journal = JournalEntry(date=datetime.date.today(), description="testing 1, 2, 3...", source=SomeSource())

    # Act
    journal.post(
        date=datetime.date(year=2020, month=1, day=1),
        account=Account("Test Account", AccountType.EXPENSES),
        quantity=Amount("$10"),
    )

    # Assert
    assert 1 == len(journal.postings)
    assert journal.postings[0].journal == journal
    assert journal.postings[0].date == datetime.date(year=2020, month=1, day=1)
    assert journal.postings[0].account == Account("Test Account", AccountType.EXPENSES)
    assert journal.postings[0].direction == Direction

# Generated at 2022-06-14 04:16:53.966406
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    je = JournalEntry(datetime.date(2020, 1, 1), 'Test', None)
    je.post(je.date, Account('Cash'), 500)
    assert je.postings[0].amount == 500

# Generated at 2022-06-14 04:16:58.993369
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # pylint: disable=unused-variable
    @dataclass(frozen=True)
    class Foo:
        pass

    # pylint: enable=unused-variable

    @dataclass(frozen=True)
    class FooSource:
        pass

    journal_entries: ReadJournalEntries[FooSource] = lambda x: []
    journal_entries(DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31)))

# Generated at 2022-06-14 04:17:04.713245
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    j1 = JournalEntry(date=datetime.date.today(), description="No Source", source=None)
    j1.post(date=datetime.date.today(), account=Account(AccountType.ASSETS, "Bank"), quantity=Amount(10))
    assert j1.postings == [Posting(j1, datetime.date.today(), Account(AccountType.ASSETS, "Bank"), Direction.INC, Amount(10))]

# Generated at 2022-06-14 04:17:06.079911
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    assert True # TODO


# Generated at 2022-06-14 04:17:15.184950
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import datetime

    from .accounts import AccountType

    def read_journal_entries_fn(period: DateRange) -> Iterable[JournalEntry[None]]:
        journal = JournalEntry(datetime.date(2020, 5, 30), "Test Journal Entry 1", None)
        journal.post(journal.date, Account(AccountType.ASSETS, "Cash"), -10)
        journal.post(journal.date, Account(AccountType.EQUITIES, "Equity"), +10)
        journal.validate()
        yield journal

        journal = JournalEntry(datetime.date(2020, 5, 31), "Test Journal Entry 2", None)
        journal.post(journal.date, Account(AccountType.ASSETS, "Cash"), -15)

# Generated at 2022-06-14 04:17:16.962012
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:17:27.170199
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import DAY, this_year

    @dataclass(frozen=True)
    class Ledger:
        """
        Provides a ledger model.
        """

        #: Name of the ledger.
        name: str

        #: Description of the ledger.
        description: str

        #: Globally unique identifier.
        guid: Guid = field(default_factory=makeguid, init=False)

    class ReadLedgerJournalEntries:
        """
        Provides a conveniently defined ``ReadJournalEntries``.
        """


# Generated at 2022-06-14 04:17:33.939848
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import ChartOfAccount
    from .accounts import AccountType
    from .accounts import Account
    from .accounts import AssetAccount
    from .accounts import LiabilityAccount
    from .accounts import RevenueAccount
    from .accounts import ExpenseAccount
    from .accounts import EquityAccount
    from .accounts import Currency
    from .accounts import Money
    from .accounts import Quantity
    from ..banking import Bank
    import datetime
    currency = Currency.USD
    date = datetime.date(2020, 2, 3)
    amount = Amount(12)
    coa: ChartOfAccount = ChartOfAccount()
    coa.create(AccountType.ASSETS, "Cash", Account)
    coa.create(AccountType.ASSETS, "Accounts receivable", AssetAccount)
    coa.create

# Generated at 2022-06-14 04:18:54.686531
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType
    from .ids import GLID, GLIDFactory
    from .sources import BankAccount
    from ..commons.numbers import Quantity

    idfactory = GLIDFactory()

    ba = BankAccount("My Bank", GLID(idfactory), False)

    ## Create journal entries:
    je1 = JournalEntry[BankAccount](datetime.date(2020, 8, 1), "Transfer to bank account #2", ba).post(
        datetime.date(2020, 8, 1), Account("Cash", AccountType.ASSETS, GLID(idfactory)), -20_000
    ).post(datetime.date(2020, 8, 1), Account("Bank", AccountType.ASSETS, GLID(idfactory)), +20_000)


# Generated at 2022-06-14 04:18:55.329760
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:18:58.618225
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read(period: DateRange) -> Iterable[JournalEntry[int]]:
        return []

    assert callable(ReadJournalEntries.__call__)
    assert isinstance(ReadJournalEntries.__call__(read, DateRange()), Iterable)

# Generated at 2022-06-14 04:18:59.179381
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass



# Generated at 2022-06-14 04:19:05.655094
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class JS:
        """
        A journal source entity.
        """
        start_date: datetime.date
        end_date: datetime.date

    JE = JournalEntry[JS]

    def source_read(period: DateRange):
        for i in range(3):
            yield JE(datetime.date(2018, 1, i + 1), f"JE-{i+1}", JS(datetime.date(2018, 1, i + 1), datetime.date(2018, 1, i + 1)))

    reader = ReadJournalEntries(source_read)
    assert len(list(reader(DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 1, 3))))) == 3

# Generated at 2022-06-14 04:19:09.808255
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Setup:
    #   Create object and set valid values
    journal = JournalEntry("2020-01-04", "description", "source")
    journal.post("2020-01-04", "account", "quantity")

    # Exercise & Verify:
    journal.validate()


# Generated at 2022-06-14 04:19:15.584786
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    path = './journal.csv'
    import csv
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
        pass

if __name__ == "__main__":
    test_JournalEntry_post()
    pass

# Generated at 2022-06-14 04:19:16.321377
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:19:18.265697
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert issubclass(ReadJournalEntries, Protocol)
    assert not hasattr(ReadJournalEntries, '__call__')

# Generated at 2022-06-14 04:19:23.348104
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    source = 1
    test_object = JournalEntry(datetime.date.today(), "Test", source)
    test_object.post(datetime.date.today(), Account("Assets", "Cash"), 100)
    test_object.post(datetime.date.today(), Account("Revenues", "Sales"), -100)
    test_object.validate()