

# Generated at 2022-06-14 04:11:22.075311
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:11:23.271162
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    #TODO: Implement it
    pass

# Generated at 2022-06-14 04:11:34.663450
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    test if the method post of class JournalEntry is working
    """
    from .accounts import Account
    from .business import Business
    from .transaction import Transaction
    from .warehouse import Warehouse, WarehouseStock
    import datetime
    b = Business()
    w = Warehouse('w', 'w', 'w')
    ws = WarehouseStock('ws', 'ws', 'ws', w, None, 0)
    t = Transaction('test_t', None, None, datetime.datetime(2020, 6, 10, 0, 0), 'test')
    je = JournalEntry(datetime.datetime.today(), 'test', t)
    a = Account('test_a', 'test_a', AccountType.EXPENSES)
    je.post(datetime.datetime.today(), a, 1)
    assert je.postings

# Generated at 2022-06-14 04:11:42.043038
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Test function for JournalEntry.validate() method
    """
    journal = JournalEntry(datetime.date.today(), "testing entry", "testing source")
    journal.postings.append(Posting(journal, datetime.date.today(), Account("asset", AccountType.ASSETS),
                                    Direction.INC, Amount(5)))
    journal.postings.append(Posting(journal, datetime.date.today(), Account("expense", AccountType.EXPENSES),
                                    Direction.DEC, Amount(5)))
    journal.validate()

# Generated at 2022-06-14 04:11:49.307065
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from ..accounts import Account, GLAccount, TAGAccount, AccountType
    JournalEntry(date=datetime.date(2020, 1, 1), description='Test Valid', source=None).post(
        date=datetime.date(2020, 1, 1), account=GLAccount('AAccount', 'Asset', AccountType.ASSETS), quantity=500).post(
        date=datetime.date(2020, 1, 1), account=GLAccount('LAccount', 'Liabilitiy', AccountType.LIABILITIES), quantity=-500).validate()

# Generated at 2022-06-14 04:11:58.771403
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType

    # Initialize Account objects
    Account1 = Account(AccountType.ASSETS, "Asset1")
    Account2 = Account(AccountType.ASSETS, "Asset2")
    Account3 = Account(AccountType.LIABILITIES, "Liability1")
    Account4 = Account(AccountType.EQUITIES, "Equity1")
    Account5 = Account(AccountType.LIABILITIES, "Liability2")
    Account6 = Account(AccountType.EXPENSES, "Expense1")
    Account7 = Account(AccountType.REVENUES, "Revenue1")
    Account8 = Account(AccountType.LIABILITIES, "Liability3")

    JournalEntry.post(datetime.date.today(),Account1,1)

# Generated at 2022-06-14 04:12:06.141665
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import Date

    @dataclass
    class Person:
        name: str

    @dataclass
    class Transaction:
        date: datetime.date
        person: Person
        account: Account
        amount: Amount

    person = Person(name="John Doe")
    transactions_1 = [
        Transaction(date=Date(2020, 1, 1), person=person, account=Account("C", "Cash"), amount=Amount(5000)),
        Transaction(date=Date(2020, 1, 1), person=person, account=Account("A", "Accounts Receivable"), amount=Amount(5000)),
    ]

# Generated at 2022-06-14 04:12:17.657412
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from bookkeeper.domain.businessobjects import BusinessObject
    from bookkeeper.domain.accounts import Account
    from bookkeeper.domain.parties import Party
    from bookkeeper.domain.products import Product
    from bookkeeper.domain.purchases import Purchase, PurchaseLineItem
    from bookkeeper.domain.sales import Sale, SaleLineItem
    from bookkeeper.domain.transactions import Transaction
    from bookkeeper.domain.journal import JournalEntry
    from bookkeeper.domain.periods import MonthPeriod

    p1 = Party(name='Party 1',
               billing_address='Billing address for party 1',
               shipping_address='Shipping address for party 1')

    p2 = Party(name='Party 2',
               billing_address='Billing address for party 2',
               shipping_address='Shipping address for party 2')


# Generated at 2022-06-14 04:12:21.685095
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountCategory
    a = AccountCategory(name="Test Account")
    j = JournalEntry(datetime.date.today(), "Test Transaction", a)
    j.post(datetime.date.today(),a, Quantity(100))

    j.validate()

# Generated at 2022-06-14 04:12:22.264977
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:12:34.921187
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .commons.zeitgeist import DateRange
    
    # set some example data 
    date = datetime.date(2019, 7, 24)
    accountA = Account(AccountType.ASSETS, "Account A")
    accountB = Account(AccountType.REVENUES, "Account B")
    quantity = 10.50
    period = DateRange(
    """
    start: 2019-07-24
    end: 2019-08-24 
    """)
    
    # Try to call the method by just import it
    from .journal_entries import JournalEntry
    journal_entry = JournalEntry(date, "Test description", [])
    journal_entry.post(date, accountA, quantity)
    journal_entry.post(date, accountB, quantity)
    journal_

# Generated at 2022-06-14 04:12:44.004673
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry(date=datetime.date(year=2019, month=1, day=1), description="", source="", postings=[])
    j.post(datetime.date(year=2019, month=1, day=1), Account(code="1011", description="Cash", type=AccountType.ASSETS), Quantity(1))
    j.post(datetime.date(year=2019, month=1, day=1), Account(code="2111", description="Product sales", type=AccountType.REVENUES), Quantity(-1))
    j.validate()


# Generated at 2022-06-14 04:12:50.955303
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    '''
    Test method post of class JournalEntry
    '''
    journalEntry = JournalEntry(date=datetime.date.today(), description="test journal entry")
    journalEntry.post(date=datetime.date.today(), account = Account(number =0, name = ""), quantity = 100)
    journalEntry.post(date=datetime.date.today(), account = Account(number =0, name = ""), quantity = -100)
    assert len(journalEntry.postings) == 2

# Generated at 2022-06-14 04:12:51.784423
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:13:04.952596
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    class TestT:
        pass
    test_date = datetime.date(2020, 4, 25)
    test_account = Account(AccountType.ASSETS, "123", "Cash")
    test_quantity = Quantity(1)
    test_T = TestT()
    test_journal = JournalEntry(test_date, "Test Journal", test_T)
    test_journal.post(test_date, test_account, test_quantity)
    assert(isinstance(test_journal.postings[0], Posting))
    assert(test_journal.postings[0].date == test_date)
    assert(test_journal.postings[0].account == test_account)
    assert(test_journal.postings[0].direction == Direction.INC)

# Generated at 2022-06-14 04:13:14.461605
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # given
    @dataclass(frozen=True)
    class BusinessObject:
        pass
    class FakeJournalEntry(JournalEntry[_T]):
        pass
    period = DateRange(date(2020, 1, 1), date(2021, 1, 1))
    class FakeReadJournalEntries(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            assert period == DateRange(date(2020, 1, 1), date(2021, 1, 1))
            return [
                FakeJournalEntry(date(2020, 1, 1), "Fake journal entry 1", BusinessObject()),
                FakeJournalEntry(date(2020, 1, 2), "Fake journal entry 2", BusinessObject()),
            ]
    read_journal_entries = FakeReadJournalEntries

# Generated at 2022-06-14 04:13:19.589432
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Fixtures
    from decimal import Decimal
    from typing import NamedTuple
    from .accounts import Account, AccountType
    from .transactions import Transaction

    @dataclass(frozen=True)
    class MockBusinessObject:
        """
        A mock business object, which serves as a transaction source.
        """

    # The mock business object for use as the source of the journal entry.
    source = MockBusinessObject()

    # The journal entry fixture.
    journal_entry = JournalEntry(
        date=datetime.date(year=2019, month=9, day=20),
        description="Test Journal Entry",
        source=source,
    )

    # The account fixtures.
    ASSETS = Account(AccountType.ASSETS, "Assets")
    EQUITIES = Account(AccountType.EQUITIES, "Equities")

# Generated at 2022-06-14 04:13:31.613632
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType
    from datetime import date
    import datetime
    assert date(2019, 1, 1)
    je = JournalEntry(datetime.datetime(2019, 1, 1), "Test", "")
    je.post(datetime.datetime(2019, 1, 1), Account(AccountType.ASSETS, "BANK_CURRENT"), 123)
    je.post(datetime.datetime(2019, 1, 1), Account(AccountType.EQUITIES, "MISC"), -123)
    je.validate()
    je = JournalEntry(datetime.datetime(2019, 1, 1), "Test", "")
    je.post(datetime.date(2019, 1, 1), Account(AccountType.ASSETS, "BANK_CURRENT"), 123)

# Generated at 2022-06-14 04:13:42.712333
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from ..accounts import Account, AccountType
    from ..commons.numbers import Quantity
    from ..domains.expenses import ExpenseCategory, Expense, PaymentMethod, \
        ExpenseService, ExpenseServiceFactory
    from ..domains.incomes import IncomeCategory, Income, IncomeService, \
        IncomeServiceFactory
    from ..domains.tasks import Task, TaskService, TaskServiceFactory
    from ..services import AppServiceProvider, ApplicationService
    from ..services.appserviceprovider import Services
    provider = AppServiceProvider()
    provider.register(Services.EXPENSE, ExpenseServiceFactory())
    provider.register(Services.INCOME, IncomeServiceFactory())
    provider.register(Services.TASK, TaskServiceFactory())
    task_service = provider.get(Services.TASK)
   

# Generated at 2022-06-14 04:13:51.408756
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    #Arrange
    date = datetime.date.today()
    date1 = date - datetime.timedelta(days=100) #100 days before current date
    description = "sample description"
    account = Account.assets_equity_capital()
    quantity = 200
    journal = JournalEntry(date1, description, account, [])
    #Act
    journal.post(date, account, quantity)
    #Assert
    assert journal.postings[0].direction == Direction.INC
    assert journal.postings[0].date == date
    assert journal.postings[0].account == account
    assert journal.postings[0].amount == Amount(200)


# Generated at 2022-06-14 04:14:08.462884
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Given:
    journal = JournalEntry[None](
        date=datetime.date(2020, 1, 1),
        description="A journal entry with an offsetting debit and credit",
        source=None,
    )

    # When:
    journal.post(date=journal.date, account="A", quantity=10)
    journal.post(date=journal.date, account="A", quantity=-10)

    # Then:
    journal.validate()

# Generated at 2022-06-14 04:14:09.611325
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    JournalEntry()


# Generated at 2022-06-14 04:14:15.807098
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Unit test for the method validate of class JournalEntry.
 
    :rtype: JournalEntry
    """
    class _JournalEntry(object):
        def __init__(self):
            self.postings = []
    journal=_JournalEntry()
    journal.postings.append(Posting(journal, datetime.date.today(), 'Equity', Direction.INC, 100))
    journal.postings.append(Posting(journal, datetime.date.today(), 'Expense', Direction.DEC, 100))
    journal_entry = JournalEntry(journal)
    try:
        journal_entry.validate()
    except:
        assert False
    journal.postings.append(Posting(journal, datetime.date.today(), 'Equity', Direction.INC, 10))
    journal_entry = JournalEntry(journal)


# Generated at 2022-06-14 04:14:28.510344
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import Account
    from .commons.zeitgeist import date
    import datetime
    from .types import AP, AccountType, Money, Quantity

    # Setup business object for journal entry.
    class Sale:
        pass

    # Define a reader.
    def read_journal_entries(period):
        return [
            JournalEntry(date(2020, 2, 3), "XYZ", Sale())
            .post(None, Account(AP, "A/P", AccountType.LIABILITIES), Quantity(10))
            .post(None, Account(Money, "Cash", AccountType.ASSETS), Quantity(10))
        ]

    # Define a reader.
    reader: ReadJournalEntries[Sale] = read_journal_entries

    # Test:

# Generated at 2022-06-14 04:14:40.571328
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Source type:
    class _Source:
        pass

    # Test journal entries:
    test_je1 = JournalEntry[_Source](datetime.date(2019, 1, 1), "JE-1", _Source())
    test_je2 = JournalEntry[_Source](datetime.date(2019, 1, 1), "JE-2", _Source())
    test_je3 = JournalEntry[_Source](datetime.date(2020, 1, 1), "JE-3", _Source())

    # Mock function which reads journal entries:
    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_Source]]:
        if period.start <= datetime.date(2019, 1, 1) <= period.end:
            return [test_je1, test_je2]

# Generated at 2022-06-14 04:14:49.304860
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Unit test for method post of class JournalEntry
    """

    from fints.accounts import AccountId
    from fints.books import LedgerBook, LedgerBookId

    import datetime
    from fints.transfers import TransferId

    from fints.accounts import AccountId
    from fints.books import LedgerBook, LedgerBookId

    from fints.postings import Direction
    from fints.transfers import TransferId
    from ..numbers import Amount, Quantity

    from datetime import date, datetime
    from fints.books import LedgerBook
    import logging
    import sys

    # logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    logging.basicConfig(level=logging.WARNING, stream=sys.stdout)


# Generated at 2022-06-14 04:14:54.429594
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    import unittest
    from ..commons.numbers import Q
    from ..ledgers.accounts import AccountType, Account 
    from ..ledgers.treatments import Treatment

    # Original tests written by `rsdev` (https://github.com/rsdev)
    class JournalEntryTests(unittest.TestCase):

        def test_validate(self):
            #: Simple journal entry
            j = JournalEntry(date = datetime.date(2020,1,1), 
                             description = "Simple posting to the same account.", 
                             source = Treatment(makeguid()))

            j.post(datetime.date(2020,1,1), Account("Assets", AccountType.ASSETS), Q(-100))

# Generated at 2022-06-14 04:15:01.189328
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    date = datetime.date(2019, 10, 6)
    a = Account('sales','assets')
    b = Account('purchase','expenses')
    journal_entry = JournalEntry(date, "sales", "sales")
    journal_entry.post(date, a, 8.99)
    journal_entry.post(date, b, -8.99)
    assert journal_entry.postings[0].amount == 8.99
    assert journal_entry.postings[1].amount == -8.99

# Generated at 2022-06-14 04:15:06.669393
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import DateRange

    def f(period: DateRange) -> Iterable[JournalEntry[str]]:
        yield JournalEntry(date=period.end, description="foo", source="bar", postings=[])

    assert f in ReadJournalEntries.__args__

# Generated at 2022-06-14 04:15:14.499114
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .test_accounts import sample_accounts
    from .test_business_objects import test_invoice
    from .test_tax_definitions import test_tax_definition_combined_no_taxes

    journal = JournalEntry[test_invoice]
    journal.date = test_invoice.date
    journal.description = test_invoice.description()
    journal.source = test_invoice
    journal.post(test_invoice.date, sample_accounts.sales_account, +test_invoice.amount())
    journal.post(test_invoice.date, sample_accounts.unearned_revenue, -test_invoice.amount())

    test_tax_definition_combined_no_taxes.apply(journal)


# Generated at 2022-06-14 04:15:44.263305
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..accounts import Account, AccountType
    from ..commons.numbers import Quantity
    from .corporate import BoughtGoods, BoughtServices
    from .money import Cash, Expenses, Liabilities, Revenues

    # Arrange:
    je = JournalEntry(datetime.date(2019, 3, 4), "The first posting", source=BoughtGoods(datetime.date(2019, 3, 4)))

    # Act:
    je.post(datetime.date(2019, 3, 4), Cash, 199)
    je.post(datetime.date(2019, 3, 4), Liabilities, -199)

    # Assert:
    assert je.postings[0].journal == je
    assert je.postings[0].date == datetime.date(2019, 3, 4)

# Generated at 2022-06-14 04:15:45.609026
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass


# Generated at 2022-06-14 04:15:48.952836
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class MyEntry:
        pass

    def read(period: DateRange) -> Iterable[JournalEntry[MyEntry]]:
        pass

    assert isinstance(read, ReadJournalEntries)

# Generated at 2022-06-14 04:15:59.751010
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import get_account
    from .taxes import _test__tax_deduction_transaction

    expected_date = datetime.date(2019, 1, 31)

    account_credit, *_ = _test__tax_deduction_transaction.get_entries(expected_date)

    account_debit=get_account("cash")

    # 1. Create a journal entry:

    journal: JournalEntry[_T] = JournalEntry(
        date=expected_date,
        description="Test journal entry",
        source=None
    )

    # 2. Post some amount to credit and debit account:

    journal.post(expected_date, account_debit, +5000)
    journal.post(expected_date, account_credit, -5000)

    # 3. Validate the journal entry:

    journal.validate()

# Generated at 2022-06-14 04:16:02.943682
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert issubclass(lambda period: [], ReadJournalEntries[str])
    assert not issubclass(lambda period: None, ReadJournalEntries[str])

# Generated at 2022-06-14 04:16:10.085280
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType, AccountContext

    ## Given
    account1 = Account(AccountType.ASSETS, "Account 1")
    account2 = Account(AccountType.LIABILITIES, "Account 2")

    ## When
    journal = JournalEntry[AccountContext].make(datetime.date(2020, 1, 2)).post(
        datetime.date(2020, 1, 2), account1, 100
    ).post(datetime.date(2020, 1, 2), account2, -100).validate()

    ## Then
    assert journal
    assert len(journal.debits) == 1
    assert len(journal.credits) == 1

# Generated at 2022-06-14 04:16:20.199457
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from datetime import date
    from pywavez.commons.numbers import Amount, Quantity

    from pywavez.ledger.accounts import Account, AccountType
    from pywavez.ledger.journal.postings import JournalEntry, Posting

    a1 = Account(AccountType.ASSETS, "cash")
    a2 = Account(AccountType.REVENUES, "sales")

    je = JournalEntry("2020-01-01", "sell", a1, [
        Posting(a1, date(2020, 1, 1), a1, Quantity(1), Amount(100)),
        Posting(a1, date(2020, 1, 1), a2, Quantity(1), Amount(100)),
    ])

    je.validate()

# Generated at 2022-06-14 04:16:31.676139
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from .accounts import Account, AccountType
    from .books import LedgerBook
    from .ledgers import Ledger
    from .transactions import Transaction
    from ..commons.numbers import Amount, Quantity

    expences_account = Account(AccountType.EXPENSES, "Expences", 1)
    revenues_account = Account(AccountType.REVENUES, "Revenues", 2)
    liability_account = Account(AccountType.LIABILITIES, "Liability", 3)
    equity_account = Account(AccountType.EQUITIES, "Equity", 4)
    cash_account = Account(AccountType.ASSETS, "Cash", 5)


# Generated at 2022-06-14 04:16:32.202994
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:16:35.579036
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    got = [0]

    class MyReadJournalEntries(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange):
            nonlocal got
            got[0] += 1
            return None

    ReadJournalEntries_: ReadJournalEntries[_T] = MyReadJournalEntries()
    ReadJournalEntries_(DateRange.now())

    assert got[0] == 1

# Generated at 2022-06-14 04:17:16.499630
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[None]]:
        for i in range(1, 4):
            yield JournalEntry(
                date=period.start + datetime.timedelta(days=i),
                description=f"Test {i}",
                source=None,
                postings=[
                    Posting(None, period.start + datetime.timedelta(days=i), Account("Assets:Temp"), Direction.INC, Amount(10)),
                    Posting(None, period.start + datetime.timedelta(days=i), Account("Expenses:Temp"), Direction.DEC, Amount(10)),
                ]
            )

    rje = ReadJournalEntries.__getitem__(None, ReadJournalEntries.__args__)

# Generated at 2022-06-14 04:17:26.771183
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import TimePeriod
    from .ledger import Ledger
    from .transactions import Transaction

    # Create test ledger
    my_ledger = Ledger("test")
    # Create test account
    my_account = my_ledger.create_account("my account", AccountType.ASSETS)
    # Create test transaction
    my_transaction = Transaction("my transaction", my_ledger.get_account("my account"), TimePeriod.today())
    # Create test journal entry
    my_journal_entry = JournalEntry(TimePeriod.today().date(), "my journal entry", my_transaction)
    # Get total number of posts
    posts_inital = len(my_journal_entry.postings)


# Generated at 2022-06-14 04:17:33.709133
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Accounts
    from .accounts import  Account, AccountType
    from .businessinfo import BusinessInfoType, BusinessInfo
    from .currency import Currency
    from .journal import JournalEntry, Posting
    from .period import Period, PeriodSummary, PeriodSummaryItem
    from .tag import Tag
    from .tagcategory import TagCategory, TagCategoryType
    from ..commons.guid import makeguid
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from ..commons.timing import now
#     curr = Currency.of("CAD")
#     usd = Currency.of("USD")
    curr = Currency
    usd = Currency
    accounts = Accounts()

# Generated at 2022-06-14 04:17:42.630640
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Tests method post of class JournalEntry.
    """
    from .accounts import Account
    # Create a test object
    journal_entry = JournalEntry[str](datetime.date(2020, 7, 26), "test description", "test source")

    # Create accounts
    assets = Account.of("assets", AccountType.ASSETS, "description assets")
    expenses = Account.of("expenses", AccountType.EXPENSES, "description expenses")

    assert len(journal_entry.postings) == 0
    journal_entry.post(datetime.date(2020, 7, 26), assets, Quantity(100)).post(datetime.date(2020, 7, 26), expenses, Quantity(-100))
    assert len(journal_entry.postings) == 2
    assert journal_entry.postings[0].account == assets
    assert journal_

# Generated at 2022-06-14 04:17:47.424471
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Case: amount is zero
    je = JournalEntry[int](datetime.date.today(), "desc", source=0)
    je.post(datetime.date.today(), Account("a"), Quantity(0))
    assert je.postings == []
    # Case: amount is positive
    je = JournalEntry[int](datetime.date.today(), "desc", source=0)
    je.post(datetime.date.today(), Account("a"), Quantity(1))
    assert len(je.postings) == 1
    assert je.postings[0].journal == je
    assert je.postings[0].date == datetime.date.today()
    assert je.postings[0].account == Account("a")
    assert je.postings[0].direction == Direction.INC

# Generated at 2022-06-14 04:17:48.736257
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass



# Generated at 2022-06-14 04:17:58.195196
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AssetAccount
    #Test for new account
    journal = JournalEntry[str]("23-Jun-2020", "Cash In")
    journal.post(DateRange.of(datetime.date(2020,6,23),datetime.date(2020,6,30)),
                AssetAccount("000", "Cash", 500, "Cash In account"),
                +500)
    journal.validate()
    assert journal.date == datetime.date(2020,6,23)
    assert journal.description == "Cash In"
    assert journal.source == "Cash In"
    assert journal.postings[0].date == datetime.date(2020,6,23)
    assert journal.postings[0].account.number == "000"
    assert journal.postings[0].account.name == "Cash"

# Generated at 2022-06-14 04:18:00.365760
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry()
    j.post(1, 5)
    j.post(2, -5)
    j.validate()

# Generated at 2022-06-14 04:18:11.412498
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class TestEntity:
        pass
    import pytest
    from datetime import date, timedelta
    from .accounts import Account
    from .journals import JournalEntry, Posting
    from .readjournalentries import ReadJournalEntries

# Generated at 2022-06-14 04:18:19.144772
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from datetime import date
    from ..ledger.accounts import AccountType
    from ..ledger.accounts import Account
    from ..ledger.accounts import PnL
    from ..ledger.accounts import BalanceSheet
    #: Date of the entry.
    date = date.today()
    #: Description of the entry.
    description = 'desc'
    #: Business object as the source of the journal entry.
    source = 0
    #: Globally unique, ephemeral identifier.
    guid = 1
    #: Postings of the journal entry.

# Generated at 2022-06-14 04:19:44.019639
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    from .diary import Diary, DairyAccount
    from .accounts import Account, AccountType

    # Init
    j = JournalEntry[int]("2018-07-1", "Dummy journal", 1)

    # assert Debit-INC
    j.postings = []
    j.post(None, Account("", AccountType.ASSETS, None), 100)
    assert len(j.postings) == 1
    print(j.postings)  # FIXME: assert ?
    assert j.postings[0].is_debit

    # assert Credit-INC
    j.postings = []
    j.post(None, Account("", AccountType.EXPENSES, None), 100)
    assert len(j.postings) == 1
    print(j.postings)  # FIXME: assert

# Generated at 2022-06-14 04:19:49.635487
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Given
    journal = JournalEntry(datetime.date(2020, 5, 25), "Fake journal entry", 'Fake source')
    # When
    journal = journal.post(datetime.date(2020, 5, 25), Account("Fake account name", AccountType.ASSETS), Quantity(5))
    # Then
    assert len(journal.debits) == 1

# Generated at 2022-06-14 04:19:55.651092
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from datetime import date
    from bookkeeper.repositories import ReadAccounts
    from bookkeeper.usecases.entities import BusinessAccount
    from bookkeeper.commons.others import makeguid
    from bookkeeper.usecases.journal import JournalEntry, JournalEntryCategory

    def instance_for_test(category :JournalEntryCategory):
        return JournalEntry(
            date=date(2018, 1, 1),
            description="",
            source=BusinessAccount(makeguid(), "account", category),
            postings=[]
        )

    j = instance_for_test(JournalEntryCategory.DEBIT)
    j.post(date(2018, 1, 1), "", 100)
    j.validate()

    j = instance_for_test(JournalEntryCategory.CREDIT)

# Generated at 2022-06-14 04:19:58.032513
# Unit test for method __call__ of class ReadJournalEntries

# Generated at 2022-06-14 04:20:02.475699
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    JournalEntry().post(datetime.date.today(), Account(1,  "Cash"), Quantity(100)).post(datetime.date.today(), Account(1,  "Cash"), -Quantity(100))
    assert len(JournalEntry().postings) == 2
    assert isinstance(JournalEntry().postings[0].account, Account)
    assert isinstance(JournalEntry().postings[0].date, datetime.date)
    assert isinstance(JournalEntry().postings[0].direction, Direction)
    assert isinstance(JournalEntry().postings[0].amount, Amount)

# Generated at 2022-06-14 04:20:06.615947
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..testing import Dummy

    class DummyImpl(ReadJournalEntries[Dummy]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[Dummy]]:
            pass

    DummyImpl().__call__(None)

# Generated at 2022-06-14 04:20:07.252165
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:20:07.990870
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:20:14.906474
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    
    je1 = JournalEntry[str]('2020-01-01','For test', 'Je1')
    je1.post(je1.date, Account('2000','Assets'),1000)
    je1.post(je1.date, Account('4000','Expenses'),-1000)
    try:
        je1.validate()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    
    je2 = JournalEntry[str]('2020-01-01','For test', 'Je2')
    je2.post(je2.date, Account('2000','Assets'),1000)
    je2.post(je2.date, Account('4000','Expenses'),-1000)
    je2.post(je2.date, Account('5000','Liabilities'),-1000)

# Generated at 2022-06-14 04:20:15.542439
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass