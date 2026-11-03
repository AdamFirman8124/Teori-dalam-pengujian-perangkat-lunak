

# Generated at 2026-11-03 00:11:16.485891
# Unit test for method __eq__ of class LedgerEntry
def test_LedgerEntry___eq__():
    from unittest.mock import MagicMock

    # Shared components used to build entries.
    ledger = MagicMock(name="ledger")
    posting = MagicMock(name="posting")
    balance = Quantity(Decimal("100.00"))

    # An entry is equal to itself.
    entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    assert entry == entry

    # Two entries with identical field values are equal.
    entry1 = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    entry2 = LedgerEntry(ledger=ledger, posting=posting, balance=balance)
    assert entry1 == entry2
    assert not entry1 != entry2

    # Entries with a different balance are not equal.
    entry_diff_balance = LedgerEntry(
        ledger=ledger, posting=posting, balance=Quantity(Decimal("200.00"))
    )
    assert entry1 != entry_diff_balance
    assert not entry1 == entry_diff_balance

    # Entries with a different posting are not equal.
    other_posting = MagicMock(name="other_posting")
    entry_diff_posting = LedgerEntry(ledger=ledger, posting=other_posting, balance=balance)
    assert entry1 != entry_diff_posting

    # Entries belonging to a different ledger are not equal.
    other_ledger = MagicMock(name="other_ledger")
    entry_diff_ledger = LedgerEntry(ledger=other_ledger, posting=posting, balance=balance)
    assert entry1 != entry_diff_ledger

    # Comparison against objects of unrelated types yields inequality.
    assert entry1 != "not-a-ledger-entry"
    assert entry1 != 42
    assert entry1 != None
    assert entry1 != [entry1]

# Generated at 2026-11-03 00:13:34.623447
# Unit test for constructor of class ReadInitialBalances
def test_ReadInitialBalances():
    import pytest

    # ReadInitialBalances is a typing.Protocol and cannot be instantiated directly.
    with pytest.raises(TypeError):
        ReadInitialBalances()

    # A concrete class implementing the protocol can be constructed and invoked.
    class _ConcreteReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {}

    reader = _ConcreteReadInitialBalances()

    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))
    balances = reader(period)

    assert isinstance(balances, dict)
    assert balances == {}
    assert isinstance(reader, _ConcreteReadInitialBalances)