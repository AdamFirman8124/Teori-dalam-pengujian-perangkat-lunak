

# Generated at 2026-10-25 04:36:21.633986
# Unit test for method __eq__ of class GeneralLedger

# Generated at 2026-10-25 04:36:43.884784
# Unit test for method __eq__ of class GeneralLedger
def test_GeneralLedger___eq__():first = GeneralLedger("2024-01-01/2024-12-31", {})

# Generated at 2026-10-25 04:36:53.378021
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from unittest.mock import Mock

    period = Mock(spec=DateRange)
    initial_balances: InitialBalances = {}
    journal_entries: List[JournalEntry[object]] = []

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

# Generated at 2026-10-25 04:37:08.061813
# Unit test for method __eq__ of class Ledger
def test_Ledger___eq__():
    account = Mock(spec=Account)
    other_account = Mock(spec=Account)
    initial = Mock(spec=Balance)
    other_initial = Mock(spec=Balance)
    entry = Mock(spec=LedgerEntry)
    other_entry = Mock(spec=LedgerEntry)

    assert Ledger(account, initial) == Ledger(account, initial)
    assert Ledger(account, initial) != Ledger(other_account, initial)
    assert Ledger(account, initial) != Ledger(account, other_initial)
    assert Ledger(account, initial) != object()

    ledger = Ledger(account, initial)
    equal_ledger = Ledger(account, initial)
    ledger.entries.append(entry)
    equal_ledger.entries.append(entry)

    assert ledger == equal_ledger

    equal_ledger.entries.append(other_entry)

    assert ledger != equal_ledger

# Generated at 2026-10-25 04:37:22.351770
# Unit test for constructor of class ReadInitialBalances
def test_ReadInitialBalances():
    """
    ReadInitialBalances is a Protocol: the protocol itself is not instantiable,
    but any object exposing a compatible ``__call__`` satisfies it.
    """
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

    # 1. The protocol itself cannot be constructed.
    with pytest.raises(TypeError):
        ReadInitialBalances()

    # 2. A structural implementation satisfies the protocol and is callable.
    class _StubReadInitialBalances:
        def __init__(self, balances: InitialBalances) -> None:
            self._balances = balances
            self.calls: List[DateRange] = []

        def __call__(self, period: DateRange) -> InitialBalances:
            self.calls.append(period)
            return self._balances

    impl = _StubReadInitialBalances({})
    stub: ReadInitialBalances = impl  # static conformance check

    assert stub(period) == {}
    assert impl.calls == [period]

# Generated at 2026-10-25 04:37:24.767443
# Unit test for constructor of class GeneralLedgerProgram

# Generated at 2026-10-25 04:38:08.430734
# Unit test for constructor of class GeneralLedgerProgram

# Generated at 2026-10-25 04:38:10.848768
# Unit test for constructor of class GeneralLedgerProgram

# Generated at 2026-10-25 04:38:13.265632
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:38:15.805224
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:38:18.220966
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:38:20.635396
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:38:23.228132
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:38:25.644749
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:39:09.287065
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:39:12.943292
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:39:16.214936
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:39:26.260242
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 12, 31),
    )
    expected: InitialBalances = {}

    class FakeReadInitialBalances:
        def module_0.__call__(self, requested_period: DateRange) -> InitialBalances:
            assert requested_period == period
            return expected

    reader: ReadInitialBalances = FakeReadInitialBalances()

    result = reader(period)

    assert result is expected

# Generated at 2026-10-25 04:39:48.163037
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:39:58.197422
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-25 04:40:07.720236
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    from unittest.mock import Mock

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

# Generated at 2026-10-25 04:40:33.218384
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from unittest.mock import Mock

    period = Mock(spec=DateRange)
    initial_balances: InitialBalances = {}
    journal_entries = []

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)

    program = compile_general_ledger_program(
        read_initial_balances,
        read_journal_entries,
    )

    result = program(period)

    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)

    assert isinstance(result, GeneralLedger)
    assert result.period is period
    assert result.ledgers == {}

# Generated at 2026-10-25 04:40:42.844033
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    period = MagicMock(spec=DateRange)
    account = MagicMock(spec=Account)
    balance = MagicMock(spec=Balance)
    expected = {account: balance}

    class StubReadInitialBalances:
        def module_0.__call__(self, requested_period: DateRange) -> InitialBalances:
            assert requested_period is period
            return expected

    reader: ReadInitialBalances = StubReadInitialBalances()

    result = reader(period)

    assert result is expected

# Generated at 2026-10-25 04:40:47.962752
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():from ..commons.zeitgeist import DateRange

    # Define a concrete implementation of the ReadInitialBalances protocol.

# Generated at 2026-10-25 04:41:10.594619
# Unit test for method add of class Ledger
def test_Ledger_add():
    from unittest.mock import Mock

    initial = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(Mock(spec=Account), initial)

    debit_posting = Mock()
    debit_posting.amount = Amount(Decimal("25.00"))
    debit_posting.direction.value = Decimal("1")

    credit_posting = Mock()
    credit_posting.amount = Amount(Decimal("10.00"))
    credit_posting.direction.value = Decimal("-1")

    debit_entry = ledger.add(debit_posting)
    credit_entry = ledger.add(credit_posting)

    assert debit_entry.ledger is ledger
    assert debit_entry.posting is debit_posting
    assert debit_entry.balance == Quantity(Decimal("125.00"))

    assert credit_entry.ledger is ledger
    assert credit_entry.posting is credit_posting
    assert credit_entry.balance == Quantity(Decimal("115.00"))

    assert ledger.entries == [debit_entry, credit_entry]

# Generated at 2026-10-25 04:41:19.810527
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import sys
    from unittest.mock import Mock, patch, sentinel

    read_initial_balances = Mock(return_value=sentinel.initial_balances)
    read_journal_entries = Mock(return_value=sentinel.journal_entries)

    module = sys.modules[compile_general_ledger_program.__module__]

    with patch.object(
        module,
        "build_general_ledger",
        return_value=sentinel.general_ledger,
    ) as build_general_ledger_mock:
        program = module_0.compile_general_ledger_program(
            read_initial_balances,
            read_journal_entries,
        )

        # Compiling the program must not perform any reads.
        read_initial_balances.assert_not_called()
        read_journal_entries.assert_not_called()
        build_general_ledger_mock.assert_not_called()

        result = program(sentinel.period)

    read_initial_balances.assert_called_once_with(sentinel.period)
    read_journal_entries.assert_called_once_with(sentinel.period)
    build_general_ledger_mock.assert_called_once_with(
        sentinel.period,
        sentinel.journal_entries,
        sentinel.initial_balances,
    )
    assert result is sentinel.general_ledger

# Generated at 2026-10-25 04:41:22.339383
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:41:24.754799
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:41:27.169268
# Unit test for method add of class Ledger

# Generated at 2026-10-25 04:41:29.584128
# Unit test for method add of class Ledger

# Generated at 2026-10-25 04:41:30.912310
# Unit test for method add of class Ledger
def test_Ledger_add():import datetime

# Generated at 2026-10-25 04:41:47.970234
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from typing import cast

    account = cast(Account, SimpleNamespace())
    initial = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account, initial)

    debit_posting = cast(
        Posting[object],
        SimpleNamespace(
            amount=Amount(Decimal("25.00")),
            direction=SimpleNamespace(value=1),
        ),
    )

    debit_entry = ledger.add(debit_posting)

    assert debit_entry.ledger is ledger
    assert debit_entry.posting is debit_posting
    assert debit_entry.balance == Quantity(Decimal("125.00"))
    assert ledger.entries == [debit_entry]

    credit_posting = cast(
        Posting[object],
        SimpleNamespace(
            amount=Amount(Decimal("10.00")),
            direction=SimpleNamespace(value=-1),
        ),
    )

    credit_entry = ledger.add(credit_posting)

    assert credit_entry.ledger is ledger
    assert credit_entry.posting is credit_posting
    assert credit_entry.balance == Quantity(Decimal("115.00"))
    assert ledger.entries == [debit_entry, credit_entry]

# Generated at 2026-10-25 04:42:04.812478
# Unit test for method add of class Ledger
def test_Ledger_add():
    initial = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account=object(), initial=initial)

    debit_posting = SimpleNamespace(
        amount=Amount(Decimal("25.50")),
        direction=SimpleNamespace(value=Decimal("1")),
    )

    debit_entry = ledger.add(debit_posting)

    assert debit_entry.ledger is ledger
    assert debit_entry.posting is debit_posting
    assert debit_entry.balance == Quantity(Decimal("125.50"))
    assert ledger.entries == [debit_entry]

    credit_posting = SimpleNamespace(
        amount=Amount(Decimal("10.25")),
        direction=SimpleNamespace(value=Decimal("-1")),
    )

    credit_entry = ledger.add(credit_posting)

    assert credit_entry.balance == Quantity(Decimal("115.25"))
    assert ledger.entries == [debit_entry, credit_entry]
    assert ledger._last_balance == Quantity(Decimal("115.25"))

# Generated at 2026-10-25 04:42:07.362038
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:42:09.890884
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:42:12.452977
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:42:14.867753
# Unit test for method add of class Ledger

# Generated at 2026-10-25 04:42:17.281739
# Unit test for method add of class Ledger

# Generated at 2026-10-25 04:42:19.867197
# Unit test for method add of class Ledger

# Generated at 2026-10-25 04:42:22.390251
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:42:24.806009
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:42:27.219782
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:42:29.636754
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:42:32.051654
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:42:34.466440
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:42:36.881420
# Unit test for method add of class Ledger

# Generated at 2026-10-25 04:42:49.104914
# Unit test for method add of class Ledger
def test_Ledger_add():from decimal import Decimal

# Generated at 2026-10-25 04:43:05.902464
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    import sys
    from unittest.mock import Mock, patch, sentinel

    read_initial_balances = Mock(return_value=sentinel.initial_balances)
    read_journal_entries = Mock(return_value=sentinel.journal_entries)

    module = sys.modules[compile_general_ledger_program.__module__]

    with patch.object(
        module,
        "build_general_ledger",
        return_value=sentinel.general_ledger,
    ) as build_general_ledger:
        program = module_0.compile_general_ledger_program(
            read_initial_balances,
            read_journal_entries,
        )

        # Compiling the program must not perform any reads.
        read_initial_balances.assert_not_called()
        read_journal_entries.assert_not_called()

        result = program(sentinel.period)

    read_initial_balances.assert_called_once_with(sentinel.period)
    read_journal_entries.assert_called_once_with(sentinel.period)
    build_general_ledger.assert_called_once_with(
        sentinel.period,
        sentinel.journal_entries,
        sentinel.initial_balances,
    )
    assert result is sentinel.general_ledger

# Generated at 2026-10-25 04:43:14.559336
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():import datetime

# Generated at 2026-10-25 04:43:24.973673
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace
    from unittest.mock import Mock

    account = Mock(spec=Account)
    initial_balance = Balance(
        datetime.date(2024, 1, 1),
        Quantity(Decimal("100.00")),
    )
    ledger = Ledger(account, initial_balance)

    debit_posting = SimpleNamespace(
        amount=Amount(Decimal("25.00")),
        direction=SimpleNamespace(value=Decimal("1")),
    )
    credit_posting = SimpleNamespace(
        amount=Amount(Decimal("10.00")),
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
    assert ledger._last_balance == Quantity(Decimal("115.00"))

# Generated at 2026-10-25 04:43:27.632186
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:43:30.181292
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:43:32.706394
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:43:35.126065
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:43:37.540658
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-25 04:43:48.188468
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

# Generated at 2026-10-25 04:44:14.301289
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(spec=DateRange)
    read_initial_balances = Mock(return_value={})
    read_journal_entries = Mock(return_value=[])

    program = compile_general_ledger_program(
        read_initial_balances=read_initial_balances,
        read_journal_entries=read_journal_entries,
    )

    result = program(period)

    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)

    assert isinstance(result, GeneralLedger)
    assert result.period is period
    assert result.ledgers == {}

# Generated at 2026-10-25 04:44:30.481871
# Unit test for method add of class Ledger
def test_Ledger_add():
    from types import SimpleNamespace

    opening_balance = Quantity(Decimal("100.00"))
    ledger = Ledger(
        account=object(),  # Account is not used by Ledger.add().
        initial=Balance(datetime.date(2024, 1, 1), opening_balance),
    )

    debit_posting = SimpleNamespace(
        amount=Amount(Decimal("25.50")),
        direction=SimpleNamespace(value=1),
    )

    debit_entry = ledger.add(debit_posting)

    assert debit_entry.ledger is ledger
    assert debit_entry.posting is debit_posting
    assert debit_entry.balance == Quantity(Decimal("125.50"))
    assert ledger.entries == [debit_entry]

    credit_posting = SimpleNamespace(
        amount=Amount(Decimal("10.25")),
        direction=SimpleNamespace(value=-1),
    )

    credit_entry = ledger.add(credit_posting)

    assert credit_entry.ledger is ledger
    assert credit_entry.posting is credit_posting
    assert credit_entry.balance == Quantity(Decimal("115.25"))
    assert ledger.entries == [debit_entry, credit_entry]

# Generated at 2026-10-25 04:44:33.018154
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:44:35.432235
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:44:37.847475
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-25 04:44:51.165490
# Unit test for method add of class Ledger

# Generated at 2026-10-25 04:44:52.501062
# Unit test for method add of class Ledger
def test_Ledger_add():import datetime

# Generated at 2026-10-25 04:45:11.134736
# Unit test for method add of class Ledger
def test_Ledger_add():from types import SimpleNamespace
from typing import cast

# Generated at 2026-10-25 04:45:36.887615
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    from unittest.mock import Mock

    period = Mock()
    account = Mock()
    initial_balance = Mock()
    initial_balances = {account: initial_balance}
    journal_entries = []

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)

    program = compile_general_ledger_program(
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

# Generated at 2026-10-25 04:45:39.297765
# Unit test for method add of class Ledger

# Generated at 2026-10-25 04:45:57.009001
# Unit test for method add of class Ledger
def test_Ledger_add():from decimal import Decimal

# Generated at 2026-10-25 04:46:29.125165
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    import sys
    from unittest.mock import Mock, patch

    period = Mock(spec=DateRange)
    initial_balances = {}
    journal_entries = []
    expected_ledger = Mock(spec=GeneralLedger)

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)

    module = sys.modules[compile_general_ledger_program.__module__]

    with patch.object(
        module,
        "build_general_ledger",
        return_value=expected_ledger,
    ) as build_general_ledger_mock:
        program = compile_general_ledger_program(
            read_initial_balances,
            read_journal_entries,
        )

        result = program(period)

    read_initial_balances.assert_called_once_with(period)
    read_journal_entries.assert_called_once_with(period)
    build_general_ledger_mock.assert_called_once_with(
        period,
        journal_entries,
        initial_balances,
    )
    assert result is expected_ledger