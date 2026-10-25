# file: project/pypara/accounting/ledger.py:189-195
# asked: {"lines": [195], "branches": []}
# gained: {"lines": [195], "branches": []}

from pypara.accounting.ledger import ReadInitialBalances
from pypara.commons.zeitgeist import DateRange


def test_read_initial_balances_protocol_call_executes_stub() -> None:
    period = object.__new__(DateRange)

    result = ReadInitialBalances.__call__(object(), period)

    assert result is None
