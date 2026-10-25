# file: project/pypara/accounting/ledger.py:189-195
# asked: {"lines": [195], "branches": []}
# gained: {"lines": [195], "branches": []}

import datetime

from pypara.accounting.ledger import ReadInitialBalances
from pypara.commons.zeitgeist import DateRange


def test_read_initial_balances_protocol_default_call_executes() -> None:
    class ConcreteReadInitialBalances(ReadInitialBalances):
        pass

    period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 1, 31),
    )

    assert ConcreteReadInitialBalances()(period) is None
