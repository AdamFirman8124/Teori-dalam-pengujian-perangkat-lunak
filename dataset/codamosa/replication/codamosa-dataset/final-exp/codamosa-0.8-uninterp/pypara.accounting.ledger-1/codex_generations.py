

# Generated at 2022-06-14 04:23:53.769422
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests the method __call__ of class GeneralLedgerProgram.
    """

    ## Define initial balances:
    initial_balances = {
        Account(code="10100", title="Cash"): Balance("2019-12-31", Quantity(Decimal("281210.86"))),
        Account(code="10200", title="Cash on hand"): Balance("2019-12-31", Quantity(Decimal("10.86"))),
    }

    def read_initial_balances(daterange: DateRange) -> InitialBalances:
        return initial_balances

    ## Define journal entries for the period:

# Generated at 2022-06-14 04:24:05.438533
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Tests method add of class Ledger
    """
    from .journaling import JournalEntry
    from .accounts import Account, Subledger
    from .commons import units

    #: Create accounts of the posting:
    bank_account = Account(Subledger.BALANCE_SHEET, "Bank account", "1001", "10")
    cash_account = Account(Subledger.BALANCE_SHEET, "Cash", "1002", "10")
    incomes_account = Account(Subledger.PROFIT_AND_LOSS, "Incomes", "2001", "10")

    #: Create journal entry:

# Generated at 2022-06-14 04:24:19.073568
# Unit test for method add of class Ledger
def test_Ledger_add():
    print("Testing method add of class Ledger")
    from ..books import BuildJournalEntry
    from ..books.algebra import build_journal_entry_register_debit, build_journal_entry_register_credit

    test_journal_entry_read_journal_entries = build_journal_entry_register_debit('00001', 'TEST1', '2019-01-01',
                                                                                 '010101', '100', 'TEST1')
    test_journal_entry_read_journal_entries = build_journal_entry_register_credit('00001', 'TEST1', '2019-01-01',
                                                                                 '010101', '100', 'TEST1')
    test_build_journal_entry = BuildJournalEntry(test_journal_entry_read_journal_entries)
    test_

# Generated at 2022-06-14 04:24:33.006567
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import dataclasses
    import unittest

    from dataclasses import dataclass
    from decimal import Decimal
    from datetime import date

    from ..commons.zeitgeist import DateRange

    from ..accounting.accounts import Account
    from ..accounting.journaling import Journal, JournalEntry, Posting

    from ..accounting.ledgers import build_general_ledger
    from ..accounting.ledgers import GeneralLedger, Ledger, LedgerEntry

    @dataclass
    class ReadInitialBalancesMock:
        def __call__(self, period: DateRange) -> Dict[Account, Quantity]:
            return {}


# Generated at 2022-06-14 04:24:39.732534
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    @dataclass
    class TestCtx:
        initial_balances: InitialBalances
        journal_entries: List[JournalEntry[int]]


# Generated at 2022-06-14 04:24:40.527432
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:24:41.264632
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:24:52.753819
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Setups:
    import typing as t
    import pytz
    from anyblok.blok import BlokManager
    from anyblok_pyramid.testing import init_registries
    from anyblok_pyramid.testing import make_test_current_request

    from .accounts import Account
    from .journaling import JournalEntry
    from .ledgering import ReadInitialBalances, build_general_ledger, compile_general_ledger_program

    # Define data for use in unit testing.
    #
    # 1. Journal entry with debit and credit postings:

# Generated at 2022-06-14 04:25:05.940575
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program.
    """

    from .mockups import mock_read_journal_entries, mock_read_initial_balances

    ## Build up the algebra:
    program = compile_general_ledger_program(mock_read_initial_balances, mock_read_journal_entries)

    ## Compute ledger for a period:
    ledger = program(DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 31)))

    ## Check the results:
    assert ledger.period == DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 31))

# Generated at 2022-06-14 04:25:14.810509
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..codex import AccountCodex

    ## Define accounts:
    cash = AccountCodex().account("Cash")
    accounts = AccountCodex().account("Accounts Receivable")

    ## Create a journal entry:
    from ..journaling import Accountant, Journal, Posting

    accountant = Accountant()
    journal = Journal(
        "first journal entry",
        accountant.book(Posting(accounts, 1000)),
        accountant.book(Posting(cash, 1000)),
    )

    ## Create opening balance:
    from .generic import Balance

    opening = {cash: Balance(datetime.date(2020, 1, 1), Quantity(Decimal(0)))} ## date and balance

    ## Build the ledger:
    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 2, 1))
   

# Generated at 2022-06-14 04:25:27.129182
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..commons.algebra import s
    from .journaling import JournalEntry, Posting
    from .accounts import Account

    @dataclass
    class Coil(JournalEntry):
        debit: Account
        credit: Account

    @dataclass
    class InitialBalance:
        account: Account
        balance: Quantity

    class ReadInitialBalances_Impl(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account(self, "revenue"): Balance(period.since, Quantity(100)),
                Account(self, "expenses"): Balance(period.since, Quantity(50)),
            }


# Generated at 2022-06-14 04:25:40.321750
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from datetime import date
    from decimal import Decimal
    from src.examples.accounting.journal.date_range import date_range
    from src.examples.accounting.journal.org_accounts import org_accounts
    from src.examples.accounting.journal.org_journals import org_journals
    from src.examples.accounting.journal.org_postings import org_postings
    from src.examples.accounting.journal.org_entries import org_entries
    from src.examples.accounting.ledger.org_initial_balances import org_initial_balances
    from src.examples.accounting.ledger.org_ledgers import general_ledger_program__org

    # create accounting period:

# Generated at 2022-06-14 04:25:53.593365
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..accounts.domain import AccountDefinition, AccountType
    from .journaling import Journaling
    from .journaling.algebra import build_journal_entry, post_entry
    from .journaling.codecs import TransactionsImporter

    ## Get a journaling API:
    journaling = Journaling(build_journal_entry, post_entry, TransactionsImporter)

    ## Import batch transactions:
    journal_entries = journaling.import_transactions("tests/data/transactions.xlsx")

    ## Initialize initial balances:
    initial_balances = {
        Account("123"): Balance(datetime.date(2019, 1, 1), 100),  # Trial balance, account 123.
        Account("000"): Balance(datetime.date(2019, 1, 1), 200),  # Trial balance, account 000.
    }



# Generated at 2022-06-14 04:25:54.975905
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    raise NotImplementedError()

# Generated at 2022-06-14 04:26:05.575873
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account(str(1), str(1), True)
    posting = Posting(None, None, None, None)
    posting.account = account
    posting.amount = Amount(-1)
    posting.direction = -1
    
    ledger = Ledger(account, None)
    entry = ledger.add(posting)
    assert entry.posting == posting
    assert entry.balance == -1
    assert entry.date == None
    assert entry.description == None
    assert entry.amount == Amount(-1)
    assert entry.cntraccts == []
    assert entry.is_debit == True
    assert entry.is_credit == False
    assert entry.debit == Amount(-1)
    assert entry.credit == None



# Generated at 2022-06-14 04:26:18.363982
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Journal, PostingDirection, Postings
    from .accounts import AccountType, Accounts

    j1 = Journal(
        datetime.date(2019, 1, 1),
        'j1',
        Postings([
            Posting(Accounts.assets.bank, Amount(10), PostingDirection.DEBIT),
            Posting(Accounts.equity.capital, Amount(10), PostingDirection.CREDIT)
        ])
    )
    j2 = Journal(
        datetime.date(2019, 2, 1),
        'j2',
        Postings([
            Posting(Accounts.assets.bank, Amount(10), PostingDirection.CREDIT),
            Posting(Accounts.expenses.taxes, Amount(10), PostingDirection.DEBIT)
        ])
    )

# Generated at 2022-06-14 04:26:31.471794
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    print("Method __call__ of class ReadInitialBalances")
    from dateutil.relativedelta import relativedelta

    today = datetime.date.today()
    period = DateRange(since=today - relativedelta(years=1), until=today)
    
    #Initialization of ReadInitialBalances

# Generated at 2022-06-14 04:26:44.541650
# Unit test for function build_general_ledger
def test_build_general_ledger():
    print("unit test for function build_general_ledger")
    ## Initialization
    accountA = Account("A")
    accountB = Account("B")
    accountC = Account("C")
    accountD = Account("D")
    accountE = Account("E")
    accountF = Account("F")
    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 2))

# Generated at 2022-06-14 04:26:55.535542
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Unit test for method __call__ of class ReadInitialBalances.
    """
    from datetime import date
    from typing import Dict

    from .accounts import Account
    from .generic import Balance
    from .numbers import Amount, Quantity

    from .commons.zeitgeist import DateRange

    def test_program(period: DateRange) -> Dict[Account, Balance]:
        """
        Test program.

        :param period: Accounting period.
        :return: Initial balances.
        """
        assert isinstance(period, DateRange)


# Generated at 2022-06-14 04:27:07.011980
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program.
    """

    ## Prepare mocks:
    import unittest
    import unittest.mock as mock
    mockReadInitialBalances = mock.MagicMock(spec=ReadInitialBalances)
    mockReadJournalEntries = mock.MagicMock(spec=ReadJournalEntries)
    mockBuildGeneralLedger = mock.MagicMock(spec=build_general_ledger)

    ## Execute the function under test:
    generalLedgerProgram = compile_general_ledger_program(
        read_initial_balances=mockReadInitialBalances,
        read_journal_entries=mockReadJournalEntries,
    )

# Generated at 2022-06-14 04:27:22.535262
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import PostingDirection, Debit
    from .accounts import AccountType, Account

    import datetime
    from decimal import Decimal

    # Initialize the account
    account = Account(
        "Assets:Bank:CheckingAccount",
        AccountType.ASSET,
    )

    # Initialize the posting
    posting = Posting(
        datetime.date.today(),
        PostingDirection.DEBIT,
        Decimal("10.0"),
        account,
    )

    # Initialize the ledger
    ledger = Ledger(
        account,
        Decimal("10.0"),
        []
    )

    # Test add method
    posting = ledger.add(posting)
    assert posting.balance == 20

# Generated at 2022-06-14 04:27:23.193938
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:27:36.404247
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests :py:meth:`GeneralLedgerProgram.__call__()`.
    """
    # A: Initial balance of Bank Account at the beginning of the period.
    IBB1 = Decimal("20")

    # B: Opening date of the period.
    B = datetime.date(2018, 11, 1)

    # C: Closing date of the period.
    C = datetime.date(2018, 11, 30)

    # D: Accounting period.
    D = DateRange(B, C)

    # E: Contributed Capital Account.
    E = Account("Contributed Capital", Account.Type.EQUITY)

    # F: Cash Account.
    F = Account("Cash", Account.Type.ASSET)

    # G: Bank Account.
    G = Account("Bank", Account.Type.ASSET)



# Generated at 2022-06-14 04:27:46.983202
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class DataModel:
        def __init__(self, data: dict):
            for k, v in data.items():
                setattr(self, k, v)

    @dataclass
    class MockReadInitialBalances:
        def __init__(self):
            self.balance_data = None

        def __call__(self, period: DateRange) -> InitialBalances:
            if self.balance_data is None:
                raise Exception("TODO")

            return {Account(row.account): Balance(row.date, Quantity(row.balance)) for row in self.balance_data}

    opening_date = datetime.date(2020, 1, 1)
    closing_date = datetime.date(2020, 12, 31)

    # GIVEN a mock of ReadInitialBalances
    mock

# Generated at 2022-06-14 04:27:47.648678
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    ...

# Generated at 2022-06-14 04:27:57.586571
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from datetime import date
    from .algebras import build_read_journal_entries, build_read_initial_balances
    from .ledger_book import LedgerBook, Record
    from .accounts import TerminalAccount, AccountEntity, AssetAccount, LiabilityAccount, ExpensesAccount
    from ..commons.zeitgeist import DateRange

    ## Date range
    period = DateRange(date(2019, 1, 1), date(2019, 12, 31))

    ## Create accounts:
    class Accounts(AccountEntity): pass
    account_1 = TerminalAccount(Accounts, 'acc_1', AssetAccount)
    account_2 = TerminalAccount(Accounts, 'acc_2', LiabilityAccount)
    account_3 = TerminalAccount(Accounts, 'acc_3', AssetAccount)

# Generated at 2022-06-14 04:28:09.711536
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import operator

    import pytest

    from ..commons.zeitgeist import DateRange, Interval
    from .accounts import Account, AccountType
    from .journaling import JournalEntry, Posting, build_journal_entry, of_posting

    @of_posting
    def _posting_of(posting: Posting[str]) -> Posting[str]:
        return posting

    def _journal_entry(**kwargs):
        return build_journal_entry(kwargs)

    #: Example accounting period:
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))

    #: Set of sample terminal accounts:

# Generated at 2022-06-14 04:28:19.171447
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..commons.validation import ValidationError

    # from . import sample_data, sample_ledgers
    from . import sample_ledgers

    ## Provide some initial balances as at end of previous period:
    initial_balances = sample_ledgers.initial_balances_sample

    ## Provide some journal entries:
    journal_entries = sample_ledgers.journal_entries_sample

    ## Compile the general ledger program using given initial balances and journal entries:
    general_ledger_program = compile_general_ledger_program(
        lambda period: initial_balances.setdefault(period, {}),
        lambda period: journal_entries.setdefault(period, []),
    )

    ## Create financial period:
    period = sample_ledgers.period

    ## Execute general ledger program:
    general_ledger = general

# Generated at 2022-06-14 04:28:22.640910
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests the :py:meth:`GeneralLedgerProgram.__call__` method.
    """

    ## Test code:
    ## <<No code -- stub method>>
    pass

# Generated at 2022-06-14 04:28:30.544104
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # A sample implementation:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        balance = Balance(period.since, Quantity(2))
        return {Account("A"): balance}

    # Should return the balance of account "A" as of the end of previous financial period:
    assert read_initial_balances(DateRange(since=datetime.date(2019, 1, 1), until=datetime.date(2019, 12, 31))) == {
        Account("A"): Balance(since=datetime.date(2019, 1, 1), value=Quantity(2))
    }



# Generated at 2022-06-14 04:28:48.459091
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    class JournalEntryProtocol(Protocol):
        """
        Type definition of the protocol for all journal entries.
        """

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    class InitBalanceProtocol(Protocol):
        """
        Type definition of the protocol for reading initial balances.
        """

        def __call__(self, period: DateRange) -> InitialBalances:
            pass


    def test_program(period: DateRange) -> GeneralLedger[_T]:
        ledger: GeneralLedger[_T] = compile_general_ledger_program(
            read_initial_balances=InitBalanceProtocol(),
            read_journal_entries=JournalEntryProtocol(),
        )(period)

        return ledger


    return test_program

# Generated at 2022-06-14 04:28:59.328409
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import pytest
    import clu.ledgers.algebras as algebras

    read_initial_balances = algebras.compile_read_initial_balances(algebras.from_balance_sheet)
    read_journal_entries = algebras.compile_read_journal_entries(algebras.from_journal)
    read_general_ledger = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Printing the `GeneralLedger` instance prints the associated `Ledger` instances:
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(read_general_ledger(DateRange(None, "2018-12-30")))



# Generated at 2022-06-14 04:29:12.548188
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..dummies import reading_journal_entries_of_stock_book
    from .accounts import Accounts
    from .booking import PostingDirection

    ## Initialize accounts:
    accounts = Accounts.dummy()

    ## Get a dummy ledger for the accounts:
    journal_entries = reading_journal_entries_of_stock_book(accounts)

    ## Build the ledger with initial balance:

# Generated at 2022-06-14 04:29:25.116101
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():

    period = DateRange.from_string("2020-01-01/2020-12-31")
    initial_balances = {Account("101"): Balance(datetime.date(2020, 1, 1), Quantity(Decimal("1000"))),}

# Generated at 2022-06-14 04:29:36.879810
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .accounts import Account
    from .commons import Balance
    from .journaling import JournalEntry, Posting, ReadJournalEntries

    # Define a temporary ledger
    ledger: List[JournalEntry[str]] = []

    # Create a procedure for reading journal entries
    def read_journal_entries(period: DateRange):
        for je in ledger:
            yield je

    # Create a temporary general ledger
    def build_gl(period: DateRange, initial_balances: InitialBalances):
        entries = read_journal_entries(period)
        return build_general_ledger(period, entries, initial_balances)

    # Define an empty function
    def read_initial_balances(period: DateRange) -> InitialBalances: ...

    # Get the program

# Generated at 2022-06-14 04:29:46.012918
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ledger.journaling import JournalEntry, Posting, build_journal
    import datetime
    from typing import Iterable
    from ledger.accounts import (
        Account,
        TerminalAccount,
        AssetAccount,
        EquityAccount,
        TerminalEquityAccount,
        LiabilityAccount,
        TerminalLiabilityAccount,
        ExpenseAccount,
        ExpenseAccount,
        IncomeAccount,
        TerminalIncomeAccount,
    )
    from decimal import Decimal
    from ledger.commons.numbers import Quantity

    ## Define some accounts:

    ## Balance sheet accounts:
    capital = TerminalEquityAccount(code="CAP", name="Capital")
    bank = TerminalAssetAccount(code="BANK", name="Bank")
    office = TerminalAssetAccount(code="OFFICE", name="Office")

# Generated at 2022-06-14 04:29:59.499249
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Tests function build_general_ledger
    """
    from ..commons.zeitgeist import Month
    from .accounts import Account, AccountTree
    from .journaling import Journal, Posting

    ## Prepare initial balances:

# Generated at 2022-06-14 04:30:06.041355
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():

    from .accounts import Account
    from .journaling import JournalEntry
    from .journaling.algebra import Post
    from .journaling.algebra import Postings
    from .storage import Memory

    # Initialize a memory backend:
    backend = Memory()

    # Define a read journal entries program:
    read_journal_entries = backend.read_journal_entries

    # Dummy read initial balances program:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {Account("1000"): Balance(period.since, Quantity(Decimal(1000))),}

    # Compile the general ledger building program:
    build_general_ledger = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    # A couple of dates:

# Generated at 2022-06-14 04:30:06.613842
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert False


# Generated at 2022-06-14 04:30:07.008400
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:30:44.267787
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..commons.testutils import TestCase

    from .journaling import ReadJournalEntries
    from .accounts import Account

    class TestReadJournalEntries(ReadJournalEntries[None]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[None]]:
            yield JournalEntry(
                datetime.date(2020, 1, 1), "Transaction 1", [Posting(Account("X"), Amount(10), True)]
            )
            yield JournalEntry(
                datetime.date(2020, 1, 2), "Transaction 2", [Posting(Account("Y"), Amount(100), False)]
            )

# Generated at 2022-06-14 04:30:45.660130
# Unit test for function build_general_ledger
def test_build_general_ledger():
    pass


# Generated at 2022-06-14 04:30:56.589960
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2022-06-14 04:31:08.075291
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():

    # Define a testing read initial balances implementation:
    @dataclass
    class _ReadInitialBalances:
        def __call__(self, period):
            return {
                Account("Account_1"): Balance(period.since, Quantity(Decimal(100))),
                Account("Account_2"): Balance(period.since, Quantity(Decimal(200))),
            }

    # Define a testing read journal entries implementation:

# Generated at 2022-06-14 04:31:16.763430
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Test GeneralLedgerProgram.__call__()
    """
    # Test with valid data
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
    assert period.since == datetime.date(2019, 1, 1)
    assert period.until == datetime.date(2019, 12, 31)
    assert period.duration == 364
    date = datetime.date(2019, 1, 1)
    assert date == datetime.date(2019, 1, 1)
    balance = Balance(datetime.date(2019, 1, 1), Quantity(Decimal(0)))
    assert balance.as_of == datetime.date(2019, 1, 1)
    assert balance.value == Quantity(0)
    initial_balances = Dict[Account, Balance]
   

# Generated at 2022-06-14 04:31:23.077584
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():

    @dataclass
    class GeneralLedgerProgramInstance:
        def __call__(self, date_range: DateRange) -> GeneralLedger[int]:
            pass

    # Assert type:
    assert GeneralLedgerProgram[int].__origin__ == Generic
    assert GeneralLedgerProgram[int].__args__ == (int,)

    # Assert instance:
    assert isinstance(GeneralLedgerProgramInstance(), GeneralLedgerProgram[int])

# Generated at 2022-06-14 04:31:36.319328
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import build_journal_entry
    from .accounts import Account, AccountType

    ## Create some sample accounts:
    a_asset = Account("1000", "Cash", AccountType.ASSET)
    a_revenue = Account("4000", "Sales", AccountType.REVENUE)
    a_expense = Account("5000", "Purchase", AccountType.EXPENSE)
    a_liab = Account("6000", "Credit", AccountType.LIABILITY)
    a_equity = Account("7000", "Capital", AccountType.EQUITY)

    ## Create sample initial balances:

# Generated at 2022-06-14 04:31:43.646107
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    ## Initialize accounting period:
    period = DateRange("2019-01-01", "2019-12-31")

    ## Create a general ledger program:
    program = compile_general_ledger_program(
        read_initial_balances=lambda p: {Account.assets.cash: Balance(p.since, Quantity(10000))},
        read_journal_entries=lambda p: [
            JournalEntry(
                date=datetime.date(2019, 6, 30),
                description="Opening balance",
                postings=[Posting(Account.assets.cash, Direction.DEBIT, Amount(10000))],
            )
        ],
    )

    ## Run general ledger program:
    gl = program(period)

    ## Assert:
    assert gl.period == period
    assert len(gl.ledgers) == 1
    assert gl.led

# Generated at 2022-06-14 04:31:55.475282
# Unit test for method add of class Ledger
def test_Ledger_add():
    from myledger.commons.zeitgeist import DateRange
    from myledger.journaling.journal import Journal
    from myledger.journaling.algebra import ReadJournalEntries
    from myledger.accounts.algebra import Accounts, ReadInitialBalances
    from myledger.accounts.memory import build_accounts
    from myledger.accounts.memory import build_initial_balances
    from myledger.journaling.memory import build_journal_entries

    ledger = Ledger(Account('20180101', 'Utilities'), Balance('20180101', Decimal(0)))
    assert ledger.initial.value == '0.00'
    posting = Posting(Journal('20180102', 'Test Journal Entry'), Account('20180101', 'Utilities'), '20180102', Amount(-100), "Debit")

# Generated at 2022-06-14 04:32:04.752766
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Test the method __call__ of class GeneralLedgerProgram.
    """
    
    # Test name:
    test_name = 'test_GeneralLedgerProgram___call__'
    print('\n{} ::: {}'.format(__file__, test_name))
    
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {}
    
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return []
    
    compiled = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    general_ledger = compiled(DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31)))

# Generated at 2022-06-14 04:33:21.855273
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.journaling import Journal, Posting, Transaction
    from ..commons.numbers import Amount
    from .accounts import Account, AccountType
    from .accounts import NominalAccount, RealAccount
    from .accounts import liability_account, expense_account, revenue_account, asset_account

    ## Create a nominal account
    nacct = NominalAccount("Nominal account", AccountType.INCOME)

    ## Create a real account
    racct = RealAccount("Real account", AccountType.EXPENSE)

    ## Set up the initial balance of the ledger
    ibal = Balance("2018-01-01", 0)

    ## Create a ledger
    ledger = Ledger(nacct,ibal)

    ## Create a posting on the nominal account
    posting = Posting(nacct, Amount(1), None)

   

# Generated at 2022-06-14 04:33:34.496231
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .journaling import JournalEntry, Posting, Balance, Quantity

    @dataclass
    class DummyJournalEntry(JournalEntry):
        def __init__(self, date, value, account1, account2, account3, account4, account5):
            self.date = date
            self.description = ""
            self.postings = [
                Posting(self, account1, value),
                Posting(self, account2, value),
                Posting(self, account3, value),
                Posting(self, account4, value),
                Posting(self, account5, value),
            ]

    period = DateRange(datetime.date(2018, 2, 1), datetime.date(2018, 4, 30))
    period0