# file: project/pypara/accounting/ledger.py:198-204
# asked: {"lines": [204], "branches": []}
# gained: {"lines": [204], "branches": []}

from datetime import date

from pypara.accounting.ledger import GeneralLedgerProgram
from pypara.commons.zeitgeist import DateRange


def test_general_ledger_program_protocol_call_default_implementation():
    period = DateRange(since=date(2024, 1, 1), until=date(2024, 1, 31))

    result = GeneralLedgerProgram.__call__(object(), period)

    assert result is None
