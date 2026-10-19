

# Generated at 2022-06-14 04:11:30.655100
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read(period: DateRange) -> Iterable[JournalEntry[int]]:
        return [JournalEntry((datetime.date.today(), "dummy", 0, []))]
    ReadJournalEntries[int].__call__(read, None)  # coverage.py does not show this without this line.

# Generated at 2022-06-14 04:11:36.131968
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    booking_account = Account('My Booking Account', AccountType.ASSETS)
    journal = JournalEntry(datetime.date(2020, 10, 1), 'My booking', 'TAB', [])
    journal.post(datetime.date(2020, 10, 1), booking_account, 100)
    journal.validate()
    print("test_JournalEntry_validate is passed!")

# Generated at 2022-06-14 04:11:42.829716
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # given
    from .accounts import Account, AccountType
    from .books import Book
    from .ledger_edit import EditLedger
    from .ledger_query import QueryLedger, Summary

    book = Book(
        guid=makeguid(),
        name="Test Book",
        description="Test Book for Integration Tests",
        ledger_edit=EditLedger(),
        ledger_query=QueryLedger(Summary()),
    )

    account = book.ledger_edit.create_account(
        name="Test Account",
        description="Account for Integration Tests",
        type=AccountType.REVENUES,
    )

    journal_date = datetime.date(2020, 1, 15)
    journal_desc = "Test Journal"
    journal_source = {}


# Generated at 2022-06-14 04:11:49.763747
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Setup
    journal: JournalEntry[str] = JournalEntry(date=datetime(2020, 1, 1), description="Transaction 1", source="Transaction")
    # Exercise
    journal.post(
        date=datetime(2020, 1, 1),
        account=Account(number="1234", name="Assets:Cash", type=AccountType.ASSETS),
        quantity=Quantity(100, Currency.USD),
    )
    journal.post(
        date=datetime(2020, 1, 1),
        account=Account(number="4321", name="Expenses:Rent", type=AccountType.EXPENSES),
        quantity=Quantity(-100, Currency.USD),
    )
    # Verify
    assert journal.postings[0].date == datetime(2020, 1, 1)

# Generated at 2022-06-14 04:11:54.635575
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    jr = JournalEntry[int]
    jr_post = jr.post
    jr_debits = jr.debits
    jr_credits = jr.credits
    jr_validate = jr.validate
    p1 = Posting(jr, datetime.date, Account('1234', 'sg', AccountType.ASSETS), Direction.INC, Amount(100))
    p2 = Posting(jr, datetime.date, Account('1235', 'sg', AccountType.LIABILITIES), Direction.INC, Amount(50))
    p3 = Posting(jr, datetime.date, Account('1236', 'sg', AccountType.EQUITIES), Direction.INC, Amount(50))

# Generated at 2022-06-14 04:12:00.301329
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class ReadJournalEntries__x(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    class ReadJournalEntries__y:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    r = ReadJournalEntries__x()

# Generated at 2022-06-14 04:12:06.489782
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    account_a = Account("A", AccountType.ASSETS)
    account_b = Account("B", AccountType.LIABILITIES)

    j = JournalEntry("2019-12-31", "Test", None)

    j.post("2019-12-31", account_a, Amount(100))
    j.post("2019-12-31", account_b, Amount(-100))
    j.validate()

test_JournalEntry_validate()

# Generated at 2022-06-14 04:12:13.967613
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry(datetime.date(2020,8,20), 'test', 'Test')
    je.post(datetime.date(2020,8,20), Account(1, AccountType.ASSETS, 'Test Account', 'Test Account'), Quantity(100))
    je.post(datetime.date(2020,8,20), Account(1, AccountType.REVENUES, 'Test Account', 'Test Account'), Quantity(-100))
    try:
        je.validate()
    except (AssertionError):
        assert False

# Generated at 2022-06-14 04:12:24.438320
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType

    #: Declares the account types.
    class AccountTypes(Enum):
        ASSETS = "Assets"
        REVENUES = "Revenues"

    #: Declares an account
    account1 = Account(AccountTypes.ASSETS, "Account1", "Account1")
    account2 = Account(AccountTypes.REVENUES, "Account2", "Account2")

    #: Create a journal entry
    journal_entry1 = JournalEntry(datetime.date(2020, 8, 1), "Description", None)
    journal_entry1.post(datetime.date(2020, 8, 1), account1, 100)
    journal_entry1.post(datetime.date(2020, 8, 1), account2, 100)
    journal_entry1.validate()

    journal_entry

# Generated at 2022-06-14 04:12:27.903534
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
     Unit test for method validate of class JournalEntry
    """
    je = JournalEntry[None]
    try:
        je.validate()
        assert False
    except AssertionError:
        assert True

# Generated at 2022-06-14 04:12:33.709504
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert True == True


# Generated at 2022-06-14 04:12:45.740997
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    @dataclass(frozen=True)
    class BusinessObject:
        name: str

    assert JournalEntry(
            date = datetime.date(2020, 1, 1),
            description = 'Test transaction',
            source = BusinessObject(name = 'Test Transaction')
        ).post(
            datetime.date(2020, 1, 1), Account(name = 'Account 1', type = AccountType.ASSETS), Quantity(100)
        ).post(
            datetime.date(2020, 1, 1), Account(name = 'Account 2', type = AccountType.ASSETS), Quantity(200)
        ).validate()


# Generated at 2022-06-14 04:12:54.047842
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class Source:
        date: datetime.date


# Generated at 2022-06-14 04:13:04.894464
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    account_type = AccountType.ASSETS
    account = Account(account_type, 'Cash')
    date = datetime.date.today()
    description = 'salary'
    source = 'company'
    period = datetime.date(2014, 1, 1)
    posting_amounts = [1000, 10]
    posting_directions = [Direction.INC, Direction.INC]

    journal = JournalEntry[str](date, description, source)
    for amount, direction in zip(posting_amounts, posting_directions):
        journal.post(date, account, amount * direction.value)
    journal.validate()
    print(journal)

# Generated at 2022-06-14 04:13:14.151342
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal = JournalEntry[str](datetime.date.today(), "Test", "Test", [], makeguid())
    journal.post(datetime.date.today(), Account("Assets", "B", AccountType.ASSETS), Quantity(100))
    journal.post(datetime.date.today(), Account("Equity", "C", AccountType.EQUITIES), Quantity(-100))
    assert journal.postings[0].is_debit == True
    assert journal.postings[1].is_debit == False
    assert journal.postings[0].account == Account("Assets", "B", AccountType.ASSETS)
    assert journal.postings[1].account == Account("Equity", "C", AccountType.EQUITIES)
    return journal



# Generated at 2022-06-14 04:13:18.251613
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from .commons.zeitgeist import DateRange

    #: Date of posting. 
    date = datetime.date(2020, 7, 20)

    #: Account to post the amount to.
    account = Account(AccountType.EQUITIES, 'Equities/investments')

    #: Signed-value to post to the account.
    quantity = Amount(-50000)

    entity = JournalEntry.of(date, "Test Description")
    entity.post(date, account, quantity)
    pprint(entity.postings)

    entity.validate()

# Generated at 2022-06-14 04:13:25.252513
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    account: Account = Account('Sales','Revenue')
    
    journal = JournalEntry(datetime.date(2020, 1, 1),'Sold goods to customer',account)
    journal.post(datetime.date(2020, 1, 1), account, 100)
    
    print(journal.is_debit)
    print(journal.postings[0].is_debit)
    
test_JournalEntry_post()

# Generated at 2022-06-14 04:13:26.450337
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:13:35.582404
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal = JournalEntry[str]("date 1", "description 1", "source 1", [])
    assert not journal.postings
    # Test balance sheet account
    journal.post("date 2", Account("a1", "Account 1", AccountType.EQUITIES), Quantity(100))
    assert journal.postings[0].is_debit
    journal.post("date 2", Account("a1", "Account 1", AccountType.EQUITIES), Quantity(100))
    assert journal.postings[1].is_debit
    journal.post("date 2", Account("a1", "Account 1", AccountType.EQUITIES), Quantity(-200))
    assert journal.postings[2].is_credit
    journal.post("date 2", Account("a1", "Account 1", AccountType.EQUITIES), Quantity(-200))

# Generated at 2022-06-14 04:13:41.764310
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime

    journal_entry = JournalEntry(date=datetime.date.today(), description="Loan taken", source="Loan")
    journal_entry.post(date=datetime.date.today(), account=Account(number="1000", name="Loan", type=AccountType.ASSETS),
                       quantity=Amount(100000))
    assert journal_entry.postings[0].amount == Amount(100000), \
        "Test Method JournalEntry.post Failed :- Amount not posted correctly !"

# Generated at 2022-06-14 04:13:51.606222
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Test JournalEntry.post method
    :return:
    """
    # Initialize Book
    j = JournalEntry(datetime.datetime.now().date(), 'test')
    # Post
    j.post(datetime.datetime.now().date(), 'TEST', 10)
    # Test
    assert j.postings[0].account == 'TEST'
    assert j.postings[0].amount == 10

# Generated at 2022-06-14 04:13:57.871353
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from budget.domain.accounts import Account
    from budget.domain.commons import Amount, Quantity
    from budget.domain.journal import JournalEntry
    from budget.domain.people import Person
    assert isinstance(JournalEntry(date.today(), "Test", Person("Tom", "Hanks")), JournalEntry)
    assert isinstance(JournalEntry(date.today(), "Test", Person("Tom", "Hanks")).post(date.today(), Account("Assets", "Cash"), Quantity(100)), JournalEntry)

# Generated at 2022-06-14 04:14:09.982975
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..accounts.journal_of_ledger import JournalOfLedger, ReadLedgerJournalEntries

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[str]]:
        return list(
            JournalOfLedger(
                ReadLedgerJournalEntries(
                    ledger_filename="tests/fixtures/ledgers/read-journal-of-ledger.dat",
                    ledger_period=period,
                )
            ).as_journal_entries()
        )


# Generated at 2022-06-14 04:14:16.007755
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from typing import Type, List

    from ..commons.others import is_unique
    from .accounts import Account, AccountType

    def test_fn(period: DateRange) -> List[Account]:
        return [
            Account("A/c 1", AccountType.ASSETS),
            Account("A/c 2", AccountType.EQUITIES),
            Account("A/c 3", AccountType.LIABILITIES),
            Account("A/c 4", AccountType.REVENUES),
            Account("A/c 5", AccountType.EXPENSES),
        ]

    #:
    def test_fn_asset(period: DateRange) -> List[Account]:
        return [Account("A/c 1", AccountType.ASSETS)]


# Generated at 2022-06-14 04:14:22.026430
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class A:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            print("test")
            if False:
                yield JournalEntry("", "", "")

    a = A()
    a("")
    #assert isinstance(a, ReadJournalEntries)


# Generated at 2022-06-14 04:14:23.306761
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Nothing to test.
    pass

# Generated at 2022-06-14 04:14:31.673571
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Arrange:
    # - Define a function which returns a journal entry.
    def make_entry():
        return JournalEntry(date=datetime.date(2019, 9, 2), description="Null Entry", source=None)

    # - Make a read journal entries object.
    read_entries = ReadJournalEntries[_T]()

    # Act:
    # - Call the read journal entries object.
    actual_entries = read_entries(None)

    # Assert:
    assert actual_entries == []


# Generated at 2022-06-14 04:14:36.445407
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from .accounts import Account, AccountType
    from .business import Business
    from .money import Currency
    from .payments import Payment, PaymentType

    ## Get a business:
    business = Business(name="ACME Investment Bank", currency=Currency.USD)

    ## Get accounts:
    account_bank = business.register_account(
        code="BNK01", type=AccountType.ASSETS, name="Bank Account", balance=100000
    )
    account_cash = business.register_account(
        code="CAS01", type=AccountType.ASSETS, name="Petty Cash", balance=5000
    )
    account_interest_expense = business.register_account(
        code="EXP01", type=AccountType.EXPENSES, name="Interest Expense", balance=0
    )


# Generated at 2022-06-14 04:14:41.042693
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    a = Account('Cash', AccountType.ASSETS)
    j = JournalEntry(datetime.date(2020, 1, 1), 'test')
    j.post(datetime.date(2020, 1, 1), a, 1000)
    j.post(datetime.date(2020, 1, 1), a, -1000)

# Generated at 2022-06-14 04:14:49.523134
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal = JournalEntry(datetime.date(2020, 1, 1),"Test Journal Entry",1)
    journal.post(datetime.date(2020, 1, 1),Account("Assets",AccountType.ASSETS),"2000")
    journal.post(datetime.date(2020, 1, 1),Account("Equities",AccountType.EQUITIES),"2000")
    journal.post(datetime.date(2020, 1, 1),Account("Liabilities",AccountType.LIABILITIES),"2000")
    journal.post(datetime.date(2020, 1, 1),Account("Liabilities",AccountType.LIABILITIES),"2000")

    assert(journal.postings[0].direction == Direction.INC)
    assert(journal.postings[0].amount == "2000")
    assert(journal.postings[0].account.name == "Assets")


# Generated at 2022-06-14 04:15:08.614756
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from .accounts import Account

    @dataclass
    class Person:
        guid: Guid
        name: str
    person1 = Person(Guid("guid-person1"), "John Doe")
    person2 = Person(Guid("guid-person2"), "Jane Roe")
    account1 = Account(Guid("guid-account1"), "Cash", AccountType.ASSETS)
    account2 = Account(Guid("guid-account2"), "Accounts Receivable", AccountType.ASSETS)
    account3 = Account(Guid("guid-account3"), "Accounts Payable", AccountType.LIABILITIES)

    entry1 = JournalEntry(datetime.date(2020,1,1), "Startup", person1)

# Generated at 2022-06-14 04:15:09.364249
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:15:20.171870
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Ledger
    from .accounts import ReadAccounts, ReadBalances
    from .accounts import WriteBalances

    from .books import Book

    from .ledgers.mem import MemLedger

    from .books.mem import MemBook

    from .accounts.mem import MemAccounts, MemBalances

    # Create test data:
    ledger = MemLedger()

    accounts = MemAccounts(ledger)
    balances = MemBalances(ledger)

    book = MemBook(ledger)

    # Create journal entries in the book:
    book.create_journal_entry(datetime.date(2020, 1, 1), "Test Entry")(
        credits={accounts.get(1001): 10.00,}, debits={accounts.get(1002): 10.00,},
    )


# Generated at 2022-06-14 04:15:30.277110
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def ReadJournalEntries___call__() -> None:
        from . import assets, ownerships, profits

        from ...commons.zeitgeist import Period

        from .accounts import AccountType

        ## Create a simple balance sheet:
        balance_sheet = assets.BalanceSheet(
            assets=[
                assets.Cash("CASH-001", description="Cash"),
                assets.Equipment("EQUIP-001", description="Equipment", original_cost=500, accumulated_depreciation=250),
            ]
        )

        ## Create a simple ownership account:
        owner = ownerships.Ownership("OWNER-001", name="Individual")

        ## Create a simple income statement:
        income_statement = profits.IncomeStatement(period=Period(Period.FISCAL_Q1, 2020))

        ## Create journal entries reader and read the journal

# Generated at 2022-06-14 04:15:37.321708
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    entry = JournalEntry[int]()
    entry.post(date=datetime.date(2001, 1, 1), account=Account(name="Test Account", type=AccountType.ASSETS, path=[]),
               quantity=100)
    assert len(entry.postings) == 1
    assert entry.postings[0].date == datetime.date(2001, 1, 1)
    assert entry.postings[0].account.name == "Test Account"
    assert entry.postings[0].account.type == AccountType.ASSETS
    assert entry.postings[0].direction == Direction.INC
    assert entry.postings[0].amount == Amount(100)


# Generated at 2022-06-14 04:15:47.755268
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountType

    from .invoice import Invoice

    from .unittest_accounts import test_accounts
    from .unittest_customers import test_customer
    from .unittest_products import test_product

    read_journalentries = ReadJournalEntries()

    invoice = Invoice(
        customer=test_customer,
        invoice_date=datetime.date(2019, 10, 30),
        invoice_number="INV-1",
        items=[
            invoice.InvoiceLine(product=test_product, quantity=2, unit=test_product.unit),
            invoice.InvoiceLine(product=test_product, quantity=3, unit=test_product.unit),
        ],
    )

    journal_entry = invoice.to_journalentry()


# Generated at 2022-06-14 04:15:51.926157
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Exercise function
    result = __call__(self, period)

    # Verify result
    assert isinstance(result, Iterable)


# Local variable to store optimization:
globals()["__call__"] = ReadJournalEntries.__call__.__func__

# Generated at 2022-06-14 04:15:52.945506
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass



# Generated at 2022-06-14 04:16:04.298754
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType
    from .businessobjects import BusinessObject

    class Currency(BusinessObject):
        def __init__(self, code: str):
            super().__init__()
            self.code = code

    usd = Currency("USD")
    btc = Currency("BTC")
    bank_account = Account("Bank Account", AccountType.ASSETS, usd)
    cash_account = Account("Cash Account", AccountType.ASSETS, usd)
    hodl_account = Account("HODL Account", AccountType.ASSETS, btc)
    revenue_account = Account("Revenue", AccountType.REVENUES, usd)
    expense_account = Account("Expense", AccountType.EXPENSES, usd)
    test_date = datetime.date.today()


# Generated at 2022-06-14 04:16:12.191680
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from unittest.mock import MagicMock
    from .events import PeriodicPaymentEvent
    from .accounts import Bank

    # Mock:
    read_journal_entries = ReadJournalEntries[PeriodicPaymentEvent]

    # Arrange:
    date_range = DateRange.for_month("2017-01").next(months=12)

    # Act:
    BILL = Bank().account("Bill Payment")
    SAVING = Bank().account("Savings")


# Generated at 2022-06-14 04:16:40.727592
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from datetime import date 
    from ..commons.others import makeguid
    from ..library.accounts import Account, AccountType, Accounts
    from .journal_entries import JournalEntry, Direction

    Accounts.define("1", Account.custom("1", "Cash", AccountType.ASSETS, 0))
    Accounts.define("2", Account.custom("2", "Bank", AccountType.ASSETS, 0))
    Accounts.define("3", Account.custom("3", "Equities", AccountType.EQUITIES, 0))
    Accounts.define("4", Account.custom("4", "Services", AccountType.REVENUES, 10))
    Accounts.define("5", Account.custom("5", "Products", AccountType.REVENUES, 20))

# Generated at 2022-06-14 04:16:50.329612
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    date_now = datetime.date.today()
    from .accounts import Account
    from .accounts import AccountType
    from .accounts import AssetType
    from .accounts import EquityType
    from .accounts import LiabilityType


    account_revenue = Account(AccountType.REVENUES, "Revenue", 0)
    account_expense = Account(AccountType.EXPENSES, "Expense", 0)
    account_assets = Account(AccountType.ASSETS, "Assets", AssetType.CASH)
    account_equity = Account(AccountType.EQUITIES, "Equities", EquityType.RETAINED_EARNINGS)
    account_liability = Account(AccountType.LIABILITIES, "Liabilities", LiabilityType.RECEIVABLE)


# Generated at 2022-06-14 04:16:51.032322
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:16:59.482336
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from typing import Dict
    from ..commons.numbers import Amount
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountType
    from .accounts import Accounts as account_accounts
    from .accounts import ReadAccounts as read_account_accounts
    from .accounts import build_accounts as build_account_accounts
    from .accounts import load_accounts as load_account_accounts
    from .accounts import test_Accounts___call__ as test_account_accounts___call__
    from .accounts import test_Accounts_get_account as test_account_accounts_get_account
    from .accounts import test_ReadAccounts as test_read_account_accounts

# Generated at 2022-06-14 04:17:04.976948
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    try:
        j = JournalEntry[int]
        j.post(datetime.date.today(), "1101", "1000")
        j.post(datetime.date.today(), "1102", "-600")
        j.post(datetime.date.today(), "5201", "300")
        j.validate()
    except AssertionError:
        print("test_JournalEntry_validate: Test FAILED")

# Generated at 2022-06-14 04:17:06.960744
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # TODO When we implement the journal entry model, add a test case to illustrate how to use the model.
    pass

# Generated at 2022-06-14 04:17:11.725098
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    ## Build subject under test:
    class A(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return list()
    sut = A()

    ## Verify:
    assert isinstance(sut.__call__(DateRange.from_year_month(2020, 1)), list)

# Generated at 2022-06-14 04:17:18.928239
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import pytest
    from ..commons.zeitgeist import DateRange, TestDate
    @dataclass
    class MockJournalEntry(JournalEntry):
        id = Guid("1a0fece6-d347-4e1c-b4d4-4a2a07a25d20")
        date = TestDate("2020-03-01")
        description = "Mock Journal Entry"
        source = "Mock Journal Source"
        postings = [Posting(MockJournalEntry, TestDate("2020-03-01"), Account("Assets:Cash", "Assets"), Direction.INC, Amount(100))]

    @dataclass
    class Mock(ReadJournalEntries):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry]:
            return [MockJournalEntry()]


# Generated at 2022-06-14 04:17:27.422026
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.time import today
    from .ledgers import Ledger

    class DummyJournalEntryReader(ReadJournalEntries[Ledger]):

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[Ledger]]:
            return (
                JournalEntry(today, "description", None)
                .post(today, Account("cash", AccountType.ASSETS), +1000)
                .post(today, Account("revenue", AccountType.REVENUES), -1000)
                for _ in range(3)
            )

    assert isinstance(DummyJournalEntryReader()(DateRange(today, today)), Iterable)  # type check

# Generated at 2022-06-14 04:17:32.096390
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # TODO: Unify with more comprehensive test
    account = Account("Revenues")
    je = JournalEntry(datetime.date(2021, 1, 1), "Description", None)
    je.post(datetime.date(2021, 1, 1), account, Quantity(+100))
    je.post(datetime.date(2021, 1, 1), account, Quantity(-100))

    assert je.postings[0].amount == Amount(100)
    assert je.postings[1].amount == Amount(100)

# Generated at 2022-06-14 04:18:08.707037
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class MyReadJournalEntries1(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    class MyReadJournalEntries2(ReadJournalEntries[_T]):
        def __call__(self, period: int) -> Iterable[JournalEntry[_T]]:
            pass

    def get_read_journal_entries() -> ReadJournalEntries[str]:
        return MyReadJournalEntries1()

    try:
        get_read_journal_entries()
    except TypeError:
        pass
    else:
        assert False, "Should have raised a TypeError"



# Generated at 2022-06-14 04:18:17.813959
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Unit test for validate method of JournalEntry class.
    """
    import datetime
    from dataclasses import dataclass, field
    from typing import List
    from .accounts import Account

    @dataclass(frozen=True)
    class AccountJournal(Generic[_T]):
        from dataclasses import dataclass, field
        from typing import List
        from .accounts import Account


        #: Date of the entry.
        date: datetime.date

        #: Description of the entry.
        description: str

        #: Postings of the journal entry.
        postings: List[JournalEntry.Posting] = field(default_factory=list, init=False)

        #: Globally unique, ephemeral identifier.

# Generated at 2022-06-14 04:18:26.486598
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
  e = JournalEntry(datetime.date(2017,1,1), "Test", None)
  e.post(e.date, Account("Cash", AccountType.ASSETS), Amount(10))
  e.post(e.date, Account("Interest", AccountType.REVENUES), Amount(-10))

  ## Assert:
  try:
    e.validate()
  except AssertionError as e:
    print(e)
    return False
  else:
    return True

# Test for validate method of JournalEntry class

# Generated at 2022-06-14 04:18:27.068711
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass

# Generated at 2022-06-14 04:18:38.027011
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import Account, AccountType
    from .equities import Equity
    from .instruments import Instrument
    from .portfolios import Portfolio
    from .prices import Price, PriceMap
    from ..commons.zeitgeist import Date, DateRange

    ## Given:
    @dataclass(frozen=True)
    class FakeReadJournalEntries:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[Equity]]:
            return [JournalEntry(date=Date(2021, 1, 15), description="Fake Journal Entry: 1", source=Equity(Instrument("GOOG"), Portfolio("P1")))]

    price_map: PriceMap = PriceMap({Instrument("GOOG"): Price(Date(2021, 1, 15), 1)})
    read_journal_ent

# Generated at 2022-06-14 04:18:43.306154
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # This is an example of how to create a function of type ReadJournalEntries
    @dataclass(frozen=True)
    class TestClass():
        field: int

    @ReadJournalEntries.instance
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[TestClass]]:
        return []

    # Unit test the code.
    assert len(list(read_journal_entries(DateRange()))) == 0

# Generated at 2022-06-14 04:18:48.863402
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    ## Setup
    jvm:JournalEntry = JournalEntry(datetime.date(2020, 1, 1),
                                     "Test journal entry",
                                     "Test business object")

    ## Setup
    jvm.post(datetime.date(2020,1,1), Account("Assets", AccountType.ASSETS), Quantity(100))
    jvm.post(datetime.date(2020,1,1), Account("Revenues", AccountType.REVENUES), Quantity(-100))

    ## Execution & Verification
    assert jvm.debits[0].amount == Amount(100)
    assert jvm.credits[0].amount == Amount(100)
    jvm.validate()

# Generated at 2022-06-14 04:18:49.842418
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:18:54.238382
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    class X:
        pass
    x = X()
    j = JournalEntry(datetime.date.today(), "Sales", x)
    j.post(datetime.date.today(), Account("Sales", AccountType.REVENUES), 100)
    j.post(datetime.date.today(), Account("Cash", AccountType.ASSETS), -100)
    j.validate()

    print(j)

# Generated at 2022-06-14 04:18:59.006320
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType
    
    account = Account(name = "Assets", type = AccountType.ASSETS, parent = 0)
    j = JournalEntry(date = date.today(), description = "Test", source = 0)
    j.post(date.today(), account, 10)
    j.post(date.today(), account, -10)
    j.validate()

# Generated at 2022-06-14 04:20:15.047389
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType, Account, AccountRepository, AccountRepositoryProtocol
    from .wallets import Wallet
    entry = JournalEntry[str]
    a1 = Account(AccountType.EQUITIES, "Income", "")
    a2 = Account(AccountType.EQUITIES, "Expense", "")
    a3 = Account(AccountType.REVENUES, "Income", "")
    a4 = Account(AccountType.EXPENSES, "Expense", "")
    a5 = Account(AccountType.LIABILITIES, "Income", "")
    a6 = Account(AccountType.LIABILITIES, "Expense", "")
    a7 = Account(AccountType.ASSETS, "Income", "")
    a8 = Account(AccountType.ASSETS, "Expense", "")
    a9

# Generated at 2022-06-14 04:20:21.903702
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    #Create an account
    test_account = Account("account1", AccountType.ASSETS)
    #Create a journal entry
    test_journal_entry = JournalEntry(date=datetime.date(2020,1,1),description="description", source="source")
    #Post an amount
    test_journal_entry.post(date=datetime.date(2020,1,1), account=test_account, quantity=100)
    #Assert that no assertion error is thrown
    assert test_journal_entry.validate()

# Generated at 2022-06-14 04:20:30.764276
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Unit test for method post of class JournalEntry
    """
    category = "jack"
    je = JournalEntry[str](
        datetime.date.today(),
        "Test journal entry",
        category,
    )
    account = Account("Checking", AccountType.ASSETS)
    quantity = Quantity(100)
    je.post(datetime.date.today(), account, quantity)

    # len of postings is 1
    assert len(je.postings) == 1

    # Posting is debit
    assert je.postings[0].is_debit
    
    # Posting amount is correct
    assert je.postings[0].amount == Amount(100)

    # Posting account is correct
    assert je.postings[0].account == account

    # Posting direction is correct

# Generated at 2022-06-14 04:20:40.648597
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountOwner

    # Create an AccountOwner
    account_owner = AccountOwner(name="Olivier", location="Gent", guid=1234)

    # Create a JournalEntry
    journal = JournalEntry(date=datetime.date(2020, 1, 1), description="New Year", source=account_owner)

    # Post to the AccountOwner
    journal.post(date=datetime.date(2020, 1, 1), account=account_owner.get_account(), quantity=20)

    # Expected result
    postings = journal.postings

    assert len(postings) == 1
    assert postings[0].journal == journal
    assert postings[0].date == datetime.date(2020, 1, 1)
    assert postings[0].account == account_owner.get_account()

# Generated at 2022-06-14 04:20:45.816236
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .businessobjs import Transaction

    #: External source of journal entries:
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[Transaction]]:
        return []

    assert issubclass(type(read_journal_entries), ReadJournalEntries[Transaction])

# Generated at 2022-06-14 04:20:49.575981
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class TestSource(Protocol):
        pass
    assert issubclass(test_ReadJournalEntries___call__.__closure__[0].cell_contents, ReadJournalEntries)

# Generated at 2022-06-14 04:21:02.333883
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import Accounts
    from .books import Books
    from .system import System

    accounts = Accounts(Books(System()))
    entries = ReadJournalEntries()(DateRange.from_month(datetime.date.today().month))
    for entry in entries:
        entry.validate()
        assert entry.date == datetime.date(2020, 10, 10)
        assert entry.description == "Test Journal Entry"
        assert len(entry.postings) == 4
        assert entry.postings[0].account == accounts["Cash"]
        assert entry.postings[0].direction == Direction.INC
        assert entry.postings[0].amount == Amount(4000)
        assert entry.postings[1].account == accounts["Equity:Opening Balances"]
        assert entry.postings[1].direction == Direction.INC
       

# Generated at 2022-06-14 04:21:10.482091
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from ledgerkeeper.bank.domain.models import BankAccount, Transaction
    from ledgerkeeper.bank.domain.models import TransactionType
    from ledgerkeeper.bank.domain.repositories import TransactionNotFoundError
    from ledgerkeeper.enums import TransactionStatus

    transaction = Transaction(
        id="random",
        bank_account=BankAccount(account="test"),
        type=TransactionType.DEPOSIT,
        status=TransactionStatus.OPEN,
        amount_in_dollars=100.0,
        is_recurring=False,
    )

    journal = JournalEntry[Transaction].from_postings(transaction, "test journal", [])
    journal.post(date=datetime.date.today(), account=Account.from_str("assets:checking:test"), quantity=1.0)

    journal.validate()

    #

# Generated at 2022-06-14 04:21:21.829314
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountType

    @dataclass(frozen=True)
    class Transaction:
        pass

    @dataclass(frozen=True)
    class JournalEntryMock(JournalEntry[Transaction]):
        pass

    JournalEntryMock(None, None, None)
