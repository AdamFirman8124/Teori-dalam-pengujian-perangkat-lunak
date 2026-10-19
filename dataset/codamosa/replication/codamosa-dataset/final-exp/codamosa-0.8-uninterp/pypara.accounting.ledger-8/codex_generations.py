

# Generated at 2022-06-14 04:23:47.115384
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Posting
    account_a = Account.of_name('a')
    account_b = Account.of_name('b')
    
    # Ledger
    ledger_a = Ledger(account_a, Balance(123, 45))
    ledger_b = Ledger(account_b, Balance(123, 45))
    
    # Journal Entry
    account_c = Account.of_name('c')
    journal_entry_1 = JournalEntry(postings=[Posting(account_a, 1, 'a', 'b', cntraccts=[(account_c, 'a')]), Posting(account_b, 1, 'a', 'b', cntraccts=[(account_c, 'a')])], description='a')

# Generated at 2022-06-14 04:23:56.203894
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .journaling import compute_balance, read_journal_entries

    # Function to read initial balances:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account.of("Assets", "Cash"): Balance(period.since, Quantity(Decimal(100))),
            Account.of("Equity", "Capital"): Balance(period.since, Quantity(Decimal(0))),
        }

    # Function to post a journal entry:
    def add_journal_entry(program: GeneralLedgerProgram[_T], journal_entry: JournalEntry[_T], balance: Quantity = None):
        """
        Adds a journal entry to the general ledger.
        """
        # Compute the individual account balances of the journal entry as per balance:

# Generated at 2022-06-14 04:24:08.199537
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests method __call__ of class GeneralLedgerProgram.
    """
    from ..commons.zeitgeist import date_range
    from .journaling import JournalEntry, Posting, journal_entry, posting
    from .ledgering import build_general_ledger

    ## Define a reference general ledger program which builds a general ledger with two ledgers.
    ## The first one is an account with a debit balance.
    ## The second one is an account with a credit balance.

# Generated at 2022-06-14 04:24:20.356110
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():

    #: Mocked initial balances.
    initial_balances = {
        "ASSETS-CASH": Balance(datetime.date(2020, 1, 1), Quantity(Decimal(10000))),
        "ASSETS-INVENTORY": Balance(datetime.date(2020, 1, 1), Quantity(Decimal(33000))),
        "LIABILITIES-PAYABLES": Balance(datetime.date(2020, 1, 1), Quantity(Decimal(9000))),
    }

    #: Mock implementation of ReadInitialBalances.
    class _ReadInitialBalances:
        def __call__(self, period: DateRange) -> Dict[Account, Balance]:
            return initial_balances

    #: Make a call and check the results

# Generated at 2022-06-14 04:24:33.126739
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from . import test_support, accounts

    ##
    ## Fixtures
    ##
    @dataclass
    class _ReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return test_support.get_test_initial_balances()

    ##
    ## Test cases
    ##
    def test_initial_balances_correct():
        actual = _ReadInitialBalances()(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31)))
        expected = test_support.get_test_initial_balances()
        assert actual == expected

    ## Test !
    test_initial_balances_correct()


# Generated at 2022-06-14 04:24:44.951701
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.zeitgeist import DateRange
    @dataclass
    class Date(Generic[_T]):
        """
        This class describes a date.
        """

        #: Day of the date.
        day: int

        #: Month of the date.
        month: int

        #: Year of the date.
        year: int

        date = property(lambda self: datetime.date(self.year, self.month, self.day))

    @dataclass
    class Account(Generic[_T]):
        """
        This class describes an account.
        """

        #: Account type.
        account_type: str

        #: Account number.
        account_number: str

        #: Account name.
        account_name: str


# Generated at 2022-06-14 04:24:52.085821
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Posting, Journal, JournalEntry
    from .accounts import Account, AccountType, AccountGroup
    from .book import Book
    from .order import Order
    from .generic import Balance
    from .trades import Execution, Trade
    from datetime import date

    # Initialize test variables
    stock = Order.from_buy(AccountType.ASSET, 10)
    trade = Trade(10, stock, Execution(date(2020, 1, 1), 10, 10, 5, 0.75))
    book = Book()
    book.add(trade)
    initial = InitialBalances({Account("Cash"): Balance(date(2020, 1, 1), Quantity(Decimal(100)))})

# Generated at 2022-06-14 04:25:01.455282
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import pytest
    from dataclasses import dataclass
    import warnings
    import uuid
    from datetime import date, datetime
    from decimal import Decimal
    from typing import List
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import AccountData, Account
    from .journaling import JournalEntry, Posting, ReadJournalEntries, InMemoryJournalStorage

    # Define a program algebra
    @dataclass
    class ProgramAlgebra:
        read_initial_balances: ReadInitialBalances
        read_journal_entries: ReadJournalEntries[JournalEntry]

    @dataclass
    class Program:
        period: DateRange
        algebra: ProgramAlgebra

    # Define a program algebra implementation

# Generated at 2022-06-14 04:25:04.066457
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # This function is not used explicitly in the code. But, the test is included here to check that the
    # type of __call__ method of the protocol class is correct.
    expected_output = {}
    assert __call__(None) == expected_output


# Generated at 2022-06-14 04:25:11.412522
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.zeitgeist import DateRange
    import datetime as dt
    import json
    from .accounts import Account
    from .journaling import Journal, Posting

    # Prepare a general ledger program
    gl_program = compile_general_ledger_program(
        read_initial_balances = lambda period: {Account("1001"): Balance(period.since, Quantity(0))},
        read_journal_entries = lambda period: [Journal.from_data(json.loads(
            """
            {
                "date": "2019-01-02",
                "description": "Journal entry #1",
                "postings": [
                    { "account": "1001", "amount": 100 },
                    { "account": "1002", "amount": -100 }
                ]
            }
            """))]
    )



# Generated at 2022-06-14 04:25:18.023139
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    return None


# Generated at 2022-06-14 04:25:26.658543
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal
    from .accounts import Account
    from .generic import Direction, Debit, Credit

    ## Define test data:
    description = "test journal entry description"
    journal = Journal(description,
                      [Posting(Account("A"), Debit.instance(), Amount(0.1)), Posting(Account("B"), Credit.instance(), Amount(0.1))])

    ## Create the ledger and add ledger entry:
    ledger = Ledger(Account("A"), Balance(datetime.date(2020, 1, 1), Quantity(0)))
    entry = ledger.add(journal.postings[0])

    ## Test the ledger entry:
    assert entry.posting == journal.postings[0]
    assert entry.ledger == ledger
    assert entry.posting == journal.postings[0]
    assert entry.amount

# Generated at 2022-06-14 04:25:40.118659
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.test_utils import decode
    from .books import BooksSpec
    from .journaling import ReadJournalEntries, GeneralJournal
    from .accounts import AccountClass, AccountCode

    class MyReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account(AccountClass.ASSET, AccountCode("1001")): Balance(period.since, Amount(Decimal(1000.0))),
                Account(AccountClass.ASSET, AccountCode("1002")): Balance(period.since, Amount(Decimal(2000.0))),
            }


# Generated at 2022-06-14 04:25:53.204754
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, Posting, JournalEntry
    from .accounts import Account, AccountType

    period = DateRange(datetime.date(2019,1,1), datetime.date(2019,12,31))
    journal = Journal('Test journal 1')
    journal_2 = Journal('Test journal 2')
    journal_3 = Journal('Test journal 3')
    account_1 = Account(name='Test account', type=AccountType.ASSET)
    account_2 = Account(name='Test account 2', type=AccountType.ASSET)
    account_3 = Account(name='Test account 3', type=AccountType.ASSET)
    posting = Posting(journal, account_1, datetime.date(2019,1,1), Decimal(0))

# Generated at 2022-06-14 04:26:04.565163
# Unit test for method add of class Ledger
def test_Ledger_add():
    import datetime
    from dataclasses import dataclass, field
    from decimal import Decimal
    from typing import Dict, List, Optional

    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .generic import Balance
    from .journaling import JournalEntry, Posting, ReadJournalEntries
    import unittest

    @dataclass
    class LedgerEntry(Generic[_T]):
        """
        Provides a ledger entry model.
        """

        #: Ledger the entry belongs to.
        ledger: "Ledger[_T]"

        #: Posting of the ledger entry.
        posting: Posting[_T]

        #: Balance of the ledger entry.
        balance: Quantity


# Generated at 2022-06-14 04:26:11.909682
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Defines a test case for method add of class Ledger.
    """
    from .accounts import Account as _Account

    ## Number of accounts:
    n = 3

    ## All accounts:
    accounts = [_Account(f"A{x}", f"Account {x}") for x in range(n)]

    ## Opening balances:
    balances = [Balance(datetime.date(2020, 1, 1), Quantity(10)) for _ in range(n)]

    ## Entries:
    entries = [
        [
            Posting(accounts[x], datetime.date(2020, 1, x + 1), Quantity(x + 1 if x else 0))
            for x in range(n)
        ]
    ]

    ## Expected balances:

# Generated at 2022-06-14 04:26:22.223623
# Unit test for method add of class Ledger
def test_Ledger_add():
    from dataclasses import dataclass
    from datetime import date
    from decimal import Decimal
    from typing import Generic, TypeVar
    from ..commons.numbers import Amount, Quantity
    from ..journaling.journaling import JournalEntry, Posting
    from .accounts import Account
    from .journaling import ReadJournalEntries
    from .generic import Balance


    # Test
    @dataclass
    class TestContext:
        """
        Test context.
        """

        #: Account ledger to test.
        account: Account = Account("41100", "Client A/C")

        #: Initial balance of the account ledger.
        initial: Balance = Balance(date(2019, 1, 1), Quantity("10000"))

        #: Test journal entry.

# Generated at 2022-06-14 04:26:30.803387
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Setup:
    from micronumerics.monetary import Money

    @dataclass
    class Mock:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("110030"): Balance(period.since, Money("10")),
                Account("505020"): Balance(period.since, Money("20")),
                Account("505030"): Balance(period.since, Money("30")),
            }

    # Exercise & Verify:
    instance = Mock()

# Generated at 2022-06-14 04:26:44.287430
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .accounts import Account
    from .journaling import Journal

    # Setup:
    account_cash = Account(124, "Cash")
    account_income = Account(400, "Income")
    account_expenses = Account(420, "Expenses")
    account_balance = Account(300, "Balance")

    journal1 = Journal(
        date=datetime.date(2018, 1, 15),
        description="Quarterly dividend",
        postings=[
            Posting(account_balance, 1000.00, direction=1),
            Posting(account_cash, 1000.00, direction=-1),
        ],
    )


# Generated at 2022-06-14 04:26:47.269158
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram
    """
    assert False
    pass

# Generated at 2022-06-14 04:27:09.031263
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..journaling.algebra import ReadJournalEntries
    import datetime
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from ..journaling.models import JournalEntry

    #: Reading journal entries:
    def read_journals(period: DateRange) -> Iterable[JournalEntry]:
        from .accounts import Account


# Generated at 2022-06-14 04:27:20.255662
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from math import isclose
    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))
    assets = Account('Assets')
    assets_nc = Account('Assets, non-current')
    assets_ca = Account('Assets, cash at bank')
    assets_tc = Account('Assets, temporary cash')
    liabilities = Account('Liabilities')
    l_opex = Account('Liabilities, operating expenses')
    e = Account('Expenses')
    e_opex = Account('Expenses, operating')
    e_opex_int = Account('Expenses, operating, interest')
    e_opex_tax = Account('Expenses, operating, tax')
    r = Account('Revenues')
    r_sales = Account('Revenues, sales')
    eq

# Generated at 2022-06-14 04:27:33.532459
# Unit test for method add of class Ledger
def test_Ledger_add():

    class TestJournal(JournalEntry):
        def __init__(self, date, description, posting):
            super().__init__(date, description, posting)

    class TestPosting(Posting):
        def __init__(self, date, account, amount, direction):
            super().__init__(date, account, amount, direction)

    TestAccount = Account("TestAccount")
    TestAmount = Amount(Decimal("100.00"))

    TestPeriod = DateRange(
        datetime.date(2019, 1, 1), datetime.date(2019, 1, 2)
    )

    TestLedger = Ledger(TestAccount, Balance(TestPeriod.since, Quantity(Decimal("0"))))


# Generated at 2022-06-14 04:27:39.798027
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    print("test_ReadInitialBalances___call__")
    @dataclass
    class ReadInitialBalances_Impl(ReadInitialBalances):
        def __call__(self, period: DateRange):
            return InitialBalances()

    test_read_initial_balances = ReadInitialBalances_Impl()
    initial_balances = test_read_initial_balances(DateRange(datetime.date(2020, 5, 1), datetime.date(2020, 5, 31)))
    assert initial_balances ==  {}
test_ReadInitialBalances___call__()


# Generated at 2022-06-14 04:27:53.014714
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import pytest
    from collections import Counter
    from dataclasses import asdict
    from decimal import Decimal
    from itertools import chain
    from .accounts import AccountType
    from .journaling import JournalEntry, Posting

    @dataclass
    class DummyInitialBalances(ReadInitialBalances):
        end_of_previous_period_balances: InitialBalances

        def __call__(self, period: DateRange):
            return self.end_of_previous_period_balances

    @dataclass
    class DummyJournalEntries(ReadJournalEntries):
        postings: List[Posting]


# Generated at 2022-06-14 04:27:54.107485
# Unit test for method add of class Ledger
def test_Ledger_add():
    pass

# Generated at 2022-06-14 04:28:04.542890
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    #### ∀ period, ∃ gl ∈ GeneralLedger:
    ####  read_initial_balances(period) ∪ read_journal_entries(period) ⟶ build_general_ledger(period, ...) = gl
    from persistence.testing import read_journal_entries
    from persistence.testing import read_initial_balances

    ## Build general ledger program:
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Run and check for the first period:
    gl = program(DateRange(datetime.date(2018, 6, 1), datetime.date(2018, 6, 30)))
    assert len(gl.ledgers) > 50



# Generated at 2022-06-14 04:28:16.036885
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from decimal import Decimal
    from pytest import approx
    import datetime
    from ..entities.journaling import Journal
    from ..entities.accounts import (
        Account,
        Assets,
        Equity,
        Expenses,
        Income,
        Liabilities,
        Revenues,
    )
    from . import read_initial_balances, read_journal_entries
    from .generic import Balance
    from .journaling import conns, entries, journals
    from .generic.util import Empty
    from .generic.access import Access
    from .accounts import account_repr, account_str
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))

# Generated at 2022-06-14 04:28:16.921391
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:28:28.853788
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import ledger
    import ledgersimple
    import datetime
    from decimal import Decimal
    import random

    accounts = ledgersimple.core.accounts.makeAccounts()
    accounts.add(ledgersimple.core.accounts.JournalAccount("JOURNAL"))
    accounts.add(ledgersimple.core.accounts.AssetsAccount("ASSETS"))
    accounts.add(ledgersimple.core.accounts.LiabilitiesAccount("LIABILITIES"))
    accounts.add(ledgersimple.core.accounts.StockholdersEquityAccount("STOCKHOLDERS EQUITY"))
    accounts.add(ledgersimple.core.accounts.RevenuesAccount("REVENUES"))
    accounts.add(ledgersimple.core.accounts.ExpensesAccount("EXPENSES"))
    accounts.add

# Generated at 2022-06-14 04:28:55.454734
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.zeitgeist import today

    from .accounts import Account
    from .accounts.programs import compile_accounts_program
    from .accounts.models import AccountClass, AccountType

    from .generic import Balance

    ## Let's compile an accounts program:
    accounts_program = compile_accounts_program()

    ## Let's add some accounts:
    acc1 = accounts_program.add_account("ACC 1", AccountType.ASSET, AccountClass.CURRENT_ASSET)
    acc2 = accounts_program.add_account("ACC 2", AccountType.ASSET, AccountClass.CURRENT_ASSET)

    ## Let's open a balance for acc1:
    accounts_program.open_balance(acc1, Balance(today, Quantity(Decimal(123))))

    ## Let's open another balance for acc1:


# Generated at 2022-06-14 04:29:00.125911
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert hasattr(ReadInitialBalances, '__call__')
    assert callable(ReadInitialBalances.__call__)
    assert len(tuple(signature(ReadInitialBalances.__call__).parameters)) == 2
    assert tuple(signature(ReadInitialBalances.__call__).parameters)[0] == 'self'
    assert tuple(signature(ReadInitialBalances.__call__).parameters)[1] == 'period'

test_ReadInitialBalances___call__()


# Generated at 2022-06-14 04:29:13.205663
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    def read_initial_balances(period: DateRange):
        assert period == DateRange(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31))
        return {}
    def read_journal_entries(period: DateRange):
        assert period == DateRange(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31))
        return []
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    general_ledger = program(DateRange(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31)))
    assert general_ledger == GeneralLedger(DateRange(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31)), {})
#

# Generated at 2022-06-14 04:29:13.876508
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:29:14.989780
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:29:27.706889
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .accounts import Group, RootAccount
    from .journaling import build_journal_entry
    from .nomenclature import Classification, ClassificationType
    from .transactions import build_transaction

    ## Setup schema:
    root = RootAccount()
    assets = root.add("Assets", Group.Asset)
    equity = root.add("Equity", Group.Equity)
    revenue = equity.add("Revenue", Group.Revenue)

    ## Initial balance on account Assets.
    initial_balance = Balance(datetime.date(2020, 1, 1), Quantity(Decimal("943.51")))

    class DummyInitialBalancesReader:
        """
        Dummy for algebra's ReadInitialBalances type.
        """


# Generated at 2022-06-14 04:29:39.029035
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from decimal import Decimal
    from ..commons.bankers import Amount
    from ..commons.numbers import Quantity
    from ..commons.zeitgeist import DateRange
    from ..models.accounts import Account, BasicAccount
    from ..models.journaling import JournalEntry, Transaction

    general_ledger = build_general_ledger(DateRange(date(2018, 10, 1), date(2018, 10, 31)), [], {})
    assert len(general_ledger.ledgers) == 0


# Generated at 2022-06-14 04:29:47.402517
# Unit test for method add of class Ledger
def test_Ledger_add():
    class dummy:
        def __init__(self, amount, type):
            self.amount = amount
            self.direction = type

        def __add__(self, a):
            return self.amount + a.amount

        def __mul__(self, a):
            return self.amount * a.value

    entry1 = Ledger(1, Balance(1, Quantity(Decimal(0))))
    entry2 = Ledger(2, Balance(2, Quantity(Decimal(0))))
    entry3 = Ledger(3, Balance(3, Quantity(Decimal(0))))
    entry4 = Ledger(4, Balance(4, Quantity(Decimal(0))))
    entry5 = Ledger(5, Balance(5, Quantity(Decimal(0))))

# Generated at 2022-06-14 04:30:01.559043
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import datetime
    from decimal import Decimal
    from fractions import Fraction

    from ..accounts import AccountingPeriod, Account, AccountId, AccountType
    from ..commons.locators import locate
    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import find_balance, read_open_accounts, read_periodic_accounts, read_terminal_accounts
    from .journaling import JournalEntry
    from .ledgers import compile_general_ledger_program

    # Define testcase data:
    ledger_date = datetime.date
    ledger_amount = Amount

    cash = Account(AccountId("A0001"), "Cash")
    sales = Account(AccountId("A0002"), "Sales")

# Generated at 2022-06-14 04:30:14.873751
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import datetime as date
    Period = date.datetime(2020, 1, 1)
    Period2 = date.datetime(2020, 2, 1)
    Period3 = date.datetime(2021, 5, 1)

    from .accounts import AssetAccount, ExpenseAccount, IncomeAccount, LiabilityAccount
    from .journaling import Journal, Posting, journal

    liquidity = AssetAccount(1, "Cash")
    assets = AssetAccount(2, "Bank")
    income = IncomeAccount(3, "Income")
    inventory = AssetAccount(4, "Inventory")
    cost = ExpenseAccount(6, "Costs")
    salary = ExpenseAccount(7, "Salary")
    liabilities = LiabilityAccount(8, "Debt")

    j1 = Journal(1, "Zaalhuur")
    p1

# Generated at 2022-06-14 04:30:57.155022
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from typing import NamedTuple
    from ..commons.zeitgeist import Date
    from .accounts import Account, AccountType
    
    class M(NamedTuple):
        accounts: Dict[Account, Balance]

    m = M({
        Account(AccountType.ASSET, '1'): Balance(Date(2020, 1, 1), Quantity(10)),
        Account(AccountType.ASSET, '2'): Balance(Date(2020, 1, 1), Quantity(20)),
        Account(AccountType.ASSET, '3'): Balance(Date(2020, 1, 1), Quantity(30)),
    })

    assert m.accounts(DateRange(Date(2020, 1, 1), Date(2020, 1, 1))) == m.accounts



# Generated at 2022-06-14 04:31:01.855697
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert (
        dataclasses.asdict(ReadInitialBalances.__call__(ReadInitialBalances, DateRange(datetime.date(2020, 6, 1),
                                                                                        datetime.date(2020, 6, 30))))
        == {}
    )


# Generated at 2022-06-14 04:31:10.997221
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from dataclasses import dataclass
    from datetime import date
    from decimal import Decimal
    from typing import Dict, List, Set

    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .generic import Balance
    from .journaling import JournalEntry, Posting

    @dataclass
    class A(Account):
        name: str
        parent: "A" = None

    @dataclass
    class JE(JournalEntry):
        description: str
        postings: Set[Posting]

    a = A("a")
    b = A("b", parent=a)
    c = A("c", parent=a)
    d = A("d", parent=c)
    e = A("e", parent=c)

# Generated at 2022-06-14 04:31:12.204718
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:31:13.610345
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass


# Generated at 2022-06-14 04:31:24.167349
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from typing import Mapping, Sequence

    import datetime

    from dataclasses import dataclass

    from decimal import Decimal

    from pytest import raises

    from szurubooru.test.dummy_context import DummyContext

    from ..commons.numbers import Amount, Quantity

    from .accounts import Account

    from .generic import Balance

    from .journaling import JournalEntry, Posting

    from .ledgers import ReadInitialBalances, build_general_ledger

    from .transactions import Transaction

    from ..test.factories import (
        create_account,
        create_balance,
        create_journal,
        create_journal_entry,
        create_posting,
    )

    @dataclass
    class Foo(Transaction):
        """
        Dummy transaction.
        """

        pass

   

# Generated at 2022-06-14 04:31:36.827507
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from datetime import date

    from ..commons.test_utils import do_test_behave_as_closure
    from ..commons.zeitgeist import DateRange
    from ..domain.journaling import LedgerID, JournalEntry
    from ..domain.ledgering import Account, Balance
    from ..domain.ledgering.accounts import AccountType, AccountCategory

    ## Read initial balances:

# Generated at 2022-06-14 04:31:43.851425
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # arrange
    from . import GenericAccount
    from .journaling import JournalEntry, Posting, ReadJournalEntries

    GeneralLedgerProgram = compile_general_ledger_program(
        lambda range: {Account("assets:asset:account"): Balance(range.since, Decimal(1))},
        lambda range: [JournalEntry(range.since, "", [Posting(Account("assets:asset:account"), range.since, Amount(1), "debit")], "")],
    )

    program = GeneralLedgerProgram(DateRange(since=datetime.date(2019, 1, 1), until=datetime.date(2019, 2, 1)))

    # act
    ledger = program(DateRange(since=datetime.date(2019, 1, 1), until=datetime.date(2019, 2, 1)))

    # assert

# Generated at 2022-06-14 04:31:45.066874
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert False, "Not implemented"


# Generated at 2022-06-14 04:31:55.711255
# Unit test for method add of class Ledger
def test_Ledger_add():
    my_journal = JournalEntry([Posting(Account(1), datetime.date(2019, 1, 1), Quantity(Decimal(100)))])
    my_journal_entries = [my_journal]
    my_initial = {}
    my_period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 1))
    my_ledger = build_general_ledger(my_period, my_journal_entries, my_initial).ledgers[Account(1)]
    my_ledger_size = len(my_ledger.entries)
    my_ledger.add(my_journal.postings[0])
    assert len(my_ledger.entries) == my_ledger_size + 1

# Generated at 2022-06-14 04:33:37.079299
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from decimal import Decimal
    from datetime import date

    from ..commons.zeitgeist import DateRange

    @dataclass
    class DummyReadInitialBalances:
        balance: Dict[str, int]

        def __call__(self, period: DateRange):
            return {key: Balance(date(2020, 5, 1), Quantity(Decimal(value))) for (key, value) in self.balance.items()}

    balance = {'a': Decimal(1), 'b': Decimal(2), 'c': Decimal(3)}
