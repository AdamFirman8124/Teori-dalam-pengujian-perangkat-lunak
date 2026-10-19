

# Generated at 2022-06-14 04:23:48.994928
# Unit test for method add of class Ledger
def test_Ledger_add():
    # :Posting of the ledger entry.
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .bookkeeping import Ledger, GeneralLedger, build_general_ledger
    from .journaling import JournalEntry, Posting

    # Date of the Posting 
    date = datetime.date(2019, 2, 1)

    # Set the initial balance of the ledger
    initial = Balance(
        period=DateRange(since=datetime.date(2018, 12, 31), until=datetime.date(2019, 1, 31)),
        value=Quantity(value=Decimal(0))
    )

    # Account to be posted
    account = Account(code="10", name="Addition and Subtraction", parent=None)

    # New Debit Posting

# Generated at 2022-06-14 04:23:56.736853
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .accounts import Assets, Cash, Inventory, Expenses
    from .journaling import Posting
    period = DateRange(since=datetime.date(2016, 1, 1), until=datetime.date(2016, 2, 1))

# Generated at 2022-06-14 04:23:57.379626
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__(): pass


# Generated at 2022-06-14 04:24:09.697421
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from typing import Dict

    from decimal import Decimal

    from pony.orm import db_session
    from pony.orm import set_sql_debug, select

    from stablestudent.commons.dateutils import add_business_days
    from stablestudent.commons.dateutils import to_date
    from stablestudent.resources.base import Resource
    from stablestudent.resources.accounts import Account
    from stablestudent.resources.ledgers import Ledger

    with db_session():
        set_sql_debug(True)

#         ## Delete all ledgers:
#         Ledger.delete(select(l for l in Ledger))
#
#         ## Define a test account:
#         asset_account = Account(
#             name       = 'Test Asset Account',
#             parent     = None,

# Generated at 2022-06-14 04:24:19.599756
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class Mock:
        pass

    ## Create stubs:
    period = DateRange(since=datetime.date(2019, 1, 1), until=datetime.date(2019, 12, 31))
    mock = Mock(return_value={Account("1000"): Balance(date=datetime.date(2019, 1, 1), value=Quantity(Decimal(1000)))})

    ## Execute and assert:
    assert {Account("1000"): Balance(date=datetime.date(2019, 1, 1), value=Quantity(Decimal(1000)))} == mock.__call__(period)


# Generated at 2022-06-14 04:24:33.253076
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .accounts import Assets, Liabilities

    from ..commons.zeitgeist import DateRange

    from .journaling import JournalEntry, Posting, PostingDirections
    from .journaling.algebras import PostToAccount

    ## Prepare a batch of journal entries:
    cash = Assets.Cash()
    debt = Liabilities.AccountsPayable()
    equity = Liabilities.Equity()

    ## Build journal entries:

# Generated at 2022-06-14 04:24:44.962382
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Posting, Journal, Account, JournalEntry, GeneralJournal

    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 3))
    initial_balances = {Account("PnL", "Income"): Balance(period.since, Quantity(1000))}

# Generated at 2022-06-14 04:24:53.976487
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Journal
    from .assets import RetainedEarnings
    from .accounts import GeneralLedgerAccount, post

    asset = GeneralLedgerAccount("1", "Asset")
    liability = GeneralLedgerAccount("2", "Liability")
    loss = GeneralLedgerAccount("4", "Loss")
    equity = GeneralLedgerAccount("7", "Equity")
    revenue = GeneralLedgerAccount("3", "Revenue")
    expense = GeneralLedgerAccount("6", "Expense")
    retained = RetainedEarnings()


# Generated at 2022-06-14 04:25:07.289475
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Builds a general ledger.
    """
    from decimal import Decimal
    from datetime import date
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, ExpenseAccount
    from .journaling import JournalEntry, Posting
    from .accounts import CREDIT, DEBIT
    from .simple import SimpleJournalEntry
    from .ledgering import build_general_ledger

    ## Sample initial balances:
    initial: InitialBalances  = {
        Account("1010"): Balance(date(2020, 7, 1), Quantity(Decimal(1000))),
        Account("4920"): Balance(date(2020, 7, 1), Quantity(Decimal(2000))),
    }

    ## Sample journal entries:

# Generated at 2022-06-14 04:25:15.107441
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program
    """

    ## Define a fake implementation of ReadInitialBalances:
    class FakeReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            ...

    ## Define a fake implementation of ReadJournalEntries:
    class FakeReadJournalEntries:
        def __call__(self, period: DateRange) -> ReadJournalEntries:
            ...

    ## Define a fake implementation of GeneralLedgerProgram
    class FakeGeneralLedgerProgram:
        def __call__(self, period: DateRange) -> GeneralLedger:
            ...

    ## Define a fake implementation of GeneralLedger
    class FakeGeneralLedger:
        def __init__(self, period: DateRange, ledgers: GeneralLedger):
            ...



# Generated at 2022-06-14 04:25:30.697363
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Needed for test
    from ..books.journaling import ReadJournalEntries
    from ..books.accounts import ReadJournalAccounts
    from ..books.accounts import ReadBalanceAccounts
    from ..books.journaling import JournalEntry
    from ..books.journaling import Posting
    from ..books.accounts import Account
    from ..books.accounts import Balance


    # Set up a dummy ledger
    account = Account(number=1, name='Test', category='Test')
    test_ledger = Ledger(account, Balance(datetime.date.today(), Quantity(0)))

    # Test with no postings in the ledger

# Generated at 2022-06-14 04:25:32.401411
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests method __call__ of class GeneralLedgerProgram.
    """
    pass

# Generated at 2022-06-14 04:25:42.837242
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account(1000)
    ledger = Ledger(account, Balance(datetime.date.fromisoformat("2020-01-01"), Quantity(0)))
    posting = Posting(datetime.date.fromisoformat("2020-01-01"), Quantity(1), 0)
    entry = ledger.add(posting)
    assert(entry.posting.date == datetime.date.fromisoformat("2020-01-01"))
    assert(entry.ledger == ledger)
    assert(entry.posting == posting)
    assert(entry.balance == 1)
    assert(entry.date == datetime.date.fromisoformat("2020-01-01"))
    assert(entry.description == "")

if __name__ == "__main__":
    test_Ledger_add()

# Generated at 2022-06-14 04:25:46.577538
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    assert isinstance(
        compile_general_ledger_program(lambda period: {}, lambda period: []),
        GeneralLedgerProgram
    )


# Generated at 2022-06-14 04:25:59.151323
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import innuendo.journaling.algebra as jalgebra
    from innuendo.accounts import AccountFactory
    from innuendo.commons.zeitgeist import DateRange, MonthRange

    ## Set-up the account factory.
    accountfactory = AccountFactory(4)
    account = accountfactory.create_account

    ## Define the account for the local currency.
    EUR = account("EUR", is_currency=True)

    ## Define the accounts for the terminal accounts.
    ASSETS = account("1200", "ASSETS", is_terminal=True)
    LIABILITIES = account("2200", "LIABILITIES", is_terminal=True)
    EQUITY = account("3000", "EQUITY", is_terminal=True)

# Generated at 2022-06-14 04:26:12.201377
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..commons.zeitgeist import  DateRange
    from .journaling import Entry, JournalEntry, Posting
    from .accounts import Account, AccountCategory

    import unittest

    class MyTestCase(unittest.TestCase):

        def test_sanity(self):
            period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 31))

            CA = Account(category = AccountCategory.Assets, number = "1100", name = "Cash on Hand")
            A1 = Account(category = AccountCategory.Assets, number = "1200", name = "Accounts Receivable")
            A2 = Account(category = AccountCategory.Assets, number = "2100", name = "Inventories")

# Generated at 2022-06-14 04:26:22.428391
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from datetime import datetime
    from typing import Dict, Tuple
    from uuid import UUID

    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from ..purchasing.receivables import PurchaseOrderAccount, PurchaseInvoiceAccount
    from ..selling.payables import SalesContractAccount, SalesReceiptAccount
    from ..selling.receivables import SalesInvoiceAccount
    from .accounts import Account, TerminalAccount, AccountCategory
    from .accounting_periods import create_accounting_period
    from .journaling import JournalEntry, Posting, Transaction, TransactionType, RecordTransaction

    from .test_journaling import test_record_transaction
    from .test_accounting_periods import test_create_accounting_period

    ## Define an abstract transaction type

# Generated at 2022-06-14 04:26:30.974208
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.zeitgeist import now,today
    from .accounts import Account, AccountType
    from .journaling import Journal, Posting, Transaction,TransactionDirection
    from .ledgering import build_general_ledger,GeneralLedger,Ledger,LedgerEntry

    # Create journal entries:
    t1 = Transaction(f"Test Transaction 1", now(), [Posting(Account.new("1000",AccountType.ASSET,"Bank Account","USD"),Decimal(100000),""), Posting(Account.new("2000",AccountType.REVENUE,"Sales","USD"),Decimal(-100000),"")])

# Generated at 2022-06-14 04:26:44.444768
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    # dummy version of the algebra implementations:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {Account(acct): Balance(period.since, Quantity(Decimal(1000))) for acct in range(3)}

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return [
            JournalEntry(_T, date, f"je {idx:02d}", [Posting(_T, date, Account(0), Direction.CREDIT, Quantity(Decimal(100)))])
            for idx, date in enumerate(period)
        ]

    # build the program:
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    # run for a datetime range:

# Generated at 2022-06-14 04:26:54.207106
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Test method __call__ of class ReadInitialBalances.
    """
    class StubReadInitialBalances(ReadInitialBalances):
        """
        Stub implementation of type ReadInitialBalances.
        """

        def __call__(self, period: DateRange) -> InitialBalances:
            """
            Stub implementation of type ReadInitialBalances.
            """
            return {}
    stub_read_initial_balances = StubReadInitialBalances()
    stub_result = stub_read_initial_balances(DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31)))
    assert(stub_result == {})


# Generated at 2022-06-14 04:27:22.290251
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..accounting.accounts import AccountId, AccountType
    from ..accounting.journaling import Journal, JournalEntryId, PostingDirection

    # Create accounts:
    a1 = AccountId("A1", AccountType.ASSET, None)
    a2 = AccountId("A2", AccountType.ASSET, None)
    l1 = AccountId("L1", AccountType.LIABILITY, None)
    e1 = AccountId("E1", AccountType.EQUITY, None)
    r1 = AccountId("R1", AccountType.REVENUE, None)
    e2 = AccountId("E2", AccountType.EXPENSE, None)

    debit = PostingDirection.DEBIT
    credit = PostingDirection.CREDIT

    # Create some postings:

# Generated at 2022-06-14 04:27:34.622384
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.numbers import Quantity
    from .accounts import Account, AccountIdentifier
    from .journaling import Journal, Posting
    from .journaling import Direction
    # Add a new entry and verify fields are populated properly
    ledger = Ledger(Account(AccountIdentifier("Test")), Balance(datetime.date(2019, 9, 27), Quantity(0)))
    journal = Journal(datetime.date(2019, 9, 27), "Test")
    posting = Posting(journal, Direction.Debit, Quantity(100))
    entry = ledger.add(posting)
    assert entry.ledger == ledger
    assert entry.posting == posting
    assert entry.balance == 100
    assert entry.balance == ledger._last_balance



# Generated at 2022-06-14 04:27:41.486022
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests the method __call__ of class GeneralLedgerProgram
    """

    # Initialize variables
    period: DateRange = DateRange(since=datetime.date(2020, 4, 1), until=datetime.date(2020, 4, 30))
    journal: Iterable[JournalEntry] = [JournalEntry(date=datetime.date(2020, 4, 1), description='Test', postings=[Posting(account='A', amount=1)])]
    initial: InitialBalances = {'A': Balance(date=datetime.date(2020, 3, 31), value=0)}

    def read_initial_balances(period: DateRange) -> InitialBalances:
        return initial

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry]:
        return journal

    # Compile the general ledger program


# Generated at 2022-06-14 04:27:49.468611
# Unit test for method add of class Ledger
def test_Ledger_add():
    test = Ledger(account = 'Test', initial = Balance(datetime.date(2020,1,1), Decimal('10.00')))
    posting = Posting(account = 'Test', date = datetime.date(2020,1,1), amount = Decimal('2.00'))
    entry = test.add(posting)
    assert entry.balance == Quantity(Decimal('12.00'))
    assert entry.is_debit == True
    assert entry.is_credit == False

# Generated at 2022-06-14 04:27:49.858592
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__(): assert True


# Generated at 2022-06-14 04:27:50.604404
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # TODO: implement
    pass


# Generated at 2022-06-14 04:27:51.533086
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    assert compile_general_ledger_program

# ----------------------------------------------------------------------------------------------------------------------

# Generated at 2022-06-14 04:27:58.842652
# Unit test for method add of class Ledger
def test_Ledger_add():
    #define a fictive journal:
    j = JournalEntry(datetime.date.today(), "test", [Posting("a", Amount(1), "DR"), Posting("b", Amount(1), "CR")])
    
    #define a fictive period
    period = DateRange(j.date, j.date)
    
    #define the Initial balances
    ib = {"a": Balance("2010-01-01", Quantity(0))}

    #build a general ledger
    gl = build_general_ledger(period, [j], ib)
    
    #test the balance of one posting:
    assert gl.ledgers["a"].entries[0].balance == Quantity(1)



# Generated at 2022-06-14 04:28:01.931277
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert read_initial_balances() == {a1: Balance(date(2020, 4, 1), Decimal(0)), a2: Balance(date(2020, 4, 1), Decimal(0))}


# Generated at 2022-06-14 04:28:03.025864
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass


# Generated at 2022-06-14 04:28:36.204175
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, Posting
    from .accounts import Account, AccountKind
    debit_account = Account('120001.01', 'Stock', AccountKind.Asset)
    credit_account = Account('110001.01', 'Cash', AccountKind.Asset)
    amount = 100
    journal = Journal(date = datetime.date(2020, 1, 1), description = 'Test', entries = None)
    posting1 = Posting(journal, debit_account, amount)
    posting2 = Posting(journal, credit_account, -amount)

    ledgers = Ledger(debit_account, Balance(datetime.date(2020, 1, 1), 100))
    return ledgers.add(posting2)

# Generated at 2022-06-14 04:28:36.882027
# Unit test for function build_general_ledger
def test_build_general_ledger():
    pass

# Generated at 2022-06-14 04:28:46.847410
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.zeitgeist import date
    from ..journaling import Assets, Expenses, Liabilities, PaymentTerm, Revenue
    from .balance_sheet import Cash
    from .generic import Journal

    #: Accounting period.
    period = DateRange(date(year=2018, month=10, day=1), date(year=2018, month=10, day=31))

    #: Journal entries.

# Generated at 2022-06-14 04:28:58.799836
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Inputs:
    since = datetime.date(year=2020, month=1, day=1)
    until = datetime.date(year=2020, month=12, day=31)

    initial_balances: InitialBalances = {
        Account(name="Cash", no=10): Balance(since, Quantity(Decimal(10000))),
        Account(name="Accounts Receivable", no=15): Balance(since, Quantity(Decimal(20000))),
        Account(name="Equipment", no=20): Balance(since, Quantity(Decimal(25000))),
        Account(name="Accounts Payable", no=25): Balance(since, Quantity(Decimal(7000))),
    }


# Generated at 2022-06-14 04:29:08.060180
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():

    @dataclass
    class _ReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    @dataclass
    class _ReadJournalEntries:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return []

    program = compile_general_ledger_program(_ReadInitialBalances(), _ReadJournalEntries())
    program(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31)))

# Generated at 2022-06-14 04:29:16.915824
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import Date
    from .accounts import Account, Asset, Expense, Liability, Revenue
    from .journaling import Journal, Posting, Transaction
    from .ledgering import debit, credit
    from ..commons.types import Direction, get_generic_type
    # FIXME: Although this method of finding the generic type is bogus,
    # unfortunately it is the most reliable one that I have right now.
    T = get_generic_type(Ledger, "_T")
    print(T)

    # Test Case 1:
    expense = Expense("Dues payable")
    liability = Liability("Dues")
    debit_entry = Posting(Date(year=2019, month=1, day=1), debit(expense, Quantity(50.00)))

# Generated at 2022-06-14 04:29:29.969258
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from ..journaling.journalbook import (
        Posting,
        JournalEntry,
        build_journal_entry,
    )
    from ..journaling.accounts import Account
    from ..commons.zeitgeist import DateRange
    from ..commons.numbers import Amount

    date1 = date(2020, 1, 30)
    date2 = date(2020, 1, 10)

    journal1 = build_journal_entry(
        date=date1, amount=Amount(100), description="Test 1", debit_account=Account(101), credit_account=Account(102)
    )
    journal2 = build_journal_entry(
        date=date2, amount=Amount(100), description="Test 2", debit_account=Account(101), credit_account=Account(102)
    )

    opening_

# Generated at 2022-06-14 04:29:30.787296
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:29:41.287827
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .algebras import AccountingAlgebra

    ## Create an instance of the algebra.
    algebra = AccountingAlgebra()

    ## Compile the program.
    program = compile_general_ledger_program(algebra.read_initial_balances, algebra.read_journal_entries)

    ## Get opening and closing dates.
    date_since = datetime.date(year=2019, month=10, day=1)
    date_until = datetime.date(year=2019, month=12, day=31)

    ## Create an instance of the final result type.
    result = program(DateRange(date_since, date_until))

    ## Check if the result is as expected.
    assert result is not None
    assert result.ledgers is not None
    assert len(result.ledgers) == 2

# Generated at 2022-06-14 04:29:43.302215
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    The following lists the use cases to be verified by this unit test method:
    | UC ID |   UC Description         |
    """
    pass

# Generated at 2022-06-14 04:30:22.296028
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..commons.algebras import Times
    from ..persistence.inmem import InMemoryRepository
    from ..persistence.times import TimesRepository
    from .journaling import JournalRepository, JournalEntryRepository
    from .accounts import AccountRepository

    ## Prepare test data:
    times = [
        Times(datetime.date(2019, 1, 1), datetime.date(2020, 12, 31)),
        Times(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31)),
        Times(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31)),
    ]


# Generated at 2022-06-14 04:30:35.978446
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import Account

    from .journaling import Journal, Posting

    # first account
    account_1 = Account(account_number=1000, account_alias="Cash", account_type="asset")
    # second account
    account_2 = Account(account_number=2000, account_alias="Accounts Receivable", account_type="asset")
    # third account
    account_3 = Account(account_number=3000, account_alias="Inventory", account_type="asset")
    # fourth account
    account_4 = Account(account_number=4000, account_alias="Accounts Payable", account_type="liability")
    # fifth account
    account_5 = Account(account_number=5000, account_alias="Retained Earnings", account_type="equity")
    # sixth account

# Generated at 2022-06-14 04:30:44.422479
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Test the compile_general_ledger_program function.
    """
    from abc import ABC, abstractmethod
    from decimal import Decimal
    from datetime import date
    from typing import List
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .generic import Balance
    from .journaling import JournalEntry, Posting, Direction
    
    ## Define the algebra's contract:
    class Algebra(ABC):
        """
        Defines an abstract algebra for the program.
        """
        
        @abstractmethod
        def initial_balances(self, period: DateRange) -> Dict[Account, Balance]:
            """
            Returns initial balances for terminal accounts.
            """
            pass
        

# Generated at 2022-06-14 04:30:49.265355
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    _program = compile_general_ledger_program(lambda period: dict(), list)
    
    GeneralLedgerProgram.__call__(_program, DateRange(datetime.date.min, datetime.date.max))


# Generated at 2022-06-14 04:30:57.884276
# Unit test for method add of class Ledger
def test_Ledger_add():
    account1 = Account(1, 1, 'A1', 'C1', True)
    tran1 = Posting(account1, 'DEBIT', 5.33)
    ledger1 = Ledger(account1, tran1)
    account2 = Account(2, 1, 'A2', 'C2')
    tran2 = Posting(account2, 'CREDIT', -10.66)
    ledger = Ledger(account2, tran2)
    entry = ledger.add(tran1)
    assert ledger.account == account2
    assert ledger.initial.value == -10.66
    assert tran2.account == ledger.entries[0].posting.account
    assert tran1.account == ledger.entries[1].posting.account
    assert ledger.entries[0].balance == -10.66

# Generated at 2022-06-14 04:31:07.341550
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, Posting, Transaction
    ledger = Ledger(Account("1000"), Balance(datetime.date(year=2020, month=1, day=1), Decimal(1234)))
    journal = Journal(Transaction(datetime.date(year=2020, month=1, day=1), "Description", [Posting(Account("1000"), Decimal(1234)), Posting(Account("2000"), Decimal(-1234))]))
    posting = journal.postings[0]
    ledger.add(posting)
    assert ledger.entries[0].posting == posting
    assert ledger.entries[0].balance == Decimal(2468)
    assert ledger.entries[0].is_debit
    assert ledger.entries[0].debit == Decimal(1234)

# Generated at 2022-06-14 04:31:20.437587
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.testing import assert_date, assert_dict
    from ..commons.zeitgeist import now, today
    from .accounts import Account, Asset, Expense, Liability, Revenue

    # Create a mock global ledger:
    open_balances = {
        Asset(1010, "Bank Accounts"): Balance(now, Quantity(Decimal(0))),
        Liability(1400, "Bank Loans"): Balance(today, Quantity(Decimal(2000))),
        Revenue(4000, "Sales Revenues"): Balance(now, Quantity(Decimal(0))),
        Expense(6000, "Cash Expenses"): Balance(now, Quantity(Decimal(0))),
    }

    # Define the date range:
    period = DateRange(now, now)

    # Call the mock global ledger to get initial balances


# Generated at 2022-06-14 04:31:28.099790
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Given a general ledger program
    read_initial_balances: ReadInitialBalances = lambda period: {}
    read_journal_entries: ReadJournalEntries = lambda period: []
    general_ledger_program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    # When I call the general ledger program with a period
    period = DateRange(since=datetime.date(2020, 1, 1), until=datetime.date(2020, 1, 31))
    general_ledger = general_ledger_program(period=period)

    # Then the general ledger period should be the one given
    assert general_ledger.period == period

# Generated at 2022-06-14 04:31:32.731136
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    initial_balances = {Account(1): Balance(datetime.date(2020, 1, 1), 0)}

    def test_function(period: DateRange) -> InitialBalances:
        assert period == DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 10))
        return initial_balances

    assert test_function(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 10))) == initial_balances


# Generated at 2022-06-14 04:31:38.368682
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class AccountData:
        balance: Balance

    @dataclass
    class ReadData:
        accounts: Dict[Account, AccountData]

    @dataclass
    class ReadInitialBalances:
        read_data: ReadData

        def __call__(self, period: DateRange) -> InitialBalances:
            return {account: account_data.balance for account, account_data in self.read_data.accounts.items()}

    account_data1: AccountData = AccountData(Balance(datetime.date(2020, 1, 1), Quantity(Decimal(100))))
    account_data2: AccountData = AccountData(Balance(datetime.date(2020, 1, 1), Quantity(Decimal(300))))

# Generated at 2022-06-14 04:32:47.233474
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import Account, Directory
    from .journaling import JournalEntry
    from .journaling import Transaction
    from .journaling import Posting
    from .journaling import ReadJournalEntries
    from .books import InitialBalances, Book

    accounts = Directory()
    equity = accounts.create(101, "Equity", "Equity", "A")
    sales = accounts.create(101, "Sales", "Income / Revenues", "I")
    cash = accounts.create(101, "Cash", "Assets", "A")
    bank = accounts.create(101, "Bank", "Assets", "A")

    ## Initial balances:

# Generated at 2022-06-14 04:33:01.310167
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from decimal import Decimal
    from ..journaling import JournalEntry, Posting, Amount
    from ..currency import Currency
    from ..accounting import account_balance, terminal_account
    from ..commons import Identity

    # Constants:
    GBP = Currency(3, 'GBP', 'Pounds Sterling', Decimal(100), '£')
    DR = Identity(-1, 'DR', 'Debit')
    CR = Identity(1, 'CR', 'Credit')

    # Utility function for creating accounts:
    def _acc(cc: str, cv: str='', an: str = '', t: bool = False)->Account:
        """
        Creates a new account.
        """

# Generated at 2022-06-14 04:33:14.324612
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..journaling import build_journal_entry
    from ..accounts import AccountNode

    ## Build a test account tree:
    root = AccountNode(0, "root")
    root.add(1, "assets")
    root.add(1000, "cash")
    root.add(2000, "receivables")
    root.add(10, "liabilities")
    root.add(20, "equity")

    ## Build a test journal entry:
    journal = build_journal_entry(
        (datetime.date(2014, 1, 1), "cash"),
        "NaN",
        [(root.assets.cash, 100), (root.equity.income, -100)],
    )

    ## Build a test general ledger:

# Generated at 2022-06-14 04:33:22.687433
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .journaling import GeneralJournal
    from .accounts import AccountClass

    # Define test data:
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))
    initial_balances = {Account("11101", AccountClass.assets, "Cash"): Balance(period.since, 100),
                        Account("11102", AccountClass.assets, "Accounts receivable"): Balance(period.since, 1000),
                        Account("11103", AccountClass.assets, "Inventory"): Balance(period.since, 10),
                        Account("21101", AccountClass.liabilities, "Accounts payable"): Balance(period.since, 500),
                        Account("31102", AccountClass.equity, "Retained earnings"): Balance(period.since, 0)}

# Generated at 2022-06-14 04:33:35.773036
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import build_journal_entry

    # Prepare: