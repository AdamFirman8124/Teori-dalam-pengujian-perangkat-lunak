

# Generated at 2022-06-14 04:11:38.373401
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from revalue.domainmodel.accounts import Account, AccountType
    from revalue.domainmodel.commons.numbers import Quantity
    from revalue.domainmodel.commons.zeitgeist import DateRange
    from revalue.domainmodel.journal.read import ReadJournalEntries
    from revalue.domainmodel.journal.entries import JournalEntry
    from revalue.domainmodel.journal.postings import Posting
    from revalue.domainmodel.journal.events import PostIncrementEvent, PostDecrementEvent

    cash_account: Account = Account(guid=0, name="Cash", type=AccountType.ASSETS)
    expense_account: Account = Account(guid=1, name="Postage Expense", type=AccountType.EXPENSES)

# Generated at 2022-06-14 04:11:47.086210
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from unittest import mock
    from .accounts import Account, RootAccount
    from ..balances.core import BalanceSheet

    class StubSource:
        def __init__(self, journal_entries: Iterable[JournalEntry[object]], balance_sheet: BalanceSheet) -> None:
            _journal_entries = list(journal_entries)
            self.journal_entries = mock.Mock(return_value=_journal_entries)
            self._balance_sheet = balance_sheet

        def balance_sheet(self, date: datetime.date) -> BalanceSheet:
            return self._balance_sheet

    class StubRjes(ReadJournalEntries[object]):
        pass

    ## Given:
    _, account_1 = Account.new("account-1")

# Generated at 2022-06-14 04:11:52.567362
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    with JournalEntry("Foo") as entries:
        entry = entries.post("2019-01-01", "Assets:Cash", 100)

    try:
        entry.validate()
    except AssertionError as e:
        assert "Total Debits and Credits are not equal" in str(e), "Expected exception type not thrown."

# Generated at 2022-06-14 04:12:01.548582
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Given
    journal = JournalEntry(datetime.date(2020, 11, 24), "Assets Debit = Liabilities Credit", None)
    journal.post(datetime.date(2020, 11, 24), Account("123", "Cash", AccountType.ASSETS), +1000)
    journal.post(datetime.date(2020, 11, 24), Account("234", "Accounts Payable", AccountType.LIABILITIES), -2000)
    print("Before Validation: ")
    for posting in journal.postings:
        print("### Posting: ", posting)
    # When
    journal.validate()
    print("After Validation: ")
    for posting in journal.postings:
        print("### Posting: ", posting)

# Generated at 2022-06-14 04:12:10.784167
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .items import ItemSalesJournal, ItemPurchaseJournal

    def test_validate(j: JournalEntry[ItemPurchaseJournal]):
        j.validate()

    test_validate(
        JournalEntry(datetime.date(2019, 1, 4), "Balance", None, None)
        .post(datetime.date(2019, 1, 5), Account("11", AccountType.ASSETS), +100)
        .post(datetime.date(2019, 1, 5), Account("101", AccountType.EXPENSES), -100)
    )


# Generated at 2022-06-14 04:12:13.580118
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert (ReadJournalEntries[int](None) == None)

# Generated at 2022-06-14 04:12:24.192310
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j1 = JournalEntry(datetime.date(2020, 1, 1), 'test post', None)
    j1.post(datetime.date(2020, 1, 1), Account('abc', AccountType.ASSETS), 10)
    j1.post(datetime.date(2020, 1, 1), Account('xyz', AccountType.ASSETS), 20)
    j1.post(datetime.date(2020, 1, 1), Account('pqr', AccountType.EXPENSES), 40)
    assert not j1.postings[0].is_debit
    assert not j1.postings[1].is_debit
    assert j1.postings[2].is_debit

# Generated at 2022-06-14 04:12:31.258373
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountFactory
    from .fixtures import AccountBook
    account_book = AccountBook()
    account_book.add_account(AccountFactory().create(name="Debit2", account_type=AccountType.LIABILITIES))

    journal1 = JournalEntry(date=datetime.date(2018, 5, 2), description="Test Journal Entry").post(
        date=datetime.date(2018, 5, 2),
        account=AccountFactory().get(name="Debit2"),
        quantity=Quantity(2000),
    )

    journal1.validate()

# Generated at 2022-06-14 04:12:42.505424
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import create_account
    from .books import create_book
    from .transactions import create_transaction

    ## Given
    book = create_book("Test Book", created="2019-07-01")
    account_sales = create_account(book, "Sales", AccountType.REVENUES)
    account_cash = create_account(book, "Cash", AccountType.ASSETS)

    transaction = create_transaction("T1", "Sales", "Cash", 100)

    ## When
    journal = transaction.journal()
    journal.post(datetime.date(2019, 1, 1), account_sales, 100)
    journal.post(datetime.date(2019, 1, 1), account_cash, -100)

    ## Then
    journal.validate()

# Generated at 2022-06-14 04:12:52.048525
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    acc1=Account("Asset", AccountType.ASSETS )
    acc2=Account("Revenue", AccountType.REVENUES)
    post1=Posting("journal", datetime.date(2014,10,30), acc1, Direction.INC, Amount(10))
    post2=Posting("journal", datetime.date(2014,10,30), acc2, Direction.DEC, Amount(5))

    assert post1.is_debit == True
    assert post1.is_credit == False

    assert post2.is_debit == False
    assert post2.is_credit == True

    journal_entry=JournalEntry( datetime.date(2014,10,30), "Description", "Balance", [post1, post2])
    journal_entry.validate()


# Generated at 2022-06-14 04:13:10.846357
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    @dataclass(frozen=True)
    class A:
        pass

    je = JournalEntry[A](date=datetime.date.today(), description='test', source=A())
    je.post(date=datetime.date.today(), account=Account(name='cash', type=AccountType.ASSETS), quantity=100)
    assert len(je.postings) == 1
    assert je.postings[0].amount == 100
    assert je.postings[0].direction == Direction.INC


if __name__ == "__main__":

    import unittest


    class JournalEntryTest(unittest.TestCase):

        def test_post(self):
            @dataclass(frozen=True)
            class A:
                pass


# Generated at 2022-06-14 04:13:18.589395
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def function(period: DateRange) -> Iterable[JournalEntry[str]]:
        yield JournalEntry(datetime.date(2020, 1, 8), "Description 1", "Source 1")
        yield JournalEntry(datetime.date(2020, 1, 1), "Description 2", "Source 2")

    assert list(function(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 7)))) == []
    assert list(function(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 8)))) == [
        JournalEntry(datetime.date(2020, 1, 1), "Description 2", "Source 2")
    ]

# Generated at 2022-06-14 04:13:30.982138
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    @dataclass(frozen=True)
    class Transaction:
        name: str

    entry = JournalEntry[Transaction]('20200602','description','transaction')
    entry.post(datetime.date(2020, 6, 2), Account('expense', 'salary'), -100)
    entry.post(datetime.date(2020, 6, 2), Account('revenue', 'salary'), 100)
    assert len(entry.debits) is 1
    assert len(entry.credits) is 1
    entry.post(datetime.date(2020, 7, 2), Account('expense', 'salary'), -0)
    assert len(entry.debits) is 1
    assert len(entry.credits) is 1

# Generated at 2022-06-14 04:13:39.602348
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from .ledgers import Ledger
    from .events import Event
    from .journals import Journal
    from .transactions import Transaction
    from .tags import Tag, TagValue
    from datetime import date
    import time

    ledger: Ledger = Ledger()
    ledger.journal().post(date(2019, 1, 1), ledger.accounts().expenses(), +500)
    ledger.journal().post(date(2019, 1, 1), ledger.accounts().revenues(), -500)
    ledger.journal().vali

# Generated at 2022-06-14 04:13:50.658673
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Test data
    date = datetime.date(2020, 4, 20)
    account = Account("Account 1", AccountType.ASSETS, "account1")
    quantity = Amount(100)

    # Create a journal entry
    j_entry = JournalEntry[None](date = date,
                                 description = "",
                                 source = None,
                                 postings = [])
    # Post an increment to the entry
    j_entry.post(date, account, quantity)

    # Test if the postings list has only one element
    assert len(j_entry.postings) == 1

    # Fetch the posted element
    posted_element = j_entry.postings[0]
    # Test if the posted element contains the data
    assert posted_element.journal == j_entry
    assert posted_element.date == date
    assert posted_

# Generated at 2022-06-14 04:13:57.306921
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    '''Test posting to assets account'''
    from ..commons.ledgers import ledgers
    je1 = JournalEntry(datetime.date(2000 , 1, 1), "Test", "JournalEntry.post")
    je1.post(datetime.date(2000 , 1, 1), ledgers.assets, 100)
    assert je1.postings[0].account == ledgers.assets 
    assert je1.postings[0].amount == 100
    assert je1.postings[0].direction == Direction.INC 



# Generated at 2022-06-14 04:14:09.172677
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .account_types import ASSETS, LIABILITIES, EQUITIES, EXPENSES, REVENUES
    from .accounts import Account
    from .account_numbers import AccountNumber

    journal_entry = JournalEntry(datetime.date.today(), "Test Journal Entry", source="Test Object")

    #: Postings to test

# Generated at 2022-06-14 04:14:19.816566
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..clients.entities import Client
    from ..commons.numbers import ZERO
    from ..books.entities import Invoice, InvoiceItem
    from ..books.repositories import find_account

    invoice = Invoice(
        id=1,
        is_active=True,
        client=Client(id=1, name="Test Client"),
        invoice_date=datetime.date.today(),
    )

    invoice.items.append(InvoiceItem(invoice, "Test item", ZERO))

    sales_revenue_account = find_account("SALES REVENUE")
    tax_receivable_account = find_account("TAX RECEIVABLE")

    journal = JournalEntry[Invoice].__new__(JournalEntry[Invoice])
    journal.date = invoice.invoice_date
   

# Generated at 2022-06-14 04:14:20.634470
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert True

# Generated at 2022-06-14 04:14:32.972815
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    from .accounts import AccountType
    from .accounts import makeaccount
    from .commons.numbers import ZERO
    from .commons.numbers import Quantity
    from .journal.values import JournalEntry
    from .journal.values import Posting
    from .journal.values import Direction
    from .types import BusinessObject

    class TestBusiness(BusinessObject):
        def __init__(self, name, guid):
            self.name = name
            self.guid = guid
            pass

    business_object = TestBusiness(name = "test", guid = "random-string-for-business-object")

    account = makeaccount(AccountType.ASSETS, "Cash")


# Generated at 2022-06-14 04:14:41.222078
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date

    j = JournalEntry(date.today(), "Test JournalEntry")
    j.post(date.today(), Account.ASSETS_CASH_ON_HAND, 100)
    j.post(date.today(), Account.ASSETS_CASH_ON_HAND, -100)
    j.validate()

# Generated at 2022-06-14 04:14:43.648548
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # JournalEntry.post(JournalEntry, date: datetime.date, account: Account, quantity: Quantity) -> "JournalEntry[_T]"
    pass



# Generated at 2022-06-14 04:14:51.167383
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountRoot
    from .domain import LedgerDomain
    from .ledgers import Ledger, Reading

    ## Build a journal entry reader:
    def journal_entry_reader(period: DateRange) -> Iterable[JournalEntry[Ledger]]:
        accounts = AccountRoot(None)

# Generated at 2022-06-14 04:14:55.453307
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    _T = TypeVar("_T")
    class ReadJournalEntriesTest(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    _ = ReadJournalEntriesTest()

# Generated at 2022-06-14 04:15:00.180366
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType
    from .codes import Code

    ## Create a valid journal entry:
    a = Account(Code.from_string("A"), AccountType.ASSETS)
    b = Account(Code.from_string("B"), AccountType.EXPENSES)
    entry = JournalEntry(datetime.date(2019, 8, 2), "Test Journal Entry", "Unit Test")
    entry.post(datetime.date(2019, 8, 2), a, 100)
    entry.post(datetime.date(2019, 8, 2), b, -100)
    entry.validate()

    ## Create an invalid journal entry:
    a = Account(Code.from_string("A"), AccountType.ASSETS)
    b = Account(Code.from_string("B"), AccountType.EXPENSES)
    entry = Journal

# Generated at 2022-06-14 04:15:11.209691
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass
    class Source:
        period: DateRange

    def read_journal_entries_factory(
        account: Account, period: DateRange
    ) -> ReadJournalEntries[Source]:
        def read_journal_entries(
            period: DateRange
        ) -> Iterable[JournalEntry[Source]]:
            return [
                JournalEntry(period.from_date, "Transfer from bank account 101 to cash on hand", Source(period), [
                    Posting(None, period.from_date, account, Direction.DEC, Amount(1000)),
                    Posting(None, period.from_date, Account.of(AccountType.ASSETS, "Cash on hand"), Direction.INC, Amount(1000)),
                ])
            ]
        return read_journal_entries


# Generated at 2022-06-14 04:15:22.889580
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import Date, DateRange
    from .accounts import Account, AccountType
    from .accounts import parse_accounts, read_accounts
    from .chartofaccounts import ChartOfAccounts
    from .ledgers import Ledger
    import io
    import os
    import tempfile

    # Ensure that the temporary directory exists:
    try:
        tempfile.TemporaryDirectory()
    except NotImplementedError:
        print("WARNING: Test skipped as the required functionality is not supported.")
        return

    # Read chart of accounts:
    chart = ChartOfAccounts(parse_accounts(read_accounts("tests/data/chartofaccounts.txt")))

    # Create a ledger:

# Generated at 2022-06-14 04:15:25.202886
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class Sample:
        pass
    def read_journal_entries(period):
        return list()

    assert callable(read_journal_entries)

# Generated at 2022-06-14 04:15:26.342144
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Write your unit test here
    pass

# Generated at 2022-06-14 04:15:34.801551
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # check with normal test case(total of debit and credit are equal)
    account1 = Account(AccountType.ASSETS, 'Cash', 'Cash')
    account2 = Account(AccountType.EXPENSES, 'Office Supplies Expense', 'Office Supplies Expense')
    je = JournalEntry(datetime.date(2019, 1, 21), 'test', None)
    je.post(datetime.date(2019, 1, 21), account1, 10000)
    je.post(datetime.date(2019, 1, 21), account2, -10000)
    je.validate()

    # check with total of debit and credit are not equal
    account3 = Account(AccountType.ASSETS, 'Cash', 'Cash')
    account4 = Account(AccountType.EXPENSES, 'Office Supplies Expense', 'Office Supplies Expense')


# Generated at 2022-06-14 04:15:41.648406
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:15:42.722266
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j1 = JournalEntry[None]

# Generated at 2022-06-14 04:15:43.340123
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    assert False

# Generated at 2022-06-14 04:15:53.812930
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Set up the test
    test_date = datetime.date(2020, 8, 5)
    test_account_1 = Account(code='A', name='Test', reporting_type='A', type=1)
    test_account_2 = Account(code='B', name='Test', reporting_type='A', type=1)
    test_journal_entry = JournalEntry[int]()
    test_journal_entry.date = test_date
    test_journal_entry.description = 'Test'
    test_journal_entry.source = 0

# Generated at 2022-06-14 04:15:58.004007
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Setup the journal entry, to check the validate method
    journal_entry = JournalEntry[None](datetime.date(2020, 3, 18), "Unbalanced", None)
    journal_entry.postings = [
        Posting(journal_entry, datetime.date(2020, 3, 18), Account("asset_1", AccountType.ASSETS), Direction.INC, Amount(27)),
        Posting(journal_entry, datetime.date(2020, 3, 18), Account("expense_1", AccountType.EXPENSES), Direction.DEC, Amount(20)),
    ]

    # Call the validate method to check that validation passes
    journal_entry.validate()

    # Setup the unbalanced journal entry, to check the validate method

# Generated at 2022-06-14 04:15:58.658277
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:16:08.999604
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from typing import List, TypeVar
    from unittest import mock
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .entries import Posting, JournalEntry
    from .journals import ReadJournalEntries
    T = TypeVar("T")
    a_source: T = mock.Mock()
    a_range = DateRange(start=datetime.date(2020, 1, 1), end=datetime.date(2020, 12, 31))
    a_account_1 = Account("Cash")
    a_account_2 = Account("Sales")
    a_account_3 = Account("Taxes")


# Generated at 2022-06-14 04:16:20.061644
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    def _assert_validates_ok(postings):
        journalEntry = JournalEntry(datetime.date.today(), 'test_JournalEntry_validate', None, postings)
        journalEntry.validate()

    _assert_validates_ok([Posting(None, datetime.date.today(), Account(AccountType.REVENUES, 'A'), Direction.INC, Amount(10))])
    _assert_validates_ok([Posting(None, datetime.date.today(), Account(AccountType.REVENUES, 'A'), Direction.INC, Amount(10)),
                          Posting(None, datetime.date.today(), Account(AccountType.EQUITIES, 'A'), Direction.DEC, Amount(10))])

# Generated at 2022-06-14 04:16:31.561829
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class Advisor:
        name: str

    @dataclass(frozen=True)
    class Fund:
        name: str

    @dataclass(frozen=True)
    class Category:
        name: str

    @dataclass(frozen=True)
    class Commodity:
        name: str

    @dataclass(frozen=True)
    class Currency:
        name: str

    account_advisors_cash = Account(AccountType.ASSETS, "Cash", "Cash balances held by the advisors")
    account_advisors_equities = Account(AccountType.ASSETS, "Equities", "Equities held by the advisors")
    account_funds_cash = Account(AccountType.ASSETS, "Cash", "Cash balances held by the funds")
   

# Generated at 2022-06-14 04:16:41.488074
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    import datetime
    from tests.finance.test_accounts import test_accounts

    # Create journal entry object
    journal = JournalEntry(datetime.date(2020,1,1), 'Description of journal entry', 3, [])
    
    # Define Account objects
    Account1 = test_accounts[1]
    Account2 = test_accounts[2]
    Account3 = test_accounts[3]
    
    # Post to Accounts
    journal.post(journal.date, Account1, 1)
    journal.post(journal.date, Account2, -1)
    journal.post(journal.date, Account3, 1)
    
    # test function
    try:
        journal.validate()
        assert True
    except AssertionError:
        assert False

# Generated at 2022-06-14 04:16:58.994015
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    source = "bank"
    date = datetime.date.today()
    account1 = Account("Equities:yourself", AccountType.EQUITIES)
    account2 = Account("Liabilities:Bank", AccountType.LIABILITIES)
    journal = JournalEntry[str](date=date, description="test", source=source)
    journal.post(date, account1, 1000)
    journal.post(date, account2, -1000)
    assert len(journal.postings) == 2, "post method failed"



# Generated at 2022-06-14 04:17:04.808324
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from ..commons.date import date, today
    from ..commons.numbers import USD, ZERO
    from .accounts import ASSETS, EQUITIES, EXPENSES, LIABILITIES, REVENUES, StockAccount

    expense_account = StockAccount(EXPENSES, "EXPENSES")
    asset_account = StockAccount(ASSETS, "ASSETS")

    # Valid journal entries:
    # 1) Journal entry with one debit and one credit - all zeroes
    journal_entry1 = JournalEntry(date(2020, 2, 1), "", None)
    journal_entry1.post(today(), expense_account, ZERO)
    journal_entry1.post(today(), asset_account, ZERO)
    journal_entry1.validate()

    # 2) Journal entry with debit and credit with same quantities (and different account types)


# Generated at 2022-06-14 04:17:05.466390
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass

# Generated at 2022-06-14 04:17:11.145952
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry.of_asset_transfer(datetime.date(2020, 1, 1), "TEST_DESCRIPTION", "TEST_SOURCE", "TEST_FROM", "TEST_TO", 100)
    je.validate()
    je.post(datetime.date(2020,1,1),"TEST_ACCOUNT",50)
    with pytest.raises(AssertionError):
        je.validate()

# Generated at 2022-06-14 04:17:18.612679
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # given 
    # Create accounts
    assets = Account(500, "Assets", AccountType.ASSETS, "INR")
    equity = Account(5000, "Equity", AccountType.EQUITIES, "INR")
    liability = Account(600, "Liability", AccountType.LIABILITIES, "INR")
    revenue = Account(4000, "Revenue", AccountType.REVENUES, "INR")
    expense = Account(300, "Expense", AccountType.EXPENSES, "INR")
    # Create journal entry
    journal_entry = JournalEntry(datetime.date(2020, 1, 1), "Sample Entry", "Transaction 1")
    assert journal_entry.postings == []
    # when
    journal_entry.post(datetime.date(2020, 1, 1), assets, +300)
    journal

# Generated at 2022-06-14 04:17:28.777333
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from unittest import TestCase

    from ..commons.zeitgeist import DateRangeAnd

    from .accounts import AccountType

    # Arrange:
    class TestAccount(Account):
        def __init__(self, type: AccountType, name: str):
            super().__init__(name, True)
            self.type = type

    def _invoke(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return __call__(period)

    def __call__(period: DateRange) -> Iterable[JournalEntry[_T]]:
        yield JournalEntry(date(2020, 9, 3), "", None).post(date(2020, 9, 3), TestAccount(AccountType.ASSETS, "A"), 100)

# Generated at 2022-06-14 04:17:32.990924
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Example:
    def read_journal_entries(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
        pass
    # Check:
    assert read_journal_entries.__call__.__doc__ == "Returns the journal entries for the period."

# Generated at 2022-06-14 04:17:42.125872
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
     #Set up
    # Set up
    from datetime import datetime
    from dataclasses import dataclass
    from typing import List
    from ledgerapi.ledger.accounts import Account
    from ledgerapi.ledger.entries import Posting
    from ledgerapi.ledger.entries import JournalEntry
    
    @dataclass
    class BankEntry:
        source: str = 'Bank'
    
    @dataclass
    class SalEntry:
        source: str = 'Sal'
    
    @dataclass
    class PurchaseEntry:
        source: str = 'Purchase'
        
    @dataclass
    class ExpEntry:
        source: str = 'Exp'
    
    
    
    date = datetime(2020, 5, 10)

# Generated at 2022-06-14 04:17:52.329880
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Type check:
    def journal_entries_by_date(
        period: DateRange
    ) -> Iterable[JournalEntry[str]]:
        return [JournalEntry(
            datetime.date.today(), "FooBar", "Baz", [])]
    journal_entries_by_date(DateRange(datetime.date.today(), datetime.date.today()))
    journal_entries_by_date(DateRange(datetime.datetime.now(), datetime.datetime.now()))
    journal_entries_by_date(DateRange(datetime.date.today(), datetime.datetime.now()))
    journal_entries_by_date(DateRange(datetime.datetime.now(), datetime.date.today()))

# Generated at 2022-06-14 04:18:00.001946
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..books.model import Account as account
    from ..books.model import ChartOfAccounts as chart_of_accounts
    from ..books.model import Transaction as transaction
    from ..books.model import AccountsBook as accounts_book
    from ..books.model import AccountsJournal as accounts_journal
    from ..books.model import ReadAccountsBook as read_accounts_book
    from ..books.model import ReadAccountsJournal as read_accounts_journal

    account_list = [account('asset', 'Bank', 'ICICI Bank Ltd.'),
                    account('expense', 'Office', 'Office Expenses'),
                    account('liability', 'Loans', 'ICICI Bank Ltd.')]

    chart_of_accounts = chart_of_accounts(account_list)

# Generated at 2022-06-14 04:18:29.688338
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    _call = lambda *args, **kwargs: lambda: (
        ReadJournalEntries,
        DateRange,
        Iterable[JournalEntry[_T]]
    )
    _call = ReadJournalEntries.__call__
    # TODO: Write unit tests

# Generated at 2022-06-14 04:18:34.968436
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Tests for validate method.
    """

    je = JournalEntry(datetime.date(2019, 2, 1), "", None)
    je.post(datetime.date(2019, 2, 1), Account("Cash"), Amount(100))
    je.post(datetime.date(2019, 2, 1), Account("Income"), Amount(-100))
    je.validate()

# Generated at 2022-06-14 04:18:43.427037
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # pylint: disable=unused-import
    from typing import Callable
    from .accounts import AccountType
    from .insiders import Insiders
    from .journal import ReadJournalEntries
    from .portfolio import Portfolio
    from .prices import Prices
    from .timeframe import Timeframe
    # pylint: enable=unused-import

    #:
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[Insiders]] :
        pass

    assert callable(ReadJournalEntries.__call__)
    assert isinstance(read_journal_entries, ReadJournalEntries[Insiders])


# Generated at 2022-06-14 04:18:51.227215
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # mock object
    mock_period = DateRange.from_dates('2019-01-01', '2019-01-01')
    mock_return_value = [JournalEntry(date=datetime.date.today())]

    def mock_function(period: DateRange) -> Iterable[JournalEntry[_T]]:
        assert period == mock_period
        return mock_return_value

    assert mock_function(mock_period) == mock_return_value

# Generated at 2022-06-14 04:19:00.725769
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType

    def assertPosting(journal, description, expectedAccount, expectedQuantity, expectedDirection):
        for posting in journal.postings:
            if expectedAccount.name == posting.account.name:
                assert description == posting.journal.description, "Description is not correct"
                assert expectedAccount.name == posting.account.name, "Account name is not correct"
                assert expectedDirection.value == posting.direction.value, "Direction is not correct"
                assert expectedQuantity == posting.amount.value, "Quantity is not correct"

    def assertPostingNotInJournal(journal, expectedAccount):
        assert not any(posting.account.name == expectedAccount.name for posting in journal.postings), "Account name is in journal"

    assets = Account(AccountType.ASSETS, "Assets")
    revenues = Account

# Generated at 2022-06-14 04:19:09.982686
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Performs unit test for the method post of class JournalEntry
    """
    # Arrange
    import datetime
    from .accounts import AccountType
    ledger = {}
    debit_account = Account("D", "Debit Account", AccountType.ASSETS)
    credit_account = Account("C", "Credit Account", AccountType.REVENUES)

    # Act
    journal_entry = JournalEntry(datetime.date.today(),"test_JournalEntry_post",ledger)
    journal_entry.post(datetime.date.today(), debit_account, 100)
    journal_entry.post(datetime.date.today(), credit_account, 100)

    # Assert
    assert journal_entry is not None

# Generated at 2022-06-14 04:19:21.877100
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # total of debits and credits will be same hence there shouldnt be any error raised
    date1=datetime.date(2020,5,5)
    date2=datetime.date(2020,5,10)
    from .accounts import Account
    from .accounts import AccountType
    from .accounts import Book
    from .accounts import Currency
    from .accounts import Root
    from .commons.numbers import Amount, Quantity

# Generated at 2022-06-14 04:19:30.070236
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from datetime import date

    # JournalEntry without posting
    je1 = JournalEntry(date(2019, 1, 1), 'Test_posting_je1', None)

    # JournalEntry with one posting
    je2 = JournalEntry(date(2019, 1, 1), 'Test_posting_je2', None)
    ac2 = Account('ac2', AccountType.LIABILITIES, None, None)
    je2.post(date(2019, 1, 1), ac2, -2000)

    # JournalEntry with two postings
    je3 = JournalEntry(date(2019, 1, 1), 'Test_posting_je3', None)
    ac1 = Account('ac1', AccountType.ASSETS, None, None)

# Generated at 2022-06-14 04:19:37.590550
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    #: Date of the entry.
    date_1 = datetime.datetime.strptime('2020-03-19', '%Y-%m-%d')

    #: Description of the entry.
    description_1 = "Description Test"

    #: Business object as the source of the journal entry.
    source_1 = "Source Test"

    #: Postings of the journal entry.
    postings_1 = list()
    postings_1.append(Posting(date_1, "Account Test", "+", 100))

    #: Globally unique, ephemeral identifier.
    guid_1 = "GUID Test"

    SourceTest = JournalEntry(date_1, description_1, source_1, postings_1, guid_1)

    #: Date of the entry.
    date_2 = datetime.datetime.str

# Generated at 2022-06-14 04:19:38.712811
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert False, "Not implemented"

# Generated at 2022-06-14 04:20:51.767901
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    data = [
        (datetime.date(2020, 1, 1), Account("Assets", AccountType.ASSETS), 400),
        (datetime.date(2020, 1, 1), Account("Revenues", AccountType.REVENUES), -400),
    ]
    
    je = JournalEntry(datetime.date(2020, 1, 1), "Test journal entry", "Source")

    for date, account, quantity in data:
        je.post(date, account, quantity)

    je.validate()

    assert data[0][2] == je.increments[0].amount
    assert data[1][2] == -je.decrements[0].amount
    assert data[0][2] == -je.credits[0].amount
    assert data[1][2] == je.debits[0].amount

# Generated at 2022-06-14 04:20:52.422592
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:20:59.483339
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():

    from unittest.mock import MagicMock

    # Set up:
    read_journal_entries = ReadJournalEntries()
    read_journal_entries.__call__ = MagicMock()

    # Exercise:
    read_journal_entries(None)

    # Verify:
    read_journal_entries.__call__.assert_called_once_with(None)

# Generated at 2022-06-14 04:21:08.910572
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    accounts = Account()
    accounts.create('11-1-1')
    accounts.create('20-1-3')
    accounts.create('20-1-4')
    accounts.create('40-1-1')
    accounts.create('40-1-2')
    accounts.create('40-1-5')
    accounts.create('40-1-6')
    accounts.create('40-1-7')
    accounts.create('40-1-8')
    accounts.create('40-1-9')
    accounts.create('40-1-10')
    accounts.create('40-1-11')
    accounts.create('40-1-12')
    accounts.create('40-1-13')
    accounts.create('40-1-14')
    accounts.create('40-1-15')
   

# Generated at 2022-06-14 04:21:20.558468
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Setup
    journal_entry_business_object = "Some business object"
    journal_entry_date = datetime.date(2000, 1, 1)
    journal_entry_description = "description"
    journal_entry = JournalEntry(journal_entry_business_object, journal_entry_date, journal_entry_description)
    account1 = Account("account1", AccountType.EXPENSES)
    account2 = Account("account2", AccountType.REVENUES)
    account3 = Account("account3", AccountType.ASSETS)
    journal_entry.post(journal_entry_date - datetime.timedelta(days=1), account1, -1000)
    journal_entry.post(journal_entry_date, account2, +1000)
    journal_entry.post(journal_entry_date, account3, -100)
