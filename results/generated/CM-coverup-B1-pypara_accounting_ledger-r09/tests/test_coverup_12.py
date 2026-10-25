# file: project/pypara/accounting/ledger.py:189-195
# asked: {"lines": [195], "branches": []}
# gained: {"lines": [195], "branches": []}

from unittest.mock import MagicMock
from pypara.accounting.ledger import ReadInitialBalances


def test_read_initial_balances_protocol_default_call_returns_none():
    fake_self = MagicMock()
    fake_period = MagicMock()
    result = ReadInitialBalances.__call__(fake_self, fake_period)
    assert result is None


def test_read_initial_balances_protocol_instance_call_returns_none():
    instance = object.__new__(ReadInitialBalances)
    fake_period = MagicMock()
    result = instance(fake_period)
    assert result is None
