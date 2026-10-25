

# Generated at 2026-10-25 03:34:07.793687
# Unit test for constructor of class LedgerEntry
def test_LedgerEntry():
    ledger = Mock()
    posting = Mock()
    balance = Quantity(Decimal("100.00"))

    entry = LedgerEntry(
        ledger=ledger,
        posting=posting,
        balance=balance,
    )

    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == balance

# Generated at 2026-10-25 03:34:15.778741
# Unit test for constructor of class LedgerEntry
def test_LedgerEntry():
    ledger = Mock(spec=Ledger)
    posting = Mock(spec=Posting)
    balance = Quantity(Decimal("125.50"))

    entry = LedgerEntry(
        ledger=ledger,
        posting=posting,
        balance=balance,
    )

    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == balance

# Generated at 2026-10-25 03:34:18.196909
# Unit test for method __repr__ of class Ledger

# Generated at 2026-10-25 03:34:20.611264
# Unit test for method __repr__ of class Ledger

# Generated at 2026-10-25 03:34:23.028433
# Unit test for method __repr__ of class Ledger

# Generated at 2026-10-25 03:34:34.461986
# Unit test for method __repr__ of class GeneralLedger
def test_GeneralLedger___repr__():
    class PeriodStub:
        def module_0.__repr__(self) -> str:
            return "PeriodStub()"

    ledger = GeneralLedger(period=PeriodStub(), ledgers={})

    assert repr(ledger) == "GeneralLedger(period=PeriodStub(), ledgers={})"

# Generated at 2026-10-25 03:34:56.232547
# Unit test for method __repr__ of class GeneralLedger
def test_GeneralLedger___repr__():ledger = GeneralLedger(period="period", ledgers={})

# Generated at 2026-10-25 03:35:15.752992
# Unit test for function build_general_ledger
def test_build_general_ledger():
    period = SimpleNamespace(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 1, 31),
    )

    cash_account = "cash"
    sales_account = "sales"

    opening_balance = Balance(
        period.since,
        Quantity(Decimal("100.00")),
    )
    initial = {cash_account: opening_balance}

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
    sales_credit = SimpleNamespace(
        account=sales_account,
        amount=Amount(Decimal("40.00")),
        direction=credit,
    )
    excluded_posting = SimpleNamespace(
        account=cash_account,
        amount=Amount(Decimal("999.00")),
        direction=debit,
    )

    journal = [
        SimpleNamespace(
            date=datetime.date(2024, 1, 10),
            postings=[cash_debit, cash_credit, sales_credit],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 2, 1),
            postings=[excluded_posting],
        ),
    ]

    result = module_0.build_general_ledger(period, journal, initial)

    assert result.period is period
    assert set(result.ledgers) == {cash_account, sales_account}

    cash_ledger = result.ledgers[cash_account]
    assert cash_ledger.initial is opening_balance
    assert [entry.posting for entry in cash_ledger.entries] == [
        cash_debit,
        cash_credit,
    ]
    assert [entry.balance for entry in cash_ledger.entries] == [
        Quantity(Decimal("125.00")),
        Quantity(Decimal("115.00")),
    ]

    sales_ledger = result.ledgers[sales_account]
    assert sales_ledger.initial.date == period.since
    assert sales_ledger.initial.value == Quantity(Decimal("0"))
    assert len(sales_ledger.entries) == 1
    assert sales_ledger.entries[0].posting is sales_credit
    assert sales_ledger.entries[0].balance == Quantity(Decimal("-40.00"))

# Generated at 2026-10-25 03:35:18.278147
# Unit test for method add of class Ledger

# Generated at 2026-10-25 03:35:20.811989
# Unit test for method add of class Ledger

# Generated at 2026-10-25 03:35:23.226296
# Unit test for method add of class Ledger

# Generated at 2026-10-25 03:35:25.641676
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:36:05.450743
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:36:08.228143
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:36:24.703065
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 12, 31),
    )
    expected: InitialBalances = {}
    received_periods: List[DateRange] = []

    class StubReadInitialBalances:
        def module_0.__call__(self, requested_period: DateRange) -> InitialBalances:
            received_periods.append(requested_period)
            return expected

    reader: ReadInitialBalances = StubReadInitialBalances()

    result = reader(period)

    assert result is expected
    assert received_periods == [period]

# Generated at 2026-10-25 03:36:41.188229
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-25 03:36:57.674677
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-25 03:37:07.709839
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 12, 31),
    )
    expected: InitialBalances = {}

    class StubReadInitialBalances:
        def module_0.__call__(self, requested_period: DateRange) -> InitialBalances:
            assert requested_period == period
            return expected

    reader: ReadInitialBalances = StubReadInitialBalances()

    result = reader(period)

    assert result is expected

# Generated at 2026-10-25 03:37:24.147536
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-25 03:37:50.514936
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from enum import Enum
    from types import SimpleNamespace

    class Direction(Enum):
        DEBIT = 1
        CREDIT = -1

    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 1, 31),
    )

    cash_account = object()
    sales_account = object()
    unused_account = object()
    outside_period_account = object()

    initial_cash_balance = Balance(
        period.since,
        Quantity(Decimal("100.00")),
    )
    initial_unused_balance = Balance(
        period.since,
        Quantity(Decimal("50.00")),
    )

    initial = {
        cash_account: initial_cash_balance,
        unused_account: initial_unused_balance,
    }

    cash_debit = SimpleNamespace(
        account=cash_account,
        amount=Amount(Decimal("25.00")),
        direction=Direction.DEBIT,
    )
    cash_credit = SimpleNamespace(
        account=cash_account,
        amount=Amount(Decimal("40.00")),
        direction=Direction.CREDIT,
    )
    sales_credit = SimpleNamespace(
        account=sales_account,
        amount=Amount(Decimal("60.00")),
        direction=Direction.CREDIT,
    )
    outside_period_posting = SimpleNamespace(
        account=outside_period_account,
        amount=Amount(Decimal("500.00")),
        direction=Direction.DEBIT,
    )

    journal = [
        SimpleNamespace(
            date=datetime.date(2023, 12, 31),
            postings=[outside_period_posting],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 1, 5),
            postings=[cash_debit],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 1, 10),
            postings=[cash_credit, sales_credit],
        ),
    ]

    result = module_0.build_general_ledger(period, journal, initial)

    assert result.period == period
    assert set(result.ledgers) == {
        cash_account,
        sales_account,
        unused_account,
    }
    assert outside_period_account not in result.ledgers

    cash_ledger = result.ledgers[cash_account]
    assert cash_ledger.initial is initial_cash_balance

# Generated at 2026-10-25 03:38:07.412947
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from typing import cast

    account = cast(Account, SimpleNamespace())
    initial_balance = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger: Ledger[None] = Ledger(account, initial_balance)

    posting = cast(
        Posting[None],
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

    # A subsequent entry must use the preceding entry's balance.
    second_posting = cast(
        Posting[None],
        SimpleNamespace(
            amount=Amount(Decimal("10.00")),
            direction=SimpleNamespace(value=Decimal("-1")),
        ),
    )

    second_entry = ledger.add(second_posting)

    assert second_entry.balance == Quantity(Decimal("115.00"))
    assert ledger.entries == [entry, second_entry]

# Generated at 2026-10-25 03:38:19.185313
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    period = Mock(spec=DateRange)
    initial_balances = {}
    journal_entries = [Mock(spec=JournalEntry)]
    expected_ledger = Mock(spec=GeneralLedger)

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)

    build_target = (
        f"{compile_general_ledger_program.__module__}.build_general_ledger"
    )

    with patch(build_target, return_value=expected_ledger) as build:
        program = module_0.compile_general_ledger_program(
            read_initial_balances,
            read_journal_entries,
        )

        result = program(period)

    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)
    build.assert_called_once_with(
        period,
        journal_entries,
        initial_balances,
    )
    assert result is expected_ledger

# Generated at 2026-10-25 03:38:26.266953
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-25 03:38:46.936990
# Unit test for method add of class Ledger
def test_Ledger_add():
    from unittest.mock import Mock

    ledger: Ledger[object] = Ledger(
        account=Mock(spec=Account),
        initial=Balance(
            datetime.date(2024, 1, 1),
            Quantity(Decimal("100")),
        ),
    )

    debit_posting: Posting[object] = Mock()
    debit_posting.amount = Amount(Decimal("25"))
    debit_posting.direction.value = Decimal("1")

    debit_entry = ledger.add(debit_posting)

    assert debit_entry.ledger is ledger
    assert debit_entry.posting is debit_posting
    assert debit_entry.balance == Quantity(Decimal("125"))
    assert ledger.entries == [debit_entry]

    credit_posting: Posting[object] = Mock()
    credit_posting.amount = Amount(Decimal("40"))
    credit_posting.direction.value = Decimal("-1")

    credit_entry = ledger.add(credit_posting)

    assert credit_entry.ledger is ledger
    assert credit_entry.posting is credit_posting
    assert credit_entry.balance == Quantity(Decimal("85"))
    assert ledger.entries == [debit_entry, credit_entry]

# Generated at 2026-10-25 03:39:02.194657
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from typing import cast

    account = cast(Account, object())
    initial = Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100.00")))
    ledger = Ledger(account, initial)

    posting = cast(
        Posting[object],
        SimpleNamespace(
            amount=Amount(Decimal("25.00")),
            direction=SimpleNamespace(value=Decimal("-1")),
        ),
    )

    entry = ledger.add(posting)

    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("75.00"))
    assert ledger.entries == [entry]
    assert ledger._last_balance == Quantity(Decimal("75.00"))

# Generated at 2026-10-25 03:39:28.208522
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from types import SimpleNamespace
    from typing import cast

    since = datetime.date(2024, 1, 1)
    until = datetime.date(2024, 1, 31)
    period = cast(DateRange, SimpleNamespace(since=since, until=until))


# Generated at 2026-10-25 03:39:30.627033
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:39:33.307646
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:39:36.086974
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:39:54.017213
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace

    initial_balance = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account=object(), initial=initial_balance)

    debit_posting = SimpleNamespace(
        amount=Amount(Decimal("25.00")),
        direction=SimpleNamespace(value=Decimal("1")),
    )

    debit_entry = ledger.add(debit_posting)

    assert debit_entry.ledger is ledger
    assert debit_entry.posting is debit_posting
    assert debit_entry.balance == Quantity(Decimal("125.00"))
    assert ledger.entries == [debit_entry]

    credit_posting = SimpleNamespace(
        amount=Amount(Decimal("10.00")),
        direction=SimpleNamespace(value=Decimal("-1")),
    )

    credit_entry = ledger.add(credit_posting)

    assert credit_entry.ledger is ledger
    assert credit_entry.posting is credit_posting
    assert credit_entry.balance == Quantity(Decimal("115.00"))
    assert ledger.entries == [debit_entry, credit_entry]
    assert ledger._last_balance == Quantity(Decimal("115.00"))

# Generated at 2026-10-25 03:40:11.827178
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from enum import Enum
    from types import SimpleNamespace

    class Direction(Enum):
        DEBIT = 1
        CREDIT = -1

    opening = datetime.date(2024, 1, 1)
    closing = datetime.date(2024, 1, 31)
    period = SimpleNamespace(since=opening, until=closing)

    cash_account = object()
    revenue_account = object()
    ignored_account = object()

    initial_cash = Quantity(Decimal("100.00"))
    initial = {
        cash_account: Balance(opening, initial_cash),
    }

    cash_debit = SimpleNamespace(
        account=cash_account,
        amount=Decimal("25.00"),
        direction=Direction.DEBIT,
    )
    cash_credit = SimpleNamespace(
        account=cash_account,
        amount=Decimal("5.00"),
        direction=Direction.CREDIT,
    )
    revenue_credit = SimpleNamespace(
        account=revenue_account,
        amount=Decimal("25.00"),
        direction=Direction.CREDIT,
    )
    ignored_posting = SimpleNamespace(
        account=ignored_account,
        amount=Decimal("999.00"),
        direction=Direction.DEBIT,
    )

    journal = [
        # Outside the period and therefore ignored.
        SimpleNamespace(
            date=datetime.date(2023, 12, 31),
            postings=[ignored_posting],
        ),
        # The period boundaries are inclusive.
        SimpleNamespace(
            date=opening,
            postings=[cash_debit, revenue_credit],
        ),
        SimpleNamespace(
            date=closing,
            postings=[cash_credit],
        ),
    ]

    general_ledger = module_0.build_general_ledger(period, journal, initial)

    assert general_ledger.period is period
    assert set(general_ledger.ledgers) == {cash_account, revenue_account}
    assert ignored_account not in general_ledger.ledgers

    cash_ledger = general_ledger.ledgers[cash_account]
    assert cash_ledger.initial.value == Quantity(Decimal("100.00"))
    assert [entry.posting for entry in cash_ledger.entries] == [
        cash_debit,
        cash_credit,
    ]
    assert [entry.balance for entry in cash_ledger.entries] == [
        Quantity(Decimal("125.00")),
        Quantity(Decimal("120.00")),
    ]

    revenue_ledger = general_ledger.ledgers[revenue_account]
    assert revenue_ledger.initial.value == Quantity(Decimal("0"))
    assert len(revenue_ledger.entries) == 1
    assert revenue_ledger.entries[0].posting is revenue_credit
    assert revenue_ledger.entries[0].balance == Quantity(Decimal("-25.00"))

# Generated at 2026-10-25 03:40:14.365568
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-25 03:40:16.890965
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-25 03:40:19.414349
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-25 03:40:21.829479
# Unit test for function build_general_ledger

# Generated at 2026-10-25 03:40:24.244397
# Unit test for function build_general_ledger

# Generated at 2026-10-25 03:40:26.660270
# Unit test for function build_general_ledger

# Generated at 2026-10-25 03:40:29.075238
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 03:40:31.490310
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 03:40:33.905639
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 03:40:36.319974
# Unit test for function build_general_ledger

# Generated at 2026-10-25 03:40:38.737558
# Unit test for function build_general_ledger

# Generated at 2026-10-25 03:40:41.151281
# Unit test for function build_general_ledger

# Generated at 2026-10-25 03:40:43.567835
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:40:46.336213
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:40:49.008293
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:41:26.179171
# Unit test for method add of class Ledger

# Generated at 2026-10-25 03:41:40.606657
# Unit test for method add of class Ledger
def test_Ledger_add():import datetime

# Generated at 2026-10-25 03:41:43.024106
# Unit test for method add of class Ledger

# Generated at 2026-10-25 03:41:44.395934
# Unit test for method add of class Ledger
def test_Ledger_add():import datetime

# Generated at 2026-10-25 03:42:06.118658
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from enum import Enum
    from types import SimpleNamespace

    class Direction(Enum):
        DEBIT = 1
        CREDIT = -1

    period = SimpleNamespace(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 1, 31),
    )

    cash = "cash"
    revenue = "revenue"
    ignored = "ignored"

    opening_balance = Balance(
        datetime.date(2023, 12, 31),
        Quantity(Decimal("100.00")),
    )

    def journal_entry(date, *posting_data):
        journal = SimpleNamespace(
            date=date,
            description=f"Entry on {date}",
            postings=[],
        )
        journal.postings = [
            SimpleNamespace(
                account=account,
                amount=Amount(Decimal(amount)),
                direction=direction,
                date=date,
                journal=journal,
                is_debit=direction is Direction.DEBIT,
                is_credit=direction is Direction.CREDIT,
            )
            for account, amount, direction in posting_data
        ]
        return journal

    journal = [
        journal_entry(
            datetime.date(2024, 1, 5),
            (cash, "25.00", Direction.DEBIT),
        ),
        journal_entry(
            datetime.date(2024, 1, 10),
            (cash, "10.00", Direction.CREDIT),
            (revenue, "10.00", Direction.DEBIT),
        ),
        # This entry is outside the accounting period and must be ignored.
        journal_entry(
            datetime.date(2024, 2, 1),
            (ignored, "50.00", Direction.DEBIT),
        ),
    ]

    result = module_0.build_general_ledger(
        period,
        journal,
        {cash: opening_balance},
    )

    assert result.period is period
    assert set(result.ledgers) == {cash, revenue}

    cash_ledger = result.ledgers[cash]
    assert cash_ledger.initial is opening_balance
    assert [entry.balance for entry in cash_ledger.entries] == [
        Quantity(Decimal("125.00")),
        Quantity(Decimal("115.00")),
    ]

    revenue_ledger = result.ledgers[revenue]
    assert revenue_ledger.initial.value == Quantity(Decimal("0"))
    assert revenue_ledger.initial.date == period.since
    assert [entry.balance for entry in revenue_ledger.entries] == [
        Quantity(Decimal("10.00")),
    ]

    assert ignored not in result.ledgers

# Generated at 2026-10-25 03:42:29.579769
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from enum import Enum
    from types import SimpleNamespace

    class Direction(Enum):
        DEBIT = Decimal("1")
        CREDIT = Decimal("-1")

    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 1, 31),
    )

    cash = object()
    inventory = object()
    revenue = object()
    outside_period = object()

    initial = {
        cash: Balance(
            datetime.date(2023, 12, 31),
            Quantity(Decimal("100")),
        ),
        inventory: Balance(
            datetime.date(2023, 12, 31),
            Quantity(Decimal("50")),
        ),
    }

    journal = [
        SimpleNamespace(
            date=datetime.date(2023, 12, 31),
            postings=[
                SimpleNamespace(
                    account=outside_period,
                    amount=Decimal("999"),
                    direction=Direction.DEBIT,
                )
            ],
        ),
        SimpleNamespace(
            date=period.since,
            postings=[
                SimpleNamespace(
                    account=cash,
                    amount=Decimal("25"),
                    direction=Direction.DEBIT,
                )
            ],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 1, 15),
            postings=[
                SimpleNamespace(
                    account=cash,
                    amount=Decimal("10"),
                    direction=Direction.CREDIT,
                ),
                SimpleNamespace(
                    account=revenue,
                    amount=Decimal("40"),
                    direction=Direction.CREDIT,
                ),
            ],
        ),
        SimpleNamespace(
            date=period.until,
            postings=[
                SimpleNamespace(
                    account=revenue,
                    amount=Decimal("5"),
                    direction=Direction.DEBIT,
                )
            ],
        ),
        SimpleNamespace(
            date=datetime.date(2024, 2, 1),
            postings=[
                SimpleNamespace(
                    account=outside_period,
                    amount=Decimal("999"),
                    direction=Direction.DEBIT,
                )
            ],
        ),
    ]

    general_ledger = module_0.build_general_ledger(period, journal, initial)

    assert general_ledger.period == period
    assert set(general_ledger.ledgers) == {cash, inventory, revenue}
    assert outside_period not in general_

# Generated at 2026-10-25 03:42:48.416353
# Unit test for function build_general_ledger
def test_build_general_ledger():
    from types import SimpleNamespace
    from typing import cast

    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 1, 31),
    )

    cash = cast(Account, object())
    revenue = cast(Account, object())
    ignored_account = cast(Account, object())

    initial = {
        cash: Balance(
            period.since,
            Quantity(Decimal("100.00")),
        ),
    }

    debit = SimpleNamespace(value=Decimal("1"))
    credit = SimpleNamespace(value=Decimal("-1"))

    def journal_entry(date, *postings):
        return cast(
            JournalEntry[object],
            SimpleNamespace(date=date, postings=list(postings)),
        )

    def posting(account, amount, direction):
        return cast(
            Posting[object],
            SimpleNamespace(
                account=account,
                amount=Amount(Decimal(amount)),
                direction=direction,
                date=period.since,
            ),
        )

    journal = [
        # Included because the period boundaries are inclusive.
        journal_entry(
            period.since,
            posting(cash, "25.00", debit),
            posting(revenue, "25.00", credit),
        ),
        journal_entry(
            period.until,
            posting(cash, "10.00", credit),
            posting(revenue, "10.00", debit),
        ),
        # Excluded because it is outside the accounting period.
        journal_entry(
            datetime.date(2024, 2, 1),
            posting(ignored_account, "50.00", debit),
        ),
    ]

    general_ledger = module_0.build_general_ledger(period, journal, initial)

    assert general_ledger.period == period
    assert set(general_ledger.ledgers) == {cash, revenue}
    assert ignored_account not in general_ledger.ledgers

    cash_ledger = general_ledger.ledgers[cash]
    assert cash_ledger.initial.value == Quantity(Decimal("100.00"))
    assert [entry.balance for entry in cash_ledger.entries] == [
        Quantity(Decimal("125.00")),
        Quantity(Decimal("115.00")),
    ]

    revenue_ledger = general_ledger.ledgers[revenue]
    assert revenue_ledger.initial.value == Quantity(Decimal("0"))
    assert [entry.balance for entry in revenue_ledger.entries] == [
        Quantity(Decimal("-25.00")),
        Quantity(Decimal("-15.00")),
    ]

# Generated at 2026-10-25 03:43:14.097576
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:43:16.750637
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:43:19.549689
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 03:43:29.781610
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 12, 31),
    )
    expected: InitialBalances = {}

    class StubReadInitialBalances:
        def module_0.__call__(self, requested_period: DateRange) -> InitialBalances:
            assert requested_period == period
            return expected

    reader: ReadInitialBalances = StubReadInitialBalances()

    assert reader(period) is expected

# Generated at 2026-10-25 03:43:44.952255
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    initial = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(Mock(spec=Account), initial)

    debit_posting = SimpleNamespace(
        amount=Amount(Decimal("25.00")),
        direction=SimpleNamespace(value=1),
    )

    first_entry = ledger.add(debit_posting)  # type: ignore[arg-type]

    assert first_entry.ledger is ledger
    assert first_entry.posting is debit_posting
    assert first_entry.balance == Quantity(Decimal("125.00"))
    assert ledger.entries == [first_entry]

    # Verify that subsequent entries use the previous entry's balance.
    credit_posting = SimpleNamespace(
        amount=Amount(Decimal("10.00")),
        direction=SimpleNamespace(value=-1),
    )

    second_entry = ledger.add(credit_posting)  # type: ignore[arg-type]

    assert second_entry.balance == Quantity(Decimal("115.00"))
    assert ledger.entries == [first_entry, second_entry]

# Generated at 2026-10-25 03:44:01.407507
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]
