# file: project/pypara/accounting/ledger.py:198-204
# asked: {"lines": [204], "branches": []}
# gained: {"lines": [204], "branches": []}

from unittest.mock import MagicMock
from pypara.accounting.ledger import GeneralLedgerProgram


def test_general_ledger_program_protocol_call_executes_pass():
    fake_self = MagicMock()
    fake_period = MagicMock()
    result = GeneralLedgerProgram.__call__(fake_self, fake_period)
    assert result is None


def test_general_ledger_program_concrete_subclass_inherits_pass():
    class ConcreteProgram(GeneralLedgerProgram):
        def __call__(self, period):  # type: ignore[override]
            return super().__call__(period)

    program = ConcreteProgram()
    fake_period = MagicMock()
    result = program(fake_period)
    assert result is None


def test_general_ledger_program_unbound_call_with_none_period():
    fake_self = MagicMock()
    result = GeneralLedgerProgram.__call__(fake_self, None)  # type: ignore[arg-type]
    assert result is None
