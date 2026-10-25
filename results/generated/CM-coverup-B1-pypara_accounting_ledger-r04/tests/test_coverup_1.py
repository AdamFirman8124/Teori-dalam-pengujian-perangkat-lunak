# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

import datetime
from decimal import Decimal

from pypara.accounting.ledger import build_general_ledger
from pypara.accounting.generic import Balance
from pypara.accounting.journaling import JournalEntry, Posting, Direction
from pypara.commons.numbers import Quantity
from pypara.commons.zeitgeist import DateRange


class AccountStub:
    """Minimal duck-typed implementation of the Account protocol."""

    def __init__(self, code: str, name: str):
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


def _positive_direction():
    for member in Direction:
        try:
            if Decimal(member.value) > 0:
                return member
        except Exception:
            continue
    return list(Direction)[0]


def _negative_direction():
    for member in Direction:
        try:
            if Decimal(member.value) < 0:
                return member
        except Exception:
            continue
    return list(Direction)[-1]


def _make_journal_entry(date: datetime.date, description: str = "test entry") -> JournalEntry:
    return JournalEntry(date=date, description=description, source=None)


def _make_posting(journal: JournalEntry, date: datetime.date, account: AccountStub,
                  direction, amount: Decimal) -> Posting:
    posting = Posting(journal=journal, date=date, account=account,
                      direction=direction, amount=amount)
    journal.postings.append(posting)
    return posting


def test_build_general_ledger_with_initial_balances_and_new_accounts():
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = DateRange(since=since, until=until)

    cash = AccountStub("100", "Cash")
    sales = AccountStub("400", "Sales")
    rent = AccountStub("500", "Rent")

    pos = _positive_direction()
    neg = _negative_direction()
    assert pos is not neg
    assert Decimal(pos.value) != 0
    assert Decimal(neg.value) != 0

    entry_in_1 = _make_journal_entry(datetime.date(2023, 3, 15))
    posting_cash_in = _make_posting(entry_in_1, datetime.date(2023, 3, 15), cash,
                                    pos, Decimal("1000"))
    posting_sales_in = _make_posting(entry_in_1, datetime.date(2023, 3, 15), sales,
                                     neg, Decimal("1000"))

    entry_in_2 = _make_journal_entry(datetime.date(2023, 6, 1))
    posting_rent_in = _make_posting(entry_in_2, datetime.date(2023, 6, 1), rent,
                                    pos, Decimal("250"))

    entry_before = _make_journal_entry(datetime.date(2022, 12, 31))
    posting_before = _make_posting(entry_before, datetime.date(2022, 12, 31), cash,
                                   pos, Decimal("99999"))

    entry_after = _make_journal_entry(datetime.date(2024, 1, 1))
    posting_after = _make_posting(entry_after, datetime.date(2024, 1, 1), cash,
                                  pos, Decimal("88888"))

    journal = [entry_before, entry_in_1, entry_in_2, entry_after]
    initial = {cash: Balance(date=since, value=Quantity(Decimal("500")))}

    ledger = build_general_ledger(period, journal, initial)

    assert ledger.period == period
    assert set(ledger.ledgers.keys()) == {cash, sales, rent}

    cash_ledger = ledger.ledgers[cash]
    assert cash_ledger.account == cash
    assert cash_ledger.initial == Balance(date=since, value=Quantity(Decimal("500")))
    assert len(cash_ledger.entries) == 1
    assert cash_ledger.entries[0].posting == posting_cash_in
    assert cash_ledger.entries[0].balance == Quantity(
        Decimal("500") + Decimal("1000") * Decimal(pos.value)
    )

    sales_ledger = ledger.ledgers[sales]
    assert sales_ledger.account == sales
    assert sales_ledger.initial == Balance(date=since, value=Quantity(Decimal("0")))
    assert len(sales_ledger.entries) == 1
    assert sales_ledger.entries[0].posting == posting_sales_in
    assert sales_ledger.entries[0].balance == Quantity(
        Decimal("1000") * Decimal(neg.value)
    )

    rent_ledger = ledger.ledgers[rent]
    assert rent_ledger.account == rent
    assert rent_ledger.initial == Balance(date=since, value=Quantity(Decimal("0")))
    assert len(rent_ledger.entries) == 1
    assert rent_ledger.entries[0].posting == posting_rent_in
    assert rent_ledger.entries[0].balance == Quantity(
        Decimal("250") * Decimal(pos.value)
    )

    all_postings = [e.posting for lgr in ledger.ledgers.values() for e in lgr.entries]
    assert posting_before not in all_postings
    assert posting_after not in all_postings
    assert posting_cash_in in all_postings
    assert posting_sales_in in all_postings
    assert posting_rent_in in all_postings


def test_build_general_ledger_with_initial_balances_only():
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = DateRange(since=since, until=until)

    cash = AccountStub("100", "Cash")
    bank = AccountStub("101", "Bank")

    entry_outside = _make_journal_entry(datetime.date(2022, 6, 1))
    _make_posting(entry_outside, datetime.date(2022, 6, 1), cash,
                  _positive_direction(), Decimal("777"))

    initial = {
        cash: Balance(date=since, value=Quantity(Decimal("100"))),
        bank: Balance(date=since, value=Quantity(Decimal("200"))),
    }

    ledger = build_general_ledger(period, [entry_outside], initial)

    assert ledger.period == period
    assert set(ledger.ledgers.keys()) == {cash, bank}
    assert ledger.ledgers[cash].initial == Balance(date=since, value=Quantity(Decimal("100")))
    assert ledger.ledgers[bank].initial == Balance(date=since, value=Quantity(Decimal("200")))
    assert all(len(lgr.entries) == 0 for lgr in ledger.ledgers.values())


def test_build_general_ledger_empty_inputs():
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 1, 31)
    period = DateRange(since=since, until=until)

    ledger = build_general_ledger(period, [], {})

    assert ledger.period == period
    assert ledger.ledgers == {}
