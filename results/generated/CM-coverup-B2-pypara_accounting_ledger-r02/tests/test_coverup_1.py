# file: project/pypara/accounting/ledger.py:162-186
# asked: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}
# gained: {"lines": [174, 177, 179, 180, 183, 186], "branches": [[177, 179], [177, 186], [179, 180], [179, 183]]}

import datetime
import types
from unittest.mock import MagicMock


import pypara.accounting.ledger as ledger_mod


def test_build_general_ledger_empty_journal_and_empty_initial(monkeypatch):
    mock_ledger_cls = MagicMock()
    mock_balance_cls = MagicMock()
    mock_gl_cls = MagicMock(return_value="GL_EMPTY_SENTINEL")
    monkeypatch.setattr(ledger_mod, "Ledger", mock_ledger_cls)
    monkeypatch.setattr(ledger_mod, "Balance", mock_balance_cls)
    monkeypatch.setattr(ledger_mod, "GeneralLedger", mock_gl_cls)

    period = types.SimpleNamespace(
        since=datetime.date(2021, 1, 1), until=datetime.date(2021, 12, 31)
    )

    result = ledger_mod.build_general_ledger(period, [], {})

    assert result == "GL_EMPTY_SENTINEL"
    mock_ledger_cls.assert_not_called()
    mock_balance_cls.assert_not_called()
    mock_gl_cls.assert_called_once()
    gl_args = mock_gl_cls.call_args[0]
    assert gl_args[0] is period
    assert gl_args[1] == {}


def test_build_general_ledger_initial_plus_new_and_filtered_entries(monkeypatch):
    mock_balance_cls = MagicMock()
    mock_gl_cls = MagicMock(return_value="GL_SENTINEL")
    # each Ledger(account, balance) call returns a fresh mock ledger
    mock_ledger_cls = MagicMock(side_effect=lambda a, b: MagicMock())
    monkeypatch.setattr(ledger_mod, "Ledger", mock_ledger_cls)
    monkeypatch.setattr(ledger_mod, "Balance", mock_balance_cls)
    monkeypatch.setattr(ledger_mod, "GeneralLedger", mock_gl_cls)

    period = types.SimpleNamespace(
        since=datetime.date(2021, 1, 1), until=datetime.date(2021, 12, 31)
    )
    acc_existing = "ACC_EXISTING"
    acc_new = "ACC_NEW"
    existing_balance = object()
    initial = {acc_existing: existing_balance}

    posting_existing = types.SimpleNamespace(account=acc_existing)
    posting_new = types.SimpleNamespace(account=acc_new)
    posting_after = types.SimpleNamespace(account="ACC_AFTER")
    posting_before = types.SimpleNamespace(account="ACC_BEFORE")

    journal = [
        types.SimpleNamespace(
            date=datetime.date(2021, 6, 15),
            postings=[posting_existing, posting_new],
        ),
        # outside period: after until -> must be filtered out
        types.SimpleNamespace(
            date=datetime.date(2022, 1, 10), postings=[posting_after]
        ),
        # outside period: before since -> must be filtered out
        types.SimpleNamespace(
            date=datetime.date(2020, 12, 31), postings=[posting_before]
        ),
    ]

    result = ledger_mod.build_general_ledger(period, journal, initial)

    assert result == "GL_SENTINEL"
    # 1 for initial + 1 for the new account inside period
    assert mock_ledger_cls.call_count == 2
    # Balance used once for the newly created ledger
    assert mock_balance_cls.call_count == 1
    bal_args = mock_balance_cls.call_args[0]
    assert bal_args[0] == period.since

    mock_gl_cls.assert_called_once()
    gl_args = mock_gl_cls.call_args[0]
    assert gl_args[0] is period
    ledgers = gl_args[1]
    assert set(ledgers.keys()) == {acc_existing, acc_new}
    # existing ledger got its posting (False branch of `if account not in ledgers`)
    ledgers[acc_existing].add.assert_called_once_with(posting_existing)
    # new ledger got its posting (True branch creating Ledger+Balance)
    ledgers[acc_new].add.assert_called_once_with(posting_new)
    # filtered postings never added
    for ledger in ledgers.values():
        for c in ledger.add.call_args_list:
            assert c[0][0] is not posting_after
            assert c[0][0] is not posting_before


def test_build_general_ledger_reuses_newly_created_ledger(monkeypatch):
    mock_balance_cls = MagicMock()
    mock_gl_cls = MagicMock(return_value="GL_REUSE_SENTINEL")
    mock_ledger_cls = MagicMock(side_effect=lambda a, b: MagicMock())
    monkeypatch.setattr(ledger_mod, "Ledger", mock_ledger_cls)
    monkeypatch.setattr(ledger_mod, "Balance", mock_balance_cls)
    monkeypatch.setattr(ledger_mod, "GeneralLedger", mock_gl_cls)

    period = types.SimpleNamespace(
        since=datetime.date(2021, 1, 1), until=datetime.date(2021, 12, 31)
    )
    acc_new = "ACC_REUSED"
    posting1 = types.SimpleNamespace(account=acc_new)
    posting2 = types.SimpleNamespace(account=acc_new)
    journal = [
        types.SimpleNamespace(
            date=datetime.date(2021, 3, 1), postings=[posting1]
        ),
        types.SimpleNamespace(
            date=datetime.date(2021, 9, 1), postings=[posting2]
        ),
    ]

    result = ledger_mod.build_general_ledger(period, journal, {})

    assert result == "GL_REUSE_SENTINEL"
    # Ledger created once (first True branch), second posting hits False branch
    assert mock_ledger_cls.call_count == 1
    assert mock_balance_cls.call_count == 1
    mock_gl_cls.assert_called_once()
    ledgers = mock_gl_cls.call_args[0][1]
    assert set(ledgers.keys()) == {acc_new}
    assert ledgers[acc_new].add.call_count == 2
    ledgers[acc_new].add.assert_any_call(posting1)
    ledgers[acc_new].add.assert_any_call(posting2)
