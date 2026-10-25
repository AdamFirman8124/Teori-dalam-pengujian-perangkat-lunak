

# Generated at 2026-10-24 03:50:36.975980
# Unit test for constructor of class Ledger
def test_Ledger():from unittest.mock import MagicMock


# Generated at 2026-10-24 03:50:38.299746
# Unit test for constructor of class GeneralLedgerProgram

# Generated at 2026-10-24 03:50:41.009304
# Unit test for constructor of class GeneralLedgerProgram
def test_GeneralLedgerProgram():import datetime

# Generated at 2026-10-24 03:51:11.764525
# Unit test for method __repr__ of class Ledger
def test_Ledger___repr__():
    from decimal import Decimal

    ## Lightweight stubs â Ledger's repr only calls repr() on its fields,
    ## so we don't depend on Account/Balance constructors:
    class _StubAccount:
        def module_0.__repr__(self) -> str:
            return "Account(code='100')"

    class _StubBalance:
        def __init__(self, value: Decimal) -> None:
            self.value = value

        def module_0.__repr__(self) -> str:
            return f"Balance(value={self.value!r})"

    class _StubPosting:
        def __init__(self, amount: Decimal) -> None:
            self.amount = amount
            self.direction = None  # not needed for repr check

    ## Empty ledger:
    account = _StubAccount()
    initial = _StubBalance(Decimal("100.00"))
    ledger = Ledger(account, initial)

    expected = (
        "Ledger(account=Account(code='100'), "
        "initial=Balance(value=Decimal('100.00')), entries=[])"
    )
    assert repr(ledger) == expected

    ## Ledger with one entry (entries must appear in repr):
    ledger.add(_StubPosting(Decimal("50.00")))
    assert repr(ledger).startswith(
        "Ledger(account=Account(code='100'), initial=Balance(value=Decimal('100.00')), "
        "entries=[LedgerEntry(ledger="
    )

# Generated at 2026-10-24 03:51:13.178635
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import datetime
    from decimal import Decimal
    from collections import namedtuple

    # -- Minimal stubs standing in for domain types (no imports from the package needed) --

    FakeQuantity = namedtuple("FakeQuantity", ["value"])

    class _Qty:
        """Wraps a running total; unwraps on + so Ledger.add math works with Decimals."""
        def __init__(self, value):
            self.value = value
        def __add__(self, other):
            return other

    class FakeBalance:
        def __init__(self, value):
            self.value = _Qty(value)

    class FakeDirection:
        def __init__(self, value):
            self.value = value  # 1 = debit, -1 = credit

    DEBIT, CREDIT = FakeDirection(1), FakeDirection(-1)

    class FakeAccount:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return self.name

    class FakePosting:
        def __init__(self, account, amount, direction):
            self.account = account
            self.amount = amount
            self.direction = direction
        @property
        def is_debit(self):
            return self.direction is DEBIT
        @property
        def is_credit(self):
            return self.direction is CREDIT

    class FakeJournal:
        def __init__(self, date, description, postings):
            self.date = date
            self.description = description
            self.postings = postings

    DateRange = namedtuple("DateRange", ["since", "until"])

    # -- Fake algebra implementations --

    cash, revenue, opening = FakeAccount("cash"), FakeAccount("revenue"), FakeAccount("opening")

    def read_initial_balances(period):
        # Only 'cash' has an opening balance; 'revenue' must be auto-created at zero.
        return {cash: FakeBalance(Decimal("1000"))}

    def read_journal_entries(period):
        return [
            FakeJournal(datetime.date(2024, 1, 15), "Sale", [
                FakePosting(cash, Decimal("500"), DEBIT),
                FakePosting(revenue, Decimal("500"), CREDIT),
            ]),
            # Outside the period â must be ignored.
            FakeJournal(datetime.date(2024, 3, 1), "Next period", [
                FakePosting(cash, Decimal("999"), DEBIT),
            ]),
            FakeJournal(datetime.date(2024, 2, 10), "Refund", [
                FakePosting(cash, Decimal("200"), CREDIT),
                FakePosting(revenue, Decimal("200"), DEBIT),
            ]),
        ]

    # -- Compile and run the program --

    from accounting.ledgering.general import compile_general_ledger_program  # adjust import path

    program = module_0.compile_general_ledger_program(read_initial_balances, read_journal_entries)
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 2, 29))
    gl = program(period)

    # -- Assertions --

    # Both touched accounts got ledgers.
    assert set(gl.ledgers) == {cash, revenue}

    # Cash: 1000 opening + 500 - 200 = 1300; 'Next period' entry excluded.
    cash_ledger = gl.ledgers[cash]
    assert len(cash_ledger.entries) == 2
    assert cash_ledger.entries[-1].balance.value == Decimal("1300")

    # Revenue: auto-created at zero, then -500 + 200 = -300.
    revenue_ledger = gl.ledgers[revenue]
    assert len(revenue_ledger.entries) == 2
    assert revenue_ledger.entries[-1].balance.value == Decimal("-300")

    # Entries are in journal order within the period.
    assert [e.date for e in cash_ledger.entries] == [
        datetime.date(2024, 1, 15), datetime.date(2024, 2, 10)
    ]

    # The program is reusable â same inputs, same result.
    gl2 = program(period)
    assert gl2.ledgers[cash].entries[-1].balance.value == Decimal("1300")

    print("test_compile_general_ledger_program passed")

# Generated at 2026-10-24 03:51:15.956601
# Unit test for constructor of class Ledger
def test_Ledger():from unittest.mock import MagicMock


# Generated at 2026-10-24 03:51:17.314501
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:51:20.063251
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:51:22.879461
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:51:24.253334
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:51:26.992841
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:51:29.666074
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:51:32.358996
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:51:33.692295
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:51:36.423370
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:51:38.937264
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:51:41.444060
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:51:43.866914
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:51:46.383539
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:51:48.798166
# Unit test for method add of class Ledger

# Generated at 2026-10-24 03:51:51.215789
# Unit test for method add of class Ledger

# Generated at 2026-10-24 03:51:53.631192
# Unit test for method add of class Ledger

# Generated at 2026-10-24 03:51:56.046747
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:51:58.461539
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:52:00.875989
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:52:03.290488
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:52:05.705630
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:52:08.123411
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:52:10.535392
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:52:12.950815
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:52:15.366188
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:52:18.008688
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:52:20.751183
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:52:23.647653
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:52:24.978070
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:52:27.746562
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:52:30.484744
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:52:57.268833
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = Mock(spec=DateRange)
    expected = {}

    class StubReadInitialBalances:
        def module_0.__call__(self, given_period: DateRange) -> InitialBalances:
            assert given_period is period
            return expected

    reader: ReadInitialBalances = StubReadInitialBalances()

    assert reader(period) is expected

# Generated at 2026-10-24 03:52:59.769731
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:53:02.186966
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:53:04.598463
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:53:07.013070
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:53:09.429912
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:53:11.849231
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:53:14.264485
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 03:53:16.804107
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 03:53:19.219515
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 03:53:21.635584
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:53:24.050746
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:53:26.467969
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:53:28.882100
# Unit test for method add of class Ledger

# Generated at 2026-10-24 03:53:31.298449
# Unit test for method add of class Ledger

# Generated at 2026-10-24 03:53:33.713234
# Unit test for method add of class Ledger

# Generated at 2026-10-24 03:53:36.129498
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:53:38.553335
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:53:40.968719
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:53:43.382616
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:53:45.797418
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:54:06.892146
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:54:08.218098
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:54:11.047080
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:54:13.826658
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:54:16.595326
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:54:19.258112
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:54:21.931371
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:54:49.119840
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

    result = reader(period)

    assert result is expected

# Generated at 2026-10-24 03:54:50.433855
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:54:53.291355
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:54:56.108111
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:55:12.813622
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from ..commons.zeitgeist import DateRange
    from .generic import Balance

    ## Arrange: a concrete implementation satisfying the ReadInitialBalances protocol.
    account = Account(1020, "Banks", AccountType.ASSET)
    balance = Balance(datetime.date(2023, 1, 1), Quantity(Decimal("100.00")))
    expected: InitialBalances = {account: balance}

    class _ReadInitialBalances:
        def module_0.__call__(self, period: DateRange) -> InitialBalances:
            assert isinstance(period, DateRange)  # period is passed through
            return expected

    read_initial_balances: ReadInitialBalances = _ReadInitialBalances()

    ## Act:
    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))
    result = read_initial_balances(period)

    ## Assert:
    assert result == expected
    assert isinstance(result, dict)
    assert account in result
    assert result[account].value == Quantity(Decimal("100.00"))

# Generated at 2026-10-24 03:55:14.179073
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:55:16.599451
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:55:19.143926
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:55:21.563760
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:55:24.362069
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:55:27.056976
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:55:29.766751
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:55:31.069826
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:55:32.383480
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:55:33.714472
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:55:36.395983
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:55:39.066695
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:56:34.118897
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 03:56:43.949622
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 12, 31),
    )


# Generated at 2026-10-24 03:56:46.690436
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:56:49.580557
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:56:52.345471
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:56:53.651560
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import datetime
    from decimal import Decimal
    from collections import namedtuple

    # -- Minimal stubs standing in for domain types (no imports from the package needed) --

    FakeQuantity = namedtuple("FakeQuantity", ["value"])

    class _Qty:
        """Wraps a running total; unwraps on + so Ledger.add math works with Decimals."""
        def __init__(self, value):
            self.value = value
        def __add__(self, other):
            return other

    class FakeBalance:
        def __init__(self, value):
            self.value = _Qty(value)

    class FakeDirection:
        def __init__(self, value):
            self.value = value  # 1 = debit, -1 = credit

    DEBIT, CREDIT = FakeDirection(1), FakeDirection(-1)

    class FakeAccount:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return self.name

    class FakePosting:
        def __init__(self, account, amount, direction):
            self.account = account
            self.amount = amount
            self.direction = direction
        @property
        def is_debit(self):
            return self.direction is DEBIT
        @property
        def is_credit(self):
            return self.direction is CREDIT

    class FakeJournal:
        def __init__(self, date, description, postings):
            self.date = date
            self.description = description
            self.postings = postings

    DateRange = namedtuple("DateRange", ["since", "until"])

    # -- Fake algebra implementations --

    cash, revenue, opening = FakeAccount("cash"), FakeAccount("revenue"), FakeAccount("opening")

    def read_initial_balances(period):
        # Only 'cash' has an opening balance; 'revenue' must be auto-created at zero.
        return {cash: FakeBalance(Decimal("1000"))}

    def read_journal_entries(period):
        return [
            FakeJournal(datetime.date(2024, 1, 15), "Sale", [
                FakePosting(cash, Decimal("500"), DEBIT),
                FakePosting(revenue, Decimal("500"), CREDIT),
            ]),
            # Outside the period â must be ignored.
            FakeJournal(datetime.date(2024, 3, 1), "Next period", [
                FakePosting(cash, Decimal("999"), DEBIT),
            ]),
            FakeJournal(datetime.date(2024, 2, 10), "Refund", [
                FakePosting(cash, Decimal("200"), CREDIT),
                FakePosting(revenue, Decimal("200"), DEBIT),
            ]),
        ]

    # -- Compile and run the program --

    from accounting.ledgering.general import compile_general_ledger_program  # adjust import path

    program = module_0.compile_general_ledger_program(read_initial_balances, read_journal_entries)
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 2, 29))
    gl = program(period)

    # -- Assertions --

    # Both touched accounts got ledgers.
    assert set(gl.ledgers) == {cash, revenue}

    # Cash: 1000 opening + 500 - 200 = 1300; 'Next period' entry excluded.
    cash_ledger = gl.ledgers[cash]
    assert len(cash_ledger.entries) == 2
    assert cash_ledger.entries[-1].balance.value == Decimal("1300")

    # Revenue: auto-created at zero, then -500 + 200 = -300.
    revenue_ledger = gl.ledgers[revenue]
    assert len(revenue_ledger.entries) == 2
    assert revenue_ledger.entries[-1].balance.value == Decimal("-300")

    # Entries are in journal order within the period.
    assert [e.date for e in cash_ledger.entries] == [
        datetime.date(2024, 1, 15), datetime.date(2024, 2, 10)
    ]

    # The program is reusable â same inputs, same result.
    gl2 = program(period)
    assert gl2.ledgers[cash].entries[-1].balance.value == Decimal("1300")

    print("test_compile_general_ledger_program passed")

# Generated at 2026-10-24 03:56:54.960746
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:57:22.658225
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 12, 31),
    )
    expected: InitialBalances = {}

    class StubReadInitialBalances:
        def module_0.__call__(self, requested_period: DateRange) -> InitialBalances:
            assert requested_period is period
            return expected

    reader: ReadInitialBalances = StubReadInitialBalances()

    result = reader(period)

    assert result is expected

# Generated at 2026-10-24 03:57:24.091179
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:57:25.407525
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:57:28.192533
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:57:30.926954
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:57:32.287112
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:58:03.197060
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = Mock(spec=DateRange)
    initial_balances: InitialBalances = {}

    read_initial_balances = Mock(
        spec=ReadInitialBalances,
        return_value=initial_balances,
    )
    read_journal_entries = Mock(return_value=[])

    program = compile_general_ledger_program(
        read_initial_balances,
        read_journal_entries,
    )

    general_ledger = program(period)

    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)
    assert general_ledger.period is period
    assert general_ledger.ledgers == {}

# Generated at 2026-10-24 03:58:06.067295
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:58:09.033834
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:58:11.834645
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:58:17.538534
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:20.293033
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:23.068033
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:24.370440
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:58:25.677509
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:58:26.981068
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:29.683837
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:32.404267
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:33.737967
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:36.405381
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:39.121689
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:40.433831
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:43.117139
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:58:45.806955
# Unit test for function build_general_ledger

# Generated at 2026-10-24 03:59:16.631033
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 12, 31),
    )
    expected: InitialBalances = {}

    class StubReadInitialBalances:
        def __init__(self) -> None:
            self.received_periods: List[DateRange] = []

        def module_0.__call__(self, requested_period: DateRange) -> InitialBalances:
            self.received_periods.append(requested_period)
            return expected

    implementation = StubReadInitialBalances()
    reader: ReadInitialBalances = implementation

    result = reader(period)

    assert result is expected
    assert implementation.received_periods == [period]

# Generated at 2026-10-24 03:59:19.484176
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:21.983895
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:25.126845
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:27.906347
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:30.656798
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:33.425892
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:34.729051
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:59:44.457234
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:47.152712
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:49.907049
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:51.222546
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:59:52.558034
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 03:59:55.339329
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 03:59:58.089342
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:00:00.865003
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:00:16.942714
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 12, 31),
    )
    expected: InitialBalances = {}

    def read_initial_balances(actual_period: DateRange) -> InitialBalances:
        assert actual_period == period
        return expected

    reader: ReadInitialBalances = read_initial_balances

    assert reader(period) is expected

# Generated at 2026-10-24 04:00:18.261981
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:00:21.450057
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:00:24.199093
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:00:25.508741
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    ledger = Ledger(
        account=Mock(spec=Account),
        initial=Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100"))),
    )
    debit = SimpleNamespace(
        amount=Amount(Decimal("50")),
        direction=SimpleNamespace(value=1),
    )
    credit = SimpleNamespace(
        amount=Amount(Decimal("30")),
        direction=SimpleNamespace(value=-1),
    )

    first = ledger.add(debit)

    assert first.ledger is ledger
    assert first.posting is debit
    assert first.balance == Quantity(Decimal("150"))
    assert ledger.entries == [first]

    second = ledger.add(credit)

    assert second.balance == Quantity(Decimal("120"))
    assert ledger.entries == [first, second]

# Generated at 2026-10-24 04:00:26.831060
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:00:29.632974
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:00:32.388618
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:00:33.718548
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import datetime
    from decimal import Decimal
    from collections import namedtuple

    # -- Minimal stubs standing in for domain types (no imports from the package needed) --

    FakeQuantity = namedtuple("FakeQuantity", ["value"])

    class _Qty:
        """Wraps a running total; unwraps on + so Ledger.add math works with Decimals."""
        def __init__(self, value):
            self.value = value
        def __add__(self, other):
            return other

    class FakeBalance:
        def __init__(self, value):
            self.value = _Qty(value)

    class FakeDirection:
        def __init__(self, value):
            self.value = value  # 1 = debit, -1 = credit

    DEBIT, CREDIT = FakeDirection(1), FakeDirection(-1)

    class FakeAccount:
        def __init__(self, name):
            self.name = name
        def __repr__(self):
            return self.name

    class FakePosting:
        def __init__(self, account, amount, direction):
            self.account = account
            self.amount = amount
            self.direction = direction
        @property
        def is_debit(self):
            return self.direction is DEBIT
        @property
        def is_credit(self):
            return self.direction is CREDIT

    class FakeJournal:
        def __init__(self, date, description, postings):
            self.date = date
            self.description = description
            self.postings = postings

    DateRange = namedtuple("DateRange", ["since", "until"])

    # -- Fake algebra implementations --

    cash, revenue, opening = FakeAccount("cash"), FakeAccount("revenue"), FakeAccount("opening")

    def read_initial_balances(period):
        # Only 'cash' has an opening balance; 'revenue' must be auto-created at zero.
        return {cash: FakeBalance(Decimal("1000"))}

    def read_journal_entries(period):
        return [
            FakeJournal(datetime.date(2024, 1, 15), "Sale", [
                FakePosting(cash, Decimal("500"), DEBIT),
                FakePosting(revenue, Decimal("500"), CREDIT),
            ]),
            # Outside the period â must be ignored.
            FakeJournal(datetime.date(2024, 3, 1), "Next period", [
                FakePosting(cash, Decimal("999"), DEBIT),
            ]),
            FakeJournal(datetime.date(2024, 2, 10), "Refund", [
                FakePosting(cash, Decimal("200"), CREDIT),
                FakePosting(revenue, Decimal("200"), DEBIT),
            ]),
        ]

    # -- Compile and run the program --

    from accounting.ledgering.general import compile_general_ledger_program  # adjust import path

    program = module_0.compile_general_ledger_program(read_initial_balances, read_journal_entries)
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 2, 29))
    gl = program(period)

    # -- Assertions --

    # Both touched accounts got ledgers.
    assert set(gl.ledgers) == {cash, revenue}

    # Cash: 1000 opening + 500 - 200 = 1300; 'Next period' entry excluded.
    cash_ledger = gl.ledgers[cash]
    assert len(cash_ledger.entries) == 2
    assert cash_ledger.entries[-1].balance.value == Decimal("1300")

    # Revenue: auto-created at zero, then -500 + 200 = -300.
    revenue_ledger = gl.ledgers[revenue]
    assert len(revenue_ledger.entries) == 2
    assert revenue_ledger.entries[-1].balance.value == Decimal("-300")

    # Entries are in journal order within the period.
    assert [e.date for e in cash_ledger.entries] == [
        datetime.date(2024, 1, 15), datetime.date(2024, 2, 10)
    ]

    # The program is reusable â same inputs, same result.
    gl2 = program(period)
    assert gl2.ledgers[cash].entries[-1].balance.value == Decimal("1300")

    print("test_compile_general_ledger_program passed")

# Generated at 2026-10-24 04:00:35.049114
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:00:37.837588
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:00:40.637011
# Unit test for function build_general_ledger