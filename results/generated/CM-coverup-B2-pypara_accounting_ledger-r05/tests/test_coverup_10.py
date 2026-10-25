# file: project/pypara/accounting/ledger.py:92-97
# asked: {"lines": [97], "branches": []}
# gained: {"lines": [97], "branches": []}

from decimal import Decimal
from types import SimpleNamespace

import pytest

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize(
    ("is_debit", "expected"),
    [
        (True, Decimal("12.34")),
        (False, None),
    ],
)
def test_ledger_entry_debit(is_debit, expected):
    amount = Decimal("12.34")
    posting = SimpleNamespace(is_debit=is_debit, amount=amount)
    entry = LedgerEntry(ledger=object(), posting=posting, balance=Decimal("0"))

    assert entry.debit == expected
    if is_debit:
        assert entry.debit is amount
