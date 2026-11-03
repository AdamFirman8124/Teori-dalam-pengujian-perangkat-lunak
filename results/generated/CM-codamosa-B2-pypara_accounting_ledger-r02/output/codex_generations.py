

# Generated at 2026-11-03 00:40:27.231805
# Unit test for method __eq__ of class Ledger

# Generated at 2026-11-03 00:42:39.836952
# Unit test for method __eq__ of class Ledger

# Generated at 2026-11-03 00:44:18.229316
# Unit test for method __eq__ of class Ledger
def test_Ledger___eq__():
    from unittest.mock import Mock

    account = Mock(name="account")
    initial = Mock(name="initial")

    ledger_a = Ledger(account=account, initial=initial)
    ledger_b = Ledger(account=account, initial=initial)

    # Equal ledgers: same account, same initial balance, both with empty entries.
    assert ledger_a == ledger_b
    assert not ledger_a != ledger_b
    assert ledger_a == ledger_a

    # Different account -> not equal.
    ledger_c = Ledger(account=Mock(name="other-account"), initial=initial)
    assert ledger_a != ledger_c
    assert not ledger_a == ledger_c

    # Different initial balance -> not equal.
    ledger_d = Ledger(account=account, initial=Mock(name="other-initial"))
    assert ledger_a != ledger_d

    # Different entries -> not equal.
    ledger_e = Ledger(account=account, initial=initial)
    ledger_e.entries.append(Mock(name="entry"))
    assert ledger_a != ledger_e
    assert not ledger_a == ledger_e
# nonce:95c36cac

# Generated at 2026-11-03 00:46:39.972544
# Unit test for constructor of class GeneralLedger