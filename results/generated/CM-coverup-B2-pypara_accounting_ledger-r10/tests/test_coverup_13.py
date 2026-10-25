# file: project/pypara/accounting/ledger.py:198-204
# asked: {"lines": [204], "branches": []}
# gained: {"lines": [204], "branches": []}

import datetime

from pypara.accounting.ledger import GeneralLedgerProgram
from pypara.commons.zeitgeist import DateRange


def test_general_ledger_program_protocol_call_body_executes():
    """
    Line 204 (`pass` in the body of ``GeneralLedgerProgram.__call__``) only
    executes when the protocol's own method body is invoked directly, since
    concrete implementations override it.
    """
    period = DateRange(since=datetime.date(2024, 1, 1), until=datetime.date(2024, 12, 31))

    # Invoke the protocol's own (unimplemented) method body with a dummy self.
    result = GeneralLedgerProgram.__call__(object(), period)  # type: ignore[arg-type]

    # Postcondition: the body is a no-op, so the call returns None.
    assert result is None
