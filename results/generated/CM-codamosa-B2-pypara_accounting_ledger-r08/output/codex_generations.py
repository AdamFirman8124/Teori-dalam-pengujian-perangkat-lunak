

# Generated at 2026-11-03 00:13:03.079606
# Unit test for constructor of class GeneralLedgerProgram
def test_GeneralLedgerProgram():
    """
    Unit test for constructor of class GeneralLedgerProgram.

    GeneralLedgerProgram is a typing.Protocol, therefore it cannot be instantiated
    directly. Instead, any callable consuming a DateRange and producing a
    GeneralLedger structurally conforms to it. This test verifies:
      1. The protocol itself is not directly instantiable.
      2. A plain function with a matching signature satisfies the protocol.
      3. A program compiled via compile_general_ledger_program conforms as well.
    """
    # 1. The protocol itself must not be instantiable.
    try:
        GeneralLedgerProgram()  # type: ignore[misc]
        instantiated = True
    except TypeError:
        instantiated = False
    assert not instantiated, "GeneralLedgerProgram is a Protocol and cannot be instantiated directly"

    # Prepare a representative accounting period.
    period = DateRange(since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31))

    # 2. A function matching the protocol's signature conforms to it.
    def _conforming_program(p: DateRange) -> GeneralLedger:
        return GeneralLedger(period=p, ledgers={})

    produced = _conforming_program(period)
    assert isinstance(produced, GeneralLedger)
    assert produced.period == period
    assert produced.ledgers == {}

    # 3. A compiled program obtained via compile_general_ledger_program also conforms.
    def _read_initial_balances(p: DateRange) -> InitialBalances:
        return {}

    def _read_journal_entries(p: DateRange) -> List[JournalEntry]:
        return []

    program = compile_general_ledger_program(_read_initial_balances, _read_journal_entries)
    assert callable(program), "Compiled general ledger program must be callable"

    gl = program(period)
    assert isinstance(gl, GeneralLedger)
    assert gl.period == period
    assert isinstance(gl.ledgers, dict)
    assert gl.ledgers == {}

# Generated at 2026-11-03 00:15:18.470453
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    """
    Tests that a concrete implementation of the ``ReadInitialBalances`` protocol,
    when invoked with a ``DateRange``, returns the expected ``InitialBalances`` mapping.
    """
    ## Prepare the accounting period:
    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))

    ## Prepare accounts and expected initial balances:
    account_cash = AccountMock("Cash")
    account_capital = AccountMock("Capital")
    expected: InitialBalances = {
        account_cash: Balance(period.since, Quantity(Decimal("1000.00"))),
        account_capital: Balance(period.since, Quantity(Decimal("1000.00"))),
    }

    ## Define a concrete implementation of the protocol:
    class _ReadInitialBalances:
        def module_0.__call__(self, period: DateRange) -> InitialBalances:
            assert isinstance(period, DateRange)
            assert period.since == datetime.date(2023, 1, 1)
            assert period.until == datetime.date(2023, 12, 31)
            return expected

    ## Ensure the implementation satisfies the protocol:
    read_initial_balances: ReadInitialBalances = _ReadInitialBalances()

    ## Invoke the callable:
    result = read_initial_balances(period)

    ## Verify the result:
    assert isinstance(result, dict)
    assert result == expected
    assert account_cash in result
    assert account_capital in result
    assert result[account_cash].value == Quantity(Decimal("1000.00"))
    assert result[account_capital].value == Quantity(Decimal("1000.00"))
    assert result[account_cash].date == period.since

# Generated at 2026-11-03 00:18:49.504988
# Unit test for method __eq__ of class LedgerEntry
def test_LedgerEntry___eq__():
    # nonce:59bda02d
    from unittest.mock import MagicMock

    # Shared components used to build ledger entries.
    ledger = MagicMock(name="ledger")
    posting = MagicMock(name="posting")
    balance = Quantity(Decimal("100.00"))

    entry = LedgerEntry(ledger, posting, balance)

    # Equality is reflexive.
    assert entry == entry

    # Two entries with the same field values are equal.
    same_entry = LedgerEntry(ledger, posting, balance)
    assert entry == same_entry
    assert same_entry == entry

    # An entry with a different balance is not equal.
    other_balance_entry = LedgerEntry(ledger, posting, Quantity(Decimal("200.00")))
    assert entry != other_balance_entry
    assert not entry == other_balance_entry

    # An entry with a different posting is not equal.
    other_posting_entry = LedgerEntry(ledger, MagicMock(name="other_posting"), balance)
    assert entry != other_posting_entry

    # An entry with a different ledger is not equal.
    other_ledger_entry = LedgerEntry(MagicMock(name="other_ledger"), posting, balance)
    assert entry != other_ledger_entry

    # An entry is not equal to objects of unrelated types.
    assert entry != "ledger entry"
    assert entry != None
    assert (entry == 42) is False
    assert (entry == None) is False