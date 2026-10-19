

# Generated at 2022-06-14 04:11:27.232501
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from hypothesis import example, given
    from hypothesis.strategies import lists, sampled_from
    import pytest
    from .domain import accounts
    from .domain.accounts import AccountName
    from .domain.sources import Source

    ## Test strategy generator:
    @given(lists(sampled_from(accounts), min_size=2, max_size=2))
    @example([accounts["cash"], accounts["equity"]])
    @example([accounts["cash"], accounts["equity"]])
    @example([accounts["cash"], accounts["revenue"]])
    @example([accounts["cash"], accounts["expense"]])
    def test_read_journal_entries(accounts: List[Account]) -> None:
        ## Arrange:
        assert len(accounts) == 2
        source = Source()
        ##

# Generated at 2022-06-14 04:11:33.386996
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    rf = JournalEntry()
    rf.post(datetime.date(2019,1,25), Account("cash"), Amount(10))
    rf.post(datetime.date(2019,1,25), Account("revenue"), Amount(5))
    rf.validate()


# Generated at 2022-06-14 04:11:43.818957
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from hamcrest import assert_that, contains_inanyorder, instance_of
    from .accounts import real_account

    def _():
        yield JournalEntry(datetime.date(2018, 1, 1), "A", None)
        yield JournalEntry(datetime.date(2018, 2, 1), "A", None)
        yield JournalEntry(datetime.date(2018, 3, 1), "A", None)
        yield JournalEntry(datetime.date(2018, 4, 1), "A", None)
        yield JournalEntry(datetime.date(2018, 5, 1), "A", None)
        yield JournalEntry(datetime.date(2018, 6, 1), "A", None)
        yield JournalEntry(datetime.date(2018, 7, 1), "A", None)

# Generated at 2022-06-14 04:11:54.929952
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    date1 = datetime.date(2018,6,1)
    date2 = datetime.date(2018,6,2)

    jentry = JournalEntry[str](date1, "Des", "Sou")
    jentry.post(date1, Account("Expenses", "Expense"), +100)
    jentry.post(date1, Account("Cash", "Asset"), +100)

    jentry.post(date2, Account("Accounts Receivable", "Asset"), +100)
    jentry.post(date2, Account("Revenue", "Revenue"), +100)
    jentry.validate()

    assert jentry.date == date1
    assert jentry.description == "Des"
    assert jentry.source == "Sou"
    assert jentry.postings[0].account.name == "Expenses"


# Generated at 2022-06-14 04:12:03.999535
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Define _T
    _T = int

    # Construct journal entry
    entry = JournalEntry(_T(20171028), "Payroll", _T(1), list())

    # Get postings
    postings = entry.postings

    # Validate postings
    assert postings == list()

    # Perform post
    entry = entry.post(datetime.date(2017, 10, 28), Account("Cash"), 10)

    # Get postings
    postings = entry.postings

    # Validate postings
    assert postings == [Posting(entry, datetime.date(2017, 10, 28), Account("Cash"), Direction.INC, Amount(10))]

    # Perform post
    entry = entry.post(datetime.date(2017, 10, 28), Account("Payroll Expense"), 10)

    # Get postings
    postings = entry.postings



# Generated at 2022-06-14 04:12:10.476911
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    acc1 = Account("Acc1", "Assets")
    acc2 = Account("Acc2", "Expenses")
    acc3 = Account("Acc3", "Assets")
    acc4 = Account("Acc4", "Equities")

    today = datetime.datetime.today()
    je1 = JournalEntry(today, "test 1", "test source")
    je1.post(today, acc1, Amount("100.00"))
    je1.post(today, acc2, Amount("100.00"))
    je1.validate()

    je2 = JournalEntry(today, "test 2", "test source")
    je2.post(today, acc1, Amount("100.00"))
    je2.post(today, acc2, Amount("50.00"))

# Generated at 2022-06-14 04:12:11.412355
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    l = JournalEntry.postings
    print(l)

# Generated at 2022-06-14 04:12:21.780797
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Arrange
    from .accounts import AccountType
    from .placebo import PlaceboDatabase

    # Act
    a1 = PlaceboDatabase.accounts.lookup(AccountType.ASSETS, "Cash")
    a2 = PlaceboDatabase.accounts.lookup(AccountType.EXPENSES, "Salary")
    je = JournalEntry[None](datetime.date(2020, 7, 1), "Pay Salary", None) \
        .post(datetime.date(2020, 7, 1), a1, -100_000) \
        .post(datetime.date(2020, 7, 1), a2, 100_000)

    # Assert
    je.validate()

# Generated at 2022-06-14 04:12:30.857635
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal = JournalEntry[str](datetime.date(2020, 6, 29), "Test Journal Entry", "Test Business Object")
    journal.post(datetime.date(2020, 6, 29), Account.ASSET_CASH, +1000)
    journal.post(datetime.date(2020, 6, 29), Account.REVENUE_REVENUE, -1000)
    journal.post(datetime.date(2020, 6, 29), Account.ASSET_CASH, 5000)
    journal.post(datetime.date(2020, 6, 29), Account.EXPENSE_MACHINES, -5000)
    journal.post(datetime.date(2020, 6, 29), Account.ASSET_INVENTORY, +10000)
    journal.validate()

# Generated at 2022-06-14 04:12:37.328682
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import read_accounts
    from .read_journal_entries import read_journal_entries
    accounts = read_accounts("./data/accounts.json")

    for period in (DateRange(datetime.date(2019, 4, 1), datetime.date(2019, 4, 30)),):
        journal_entries = read_journal_entries("./data/journal-entries.json", accounts)(period)
        merged_journal_entries = list(journal_entries)  # read into memory before assertions
        i = 0  # index
        assert len(merged_journal_entries) == 1
        j = merged_journal_entries[i]
        assert j.date == datetime.date(2019, 4, 1)
        assert j.description == "Salary for April"

# Generated at 2022-06-14 04:12:52.348292
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from ..commons.testings import capture_stdout_stderr, redirect_stdout_stderr
    from .accounts import AccountType
    from .accounts import Account as acct
    from .accounts import Currency as ccy

    class Source:
        pass

    # Test 1
    date = datetime.datetime(2020, 1, 1)
    with capture_stdout_stderr() as (stdout, stderr):
        entry = JournalEntry(date, "Test Journal Entry", Source())
        entry = entry.post(date, acct(ccy, AccountType.ASSETS, "ASSETS.CASH"), +100)
        entry = entry.post(date, acct(ccy, AccountType.EXPENSES, "EXPENSES.DONATIONS"), -100)
        entry.validate()


# Generated at 2022-06-14 04:12:53.425854
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass


# Generated at 2022-06-14 04:13:06.346638
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Test data
    j1 = JournalEntry(datetime.date(2019, 2, 1), "journal-1", None)
    j2 = JournalEntry(datetime.date(2019, 2, 2), "journal-2", None)
    j3 = JournalEntry(datetime.date(2019, 2, 3), "journal-3", None)
    journal_entries = [j1, j2, j3]
    period = DateRange(datetime.date(2019, 2, 2), datetime.date(2019, 2, 3))

    # Test code
    def read_journal_entries():
        return journal_entries

    # Assertions
    assert list(read_journal_entries(period)) == [j2, j3] # type: ignore[arg-type]


# Generated at 2022-06-14 04:13:16.364991
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime
    from gilded.commons.numbers import Amount, Quantity
    from gilded.commons.others import makeguid
    from gilded.model.accounts import Account, AccountType
    from gilded.model.journal import JournalEntry
    from gilded.model.ledger import Ledger

    class DummyJournalEntry(JournalEntry):
        pass


    # Define a ledger:
    ledger = Ledger()

    # Create an entry:
    entry = DummyJournalEntry(date=datetime.date(2020, 1, 1), description="test", source=None)

    # Post to accounts:
    entry.post(date=entry.date, account=ledger.accounts.balance_sheet.assets.cash, quantity=Amount(2000))

# Generated at 2022-06-14 04:13:24.212154
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry(
        date=datetime.date(2019, 12, 1),
        description='Validating Journal Entry',
        source='Some source',
    )

    je.post(date=datetime.date(2019, 12, 1), account='123', quantity=100)
    je.post(date=datetime.date(2019, 12, 1), account='456', quantity=-100)
    je.validate()
    return

# Generated at 2022-06-14 04:13:31.262862
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    je = JournalEntry(datetime.date(2020, 1, 1), "", object())
    je.post(datetime.date(2020, 1, 1), Account("Assets", "Cash"), 10000)
    assert je.postings[0].amount == Amount(10000)
    assert je.postings[0].direction == Direction.INC
    assert je.postings[0].is_debit == True
    assert je.postings[0].is_credit == False


# Generated at 2022-06-14 04:13:32.211531
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    assert True

# Generated at 2022-06-14 04:13:41.135702
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    journal_entry = JournalEntry[int](datetime.date(2019, 11, 7), 'Payment to A', 74440)
    journal_entry.post(datetime.date(2019, 11, 7), Account('Cheque', 'Bank', AccountType.ASSETS), -1000)
    journal_entry.post(datetime.date(2019, 11, 7), Account('Equity', 'Capital', AccountType.EQUITIES), 1000)
    journal_entry.validate()

    assert journal_entry.postings[0].direction == Direction.DEC
    assert journal_entry.postings[1].direction == Direction.INC

# Generated at 2022-06-14 04:13:51.912671
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountType, ReadAccounts

    account1 = Account("Account1", AccountType.ASSETS)
    account2 = Account("Account2", AccountType.REVENUES)

    # Create a dummy client:
    @dataclass(frozen=True)
    class Client:
        name: str

    client = Client("Client ABC Pty Ltd")
    je = JournalEntry(datetime.date(2020, 4, 1), "Foo", client)

    # Add some postings:
    # debits(increments):
    je.post(datetime.date(2020, 4, 1), account1, Quantity(15))

# Generated at 2022-06-14 04:13:57.097466
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import dataclass
    @dataclass(frozen=True)
    class ReadJournalEntriesDummy(ReadJournalEntries[object]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[object]]:
            return ()

    ReadJournalEntriesDummy()(DateRange(datetime.date(2020, 4, 1), datetime.date(2020, 4, 30)))

# Generated at 2022-06-14 04:14:26.008355
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    je1 = JournalEntry[int](date=datetime.date(day=8, month=10, year=2018), description='Transfering to bank #1', source=0)
    je1.post(date=datetime.date(day=8, month=10, year=2018), account=Account('Bank Account #1', AccountType.ASSETS), quantity=10)
    je1.post(date=datetime.date(day=8, month=10, year=2018), account=Account('Cash on Hand', AccountType.ASSETS), quantity=-10)
    print(f'Journal Entry: {je1}')

    je1.validate()

    je2 = JournalEntry[int](date=datetime.date(day=8, month=10, year=2018), description='Transfering to bank #1', source=0)
    je

# Generated at 2022-06-14 04:14:38.054258
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    account1 = Account('Assets', 'Bank', 'Current Account')
    account2 = Account('Liability', 'Credit Card', '1234567890')

    transaction = JournalEntry(datetime.date.today(), 'description', 'source')
    assert transaction.post(datetime.date.today(), account1, 100) == transaction
    assert transaction.post(datetime.date.today(), account2, -100) == transaction
    assert len(transaction.postings) == 2

    assert transaction.postings[0].journal == transaction
    assert transaction.postings[0].date == datetime.date.today()
    assert transaction.postings[0].account == account1
    assert transaction.postings[0].direction == Direction.INC
    assert transaction.postings[0].amount == Amount(100)

# Generated at 2022-06-14 04:14:47.932197
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import dateutil.parser

    # Setup:

# Generated at 2022-06-14 04:14:58.111770
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Note: doctest is not used because it is a class.
    @dataclass(frozen=True)
    class Sample(ReadJournalEntries[str]):
        data: List[JournalEntry[str]] = field(default_factory=list)

    now = datetime.date.today()
    delta = datetime.timedelta(days=1)
    sample = Sample(
        data=[
            JournalEntry(now, "1", "",),
            JournalEntry(now - delta, "2", ""),
            JournalEntry(now + delta, "3", ""),
        ]
    )
    assert list(sample(DateRange.of_single_day(now))) == [sample.data[0]]

# Generated at 2022-06-14 04:15:04.843627
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry[str](date = datetime.date.today(), description = "Sample Journal Entry", source = "Sample Source")
    je.post(date = datetime.date.today(), account = Account("Assets", AccountType.ASSETS), quantity = 10)
    je.post(date = datetime.date.today(), account = Account("Equities", AccountType.EQUITIES), quantity = -10)
    je.validate()

# Generated at 2022-06-14 04:15:13.664152
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    from .accounts import Ledger
    from .accounts import Organization
    from datetime import date
    from .accounts import Amount as AccountAmount

    org: Organization = Organization(name="The Org")
    ledger: Ledger = Ledger()
    amount: AccountAmount = AccountAmount(100)
    targetdate: date = date(2019, 3, 1)
    duration = DateRange(date(1970, 1, 1), date(2060, 1, 1))

# Generated at 2022-06-14 04:15:23.482695
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType

    journal = JournalEntry(datetime.date(2020, 10, 1), "Test journal entry.", "Test source")
    assert journal.postings == []
    assert journal.is_balanced() == True

    journal.post(datetime.date(2020, 10, 1), Account("Test account", AccountType.ASSETS), Quantity(10))
    assert journal.postings != []
    assert len(journal.postings) == 1
    assert journal.is_balanced() == True

    journal.post(datetime.date(2020, 10, 1), Account("Test account", AccountType.ASSETS), Quantity(-10))
    assert len(journal.postings) == 2
    assert journal.is_balanced() == True



# Generated at 2022-06-14 04:15:33.180590
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.numbers import Amount, Quantity
    from ..entities.accounts import Account, AccountType
    je = JournalEntry()
    je.post(datetime.date(2019, 12, 31), Account("Bank", AccountType.ASSETS), Quantity(100))
    assert len(je.postings) == 1
    assert je.postings[0].date == datetime.date(2019, 12, 31)
    assert je.postings[0].account.name == "Bank"
    assert je.postings[0].account.type == AccountType.ASSETS
    assert je.postings[0].direction == Direction.INC
    assert je.postings[0].amount == Amount(100)

    je.post(datetime.date(2019, 12, 31), Account("Salary", AccountType.REVENUES), Quantity(-100))

# Generated at 2022-06-14 04:15:39.003863
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Arrange
    from .accounts import AccountType
    from .ledger import Ledger

    ledger = Ledger(name="Test")
    ledger.create_account(account="SAVINGS", type=AccountType.ASSETS)
    ledger.create_account(account="INCOME", type=AccountType.REVENUES)
    ledger.create_account(account="EXPENSE", type=AccountType.EXPENSES)
    ledger.create_account(account="EQUITY", type=AccountType.EQUITIES)
    entry = JournalEntry(date=datetime.date(2019, 9, 1),
                         description="Credit income, debit expense and debit income")
    entry.post(datetime.date(2019, 9, 1), ledger.account("SAVINGS"), +100)

# Generated at 2022-06-14 04:15:49.825245
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j = JournalEntry(datetime.date.today(), "Description", None)
    j.post(datetime.date.today(), Account("Assets", AccountType.ASSETS), Quantity(100))
    j.post(datetime.date.today(), Account("Equities", AccountType.EQUITIES), Quantity(100))
    j.post(datetime.date.today(), Account("Revenues", AccountType.REVENUES), Quantity(100))
    j.post(datetime.date.today(), Account("Expenses", AccountType.EXPENSES), Quantity(100))
    assert len(j.postings) == 4
    assert j.postings[0].is_debit
    assert j.postings[1].is_debit
    assert j.postings[2].is_credit
    assert j.postings[3].is_

# Generated at 2022-06-14 04:16:08.384581
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..core.accounts import Account, AccountType
    from ..core.journal.journal_entry import JournalEntry
    je = JournalEntry(date=datetime.date.today(), description='abc', source=None)
    je.post(date=datetime.date.today(), account=Account('XYZ', AccountType.EXPENSES), quantity=123)
    je.post(date=datetime.date.today(), account=Account('X', AccountType.LIABILITIES), quantity=-321)
    je.validate()

# Generated at 2022-06-14 04:16:15.741734
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    a = Account("a", 0)
    b = Account("b", 0)
    journal = JournalEntry(datetime.date(2019, 1, 1), "test journal")
    journal.post(datetime.date(2019, 1, 1), a, 10)
    journal.post(datetime.date(2019, 1, 1), b, -10)
    journal.validate()

# Generated at 2022-06-14 04:16:22.740730
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..ledger.accounts import AccountType, ExpenseAccount, FluctuatingAccount, RevenueAccount
    from ..ledger.events import Event, EventStatus
    from .events import EventSubType, IncomeStatementEventType

    # Arrange, Act and Assert
    j = JournalEntry[Event]()
    j.post(date=datetime.date(2019, 1, 1), account=RevenueAccount("R"), quantity=10)
    j.post(date=datetime.date(2019, 1, 1), account=ExpenseAccount("E"), quantity=10)
    j.validate()
    assert len(j.postings) == 2

    # Arrange, Act and Assert
    j = JournalEntry[Event]()

# Generated at 2022-06-14 04:16:32.505816
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..services.accounts import Account
    from .book import Book, BookConstructor
    test_coa = Account.get_default_instance()
    test_book = Book('testbook', 'testbook', test_coa)
    test_date = datetime.date(2018, 1, 1)
    test_desc = 'test_desc'
    test_source = 'test_source'
    test_posting = JournalEntry(test_date, test_desc, test_source)

    test_posting.post(test_date, test_coa.revenues, -50)
    test_posting.post(test_date, test_coa.liabilities, 50)
    test_posting.validate()


if __name__ == "__main__":
    print("Running", __file__)
    test

# Generated at 2022-06-14 04:16:41.973571
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    class InsurancePolicy:
        pass
    p1 = InsurancePolicy()
    p2 = InsurancePolicy()
    j1 = JournalEntry(datetime.date(2020, 5, 21), 'Anniversary payment', p1)
    j2 = JournalEntry(datetime.date(2020, 5, 22), 'Quarterly payment', p2)
    exp1 = [Posting(j1,datetime.date(2020, 5, 21),Account(1,'Property',AccountType.ASSETS),Direction.INC, Amount(100)),
            Posting(j1,datetime.date(2020, 5, 21),Account(2,'Premium',AccountType.REVENUES),Direction.DEC, Amount(100))]

# Generated at 2022-06-14 04:16:48.137687
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    account1 = Account('1', 'Assets', 'Cash', AccountType.ASSETS)
    account2 = Account('2', 'Revenues', 'Revenues', AccountType.REVENUES)
    j = JournalEntry[int](datetime.date.today(), "test", 2)
    j.post(datetime.date.today(), account1, 5)
    j.post(datetime.date.today(), account2, -5)
    j.validate()

# Generated at 2022-06-14 04:16:58.349904
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Declare a class to use in testing:
    class Entry:
        def __init__(self, date, description, source):
            self.date = date
            self.description = description
            self.source = source
    # Create some entries:
    entries = [
        Entry(datetime.date(2017, 1, 1), "Foo", "Bar"),
        Entry(datetime.date(2017, 2, 1), "Foo", "Bar"),
        Entry(datetime.date(2017, 3, 1), "Foo", "Bar"),
        Entry(datetime.date(2017, 4, 1), "Foo", "Bar"),
    ]
    # Define a read function:

# Generated at 2022-06-14 04:17:08.235088
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    entries = [
        JournalEntry(datetime.date(year=2020, month=1, day=1), description="Entry 1", source=None),
        JournalEntry(datetime.date(year=2020, month=1, day=2), description="Entry 2", source=None),
        JournalEntry(datetime.date(year=2020, month=2, day=1), description="Entry 3", source=None),
    ]
    # If a date range is given, filter by that range only:
    assert list(ReadJournalEntries(lambda period: entries)(DateRange(datetime.date(year=2020, month=1, day=1), datetime.date(year=2020, month=1, day=31)))) == [
        entries[0],
        entries[1],
    ]
    # If None is given, return everything:

# Generated at 2022-06-14 04:17:13.171517
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j1 = JournalEntry(date=datetime.date(2014, 1, 1), description="sample")
    j1.post(date=datetime.date(2014, 1, 1), account=Account(code="cash", name="Cash In Hand", type=AccountType.ASSETS), quantity=100)
    j1.post(date=datetime.date(2014, 1, 1), account=Account(code="capital", name="Owner's Equity", type=AccountType.EQUITIES), quantity=-100)
    j1.validate()

    j2 = JournalEntry(date=datetime.date(2014, 1, 2), description="sample")
    j2.post(date=datetime.date(2014, 1, 2), account=Account(code="cash", name="Cash In Hand", type=AccountType.ASSETS), quantity=0)
    j

# Generated at 2022-06-14 04:17:15.650959
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class MyClass:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return period
    obj = MyClass()
    assert obj.__call__(DateRange())

# Generated at 2022-06-14 04:17:54.775365
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons import CurrentDate
    from .accounts import Account
    from .accounts import InMemoryAccountRepository
   
    def CurrentDate_now():
        return datetime.date(2020, 7, 26)

    CurrentDate.now = CurrentDate_now

    def find(account_name: str) -> Account:
        return InMemoryAccountRepository.find(account_name)

    # Debit to Expense:
    journal = JournalEntry(date = datetime.date(2020, 7, 24), description = "Test Journal Entry", source = "Test Journal Entry")
    journal.post(journal.date, find('CONTRIBUTION'), -100)
    journal.validate()

# Generated at 2022-06-14 04:18:00.142729
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from .accounts import EquityAccount, ExpensesAccount, AssetsAccount, LiabilitiesAccount, RevenueAccount
    from .journal import JournalEntry as j
    from .journal import Direction
    from .journal import Posting

    # Arrange
    assets = AssetsAccount()
    liabilities = LiabilitiesAccount()
    expenses = ExpensesAccount()
    revenue = RevenueAccount()
    equity = EquityAccount()

    # Act
    journal1 = j(datetime.datetime.utcnow().date(),"stock", equity).post(datetime.datetime.utcnow().date(),assets,100).post(datetime.datetime.utcnow().date(),liabilities,100)

# Generated at 2022-06-14 04:18:04.008900
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    je = JournalEntry(datetime.date.today())
    je.post(datetime.date.today(), "A", 4)
    je.post(datetime.date.today(), "A", -4)
    je.validate()

# Generated at 2022-06-14 04:18:14.721771
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .currencies import Currency
    from .accounts import Account

    je = JournalEntry(
        datetime.date(2019, 1, 1), "Journal Entry with Postings", None
    ).post(
        datetime.date(2019, 1, 1), Account("Account 1", "Description 1", Currency("Currency 1"), AccountType.ASSETS), 100
    ).post(
        datetime.date(2019, 1, 1), Account("Account 2", "Description 2", Currency("Currency 2"), AccountType.ASSETS), -25
    )

    assert len(je.postings) == 2
    assert je.postings[0].account == Account("Account 1", "Description 1", Currency("Currency 1"), AccountType.ASSETS)

# Generated at 2022-06-14 04:18:19.101142
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry(datetime.date.today(), "Description", "Source")
    je.post(datetime.date.today(), Account(1, AccountType.ASSETS), 100)
    je.post(datetime.date.today(), Account(2, AccountType.EXPENSES), -100)
    je.validate()

# Generated at 2022-06-14 04:18:30.884995
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date

    def read_journals_from_file(period: DateRange) -> Iterable[JournalEntry[type]]:
        for journal in journals:
            if period.contains(journal.date):
                yield journal


# Generated at 2022-06-14 04:18:40.319244
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .currencies import Currency, CurrencyContext, CurrencyPair

    # 4. Initiate currency context by registering USD and INR with their respective base currencies.
    USD = Currency("USD")
    INR = Currency("INR")
    CurrencyContext.register(INR, INR)
    CurrencyContext.register(USD, USD)
    CurrencyContext.register(CurrencyPair(USD, INR), INR)

    # 5. Initiate currency context by registering USD and INR with their respective base currencies.
    INR_ASSET = Account("INR ASSET", AccountType.ASSETS)
    INR_LIABILITY = Account("INR LIABILITY", AccountType.LIABILITIES)
    USD_ASSET = Account("USD ASSET", AccountType.ASSETS)
    USD_LIABL

# Generated at 2022-06-14 04:18:47.626004
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Test code goes in here
    journal1 = JournalEntry[str](datetime.date.today(), "Sale of Furniture", "S01", [])
    journal2 = JournalEntry[str](datetime.date.today(), "Sale of Furniture", "S01", [])

    journal1.post(datetime.date.today(), Account(AccountType.ASSETS, "Receivables", ["Customers", "John Doe"]), 100)
    journal1.post(datetime.date.today(), Account(AccountType.REVENUES, "Sales", ["Furniture", "Retail Sales"]), 100)

    journal2.post(datetime.date.today(), Account(AccountType.ASSETS, "Receivables", ["Customers", "John Doe"]), 100)


# Generated at 2022-06-14 04:18:56.714331
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class BusObj:
        pass

    def read(date_range):
        return [
            JournalEntry(datetime.date(2000, 1, 1), "desc", BusObj()).post(datetime.date(2000, 1, 1), Account.of(1), 100),
            JournalEntry(datetime.date(2000, 1, 2), "desc", BusObj()).post(datetime.date(2000, 1, 2), Account.of(1), 200)
        ]

    for i in ReadJournalEntries.__subclasscheck__(read):
        assert i

    for i in read(DateRange.of(datetime.date(2000, 1, 1), datetime.date(2000, 1, 5))):
        assert i.date == datetime.date(2000, 1, 1)

# Generated at 2022-06-14 04:19:03.383702
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .periods import Period
    from zeitgeist.dataclasses import PeriodRange
    from ddkcore.commons.zeitgeist import today
    from ddkcore.commons.numbers import Amount, Currency, Quantity
    from ddkcore.core.journal import JournalEntry, Direction, Posting, _debit_mapping
    from ddkcore.core.businessobjects import BusinessObject, Attribute, Persisted
    from ddkcore.core.orders import Order, OrderType, OrderStatus, OrderSide, OrderInput
    from ddkcore.core.portfolio import Position, Portfolio, PortfolioInput

    #: Defines the currency to be used for transactions.
    currency = Currency.USD

    #: Defines the position class.

# Generated at 2022-06-14 04:20:21.621202
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def f(period: DateRange) -> None:
        pass
    ReadJournalEntries.__call__(f, DateRange())

# Generated at 2022-06-14 04:20:29.231889
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Arrange:
    def f(period: DateRange) -> Iterable[JournalEntry[str]]:
        return [JournalEntry(period.start, "test", "test")]

    # two functions with the same signature
    assert f.__call__.__name__ == "__call__"
    assert f.__call__.__qualname__ == "ReadJournalEntries.<locals>.f.__call__"

    # Act & Assert:
    assert f.__call__(DateRange(datetime.date.today(), datetime.date.today()))
    assert f(DateRange(datetime.date.today(), datetime.date.today()))

# Generated at 2022-06-14 04:20:33.980195
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class ReadJournalEntriesImplementation:
        """
        Implements ReadJournalEntries.
        """

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    ReadJournalEntriesImplementation()

# Generated at 2022-06-14 04:20:42.525334
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    from .accounts import AccountType

    # Test-1: test case for posting two amounts in different direction
    account_salary_rec = Account(name='Salary Received', type=AccountType.ASSETS, level=1)
    account_rent = Account(name='Rent', type=AccountType.EXPENSES, level=1)
    account_cash = Account(name='Cash', type=AccountType.ASSETS, level=1)
    account_savings = Account(name='Savings', type=AccountType.ASSETS, level=1)

    today = datetime.date.today()

    je1 = JournalEntry(date=today, description='Salary received')

    je1.post(date=today, account=account_salary_rec, quantity=50000)

# Generated at 2022-06-14 04:20:52.357293
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import SimpleAccounts, AccountType
    accounts = SimpleAccounts()
    account = accounts.create(AccountType.ASSETS, "Cash")
    journal = JournalEntry[str](datetime.date.today(), "Test description", "Test Source").post(datetime.date.today(), account, 1000).post(datetime.date.today(), account, 1000)
    assert journal.increments[0].amount == Amount(1000)
    assert journal.increments[1].amount == Amount(1000)
    assert sum([x.amount for x in journal.increments]) == sum([x.amount for x in journal.debits]) == sum([x.amount for x in journal.credits])
    journal.post(datetime.date.today(), account, -500)
    assert journal.decrements[0].amount == Amount(500)


# Generated at 2022-06-14 04:21:00.978717
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():

    # Test journal entry.
    class TestJournalEntry(JournalEntry[int]):
        pass

    # Test read-journal-entries function.
    def test_read_journal_entries(period: DateRange) -> Iterable[TestJournalEntry]:
        yield TestJournalEntry(date=period.start, description="", source=0, postings=[])

    # Type check.
    test_read_journal_entries: ReadJournalEntries[int] = test_read_journal_entries

# Generated at 2022-06-14 04:21:07.348130
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Test the method post of a journal entry.
    """
    from .others import ZeroTransaction
    from .manu import Manufacture
    from .manu.manu import ManufactureResource
    from .base import AccountHolder
    from .base.accounts import AccountBlueprint

    class TestHolder(AccountHolder):
        """
        Test holder of accounts.
        """

        def __init__(self) -> None:
            #: Test resource.
            self.resource = ManufactureResource(
                acc=AccountBlueprint(name="Resource Unit", type=AccountType.ASSETS, tags={"manufacture", "resource"})
            )

    holder = TestHolder()
    zero = ZeroTransaction()
    factory = Manufacture()

    # Create journal entry and post it to the holder

# Generated at 2022-06-14 04:21:19.157491
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Setup
    a = Account("account1")
    b = Account("account2")
    journal_entry = JournalEntry[str]("20170101", "description", "source", [])


    # When
    journal_entry.post("20170101", a, +300)
    journal_entry.post("20170101", b, -300)

    # Then
    assert len(journal_entry.postings) == 2

    # When
    journal_entry.post("20170101", a, +0)

    # Then
    assert len(journal_entry.postings) == 2

    # When
    journal_entry.post("20170101", a, -0)

    # Then
    assert len(journal_entry.postings) == 2

    # When