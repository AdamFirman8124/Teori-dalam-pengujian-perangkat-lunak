

# Generated at 2022-06-14 04:11:31.395152
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # TODO: This can be part of tests of `Posting` dataclass.
    from .accounts import create_account

    from dataclasses import asdict

    from .taxes import FlatFIT, FlatSIT
    from .currencies import Currency, CurrencyAccount

    #: Create a dummy currency.
    USD = Currency("USD", "US Dollar", "USD")

    #: Create accounts for Assets and Expenses.
    ACC_A_USD = create_account(USD, "A.USD", AccountType.ASSETS)
    ACC_E_USD = create_account(USD, "E.USD", AccountType.EXPENSES)

    #: Create a dummy Income Tax regime.
    REG_TAX_INCOME = FlatSIT(USD, "Taxable Income", "", "", "", "", "", "", "")



# Generated at 2022-06-14 04:11:42.388579
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from .sources import JournalEntrySource
    from .sources import InMemoryJournalEntrySource
    from .sources.conventions import Business

    # Creating a journal entry source:
    source = InMemoryJournalEntrySource()
    journal_entry_source = JournalEntrySource(source, Business)

    # Creating a journal entry:
    source.add(
        date(2019, 9, 1),
        "This is a journal entry.",
        journal_entry_source.journals.purchases.create(date(2019, 9, 1)),
    )

    # Creating a read function:
    read_journal_entries = ReadJournalEntries.__getitem__(Business, int)

    # Asserting isinstance:
    assert isinstance(read_journal_entries, ReadJournalEntries)

# Generated at 2022-06-14 04:11:54.019467
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .books import Book
    from .constants import SystemAccount
    from .ledger import Ledger
    from .transactions import Transaction

    book = Book.at(datetime.date(2018, 4, 1))

    ledger = Ledger.of(book, _get_accounts(book))

    with ledger.handle() as l:

        l.start(Transaction.of(book, "Closing")).post(
            date=book.date,
            account=SystemAccount.RETAINED_EARNINGS,
            amount=100,
        ).complete()


# Generated at 2022-06-14 04:11:57.400170
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_journals(period: DateRange) -> Iterable[JournalEntry[None]]:
        return []
    assert read_journals

# Generated at 2022-06-14 04:11:59.465845
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Create an JournalEntry
    je = JournalEntry(datetime.date.today(), "Description", "Source")
    assert je.validate() is None

# Generated at 2022-06-14 04:12:06.644066
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .demo.domain.v1.accounts import Accounts
    from .demo.domain.v1.sales import Sale

    demo_accounts = Accounts()

    sale = Sale(date=datetime.date(2020,1,1), number="S-2020-01-01-0001", amount=100)

    entry = JournalEntry[Sale]()
    entry.date = datetime.date(2020, 1, 1)
    entry.description = "Test"
    entry.source = sale

    entry.post(date=datetime.date(2020,1,1), account=demo_accounts.cash, quantity=100)
    entry.post(date=datetime.date(2020,1,1), account=demo_accounts.sales, quantity=-100)

    assert entry.validate() is None

# Generated at 2022-06-14 04:12:11.161431
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountType

    @dataclass(frozen=True)
    class StubObject:
        pass

    @dataclass(frozen=True)
    class StubAccount(Account):
        pass

    stub_object = StubObject()

    def _journal_entry(id: str, date: datetime.date) -> JournalEntry[StubObject]:
        journal_entry = JournalEntry[StubObject](date, f"Description for journal entry {id}", stub_object)
        journal_entry.post(date, StubAccount("ID1", AccountType.REVENUES), 100)
        journal_entry.post(date, StubAccount("ID2", AccountType.EXPENSES), 50)
        journal_entry.post(date, StubAccount("ID3", AccountType.EXPENSES), 50)
        return journal_entry



# Generated at 2022-06-14 04:12:23.283959
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    ## Setup:
    # Create source for journal entry
    source = "Test source"

    # Create account 1
    account1 = Account(
        guid=makeguid(),
        name="Test account 1",
        type=AccountType.ASSETS,
        description="Test account 1"
    )

    # Create account 2
    account2 = Account(
        guid=makeguid(),
        name="Test account 2",
        type=AccountType.EXPENSES,
        description="Test account 2"
    )

    # Create journal entry
    journal_entry = JournalEntry(
        date=datetime.date.today(),
        description="Test journal entry",
        source=source,
        postings=[],
        guid=makeguid(),
    )

    ## Validate:

# Generated at 2022-06-14 04:12:31.967183
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry[str]('2020-01-01', 'Test', 'Source')
    je.post('2020-01-01', Account('Asset1', 'Assets'), 1)
    je.post('2020-01-01', Account('Revenue1', 'Revenues'), -1)
    je.validate() # Should not raise any exception

    je = JournalEntry[str]('2020-01-01', 'Test', 'Source')
    je.post('2020-01-01', Account('Asset1', 'Assets'), 1)
    je.post('2020-01-01', Account('Revenue1', 'Revenues'), 1)
    try:
        je.validate()
        assert False
    except AssertionError:
        assert True

# Generated at 2022-06-14 04:12:44.344174
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from . import ChartOfAccounts
    from .ledgers import Ledger

    coa = ChartOfAccounts()

    l: Ledger[str] = {}

    j1 = JournalEntry[str](date=datetime.date.today(), description="Calculate revenues", source="Revenue event")
    j1.post(date=datetime.date.today(), account=coa.get("Cash"), quantity=100)
    j1.post(date=datetime.date.today(), account=coa.get("Revenues"), quantity=-100)

    j1.validate()

    l["J1"] = j1

    assert l["J1"].postings[0].direction == Direction.INC
    assert l["J1"].postings[1].direction == Direction.DEC

   

# Generated at 2022-06-14 04:12:56.978918
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    print("Testing class JournalEntry, method validate")

    # Setting up test data
    journal_entry_valid = JournalEntry(date=datetime.date(2020, 2, 1), description='valid', source=None)
    journal_entry_invalid = JournalEntry(date=datetime.date(2020, 2, 1), description='valid', source=None)

    journal_entry_valid.post(date=datetime.date(2020, 2, 1), account=Account(name='account1', account_type=AccountType.ASSETS), quantity=10)
    journal_entry_valid.post(date=datetime.date(2020, 2, 1), account=Account(name='account2', account_type=AccountType.EQUITIES), quantity=-10)


# Generated at 2022-06-14 04:12:57.651961
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:13:07.879590
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():

    """
    Test that 'validate' method of class JournalEntry returns AssertionError when the journal
    entry is inconsistent.
    """

    # Define an account to post the amount to
    account = Account('TestAccount', 'TestSubAccount', 'TestAccountType')

    # Define an event to post to the account
    event = JournalEntry(datetime.date(2016, 1, 1), 'TestEvent', account)

    # Post an event to the account
    event.post(datetime.date(2016, 1, 1), account, 0)

    # Try to validate the event
    try:
        event.validate()
    except AssertionError:
        return
    raise RuntimeError("The event should be inconsistent")

# Generated at 2022-06-14 04:13:17.149822
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import dataclass, field
    from typing import List
    from unittest import TestCase
    from .accounts import Account
    class MyCase(TestCase):
        def setUp(self):
            @dataclass
            class Data:
                identifier: str
            @dataclass
            class Config:
                source: List[Data] = field(default_factory=list)
            self.config = Config()
            self.source = self.config.source
            self.subject = ReadJournalEntries
        def test_returns_empty_iterable_when_empty(self):
            actual = self.subject(self.config)(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 1)))
            self.assertEqual(len(actual), 0)

# Generated at 2022-06-14 04:13:30.208691
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Setup
    class Product:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    def read_entries(period: DateRange) -> Iterable[JournalEntry[Product]]:
        p1 = Product(1, 'Product 1')
        p2 = Product(2, 'Product 2')


# Generated at 2022-06-14 04:13:30.712569
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:13:39.603502
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Validation test for journal entry
    """
    with pytest.raises(AssertionError):
        je = JournalEntry[str](date=date(2020,1,1), description='Sample', source='Sample')
        je.post(date(2020,1,1), account=Account(code='10100', name='Cash', type=AccountType.ASSETS), quantity=100)
        je.post(date(2020,1,1), account=Account(code='20100', name='Sales', type=AccountType.REVENUES), quantity=100)
        je.validate()

# Generated at 2022-06-14 04:13:50.668163
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from .parties import Party, Parties
    from .invoices import Invoice, SalesInvoices, PurchaseInvoices

    parties = Parties()
    sales_invoices = SalesInvoices()
    purchases_invoices = PurchaseInvoices()

    @dataclass(frozen=True)
    class When(object):
        pass

    # def test_JournalEntry_post(self):
    when = When()
    # GIVEN some parties
    bill = parties.add(Party("Bill"))
    amit = parties.add(Party("Amit"))
    # AND some invoice

# Generated at 2022-06-14 04:13:51.235960
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass


# Unit test

# Generated at 2022-06-14 04:13:57.357127
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Exercise:
    j = JournalEntry(
        datetime.date(2020, 6, 11),
        "Test Journal Entry",
        "Source"
    ).post(datetime.date(2020, 6, 11), Account("A", "Assets Account", AccountType.ASSETS), +100.50) \
            .post(datetime.date(2020, 6, 11), Account("E", "Equities Account", AccountType.EQUITIES), -50.25)

    # Verify:
    j.validate()

# Generated at 2022-06-14 04:14:31.767855
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .company import Company
    from .currencies import Currency, USD
    from .ledgers import Ledger
    from .products import Service

    ## Setup:
    company: Company[Service] = Company("ACME", USD)
    ledger: Ledger = Ledger("Main Ledger")
    ledger.add_account(Account("Cash", AccountType.ASSETS))
    ledger.add_account(Account("Sales", AccountType.REVENUES))
    ledger.add_account(Account("Inventory", AccountType.ASSETS))
    ledger.add_account(Account("COGS", AccountType.EXPENSES))
    journal: JournalEntry[Service] = JournalEntry(datetime.date.today(), "Test Journal Entry", company)

    #: Execute:

# Generated at 2022-06-14 04:14:36.909898
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons import Quantity
    from . import accounts
    journal= JournalEntry("2019-03-10", "test journal entry", "source")
    journal.post("2019-03-10", accounts.Account("Assets", accounts.AccountType.ASSETS), Quantity("10"))
    journal.validate()

# Generated at 2022-06-14 04:14:47.175874
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from decimal import Decimal
    from dataclasses import asdict
    from .accounts import Account, AccountType
    from .accounts.books import AccountTree, TEST_ACCOUNTS_MAP
    from .commons.numbers import Quantity
    from .commons.others import mock_datetime
    from .transaction import Transaction
    from .transaction.books import TransactionTree
    from .transaction.dsl import begin, source, post, commit
    
    # Setup:
    mock_datetime(2020, 5, 1, 15, 0, 0)
    acc_tree = AccountTree(TEST_ACCOUNTS_MAP)
    trans_tree = TransactionTree()
    rjes: ReadJournalEntries[Transaction] = trans_tree.read_journal_entries

    # Note:
    # * Test `TransactionTree.read_

# Generated at 2022-06-14 04:14:58.558635
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    ## Create a journal entry for testing
    # Create "example" source business object
    class Example:
        def __init__(self, id):
            self.id = id
    example_source_obj1 = Example(1)
    example_source_obj2 = Example(2)
    # Create cash account
    cash_account = Account(1, "Cash", AccountType.ASSETS)
    # Create journal entry for testing
    journal_entry_test1 = JournalEntry(datetime.date.today(), "test1", example_source_obj1)
    journal_entry_test1.post(datetime.date.today(), cash_account, 1000)
    journal_entry_test1.post(datetime.date.today(), cash_account, -1000)

# Generated at 2022-06-14 04:15:05.309702
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal = JournalEntry(datetime.date.today(), "description", "")
    journal.post(datetime.date.today(), Account("account"), Quantity(10))
    journal.validate()
    assert journal.postings[0].amount == Amount(10)
    assert journal.postings[0].direction == Direction.INC
    assert journal.postings[0].is_credit == False
    assert journal.postings[0].is_debit == True

# Generated at 2022-06-14 04:15:06.911544
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    _f = lambda period: []
    assert isinstance(_f, ReadJournalEntries)

# Generated at 2022-06-14 04:15:14.654226
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.zeitgeist import DateRange
    from .accounts import Accounts
    from .data import make_journal_entries_from_ledger, read_ledger
    from .ledger import get_transactions

    accounts = Accounts()
    budget_account = accounts.add("test", AccountType.REVENUES, "test", "testing")
    journal_entries = make_journal_entries_from_ledger(accounts, read_ledger(get_transactions("test/sample_ledger.dat")))
    assert all(len(journal_entry.postings) >= 2 for journal_entry in journal_entries)
    assert all(journal_entry.source is not None for journal_entry in journal_entries)
    assert all(journal_entry.guid != "" for journal_entry in journal_entries)


# Generated at 2022-06-14 04:15:17.573018
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    rje = ReadJournalEntries(period)
    rje.check_type(Iterable[JournalEntry[_T]])


# Generated at 2022-06-14 04:15:22.814760
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    #setup
    journal = JournalEntry('2020-09-17', 1, 1)
    journal.post('2020-09-17', Account("JE", AccountType.ASSETS, "journal entry", None), 1)
    journal.post('2020-09-17', Account("JE", AccountType.EQUITIES, "journal entry", None), -1)
    #assert
    journal.validate()

# Generated at 2022-06-14 04:15:25.709072
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_entries(period: DateRange) -> Iterable[JournalEntry[str]]:
        ...
    assert issubclass(type(read_entries), ReadJournalEntries)

# Generated at 2022-06-14 04:15:49.129171
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import dataclass
    from .accounts import Account, AccountType

    @dataclass()
    class Source:
        pass

    j1 = JournalEntry(
        datetime.date(year=2000, month=1, day=1),
        "JE1",
        Source(),
        [
            Posting(j1, datetime.date(year=2000, month=1, day=1), Account(AccountType.ASSETS, "Bank"), Direction.INC, Amount(100)),
            Posting(j1, datetime.date(year=2000, month=1, day=1), Account(AccountType.REVENUES, "Deposit"), Direction.DEC, Amount(100)),
        ],
    )

# Generated at 2022-06-14 04:15:59.829045
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():

    from .accounts import account_of
    
    # Journal entry setup:
    account_cash = account_of("Cash",AccountType.ASSETS)
    account_ap = account_of("Accounts Payable",AccountType.LIABILITIES)
    account_to_invest = account_of("To Invest",AccountType.EQUITIES)
    account_overtime_salary = account_of("Overtime Salary",AccountType.EXPENSES)
    account_intrest_income = account_of("Intrest Income",AccountType.REVENUES)

    # Construct JournalEntry:
    from datetime import date
    journal_entry = JournalEntry[str](description="Adjust for Intrest Income and Salary paid for Overtime", source="", date=date(2019, 4, 6))

# Generated at 2022-06-14 04:16:07.814946
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from .accounts import AssetAccount, ExpenseAccount, EquityAccount

    entry = JournalEntry(date.today(), "Wages from Joe", None)

    entry.post(date.today(), AssetAccount("Cash"), -600)
    entry.post(date.today(), ExpenseAccount("Wages"), 600)

    entry.post(date.today(), EquityAccount("Capital"), 100)

    assert len(entry.postings) == 3

    print(entry)

    # Unit test for method validate of class JournalEntry
    entry.validate()



# Generated at 2022-06-14 04:16:08.349020
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:16:17.258588
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Test case 1
    j_entry = JournalEntry[int](date = datetime.date.today(), description = 'Test_Entry', source = 1)
    j_entry.post(date = datetime.date.today(), account = Account(type = AccountType.EQUITIES, name = 'Test_acc'), quantity = 1)
    assert len(j_entry.increments) == 1
    assert len(j_entry.decrements) == 0
    assert len(j_entry.debits) == 0
    assert len(j_entry.credits) == 1

# Generated at 2022-06-14 04:16:26.277666
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal_entry = JournalEntry[int](datetime.date.today(), "Test Journal Entry Posting", 0)
    assert len(journal_entry.postings) == 0
    journal_entry.post(datetime.date.today(), Account("Test Account", AccountType.ASSETS), -12)
    assert len(journal_entry.postings) == 1
    assert journal_entry.postings[0].account.name == "Test Account"
    assert journal_entry.postings[0].account.type == AccountType.ASSETS
    assert journal_entry.postings[0].amount == 12

# Generated at 2022-06-14 04:16:34.421773
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import replace
    from ..commons.zeitgeist import DateTimeSpan

    import pytest
    from typeguard import typechecked
    from .accounts import Account

    @typechecked
    def TestSource(value: int) -> TestSource:
        return TestSource(value)

    @dataclass(frozen=True)
    class TestSource:
        #: Test value.
        value: int

    @dataclass(frozen=True)
    class TestJournalEntry(JournalEntry[TestSource]):
        #: Test value.
        value: int = field(init=False)

        @property
        def source(self) -> TestSource:
            return TestSource(self.value)


# Generated at 2022-06-14 04:16:42.313059
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():

    # Given: A new instance of JournalEntry.
    je = JournalEntry(datetime.date(2019, 12, 31), "12/31", "")

    # When: Add posting with debit (increment).
    je.post(datetime.date(2019, 12, 31), Account("A-111", AccountType.ASSETS), 100)

    # And: Add posting with credit (decrement).
    je.post(datetime.date(2019, 12, 31), Account("E-111", AccountType.EQUITIES), -100)

    # Then: Total debits and credits should be equal.
    assert sum(posting.amount for posting in je.debits) == sum(posting.amount for posting in je.credits)

# Generated at 2022-06-14 04:16:45.601587
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    #pylint: disable=unused-argument
    def func(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return iter(())

    assert func.__name__ == "func"

# Generated at 2022-06-14 04:16:48.212538
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class _DefaultImplementation:

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    _DefaultImplementation()


# Generated at 2022-06-14 04:17:29.002658
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    ## Prepare:
    from datetime import date
    from .. import accounts
    journal = JournalEntry(date(2018, 10, 3), "Taxi fare", "Trip")
    journal.post(date(2018, 10, 3), accounts.CASH, +25)
    journal.post(date(2018, 10, 3), accounts.BANK, +25)
    journal.post(date(2018, 10, 3), accounts.FREIGHT, +25)

    ## Execute:
    journal.validate()

    ## Verify:
    assert True

# Generated at 2022-06-14 04:17:29.895965
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass
test_JournalEntry_post()

# Generated at 2022-06-14 04:17:31.579492
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass


# Generated at 2022-06-14 04:17:32.588475
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert "Not implemented"


# Generated at 2022-06-14 04:17:40.327306
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    je=JournalEntry(date=datetime.date(2020,1,1), description="First Entry", source="Java")
    je2=je.post(datetime.date(2020,1,1), account="Bank", quantity=1300)
    je3=je.post(datetime.date(2020,1,1), account="Cash", quantity=-1300)
    assert je3.credits is not None
    assert je3.debits is not None
    assert je3.postings is not None
    assert je3.postings[0].is_debit is True
    assert je3.postings[1].is_credit is True
    

# Generated at 2022-06-14 04:17:43.050570
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime as dt
    date1 = dt.date(2020, 7, 1)
    account1 = Account()
    quantity1 = 100
    j = JournalEntry[int](date1, '', 0)
    j.post(date1,account1,quantity1)

# Generated at 2022-06-14 04:17:53.688954
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import unittest

    from dataclasses import asdict
    from mydata.commons.zeitgeist import DateRange

    from .accounts import Account, AccountType

    ## Mock JournalEntry instances:
    @dataclass(frozen=True)
    class JournalEntry:
        pass

    journal_entries = [
        JournalEntry(),
        JournalEntry(),
    ]

    ## Mock functions:
    def _read_journal_entries(date_range: DateRange) -> Iterable[JournalEntry]:
        return journal_entries

    ## Test:
    read_journal_entries = ReadJournalEntries.__getitem__(
        (JournalEntry,),
        lambda: _read_journal_entries,
    )

# Generated at 2022-06-14 04:17:54.719985
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    x = ReadJournalEntries()
    assert x is not None and isinstance(x, Protocol)


# Generated at 2022-06-14 04:18:00.071183
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Create an arbitrary JournalEntry
    entry = JournalEntry(datetime.date(2020, 1, 1), "test", "test")

    # Create debit and credit accounts
    debit_account = Account(AccountType.ASSETS, "test")
    credit_account = Account(AccountType.EQUITIES, "test")

    # Add debit and credit postings
    entry.post(datetime.date(2020, 1, 1), debit_account, Quantity(50))
    entry.post(datetime.date(2020, 1, 1), credit_account, Quantity(-50))

    # The entry should be inconsistent
    entry.validate()

    # Add an extra credit posting to balance the debits and credits
    entry.post(datetime.date(2020, 1, 1), debit_account, Quantity(-50))

    # The entry should be consistent

# Generated at 2022-06-14 04:18:10.789824
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    je = JournalEntry(date=datetime.date.today(), description="Testing")
    account = Account(type=AccountType.ASSETS, name="Test")
    je.post(date=datetime.date.today(), account=account, quantity=100)
    assert je.post(date=datetime.date.today(), account=account, quantity=100) == je
    assert je.guid != None
    assert je.source == None
    assert je.date == datetime.date.today()
    assert je.description == "Testing"
    assert je.increments != None
    assert je.decrements != None
    assert je.debits != None
    assert je.credits != None

if __name__ == "__main__":
    test_JournalEntry_post()

# Generated at 2022-06-14 04:19:34.135761
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    assert len(JournalEntry[str](datetime.datetime.now().date(), "Test Journal Entry", "source").post(datetime.datetime.now().date(), Account("Test Account"), 2).postings) == 1
    assert len(JournalEntry[str](datetime.datetime.now().date(), "Test Journal Entry", "source").post(datetime.datetime.now().date(), Account("Test Account"), 0).postings) == 0
    assert len(JournalEntry[str](datetime.datetime.now().date(), "Test Journal Entry", "source").post(datetime.datetime.now().date(), Account("Test Account"), -2).postings) == 1

# Generated at 2022-06-14 04:19:44.362899
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Simple journal entry
    j = JournalEntry[str]("2018-08-18", "description", "source")
    j.post("2018-08-18", Account("a1", AccountType.ASSETS, "Assets"), Amount(10))
    j.post("2018-08-18", Account("l1", AccountType.LIABILITIES, "Liabilities"), Amount(-10))
    assert j.postings[0].amount == Amount(10)
    assert j.postings[1].amount == Amount(10)

    # Debit and credit same amount
    j = JournalEntry[str]("2018-08-18", "description", "source")
    j.post("2018-08-18", Account("a1", AccountType.ASSETS, "Assets"), Amount(10))

# Generated at 2022-06-14 04:19:51.889775
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountData
    from .ledgers import Ledger

    ledger = Ledger.build(AccountData.PROVIDED)
    read_posts = ReadJournalEntries[str]()
    def posts(period: DateRange) -> Iterable[JournalEntry[str]]:
        return iter(ledger.entries(period))
    read_posts.__call__ = posts
    assert len(list(read_posts(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 31))))) > 0

# Generated at 2022-06-14 04:19:52.615694
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass

# Generated at 2022-06-14 04:20:03.164000
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from .accounts import Account

    # set up the acccounts
    asset = Account(type = AccountType.ASSETS, name = "Cash")
    expense = Account(type = AccountType.EXPENSES, name = "Rent")
    revenue = Account(type = AccountType.REVENUES, name = "Sales")
    equity = Account(type = AccountType.EQUITIES, name = "Owner")
    liability = Account(type = AccountType.LIABILITIES, name = "Creditor")

    assert len(asset.postings) == 0
    assert len(expense.postings) == 0
    assert len(revenue.postings) == 0
    assert len(equity.postings) == 0
    assert len(liability.postings) == 0

    # set up the transactions
   

# Generated at 2022-06-14 04:20:09.681549
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry(datetime.date(2019,11,21), "Income", None)
    j.post(datetime.date(2019,11,21), Account("Allocation:Salary","Status:Balance",AccountType.REVENUES), Quantity("1001.00"))
    j.post(datetime.date(2019,11,21), Account("Expense:Salary","Expenses:Balance",AccountType.EXPENSES), Quantity("1001.00"))
    j.validate()

# Generated at 2022-06-14 04:20:11.523877
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    jo = JournalEntry(date=None, description=None, source=None)
    jo.post(date=None, account=None, quantity=None)

# Generated at 2022-06-14 04:20:18.993550
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    #arrange
    acc1 = Account("Account1","ASSETS","Cash in hand")
    acc2 = Account("Account2","EXPENSES","Rent")
    entry = JournalEntry(date = datetime.date(2020,4,4), description = "April Rent", source = None)
    entry.post(datetime.date(2020,4,4), acc1, -1000)
    entry.post(datetime.date(2020,4,4), acc2, 1000)
    #act
    #assert
    entry.validate()

# Generated at 2022-06-14 04:20:28.705927
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..booking.income import SalesInvoice
    from ..booking.ledgers import Ledger
    from ..booking.costofgoods import PurchaseInvoice

    journal = JournalEntry[SalesInvoice](datetime.date.today(), "Credit customer1", SalesInvoice(1, "CUSTOMER1", 1000))

    journal = journal.post(datetime.date.today(), Ledger.ASSETS.CREDITOR_1, 1000)
    journal = journal.post(datetime.date.today(), Ledger.EXPENSES.GOODS_SOLD, 500)
    journal = journal.post(datetime.date.today(), Ledger.EXPENSES.VAT_PAID, 75)
    journal = journal.post(datetime.date.today(), Ledger.REVENUES.SALES, 425)

    journal = journal

# Generated at 2022-06-14 04:20:36.437342
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .ledgers import GeneralLedger, GLPosting, GLTransaction
    from .tags import Tag
    from .units import UnitType

    s: GLTransaction = GLTransaction(
        date=datetime.date(2000, 1, 1),
        description="Dummy Transaction",
        source=Tag(name="Dummy"),
        guid="dummy",
    )
    s.post(date=datetime.date(2000, 1, 1), account=Account(name="Assets:Cash", type=AccountType.ASSETS), quantity=1)
    s.post(date=datetime.date(2000, 1, 1), account=Account(name="Assets:Cash", type=AccountType.ASSETS), quantity=1)