# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

from datetime import date
from decimal import Decimal
from types import SimpleNamespace

from pypara.accounting import ledger as ledger_module
from pypara.accounting.generic import Balance
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


def test_build_general_ledger_initializes_adds_and_filters_postings(monkeypatch):
    class RecordingLedger:
        def __init__(self, account, initial):
            self.account = account
            self.initial = initial
            self.added = []

        def add(self, posting):
            self.added.append(posting)

    monkeypatch.setattr(ledger_module, "Ledger", RecordingLedger)

    period = DateRange(date(2024, 1, 1), date(2024, 1, 31))
    existing_account = object()
    new_account = object()
    excluded_account = object()
    opening_balance = Balance(date(2023, 12, 31), Quantity(Decimal("125.50")))

    existing_posting = SimpleNamespace(account=existing_account)
    new_posting = SimpleNamespace(account=new_account)
    excluded_posting = SimpleNamespace(account=excluded_account)

    journal = [
        SimpleNamespace(
            date=period.since,
            postings=[existing_posting, new_posting],
        ),
        SimpleNamespace(
            date=period.until,
            postings=[new_posting],
        ),
        SimpleNamespace(
            date=date(2023, 12, 31),
            postings=[excluded_posting],
        ),
        SimpleNamespace(
            date=date(2024, 2, 1),
            postings=[excluded_posting],
        ),
    ]

    result = ledger_module.build_general_ledger(
        period,
        journal,
        {existing_account: opening_balance},
    )

    assert result.period == period
    assert set(result.ledgers) == {existing_account, new_account}

    existing_ledger = result.ledgers[existing_account]
    assert existing_ledger.account is existing_account
    assert existing_ledger.initial == opening_balance
    assert existing_ledger.added == [existing_posting]

    new_ledger = result.ledgers[new_account]
    assert new_ledger.account is new_account
    assert new_ledger.initial == Balance(
        period.since,
        Quantity(Decimal("0")),
    )
    assert new_ledger.added == [new_posting, new_posting]

    assert excluded_account not in result.ledgers


def test_build_general_ledger_returns_empty_ledger_for_no_balances_or_postings():
    period = DateRange(date(2024, 3, 1), date(2024, 3, 31))

    result = ledger_module.build_general_ledger(period, [], {})

    assert result.period == period
    assert result.ledgers == {}
