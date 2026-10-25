# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

from decimal import Decimal
from types import SimpleNamespace

import pytest

from pypara.accounting.ledger import LedgerEntry


@pytest.mark.parametrize("is_debit", [True, False])
def test_ledger_entry_is_debit_delegates_to_posting(is_debit):
    posting = SimpleNamespace(is_debit=is_debit)
    entry = LedgerEntry(
        ledger=None,
        posting=posting,
        balance=Decimal("0"),
    )

    assert entry.is_debit is is_debit
