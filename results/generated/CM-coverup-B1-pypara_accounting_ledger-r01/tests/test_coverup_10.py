# file: project/pypara/accounting/ledger.py:92-97
# asked: {"lines": [97], "branches": []}
# gained: {"lines": [97], "branches": []}

from decimal import Decimal
from unittest.mock import MagicMock, PropertyMock, patch

from pypara.accounting.ledger import LedgerEntry


def test_debit_returns_amount_when_is_debit():
    entry = LedgerEntry(ledger=MagicMock(), posting=MagicMock(), balance=Decimal("0"))
    expected = Decimal("100.00")
    with patch.object(LedgerEntry, "is_debit", new_callable=PropertyMock) as mock_is_debit:
        mock_is_debit.return_value = True
        with patch.object(LedgerEntry, "amount", new_callable=PropertyMock) as mock_amount:
            mock_amount.return_value = expected
            result = entry.debit
            assert result == expected
            assert result is expected


def test_debit_returns_none_when_is_credit():
    entry = LedgerEntry(ledger=MagicMock(), posting=MagicMock(), balance=Decimal("0"))
    with patch.object(LedgerEntry, "is_debit", new_callable=PropertyMock) as mock_is_debit:
        mock_is_debit.return_value = False
        with patch.object(LedgerEntry, "amount", new_callable=PropertyMock) as mock_amount:
            mock_amount.return_value = Decimal("100.00")
            result = entry.debit
            assert result is None
