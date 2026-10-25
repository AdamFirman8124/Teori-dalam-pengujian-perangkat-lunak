# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

from datetime import date
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Direction, Posting
from pypara.accounting.ledger import Ledger
from pypara.commons.numbers import Amount, Quantity


class _StubAccount:
    """Minimal stand-in satisfying the runtime-checkable Account protocol."""

    def __init__(self, code: str, name: str):
        self.code = code
        self.name = name
        self.type = None
        self.coa = None
        self.parent = None


class _StubJournal:
    """Minimal stand-in for a JournalEntry (only used as a reference)."""


def _make_posting(direction: Direction, amount: Amount) -> Posting:
    return Posting(
        journal=_StubJournal(),
        date=date(2024, 1, 15),
        account=_StubAccount("100", "Cash"),
        direction=direction,
        amount=amount,
    )


def test_add_first_entry_uses_initial_balance():
    """Lines 127-130 (IndexError branch) and 140-146: adding to an empty ledger
    must base the running balance on the ledger's initial balance."""
    initial_value = Quantity(Decimal("1000"))
    ledger = Ledger(
        account=_StubAccount("100", "Cash"),
        initial=Balance(date(2024, 1, 1), initial_value),
    )

    # Empty ledger: _last_balance must fall back to initial.value (IndexError branch).
    assert ledger._last_balance == initial_value
    assert ledger.entries == []

    posting = _make_posting(Direction.INC, Amount(Decimal("250")))
    entry = ledger.add(posting)

    # Postconditions of add() (lines 140-146).
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance == Quantity(Decimal("1250"))  # 1000 + 250 * (+1)
    assert ledger.entries == [entry]
    assert ledger._last_balance == Quantity(Decimal("1250"))


def test_add_first_entry_decrement_direction():
    """A DEC posting on an empty ledger subtracts from the initial balance."""
    ledger = Ledger(
        account=_StubAccount("200", "Payables"),
        initial=Balance(date(2024, 1, 1), Quantity(Decimal("500"))),
    )

    posting = _make_posting(Direction.DEC, Amount(Decimal("120")))
    entry = ledger.add(posting)

    assert entry.balance == Quantity(Decimal("380"))  # 500 + 120 * (-1)
    assert ledger._last_balance == Quantity(Decimal("380"))
    assert len(ledger.entries) == 1


def test_add_subsequent_entry_chains_balance():
    """Line 128 (non-exception branch of _last_balance) and 140-146: a second
    posting must chain from the last entry's balance, not the initial one."""
    ledger = Ledger(
        account=_StubAccount("100", "Cash"),
        initial=Balance(date(2024, 1, 1), Quantity(Decimal("100"))),
    )

    first = ledger.add(_make_posting(Direction.INC, Amount(Decimal("50"))))
    second = ledger.add(_make_posting(Direction.DEC, Amount(Decimal("30"))))
    third = ledger.add(_make_posting(Direction.INC, Amount(Decimal("5"))))

    assert first.balance == Quantity(Decimal("150"))   # 100 + 50
    assert second.balance == Quantity(Decimal("120"))  # 150 - 30
    assert third.balance == Quantity(Decimal("125"))   # 120 + 5
    assert ledger.entries == [first, second, third]
    assert ledger._last_balance == Quantity(Decimal("125"))
