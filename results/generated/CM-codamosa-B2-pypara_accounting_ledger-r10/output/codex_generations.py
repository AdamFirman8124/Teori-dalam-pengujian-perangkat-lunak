

# Generated at 2026-11-02 17:46:23.553101
# Unit test for function build_general_ledger

# Generated at 2026-11-02 17:48:18.525732
# Unit test for function build_general_ledger
def test_build_general_ledger():from decimal import Decimal


# Generated at 2026-11-02 17:51:59.731770
# Unit test for constructor of class ReadInitialBalances
def test_ReadInitialBalances():
    """
    Unit test for the constructor of class ReadInitialBalances.

    ReadInitialBalances is a typing.Protocol and therefore cannot be instantiated
    directly; it defines the structure of functions which read initial balances.
    """
    from decimal import Decimal
    from typing import cast

    from ..commons.numbers import Quantity
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .generic import Balance
    from .ledgering import InitialBalances, ReadInitialBalances

    ## Attempting to instantiate a Protocol directly must fail:
    try:
        ReadInitialBalances()  # type: ignore[abstract]
        raised = False
    except TypeError:
        raised = True
    assert raised, "Instantiating the ReadInitialBalances protocol should raise TypeError"

    ## Opening and closing dates of the accounting period:
    since = datetime.date(2023, 1, 1)
    until = datetime.date(2023, 12, 31)
    period = DateRange(since, until)

    ## Prepare a sample account and its opening balance:
    account = Account(1, "Cash")
    balance = Balance(since, Quantity(Decimal("1000.00")))

    ## Define a function conforming to the ReadInitialBalances protocol:
    def read_initial_balances_impl(period: DateRange) -> InitialBalances:
        return {account: balance}

    ## Cast to the protocol to simulate static conformance:
    reader = cast(ReadInitialBalances, read_initial_balances_impl)

    ## Invoke the conforming implementation and validate the result:
    result = reader(period)

    assert isinstance(result, dict)
    assert account in result
    assert result[account].value == Quantity(Decimal("1000.00"))
    assert result[account].date == since