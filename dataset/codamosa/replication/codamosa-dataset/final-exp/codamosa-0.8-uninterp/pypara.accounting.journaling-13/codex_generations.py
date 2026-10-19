

# Generated at 2022-06-14 04:11:37.168357
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import dataclass
    from typing import Any, cast
    from unittest.mock import MagicMock

    # Define a mock read function:
    @dataclass(frozen=True)
    class ReadMock:
        _function: MagicMock
        _return_values: Any = None

        def __call__(self, *args, **kwargs) -> Any:
            return self._function(*args, **kwargs)

        def __enter__(self) -> Any:
            self._function.reset_mock()
            return self

        def __exit__(self, *args) -> None:
            pass

    # Create a mock object for reading journal entries:

# Generated at 2022-06-14 04:11:38.406504
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass


# Generated at 2022-06-14 04:11:43.452480
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry[str](date=datetime.date(2019, 1, 1), description="Test", source="Test")
    je.post(datetime.date(2019, 1, 1), Account("Test", AccountType.ASSETS), +100)
    je.post(datetime.date(2019, 1, 1), Account("Test", AccountType.REVENUES), -100)
    je.validate()

# Generated at 2022-06-14 04:11:44.292139
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # TODO: Implement
    pass

# Generated at 2022-06-14 04:11:50.576181
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():

    from datetime import date as D

    @dataclass(frozen=True)
    class Event:
        """
        Provides an event to be journalized.
        """

        id: int

    def read(period: DateRange) -> Iterable[JournalEntry[Event]]:
        """
        The function that creates the instances that we want to test.
        """
        yield JournalEntry(D(2017, 1, 1), "An Event", Event(0))
        if period is not None:
            if period.start and period.finish:
                yield JournalEntry(D(2018, 1, 1), "Another Event", Event(1))
            else:
                yield JournalEntry(D(2019, 1, 1), "Yet Another Event", Event(2))


# Generated at 2022-06-14 04:11:51.182946
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:11:55.168306
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    a = Account("assets")
    r = Account("revenues")
    j = JournalEntry("", "", "", [Posting("", 0, a, Direction.INC, 1), Posting("", 0, r, Direction.DEC, 1)])
    j.validate()

# Generated at 2022-06-14 04:12:00.301377
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry(date= datetime.date(year= 2020, month= 15, day= 10), description="test", source=None)
    j.post(date= datetime.date(year= 2020, month= 15, day= 10), account= Account(code= "1001", type= AccountType.ASSETS, name= "Cash in Hand"), quantity= Quantity(100))
    j.post(date= datetime.date(year= 2020, month= 15, day= 10), account= Account(code= "1002", type= AccountType.ASSETS, name= "Cash in Bank"), quantity= -Quantity(100))
    j.validate()
    #Since the total debit and credit amounts are equal (so total_debit == total_credit) , the test will pass.

    #Unit test for method validate of class JournalEntry
    j1 = Journal

# Generated at 2022-06-14 04:12:09.936643
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Test the post() method of JournalEntry.
    """
    # get the instance
    je = JournalEntry(datetime.date.today(), "test description", "test source")
    # assert the instance
    assert je.postings == []
    # post the amount 20 to the account
    je.post(datetime.date.today(), Account("TESTACCOUNT", AccountType.ASSETS), 20)
    # assert the instance
    assert je.postings == [Posting(je, datetime.date.today(), Account("TESTACCOUNT", AccountType.ASSETS), Direction.INC, Amount(20))]
    # post the amount -10 to the account
    je.post(datetime.date.today(), Account("TESTACCOUNT", AccountType.ASSETS), -10)
    # assert the instance
    assert je.postings

# Generated at 2022-06-14 04:12:21.780680
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Unit test for method __call__ of class ReadJournalEntries.
    """
    from .accounts import BalanceSheetAccount, IncomeStatementAccount
    from .business import Business
    from .events import Event, RecordJournalEntry
    from .reporting import Reporting
    from .sources import EventStore

    # Setup a business:
    curr_bus = Business.start(EventStore(), EventStore())

    # Prepare a function to read journal entries:
    def read_journals(period: DateRange) -> Iterable[JournalEntry[Event]]:
        """
        Reads journal entries from the event store of the `Business`.
        """
        # Get reporting instance:
        report = Reporting.from_business(curr_bus)

        # Get all relevant events:
        relevant_events = report.get_events(RecordJournalEntry, period)

       

# Generated at 2022-06-14 04:12:31.780478
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    new_journalentry = JournalEntry(date=datetime.date(2019,10,3), description="test", source="test")
    new_journalentry.post(date=datetime.date(2019,10,3), account=Account(id="test",name="test",type=AccountType.ASSETS), quantity=Quantity(1))
    new_journalentry.post(date=datetime.date(2019,10,3), account=Account(id="test",name="test",type=AccountType.EXPENSES), quantity=Quantity(-1))
    new_journalentry.validate()

# Generated at 2022-06-14 04:12:44.005862
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import make_accounts

    accounts = make_accounts()

    def reader(period: DateRange) -> Iterable[JournalEntry[object]]:
        yield JournalEntry(
            datetime.date.today(), "Journal Entry 1", None, [
                Posting(None, datetime.date.today(), accounts["cash"], Direction.INC, Amount(100)),
                Posting(None, datetime.date.today(), accounts["revenue"], Direction.DEC, Amount(100)),
            ]
        )

# Generated at 2022-06-14 04:12:51.830087
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry(None, None, None)
    je.post(
        datetime.date(2020, 1, 1),
        Account(Account.root, 'Account1', AccountType.ASSETS),
        +100,
    )
    je.post(
        datetime.date(2020, 1, 1),
        Account(Account.root, 'Account2', AccountType.EXPENSES),
        -100,
    )
    je.validate()
    print(je)

if __name__ == "__main__":
    test_JournalEntry_validate()

# Generated at 2022-06-14 04:13:04.951843
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    with pytest.raises(AssertionError) as exinfo:
        JournalEntry(
            date=datetime.date(2020, 1, 1),
            description="Test Journal Entry",
            source="Test Source"
        ).post(
            date=datetime.date(2020, 1, 1),
            account=Account(
                code="101", type=AccountType.ASSETS, name="Cash"
            ),
            quantity=Decimal("100.00")
        ).post(
            date=datetime.date(2020, 1, 1),
            account=Account(
                code="102", type=AccountType.ASSETS, name="Bank"
            ),
            quantity=Decimal("200.00")
        ).validate()


# Generated at 2022-06-14 04:13:09.385868
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    account = Account('Cash', 'Assets', 'Current Assets')
    entry = JournalEntry.new('2016-01-01', 'Starting Balance')
    entry.post(account, Amount(100))

    assert callable(ReadJournalEntries.__call__)


# Generated at 2022-06-14 04:13:17.847258
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    def _helper(journalEntry):
        try:
            journalEntry.validate()
            print("PASSED: JournalEntry test")
        except AssertionError:
            print("FAILED: JournalEntry test")
    from .accounts import Account, AccountType
    from .commons.zeitgeist import DateRange
    from .transactions import ReadTransactions
    from .apps import read_applications
    from .accounts import read_accounts
    from .journal import make_journal_entry
    from .journal import ReadJournalEntries

    apps = read_applications("./Data/applications.txt")
    accounts = read_accounts("./Data/accounts.txt")
    account = accounts['CASH']
    transaction1 = apps[0]
    transaction2 = apps[0]

# Generated at 2022-06-14 04:13:30.585624
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, parse_account
    from .currencies import USD, EUR
    from .exchangerates import ExchangeRate, ExchangerateRegistry
    from .debtors import Debtor, DebtorRegistry
    from .invoices import Invoice, InvoiceRegistry

    journal = JournalEntry(date=datetime.date(2020, 1, 1), description="Opening balance.")
    journal.post(date=datetime.date(2020, 1, 1), account=parse_account('Assets:Bank:Checking'), quantity=1000)
    journal.post(date=datetime.date(2020, 1, 1), account=parse_account('Equities:Opening Balances'), quantity=-1000)


# Generated at 2022-06-14 04:13:35.936426
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass
    class _Foo:
        pass

    @dataclass
    class _Bar:
        pass

    calling = ReadJournalEntries()

    assert hasattr(calling, '__call__')
    assert not hasattr(calling, '__getitem__')



# Generated at 2022-06-14 04:13:36.550743
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:13:44.841142
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j1 = JournalEntry(
        date=datetime.date.today(),
        description="Test",
        source=None,
    )
    j1.postings.append(Posting(
        journal=j1,
        date=datetime.date.today(),
        account=Account("A", AccountType.ASSETS),
        direction=Direction.INC,
        amount=Amount(10),
    ))
    j1.postings.append(Posting(
        journal=j1,
        date=datetime.date.today(),
        account=Account("B", AccountType.ASSETS),
        direction=Direction.INC,
        amount=Amount(15),
    ))

# Generated at 2022-06-14 04:14:02.099743
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..accounts.accounts import Account, AccountType
    from .journal import JournalEntry

    DEPOSIT_A = Account(AccountType.LIABILITIES, "Deposit A")
    SALARY = Account(AccountType.EXPENSES, "Salary")

    entry = JournalEntry("2018-05-01", "Employees' salary", None)
    entry = entry.post("2018-05-01", DEPOSIT_A, +1_00_000)
    entry = entry.post("2018-05-01", SALARY, -1_00_000)

    entry.validate()

    assert len(entry.postings) == 2
    assert entry.debits[0].amount == -1_00_000
    assert entry.credits[0].amount == +1_00_000

# Generated at 2022-06-14 04:14:12.518806
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    class Test:
        def __init__(self, date, description, account_type, account_name, quantity, is_debit):
            self.date, self.description, self.account_type, self.account_name, self.quantity, self.is_debit = date, description, account_type, account_name, quantity, is_debit
    
    accounts = [
        Account("SAVINGS", AccountType.ASSETS),
        Account("INCOME", AccountType.REVENUES),
        Account("EXPENSES", AccountType.EXPENSES),
        Account("EQUITIES", AccountType.EQUITIES)
    ]

# Generated at 2022-06-14 04:14:13.424240
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:14:16.748340
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    period = DateRange(None, None)
    entries = list()
    read = lambda period: entries
    def test():
        assert read.__call__(period) == entries
    test()

# Generated at 2022-06-14 04:14:20.908136
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert issubclass(list, ReadJournalEntries[int])
    assert isinstance(ReadJournalEntries.__call__, property)
    assert ReadJournalEntries[int].__annotations__['return'] == Iterable[JournalEntry[int]]

# Generated at 2022-06-14 04:14:33.022912
# Unit test for method __call__ of class ReadJournalEntries

# Generated at 2022-06-14 04:14:44.456023
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from unittest import TestCase, main
    from dataclasses import asdict, field
    from typing import Dict, List
    from uuid import uuid4
    from datetime import date
    from ..commons.money import isum, Amount
    from ..commons.others import get_now
    from ..commons.zeitgeist import DateRange
    from ..commons.types import DateField
    from ..commons.accounts import Account, AccountType
    from ..data.movement import Movement
    from ..data.journal import JournalEntry, ReadJournalEntries

    class TestObject(TestCase, ReadJournalEntries):
        def __call__(self, period: DateRange):
            return self.journal_entries


# Generated at 2022-06-14 04:14:56.601137
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Test case when quantity is zero
    from .accounts import Account
    from .account_types import AccountType
    from .posting_types import PostingType
    from .commons import Amount
    from .commons import Quantity
    from .commons import DateRange
    from .commons import datetime
    from .commons import Guid
    from .globals import JournalEntries
    from .read_journal_entries import ReadJournalEntries
    journalEntry = JournalEntry()
    date = datetime.date.today()
    quantity = Quantity(0)
    account = Account("Account", AccountType.ASSETS, PostingType.BASIC)
    
    assert journalEntry.post(datetime.date.today(), "Account", 0).postings == []

# Generated at 2022-06-14 04:15:07.983734
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Test the method post of class JournalEntry
    """
    amount = 14.0
    account = Account(
        "abc",
        "Acme Inc.",
        AccountType.ASSETS
    )
    account2 = Account(
        "abc2",
        "Acme Inc.",
        AccountType.ASSETS
    )
    
    date = datetime.date(2020, 1, 1)
    date2 = datetime.date(2020, 1, 2)
    date3 = datetime.date(2020, 1, 3)
    
    description = "Sales of widgets"
    description2 = "Sale of widgets"
    
    source = "sale_of_widgets"
    
    quantity = 14.0
    quantity2 = -14.0
    

# Generated at 2022-06-14 04:15:15.287973
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from .ledger import Ledger, GeneralLedger
    from .accounts import Account, AccountFactory
    from .validate import Validate
    ledger = Ledger(
        general_ledger=GeneralLedger(
            account_factory=AccountFactory(
                accounts=[Account("Assets", AccountType.ASSETS), Account("Equities", AccountType.EQUITIES), Account("Liabilities", AccountType.LIABILITIES), Account("Revenue", AccountType.REVENUES), Account("Expenses", AccountType.EXPENSES)]),
        account_validator=Validate.Ledger.Account()),
        journal_validator=Validate.Ledger.Journal(),
    )
    journal = JournalEntry(date=date(2019, 10, 10), description='Description')

# Generated at 2022-06-14 04:15:37.798325
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # setup journal entries
    today = datetime.date.today()
    je1 = JournalEntry[int](today, "Testing posting 1", 1)
    je2 = JournalEntry[int](today, "Testing posting 2", 2)
    je3 = JournalEntry[int](today, "Testing posting 3", 3)

    # setup accounts
    account1 = Account("account1", AccountType.EXPENSES)
    account2 = Account("account2", AccountType.EXPENSES)

    # make a posting
    je1.post(today, account1, 25)
    je2.post(today, account2, -20)
    je3.post(today, account1, 12.5)

    assert len(je1.postings) == 1
    assert len(je2.postings) == 1

# Generated at 2022-06-14 04:15:42.251433
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Setup
    je = JournalEntry[str]("2020-01-01", "Description", "Source", [], 'je_guid')
    je.postings.append( Posting(je, datetime.date(2020, 1, 1), 'asset', 'INC', 10))
    je.postings.append( Posting(je, datetime.date(2020, 1, 1), 'liability', 'DEC', 10))
    # Exercise
    je.post(datetime.date(2020, 1, 1), 'revenue', -50)
    # Verify
    assert je.postings[0].amount == 10
    assert je.postings[1].amount == 50
    assert je.postings[2].amount == 10
    assert je.postings[2].direction == 'DEC'

# Generated at 2022-06-14 04:15:52.062978
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from typing import Dict, Iterable, List
    
    reader = ReadJournalEntries()

    def read_entries(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
        return [
            JournalEntry(date(2018,12,31), "Journal entry 1 (dec 31, 2018)", "Source 1", []),
            JournalEntry(date(2019,1,1), "Journal entry 2 (jan 1, 2019)", "Source 2", [])]
    
    reader.__call__ = read_entries.__get__(reader, ReadJournalEntries)
    entries: Iterable[JournalEntry[_T]] = reader(DateRange(date(2018,12,30), date(2019,1,2)))


# Generated at 2022-06-14 04:16:03.353573
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountType

    #: Declares an arbitrary date.
    date = datetime.date(2019, 1, 1)

    #: Declares a date range to use for testing.
    date_range = DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))

    #: Declares an asset account to use for testing.
    asset_account = Account("Asset", AccountType.ASSETS)

    #: Defines a class derived from ``ReadJournalEntries`` protocol.
    class DerivedReadJournalEntries(ReadJournalEntries):

        #: Overrides the function ``__call__``.
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            #: Declares an arbitrary journal entry.
            journal_entry = JournalEntry

# Generated at 2022-06-14 04:16:11.683686
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():

    from .accounts import Account
    from .books import Book
    from .chart import Chart
    from .products import Product

    chart = Chart()
    chart.add_product_category(name="Saab")
    chart.add_account(name="Imprest", type=AccountType.CASH)

    book = Book()
    book.chart = chart

    product_a = Product(name="A")
    product_a.id = Guid.from_str("f07fa7e3-067d-47d2-8c1d-0a927c29598a")

    product_b = Product(name="B")
    product_b.id = Guid.from_str("f07fa7e3-067d-47d2-8c1d-0a927c29598b")

    journal_entry1

# Generated at 2022-06-14 04:16:21.153162
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..model import Account, AccountType
    from ..model import JournalEntry
    from ..model import Quantity
    from ..model import Direction
    from datetime import date
    expense = Account(AccountType.EXPENSES, 'Telephone', 'Telephone Expense')
    revenue = Account(AccountType.REVENUES, 'Sales', 'Sales Revenue')
    expense_journal_entry = JournalEntry(date.today(), 'Expense telephone', expense)
    expense_journal_entry.post(date.today(), expense, Quantity('-300'))
    assert len(expense_journal_entry.decrements) == 1
    assert expense_journal_entry.decrements[0].direction == Direction.DEC
    revenue_journal_entry = JournalEntry(date.today(), 'Sale', revenue)

# Generated at 2022-06-14 04:16:31.943300
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    a = JournalEntry(datetime.date(2020, 5, 4), "", "")
    a.post(datetime.date(2020, 5, 4), Account(AccountType.ASSETS, "1100000"), -51121)
    a.post(datetime.date(2020, 5, 4), Account(AccountType.REVENUES, "4100000"), 51121)
    a.validate()
    b = JournalEntry(datetime.date(2020, 5, 4), "", "")
    b.post(datetime.date(2020, 5, 4), Account(AccountType.ASSETS, "1100000"), -51121)

# Generated at 2022-06-14 04:16:41.672439
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    def assertNoExceptions(self, date, account, quantity):
        self.post(date, account, quantity).validate()
    
    cash = Account("Cash")
    income = Account("Income")
    expense = Account("Expense")
    je = JournalEntry(datetime.date.today(), "Test Journal Entry")
    
    # [1] If quantity is zero, post nothing.
    assertNoExceptions(je, datetime.date.today(), cash, Amount(0))
    assert len(je.postings) == 0

    # [2] If quantity is non-zero and debits == credits, exception is not raised.
    assertNoExceptions(je, datetime.date.today(), cash, Amount(100))
    assertNoExceptions(je, datetime.date.today(), income, Amount(100))

# Generated at 2022-06-14 04:16:49.639927
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Setup:
    class X:
        pass

    dummy = X()
    start_date = datetime.date(2000, 1, 1)
    dummy_range = DateRange(begin=start_date, end=datetime.date.today())

    def __call__(self, period: DateRange) -> Iterable[JournalEntry[X]]:
        assert self is dummy
        assert period.is_same(dummy_range)
        return []

    # Exercise:
    ReadJournalEntries.__call__(__call__, dummy, dummy_range)

    # Teardown:
    del dummy
    del dummy_range
    del __call__



# Generated at 2022-06-14 04:16:56.555285
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    journal_entry = JournalEntry[str](datetime.date.today(), "description", "source")
    journal_entry.post(datetime.date.today(), Account.asset("Chequing Account"), +100)

    #
    journal_entry.post(datetime.date.today(), Account.asset("Cash"), -50)
    journal_entry.post(datetime.date.today(), Account.expense("Restaurants"), -50)

    journal_entry.validate()
    return journal_entry


# Generated at 2022-06-14 04:17:39.370332
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType, Account, accounts
    from .chartofaccounts import ChartOfAccounts
    from .accounts import DefaultChartOfAccounts
    import datetime

    ChartOfAccounts.of = DefaultChartOfAccounts
    assets = AccountType.ASSETS
    equity = AccountType.EQUITIES
    liabilities = AccountType.LIABILITIES
    revenue = AccountType.REVENUES
    expenses = AccountType.EXPENSES

    # simple test to see if the posting method works or not
    def test_posting():
        chart = ChartOfAccounts()
        accounts(chart, ("Cash", assets), ("Equity", equity), ("Liability", liabilities))
        accounts(chart.account_type("Assets"), ("Bank", assets))
        accounts(chart.account_type("Expenses"), ("Cost of goods sold", expenses))



# Generated at 2022-06-14 04:17:49.147454
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    assert True

    journalEntry = JournalEntry[str](date=datetime.date.today(), description='test1', source='test1')
    journalEntry.post(datetime.date.today(), account=Account(name='A1', type=AccountType.ASSETS), quantity=500)
    journalEntry.post(datetime.date.today(), account=Account(name='L1', type=AccountType.LIABILITIES), quantity=-500)
    try:
        journalEntry.validate()
    except AssertionError as error:
        assert False

    journalEntry = JournalEntry[str](date=datetime.date.today(), description='test2', source='test2')
    journalEntry.post(datetime.date.today(), account=Account(name='A1', type=AccountType.ASSETS), quantity=500)

# Generated at 2022-06-14 04:17:58.418122
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    ## Setup
    journal_entry = JournalEntry(
        date = datetime.date(2019, 8, 23),
        source = "Payroll 1",
        description = "Salary for August",
    )

    journal_entry.post(
        date = datetime.date(2019, 8, 23),
        account = Account(
            code = "1000.1",
            name = "Cash",
            type = AccountType.ASSETS
        ),
        quantity = 150000
    )

    journal_entry.post(
        date = datetime.date(2019, 8, 23),
        account = Account(
            code = "4040.1",
            name = "Salaries",
            type = AccountType.EXPENSES
        ),
        quantity = -150000
    )

    ## Execute
    journal_entry.validate()

# Generated at 2022-06-14 04:18:08.171990
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ledger.accounts import AccountType
    from ledger.toy import create_toy_ledger
    from ledger.journal import JournalEntry, Direction

    ledger = create_toy_ledger()
    j = JournalEntry(datetime.date(2018, 1, 2), "Test Journal Entry")
    j.post(datetime.date(2018, 1, 3), ledger.accounts.expenses_sales_accounts_sales_discounts, -100)
    j.post(datetime.date(2018, 1, 3), ledger.accounts.equity_owner_equity_owners_contributions, 100)
    assert j.postings[0].is_debit
    assert j.postings[1].is_credit

# Generated at 2022-06-14 04:18:11.043328
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-14 04:18:18.719769
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    correct_JournalEntry = JournalEntry[int](date=datetime.date(2000,1,1), description="test", source=1)
    correct_JournalEntry.post(date=datetime.date(2000,1,1), account=Account(name="an Account", type=AccountType.REVENUES), quantity=40)
    correct_JournalEntry.post(date=datetime.date(2000,1,1), account=Account(name="another Account", type=AccountType.EXPENSES), quantity=-40)
    try:
        correct_JournalEntry.validate()
    except AssertionError as e:
        assert False, f"AssertionError: {e}"
    else:
        assert True, "No AssertionError thrown. Test passed"


  

# Generated at 2022-06-14 04:18:30.477289
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    #: Dummy account for unit testing.
    account = Account("MyAccount")
    #: Dummy business object for unit testing.
    business_object = object()
    #: Dummy journal entry for unit testing.
    journal_entry = JournalEntry(datetime.date.today(), "", business_object)
    #: Dummy posting for unit testing.
    posting = Posting(journal_entry, datetime.date.today(), account, Direction.INC, Amount(100))
    #: List of postings.
    postings = [posting]
    #: Dummy journal entry for unit testing.
    journal_entry = JournalEntry(datetime.date.today(), "", business_object, postings)
    #: Validate the journal entry.
    journal_entry.validate()
    #: Dummy journal entry for unit testing.
    journal_

# Generated at 2022-06-14 04:18:38.797830
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.numbers import USD

    # Create JournalEntry, Account and Posting objects
    account = Account(AccountType.ASSETS, 'Cash')
    journal = JournalEntry(date = datetime.date.today(), description = 'test', source = 'test')
    posting = Posting(journal, date = datetime.date.today(), account = account, direction = Direction.INC, amount = USD(100))

    # Append posting to list of postings in journal
    journal.postings.append(posting)

    # Check if posting is listed in journal.postings.
    assert posting in journal.postings


# Generated at 2022-06-14 04:18:42.978773
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass
    class MyJournalEntry(JournalEntry):
        pass

    @dataclass
    class MyBusinessObject:
        pass


# Generated at 2022-06-14 04:18:44.169850
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Type signature for method __call__ of class ReadJournalEntries
    """

# Generated at 2022-06-14 04:19:59.512837
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():

    from unittest.mock import call
    from unittest.mock import Mock
    from unittest.mock import sentinel
    from unittest.mock import patch
    class ReadJournalEntriesMock(ReadJournalEntries[str]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[str]]:
            return isum(Mock(), Mock())

    with patch("pyfi.books.journal.isum") as isum_mock:
        ReadJournalEntriesMock()(sentinel.period)
        isum_mock.assert_called_once_with(call(), call())

# Generated at 2022-06-14 04:20:11.111964
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal_entry = JournalEntry[int](
        date=datetime.date.today(),
        description="description",
        source=123,
    )
    journal_entry.post(
        date=datetime.date.today(),
        account=Account(code="ABC", type=AccountType.ASSETS),
        quantity=Quantity(100),
    )
    journal_entry.post(
        date=datetime.date.today(),
        account=Account(code="ABC", type=AccountType.EXPENSES),
        quantity=Quantity(40),
    )
    journal_entry.post(
        date=datetime.date.today(),
        account=Account(code="ABC", type=AccountType.REVENUES),
        quantity=Quantity(-40),
    )

# Generated at 2022-06-14 04:20:12.344241
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert True



# Generated at 2022-06-14 04:20:16.681916
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    je = JournalEntry(datetime.date.today(), "test", "test")
    je.post(datetime.date.today(), "taj", 400)
    je.post(datetime.date.today(), "taj", 0)
    assert len(je.postings) == 1

# Generated at 2022-06-14 04:20:20.495916
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class ReadJournalEntriesStub(ReadJournalEntries[str]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[str]]:
            return []
    assert isinstance(ReadJournalEntriesStub(), ReadJournalEntries)

# Generated at 2022-06-14 04:20:27.286911
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    import random
    from .accounts import AccountType

    for i in range(1, 10):
        journal = JournalEntry(datetime.date.today(), "Test", None)
        journal.post(datetime.date.today(), Account(str(random.randint(1, 1000)), AccountType.ASSETS), random.randint(1,1000))
        journal.post(datetime.date.today(), Account(str(random.randint(1, 1000)), AccountType.LIABILITIES), random.randint(1,1000))
        journal.validate()

# Generated at 2022-06-14 04:20:34.541409
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Arrange:
    from .business import Business, BusinessType, BusinessField, BusinessFields
    from .accounts import AccountType
    from .tags import Tag, TagType
    from .transactions import Transaction

# Generated at 2022-06-14 04:20:42.922178
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import unittest

    class SampleJournalEntry(JournalEntry[_T]):
        def __init__(self, date: datetime.date, description: str) -> None:
            super().__init__()
            self.date = date
            self.description = description
            self.postings = []

    class F(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            if period.starts_after(datetime.date(2019, 6, 1)):
                yield SampleJournalEntry(datetime.date(2019, 6, 1), "Hello")
            if period.covers(datetime.date(2019, 7, 1)):
                yield SampleJournalEntry(datetime.date(2019, 7, 1), "World")

    f = F()


# Generated at 2022-06-14 04:20:52.490106
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..branches.banks import Account as BankAccount
    from ..branches.sales import Sale
    import datetime

    bank_account: BankAccount = BankAccount("CITI", "12345", "Ketan Pandya")
    sale = Sale("CITI:12345", date=datetime.date(2019, 10, 9), amount=1000)
    journal_entry = JournalEntry(date=datetime.date(2019, 10, 9), description="CUST_PAYMENT", source=sale)
    journal_entry.post(date=datetime.date(2019, 10, 9), account=bank_account.liability, quantity=-1000)
    journal_entry.post(date=datetime.date(2019, 10, 9), account=sale.revenue, quantity=1000)
    return journal_entry


# Generated at 2022-06-14 04:21:02.127768
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import read_accounts
    from .fixtures import read_journal_fixtures
    from .readers import read_journal_entries


    accounts = read_accounts(read_journal_fixtures)
    je_reader: ReadJournalEntries[None] = read_journal_entries(accounts, read_journal_fixtures)
    period = DateRange.make(datetime.date(2020, 1, 1), datetime.date(2020, 1, 31))

    assert len(list(je_reader(period))) == 5
