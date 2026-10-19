

# Generated at 2022-06-14 04:23:46.663585
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account("a")
    ledger = Ledger(account, Balance(datetime.date(2000, 1, 1), Quantity(Decimal(0))))

    journal_entry = JournalEntry()
    journal_entry.date = datetime.date(2000, 1, 1)
    journal_entry.postings.append(Posting())
    journal_entry.postings[0].account = account
    journal_entry.postings[0].amount = 100
    journal_entry.postings[0].direction = Decimal(1)

    ledger.add(journal_entry.postings[0])
    assert ledger.balance == 100
    assert ledger.amount == 100

    journal_entry.postings.append(Posting())
    journal_entry.postings[1].account = account
    journal_entry.postings[1].amount = -200


# Generated at 2022-06-14 04:23:56.017735
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..commons.zeitgeist import get_last_day_of_month

    from .accounts import AccountType, Country, is_terminal

    from .ledgering import ReadJournalEntries

    accounts = {
        Account(code="1010", name="cash", account_type=AccountType.assets, country=Country.np),
        Account(code="2020", name="suppliers", account_type=AccountType.liabilities, country=Country.np),
        Account(code="3020", name="sales", account_type=AccountType.revenue, country=Country.np),
        Account(code="4030", name="accounts receivable", account_type=AccountType.assets, country=Country.np),
    }


# Generated at 2022-06-14 04:24:08.026208
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Is the result of calling the method equal to the expected result.
    assert (
        compile_general_ledger_program(read_initial_balances=lambda period: {}, read_journal_entries=lambda period: [])
        (period="")
        == GeneralLedger(period="", ledgers=dict())
    )
    # Is the result of calling the method equal to the expected result.
    assert (
        compile_general_ledger_program(
            read_initial_balances=lambda period: {}.__contains__(account=[]), read_journal_entries=lambda period: [],
        )
        (period="")
        == GeneralLedger(period="", ledgers=dict())
    )
    # Is the result of calling the method equal to the expected result.

# Generated at 2022-06-14 04:24:20.271470
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Test setup
    from ..import accounting
    from ..commons.zeitgeist import Date
    from ..entities.entries import JournalEntry, Posting
    from ..entities.assets import CashRegister, Cash, Account
    from ..entities.accounts import ReceivablesControl
    from ..protocols.initial_balances import ReadInitialBalances
    from ..protocols.ledgers import Ledger
    from ..protocols.algebras import ReadJournalEntries

    # defining a ledger
    ledger = Ledger(Account.of_cash, Quantity(0))

    # defining a journal entry
    journal_entry = []
    journal_entry.append(JournalEntry.of_payment(
        Date(1910, 1, 1), "payment", -Cash.from_usd(1000)))

    # testing that the object ledger is of

# Generated at 2022-06-14 04:24:33.960285
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from datetime import date
    from decimal import Decimal
    from typing import Dict, Iterable, List, Optional, Tuple
    from unittest.mock import Mock, call
    from .accounts import Account, AccountType, AccountCategory
    from .commons.zeitgeist import DateRange
    from .journaling import JournalEntry, Posting, Journal, JournalType, TransactionType
    from ..commons.numbers import Amount, Quantity

    Period = DateRange(date(2019, 1, 1), date(2019, 12, 31))

    @dataclass
    class MockJournalEntry(JournalEntry):
        postings: List[Posting[None]]


# Generated at 2022-06-14 04:24:45.277718
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..journaling.journal import Journal
    from ..journaling.post import Post

    period = DateRange(since=datetime.date(2018, 1, 1), until=datetime.date(2018, 1, 10))

# Generated at 2022-06-14 04:24:52.297871
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .model import JournalEntry, Posting
    from datetime import date
    from dataclasses import dataclass
    from decimal import Decimal
    from typing import Dict, List
    from functools import singledispatchmethod
    from .accounts import Account

    @dataclass
    class SomeModel:
        """
        Sample model for testing
        """

        pass

    class AccountLedger(Generic[_T]):
        """
        Example of Ledger
        """

        @singledispatchmethod
        def debit(self, x: _T, amount: Decimal):
            """
            Sample debit
            """
            pass

        @debit.register
        def _(self, x: SomeModel, amount: Decimal):
            pass


# Generated at 2022-06-14 04:25:05.293120
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Test setup
    import uuid
    from ..accounts.implementation import Account

    # Define journal entries
    @dataclass
    class JournalEntry:
        id: uuid.uuid4()
        date: datetime.date(2020,1,1)
        description: "Test Entry"
        debit: Amount(100.00)
        credit: Amount(100.00)
    
    # Define postings
    @dataclass
    class Posting:
        account: Account
        journal: JournalEntry
        amount: Amount(100.00)
        direction: 1

    # Define the ledger
    @dataclass
    class Ledger(Generic[_T]):
        #: Account of the ledger.
        account: Account

        #: Initial balance of the ledger.
        initial: Balance

        #: Ledger entries

# Generated at 2022-06-14 04:25:14.563922
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():  # noqa
    from .journaling import JournalEntry
    from .accounts import Account

    from .commons.algebraic import consume_iterable

    class MockReadInitialBalances:
        def __init__(self, initial_balances):
            self.initial_balances = initial_balances

        def __call__(self, period: DateRange):
            return self.initial_balances

    class MockReadJournalEntries:
        def __init__(self, journal_entries):
            self.journal_entries = journal_entries

        def __call__(self, period: DateRange):
            return self.journal_entries

    class MockJournalEntry:
        def __init__(self, date: datetime.date, description: str, postings):
            self.date = date
            self.description = description
            self

# Generated at 2022-06-14 04:25:25.230009
# Unit test for function build_general_ledger
def test_build_general_ledger():
    # Set up
    from .accounts import Account, AccountType
    from datetime import date
    from decimal import Decimal


# Generated at 2022-06-14 04:25:42.265574
# Unit test for function build_general_ledger
def test_build_general_ledger():

    from .journaling import build_journal_entry

    # Given
    period = DateRange(since=datetime.date(2019, 1, 1), until=datetime.date(2019, 12, 31))

# Generated at 2022-06-14 04:25:56.116505
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    a1 = Account(acct_id=1, group='asset', subgroup='ca')
    a2 = Account(acct_id=2, group='liability', subgroup='current_liability')
    p1 = Posting(account=a1, date=date(2020, 5, 6), amount=-150, direction=-1)
    p2 = Posting(account=a2, date=date(2020, 5, 6), amount=150, direction=1)
    j = JournalEntry(date=date(2020, 5, 6), description="expenses", postings=[p1, p2])
    initial = {a1: Balance(date(2020, 5, 6), Quantity(100))}

    period = DateRange(since=date(2020, 5, 6), until=date(2020, 5, 6))

# Generated at 2022-06-14 04:25:57.601961
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert (ReadInitialBalances.__call__)



# Generated at 2022-06-14 04:26:07.114759
# Unit test for method add of class Ledger
def test_Ledger_add():
    ledger = Ledger(Account("ACCOUNT"), Balance(datetime.date(2019, 1, 1), Decimal(3000)))
    posting = Posting(datetime.date(2019, 1, 1), Account("ACCOUNT"), Decimal(1500), "Dr", "Test-1")
    entry = ledger.add(posting)
    assert ledger.entries == [entry]
    assert ledger.entries[0].balance == Decimal(4500)
    posting = Posting(datetime.date(2019, 1, 1), Account("ACCOUNT"), Decimal(-1500), "Cr", "Test-2")
    entry = ledger.add(posting)
    assert ledger.entries == [entry]
    assert ledger.entries[0].balance == Decimal(3000)

# Generated at 2022-06-14 04:26:19.058465
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.zeitgeist import date_from_str
    from .accounts import Account, AccountType
    from .journaling import Journal, JournalEntry, LedgerDirection, Posting

    # account/ledger definitions
    asset = Account("1110", "Cash", AccountType.ASSET)
    liability = Account("3270", "Accounts Payable", AccountType.LIABILITY)
    equity = Account("2110", "Capital", AccountType.EQUITY)

    # ledger instances
    ledg_asset = Ledger(asset, Balance(date_from_str("2020-06-01"), Quantity(0)))
    ledg_liability = Ledger(liability, Balance(date_from_str("2020-06-01"), Quantity(0)))

    # transaction instances
    # asset debit, liability credit
    posting_a

# Generated at 2022-06-14 04:26:32.081912
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from business.accounting.journaling import (
        JournalEntry,
        Posting,
    )
    from .accounts import Account

    accounts = {
        Account("1000"): Balance(decimal.Decimal("10000")),
        Account("2000"): Balance(decimal.Decimal("10000")),
        Account("3000"): Balance(decimal.Decimal("10000")),
    }

    journal = [
        JournalEntry(
            date=datetime.date(2019, 12, 1),
            description="Income",
            postings=[
                Posting(
                    account="1000",
                    amount=decimal.Decimal("10000"),
                    direction=PostingDirection.CREDIT,
                    cntracts=[Account("2000"), Account("3000")],
                )
            ],
        )
    ]

    ledger = build_

# Generated at 2022-06-14 04:26:45.287235
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.zeitgeist import ZeroPoint

    from .accounts import Account, AccountType

    from .journaling import Journal, PostingDirection

    #: Declare sample accounts.
    asset = Account("1000", AccountType.ASSET, "Cash on hand")
    expense = Account("3000", AccountType.EXPENSE, "Office supplies")

    #: Declare a sample journal entry.
    journal = Journal(
        ZeroPoint.as_date(), "Paid office supplies", [
            Posting(asset, PostingDirection.DEBIT, Amount(Decimal(1000))), Posting(expense, PostingDirection.CREDIT, Amount(Decimal(1000))),
        ]
    )

    #: Create a ledger for account asset.

# Generated at 2022-06-14 04:26:52.957621
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():

    from datetime import date
    from decimal import Decimal
    from .accounts import AssetAccount

    def read_initial_balances(period):
        return {AssetAccount("000"): Balance(date(2019, 1, 1), Decimal(0))}

    assert read_initial_balances(DateRange(date(2019, 1, 1), date(2019, 12, 31))) == {
        AssetAccount("000"): Balance(date(2019, 1, 1), Decimal(0))
    }


# Generated at 2022-06-14 04:27:05.431802
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..commons.zeitgeist import DateTime
    from .accounts import Accounts
    from .journaling import Journal

    import collections.abc
    import datetime
    from decimal import Decimal
    from typing import Any, Mapping
    import unittest

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.accounts = Accounts()


# Generated at 2022-06-14 04:27:18.060977
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram.
    """

    from unittest import TestCase
    from unittest.mock import MagicMock, patch

    from .accounts import AssetAccount


# Generated at 2022-06-14 04:27:49.222464
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Parameters:
    p = DateRange(since=datetime.date(2018, 1, 1), until=datetime.date(2018, 12, 31))

    # Expected result:
    expected = dict()

    # Actual result:
    actual = ReadInitialBalances.__call__(None, p)

    # Assertions:
    assert actual == expected


# Generated at 2022-06-14 04:27:54.658991
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class MockReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return dict()

    instance = MockReadInitialBalances()
    result = instance.__call__('period')
    assert type(result) is dict

# Generated at 2022-06-14 04:28:05.645056
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """Unit test for function compile_general_ledger_program"""

    from datetime import date
    from typing import Protocol, cast

    from ..commons.algebra import Algebra

    from .accounts import Asset, Expense, Liability, Revenue
    from .journaling import JournalEntry, Posting, build_journaling_program, read_journal_entries
    from .payables_receivables import ReadInitialBalances, build_payables_receivables_algebra

    ## Initial balances:

# Generated at 2022-06-14 04:28:17.359586
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for :py:func:`GeneralLedgerProgram.__call__`.
    """

    ## Imports:
    import datetime
    from decimal import Decimal
    from typing import Iterable, Iterator
    from unittest.mock import Mock  # noqa: F401
    from .accounts import Account, AssetAccount, LiabilityAccount
    from .journaling import JournalEntry, Posting
    from .numbers import Amount, Currency, Quantity

    ## Mocks:

# Generated at 2022-06-14 04:28:22.585359
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import datetime

    @dataclass
    class _ReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            pass
    assert(isinstance(_ReadInitialBalances(), ReadInitialBalances))


# Generated at 2022-06-14 04:28:24.780875
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program.

    :return:
    """
    pass

# Generated at 2022-06-14 04:28:35.198445
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import datetime
    from dataclasses import dataclass, field
    from decimal import Decimal
    from typing import Dict, Iterable
    from unittest import TestCase

    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountCode
    from .journaling import JournalEntry, Posting, ReadJournalEntries
    from . import general_ledgers as m

    #: Initial balances:
    InitialBalances = Dict[Account, Balance]

    # Test setup:
    @dataclass
    class Balance:
        """
        Model for a balance.
        """

        #: Balance date.
        date: datetime.date

        #: Balance amount.
        amount: Quantity


# Generated at 2022-06-14 04:28:46.006988
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import pytest
    from ..books import LedgerAccount
    from ..ledgers.generic import Balance
    from ..ledgers.journaling import JournalEntry, Posting, TypeOfLedgerEntry

    # Read initial balances:
    read_initial_balances = lambda p: {
        "equity": Balance(p.since, Quantity(Decimal(0))),
        "revenue": Balance(p.since, Quantity(Decimal(0))),
        "expenses": Balance(p.since, Quantity(Decimal(0))),
    }

    # Read journal entries:

# Generated at 2022-06-14 04:28:58.407171
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    def _assert_compiled_program_returns_expected_general_ledger(compiled_program):
        ## Set up accounting period and expected general ledger:
        period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))
        general_ledger = GeneralLedger(period, {})

        ## Invoke the compiled program. Note we have to cast the result to the expected type!
        assert compiled_program(period) == general_ledger

    def _assert_compiled_program_returns_expected_general_ledger_at_different_period(compiled_program):
        ## Set up accounting period and expected general ledger:
        period = DateRange(datetime.date(2020, 3, 1), datetime.date(2020, 12, 31))
        general_ledger = GeneralLedger

# Generated at 2022-06-14 04:29:11.408823
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    ## Compile
    program = compile_general_ledger_program(
        lambda period: {},
        lambda period: (
            JournalEntry(
                date=datetime.date(2020, 1, 1),
                description="sample journal entry",
                postings=[Posting("a1", Decimal(1), "b1"), Posting("a2", Decimal(-1), "b2")],
            ),
        ),
    )

    ## Execute:
    gl = program(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 1)))

    ## Validate results:
    assert len(gl.ledgers) == 2

# Generated at 2022-06-14 04:30:17.301410
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest.mock import call, Mock

    ## Mock the ReadInitialBalances interface.
    mock = Mock(spec=ReadInitialBalances)

    ## Call the mock and verify.
    assert mock(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))) == mock.return_value

    assert mock.call_args == call(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31)))


# Generated at 2022-06-14 04:30:23.016201
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from ledgersimple.model.accounts import AccountName, AccountType
    from ledgersimple.model.journaling import Balance
    assert isinstance(__call__, ReadInitialBalances)
    period = DateRange(since=date(2019, 1, 1), until=date(2019, 1, 2))
    expected = {Account(AccountName.CASH, AccountType.ASSETS): Balance(date(2018, 12, 31), Decimal(10))}
    actual = __call__(period)
    assert expected == actual


# Generated at 2022-06-14 04:30:23.863840
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert False

# Generated at 2022-06-14 04:30:24.637210
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass  # TODO

# Generated at 2022-06-14 04:30:37.674914
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program
    """

    #from datetime import date
    #from decimal import Decimal
    #from typing import Iterable
    #from unittest.mock import Mock

    #from ..commons.amounts import Amount
    #from ..commons.numbers import Quantity
    #from ..commons.zeitgeist import DateRange

    #from .accounts import Account, Accounts
    #from .journaling import JournalEntry, Posting

    #from ..algebras.accounting import DATATYPE as DATATYPE_T
    #from ..algebras.accounting import ReadInitialBalances as ReadInitialBalances_T
    #from ..algebras.journaling import ReadJournalEntries as ReadJournalEntries_T

    #from .accounting import

# Generated at 2022-06-14 04:30:45.321575
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import Account, AccountType

    from .journaling import JournalEntry, Posting

    from .types import Transaction

    def test_read_initial_balances(period: DateRange) -> InitialBalances:
        a1 = Account(AccountType.ASSET, "A1")
        a2 = Account(AccountType.ASSET, "A2")
        return {
            a1: Balance(period.since, Quantity(Decimal(5))),
            a2: Balance(period.since, Quantity(Decimal(10))),
        }


    def test_read_journal_entries(period: DateRange) -> Iterable[JournalEntry[Transaction]]:
        a1 = Account(AccountType.ASSET, "A1")
        a2 = Account(AccountType.ASSET, "A2")

# Generated at 2022-06-14 04:30:56.446615
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Create an account
    account = Account("N")
    # Create an initial balance
    initial = Balance(datetime.date(2020,1,1), Quantity(Decimal(0)))
    # Create a ledger based on the account and initial balance
    ledger = Ledger(account, initial)
    # Create a description for the Journal
    description = "Jan 1 2020"
    # Create a debit amount for the Posting
    debit = Amount(Decimal(100))
    # Create a posting date
    date = datetime.date(2020, 1, 1)
    # Create a transaction
    transaction = Posting(account, debit, date)
    # Create a journal based on the description, transaction, and date
    journal = JournalEntry(description, transaction, date)
    # Post the journal to the ledger
    ledger_entry = ledger.add(transaction)

# Generated at 2022-06-14 04:31:07.955664
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounting import Journal, Posting
    from .accounts import AccountType, Account, GeneralLedgerAccount
    from .journaling import JournalEntry

    class StubReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}


# Generated at 2022-06-14 04:31:12.085380
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Tests for the compile_general_ledger_program function.
    """

    @dataclass
    class ReadInitialBalances(Protocol):
        """
        Type of functions which reads and returns initial balances.
        """

        def __call__(self, period: DateRange) -> InitialBalances:
            pass

    @dataclass
    class ReadJournalEntries(Protocol):
        """
        Type of functions which reads and returns journal entries.
        """

        def __call__(self, period: DateRange) -> Iterable[JournalEntry]:
            pass

    @dataclass
    class GeneralLedgerProgram(Protocol):
        """
        Type definition of the program which builds general ledger.
        """

        def __call__(self, period: DateRange) -> GeneralLedger:
            pass


# Generated at 2022-06-14 04:31:23.518207
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Test case for method __call__ of class GeneralLedgerProgram.
    """
    import os
    import pathlib
    import tempfile
    import unittest

    from ..accounts import Account
    from ..commons.zeitgeist import DateRange
    from .accounts import Balance, ASSET, EXPENSE, LIABILITY, POSTED, REVENUE
    from .journaling import JournalEntry, Posting, Transaction

    FIXTURES_PATH = f"{pathlib.Path(__file__).parent}/../../fixtures"

    # Accounts:

# Generated at 2022-06-14 04:33:07.272903
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # arrange
    ledger = build_general_ledger(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 31)),
                                  [JournalEntry(datetime.date(2020, 1, 1),
                                   "Description",
                                   [Posting(Account(1, "A"), Amount(Decimal(10), "currency")),
                                    Posting(Account(2, "B"), Amount(Decimal(-10), "currency"))])],
                                  {Account(1, "A"): Balance(datetime.date(2020, 1, 1), Decimal(100))})

    # act
    assert ledger.period.since == datetime.date(2020, 1, 1)
    assert ledger.period.until == datetime.date(2020, 1, 31)
    assert len(ledger.ledgers)

# Generated at 2022-06-14 04:33:18.726624
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import dataclasses
    import datetime
    from decimal import Decimal
    from typing import Any
    from .accounts import Account
    from .generic import Balance
    from .journaling import Posting
    def test_impl(period: DateRange) -> InitialBalances:
        return {}

    ReadInitialBalancesImpl = test_impl
    ReadInitialBalancesImpl.__doc__ = ReadInitialBalances.__doc__
    ReadInitialBalancesImpl.__annotations__ = ReadInitialBalances.__annotations__

    assert not dataclasses.is_dataclass(ReadInitialBalancesImpl)
    assert isinstance(ReadInitialBalancesImpl(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))),
                      InitialBalances)


# Generated at 2022-06-14 04:33:33.093931
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Test data
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))