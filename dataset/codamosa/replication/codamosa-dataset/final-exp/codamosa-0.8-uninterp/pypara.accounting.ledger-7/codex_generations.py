

# Generated at 2022-06-14 04:23:53.859056
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.zeitgeist import DateRange
    from ..commons.numbers import Amount
    from .accounts import AccountType
    from .journaling import JournalEntry
    from .ledgering import Ledger,LedgerEntry
    from .generic import Balance
    import datetime
    period = DateRange(since=datetime.date(2017, 1, 1),until= datetime.date(2017, 12, 31))

# Generated at 2022-06-14 04:24:05.497237
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from datetime import date
    from math import isclose
    from typing import Callable
    from .accounts import Account as A
    from .commons.zeitgeist import DateRange as DR
    from .journaling import JournalEntry as JE, Posting as P
    from .auxiliary import ReadInitialBalances as RIB, ReadJournalEntries as RJE
    from .general_ledger import GeneralLedger as GL, compile_general_ledger_program as CLG
    from .ledger import Ledger as L
    from .ledgers import ReadLedgers as RL, ReadLedgerEntries as RLE

    # Initial balances:

# Generated at 2022-06-14 04:24:19.106786
# Unit test for method add of class Ledger
def test_Ledger_add():
    d1 = datetime.date(2020, 2, 1)
    d2 = datetime.date(2020, 2, 20)
    a1 = datetime.date(2020, 1, 31)
    a2 = datetime.date(2020, 2, 29)
    account = Account()
    balance = Balance(a1, Quantity(Decimal(0)))
    amount = Amount(Decimal(10))
    journal = JournalEntry(d1, "Test description")
    journal.add(account, amount)
    posting = journal.postings[0]
    generalLedger = Ledger(account, balance)
    generalLedger.add(posting)
    assert generalLedger.entries[-1].date == d1
    assert generalLedger.entries[-1].description == "Test description"
    assert generalLedger.ent

# Generated at 2022-06-14 04:24:33.064944
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    An account ledger holds initial balance and the list of ledger entries.
    The ledger entry is created by method add. The balance of the ledger entry is defined as the balance of the last
    ledger entry + the amount of the posting times the sign of the posting.
    """
    import datetime
    from decimal import Decimal
    from ..commons.numbers import Amount
    from ..commons.zeitgeist import DateRange
    start = datetime.date(2020, 1, 1)
    end = datetime.date(2020, 12, 31)
    period = DateRange(start, end)
    account = Account(1)
    amount = Amount(Decimal('100'))
    balance = Balance(period.since, amount)
    ledger = Ledger(account, balance)
    assert ledger.account == account
    assert ledger.initial == balance



# Generated at 2022-06-14 04:24:38.307076
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    read_initial_balances = lambda period: {Account("Account") : Balance(period.since, Quantity(Decimal(0)))}
    assert read_initial_balances(DateRange("2020-JAN-01", "2020-DEC-31")) == {Account("Account") : Balance(datetime.date(2020, 1, 1), Quantity(Decimal(0)))}


# Generated at 2022-06-14 04:24:39.038074
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:24:51.674209
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import AccountClass
    from .journaling import Journal, Posting, ReadJournalEntries
    import pathlib

    @dataclass
    class Config:
        root: pathlib.Path

    @dataclass
    class Metadata:
        path: pathlib.Path


# Generated at 2022-06-14 04:24:52.291946
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:25:05.293170
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import hypothesis.strategies as st
    from .accounts import LedgerAccount, TerminalAccount, AccountFamily
    from .journaling import GLJournalEntry

    def _build_AccountFamily():
        return AccountFamily("Test", "Test", LedgerAccount("Test", "Test"))

    @dataclass
    class _FakeInitialBalances(dict):
        def __call__(self, period: DateRange):
            return self

    class _FakeReadJournalEntries(dict):
        def __call__(self, period: DateRange):
            return self

    @dataclass
    class _FakeGeneralLedger(dict):
        pass

    @dataclass
    class _FakeJournalEntry(dict):
        pass


# Generated at 2022-06-14 04:25:11.807879
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Purpose: Unit test method __call__ of the class GeneralLedgerProgram.
    """
    #: Date range
    period = DateRange(datetime.date(2020, 10, 1), datetime.date(2020, 10, 31))

    #: List of journal entries

# Generated at 2022-06-14 04:25:16.178623
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:25:25.522550
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():

    @dataclass
    class _IB_Dummy:
        period: DateRange
        ibs: InitialBalances = field(default_factory=lambda: {Account("1100"): Balance(period.since, Quantity(Decimal(10)))})

        def __call__(self, period: DateRange) -> InitialBalances:
            return self.ibs

    @dataclass
    class _JE_Dummy:
        period: DateRange
        ents: Iterable[JournalEntry[_T]] = field(default_factory=lambda: [])

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return self.ents

    # TODO: test_compile_general_ledger_program

# Generated at 2022-06-14 04:25:26.666850
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    return True


# Generated at 2022-06-14 04:25:40.117340
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..accounts.accounttypes import CurrentAsset
    from ..accounts.accounttypes import CurrentLiability
    from ..accounts.accounttypes import Equity
    from ..accounts.accounttypes import Revenue
    from ..accounts.accounttypes import Expense

    from ..commons.zeitgeist import TODAY

    from ..journaling.journalentries import JournalEntry
    from ..journaling.journalentries import Posting
    from ..journaling.journalentries import PostingDirection

    from ..journaling.journals import Journal


# Generated at 2022-06-14 04:25:41.634050
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    assert compile_general_ledger_program


# Generated at 2022-06-14 04:25:55.464197
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .journaling import read_journal, post_journal_entry

    # -------------------------------------------------------------------------
    ## Arrange:
    ## 1. Define a list of mock journal entries.

# Generated at 2022-06-14 04:26:06.407878
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Arrange
    @dataclass
    class DateRangeStub:
        since: datetime.date
        until: datetime.date

    date_range_stub = DateRangeStub(datetime.date(2020, 1, 1), datetime.date(2020, 1, 31))

    class ReadInitialBalancesStub:
        def __call__(self, period: DateRange) -> InitialBalances:
            assert period == date_range_stub
            return {Account("1001"): Balance(datetime.date(2020, 1, 1), Quantity(Decimal(0)))}

    read_initial_balances_stub = ReadInitialBalancesStub()

    @dataclass
    class JournalEntryStub:
        date: datetime.date


# Generated at 2022-06-14 04:26:18.729259
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from . import accounts, journaling
    from datetime import date

    # Dictionary to simulate a list of initial balances.
    initial_balances = {
        accounts.asset_bank_accounts: Balance(date(2000, 1, 1), Quantity(100)),
        accounts.expense_general: Balance(date(2000, 1, 1), Quantity(10)),
        accounts.expense_salaries: Balance(date(2000, 1, 1), Quantity(5)),
    }

    # A function to simulate the read_initial_balances algebra.
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return initial_balances

    # A list of journal entries.

# Generated at 2022-06-14 04:26:31.789829
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ...core.domain.accounts import DefineAccount, DefineAccounts, account_book
    from ...core.domain.journaling import JournalEntry

    from .accounts import Account, AccountCategory
    from .journaling import Posting
    from .read import read_accounts
    from ..commons.numbers import Amount

    ## Account book:

# Generated at 2022-06-14 04:26:44.905217
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .generic import Balance

    from .accounts import Account

    from .journaling import JournalEntry, Posting, PostingOption

    from .mock import read_initial_balances, read_journal_entries, run_test_context

    ## Run test context:
    with run_test_context() as context:

        ## Algebra implementations:
        read_initial_balances_algebra = read_initial_balances(context)
        read_journal_entries_algebra = read_journal_entries(context)

        ## Compile the program:
        build_general_ledger_program = compile_general_ledger_program(
            read_initial_balances_algebra,
            read_journal_entries_algebra,
        )

        ## Accounting period:

# Generated at 2022-06-14 04:27:04.218357
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    _period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))
    _initial_balances_expected = [
        (
            Account("0000", "Dummy Account 1", "Dummy Account 1", "Dummy Account 1"),
            Balance(datetime.date(2020, 1, 1), Quantity(Decimal("0"))),
        ),
        (
            Account("0000", "Dummy Account 2", "Dummy Account 2", "Dummy Account 2"),
            Balance(datetime.date(2020, 1, 1), Quantity(Decimal("0"))),
        ),
    ]
    def _read_initial_balances(period: DateRange) -> Dict[Account, Balance]:
        assert period == _period

# Generated at 2022-06-14 04:27:12.770519
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ledger.models import TestAccounts
    from ledger.algebras import TestInitialBalances, TestJournalEntries

    ## Build the program:
    program = compile_general_ledger_program(TestInitialBalances(), TestJournalEntries())

    ## Define dates.
    since = datetime.date(2019, 1, 1)
    until = datetime.date(2019, 12, 31)

    ## Call the program and produce a general ledger.
    gl = program(DateRange(since, until))

    ## Check ledger balance.
    assert gl.ledgers[TestAccounts.sales]._last_balance == Decimal(12000)

    ## Check individual ledger entries.
    assert len(gl.ledgers[TestAccounts.sales].entries) == 3

# Generated at 2022-06-14 04:27:23.570003
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import AccountType, ChartOfAccounts
    from .journaling import JournalEntry, Posting, create_journal_entry
    from .numbers import Amount, Balance, Quantity, Signed
    from .units import Unit
    from .zeitgeist import DateRange, dates

    # Define demo-date utility:
    demo_date = dates(2020, 1, 1)

    # Define accounts:
    chart = ChartOfAccounts()
    cash = chart.add(AccountType.Asset, "1001", "Cash")
    accounts_payable = chart.add(AccountType.Liability, "2000", "Accounts payable")

    # Define currencies:
    base = Unit()
    usd = Unit(base, "USD")

    # Define initial balance:

# Generated at 2022-06-14 04:27:36.828478
# Unit test for function build_general_ledger
def test_build_general_ledger():

    from ..commons import DateInterval
    from ..commons.zeitgeist import Date

    from .accounts import TerminalAccount

    from .journaling import Journal, Posting, JournalEntry

    from .trialbalance import read_trial_balance_by_period, read_journal_entries_by_period

    ## Initial setup:
    period = DateRange(since=Date(2014, 1, 1), until=Date(2014, 12, 31))
    initial_balances = read_trial_balance_by_period(period)


# Generated at 2022-06-14 04:27:37.333741
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:27:51.503793
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Given
    from ..algebras.journaling import build_read_journal_entries, JournalEntry
    from ..algebras.accounts import build_read_account_tree, Account, AccountKind

    # noinspection PyTypeChecker
    read_initial_balances = lambda period: {
        Account("9400", AccountKind.ASSET, "Assets: Bank: Savings"): Balance(datetime.date(2019, 12, 31), Quantity(1300)),
        Account("9700", AccountKind.LIABILITY, "Liabilities: Tax"): Balance(datetime.date(2019, 12, 31), Quantity(1600)),
    }


# Generated at 2022-06-14 04:27:59.544467
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import BookkeepingSystem
    from .finance import Money, Cash

    def _test1():
        ## Define a date range:
        period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))

        ## Define initial balances:
        initial: InitialBalances = {
            Cash: Balance(period.since, Money(0, "TRY")),
        }

        ## Define journal entries:
        journal = []

        ## Build the general ledger:
        general_ledger = build_general_ledger(period, journal, initial)

        ## Done, return:
        return general_ledger


# Generated at 2022-06-14 04:28:01.088525
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    # TODO: This is a placeholder for test.
    pass

# Generated at 2022-06-14 04:28:11.025197
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.zeitgeist import now

    from .accounts import Account

    # Instanciate Account
    account = Account("compte", "compte n°1")

    # Instanciate a Ledger
    ledger = Ledger(account, Balance(now(), Quantity(Decimal(0))))

    # Declare a posting
    posting = Posting(
        account,
        now(),
        Amount(Decimal(10)),
        Quantity(Decimal(10)),
    )

    # Declare an expected value for entry.balance
    expected = Quantity(Decimal(10))

    # Add the posting to the ledger
    entry = ledger.add(posting)

    # Check if post.balance got the correct value
    assert entry.balance == expected

# Generated at 2022-06-14 04:28:12.568258
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:28:35.475287
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import build_journal_entry

    ## Setup a ledger and initial balances to test with:
    ledger = Ledger(Account(name="Main Account"), Balance(datetime.date(2019, 12, 31), Decimal("0")))

    ## Setup journal entries to post:
    journal_entries = [
        build_journal_entry(datetime.date(2020, 1, 1), "Opening Balance", [("Main Account", Decimal("1000"))])
    ]

    ## Compute the expected balance after posting all journal entries:
    balance = Quantity(reduce(lambda x, y: x + y, [je.postings[0].amount * je.postings[0].direction.value for je in journal_entries], Decimal("0")))

    ## Post the journal entries:

# Generated at 2022-06-14 04:28:46.207374
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account(0, "A")
    assert account != None

    initial = Balance(datetime.date(2019, 1, 1), Quantity(Decimal(0)))
    assert initial != None

    debit = Posting(account, datetime.date(2019, 1, 1), Quantity(Decimal(5000)), Direction.debit)
    assert debit != None

    credit = Posting(account, datetime.date(2019, 1, 1), Quantity(Decimal(1000)), Direction.credit)
    assert credit != None

    ledger = Ledger(account, initial)
    assert ledger != None
    assert ledger.account == account
    assert ledger.initial == initial
    assert ledger.entries == []

    assert ledger.account.code == 0
    assert ledger.initial.date.year == 2019
    assert ledger.initial.date.month == 1
   

# Generated at 2022-06-14 04:28:58.523885
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from hypothesis import given
    from .accounts import ACCT1, ACCT2, ACCT3, ACCT4
    from .generic import Balance
    from .journaling import Posting, JournalEntry
    from .money import EUR
    from .numbers import Quantity
    from .commodities import Commodity
    from .market import Market
    from .closing_rates import ClosingRates
    from .currency_market import CurrencyMarket, CurrencyMarketData
    from .algebra import (
        ReadInitialBalances,
        ReadJournalEntries,
        build_general_ledger,
        compile_general_ledger_program,
    )
    from typing import List
    from dataclasses import dataclass
    from datetime import date
    from decimal import Decimal
    from textwrap import dedent
    import pytest

# Generated at 2022-06-14 04:29:09.612464
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class Algebra(ReadInitialBalances):
        """
        An implementation of ReadInitialBalances.
        """

        initial_balances: InitialBalances

        def __call__(self, period: DateRange) -> InitialBalances:
            return self.initial_balances

    initial_balances = {Account(1, "Cash"): Balance(datetime.date(2018, 5, 1), Quantity(Decimal(1000)))}
    algebra = Algebra(initial_balances)
    assert algebra(DateRange(datetime.date(2018, 5, 1), datetime.date(2018, 7, 31))) == initial_balances



# Generated at 2022-06-14 04:29:10.640330
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Test for compile_general_ledger_program
    """
    pass

# Generated at 2022-06-14 04:29:11.044435
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:29:18.047398
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import JournalEntry as _JournalEntry, Posting as _Posting, Journal as _Journal
    from .accounts import Account as _Account

    from .algebra import Algebra as _Algebra

    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))

    def read_initial_balances() -> InitialBalances:
        return {_Account("10100"): Balance(period.since, Quantity(Decimal(5000))), _Account("10200"): Balance(period.since, Quantity(Decimal(-2000)))}


# Generated at 2022-06-14 04:29:18.767632
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:29:29.725642
# Unit test for function build_general_ledger
def test_build_general_ledger():
    ## Define a journal:
    @dataclass
    class JournalEntry1(JournalEntry):
        postings: List[Posting] = None

    journal_entry1 = JournalEntry1(date=datetime.date(2020, 1, 1), description="Open bank 1", postings=[])
    journal_entry2 = JournalEntry1(date=datetime.date(2020, 1, 2), description="Open bank 2", postings=[])
    ## Define an account:
    @dataclass
    class Account1(Account):
        name: str = "1000"
    account1 = Account1()

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry]:
        return [journal_entry1, journal_entry2]


# Generated at 2022-06-14 04:29:40.337908
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    This function tests the functionality of the function build_general_ledger()
    """
    # Create a test date range
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 1))
    # Create a test initial balance
    initial = {
        1: Balance(datetime.date(2018, 12, 30), Quantity(0.0)),
        2: Balance(datetime.date(2018, 12, 31), Quantity(1000.0))
    }
    # Create a test journal entry

# Generated at 2022-06-14 04:30:43.363716
# Unit test for method add of class Ledger
def test_Ledger_add():
    forTest = Account('Assets', 'Cash')
    forTest2 = Account('Assets', 'Accounts receivable')
    forTest3 = Account('Expenses', 'Rent')
    forTest4 = Account('Expenses', 'Operating Expenses')
    forTest5 = Account('Revenues', 'Revenue')
    forTest6 = Account('Revenues', 'Revenue 2')
    forTest7 = Account('Liabilities', 'Accounts Payable')
    forTest8 = Account('Equity', 'Paid in Capital')

    led1 = Ledger(forTest, Balance(datetime.date(2020, 7, 11), Quantity(Decimal(100))))
    led1.add(Posting(datetime.date(2020, 7, 11), Amount(Decimal(100)), forTest, 1))

# Generated at 2022-06-14 04:30:44.030097
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert "Not Implemented"


# Generated at 2022-06-14 04:30:55.901515
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import AccountTree, AccountType
    from .journaling import JournalEntry, Posting

    #
    # Set up fixtures:
    #
    # Reduce the period to a single week for unit-test convenience.
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 7))

    # Build an account tree.

# Generated at 2022-06-14 04:30:56.957511
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert False, "Test not implemented"


# Generated at 2022-06-14 04:31:03.644804
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Setup
    def initial_balances(period, result):
        assert period == DateRange(date(2019,1,1), date(2019,12,31))
        return result
    read_initial_balances = ReadInitialBalances()
    read_initial_balances.__call__ = initial_balances
        
    # Exercise
    result = read_initial_balances(DateRange(date(2019,1,1), date(2019,12,31)))

    # Verify
    assert result == result


# Generated at 2022-06-14 04:31:12.100949
# Unit test for function build_general_ledger
def test_build_general_ledger():
    # Load account database:
    from ..persistence.sql import SqlAccountRepository
    from ..persistence.accounts import test_account_repository
    from ..persistence.sql import create_sqlite_engine
    import os

    # Initialize database engine:
    db = create_sqlite_engine(os.path.join(os.path.dirname(__file__), "test.db"))
    db.connect()

    # Build a test account repository:
    account_repository = SqlAccountRepository(db)

    # Load test accounts into the repository:
    test_account_repository(account_repository)

    # Build an SQL-based journal entry reader:
    from ..persistence.sql import SqlJournalEntryRepository

    # Build an SQL-based journal entry repository:
    journal_repos

# Generated at 2022-06-14 04:31:23.537047
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Invoke the __call__ method of GeneralLedgerProgram and ensure it works properly.
    """
    ## Import packages:
    import datetime as dt
    from typing import Any, Iterable
    from unittest.mock import Mock

    ## Import the code to be tested:
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .generic import Amount, Balance
    from .journaling import JournalEntry, Posting, Quantity, Unit

    ## Define a sample class to be constructed for type safety:
    class _T:
        pass

    ## Define initial balances:
    starting_balance = Balance(dt.date(2000, 1, 1), Quantity(Decimal(0)))

# Generated at 2022-06-14 04:31:36.670588
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import JournalEntry, Posting, create_journal_entry
    import asysys.commons.numbers as numbers
    import asysys.commons.zeitgeist as zeitgeist
    import datetime
    import random

    ## Prepare a random date:
    date = datetime.date(random.randrange(2015, 2020, 1), random.randint(1, 12), random.randint(1, 28))

    ## Prepare a journal entry:
    journal_entry = create_journal_entry(
        date,
        "Random journal entry",
        (Posting("Debit account", numbers.Debit, random.randrange(1, 10000, 1)),),
        (Posting("Credit account", numbers.Credit, random.randrange(1, 10000, 1)),),
    )

    ## Build a general ledger for the journal

# Generated at 2022-06-14 04:31:43.806272
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import build_journal, JournalEntry
    from .accounts import Account, build_account

    ## Initialize the accounts and their balances for opening the ledger.
    accounts = [
        build_account(
            id=1, code="1010", basic_type="asset", short_name="Test asset", long_name="Test asset account",
        ),
        build_account(
            id=2, code="2020", basic_type="liability", short_name="Test liability", long_name="Test liability account",
        ),
    ]

    balances = [Balance(datetime.date(2019, 1, 1), Quantity(Decimal(100))), Balance(datetime.date(2019, 1, 1), Quantity(Decimal(200)))]

    ## Initialize example posting as if in a journal entry.
    posting_1 = Posting

# Generated at 2022-06-14 04:31:44.479199
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass


# Generated at 2022-06-14 04:33:03.643368
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Test the algebra:
    import re

    from .accounts import AccountBook, AccountNumberError, read_account_structure

    from .journaling import JournalEntry, Posting, Quantity, read_journal_entries

    from .ledgers import build_general_ledger, compile_general_ledger_program, GeneralLedger, GeneralLedgerProgram, \
        InitialBalances, Ledger, LedgerEntry, ReadInitialBalances

    from .registering import AccountRegister, ReadAccountRegister, read_account_register

    from .revaluing import ReadRevaluation, revalue_ledgers

    from .vouchering import Voucher

    from ..commons import datetime_range, datetime_today, unique_name
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange

   

# Generated at 2022-06-14 04:33:05.622143
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert callable(ReadInitialBalances.__call__)


# Generated at 2022-06-14 04:33:17.952031
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    @dataclass
    class JournalEntry:
        date: datetime.date
        description: str
        postings: List["Posting"]

    @dataclass
    class Posting:
        date: datetime.date
        account: str
        amount: int

    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {Account("A"): Balance(period.since, Quantity(10))}

    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry]:
        yield JournalEntry(datetime.date(2020, 1, 1), "Test journal entry 1", [Posting(datetime.date(2020, 1, 1), "A", 20)])

# Generated at 2022-06-14 04:33:24.264902
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import datetime

    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .journaling import Posting, JournalEntry


# Generated at 2022-06-14 04:33:25.025055
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    pass

# Generated at 2022-06-14 04:33:27.177540
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """Test compile_general_ledger_program, see documentation of that function."""
    from .journaling import compile_post_journal_entry_program

    assert compile_general_ledger_program(None, None)
    assert not compile_post_journal_entry_program([])

# Generated at 2022-06-14 04:33:37.901854
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    ##
    ## data
    ##
    period = DateRange(since=datetime.date(2020, 1, 1), until=datetime.date(2020, 2, 29))
    general_ledger = GeneralLedger(period, dict())
    ##
    ## mocks
    ##
    class ReadInitialBalancesMock:
        def __call__(self, period):
            return InitialBalances()

    class ReadJournalEntriesMock:
        def __call__(self, period):
            return list()

    class BuildGeneralLedgerMock:
        def __call__(self, period, journal, initial):
            return general_ledger

    ##
    ## exercise
    ##
    build_general_ledger_mock = BuildGeneralLedgerMock()
    general_ledger_program = compile_general_ledger_