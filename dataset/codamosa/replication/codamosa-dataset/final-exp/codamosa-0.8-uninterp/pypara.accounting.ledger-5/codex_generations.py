

# Generated at 2022-06-14 04:23:50.903901
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import posting
    from .commons.zeitgeist import DateRange

    from . import accounts

    # Setup test journal
    j1_date = datetime.date.fromisoformat("2017-01-01")
    j1_desc = "Journal entry 1"
    j1_postings = [
        posting(accounts.credit_card_chase_visa, debit=(-86.54), date=j1_date),
        posting(accounts.current_assets_bank_chase, credit=86.54, date=j1_date),
    ]
    j2_date = datetime.date.fromisoformat("2017-01-02")
    j2_desc = "Journal entry 2"

# Generated at 2022-06-14 04:23:55.438472
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from decimal import Decimal
    from dataclasses import dataclass
    from ..commons.numbers import Quantity
    from .accounts import Account
    from .generic import Balance

    # val period : DateRange
    period = None

    # let result : InitialBalances
    result = None

    pass  # TODO

    assert result is None
    return


# Generated at 2022-06-14 04:23:56.683339
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    raise NotImplementedError()

# Generated at 2022-06-14 04:24:01.439735
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class _ReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    assert _ReadInitialBalances()(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))) == {}



# Generated at 2022-06-14 04:24:15.152139
# Unit test for function build_general_ledger
def test_build_general_ledger():
    ## Import
    import unittest
    from ..commons.zeitgeist import date_range
    from .accounts import AccountType, Account, Code
    from .journaling import JournalEntry, Posting
    from ..commons.numbers import Amount, Quantity

    ## Set up test fixture

    # Build ledger initial balances
    initial_balances = {
        Account(AccountType.Asset, Code("1001")): Balance(date_range("2020-01-01", "2020-01-03").since, Quantity(100)),
        Account(AccountType.Liability, Code("2001")): Balance(date_range("2020-01-03", "2020-01-04").since, Quantity(50)),
    }

    # Build journal entries
    # pylint: disable=bad-whitespace

# Generated at 2022-06-14 04:24:24.484158
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class _Test_ReadInitialBalances_Impl(ReadInitialBalances):
        _result: InitialBalances

        def __call__(self, _period: DateRange) -> InitialBalances:
            return self._result

    assert (_Test_ReadInitialBalances_Impl({}))({}) == {}

# Generated at 2022-06-14 04:24:29.398634
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # 1. Setup
    # 1.1 Create an object m of class ReadInitialBalances
    m = ReadInitialBalances()
    # 1.2 Call method __call__ of object m
    # 1.3 Accept the result
    assert m.__call__



# Generated at 2022-06-14 04:24:38.759874
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests method __call__ of class GeneralLedgerProgram.
    """

    ##
    ## Read initial balances:
    ##

    def _read_initial_balances(period: DateRange) -> InitialBalances:
        """
        Reads and returns initial balances.
        """
        return {Account("Foo"): Balance(period.since, Quantity(Decimal("4.00"))), Account("Bar"): Balance(period.since, Quantity(Decimal("-5.25")))}

    ##
    ## Read journal entries:
    ##

    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        """
        Reads and returns journal entries.
        """

# Generated at 2022-06-14 04:24:51.421232
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, JournalEntry
    from .accounting import Account

    account = Account(number = "X", name = "X for testing")
    journal = Journal('R')

    ledger = Ledger(account, initial=Balance(datetime.date(2019,1,1),Quantity(Decimal(0))))

    entry = JournalEntry(date = datetime.date(2019,1,1), description = "X journal entry",
                         journal = journal, is_complete = True)
    posting1 = Posting(account, entry, amount = Decimal("10000"), direction = "D")
    posting2 = Posting(account, entry, amount = Decimal("-10000"), direction = "C")
    entry.add_postings(posting1, posting2)

    ledger.add(posting1)
    assert ledger.account == account
   

# Generated at 2022-06-14 04:24:52.140479
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__(): ...


# Generated at 2022-06-14 04:25:04.302810
# Unit test for method add of class Ledger
def test_Ledger_add():
    new_posting = Posting(None,None,Quantity(Decimal(2.00)))
    new_ledger = Ledger(Account("test"),Balance(datetime.date(2019,9,10),Quantity(Decimal(0.00))))
    new_entry = new_ledger.add(new_posting)
    assert new_entry.balance == Quantity(Decimal(2.00))

# Generated at 2022-06-14 04:25:11.496421
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    period = DateRange(datetime.date(2017, 1, 1), datetime.date(2017, 1, 31))
    initial = {
        Account("051", "CASH BRANCHES"),
        Account("052", "BANK ACCOUNTS"),
        Account("053", "LOAN AND ADVANCES"),
    }
    journal = [
        JournalEntry(
            datetime.date(2017, 1, 1),
            "JOURNAL POSTING ENTRY",
            [
                Posting(Account("051", "CASH BRANCHES"), Decimal("100"), 1),
                Posting(Account("052", "BANK ACCOUNTS"), Decimal("-100"), -1),
            ],
        )
    ]


# Generated at 2022-06-14 04:25:12.216705
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:25:23.572504
# Unit test for method add of class Ledger
def test_Ledger_add():
    # When I have a ledger
    ledger = Ledger(Account("1234"), Balance(datetime.date(2020, 1, 1), Quantity(1456)))

    # When I add a posting
    posting = Posting(
        datetime.date(2020, 1, 4),
        Journal("Description", [Posting(datetime.date(2020, 1, 3), Account("1234"), Quantity(1), None)]),
        Account("1234"),
        Quantity(1),
        None
    )
    ledger_entry = ledger.add(posting)

    # Then the ledger entry is correct
    assert ledger_entry.date == datetime.date(2020, 1, 4)
    assert ledger_entry.description == "Description"



# Generated at 2022-06-14 04:25:32.403850
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import Account
    from .commons.zeitgeist import DateRange
    from .journaling import JournalEntry, Posting

    def _read_initial_balances(period: DateRange) -> InitialBalances:
        from .accounts import Account, AccountType
        from .generic import Balance

        return {
            Account("Account #1", AccountType.LIABILITY): Balance(period.since, Quantity(Decimal("1"))),
            Account("Account #2", AccountType.ASSET): Balance(period.since, Quantity(Decimal("2"))),
            Account("Account #3", AccountType.INCOME): Balance(period.since, Quantity(Decimal("3"))),
            Account("Account #4", AccountType.EXPENSE): Balance(period.since, Quantity(Decimal("4"))),
        }


# Generated at 2022-06-14 04:25:33.825604
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:25:45.318314
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Unit tests: method add of class Ledger
    """
    entry1 = JournalEntry(datetime.date(2020, 2, 20), '12', [Posting(Account('111'), Decimal(100))])
    entry2 = JournalEntry(datetime.date(2020, 2, 20), '21', [Posting(Account('111'), Decimal(100))])
    entry3 = JournalEntry(datetime.date(2020, 2, 20), '34', [Posting(Account('111'), Decimal(100))])

    balance = Balance(datetime.date(2020, 2, 19), Decimal(200))
    l1 = Ledger(Account('111'), balance)

    l1.add(entry1.postings[0])
    assert l1.initial.value == Decimal(200)


# Generated at 2022-06-14 04:25:58.294960
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from bookkeeper.model.accounts import AccountType
    from bookkeeper.model.accounts.test.test_accounts import test_Account

    def _algebra(period : 'DateRange') -> 'InitialBalances':
        return {
            test_Account('12345', AccountType.EXPENSE, 'Rent Expense',): Balance(date(2019,12,1), Quantity(23456)),
            test_Account('54321', AccountType.ASSET, 'Bank Account RBC (CAD)',): Balance(date(2019,12,1), Quantity(34567))
        }


# Generated at 2022-06-14 04:26:08.187222
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():

    from unittest.mock import Mock

    ReadInitialBalancesProxy = Mock(spec=ReadInitialBalances)
    ReadJournalEntriesProxy = Mock(spec=ReadJournalEntries)

    _ = compile_general_ledger_program(ReadInitialBalancesProxy, ReadJournalEntriesProxy)

    ReadInitialBalancesProxy.assert_not_called()
    ReadJournalEntriesProxy.assert_not_called()

    program = _(DateRange(since=datetime.date(2018, 1, 1), until=datetime.date(2018, 9, 30)))

    ReadInitialBalancesProxy.assert_called_once()
    ReadJournalEntriesProxy.assert_called_once()

# Generated at 2022-06-14 04:26:19.701562
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import compile_journal_entry_program
    from .posting.algebra import compile_posting_program
    from .accounts import AccountCode

    ## Define the initial balnce on this date:
    initial_balances = {
        AccountCode("1100"): Balance(datetime.date(2019, 7, 1), Quantity(Decimal(50))),
        AccountCode("1900"): Balance(datetime.date(2019, 7, 1), Quantity(Decimal(150))),
        AccountCode("1300"): Balance(datetime.date(2019, 7, 1), Quantity(Decimal(0))),
    }

    ## Define program to read initial balances:
    read_initial_balances = lambda period: initial_balances

    ## Define the journal entry:
    journal_entry1 = compile_journal_entry_

# Generated at 2022-06-14 04:26:44.280612
# Unit test for function build_general_ledger
def test_build_general_ledger():
    A = Account("A", "Cash in hand", [], 10)
    B = Account("B", "Bank current account", [], 20)
    C = Account("C", "Sales", [], 30)
    D = Account("D", "Salaries", [], 40)
    E = Account("E", "Income tax", [], 50)
    F = Account("F", "Cost of goods sold", [], 60)

    j1 = JournalEntry(datetime.date(2020, 1, 1), "Cash from customer", [Posting(A, Amount(100), True)])
    j2 = JournalEntry(datetime.date(2020, 1, 2), "Supplier invoice", [Posting(C, Amount(200), True)])

# Generated at 2022-06-14 04:26:55.311724
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .accounts import Account
    from .generic import Unit, Balance

    initial = {
        Account("A", "Cash"): Balance(datetime.date(2020, 1, 1), Quantity(Decimal(100))),
        Account("B", "Bank"): Balance(datetime.date(2020, 1, 1), Quantity(Decimal(200))),
    }


# Generated at 2022-06-14 04:27:06.926680
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():

    from .accounts import AccountGroup
    from .journaling import Journal, JournalDate, PostingDirection
    from .processing import build_accounting_period
    from .books import build_general_journal

    print(compile_general_ledger_program(None, None))
    # <function compile_general_ledger_program.<locals>._program at 0x7f5d8e8210a0>

    # Define a read initial balances algebra implementation:

# Generated at 2022-06-14 04:27:18.947561
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from src.accounting.journaling import Posting
    from src.accounting.accounts import AssetAccount as Asset
    from src.accounting.accounts import LiabilityAccount as Liability

    ## Initial balances:
    initial = {Asset.Cash: Balance(datetime.date(2019, 12, 31), Quantity(Decimal(100))),
               Asset.BillsReceivable: Balance(datetime.date(2019, 12, 31), Quantity(Decimal(50))),
               Liability.AccountsPayable: Balance(datetime.date(2019, 12, 31), Quantity(Decimal(50)))}

    ## Journal entries:
    january = datetime.date(2020, 1, 1)
    february = datetime.date(2020, 2, 1)
    march = datetime.date(2020, 3, 1)


# Generated at 2022-06-14 04:27:26.824732
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..fiscalbook.journaling import JournalEntry, Posting

    initial_balances = {}
    period = DateRange(datetime.date(2016, 12, 31), datetime.date(2017, 11, 30))
    journal: Iterable[JournalEntry] = []

    # Verifies general ledger is build from the input info
    ledger = build_general_ledger(period, journal, initial_balances)
    assert ledger is not None
    assert ledger.__dict__ != {}
    assert ledger.ledgers == {}
    assert ledger.ledgers.__class__.__name__ == "dict"
    assert ledger.period.__dict__ != {}
    assert ledger.period.__class__.__name__ == "DateRange"
    assert ledger.period.since == datetime.date(2016, 12, 31)
    assert ledger.period

# Generated at 2022-06-14 04:27:38.212743
# Unit test for function build_general_ledger
def test_build_general_ledger():
    
    from datetime import date, datetime, timedelta
    from decimal import Decimal
    import pytest
    from ..commons.objects import timeseries
    
    from ..accounts import Account, AccountSystem
    from ..journaling import JournalEntry, Posting, PostingSystem
    from ..commons.units import AmountUnit
    from ..commons.types import Date, Description, Price
    from ..commons.numbers import Quantity, Amount

    # Defines datetime with timezones
    today = date.today()
    period = DateRange(
    Date(date(today.year, today.month, 1)), Date(date(today.year, today.month, 30)))

    ## Define a minimal accounting system:
    # My account system is defined using sequence of tuples ('id', 'name'):

# Generated at 2022-06-14 04:27:49.760125
# Unit test for method add of class Ledger
def test_Ledger_add():
    from . import accounts
    from .journaling import JournalEntry, Posting
    from .commons import Direction, Reference
    from datetime import date
    account = accounts.Account.get_account()
    ledger = Ledger(account, Balance(date(1901,1,1),100))
    je = JournalEntry(date(1901,1,1),"test")
    posting = Posting(je, account, Direction.Debit, Reference.get_reference(), Amount(1))
    ledger.add(posting)
    assert ledger.entries[0].amount == ledger.entries[0].debit
    assert ledger.entries[0].balance == 101



# Generated at 2022-06-14 04:27:55.803428
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class MockReadInitialBalances(ReadInitialBalances):
        #: Stubbed results.
        initial_balances: InitialBalances

        def __call__(self, period: DateRange) -> InitialBalances:
            return self.initial_balances

    read_initial_balances = MockReadInitialBalances({})
    assert read_initial_balances({}) == {}


# Generated at 2022-06-14 04:28:06.447975
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    This function serves as unit test for function
    :py:func:`compile_general_ledger_program`.
    """
    from ..fakes import Constant, FakePeriod
    from ..fakes.fake_journal import FakeJournal
    from ..fakes.fake_initial_balances import FakeInitialBalances
    from ..fakes.fake_program_logger import FakeProgramLogger

    ## TODO: Write an actual unit test
    assert compile_general_ledger_program(
        FakeInitialBalances(Constant({"0000": Balance(FakePeriod, 1)}), FakeProgramLogger()),
        FakeJournal(Constant([FakeJournal(date=FakePeriod)])),
    )(FakePeriod)

# Generated at 2022-06-14 04:28:17.724970
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import io
    import unittest

    from datetime import date
    from reporting.commons.accounts import (
        Account,
        AccountType,
    )
    from reporting.commons.zeitgeist import DateRange
    from reporting.gl.gl_accounts import Accounts
    from reporting.journaling.journaling import Journal, JournalEntry, JournalType, Posting
    from reporting.gl.gl_initial import build_initial_gl

    # Helper functions
    def generate_journal(account, amount):
        return Journal(
            date=date(2019,12,5),
            type=JournalType.MANUAL,
            description='Manual journal',
            postings=[
                Posting(account, 1, amount),
                Posting(Accounts.CASH, 0, amount)
            ]
        )


# Generated at 2022-06-14 04:28:35.131750
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from datetime import date, timedelta
    from typing import cast
    from decimal import Decimal
    from pytest import raises

    from ..commons import zeitgeist
    from ..domain.accounting.accounts import LedgerAccount
    from ..domain.accounting.journaling import JournalEntry
    from ..domain.accounting.journaling import Posting
    from ..domain.accounting.journaling import PostingDirection
    from .accounts import Account
    from .accounts import CurrencyAccount
    from .accounts import MoneyAccount
    from .accounts import build_account
    from .accounts import build_ledger_account
    from .accounts import build_money_account
    from .accounting import InitialBalances
    from .generic import Balance
    from .generic import BalanceSheet
    from .generic import IncomeStatement

# Generated at 2022-06-14 04:28:35.815589
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:28:36.965082
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:28:44.600867
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram.
    """

    ## Build and execute the program:
    period = DateRange(datetime.date(2020, 6, 1), datetime.date(2020, 6, 15))

# Generated at 2022-06-14 04:28:57.678993
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from decimal import Decimal
    from ..commons.numbers import Amount
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountType
    from .journaling import JournalEntry, Posting, PostingDirection

    # Setup

    period = DateRange(date(1992, 1, 1), date(1992, 12, 31))
    initial = {
        "000": Balance(date(1991, 12, 31), Quantity(Decimal("1000"))),
        "010": Balance(date(1991, 12, 31), Quantity(Decimal("800"))),
    }

# Generated at 2022-06-14 04:29:01.754016
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Given the stub
    stub_return_value = {}

    # When I invoke the protocol method
    stub_result = ReadInitialBalances.__call__(lambda period: stub_return_value, any)

    # Then I expect the returned result to match the stub return value
    assert stub_result is stub_return_value


# Generated at 2022-06-14 04:29:03.033765
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:29:05.358238
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    assert compile_general_ledger_program(None, None)



# Generated at 2022-06-14 04:29:06.083620
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:29:16.091401
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account("1000", "test_Account", False)
    initial = Balance(datetime.date(2020,1,1), Quantity(0))
    ledger = Ledger(account, initial)
    posting = Posting(Decimal(1), datetime.date(2020,2,2))
    posting.account = account
    posting.journal.postings[0] = posting
    posting.journal.postings[1] = posting
    journal = []
    journal.append(posting.journal)
    ledger.add(posting)
    assert ledger.entries[0].posting.date == datetime.date(2020,2,2)
    assert ledger.entries[0].posting.amount == Decimal(1)
    assert ledger.entries[0].balance == Decimal(1)


# Generated at 2022-06-14 04:29:41.095722
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from dataclasses import dataclass
    from decimal import Decimal
    from .accounts import Account, AccountType
    from .journaling import JournalEntry, Posting, Journal

    @dataclass
    class MyThing:
        pass

    ## Prepare initial balances for accounts with initial balances:
    initial_balances = {
        Account("101", AccountType.ASSET): Balance(date(2000, 1, 1), Quantity(Decimal(1.01))),
        Account("102", AccountType.ASSET): Balance(date(2000, 1, 1), Quantity(Decimal(2.02))),
    }

    ## Prepare journal entries:

# Generated at 2022-06-14 04:29:48.897821
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import accounts
    import journaling
    import transactions
    from ..commons.zeitgeist import Date
    from accounts import Account, TerminalAccount, AccountGroup
    from journaling import JournalEntry, Posting
    from transactions import Money, Equation

    # Prepare initial balances of some accounts:

# Generated at 2022-06-14 04:30:02.294218
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from decimal import Decimal
    from unittest import TestCase

    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from ..journaling import JournalEntry, Posting

    from .accounts import Account
    from .generic import Balance

    # pylint: disable=abstract-method
    class FakeReadInitialBalances(ReadInitialBalances):
        """
        A fake ReadInitialBalances.
        """

        def __call__(self, period: DateRange) -> InitialBalances:
            """
            Returns initial balances.
            """

# Generated at 2022-06-14 04:30:02.724150
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:30:05.334600
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:30:06.552599
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .accounts import Account

    assert False

# Generated at 2022-06-14 04:30:18.357938
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    #: Accounting period.
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))

    #: Initial balances.
    initial_balances = {
        Account("A", "C", "1"): Balance(period.since, Quantity(Decimal(1000)))
    }

    #: Journal entries.

# Generated at 2022-06-14 04:30:25.082311
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram
    """

    import datetime
    from decimal import Decimal
    from ...domain.accounting.accounts import Account
    from ...domain.accounting.journaling import Journal, Posting
    from ...domain.accounting.ledgers import GeneralLedger
    from ...domain.accounting.ledgers import compile_general_ledger_program
    from ...domain.accounting.ledgers import nop_ReadInitialBalances
    from ...domain.accounting.ledgers import nop_ReadJournalEntries
    from ...domain.accounting.lib.journaling import infer_postings

    ## A date we can use in tests:
    date = datetime.date(2019, 12, 31)

    ## Define the `read_initial_balances` algebra implementation:

# Generated at 2022-06-14 04:30:38.472178
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import create_journal_entry, create_posting
    from .test_data import equity, asset, expense, now, today
    from .accounts import AccountDirection

    expense_posting = create_posting(now, expense, 100, AccountDirection.DR)
    revenue_posting = create_posting(now, equity, 100, AccountDirection.CR)
    expense_entry = create_journal_entry([expense_posting, revenue_posting])
    period = DateRange(today, today)
    initial_balances = {expense: Balance(datetime.date(2020, 1, 1), Quantity(0))}

    gen_ledger = build_general_ledger(period, [expense_entry], initial_balances)

# Generated at 2022-06-14 04:30:51.781102
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .accounts import AccountType

    # Data:
    from datetime import date
    from decimal import Decimal
    from ..commons.zeitgeist import DateRange
    from .generic import Balance
    from .accounts import Account

    # Method under test:
    from abcbook.control.accounting.generalledger import ReadInitialBalances

    ## Implementation of the algebra:
    class MyReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account(code="101", type=AccountType.ASSET, desc="Account 101"): Balance(date(2020, 1, 1), Decimal(100))
            }

    ## Method under test:

# Generated at 2022-06-14 04:31:25.407832
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..commons.money import USD
    from ..trial_balance.algebra import ReadTrialBalanceAt
    from ..trial_balance.taxonomy import Account
    from ..trial_balance.trial_balance import TrialBalance
    from .algebra import ReadInitialBalances, ReadLedgerAt, ReadTrialBalanceAt
    from .ledger import GeneralLedgerProgram

    @dataclass
    class MockReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("1000"): Balance(datetime.date(year=2020, month=1, day=1), Quantity(Decimal("10"))),
                Account("2000"): Balance(datetime.date(year=2020, month=1, day=1), Quantity(Decimal("-10"))),
            }

# Generated at 2022-06-14 04:31:37.477604
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..foundation.journaling import JournalEntry, Posting, ReadJournalEntries, journal_entry_post
    from .accounts import Account, AccountCategory

    from ..commons.numbers import Quantity

    import datetime

    aliases = {
        "Opening Balances": Account(1001, AccountCategory.ASSET, "Opening Balances"),
        "Debtors": Account(1011, AccountCategory.ASSET, "Debtors"),
        "Cash at Bank": Account(1002, AccountCategory.ASSET, "Cash at Bank"),
        "Direct Expenses": Account(1210, AccountCategory.EXPENSE, "Direct Expenses"),
        "Sales": Account(4001, AccountCategory.REVENUE, "Sales"),
        "VAT Input": Account(4051, AccountCategory.TAX, "VAT Input"),
    }


# Generated at 2022-06-14 04:31:44.194919
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..core.core import double_entry_book_core
    from datetime import date

    ## Get accounting period:
    period = DateRange(date(2013, 1, 1), date(2013, 12, 31))

    ## Get core implementation of the algebra:
    ReadInitialBalances = double_entry_book_core.ReadInitialBalances

    ## Get the program to compile:
    ReadInitialBalances__call__ = compile_general_ledger_program(ReadInitialBalances, ReadJournalEntries)

    ## Compile the program:
    ReadInitialBalances__call__(period)



# Generated at 2022-06-14 04:31:49.631781
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Unit test for method __call__ of class ReadInitialBalances
    """

    ## Test for open date before since date, as a result, no initial balances are returned.
    assert {} == ReadInitialBalances.__call__(DateRange.__call__(datetime.date(y, m, d), datetime.date(y, m, d)))

# Generated at 2022-06-14 04:32:01.096885
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import unittest

    from .accounts import Account
    from .generic import Balance

    class DummyReadInitialBalances(ReadInitialBalances):
        def __init__(self, balances: InitialBalances):
            self._balances = balances

        def __call__(self, period: DateRange) -> InitialBalances:
            return self._balances

    class ReadInitialBalancesTest(unittest.TestCase):
        def test_happy_path(self):
            period = DateRange(
                since=datetime.date(2019, 1, 1),
                until=datetime.date(2019, 12, 31),
            )

# Generated at 2022-06-14 04:32:12.297952
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import Account

    acct = Account("13", "test", True,  "")
    acct4 = Account("4", "test4", False,  "")
    acct5 = Account("5", "test5", True,  "")
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
    balance = Balance(period.since, Quantity(Decimal(1000)))
    ldgr = Ledger(acct, balance)
    from .journaling import Journal, Posting
    from .journaling import JournalEntry
    from .journaling import PostingDirection as PD
    je1 = JournalEntry(datetime.date(2019, 1, 1), "test", Journal([Posting(acct, PD.Debit, Decimal(100))]))
   

# Generated at 2022-06-14 04:32:25.413120
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .accounts import AccountType
    from .journaling import JournalEntryBuilder
    from .commons.chrono import Date
    from dataclasses import dataclass
    from datetime import date
    from .commons.numbers import Amount
    from .commons.zeitgeist import DateRange
    from .ledgering import build_general_ledger

    # Create an account with a balance
    @dataclass
    class _Account:
        account: str
        balance:  Amount = Amount(100)

    sql = """
    create table accnt(
      accnt character varying(255) NOT NULL,
      bal decimal NOT NULL,
      CONSTRAINT accnt_pkey PRIMARY KEY (accnt)
    )
    """
    db = _Database(sql)


# Generated at 2022-06-14 04:32:34.126378
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..commons.zeitgeist import date
    from .accounts import Account, AccountType
    from .journaling import Journal, Posting, _posting_set

    AccountingPeriod = DateRange
    JournalEntries = List[Journal]

    def test_read_initial_balances(period: AccountingPeriod) -> InitialBalances:
        return {
            Account("checking", AccountType.Asset): Balance(date(period.since.year, period.since.month, 1), 1000),
            Account("savings", AccountType.Asset): Balance(date(period.since.year, period.since.month, 1), 1000),
        }


# Generated at 2022-06-14 04:32:42.654797
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    ## Obtain opening and closing dates:
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 3, 31))

    ## Mock up initial balances algebra implementation:
    initial_balances = {Account("1001"): Balance(period.since, Quantity(1000))}
    def read_initial_balances(pd: DateRange) -> Dict[Account, Balance]:
        assert pd == period
        return initial_balances

    ## Mock up journal entries algebra implementation:
    journal_entries = [
        JournalEntry(
            1, datetime.date(2019, 1, 1), "Debit", [Posting(Account("1001"), Quantity(100), +1)], None
        )
    ]

# Generated at 2022-06-14 04:32:49.991007
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Initializations:
    # - Mock the algebra.
    # - Create a program to test.
    #   - Read initial balances.
    #   - Read journal entries.
    # - Create a dummy accounting period.
    # - Create a dummy opening balance,
    # - Create a dummy journal entry.
    # - Create a dummy general ledger.
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {}

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        pass

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    period = DateRange(datetime.date(2000, 1, 1), datetime.date(2000, 12, 31))