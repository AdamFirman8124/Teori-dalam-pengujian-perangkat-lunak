

# Generated at 2022-06-14 04:23:41.476383
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import datetime

    @dataclass
    class FakeReadInitialBalances(ReadInitialBalances):
        initial_balances: InitialBalances

        def __call__(self, period: DateRange) -> InitialBalances:
            return self.initial_balances

    x = FakeReadInitialBalances({})
    assert isinstance(x, ReadInitialBalances), "Should be a ReadInitialBalances"
    assert x({}), "Should be callable"


# Generated at 2022-06-14 04:23:52.676069
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Unit test for function build_general_ledger
    """
    ## Import needed modules:
    from ..commons.zeitgeist import DateRange
    from ..modeling.accounts import Account, AccountType
    from ..modeling.journaling import JournalEntry, Posting

    ## Build a sample account tree:

# Generated at 2022-06-14 04:24:03.802384
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, JournalEntry
    from .accounts import Account

    # The account under test
    a = Account('Assets.Cash')
    b = Account('Liabilities.Loans')
    # The initial balances
    initial_balances = {a: Balance(datetime.date(2019, 1, 1), 0)}
    # The journal entry under test
    j = Journal('<JournalEntry>')
    j.posting(a,+100,'<Posting>')
    j.posting(b,-100,'<Posting>')
    j.date(datetime.date(2019, 1, 1))
    j.description('<Description>')
    # The ledger under test
    l = Ledger(a, initial_balances[a])
    l.add(j.postings[0])

# Generated at 2022-06-14 04:24:17.291804
# Unit test for method add of class Ledger
def test_Ledger_add():
    import unittest
    from .accounts import Account
    from .journaling import Journal, Direction, Posting
    from .commons.numbers import Amount

    account = Account(1, 'asset', 'Cash')
    balance = Balance(datetime.date(2020, 1, 1), Amount(0))
    test_ledger = Ledger(account, balance)
    entries = test_ledger.entries
    journal = Journal(datetime.date(2020,1,1), "Test Journal", Entries.asset_credit)
    posting = Posting(account, Direction.CREDIT, Amount(10), journal)
    test_ledger.add(posting)
    entries = test_ledger.entries
    assert entries[-1].balance == Amount(10)

# Generated at 2022-06-14 04:24:22.840952
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .accounts import Account
    from .generic import Balance

    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {Account("0000"): Balance(period.since, Decimal(0))}

    ## Define a ReadInitialBalances instance:
    read_initial_balances = _read_initial_balances
    ## Use it to read initial balances:
    initial_balances = read_initial_balances(DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31)))
    ## Check the returned initial balances:
    assert initial_balances == {Account("0000"): Balance(datetime.date(2018, 1, 1), Decimal(0))}



# Generated at 2022-06-14 04:24:24.222217
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:24:35.033207
# Unit test for method add of class Ledger
def test_Ledger_add():
    posting = Posting(
        journal=JournalEntry(date=datetime.date(2020, 1, 1), description="Test", postings=[
            Posting(date=datetime.date(2020, 1, 1), account=Account("101"), direction=Debit, amount=Decimal(500)),
            Posting(date=datetime.date(2020, 1, 1), account=Account("201"), direction=Credit, amount=Decimal(500))
        ]),
        account=Account("101"),
        direction=Debit,
        amount=Decimal(500)
    )
    result = test_Ledger.add(posting)
    assert result.balance == Decimal(500)

# Generated at 2022-06-14 04:24:46.420787
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program()
    """
    import sys
    import typing
    from contextlib import contextmanager
    from .accounts import Account

    class ReadInitialBalances(Protocol):
        def __call__(self, period: DateRange) -> InitialBalances:
            pass

    class ReadJournalEntries(Protocol):
        def __call__(self, period: DateRange) -> typing.Iterable[JournalEntry]:
            pass

    @contextmanager
    def tester(program: ReadJournalEntries):
        old_stdout = sys.stdout
        result: Optional[str] = None

# Generated at 2022-06-14 04:24:51.365592
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal

    j = Journal(id="J1", date=datetime.date(2018,1,1), description="Desc", postings=None)
    l = Ledger('1233', Balance(datetime.date(2018,1,31), Quantity(Decimal(0))))
    p = Posting(j, '1233', datetime.date(2018,1,31), Quantity(Decimal(10)), True)
    entry = l.add(p)
    assert entry == LedgerEntry(l, p, Quantity(Decimal(10)))


# Generated at 2022-06-14 04:25:00.972217
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import random
    from .journaling import JournalEntry, Posting, Journal, Direction

    from .ledgers import build_general_ledger, compile_general_ledger_program
    from .accounts import Account
    from .commons.numbers import Amount, Quantity
    from .commons.zeitgeist import DateRange
    from .commons.czl import parse_date, parse_amount
    from . import ledgers, catalogs, entries, accounts, journals

    # Prepare data:
    acc = {i: a for i, a in enumerate(sorted(accounts.accounts(catalogs.test_catalog_2, {}), key=lambda a: a.name))}

# Generated at 2022-06-14 04:25:14.833404
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import pytest
    from ..adapters.in_memory import in_memory_initial_balances, in_memory_journal_entries
    from ..domain.services import account as account_service
    from ..domain.services import general_ledger as general_ledger_service
    from .journaling import build_journal, compile_journal_program
    from .accounts import build_account, compile_account_program

    #: Data to be used in test cases.
    @dataclass
    class Args:
        #: Initial balances.
        initial: str

        #: Journal entries.
        journal: str

    ## Parameters.

# Generated at 2022-06-14 04:25:18.929546
# Unit test for method add of class Ledger
def test_Ledger_add():
    journal = JournalEntry(datetime.date(2020,6,22), "test entry")
    journal.add(Posting(Account(1), Amount(1)))
    journal.add(Posting(Account(2), Amount(-1)))
    ledger = Ledger(Account(1), Balance(datetime.date(2020,6,22), Amount(0)))
    ledger.add(journal.postings[0])
    assert ledger.entries[0].balance.value == Decimal(1)

# Generated at 2022-06-14 04:25:27.060236
# Unit test for method add of class Ledger
def test_Ledger_add():
    ledger = Ledger(Account("0000", ""), Balance(datetime.date(2020, 6, 1), Quantity(Decimal(0))))
    entry = ledger.add(
        Posting(
            Account("0000", ""),
            Quantity(Decimal(500)),
            datetime.date(2020, 6, 3),
            1,
            JournalEntry("test", datetime.date(2020, 6, 3)),
        )
    )
    assert ledger.account == Account("0000", "")
    assert ledger.initial._value == Decimal(0)
    assert ledger.entries[0].ledger == ledger

# Generated at 2022-06-14 04:25:28.235579
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:25:29.671770
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:25:41.830658
# Unit test for function build_general_ledger
def test_build_general_ledger():
    # Setup
    from .journaling import compile_journal_entry_program
    from .accounts import compile_account_program

    journal_program = compile_journal_entry_program(compile_account_program(), datetime.date.today())
    # Exercise
    entries = []
    entries.append(journal_program("Debit", "Credit", 100))
    entries.append(journal_program("Credit", "Debit", 100))
    entries.append(journal_program("Debit", "Credit", 100))
    entries.append(journal_program("Credit", "Debit", 100))
    initial_balances = {entries[0].postings[1].account: Balance(datetime.date.today(), 200)}

# Generated at 2022-06-14 04:25:55.711903
# Unit test for function build_general_ledger
def test_build_general_ledger():
    # Define the accounts:
    Assets = Account("Assets")
    Capital = Account("Capital")
    Expenses = Account("Expenses")
    Income = Account("Income")
    Liabilities = Account("Liabilities")

    # Define the initial balances:
    initial_balances = {Capital: Balance(datetime.date(2018, 1, 1), Quantity(Decimal(40000)))}

    # Define the journal:

# Generated at 2022-06-14 04:26:06.558141
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import JournalEntry
    from .accounts import Account
    from .generic import Balance
    from ..commons import zeitgeist
    from unittest.mock import Mock, call

    # Given
    # an account
    cntracct = Account(code="0000", title="Cash")
    # an account
    assetacct = Account(code="1000", title="Assets")
    # a date
    date = zeitgeist.now()
    # a journal
    journal = JournalEntry(date, "Journal1")
    journal.append_posting(cntracct, Amount(Decimal(1000)), True)
    journal.append_posting(assetacct, Amount(Decimal(1000)), False)
    # and a list of such journals
    journal_entries = [journal]
    # an initial balance


# Generated at 2022-06-14 04:26:13.139286
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..accounting import accounts
    from ..accounting.journaling import Journal, Posting, Transaction
    from datetime import date, datetime

# Generated at 2022-06-14 04:26:22.912937
# Unit test for function build_general_ledger
def test_build_general_ledger():

    from datetime import date

    from ..commons.numbers import Amount
    from .accounts import Account

    from .generic import Balance

    from .journaling import JournalEntry, Posting

    def _entry(date: date, description: str = None) -> JournalEntry:

        return JournalEntry(date, description, [Posting(date, "TEST", Account("EXPENSES"), Quantity(120), Amount(100))])

    def _entry2(date: date, description: str = None) -> JournalEntry:
 
        return JournalEntry(date, description, [Posting(date, "TEST", Account("EQUITY"), Quantity(120), Amount(100))])


# Generated at 2022-06-14 04:26:37.818283
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Unit tests for the method add of the class Ledger.
    """
    # Define the date for the Date for the LedgerEntry
    date_ledger = datetime.datetime(2020, 1, 1)
    # Define the date for the Date for the JournalEntry
    date_journal = datetime.datetime(2020, 1, 1)
    # Define the test variables for the Ledger class
    account = Account("1234", "Testaccount", True, True)
    initial = Balance(date_ledger, Quantity(1.0))
    # Define the test variables for the Journal class
    description = "TestJournal"
    # Define the test variables for the Posting class
    accountp = Account("1234", "Testaccount", True, True)
    amount = Amount(1.0)
    direction = 1


# Generated at 2022-06-14 04:26:39.172922
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    print(__name__)
    print("    test_compile_general_ledger_program")

# Generated at 2022-06-14 04:26:45.489578
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Account = account_num = 0
    Entry = Transaction number = 0
    Date = 0
    amount = 0
    debit = 0
    credit = 0
    description = 0
    """
    """
    If a debit is greater than zero
        Assert debit increases by amount * direction
    If a credit is greater than zero
        Assert credit increases by amount * direction
    If a debit is less than or equal to zero
        Assert credit is an empty string
    """
    ledger = Ledger(
        account=Account(
            number=0,
            name="Account",
        ),
        initial=Balance(
            date=0,
            value=0
        ),
    )

# Generated at 2022-06-14 04:26:52.349034
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from decimal import Decimal
    from datetime import date
    from ..accounts.billing import BillingAccount
    from ..commons.configuration import LocalConfiguration
    from .generic import InitialBalance
    from .journaling import Journal
    
    # Build database configuration.
    config = LocalConfiguration({
        "database": {
            "engine": "sqlite",
            "host": ":memory:",
        },
    })

    # Build database and journal.
    database = config.database
    database.apply_migrations()
    database.populate_accounts_dict()
    journal = Journal(config)

    # Test data.
    program = compile_general_ledger_program(
        database.journal.read_initial_balances,
        database.journal.read_journal_entries,
    )

# Generated at 2022-06-14 04:27:04.945730
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..inmemory import InMemoryJournalEntries, InMemoryInitialBalances
    from ..ledgers.journaling import Posting

    ## Example journal postings:
    db = InMemoryJournalEntries()
    db.post(
        2,
        Posting(2, "Assets:Bank:Checking", 1000, "Dr", "Payment of Rent"),
        Posting(2, "Expenses:Rent", 1000, "Cr", "Payment of Rent"),
    )
    db.post(
        1,
        Posting(1, "Assets:Bank:Cash", 1000, "Dr", "Sales Proceeds"),
        Posting(1, "Income", 1000, "Cr", "Sales Proceeds"),
    )

    ## Example initial balances:
    ib = InMemoryInitialBalances()

# Generated at 2022-06-14 04:27:15.847996
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .accounts import Account
    from .generic import Balance

    @dataclass
    class Algebra(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("1010", "Cash", side="L"): Balance(period.since, Quantity(Decimal(100_00)))}

    assert compile_general_ledger_program(Algebra(), ReadJournalEntries(lambda: []))(DateRange("2019-01-01", "2019-12-31")).ledgers[Account("1010", "Cash", side="L")].initial.value == Decimal(100_00)

# Generated at 2022-06-14 04:27:25.086963
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from decimal import Decimal
    from datetime import date
    from typing import Dict
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountType
    from .journaling import Amount, Posting, JournalEntry
    from .generic import Balance
    from .initial_balances import ReadInitialBalancesForNewPeriod
    from .journal_entries import ReadJournalEntries
    from .read_tables import read_accounts, read_entries

    ## Initialize entries.
    entries = read_entries("./data/xbook.txt")

    ## Initialize accounts.
    accounts = read_accounts("./data/xbook.txt")

    ## Initialize read initial balances.
    read_initial_balances = ReadInitialBalancesForNewPeriod(entries, accounts)

    ## Initial

# Generated at 2022-06-14 04:27:37.670079
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():

    from .accounts import Account, AccountGroup
    from .commons.numbers import Amount, Quantity
    from .journaling import JournalEntry, Posting
    from ..commons.zeitgeist import Date, DateRange
    from .accounts import Accounts

    ## Define the accounts:
    salary, revenue, fuel, maintenance, bank, cash = (
        Account(1, "Salary", AccountGroup.EXPENSE),
        Account(2, "Revenue", AccountGroup.INCOME),
        Account(3, "Fuel", AccountGroup.EXPENSE),
        Account(4, "Maintenance", AccountGroup.EXPENSE),
        Account(5, "Bank", AccountGroup.ASSET),
        Account(6, "Cash", AccountGroup.ASSET),
    )

    ## Define journal entries:

# Generated at 2022-06-14 04:27:51.633659
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest import mock
    from pytest import raises
    from .accounts import Account
    from .generic import Balance
    from .commons.zeitgeist import DateRange
    from .commons.types import ValidMoney
    _ReadInitialBalances = ReadInitialBalances()
    with raises(NotImplementedError):
        _ReadInitialBalances(None)
    _ReadInitialBalancesMock = mock.MagicMock(spec=_ReadInitialBalances)
    _period = DateRange("2000-01-01", "2000-12-31")
    _initial_balances = {Account("1000"): Balance("2000-01-01", ValidMoney(0))}
    _ReadInitialBalancesMock.__call__.return_value = _initial_balances
    assert _ReadInitialBalancesMock(_period) == _initial

# Generated at 2022-06-14 04:28:03.165262
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import Account
    from .parsing import parse_journal_entry
    from .program import ReadJournalEntries
    from .journaling import JournalEntry
    from ..commons.zeitgeist import DateRange

    import datetime

    @dataclass
    class JournalEntryStore:
        entries: List[JournalEntry]

    @dataclass
    class InitialBalanceStore:
        balances: Dict[Account,Balance]

    ## A journal entry store
    je_store = JournalEntryStore(list())
    def _read_journal_entries(period : DateRange) -> Iterable[JournalEntry]:
        return (x for x in je_store.entries if x.date >= period.since and x.date <= period.until)
    read_journal_entries = ReadJournalEntries(_read_journal_entries)

   

# Generated at 2022-06-14 04:28:24.611676
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import datetime
    from types import FunctionType
    from typing import List, TypeVar

    from ..commons.zeitgeist import DateRange
    from .accounts import AccountType
    from .commons import BaseTest
    from .journaling import JournalEntry, Posting

    #: Type variable for general ledger program.
    _T = TypeVar("_T")

    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {Account("A", AccountType.ASSET): Balance(period.since, Quantity(Decimal(100)))}


# Generated at 2022-06-14 04:28:32.083095
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from decimal import Decimal
    from .accounts import Account
    from .commons.zeitgeist import dtnow
    from .journaling import JournalEntry, Posting

    assert None is not build_general_ledger(
        DateRange(datetime.datetime(2019, 1, 1), datetime.datetime(2019, 1, 2)),
        [],
        {Account(111000): Balance(dtnow(), Quantity(Decimal(1000)))},
    )



# Generated at 2022-06-14 04:28:33.132610
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:28:44.967825
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Import classes.
    from .accounts import Account
    from .journaling import Journal, Posting
    from datetime import date
    from decimal import Decimal

    ## Define test account.
    account = Account("Assets:Bank:Checking")
    ## Define test date.
    date = date(2020, 1, 1)
    ## Define test initial balance.
    initial = Balance(date(2020, 1, 1), Quantity(Decimal(50)))
    ## Define test ledger.
    ledger = Ledger(account, initial)
    ## Define test journal.
    journal = Journal(date, "Test")
    ## Define the postings.
    debit = Posting(journal, account, Quantity(10), -1)
    credit = Posting(journal, account, Quantity(5), 1)

    ## Add the postings as new

# Generated at 2022-06-14 04:28:57.995810
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import dataclasses
    from typing import Dict, Any
    from .accounts import Account
    from .generic import Balance
    from .journal import Journal
    from .journaling import Posting
    from .ledgers import InitialBalances, ReadJournalEntries
    from .tax import Tax
    

# Generated at 2022-06-14 04:29:06.234929
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.zeitgeist import Date
    from .accounts import Account, AccountType
    from .generic import Balance
    from .journaling import AccountingPeriod, JournalEntry, Posting, TransactionReference
    from .money import Currency
    from .operations import Operation
    from .taxes import VATRate
    from .tokens import AccountToken, ParticularsToken, QuantityToken, VATRateToken, AmountToken, ActionToken, \
        DateToken, DescriptionToken, VATToken, TransactionReferenceToken

    ## Create the token list:

# Generated at 2022-06-14 04:29:16.142211
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Arrange
    from datetime import date, timedelta
    from .utils import create_balance, create_journal_entry, create_posting

    from .programs.algos.initial_balances import read_initial_balances
    from .programs.algos.journal_entries import read_journal_entries

    today = date.today()
    period = DateRange(today - timedelta(days=365), today)

    def mock_read_initial_balances(p: DateRange) -> InitialBalances:
        return {
            Account("1010"): create_balance(period.since, value=Quantity(Decimal(100))),
            Account("1011"): create_balance(period.since, value=Quantity(Decimal(100))),
        }


# Generated at 2022-06-14 04:29:25.660949
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .commons import ReadInitialBalances
    from .commons import DateRange
    from .commons import ReadJournalEntries
    from .journaling import JournalEntry
    from .accounts import Account

    @dataclass
    class MyReadInitialBalances(ReadInitialBalances):
        # Consumes a date range and returns a dictionary where keys
        # are terminal accounts, and values are their balances on the
        # last day of the period.

        def __call__(self, period: DateRange) -> Dict[Account, Decimal]:
            return {Account("R100"): Decimal(100)}


# Generated at 2022-06-14 04:29:37.517590
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    This is a unit test for method __call__ of class GeneralLedgerProgram.
    """

    # Algebra implementations:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        """
        Algebra implementation which reads initial balances.

        :param period: Accounting period.
        :return: Initial balances.
        """
        return {
            Account(acct_no=1, name="Sales"): Balance(
                period.until, Quantity(Decimal(0)), Quantity(Decimal(0)), Quantity(Decimal(0))
            ),
            Account(acct_no=2, name="Inventory"): Balance(
                period.until, Quantity(Decimal(0)), Quantity(Decimal(0)), Quantity(Decimal(-60000))
            ),
        }


# Generated at 2022-06-14 04:29:46.397888
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():

    from unittest.mock import call, Mock

    # Create mocked algebra implementations:
    read_initial_balances = Mock(spec=ReadInitialBalances, autospec=None, side_effect=[{}])
    read_journal_entries = Mock(spec=ReadJournalEntries, autospec=None, side_effect=[[]])

    # Compile the function:
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    # Call program:
    period = DateRange(datetime.date(2013, 1, 1), datetime.date(2013, 12, 31))
    ledger = program(period)

    # Check algebra implementations were called correctly:
    assert read_initial_balances.mock_calls == [call(period)]

# Generated at 2022-06-14 04:30:20.357135
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account('Assets', 'current assets', 'cash')
    description = 'test description'
    date = datetime.date(2020, 2, 1)
    journal = JournalEntry(description, date, None)
    amount = 100
    direction = Posting.Direction.DEBIT
    posting = Posting(account, amount, direction, journal)
    
    balance = Balance(datetime.date(2020, 1, 1), 0)
    ledger = Ledger(account, balance)
    ledger.add(posting)

    assert ledger.entries[0].balance == 100


# Generated at 2022-06-14 04:30:28.057228
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass(frozen=True)
    class Actual(Generic[_T]):
        period: DateRange
        balances: Dict[Account, Balance]

    @dataclass(frozen=True)
    class Expected(Generic[_T]):
        period: DateRange

    def assert_actual_equals_expected(actual: Actual[_T], expected: Expected[_T]):
        assert actual.period == expected.period

    def read_initial_balances(period: DateRange) -> Dict[Account, Balance]:
        return {a: Balance(period.until, Quantity(0)) for a in [Account("CASH"), Account("INCOME")]}


# Generated at 2022-06-14 04:30:30.093573
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:30:41.227943
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    This function test the functionality of function build_general_ledger
    """
    from .journaling import create_journal_entry, create_posting
    from .accounts import create_account
    from .commons.zeitgeist import DateRange

    from . import easyledger as el

    # def build_general_ledger(
    #     period: DateRange, journal: Iterable[JournalEntry[_T]], initial: InitialBalances
    # ) -> GeneralLedger[_T]:
    # args:
    period=DateRange(datetime.date.today(), datetime.date.today())

# Generated at 2022-06-14 04:30:46.770578
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Create a ledger for A:
    d = Ledger(
        account = Account.of_string("A"),
        initial = Balance(datetime.date(2000, 1, 1), Quantity(Decimal(0)))
    )

    ## Create a bicentenary journal entry:
    bicentenary = JournalEntry(
        date = datetime.date(2000, 1, 1),
        description = "Bicentenary",
        postings = [
            Posting(account = Account.of_string("A"), direction = -1, amount = Amount(Decimal(100))),
            Posting(account = Account.of_string("B"), direction = +1, amount = Amount(Decimal(100))),
        ]
    )

    ## Post it:
    d.add(bicentenary.postings[0])

    ## Create a Christmas journal entry:

# Generated at 2022-06-14 04:30:56.977810
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from .accounts import Account
    from .generic import Balance
    from .journaling import BalanceInquiry, InitialBalance

    # Define a dictionary used to hold the return values
    rv = dict(initial_balances={}, journal_entries=[])

    # Define return values for method `__call__` of class `ReadInitialBalances`
    def _(period: "DateRange") -> "InitialBalances":
        return rv["initial_balances"]

    # Define the instance of `ReadInitialBalances` used in the test
    read_initial_balances = _

    # Define return values for method `__call__` of class `ReadJournalEntries`
    def _(period: "DateRange") -> "Iterable[JournalEntry]":
        yield from rv["journal_entries"]

# Generated at 2022-06-14 04:31:08.235289
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests the method :py:meth:`GeneralLedgerProgram.__call__` of class :py:class:`GeneralLedgerProgram`.
    """
    # Import test data
    import pickle

    # Import test case data
    from .test_general_ledger_program_data import (
        ACCOUNTS,
        BALANCES_PREVIOUS,
        BALANCES_START,
        JOURNAL_ENTRIES,
        LEDGERS,
        PERIOD,
    )

    # Create the initial balances
    initial_balances = {a: Balance(PERIOD.since, b - BALANCES_PREVIOUS[a]) for a, b in BALANCES_START.items()}

    # Create the initial balances reader

# Generated at 2022-06-14 04:31:17.038430
# Unit test for method add of class Ledger
def test_Ledger_add():
    a1 = Account("1012", "1012")
    a2 = Account("101", "101")
    je = JournalEntry(1, datetime.date(2019, 1, 2), "test")
    p1 = Posting(a1, datetime.date(2019, 1, 2), je, Decimal(500.00), 1)
    p2 = Posting(a2, datetime.date(2019, 1, 2), je, Decimal(500.00), -1)
    je.add(p1)
    je.add(p2)

    b = Balance(datetime.date(2019, 1, 1), 0)
    l = Ledger(a2, b)
    l.add(p1)
    assert l.entries[0].balance == Decimal(500.00)
    assert l.entries

# Generated at 2022-06-14 04:31:25.475418
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..articles.assets import Asset, AssetType
    from ..articles.entities import Entity
    from ..articles.liabilities import Liability, LiabilityType
    from ..articles.revenues_and_expenses import Revenue, RevenueType
    from ..journaling.generic import JournalEntry
    from ..journaling.machinery import Posting
    from ..journaling.directions import Debit, Credit

    period_start = datetime.date(2018, 1, 1)
    period_end = datetime.date(2018, 12, 31)
    before_period_date = datetime.date(2017, 12, 31)

    ## Build initial balances:

# Generated at 2022-06-14 04:31:31.259142
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account(code = "accountCode", name = "accountName", parent = None)
    initial = Balance(datetime.date(2019, 11, 7), Decimal(10))
    ledger = Ledger(account, initial)
    posting = Posting(Decimal(10), datetime.date(2019, 11, 8), None, None, None)
    ledger.add(posting)
    assert ledger.entries[0].balance == 20
    assert ledger.entries[0].posting.amount == 10


# Generated at 2022-06-14 04:32:02.004922
# Unit test for method add of class Ledger
def test_Ledger_add():
    # initialize test var
    # TODO: initialize
    posting = Posting(JournalEntry(postings=[Posting(account=Account(code_num=1, code_alpha='A'), amount = 1)]))
    # initialize test item
    ledger = Ledger(account=Account(code_num=1, code_alpha='A'),initial=Balance(since=datetime,value=1))
    # Assertion

    expected = ledger.add(posting)
    assert expected.posting == posting
    assert expected.balance == 1


# Generated at 2022-06-14 04:32:12.556084
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from decimal import Decimal
    from datetime import date
    from ..commons.zeitgeist import DateRange
    from .accounts import Asset, Liability, Revenue, Expense, Equity
    from .journaling import JournalEntry, Posting, Direction

    ## Create dummy entries:

# Generated at 2022-06-14 04:32:25.667204
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import Account, AccountClass
    from .journaling import Journal, Posting
    from ..commons.zeitgeist import DateRange

    from .generic import Balance


# Generated at 2022-06-14 04:32:31.334501
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test function build_general_ledger
    """
    ## Set period:
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))

    ## Define initial balances:
    initial_balances = {
        "Cash": Balance(period.since, Quantity(10000)),
        "Sales": Balance(period.since, Quantity(Decimal(0))),
        "Cost of Goods Sold": Balance(period.since, Quantity(Decimal(0))),
    }

    ## Create a journal entry:

# Generated at 2022-06-14 04:32:33.262281
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass



# Generated at 2022-06-14 04:32:40.549639
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    r = (DateRange(datetime.date(2016, 1, 1), datetime.date(2016, 12, 31)),
         InitialBalances(
            {
                Account(id="A", name="Accumulated depreciation of plant, net"),
                Balance(datetime.date(2015, 12, 31), Quantity(0)),
            },
         ),
    )
    assert r.__call__("a", "b"), "__call__ should return the two items in r"

# Generated at 2022-06-14 04:32:42.569725
# Unit test for function build_general_ledger
def test_build_general_ledger():
    ## TODO: Implement this unit test
    assert 0 == 0

# Generated at 2022-06-14 04:32:43.074209
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__(): ...

# Generated at 2022-06-14 04:32:50.325770
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """ Unit test for function compile_general_ledger_program """
    from ..algebra.accounting.journaling import build_posting
    from ..commons.zeitgeist import Date
    from .accounts import AccountCode, AccountType
    from .generic import BalanceType

    # Set up the reference data
    a1 = Account(AccountType.ASSET, AccountCode(code="1010", name="Cash"))
    a2 = Account(AccountType.ASSET, AccountCode(code="1020", name="Bank"))
    a3 = Account(AccountType.ASSET, AccountCode(code="1030", name="Inventory"))
    a4 = Account(AccountType.ASSET, AccountCode(code="1040", name="Other asset"))

# Generated at 2022-06-14 04:33:02.150393
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    def read_initial_balances(period):
        return {Account(10): Balance(period.since, Quantity(Decimal(0)))}

    def read_journal_entries(period):
        return [
            JournalEntry(
                1, period.since, "First", [Posting(Account(10), period.since, Quantity(Decimal(13)))]
            )
        ]

    run_general_ledger_program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    assert run_general_ledger_program(DateRange(since=datetime.date(2020, 4, 1), until=datetime.date(2020, 4, 30))).ledgers[Account(10)].entries[0].balance == Quantity(Decimal(13))