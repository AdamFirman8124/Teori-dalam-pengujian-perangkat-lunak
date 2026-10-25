

# Generated at 2026-10-24 04:49:10.176873
# Unit test for method __eq__ of class LedgerEntry

# Generated at 2026-10-24 04:49:12.589917
# Unit test for method __eq__ of class LedgerEntry

# Generated at 2026-10-24 04:49:15.004674
# Unit test for method __eq__ of class LedgerEntry

# Generated at 2026-10-24 04:49:17.563385
# Unit test for constructor of class Ledger

# Generated at 2026-10-24 04:49:19.974960
# Unit test for constructor of class Ledger

# Generated at 2026-10-24 04:49:22.389093
# Unit test for constructor of class Ledger

# Generated at 2026-10-24 04:49:24.802773
# Unit test for method __repr__ of class LedgerEntry

# Generated at 2026-10-24 04:49:27.219197
# Unit test for method __repr__ of class LedgerEntry

# Generated at 2026-10-24 04:49:29.634812
# Unit test for method __repr__ of class LedgerEntry

# Generated at 2026-10-24 04:49:32.044674
# Unit test for constructor of class LedgerEntry

# Generated at 2026-10-24 04:49:34.461646
# Unit test for constructor of class LedgerEntry

# Generated at 2026-10-24 04:49:36.876555
# Unit test for constructor of class LedgerEntry

# Generated at 2026-10-24 04:49:39.292221
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:49:41.703936
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:49:44.116412
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:49:46.527482
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:49:48.944525
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:50:02.080633
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-24 04:50:03.414382
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

# Generated at 2026-10-24 04:50:04.727578
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:07.772893
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:10.766378
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:12.287520
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:15.043487
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:17.582418
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:20.142740
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:50:22.558168
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:50:24.969571
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:50:27.500225
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:50:29.910895
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:50:32.502873
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:50:34.918041
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:50:37.334167
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:50:39.744761
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:50:42.161737
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:50:44.576840
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:50:46.994562
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:50:49.408893
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:51.819547
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:54.236341
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:56.651910
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:50:59.064118
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:51:01.479807
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:51:03.894527
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:51:06.307994
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:51:08.727834
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:51:11.134288
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:51:13.547948
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:51:15.964207
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:51:18.375734
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:51:20.790521
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:51:23.207284
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:51:25.616410
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:51:28.031950
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:51:30.447596
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:51:32.860866
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:51:35.433703
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:51:45.289320
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-24 04:51:46.618730
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

# Generated at 2026-10-24 04:52:02.543237
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = cast(DateRange, object())
    expected: InitialBalances = {}

    class StubReadInitialBalances:
        def module_0.__call__(self, actual_period: DateRange) -> InitialBalances:
            assert actual_period is period
            return expected

    read_initial_balances: ReadInitialBalances = StubReadInitialBalances()

    assert read_initial_balances(period) is expected

# Generated at 2026-10-24 04:52:05.311485
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:08.072017
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:10.837481
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:12.143217
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

# Generated at 2026-10-24 04:52:13.449762
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:52:16.247307
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:52:18.921112
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:52:21.710840
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:24.455816
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:27.220645
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:29.816382
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:52:32.321307
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:52:34.734010
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:52:37.146313
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:52:39.557045
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:52:41.966600
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:52:44.378860
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:46.790321
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:49.205254
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:51.618798
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:54.027744
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:52:56.443636
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:53:20.576969
# Unit test for function build_general_ledger
def test_build_general_ledger():from types import SimpleNamespace


# Generated at 2026-10-24 04:53:21.893303
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:53:24.595830
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:53:27.315280
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:53:43.811857
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

# Generated at 2026-10-24 04:53:46.225296
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:53:48.636756
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:53:51.048545
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:53:53.461384
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:53:55.873904
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:53:58.287777
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:54:00.701433
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:54:03.162599
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:54:05.533465
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:54:07.948558
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:54:10.364939
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:54:12.783759
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:54:14.232056
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

# Generated at 2026-10-24 04:54:29.454258
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = object()
    expected = {}

    class StubReadInitialBalances:
        def module_0.__call__(self, requested_period):
            assert requested_period is period
            return expected

    reader: ReadInitialBalances = StubReadInitialBalances()

    assert reader(period) is expected

# Generated at 2026-10-24 04:54:30.820863
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:54:33.498069
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:54:36.283454
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:54:39.328097
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:54:42.082920
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:54:44.786254
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:54:46.089888
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

# Generated at 2026-10-24 04:54:48.878482
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:54:51.583336
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:54:54.395069
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:54:57.076185
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:54:59.491175
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:55:01.904787
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:55:04.455455
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:55:06.870651
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:55:09.280796
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:55:11.700844
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:55:14.111910
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:55:23.554635
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():from datetime import date


# Generated at 2026-10-24 04:55:24.867956
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:55:27.694168
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:55:30.621061
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:55:31.920505
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:55:34.725415
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:55:37.528436
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:55:38.859636
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

# Generated at 2026-10-24 04:55:40.185986
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:55:42.870665
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:55:45.668035
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:56:11.483668
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = DateRange(
        datetime.date(2024, 1, 1),
        datetime.date(2024, 12, 31),
    )
    expected: InitialBalances = {}

    class StubReadInitialBalances:
        def __init__(self) -> None:
            self.received_period: Optional[DateRange] = None

        def module_0.__call__(self, period: DateRange) -> InitialBalances:
            self.received_period = period
            return expected

    reader: ReadInitialBalances = StubReadInitialBalances()

    result = reader(period)

    assert result is expected
    assert reader.received_period == period

# Generated at 2026-10-24 04:56:13.984150
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:56:16.398665
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:56:18.811013
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:56:47.085681
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = Mock(spec=DateRange)
    expected: InitialBalances = {}

    reader: ReadInitialBalances = Mock(return_value=expected)

    result = reader(period)

    assert result is expected
    reader.assert_called_once_with(period)

# Generated at 2026-10-24 04:56:48.551725
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

# Generated at 2026-10-24 04:56:49.871038
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

# Generated at 2026-10-24 04:56:51.220294
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:56:53.979703
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:56:56.684342
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:56:59.194130
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:57:01.609502
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:57:04.115088
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:57:06.537318
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:57:08.953675
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:57:11.362608
# Unit test for method add of class Ledger

# Generated at 2026-10-24 04:57:13.785153
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:57:16.197383
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:57:18.608470
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:57:21.033750
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:57:23.432189
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:57:25.842415
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:57:28.263856
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:57:30.671431
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:57:33.082224
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:57:35.493580
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:57:37.905232
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:57:40.317959
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 04:57:42.730031
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:57:45.162969
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:57:47.766995
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:57:50.504235
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:57:53.264669
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:57:55.969674
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:57:57.285651
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

# Generated at 2026-10-24 04:58:01.548564
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:58:04.528919
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:58:07.703746
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:58:09.048295
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:58:11.767111
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:58:14.558678
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:58:17.312636
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:58:19.730000
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:58:22.143792
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:58:24.556449
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:58:26.973529
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:58:29.525845
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:58:31.941677
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:58:34.355005
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:58:36.767716
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:58:39.393152
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:58:41.808199
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:58:44.219801
# Unit test for function build_general_ledger

# Generated at 2026-10-24 04:58:46.635124
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:58:49.048878
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:58:51.461213
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:58:53.876822
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:58:56.291825
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:58:58.880698
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 04:59:00.209761
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

# Generated at 2026-10-24 04:59:01.671495
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

# Generated at 2026-10-24 04:59:09.498375
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:59:12.222287
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 04:59:14.982361
# Unit test for method __call__ of class GeneralLedgerProgram