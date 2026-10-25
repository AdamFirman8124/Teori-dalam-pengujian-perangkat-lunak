# file: project/pypara/accounting/ledger.py:189-195
# asked: {"lines": [195], "branches": []}
# gained: {"lines": [195], "branches": []}

from pypara.accounting.ledger import ReadInitialBalances


def test_read_initial_balances_protocol_call_stub() -> None:
    result = ReadInitialBalances.__call__(object(), object())

    assert result is None
