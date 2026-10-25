

# Generated at 2026-10-24 21:40:54.050068
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:40:56.477667
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:40:58.898906
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:41:01.314982
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:41:03.729748
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:41:06.146684
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:41:08.564773
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:41:10.990926
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:41:13.406582
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:41:15.825158
# Unit test for constructor of class GeneralLedger

# Generated at 2026-10-24 21:41:18.238426
# Unit test for constructor of class GeneralLedger

# Generated at 2026-10-24 21:41:20.657144
# Unit test for constructor of class GeneralLedger

# Generated at 2026-10-24 21:41:23.074924
# Unit test for constructor of class LedgerEntry

# Generated at 2026-10-24 21:41:40.287383
# Unit test for constructor of class LedgerEntry
def test_LedgerEntry():
    from types import SimpleNamespace

    ledger = SimpleNamespace(account="cash")

    debit_direction = SimpleNamespace(value=1)
    credit_direction = SimpleNamespace(value=-1)

    journal = SimpleNamespace(
        description="Office supplies purchase",
        postings=[
            SimpleNamespace(account="cash", direction=debit_direction),
            SimpleNamespace(account="expenses", direction=credit_direction),
        ],
    )

    posting = SimpleNamespace(
        date=datetime.date(2023, 1, 15),
        journal=journal,
        amount=Decimal("100.00"),
        direction=debit_direction,
        is_debit=True,
        is_credit=False,
    )

    entry = LedgerEntry(ledger, posting, Decimal("150.00"))

    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Decimal("150.00")
    assert entry.date == datetime.date(2023, 1, 15)
    assert entry.description == "Office supplies purchase"
    assert entry.amount == Decimal("100.00")
    assert entry.is_debit is True
    assert entry.is_credit is False
    assert entry.debit == Decimal("100.00")
    assert entry.credit is None
    assert entry.cntraccts == ["expenses"]

# Generated at 2026-10-24 21:41:41.634451
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-24 21:42:03.304055
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from enum import Enum
    from types import SimpleNamespace

    class Direction(Enum):
        DEBIT = 1
        CREDIT = -1

    period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 1, 31),
    )

    cash = "cash"
    expenses = "expenses"
    retained_earnings = "retained-earnings"
    excluded_account = "excluded"

    initial_cash = Balance(
        period.since,
        Quantity(Decimal("100.00")),
    )
    initial_retained_earnings = Balance(
        period.since,
        Quantity(Decimal("50.00")),
    )

    initial = {
        cash: initial_cash,
        retained_earnings: initial_retained_earnings,
    }

    cash_debit = SimpleNamespace(
        account=cash,
        amount=Decimal("25.00"),
        direction=Direction.DEBIT,
    )
    cash_credit = SimpleNamespace(
        account=cash,
        amount=Decimal("10.00"),
        direction=Direction.CREDIT,
    )
    expense_debit = SimpleNamespace(
        account=expenses,
        amount=Decimal("7.50"),
        direction=Direction.DEBIT,
    )
    excluded_posting = SimpleNamespace(
        account=excluded_account,
        amount=Decimal("999.00"),
        direction=Direction.DEBIT,
    )

    journal = [
        SimpleNamespace(
            date=period.since - datetime.timedelta(days=1),
            postings=[excluded_posting],
        ),
        SimpleNamespace(
            date=period.since,
            postings=[cash_debit],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 1, 15),
            postings=[expense_debit],
        ),
        SimpleNamespace(
            date=period.until,
            postings=[cash_credit],
        ),
    ]

    result = module_0.build_general_ledger(period, journal, initial)

    assert result.period == period
    assert set(result.ledgers) == {cash, expenses, retained_earnings}
    assert excluded_account not in result.ledgers

    cash_ledger = result.ledgers[cash]
    assert cash_ledger.initial is initial_cash
    assert [entry.posting for entry in cash_ledger.entries] == [
        cash_debit,
        cash_credit,
    ]
    assert [entry.balance for entry in cash_ledger.entries] == [
        Quantity(Decimal("125.00")),
        Quantity(Decimal("115.00")),
    ]

    expense_ledger = result.ledgers[expenses]
    assert expense_ledger.initial.value == Quantity(Decimal("0"))
    assert expense_ledger.initial.date == period.since
    assert len(expense_ledger.entries) == 1
    assert expense_ledger.entries[0].posting is expense_debit
    assert expense_ledger.entries[0].balance == Quantity(Decimal("7.50"))

    retained_earnings_ledger = result.ledgers[retained_earnings]
    assert retained_earnings_ledger.initial is initial_retained_earnings
    assert retained_earnings_ledger.entries == []

# Generated at 2026-10-24 21:42:05.716200
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:42:08.131631
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:42:10.549160
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:42:12.967731
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:42:15.543257
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:42:17.960650
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:42:20.537262
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:42:22.950502
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:42:25.371926
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:42:26.729584
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest.mock import Mock

    ## ReadInitialBalances is a Protocol: it cannot be instantiated, so the
    ## contract is exercised through a concrete implementation fed to the program.
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    account = Mock(spec=Account)
    balance = Balance(period.since, Quantity(Decimal("100")))

    seen = []

    def read_initial_balances(p):
        seen.append(p)
        return {account: balance}

    def read_journal_entries(p):
        return []

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    ledger = program(period)

    ## Called exactly once, with the exact period object passed in.
    assert seen == [period]

    ## Returned balances became the ledgers' opening balances.
    assert ledger.period is period
    assert ledger.ledgers[account].initial is balance
    assert ledger.ledgers[account].entries == []

# Generated at 2026-10-24 21:42:57.566823
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Arrange: ledger opening at 100, no entries yet.
    ledger = Ledger(Mock(name="account"), Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))))
    assert ledger.entries == []

    debit = Mock(name="debit_posting")
    debit.amount = Quantity(Decimal("50"))
    debit.direction = Mock(value=1)

    credit = Mock(name="credit_posting")
    credit.amount = Quantity(Decimal("30"))
    credit.direction = Mock(value=-1)

    # Act
    first = ledger.add(debit)
    second = ledger.add(credit)

    # Assert: appended in order, wired to ledger + posting, running balance correct.
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 21:42:59.987037
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:43:02.403779
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:43:04.819739
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:43:07.237858
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:43:09.653788
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:43:12.072238
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:43:14.639327
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:43:17.053428
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:43:19.471351
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:43:21.889518
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:43:24.307016
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:43:26.725187
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:43:29.141746
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:43:31.558487
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:43:33.981413
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:43:36.397020
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:43:38.813405
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:43:41.229222
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:43:43.644349
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:43:46.061957
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:43:48.478938
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:43:50.896639
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:43:53.315378
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:43:55.732914
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:43:57.097049
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-24 21:44:08.434128
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from unittest.mock import Mock

    period = Mock(spec=DateRange)
    account = Mock(spec=Account)
    initial_balance = Mock(spec=Balance)

    read_initial_balances = Mock(return_value={account: initial_balance})
    read_journal_entries = Mock(return_value=[])

    program = module_0.compile_general_ledger_program(
        read_initial_balances,
        read_journal_entries,
    )
    result = program(period)

    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)

    assert isinstance(result, GeneralLedger)
    assert result.period is period
    assert set(result.ledgers) == {account}
    assert result.ledgers[account].account is account
    assert result.ledgers[account].initial is initial_balance
    assert result.ledgers[account].entries == []

# Generated at 2026-10-24 21:44:09.760353
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-24 21:44:11.083237
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest.mock import Mock

    ## ReadInitialBalances is a Protocol: it cannot be instantiated, so the
    ## contract is exercised through a concrete implementation fed to the program.
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    account = Mock(spec=Account)
    balance = Balance(period.since, Quantity(Decimal("100")))

    seen = []

    def read_initial_balances(p):
        seen.append(p)
        return {account: balance}

    def read_journal_entries(p):
        return []

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    ledger = program(period)

    ## Called exactly once, with the exact period object passed in.
    assert seen == [period]

    ## Returned balances became the ledgers' opening balances.
    assert ledger.period is period
    assert ledger.ledgers[account].initial is balance
    assert ledger.ledgers[account].entries == []

# Generated at 2026-10-24 21:45:52.377908
# Unit test for method add of class Ledger
def test_Ledger_add():
    class Direction:
        def __init__(self, value: int):
            self.value = value

    class StubPosting:
        def __init__(self, amount: Decimal, direction: Direction):
            self.amount = amount
            self.direction = direction

    initial_balance = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(object(), initial_balance)

    debit_posting = StubPosting(Decimal("25.50"), Direction(1))
    debit_entry = ledger.add(debit_posting)  # type: ignore[arg-type]

    assert debit_entry.ledger is ledger
    assert debit_entry.posting is debit_posting
    assert debit_entry.balance == Quantity(Decimal("125.50"))
    assert len(ledger.entries) == 1
    assert ledger.entries[0] is debit_entry

    # A subsequent entry must use the previous entry's balance.
    credit_posting = StubPosting(Decimal("10.00"), Direction(-1))
    credit_entry = ledger.add(credit_posting)  # type: ignore[arg-type]

    assert credit_entry.balance == Quantity(Decimal("115.50"))
    assert len(ledger.entries) == 2
    assert ledger.entries[1] is credit_entry

# Generated at 2026-10-24 21:45:54.799048
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:45:57.216404
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:45:59.635208
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:46:22.573260
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from datetime import date
    from decimal import Decimal

    from ..commons.numbers import Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account, AccountType
    from .generic import Balance

    ## Prepare the accounting period:
    period = DateRange(date(2023, 1, 1), date(2023, 12, 31))

    ## Prepare an account and its expected opening balance:
    account = Account(1, AccountType.DEBIT, "Test Account")
    expected_balance = Balance(period.since, Quantity(Decimal("1000")))

    ## Define a fake implementation conforming to the ReadInitialBalances protocol:
    class _FakeReadInitialBalances:
        """
        Fake implementation of the initial-balances algebra.
        """

        def module_0.__call__(self, period: DateRange) -> InitialBalances:
            """
            Returns the initial balances for the given period.
            """
            return {account: expected_balance}

    ## Instantiate the fake reader:
    read_initial_balances = _FakeReadInitialBalances()

    ## Invoke the protocol method:
    initial_balances = read_initial_balances(period)

    ## Assert the result is a dictionary (InitialBalances):
    assert isinstance(initial_balances, dict)

    ## Assert the account is present as a key:
    assert account in initial_balances

    ## Assert the balance value and date are as expected:
    balance = initial_balances[account]
    assert isinstance(balance, Balance)
    assert balance.value == Quantity(Decimal("1000"))
    assert balance.date == period.since

# Generated at 2026-10-24 21:46:52.676708
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:46:55.095564
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:46:57.512883
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:46:59.929369
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:47:18.072327
# Unit test for function build_general_ledger
def test_build_general_ledger():from datetime import date

# Generated at 2026-10-24 21:47:19.405484
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest.mock import Mock

    ## ReadInitialBalances is a Protocol: it cannot be instantiated, so the
    ## contract is exercised through a concrete implementation fed to the program.
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    account = Mock(spec=Account)
    balance = Balance(period.since, Quantity(Decimal("100")))

    seen = []

    def read_initial_balances(p):
        seen.append(p)
        return {account: balance}

    def read_journal_entries(p):
        return []

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    ledger = program(period)

    ## Called exactly once, with the exact period object passed in.
    assert seen == [period]

    ## Returned balances became the ledgers' opening balances.
    assert ledger.period is period
    assert ledger.ledgers[account].initial is balance
    assert ledger.ledgers[account].entries == []

# Generated at 2026-10-24 21:47:20.838055
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest.mock import Mock

    ## ReadInitialBalances is a Protocol: it cannot be instantiated, so the
    ## contract is exercised through a concrete implementation fed to the program.
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    account = Mock(spec=Account)
    balance = Balance(period.since, Quantity(Decimal("100")))

    seen = []

    def read_initial_balances(p):
        seen.append(p)
        return {account: balance}

    def read_journal_entries(p):
        return []

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    ledger = program(period)

    ## Called exactly once, with the exact period object passed in.
    assert seen == [period]

    ## Returned balances became the ledgers' opening balances.
    assert ledger.period is period
    assert ledger.ledgers[account].initial is balance
    assert ledger.ledgers[account].entries == []

# Generated at 2026-10-24 21:47:22.162224
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest.mock import Mock

    ## ReadInitialBalances is a Protocol: it cannot be instantiated, so the
    ## contract is exercised through a concrete implementation fed to the program.
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    account = Mock(spec=Account)
    balance = Balance(period.since, Quantity(Decimal("100")))

    seen = []

    def read_initial_balances(p):
        seen.append(p)
        return {account: balance}

    def read_journal_entries(p):
        return []

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    ledger = program(period)

    ## Called exactly once, with the exact period object passed in.
    assert seen == [period]

    ## Returned balances became the ledgers' opening balances.
    assert ledger.period is period
    assert ledger.ledgers[account].initial is balance
    assert ledger.ledgers[account].entries == []

# Generated at 2026-10-24 21:47:24.583518
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:47:27.001392
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:47:29.418626
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:47:31.835320
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:47:34.254147
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:47:36.669594
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:47:39.087033
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:47:41.506923
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:47:43.923050
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:47:46.341612
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:47:48.754620
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:47:51.175113
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:47:53.590499
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:47:56.008400
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:47:58.427040
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:48:00.845327
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:48:03.263809
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:48:05.679616
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:48:08.100266
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:48:10.513512
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:48:12.931512
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 21:48:15.350250
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:48:17.767188
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:48:20.185520
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:48:22.600882
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:48:25.017850
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:48:27.436768
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:48:29.854891
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:48:32.272533
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:48:34.688821
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:48:51.155340
# Unit test for method add of class Ledger
def test_Ledger_add():
    # Arrange: ledger opening at 100, no entries yet.
    ledger = Ledger(Mock(name="account"), Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))))
    assert ledger.entries == []

    debit = Mock(name="debit_posting")
    debit.amount = Quantity(Decimal("50"))
    debit.direction = Mock(value=1)

    credit = Mock(name="credit_posting")
    credit.amount = Quantity(Decimal("30"))
    credit.direction = Mock(value=-1)

    # Act
    first = ledger.add(debit)
    second = ledger.add(credit)

    # Assert: appended in order, wired to ledger + posting, running balance correct.
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 21:49:22.387571
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace

    initial_balance = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account=object(), initial=initial_balance)

    posting = SimpleNamespace(
        amount=Decimal("25.00"),
        direction=SimpleNamespace(value=Decimal("1")),
    )

    entry = ledger.add(posting)

    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("125.00"))
    assert ledger.entries == [entry]

# Generated at 2026-10-24 21:49:24.808982
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:49:27.228642
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:49:29.645947
# Unit test for function build_general_ledger

# Generated at 2026-10-24 21:49:32.064528
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:49:34.481882
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:49:36.899258
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 21:49:39.316909
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:49:41.736263
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:49:44.154397
# Unit test for method add of class Ledger

# Generated at 2026-10-24 21:49:46.571760
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 21:49:48.988620
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 21:49:51.405342
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 21:49:53.821585
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 21:49:56.238969
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 21:49:58.657090
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 21:50:23.728427
# Unit test for method add of class Ledger
def test_Ledger_add():
    from unittest.mock import Mock

    account = Mock(spec=Account)
    initial = Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100.00")))
    ledger = Ledger(account, initial)

    posting = Mock(spec=Posting)
    posting.amount = Amount(Decimal("25.50"))
    posting.direction.value = Decimal("1")

    entry = ledger.add(posting)

    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("125.50"))
    assert ledger.entries == [entry]
    assert ledger._last_balance == Quantity(Decimal("125.50"))

# Generated at 2026-10-24 21:50:56.288335
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace

    initial_balance = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account=SimpleNamespace(), initial=initial_balance)

    posting = SimpleNamespace(
        amount=Amount(Decimal("25.50")),
        direction=SimpleNamespace(value=Decimal("1")),
    )

    entry = ledger.add(posting)

    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("125.50"))
    assert ledger.entries == [entry]
    assert ledger._last_balance == Quantity(Decimal("125.50"))