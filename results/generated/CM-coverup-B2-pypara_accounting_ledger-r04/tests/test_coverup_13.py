# file: project/pypara/accounting/ledger.py:198-204
# asked: {"lines": [204], "branches": []}
# gained: {"lines": [204], "branches": []}

from pypara.accounting.ledger import GeneralLedgerProgram


def test_general_ledger_program_protocol_call_body() -> None:
    period = object()

    result = GeneralLedgerProgram.__call__(object(), period)

    assert result is None
