

# Generated at 2022-06-14 04:11:21.028316
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:11:29.562501
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType

    asset_acc = Account('asset_acc', AccountType.ASSETS)
    exp_acc = Account('exp_acc', AccountType.EXPENSES)
    a = JournalEntry(datetime.date.today(),'', None)
    a.post(datetime.date.today(), asset_acc, 30)
    a.post(datetime.date.today(), exp_acc, -30)
    a.validate()

# Generated at 2022-06-14 04:11:40.753182
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    ## Fake data:
    account = Account("Expense", AccountType.EXPENSES)
    account2 = Account("Revenue", AccountType.REVENUES)
    account3 = Account("Expense", AccountType.EXPENSES)
    period = DateRange.from_dates(1, 4,2020, 2, 4, 2020)

    ## Scenario:
    with pytest.raises(AssertionError) as excinfo:
        ## When:
        entry = JournalEntry(datetime.date(2020, 4, 30), "Test", None)
        entry.post(datetime.date(2020, 4, 30), account, -20)
        entry.post(datetime.date(2020, 4, 30), account2, -30)
        entry.post(datetime.date(2020, 4, 30), account, -20)
       

# Generated at 2022-06-14 04:11:45.061942
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .journal import Journal

    class ReadJournalEntriesImpl:
        def __init__(self, journal: Journal[_T]) -> None:
            self.journal = journal

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            yield from journal.entries(period)

    journal: Journal[_T]

    ReadJournalEntriesImpl(journal)

# Generated at 2022-06-14 04:11:55.207290
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry(datetime.date.today(), "Test", None).post(datetime.date.today(), Account.of("test", "Assets"), 10)
    je.validate()
    je.post(datetime.date.today(), Account.of("test", "Expenses"), -5)
    je.validate()
    je.post(datetime.date.today(), Account.of("test", "Expenses"), -5)
    je.validate()
    je.post(datetime.date.today(), Account.of("test", "Expenses"), 2)
    try:
        je.validate()
        raise AssertionError("Validate should have thrown an Exception")
    except AssertionError:
        pass

# Generated at 2022-06-14 04:12:03.992446
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    fake_account = Account("fake", AccountType.ASSETS)
    fake_account2 = Account("fake2", AccountType.REVENUES)
    credits = []
    debits = []

    # positive balance
    try:
        credits.append(Posting(1, datetime.datetime.today(), fake_account, Direction.INC, Decimal("75")))
    except AssertionError:
        print("test_JournalEntry_validate:1: Credits list can't append Posting")
    try:
        debits.append(Posting(1, datetime.datetime.today(), fake_account2, Direction.DEC, Decimal("50")))
    except AssertionError:
        print("test_JournalEntry_validate:2: Debits list can't append Posting")

# Generated at 2022-06-14 04:12:11.998034
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Asset, Revenues
    from datetime import date

    je = JournalEntry[int](date.today(), "Journal entry for testing", 0)
    je.post(je.date, Asset("101"), 100)

    assert len(je.postings) == 1, "Incorrect number of postings"
    assert je.postings[0]
    assert je.postings[0].journal == je
    assert je.postings[0].date == je.date
    assert je.postings[0].account == Asset("101")
    assert je.postings[0].direction == Direction.INC
    assert je.postings[0].amount == Amount(100)
    assert je.postings[0].is_debit
    assert je.postings[0].is_credit


# Generated at 2022-06-14 04:12:23.441954
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType

    from .currencies import Currency
    from datetime import date
    from dataclasses import FrozenInstanceError

    account = Account("A", AccountType.ASSETS, Currency.USD)
    account2 = Account("B", AccountType.EXPENSES, Currency.USD)

    j = JournalEntry[object](date.today(), '')
    j.post(date.today(), account, 1)
    j.post(date.today(), account, 1)
    j.post(date.today(), account, 0)
    j.post(date.today(), account2, -1)

    assert isinstance(j.postings[0], Posting[object])
    assert isinstance(j.postings[1], Posting[object])

# Generated at 2022-06-14 04:12:32.404041
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType, Account, Accounts
    account1 = Account("A1", AccountType.ASSETS)
    account2 = Account("A2", AccountType.EXPENSES)
    accounts = Accounts()
    accounts.register(account1, account2)

    # assert(accounts.exists_account("A1"))
    # assert(accounts.exists_account("A2"))

    je = JournalEntry(date=datetime.date(2018, 1, 1), description="Test")
    je.post(datetime.date(2018, 1, 1),accounts.get_account("A1"), 2)
    je.post(datetime.date(2018, 1, 1),accounts.get_account("A2"), -2)
    je.validate()

    pass

# Generated at 2022-06-14 04:12:41.231278
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from unittest.mock import Mock
    source = Mock()
    source.description = "Test description"
    a = JournalEntry[type(source)](date.today(), source.description, source)
    b = a.post(date.today(), Account('Assets'), -10)
    c = a.post(date.today(), Account('Expenses'), 10)
    assert len(b.postings) == len(c.postings) == 1

# Generated at 2022-06-14 04:12:51.702318
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate(): 
    JE_test = JournalEntry(datetime.date(2019, 1, 1), 'description', 'test')
    JE_test.post(datetime.date(2019, 1, 1), Account(1, 'Cash', 'Assets'), 10)
    JE_test.post(datetime.date(2019, 1, 1), Account(2, 'Building', 'Assets'), -10)
    JE_test.validate()

# Generated at 2022-06-14 04:13:04.952491
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry(
            datetime.date(2020, 5, 1),
            'Test Journal',
            None
        )\
        .post(datetime.date(2020, 5, 1), Account(1, 'Account1', AccountType.ASSETS), 10000)\
        .post(datetime.date(2020, 5, 1), Account(2, 'Account2', AccountType.EQUITIES), -10000)
    je.validate()
    #

# Generated at 2022-06-14 04:13:06.304207
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # No implementation. Method is just to provide the type.
    pass

# Generated at 2022-06-14 04:13:16.366470
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import load_accounts, Account

    load_accounts()

    class JE:
        def __init__(self):
            self.postings = []
        def post(self, date, account, quantity):
            if not quantity.is_zero():
                self.postings.append(Posting(self, date, account, Direction.of(quantity), Amount(abs(quantity))))
        def validate(self):
            ## Get total debit and credit amounts:
            total_debit = isum(i.amount for i in self.debits)
            total_credit = isum(i.amount for i in self.credits)

            ## Check:
            assert total_debit == total_credit, f"Total Debits and Credits are not equal: {total_debit} != {total_credit}"


# Generated at 2022-06-14 04:13:28.412118
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    @dataclass(frozen=True)
    class CBT:
        pass

    je = JournalEntry[CBT](
        date=datetime.date(2019, 1, 1),
        description="Test Validation",
        source=CBT()
    )

    je.post(datetime.date(2019, 1, 1), Account(AccountType.ASSETS, '0000', 'Assets'), 1)
    je.post(datetime.date(2019, 1, 1), Account(AccountType.REVENUES, '1001', 'Revenues'), -1)

    try:
        je.validate()
    except AssertionError as ae:
        print(ae)
        assert True
    else:
        assert False

# Generated at 2022-06-14 04:13:36.726530
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .currencies import Currency
    from .wallets import CashWallet

    ## Wallet to use for testing:
    wallet = CashWallet("USD", Currency("USD"))

    ## Entry instance:
    e = JournalEntry(date=datetime.date.today(), description="TEST ENTRY", source=wallet)
    assert len(e.postings) == 0, "Expected no postings in entry."

    ## Post an amount to the wallet:
    e.post(date=datetime.date.today(), account=Account.of(wallet.name, AccountType.ASSETS), quantity=Amount(1.0))
    assert len(e.postings) == 1, "Expected one posting in the entry."

    ## Check the posting:
    p = e.postings[0]
    assert p is not None

# Generated at 2022-06-14 04:13:44.937924
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from itertools import repeat
    from . import accounts
    je = JournalEntry(date(2019, 1, 1), 'description', object())
    posting = lambda je, d, a, q: je.post(d, a, q)
    assert(len(je.postings) == 0)
    posting(je, date(2019, 1, 1), accounts.Account('a', 'A', accounts.AccountType.ASSETS), Quantity(1))
    assert(len(je.postings) == 1)
    posting(je, date(2019, 1, 1), accounts.Account('a', 'A', accounts.AccountType.ASSETS), Quantity(0))
    assert(len(je.postings) == 1)

# Generated at 2022-06-14 04:13:54.682792
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    ######
    # Define journal entries
    # We define the journal entry entries_to_validate with a valid posting (debit and credit)
    # We define the journal entry entries_to_not_validate with an invalid posting (debit and credit)
    # The validate function of the JournalEntry class should successfully validate the entries_to_validate
    # and should not validate entries_to_not_validate
    ######
    from .accounts import Account, AccountType
    from .commons.numbers import Amount
    from .journal import Direction, JournalEntry, Posting
    from .utils import datemodule
    from datetime import date

    entries_to_validate = []
    entries_to_not_validate = []


# Generated at 2022-06-14 04:14:00.498319
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    account_asset = Account(AccountType.ASSETS,'cash', 'cash')
    account_revenue = Account(AccountType.REVENUES, 'sales', 'sales')
    journal_entry = JournalEntry[int](date = datetime.date.today(), description = 'opening sales', source = 1)
    journal_entry.post(date = datetime.date.today(), account = account_asset, quantity = 100.0)
    journal_entry.post(date = datetime.date.today(), account = account_revenue, quantity = -100.0)
    journal_entry.validate()

# Generated at 2022-06-14 04:14:11.560967
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime
    from src.accounts.models import Account, AccountType
    from src.entries.models import JournalEntry, Direction, Direction
    je = JournalEntry(datetime.date.today(), 'test description', None)
    je = je.post(datetime.date.today(), Account('test account', AccountType.ASSETS), 60)
    je = je.post(datetime.date.today(), Account('test account', AccountType.LIABILITIES), -60)
    assert len(je.increments) == 1, 'check if increments contains one posting'
    assert je.increments == [p for p in je.postings if p.direction == Direction.INC], 'check if increments contains the correct posting'
    assert len(je.decrements) == 1, 'check if decrements contains one posting'
    assert je.decrements

# Generated at 2022-06-14 04:14:32.926884
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    account1 = Account(type=AccountType.ASSETS, name="Cash")
    account2 = Account(type=AccountType.EXPENSES, name="Wages")
    account3 = Account(type=AccountType.REVENUES, name="Sales")
    je = JournalEntry(date=datetime.date(2020, 1, 1), description="Monthly Wages", source=None)
    je.post(date=datetime.date(2020, 1, 1), account=account1, quantity=100)
    je.post(date=datetime.date(2020, 1, 1), account=account2, quantity=-100)
    je.post(date=datetime.date(2020, 1, 1), account=account1, quantity=200)

# Generated at 2022-06-14 04:14:39.264769
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    journal_entry = JournalEntry[int](date=datetime.date.today(),
        postings=[Posting(journal=None, date=datetime.date.today(), account=Account(code='000', type=AccountType.EQUITIES), direction=Direction.INC, amount=Amount(quantity=5))],
        description="Entry #1",
        source=1)
    journal_entry.validate()

# Generated at 2022-06-14 04:14:40.528780
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass


# Generated at 2022-06-14 04:14:49.246681
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import datetime
    from ..commons.others import makeguid
    from pytest import fixture
    from pytest_mock import MockFixture
    from .accounts import Account, AccountType
    from .journal import JournalEntry
    from .users import User

    @fixture
    def mocks(mocker: MockFixture) -> Dict:
        return {
            "read_journal_entries": mocker.patch("flowserv.data.models.journal.read_journal_entries")
        }

    @fixture
    def journal_entry_1(journal_entry_id: str, user: User) -> JournalEntry[User]:
        return JournalEntry(
            journal_entry_id,
            datetime.date(2020, 1, 19),
            "Test Event",
            user,
            []
        )

   

# Generated at 2022-06-14 04:15:00.235337
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    acc1 = Account(code="acc1", name="Name_acc1", type=AccountType.ASSETS, description="资产类")
    acc2 = Account(code="acc2", name="Name_acc2", type=AccountType.EQUITIES, description="负债类")
    acc3 = Account(code="acc3", name="Name_acc3", type=AccountType.EXPENSES, description="费用类")
    acc4 = Account(code="acc4", name="Name_acc4", type=AccountType.LIABILITIES, description="权益类")
    acc5 = Account(code="acc5", name="Name_acc5", type=AccountType.REVENUES, description="收入类")


# Generated at 2022-06-14 04:15:07.180208
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    je = JournalEntry(datetime.date(2000, 1, 1), "description", None)
    je.post(datetime.date(2000, 1, 1), Account("Account", AccountType.ASSETS), 1)
    je.post(datetime.date(2000, 1, 1), Account("Account", AccountType.ASSETS), -1)

    assert je.increments[0].amount == 1
    assert je.decrements[0].amount == 1

# Generated at 2022-06-14 04:15:11.129921
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Code
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        #return None
        pass

    # Test

# Generated at 2022-06-14 04:15:11.621573
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:15:12.900077
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:15:19.249928
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Unit test for method validate of class JournalEntry.
    :return:
    """
    JE = JournalEntry[int]

    JE(datetime.date.today(), "Test JE", 100).post(datetime.date.today(), Account.ASSETS.of("Cash"), 1000).post(
        datetime.date.today(), Account.LIABILITIES.of("Loan"), -1000).validate()

# Generated at 2022-06-14 04:15:40.912051
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Given

    # When

    # Then
    pass



# Generated at 2022-06-14 04:15:51.321713
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import make_account
    from .buz_sources import BuzSource, make_buz_source, get_buz_source

    # -------------------------
    # Given:
    # A mock for 'ReadJournalEntries' protocol
    @dataclass(frozen=True)
    class _MockReadJournalEntries(ReadJournalEntries[BuzSource]):
        def __call__(self, period: DateRange):
            return (
                JournalEntry(i[0], i[1], bus_object, [])
                for i, bus_object in get_buz_source(period)
            )

    # -------------------------
    # When:
    # 'ReadJournalEntries' protocol method '__call__' is invoked

# Generated at 2022-06-14 04:15:55.778096
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j = JournalEntry[int](datetime.date.today(), "Test", 2)
    j.post('2019-04-27', Account('Sales'), -100.10)
    assert str(j) == 'JournalEntry(date=2019-04-27, description=Test, source=2, postings=...)'

# Generated at 2022-06-14 04:16:06.384652
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from .accounts import Account, AccountType, create_account
    from .ledgers import Ledger, create_ledger
    journal = JournalEntry[Ledger]()
    journal.post(date(2011, 12, 12), create_account(account_type=AccountType.ASSETS, entity_id="ABCD_ABCD_A", name="Cash"), 2)
    assert journal.postings[0].is_debit == True
    journal.post(date(2011, 12, 12), create_account(account_type=AccountType.EQUITIES, entity_id="ABCD_ABCD_E", name="Equity"), -2)
    assert journal.postings[1].is_debit == False
    assert len(journal.postings) == 2


# Generated at 2022-06-14 04:16:13.462321
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import read_accounts
    from .books import Book
    from .memories import AccountsMemory, JournalEntriesMemory, SourcesMemory
    from .sources import read_sources
    from .types import Type, read_types

    # Read types:
    class Savings(Type):
        """Savings"""

    class Expenses(Type):
        """Expenses"""

    types = list(read_types([Savings, Expenses]))

    # Get owner:
    owner = types[0]

    # Read accounts:

# Generated at 2022-06-14 04:16:18.010937
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry(datetime.date(2015, 1, 1), "debit", "cash", [])
    je.post(datetime.date(2015, 1, 1), "cash", 1000)
    je.post(datetime.date(2015, 1, 1), "equity", -1000)
    je.validate()

# Generated at 2022-06-14 04:16:30.128278
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from ..ledgers.journal_ledger import JournalLedger
    from .accounts import Accounts
    from .accounts import Account

    ledger = JournalLedger(Accounts({}))
    ledger.add(Account('A'), DateRange(datetime.date(2020, 11, 12),datetime.date(2020, 11, 12)),1)
    ledger.add(Account('B'), DateRange(datetime.date(2020, 11, 12),datetime.date(2020, 11, 12)),1)
    ledger.add(Account('C'), DateRange(datetime.date(2020, 11, 12),datetime.date(2020, 11, 12)),-2)
    
    assert len(list(ledger.entries(DateRange(datetime.date(2020, 11, 1),datetime.date(2020, 11, 30))))) == 3


# Generated at 2022-06-14 04:16:40.852447
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .. import config
    from . import stocks, transactions

    assert config.universe is not None, "Configure the universe with `config.universe = ...` before running tests"

    # Create a journal entry:
    journal = JournalEntry[transactions.Order]()

    # Create the expected book-keeping entries:

    # p1 = Posting(journal, datetime.date(2020, 1, 1), Universe.accounts.equities.cash, Direction.INC, Amount(10000))
    p2 = Posting(journal, datetime.date(2020, 1, 1), Universe.accounts.equities.portfolio, Direction.INC, Amount(10000))
    p3 = Posting(journal, datetime.date(2020, 1, 1), Universe.accounts.equities.dividend, Direction.DEC, Amount(1000))
    p4

# Generated at 2022-06-14 04:16:50.103711
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():

#     def test_ReadJournalEntries___call__():
        def spy_call(*args, **kwargs) -> Iterable[JournalEntry[_T]]:
            """
            Helper to keep track of calls.
            """
            spy_call.times_called += 1
            return spy_call.original_fn(*args, **kwargs)

        #: A callable to be spied on.
        fn: ReadJournalEntries[_T] = lambda period: []
        spy_call.original_fn = fn
        spy_call.times_called = 0

        #: Spy instance.
        spy: ReadJournalEntries[_T] = spy_call

        #: Invoke the spy.
        _ = list(spy(DateRange.all()))
        assert spy_call.times_called == 1

# Generated at 2022-06-14 04:16:56.233543
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Setup
    journal = JournalEntry(datetime.date(2019, 1, 1), "A journal entry")

    # Exercise
    journal.post(datetime.date(2019, 1, 1), Account("NetIncome"), -1000)
    journal.post(datetime.date(2019, 1, 1), Account("DividendPayout"), +1000)

    # Verify
    assert len(journal.debits) == 1
    assert len(journal.credits) == 1
    assert journal.increments[0].amount == Amount(1000)
    assert journal.decrements[0].amount == Amount(1000)



# Generated at 2022-06-14 04:17:30.010755
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    j = JournalEntry
    j.post(True, 'A', 12)

# Generated at 2022-06-14 04:17:35.439272
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry[str](datetime.date.today(), "Test", "Test")
    je.post(datetime.date.today(), Account("A", AccountType.ASSETS), +100)
    je.post(datetime.date.today(), Account("B", AccountType.EQUITIES), -100)
    je.validate()

# Generated at 2022-06-14 04:17:43.534475
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from .accounts import Account, AccountType

    #: Define a dummy ledger to read journal entries from.
    class DummyLedger:
        def __init__(self):
            #: Amount of the ledger
            self.amount = 1000
            #: List of events of the ledger
            self.eventList = []
        def getSum(self):
            return self.amount
        def getEvents(self):
            return self.eventList

    #: Define a dummy account to work with
    class DummyAccount(Account):
        def __init__(self):
            super().__init__("dummy", AccountType.ASSETS)
            self.amount = 0
            self.amountList = []
            self.eventList = []
        def getSum(self):
            return self.amount

# Generated at 2022-06-14 04:17:54.301504
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.exchange import to_amount
    from .accounts import Account, AccountType
    from .inventory import InventoryRepository
    
    JOURNAL_ENTRY_1 = JournalEntry[InventoryRepository].of(
        date=datetime.date(2019, 10, 4),
        description="Invoice 1",
        source=InventoryRepository.get_instance(),
    )

    JOURNAL_ENTRY_2 = JournalEntry[InventoryRepository].of(
        date=datetime.date(2019, 10, 16),
        description="Invoice 2",
        source=InventoryRepository.get_instance(),
    )
    
    ### Revenue Journal Entries

# Generated at 2022-06-14 04:17:59.017762
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    x = JournalEntry[int](date=datetime.date.today(), description="Test", source=0)
    x.post(datetime.date.today(), account=Account.make(name="Cash", type=AccountType.ASSETS), quantity=Quantity(10))
    x.post(datetime.date.today(), account=Account.make(name="Sales", type=AccountType.REVENUES), quantity=Quantity(-10))
    x.validate()

test_JournalEntry_post()

# Generated at 2022-06-14 04:18:09.563245
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Tests the method `post` of class `JournalEntry`.
    """
    ## setup:
    #: Date of journal entry.
    date = datetime.date(2020, 6, 1)

    #: Description of journal entry.
    description = "some description"

    #: Source for journal entry.
    source = None

    #: Dummy account:
    account = Account("something", AccountType.REVENUES)

    #: Journal entry value object.
    journal = JournalEntry(date, description, source)

    #: Quantity values to post.
    quantities = (0, 1, -2, 3, -4)

    #: Expected postings.

# Generated at 2022-06-14 04:18:11.247235
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Check
    assert issubclass(ReadJournalEntries, Protocol)

# Generated at 2022-06-14 04:18:19.079913
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date

    from .accounts import Account, AccountType

    from .db import Database
    from .db.codecs import decode, encode

    from ..commons.strings import is_blank
    from ..commons.zeitgeist import datetime_from_string, datetime_to_string

    #
    # Assertion helpers
    #

    class Helper:
        @staticmethod
        def assert_journals(actual_journals: Iterable[JournalEntry[str]], expected_journals: Iterable[JournalEntry[str]]):
            assert len(actual_journals) == len(expected_journals), f"Unexpected journal count: expected: {len(actual_journals)}, actual: {len(expected_journals)}"


# Generated at 2022-06-14 04:18:30.844002
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..books.accounts import AccountType, Account, chart_of_accounts
    from ..books.journals import JournalEntry, Direction, Posting
    from ..commons.numbers import Amount, Quantity

    journal = JournalEntry(datetime.date(2020, 6, 15), "Journal description", 'Source value object')
    journal.post(None, chart_of_accounts['cash'], Quantity(10))
    journal.post(None, chart_of_accounts['revenue'], Quantity(7))

    print(journal)
    print(journal.postings)
    print(journal.increments)
    print(journal.decrements)
    print(journal.debits)
    print(journal.credits)

    # Ensure journal entry is immutable:
    # journal.postings.append(Posting(journal, None, chart

# Generated at 2022-06-14 04:18:37.500353
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from typing import Callable

    class R(ReadJournalEntries[str]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[str]]: pass

    def f(period: DateRange) -> Iterable[JournalEntry[str]]: pass

    def h(period: DateRange = None) -> Iterable[JournalEntry[str]]: pass

    #: Will not raise an error.
    R()
    f
    h



# Generated at 2022-06-14 04:20:02.394946
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Test Case 1
    j1 = JournalEntry(datetime.date(2020, 10, 20), 'Test Case 1', 'Business Object 1')
    j1.post(datetime.date(2020, 10, 20), 'Test Account1', 1000)
    assert not j1.postings == []
    j1.post(datetime.date(2020, 10, 20), 'Test Account2', -1000)
    j1.validate()
    # Test Case 2
    j2 = JournalEntry(datetime.date(2020, 10, 20), 'Test Case 2', 'Business Object 1')
    j2.post(datetime.date(2020, 10, 20), 'Test Account1', 1000)
    assert not j2.postings == []

# Generated at 2022-06-14 04:20:12.196580
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    account1 = Account(1, 'Expenses', AccountType.EXPENSES)
    account2 = Account(2, 'Assets', AccountType.ASSETS)

    # valid journal entry
    je1 = JournalEntry(datetime.date(2017, 12, 22), 'My Description', 'My Object')
    je1.post(datetime.date(2017, 12, 22), account1, 5)
    je1.post(datetime.date(2017, 12, 22), account2, 5)
    je1.validate()

    # invalid journal entry
    je2 = JournalEntry( datetime.date(2017, 11, 22), 'My Description', 'My Object')
    je2.post(datetime.date(2017, 12, 22), account1, 5)

# Generated at 2022-06-14 04:20:17.342856
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # IMPLEMENTATION DETAILS:
    # When decorating a method whose first parameter is self with this protocol, the MyPy
    # compiler does not like it. So, we use an "intermediate" function to do the binding.
    @ReadJournalEntries
    def read(period: DateRange) -> Iterable[JournalEntry[_T]]:
        ...

# Generated at 2022-06-14 04:20:27.244937
# Unit test for method post of class JournalEntry

# Generated at 2022-06-14 04:20:30.422845
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class journal: pass
    ReadJournalEntries.register(lambda period: [journal()])

    ret: Iterable[object] = ReadJournalEntries(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 31))).__call__()
    assert list(ret) == [journal()]

# Generated at 2022-06-14 04:20:33.833062
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    read_journals: ReadJournalEntries[_T] = lambda period: iter([])
    assert len(list(read_journals(DateRange.unbounded()))) == 0

# Generated at 2022-06-14 04:20:38.202634
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Arrange
    # Acct 2011-2, 3
    # Acct 2012-1, 2
    # Acct 2013-3, 4
    def f(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return []

    # Act
    # Assert
    assert isinstance(f, ReadJournalEntries)



# Generated at 2022-06-14 04:20:43.304926
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    J = JournalEntry
    j = J(date = datetime.date(12, 2, 2), description="Desc")
    j.post(datetime.date(2, 3, 4), Account("name"), Quantity(10))
    assert len(j.postings) == 1

# Generated at 2022-06-14 04:20:52.596902
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType
    from .businessobjects import BusinessObject, Payee

    class D:

        def __init__(self, date):
            self.date = date

    # create assets account
    a1 = Account("assets1", AccountType.ASSETS)

    # create receivables account
    a2 = Account("receivables1", AccountType.ASSETS)

    # create owner's equity account
    a3 = Account("owner's equity", AccountType.EQUITIES)

    # create expense account
    a4 = Account("expenses1", AccountType.EXPENSES)

    # create revenues account
    a5 = Account("revenues1", AccountType.REVENUES)

    # create buyer
    b1 = Payee("buyer1", "buyer1")

    # create seller

# Generated at 2022-06-14 04:21:04.941319
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Unit testing the validate method of JournalEntry
    """
    journal = JournalEntry[int](datetime.date(2020,9,18),"Test",1)

    # Entry with only debit posting
    journal.post(datetime.date(2020,9,18),Account("Test"),Quantity(1000))
    journal.validate()

    # Entry with only credit posting
    journal = JournalEntry[int](datetime.date(2020,9,18),"Test",1)
    journal.post(datetime.date(2020,9,18),Account("Test"),Quantity(-1000))
    journal.validate()

    # Entry with debit and credit posting of same amount
    journal = JournalEntry[int](datetime.date(2020,9,18),"Test",1)