

# Generated at 2022-06-14 04:23:42.013709
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:23:50.613843
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .accounts import TransactionAccount

    @dataclass
    class MockReadInitialBalances(ReadInitialBalances):
        def __call__(self, period) -> InitialBalances:
            return {TransactionAccount("1"): Balance(period.since, Quantity(Decimal(0)))}

    assert MockReadInitialBalances()(DateRange(datetime.date.today(), datetime.date.today())) == {
        TransactionAccount("1"): Balance(datetime.date.today(), Quantity(Decimal(0)))
    }

# Generated at 2022-06-14 04:23:56.580322
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .commons.testing import assert_equal
    from .commons.testing import assert_all_equal
    from .journaling import JournalEntry, Posting

    print("test_ReadInitialBalances___call__")

    def read_initial_balances() -> Dict[Account, Balance]:
        return {Account("101500"): Balance(datetime.date(2014, 1, 1), Quantity(Decimal(0)))}

    assert_equal(len(read_initial_balances()), 1)
    assert_equal(read_initial_balances()[Account("101500")].value, Quantity(Decimal(0)))


# Generated at 2022-06-14 04:24:08.617523
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .journaling import Journal, Posting

    # create a Journal
    example_journal = Journal(datetime.date(2020, 2, 1), 'name', [])

    # create a Posting
    example_posting = Posting(example_journal, Account('code', 'name', 'type'), 100, 'debit')

    # create a Ledger
    example_balance = Balance(datetime.datetime(2020, 1, 1), 100)
    example_account = Account('name', 'description', 'type')
    register = Ledger(example_account, example_balance)

    assert register.add(example_posting) == LedgerEntry(register, example_posting, Quantity(Decimal(200)))



# Generated at 2022-06-14 04:24:09.426457
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:24:20.841689
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Unit Tests for methods of class Ledger.
    """
    # The ledger being tested
    test_account = Account(221100)
    test_initial = Balance(datetime.date(2020,1,1), Quantity(100.00))
    test_ledger = Ledger(test_account,test_initial)

    # Two postings to test the method
    test_posting = Posting(JournalEntry(datetime.date(2020,1,1), Account(221100), "Test entry"), Quantity(10.0), Account(221100))
    test_posting2 = Posting(JournalEntry(datetime.date(2020,1,2), Account(221100), "Test entry"), Quantity(20.0), Account(221100))

    # Test add method of class Ledger
    test_ledger2 = test_ledger.add

# Generated at 2022-06-14 04:24:34.529800
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Unit test for function :py:func:`build_general_ledger`
    """

    from datetime import date
    from decimal import Decimal
    from collections import defaultdict

    # Test data input
    period = DateRange(date(2020, 1, 1), date(2020, 1, 10))

# Generated at 2022-06-14 04:24:45.966630
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test function build_general_ledger
    """
    from datetime import date
    from .journaling import JournalEntry, Posting, Journal, Money, Amount

    # First, create some accounts:
    from .accounts import Account, Booking, Ledger, AccountType

    # We need a ledger to book on and an account to work on:
    ledger = Ledger(title = "Test ledger")
    account = Account(ledger, "1001", title = "Test account 1", account_type = AccountType.ASSET, booking = Booking.DEBIT)
    account_2 = Account(ledger, "1002", account_type = AccountType.LIABILITY)
    account_3 = Account(ledger, "1003", account_type = AccountType.INCOME)

# Generated at 2022-06-14 04:24:52.192897
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Tests function compile_general_ledger_program for non-tautological expectations.
    """
    ## Create and compile a general ledger program.
    program = compile_general_ledger_program(
        lambda period: {}, lambda period: [JournalEntry("")]
    )

    ## Execute the program.
    general_ledger = program(DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31)))

    ## Assert general ledger properties.
    assert general_ledger.period == DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))
    assert general_ledger.ledgers == {}

    ## Done, return.
    return

# Generated at 2022-06-14 04:25:02.771299
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    def read_initial_balances(period: DateRange) -> InitialBalances:
        pass

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        pass

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    
    period: DateRange = DateRange(since=datetime.date(2020, 1, 1), until=datetime.date(2020, 1, 31))
    actual = program(period)
    assert isinstance(actual, GeneralLedger)
    assert actual.period == period
    assert actual.ledgers == {}


# Generated at 2022-06-14 04:25:21.862738
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..journaling.journaling import build_journal_entry
    from ..commons.zeitgeist import now, month_of, day_after

    ## fixture for individual journal entries
    account_a = Account("A")
    account_b = Account("B")
    account_c = Account("C")
    date_1 = now()
    date_2 = day_after(date_1)
    date_3 = day_after(date_2)
    date_4 = day_after(date_3)
    entry_1 = build_journal_entry(
        "fourth",
        [account_a.debit(Decimal(1), "b"), account_b.debit(Decimal(2), "a"), account_c.credit(Decimal(3), "c")],
        date_1,
    )
    entry

# Generated at 2022-06-14 04:25:31.308643
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    
    # Assuming we have two sets of data: all the initial balances, and all the transactions.
    # You can imagine these as CSV files loaded into memory as dictionaries.
    initial_balances = {
        Account('A1', 'Assets'): Balance(date(2018, 1, 1), Quantity(Decimal('100'))),
        Account('E1', 'Equity'): Balance(date(2018, 1, 1), Quantity(Decimal('200')))
    }

    journal_entries = [
        JournalEntry(date(2018, 1, 1), 'J1', [
            Posting(Account('O1', None), True, Quantity(Decimal('-10'))),
            Posting(Account('A1', 'Assets'), False, Quantity(Decimal('10')))
        ])
    ]

    # We can define the functions

# Generated at 2022-06-14 04:25:44.104431
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    ## Create a sample period
    r=DateRange(datetime.date(2019,1,1),datetime.date(2019,1,31))
    ## Create a read journal entries algebra
    def read_journal_entries(period: DateRange) -> List[JournalEntry[_T]]:
        return journal_entries

    ## Create a read initial balances algebra
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return initial_balances

    ## Create a sample initial balances
    initial_balances={}
    ## Create a sample journal entries
    journal_entries=[]
    ## Compile
    general_ledger_program = compile_general_ledger_program(read_initial_balances,read_journal_entries)
    ## Test

# Generated at 2022-06-14 04:25:57.478688
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Get an instance of Ledger
    account = Account("1010")
    initial = Balance(datetime.date.today(), Quantity(1))
    posting = Posting(datetime.date.today(), Quantity(1))
    ledger = Ledger(account, initial)

    # Call add and test the outcome
    entry = ledger.add(posting)
    assert ledger.entries[0] == entry
    assert ledger.entries[0].balance == Quantity(2)
    assert ledger.entries[0].posting == posting
    assert ledger.entries[0].ledger == ledger
    assert ledger.entries[0].cntraccts == []
    assert ledger.entries[0].date == datetime.date.today()
    assert ledger.entries[0].amount == Quantity(1)

# Generated at 2022-06-14 04:26:03.785942
# Unit test for method add of class Ledger
def test_Ledger_add():
    ledger = Ledger(account=Account(number=1), initial=Balance(date=datetime.datetime.now(), value=Decimal(0)))
    posting = Posting(date=datetime.datetime.now(), account=Account(number=1), amount=Amount(Decimal(10)))
    ledger.add(posting=posting)
    assert ledger.entries[0].balance == Decimal(10)

# Generated at 2022-06-14 04:26:16.536733
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .accounts import build_accounts
    from .journaling import build_journal_entries

    ## Step 1: Create accounts:
    accounts = build_accounts(
        account_number=["1101", "1201", "1202", "1203", "2001", "2101"],
        description=["Cash", "Accounts receivable", "Inventory", "Office supplies", "Income", "Expenses"],
        is_terminal=[True, True, True, True, False, False],
    )
    terminals = [a for a in accounts.values() if a.is_terminal]

    ## Step 2: Create journal entries:

# Generated at 2022-06-14 04:26:30.367817
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # GIVEN a general ledger program
    general_ledger_program = compile_general_ledger_program(
        read_initial_balances=lambda period: {}, read_journal_entries=lambda period: []
    )

    # WHEN the program is called
    with pytest.raises(TypeError):
        general_ledger_program()

    # THEN the exception is raised
    # GIVEN an accounting period
    period = DateRange(since=datetime.date(2020, 12, 1), until=datetime.date(2020, 12, 31))

    # GIVEN a general ledger program
    general_ledger_program = compile_general_ledger_program(
        read_initial_balances=lambda period: {}, read_journal_entries=lambda period: []
    )

    # WHEN the program is called with

# Generated at 2022-06-14 04:26:31.710127
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:26:44.854269
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import JournalEntry, Posting
    from .accounts import Account, AccountType
    from ..commons.zeitgeist import DateRange

    account = Account(AccountType.ASSET, 'cash')
    account2 = Account(AccountType.ASSET, 'cash')
    account3 = Account(AccountType.ASSET, 'cash')
    account4 = Account(AccountType.ASSET, 'cash')

    posting = Posting(account, Quantity(Decimal(10.0)))
    posting2 = Posting(account2, Quantity(Decimal(10.0)))
    posting3 = Posting(account3, Quantity(Decimal(10.0)))
    posting4 = Posting(account4, Quantity(Decimal(10.0)))


# Generated at 2022-06-14 04:26:53.237381
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from .accounts import Account
    from .generic import Balance

    class SomeReader(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("1001"): Balance(date(2020, 1, 1), 100),
                Account("1002"): Balance(date(2020, 1, 1), 200),
            }

    SomeReader()(DateRange(date(2020, 1, 1), date(2020, 1, 31)))


# Generated at 2022-06-14 04:27:06.499300
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .algebra import read_initial_balances, read_journal_entries
    from .types import BatchID, LineID, LineOfBusiness

    program = compile_general_ledger_program(read_initial_balances(), read_journal_entries())
    period = DateRange(since=datetime.date(2020, 1, 1), until=datetime.date(2020, 6, 30))
    gl = program(period)

    assert all(len(l.entries) > 0 for l in gl.ledgers.values())



# Generated at 2022-06-14 04:27:15.147312
# Unit test for method add of class Ledger
def test_Ledger_add():
    ledger = Ledger(Account(12345), Balance(datetime.date(2000, 1, 1), Quantity(Decimal(0))))

    posting = Posting(
        datetime.date(2000, 1, 1), Journal(datetime.date(2000, 1, 1), "abc"), Quantity(Decimal(1)), Account(12345)
    )

    posting.is_debit = True

    entry = ledger.add(posting)

    assert entry.posting == posting
    assert entry.balance == Quantity(Decimal(1))

# Generated at 2022-06-14 04:27:16.056602
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:27:16.793915
# Unit test for method add of class Ledger
def test_Ledger_add():
    pass

# Generated at 2022-06-14 04:27:25.586202
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """Function build_general_ledger unit test"""

    # Subsidiary ledger

# Generated at 2022-06-14 04:27:37.703328
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .journaling import StoreJournalEntries, StorePostings
    from .accounts import StoreAccounts, StoreInitialBalances
    from .commons.testing import load_ledger
    from ..commons.numbers import round_down
    from ..commons.zeitgeist import DateRange
    from infocount import InfoCount, InfoDict
    #Open DateRange
    period = DateRange(datetime.date(year=2019, month=1, day=1), datetime.date(year=2019, month=1, day=31))

    #Open and load ledger
    ledger = load_ledger(filename="data/full-stack-example.xml")

    #Return initial balance
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return StoreInitialBalances(ledger.initial_balances)()

# Generated at 2022-06-14 04:27:51.633335
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import JournalEntry, Posting, debit, credit, journal_entry
    from .accounts import Account, PremiumAccount, TerminalAccount, AccountType, Currency
    from ..commons.zeitgeist import DateRange
    from ..commons import currencies

    ## Initialize account:
    cash = Account("cash", AccountType.TERMINAL, currencies.CAD)

    ## Initialize journal entries:

# Generated at 2022-06-14 04:27:52.359273
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:28:04.600617
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import JournalEntry, Posting
    from .accounts import Account

    import datetime

    account1 = Account(1, 'Cash', is_terminal=True)
    account2 = Account(2, 'Salary')
    account3 = Account(3, 'Rent', is_terminal=True)

    period = DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))

    journalEntry = JournalEntry(period.since, 'Salary', [Posting(account2, 2, period.since)])

    journal = [journalEntry]

    initial = {}
    initial[account1] = Balance(period.since, Quantity(Decimal(15)))
    initial[account3] = Balance(period.since, Quantity(Decimal(15)))

    generalLedger = build_general

# Generated at 2022-06-14 04:28:16.370119
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.zeitgeist import Date
    from ..journaling.algebras import create_journal_entries
    from ..journaling.models import Journal
    from .accounts.models import TerminalAccount

    ## Initialization:

    ## Create journal entries for test.
    journal_entries = create_journal_entries(
        [Journal(Date(2020, 5, 16), "", [Posting(TerminalAccount("Acc01", "C01"), Amount(10), "")])]
    )

    ## Initialize a ledger for the test.
    ledger = Ledger(TerminalAccount("Acc01", "C01"), Balance(Date(2020, 5, 15), Quantity(0)))

    ## Test:

    ## Add a journal entry to the ledger.

# Generated at 2022-06-14 04:28:35.443214
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal

    a = Account(100, "Revenue")
    b = Account(200, "Cash")
    j = Journal(datetime.date(2020, 1, 1), "Sold something")
    j.post(a, 1000)
    j.post(b, 1000)

    l = Ledger(a, Balance(0,0))
    l.add(j.postings[0])

    assert l.entries[0].is_debit == True

# Generated at 2022-06-14 04:28:36.159750
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:28:44.159027
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal

    account = Account("12345X", "Fixed Assets")
    period = DateRange(datetime.date(2019, 1, 1))
    initial = Balance(period.since, Quantity(100))
    journal = Journal(1, datetime.date(2019, 1, 1), "Purchase of fixed asset")

    ledger = Ledger(account, initial)
    posting = journal.add(account, 100)
    assert ledger.add(posting) == LedgerEntry(ledger, posting, Quantity(200))

# Generated at 2022-06-14 04:28:57.252068
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Unit test for function build_general_ledger
    """
    # Import required modules and functions
    from .accounts import Account
    from .journaling import JournalEntry, Posting
    from ..commons.zeitgeist import DateRange

    # Create test accounts
    account_1 = Account("1", True)
    account_2 = Account("2", True)

    # Create test journal entries
    journal_entry_1 = JournalEntry(
        "Journal 1", datetime.date(2020, 1, 1), [
            Posting(account_1, Decimal("-100"), "debit"),
            Posting(account_2, Decimal("100"), "credit"),
        ],
    )

# Generated at 2022-06-14 04:29:05.700984
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Posting, JournalEntry
    from .accounts import Account
    from .generic import Balance

    account_1 = Account(1, "asset", "cash")
    account_2 = Account(2, "asset", "bank")

    entry_1 = JournalEntry(
        date=datetime.date(2019, 1, 1),
        description= "cash to bank",
        postings=[
            Posting(account=account_1, direction=-1, amount=100, currency="USD"),
            Posting(account=account_2, direction=1, amount=100, currency="USD"),
        ],
    )


# Generated at 2022-06-14 04:29:15.925012
# Unit test for function build_general_ledger
def test_build_general_ledger():
    @dataclass
    class LedgerEntry:
        date: datetime.date
        description: str
        debit: Optional[Amount]
        credit: Optional[Amount]
        balance: Amount
        is_debit: bool

    @dataclass
    class Ledger:
        account: str
        initial: Amount
        entries: List[LedgerEntry]

    def build():
        from ..ledger.algebras import JournalReader, InitialBalanceReader
        from ..ledger.models import Transaction
        from ..ledger.read import read_initial_balances, read_journal_entries

        ## Algebra implementations:

# Generated at 2022-06-14 04:29:25.446983
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.zeitgeist import now
    from ..journaling import Journal, build_journal
    from ..transactions import build_transaction
    from ..algebra import initial_balances, journal_entries, transaction_entries

    # TODO: change this to use the program
    # Setup:
    start = datetime.date(2020, 1, 1)
    today = now().date()

# Generated at 2022-06-14 04:29:37.370129
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from dataclasses import dataclass, field
    from decimal import Decimal
    from typing import cast

    @dataclass
    class Tx:
        """
        Type alias for transactions.
        """
        pass

    @dataclass
    class TestJournalEntry(JournalEntry[Tx]):
        """
        Test journal entry.
        """

        #: Transaction of the entry.
        tx: Tx


# Generated at 2022-06-14 04:29:46.272870
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Arrange
    period: DateRange = DateRange(datetime.date(2018, 12, 25), datetime.date(2019, 4, 16))

    # Act

# Generated at 2022-06-14 04:29:50.768473
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 1, 31))
    read_initial_balances = lambda _: {}
    read_journal_entries = lambda _: []
    glp = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    gl = glp(period)
    assert gl.period == period
    assert gl.ledgers == {}

# Generated at 2022-06-14 04:31:13.117628
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    ## Example input data:
    initial_balances = {Account("10100"): Balance(datetime.date(2020, 5, 31), 1000), Account("10200"): Balance(datetime.date(2020, 5, 31), 2000)}
    journal_entries = [
        JournalEntry(datetime.date(2020, 6, 2), "", [Posting(Account("10100"), 1000), Posting(Account("10200"), -1000)]),
        JournalEntry(datetime.date(2020, 6, 11), "", [Posting(Account("10100"), -1000), Posting(Account("10200"), 1000)]),
    ]
    period = DateRange(datetime.date(2020, 6, 1), datetime.date(2020, 6, 30))
    ## Compile the program:

# Generated at 2022-06-14 04:31:15.886499
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    def _assert(period: DateRange):
        raise NotImplementedError()

    assert hasattr(_assert, "__call__")



# Generated at 2022-06-14 04:31:21.604114
# Unit test for method add of class Ledger
def test_Ledger_add():
    ledger=Ledger(Account('acc'),Balance(datetime.date(1,1,1),10))
    posting=Posting(datetime.date(1,1,1),Account('penis'),Account('penis'),-0.5,JournalEntry('description','description'))
    assert ledger.add(posting).balance==9.5

# Generated at 2022-06-14 04:31:30.476190
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.tosca import tosca
    from .accounts import AccountType
    from .journaling import ReadJournalEntries

    # Test cases

# Generated at 2022-06-14 04:31:36.380711
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Test method add of class Ledger
    """
    import pytest
    from ..commons.context import Omit
    from ..commons.numbers import Amount
    from .accounts import Account
    from .journaling import Journal, Posting

    class JournalingContext:
        def __init__(self):
            self.journaling_values = []

        def add_journal_entry(self, journal):
            self.journaling_values.append(journal)

    def get_fixture(account_number, date, description, amount, direction):
        # journaling_context
        journaling_context = JournalingContext()

        # account
        account = Account(account_number)

        # initial
        initial_balance = Amount(2)

# Generated at 2022-06-14 04:31:41.206516
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class ReadInitialBalancesImpl(ReadInitialBalances):
        """
        Provides an implementation of the algebra.
        """

        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    ReadInitialBalancesImpl()(DateRange(datetime.date(2020, 6, 1), datetime.date(2020, 6, 30)))

# Generated at 2022-06-14 04:31:49.573098
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.zeitgeist import DateRange
    from ..util.random import generate_random_dict, generate_random_date_range, generate_random_balance

    b = {generate_random_balance(): generate_random_balance() for _ in range(100)}

    def _(p: DateRange) -> {generate_random_balance(): generate_random_balance()}:
        return b

    assert _(generate_random_date_range()) == b


# Generated at 2022-06-14 04:32:01.042670
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounting import Period
    from .program import program
    from .units import BalanceSheet, create_accounts_hierarchy

    # Define initial balances:

# Generated at 2022-06-14 04:32:12.270342
# Unit test for function build_general_ledger
def test_build_general_ledger():
    ## Define the accounting period.
    period = DateRange(datetime.datetime(2019, 3, 31, 0, 0, 0), datetime.datetime(2019, 6, 30, 0, 0, 0))

    ## Initial Balances:
    initial_balances = {
        Account("Cash", "111100"): Balance(period.since, Quantity(Decimal(1000))),
        Account("Accounts Receivable", "112100"): Balance(period.since, Quantity(Decimal(0))),
    }

    ## Journal Entries:

# Generated at 2022-06-14 04:32:18.839612
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from ..commons.zeitgeist import Period
    from ..accountancy.ledgers import InitialBalances
    period = Period("2019-01-01", "2019-12-31")
    initial_balances = InitialBalances({})
    assert initial_balances == InitialBalances({})
    

# Generated at 2022-06-14 04:32:55.266824
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    try:
        Period = DateRange  # type: ignore
    except:
        def Period(since: datetime.date, until: datetime.date) -> DateRange:
            return DateRange(since, until)

    import datetime
    from unittest.mock import MagicMock

    from .accounts import Account
    from .journaling import Journal, Posting

    assert compile_general_ledger_program

    ## Set up account model:
    a = Account("a")
    b = Account("b")
    c = Account("c")
    d = Account("d")

    ## Set up journal entries:
    j1 = Journal("j1", datetime.date(2020, 12, 31), [Posting(a, Decimal("100.00")), Posting(b, Decimal("-100.00"))])
    j

# Generated at 2022-06-14 04:33:04.872407
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import datetime
    from decimal import Decimal
    from ..commons.types import K
    from ..commons.zeitgeist import DateRange
    from .accounts import AccountType, Account
    from .generic import Balance
    from .journaling import JournalEntry, Posting
    from .core import BusinessObject

    # 1. Define the general ledger program

# Generated at 2022-06-14 04:33:15.116896
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Create test Ledger
    account = Account()
    initial = Balance(initial_date=datetime.date(year=2020, month=1, day=1), initial_value=Quantity(7))
    test_ledger = Ledger(account=account, initial=initial)
    account2 = Account()
    posting = Posting(account=account2, amount=Amount(1), direction=Direction.CREDIT)
    posting2 = Posting(account=account2, amount=Amount(1), direction=Direction.DEBIT)
    test_ledger.add(posting)
    test_ledger.add(posting2)
    print(test_ledger.entries)

# Generated at 2022-06-14 04:33:16.662794
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert callable(ReadInitialBalances.__call__)


# Generated at 2022-06-14 04:33:23.804140
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Builds a general ledger with a single account.
    """
    from datetime import date
    from freezegun import freeze_time

    ## Import local account types.
    from ..accounts import AccountType, Account

    ## Import local journaling types.
    from ..journaling import JournalEntry, Posting

    ## Import local ledger entries types.
    from ..ledgers import GeneralLedger, Ledger, LedgerEntry

    ## Define an account type.
    account_type = AccountType("Test", 100000, "Test account type.")

    ## Define a terminal account.
    account = Account(10000, "Test", "Test account.", account_type)

    ## Define a journal entry.
    journal_entry = JournalEntry(date(2019, 1, 1), "Test journal entry.")

    ## Define the corresponding posting.
   

# Generated at 2022-06-14 04:33:29.819900
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert ReadInitialBalances[object].__call__.__doc__ == '__call__(self, period: DateRange) -> InitialBalances'
    assert ReadInitialBalances[object].__call__.__annotations__ == {'self': ReadInitialBalances[object], 'period': DateRange, 'return': InitialBalances}


# Generated at 2022-06-14 04:33:38.875090
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .commons import T
    from .journaling import Journal, Posting
    from .generic import Balance

    @dataclass
    class Program(GeneralLedgerProgram[T]):
        def __call__(self, period: DateRange) -> GeneralLedger[T]:
            pass

    from datetime import date
    from hamcrest import assert_that, is_
    assert_that(
        Program()(DateRange(date(2018, 1, 1), date(2018, 12, 31))),
        is_(GeneralLedger(DateRange(date(2018, 1, 1), date(2018, 12, 31)), {})),
    )
