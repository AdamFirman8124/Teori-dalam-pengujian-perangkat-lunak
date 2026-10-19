

# Generated at 2022-06-14 04:23:51.644870
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import open, close
    from .journaling import unit_posting
    from .posting_child import PostingChild, CompilePostingChildProgram
    from .ledger_child import LedgerChild, CompileLedgerChildProgram

    class TestInitialBalances:
        def __call__(self, period):
            return {}


# Generated at 2022-06-14 04:23:53.432197
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:24:05.089029
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Test for method add of class Ledger
    """

    from .accounts import AccountCode

    @dataclass
    class _MockJournal:
        description: str = ""

    @dataclass
    class _MockJournalEntry:
        date: datetime.date
        description: str = ""
        postings: List[Posting[_T]] = field(default_factory=list)

    @dataclass
    class _MockPosting:
        account: Account
        amount: Amount
        direction: int
        journal: _MockJournal

    # creating entry to use as parameter
    criacao_posting = _MockPosting(Account(AccountCode("1.1.1.01.1")), 100.00, 1, _MockJournal())

# Generated at 2022-06-14 04:24:13.456566
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .journaling import Posting

    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account("1.10.1"): Balance(period.since, Quantity(10)),
            Account("1.20.1"): Balance(period.since, Quantity(20)),
            Account("1.40.1"): Balance(period.since, Quantity(40)),
        }

    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[Posting]]:
        from .journaling import Journal


# Generated at 2022-06-14 04:24:14.622751
# Unit test for method add of class Ledger
def test_Ledger_add():
    pass

# Generated at 2022-06-14 04:24:24.160090
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Compiles a general ledger program.
    """
    ## Prepare test data:
    period = DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))

# Generated at 2022-06-14 04:24:31.522784
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class MockReadInitialBalances(ReadInitialBalances):
        #: The initial balances to be returned.
        balances: InitialBalances

        def __call__(self, period: DateRange) -> InitialBalances:
            return self.balances

    ## This test is for code coverage, no assertions are required.
    MockReadInitialBalances({})(DateRange(datetime.date.today()))


# Generated at 2022-06-14 04:24:39.283764
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Posting, JournalEntry
    from .accounts import Account

    # A test fixture.
    # Describes journal entry for setting initial balances as of 01-Jan-2020:
    accounts = [Account(id="", name="", number="", terminal=True)]
    postings = [Posting(account=account, amount=0, direction=Debit) for account in accounts]
    journal_entry = JournalEntry(description="Initial balances as of 01-Jan-2020",
                                 date=datetime.date(2020, 1, 1),
                                 postings=postings)

    # A test fixture.
    # Describes a journal entry for "Gain on sale of equipment":

# Generated at 2022-06-14 04:24:51.888088
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import Account, AccountCategory
    from .journaling import Journal, Posting, Transaction
    from ..commons.zeitgeist import now

    # Build a journal:
    journal = Journal(
        "XYZ", now(), Transaction(
            [
                Posting(Account(123, AccountCategory.Expense), now(), Amount(100)),
                Posting(Account(456, AccountCategory.Revenue), now(), Amount(100)),
            ]
        )
    )

    # Create an empty ledger:
    ledger = Ledger(Account(456, AccountCategory.Revenue), Balance(now(), Quantity(Decimal(0))))

    # Add a posting to it:
    posting = ledger.add(journal.postings[1])

    assert posting.account == ledger.account
    assert posting.balance == Balance(now(), Amount(100))

# Generated at 2022-06-14 04:24:52.925314
# Unit test for method add of class Ledger
def test_Ledger_add():
    # TODO
    pass

# Generated at 2022-06-14 04:25:08.726976
# Unit test for method add of class Ledger
def test_Ledger_add():
    pass
    # account = Account(1, 'Account A', 'Ledger A')
    # a = Posting(1, datetime.date(2020, 1, 10), account, Amount(1), 1, '')
    # b = Posting(2, datetime.date(2020, 1, 10), account, Amount(1), -1, '')
    # c = Posting(3, datetime.date(2020, 1, 10), account, Amount(2), 1, '')
    # d = Posting(4, datetime.date(2020, 1, 10), account, Amount(3), -1, '')
    # e = Posting(5, datetime.date(2020, 1, 10), account, Amount(4), 1, '')
    # f = Posting(6, datetime.date(2020, 1, 10), account

# Generated at 2022-06-14 04:25:18.491723
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .common.algebras import read_journal_entries, read_initial_balances

    ## Compile the program:
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Build the general ledger:
    general_ledger = program(DateRange.parse('2015-01-01', '2015-12-31'))

    ## There should be six ledger entries in the first ledger:
    assert len(general_ledger.ledgers['X'].entries) == 6

# Generated at 2022-06-14 04:25:26.832319
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class MockedInitialBalance:
        pass

    @dataclass
    class MockedReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    MockedInitialBalance.balance = lambda self: Balance(datetime.date(2019, 4, 1), Quantity(Decimal(0)))

    MockedReadInitialBalances.read_initial_balances = MockedInitialBalance

    @dataclass
    class MockedJournalEntry:
        pass


# Generated at 2022-06-14 04:25:33.732598
# Unit test for method add of class Ledger
def test_Ledger_add():
    """
    Unit test for method add of class Ledger
    """

    from .journaling import Journal, Posting

    def test_debit():
        """
        Test debit
        """
        from decimal import Decimal

        ledger = Ledger(
            account=Account(code="1010", name="Cash"), initial=Balance(date=datetime.date(2020, 1, 1), value=Decimal(99))
        )
        test_journal = Journal(
            date=datetime.date(2019, 12, 31),
            description="Testing debit",
            postings=[
                Posting(account=Account(code="1010", name="Cash"), amount=Decimal(123), direction=Posting.Direction.DEBIT)
            ],
        )

        ledger.add(test_journal.postings[0])
        assert ledger.entries

# Generated at 2022-06-14 04:25:45.288142
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import datetime
    from dataclasses import make_dataclass
    from decimal import Decimal
    from typing import Callable
    import pytest
    from .accounts import Asset, Liability
    from .commons.numbers import Amount, Quantity
    from .journaling import JournalEntry
    from .posting import Posting, Direction

    ## GeneralLedgerProgram-like function object.
    @make_dataclass
    class Program:
        since: datetime.date
        until: datetime.date
        result: GeneralLedger[int]
        bal_a: Optional[Balance[int]] = None
        bal_l: Optional[Balance[int]] = None
        bal_oe: Optional[Balance[int]] = None
        bal_ie: Optional[Balance[int]] = None
        bal_oie: Optional[Balance[int]]

# Generated at 2022-06-14 04:25:58.269655
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.types import Currency
    from ..nubank import pkgdir, NubankJournal

    ## Journal:
    journal = NubankJournal.load(pkgdir / "test" / "nubank.json", Currency.BRL)

    ## Account balances at period end:
    initial_balances = {
        Account.ASSET_NUBANK_BRASIL_SA: Balance(datetime.date(2020, 3, 1), Quantity(Decimal(1000))),
        Account.ASSET_NUBANK_BRASIL_SA_DEBIT: Balance(datetime.date(2020, 3, 1), Quantity(Decimal(0))),
        Account.LIABILITY_ME: Balance(datetime.date(2020, 3, 1), Quantity(Decimal(0))),
    }

    ## Accounting period:
    period

# Generated at 2022-06-14 04:26:05.057713
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account("1001", "My Test Account")
    initial = Balance(datetime.date(2020, 1, 1), Quantity(10))
    ledger = Ledger(account, initial)
    journal = JournalEntry([Posting(ledger.account, datetime.date(2020, 1, 1), Quantity(5))])
    posting = journal[0]
    entry = ledger.add(posting)
    assert entry.balance == Quantity(15)


# Generated at 2022-06-14 04:26:12.230998
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = Account(["Cash", "Cash in wallet"])
    initial = Balance(datetime.date(2019, 1, 2), Quantity(Decimal(1280)))
    ledger = Ledger(account, initial)

    journal = JournalEntry(
        "Salary and Lottery winnings",
        datetime.date(2019, 1, 4),
        [
            Posting(account, Amount(Decimal(1000)), True),
            Posting(account, Amount(Decimal(4000)), False),
            Posting(account, Amount(Decimal(5000)), False),
        ],
    )

    entry = ledger.add(journal.postings[0])
    assert entry.balance.value == 2280

    entry = ledger.add(journal.postings[1])
    assert entry.balance.value == 2280


# Generated at 2022-06-14 04:26:22.470434
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..commons.zeitgeist import TimeRange
    from .journaling import build_journal_entries
    from .accounts import AccountType
    from ..commons.transaction import Transaction
    from .accounts import Relationship
    from .accounts import build_chart

    ## Accounts:
    acct1 = Account(name="Sales", account_type=AccountType.Revenue, relationships=[Relationship.Increase])
    acct2 = Account(name="Cost of Goods Sold", account_type=AccountType.Expense, relationships=[Relationship.Decrease])
    acct3 = Account(name="Assets", account_type=AccountType.Asset, relationships=[Relationship.Increase])
    acct4 = Account(name="Liabilities", account_type=AccountType.Liability, relationships=[Relationship.Decrease])

    ## Chart of accounts:
   

# Generated at 2022-06-14 04:26:31.005249
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import build_journal_entry

    ## Create a dummy journal entry:
    j1 = build_journal_entry(
        '2018-01-01',
        'Test journal entry 1',
        [
            Posting('Asset:Current:Cash', Quantity(0)),
            Posting('Income:Revenue', Quantity(0)),
            Posting('Liability:Current:Accounts Payable', Quantity(0)),
            Posting('Expense:Cost of Goods Sold', Quantity(0)),
        ],
    )

    ## Create a dummy journal entry:

# Generated at 2022-06-14 04:26:49.538286
# Unit test for function build_general_ledger
def test_build_general_ledger():
    ## Set up accounting period:
    period = DateRange(since=datetime.date(year=2019, month=1, day=1), until=datetime.date(year=2019, month=12, day=31))

    ## Set up initial balances, if any:
    initial = {
        Account("101002"): Balance(datetime.date(year=2018, month=12, day=1), Quantity(Decimal(1000.00))),
        Account("103001"): Balance(datetime.date(year=2018, month=12, day=1), Quantity(Decimal(0.00))),
    }

    ## Set up journal entries:

# Generated at 2022-06-14 04:26:59.691961
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import AccountId
    from .journaling import JournalEntryId

    from mydata.commons.zeitgeist import today
    from mydata.commons.numbers import Amount, Quantity
    from mydata.commons.money import USD
    from mydata.domain.accounts import read_terminal_accounts_as_dict
    from mydata.domain.journaling import read_journal_entries_as_list


# Generated at 2022-06-14 04:27:04.901886
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    class ReadInitialBalancesImpl(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    test_value = ReadInitialBalancesImpl()(DateRange.from_iso(None))
    assert test_value == {}


# Generated at 2022-06-14 04:27:17.811690
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():


    def _read_initial_balances(period: DateRange) -> InitialBalances:
        raise NotImplementedError

    def _read_journal_entries(period: DateRange) -> List[JournalEntry[_T]]:
        raise NotImplementedError

    ## Compile general ledger program
    gl_program = compile_general_ledger_program(_read_initial_balances, _read_journal_entries)


    def _read_initial_balances1(period: DateRange) -> InitialBalances:
        raise NotImplementedError

    def _read_journal_entries1(period: DateRange) -> List[JournalEntry[_T]]:
        raise NotImplementedError

    ## Compile general ledger program

# Generated at 2022-06-14 04:27:18.780041
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:27:26.721353
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .._test.fixtures import (
        dummy_balance_initial,
        dummy_journal_entry,
        dummy_journal_entries,
        dummy_ledger_entry,
        dummy_ledger_entries,
        dummy_read_initial_balances,
        dummy_read_journal_entries,
    )

# Generated at 2022-06-14 04:27:38.145643
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Unit test for function :py:func:`compile_general_ledger_program`.
    """
    ## Define test data:
    period = DateRange.last_year()
    initial_balances = {Account("1234"): Balance(period.since, Decimal("0"))}
    journal = [
        JournalEntry(datetime.date(2017, 1, 1), "0000", "", [Posting(Account("1234"), Decimal("100"), 1)])
    ]

    ## Mock the read_initial_balances algebra:
    class _MockReadInitialBalances(ReadInitialBalances):
        def __call__(self, _: DateRange) -> InitialBalances:
            return initial_balances

    ## Mock the read_journal_entries algebra:

# Generated at 2022-06-14 04:27:39.237978
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:27:52.474292
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    @dataclass
    class _Query:
        period: DateRange

    @dataclass
    class _QueryResult:
        balances: InitialBalances
        postings: List[Posting[_T]]

    @dataclass
    class _Queryable:
        fetch: _QueryResult

    @dataclass
    class _InitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return _Queryable(
                _QueryResult(
                    {Account(11, "Assets"), Account(12, "Liabilities"), Account(13, "Equity"), Account(14, "Income")},
                    [],
                )
            ).fetch(period)


# Generated at 2022-06-14 04:27:54.488512
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:28:16.716305
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..commons.zeitgeist import date
    from .journaling import JournalEntries
    from .accounts import AccountRoot

    initial_balances = {AccountRoot.ASSETS: Balance(date(2017, 1, 1), Quantity(0))}
    period = DateRange(since=date(2017, 1, 1), until=date(2017, 1, 2))
    journal = JournalEntries([JournalEntry(date(2017, 1, 1), "Salary", [Posting(AccountRoot.ASSETS, 100, Quantity(1))])])

# Generated at 2022-06-14 04:28:22.944914
# Unit test for method add of class Ledger
def test_Ledger_add():
    l = Ledger(0, Balance(0,0))
    l.add(Posting(DateRange(0,0), Journal("", Description(""), Decimal(0))))
    assert l.entries == [LedgerEntry(l,Posting(DateRange(0,0), Journal("", Description(""), Decimal(0)),None),0)]

# Generated at 2022-06-14 04:28:24.216472
# Unit test for method add of class Ledger
def test_Ledger_add():
    assert True == True


# Generated at 2022-06-14 04:28:30.737999
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class _Mock(ReadInitialBalances):
        pass

    actual = _Mock.__call__.__annotations__
    expected = {
        'return': InitialBalances,
        'period': DateRange,
    }

    assert actual == expected, f'Actual: {actual}, expected: {expected}'


# Generated at 2022-06-14 04:28:31.388576
# Unit test for function build_general_ledger
def test_build_general_ledger():
    pass

# Generated at 2022-06-14 04:28:43.937508
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from ..journaling.algebras import generate_journal_entries
    from ..journaling.model import JournalEntry as Entry

    ## Define the accounting period:
    period = DateRange(date(2000, 1, 1), date(2000, 2, 1))

    ## Define the initial balances:
    _initial_balances = {
        101: Balance(period.since, Quantity(0)),
        200: Balance(period.since, Quantity(0)),
        300: Balance(period.since, Quantity(0)),
    }

    ## Define the journal entries:

# Generated at 2022-06-14 04:28:45.036119
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert True


# Generated at 2022-06-14 04:28:46.470916
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass


# Generated at 2022-06-14 04:28:58.637441
# Unit test for method add of class Ledger
def test_Ledger_add():
    from pprint import pprint
    from zeitgeist.journaling import JournalEntry, Posting, PostingType

    def _build_entry(
        description: str,
        date: datetime.date,
        postings: List[Posting],
    ) -> JournalEntry[str]:
        return JournalEntry(description, date, postings)

    #: Set of account identifiers.
    accounts = {"a", "b", "c", "d", "e", "f"}

    #: Initial balances.
    initial_balances = {
        account: Balance(datetime.date(2020, 4, 1), Quantity(1)) for account in accounts
    }

    #: Set of general ledger accounts.
    ledger_accounts = {account for account in accounts if len(account) == 1}

    #: Accounting period.

# Generated at 2022-06-14 04:29:11.681284
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    def test_case(period, read_journal_entries, read_initial_balances, expected):
        actual = compile_general_ledger_program(read_initial_balances, read_journal_entries)(period)
        assert expected == actual
    test_case.description = "Unit test for method __call__ of class GeneralLedgerProgram"

    from .journaling import Journal, Posting
    from .accounts import Account

    ## Setup ledgers and entries:
    import datetime as dt

# Generated at 2022-06-14 04:29:33.888060
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Unit test for method __call__ of class ReadInitialBalances
    """
    raise NotImplementedError


# Generated at 2022-06-14 04:29:43.846257
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Journal, Posting, build_journal
    from .accounts import Account, build_accounts

    account, payroll_account, voucher_account = build_accounts(
        ('[101] Test account', '[102] Payroll', '[103] Voucher')
    )
    period = DateRange(since=datetime.date(2017, 1, 1), until=datetime.date(2017, 1, 31))
    journal = build_journal(('[001] Test journal', '[002] Payroll', '[003] Voucher'))

    balance = Balance(datetime.date(2016, 12, 31), Quantity(1001))
    pst = Posting(journal[0], account, Amount(1000))
    p1 = Posting(journal[1], payroll_account, Amount(100))

# Generated at 2022-06-14 04:29:58.164868
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from decimal import Decimal
    from gordon import Balance, Ledger, Quantity
    from gordon.accounting.accounts import Account
    from gordon.accounting.algebras import PeriodicBalance, ReadPeriodicBalance
    #
    # Test data:
    a = Account(
        '1',
        'Client account',
    )
    b = Account(
        '1.1',
        'Client account, first quarter',
    )
    dt = date(2019,10,1)
    #
    # Test:
    assert ReadInitialBalances.__call__(ReadInitialBalances, PeriodicBalance(dt-datetime.timedelta(100), ()), dt) == {}

# Generated at 2022-06-14 04:30:05.723460
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import datetime as dt
    import pytest
    from decimal import Decimal
    from dataclasses import dataclass, field
    from typing import List

    from ..commons.numbers import Amount, Currency, Quantity

    @dataclass
    class JournalEntry:
        """
        Provides a journal entry model.
        """

        #: Journal entry number.
        id: int

        #: Journal entry date.
        date: dt.date

        #: Journal entry description.
        description: str

        #: List of journal entry postings.
        postings: List[Posting] = field(default_factory=list)

    @dataclass
    class Posting:
        """
        Provides a journal entry posting model.
        """

        #: Posting account.
        account: Account

        #: Posting amount.
       

# Generated at 2022-06-14 04:30:11.435510
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class _implication(ReadInitialBalances):

        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    assert(_implication()(DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))) == {})



# Generated at 2022-06-14 04:30:18.247392
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from unittest.mock import Mock
    balance = Balance(date(2020, 1, 1), Quantity(1))
    alg = Mock(spec_set=ReadInitialBalances)
    alg.__call__.return_value = {Account():balance}
    actual = alg(None)
    alg.__call__.assert_called_once_with(None)
    assert actual == {Account():balance}


# Generated at 2022-06-14 04:30:26.994005
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests method __call__ of class GeneralLedgerProgram.
    """
    ## Import modules under test:
    from ..commons.zeitgeist import DateRange
    from .algebras import Money
    from .ledgering import compile_general_ledger_program

    ## Define an initial balances algebra:
    def _read_initial_balances(period: DateRange) -> Dict[Account, Balance]:
        return {
            Account("A"),
            Account("B"),
            Account("C"),
        }

    ## Define a journal entries algebra:

# Generated at 2022-06-14 04:30:39.563919
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test function build_general_ledger
    """
    # import statements
    from decimal import Decimal
    from datetime import date
    from ..commons.zeitgeist import DateRange
    from ..commons.numbers import amount
    from ..commons.accounting import Posting, JournalEntry
    from ..commons.posting import Transaction, Side, Direction
    from .accounts import Account
    from .journaling import Posting
    from .general_ledger import build_general_ledger, Ledger, LedgerEntry
    from .generic import Quantity, Balance

    # dates
    d = date

    # transactions

# Generated at 2022-06-14 04:30:52.977478
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Tests :py:func:`build_general_ledger`.
    """
    from ..commons.zeitgeist import DateRange
    from ..journaling.generic import build_journal_entry
    from ..journaling.postings import build_posting_from_object

    # Define some accounts:
    from ..foundation.accounts import Account, build_account

    a1 = build_account(Account("A1"), Decimal("123.45"))
    a2 = build_account(Account("A2"), Decimal("72.33"))
    a3 = build_account(Account("A3"), Decimal("-45.89"))
    a4 = build_account(Account("A4"), Decimal("-12.03"))

    # Define initial balances:

# Generated at 2022-06-14 04:31:04.187884
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Given a testing stack
    from . import accounts
    from . import journaling

    # Prepare program...

# Generated at 2022-06-14 04:31:54.370445
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    class ReadInitialBalancesImpl:
        def __init__(self):
            self.period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 3, 31))

# Generated at 2022-06-14 04:32:04.245261
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Performs unit tests on method compile_general_ledger_program.
    """
    from datetime import date
    from decimal import Decimal
    from . import algebra

    ## Helper function for building a general ledger.
    def build_ledger(opening: date, closing: date) -> GeneralLedger[algebra.Transaction]:
        ## Compile program:
        program = compile_general_ledger_program(
            read_initial_balances=algebra.read_initial_balances,
            read_journal_entries=algebra.read_journal_entries,
        )

        ## Pass opening and closing dates to the program and return the general ledger:
        return program(DateRange(opening, closing))

    ## This is a real account ledger:

# Generated at 2022-06-14 04:32:05.303145
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:32:11.437508
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Tests function compile_general_ledger_program.
    """
    def read_initial_balances(period: DateRange) -> InitialBalances:
        pass

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        pass

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    assert callable(program)

# EOF

# Generated at 2022-06-14 04:32:24.290252
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .algebras.journal import PostJournalEntry

    from .testing.algebras.journal import MockJournalRepository

    from .commons.zeitgeist import DateRange
    from .commons.numbers import Amount
    from .accounts import Account, AccountType
    from .journaling import Posting
    from .journaling import JournalEntry

    @dataclass
    class MockAccount:
        id: str
        number: int
        name: str
        account_type: AccountType

    def MockReadInitialBalances(period: DateRange) -> InitialBalances:
        # Balance 1
        account = Account(
            MockAccount(
                "1",
                710,
                "CASH (EUR)",
                AccountType.ASSET,
            )
        )

# Generated at 2022-06-14 04:32:34.102543
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    AlgebraInput = Dict[DateRange, Optional[InitialBalances]]

    def read_initial_balances(period: DateRange) -> InitialBalances:
        return dict(period=period, initial_balances=AlgebraInput[period])

    def read_journal_entries(
        period: DateRange, initial_balances: InitialBalances
    ) -> Iterable[JournalEntry[_T]]:
        return dict(period=period, initial_balances=initial_balances)

    ## Compile program:
    gl = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Use the program:
    accounts = {101: Balance(period.since, Quantity(Decimal(0))), 201: Balance(period.since, Quantity(Decimal(0)))}

# Generated at 2022-06-14 04:32:45.131099
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import Account
    from .journaling import Journal, Posting
    from .ledgers import build_general_ledger, Ledger, LedgerEntry

    # Given
    ledger = Ledger(Account(1), Balance(datetime.date(2020, 5, 21), Quantity(Decimal(0))))
    debit_journal = Journal(
        date=datetime.date(2020, 5, 22),
        description="Konto 1",
        postings=[Posting(Account(2), Quantity(100))],
    )
    credit_journal = Journal(
        date=datetime.date(2020, 5, 23),
        description="Konto 2",
        postings=[Posting(Account(1), Quantity(100))],
    )

    # When
    ledger_entry_1 = ledger.add(debit_journal.postings[0])

# Generated at 2022-06-14 04:32:50.954155
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Arrange:
    class Stub:
        def __call__(self, arg): return arg
    
    # Act:
    subject = Stub()
    actual = subject(42)

    # Assert:
    assert actual == 42


# Generated at 2022-06-14 04:33:02.724123
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.zeitgeist import Date
    from .accounts import Account
    from .generic import Balance

    period = DateRange(Date(2019, 1, 1), Date(2019, 12, 31))

    # Example of a possible implementation.
    class Imp(ReadInitialBalances):

        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("cash", Account.Assets): Balance(period.since, Quantity(0)),
                Account("stock", Account.Assets): Balance(period.since, Quantity(0)),
            }

    ib = Imp()


# Generated at 2022-06-14 04:33:11.049480
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Tests the functionality of method __call__ of class ReadInitialBalances.
    """

    # Define a dummy implementation of ReadInitialBalances:
    @dataclass
    class ReadInitialBalancesImpl(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    # Create the dummy and check if it is a subtype of ReadInitialBalances:
    ReadInitialBalancesImpl()
