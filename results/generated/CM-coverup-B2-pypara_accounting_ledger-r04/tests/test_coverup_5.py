# file: project/pypara/accounting/ledger.py:57-62
# asked: {"lines": [62], "branches": []}
# gained: {"lines": [62], "branches": []}

"""
Tests targeting the previously uncovered ``LedgerEntry.description`` property
(line 62 of ``pypara/accounting/ledger.py``), which delegates to the
description of the journal entry behind the entry's posting.
"""

import datetime
from decimal import Decimal

import pytest

from pypara.accounting.journaling import JournalEntry, Posting
from pypara.accounting.ledger import LedgerEntry

try:  # ``Direction`` normally lives in ``journaling``; fall back just in case.
    from pypara.accounting.journaling import Direction
except ImportError:  # pragma: no cover
    from pypara.accounting.ledger import Direction


def _any_direction():
    """
    Resolve a valid ``Direction`` member without hard-coding its name,
    since the exact enum member labels vary across versions.
    """
    for candidate in ("INC", "DEBIT", "DR", "INCREASE"):
        if hasattr(Direction, candidate):
            return getattr(Direction, candidate)
    raise AssertionError(f"No usable direction member found on {Direction!r}")


class _StubAccount:
    """Minimal stand-in satisfying the ``Account`` protocol."""

    code = "100"
    name = "Cash"
    type = None
    coa = None
    parent = None


@pytest.mark.parametrize(
    "description",
    [
        "Sale of goods on credit",
        "Bank service charges",
    ],
)
def test_ledger_entry_description_delegates_to_journal_entry(description):
    """
    ``LedgerEntry.description`` must return the description of the journal
    entry that the underlying posting belongs to (line 62).
    """
    date = datetime.date(2024, 1, 1)

    journal = JournalEntry(date=date, description=description, source=None)
    posting = Posting(
        journal=journal,
        date=date,
        account=_StubAccount(),
        direction=_any_direction(),
        amount=Decimal("100"),
    )
    entry = LedgerEntry(ledger=None, posting=posting, balance=Decimal("100"))

    # Postcondition: the property delegates to the journal entry's description.
    assert entry.description == description
    assert entry.description == journal.description
