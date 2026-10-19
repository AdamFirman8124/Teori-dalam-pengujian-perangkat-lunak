

# Generated at 2022-06-14 04:23:55.715091
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from . import accounts as a, journaling as j
    from datetime import date, timedelta
    from decimal import Decimal
    from fractions import Fraction
    from .journaling import Posting, Journal

    # A sample set of journal entries.

# Generated at 2022-06-14 04:23:58.607598
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    def __call__(self, period: DateRange) -> InitialBalances:
        pass

    assert isinstance(__call__, ReadInitialBalances)


# Generated at 2022-06-14 04:24:11.649276
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .algebras import JournalingAlgebra

    from .algebras import JournalingAlgebra
    from .accounts import Account, AccountType
    from .journaling import JournalEntry

    ## Define programs:
    read_initial_balances = lambda period: {}
    read_journal_entries = lambda period: []
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Build general ledger:
    ledger = program(DateRange(datetime.date(2021, 3, 12), datetime.date(2021, 3, 13)))

    ## Verify type:
    assert isinstance(ledger, GeneralLedger)

    ## Verify period:
    assert ledger.period.since == datetime.date(2021, 3, 12)
    assert ledger.period.until

# Generated at 2022-06-14 04:24:21.484700
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .standards import AccountingPeriod
    from .journaling import Journal
    from .accounts import AccountType
    from datetime import datetime
    import random
    import pytest
    from dataclasses import dataclass, field
    from decimal import Decimal
    from typing import List, Dict
    from pykechain.commons.zeitgeist import DateRange
    from pykechain.commons.numbers import Amount, Quantity
    from pykechain.models import Account, Balance

    Assets = AccountType("Assets")
    Expenses = AccountType("Expenses")

    Cash = Account("Cash", Assets, "not_term")
    Bank = Account("Bank", Assets, "not_term")
    AccountsReceivable = Account("AR", Assets, "term")
    Prepayments = Account("Prepayments", Assets, "term")



# Generated at 2022-06-14 04:24:29.713949
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {}

    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return []

    gl = compile_general_ledger_program(_read_initial_balances, _read_journal_entries)(DateRange(datetime.date(2000, 1, 1), datetime.date(2000, 12, 31)))
    assert type(gl) == GeneralLedger

# Generated at 2022-06-14 04:24:30.897353
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass



# Generated at 2022-06-14 04:24:39.059306
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import Account, AccountId, AccountType

    #: Accounting period.
    period = DateRange("2018-01-01", "2018-12-31")

    #: An account.
    account = Account(AccountId("1"), AccountType("EXPENSE", "Expense"), "Rent")

    #: Opening balance.
    opening_balance = Balance(period.since, Quantity(Decimal("1")))

    #: A journal entry.
    journal_entry = JournalEntry(
        _date=period.since,
        _description="Rent for January 2018.",
        _postings=[
            Posting(
                account=account,
                amount=Amount(Decimal("1")),
                description="Rent for January 2018.",
                journal=journal_entry,
            )
        ],
    )

    #: An implementation of

# Generated at 2022-06-14 04:24:51.724608
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import datetime
    #from commons.dbconnection import IDBConnection
    #from dataclasses import dataclass
    from decimal import Decimal
    #from typing import Dict, Generic, Iterable, List, Optional, TypeVar
    from unittest.mock import Mock
    from unittest.mock import MagicMock
    from .accounts import Account
    from .journaling import JournalEntry, Posting, ReadJournalEntries
    from .validation import ValidatedAccountTree

    #: Defines a generic type variable.
    _T = TypeVar("_T")

    #: Initial balances:
    InitialBalances = Dict[Account, Balance]

    #: ReadInitialBalances implementation

# Generated at 2022-06-14 04:24:57.519980
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Create an instance of ReadInitialBalances:
    read_initial_balances = ReadInitialBalances()

    # Try to invoke method __call__ of class ReadInitialBalances:
    try:
        read_initial_balances.__call__(DateRange(datetime.date(2018,1,1), datetime.date(2018,12,31)))
    except AttributeError:
        print('Method __call__ of class ReadInitialBalances is undefined')


# Generated at 2022-06-14 04:25:08.967173
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import Account
    from .journaling import JournalEntry
    from .primitives import Quantity

    class TestReadInitialBalances:
        def __call__(self, period: Period) -> InitialBalances:
            return {Account("1"), Account("21")};

    class TestReadJournalEntries:
        def __call__(self, period: Period) -> Iterable[JournalEntry]:
            return [Entry, Entry2]

    Entry = JournalEntry(datetime.date(2019, 12, 1), "JE1", [
        Posting(Account("1"), Quantity(1000)),
        Posting(Account("2"), Quantity(1000))
    ])


# Generated at 2022-06-14 04:25:24.514717
# Unit test for function build_general_ledger
def test_build_general_ledger():
    period = DateRange(since=datetime.date(2018, 1, 1), until=datetime.date(2018, 12, 31))
    journal = [
        JournalEntry(
            date=datetime.date(2018, 1, 1),
            description="Hello world",
            postings=[
                Posting(account=Account.ASSET.CASH, amount=Amount(Decimal(1000.00)), direction=Posting.Debit),
                Posting(account=Account.REVENUE.SALES, amount=Amount(Decimal(1000.00)), direction=Posting.Credit),
            ],
        )
    ]
    initial = {Account.ASSET.CASH: Balance(datetime.date(2018, 1, 1), Quantity(Decimal(100.00)))}

# Generated at 2022-06-14 04:25:37.516242
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import AccountId, AccountTree
    from .journaling import JournalEntry, Posting, build_journal_entry
    from .generic import Balance
    from datetime import datetime, timedelta

    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {a: Balance(period.since, Quantity(Decimal(0))) for a in AccountTree.root.get_terminal_accounts()}

    def _read_journal_entries(period: DateRange) -> List[JournalEntry[_T]]:
        return [build_journal_entry(datetime.now(), "TEST JOURNAL ENTRY")]

    _program = compile_general_ledger_program(_read_initial_balances, _read_journal_entries)

# Generated at 2022-06-14 04:25:46.911361
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from dataclasses import dataclass
    from datetime import date, timedelta
    from decimal import Decimal
    from itertools import product
    from .accounts import Account, AccountGroup
    from .journaling import Journal, JournalEntry, Posting
    from ..commons.enumeration import Direction

    #: Test account groups:
    income = AccountGroup(0, "Income")
    trade = income.subgroup(1, "Trade")
    expense = AccountGroup(2, "Expense")
    provision = expense.subgroup(3, "Provision")
    assets = AccountGroup(4, "Assets")
    liabilities = AccountGroup(5, "Liabilities")

    #: Test accounts:
    account_a = trade.account(1, "A")

# Generated at 2022-06-14 04:25:59.363032
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from . import Accounts
    from .journaling import Journal
    from .journaling.algebra import journal_entry

    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 4))
    initial_balances = {Accounts.cash(): Balance(datetime.date(2019, 12, 31), Quantity(1200))}
    journal_entries = [
        journal_entry(1, period.since, Accounts.petty_cash(), Accounts.cash(), 200),
        journal_entry(2, period.since, Accounts.cash(), Accounts.accounts_receivable(), 150),
        journal_entry(3, period.since, Accounts.accounts_receivable(), Accounts.cash(), 130),
    ]

    gl = build_general_ledger(period, journal_entries, initial_balances)

   

# Generated at 2022-06-14 04:26:12.483070
# Unit test for method add of class Ledger
def test_Ledger_add():
    G = Ledger("Ledger1")
    G.add(Posting("D", Decimal("10")))
    assert G.entries[0] == LedgerEntry(G, Posting("D", Decimal("10")))
    assert G.entries[0].balance == Decimal("10")
    G.add(Posting("C", Decimal("5")))
    assert G.entries[1] == LedgerEntry(G, Posting("C", Decimal("5")))
    assert G.entries[1].balance == Decimal("5")
    assert G.entries[0].balance == Decimal("10")
    G.add(Posting("D", Decimal("5")))
    assert G.entries[2] == LedgerEntry(G, Posting("D", Decimal("5")))

# Generated at 2022-06-14 04:26:20.392423
# Unit test for method add of class Ledger
def test_Ledger_add():
    print("Entering test_Ledger_add()")
    @dataclass
    class _Journal:
        description: str = ""
        entries: List[JournalEntry] = field(default_factory=list)

    journal = _Journal()

    L = Ledger(Account(123), Balance(datetime.date(1,1,1), Quantity(1)))
    L.add(Posting(JournalEntry(datetime.date(1,1,1), Amount(1)), Account(1), Account(2), 1))

if __name__ == "__main__":
    test_Ledger_add()

# Generated at 2022-06-14 04:26:32.651604
# Unit test for function build_general_ledger
def test_build_general_ledger():
    @dataclass
    class Unit:
        """
        We will use this mock class as the :py:class:`~app.journaling.Posting.unit` property.
        """

        name: str

    # A few journals:

# Generated at 2022-06-14 04:26:45.530801
# Unit test for function build_general_ledger
def test_build_general_ledger():
    #: Defines a generic type variable.
    _T = TypeVar("_T")
    from .accounts import Account, Asset, Liability
    from .journaling import JournalEntry, Posting

    ## Helper alias.
    date = datetime.date

    ## Assets
    checking_acct = Account(Asset, "1111", "Checking")
    cashier_check_acct = Account(Asset, "1112", "Cashier's Check")
    ## Liabilities
    capital_acct = Account(Liability, "2101", "Capital")
    capital_draw_acct = Account(Liability, "2102", "Capital Draw")

    ## Initial balances:

# Generated at 2022-06-14 04:26:55.747156
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import Account
    from .journaling import JournalEntry, Posting, SimpleJournal

    @dataclass
    class AccountsReadInitialBalances:
        initial: InitialBalances

        def __call__(self, period: DateRange) -> InitialBalances:
            return self.initial

    initial_balances = InitialBalances({
        Account(10000, "Cash"): Balance(datetime.date(2019, 1, 1), Quantity(0))
    })

    @dataclass
    class AccountsReadJournalEntries:
        journal: Iterable[JournalEntry]

        def __call__(self, period: DateRange) -> Iterable[JournalEntry]:
            return self.journal


# Generated at 2022-06-14 04:26:57.428516
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    ## This unit test requires manual checking.
    pass

# Generated at 2022-06-14 04:27:12.669476
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2022-06-14 04:27:16.886988
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # a dummy implementation of the ReadInitialBalances algebra.
    def _read_initial_balances(period: DateRange) -> InitialBalances:
        # the initial balances for account 6
        initial_balances = {6: Balance(period.since, Quantity(Decimal(0)))}
        # return the initial balances
        return initial_balances
    # a dummy implementation of the ReadJournalEntries algebra.
    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        # create a dummy journal entry
        journal_entry = JournalEntry(_T=None, date=period.until, description="Dummy journal entry", postings=[])
        # return the dummy journal entry
        return [journal_entry]
    # compile the program

# Generated at 2022-06-14 04:27:25.644611
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Validates if the general ledger program works as expected:
    """
    ## Define a journal entry model:
    @dataclass
    class TransactionModel:
        id: int

    ## Create the program:

# Generated at 2022-06-14 04:27:30.074679
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from copy import copy
    from io import StringIO
    from datetime import date
    from decimal import Decimal
    from unittest import TestCase
    from uuid import uuid4
    from .commons.zeitgeist import DateRange
    from .journaling import JournalEntry
    from .accounts import Account, TerminalAccount
    from .generic import Balance
    from .adapters.mem import TransactionJournalEntries, TransactionInitialBalances
    from .adapters.csv import JournalEntryParser
    from .api import compile_general_ledger_program
    from .ledgers import build_general_ledger, GeneralLedger, LedgerEntry, Ledger

    ## VARIABLES
    #: Some test accounts.
    A_ASSETS = TerminalAccount(uuid4(), 0, "ASSETS", True, None)
    A_EQUITY

# Generated at 2022-06-14 04:27:39.745141
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..commons.zeitgeist import parse_datetime
    from .accounts import Account
    from .generic import Balance, Quantity
    from .journaling import JournalEntry, Posting

    # Define accounts:
    assets = Account('Assets', None)
    expenses = Account('Expenses', assets)
    advertising = Account('Advertising', expenses)
    cash = Account('Cash', assets)
    ltd = Account('LTD', assets)
    revenue = Account('Revenue', None)
    sales = Account(
        'Sales', revenue
    )  # This account will be skipped because it's not a terminal account.
    eu_sales = Account('EU Sales', sales)
    nz_sales = Account('NZ Sales', sales)
    wages = Account('Wages', expenses)

    # Define initial balances:
    initial_

# Generated at 2022-06-14 04:27:41.983982
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert False, "Unit test not implemented."


# Generated at 2022-06-14 04:27:46.320810
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class Mock(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return InitialBalances

    assert Mock()(DateRange()) == InitialBalances


# Generated at 2022-06-14 04:27:57.010640
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Initialize accounts
    a = Account("A")
    b = Account("B")
    c = Account("C")

    # Initialize ledger
    ledger_AB = Ledger(a, 0)

    # Initialize and add journal entries
    je1 = JournalEntry(20190710, "JE1")
    je1.add_posting(a, 1)
    je1.add_posting(b, 1)
    je2 = JournalEntry(20190710, "JE2")
    je2.add_posting(a, 1)
    je2.add_posting(c, 1)
    ledger_AB.add(je1.postings[0])
    ledger_AB.add(je2.postings[0])

    # Check balance of account A
    assert ledger_AB.initial.value == 0

# Generated at 2022-06-14 04:28:09.214462
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    
    from .accounts import Account

    from .journaling import Posting, JournalEntry, JournalWrite, JournalRead

    ### Lightweight implementations for testing purposes:
    journal_write = JournalWrite()
    journal_read = JournalRead()

    ### Sample journal entries:
    je1 = JournalEntry(
        date(2019, 12, 31), "Capital 2019", [Posting("Asset", "Bank", 100), Posting("Equity", "Capital", -100)]
    )
    je2 = JournalEntry(
        date(2019, 12, 31), "Sales 2019", [Posting("Asset", "Accounts Receivable", 500), Posting("Income", "Sales", -500)]
    )

# Generated at 2022-06-14 04:28:10.277011
# Unit test for method add of class Ledger
def test_Ledger_add():
    # TODO: Implement unit tests
    not_implemented_yet()

# Generated at 2022-06-14 04:28:27.665979
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Perform a unit test for method add of class Ledger
    """
    from .accounts import Account, AccountType

    Posting1 = Posting(Account(AccountType.ASSET, code=1234, name="Customer Receivables (1234)"),
                       Date(2019, 1, 1), Quantity(100), "Description")
    Posting2 = Posting(Account(AccountType.ASSET, code=1234, name="Customer Receivables (1234)"),
                       Date(2019, 1, 1), Quantity(100), "Description")
    Posting3 = Posting(Account(AccountType.ASSET, code=1234, name="Customer Receivables (1234)"),
                       Date(2019, 1, 1), Quantity(100), "Description")

# Generated at 2022-06-14 04:28:36.484964
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Journal, Posting, JournalEntry

    _a1 = Account("A1")  # Receivables
    _a2 = Account("A2")  # Payables
    _a3 = Account("A3")  # Inventories
    _a4 = Account("A4")  # Sales
    _a5 = Account("A5")  # Other Revenue
    _a6 = Account("A6")  # Cost of Sales
    _a7 = Account("A7")  # Gross Profit
    _a8 = Account("A8")  # Expenses

    _b1 = Balance(datetime.date(2020, 1, 31), Quantity(20000))
    _b2 = Balance(datetime.date(2020, 1, 31), Quantity(-3000))

# Generated at 2022-06-14 04:28:37.393318
# Unit test for function build_general_ledger
def test_build_general_ledger():
    pass

# Generated at 2022-06-14 04:28:38.459545
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass


# Generated at 2022-06-14 04:28:40.361812
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert ReadInitialBalances.__call__(object, datetime.datetime)

# Generated at 2022-06-14 04:28:47.939018
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from random import randint, seed
    from ..bank.bookkeeping import JournalEntry
    from ..commons.zeitgeist import date

    ## Set seed:
    seed(0)

    period = DateRange(date(2020, 1, 1), date(2020, 6, 1))

    ## Define initial balances:

# Generated at 2022-06-14 04:28:59.107714
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import datetime
    from ..commons.numbers import EUR, Amount, Quantity
    from ..journaling.algebra import ReadJournalProgram
    from ..journaling.entities import Journal
    from ..journaling.journal import ReadJournalEntries
    from .accounts import Account
    from .journaling import Posting

    def run(period: datetime.date):
        ## Basics of our test:
        ledger_period = DateRange(datetime.date(period.year, 1, 1), datetime.date(period.year, 12, 31))
        ## Account for the ledger:
        account = Account(1, "Test account")
        ## Journal of ledger entries:
        journal = Journal(datetime.date(period.year, 1, 1), "Test journal")
        ## Create postings for the journal:
        posting = lambda d, a: Posting

# Generated at 2022-06-14 04:29:12.279175
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.chronos import Day
    from ..commons.numbers import Quantity
    from ..commons.zeitgeist import DateRange
    from ..masterdata.accounts import Account

    from ..journaling import build_journal_entry

    from .journaling import Posting

    import datetime

    ## Setup the test period:
    d1 = datetime.date(2019, 3, 4)
    d2 = datetime.date(2019, 4, 2)
    period = DateRange(Day(d1), Day(d2))

    ## Setup some test accounts:
    cash = Account(10000, "CASH AND CASH EQUIVALENTS")
    sales_revenue = Account(40000, "SALES REVENUE")
    accounts_receivable = Account(50000, "ACCOUNTS RECEIVABLE")
    sales

# Generated at 2022-06-14 04:29:25.063273
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import JournalEntry, Posting, ReadJournalEntries
    from .accounts import Account, AccountKind

    ## Define a test account:
    test_account = Account(
        name="Test Account",
        description="Test Account for Unit Testing",
        kind=AccountKind.LIABILITY,
        number=100,
    )

    ## Define test initial balances as of the end of previous financial period:
    initial_balances = {test_account: Balance(datetime.date(2018, 12, 31), Quantity(Decimal(1000)))}

    ## Define the test journal entries:

# Generated at 2022-06-14 04:29:25.746067
# Unit test for method add of class Ledger
def test_Ledger_add():
    assert True

# Generated at 2022-06-14 04:30:03.134965
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import PostingDirection
    from .accounts import AccountType

    a_account = Account.get_account("1.1.1.1", "A", AccountType.ASSETS)
    b_account = Account.get_account("1.1.1.2", "B", AccountType.ASSETS)
    c_account = Account.get_account("1.1.1.3", "C", AccountType.ASSETS)
    d_account = Account.get_account("1.1.3.1", "D", AccountType.LIABILITIES)
    e_account = Account.get_account("1.1.3.2", "E", AccountType.LIABILITIES)
    f_account = Account.get_account("1.1.3.3", "F", AccountType.LIABILITIES)
    g

# Generated at 2022-06-14 04:30:16.116033
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from typing import Dict
    from decimal import Decimal
    from datetime import date
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .generic import Balance
    from .ledgering import ReadInitialBalances

    class MockReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> Dict[Account, Balance]:
            return {Account.parse('1100'): Balance(date(2018, 12, 31), Decimal(100)),
                    Account.parse('1200'): Balance(date(2018, 12, 31), Decimal(200))}

    # subject
    subject = MockReadInitialBalances()

    # expectations

# Generated at 2022-06-14 04:30:23.939710
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program.
    """
    ## Required imports:
    from logging import DEBUG, basicConfig, getLogger
    from ..commons.algebra import Algebra
    from .accounts import read_accounts, AccountProgram
    from .journaling import JournalEntryProgram
    
    ## Configure basic logging for unit-test:
    basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=DEBUG)

    ## Initialize a logger for this unit-test:
    logger = getLogger(__name__)

    ## Initialize the algebra:
    algebra = Algebra(logger=logger)

    ## Initialize the account program:
    account_program = AccountProgram(read_accounts(algebra))

    ## Initialize the

# Generated at 2022-06-14 04:30:26.063080
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram
    """
    pass

# Generated at 2022-06-14 04:30:39.044758
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import Account, AccountType, BasicAccount
    from .journaling import Journal
    from .numbers import Decimal, Date

    @dataclass
    class FakeAlgebra:
        def __call__(self, period: DateRange):
            pass

    @dataclass
    class FakeInitialBalances(FakeAlgebra):
        def __call__(self, period: DateRange):
            return {}

    @dataclass
    class FakeJournalEntries(FakeAlgebra):
        def __call__(self, period: DateRange):
            return {}

    alg1 = FakeInitialBalances()
    alg2 = FakeJournalEntries()
    p = compile_general_ledger_program(alg1, alg2)

    #: Generate a random date range.

# Generated at 2022-06-14 04:30:41.343479
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class Mock(Generic[_T]):
        def __call__(self, period: DateRange) -> InitialBalances:
            pass

    Mock()

# Generated at 2022-06-14 04:30:45.363627
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Unit tests for method __call__ of class ReadInitialBalances
    """
    from .tests.fixtures.algebra import read_initial_balances

    assert read_initial_balances(DateRange(datetime.date(2019, 4, 1), datetime.date(2019, 6, 30))) == {
        Account.from_string("1110/101 Cash in hand"): Balance(datetime.date(2019, 4, 1), Quantity(Decimal(3000)))
    }



# Generated at 2022-06-14 04:30:46.423371
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:30:49.321168
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests for method __call__ of class GeneralLedgerProgram.
    """

    assert compile_general_ledger_program(None, None)

# Generated at 2022-06-14 04:30:56.656229
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():

    from unittest.mock import Mock

    from .algebra import build_accounts

    ## Mock reading of initial balances:
    read_initial_balances = Mock(spec_set=ReadInitialBalances)
    read_initial_balances.return_value = {
        Account("BANK"): Balance(datetime.date(2020, 1, 1), Decimal(0)),
        Account("EQUITY"): Balance(datetime.date(2020, 1, 1), Decimal(0)),
    }

    ## Mock reading journal entries:
    read_journal_entries = Mock(spec_set=ReadJournalEntries)
    read_journal_entries.return_value = list(build_accounts(datetime.date(2020, 2, 1)).journal())

    ## Compile the general ledger program:
    general_ledger_program

# Generated at 2022-06-14 04:31:56.589437
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import AccountFactory
    from .journaling import JournalEntry, Posting
    from .protocols import JournalPosting, PostingStuff

    # Create an account
    account = AccountFactory.assets("PLDT")

    # Create a posting
    posting = Posting(
        '2018-01-01',
        JournalEntry('2018-01-01', 'Description', [
            PostingStuff(account, 'Debit', 100)
        ])
    )

    # Create a ledger
    balance = Balance('2018-01-01', Quantity(Decimal(1000)))
    ledger = Ledger(account, balance)

    # Add a posting to the ledger
    posting = ledger.add(posting)

    assert posting.balance == 1100
    assert posting.balance == ledger._last_balance

# Generated at 2022-06-14 04:32:05.292323
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Use the Zeepin package itself as a test case.
    import zeepin.algebra.transaction as transaction

    # Define an accounting period
    period = DateRange(since=datetime.date(2018, 1, 1), until=datetime.date(2018, 12, 31))

    # Define a general ledger program
    program = compile_general_ledger_program(transaction.read_initial_balances, transaction.read_journal_entries)

    # Exceute the program
    general_ledger = program(period)

    # Assert the general ledger
    assert len(general_ledger.ledgers) == 21
    assert general_ledger.period.since == period.since
    assert general_ledger.period.until == period.until


# Generated at 2022-06-14 04:32:14.806066
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import datetime
    from decimal import Decimal
    from typing import cast
    from unittest.mock import Mock
    from ..commons.numbers import Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .generic import Balance

    ## Create a date and a date range:
    date = datetime.date.today()

    ## Create a mock account:
    account = Account("A1", "A1 Account")

    ## Create a mock balance:
    balance = Balance(date, Quantity(Decimal(1)))

    ## Create a mock ReadInitialBalances instance:
    read_initial_balances = Mock(spec=ReadInitialBalances, wraps=lambda period: {account: balance})

    ## Call the mock instance as if an instance of ReadInitialBalances:
    result = read_initial_

# Generated at 2022-06-14 04:32:27.393415
# Unit test for function compile_general_ledger_program

# Generated at 2022-06-14 04:32:40.921068
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from fractions import Fraction

    from .accounts import Account, AccountScheme
    from .accounts import build_terminal_accounts

    from .journaling import JournalEntry
    from .journaling import Posting, Direction

    from .quantities import Balance
    from .quantities import Quantity


# Generated at 2022-06-14 04:32:49.475987
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .algebra import algebra
    from .commons.zeitgeist import DATE
    from .journaling import journal_entry, Posting, simple_posting
    from .pedigree import Person

    def _read_initial_balances(period):
        return {
            Account("Assets", "Cash"): Balance(DATE("2020-01-01"), Quantity(Decimal(1000))),
            Account("Liabilities", "Payable"): Balance(DATE("2020-01-01"), Quantity(Decimal(2000))),
            Account("Equity", "Capital"): Balance(DATE("2020-01-01"), Quantity(Decimal(-2000))),
        }

    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[Person]]:
        journal_entries = list()

# Generated at 2022-06-14 04:32:50.793964
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert False


# Generated at 2022-06-14 04:32:56.933835
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..accounts import Account

    l = Ledger(Account('A'), Balance(datetime.datetime.now(), Quantity(Decimal(0))))
    l.add(Posting(JournalEntry(), Account('A'), Amount('1'), is_debit=True, date=datetime.datetime.now()))
    assert len(l.entries) == 1

# Generated at 2022-06-14 04:33:04.767827
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    ## We're using some fakes instead of actual algebras:
    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 6, 30))

    initial_balances = {
        Account(["Assets", "Cash"]): Balance(datetime.date(2019, 12, 31), Quantity(Decimal(1000))),
        Account(["Assets", "Liabilities", "Account Payable"]): Balance(datetime.date(2019, 12, 31), Quantity(Decimal(2000))),
        Account(["Equity", "Retained Earnings"]): Balance(datetime.date(2019, 12, 31), Quantity(Decimal(3000))),
    }


# Generated at 2022-06-14 04:33:14.636692
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Testing method add of class Ledger
    """
    account1 = Account('1', 'TEST')
    balance1 = Balance(datetime.date(2020,6,30), Decimal(0))
    ledger1 = Ledger(account1, balance1)
    assert ledger1.account.name=="1"
    posting1 = Posting(DEBIT, Decimal(2), account1)
    assert ledger1.add(posting1).balance == Decimal(2)
    posting2 = Posting(DEBIT, Decimal(3), account1)
    assert ledger1.add(posting2).balance == Decimal(5)
