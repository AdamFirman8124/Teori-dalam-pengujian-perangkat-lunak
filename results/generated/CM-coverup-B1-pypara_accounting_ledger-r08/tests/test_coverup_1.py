# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

import datetime
from decimal import Decimal
from unittest.mock import MagicMock

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import GeneralLedger, build_general_ledger
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


def _mock_account(label):
    acct = MagicMock()
    acct.name = label
    acct.__repr__ = lambda s=acct, l=label: f"<Account {l}>"
    return acct


def _qty(value):
    return Quantity(Decimal(str(value)))


def _balance(on, value):
    return Balance(on, _qty(value))


def _entry(entry_date, specs, description="test entry", source="test-src"):
    e = JournalEntry(date=entry_date, description=description, source=source)
    for p_date, acct, amount in specs:
        e.post(p_date, acct, _qty(amount))
    return e


def test_build_general_ledger_empty_journal_empty_initial():
    period = DateRange(
        since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31)
    )
    result = build_general_ledger(period, [], {})
    assert isinstance(result, GeneralLedger)
    assert result.period == period
    assert result.ledgers == {}


def test_build_general_ledger_creates_ledgers_for_new_accounts():
    period = DateRange(
        since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31)
    )
    acc_a = _mock_account("A")
    acc_b = _mock_account("B")
    mid = datetime.date(2023, 6, 15)
    j1 = _entry(mid, [(mid, acc_a, "100")], description="j1")
    j2 = _entry(mid, [(mid, acc_b, "200")], description="j2")
    result = build_general_ledger(period, [j1, j2], {})
    assert isinstance(result, GeneralLedger)
    assert result.period == period
    assert set(result.ledgers.keys()) == {acc_a, acc_b}
    # new ledgers get zero opening balance at period.since
    assert result.ledgers[acc_a].account is acc_a
    assert result.ledgers[acc_b].account is acc_b
    assert result.ledgers[acc_a].initial.value == _qty("0")
    assert result.ledgers[acc_a].initial.date == period.since
    assert result.ledgers[acc_b].initial.value == _qty("0")
    assert result.ledgers[acc_b].initial.date == period.since
    # one posting each added
    assert len(result.ledgers[acc_a].entries) == 1
    assert len(result.ledgers[acc_b].entries) == 1


def test_build_general_ledger_reuses_initial_and_new_ledgers():
    period = DateRange(
        since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31)
    )
    acc_init = _mock_account("INIT")
    acc_new = _mock_account("NEW")
    opening = _balance(period.since, "1000")
    initial = {acc_init: opening}
    mid = datetime.date(2023, 3, 10)
    # one posting to already-ledgred account, one to brand-new account,
    # plus a second posting to the brand-new account to hit the
    # `account in ledgers` False-branch for a just-created ledger
    j1 = _entry(mid, [(mid, acc_init, "50")], description="uses initial")
    j2 = _entry(mid, [(mid, acc_new, "70")], description="creates new")
    j3 = _entry(mid, [(mid, acc_new, "30")], description="reuses new")
    result = build_general_ledger(period, [j1, j2, j3], initial)
    assert set(result.ledgers.keys()) == {acc_init, acc_new}
    # initial ledger object preserved as opening balance
    assert result.ledgers[acc_init].initial == opening
    assert result.ledgers[acc_init].account is acc_init
    assert len(result.ledgers[acc_init].entries) == 1
    # new ledger got zero opening and two entries
    assert result.ledgers[acc_new].initial.value == _qty("0")
    assert result.ledgers[acc_new].initial.date == period.since
    assert len(result.ledgers[acc_new].entries) == 2
    # input dict not mutated in size
    assert set(initial.keys()) == {acc_init}


def test_build_general_ledger_filters_out_of_period_entries():
    period = DateRange(
        since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31)
    )
    acc_in = _mock_account("IN")
    acc_out = _mock_account("OUT")
    before = datetime.date(2022, 12, 31)
    after = datetime.date(2024, 1, 1)
    inside = datetime.date(2023, 7, 1)
    j_before = _entry(before, [(before, acc_out, "999")], description="before")
    j_after = _entry(after, [(after, acc_out, "999")], description="after")
    j_inside = _entry(inside, [(inside, acc_in, "123")], description="inside")
    result = build_general_ledger(period, [j_before, j_inside, j_after], {})
    assert set(result.ledgers.keys()) == {acc_in}
    assert len(result.ledgers[acc_in].entries) == 1
    assert acc_out not in result.ledgers


def test_build_general_ledger_includes_boundary_dates():
    period = DateRange(
        since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31)
    )
    acc = _mock_account("BOUND")
    j_since = _entry(period.since, [(period.since, acc, "10")], description="since")
    j_until = _entry(period.until, [(period.until, acc, "20")], description="until")
    result = build_general_ledger(period, [j_since, j_until], {})
    # both boundary entries are inclusive, same account reuses ledger
    assert set(result.ledgers.keys()) == {acc}
    assert len(result.ledgers[acc].entries) == 2
