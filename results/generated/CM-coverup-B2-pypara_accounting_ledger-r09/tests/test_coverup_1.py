# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

import datetime
from decimal import Decimal

import pytest

from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import GeneralLedger, Ledger, build_general_ledger
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


class _StubAccount:
    """Minimal concrete implementation of the ``Account`` protocol."""

    def __init__(self, code: str, name: str = "Stub") -> None:
        self._code = code
        self._name = name

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return None

    @property
    def coa(self):
        return None

    @property
    def parent(self):
        return None

    def __repr__(self) -> str:
        return f"_StubAccount({self._code!r})"


@pytest.fixture
def period() -> DateRange:
    return DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))


def _entry(date: datetime.date, *postings) -> JournalEntry:
    entry = JournalEntry(date, "test entry", "test-source")
    for account, quantity in postings:
        entry = entry.post(date, account, Quantity(Decimal(quantity)))
    return entry


def test_build_general_ledger_uses_initial_balances_and_adds_postings(period):
    cash = _StubAccount("1000")
    sales = _StubAccount("4000")
    opening = Balance(datetime.date(2023, 1, 1), Quantity(Decimal("100.00")))
    initial = {cash: opening}

    entry = _entry(
        datetime.date(2023, 3, 1),
        (cash, "50.00"),
        (sales, "-50.00"),
    )

    gl = build_general_ledger(period, [entry], initial)

    assert isinstance(gl, GeneralLedger)
    assert gl.period is period
    assert set(gl.ledgers) == {cash, sales}

    # Pre-existing ledger keeps its opening balance and receives the posting.
    assert isinstance(gl.ledgers[cash], Ledger)
    assert gl.ledgers[cash].account is cash
    assert gl.ledgers[cash].initial == opening
    assert len(gl.ledgers[cash].entries) == 1

    # Unknown account gets a ledger seeded with a zero balance at period start.
    assert gl.ledgers[sales].account is sales
    assert gl.ledgers[sales].initial == Balance(period.since, Quantity(Decimal(0)))
    assert len(gl.ledgers[sales].entries) == 1

    # The caller's initial balances mapping must not be mutated.
    assert initial == {cash: opening}


def test_build_general_ledger_ignores_entries_outside_period(period):
    cash = _StubAccount("1000")
    before = _entry(datetime.date(2022, 12, 31), (cash, "10.00"))
    after = _entry(datetime.date(2024, 1, 1), (cash, "20.00"))
    inside = _entry(datetime.date(2023, 6, 15), (cash, "30.00"))

    gl = build_general_ledger(period, [before, inside, after], {})

    assert set(gl.ledgers) == {cash}
    assert len(gl.ledgers[cash].entries) == 1
    assert gl.ledgers[cash].initial == Balance(period.since, Quantity(Decimal(0)))


def test_build_general_ledger_accepts_empty_journal(period):
    cash = _StubAccount("1000")
    opening = Balance(datetime.date(2023, 1, 1), Quantity(Decimal("7.00")))
    initial = {cash: opening}

    gl = build_general_ledger(period, [], initial)

    assert gl.period is period
    assert set(gl.ledgers) == {cash}
    assert gl.ledgers[cash].initial == opening
    assert gl.ledgers[cash].entries == []
    assert initial == {cash: opening}


def test_build_general_ledger_accepts_generator_journal(period):
    cash = _StubAccount("1000")
    sales = _StubAccount("4000")
    entries = (
        _entry(datetime.date(2023, 2, 1), (cash, "5.00"), (sales, "-5.00")),
        _entry(datetime.date(2023, 4, 1), (cash, "6.00"), (sales, "-6.00")),
    )

    gl = build_general_ledger(period, (e for e in entries), {})

    assert set(gl.ledgers) == {cash, sales}
    assert len(gl.ledgers[cash].entries) == 2
    assert len(gl.ledgers[sales].entries) == 2


def test_build_general_ledger_does_not_mutate_initial_mapping(period, monkeypatch):
    cash = _StubAccount("1000")
    sales = _StubAccount("4000")
    opening = Balance(datetime.date(2023, 1, 1), Quantity(Decimal("1.00")))
    initial = {cash: opening}
    snapshot = dict(initial)

    entry = _entry(datetime.date(2023, 5, 1), (cash, "2.00"), (sales, "-2.00"))
    gl = build_general_ledger(period, [entry], initial)

    assert initial == snapshot
    assert sales not in initial
    assert gl.ledgers is not initial
    assert gl.ledgers[cash].initial == opening
