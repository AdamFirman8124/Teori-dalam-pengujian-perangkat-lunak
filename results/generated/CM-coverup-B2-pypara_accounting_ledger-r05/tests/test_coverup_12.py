# file: project/pypara/accounting/ledger.py:189-195
# asked: {"lines": [195], "branches": []}
# gained: {"lines": [195], "branches": []}

from unittest.mock import Mock

from pypara.accounting.ledger import ReadInitialBalances
from pypara.commons.zeitgeist import DateRange


def test_read_initial_balances_protocol_default_call_returns_none():
    class Reader(ReadInitialBalances):
        pass

    period = Mock(spec=DateRange)

    assert Reader()(period) is None
