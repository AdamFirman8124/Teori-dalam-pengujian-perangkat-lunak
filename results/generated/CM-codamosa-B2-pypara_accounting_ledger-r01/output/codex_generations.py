

# Generated at 2026-10-24 06:47:24.931109
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:47:27.445604
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:47:29.946607
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:47:32.361225
# Unit test for method __repr__ of class GeneralLedger

# Generated at 2026-10-24 06:47:34.919011
# Unit test for method __repr__ of class GeneralLedger

# Generated at 2026-10-24 06:47:37.418112
# Unit test for method __repr__ of class GeneralLedger

# Generated at 2026-10-24 06:47:39.835017
# Unit test for constructor of class GeneralLedgerProgram

# Generated at 2026-10-24 06:47:42.255603
# Unit test for constructor of class GeneralLedgerProgram

# Generated at 2026-10-24 06:47:44.670557
# Unit test for constructor of class GeneralLedgerProgram

# Generated at 2026-10-24 06:47:47.089277
# Unit test for method __repr__ of class LedgerEntry

# Generated at 2026-10-24 06:47:49.506143
# Unit test for method __repr__ of class LedgerEntry

# Generated at 2026-10-24 06:47:51.928309
# Unit test for method __repr__ of class LedgerEntry

# Generated at 2026-10-24 06:47:54.344076
# Unit test for constructor of class ReadInitialBalances

# Generated at 2026-10-24 06:47:56.761562
# Unit test for constructor of class ReadInitialBalances

# Generated at 2026-10-24 06:47:59.175295
# Unit test for constructor of class ReadInitialBalances

# Generated at 2026-10-24 06:48:01.590467
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:48:04.007428
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:48:21.153891
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    import datetime
    from types import SimpleNamespace

    # Concrete accounting period (structural stand-in for DateRange).
    period = SimpleNamespace(since=datetime.date(2024, 1, 1), until=datetime.date(2024, 12, 31))

    # Concrete account and balance stand-ins.
    account = SimpleNamespace(name="Cash")
    opening_balance = SimpleNamespace(value=1000)

    # Concrete implementation of the ReadInitialBalances protocol.
    class _ReadInitialBalances:
        def module_0.__call__(self, period):
            return {account: opening_balance}

    # Direct call: must return the initial balances for the given period.
    read_initial_balances = _ReadInitialBalances()
    result = read_initial_balances(period)
    assert result == {account: opening_balance}
    assert result[account] is opening_balance

    # Protocol integration: the compiled program must consume the same
    # initial balances when building the general ledger.
    compiled = compile_general_ledger_program(read_initial_balances, lambda p: [])
    general_ledger = compiled(period)

    assert general_ledger.period is period
    assert account in general_ledger.ledgers
    assert general_ledger.ledgers[account].account is account
    assert general_ledger.ledgers[account].initial is opening_balance
    assert general_ledger.ledgers[account].entries == []

# Generated at 2026-10-24 06:48:23.886349
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:48:26.679355
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:48:29.369786
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:48:45.803896
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

# Generated at 2026-10-24 06:48:48.225167
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:48:50.641936
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:48:53.342301
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:48:55.756492
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:48:58.173500
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:49:00.591274
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:49:03.004063
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:49:05.421992
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:49:07.838734
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:49:10.255495
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:49:12.674136
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:49:15.092616
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:49:17.507006
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:49:19.924251
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:49:22.341384
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:49:24.745449
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:49:27.160135
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:49:29.575064
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:49:31.989614
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:49:34.710152
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:49:37.399498
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:49:53.809782
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

# Generated at 2026-10-24 06:49:55.336128
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

# Generated at 2026-10-24 06:49:58.233676
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:50:01.058148
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:50:03.861768
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:50:05.184023
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:50:08.050794
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:50:10.930888
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:50:13.684115
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:50:16.530242
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:50:19.103098
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:50:21.524609
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:50:23.941831
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:50:26.359408
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:50:28.774025
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:50:31.196464
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:50:33.832030
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:50:36.243773
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:50:38.883502
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:50:41.780885
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:50:58.541738
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

# Generated at 2026-10-24 06:51:40.061137
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    # Test for method __call__ of class ReadInitialBalances

    ## Arrange:
    from unittest.mock import MagicMock

    account_1: Account = MagicMock(spec=Account)
    account_2: Account = MagicMock(spec=Account)

    period: DateRange = DateRange(
        since=datetime.date(2023, 1, 1),
        until=datetime.date(2023, 12, 31),
    )

    expected_balances: InitialBalances = {
        account_1: Balance(period.since, Quantity(Decimal("1000.00"))),
        account_2: Balance(period.since, Quantity(Decimal("-500.00"))),
    }

    ## A concrete implementation of the ReadInitialBalances protocol:
    class MockReadInitialBalances:
        """
        Mock implementation of the ReadInitialBalances protocol.
        """

        def __init__(self, balances: InitialBalances) -> None:
            self._balances = balances
            self.calls: List[DateRange] = []

        def module_0.__call__(self, period: DateRange) -> InitialBalances:
            self.calls.append(period)
            return self._balances

    read_initial_balances = MockReadInitialBalances(expected_balances)

    ## Act:
    result = read_initial_balances(period)

    ## Assert:
    assert result is not None
    assert isinstance(result, dict)
    assert result == expected_balances
    assert account_1 in result
    assert account_2 in result
    assert result[account_1].value == Quantity(Decimal("1000.00"))
    assert result[account_2].value == Quantity(Decimal("-500.00"))

    ## Assert the protocol was invoked exactly once with the given period:
    assert read_initial_balances.calls == [period]
    assert read_initial_balances.calls[0].since == period.since
    assert read_initial_balances.calls[0].until == period.until

    ## Assert protocol conformance (structural typing):
    def _accepts_protocol(impl: ReadInitialBalances) -> None:
        pass

    _accepts_protocol(read_initial_balances)

    ## Assert empty initial balances are handled gracefully:
    empty_reader = MockReadInitialBalances({})
    assert empty_reader(period) == {}
    assert empty_reader.calls == [period]

# Generated at 2026-10-24 06:51:41.402211
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

# Generated at 2026-10-24 06:51:42.795689
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:51:45.537284
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:51:48.376990
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:51:49.750564
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

# Generated at 2026-10-24 06:51:52.670615
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:51:55.886451
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:51:58.724162
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:52:00.055157
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

# Generated at 2026-10-24 06:52:16.563375
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

# Generated at 2026-10-24 06:52:17.894563
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:52:20.694241
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:52:23.416971
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:52:25.835963
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:52:28.250319
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:52:30.670400
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:52:33.087799
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:52:35.505801
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:52:37.920686
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:52:40.334346
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:52:42.756150
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:52:45.506101
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:52:47.190462
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

# Generated at 2026-10-24 06:52:49.937035
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:52:52.662614
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:52:55.380103
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:52:56.817952
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

# Generated at 2026-10-24 06:52:58.132323
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:53:00.896986
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:53:03.755753
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:53:05.075228
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

# Generated at 2026-10-24 06:53:06.392759
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:53:09.218888
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:53:13.732757
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:53:15.059875
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:53:17.803442
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:53:20.563396
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:53:21.873463
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

# Generated at 2026-10-24 06:53:24.544941
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:53:26.960388
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:53:29.378156
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:53:31.879471
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:53:34.294249
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:53:36.708437
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:53:40.382599
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:53:42.796589
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:53:45.212551
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:54:13.512262
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:54:47.490086
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:55:22.735576
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:55:25.159981
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:55:27.576379
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:55:29.993224
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:55:32.498458
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:55:34.999585
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:55:37.416494
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:55:39.831182
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:55:42.244624
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:55:44.660519
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:55:47.076235
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:55:49.491555
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:55:52.100568
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:56:08.715776
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

# Generated at 2026-10-24 06:56:11.460867
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:56:14.240990
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:56:16.939887
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:56:33.304566
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

# Generated at 2026-10-24 06:56:35.724769
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:56:38.142316
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:56:40.555960
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:56:45.619230
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:56:48.035117
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:56:50.451459
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:56:52.868326
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:56:55.283995
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:56:57.703753
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:57:19.780804
# Unit test for method add of class Ledger