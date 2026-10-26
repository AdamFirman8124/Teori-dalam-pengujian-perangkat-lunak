# file: project/pypara/accounting/ledger.py:92-97
# asked: {"lines": [97], "branches": []}
# gained: {"lines": [97], "branches": []}

from pypara.accounting.ledger import LedgerEntry


def test_ledger_entry_debit_returns_amount_when_debit(monkeypatch):
    amount = object()
    entry = object.__new__(LedgerEntry)

    monkeypatch.setattr(LedgerEntry, "is_debit", property(lambda self: True))
    monkeypatch.setattr(LedgerEntry, "amount", property(lambda self: amount))

    assert entry.debit is amount


def test_ledger_entry_debit_returns_none_when_not_debit(monkeypatch):
    entry = object.__new__(LedgerEntry)

    def unexpected_amount_access(self):
        raise AssertionError("amount must not be accessed for a non-debit entry")

    monkeypatch.setattr(LedgerEntry, "is_debit", property(lambda self: False))
    monkeypatch.setattr(
        LedgerEntry,
        "amount",
        property(unexpected_amount_access),
    )

    assert entry.debit is None
