

# Generated at 2022-06-14 04:11:28.998288
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry[int](
        date = datetime.date(2020, 10, 5),
        description = 'Sample journal entry',
        source = 0,
    )
    j.post(date = datetime.date(2020, 10, 5), account = Account.EXPENSES, quantity = -1000)
    j.post(date = datetime.date(2020, 10, 5), account = Account.CASH, quantity = 1000)
    j.validate()
    assert True


# Generated at 2022-06-14 04:11:32.507002
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j = JournalEntry(datetime.datetime.now(),'test',None)
    j.post(datetime.datetime.now(),Account(AccountType.ASSETS,1),Quantity(2))

# Generated at 2022-06-14 04:11:37.269359
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Unit test for method __call__ of class ReadJournalEntries.
    """

    # Test: Normal Use Case
    with mock.patch("bla", return_value=None):
        pass

    # Test: Normal Use Case
    with mock.patch("bla", return_value=None):
        pass

# Generated at 2022-06-14 04:11:41.582075
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j1 = JournalEntry(datetime.date.today(), "Description", None)
    j1.post(datetime.date.today(), Account("A"), Quantity(100))
    j1.post(datetime.date.today(), Account("B"), Quantity(-100))
    j1.validate()

# Generated at 2022-06-14 04:11:49.034576
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType
    from .globals import books
    from .currencies import currency
    from datetime import date
    journalentry = JournalEntry[1]
    journalentry.date = date.today()
    journalentry.description = "sample"
    journalentry.source = 1

    #post
    journalentry.post(date.today(), Account(AccountType.REVENUES, "Sales", currency(value=10), 1), Amount(40))
    journalentry.post(date.today(), Account(AccountType.REVENUES, "Sales", currency(value=10), 1), Amount(40))
    journalentry.validate()

    #test fail
    journalentry.post(date.today(), Account(AccountType.REVENUES, "Sales", currency(value=10), 1), Amount(40))

# Generated at 2022-06-14 04:11:56.164041
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime
    from .accounts import Account, AccountType
    from .books import Book
    from .currencies import Currency

    journal_entry = JournalEntry[Book]
    date = datetime.date.today()
    account = Account("Assets:Cash", AccountType.ASSETS, Currency.USD)
    quantity = Quantity(12)

    j = journal_entry(date, "Description", Book()).post(date, account, quantity)
    assert j.postings[0].is_debit


# Generated at 2022-06-14 04:11:58.753047
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_entries(period: DateRange) -> Iterable[JournalEntry[None]]:
        pass

    assert issubclass(read_entries.__class__, ReadJournalEntries)

# Generated at 2022-06-14 04:12:08.848855
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType

    # Create the test account
    test_account = Account(AccountType.ASSETS, "Test account")

    # Create test journal entry
    test_journal_entry = JournalEntry(datetime.date(2020, 1, 1), "test", "testing")

    # Post to this test journal entry:
    test_journal_entry.post(datetime.date(2020, 1, 1), test_account, 1)
    test_journal_entry.post(datetime.date(2020, 1, 1), test_account, -1)

    # Check if this test journal entry is consistent
    test_journal_entry.validate()

    # Post to this test journal entry again:
    test_journal_entry.post(datetime.date(2020, 1, 1), test_account, 1)


# Generated at 2022-06-14 04:12:20.652326
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .ledgers import Ledger
    from .accounts import AccountingPeriod, Account
    from .accounttypes import AccountType
    from .reporting import OwnerEquityCalculator
    from .currency import Currency

    # given: A ledger with an account for trial balance and an account for owner equity calculation, and a reporting period.
    ledger = Ledger()
    trial_balance_account = ledger.trial_balance.account
    owner_equity_account = ledger.open_account(AccountType.EQUITIES, 'OwnerEquity')
    reporting_period = AccountingPeriod('2020-01-01', '2020-12-31')

    # and: The ledger is empty
    assert owner_equity_account.get_balance(reporting_period) == 0.0

    # when: A journal entry is posted,
    entry = JournalEntry()
    entry

# Generated at 2022-06-14 04:12:24.832574
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    with JournalEntry[None](datetime.date.today(), "A journal entry") as entry:
        entry.post(datetime.date.today(), Account("CASH"), 1000)
        entry.post(datetime.date.today(), Account("SALES"), -1000)
    
    entry.validate()

# Generated at 2022-06-14 04:12:30.978454
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
  je = JournalEntry.post()

# Generated at 2022-06-14 04:12:37.382296
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from accounting.entities.accounts import Account
    
    journal_entry1 = JournalEntry[str](date(2020,1,1),'FOO', 'FIRST JOURNAL ENTRY')
    journal_entry1.post(date(2020,1,1), Account('12300', AccountType.ASSETS), 123)
    journal_entry1.post(date(2020,1,1), Account('54300', AccountType.EQUITIES), 423)
    assert journal_entry1.postings[0].account.number == '12300' and journal_entry1.postings[1].account.number == '54300'
    assert journal_entry1.postings[0].amount.value == 123 and journal_entry1.postings[1].amount.value == 423

# Generated at 2022-06-14 04:12:47.813888
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():

    from .accounts import Account, AccountType
    from .commons.zeitgeist import DateRange

    je1 = JournalEntry(datetime.date(2020, 7, 1), "accrual for July 1st", None) \
        .post(datetime.date(2020, 7, 1), Account("1000", "cash", AccountType.ASSETS), +1000) \
        .post(datetime.date(2020, 7, 1), Account("2801", "salary payable", AccountType.LIABILITIES), -1000)


# Generated at 2022-06-14 04:12:54.984667
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    account1 = Account(
        name="Cash",
        code="100",
        type=AccountType.ASSETS,
        description="Cash on hand",
        is_primary=True,
        is_pl=True,
        is_balance_sheet=True,
    )
    account2 = Account(
        name="Salary",
        code="200",
        type=AccountType.EXPENSES,
        description="Salary for the month",
        is_primary=True,
        is_pl=True,
        is_balance_sheet=True,
    )

# Generated at 2022-06-14 04:13:06.821177
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry(
        description="Test Journal Entry",
        date=datetime.date(2020, 8, 30),
        source=None,
        postings=[
            Posting(journal=None, date=datetime.date(2020, 8, 30), account=Account(str(0)), direction=Direction.INC, amount=Amount(1)),
            Posting(journal=None, date=datetime.date(2020, 8, 30), account=Account(str(0)), direction=Direction.INC, amount=Amount(2)),
            Posting(journal=None, date=datetime.date(2020, 8, 30), account=Account(str(0)), direction=Direction.DEC, amount=Amount(3)),
        ]
    )
    assert j.validate() is None

# Generated at 2022-06-14 04:13:07.889943
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass



# Generated at 2022-06-14 04:13:16.459714
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    class MockObject:
        def __init__(self, date: datetime.date, description: str, Debits: Amount) -> None:
            self.date = date
            self.description = description
            self.Debits = Debits

    ExpensesAccount = Account('Expenses', AccountType.EXPENSES)
    EquityAccount = Account('Equity', AccountType.EQUITIES)

    MockJournalEntry = JournalEntry[MockObject]
    obj = MockObject(datetime.date(2012, 10, 10), 'Description', 5)
    je = MockJournalEntry(date=obj.date, description=obj.description, source=obj)
    je.post(date=obj.date, account=ExpensesAccount, quantity=obj.Debits)

# Generated at 2022-06-14 04:13:25.098267
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    from .journaling import JournalEntry
    from .zeitgeist import DateRange

    ## Arrange:
    je = JournalEntry(date = '2018/10/10', description = 'Test of method post')

    ## Act:
    je.post('2018/10/10', Account(type = "ASSETS", name = "Test CASH account"), -100)

    ## Assert:
    assert je.date.is_overlapping(DateRange('2018/10/10'))



# Generated at 2022-06-14 04:13:35.057788
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from ..commons.numbers import Amount
    from .accounts import Account, AccountType

    acc1 = Account(name="Account One", number="1", type=AccountType.EQUITIES)
    je = JournalEntry[str](date=date(2018, 1, 1), description="desc", source="src")
    je.post(date=date(2018, 1, 1), account=acc1, quantity=100)

    assert je.postings[0].is_debit

    je = JournalEntry[str](date=date(2018, 1, 1), description="desc", source="src")
    je.post(date=date(2018, 1, 1), account=acc1, quantity=-100)

    assert je.postings[0].is_credit


# Generated at 2022-06-14 04:13:41.023628
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry(datetime.date(2019, 12, 31), "Test", None)
    je.post(datetime.date(2019, 12, 31), Account("test_account", "Test Account", None, AccountType.ASSETS), Quantity(100))
    je.post(datetime.date(2019, 12, 31), Account("test_account", "Test Account", None, AccountType.REVENUES), Quantity(-100))
    je.validate()

# Generated at 2022-06-14 04:13:51.605161
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_journals(period: DateRange) -> Iterable[JournalEntry[str]]:
        return [JournalEntry(datetime.date(2019, 5, 12), "Test", "Test")]

    assert read_journals(None) is not None
    assert read_journals(DateRange.all()) is not None
    assert read_journals(DateRange(None, None)) is not None


# Generated at 2022-06-14 04:13:58.739464
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime
    from ..commons.numbers import Quantity
    from .accounts import Account, AccountType

    je = JournalEntry[int].__new__(JournalEntry[int])
    je.date = datetime.date.today()
    je.description = "Test Journal Entry"
    je.source = 123
    je.postings = []

    je.post(datetime.date.today(), Account(AccountType.ASSETS, "Bank"), Quantity(100))
    je.post(datetime.date.today(), Account(AccountType.EXPENSES, "Rent"), Quantity(-100))
    je.validate()
    print("Journal Entry: ", je)

# Generated at 2022-06-14 04:14:10.672480
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .fixtures import JournalEntry_with_posting
    from decimal import Decimal
    from dataclasses import asdict

    journal = JournalEntry_with_posting()

    assert asdict(journal) == asdict(
        JournalEntry_with_posting(postings=[
            Posting(journal=JournalEntry_with_posting(), date=journal.date, account=Account("sales", AccountType.REVENUES), direction=Direction.INC, amount=Amount(Decimal("12.34"))),
            Posting(journal=JournalEntry_with_posting(), date=journal.date, account=Account("inventory", AccountType.ASSETS), direction=Direction.INC, amount=Amount(Decimal("12.34"))),
        ])
    )

# Generated at 2022-06-14 04:14:16.357726
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account
    from .commons import test_commons

    ass = Account.ASSETS.label(test_commons.any_string(), AccountType.EQUITIES)
    inc = Account.INCOMES.label(test_commons.any_string(), AccountType.REVENUES)
    exp = Account.EXPENSES.label(test_commons.any_string(), AccountType.EXPENSES)
    equ = Account.EQUITIES.label(test_commons.any_string(), AccountType.EQUITIES)
    rev = Account.REVENUES.label(test_commons.any_string(), AccountType.REVENUES)
    exp = Account.EXPENSES.label(test_commons.any_string(), AccountType.EXPENSES)

# Generated at 2022-06-14 04:14:27.486240
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j1 = JournalEntry(datetime.date(2020, 8, 8), 'j1', None).post(datetime.date(2020, 8, 8), Account('A', AccountType.ASSETS, 'Equity'), Quantity(100)).post(datetime.date(2020, 8, 8), Account('B', AccountType.EQUITIES, 'Equity'), Quantity(-100))
    j2 = JournalEntry(datetime.date(2020, 8, 8), 'j2', None).post(datetime.date(2020, 8, 8), Account('A', AccountType.ASSETS, 'Equity'), Quantity(100)).post(datetime.date(2020, 8, 8), Account('B', AccountType.EQUITIES, 'Equity'), Quantity(-101))

# Generated at 2022-06-14 04:14:39.320428
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..bookends.books import Book
    from ..bookends.journal import Journal
    from ..bookends.ledgers import Ledger
    from .accounts import Chart
    
    # Arrange
    book = Book("Test Journal")
    journal = Journal(book)
    ledger = Ledger(book)
    chart = Chart()
    
    journal_entry = JournalEntry(datetime.date(2018,12,31), 'Test', 'Source')
    test_account_id = Guid.parse('ec5fea58-28d7-4e1a-ad7a-5f5267c711fd')
    test_account = Account(test_account_id, 'Test Account', AccountType.ASSETS, chart)
    
    # Act

# Generated at 2022-06-14 04:14:43.765323
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    a = JournalEntry(datetime.date(2020, 1, 1), "hi", 1)
    a.post(datetime.date(2020, 1, 1), Account('a1'), 100)
    a.post(datetime.date(2020, 1, 1), Account('a2'), -100)
    a.validate()

# Generated at 2022-06-14 04:14:50.374415
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account
    from . import products
    from . import products
    from . import customers
    from . import revenues
    from . import expenses
    from . import income_taxes
    journal = JournalEntry[products.Product]()


    journal.date = datetime.date.today()
    journal.description = "Product sales"
    journal.source = products.Product("Coke", price = Amount(1.0), cost = Amount(0.5))
    journal.post(datetime.date.today(), Account.REVENUES, Amount(1.0))
    journal.post(datetime.date.today(), Account.EXPENSES, Amount(1.0))


    journal.validate()

# Generated at 2022-06-14 04:15:01.057299
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import unittest
    from dataclasses import MISSING
    from typing import Generic, TypeVar

    from ..commons.zeitgeist import DateRange, today

    from .accounts import AccountType, Assets, Cash

    from .postings import Direction

    #: Declares a type variable.
    _T = TypeVar("_T")

    @dataclass(frozen=True)
    class _JournalEntry(Generic[_T]):
        """
        Provides a journal entry model.
        """

        #: Date of the entry.
        date: datetime.date

        #: Description of the entry.
        description: str

        #: Business object as the source of the journal entry.
        source: _T

        #: Postings of the journal entry.

# Generated at 2022-06-14 04:15:11.937249
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry[None](datetime.date(2018, 1, 1), "Desc", None)
    je2 = je.post(datetime.date(2018, 1, 1), Account(AccountType.ASSETS, "A"), 100)
    je2.validate()
    je2 = je.post(datetime.date(2018, 1, 1), Account(AccountType.ASSETS, "A"), -100)
    je2.validate()
    je2 = je.post(datetime.date(2018, 1, 1), Account(AccountType.ASSETS, "A"), 50) \
        .post(datetime.date(2018, 1, 1), Account(AccountType.ASSETS, "A"), 50)
    je2.validate()

# Generated at 2022-06-14 04:15:25.930643
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class _ReadJournalEntriesImpl(_T):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return None

    ReadJournalEntries(_ReadJournalEntriesImpl())

# EOF

# Generated at 2022-06-14 04:15:26.527396
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    assert True

# Generated at 2022-06-14 04:15:34.965019
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from decimal import Decimal
    from ..model.accounts import Account, AccountType
    from ..model.journals import Direction, JournalEntry
    from ..commons.numbers import Quantity

    je_1 = JournalEntry(datetime.date, 'description', 'source')
    a_1 = Account('A1', AccountType.REVENUES)
    a_2 = Account('A2', AccountType.EXPENSES)
    je_1.post(datetime.date, a_1, Quantity(Decimal(5)))
    je_1.post(datetime.date, a_2, Quantity(Decimal(-5)))
    assert list(je_1.increments) == [Posting(je_1, datetime.date, a_1, Direction.INC, Amount(Decimal(5)))]

# Generated at 2022-06-14 04:15:43.097935
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    account1 = Account("Checking", AccountType.ASSETS)
    account2 = Account("Insurance", AccountType.EXPENSES)
    journal = JournalEntry(datetime.date.today(), "Salary", None)
    journal.post(datetime.date.today(), account1, Amount(3500))
    journal.post(datetime.date.today(), account2, Amount(500))

    journal.validate()

    # Will throw AssertionError
    # journal.post(datetime.date.today(), account1, Amount(3500))
    # journal.validate()

# Generated at 2022-06-14 04:15:47.671382
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    entry = JournalEntry[None](datetime.date.today(), "test", None)
    entry.post(datetime.date.today(), Account("Assets", AccountType.ASSETS, None), 1)
    entry.post(datetime.date.today(), Account("Revenues", AccountType.REVENUES, None), -1)
    entry.validate()

# Generated at 2022-06-14 04:15:56.261537
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account
    asset = Account(name="Cash", type = AccountType.ASSETS)
    revenue = Account(name="Fees", type = AccountType.REVENUES)
    expense = Account(name="Supplies", type = AccountType.EXPENSES)
    date = datetime.date.today()
    description = "abc"
    source = "abc"
    journal_entry = JournalEntry(date, description, source)
    journal_entry.post(date, asset, 1000)
    journal_entry.post(date, revenue, 200)
    journal_entry.post(date, expense, 200)
    journal_entry.validate()

# Generated at 2022-06-14 04:16:07.178005
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from typing import Any
    import pytest
    from datetime import date
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class _T:
        pass

    @dataclass(frozen=True)
    class _U:
        pass

    @dataclass(frozen=True)
    class _V:
        pass

    def _f() -> Iterable[JournalEntry[Any]]:
        yield JournalEntry(date(2014, 1, 1), "", _T())
        yield JournalEntry(date(2014, 1, 2), "", _U())
        yield JournalEntry(date(2015, 1, 1), "", _V())


# Generated at 2022-06-14 04:16:10.866296
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from unittest import mock

    with mock.patch.object(DateRange, "__init__", return_value=None) as mock_init_:
        mock_init_.assert_not_called()
        # Do something here
    mock_init_.assert_called_once_with(datetime.date(2020, 1, 1), datetime.date(2020, 1, 31))

# Generated at 2022-06-14 04:16:21.074415
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .persistence import inmemory_journal_repo
    from .samples import sample_journal_entry_from_invoice, sample_invoice
    from .transactions import submit_journal_entry, TransactionContext

    # Prepare:
    repo = inmemory_journal_repo()
    journal = sample_journal_entry_from_invoice(sample_invoice())

    # Test:
    journal.post(date=journal.date, account=Account(AccountType.ASSETS, "1"), quantity=1)
    journal.post(date=journal.date, account=Account(AccountType.EXPENSES, "1"), quantity=1)
    journal.post(date=journal.date, account=Account(AccountType.EXPENSES, "1"), quantity=-1)

    # Submit and verify:

# Generated at 2022-06-14 04:16:31.941884
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from ..commons.numbers import Amount, Quantity

    ## Declare test variables
    a_date = datetime.date(2019, 12, 31)
    a_description = 'sample description'
    a_business_object = 'a business object'
    some_postings = []
    an_account = Account(1, 'Testaccount', AccountType.ASSETS)
    a_posting = Posting(JournalEntry(a_date, a_description, a_business_object, some_postings), a_date, an_account, Direction.DEC, Amount(Quantity(1)))
    a_journal_entry = JournalEntry(a_date, a_description, a_business_object, some_postings)
    
    ## Run the post method

# Generated at 2022-06-14 04:16:52.654521
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from . import accounts
    from .accounts import Account, AccountType

    expense_account = Account("Expense", AccountType.EXPENSES)
    revenue_account = Account("Revenue", AccountType.REVENUES)
    asset_account = Account("Asset", AccountType.ASSETS)
    liability_account = Account("Liability", AccountType.LIABILITIES)
    equity_account = Account("Equity", AccountType.EQUITIES)
    asset = accounts.Asset.make(1, "ASSET", asset_account, Amount(100), DateRange.of(30))
    #liability = accounts.Liability.make(2, "LIABILITY", liability_account, Amount(100), DateRange.of(30))

# Generated at 2022-06-14 04:16:58.495034
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    class B:
        pass
    a = JournalEntry(datetime.date(2018,1,1), "", B())
    a = a.post(datetime.date(2018,1,1), Account("a"), 10)
    a = a.post(datetime.date(2018,1,1), Account("b"), -10)
    a = a.post(datetime.date(2018,1,1), Account("c"), 0)
    a.validate()
    print("test_JournalEntry_post: ", a)


# Generated at 2022-06-14 04:16:59.057833
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:17:06.379729
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    account_ABC = Account(name="ABC", type_=AccountType.ASSETS)
    amount_100 = Quantity(100)

    entry = JournalEntry[None](datetime.date(2020, 1, 1), "Test", None)
    entry = entry.post(datetime.date(2020, 1, 1), account_ABC, amount_100)

    assert entry.postings[0].account == account_ABC
    assert entry.postings[0].amount == amount_100
    assert entry.postings[0].direction == Direction.INC
    assert entry.postings[0].is_debit

# Generated at 2022-06-14 04:17:12.529339
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def journalReader(period: DateRange):
      return [
          JournalEntry(datetime.date(2019, 4, 1), "Description 3", None),
          JournalEntry(datetime.date(2019, 4, 2), "Description 4", None)
      ]

    assert list(journalReader(DateRange.all)) == [
        JournalEntry(datetime.date(2019, 4, 1), "Description 3", None),
        JournalEntry(datetime.date(2019, 4, 2), "Description 4", None)
    ]

# Generated at 2022-06-14 04:17:18.939771
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    JE = JournalEntry(date=datetime.date(2020, 6, 15), description="test")
    account = Account("test", AccountType.ASSETS)
    JE.post(datetime.date(2020, 6, 15), account, Amount(500))
    assert JE.postings[0].direction == Direction.INC
    assert JE.postings[0].account == account
    assert JE.postings[0].amount == Amount(500)

# Generated at 2022-06-14 04:17:22.414289
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    print("Executing test_JournalEntry_post...")
    account = Account('InterestOnSavings', AccountType.REVENUES)
    jentry = JournalEntry(datetime.date(2020, 1, 25), "Interest on savings for Jan'20", account, [])
    jentry.post(datetime.date(2020, 1, 31), account, 100)
    for posting in jentry.postings:
        print(posting)
    print()

test_JournalEntry_post()

# Generated at 2022-06-14 04:17:28.145204
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Setup test data
    account = Account("A", AccountType.ASSETS)
    account2 = Account("A2", AccountType.EXPENSES)
    journalEntry = JournalEntry("A","B")
    journalEntry.post(datetime.date(2020, 5, 26), account, 1)
    journalEntry.post(datetime.date(2020, 5, 26), account2, -1)

    assert journalEntry.postings[0].amount == 1

# Generated at 2022-06-14 04:17:36.348579
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account

    ass1 = Account(AccountType.ASSETS, "100", "10000")
    j1 = JournalEntry(datetime.datetime.now().date(), "a", "", [])
    j2 = j1.post(datetime.datetime.now().date(), ass1, 10)
    j3 = j2.post(datetime.datetime.now().date(), ass1, 40)
    j4 = j3.post(datetime.datetime.now().date(), ass1, -50)
    assert j4._postings[-1].amount == Quantity(10)

# Generated at 2022-06-14 04:17:44.083790
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import now

    class DummyEntry(JournalEntry[None]):
        pass

    dummy_journal_entry_1 = DummyEntry(now().minus(days=3), "dummy description 1", None)
    dummy_journal_entry_2 = DummyEntry(now().minus(days=2), "dummy description 2", None)
    dummy_journal_entry_3 = DummyEntry(now().minus(days=1), "dummy description 3", None)

    class DummyReader(ReadJournalEntries[None]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[None]]:
            return [dummy_journal_entry_1, dummy_journal_entry_2, dummy_journal_entry_3]


# Generated at 2022-06-14 04:18:18.533067
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Sample Data to be used in Class JournalEntry
    date = datetime.date(2020, 9, 1)
    account1 = Account("101", "Income", AccountType.REVENUES)
    account2 = Account("102", "Expense", AccountType.EXPENSES)
    amount1 = Amount(2000)
    amount2 = Amount(1000)
    # Expected Result of posting for debit and credit
    expected_result = [
        Posting(journal=None, date=date, account=account1, direction=Direction.INC, amount=amount1),
        Posting(journal=None, date=date, account=account2, direction=Direction.DEC, amount=amount2),
    ]
    # Creating Instance of JournalEntry
    journal_entry = JournalEntry[int]
    # Posting the data on Journal Entry
    journal

# Generated at 2022-06-14 04:18:26.178080
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .events import JournalEntry
    from .events import Posting

    # Arrange
    journal = JournalEntry('01/01/2019', "", "")

    # Act
    journal.post(journal.date, Account("1234", AccountType.ASSETS, '', ''), 1)

    # Assert
    assert len(journal.postings) == 1
    assert isinstance(journal.postings[0], Posting)



# Generated at 2022-06-14 04:18:35.547314
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType, TransactionType

    # JournalEntry
    je = JournalEntry(datetime.datetime.now().date(),"Achat de Farine","GRUAU")
    # Create Account

    a = Account('6540', AccountType.ASSETS, TransactionType.BOTH, "Achats")
    b = Account('4111', AccountType.EXPENSES, TransactionType.CREDIT, "Frais Bancaires")
    c = Account('1234', AccountType.REVENUES, TransactionType.DEBIT, "Frais Généraux")

    je.post(datetime.datetime.now().date(),a,100)
    je.post(datetime.datetime.now().date(),b,100)
    je.post(datetime.datetime.now().date(),c,-100)

   

# Generated at 2022-06-14 04:18:40.258211
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    '''
    Test for method validate of class JournalEntry
    '''
    journal = JournalEntry(datetime.date(2020, 1, 1), 'Test', None)
    journal.post(datetime.date(2020, 1, 1), Account('A', AccountType.ASSETS), 100)
    journal.validate()

# Generated at 2022-06-14 04:18:41.469051
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass


# unit test for method post of class JournalEntry

# Generated at 2022-06-14 04:18:47.124097
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    date = datetime.date(2020, 5, 4)
    source = "test source"
    description = "test description"

    account1 = Account("test-asset-account-1", description="", type=AccountType.ASSETS, is_operational=True)
    account2 = Account("test-expense-account-1", description="", type=AccountType.EXPENSES, is_operational=True)

    j = JournalEntry(date, description, source)
    j.post(date, account1, Quantity(10))
    j.post(date, account2, Quantity(-10))
    j.validate()

# Generated at 2022-06-14 04:18:55.569988
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountType
    from .business_objects import Entity
    from .journal_entries import JournalEntry

    class MockReadJournalEntries(ReadJournalEntries[Entity]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[Entity]]:
            return (JournalEntry(date=datetime.date(2020, 1, 1), description="Dummy Journal Entry", source=Entity()),)

    account = Account(type=AccountType.ASSETS, name="Bank")
    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 2))

    journal_entry = MockReadJournalEntries()(period=period)[0]
    assert journal_entry.date == period.start

# Generated at 2022-06-14 04:19:02.685285
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType
    from .ledger_file import LedgerFile
    from .ledger_file_service import LedgerFileService
    from .transactions import Transaction

    ## Configure:
    acc_recv = Account("100", "Accounts Receivable", AccountType.ASSETS)
    acc_sales = Account("200", "Sales", AccountType.REVENUES)
    acc_com_income = Account("300", "Commission Income", AccountType.REVENUES)

    ## Run exercise:
    journal = JournalEntry(datetime.date(2019, 1, 30), "Sales", Transaction("T1001", "XYZ Corp.", datetime.date(2019, 1, 30)))
    journal.post(journal.date, acc_recv, +100)

# Generated at 2022-06-14 04:19:06.283421
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class ReadJournalEntriesStub(ReadJournalEntries[str]):
        def __call__(self, *args, **kwargs):
            pass

    object = ReadJournalEntriesStub()
    assert object is not None



# Generated at 2022-06-14 04:19:13.121126
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..accounts.accounts import Account, AccountType

    @dataclass(frozen=True)
    class eTrans(Generic[_T]):
        pass

    journal = JournalEntry[eTrans]

    je = JournalEntry[eTrans](date=datetime.date(2019, 1, 1), description="Test")
    je.post(
        datetime.date(2019, 1, 1),
        Account(AccountType.ASSETS, "Cash in Bank"),
        +1000,
    )
    je.post(
        datetime.date(2019, 1, 1),
        Account(AccountType.REVENUES, "Equipment Sales"),
        -1000,
    )
    je.validate()

# Generated at 2022-06-14 04:20:39.472898
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Tests method post of class JournalEntry.
    """

    class DummySource:

        def __init__(self):
            self.inc_acc1 = Account("IncAcc1", "IncAcc1", AccountType.ASSETS)
            self.inc_acc2 = Account("IncAcc2", "IncAcc2", AccountType.REVENUES)
            self.date = datetime.date(2019, 1, 1)

        def inc_postings(self):
            """
            Returns journal entry instance with increment postings.
            """

            # Declare journal entry:
            journ = JournalEntry[DummySource](self.date, "Inc Postings", self)

            # Post to accounts:
            journ.post(self.date, self.inc_acc1, +45)

# Generated at 2022-06-14 04:20:50.925295
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():

    amount = Amount(1)
    date = datetime.date(2020, 1, 1)
    accountType = AccountType.ASSETS
    accountName = "Assets"
    description = "Dummy entry"
    guid = Guid("00000000-0000-0000-0000-000000000000")
    quantity = Quantity(1)

    posting = Posting(JournalEntry, date, Account(accountName, accountType), Direction.INC, amount)

    assert posting.date == date
    assert str(posting.account) == accountName
    assert posting.account.type == accountType
    assert posting.direction == Direction.INC
    assert posting.amount == amount
    assert posting.is_debit == True
    assert posting.is_credit == False

    journalEntry = JournalEntry(date, description, JournalEntry)

# Generated at 2022-06-14 04:21:03.337473
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
  from .accounts import make_account
  from .currencies import make_currency
  JournalEntry.debits = 0
  JournalEntry.credits = 0
  JournalEntry.date = 0
  JournalEntry.description = 0
  JournalEntry.postings = [Posting(JournalEntry,0,make_account("1","1","1"),Direction.DEC,10),Posting(JournalEntry,0,make_account("1","1","1"),Direction.DEC,20),Posting(JournalEntry,0,make_account("1","1","1"),Direction.DEC,35)]
  JournalEntry.postings[0].amount = 10
  JournalEntry.postings[1].amount = 20
  JournalEntry.postings[2].amount = 35
  JournalEntry.guid = 0
  JournalEntry.validate()

# Generated at 2022-06-14 04:21:04.134720
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:21:11.255989
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    class Obj:
        pass
    Obj1 = Obj()
    Obj2 = Obj()
    # Test 1 - Pass
    je = JournalEntry(datetime.date.today(), 'Test Entry for validate method', Obj1)
    je.post(datetime.date.today(), None, 200).validate()
    je.post(datetime.date.today(), None, -200).validate()
    # Test 2 - Pass
    j1 = je.post(datetime.date.today(), None, 200)
    j2 = je.post(datetime.date.today(), None, -200)
    j1.validate()
    j2.validate()
    # Test 3 - Pass
    je.post(datetime.date.today(), None, 200).validate()

# Generated at 2022-06-14 04:21:16.357861
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from abc import ABC, abstractmethod

    class _Impl(ReadJournalEntries[str]):
        @abstractmethod
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[str]]:
            pass

    _Impl.__abstractmethods__