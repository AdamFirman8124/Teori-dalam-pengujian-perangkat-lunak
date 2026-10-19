

# Generated at 2022-06-14 04:23:52.865147
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal
    from .journaling.algebra import build_basic_journaling_algebra

    # Unit test for method add of class Ledger

    # Set up key accounts:
    test_accounts = [Account("0000"), Account("0001"), Account("0002")]
    # Set up journal:
    test_journal = Journal(datetime.date(2020, 6, 1), "TEST-1", {"0000": Quantity(Decimal(100))}, test_accounts)
    # Set up ledger:
    test_ledger = Ledger(test_accounts[0], Balance(datetime.date(2020, 5, 31), Quantity(Decimal(42))))
    # First time running method add:

# Generated at 2022-06-14 04:23:58.914636
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..books.algebra import ReadInitialBalances as _ReadInitialBalances
    from ..books.algebra import ReadJournalEntries as _ReadJournalEntries

    # Types
    class _ReadInitialBalancesImpl(_ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    class _ReadJournalEntriesImpl(_ReadJournalEntries):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return []

    # Tests
    fn = compile_general_ledger_program(
        _ReadInitialBalancesImpl(), _ReadJournalEntriesImpl()
    )
    assert fn

    gl = fn(DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31)))
    assert gl
   

# Generated at 2022-06-14 04:24:12.036596
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Tests :func:`build_general_ledger`.
    """
    ## Define the test journal:
    journal = [
        JournalEntry("1", datetime.date(2017, 3, 5), "A", [Posting("A", Decimal("100.00"), False)])
    ]

    ## Define initial balances:
    initial_balances = {Account("A"): Balance(datetime.date(2017, 3, 5), Quantity(Decimal("50.00")))}

    ## Define the general ledger:
    gl = build_general_ledger(DateRange(datetime.date(2017, 3, 1), datetime.date(2017, 3, 5)), journal, initial_balances)

    ## Check account A:
    a = gl.ledgers[Account("A")]


# Generated at 2022-06-14 04:24:21.628186
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ... import axel_base as base
    from ...axel.accounts.axel_base import M
    from ...axel.journaling.axel_base import Posting

    class TestReadInitialBalances:
        def __call__(self, period: DateRange):
            return {
                Account.from_str("A101"): Balance(period.since, Quantity(Decimal(10000))),
                Account.from_str("A201"): Balance(period.since, Quantity(Decimal(1000))),
                Account.from_str("A302"): Balance(period.since, Quantity(Decimal(1000))),
            }

    J = base.journal

# Generated at 2022-06-14 04:24:23.020737
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert 0



# Generated at 2022-06-14 04:24:30.541839
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    class ReadInitialBalancesMock:
        period: DateRange = None

        def __call__(self, period: DateRange) -> InitialBalances:
            self.period = period
            return {}

    mock = ReadInitialBalancesMock()
    period = DateRange.parse("2000-01-01", "2000-12-31")
    assert mock.period is None
    mock(period)
    assert mock.period == period



# Generated at 2022-06-14 04:24:38.730652
# Unit test for method add of class Ledger
def test_Ledger_add():
    #Test the first entry is the initial balance
    account = Account('01', 'inventory', 'inventory')
    initialBalance = Balance(datetime.date(2018, 1, 1), Quantity(Decimal(0)))
    inventory = Ledger(account, initialBalance)
    journalEntry = JournalEntry(datetime.date(2018, 1, 1), 'Initial balance',
                                [Posting(account, Quantity(Decimal(1000)), 'debit'),
                                Posting(Account('15', 'bank', 'bank'), Quantity(Decimal(1000)), 'credit')])

    inventory.add(journalEntry.postings[0])
    assert inventory.entries[0].balance == Quantity(Decimal(1000))
    assert inventory.entries[0].description == 'Initial balance'


# Generated at 2022-06-14 04:24:51.420526
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import ledger
    read_journal_entries = ledger.compile_read_journal_entries(
        ledger.journal.read_journal_entries("./data/journal.csv")
    )

    get_initial_balances = ledger.compile_get_initial_balances(
        ledger.balances.get_initial_balances(ledger.balances.read_initial_balances("./data/balances.csv"))
    )

    general_ledger_program = ledger.compile_general_ledger_program(get_initial_balances, read_journal_entries)


# Generated at 2022-06-14 04:25:01.047199
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from dataclasses import dataclass
    from typing import NamedTuple
    import unittest
    import datetime
    # Data:
    # Tuple containing the accounting period, the account numbers, the journal entries and the initial balances
    TestData = NamedTuple("TestData", [("period", DateRange), ("accounts", [int]), ("journal_entries", [JournalEntry]), ("initial_balances", InitialBalances)])

# Generated at 2022-06-14 04:25:06.222007
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    class TestReadInitialBalances(ReadInitialBalances):
        def __call__(self, period):
            pass

    readInitialBalances = TestReadInitialBalances()
    readInitialBalances.__call__(datetime.datetime.now)


# Generated at 2022-06-14 04:25:22.451763
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import JournalEntryFactory, PostingFactory
    from ..commons.zeitgeist import datetime_from_date

    from .accounts import Assets, Equity, Liabilities, Revenue
    from .balances import BalanceFactory
    from .journaling import JournalEntry
    from .journaling import PostingFactory


# Generated at 2022-06-14 04:25:31.692325
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    def _read_initial_balances(_: DateRange) -> InitialBalances:
        return {
            Account.asset("cash"): Balance(datetime.date(2018, 1, 1), Quantity(Decimal(7185.00))),
            Account.liability("vat payable"): Balance(datetime.date(2018, 1, 1), Quantity(Decimal(40.00))),
            Account.equity("capital"): Balance(datetime.date(2018, 1, 1), Quantity(Decimal(100000.00))),
            Account.expense("wages"): Balance(datetime.date(2018, 1, 1), Quantity(Decimal(0.00))),
        }


# Generated at 2022-06-14 04:25:42.701494
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import Account, AccountType

    # Define accounts and their opening balances:
    account_a = Account("A", AccountType.ASSET)
    account_b = Account("B", AccountType.ASSET)
    account_c = Account("C", AccountType.LIABILITY)
    account_d = Account("D", AccountType.LIABILITY)
    account_e = Account("E", AccountType.EXPENSE)
    account_f = Account("F", AccountType.EXPENSE)
    account_g = Account("G", AccountType.INCOME)
    account_h = Account("H", AccountType.INCOME)
    account_i = Account("I", AccountType.CAPITAL)
    account_j = Account("J", AccountType.CAPITAL)

# Generated at 2022-06-14 04:25:56.504284
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .conf import is_test_run
    from .data import AccountData, BalanceData, ReadInitialBalances as ReadInitialBalances_

    def _program_to_test(period: DateRange) -> InitialBalances:
        """
        Consumes the opening and closing dates and produces a general ledger.

        :param period: Accounting period.
        :return: A general ledger.
        """
        ## Get initial balances as of the end of previous financial period:
        initial_balances = ReadInitialBalances_(AccountData(), BalanceData()).__call__(period)

        ## Return initial balances.
        return initial_balances

    if is_test_run():
        from .commons.test_utils import assert_test_case

        # Test for the period including dates on which there are balances for the terminal accounts.

# Generated at 2022-06-14 04:25:57.601786
# Unit test for method add of class Ledger
def test_Ledger_add():
    pass
    # TODO

# Generated at 2022-06-14 04:26:07.690237
# Unit test for function build_general_ledger
def test_build_general_ledger():

    from ..journal.interfaces import JournalFactory
    ledger_journal_factory = JournalFactory()
    ledger_journal_factory.parse_journal_entry('2019-01-15 * "Pay cheque" \n\
                                               Expenses:Food           $10.00 USD\n\
                                               Assets:Savings:Cash                 ')

    from ..accounts.interfaces import AccountFactory
    ledger_account_factory = AccountFactory()
    ledger_account_factory.parse_account('Expenses')
    ledger_account_factory.parse_account('Expenses:Food')
    ledger_account_factory.parse_account('Assets')
    ledger_account_factory.parse_account('Assets:Savings')
    ledger_account_factory.parse_account('Assets:Savings:Cash')


# Generated at 2022-06-14 04:26:19.397744
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, Posting, Transaction
    from .accounts import Account, RootAccount, AccountNode
    from .types import SimpleType, CalculationType
    from .types.simple import Asset, Expense
    from .types.calculation import Income

    account_root = RootAccount()
    account = Account.create(
        account_root, "main", description="Main account", type=SimpleType(Asset), currency="TRY"
    )
    journal = Journal("description", "journal_entry")
    posting = Posting(journal, account, 10)
    ledger = Ledger(account, Balance(datetime.date(2018, 1, 1), 5))
    ledger.add(posting)
    assert ledger.entries[0].balance == 15

    account_root = RootAccount()

# Generated at 2022-06-14 04:26:32.178228
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """Unit test for method __call__ of class ReadInitialBalances"""
    from .accounts import Accounts
    from .algebra import ReadInitialBalances as _ReadInitialBalances
    from .algebra import ReadJournalEntries as _ReadJournalEntries
    from .generic import Balance as _Balance
    from .journaling import JournalEntry as _JournalEntry
    from .journaling import Posting as _Posting
    from commons.daterange import DateRange as _DateRange
    from commons.numbers import Amount as _Amount
    from commons.numbers import Quantity as _Quantity
    from datetime import date as _date
    from datetime import timedelta as _timedelta
    # Compile the general ledger program

# Generated at 2022-06-14 04:26:45.337016
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Tests the ``compile_general_ledger_program`` function.
    """
    import unittest

    from ..commons.algebras import NewType
    from ..commons.timing import MockDate

    from .accounts import Account
    from .journaling import JournalEntry

    ## Define the mock clock:
    class MockClock(NewType):
        """
        Mock clock:
        """

    ## Define the mock journal:
    class MockJournal(NewType):
        """
        Mock journal:
        """

    ## Define the mock journal entry:
    class MockJournalEntry(NewType):
        """
        Mock journal entry:
        """

    ## Define the mock posting:
    class MockPosting(NewType):
        """
        Mock posting:
        """

    ## Define the mock ledger

# Generated at 2022-06-14 04:26:49.212660
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Setup
    import datetime
    from decimal import Decimal
    from enum import Enum
    from typing import Dict
    from ..commons.numbers import Amount, Quantity
    from .accounts import Account
    from .generic import Balance
    ...
    # Exercise
    ...
    # Verify
    raise NotImplementedError()


# Generated at 2022-06-14 04:27:05.129943
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:27:06.649137
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass



# Generated at 2022-06-14 04:27:18.895935
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test case: build_general_ledger
    """
    from datetime import date, timedelta
    from decimal import Decimal
    from itertools import combinations
    from hypatia import algebra

    ## Mocking initial balances algebra implementation:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {a: Balance(period.until, Decimal(0)) for a in algebra._accounts}

    ## Mocking journaling algebra implementation:

# Generated at 2022-06-14 04:27:23.748136
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert callable(ReadInitialBalances.__call__)
    assert len(ReadInitialBalances.__call__.__annotations__) == 2
    assert ReadInitialBalances.__call__.__annotations__["self"] == "ReadInitialBalances"
    assert ReadInitialBalances.__call__.__annotations__["return"] == InitialBalances


# Generated at 2022-06-14 04:27:36.971083
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest import TestCase
    from datetime import date
    from inspect import isabstract
    from pyspec.acc.accounts import Account
    from pyspec.accounting.commons.numbers import Amount, Quantity
    from pyspec.accounting.commons.zeitgeist import DateRange
    from pyspec.accounting.generic import Balance
    from pyspec.accounting.general.asset import AssetAccount

    actual = ReadInitialBalances.__abstractmethods__
    expected = {
        "__call__",
    }
    TestCase().assertSetEqual(actual, expected)

    acctbs = Amount("5", "USD")
    acctbl = Amount("10", "USD")
    acctpl = Amount("20", "USD")


# Generated at 2022-06-14 04:27:50.975901
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Compiles a program which builds general ledger.
    """
    ## This is the read_initial_balances function required by compile_general_ledger_program()
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {}

    ## This is the read_journal_entries function required by compile_general_ledger_program()
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return {}

    ## Invoke the compiler to build the program.
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Invoke the program, for example for period 2018.

# Generated at 2022-06-14 04:27:59.378071
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from unittest import TestCase, main

    from pyphi.commons.numbers import Quantity, Amount
    from pyphi.accounting.accounts import Account
    from pyphi.accounting.generic import Balance

    class _ReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account(1, "cash"): Balance(date(2020, 1, 1), Quantity(10)),
                Account(2, "revenue"): Balance(date(2020, 1, 1), Quantity(100)),
                Account(3, "cost of goods sold"): Balance(date(2020, 1, 1), Quantity(30)),
                Account(4, "capital"): Balance(date(2020, 1, 1), Quantity(100)),
            }

   

# Generated at 2022-06-14 04:28:10.615708
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Set up account
    account = Account(id=str(uuid.uuid4()), number='012', name='Starbucks')
    ## Set up period
    period = DateRange(since=datetime.date(2020,9,23),until=datetime.date(2020,12,31))
    ## Set up journal
    journal = Journal(
        date=datetime.date(2020,9,23), description= "Coffee", id=str(uuid.uuid4())
    )
    ## Set up posting
    posting = Posting(
        account=account,
        amount=Decimal("-2.99"),
        direction=Direction.DEBIT
    )

    initial = Balance(period.since, Quantity(Decimal("0")))
    ## Set up balance

# Generated at 2022-06-14 04:28:24.501756
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():

    ## Mock some data:
    period = DateRange.from_str("2020-01-01", "2020-12-31")


# Generated at 2022-06-14 04:28:35.165666
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import unittest
    #from typing import TYPE_CHECKING
    #if TYPE_CHECKING:
    #    from dateutil.rrule import rrule
    #else:
    from dateutil.rrule import rrule

    class ReadInitialBalancesStub(ReadInitialBalances):
        def __init__(self, initial_balances):
            self._initial_balances = initial_balances

        def __call__(self, period):
            return self._initial_balances

    class GeneralLedgerProgramStub(GeneralLedgerProgram):
        def __init__(self, ledgers):
            self._ledgers = ledgers

        def __call__(self, period):
            return self._ledgers


# Generated at 2022-06-14 04:29:27.540012
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Create a mock ReadInitialBalances
    mock_ReadInitialBalances = ReadInitialBalances()
    # Create a mock DateRange
    mock_DateRange = DateRange('2020-07-01', '2020-08-01')
    # Create a mock InitialBalances implementing the type Protocol for ReadInitialBalances
    mock_InitialBalances = InitialBalances()

    # Mock __call__ function
    # The mock function will return a mock InitialBalances
    mock_ReadInitialBalances.__call__ = lambda x : mock_InitialBalances

    # Initialize a mock account
    mock_Account = Account("A")
    # Initialize a mock balance
    mock_Balance = Balance("2020-05-01", 1000)

    # Add the mock account and balance to the mock InitialBalances
    mock_InitialBalances[mock_Account] = mock_

# Generated at 2022-06-14 04:29:34.511513
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    A test for function :py:func:`compile_general_ledger_program`.
    """
    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {}

    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return []

    assert compile_general_ledger_program(_read_initial_balances, _read_journal_entries) is not None

# Generated at 2022-06-14 04:29:44.621281
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test the build_general_ledger() function using journal entries from `./notes/journal_entries.md`
    """

    ## Module imports:
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountNature
    from .journaling import Posting
    from .journaling.journal_entries import journal_entries

    ## Helper method for creating postings for testing.
    def _posting(amount: str, account_code: str, debit: bool = True) -> Posting[int]:
        return Posting(
            journal,
            account=Account(account_code, "", AccountNature.ASSET, ""),
            direction=Posting.Direction.DEBIT if debit else Posting.Direction.CREDIT,
            amount=float(amount),
            description="",
        )



# Generated at 2022-06-14 04:29:58.436154
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from unittest import TestCase
    from unittest.mock import Mock

    from ..commons.accounting import ForeignCurrency
    from ..commons.zeitgeist import DatetimeRange
    from .accounts import Asset, Expense

    class TestCompileGeneralLedgerProgram(TestCase):
        def test_initial_balances_not_found(self) -> None:
            read_initial_balances = Mock()  # type: ReadInitialBalances
            read_initial_balances.return_value = {}
            read_journal_entries = Mock()  # type: ReadJournalEntries[ForeignCurrency]
            _program = compile_general_ledger_program(read_initial_balances, read_journal_entries)


# Generated at 2022-06-14 04:30:05.910288
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountType
    from .journaling import Journal
    from .types import Money
    from .values import FinancialPeriod

    from testing import sample

    financial_period = FinancialPeriod(
        date_range=DateRange(since=datetime.date(2017, 1, 1), until=datetime.date(2017, 3, 31)),
        fiscal_quarter=sample.fiscal_quarter,
        fiscal_year=sample.fiscal_year,
        fiscal_period=sample.fiscal_period,
    )

# Generated at 2022-06-14 04:30:12.571430
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import typing
    import unittest
    import unittest.mock

    from ..commons.algebra import Function
    from ..commons.zeitgeist import AccountingPeriod

    test_case = unittest.TestCase()

    class MockReadInitialBalances(ReadInitialBalances, Function[AccountingPeriod, InitialBalances]):
        def _apply(self, period: AccountingPeriod) -> InitialBalances:
            return {
                "Bank": Balance(period.since, Quantity(Decimal(100))),
                "Cash": Balance(period.since, Quantity(Decimal(200))),
            }


# Generated at 2022-06-14 04:30:22.782020
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .accounts import Account, Accounts
    from .journals import Journal
    from .journaling import Posting, PostingDirection

    # Setup
    stmt_date = datetime.date(2019, 1, 1)
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 31))
    start_balance = Decimal(10)

    sample_journal = Journal(stmt_date, 'Journal Entry', [
        Posting(PostingDirection.CR, Accounts.get('4011.00'), 10),
    ])

    sample_initials = {Accounts.get('4011.00'): Balance(stmt_date, start_balance)}


    # Execute
    gl = build_general_ledger(period, [sample_journal], sample_initials)

    #

# Generated at 2022-06-14 04:30:36.467315
# Unit test for function build_general_ledger
def test_build_general_ledger():
    print("Begin unit test for function 'build_general_ledger'")

    """
    Functional tests for the build_general_ledger function.
    """

    from datetime import date
    from decimal import Decimal
    from itertools import islice
    from ..commons.zeitgeist import parse_date

    from .accounting import Accounting
    from .accounts import register_account, register_terminal_account, register_category
    from .journaling import AccountingInterval, AccountingPeriod, JournalEntry, Posting, Journal, AccountingEvent

    ## 0 - Setup 3 accounts and 2 terminal accounts.
    @register_account("Assets")
    class Assets(Account):
        pass

    @register_account("Expenses")
    class Expenses(Account):
        pass


# Generated at 2022-06-14 04:30:49.183151
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.zeitgeist import datetime_of
    from .accounts import AccountType
    from .journaling import Journal, Posting

    ## Set up accounts:
    current_assets = Account("1010", AccountType.Asset, "Current Assets")
    cash = Account("1020", AccountType.Asset, "Cash")
    sales = Account("4000", AccountType.Revenue, "Sales")
    accruals = Account("5000", AccountType.Liability, "Accruals")

    ## Set up general ledger program:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {cash: Balance(datetime_of("2020-01-01"), Quantity(Decimal("0")))}


# Generated at 2022-06-14 04:30:57.474858
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    @dataclass
    class _MockInitialBalancesReader:
        def __call__(self, period: DateRange):
            return {}

    @dataclass
    class _MockJournalEntriesReader:
        def __call__(self, period: DateRange):
            return []

    general_ledger_program = compile_general_ledger_program(
        read_initial_balances=_MockInitialBalancesReader(),
        read_journal_entries=_MockJournalEntriesReader(),
    )
    date_range = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 31))
    general_ledger = general_ledger_program(date_range)
    return general_ledger

# Generated at 2022-06-14 04:31:32.878520
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import journal_entry, posting, DEBIT, CREDIT

    open_balances = {
        "CASH": Balance(None, Quantity(10000)),
        "EQUITY": Balance(None, Quantity(0)),
    }
    retrieved_balances = build_general_ledger(DateRange(None, None), [], open_balances).ledgers

    # assert open_balances == retrieved_balances
    for i in open_balances:
        assert open_balances[i] == retrieved_balances[i]


# Generated at 2022-06-14 04:31:33.306236
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:31:38.798211
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import build_journal_entry
    from .accounts import RawAccount, TerminalAccount

    ## Get test account numbers:
    ARCash = RawAccount.of("1110")
    ARDeduction = RawAccount.of("1115")
    ARDiscounts = RawAccount.of("1120")
    ARBilling = RawAccount.of("1130")

    ## Compile the program:

# Generated at 2022-06-14 04:31:47.654375
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import Posting, ReadJournalEntries, JournalEntry
    from . import accounts

    def read_initial_balances(period):
        return {accounts.Equity: Balance(period.since, Quantity(Decimal(0)))}


# Generated at 2022-06-14 04:31:48.888569
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert ReadInitialBalances.__call__.__doc__ == "Reads and returns initial balances."



# Generated at 2022-06-14 04:31:56.108697
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest.mock import Mock, patch

    @dataclass
    class FakeInitialBalances(_T):
        def __init__(self):
            self.return_value: _T = Mock(return_value={})
        def __call__(self, period: DateRange) -> InitialBalances:
            return self.return_value

    ## Prepare a mock for testing:
    initial_balances = FakeInitialBalances()

    with patch(target="python_accounting.books.ledgers.ReadInitialBalances", new=initial_balances):
        ## Present object:
        read_initial_balances = ReadInitialBalances()
        
        ## Call the method under test:
        result = read_initial_balances(None)

        ## Check the result:
        assert result is initial_balances.return_value

#

# Generated at 2022-06-14 04:32:05.080067
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests method __call__ of class GeneralLedgerProgram.
    """

    ## Import libraries.
    from datetime import date
    from decimal import Decimal
    from unittest import TestCase, mock

    ## Try to import the package.
    try:
        from accounting.algebras.general_ledger import GeneralLedgerProgram
        from accounting.commons.numbers import Quantity
        from accounting.models.accounts import Account
        from accounting.models.journaling import JournalEntry
    except ImportError:
        return

    ## Create a mock for the general ledger program.
    class MockGeneralLedgerProgram(GeneralLedgerProgram):
        """
        A mock for the general ledger program.
        """

        def __init__(self, general_ledger):
            """
            Initializes the instance.
            """
            self._

# Generated at 2022-06-14 04:32:06.278995
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:32:14.013875
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    This test case ensures function compile_general_ledger_program works as expected.
    """
    ## Import standard library modules:
    from unittest.mock import MagicMock

    ## Define mock algebra implementations:
    read_initial_balances = MagicMock()
    read_journal_entries = MagicMock()

    ## Compile the program using the mock algebra implementations:
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Call the program and inspect the mocked algebra implementations:
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
    program(period)

    ## Assert the mocks were called with the given period:
    read_initial_balances.assert_called_once_with

# Generated at 2022-06-14 04:32:27.173494
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, TerminalAccount
    from .journaling import Journal, Posting, create_journal_entry

    ## Define a terminal account:
    asset = TerminalAccount(
        number=Account.Number("1"), description="Cash and Cash Equivalents"
    )

    ## Define a journal:
    journal = Journal(date=datetime.date(2020, 1, 1), description="Bank Deposit")

    ## Define initial balances:
    initial_balances = InitialBalances({asset: Balance(datetime.date(2019, 12, 31), Quantity(0))})

    ## Define journal entry:

# Generated at 2022-06-14 04:33:40.187747
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Create account
    account = Account(code="100", name="BANK ACT#1")

    ## Initial balance
    initial = Balance(since=datetime.date(year=2019, month=1, day=1), value=Quantity(Decimal('100')))

    ## Account ledger
    ledger = Ledger(account=account, initial=initial)

    ## Journal entry for new transaction
    description = "CLAIMS - TRUSTS"
    date = datetime.date(year=2019, month=1, day=2)
    journal_entry = JournalEntry(date=date, description=description)
    amount = Amount(Decimal("10"))
    posting_debit = Posting(journal=journal_entry, account=account, direction=+1, amount=amount)