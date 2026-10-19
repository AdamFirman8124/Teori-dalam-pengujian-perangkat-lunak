

# Generated at 2022-06-14 04:23:52.579385
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram.
    """

    from . import accounts, journal

    #: Mock function for read initial balances, takes an account and a date range
    def read_initial_balances_mock(period: DateRange) -> InitialBalances:
        return {accounts.Cash: Balance(period.since, Quantity(Decimal(1000)))}

    #: Mock function for read journal entries, takes an account and a date range

# Generated at 2022-06-14 04:23:53.532133
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:23:59.815955
# Unit test for method add of class Ledger
def test_Ledger_add():


    from .accounts import AccountType
    account = Account(code = "1000", name = "Testaccount", acc_type = AccountType.ASSET)
    led = Ledger(account = account, initial = Balance(date = "2019-01-01", value = 0))
    led.add(Posting(date = "2019-01-01", acc = "1000", amount = 10))
    assert led.entries[0].balance == 10

# Generated at 2022-06-14 04:24:10.960637
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    This test function creates a new journal entry and posting, creates a new general ledger, and then appends the
    posting to the ledger. It then checks the general ledger's records if the newly added record exists.
    """

    from .journaling import JournalEntry, Posting, Direction

    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))
    initial = {Account("a", "b", "c"): Balance(period.since, Quantity(Decimal(0)))}

# Generated at 2022-06-14 04:24:16.293632
# Unit test for function build_general_ledger
def test_build_general_ledger():
    # Initialize a general journal
    journal = []

    # Account definition
    Account.register(1, 'Cash')
    Account.register(2, 'Accounts Receivable')
    Account.register(3, 'Supplies')
    Account.register(4, 'Accounts Payable')
    Account.register(5, 'Sales')
    Account.register(6, 'Sales Returns and Allowances')
    Account.register(7, 'Cost of Goods Sold')
    Account.register(8, 'Salaries Expense')
    Account.register(9, 'Selling Expenses')

    # Initial Balances of each account

# Generated at 2022-06-14 04:24:19.389776
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2022-06-14 04:24:20.628919
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:24:32.291913
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .repository import AccountRepository

    assert (
        ReadInitialBalances.__call__(
            AccountRepository(),
            DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31)),
        )
        == {
            Account("1001"): Balance(datetime.date(2020, 1, 1), Quantity(Decimal(15000.00))),
            Account("1021"): Balance(datetime.date(2020, 1, 1), Quantity(Decimal(1000.00))),
            Account("1025"): Balance(datetime.date(2020, 1, 1), Quantity(Decimal(1000.00))),
        }
    )

# Generated at 2022-06-14 04:24:39.537817
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program
    """

    @dataclass
    class ReadInitialBalancesMock:
        """
        Mocks the algebra implementation which reads initial balances.
        """

        def __call__(self, period: DateRange) -> InitialBalances:
            """
            Mocks the algebra implementation which reads initial balances.
            """
            return {}

    @dataclass
    class ReadJournalEntriesMock:
        """
        Mocks the algebra implementation which reads journal entries.
        """

        def __call__(self, period: DateRange) -> List[JournalEntry]:
            """
            Mocks the algebra implementation which reads journal entries.
            """
            return []

    ## Get initial balances as of the end of previous financial period:
    initial_balances = ReadInitialBalancesMock()

# Generated at 2022-06-14 04:24:45.396431
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Define a mock function for this protocol which returns a dictionary with a single entry
    def mock_function(period: DateRange) -> InitialBalances:
        return {}

    assert callable(mock_function)  # Mock function is callable
    assert isinstance(mock_function, ReadInitialBalances)


# Generated at 2022-06-14 04:24:54.967610
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account(1, "Test Account", "Test Account", False, False)
    ledger = Ledger(account, Balance(datetime.date.today(), Quantity(Decimal(0))))
    posting = Posting(
        datetime.date.today(),
        None,
        None,
        "",
        Amount(0.0),
        1,
        account,
    )
    ledger.add(posting)
    # Test date property
    assert ledger.entries[0].date == datetime.date.today()
    # Test description property
    assert ledger.entries[0].description == ""
    # Test amount property
    assert ledger.entries[0].amount == Amount(0.0)
    # Test cntraccts property
    assert ledger.entries[0].cntraccts == []
    # Test

# Generated at 2022-06-14 04:25:08.108176
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    ## Import needed stuff:
    import pytest
    from typing import Callable

    ## Import test data:
    from ..test_data.accounts import accs
    from ..test_data.journal import posts, jours
    from ..test_data.ledger import genls

    ## Define a mock implementation of the algebra
    def mock_implementation() -> Callable[..., InitialBalances]:
        # pylint: disable=missing-function-docstring,function-redefined
        def implementation(period: DateRange) -> InitialBalances:
            return {
                accs["5015"]: Balance(period.since, Decimal("10.50")),
                accs["1100"]: Balance(period.since, Decimal("1600.00")),
            }

        return implementation

    ## Define a mock implementation of the algebra

# Generated at 2022-06-14 04:25:21.698382
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    The method add of class Ledger should add a new entry at the end of the ledger,
    based on the input passed in parameter
    """
    # Initial balance to be used in the test
    initial_balance = Balance(datetime.date(2020,1,1), Quantity(Decimal(1000)))
    # Account to be used in the test
    account = Account("Test account")
    # JournalEntry to be used in the test
    journal = JournalEntry(datetime.date(2020,1,1), "Test description")
    # Ledger to be used in the test
    ledger = Ledger(account, initial_balance)
    # Posting to be used in the test
    posting = journal.add_credit(account, Quantity(Decimal(100)))
    # Call the method to test
    Ledger.add(ledger, posting)


# Generated at 2022-06-14 04:25:31.304076
# Unit test for function build_general_ledger
def test_build_general_ledger():
    # Imports:
    from ..doubles.journaling import BalanceD, JournalEntryD
    from .accounts import Asset, Debt, Equity

    ## Create test data:
    dummy_accounts = Asset, Debt, Equity
    dummy_debtor = Debt("DEBTOR")
    dummy_creditor = Asset("CREDITOR")
    dummy_owner = Equity("OWNER")
    dummy_entries = [
        JournalEntryD(
            "Entry 1",
            Asset("A1"),
            Debt("D1"),
            *dummy_accounts,
        ),
        JournalEntryD(
            "Entry 2",
            Asset("A2"),
            *dummy_accounts,
        ),
        JournalEntryD(
            "Entry 3",
            *dummy_accounts,
        ),
    ]
    dummy_

# Generated at 2022-06-14 04:25:32.515128
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert (False)


# Generated at 2022-06-14 04:25:39.445610
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import datetime
    from decimal import Decimal

    # Dirty hack to satisfy mypy's strictness
    class Mock(ReadInitialBalances):
        def __call__(self, period: datetime.date) -> Dict[str, Decimal]:
            return {}
    mock = Mock()
    mock(datetime.date(2020, 1, 1))
    assert True

# Generated at 2022-06-14 04:25:47.561061
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .journaling import ReadJournalEntries, build_journal_entry, compile_posting_program
    from .accounts import Account, ReadAccounts

    ## Prepare stubs
    now = datetime.date.today()
    accounts = {
        Account.get(1010): 10,
        Account.get(3010): -100,
        Account.get(4010): 0,
    }

    ## Compile functions:
    read_journal_entries: ReadJournalEntries[int] = compile_posting_program(ReadAccounts(accounts))
    read_initial_balances: ReadInitialBalances = lambda _: accounts

    ## Compile program:
    program: GeneralLedgerProgram[int] = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Build a journal entry

# Generated at 2022-06-14 04:25:59.621646
# Unit test for function build_general_ledger
def test_build_general_ledger():
    
    from .generic import Direction
    from .accounts import AccountType
    from .journaling import JournalEntry, Posting
    from .commons.zeitgeist import DateRange

    # Date range
    period = DateRange(datetime.date(2019,8,10), datetime.date(2019,8,13))

    
    # Create some accounts
    account_1000 = Account(1000, "Cash", AccountType.ASSET, None)
    account_2000 = Account(2000, "Inventory", AccountType.ASSET, None)
    account_1100 = Account(1100, "Accounts Receivable", AccountType.ASSET, None)
    account_1200 = Account(1200, "Prepaid Expenses", AccountType.ASSET, None)

# Generated at 2022-06-14 04:26:09.204734
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Unit test for method __call__ of class ReadInitialBalances.
    """

    # Initialize required parameters:
    period = DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))
    # pylint: disable=unnecessary-lambda
    result = compile_general_ledger_program(lambda x: {}, lambda x: [])(period)
    # pylint: enable=unnecessary-lambda
    assert type(result) == GeneralLedger
    assert result.period == period
    assert result.ledgers == {}

# Generated at 2022-06-14 04:26:20.214430
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():

    from datetime import date

    from ..commons.zeitgeist import this_year

    # Typical initial balances as of 31-Dec-2019:
    initial_balances = {
        Account("Cash"): Balance(date(2019, 12, 31), Quantity(Decimal("50000.00"))),
        Account("Accounts Receivable"): Balance(date(2019, 12, 31), Quantity(Decimal("50000.00"))),
        Account("Inventory"): Balance(date(2019, 12, 31), Quantity(Decimal("75000.00"))),
        Account("Prepaid Expenses"): Balance(date(2019, 12, 31), Quantity(Decimal("5000.00"))),
        Account("Capital"): Balance(date(2019, 12, 31), Quantity(Decimal("100000.00"))),
    }

    # Typical journal entry posted on

# Generated at 2022-06-14 04:26:36.786966
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import BalanceSheet, IncomeStatement, ReadAccounts
    from .journaling import PostJournalEntries
    from .reporting import ReadReport
    from .transactions import ReadTransactions
    from .unit_of_work import MemoryUnitOfWork

    ## UoW, accounts and transactions:
    uow = MemoryUnitOfWork()
    read_transactions = ReadTransactions(uow)
    read_accounts = ReadAccounts(uow)

    ## Journal entries and initial balances:
    post_journal_entries = PostJournalEntries(uow)
    read_journal_entries = ReadJournalEntries(uow)

    ## Prepare initial balances:

# Generated at 2022-06-14 04:26:45.775710
# Unit test for method add of class Ledger
def test_Ledger_add():
    l = Ledger(Account(123), Balance(datetime.date(2020,2,1), Quantity(12)))
    j = JournalEntry(datetime.date(2020,2,1), " ", (Posting(Account(123), Quantity(3)), Posting(Account(234), Quantity(3))))
    p = Posting(Account(123), Quantity(1))
    l.add(p)
    assert l.entries[0].posting.account == p.account
    assert l.entries[0].posting.amount == p.amount
    assert l.entries[0].balance == Quantity(Decimal(13))

# Generated at 2022-06-14 04:26:55.852235
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {Account(no, 'DUMMY', 'ASSET'): Balance(dt=period.since, value=Quantity(Decimal(0))) for no in range(0, 2) }
    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return ()
    glp = compile_general_ledger_program(read_initial_balances=_read_initial_balances, read_journal_entries=_read_journal_entries)
    gl = glp(DateRange(since=datetime.date(2020,1,1),until=datetime.date(2020,6,30)))
    assert len(gl.ledgers)==2

# Generated at 2022-06-14 04:27:07.153866
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import TerminalAccount
    from .commons import Direction

    account = TerminalAccount('Assets/Current Assets/Accounts Receivable')
    ledger = Ledger(account, Balance(date=datetime.date.today(), value=Decimal(0)))
    posting = Posting(account, date=datetime.date.today(), amount=Decimal(100), direction=Direction.DEBIT)
    entry = ledger.add(posting)
    assert entry.balance == Decimal(100)
    assert ledger.entries[-1].balance == Decimal(100)

    posting2 = Posting(account, date=datetime.date.today(), amount=Decimal(50), direction=Direction.CREDIT)
    entry2 = ledger.add(posting2)
    assert entry2.balance == Decimal(50)
    assert ledger

# Generated at 2022-06-14 04:27:18.990509
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    ## Mock initial balance reader:
    def _initial_balances(period: DateRange) -> InitialBalances:
        return {Account("1000"): Balance(period.since, Quantity(Decimal(10000)))}

    ## Mock journal entry reader:
    def _read_journal_entries(period: DateRange) -> List[JournalEntry]:
        return [
            JournalEntry(
                date=period.since,
                description="Cash Deposit",
                account="1000",
                credit=Decimal(1000),
            ),
            JournalEntry(
                date=period.until,
                description="Cash Withdrawal",
                account="1000",
                debit=Decimal(1000),
            ),
        ]

    ## Compile the program:
    program = compile_general_ledger_program(_initial_balances, _read_journal_entries)



# Generated at 2022-06-14 04:27:26.865773
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import Account

    from .generic import read_initial_balances

    from .journaling import ReadJournalEntries, StandardJournalEntry

    ## Consume implementations of the algebra and return a program:
    program = compile_general_ledger_program(read_initial_balances, ReadJournalEntries.from_dict)

    ## Mock initial balances algorithm:
    initial_balances = {
        Account.where(name="CA").first(): Balance(datetime.date(2019, 1, 1), Quantity(Decimal(10)))
    }

# Generated at 2022-06-14 04:27:38.246336
# Unit test for method add of class Ledger
def test_Ledger_add():
    date = datetime.date(2020, 1, 1)
    debit_account = Account(0, "Debit Account")
    credit_account = Account(1, "Credit Account")
    journal = JournalEntry(0, date, 0, "Test", [debit_account, credit_account])
    posting = Posting(journal, debit_account, Amount(Decimal(2)))
    ledger = Ledger(debit_account, Balance(date, Quantity(Decimal(0))))
    entry = ledger.add(posting)
    assert entry.balance == Quantity(Decimal(2))
    assert entry.is_debit
    assert ledger._last_balance == Quantity(Decimal(2))

if __name__ == "__main__":
    import pytest

    pytest.main(args=["-s", __file__])

# Generated at 2022-06-14 04:27:51.815342
# Unit test for method add of class Ledger
def test_Ledger_add():
    # given
    test_posting = Posting(date = datetime.date(2020, 4, 1),account = "the account", quantity = Quantity(5000),direction="D")
    test_balance = Balance(date = datetime.date(2020, 4, 1), account = "the account",value = Quantity(2000))
    # when
    test_ledger = Ledger(account = "the account",initial = test_balance)
    # then
    test_ledger.add(test_posting)
    assert test_ledger.initial.value == Quantity(2000)
    assert isinstance(test_ledger.entries, list)
    assert isinstance(test_ledger.entries[0], LedgerEntry)
    assert test_ledger.entries[0].balance == Quantity(7000)

# Generated at 2022-06-14 04:27:59.667341
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import datetime
    from dataclasses import dataclass
    from decimal import Decimal
    from typing import List, Iterable, Optional
    from collections import defaultdict
    from ...commons.exceptions import ProgrammingError

    __all__ = [
        "JournalEntry",
        "Posting",
        "build_general_ledger",
    ]

    @dataclass
    class Posting:
        """
        Posted amounts for an account.
        """

        #: Account posting (debit or credit) applies to.
        account: Account

        #: Amount posted.
        amount: Amount

        #: Date of posting.
        date: datetime.date

        @property
        def is_debit(self) -> bool:
            """
            Indicates if the posting is a debit.
            """
            return self.amount < Dec

# Generated at 2022-06-14 04:28:00.257291
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    ...

# Generated at 2022-06-14 04:28:24.780636
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import Account as Acct
    from .journaling import JournalEntry as Jentry, Posting as Pstg, build_journal_entry as bjentry


# Generated at 2022-06-14 04:28:35.199487
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test function build_general_ledger
    """
    from .journaling import Posting, JournalEntry

    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
    initial = {}
    journal = []

    general_ledger = build_general_ledger(period, journal, initial)

    assert general_ledger == GeneralLedger(
        period,
        {},
    )

    initial = {
        Account(["1234.56.789", ]): Balance(period.since, Quantity(Decimal(10)))
    }

# Generated at 2022-06-14 04:28:38.939947
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    def _callback(period: DateRange) -> InitialBalances:
        return {}
    test = ReadInitialBalances.__call__(_callback, DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 31)))
    assert isinstance(test, dict)


# Generated at 2022-06-14 04:28:47.572496
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import JournalingTestSupport
    """
    Tests :py:func:`build_general_ledger`.
    """
    ## Account numbers:
    acc_100100 = Account("100100", "Cash in hand")
    acc_100500 = Account("100500", "Cash at bank")
    acc_101000 = Account("101000", "Accounts receivable")
    acc_102000 = Account("102000", "Inventory")
    acc_102001 = Account("102001", "Inventory - Raw materials")
    acc_102002 = Account("102002", "Inventory - Work-in-progress")
    acc_102003 = Account("102003", "Inventory - Finished goods")
    acc_111000 = Account("111000", "Land")
    acc_112000 = Account("112000", "Buildings")
   

# Generated at 2022-06-14 04:28:48.300156
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:28:59.257953
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import datetime
    from abc import ABC
    from dataclasses import dataclass
    from typing import Callable, List, Tuple
    from unittest.mock import Mock
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, Accounts
    from .journaling import JournalEntry, Posting, JournalEntries

    #: Concrete ledger program.
    _LedgerProgram = GeneralLedgerProgram[None]

    ## We define this as a dataclass for easier introspection:
    @dataclass
    class _TestInitialBalances:
        """
        Helper class for initial balances.
        """

        #: Period to return initial balances for.
        period: DateRange

        #: Actual initial balances to return.
        balances: InitialBalances

    ## We define this as a dataclass for easier

# Generated at 2022-06-14 04:29:12.443508
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from .accounts import Account, AccountKind
    from .generic import Currency, Stock
    from .numbers import Amount, Quantity

    @dataclass
    class Mock(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account(1, "Cash", AccountKind.Asset): Balance(date(2020, 1, 1), Quantity(Decimal(10000), Currency.USD)),
                Account(2, "Equity", AccountKind.Equity): Balance(
                    date(2020, 1, 1), Quantity(Decimal(5000), Currency.USD)
                ),
                Account(3, "Stock", AccountKind.Asset): Balance(
                    date(2020, 1, 1), Quantity(Decimal(100), Stock.AAPL)
                ),
            }

   

# Generated at 2022-06-14 04:29:25.067604
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test case for function build_general_ledger
    """
    from .accounts import Account
    from .journaling import create_journal_entry
    import datetime
    from decimal import Decimal
    from .numbers import Amount, Balance, Quantity, Currency
    from .zeitgeist import DateRange
    test_account = Account(**{"id": 1, "type": "A", "name": "A1", "description": "TEST"})
    test_initial_balance = Balance(**{"date": datetime.date(2019, 9, 26), "value": Quantity(**{"amount": Decimal('33.00'), "currency": Currency(**{"code": "USD", "symbol": "$", "name": "US Dollar"})})})

# Generated at 2022-06-14 04:29:28.460753
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ... import __version__

    print(
        f"test__ReadInitialBalances___call__: version {__version__}"
    )  # pragma: no cover


# Generated at 2022-06-14 04:29:32.607391
# Unit test for method add of class Ledger
def test_Ledger_add():
    #test 1
    a = 1
    b = 1
    assert a == b, "test 1: a != b"
    #test 2
    a = 2
    b = 2
    assert a == b, "test 1: a != b"



# Generated at 2022-06-14 04:30:04.868690
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram
    """
    class MockReadInitialBalances(Protocol):
        """
        Mock: Type of functions which reads and returns initial balances.
        """

        def __call__(self, period: DateRange) -> InitialBalances:
            pass

    class MockReadJournalEntries(Protocol):
        """
        Mock: Type of functions which reads journal entries.
        """

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    class MockBuildGeneralLedger(Protocol):
        """
        Mock: Type of functions which builds a general ledger.
        """


# Generated at 2022-06-14 04:30:16.726015
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Posting, JournalEntry
    from dataclasses import asdict


# Generated at 2022-06-14 04:30:24.253603
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test function build_general_ledger.
    """
    from ..journal_entries import CashTypes, Withdrawal

    #: Define a simple journal entry:
    je = JournalEntry(
        date=datetime.date(2020, 1, 1),
        description="Cash withdrawal",
        postings=[
            Posting(CashTypes.Cash, Amount(250.00), Withdrawal),
            Posting(CashTypes.PettyCash, Amount(250.00), Withdrawal),
        ],
    )

    #: Define initial balances:
    initial = {
        CashTypes.Cash: Balance(datetime.date(2019, 12, 31), Quantity(5_000.00)),
        CashTypes.PettyCash: Balance(datetime.date(2019, 12, 31), Quantity(1_000.00)),
    }



# Generated at 2022-06-14 04:30:37.470700
# Unit test for function build_general_ledger
def test_build_general_ledger():

    import os
    import datetime
    from decimal import Decimal
    from typing import Dict
    from dataclasses import dataclass, field
    import pandas as pd
    import numpy as np
    from ..journaling.models import Journal, JournalEntry, Posting

    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from matplotlib.dates import MonthLocator, DateFormatter

    from ..commons.zeitgeist import DateRange
    from ..commons.numbers import Amount, Quantity
    from .accounts import Account
    from .generic import Balance
    from .journaling import ReadJournalEntries
    from .ledgers import GeneralLedger, build_general_ledger, ReadInitialBalances

    from .reports import GeneralLedgerReport

# Generated at 2022-06-14 04:30:50.358806
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .accounts import get_account
    from .journaling import JournalEntry, Posting, build_journal_entry, get_account_posting, get_tax_posting

    from .journaling import AccountingMethod
    from .taxing import Tax, TaxAccountingAction
    from .taxing import TaxAccountingMethod, TaxingMethod
    from .taxing import TaxCode, TaxRate
    from .taxing import TaxPayable, TaxReceivable, UseTaxPayable
    from .taxing import build_tax_payable_account, build_tax_receivable_account, build_use_tax_payable_account

    from .taxing import TaxCode, TaxRate, build_tax_code
    from .taxing import Tax, TaxAccountingAction, TaxAccountingMethod, TaxingMethod, build_tax

    from .taxing import build_tax_

# Generated at 2022-06-14 04:30:58.244734
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Tests the build_general_ledger function
    """
    from .accounts import Account
    from .journaling import (
        CashJournalEntry,
        JournalEntry,
        Posting,
        ReverseJournalEntry,
        SalesInvoiceJournalEntry,
    )
    from .products import BaseProduct, Product

    product1 = BaseProduct("Product 1", "P1", 10.0)
    product2 = Product("Product 2", "P2", product1, 1.5)
    product3 = Product("Product 3", "P3", product1, 2.0)
    product4 = Product("Product 4", "P4", product1, 2.5)


# Generated at 2022-06-14 04:31:00.822957
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # TODO: Implement test for method __call__
    raise NotImplementedError  # TODO: Remove this line


# Generated at 2022-06-14 04:31:08.572068
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import make_journal_entry

    debits = [
        ("Sales", 100),
        ("Sales", 200),
        ("Sales", 300),
        ("Sales", 400),
        ("Sales", 500),
        ("Sales", 600),
        ("Sales", 700),
    ]

    credits = [
        ("Accounts Receivable", 100),
        ("Accounts Receivable", 200),
        ("Accounts Receivable", 300),
        ("Accounts Receivable", 400),
        ("Accounts Receivable", 500),
        ("Accounts Receivable", 600),
        ("Accounts Receivable", 700),
    ]

    initial = {Account("Cash"): Balance(datetime.date(2019, 1, 1), Quantity(0))}


# Generated at 2022-06-14 04:31:17.516990
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import datetime
    from decimal import Decimal
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, GeneralLedgerAccount
    from .generic import Balance
    from .journaling import JournalEntry, Posting, PostingDirection

    ## Prepare a billing journal, i.e. an increase in our receivables and income accounts:

# Generated at 2022-06-14 04:31:24.224240
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    assert hasattr(
        compile_general_ledger_program(lambda p: {}, lambda p: []),
        "__call__",
    ), "Must return a function."

    assert isinstance(
        compile_general_ledger_program(lambda p: {}, lambda p: [])(DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))),
        GeneralLedger,
    ), "Must return a general ledger."

# Generated at 2022-06-14 04:32:24.869695
# Unit test for method add of class Ledger
def test_Ledger_add():
    #Init account, journal, and ledger
    acct = Account("Test", "TST", "TST", "TST")
    journal = JournalEntry("Test Journal", datetime.datetime.now(), "TST")
    ledger = Ledger(acct, Balance(datetime.datetime(2020, 7, 1), 1))

    #Posting 1
    post1 = Posting(journal, acct, 1, True)
    entry1 = LedgerEntry(ledger, post1, Quantity(Decimal(1)))
    assert entry1.balance == 2
    #Posting 2
    post2 = Posting(journal, acct, 2, False)
    entry2 = LedgerEntry(ledger, post2, Quantity(Decimal(0)))
    assert entry2.balance == -2

# Generated at 2022-06-14 04:32:31.061259
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import unittest

    from ..commons.files import read_json_from_file
    from ..commons.zeitgeist import today, yesterday
    from .accounts import Account, AccountType, Assets, Equity, Liabilities
    from .journaling import write_journal_entries, Journal
    from .journaling.algebra import ConsumeJournalEntries
    from .journaling.exceptions import NoMoreEntriesAvailable

    # Set up the input file:
    input_file_path = "./test_GeneralLedgerProgram___call__.json"
    entries_buffer = []

    def write_journal_entries_to_buffer(account: Account, entries: Iterable[Journal]) -> None:
        nonlocal entries_buffer
        entries_buffer += list(entries)


# Generated at 2022-06-14 04:32:41.743793
# Unit test for method add of class Ledger
def test_Ledger_add():
    from datetime import datetime
    from efb import commons
    from efb import journaling
    from efb_teller import ledgers
    account = commons.accounts.Account('000')
    journal = journaling.JournalEntry(datetime.now(), '', [journaling.Posting(account, commons.Amount(123), commons.Direction.Debit)])
    Ledger = ledgers.Ledger
    entry = Ledger.add(account, Balance(datetime.now(), commons.Quantity(123)), journal)
    assert entry.account == account
    assert entry.balance == commons.Quantity(246)

# Generated at 2022-06-14 04:32:49.564777
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from dataclasses import asdict
    import datetime
    from decimal import Decimal
    from typing import Generator
    from unittest import mock
    from unittest.mock import Mock
    from .accounts import Accounts
    from .journaling import Journal, Posting, ReadJournalEntries

    ## Mock implementation for the algebra which reads journal entries:
    read_journal_entries: ReadJournalEntries = Mock(spec=ReadJournalEntries)

# Generated at 2022-06-14 04:32:54.480404
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date, timedelta

    from ..commons.numbers import Amount, Quantity
    from .accounts import Account
    from .journaling import JournalEntry, JournalType, Posting, build_journal_entry, build_standard_journal

    # Define a function which returns test journal entries:
    def _get_journal_entries(period: DateRange) -> Iterable[JournalEntry]:
        # Define a function which returns test journal entries:
        def _create_journal_entry(date:datetime.date, description:str) -> JournalEntry:
            acc = Account("Account", 1)
            acc.set_balance(Balance(date, Amount(Decimal(10))))
            # Test class JournalEntry

# Generated at 2022-06-14 04:33:03.955234
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Journal

    journal = (
        Journal(datetime.date(2019, 1, 1), "A", Posting(Account("A"), Quantity(10))),
        Journal(datetime.date(2019, 1, 2), "B", Posting(Account("B"), Quantity(5))),
        Journal(datetime.date(2019, 1, 3), "C", Posting(Account("C"), Quantity(25))),
    )

    ledger = build_general_ledger(DateRange(datetime.date(2018, 12, 1), datetime.date(2019, 12, 31)), journal, {})
    assert ledger.period == DateRange(datetime.date(2018, 12, 1), datetime.date(2019, 12, 31))
    assert ledger.ledgers["A"].account == Account("A")

# Generated at 2022-06-14 04:33:10.031265
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {}
    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return []
    assert compile_general_ledger_program(_read_initial_balances, _read_journal_entries)

# Generated at 2022-06-14 04:33:10.790611
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:33:18.727333
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    #: Arrange:
    period = DateRange(since=datetime.date(2018, 1, 1), until=datetime.date(2018, 1, 31))
    ## Return a general ledger for the same period.
    gl = compile_general_ledger_program(lambda _: dict(), lambda _: iter([]))(period)

    #: Act:
    ## Extract the general ledger from the program and compare against the gl variable.
    result = gl == gl

    #: Assert:
    ## Expect the result to be True.
    assert result == True

# Generated at 2022-06-14 04:33:33.094486
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Verifies the GeneralLedgerProgram.__call__() method.
    """

    import datetime
    from typing import Callable
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .generic import Balance
    from .journaling import JournalEntry, JournalType, NewJournal, Posting, PostJournal, PostingDirection
    from .transactions import Transaction

    ## Create an initial balances map:
    def _initial_balances(period: DateRange) -> Dict[Account, Balance]:
        return {a: Balance(period.since, Quantity(Decimal(100))) for a in range(4)}

    ## Define read journal entries implementation: