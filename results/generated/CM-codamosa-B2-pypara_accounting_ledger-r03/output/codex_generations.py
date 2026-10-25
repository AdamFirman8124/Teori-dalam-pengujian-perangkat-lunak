

# Generated at 2026-10-24 13:34:59.041655
# Unit test for method __eq__ of class LedgerEntry
def test_LedgerEntry___eq__():
    ledger = object()
    posting = object()
    balance = object()

    entry = LedgerEntry(ledger, posting, balance)
    equal_entry = LedgerEntry(ledger, posting, balance)

    assert entry == equal_entry
    assert entry != object()

    assert entry != LedgerEntry(object(), posting, balance)
    assert entry != LedgerEntry(ledger, object(), balance)
    assert entry != LedgerEntry(ledger, posting, object())

# Generated at 2026-10-24 13:35:13.757796
# Unit test for constructor of class ReadInitialBalances
def test_ReadInitialBalances():import pytest


# Generated at 2026-10-24 13:35:15.111015
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import datetime
    import enum
    from dataclasses import dataclass
    from decimal import Decimal

    # -- Stubs mirroring the domain types the program touches ----------
    class _Direction(enum.Enum):
        DEBIT = 1
        CREDIT = -1

    @dataclass(frozen=True)
    class _Account:
        code: str

    class _Quantity:
        def __init__(self, value):
            self.value = value

        def __add__(self, other):
            return _Quantity(self.value + other.value)

        def __eq__(self, other):
            return isinstance(other, _Quantity) and self.value == other.value

    class _Balance:
        def __init__(self, date, quantity):
            self.date = date
            self.value = quantity

    class _DateRange:
        def __init__(self, since, until):
            self.since = since
            self.until = until

    class _Posting:
        def __init__(self, journal, date, account, amount, direction):
            self.journal = journal
            self.date = date
            self.account = account
            self.amount = amount
            self.direction = direction

        @property
        def is_debit(self):
            return self.direction == _Direction.DEBIT

        @property
        def is_credit(self):
            return self.direction == _Direction.CREDIT

    class _JournalEntry:
        def __init__(self, date, postings):
            self.date = date
            self.postings = postings

    # -- Fixtures -------------------------------------------------------
    period = _DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    cash = _Account("1000")
    sales = _Account("4000")
    rent

# Generated at 2026-10-24 13:35:18.175388
# Unit test for method __eq__ of class GeneralLedger
def test_GeneralLedger___eq__():
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    other_period = DateRange(datetime.date(2025, 1, 1), datetime.date(2025, 12, 31))
    account = "1000"
    ledger = Ledger(account, Balance(period.since, Quantity(Decimal(0))))
    general_ledger = GeneralLedger(period, {account: ledger})
    assert general_ledger == general_ledger
    assert general_ledger == GeneralLedger(
        DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31)), {account: ledger}
    )
    assert general_ledger != GeneralLedger(other_period, {account: ledger})
    assert general_ledger != GeneralLedger(period, {})
    assert general_ledger != GeneralLedger(period, {"2000": ledger})
    assert (general_ledger == object()) is False
    assert (general_ledger != object()) is True

# Generated at 2026-10-24 13:35:50.930437
# Unit test for method __eq__ of class GeneralLedger
def test_GeneralLedger___eq__():
    ## Build a period and two ledgers with identical content:
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    balance = Balance(datetime.date(2024, 1, 1), Quantity(Decimal("100")))

    account_a = Account(...)  # FIXME: adjust to your Account constructor
    account_b = Account(...)  # FIXME: adjust to your Account constructor

    ledger_a = Ledger(account_a, balance)
    ledger_b = Ledger(account_b, balance)

    ## Identical content, distinct instances:
    gl1 = GeneralLedger(period, {account_a: ledger_a, account_b: ledger_b})
    gl2 = GeneralLedger(period, {account_a: ledger_a, account_b: ledger_b})
    assert gl1 == gl2
    assert not (gl1 != gl2)

    ## Identity:
    assert gl1 == gl1

    ## Different period:
    other_period = DateRange(datetime.date(2025, 1, 1), datetime.date(2025, 12, 31))
    assert gl1 != GeneralLedger(other_period, gl1.ledgers)

    ## Different ledgers:
    assert gl1 != GeneralLedger(period, {account_a: ledger_a})

    ## Comparison with a non-GeneralLedger:
    assert gl1 != "not a general ledger"
    assert gl1 != None  # noqa: E711

# Generated at 2026-10-24 13:35:53.349218
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:35:55.766006
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:35:58.184568
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:36:00.601328
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:36:03.024979
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:36:05.439681
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:36:07.855547
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:36:10.285263
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:36:12.700609
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:36:15.116933
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:36:48.971651
# Unit test for method add of class Ledger
def test_Ledger_add():from decimal import Decimal

# Generated at 2026-10-24 13:36:51.663909
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:36:54.616139
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:36:57.736262
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:36:59.126189
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import datetime
    import enum
    from dataclasses import dataclass
    from decimal import Decimal

    # -- Stubs mirroring the domain types the program touches ----------
    class _Direction(enum.Enum):
        DEBIT = 1
        CREDIT = -1

    @dataclass(frozen=True)
    class _Account:
        code: str

    class _Quantity:
        def __init__(self, value):
            self.value = value

        def __add__(self, other):
            return _Quantity(self.value + other.value)

        def __eq__(self, other):
            return isinstance(other, _Quantity) and self.value == other.value

    class _Balance:
        def __init__(self, date, quantity):
            self.date = date
            self.value = quantity

    class _DateRange:
        def __init__(self, since, until):
            self.since = since
            self.until = until

    class _Posting:
        def __init__(self, journal, date, account, amount, direction):
            self.journal = journal
            self.date = date
            self.account = account
            self.amount = amount
            self.direction = direction

        @property
        def is_debit(self):
            return self.direction == _Direction.DEBIT

        @property
        def is_credit(self):
            return self.direction == _Direction.CREDIT

    class _JournalEntry:
        def __init__(self, date, postings):
            self.date = date
            self.postings = postings

    # -- Fixtures -------------------------------------------------------
    period = _DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    cash = _Account("1000")
    sales = _Account("4000")
    rent

# Generated at 2026-10-24 13:37:00.473311
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import datetime
    import enum
    from dataclasses import dataclass
    from decimal import Decimal

    # -- Stubs mirroring the domain types the program touches ----------
    class _Direction(enum.Enum):
        DEBIT = 1
        CREDIT = -1

    @dataclass(frozen=True)
    class _Account:
        code: str

    class _Quantity:
        def __init__(self, value):
            self.value = value

        def __add__(self, other):
            return _Quantity(self.value + other.value)

        def __eq__(self, other):
            return isinstance(other, _Quantity) and self.value == other.value

    class _Balance:
        def __init__(self, date, quantity):
            self.date = date
            self.value = quantity

    class _DateRange:
        def __init__(self, since, until):
            self.since = since
            self.until = until

    class _Posting:
        def __init__(self, journal, date, account, amount, direction):
            self.journal = journal
            self.date = date
            self.account = account
            self.amount = amount
            self.direction = direction

        @property
        def is_debit(self):
            return self.direction == _Direction.DEBIT

        @property
        def is_credit(self):
            return self.direction == _Direction.CREDIT

    class _JournalEntry:
        def __init__(self, date, postings):
            self.date = date
            self.postings = postings

    # -- Fixtures -------------------------------------------------------
    period = _DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    cash = _Account("1000")
    sales = _Account("4000")
    rent

# Generated at 2026-10-24 13:37:03.166166
# Unit test for method add of class Ledger
def test_Ledger_add():
    # -- Arrange --
    import datetime
    from decimal import Decimal
    from unittest.mock import MagicMock

    account = MagicMock(name="account")

    # Initial balance of 1000 as of the first day of the period:
    initial_balance = Balance(datetime.date(2023, 1, 1), Quantity(Decimal("1000")))

    ledger = Ledger(account, initial_balance)

    # A debit posting of 250 (direction value +1 means debit):
    posting_1 = MagicMock(name="posting-1")
    posting_1.date = datetime.date(2023, 1, 15)
    posting_1.amount = Amount(Decimal("250"))
    posting_1.direction.value = 1

    # A credit posting of 400 (direction value -1 means credit):
    posting_2 = MagicMock(name="posting-2")
    posting_2.date = datetime.date(2023, 1, 20)
    posting_2.amount = Amount(Decimal("400"))
    posting_2.direction.value = -1

    # -- Act --
    entry_1 = ledger.add(posting_1)
    entry_2 = ledger.add(posting_2)

    # -- Assert --
    # Entries are buffered in insertion order:
    assert ledger.entries == [entry_1, entry_2]

    # Each entry is linked back to its ledger and posting:
    assert entry_1.ledger is ledger
    assert entry_1.posting is posting_1
    assert entry_2.ledger is ledger
    assert entry_2.posting is posting_2

    # First entry balances the initial balance plus the signed amount:
    assert entry_1.balance == Quantity(Decimal("1250"))

    # Second entry chains onto the running balance, subtracting the credit:
    assert entry_2.balance == Quantity(Decimal("850"))

# Generated at 2026-10-24 13:37:05.675796
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:37:08.089592
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:37:10.502017
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:37:12.915327
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:37:15.328811
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:37:43.636001
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:38:01.297526
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:38:03.712594
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:38:06.126483
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:38:08.540631
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:38:10.954973
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:38:13.369642
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:38:15.783927
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:18.199071
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:20.617723
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:23.025753
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:25.439613
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:27.855294
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:30.270375
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:38:32.680470
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:38:35.093965
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:38:37.505413
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:39.917902
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:42.331622
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:44.746167
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:38:47.161345
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:38:49.575254
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:38:51.988382
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:54.401717
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:56.814890
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:38:59.228565
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:39:01.641663
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:39:04.055950
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:39:06.469405
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:39:08.881790
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:39:11.293159
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:39:13.706195
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:39:16.116023
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:39:18.528688
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:39:20.941074
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:39:23.355436
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:39:25.769191
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:39:28.182657
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:39:30.596411
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:39:33.016509
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:39:35.425276
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:39:37.838614
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:39:40.251815
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:39:42.665511
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:39:45.079043
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:39:47.492403
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:39:49.905090
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:39:52.318073
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:39:54.729858
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:39:57.142233
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:39:59.556458
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:40:01.969934
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:40:04.387198
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:40:06.796415
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:40:09.210849
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:40:11.625698
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:40:14.038069
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:40:16.451474
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:40:18.864836
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:40:21.278835
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:40:23.692923
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:40:26.186484
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:40:28.601014
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:40:31.016000
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:40:33.430604
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:40:35.842270
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:40:38.255011
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:40:40.670058
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:40:43.081800
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:40:45.496420
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:40:47.911028
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:40:50.325761
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:40:52.741030
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:40:55.153286
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:40:57.567767
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:40:59.981971
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:41:02.395078
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:41:04.808686
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:41:07.222535
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:41:09.636663
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:41:12.051893
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:41:14.467211
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:41:16.878863
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:41:19.292043
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:41:21.704932
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:41:24.120176
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:41:26.533533
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:41:28.949833
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:41:31.363843
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:41:33.777676
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:41:36.191067
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:41:39.977006
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:41:42.390683
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:41:44.805358
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:41:47.219468
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:41:49.634568
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:41:52.047000
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:41:54.460825
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:41:56.874857
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:41:59.291669
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:42:01.703314
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:42:04.116360
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:42:06.530526
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:42:08.943222
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:42:11.357049
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:42:13.771617
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:42:16.186887
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:42:18.599793
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:42:21.013170
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:42:23.426694
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:42:41.677832
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:42:59.475818
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:43:01.890694
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:43:04.304317
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:43:06.718108
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:43:09.287119
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:43:11.701999
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:43:14.116832
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:43:16.531054
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:43:18.946772
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:43:21.360302
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:43:33.060326
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:43:35.475130
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:43:37.888166
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:43:40.302237
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:43:42.715428
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:43:45.129457
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:43:47.543942
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:43:49.959490
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:43:52.373675
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:43:54.787382
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:43:57.201379
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:43:59.617323
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:44:02.031013
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:44:04.444760
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:44:06.857920
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:44:09.273250
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:44:11.692767
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:44:14.103804
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:44:16.515561
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:44:18.930736
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:44:21.343211
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:44:23.756845
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:44:26.172655
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:44:28.587629
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:44:30.999511
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:44:33.412817
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:44:35.826009
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:44:38.239072
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:44:40.653813
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:44:43.067001
# Unit test for method __call__ of class ReadInitialBalances