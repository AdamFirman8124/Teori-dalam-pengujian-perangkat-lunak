

# Generated at 2026-10-24 13:25:29.358022
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

# Generated at 2026-10-24 13:26:07.767076
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

# Generated at 2026-10-24 13:27:06.439279
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:27:09.210950
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:27:11.869002
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:28:01.424355
# Unit test for constructor of class ReadInitialBalances

# Generated at 2026-10-24 13:28:10.169482
# Unit test for constructor of class ReadInitialBalances
def test_ReadInitialBalances():
    import pytest

    assert isinstance(ReadInitialBalances, type)
    assert callable(ReadInitialBalances)
    with pytest.raises(TypeError):
        ReadInitialBalances()

# Generated at 2026-10-24 13:28:12.591152
# Unit test for method __repr__ of class LedgerEntry

# Generated at 2026-10-24 13:28:15.007106
# Unit test for method __repr__ of class LedgerEntry

# Generated at 2026-10-24 13:28:17.425045
# Unit test for method __repr__ of class LedgerEntry

# Generated at 2026-10-24 13:28:19.840637
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:28:22.428377
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:28:24.842666
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:28:27.260936
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:28:29.680089
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:28:32.098722
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:28:53.241415
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-24 13:28:55.898382
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:29:13.724215
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:29:16.146714
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:29:18.560852
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:29:20.976275
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:29:23.391926
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:29:25.822343
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:29:28.234629
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:29:30.649252
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:29:33.067691
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:29:35.483257
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:29:52.936799
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:30:15.788305
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

# Generated at 2026-10-24 13:30:18.204424
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:30:20.619633
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:30:23.035035
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:30:25.449002
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:30:27.864185
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:30:30.286403
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:30:32.699057
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:30:35.117440
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:30:37.536960
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:30:43.297183
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

# Generated at 2026-10-24 13:31:04.013080
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-24 13:31:06.420330
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:31:08.838493
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:31:11.462500
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:31:13.875605
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:31:16.409004
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:31:18.825599
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:31:21.243013
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:31:23.664623
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:31:26.077035
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:31:28.493759
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:31:30.935360
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:31:33.529502
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:31:35.974596
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:31:38.497464
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:31:40.910997
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:31:44.087855
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

# Generated at 2026-10-24 13:31:46.753645
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:31:49.410044
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:31:52.149537
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:31:54.874529
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

# Generated at 2026-10-24 13:31:56.217855
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

# Generated at 2026-10-24 13:31:58.924688
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

# Generated at 2026-10-24 13:32:01.983765
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:32:04.575151
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:32:06.989996
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:32:09.406577
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:32:11.822134
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:32:14.365371
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:32:16.796111
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:32:19.212711
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:32:21.629046
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:32:24.207073
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:32:26.621051
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:32:29.035283
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:32:31.451304
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:32:33.866589
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:32:36.280373
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:32:38.694021
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:32:41.107679
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:32:43.520727
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:32:45.934611
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:32:48.354739
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:32:50.770210
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 13:32:53.215435
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:32:55.629609
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:32:58.590730
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:33:01.342646
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-24 13:33:04.183134
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

# Generated at 2026-10-24 13:33:06.881803
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

# Generated at 2026-10-24 13:33:09.964072
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:33:12.719709
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:33:15.389058
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 13:33:18.110644
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:33:35.901610
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:33:38.320189
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:33:40.736145
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:33:43.291219
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:33:45.715938
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 13:33:48.131244
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:33:50.546550
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:33:53.142435
# Unit test for method add of class Ledger

# Generated at 2026-10-24 13:33:55.558955
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:33:57.979370
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:34:16.210579
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:34:18.940637
# Unit test for function build_general_ledger

# Generated at 2026-10-24 13:34:36.820242
# Unit test for function build_general_ledger