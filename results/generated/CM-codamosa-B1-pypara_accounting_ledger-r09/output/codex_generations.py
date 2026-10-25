

# Generated at 2026-10-24 22:09:52.220431
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from enum import Enum
    from types import SimpleNamespace

    class Direction(Enum):
        DEBIT = 1
        CREDIT = -1

    def quantity(value: str) -> Quantity:
        return Quantity(Decimal(value))

    def amount(value: str) -> Amount:
        return Amount(Decimal(value))

    def make_posting(account, value: str, direction: Direction):
        return SimpleNamespace(
            account=account,
            amount=amount(value),
            direction=direction,
        )

    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 1, 31),
    )

    cash_account = object()
    sales_account = object()
    opening_only_account = object()
    outside_period_account = object()

    cash_initial = Balance(datetime.date(2023, 12, 31), quantity("100"))
    opening_only_initial = Balance(datetime.date(2023, 12, 31), quantity("75"))

    initial = {
        cash_account: cash_initial,
        opening_only_account: opening_only_initial,
    }

    opening_debit = make_posting(cash_account, "25", Direction.DEBIT)
    cash_credit = make_posting(cash_account, "10", Direction.CREDIT)
    sales_credit = make_posting(sales_account, "40", Direction.CREDIT)
    before_period = make_posting(outside_period_account, "50", Direction.DEBIT)
    after_period = make_posting(outside_period_account, "60", Direction.DEBIT)

    journal = [
        SimpleNamespace(
            date=datetime.date(2023, 12, 31),
            postings=[before_period],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 1, 1),
            postings=[opening_debit],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 1, 15),
            postings=[cash_credit],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 1, 31),
            postings=[sales_credit],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 2, 1),
            postings=[after_period],
        ),
    ]

    result = module_0.build_general_ledger(period, journal, initial)

    assert result.period == period

# Generated at 2026-10-24 22:10:08.702778
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

# Generated at 2026-10-24 22:10:18.164125
# Unit test for constructor of class GeneralLedger
def test_GeneralLedger():
    period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 12, 31),
    )
    ledgers = {}

    general_ledger = GeneralLedger(period=period, ledgers=ledgers)

    assert general_ledger.period == period
    assert general_ledger.ledgers is ledgers

# Generated at 2026-10-24 22:10:34.510197
# Unit test for constructor of class LedgerEntry
def test_LedgerEntry():
    from unittest.mock import Mock

    ## -- Case 1: DEBIT entry.

    ## Fake the posting and its parent journal:
    posting = Mock()
    posting.date = datetime.date(2023, 5, 1)
    posting.amount = Amount(Decimal("100.00"))
    posting.direction = 1  # debit direction
    posting.is_debit = True
    posting.is_credit = False
    posting.journal.description = "Sale of goods"

    ## Counter-posting sits on the same journal with opposite direction:
    counter_posting = Mock()
    counter_posting.direction = -1
    counter_posting.account = "ACCOUNT-2"
    posting.journal.postings = [posting, counter_posting]

    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Quantity(Decimal("150.00")))

    ## Verify constructor stored the balance:
    assert entry.balance == Quantity(Decimal("150.00"))
    assert entry.ledger is not None

    ## Verify delegated properties:
    assert entry.date == datetime.date(2023, 5, 1)
    assert entry.description == "Sale of goods"
    assert entry.amount == Amount(Decimal("100.00"))
    assert entry.is_debit is True
    assert entry.is_credit is False
    assert entry.debit == Amount(Decimal("100.00"))
    assert entry.credit is None

    ## Verify counter accounts exclude same-direction postings:
    assert entry.cntraccts == ["ACCOUNT-2"]

    ## -- Case 2: CREDIT entry.

    posting = Mock()
    posting.date = datetime.date(2023, 5, 2)
    posting.amount = Amount(Decimal("40.00"))
    posting.direction = -1  # credit direction
    posting.is_debit = False
    posting.is_credit = True
    posting.journal.description = "Bank charge"
    posting.journal.postings = [posting]  # no counter postings

    entry = LedgerEntry(ledger=Mock(), posting=posting, balance=Quantity(Decimal("110.00")))

    assert entry.is_debit is False
    assert entry.is_credit is True
    assert entry.debit is None
    assert entry.credit == Amount(Decimal("40.00"))
    assert entry.cntraccts == []  # nothing with a different direction

# Generated at 2026-10-24 22:10:36.940093
# Unit test for constructor of class Ledger

# Generated at 2026-10-24 22:10:39.354434
# Unit test for constructor of class Ledger

# Generated at 2026-10-24 22:10:41.773247
# Unit test for constructor of class Ledger

# Generated at 2026-10-24 22:10:44.190694
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 22:10:46.611359
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 22:10:49.029803
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 22:10:51.449219
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:10:53.865786
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:10:56.283282
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:11:50.796686
# Unit test for function build_general_ledger

# Generated at 2026-10-24 22:12:12.560578
# Unit test for function build_general_ledger
def test_build_general_ledger():from datetime import date

# Generated at 2026-10-24 22:12:22.848748
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:12:25.518645
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:12:28.171264
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:12:59.611014
# Unit test for method add of class Ledger
def test_Ledger_add():
    initial = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account=object(), initial=initial)

    debit_posting = SimpleNamespace(
        amount=Decimal("25.00"),
        direction=SimpleNamespace(value=Decimal("1")),
    )
    credit_posting = SimpleNamespace(
        amount=Decimal("10.00"),
        direction=SimpleNamespace(value=Decimal("-1")),
    )

    debit_entry = ledger.add(debit_posting)
    credit_entry = ledger.add(credit_posting)

    assert debit_entry.ledger is ledger
    assert debit_entry.posting is debit_posting
    assert debit_entry.balance == Quantity(Decimal("125.00"))

    assert credit_entry.ledger is ledger
    assert credit_entry.posting is credit_posting
    assert credit_entry.balance == Quantity(Decimal("115.00"))

    assert ledger.entries == [debit_entry, credit_entry]

# Generated at 2026-10-24 22:13:15.585790
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    read_initial_balances = Mock(return_value=sentinel.initial_balances)
    read_journal_entries = Mock(return_value=sentinel.journal_entries)
    build = Mock(return_value=sentinel.general_ledger)

    with patch.dict(
        compile_general_ledger_program.__globals__,
        {"build_general_ledger": build},
    ):
        program = module_0.compile_general_ledger_program(
            read_initial_balances,
            read_journal_entries,
        )
        result = program(sentinel.period)

    read_initial_balances.assert_called_once_with(sentinel.period)
    read_journal_entries.assert_called_once_with(sentinel.period)
    build.assert_called_once_with(
        sentinel.period,
        sentinel.journal_entries,
        sentinel.initial_balances,
    )
    assert result is sentinel.general_ledger

# Generated at 2026-10-24 22:13:18.240148
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:13:20.959576
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:13:22.280985
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

# Generated at 2026-10-24 22:13:23.605153
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-24 22:13:54.087526
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = object()
    initial = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account, initial)

    posting = Mock()
    posting.amount = Amount(Decimal("25.00"))
    posting.direction.value = 1

    entry = ledger.add(posting)

    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("125.00"))
    assert ledger.entries == [entry]

# Generated at 2026-10-24 22:13:56.507565
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 22:13:58.925083
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 22:14:01.341876
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 22:14:18.222514
# Unit test for method add of class Ledger
def test_Ledger_add():from types import SimpleNamespace


# Generated at 2026-10-24 22:14:34.743240
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

# Generated at 2026-10-24 22:14:36.067324
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

# Generated at 2026-10-24 22:14:37.394989
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-24 22:15:04.027760
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from typing import cast

    account = cast(Account, object())
    initial_balance = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger: Ledger[object] = Ledger(account, initial_balance)

    debit_posting = cast(
        Posting[object],
        SimpleNamespace(
            amount=Amount(Decimal("25.00")),
            direction=SimpleNamespace(value=1),
        ),
    )
    credit_posting = cast(
        Posting[object],
        SimpleNamespace(
            amount=Amount(Decimal("10.00")),
            direction=SimpleNamespace(value=-1),
        ),
    )

    first_entry = ledger.add(debit_posting)
    second_entry = ledger.add(credit_posting)

    assert ledger.entries == [first_entry, second_entry]

    assert first_entry.ledger is ledger
    assert first_entry.posting is debit_posting
    assert first_entry.balance == Quantity(Decimal("125.00"))

    assert second_entry.ledger is ledger
    assert second_entry.posting is credit_posting
    assert second_entry.balance == Quantity(Decimal("115.00"))

    assert ledger._last_balance == Quantity(Decimal("115.00"))

# Generated at 2026-10-24 22:15:05.459526
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-24 22:15:34.644636
# Unit test for function build_general_ledger

# Generated at 2026-10-24 22:15:49.186951
# Unit test for function build_general_ledger
def test_build_general_ledger():period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 12, 31),
    )


# Generated at 2026-10-24 22:15:50.511607
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-24 22:15:51.843219
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

# Generated at 2026-10-24 22:15:53.164820
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

# Generated at 2026-10-24 22:16:18.266769
# Unit test for method add of class Ledger
def test_Ledger_add():
    account = cast(Account, object())
    initial = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account, initial)

    posting = cast(
        Posting[object],
        SimpleNamespace(
            amount=Amount(Decimal("25.00")),
            direction=SimpleNamespace(value=Decimal("1")),
        ),
    )

    entry = ledger.add(posting)

    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("125.00"))
    assert ledger.entries == [entry]

# Generated at 2026-10-24 22:16:27.997059
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:16:30.643834
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:16:33.417610
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:16:49.910831
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

# Generated at 2026-10-24 22:16:52.328187
# Unit test for method add of class Ledger

# Generated at 2026-10-24 22:16:54.743782
# Unit test for method add of class Ledger

# Generated at 2026-10-24 22:16:57.164526
# Unit test for method add of class Ledger

# Generated at 2026-10-24 22:16:59.579918
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:17:01.997114
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:17:04.413743
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:17:06.833931
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 22:17:09.250910
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 22:17:11.671758
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 22:17:14.088214
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 22:17:16.506405
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 22:17:30.868934
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():import datetime


# Generated at 2026-10-24 22:17:51.448582
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from types import SimpleNamespace

    since = datetime.date(2024, 1, 1)
    until = datetime.date(2024, 1, 31)
    period = DateRange(since, until)

    cash_account = SimpleNamespace(number="1000")
    revenue_account = SimpleNamespace(number="4000")
    excluded_account = SimpleNamespace(number="9999")

    # SimpleNamespace is not hashable, so use stable hashable account doubles.
    cash_account = ("account", "1000")
    revenue_account = ("account", "4000")
    excluded_account = ("account", "9999")

    debit = SimpleNamespace(value=Decimal("1"))
    credit = SimpleNamespace(value=Decimal("-1"))

    cash_debit = SimpleNamespace(
        account=cash_account,
        amount=Amount(Decimal("25.00")),
        direction=debit,
    )
    cash_credit = SimpleNamespace(
        account=cash_account,
        amount=Amount(Decimal("10.00")),
        direction=credit,
    )
    revenue_credit = SimpleNamespace(
        account=revenue_account,
        amount=Amount(Decimal("40.00")),
        direction=credit,
    )
    excluded_posting = SimpleNamespace(
        account=excluded_account,
        amount=Amount(Decimal("500.00")),
        direction=debit,
    )

    journal = [
        SimpleNamespace(date=since, postings=[cash_debit]),
        SimpleNamespace(date=datetime.date(2024, 1, 15), postings=[cash_credit, revenue_credit]),
        SimpleNamespace(date=datetime.date(2024, 2, 1), postings=[excluded_posting]),
    ]

    initial = {
        cash_account: Balance(
            since,
            Quantity(Decimal("100.00")),
        )
    }

    result = module_0.build_general_ledger(period, journal, initial)

    assert result.period == period
    assert set(result.ledgers) == {cash_account, revenue_account}
    assert excluded_account not in result.ledgers

    cash_ledger = result.ledgers[cash_account]
    assert cash_ledger.initial == initial[cash_account]
    assert [entry.posting for entry in cash_ledger.entries] == [
        cash_debit,
        cash_credit,
    ]
    assert [entry.balance for entry in cash_ledger.entries] == [
        Quantity(Decimal("125.00")),
        Quantity(Decimal("115.00")),
    ]

    revenue_ledger = result.ledgers[revenue_account]
    assert revenue_ledger.initial.date == since
    assert revenue_ledger.initial.value == Quantity(Decimal("0"))
    assert len(revenue_ledger.entries) == 1
    assert revenue_ledger.entries[0].posting is revenue_credit
    assert revenue_ledger.entries[0].balance == Quantity(Decimal("-40.00"))

# Generated at 2026-10-24 22:17:52.773271
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-24 22:18:30.056145
# Unit test for method add of class Ledger
def test_Ledger_add():from types import SimpleNamespace
from typing import cast

# Generated at 2026-10-24 22:18:32.026628
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

# Generated at 2026-10-24 22:18:33.352728
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

# Generated at 2026-10-24 22:18:34.675634
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

# Generated at 2026-10-24 22:18:36.000494
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

# Generated at 2026-10-24 22:18:46.850641
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    period = Mock(spec=DateRange)
    initial_balances: InitialBalances = {}
    journal_entries = []

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)

    program = module_0.compile_general_ledger_program(
        read_initial_balances,
        read_journal_entries,
    )
    result = program(period)

    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)

    assert isinstance(result, GeneralLedger)
    assert result.period is period
    assert result.ledgers == {}

# Generated at 2026-10-24 22:19:10.916383
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from enum import Enum
    from types import SimpleNamespace

    class Direction(Enum):
        DEBIT = 1
        CREDIT = -1

    opening_date = datetime.date(2024, 1, 1)
    closing_date = datetime.date(2024, 1, 31)
    period = DateRange(since=opening_date, until=closing_date)

    cash_account = object()
    revenue_account = object()
    expense_account = object()
    unused_account = object()
    outside_account = object()

    cash_opening = Balance(opening_date, Quantity(Decimal("100")))
    unused_opening = Balance(opening_date, Quantity(Decimal("50")))
    initial = {
        cash_account: cash_opening,
        unused_account: unused_opening,
    }

    cash_debit = SimpleNamespace(
        account=cash_account,
        amount=Decimal("25"),
        direction=Direction.DEBIT,
    )
    revenue_credit = SimpleNamespace(
        account=revenue_account,
        amount=Decimal("25"),
        direction=Direction.CREDIT,
    )
    cash_credit = SimpleNamespace(
        account=cash_account,
        amount=Decimal("5"),
        direction=Direction.CREDIT,
    )
    expense_debit = SimpleNamespace(
        account=expense_account,
        amount=Decimal("5"),
        direction=Direction.DEBIT,
    )

    journal = [
        # These entries are outside the accounting period and must be ignored.
        SimpleNamespace(
            date=datetime.date(2023, 12, 31),
            postings=[
                SimpleNamespace(
                    account=outside_account,
                    amount=Decimal("999"),
                    direction=Direction.DEBIT,
                )
            ],
        ),
        # The period boundaries are inclusive.
        SimpleNamespace(
            date=opening_date,
            postings=[cash_debit, revenue_credit],
        ),
        SimpleNamespace(
            date=closing_date,
            postings=[cash_credit, expense_debit],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 2, 1),
            postings=[
                SimpleNamespace(
                    account=outside_account,
                    amount=Decimal("999"),
                    direction=Direction.CREDIT,
                )
            ],
        ),
    ]

    result = module_0.build_general_ledger(period, journal, initial)

    assert result.period == period

# Generated at 2026-10-24 22:19:13.504511
# Unit test for function build_general_ledger

# Generated at 2026-10-24 22:19:15.921281
# Unit test for function build_general_ledger

# Generated at 2026-10-24 22:19:18.343981
# Unit test for function build_general_ledger

# Generated at 2026-10-24 22:19:20.762205
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:19:23.466458
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 22:19:26.275369
# Unit test for function compile_general_ledger_program