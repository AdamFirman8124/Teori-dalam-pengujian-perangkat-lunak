

# Generated at 2022-06-14 04:23:55.913939
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import Journal, Posting
    from .accounts import Account, AccountType
    from .commons.zeitgeist import DateRange

    import datetime

    # A program which reads journal entries for a given period, as would be defined in the infrastructure layer.

# Generated at 2022-06-14 04:24:04.975284
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    "ReadInitialBalances.__call__"
    from .accounts import Account

    from .journaling import Journal
    from .. import seed_accounts

    from .accounting import Posting

    accts = seed_accounts(3)
    journal = Journal("Test Journal")
    journal.post(Posting(accts[0], Amount(123), "TestPosting"))

    ReadInitialBalances = ReadInitialBalances

    IniBalances: InitialBalances = {}

    result = ReadInitialBalances.__call__(IniBalances)

    assert isinstance(result, InitialBalances)

# Generated at 2022-06-14 04:24:18.806000
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    ## Define a test journal entry:
    dummy_journal_entry = JournalEntry(postings=[])

    ## Define a test implementation of the function read_journal_entries
    def read_journal_entries(period):
        return [dummy_journal_entry]

    ## Define a test implementation of the function read_initial_balances
    def read_initial_balances(period):
        return {Account("foo"): Balance("bar", Quantity("1"))}

    ## Define an empty accounting period
    period = DateRange("0", "1")

    ## Define a GeneralLedgerProgram
    general_ledger_program = compile_general_ledger_program(
        read_initial_balances, read_journal_entries
    )

    ## Call the method __call__ of GeneralLedgerProgram

# Generated at 2022-06-14 04:24:26.306494
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Test case for adding a new entry to a ledger.
    """
    # Import needed modules
    from .accounts import Account
    from .journaling import Journal, Posting
    from .ledgers import Ledger, LedgerEntry

    # Set journal date
    date_journal = datetime.date(2019, 3, 17)

    # Set new ledger
    ledger = Ledger(
        account=Account(number="6050", name="Cash"), initial=Balance(date_journal, 0)
    )

    # Set new posting
    posting = Posting(is_debit=False, amount=100, account=Account(number="6050", name="Cash"))
    posting.journal = Journal(date_journal, "Test Journal")

    # Add new ledger entry
    ledger_entry = ledger.add(posting)

    # Test ledger balance

# Generated at 2022-06-14 04:24:35.331881
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import AccountType
    from .journaling import Journal

    Assets = AccountType("assets")
    Expenses = AccountType("expenses")

    checking = Account("Checking", Assets, None)
    ledger = Ledger(checking, Balance(Decimal(0)))
    journal = Journal("January 1, 2020", "Monthly paycheck", [Posting(checking, Decimal(3000), 1)])
    entry = ledger.add(journal.postings[0])

    assert entry.date == datetime.date(2020, 1, 1)
    assert entry.posting.account.name == "Checking"
    assert entry.amount == Decimal(3000)
    assert entry.is_debit == True
    assert entry.is_credit == False
    assert entry.balance == Decimal(3000)



# Generated at 2022-06-14 04:24:46.696459
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program.
    """

    from ..commons.algebra import (
        compose,
        consumer,
        filter,
        read_from_dict,
        stable_sorting,
        traverse,
        lambda_,
    )
    from ..commons.identity import identity
    from ..commons.zeitgeist import today
    from .accounts import (
        Account,
        AccountBranch,
        AccountType,
        StandardAccountGroup,
        SubAccountType,
    )
    from .journaling import JournalEntry

    ## Define a sample publication date of journal entries:
    date = today()

    ## Define a filter function:

# Generated at 2022-06-14 04:24:52.932096
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function compile_general_ledger_program.
    """
    # pylint: disable=unsupported-assignment-operation

    @dataclass
    class _MockReadJournalEntries(Generic[_T]):

        @staticmethod
        def __call__(period: DateRange) -> Iterable[JournalEntry]:
            return []

    @dataclass
    class _MockReadInitialBalances:

        @staticmethod
        def __call__(period: DateRange) -> Dict[Account, Balance]:
            return {}

    program = compile_general_ledger_program(_MockReadInitialBalances(), _MockReadJournalEntries())

    assert isinstance(program, GeneralLedgerProgram)


# Generated at 2022-06-14 04:25:06.160529
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from decimal import Decimal
    from decimal import ROUND_HALF_UP
    from ..commons.numbers import Quantity

    @dataclass
    class GeneralLedger:
        #: Accounting period.
        period: DateRange

        #: Individual account ledgers of the general ledger.
        ledgers: Dict[Account, Ledger[_T]]
        balance: Quantity

    @dataclass
    class Ledger:
        #: Account of the ledger.
        account: Account

        #: Initial balance of the ledger.
        initial: Balance

        #: Ledger entries.
        entries: List[LedgerEntry[_T]] = field(default_factory=list, init=False)
        balance: Quantity


# Generated at 2022-06-14 04:25:07.566491
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
  pass


# Generated at 2022-06-14 04:25:13.623089
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from unittest.mock import sentinel
    from ..commons.zeitgeist import DateRange

    program = compile_general_ledger_program(
        lambda p: sentinel.initial_balances,
        lambda p: sentinel.journal_entries,
    )

    general_ledger = program(DateRange(sentinel.since, sentinel.until))
    assert general_ledger.period == DateRange(sentinel.since, sentinel.until)
    assert general_ledger.ledgers == sentinel.ledgers

# Generated at 2022-06-14 04:25:26.145305
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Journal
    from .accounts import Account

    from datetime import date

    j = Journal(
        date(2000, 1, 1),
        "Test",
        [
            Posting(Account.get("10001"), Amount(100)),
            Posting(Account.get("10002"), Amount(-100)),
        ],
    )

    j2 = Journal(
        date(2000, 1, 1),
        "Test",
        [
            Posting(Account.get("10001"), Amount(100)),
            Posting(Account.get("10002"), Amount(-100)),
        ],
    )


# Generated at 2022-06-14 04:25:39.678622
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..contrib.accounts.types import Account

    ## Source data:
    a = Account(code="000", name="Cash")
    b = Account(code="100", name="Receivables")
    c = Account(code="200", name="Payables")
    foobar = Ledger(account=a, initial=Balance(date=datetime.date(2018, 1, 1), value=Decimal(100)))
    e1 = LedgerEntry(ledger=foobar, posting=Posting(account=b, amount=Decimal(50), direction=1), balance=Decimal(150))
    e2 = LedgerEntry(ledger=foobar, posting=Posting(account=c, amount=Decimal(60), direction=-1), balance=Decimal(90))

    ## Add two entries:

# Generated at 2022-06-14 04:25:46.885792
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Test Data
    posting1 = Posting(
        1,
        10,
        'F','A',
        datetime.date.today(),
    )
    entry1 = LedgerEntry(
        0,
        posting1,
        10,
    )
    x = Ledger(
        1,
        Balance(
            datetime.date.today(),
            20,
        ),
    )
    ## Test
    x.add(posting1)
    ## Assertion
    assert x.entries == [entry1]
    assert x.entries[0].posting == posting1
    assert x.entries[0].balance == 20


# Generated at 2022-06-14 04:25:59.310726
# Unit test for function build_general_ledger
def test_build_general_ledger():
    # Initialization
    p1 = Posting("A", Quantity("100"))
    p2 = Posting("B", Quantity("-100"))

    j1 = JournalEntry("1", datetime.date(2015, 1, 1), p1, p2)

    entries = [j1]

    period = DateRange(datetime.date(2015, 1, 1), datetime.date(2015, 1, 30))

    initial = {}

    # Execution
    result = build_general_ledger(period, entries, initial)

    # Verification
    assert result.ledgers.keys() == {"A", "B"}
    assert result.ledgers["A"].entries[0].balance == Quantity("100")
    assert result.ledgers["B"].entries[0].balance == Quantity("-100")

    # Cleanup - none necessary



# Generated at 2022-06-14 04:26:04.341306
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from apel.utils import R
    from ..commons.zeitgeist import DateRange

    class MockReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            raise NotImplementedError

    R(MockReadInitialBalances())

# Generated at 2022-06-14 04:26:17.519371
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit tests for function compile_general_ledger_program
    """

    from .accounts import DirectedAccount, select_debit, select_credit
    from .journaling import Posting, Journal, JournalEntry
    from .monads import Monad

    from ..commons.functional import identity

    ## Define sample abstract algebra implementations:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {}

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        ## Define a sample journal entry
        posting = Posting("Description", DirectedAccount("Sample account"), Decimal("42.24"), datetime.date.today())
        journal = Journal("Sample journal", posting, [posting])

        ## Return the journal entry
        return [journal]

   

# Generated at 2022-06-14 04:26:29.926005
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .journaling import compile_journal_program
    from .journaling.in_memory import InMemoryJournalEntries
    from .accounts import Account, AccountType
    from .accounts.in_memory import InMemoryAccounts
    from .accounts.types import in_memory_account_types
    from .commons.zeitgeist import Date, DateRange
    general_ledger_program = compile_general_ledger_program(in_memory_account_types, compile_journal_program(InMemoryJournalEntries()))
    accounts = InMemoryAccounts()
    account = Account('101', 'A', 0, balance_validity_range=DateRange(from_date=Date(2018, 10, 20)))
    accounts.add(account)

# Generated at 2022-06-14 04:26:31.905521
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Tests the `compile_general_ledger_program` function.
    """
    pass

# Generated at 2022-06-14 04:26:41.102747
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .journaling import compile_journaling_program
    from .accounts import compile_accounting_program

    read_journal_entries = compile_journaling_program()
    read_initial_balances = compile_accounting_program()

    _program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))

    assert _program(period) is not None

# Generated at 2022-06-14 04:26:50.101434
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.zeitgeist import today
    test_data = [
        (
            [
                JournalEntry(today(), [
                    Posting("EQ", "1,000.00 CR", account="120"),
                    Posting("EQ", "1,000.00 DR", account="100")
                ])
            ],
            {"120": Balance(today(), Quantity(1000))}
        ),
    ]
    for journal, initial in test_data:
        l = build_general_ledger(
            period=DateRange(today(), today()),
            journal=journal,
            initial=initial)
        assert len(l.ledgers) == len(initial) + 1
        for ledger in l.ledgers.values():
            if ledger.account == "120":
                assert ledger.initial.value == -1000

# Generated at 2022-06-14 04:27:07.384627
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account(
        code="1101",
        name="Cash on Hand",
        kind="asset",
        type="current",
        category="liquid",
        terminal=True,
    )
    ledger = Ledger(account,Balance(Decimal(1000)))
    posting = Posting(direction=1,account=account,amount=Decimal(1000),journal = JournalEntry(date=datetime.date(2020,1,15),description="Cash on Hand"))
    entry = ledger.add(posting)
    assert entry.posting.account == account
    assert entry.posting.direction == 1
    assert entry.posting.amount == Decimal(1000)


# Generated at 2022-06-14 04:27:17.500463
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import get_journal_entries, post_journal_entry
    from .accounts import Account, AccountCategory
    from .accounts.algebra import get_accounts_by_category
    from .commons.zeitgeist import DateRange
    period = DateRange(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31))
    account_list = get_accounts_by_category(AccountCategory.Asset)
    account_list_1 = get_accounts_by_category(AccountCategory.Liability)
    account_list_2 = get_accounts_by_category(AccountCategory.Equity)
    account_list_3 = get_accounts_by_category(AccountCategory.Income)

# Generated at 2022-06-14 04:27:19.222723
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    import doctest
    from decimal import Decimal

    doctest.testmod()

# Generated at 2022-06-14 04:27:26.942915
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from . import Integer
    from .journaling import build_program

    # Define the accounting period:
    period = DateRange(datetime.date(2030, 1, 1), datetime.date(2030, 12, 31))

    # Define an initial balance:
    initial_balances = {
        Account("Assets:Current:Cash"): Balance(datetime.date(2029, 12, 31), Quantity(Decimal("10000"))),
    }

    # Define journal entries:

# Generated at 2022-06-14 04:27:38.133015
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    # pylint: disable=R0201
    class TestAlgebra:

        def __init__(self, initial_balances, journal_entries):
            self._initial_balances = initial_balances
            self._journal_entries = journal_entries

        def get_initial_balances(self, period):
            return self._initial_balances[period]

        def get_journal_entries(self, period):
            return self._journal_entries[period]

    #: Accounts:
    accounts = map(Account, (("A",), ("B",), ("C",), ("D",), ("E",), ("F",), ("G",), ("H",)))

    #: Concepts:

# Generated at 2022-06-14 04:27:51.763092
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Given a general ledger;
    general_ledger = GeneralLedger(
        period=DateRange.of(datetime.date(2018, 9, 1), datetime.date(2018, 9, 30)),
        ledgers={
            Account.of("a-c-001"): Ledger(
                Account.of("a-c-001"), Balance(datetime.date(2018, 9, 1), Quantity(Decimal(10))), []
            )
        },
    )

    # And a function to read ledger initial balances;
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return dict([(a, l.initial) for a, l in general_ledger.ledgers.items()])

    # And a function to read journal entries;

# Generated at 2022-06-14 04:27:59.642877
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2022-06-14 04:28:10.755672
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from dataclasses import dataclass, field
    from datetime import date
    from decimal import Decimal
    from typing import Dict
    from ..commons.numbers import Quantity
    from .accounts import Account
    from .generic import Balance


    @dataclass
    class InitialBalancesInMemoryWithGivenBalances(ReadInitialBalances):
        balances: Dict[Account, Balance] = field(default_factory=dict)

        def __call__(self, period: DateRange) -> Dict[Account, Balance]:
            return self.balances


    ## Create the initial balances algebra implementation.
    alg = InitialBalancesInMemoryWithGivenBalances()

    ## Create the program using the algebra implementation.
    initial_balances = compile_general_ledger_program(alg, lambda period: [])

    ## Running the program

# Generated at 2022-06-14 04:28:12.673020
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:28:25.687608
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import create_journal
    from .commons.zeitgeist import DateRange
    from .accounts.models import Accounts

    ## Define a period for the general ledger:
    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))

    ## Define defining accounts:
    assets = Accounts.create("Assets")
    equity = Accounts.create("Equity")
    liability = Accounts.create("Liability")
    revenue = Accounts.create("Revenue")
    expense = Accounts.create("Expense")

    ## Create a bank account:
    bank = Accounts.create("Bank", assets, balance="cr")

    ## Create an account for rent expense:
    rent = Accounts.create("Rent", expense, balance="dr")

    ## Create an account for loan receivables:

# Generated at 2022-06-14 04:28:38.785735
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__(): ...

# Generated at 2022-06-14 04:28:40.251957
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:28:42.183014
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass



# Generated at 2022-06-14 04:28:48.252988
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from datetime import date
    from .algebra import initial_balances_as_of, read_journal_entries
    from .accounts import Account, AccountName, AccountType

    def is_asset(a: Account) -> bool:
        return a.name.category == AccountName.Category.asset

    asset_initial_balances = initial_balances_as_of(is_asset)
    asset_journal_entries = read_journal_entries(lambda a: is_asset(a) and a.type == AccountType.terminal)
    general_ledger_program = compile_general_ledger_program(asset_initial_balances, asset_journal_entries)
    general_ledger = general_ledger_program(DateRange(date(2019, 1, 1), date(2019, 3, 31)))

# Generated at 2022-06-14 04:28:59.236085
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram
    """
    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account("11100"): Balance(period.since, Quantity(Decimal("500.00"))),
            Account("11101"): Balance(period.since, Quantity(Decimal("300.00"))),
        }


# Generated at 2022-06-14 04:29:10.969276
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    class FakeReadInitialBalances:
        def __call__(self, period):
            return {}

    class FakeReadJournalEntries:
        def __call__(self, period):
            return []

    program = compile_general_ledger_program(FakeReadInitialBalances(), FakeReadJournalEntries())
    gl = program(DateRange(datetime.date(1999, 1, 1), datetime.date(1999, 1, 31)))
    assert gl.period == DateRange(datetime.date(1999, 1, 1), datetime.date(1999, 1, 31))
    assert gl.ledgers == {}


# pylint: disable=protected-access
# Get the object attribute names expected by GeneralLedgerProgram

# Generated at 2022-06-14 04:29:18.027926
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import Account
    from .commons.numbers import Amount, Quantity

    ## Test data:

# Generated at 2022-06-14 04:29:18.722190
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:29:31.341177
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import Account
    from .commons import ModuleID
    from .journaling import LedgerEntry
    from .testing.journaling import mock_journal_entry
    import datetime

    """
    Tests that the general ledger program compiles and runs smoothly.
    """

    ## Mock the ledger entry:
    entry = mock_journal_entry("001", datetime.date(2015, 12, 31))

    ## Create the ledger entry:
    ledger_entry = LedgerEntry(ModuleID("test"), entry, entry.postings[0])

    ## Create the read initial balances algorithm:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {entry.postings[2].account: Balance(period.since, Quantity(10.00))}

    ## Create the read journal entries algorithm:

# Generated at 2022-06-14 04:29:42.017704
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from . import accounts
    from .commons.zeitgeist import now
    from .journaling import _test_journaling
    from .journaling.algebra import construct_journal_entry

    # pylint: disable=too-many-locals

    ## Inputs:
    ## - Cash and bank accounts:
    bank1 = accounts.BankAccount(code="101", description="Bank 1")
    bank2 = accounts.BankAccount(code="102", description="Bank 2")
    cash1 = accounts.CashAccount(code="201", description="Cash 1")
    cash2 = accounts.CashAccount(code="202", description="Cash 2")
    ## - Debtors:
    debtor1 = accounts.DebtorAccount(code="301", description="Debtor 1")
    debtor2 = accounts.DebtorAccount(code="302", description="Debtor 2")

# Generated at 2022-06-14 04:30:11.133737
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:30:21.575751
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for the compiled general ledger program.
    """

    ## Define test data:
    dt = datetime.date
    from .journaling import JournalEntry, Posting
    from .accounts import Account, Class
    from . import generic

    def _assert_equal(lhs: LedgerEntry, rhs: Posting):
        assert lhs.posting.journal.date == rhs.journal.date
        assert lhs.posting.account == rhs.account
        assert lhs.posting.amount == rhs.amount
        assert lhs.balance == rhs.amount

    ## Define test algebras:
    import random
    from collections import namedtuple
    from datetime import date, timedelta


# Generated at 2022-06-14 04:30:35.227752
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest import TestCase
    from dataclasses import replace
    from pyrsistent import pmap
    from ..commons.zeitgeist import datetime_of
    from .accounts import Account
    from .generic import Amount, Balance, Quantity

    ## Defines a mock of the service for reading initial balances.

# Generated at 2022-06-14 04:30:36.372369
# Unit test for function build_general_ledger
def test_build_general_ledger():
    pass


# Generated at 2022-06-14 04:30:37.294200
# Unit test for function build_general_ledger
def test_build_general_ledger():
    pass


# Generated at 2022-06-14 04:30:44.087385
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():

    # Define a concrete type which satisfies our protocol.
    @dataclass
    class _TestReadInitialBalances(ReadInitialBalances):

        def __call__(self, period: DateRange) -> InitialBalances:
            return InitialBalances()

    # Instantiate the concrete type.
    _x = _TestReadInitialBalances()

    # Call the protocol method.
    _x.__call__(DateRange(None, None))


# Generated at 2022-06-14 04:30:55.928498
# Unit test for function build_general_ledger
def test_build_general_ledger():

    from ..commons.zeitgeist import date

    from .accounts import Account, Accounts
    from .journaling import Journal, Posting

    from .generic import QuantityT

    from .accounts import Accounts
    from .journaling import Journal, Posting

    # Create a journal instance:
    journal = Journal[QuantityT](
        date(2020, 1, 1), date(2020, 1, 2), "Purchase from 01", [Posting(Accounts.asset, QuantityT(100)), Posting(Accounts.profit, QuantityT(100))]
    )
    # Create a journal instance:

# Generated at 2022-06-14 04:31:07.457512
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.testing import expect
    
    @dataclass
    class Prog:
        initial: InitialBalances
        period: DateRange
        expected: InitialBalances
        x: bool = False
    

# Generated at 2022-06-14 04:31:20.541462
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .journaling import Posting, ReadJournalEntries

    @dataclass
    class JournalEntryMock:
        date: datetime.date
        description: str
        postings: List[Posting]
    @dataclass
    class ReadJournalEntriesMock:
        def __call__(self, period: DateRange) -> Iterable[JournalEntryMock]:
            yield JournalEntryMock(period.since, "foo", [Posting.debit(Account(1), Amount(1))])
            yield JournalEntryMock(period.until, "bar", [Posting.debit(Account(2), Amount(2))])

# Generated at 2022-06-14 04:31:29.467255
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    ## Mock an initial balances reader:
    from unittest.mock import Mock
    ib_reader_mock = Mock(return_value=dict())
    type(ib_reader_mock).__call__ = ib_reader_mock

    ## Mock a journal entries reader:
    je_reader_mock = Mock(return_value=tuple())
    type(je_reader_mock).__call__ = je_reader_mock

    ## Compile a general ledger program:
    gl_program = compile_general_ledger_program(ib_reader_mock, je_reader_mock)

    ## Compile a new general ledger:
    gl = gl_program(DateRange(datetime.date.today(), datetime.date.today()))

    ## Check initial balances and journal entries readers are actually called:
    ib_reader

# Generated at 2022-06-14 04:32:30.596474
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Imports
    from collections import namedtuple
    from decimal import Decimal

    # Aliases
    Account = namedtuple('Account', 'code')
    Currency = namedtuple('Currency', 'code')

    ##
    ## Setup fixture
    ##

    # Define the period
    period = DateRange(since=datetime.date(2016, 1, 1), until=datetime.date(2016, 1, 8))

    # Define the initial balances
    initial_balances = {Account('123'): Balance(period.since, Quantity(Decimal('1000')))}

    # Define a dummy read initial balances
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return initial_balances

    # Define the expected output
    expected_output = initial_balances

    ##
    ##

# Generated at 2022-06-14 04:32:43.897910
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import JournalEntry, Posting, post
    from .accounts import Account

    Account_100 = Account(100)
    Account_200 = Account(200)
    Account_300 = Account(300)
    Account_400 = Account(400)
    Account_500 = Account(500)
    Account_900 = Account(900)

    JE01 = JournalEntry(20190101, "Journal Entry 01")
    JE02 = JournalEntry(20190102, "Journal Entry 02")
    JE03 = JournalEntry(20190103, "Journal Entry 03")
    JE04 = JournalEntry(20190104, "Journal Entry 04")
    JE05 = JournalEntry(20190105, "Journal Entry 05")
    JE06 = JournalEntry(20190106, "Journal Entry 06")

# Generated at 2022-06-14 04:32:50.855550
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .journaling import ReadJournalEntries
    from .accounts import read_accounts
    from .journaling import read_journal_entries
    from .balances import read_initial_balances
    from .journaling import JournalEntry, Posting
    from .accounts import Account
    from .commons.zeitgeist import DateRange
    from .commons import numbers
    from . import generic
    from . import accounting



# Generated at 2022-06-14 04:33:02.665506
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Set test case for class Ledger:
    # import os
    # from ..commons.journaling import JournalEntry, Posting, ReadJournalEntries
    # from .accounts import Account, AccountType
    # from .journaling import ReadJournalEntries
    from .read_journal_entries import read_journal_entries

    # def _read(period: DateRange) -> Iterable[JournalEntry[str]]:
    #     TEST_DATA_BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    #     TEST_DATA_FILE_NAME = os.path.join(TEST_DATA_BASE_DIR, "test_data.csv")
    #     return read_journal_entries(period, TEST_DATA_FILE_NAME)

    # read_journal_entries = ReadJournal

# Generated at 2022-06-14 04:33:15.542314
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import Account
    from .journaling import Journal, Posting, JournalEntry, Direction
    import datetime
    from decimal import Decimal
    from typing import cast

    @dataclass
    class FakeBalance:
        _value: Decimal

        @property
        def value(self):
            return cast(Quantity, self._value)

    @dataclass
    class FakeInitialBalances:
        account: Account
        balance: Decimal

        def __getitem__(self, item):
            return FakeBalance(self.balance)

    @dataclass
    class FakeLedger(Ledger):
        def __init__(self, account=None, initial=None, entries=None):
            self.account = account
            self.initial = initial
            self.entries = entries


# Generated at 2022-06-14 04:33:23.261971
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():

    from ..commons.time import dates
    from .accounts import load_accounts, Ref
    from .journaling import Entry, Posting, Transaction, load_entries

    ## Load master data:
    accounts = load_accounts("static/accounts.json")

    ## Get initial balances:
    opening_balance = {a: Balance(dates.since(2019, 1, 1), Quantity(Decimal(0))) for a in accounts.of_type("asset")}

    ## Load journal entries data:
    journal_entries = load_entries("static/entries.json")

    # Compile an instance:
    program = compile_general_ledger_program(lambda p: opening_balance, lambda p: journal_entries)

    # Compile and evaluate

# Generated at 2022-06-14 04:33:36.202763
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..backend import ReadJournalEntriesAlgebraBackend
    from ..commons.zeitgeist import date_range
    from .generic import Balance, InitialBalances
    from .accounts import Account, ACCOUNTS
    from .journaling import JournalEntry
    from .books import Book
    from .units import MoneySign

    # Define accounting period:
    PERIOD = date_range(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))

    # Define initial balances:
    INITIAL_BALANCES = InitialBalances(
        {a: Balance(PERIOD.since, MoneySign.CREDIT.unit(0)) for a in ACCOUNTS.values()}
    )

    # Define journal entries: