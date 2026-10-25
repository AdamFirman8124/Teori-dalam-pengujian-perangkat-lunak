# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

import datetime
from decimal import Decimal
from unittest.mock import MagicMock

from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry
from pypara.accounting.ledger import build_general_ledger


class _FakeAccount:
    def __init__(self, code="1000", name="Fake"):
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
        try:
            from pypara.accounting.accounts import AccountType  # type: ignore
            members = list(AccountType)
            if members:
                return members[0]
        except Exception:
            pass
        return MagicMock()

    @property
    def coa(self):
        return MagicMock()

    @property
    def parent(self):
        return None

    def __hash__(self):
        return object.__hash__(self)

    def __eq__(self, other):
        return self is other


def _make_balance(asof, amount_str):
    qty = Quantity(Decimal(amount_str))
    try:
        return Balance(asof, qty)
    except Exception:
        try:
            return Balance(date=asof, quantity=qty)  # type: ignore
        except Exception:
            pass
        try:
            return Balance(asof=asof, value=qty)  # type: ignore
        except Exception:
            pass
        raise


def _try_make_posting(jdate, account, qty):
    from pypara.accounting.journaling import Posting
    import inspect

    # Try introspected signature with keywords if possible
    try:
        sig = inspect.signature(Posting)
        kwargs = {}
        for pname in sig.parameters:
            lname = pname.lower()
            if lname in ("date", "asof", "when"):
                kwargs[pname] = jdate
            elif lname in ("account", "acct"):
                kwargs[pname] = account
            elif lname in ("quantity", "qty", "amount", "value", "balance"):
                kwargs[pname] = qty
        if len(kwargs) >= 3:
            try:
                return Posting(**kwargs)
            except Exception:
                pass
    except Exception:
        pass
    # Try common positional / keyword combos
    attempts = [
        lambda: Posting(jdate, account, qty),
        lambda: Posting(date=jdate, account=account, quantity=qty),
        lambda: Posting(jdate, account, quantity=qty),
    ]
    last_exc = None
    for fn in attempts:
        try:
            return fn()
        except Exception as exc:
            last_exc = exc
            continue
    if last_exc is not None:
        raise last_exc
    raise AssertionError("could not construct Posting")


def _make_entry(jdate, account, amount_str, description="test entry"):
    entry = JournalEntry(date=jdate, description=description, source="test-src")
    qty = Quantity(Decimal(amount_str))
    posted = False
    try:
        res = entry.post(jdate, account, qty)
        if res is not None and isinstance(res, JournalEntry) and res is not entry:
            entry = res
        if len(entry.postings) > 0:
            posted = True
    except Exception:
        posted = False
    if not posted:
        # Fallback: manually append a Posting
        # Ensure postings list is accessible (frozen dataclass still has mutable list)
        try:
            if len(entry.postings) == 0:
                posting = _try_make_posting(jdate, account, qty)
                entry.postings.append(posting)
        except Exception:
            # If manual construction also fails, re-raise to surface error
            raise
    assert len(entry.postings) > 0
    return entry


def _make_period(since, until):
    return DateRange(since=since, until=until)


def test_build_general_ledger_empty_journal_and_empty_initial():
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = _make_period(since, until)
    initial = {}
    journal = []
    gl = build_general_ledger(period, journal, initial)
    assert gl.period == period
    assert gl.ledgers == {}
    assert isinstance(gl.ledgers, dict)


def test_build_general_ledger_creates_ledger_for_new_account():
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = _make_period(since, until)
    account = _FakeAccount(code="1010", name="Cash")
    jdate = datetime.date(2023, 6, 15)
    entry = _make_entry(jdate, account, "100")
    gl = build_general_ledger(period, [entry], {})
    # New ledger must have been created (line 180) and posting added (line 183)
    assert account in gl.ledgers
    ledger = gl.ledgers[account]
    assert ledger.account is account
    assert len(ledger.entries) == 1
    # Initial balance for auto-created ledger must be zero at period.since
    expected_initial = Balance(period.since, Quantity(Decimal(0)))
    assert ledger.initial == expected_initial
    assert gl.period == period


def test_build_general_ledger_reuses_ledger_for_initial_account():
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = _make_period(since, until)
    account = _FakeAccount(code="2020", name="Equity")
    opening = _make_balance(since, "1000")
    initial = {account: opening}
    jdate = datetime.date(2023, 3, 10)
    entry = _make_entry(jdate, account, "250")
    gl = build_general_ledger(period, [entry], initial)
    # Account already in ledgers: must NOT overwrite initial (covers False branch)
    assert account in gl.ledgers
    ledger = gl.ledgers[account]
    assert ledger.initial == opening
    assert ledger.initial is opening or ledger.initial == opening
    assert len(ledger.entries) == 1
    # Ensure zero-balance was not used
    assert ledger.initial != Balance(period.since, Quantity(Decimal(0))) or opening == Balance(period.since, Quantity(Decimal(0)))


def test_build_general_ledger_ignores_out_of_period_entries():
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = _make_period(since, until)
    acc_before = _FakeAccount(code="3010", name="Before")
    acc_after = _FakeAccount(code="3020", name="After")
    acc_inside = _FakeAccount(code="3030", name="Inside")
    entry_before = _make_entry(datetime.date(2022, 12, 31), acc_before, "10", description="before")
    entry_after = _make_entry(datetime.date(2024, 1, 1), acc_after, "20", description="after")
    entry_inside = _make_entry(datetime.date(2023, 5, 5), acc_inside, "30", description="inside")
    # Boundary dates are inclusive
    entry_since = _make_entry(since, _FakeAccount(code="3040", name="Since"), "40", description="since")
    entry_until = _make_entry(until, _FakeAccount(code="3050", name="Until"), "50", description="until")
    since_acc = entry_since.postings[0].account
    until_acc = entry_until.postings[0].account
    gl = build_general_ledger(period, [entry_before, entry_after, entry_inside, entry_since, entry_until], {})
    assert acc_before not in gl.ledgers
    assert acc_after not in gl.ledgers
    assert acc_inside in gl.ledgers
    assert since_acc in gl.ledgers
    assert until_acc in gl.ledgers
    assert len(gl.ledgers[acc_inside].entries) == 1
    assert len(gl.ledgers) == 3


def test_build_general_ledger_mixed_new_and_existing_with_filtering():
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 6, 30)
    period = _make_period(since, until)
    existing = _FakeAccount(code="4010", name="Existing")
    new_acc = _FakeAccount(code="4020", name="New")
    opening = _make_balance(since, "500")
    initial = {existing: opening}
    # Two postings for existing account (covers reuse twice) + one for new + one out-of-period
    e1 = _make_entry(datetime.date(2023, 2, 1), existing, "100", description="e1")
    e2 = _make_entry(datetime.date(2023, 4, 1), existing, "200", description="e2")
    e3 = _make_entry(datetime.date(2023, 3, 15), new_acc, "300", description="e3")
    e_out = _make_entry(datetime.date(2023, 7, 1), new_acc, "999", description="out")
    gl = build_general_ledger(period, [e1, e2, e3, e_out], initial)
    assert set(gl.ledgers.keys()) == {existing, new_acc}
    assert gl.ledgers[existing].initial == opening
    assert len(gl.ledgers[existing].entries) == 2
    assert len(gl.ledgers[new_acc].entries) == 1
    # Verify out-of-period posting was not added (only 1 entry for new_acc, not 2)
    assert gl.period == period
    # Verify auto-created initial is zero
    assert gl.ledgers[new_acc].initial == Balance(period.since, Quantity(Decimal(0)))
