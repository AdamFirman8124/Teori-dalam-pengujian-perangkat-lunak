# file: project/pypara/accounting/ledger.py:64-69
# asked: {"lines": [69], "branches": []}
# gained: {"lines": [69], "branches": []}

"""
Coverage tests for ``pypara.accounting.ledger.LedgerEntry.amount``.

The previously uncovered line 69 (``return self.posting.amount``) is executed
by accessing the ``amount`` property on ``LedgerEntry`` instances built around
real ``Posting`` value objects.

All objects created here are pure in-memory values/mocks, so no global state
is touched and no cleanup (monkeypatching, temp files, etc.) is required.
"""

import datetime
from unittest import mock

from pypara.accounting.journaling import Posting
from pypara.accounting.ledger import LedgerEntry
from pypara.commons.numbers import Amount, Quantity


def _make_posting(amount):
    """
    Build a minimal ``Posting`` value object.

    Only the ``amount`` attribute is relevant for the property under test;
    the remaining collaborators are inert mocks/sentinels, which is safe
    because ``Posting`` is a plain (frozen) dataclass without validation.
    """
    return Posting(
        journal=mock.Mock(name="journal-entry"),
        date=datetime.date(2021, 3, 15),
        account=mock.Mock(name="account"),
        direction=mock.sentinel.debit,
        amount=amount,
    )


def test_ledger_entry_amount_delegates_to_posting_amount():
    """
    ``LedgerEntry.amount`` must return exactly the amount carried by its
    posting (executes line 69: ``return self.posting.amount``).
    """
    amount = Amount("250")
    posting = _make_posting(amount)
    balance = Quantity("120")
    ledger = mock.Mock(name="ledger")

    entry = LedgerEntry(ledger=ledger, posting=posting, balance=balance)

    # Postcondition: the property delegates to the posting's amount.
    assert entry.amount == amount
    assert entry.amount == posting.amount

    # Sanity: the entry preserves the collaborators it was constructed with.
    assert entry.posting is posting
    assert entry.ledger is ledger
    assert entry.balance == balance


def test_ledger_entry_amount_reflects_each_entries_own_posting():
    """
    Two ledger entries built from different postings each report the amount
    of their *own* posting, proving the property reads ``self.posting.amount``
    rather than any cached or shared value.
    """
    first_amount = Amount("100")
    second_amount = Amount("75.50")

    first = LedgerEntry(
        ledger=mock.Mock(name="ledger-1"),
        posting=_make_posting(first_amount),
        balance=Quantity("100"),
    )
    second = LedgerEntry(
        ledger=mock.Mock(name="ledger-2"),
        posting=_make_posting(second_amount),
        balance=Quantity("-24.50"),
    )

    assert first.amount == first_amount
    assert second.amount == second_amount
    assert first.amount != second_amount
