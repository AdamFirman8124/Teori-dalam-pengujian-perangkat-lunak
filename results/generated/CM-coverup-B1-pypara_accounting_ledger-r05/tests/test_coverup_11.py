# file: project/pypara/accounting/ledger.py:189-195
# asked: {"lines": [195], "branches": []}
# gained: {"lines": [195], "branches": []}

import datetime

from pypara.accounting.ledger import ReadInitialBalances
from pypara.commons.zeitgeist import DateRange


class _ConcreteReadInitialBalances(ReadInitialBalances):
    """
    Concrete subclass whose __call__ delegates to the Protocol's own
    (unimplemented) __call__ body, thereby executing line 195 (`pass`).
    """

    def __call__(self, period: DateRange):
        # Invoking the Protocol method directly executes its `pass` body.
        result = super().__call__(period)
        # The Protocol body is `pass`, so it must return None.
        assert result is None
        return {}


def test_read_initial_balances_protocol_body_executes():
    period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 12, 31),
    )
    reader = _ConcreteReadInitialBalances()

    result = reader(period)

    # Postcondition: the concrete wrapper returns its own (empty) mapping,
    # proving the call chain through the Protocol body completed.
    assert result == {}
