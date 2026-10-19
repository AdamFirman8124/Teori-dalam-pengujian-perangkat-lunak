

# Generated at 2022-06-14 04:11:33.345934
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    source = 1
    posting = Posting(JournalEntry(datetime.date(2020,1,1), "Description", source), datetime.date(2020,1,1), Account("TestAccount"), Direction.INC, Amount(100))
    assert posting.direction == Direction.INC
    assert posting.account.name == "TestAccount"
    assert posting.amount == Amount(100)

# Generated at 2022-06-14 04:11:40.413476
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    #: Sample journal entries for testing.
    journal_entries: List[JournalEntry[str]] = []
    journal_entries.append(
        JournalEntry(
            date=datetime.date(2020, 9, 1),
            description="Transaction 1",
            source="source 1",
        ).post(  # Date, Account, Quantity
            date=datetime.date(2020, 9, 1),
            account=Account("ACC1", AccountType.ASSETS),
            quantity=+10.0,
        ).post(
            date=datetime.date(2020, 9, 1),
            account=Account("ACC2", AccountType.EXPENSES),
            quantity=-10.0,
        )
    )

# Generated at 2022-06-14 04:11:47.915232
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountStub

    # Arrange
    journal = JournalEntry[int]
    date = datetime.date.today()
    account = AccountStub("JE-TEST", AccountType.ASSETS)
    quantity = 100

    # Act
    je = journal.post(date, account, quantity)
    
    # Assert
    assert 1 == len(je.postings)
    assert date == je.postings[0].date
    assert account == je.postings[0].account
    assert 100 == je.postings[0].amount
    assert Direction.INC == je.postings[0].direction
    
    return

if __name__ == "__main__":
    test_JournalEntry_post()

# Generated at 2022-06-14 04:11:53.372343
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry[object]
    j.date = datetime.date(2020, 1, 1)
    j.description = "TEST"
    j.post(datetime.date(2020, 1, 1), Account(""), 1000)
    j.post(datetime.date(2020, 1, 1), Account(""), -1000)
    j.validate()

# Generated at 2022-06-14 04:12:00.300491
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    obj = lambda period: iter([
        JournalEntry(datetime.date(2019, 1, 1), "", None),
        JournalEntry(datetime.date(2019, 1, 2), "", None),
        JournalEntry(datetime.date(2019, 1, 3), "", None),
        JournalEntry(datetime.date(2019, 1, 4), "", None),
        JournalEntry(datetime.date(2019, 1, 5), "", None),
        JournalEntry(datetime.date(2019, 1, 6), "", None),
        JournalEntry(datetime.date(2019, 1, 7), "", None),
    ])

    assert len(list(obj(DateRange(datetime.date(2019, 1, 3), datetime.date(2019, 1, 6))))) == 4

# Generated at 2022-06-14 04:12:06.490000
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j = JournalEntry['T']
    j.post(datetime.date.today(), Account(Guid(), 'Cash Account', 'Asset'), 10)
    assert j.postings[0].account.type == AccountType.ASSETS
    j.post(datetime.date.today(), Account(Guid(), 'Cash Account', 'Revenue'), -20)
    assert j.postings[1].account.type == AccountType.REVENUES

# Generated at 2022-06-14 04:12:11.635728
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    source = Asset("A")
    journal = JournalEntry(datetime.date.today(), "Description", source)
    journal.post(datetime.date.today(), Account("AA"), 100)
    journal.post(datetime.date.today(), Account("BB"), -100)

    # assert journal.postings == [
    #     Posting(journal, datetime.date.today(), Account("AA"), 1, 100),
    #     Posting(journal, datetime.date.today(), Account("BB"), -1, 100),
    # ]


# Generated at 2022-06-14 04:12:23.402822
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .ledgers import Ledger
    from .books import Book, BookReadAPI
    from .transactions import Transaction, TransactionReadAPI
    from .businesses import BusinessReadAPI, Party
    from .invoices import Invoice, InvoiceReadAPI, ReadInvoices

    ledger: Ledger = Ledger("Your Ledger")

    def read_businesses(period: DateRange) -> Iterable[Party]:
        return []

    def read_transactions(period: DateRange) -> Iterable[Transaction]:
        return []

    def read_invoices(period: DateRange) -> Iterable[Invoice]:
        return []

    bookreadapi: BookReadAPI[Transaction, Invoice] = BookReadAPI(
        read_transactions=read_transactions, read_invoices=read_invoices
    )


# Generated at 2022-06-14 04:12:32.652174
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class Source:
        pass

    @dataclass
    class DummyJournalEntry(JournalEntry[Source]):
        pass


# Generated at 2022-06-14 04:12:45.433750
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    class X:
        pass
    x1 = X()
    x2 = X()

    je = JournalEntry[X](datetime.date(2020, 2, 1), 'x', x1)
    je.post(datetime.date(2020, 2, 1), Account('a1', AccountType.ASSETS), 100)
    je.post(datetime.date(2020, 2, 1), Account('a2', AccountType.ASSETS), -100)
    je.post(datetime.date(2020, 2, 1), Account('a3', AccountType.ASSETS), 0)
    assert(len(je.postings) == 2)

    je2 = JournalEntry[X](datetime.date(2020, 2, 1), 'x', x2)

# Generated at 2022-06-14 04:12:52.375215
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Given
    entries = []
    # When
    ReadJournalEntries.__call__(entries, None)
    # Then
    pass

# Generated at 2022-06-14 04:13:05.471261
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():

    # ==========================================================================
    # Setup
    # ==========================================================================
    from datetime import date
    import time
    import unittest

    from .accounts import Account
    from .accounts import AccountHierarchy
    from .accounts import AccountType
    from .accounts import read_accounts
    from ..commons.numbers import Q

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[None]]:
        account_hierarchy = read_accounts()
        revenue_account, expense_account = account_hierarchy.get_accounts(
            {AccountType.REVENUES, AccountType.EXPENSES}
        )
        capital_account = account_hierarchy.get_account(Account("Capital"))


# Generated at 2022-06-14 04:13:08.935599
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry(date = "11/11/2020", description = "This is a test", source = "TRANSACTION")
    j.post(date = "11/11/2020", account = "ASSETS", quantity = 1000)
    j.validate()
    return

# Generated at 2022-06-14 04:13:09.641160
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:13:12.830870
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import Date

    class TestClass(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass
    TestClass()

# Generated at 2022-06-14 04:13:18.478456
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():

    @dataclass(frozen=True)
    class Foobar:
        pass

    def read_journal_entries_for_foobar(period: DateRange) -> Iterable[JournalEntry[Foobar]]:
        pass

    #: Defines a sample function that adheres to the `ReadJournalEntries` protocol.
    sample_1: ReadJournalEntries[Foobar] = read_journal_entries_for_foobar

    ## No error should occur given the above sample is properly typed:
    sample_1(period=DateRange(datetime.date.today(), datetime.date.today()))



# Generated at 2022-06-14 04:13:27.142602
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    inc = Account(AccountType.ASSETS, "Income")
    exp = Account(AccountType.EXPENSES, "Expenses")

    entry = JournalEntry[int](datetime.date.today(), "Test", 2)
    entry.post(datetime.date.today(), inc, 100)
    entry.post(datetime.date.today(), exp, -100)
    entry.validate()

    entry.post(datetime.date.today(), exp, -1)
    entry.validate()

# Generated at 2022-06-14 04:13:29.277881
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Unit test for method __call__ of class ReadJournalEntries
    """
    pass

# Generated at 2022-06-14 04:13:34.683055
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass
    class Entry(JournalEntry[None]):
        pass
    source: Iterable[JournalEntry[None]] = [Entry(date=datetime.date(2000, 1, 1), description="")]
    assert list(ReadJournalEntries.__call__(lambda: source)) == source
    assert list(ReadJournalEntries.__call__(lambda period: source)) == source

# Generated at 2022-06-14 04:13:43.844664
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # initialize three accounts
    from .accounts import ChartOfAccounts
    coa = ChartOfAccounts()
    coa.register_account({'code': 3020, 'name': 'Cash', 'category': 'Assets', 'group': 'Cash & Equivalents', 'type': 'Current Assets', 'subtype': 'Cash'})
    coa.register_account({'code': 4030, 'name': 'Accounts Receivable', 'category': 'Assets', 'group': 'Receivables', 'type': 'Current Assets', 'subtype': 'Accounts Receivable'})
    coa.register_account({'code': 6410, 'name': 'Accounts Payable', 'category': 'Liabilities', 'group': 'Payables', 'type': 'Current Liabilities', 'subtype': 'Accounts Payable'})

    # initialize 3

# Generated at 2022-06-14 04:13:58.369331
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import now
    from .accounts import Account
    from .books import Book

    book = Book()
    sales = book.create_account(AccountType.REVENUES, "Sales", code="4")
    salary = book.create_account(AccountType.REVENUES, "Salary")

    j = JournalEntry(now().date, "Expenses", "")

    j.post(now().date, sales, Quantity(13, 1000))
    j.post(now().date, salary, Quantity(11, 1000))

    print(j)



# Generated at 2022-06-14 04:14:07.073952
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal = "Journal"
    date = datetime.date(2020,3,27)
    account1 = "Account 1"
    account2 = "Account 2"
    amount = 1000
    quantity1 = 500
    quantity2 = -500
    j1 = JournalEntry(date, "description", journal, account1, quantity1)
    j2 = j1.post(date, account2, quantity2)
    for p in j2.postings:
        assert p.account in [account1,account2]

# Generated at 2022-06-14 04:14:14.519604
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Accounts
    from .accounts import AccountType

    accounts = Accounts()

    class MyAccount(accounts._AccountRegistrar):
        """
        My account.
        """

        def __init__(self):
            super().__init__("My Account", AccountType.ASSETS)

    my_account = MyAccount()

    # Create journal entries with different combinations of debit and credit.
    class MyBusinessObject:
        """
        My business object.
        """


# Generated at 2022-06-14 04:14:18.340349
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class T(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            raise NotImplementedError()

    T()

# Generated at 2022-06-14 04:14:26.581900
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Arrange
    class BusinessObject:
        pass
    journalEntry = JournalEntry(datetime.date(2020, 1, 1), "Description", BusinessObject())

    # Act
    journalEntry.post(datetime.date(2020, 1, 1), Account(AccountType.ASSETS, "A"), 10)
    journalEntry.post(datetime.date(2020, 1, 1), Account(AccountType.REVENUES, "R"), -10)

    # Assert
    assert len(journalEntry.postings) == 2

# Generated at 2022-06-14 04:14:28.532370
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .books import Book
    from .ledgers import Ledger
    from .periods import AccountingPeriod
    from .publications import Publication
    from .reader import Rea

# Generated at 2022-06-14 04:14:40.572821
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Create object of class JournalEntry
    journalEntry = JournalEntry(datetime.date(2019,11,8),"Test the method",None)
    journalEntry.post(datetime.date(2019,11,8),Account("Assets", AccountType.ASSETS),Amount(1.0))
    assert journalEntry.postings[0].amount == Amount(1.0)
    assert journalEntry.postings[0].account.name == "Assets"
    assert journalEntry.postings[0].direction == Direction.INC

    journalEntry.post(datetime.date(2019,11,8),Account("Assets", AccountType.ASSETS),Amount(-0.5))
    assert journalEntry.postings[1].amount == Amount(0.5)
    assert journalEntry.postings[1].account.name == "Assets"
    assert journal

# Generated at 2022-06-14 04:14:49.278581
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    ce = JournalEntry(datetime.date(2020,5,10), "some text", "some other text")
    ce.post(datetime.date(2020,5,10), "account", 2)
    assert ce.postings[0].journal == ce
    assert ce.postings[0].date == datetime.date(2020,5,10)
    assert ce.postings[0].account == "account"
    assert ce.postings[0].direction == Direction.INC
    assert ce.postings[0].amount == 2
    assert ce.postings[0].is_debit is True
    assert ce.postings[0].is_credit is False
    assert list(ce.increments) == [ce.postings[0]]
    assert list(ce.debits) == [ce.postings[0]]
    print

# Generated at 2022-06-14 04:14:54.990076
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    def act():
        journal_entry = JournalEntry(1)
        journal_entry.post(2, 3, 4)
        return journal_entry
    journal_entry = act()
    assert journal_entry.postings[0].date == 2
    assert journal_entry.postings[0].account == 3
    assert journal_entry.postings[0].amount == 4

# Generated at 2022-06-14 04:15:06.366201
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from .mapping import AccountMapping, AccountMappingType
    posting = None
    journal = JournalEntry[AccountMapping](datetime.date(2020, 5, 21), "", AccountMapping(AccountMappingType.GLOBAL, Guid("b064c62f-7c51-43e9-9f5d-63a647d15a1c")))
    posting = journal.post(datetime.date(2020, 5, 21), Account(AccountType.ASSETS, Guid("b064c62f-7c51-43e9-9f5d-63a647d15a1c"), ""), 1000)

# Generated at 2022-06-14 04:15:30.640292
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():

    from datetime import date
    from .accountsets import AccountSet
    from .accounts import Account
    from .tags import Tag
    from .segments import Segment

    accounts = AccountSet()
    accounts.register(Account("Assets", AccountType.ASSETS))
    accounts.register(Account("Liabilities", AccountType.LIABILITIES))
    accounts.register(Account("Revenues", AccountType.REVENUES))
    accounts.register(Account("Expenses", AccountType.EXPENSES))
    accounts.register(Account("Equities", AccountType.EQUITIES))
    accounts.register(Account("Equities-OpeningBalances", AccountType.EQUITIES, tags=[Tag("Equities", "RetainedEarnings")], segments=[Segment("Equities", "OpeningBalances")]))


# Generated at 2022-06-14 04:15:33.763345
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    tran = JournalEntry(datetime.date.today(), "test", "test")
    tran.post(datetime.date.today(), Account(), 10)
    tran.post(datetime.date.today(), Account(), -10)
    tran.validate()

# Generated at 2022-06-14 04:15:38.628201
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    d = datetime.date(2020, 4, 9)
    j = JournalEntry[int](d, "Test", 1)
    j.post(d, Account("Cash", AccountType.ASSETS, ""), 100)
    j.post(d, Account("Services", AccountType.EXPENSES, "Labor"), -100)
    j.validate()

# Generated at 2022-06-14 04:15:45.078747
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from operator import __call__

    class Source:
        def journal(self, period):
            return list()

    source = Source()
    func = ReadJournalEntries.__getitem__(type(source))(source.journal)
    assert isinstance(func, ReadJournalEntries)
    assert func.__qualname__ == "<lambda>", "Closure object should have __qualname__ of '<lambda>'"
    assert func is __call__(func)

# Generated at 2022-06-14 04:15:54.736510
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from .currencies import Currency
    from .money import Money
    from ..commons.numbers import Quantity

    journal = JournalEntry[str](datetime.date.today(), "Test journal entry", "Test")
    journal.post(datetime.date.today(), 
                 Account("Assets", "Cash", AccountType.ASSETS), 
                 Quantity(100))
    journal.post(datetime.date.today(), 
                 Account("Expenses", "Food", AccountType.EXPENSES),
                 Quantity(-100))
    journal.validate()

if __name__ == "__main__":
    print("Running journal tests...")
    test_JournalEntry_post()
    print("All journal tests passed.")

# Generated at 2022-06-14 04:16:05.751986
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    prev_period_je = JournalEntry(datetime.date(2020, 5, 3),"hi",None)
    prev_period_je.post(datetime.date(2020, 5, 1), Account("Assets", AccountType.ASSETS), Quantity(1000))
    prev_period_je.post(datetime.date(2020, 5, 1), Account("Revenues", AccountType.REVENUES), Quantity(1000))

    # Test for when total debit and total credit are equal
    assert prev_period_je.debits == prev_period_je.credits

    # Test for when total debit and total credit are not equal
    prev_period_je.post(datetime.date(2020, 5, 1), Account("Revenues", AccountType.REVENUES), Quantity(100))
    assert prev_period_je.debits != prev_period

# Generated at 2022-06-14 04:16:13.035104
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from ..commons.numbers import Amount, Quantity
    from .core import Currency

    eur = Currency("EUR")
    usd = Currency("USD")

    Account("cash", AccountType.ASSETS)

    Account("revenue", AccountType.REVENUES)

    Account("expense", AccountType.EXPENSES)

    Account("equity", AccountType.EQUITIES)

    Account("liability", AccountType.LIABILITIES)

    usd_cash_account = Account("usd-cash", AccountType.ASSETS, usd)
    eur_cash_account = Account("eur-cash", AccountType.ASSETS, eur)

    usd_revenue_account = Account("usd-revenue", AccountType.REVENUES, usd)
    eur_

# Generated at 2022-06-14 04:16:20.199073
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Ledger

    # arrange
    ledger = Ledger()
    root = ledger.root
    j1 = JournalEntry(datetime.date.today(), "j1", None)
    a1 = ledger.create(root, "a1")
    b1 = ledger.create(root, "b1")
    a2 = ledger.create(root, "a2")
    b2 = ledger.create(root, "b2")

    # act
    j2 = j1.post(datetime.date.today(),a1,500)

    # assert
    assert j1 == j2



# Generated at 2022-06-14 04:16:31.676029
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Test the method post of class JournalEntry.
    """
    from .accounts import Account, AccountType
    from .commons.numbers import Amount, Quantity

    # Create object account
    account = Account(AccountType.ASSETS, "Cash")

    # Create object journal_entry
    journal_entry = JournalEntry(datetime.datetime.now().date(), "description", "source")

    # Check the first value of list attribute postings
    assert not journal_entry.postings

    # Add a new value to list attribute postings
    journal_entry.post(datetime.datetime.now().date(), account, Quantity(100))

    # Check the first value of list attribute postings
    assert journal_entry.postings[0].date == datetime.datetime.now().date()

# Generated at 2022-06-14 04:16:41.551018
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    acc1 = Account("1100", "Cash")
    # Create first journal entry with two postings
    j1 = JournalEntry(datetime.date(2020, 9, 1), description="Sale", source="Sale of goods")
    j1.post(date=j1.date, account=acc1, quantity=12000)
    j1.post(date=j1.date, account=acc1, quantity=-12000)
    # Create second journal entry with one posting
    j2 = JournalEntry(datetime.date(2020, 9, 1), description="Sale", source="Sale of goods")
    j2.post(date=j2.date, account=acc1, quantity=12000)
    # Validate journal entry with two postings
    j1.validate()
    # Try to validate journal entry with one posting

# Generated at 2022-06-14 04:17:17.759232
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    #
    # Test validity of postings
    #
    journal = JournalEntry(datetime.date(2020, 1, 1), "Test1", 2)
    journal.post(datetime.date(2020, 1, 1), Account.new_assets_account(1, "Cash"), 1000)
    journal.post(datetime.date(2020, 1, 1), Account.new_expenses_account(2, "Salaries Payable"), -1000)
    journal.validate()

    #
    # Test if postings are immutable
    #
    postings = journal.postings.copy()
    journal.post(datetime.date(2020, 1, 1), Account.new_assets_account(1, "Cash"), 1000)
    assert journal.postings == postings


# Generated at 2022-06-14 04:17:24.074326
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    account1 = Account("a1", AccountType.ASSETS)
    account2 = Account("a1", AccountType.EXPENSES)
    je = JournalEntry("1", "desc", None)

    je.post(datetime.date.today(), account1, 100)
    je.post(datetime.date.today(), account1, -50)
    je.post(datetime.date.today(), account2, -110)
    je.validate()

# Generated at 2022-06-14 04:17:32.041102
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.numbers import Amount
    #: Date of the entry.
    date = datetime.date(2019,10,10)
    #: Description of the entry.
    description = "Test Posting"
    #: Business object as the source of the journal entry.
    source = "abc"
    #: Postings of the journal entry.
    postings = []
    #: Globally unique, ephemeral identifier.
    guid = "Guid"
    #: Class object
    journal_entry = JournalEntry(date,description,source,postings,guid)
    #: Object property - guid
    guid1 = journal_entry.guid

    #: Object property - date
    date1 = journal_entry.date
    #print(date1)

    #: Object property - description

# Generated at 2022-06-14 04:17:40.286618
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    source = ','
    date = datetime.date(2020,1,1)
    account = Account('00001', 'Asset', AccountType.ASSETS)
    quantity = Quantity(10, 'g')
    je = JournalEntry(date, 'testing', source)
    result = je.post(date, account, quantity)
    assert type(result) == JournalEntry, 'post to JournalEntry should return JournalEntry'
    assert hasattr(je, 'postings'), 'JournalEntry should have postings'
    assert type(je.postings) == list, 'JournalEntry postings should be list'
    assert len(je.postings) == 1, 'JournalEntry postings should have 1 element'


# Generated at 2022-06-14 04:17:45.676462
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    account : Account 
    account = Account('ABC',AccountType.ASSETS)

    entry : JournalEntry
    entry = JournalEntry(datetime.date(2018,1,1), "Test", None)

    assert len(entry.postings) == 0
    entry.post(datetime.date(2018,1,1), account, Quantity(0))
    assert len(entry.postings) == 0
    entry.post(datetime.date(2018,1,1), account, Quantity(10))
    assert len(entry.postings) == 1
    entry.post(datetime.date(2018,1,1), account, Quantity(-10))
    assert len(entry.postings) == 2

# Generated at 2022-06-14 04:17:53.142983
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account

    acc = Account(id="A1", type=AccountType.EXPENSES)
    je = JournalEntry(date=datetime.date(2018, 10, 10), description="Test", source=None)
    assert len(je.debits) == 0
    assert len(je.credits) == 0
    je.post(datetime.date(2018, 10, 10), acc, 5)
    assert len(je.debits) == 1
    assert len(je.credits) == 0

# Generated at 2022-06-14 04:18:00.471310
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountFactory

    entry = JournalEntry(datetime.date(2020, 6, 18), "Test Posting", "Test Business Object")
    asset = AccountFactory.assets("Cash in Wallet", "A1")
    entry.post(datetime.date(2020, 6, 18), asset, 1000)
    entry.post(datetime.date(2020, 6, 18), asset, -500)

    assert entry.postings[0].account == entry.postings[1].account
    assert entry.postings[0].account == asset
    assert entry.postings[0].is_debit and entry.postings[1].is_credit
    assert entry.postings[0].amount.value == 1000 and entry.postings[1].amount.value == 500
    assert entry.postings[0].direction == Direction.INC and entry

# Generated at 2022-06-14 04:18:11.533404
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class Data:
        obj: object
        period: DateRange

    import datetime
    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from .accounts import AccountList

    class AccountListFake:
        def get(self, name: str) -> Account:
            return Account(name)

    class ReadJournalEntriesFake:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return [
                JournalEntry(
                    date=datetime.date(2020, 1, 1),
                    description="",
                    source=Data(1, period)
                )
            ]

    fake: ReadJournalEntries = ReadJournalEntriesFake()

# Generated at 2022-06-14 04:18:13.088522
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Test JournalEntry.validate()
    """

    pass

# Generated at 2022-06-14 04:18:20.307372
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # GIVEN
    source = object()
    today = datetime.date.today()
    entry = JournalEntry[object](date=today, description="entry", source=source)

    # WHEN
    entry.post(today, Account("11.00", AccountType.ASSETS, "Cash"), +100)
    entry.post(today, Account("11.01", AccountType.ASSETS, "Postdated Check"), -100)

    # THEN
    entry.validate()

    # GIVEN
    entry = JournalEntry[object](date=today, description="entry", source=source)

    # WHEN
    entry.post(today, Account("11.00", AccountType.ASSETS, "Cash"), +100)
    entry.post(today, Account("11.01", AccountType.ASSETS, "Postdated Check"), -101)

   

# Generated at 2022-06-14 04:19:28.394807
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    account = Account('430000', 'Expense', 'Expense')
    date = datetime.date.today()
    quantity = Quantity(1000)

    journal_entry = JournalEntry(date = date, description = "test journal entry", source = None)
    journal_entry.post(date, account, quantity)

    assert journal_entry.postings[0].date == date
    assert journal_entry.postings[0].account == account
    assert journal_entry.postings[0].direction == Direction.DEC
    assert journal_entry.postings[0].amount == Amount(1000)

# Generated at 2022-06-14 04:19:29.027169
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass

# Generated at 2022-06-14 04:19:29.989771
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountRepository

    assert True

# Generated at 2022-06-14 04:19:37.558455
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    
    # create account
    account = Account.create(account_type=AccountType.ASSETS, parent=None, name='asset_account')
    # create journal entry
    journal = JournalEntry[object]()
    # create date
    date = datetime.date.today()
    # create quantity
    quantity = 100
    # test post method
    journal.post(date=date, quantity=quantity, account=account)
    # check postings
    assert tuple(journal.postings)[-1].amount == quantity
    assert tuple(journal.postings)[-1].account == account
    assert tuple(journal.postings)[-1].date == date
    assert tuple(journal.postings)[-1].direction == Direction.INC
    assert tuple(journal.postings)[-1].is_debit


# Generated at 2022-06-14 04:19:38.658655
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # TODO: Implement
    pass

# Generated at 2022-06-14 04:19:50.862712
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
  je = JournalEntry(date = datetime.date(2019,12,31), description = "test Journal entrée")
  post1 = je.post(date = datetime.date(2019,12,31), account = Account('CODE_1', 'NAME_1', AccountType.ASSETS), quantity = 1)

  assert post1.postings[0].date == post1.date
  assert post1.postings[0].account.code == 'CODE_1'
  assert post1.postings[0].amount == 1

  post2 = je.post(date = datetime.date(2020,1,1), account = Account('CODE_2', 'NAME_2', AccountType.REVENUES), quantity = 2)
  assert post2.postings[0].date == datetime.date(2020,1,1)

# Generated at 2022-06-14 04:20:02.515986
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .currencies import Currency

    # Create a dummy callable for 'ReadJournalEntries'
    def dummy_fn(period: DateRange) -> Iterable[JournalEntry[str]]:
        yield JournalEntry(
            datetime.date(2020, 4, 1), "Dummy Entry 1", "Source 1", [
                Posting(None, datetime.date(2020, 4, 1), Account(None, "Salaries Account", AccountType.EXPENSES), Direction.INC, Amount(Currency.USD, 100))
            ]
        )

# Generated at 2022-06-14 04:20:03.534811
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass



# Generated at 2022-06-14 04:20:12.945247
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..domain.ledgers import JournalEntrySource
    from ..domain.repositories import Repository
    from .accounts import Account, AccountType

    def post_transactions(journal: JournalEntrySource[Repository], period: DateRange):
        for i in range(0, 10):
            journal.post_begin() \
                .post(datetime.date(2019, 10, 10), account=Account(f"Debit-Account-{i}", AccountType.ASSETS),
                      quantity=100 * i) \
                .post(datetime.date(2019, 10, 10), account=Account(f"Credit-Account-{i}", AccountType.EXPENSES),
                      quantity=-100 * i) \
                .post_end()

# Generated at 2022-06-14 04:20:23.153447
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime
    from dokusan.accounting.core.accounts import *
    from dokusan.accounting.core.documents import Document
    
    # Create an empty journal entry
    entry1 = JournalEntry(datetime.date.today(), 'Opening Balance', Document())
    # Post an amount to a revenue account
    entry1.post(datetime.date.today(), Account(AccountType.REVENUES, 'Sales'), 1000)
    # Post an amount to a liability account
    entry1.post(datetime.date.today(), Account(AccountType.LIABILITIES, 'Sales Tax Payable'), 200)
    
    print(entry1)
    print(entry1.postings)
    print(entry1.debits)
    print(entry1.decrements)
    print(entry1.increments)
    print