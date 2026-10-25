

# Generated at 2026-10-24 06:00:35.786867
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:00:38.549274
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:00:41.410104
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:00:42.842964
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

# Generated at 2026-10-24 06:01:04.551744
# Unit test for method __eq__ of class GeneralLedger

# Generated at 2026-10-24 06:01:06.958748
# Unit test for method __eq__ of class GeneralLedger

# Generated at 2026-10-24 06:01:09.371713
# Unit test for method __eq__ of class GeneralLedger

# Generated at 2026-10-24 06:01:11.787380
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:01:14.200730
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:01:16.616107
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:01:19.030835
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:01:21.444905
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:01:23.859535
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:01:26.273665
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:01:28.688498
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:01:31.102285
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:01:33.519221
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:01:35.937066
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:01:38.351436
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:01:40.765788
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:01:43.178895
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:01:45.596220
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:01:48.009311
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:01:50.424929
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:01:52.841852
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:01:55.256442
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:01:57.677894
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:02:00.086297
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:02:02.501771
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:02:04.917455
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:02:07.331791
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:02:09.749645
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:02:12.163476
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:02:14.576951
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:02:16.997252
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:02:19.408081
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:02:21.824847
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:02:24.239627
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:02:37.019287
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-24 06:02:38.458720
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:02:41.318383
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:02:44.122786
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:02:45.489406
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:02:48.386535
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:02:51.264535
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:02:53.985832
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:02:56.658773
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:02:59.453331
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:03:00.764593
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

# Generated at 2026-10-24 06:03:02.138967
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:04.797554
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:07.212546
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:09.741286
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:03:12.158161
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:03:14.573576
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:03:16.988708
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:19.402007
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:21.818313
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:24.383976
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:03:26.798178
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:03:29.213731
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:03:31.628963
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:03:34.043063
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:03:36.458177
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:03:38.872774
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:03:41.290097
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:03:43.703889
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:03:46.117843
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:48.545611
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:50.960543
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:53.379420
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:55.800222
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:03:58.426698
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:04:01.215404
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:04:04.013852
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:04:06.824049
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:04:08.171529
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:04:10.920357
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:04:13.646835
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:04:39.618444
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-24 06:04:42.038560
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:04:44.454262
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:04:46.876344
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:04:49.291705
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:04:51.858037
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:04:54.623747
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:04:57.389130
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:05:00.127284
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:05:02.880110
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:05:04.206488
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

# Generated at 2026-10-24 06:05:05.537457
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

# Generated at 2026-10-24 06:05:08.356625
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:05:11.132221
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:05:13.749627
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:05:16.168351
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:05:18.581253
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:05:20.999446
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:05:23.414879
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:05:25.978848
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:05:28.393455
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:05:30.812734
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:05:33.232338
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:05:35.648777
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:05:38.058947
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:05:40.506642
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:05:42.901571
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:05:45.318305
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:05:47.732628
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:05:50.146778
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:05:52.563830
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:05:54.982036
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:05:57.395967
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:05:59.813664
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:06:02.231060
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:06:04.645657
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:06:07.061132
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:06:09.486359
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:06:11.889976
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:06:14.306306
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:06:16.721884
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:06:19.134946
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:06:21.549066
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:06:23.965967
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:06:26.379463
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:06:28.793059
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:06:31.207673
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:06:33.622522
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:06:36.035343
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:06:38.450027
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:06:40.863238
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:06:43.278548
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:06:45.694126
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:06:48.107906
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:06:50.523962
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:06:52.939686
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:06:55.354458
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:06:57.769979
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:07:00.184419
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:07:02.598352
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:07:05.015637
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:07:07.431473
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:07:09.845146
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:07:12.259260
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:07:14.676316
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:07:17.089519
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:07:19.505158
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:07:21.919775
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:07:24.335261
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:07:26.748582
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:07:29.165740
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:07:31.582868
# Unit test for method add of class Ledger

# Generated at 2026-10-24 06:07:33.997062
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:07:36.410783
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:07:38.828396
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:07:57.599110
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

# Generated at 2026-10-24 06:07:58.930966
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:08:01.750537
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:08:04.473341
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:08:30.915698
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

    assert reader(period) is expected

# Generated at 2026-10-24 06:08:32.229305
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

# Generated at 2026-10-24 06:08:33.536906
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

# Generated at 2026-10-24 06:08:36.259483
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:08:39.005450
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:08:41.769105
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 06:08:43.101078
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

# Generated at 2026-10-24 06:08:44.408919
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

# Generated at 2026-10-24 06:09:02.233537
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:09:04.753452
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:09:07.172679
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:09:09.584713
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:09:12.000944
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:09:14.625573
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:09:33.168840
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = DateRange(date(2024, 1, 1), date(2024, 12, 31))
    expected_balances = {}

    class StubReadInitialBalances:
        def module_0.__call__(self, actual_period: DateRange):
            assert actual_period == period
            return expected_balances

    reader: ReadInitialBalances = StubReadInitialBalances()

    result = reader(period)

    assert result is expected_balances

# Generated at 2026-10-24 06:09:49.588510
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

# Generated at 2026-10-24 06:09:52.093309
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:09:54.510048
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:09:56.923942
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:09:59.342672
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:10:01.907877
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:10:04.323324
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:10:06.739195
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:10:09.157784
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:10:11.570887
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 06:10:13.988707
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:10:16.403467
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:10:18.817670
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:10:21.233802
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 06:10:29.802795
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-24 06:10:31.128926
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:10:33.864835
# Unit test for function build_general_ledger

# Generated at 2026-10-24 06:10:36.658830
# Unit test for function build_general_ledger