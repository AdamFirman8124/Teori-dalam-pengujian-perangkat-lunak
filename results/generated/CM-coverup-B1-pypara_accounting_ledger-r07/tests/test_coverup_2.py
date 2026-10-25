# file: project/pypara/accounting/ledger.py:107-146
# asked: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}
# gained: {"lines": [127, 128, 129, 130, 140, 143, 146], "branches": []}

import datetime
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import Posting
try:
    from pypara.accounting.journaling import Direction
except ImportError:  # fallback if re-exported elsewhere
    from pypara.commons.numbers import Direction
from pypara.accounting.ledger import Ledger, LedgerEntry


def _date(y=2023, m=1, d=1):
    return datetime.date(y, m, d)


def test_last_balance_empty_returns_initial_value():
    account = object()
    initial = Balance(date=_date(), value=Decimal("100"))
    ledger = Ledger(account=account, initial=initial)
    assert ledger.entries == []
    assert ledger._last_balance == Decimal("100")
    assert ledger._last_balance == initial.value


def test_last_balance_returns_last_entry_balance():
    account = object()
    initial = Balance(date=_date(), value=Decimal("100"))
    ledger = Ledger(account=account, initial=initial)
    posting = Posting(
        journal=None,
        date=_date(),
        account=account,
        direction=Direction.INC,
        amount=Decimal("10"),
    )
    first = LedgerEntry(ledger=ledger, posting=posting, balance=Decimal("110"))
    second = LedgerEntry(ledger=ledger, posting=posting, balance=Decimal("125"))
    ledger.entries.append(first)
    ledger.entries.append(second)
    try:
        assert ledger._last_balance == Decimal("125")
        assert ledger._last_balance == second.balance
        assert ledger._last_balance is second.balance
    finally:
        ledger.entries.clear()


def test_add_first_entry_uses_initial_balance_inc():
    account = object()
    initial = Balance(date=_date(), value=Decimal("100"))
    ledger = Ledger(account=account, initial=initial)
    posting = Posting(
        journal=None,
        date=_date(),
        account=account,
        direction=Direction.INC,
        amount=Decimal("25"),
    )
    entry = ledger.add(posting)
    try:
        assert entry.ledger is ledger
        assert entry.posting is posting
        assert entry.balance == Decimal("125")
        assert len(ledger.entries) == 1
        assert ledger.entries[0] is entry
        assert ledger._last_balance == Decimal("125")
    finally:
        ledger.entries.clear()


def test_add_chains_balances_and_supports_dec():
    account = object()
    initial = Balance(date=_date(), value=Decimal("200"))
    ledger = Ledger(account=account, initial=initial)
    posting_inc = Posting(
        journal=None,
        date=_date(),
        account=account,
        direction=Direction.INC,
        amount=Decimal("50"),
    )
    posting_dec = Posting(
        journal=None,
        date=_date(2023, 1, 2),
        account=account,
        direction=Direction.DEC,
        amount=Decimal("30"),
    )
    try:
        e1 = ledger.add(posting_inc)
        assert e1.balance == Decimal("250")
        assert ledger._last_balance == Decimal("250")
        e2 = ledger.add(posting_dec)
        assert e2.balance == Decimal("220")
        assert e2.ledger is ledger
        assert e2.posting is posting_dec
        assert len(ledger.entries) == 2
        assert ledger.entries[0] is e1
        assert ledger.entries[1] is e2
        assert ledger._last_balance == Decimal("220")
    finally:
        ledger.entries.clear()
