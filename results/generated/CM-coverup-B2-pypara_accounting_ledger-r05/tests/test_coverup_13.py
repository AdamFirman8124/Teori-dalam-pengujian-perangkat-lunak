# file: project/pypara/accounting/ledger.py:198-204
# asked: {"lines": [204], "branches": []}
# gained: {"lines": [204], "branches": []}

import datetime

from pypara.accounting.ledger import GeneralLedgerProgram
from pypara.commons.zeitgeist import DateRange


def test_general_ledger_program_call_protocol_stub_returns_none():
    period = DateRange(
        since=datetime.date(2024, 1, 1),
        until=datetime.date(2024, 12, 31),
    )

    result = GeneralLedgerProgram.__call__(object(), period)

    assert result is None
