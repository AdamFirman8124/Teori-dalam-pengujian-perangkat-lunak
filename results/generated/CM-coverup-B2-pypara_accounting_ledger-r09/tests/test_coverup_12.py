# file: project/pypara/accounting/ledger.py:189-195
# asked: {"lines": [195], "branches": []}
# gained: {"lines": [195], "branches": []}

import datetime

from pypara.accounting.ledger import ReadInitialBalances
from pypara.commons.zeitgeist import DateRange


def test_read_initial_balances_protocol_call_body_executes_directly():
    period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 12, 31),
    )

    result = ReadInitialBalances.__call__(object(), period)

    assert result is None


def test_read_initial_balances_protocol_call_body_executes_via_subclass():
    class _Reader(ReadInitialBalances):
        pass

    period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 12, 31),
    )
    reader = _Reader()

    result = reader(period)

    assert result is None
    assert reader.__call__(period) is None


def test_read_initial_balances_protocol_call_body_executes_via_super():
    class _Reader(ReadInitialBalances):
        def __call__(self, period: DateRange):
            return super().__call__(period)

    period = DateRange(
        since=datetime.date(2025, 1, 1),
        until=datetime.date(2025, 6, 30),
    )
    reader = _Reader()

    result = reader(period)

    assert result is None
