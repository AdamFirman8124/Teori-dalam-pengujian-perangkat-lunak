# file: project/pypara/accounting/ledger.py:189-195
# asked: {"lines": [195], "branches": []}
# gained: {"lines": [195], "branches": []}

from pypara.accounting.ledger import ReadInitialBalances


def test_read_initial_balances_protocol_call_returns_none():
    period = object()

    result = ReadInitialBalances.__call__(object(), period)

    assert result is None
