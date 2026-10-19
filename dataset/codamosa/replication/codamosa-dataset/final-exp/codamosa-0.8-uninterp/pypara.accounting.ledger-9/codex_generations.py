

# Generated at 2022-06-14 04:23:51.608433
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Initialization of data to test
    account = Account(id="id",name="name")
    bal = Balance(datetime.date(2020, 6, 19), Quantity(2600))
    acc = Account(id="id",name="name")
    dr = Decimal()
    dr.from_float(2600)
    am = Amount(dr)
    je = JournalEntry(
        id="je",
        description="desc",
        date=datetime.date(2020, 6, 19),
        reference="ref",
        postings=[Posting(id="pstng_id",account=acc,direction=Posting.Direction.DEBIT,amount=am,journal=je)])

# Generated at 2022-06-14 04:24:03.746128
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from ..dal.journaling import JournalEntry, Posting
    from ..dom.accounts import Account, AccountType
    from ..dom.journaling import Direction, Journal
    from ..dom.numbers import Amount
    from ..dom.zeitgeist import DateRange
    from .accounts import compile_accounts_program
    from .journaling import compile_journaling_program, JournalEntrySource

    # # Assign test data:
    # def _test_data() -> Iterable[JournalEntry]:
    #     return [
    #         JournalEntry(
    #             Journal(description="Opening balance"),
    #             [
    #                 Posting(Account(AccountType.asset, "100"), Direction.debit, Amount(Decimal(100)), datetime.date(2019, 1, 1)),
    #                 Posting(Account(AccountType.expense

# Generated at 2022-06-14 04:24:18.426842
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.numbers import Amount, Quantity
    from .journaling import Journal, JournalEntry, Posting
    from ..accounts.accounts import Account
    from ..journaling.journaling import JournalEntry
    from ..accounts.accounts import Account
    from ..commons.zeitgeist import DateRange
    ## Create the journal.
    journal = Journal()

    ## Add the journal entries.
    journal.add(JournalEntry(datetime.date.today(), "Journal Entry #1", []))
    journal.add(JournalEntry(datetime.date.today(), "Journal Entry #2", []))

    # Add the postings.
    journal.postings.append(Posting(Account(), Amount(Decimal(0))))
    journal.postings.append(Posting(Account(), Amount(Decimal(0))))

    ## Create the ledger.


# Generated at 2022-06-14 04:24:26.066673
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    balance_1 = Balance(datetime.date(2020, 1, 1), Quantity(Decimal(0)))
    balance_2 = Balance(datetime.date(2020, 1, 1), Quantity(Decimal(10)))
    balance_3 = Balance(datetime.date(2020, 1, 1), Quantity(Decimal(11)))
    period = DateRange(since=datetime.date(2020,1,1),until=datetime.date(2020,1,10))
    account_1 = Account("00001")
    account_2 = Account("00002")
    account_3 = Account("00003")

    def _read_initial_balances(period: DateRange) -> InitialBalances:
        initial_balance: InitialBalances = {account_1: balance_1,account_2:balance_2, account_3:balance_3}

# Generated at 2022-06-14 04:24:37.102137
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, Posting

    # Initialize Ledger object
    account = Account("10000")
    initial = Balance('2009-01-01', Quantity(Decimal(0)))
    entries = list()
    ledger = Ledger(account, initial, entries)

    # Initialize a Journal object
    date = datetime.date(2020, 1, 1)
    description = "New Journal"
    postings = [ Posting("SA", Quantity(Decimal("10.00")))]
    journal = Journal(date, description, postings)

    # Initialize a Posting object
    direction = 1
    account = Account("20000")
    amount = Quantity(Decimal("10.00"))
    posting = Posting(account, amount, direction)

    # Add a posting to the journal entries
    ledger_entry = ledger.add(posting)

# Generated at 2022-06-14 04:24:38.387369
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:24:51.108834
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    # Test data:
    from ..test_data import journal
    from .journaling import read_journal_entries
    from ..commons.adt import DateRange

    # Compile the general ledger program:
    gl_program = compile_general_ledger_program(read_initial_balances=lambda _: {}, read_journal_entries=read_journal_entries)

    # Apply the program:
    gl = gl_program(DateRange(since=journal[0].date, until=journal[-1].date))

    # Expected ledger:

# Generated at 2022-06-14 04:25:00.972574
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Posting
    from .accounts import Account, AccountType, AccountGroup
    from .generic import GenericAccount
    from dataclasses import dataclass, field
    import datetime

    assert Account(1, AccountType.ASSET, AccountGroup.CASH, "CASH", GenericAccount()).code == "1"

    period = DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 31))

    journal = [
        JournalEntry("1", datetime.date(2019, 1, 1), "ABC"),
        JournalEntry("2", datetime.date(2019, 1, 1), "DEF"),
        JournalEntry("3", datetime.date(2019, 1, 2), "GHI"),
    ]


# Generated at 2022-06-14 04:25:10.408597
# Unit test for method add of class Ledger
def test_Ledger_add():
    Account1 = Account("0001", "Account 1")
    Account2 = Account("0002", "Account 2")
    Journal1 = JournalEntry("This is Journal 1.")
    Journal1.post(Posting(Account1, Amount(100), "Debit", "This is Posting 1."))
    Journal1.post(Posting(Account2, Amount(100), "Credit", "This is Posting 2."))
    Ledger1 = Ledger(Account1, Balance(datetime.date(2019, 12, 31), Quantity(Decimal(0))))
    Posting1 = Posting(Account1, Amount(100), "Debit", "This is Posting 1.")
    Balance1 = Quantity(Decimal(0))
    Balance2 = Balance1 + Posting1.amount * Posting1.direction.value

# Generated at 2022-06-14 04:25:22.971883
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from decimal import Decimal
    from ..commons.amounts import Amount
    from ..commons.numbers import Quantity
    from ..commons.zeitgeist import DateRange 
    from ..journaling import JournalEntry, Posting, Direction

    # Set up test data
    period = DateRange(since=date(2019, 12, 31), until=date(2020, 12, 31))

# Generated at 2022-06-14 04:25:39.792878
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    Tests for function compile_general_ledger_program.
    """

    ## Mock read initial balances, journal entries:
    def _read_initial_balances(period: DateRange) -> InitialBalances:
        return {Account(1): Balance(period.since, Quantity(Decimal(100))), Account(2): Balance(period.since, Quantity(Decimal(200)))}


# Generated at 2022-06-14 04:25:47.728116
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from datetime import date
    from journalbot.commons import algebra

    ## Initial balances as of 31/12/2015:

# Generated at 2022-06-14 04:25:53.560769
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal
    journal = Journal(datetime.date.today(), "")
    journal.post(Account.get_instance("cash"), Decimal(20), "test")
    posting = journal.post(Account.get_instance("test"), Decimal(-20), "test")
    ledger = Ledger(Account.get_instance("cash"), Balance(datetime.date.today(), Decimal(0)))
    entry = ledger.add(posting)
    assert posting == entry.posting
    assert posting.amount == entry.amount

# Generated at 2022-06-14 04:26:05.294465
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    """
    Test GeneralLedgerProgram.__call__()
    """
    import copy, random, uuid
    from decimal import Decimal
    from datetime import date
    from dateutil.relativedelta import relativedelta
    from zsl.commons.random import RandomData, RandomDate

    from ..commons.zeitgeist import previous_period

    from .accounts import Account, AccountTree
    from .journaling import Journal, JournalEntry, Posting, create_journal_entry

    def _create_account_tree(
        code: str, name: str, parent: Optional[AccountTree] = None, children: Optional[List[AccountTree]] = None
    ) -> AccountTree:
        """
        A helper function which creates an account tree.
        """
        ## Initialize empty children buffer:
        if children is None:
            children

# Generated at 2022-06-14 04:26:12.396998
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Posting, JournalEntry
    
    import datetime
    from numeric import Quantity
    
    period = DateRange(
        datetime.date(2018, 1, 1),
        datetime.date(2018, 12, 31),
    )
    

# Generated at 2022-06-14 04:26:22.579315
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..commons.transacts import Transact

    ## Create the ledger.
    account = Account("1", "Cash", True)
    initial_balance = Balance("2017-12-31", Quantity(Decimal(10)))
    ledger = Ledger(account, initial_balance)

    ## Add an entry to the ledger.
    posting = Posting("2017-12-31", Transact("Debit"), Decimal(10), account)
    entry = ledger.add(posting)

    ## Check the entry.
    assert entry.ledger == ledger
    assert entry.posting == posting
    assert entry.balance == Quantity(Decimal(20))
    assert entry.date == datetime.date(2017, 12, 31)
    assert entry.description == "Debit"
    assert entry.amount == Decimal(10)
    assert entry.cnt

# Generated at 2022-06-14 04:26:23.710183
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    pass


# Generated at 2022-06-14 04:26:32.281604
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest import mock

    mock_ReadInitialBalances = mock.Mock(spec=ReadInitialBalances, autospec=True)
    mock_ReadInitialBalances.return_value = {}

    mock_ReadInitialBalances(DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31)))

    mock_ReadInitialBalances.assert_called_once_with(DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31)))


# Generated at 2022-06-14 04:26:45.341372
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from ..commons.architecture import build_algebra
    from .algebras import InitialBalances, JournalEntry, ReadJournalEntries
    from .domains.debit_credit import Debit, Direction, Journal
    from .domains.double_entry import Posting
    from .domains.monetary import Amount, Currency
    from .domains.ledgers import TrialBalance

    # Build the algebra:
    algebra = build_algebra([InitialBalances, JournalEntry, ReadJournalEntries, TrialBalance])

    # Get algebra implementation:
    initial_balances = algebra(InitialBalances)
    journal_entry = algebra(JournalEntry)
    read_journal_entries = algebra(ReadJournalEntries)

    # Define the ledger accounts:
    ASSET = Account(code="ASSET", title="Asset")
    EQUITY = Account

# Generated at 2022-06-14 04:26:51.969816
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    @dataclass
    class MockReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    @dataclass
    class MockReadJournalEntries(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return []

    mock_read_initial_balances = MockReadInitialBalances()
    mock_read_journal_entries = MockReadJournalEntries()

    compile_general_ledger_program(mock_read_initial_balances, mock_read_journal_entries)(DateRange(datetime.date(2019,1,1),datetime.date(2019,12,31)))

# Generated at 2022-06-14 04:27:08.573735
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Initialize some accounts:
    account_1 = Account("Asset", "Office equipment", "Truck")
    account_2 = Account("Expense", "Operations", "Fuel")
    account_3 = Account("Asset", "Bank", "BNI")

    ## Create a ledger for the bank account:
    ledger = Ledger(account_3, Balance(datetime.date(2019, 10, 1), Quantity(Decimal(0))))

    ## Add a posting:
    entry = ledger.add(Posting(account_3, Quantity(Decimal(0)), datetime.date(2019, 10, 1), "Initial amount"))
    assert entry.balance == Decimal(0)

    ## Add a second posting:

# Generated at 2022-06-14 04:27:19.953481
# Unit test for method add of class Ledger
def test_Ledger_add():
    from . import accounts

    # Initial conditions
    c1 = accounts.Cash()
    l1 = Ledger(c1, Balance(datetime.date(2020, 1, 1), Quantity(200)))
    d1 = datetime.date(2020, 1, 1)
    j1 = JournalEntry(d1, "J1", None)
    p1 = Posting(j1, c1, Amount(150), None)
    p2 = Posting(j1, c1, Amount(-50), None)

    # Actual results
    e1 = l1.add(p1)
    e2 = l1.add(p2)

    # Expected results
    le1 = LedgerEntry(l1, p1, Quantity(200 + 150))

# Generated at 2022-06-14 04:27:20.586423
# Unit test for method add of class Ledger
def test_Ledger_add():
    pass

# Generated at 2022-06-14 04:27:33.875957
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2022-06-14 04:27:41.319521
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    # Create initial balances:
    initial_balances = {
        Account("PL401001"): Balance(datetime.date(2020, 1, 1), Quantity(Decimal("1750.00")))
    }
    # Create journal entries:
    journal1: JournalEntry = JournalEntry(
        "",
        datetime.date(2020, 1, 3),
        [Posting(Account("PL401001"), Quantity(Decimal("-15.00")), ""), Posting(Account("PL402001"), Quantity(Decimal("15.00")), "")],
    )

# Generated at 2022-06-14 04:27:52.155943
# Unit test for method add of class Ledger
def test_Ledger_add():
    account1 = Account("1111", "Account 1")
    account2 = Account("2222", "Account 2")
    account3 = Account("3333", "Account 3")
    account4 = Account("4444", "Account 4")
    account5 = Account("5555", "Account 5")
    account6 = Account("6666", "Account 6")
    account7 = Account("7777", "Account 7")
    account8 = Account("8888", "Account 8")
    account9 = Account("9999", "Account 9")
    account10 = Account("1010", "Account 10")
    account11 = Account("1111", "Account 11")
    account12 = Account("1212", "Account 12")
    account13 = Account("1313", "Account 13")
    account14 = Account("1414", "Account 14")

# Generated at 2022-06-14 04:27:59.812530
# Unit test for function build_general_ledger
def test_build_general_ledger():
    """
    Unit test for function build_general_ledger.
    """

    ## Define a variable which is the aggregation of all test dates.
    test_dates = set()

    ## Define test date range.
    date_range = DateRange(datetime.date.today() - datetime.timedelta(days=100), datetime.date.today())

    ## Define test balances.

# Generated at 2022-06-14 04:28:11.440004
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .accounts import AccountType
    from .journaling import Posting, Entry

    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))
    entry = Entry(datetime.date(2020, 1, 1), "Sample Journal", [
        Posting(1, 1, Amount(100), Account(100, AccountType.ASSET)),
        Posting(-1, 1, Amount(100), Account(200, AccountType.EXPENSE))
    ])
    journal = [entry]
    initial = {Account(100, AccountType.ASSET): Balance(datetime.date(2020, 1, 1), Quantity(0))}
    gl = build_general_ledger(period, journal, initial)
    assert len(gl.ledgers) == 2

# Generated at 2022-06-14 04:28:25.124597
# Unit test for function build_general_ledger
def test_build_general_ledger():
    import datetime
    from ..commons.numbers import BasicCurrencies
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountType
    from .journaling import JournalEntry, Posting

    ## Some test accounts:
    class Cash(Account):
        """
        Cash account.
        """

        def __init__(self) -> None:
            super().__init__(
                "Cash",
                AccountType.asset,
                BasicCurrencies.USD,
                True,
                True,
            )


    class Equipment(Account):
        """
        Equipment account.
        """


# Generated at 2022-06-14 04:28:30.064878
# Unit test for method add of class Ledger
def test_Ledger_add():
    l = Ledger(Account('12345'), Balance(Quantity(Decimal(0))))
    l.add(Posting(DateRange(), Account('1234'), Amount(Decimal(5000.00))))
    assert l.entries[0].balance == Quantity(Decimal(5000.00))


# Generated at 2022-06-14 04:28:55.891927
# Unit test for method add of class Ledger
def test_Ledger_add():
    from golf.journaling import Journal, JournalEntry, Posting
    from golf.accounts import Account, NonTerminalAccount, TerminalAccount
    from golf.commons.numbers import Quantity

    from golf.gl import build_general_ledger, GeneralLedger, Ledger, LedgerEntry

    # Create test accounts
    account1=Account(id='Asset',name='Asset',account_type='Asset')
    account2=Account(id='Equity',name='Equity',account_type='Equity')
    account3=Account(id='Liab',name='Liab',account_type='Liability')
    account4=Account(id='Revenue',name='Revenue',account_type='Revenue')
    account5=Account(id='Expense',name='Expense',account_type='Expense')

    # Create test postings
    posting

# Generated at 2022-06-14 04:29:05.589523
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from io import StringIO
    from copy import copy
    from dataclasses import asdict
    import datetime

    from ..commons.numbers import BaseCurrency

    from .accounts import Account, AccountInfo
    from .journaling import JournalEntry, Posting
    from .reporting import ReportingPeriod

    ## Initialize a journal entry:
    cash_account = Account(AccountInfo("Cash", True, False, False))
    bank_account = Account(AccountInfo("Bank", True, True, False), alias="Cash")

# Generated at 2022-06-14 04:29:15.863384
# Unit test for method add of class Ledger
def test_Ledger_add():
    T = TypeVar("T")
    from .journaling import JournalEntry, Posting

    debit = Posting(
        Account(1000, "Debit account"), 1, JournalEntry(datetime.datetime(2018, 12, 31), "Debit entry")
    )
    credit = Posting(
        Account(2000, "Credit account"), -1, JournalEntry(datetime.datetime(2018, 12, 31), "Credit entry")
    )

    ledger = Ledger(Account(1000), Balance(datetime.date(2018, 12, 31), Quantity(Decimal(100))))

    debit_entry = ledger.add(debit)
    credit_entry = ledger.add(credit)

    print(debit_entry.balance)
    print(credit_entry.balance)


# Tests for method build_general_ledger of module general_led

# Generated at 2022-06-14 04:29:25.409756
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from datetime import date
    from dateutil.relativedelta import relativedelta
    from ..commons.zeitgeist import Month, Quarter, Year
    from ..journaling.monetary import MonetaryJournal

    # We initialize a financial period and an initial balance
    book_closing = date(2016, 1, 1)
    initial_balance = {11100100: Balance(book_closing - relativedelta(years=1), Quantity(1000))}

    # We generate sample journal entries
    journal_1 = MonetaryJournal(
        date(2015, 1, 1),
        "Description 1",
        [
            Posting(11100100, Amount(100.0, "USD"), False),
            Posting(11100200, Amount(100.0, "USD"), True),
        ]
    )

# Generated at 2022-06-14 04:29:37.362949
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    ## Define algebra for loading balances:
    def read_initial_balances(period):
        return {
            Account("A", 1): Balance(period.since, Quantity(Decimal(20))),
            Account("B", 2): Balance(period.since, Quantity(Decimal(30))),
        }

    ## Define algebra for loading journal entries:

# Generated at 2022-06-14 04:29:46.271584
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from ..financials.hongkong import HKMA
    from ..financials.hongkong.hkd import HKD

    from ..algebras import read_initial_balances
    from ..algebras.journal_entries import read_journal_entries

    from .journaling import build_journal
    from .accounts import validate_account, build_account

    from datetime import date

    @dataclass
    class Transaction:
        date: date
        debit_account: str = ""
        debit_amount: Amount = Amount(0)
        credit_account: str = ""
        credit_amount: Amount = Amount(0)
        narrative: str = "Transaction"


# Generated at 2022-06-14 04:29:59.710689
# Unit test for method add of class Ledger
def test_Ledger_add():
    ## Import:
    from .accounts import Account

    ## Instantiate ledger:
    ledger = Ledger(Account.parse("A1"), Balance(datetime.date(2018, 1, 1), Quantity(Decimal(0))))

    ## Add posting:
    posting = Posting(datetime.date(2018, 1, 2), Account.parse("A1-2"), Amount(Decimal(100)), +1)
    ledger.add(posting)

    ## Verify:
    assert len(ledger.entries) == 1
    assert ledger.entries[0].posting == posting
    assert ledger.entries[0].balance == Quantity(Decimal(100))

    ## Add another posting:

# Generated at 2022-06-14 04:30:04.958883
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():

    # Stub implementation of read_initial_balances
    def read_initial_balances(period: DateRange) -> InitialBalances:
        pass

    # Stub implementation of read_journal_entries
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        pass

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)

    assert callable(program)
    assert program(DateRange(datetime.date(2014, 12, 31), datetime.date(2015, 12, 31)))

# Generated at 2022-06-14 04:30:11.452679
# Unit test for method add of class Ledger
def test_Ledger_add():
    from ..accounts.data import Account as A
    from ..journaling.data import JournalEntry as JE, Posting as P

    ledger = Ledger(A("bank", [], "Bank Account"), Balance(datetime.date(2020, 1, 1), Quantity(Decimal(1000))))

    # add new ledger entry, debt
    assert ledger.add(P(A("bank", [], "Bank Account"), JE(datetime.date(2020, 1, 2), "Debt", [P(A("bank", [], "Bank Account"), Decimal(100))]))) == LedgerEntry(ledger, P(A("bank", [], "Bank Account"), JE(datetime.date(2020, 1, 2), "Debt", [P(A("bank", [], "Bank Account"), Decimal(100))])), Quantity(1100))
    # add

# Generated at 2022-06-14 04:30:11.987048
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    pass

# Generated at 2022-06-14 04:30:55.344668
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    class _ReadInitialBalances_Impl(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("D100"): Balance(period.since, Quantity(100)), Account("D101"): Balance(period.since, Quantity(125))}

    read_initial_balances = _ReadInitialBalances_Impl()

    #: Accounting period.
    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 12, 31))

    assert read_initial_balances(period) == {Account("D100"): Balance(period.since, Quantity(100)), Account("D101"): Balance(period.since, Quantity(125))}


# Generated at 2022-06-14 04:31:05.629654
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Set current date
    currentDate = datetime.datetime.now()
    # Create dictionary of initial balances for terminal accounts
    initialBalances = {}
    # Dictionary of journal entries
    journalEntries = {}
    # Set accounting period
    period = DateRange(currentDate, currentDate)
    # Set initial balance for account "Rent"
    initialBalances["Rent"] = Balance(period.since, Quantity(Decimal(0)))
    # Create journal entry with id "12345", date currentDate, and description "Received rent"
    journalEntries["12345"] = JournalEntry(currentDate, "Received rent")
    # Add posting to account "Rent" with debit amount $1000
    journalEntries["12345"].post(Account("Rent"), Decimal(1000), "Received rent")
    # Create ledger of account "

# Generated at 2022-06-14 04:31:12.958931
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from .algebras import ReadInitialBalancesTestImpl, ReadJournalEntriesTestImpl

    ## Create instances of algebras:
    initial_balances_impl = ReadInitialBalancesTestImpl()
    journal_entries_impl = ReadJournalEntriesTestImpl()

    ## Compile the program:
    program_impl = compile_general_ledger_program(
        read_initial_balances=initial_balances_impl, read_journal_entries=journal_entries_impl
    )

    ## Call the program and ensure we get an instance of class GeneralLedger
    period = DateRange(since=datetime.date(2019, 1, 1), until=datetime.date(2019, 1, 31))
    assert isinstance(program_impl(period), GeneralLedger)



# Generated at 2022-06-14 04:31:23.653533
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    """
    This is a unit test for the function compile_general_ledger_program.
    """
    def _read_initial_balances(period: DateRange) -> InitialBalances:
        """
        A dummy implementation of the algebra ReadInitialBalances.
        """
        ## Nothing to do here.
        pass

    def _read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        """
        A dummy implementation of the algebra ReadJournalEntries.
        """
        ## Nothing to do here.
        pass

    ## Check that we get an instance of GeneralLedgerProgram as a result.
    assert isinstance(compile_general_ledger_program(_read_initial_balances, _read_journal_entries), GeneralLedgerProgram)

# Generated at 2022-06-14 04:31:32.822790
# Unit test for method add of class Ledger
def test_Ledger_add():
    from .journaling import Journal, Posting
    a = Account('some_account_name')
    l = Ledger[str](a, Balance(datetime.date(2019, 1, 1), Decimal(10)))
    j = Journal[str]('some_journal', 'some_description', datetime.date(2019, 1, 2))
    p = Posting[str](j, a, Decimal(10))
    l.add(p)
    assert(len(l.entries) == 1)

# Generated at 2022-06-14 04:31:34.646861
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Create test data
    #ledger =
    #posting =
    # Run the method
    #ledger.add(posting)
    # Make the tests
    assert True


# Generated at 2022-06-14 04:31:43.805655
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    @dataclass
    class _FakeReadInitialBalances(ReadInitialBalances):
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("A"): Balance(period.since, Quantity(0))}

    @dataclass
    class _FakeReadJournalEntries(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return []

    program = compile_general_ledger_program(
        _FakeReadInitialBalances(),
        _FakeReadJournalEntries(),
    )

    general_ledger = program(DateRange(datetime.date(2010, 1, 1), datetime.date(2010, 12, 31)))


# Generated at 2022-06-14 04:31:55.570741
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Execute callable
    acc = Account("Account")
    bal = Balance(datetime.date(2019, 1, 1), Quantity(Decimal(0)))
    posting = Posting(datetime.date(2020, 10, 1), JournalEntry("Description", [Posting(datetime.date(2020, 10, 1), "Account", Amount(Decimal(10)))]), acc, Amount(Decimal(10)))

    ldr = Ledger(acc, bal)
    ldr.add(posting)

    # Validate outcome
    assert ldr.entries[0].ledger == ldr
    assert ldr.entries[0].posting == posting
    assert ldr.entries[0].balance == posting.amount
    assert ldr.entries[0].date == datetime.date(2020, 10, 1)

# Generated at 2022-06-14 04:32:08.336225
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2022-06-14 04:32:11.442782
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Unit test for method __call__ of class ReadInitialBalances.
    """


# Generated at 2022-06-14 04:33:32.380678
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from .journaling import Posting, JournalEntry

    from ..commons.numbers import Amount

    from .accounts import Account

    from .generic import Balance

    from .books.journal import Journal, CreateJournalEntry


    j = Journal()
    CreateJournalEntry(j, datetime.date(2018, 2, 1), 'desc', [Posting(Account('A1'), Amount(100))])
    CreateJournalEntry(j, datetime.date(2018, 2, 9), 'desc', [Posting(Account('A2'), Amount(200))])
    CreateJournalEntry(j, datetime.date(2018, 2, 11), 'desc', [Posting(Account('A2'), Amount(300))])