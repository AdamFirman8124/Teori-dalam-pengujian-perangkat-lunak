

# Generated at 2022-06-14 04:23:53.648259
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..journaling import journal_entry  # noqa: F401
    from ..journaling.parsing import parse_journal_entry  # noqa: F401
    from ..journaling.algebra import read_journal_entries  # noqa: F401
    from .accounts import Account, AccountType  # noqa: F401
    from .algebra import query_initial_balances  # noqa: F401
    from .generic import GenericBalance, GenericInitialBalances  # noqa: F401
    from .parsing import parse_initial_balance  # noqa: F401
    from ...commons.zeitgeist import DateRange  # noqa: F401
    from datetime import date  # noqa: F401
    from decimal import Decimal  # noqa: F401
    from io import StringIO  # noqa

# Generated at 2022-06-14 04:24:05.268851
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..journaling.generic import create_journal_entry
    from ..config import Configuration
    from datetime import date

    config = Configuration.from_dict(
        {
            "accounts": [{"id": "1", "title": "Cash", "type": "Asset"}, {"id": "101000", "title": "Sales", "type": "Income"}],
            "account_defaults": [],
            "currency": "AUD",
            "rounding": "floor10",
        }
    )

# Generated at 2022-06-14 04:24:17.162124
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, Direction
    from .accounts import Account


    j = Journal(datetime.date(2020,4,1), 'test', 'test')
    j.add(Posting(Direction.debit, Account('test'), 100))
    j.add(Posting(Direction.credit, Account('test'), 100))
    l = Ledger(Account('test'), Balance(datetime.date(2020,4,1), 0))
    le = l.add(j.postings[0])
    # assert that the balance of the ledger is the same as the amount of the posting
    assert le.balance == 100
    le = l.add(j.postings[1])
    assert le.balance == 0

# Generated at 2022-06-14 04:24:19.388294
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class Foo:
        pass

    assert isinstance(Foo, ReadInitialBalances)


# Generated at 2022-06-14 04:24:20.159361
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:24:32.880804
# Unit test for method add of class Ledger
def test_Ledger_add():
    a = Account(
        code=1,
        name="Test account",
        description="Test account description",
        is_terminal=True,
    )
    b = Balance(
        date="2020-01-01",
        value=0,
    )
    l = Ledger(account=a, initial=b)
    j = JournalEntry(
        date="2020-01-31",
        description="Test debit entry",
        postings=[
            Posting(
                account=a,
                amount=10,
                direction=Quantity.Direction.DEBIT,
            ),
        ]
    )
    l.add(
        posting=j.postings[0]
    )
    assert len(l.entries) == 1


# Generated at 2022-06-14 04:24:39.250145
# Unit test for method add of class Ledger
def test_Ledger_add():

    from .journaling import Journal, PostingDirection

    a = Account("A")
    b = Account("B")

    j = Journal("Test", Date(2020, 12, 31), [Posting(a, Decimal(1), PostingDirection.DEBIT)])

    l = Ledger(a, Balance(Date(2020, 9, 30), Decimal(0)))

    l.add(j.postings[0])

    assert l.entries[0].balance == Decimal(1)

# Generated at 2022-06-14 04:24:51.820284
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from .accounts import read_accounts
    from .journaling import ReadJournalEntries

    read_journal_entries = ReadJournalEntries()


# Generated at 2022-06-14 04:25:01.257269
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import SimpleJournalEntry

    ## Test data:
    P = DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 5, 31))
    INITIAL = {Account("1101"): Balance(P.since, Quantity(Decimal(20000))), Account("1102"): Balance(P.since, Quantity(Decimal(0)))}
    JOURNAL = [
        SimpleJournalEntry(P.since, "Doc1", [Posting(Account("1101"), Amount(Decimal(30))), Posting(Account("1102"), Amount(Decimal(-30)))]),
        SimpleJournalEntry(P.since, "Doc2", [Posting(Account("1101"), Amount(Decimal(-20))), Posting(Account("1102"), Amount(Decimal(20)))]),
    ]

# Generated at 2022-06-14 04:25:03.482231
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Test the compile_general_ledger program function
    """
    pass

# Generated at 2022-06-14 04:25:22.179771
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import datetime
    from decimal import Decimal
    from typing import Callable, cast
    from unittest import mock
    from zeitgeist.datamodel.numbers import Amount
    from zeitgeist.datamodel.accounting.accounts import Account, AccountType
    from zeitgeist.datamodel.accounting.journaling import Journal
    from zeitgeist.datamodel.accounting.journaling import JournalEntry as JournalEntry_
    from zeitgeist.datamodel.accounting.journaling import Posting as Posting_
    from zeitgeist.datamodel.accounting.generic import Balance
    from zeitgeist.datamodel.accounting.general_ledger import GeneralLedger as GeneralLedger_

# Generated at 2022-06-14 04:25:31.518966
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test function build_general_ledger.
    """

    ## Import dependencies
    import datetime
    from decimal import Decimal
    from klotan import JournalEntry
    from klotan.ledger import Posting, Balance
    from klotan.accounts import Account, AccountType
    from klotan.general_ledger import build_general_ledger, Ledger, LedgerEntry


    ## 1. Define a test account ledger and a dummy journal entry
    accounts = [Account(code, AccountType(code), [], []) for code in ["1000", "1200", "1300"]]

# Generated at 2022-06-14 04:25:44.104427
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import datetime

    from ..commons.conversions import str2date

    from .accounts import AccountType

    ## Initialize a couple of accounts:
    checking_acct = Account("Checking", AccountType.Cash)
    saving_acct = Account("Savings", AccountType.Cash)
    trading_acct = Account("Trading", AccountType.Cash)
    life_insurance_premium_acct = Account("Life Insurance Premiums", AccountType.Receivable)

    ## Initialize a couple of journal entries:

# Generated at 2022-06-14 04:25:57.478500
# Unit test for function build_general_ledger
def test_build_general_ledger():
    journal_entries = [
        JournalEntry(
            date=datetime.date(2019, 1, 1),
            description="",
            postings=[
                Posting(account="A", amount=Amount(Decimal("100.00")), direction="DEBIT"),
                Posting(account="B", amount=Amount(Decimal("-100.00")), direction="CREDIT"),
            ],
        )
    ]
    initial_balances = {
        "A": Balance(date=datetime.date(2018, 12, 31), value=Quantity(Decimal("0"))),
        "B": Balance(date=datetime.date(2018, 12, 31), value=Quantity(Decimal("0"))),
    }

# Generated at 2022-06-14 04:26:07.615718
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Test cases for build_general_ledger
    """
    ## Run the test:
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 10))
    journal = [JournalEntry(datetime.date(2019, 1, 5), "Test", [Posting(datetime.date(2019, 1, 5), "MCR", "Assets:Cash", Amount(Decimal(100)))])]
    initial = {"Assets:Cash": Balance(datetime.date(2019, 1, 1), Quantity(Decimal(100)))}
    result = build_general_ledger(period, journal, initial)
    assert result.period == period

# Generated at 2022-06-14 04:26:19.358827
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    @dataclass
    class ReadInitialBalancesMock:
        initial_balances: InitialBalances

        def __call__(self, period: DateRange) -> InitialBalances:
            return self.initial_balances

    @dataclass
    class ReadJournalEntriesMock:
        journal_entries: List[JournalEntry]

        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return self.journal_entries


# Generated at 2022-06-14 04:26:20.580275
# Unit test for function build_general_ledger
def test_build_general_ledger():
    assert 0


# Generated at 2022-06-14 04:26:22.961135
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Unit test for method __call__ of class GeneralLedgerProgram
    """
    # test failure
    assert False

# Generated at 2022-06-14 04:26:35.019100
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    class MockReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account(code="A1", name="ASSETS1", type="ASSETS", level=1),
                Balance(period.since, Amount(100)),
                Account(code="A2", name="ASSETS2", type="ASSETS", level=1),
                Balance(period.since, Amount(150)),
                Account(code="E1", name="EQUITY1", type="EQUITY", level=1),
                Balance(period.since, Amount(200)),
            }

# Generated at 2022-06-14 04:26:36.441269
# Unit test for method add of class Ledger
def test_Ledger_add():
    assert True

# Generated at 2022-06-14 04:27:02.369079
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert False, "Not implemented"


# Generated at 2022-06-14 04:27:10.848902
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, Posting
    from .accounts import Account
    from ..commons.primitives import Direction
    from datetime import date

    #Set up account for testing
    account = Account(number="0", name="testaccount")

    #Setup balance for testing
    balance = Balance(date.today(), Quantity(Decimal(0)))

    #Setup the ledger to test
    ledger = Ledger(account, balance)

    #Setup journal and posting to input into add method
    journal = Journal()
    posting = Posting(account, Direction.DEBIT, Quantity(Decimal(10)))
    journal.add(posting)

    #Test that ledger.entries is empty
    assert len(ledger.entries) == 0

    #Run add method
    ledger.add(posting)

    #Test that ledger.entries has

# Generated at 2022-06-14 04:27:20.297307
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class A:
        period: DateRange
        initial_balances: InitialBalances

    @dataclass
    class B:
        a: A

    read_initial_balances = lambda period: B(A(period, InitialBalances({Account("1"), Balance(Decimal(0))})))

    assert(read_initial_balances(DateRange.parse_iso_date_range("2017-01-01/2017-12-31")) == B(
        A(DateRange(datetime.date(2017, 1, 1), datetime.date(2017, 12, 31)),
          InitialBalances({Account("1"), Balance(Decimal(0))}))))



# Generated at 2022-06-14 04:27:21.337130
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass  # Nothing to test


# Generated at 2022-06-14 04:27:35.092057
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, JournalEntry

    account = Account('12000')
    period = DateRange(datetime.date(year=2018, month=1, day=1), datetime.date(year=2018, month=12, day=31))

    ledger = Ledger(account, Balance(period.since, Quantity(Decimal(0))))

    journal = Journal(
        date=period.since,
        description='Ledger test',
        postings=[
            Posting(account, Quantity(Decimal('100.00')), None),
            Posting(Account('40000'), Quantity(Decimal('100.00')), None),
        ]
    )

    entry = JournalEntry(journal)
    posting = entry.postings[0]

    ledger.add(posting)


# Generated at 2022-06-14 04:27:41.662337
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import datetime
    from dataclasses import dataclass, field
    #from decimal import Decimal
    from typing import Dict, Iterable, List, Optional, TypeVar

    from ..commons.numbers import Amount, Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .generic import Balance
    from .journaling import JournalEntry, Posting, ReadJournalEntries

    #: Defines a generic type variable.
    _T = TypeVar("_T")


    @dataclass
    class LedgerEntry(Generic[_T]):
        """
        Provides a ledger entry model.
        """

        #: Ledger the entry belongs to.
        ledger: "Ledger[_T]"

        #: Posting of the ledger entry.
        posting: Posting[_T]

        #:

# Generated at 2022-06-14 04:27:54.665961
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Executes test for method __call__ of class GeneralLedgerProgram.
    """

    ## Test data:
    read_initial_balances: ReadInitialBalances = lambda period: {Account("cash"): Balance(period.since, Quantity(100))}
    read_journal_entries: ReadJournalEntries[int] = lambda period: [
        JournalEntry(
            period.since,
            "test",
            [Posting(Account("cash"), Quantity(10)), Posting(Account("expenses"), Quantity(10))],
            1,
        )
    ]
    period: DateRange = DateRange.of_date(datetime.date(2020, 1, 1))

    ## Compile program:
    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Exec

# Generated at 2022-06-14 04:28:05.684500
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .generic import Account, Balance, AccountType


# Generated at 2022-06-14 04:28:17.393453
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ._test_journaling import (
        _test_read_journal_entries,
        _test_read_initial_balances,
    )

    ## Compile the program.
    read_journal_entries = _test_read_journal_entries()
    read_initial_balances = _test_read_initial_balances()
    read_general_ledger = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    ## Execute the program.
    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 2, 28))
    general_ledger = read_general_ledger(period)

    ## Assertions:
    assert general_ledger.period == period

# Generated at 2022-06-14 04:28:17.862961
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass

# Generated at 2022-06-14 04:28:37.770955
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from dataclasses import asdict
    from datetime import date
    from decimal import Decimal
    from typing import cast
    from pyledger.model.accounts import AccountType
    from pyledger.model.commons.numbers import Amount, Quantity
    from pyledger.model.commons.zeitgeist import DateRange
    from pyledger.model.journaling import JournalEntry, Journaling, Posting
    from pyledger.model.generic import Balance
    from .ledgers import build_general_ledger, LedgerEntry
    from .accounts import Account
    from .journaling import PostingDirection
    from .generic import Balance
    ## Prepare environment:
    ## Declare a journaling algebra implementation, for the purposes of the unit test:

# Generated at 2022-06-14 04:28:46.337755
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .teapot import Teapot
    from .accounts import IncomeAccount, ExpenseAccount

    teapot = Teapot()

    income_account = IncomeAccount("Tea revenue")

    expense_account = ExpenseAccount("Tea cost")

    initial_balance = Balance(datetime.date(2020, 1, 1), Quantity(Decimal("0")))

    ledger = Ledger(income_account, initial_balance)

    entry = ledger.add(
        Posting(teapot.next_id(), expense_account, datetime.date(2020, 1, 1), Amount(Decimal("1")), True)
    )

    assert entry.balance == Quantity(Decimal("1"))

# Generated at 2022-06-14 04:28:58.581528
# Unit test for function build_general_ledger
def test_build_general_ledger():
    # This test is just to make sure everything runs. The specific tests are in ../journaling/tests.py
    # It is a unit test because the test occurs at a low level of abstraction.
    from ..commons.zeitgeist import DateRange
    from ..journaling.journaling import JournalEntry
    from ..journaling.accounts import Account

    period = DateRange("2019-01-01", "2019-02-01")
    je = JournalEntry("purchase", "2019-01-01", ["cogs", "ap"])
    initial_balances = {
        Account("cogs"): Balance(period.since, Quantity(Decimal(0))),
        Account("ap"): Balance(period.since, Quantity(Decimal(0)))
    }

    gl = build_general_ledger(period, [je], initial_balances)

# Generated at 2022-06-14 04:29:05.358369
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Tests the method __call__ of class ReadInitialBalances
    """

    class MockReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            pass

    MockReadInitialBalances()(DateRange(datetime.date(2020, 10, 1), datetime.date(2020, 10, 31)))



# Generated at 2022-06-14 04:29:12.038216
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..commons.algebra import read_initial_balances, read_journal_entries
    from ..commons.zeitgeist import Date, DateRange

    period = DateRange(Date(2017, 1, 1), Date(2017, 12, 31))

    initial_balances = {
        "Assets:Cash": Balance(period.since, Decimal(100)),
        "Assets:Bank": Balance(period.since, Decimal(100)),
        "Equity:Opening Balances": Balance(period.since, Decimal(200)),
        "Liabilities:Taxes:VAT": Balance(period.since, Decimal(100)),
    }


# Generated at 2022-06-14 04:29:15.511321
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    assert ReadInitialBalances.__call__.__doc__ == "__call__(self, period: DateRange) -> InitialBalances:\n        pass"


# Generated at 2022-06-14 04:29:28.346597
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .commons import config
    from . import accounts_alg, books_alg, journals_alg, storage

    ## Define the period to build the ledger for:
    config.start_of_accounting = datetime.date(2018, 1, 1)
    period = DateRange(datetime.date(2018, 1, 1), datetime.date(2018, 12, 31))

    ## Consume the program which builds general ledger:
    program = compile_general_ledger_program(
        accounts_alg.read(storage.read(config.accounts_path)),
        journals_alg.read(books_alg.read(storage.read(config.books_path))),
    )

    ## Build the general ledger:
    general_ledger = program(period)

    ## Confirm balances match:

# Generated at 2022-06-14 04:29:37.837262
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():

    from datetime import date
    from decimal import Decimal

    from ..ledger import accounts, balance

    # Setup the ledger:
    ledger = {
        accounts.ASSETS: {
            accounts.CASH: balance.Balance(date(2018, 1, 1), Decimal(12.23)),
        }
    }

    # Define the read initial balances algebra:
    def read_initial_balances(period: DateRange) -> InitialBalances:
        return {a: b for a, b in ledger.items()}

    # Assert:
    assert read_initial_balances(DateRange(date(2018, 1, 1), date(2018, 1, 1))) == ledger


# Generated at 2022-06-14 04:29:46.672404
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Tests GeneralLedgerProgram__call__.
    """
    from hamcrest import assert_that, has_length, is_, has_entries
    from pyhamcrest.core.common.issubsetof import subset_of
    from pyhamcrest.library.number.ordering_comparison import greater_than_or_equal_to

    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountCategory, list_accounts
    from .generic import Balance, BalanceEffect
    from .journaling import JournalEntry, Posting, Journal

    ## Initial end of the previous financial period:
    common_since: datetime.date = datetime.date(2020, 9, 1)

    ## Opening date of the period:

# Generated at 2022-06-14 04:30:00.841182
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .accounts import build_accounts_book

    from .journaling import build_journal_entry

    from .journaling import build_posting

    accounts_book = build_accounts_book()

    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))

    accounts = [accounts_book.get(a) for a in ["101", "102", "201", "301", "401", "501", "601"]]


# Generated at 2022-06-14 04:31:07.669027
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .journaling import Journal, Posting, journal_entries

    from .accounts import create_account, terminal_accounts

    from .commons.zeitgeist import DateRange

    from .generic import Balance, Quantity

    from .books import build_book

    from .datasources import memory

    from ..commons.numbers import Amount

    opening_date = datetime.date(2000, 1, 1)

    closing_date = datetime.date(2000, 12, 31)

    selected_period = DateRange(opening_date, closing_date)

    opening_balance = Balance(opening_date, Quantity(Decimal("100")))

    initial_balances = {create_account("110000"): opening_balance}


# Generated at 2022-06-14 04:31:20.746051
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import CreateJournalEntry
    from .commons.identity import generate_uuid
    journal_entry = CreateJournalEntry(
        date=datetime.datetime.today(),
        description='Tester les unit tests',
        debit='00001 Débit',
        credit='00002 Crédit',
    )
    journal_entry(journal_id=generate_uuid(), journal_entries=[])
    # TODO Add the expected result
    #if entries[0] == journal_entry(
    #        journal_id=generate_uuid(), journal_entries=[]) and entries[
    #            1] == journal_entry(
    #                journal_id=generate_uuid(), journal_entries=[]):
    #    return True
    #else:
    #    return False

# Unit test

# Generated at 2022-06-14 04:31:29.664565
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import random
    import unittest.mock as mock

    mock_read_initial_balances: ReadInitialBalances = mock.Mock(spec=ReadInitialBalances)
    mock_read_journal_entries: ReadJournalEntries = mock.Mock(spec=ReadJournalEntries)

    mock_read_initial_balances.__call__.return_value = {a: Balance(d, q) for a, d, q in [
        (Account("100100"), datetime.date(2019, 1, 1), random.randint(0, 1000)),
        (Account("100200"), datetime.date(2019, 1, 1), -random.randint(0, 1000)),
    ]}

# Generated at 2022-06-14 04:31:40.617702
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import Account
    from .journals import Journal, JournalEntry
    from .posts import Posting
    from .accounting import Transaction, TransactionPosting

    date = datetime.date(2020, 1, 10)
    account_banking = Account("Banking", "Cash and bank balance")
    account_revenue = Account("Revenue", "Revenue")
    account_expenses = Account("Expenses", "Expenses")
    amount = Amount(100.00)
    description = "New revenue"
    journal = Journal(date, description)
    journal.post(account_banking, amount)
    journal.post(account_revenue, -amount)
    initial = Balance(datetime.date(2020, 1, 1), Decimal(100))
    ledger = Ledger(account_banking, initial)
    ledger.add

# Generated at 2022-06-14 04:31:49.281704
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from .initial_balances import ReadInitialBalances1
    from .journaling import ReadJournalEntries1
    t1 = datetime.date(2020,1,1)
    t2 = datetime.date(2020,2,1)
    read_intial_balances = ReadInitialBalances1(t1)
    read_journal_entries = ReadJournalEntries1()
    compile_general_ledger_program(read_intial_balances, read_journal_entries)(t2)

# Generated at 2022-06-14 04:31:49.984028
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__(): pass

# Generated at 2022-06-14 04:32:01.311911
# Unit test for function build_general_ledger
def test_build_general_ledger():
    period = DateRange(since=datetime.date(2000, 1, 1), until=datetime.date(2000, 2, 1))
    journal = [
        JournalEntry(
            datetime.date(2000, 1, 1),
            "Testing",
            [
                Posting('Assets:Cash','Income:Revenue',Decimal(100)),
                Posting('Income:Revenue','Equity:Starting'),
            ],
        ),
    ]
    general_ledger = build_general_ledger(period, journal, {})

# Generated at 2022-06-14 04:32:02.441486
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    ...

# Generated at 2022-06-14 04:32:08.642053
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class TestReadInitialBalances:
        value: InitialBalances
        def __call__(self, period: DateRange) -> InitialBalances:
            return self.value
    TestReadInitialBalances(InitialBalances({Account("12000"): Balance(datetime.date(2019, 1, 1), Quantity(Decimal(0)))}))


# Generated at 2022-06-14 04:32:10.686348
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass  # sure!



# Generated at 2022-06-14 04:33:28.284823
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account("11.01.00", "Current Assets", "Cash"): Balance(datetime.date(2017, 12, 31), Quantity(Decimal(0))),
            Account("11.02.00", "Current Assets", "Cash In The Bank"): Balance(datetime.date(2017, 12, 31), Quantity(0)),
        }

    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        from .journaling.journal_entry import JournalEntry_T


# Generated at 2022-06-14 04:33:32.897657
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .accounts import AccountType
    from .journaling import JournalEntry, Posting
    from .categories import TransactionCategory, TransactionType
    
    # Create an Asset account
    account = Account("Cash", AccountType.Asset)
    
    # Create a cash transaction
    transaction = TransactionCategory("Cash", TransactionType.Receipt)
    
    # Create a journal entry
    entry = JournalEntry("Cash Receipt", "Receipt of $100", datetime.date(2019,12,31))
    entry.post(Posting(account, transaction, 100))
    
    # Test initial balance = 0, as no Ledgers have been created yet
    assert Balance(datetime.date.today(), 0) == Balance.current()
    
    # Create a ledger for the account
    ledger = Ledger(account, Balance.current())
    
   