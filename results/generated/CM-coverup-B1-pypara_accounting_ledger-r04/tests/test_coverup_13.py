# file: project/pypara/accounting/ledger.py:198-204
# asked: {"lines": [204], "branches": []}
# gained: {"lines": [204], "branches": []}

from pypara.accounting.ledger import GeneralLedgerProgram


def test_general_ledger_program_call_protocol_stub() -> None:
    result = GeneralLedgerProgram.__call__(object(), object())

    assert result is None
