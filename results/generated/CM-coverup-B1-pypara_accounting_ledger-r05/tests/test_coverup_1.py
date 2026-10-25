# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

from datetime import date
from decimal import Decimal

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import GeneralLedger, build_general_ledger
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


def test_build_general_ledger_initializes_adds_and_filters_postings():
    period = DateRange(date(2024, 1, 1), date(2024, 1, 31))
    existing_account = object()
    new_account = object()
    excluded_account = object()

    opening_balance = Balance(period.since, Quantity(Decimal("10")))
    initial = {existing_account: opening_balance}

    included_entry = JournalEntry(date(2024, 1, 15), "included", None)
    included_entry.post(
        date(2024, 1, 15), existing_account, Quantity(Decimal("2"))
    )
    included_entry.post(
        date(2024, 1, 15), new_account, Quantity(Decimal("-3"))
    )

    before_period = JournalEntry(date(2023, 12, 31), "before", None)
    before_period.post(
        date(2023, 12, 31), excluded_account, Quantity(Decimal("100"))
    )

    after_period = JournalEntry(date(2024, 2, 1), "after", None)
    after_period.post(
        date(2024, 2, 1), excluded_account, Quantity(Decimal("200"))
    )

    result = build_general_ledger(
        period,
        [before_period, included_entry, after_period],
        initial,
    )

    assert isinstance(result, GeneralLedger)
    assert result.period == period
    assert set(result.ledgers) == {existing_account, new_account}
    assert excluded_account not in result.ledgers

    existing_ledger = result.ledgers[existing_account]
    assert existing_ledger.account is existing_account
    assert existing_ledger.initial == opening_balance
    assert len(existing_ledger.entries) == 1
    assert existing_ledger.entries[0].posting is included_entry.postings[0]
    assert existing_ledger.entries[0].balance == Quantity(Decimal("12"))

    new_ledger = result.ledgers[new_account]
    assert new_ledger.account is new_account
    assert new_ledger.initial == Balance(
        period.since, Quantity(Decimal("0"))
    )
    assert len(new_ledger.entries) == 1
    assert new_ledger.entries[0].posting is included_entry.postings[1]
    assert new_ledger.entries[0].balance == Quantity(Decimal("-3"))
