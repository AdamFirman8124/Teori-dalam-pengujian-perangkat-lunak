

# Generated at 2022-06-14 04:23:53.976791
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Test for method add of class Ledger.

    It tests if the ledger is updating the value of its balance after method add is called.
    """
    # Initialize a journal entry
    entry_date: datetime.date = datetime.date(2019, 12, 20)
    journal_entry: JournalEntry[_T] = JournalEntry(entry_date, "", "")
    posting: Posting[_T] = Posting(journal_entry, Account(""), Decimal(100), False)

    # Initialize a ledger
    account: Account = posting.account
    initial_balance: Balance = Balance(datetime.date(2019, 1, 1), Decimal(100))
    ledger: Ledger[_T] = Ledger(account, initial_balance)

    # Call method add of ledger, then check if the last balance of the ledger is
    #

# Generated at 2022-06-14 04:24:05.676077
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Verifies that the general ledger is built properly.
    """
    ## Verify

# Generated at 2022-06-14 04:24:19.201874
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..journaling.journaling import build_journal_entries_from_csv, JournalReader

    ## Build a list of journal entries from test CSV file:
    journal_entries = build_journal_entries_from_csv(
        JournalReader(account_mapping='account_mapping.csv', csv_pathname='journal.csv')
    )

    ## Build an initial balance map:
    initial_balances = {
        Account("Assets:Cash:Checking"): Balance(datetime.date(2020, 1, 1), Decimal("1000.00")),
        Account("Liabilities:AccountsPayable"): Balance(datetime.date(2020, 1, 1), Decimal("2000.00")),
    }

    ## Build a general ledger:

# Generated at 2022-06-14 04:24:33.132758
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from decimal import Decimal
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .journaling import Journal, JournalEntry, Posting, post_entry
    from .tellers import Teller
    from .ledgering import build_general_ledger, InitialBalances, Ledger, GeneralLedger
    from .reading import InitialBalancesRead, JournalEntriesRead
    from .datastore import MemoryDataStore
    from .generic import Record, RecordId, WriteRecord

    # Algebra implementations:
    memory_datastore = MemoryDataStore()
    read_initial_balances: InitialBalancesRead = InitialBalancesRead(MemoryDataStore())
    read_journal_entries: JournalEntriesRead[_T] = JournalEnt

# Generated at 2022-06-14 04:24:44.950091
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import unittest
    import doctest
    from .accounts import Account, to_account
    from .generic import Balance
    from .commons.numbers import Quantity
    from .commons.zeitgeist import DateRange
    from .journaling import JournalEntry, Posting, to_journal_entry
    from .accounts import ReadAccounts, to_read_accounts
    from .journaling import ReadJournalEntries, to_read_journal_entries
    from .general_ledger import compile_general_ledger_program, GeneralLedger
    from .accounts import Account
    from .commons.numbers import Quantity


# Generated at 2022-06-14 04:24:46.008821
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:24:52.605626
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Define some test data:
    account = Account("assets", "cash")
    amount = Amount(100_00)
    description = "paycheck"
    date = datetime.date(2020, 2, 1)
    debitaccount = Account("expenses", "salaries")
    creditaccount = Account("assets", "cash")

    ## Create the ledger:
    ledger = Ledger(
        account,
        Balance(date, Quantity(Decimal(0))),
    )

    ## Add the posting:
    journal = JournalEntry(date, description, Posting(debitaccount, amount), Posting(creditaccount, amount))
    posting = Posting(debitaccount, amount)
    entry = ledger.add(posting)

    ## Check the result:
    assert entry.balance == Quantity(100_00)



# Generated at 2022-06-14 04:25:05.792787
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons import zeitgeist
    from .journaling import Journal, Posting, build_journal, Transaction
    from .accounts import AccountSystem
    from .accounts.books import Assets, Liabilities, Revenues, Expenses
    from .accounts.business.suppliers import Suppliers
    from .accounts.business.revenues import Sales

    def build_transaction_1() -> Transaction:
        return Transaction(description="Purchase goods")

    def build_transaction_2() -> Transaction:
        return Transaction(description="Sell goods")

    account_system = AccountSystem()


# Generated at 2022-06-14 04:25:14.785544
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Tests function :py:func:`compile_general_ledger_program`
    """
    from ..commons.dataloading import from_dict
    from ..commons.testing import assert_arg_not_none
    from .accounts import read_accounts
    from .journaling import from_postings
    from .testing.mocks import MockPosting, MockReadJournalEntries
    from .testing.mocks import MockReadJournalEntries, MockReadInitialBalances

    ## Compile the program:
    program = compile_general_ledger_program(from_dict(dict()), MockReadJournalEntries(dict()))

    ## Ensure the program has a correct signature:
    assert_arg_not_none(program, 0, DateRange)

    ## Get the accounts:
    assets, liabilities, equity, revenue, expense

# Generated at 2022-06-14 04:25:25.340273
# Unit test for function build_general_ledger
def test_build_general_ledger():

    import datetime

    from decimal import Decimal

    from ..commons.zeitgeist import DateRange

    from .journaling import JournalEntry, Posting

    from .accounts import Account, AccountType, Group

    from .generic import Amount, Quantity

    from .currencies import Currency, CurrencyUnit

    from .measurements import Unit, UnitMix

    from .numbers import Zero

    from .functors import Functor, Identity

    # Create currency units:
    BRL = CurrencyUnit.create("BRL", Currency.of("Brazilian Real"), Quantity(Decimal(1)))
    USD = CurrencyUnit.create("USD", Currency.of("US Dollar"), Quantity(Decimal(0.38)))
    EUR = CurrencyUnit.create("EUR", Currency.of("Euro"), Quantity(Decimal(0.42)))

    # Create account groups:
    Asset

# Generated at 2022-06-14 04:25:42.388804
# Unit test for function build_general_ledger
def test_build_general_ledger():

    from .journaling import Posting, JournalEntry
    from .accounts import Account, AccountId
    from .accounts import Asset, Liability, Equity
    from .accounts import Revenue, Expense

    print("Testing build_general_ledger...")

    # Dummy Period
    period = DateRange(datetime.date(2019, 10, 1), datetime.date(2019, 10, 31))

    # Dummy Journal Entries

# Generated at 2022-06-14 04:25:56.230630
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Tests whether compiling a program actually returns a proper program.
    """

    ##
    ## Define a simple initial balance reader:
    ##
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {Account("a:b:c:d"): Balance(period.since, Decimal(100))}


    ##
    ## Define a simple journal entry reader:
    ##
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry]:
        yield JournalEntry(
            period.since,
            ["debit", "d:e:f"],
            "Transaction 1",
            [Posting(Amount(10), Account("a:b:c:d")), Posting(Amount(-10), Account("d:e:f"))],
        )

# Generated at 2022-06-14 04:26:06.746735
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.zeitgeist import format_date, now

    # Build sample general ledger entries

# Generated at 2022-06-14 04:26:18.809685
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..books.algebras import ReadJournalEntries
    from ..books.models import JournalEntry
    from ..books.prepare import compile_read_journal_entries_program
    from ..books.types import Journal

    from .models import Transaction
    from .prepare import compile_read_transactions_program

    ## Compile the transaction reader:
    read_transactions = compile_read_transactions_program()

    ## Compile the journal entries reader:
    read_journal_entries = compile_read_journal_entries_program(
        read_transactions, Journal.__root__.__post__
    )

    ## Get journal entries:
    journal_entries = read_journal_entries(DateRange(period=60))

    ## Get the correct general ledger:

# Generated at 2022-06-14 04:26:25.331044
# Unit test for function build_general_ledger
def test_build_general_ledger():
    # ARRANGE
    period = DateRange(since=datetime.date(2000, 1, 1), until=datetime.date(2000, 12, 31))
    journal = []
    initial = {}

    # ACT
    gl = build_general_ledger(period, journal, initial)

    # ASSERT
    assert gl.period == period
    assert gl.ledgers == {}

# Generated at 2022-06-14 04:26:36.700254
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from beancount.core.data import Open, Posting
    from datetime import date
    cashAcnt = Account('Assets:Cash')
    merchantsAcnt = Account('Expenses:Merchants')
    salaryAcnt = Account('Income:Salary')

    ## Journal entry with a single posting:
    je1 = [
        JournalEntry(
            date=date(2014, 12, 27),
            description='Purchase of goods',
            postings=[
                Posting(elem.account, elem.units, elem.cost)
                                 for elem in [
                                     Posting(cashAcnt,
                                             Amount('-100 USD'), None),
                                     Posting(merchantsAcnt,
                                             Amount('100 USD'), None)
                                     ]]
        ),
    ]

    ## Journal entry with two

# Generated at 2022-06-14 04:26:48.253288
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import Account, Named
    from .journaling import JournalEntry, Posting
    from .types import AccountType, BalanceType

    def initial(period: DateRange) -> InitialBalances:
        return {
            Account(Named("0.0.1", "Assets"), AccountType("Current Assets", BalanceType("Dr"))): Balance(
                period.since, Quantity(100)
            ),
            Account(Named("0.0.2", "Stock"), AccountType("Inventories", BalanceType("Dr"))): Balance(
                period.since, Quantity(10)
            ),
            Account(Named("0.1.1", "Equity"), AccountType("Stockholders' Equity", BalanceType("Cr"))): Balance(
                period.since, Quantity(100)
            ),
        }


# Generated at 2022-06-14 04:26:49.449698
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:26:59.581073
# Unit test for method add of class Ledger
def test_Ledger_add():
    dummy_posting = Posting(datetime.date(2012,1,1), datetime.date(2012,1,1), "Journal Entry", "Description", 5, 1, None)
    dummy_ledger = Ledger('accounts_0', initial = Balance(Decimal(7), Decimal(0)))
    dummy_ledger.add(dummy_posting)    
    assert dummy_ledger.initial.value == Decimal(7)
    assert dummy_ledger.account == 'accounts_0'
    assert dummy_ledger.entries[0].balance == Decimal(12)
    assert dummy_ledger.entries[0].date == datetime.date(2012,1,1)
    assert dummy_ledger.entries[0].description == 'Description'

# Generated at 2022-06-14 04:27:08.836083
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Creating test object
    ledger = Ledger(Account(1), Balance(datetime.date(2019,1,1), Quantity(Decimal(0))))
    # Creating Posting
    account = Account(1)
    journal = JournalEntry(datetime.date(2019,1,1), 'test description', 'test source')
    amount = Amount(Decimal(500))
    direction = Posting.DEBIT
    posting = Posting(account, journal, amount, direction)
    # Executing function
    actual_result = ledger.add(posting)
    # Asserting results
    assert actual_result == LedgerEntry(ledger, posting, Quantity(Decimal(500)))

    return 'Unit test for method add of class Ledger completed successfully'


# Generated at 2022-06-14 04:27:27.007777
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from ..commons.zeitgeist import YearRange
    from .accounts import Accounts, Account, AccountType
    from .journaling import Posting, JournalEntry
    from .journaling import _T

    post = Posting[_T]
    journal = JournalEntry[_T]
    ledger = Ledger[_T]
    ledger_entry = LedgerEntry[_T]

    print("Testing model: build_general_ledger")
    ## Define a period:
    period = YearRange(2018)

    ## Create accounts:
    A = Account(AccountType.ASSET, "A")
    B = Account(AccountType.ASSET, "B")
    C = Account(AccountType.ASSET, "C")
    D = Account(AccountType.ASSET, "D")

# Generated at 2022-06-14 04:27:33.473440
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ... import Account, Balance

    account = Account("111")
    ledger = Ledger(account, Balance(0, Decimal(10)))
    posting = Posting(0, account, Decimal(5))

    ledger.add(posting)
    assert ledger.entries[0].balance == Decimal(15)

    ledger.add(posting)
    assert ledger.entries[1].balance == Decimal(20)

# Generated at 2022-06-14 04:27:41.154589
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import io
    import json
    import sys

    # This minimal read_initial_balances works only for testing purposes.

# Generated at 2022-06-14 04:27:52.102587
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..fs import read_initial_balances, read_journal_entries
    from .accounts import Account, AccountCategory
    from .journaling import JournalEntry
    import datetime as d
    # ledger_entry
    def test1():
        # Test add with debit
        entry_date = d.date(2020, 1, 1)
        entry_acc = Account(1, 1, AccountCategory.ASSET, 'Test Account', True)

# Generated at 2022-06-14 04:27:52.844581
# Unit test for function build_general_ledger
def test_build_general_ledger():
    pass

# Generated at 2022-06-14 04:28:04.670330
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..unit_tests.doubles import (
        AccountStub,
        BalanceStub,
        JournalEntryStub,
        PostingStub,
        StringValueStub,
    )
   
    posting1 = PostingStub(
        AccountStub("101", "Cash"),
        StringValueStub("USD", "Currency"),
        Decimal(100),
        Decimal(100),
    )
    posting2 = PostingStub(
        AccountStub("201", "Account receivable"),
        StringValueStub("USD", "Currency"),
        Decimal(100),
        Decimal(100),
    )

# Generated at 2022-06-14 04:28:16.402233
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import Account, Asset, Capital, Liability, Revenue

    from .initial_balances import read_initial_balances

    from .journaling import ReadJournalEntries

    from .posting_rules import ReadPostingRules
    from .read_journals import read_journal_entries
    from .rules import (
        Credit,
        Debit,
        Expense,
        GeneralLedgerRule,
        Income,
        LedgerRule,
        PostingRule,
        read_general_ledger_rules,
        read_ledger_rules,
        read_posting_rules,
    )

    ## Posting rules

# Generated at 2022-06-14 04:28:28.089067
# Unit test for method add of class Ledger
def test_Ledger_add():
    #account = Account.get("410", "123")
    #initial_balance = Balance(datetime.date(2018, 1, 1), Quantity(Decimal(0)))
    #ledger = Ledger(account, initial_balance)
    #debit = Posting(account, datetime.date(2018, 1, 15), Quantity(Decimal(80)), "Test Journal Entry")
    #credit = Posting(account, datetime.date(2018, 1, 16), Quantity(Decimal(80)), "Test Journal Entry")
    #ledger.add(debit)
    #ledger.add(credit)
    #assert ledger.balance.value == 0
    #assert ledger.entries[0].balance.value == 80
    #assert ledger.entries[1].balance.value == 0
    pass

# Generated at 2022-06-14 04:28:28.742624
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    pass

# Generated at 2022-06-14 04:28:36.945024
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .posting_program import Entry, CompileJournalEntryCreation
    from .ledger_program import build_journal, build_ledger, compile_general_ledger_program
    from .commons.zeitgeist import now

    period: DateRange = DateRange(now().date(), now().date())
    entry: Entry = Entry(
        period.since,
        "Description",
        "Cash",
        {"Sales": "Debit", "Sales Tax Payable": "Credit"},
    )
    posting = CompileJournalEntryCreation()(entry)
    journal = build_journal(iter([posting.journal]), period)
    if posting.is_debit:
        initial = dict({posting.account: Balance(period.since, Quantity(Decimal(1000)))})

# Generated at 2022-06-14 04:29:16.563053
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..commons.testing import check_function_return_type

    check_function_return_type(
        compile_general_ledger_program,
        (
            (
                lambda period: {"Initial Balances": period},  # type: ReadInitialBalances
                lambda period: [],  # type: ReadJournalEntries[Dict[str, str]]
            ),
            (
                lambda period: {"Initial Balances": period},  # type: ReadInitialBalances
                lambda period: [],  # type: ReadJournalEntries[Dict[str, str]]
            ),
        ),
        GeneralLedgerProgram[Dict[str, str]],
    )

# Generated at 2022-06-14 04:29:25.970236
# Unit test for method add of class Ledger
def test_Ledger_add():
    class A:
        pass

    a = A()

    class B:
        pass

    b = B()

    class C:
        pass

    c = C()

    class D:
        pass

    d = D()

    class Posting(Posting[A]):
        def __init__(self, date, amount, direction, entity):
            self.date = date
            self.amount = Amount(amount)
            self.direction = direction
            self.entity = entity

        @property
        def journal(self) -> JournalEntry[A]:
            return JournalEntry(self.date, "", [self])

    class LedgerEntry1(LedgerEntry[A]):
        def __init__(self, ledger, posting, balance):
            self.ledger = ledger
            self.posting = posting

# Generated at 2022-06-14 04:29:34.381338
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .algebras.assay import read_initial_balances, read_journal_entries

    glp = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    gl = glp(DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31)))
    assert gl is not None
    assert len(gl.ledgers) > 0
    assert gl.period == DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))

# Generated at 2022-06-14 04:29:44.095289
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import datetime
    from decimal import Decimal
    from dateutil import rrule
    from dateutil.relativedelta import relativedelta
    from math import pi
    from pytz import utc
    import unittest
    import unittest.mock

    from dateutil.tz import tzutc

    from financeager.algebras import make_journal_entry, make_posting
    from financeager.commons.numbers import Amount, Quantity
    from financeager.commons.zeitgeist import DateRange
    from financeager.financial.accounts import Account, AccountType, IncomeStatementAccountType
    from financeager.financial.generic import Balance
    from financeager.financial.journaling import Journal
    from financeager.financial import ledgers
    from financeager.financial import transactions


# Generated at 2022-06-14 04:29:58.219663
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import create_journal_entry
    from .accounts import LedgerAccount, GeneralLedgerAccount
    from datetime import date
    import pytest
    ## Assets account numbers
    cash_account_number = '1010.00'
    accounts_receivable_account_number = '1010.01'
    inventory_account_number = '1010.10'
    ## Liabilities account numbers
    accounts_payable_account_number = '2020.00'
    ## Expenses account numbers
    supplies_expense_account_number = '3000.00'
    direct_labor_account_number = '3100.00'
    manufacturing_overhead_account_number = '3200.00'
    ## Revenues account numbers
    sales_revenue_account_number = '4000.00'
    return_on_

# Generated at 2022-06-14 04:30:05.748846
# Unit test for function build_general_ledger
def test_build_general_ledger():

    from datetime import date
    from typing import TYPE_CHECKING
    from .accounts import Book, BookCode, Nature, Number
    from .journaling import JournalEntry, Posting, Journal

    if TYPE_CHECKING:
        from . import journaling

    ## Define initial balances:

# Generated at 2022-06-14 04:30:17.617344
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..domain.accounts import AccountID
    from ..domain.journaling import (
        Posting,
        PostingDirection,
        PostingTypes,
        JournalEntry,
        JournalID,
    )
    from .accounts import Account

    @dataclass
    class ExampleGeneralLedgerProgram(GeneralLedgerProgram):
        pass

    @dataclass
    class ExampleJournalEntries(ReadJournalEntries):
        pass

    @dataclass
    class ExampleInitialBalances(ReadInitialBalances):
        pass

    example_program = ExampleGeneralLedgerProgram()
    example_journal_entries = ExampleJournalEntries()
    example_initial_balances = ExampleInitialBalances()

    example_period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 2, 1))
   

# Generated at 2022-06-14 04:30:24.230543
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal
    from .accounts import Account
    from .accounts import AccountDirection

    ledger = Ledger(Account("1", AccountDirection.DEBIT), Balance(datetime.datetime.now(), Quantity(Decimal('0.00'))))
    journal = Journal(datetime.datetime.now(), "Entry 1")
    posting = Posting(journal, Account("1", AccountDirection.DEBIT), Amount(Decimal('50.00')), None)
    ledger.add(posting)
    assert ledger.entries[0].balance == Quantity(Decimal('50.00'))

# Generated at 2022-06-14 04:30:37.419830
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram.
    """
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            "Assets:Cash": Balance("2012-01-01", Quantity("1000"))
        }

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry]:
        from .journaling import Journal

        return [
            Journal("2012-01-01", "A", [("Assets:Cash", Quantity("1000"), None)]),
            Journal("2012-01-02", "B", [("Assets:Cash", Quantity("2000"), None)]),
            Journal("2012-01-03", "C", [("Assets:Cash", Quantity("3000"), None)]),
        ]

    ## Build general ledger program:
    program = compile

# Generated at 2022-06-14 04:30:38.100302
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # 
    pass

# Generated at 2022-06-14 04:31:43.928747
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .accounts import Account, Balance
    from .commons.numbers import Amount, Quantity

    @dataclass
    class ReadInitialBalancesMock:
        """
        This object's method __call__ can be used as the parameter read_initial_balances of the function
        compile_general_ledger_program.
        """

        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("100"): Balance(
                    period.since - datetime.timedelta(days=30), Quantity(Amount("100.50"))
                ),
                Account("200"): Balance(
                    period.since - datetime.timedelta(days=30), Quantity(Amount("200.75"))
                ),
            }


# Generated at 2022-06-14 04:31:55.627785
# Unit test for method add of class Ledger
def test_Ledger_add():
    pa = Account(account_id = "123")
    pb = Account(account_id = "12")

# Generated at 2022-06-14 04:32:08.390199
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.zeitgeist import Date
    from .accounts import AccountTree

    ## Define accounting period:
    period = DateRange(Date(2020, 1, 1), Date(2020, 6, 30))

    ## Define an account tree:
    tree = AccountTree()
    tree.add(Account(101))
    tree.add(Account(201, parent=101))
    tree.add(Account(202, parent=101))
    tree.add(Account(301, parent=201))
    tree.add(Account(302, parent=202))

    ## Define initial balances:

# Generated at 2022-06-14 04:32:11.804523
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

ReadInitialBalances.__call__.__annotations__ = {'return': InitialBalances}


# Generated at 2022-06-14 04:32:24.826575
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Testing the add method of Ledger
    #Test data:
    account = Account()
    account.name = "Cash"
    account.account_type = "Asset"
    account.group = "Current Assets"
    account.code = 100
    account.is_terminal = True
    account.description = "Bank account"
    
    date = datetime.date(2020, 1, 2)
    description = "Payment for expenses"
    amount = Decimal(10)
    direction = "Debit"

    posting = Posting(date, account, direction, amount)
    journal_entry = JournalEntry(posting, description)
    
    journal_entries = []
    journal_entries.append(journal_entry)

    period = DateRange(since=date, until=date)

    initial_balances = {}
   

# Generated at 2022-06-14 04:32:25.950155
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:32:31.499418
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class _ReadInitialBalancesImplementation:
        initial: InitialBalances

        def __call__(self, period: DateRange) -> InitialBalances:
            return self.initial

    ## Create a ReadInitialBalances instance:
    read_initial_balances = _ReadInitialBalancesImplementation({})

    ## Testing:
    assert isinstance(read_initial_balances, ReadInitialBalances)



# Generated at 2022-06-14 04:32:42.317423
# Unit test for function build_general_ledger
def test_build_general_ledger():
    initial = {Account("1110"): Balance(datetime.date(2013, 1, 1), Quantity(Decimal("10.5")))}
    program = compile_general_ledger_program(lambda p: initial, lambda p: [])
    gl = program(DateRange(datetime.date(2013, 1, 1), datetime.date(2013, 1, 31)))
    assert "1110" in gl.ledgers
    assert gl.ledgers["1110"].initial.value == Decimal("10.5")
    assert len(gl.ledgers["1110"].entries) == 0
    assert gl.ledgers["1110"].entries == []

# Generated at 2022-06-14 04:32:43.183839
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:32:44.152634
# Unit test for function build_general_ledger