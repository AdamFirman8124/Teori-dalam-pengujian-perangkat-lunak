# file: project/pypara/accounting/ledger.py:198-204
# asked: {"lines": [204], "branches": []}
# gained: {"lines": [204], "branches": []}

from datetime import date

from pypara.accounting.ledger import GeneralLedgerProgram
from pypara.commons.zeitgeist import DateRange


def test_general_ledger_program_protocol_call_body_executes():
    """
    The `__call__` method of the `GeneralLedgerProgram` protocol only contains
    a `pass` statement. Since protocols cannot be instantiated, the method body
    is executed by invoking the unbound function with a dummy `self`.
    """
    period = DateRange(since=date(2021, 1, 1), until=date(2021, 12, 31))

    # Invoke the protocol method body directly (line 204: `pass`).
    result = GeneralLedgerProgram.__call__(object(), period)

    # Postcondition: the protocol stub returns nothing.
    assert result is None
