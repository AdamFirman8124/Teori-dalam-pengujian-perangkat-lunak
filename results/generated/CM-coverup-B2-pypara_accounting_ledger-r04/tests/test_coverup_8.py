# file: project/pypara/accounting/ledger.py:78-83
# asked: {"lines": [83], "branches": []}
# gained: {"lines": [83], "branches": []}

"""
Tests targeting `LedgerEntry.is_debit` (line 83 of pypara/accounting/ledger.py),
which delegates to the `is_debit` property of the underlying posting.

`Posting.is_debit` is computed from the posting direction and the type of the
account posted to (via the `_debit_mapping` of the journaling module), so the
mock account used here is given a real account type taken from that mapping
itself. All objects are created locally, no global state is patched or
modified, hence there is no state pollution and no cleanup is required.
"""

import datetime
from unittest.mock import Mock

from pypara.accounting import journaling as journaling_module
from pypara.accounting.journaling import Direction, JournalEntry, Posting
from pypara.accounting.ledger import LedgerEntry


def _all_account_types():
    """
    Returns all account types referenced by the journaling module's debit
    mapping, in a deterministic order.
    """
    return sorted(set().union(*journaling_module._debit_mapping.values()), key=lambda t: t.name)


def _debit_combination():
    """
    Returns a (direction, account_type) combination that the journaling module
    itself considers a debit.
    """
    for direction in (Direction.INC, Direction.DEC):
        types = sorted(journaling_module._debit_mapping[direction], key=lambda t: t.name)
        if types:
            return direction, types[0]
    raise AssertionError("no debit combination found in the journaling debit mapping")


def _credit_combination():
    """
    Returns a (direction, account_type) combination that the journaling module
    itself considers NOT a debit (i.e. a credit).
    """
    for direction in (Direction.INC, Direction.DEC):
        debit_types = set(journaling_module._debit_mapping[direction])
        for account_type in _all_account_types():
            if account_type not in debit_types:
                return direction, account_type
    raise AssertionError("no credit combination found in the journaling debit mapping")


def _make_posting(direction, account_type):
    """
    Builds a real `Posting` with the given direction and account type.

    The account is a mock carrying a real account type (the only attribute
    consulted by `Posting.is_debit`), and the amount is a mock as well, since
    it is irrelevant for the property under test.
    """
    journal = JournalEntry(
        date=datetime.date(2020, 1, 1),
        description="Test journal entry",
        source=None,
    )
    account = Mock(name="account")
    account.type = account_type
    return Posting(
        journal=journal,
        date=datetime.date(2020, 1, 1),
        account=account,
        direction=direction,
        amount=Mock(name="amount"),
    )


def _make_entry(posting):
    """
    Builds a `LedgerEntry` for the given posting.

    Neither the ledger nor the balance are touched by `LedgerEntry.is_debit`,
    so mocks are used for them.
    """
    return LedgerEntry(
        ledger=Mock(name="ledger"),
        posting=posting,
        balance=Mock(name="balance"),
    )


def test_ledger_entry_is_debit_true_when_posting_is_debit():
    """
    `LedgerEntry.is_debit` must return `True` when the underlying posting is a
    debit.
    """
    direction, account_type = _debit_combination()
    posting = _make_posting(direction, account_type)
    entry = _make_entry(posting)

    # Sanity check: the chosen combination really is a debit per the posting.
    assert posting.is_debit is True
    # The ledger entry must delegate to its posting.
    assert entry.is_debit is True
    assert entry.is_debit == posting.is_debit


def test_ledger_entry_is_debit_false_when_posting_is_credit():
    """
    `LedgerEntry.is_debit` must return `False` when the underlying posting is a
    credit.
    """
    direction, account_type = _credit_combination()
    posting = _make_posting(direction, account_type)
    entry = _make_entry(posting)

    # Sanity check: the chosen combination really is a credit per the posting.
    assert posting.is_debit is False
    # The ledger entry must delegate to its posting.
    assert entry.is_debit is False
    assert entry.is_debit == posting.is_debit
