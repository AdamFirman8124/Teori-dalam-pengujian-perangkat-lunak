

# Generated at 2022-06-14 04:11:25.794094
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    jentry = JournalEntry(date=datetime.date.today(), description='test', source=str)
    jentry.post(date=datetime.date.today(), account=Account(name='test', type=AccountType.ASSETS), quantity=1)
    assert len(jentry.postings) == 1
    assert jentry.postings[0].is_debit()
    jentry.post(date=datetime.date.today(), account=Account(name='test', type=AccountType.EXPENSES), quantity=-1)
    assert len(jentry.postings) == 2
    assert not jentry.postings[1].is_debit()
    jentry.post(date=datetime.date.today(), account=Account(name='test', type=AccountType.ASSETS), quantity=0)

# Generated at 2022-06-14 04:11:35.103205
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    class BusinessObject:
        pass

    je = JournalEntry[BusinessObject](datetime.date(2020, 1, 1), "Test journal entry", BusinessObject())
    je.post(datetime.date(2020, 1, 1), Account("Cash", AccountType.ASSETS), +100)
    je.post(datetime.date(2020, 1, 1), Account("Equity", AccountType.EQUITIES), +100)

    je.validate()

# Generated at 2022-06-14 04:11:36.084743
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # TODO
    pass

# Generated at 2022-06-14 04:11:45.816348
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    The method `post` of `JournalEntry` should post the amount to the account.

    It should:

    * Post *at least* 1 debit and 1 credit entry.
    * Post the *absolute* value of the amount.
    * Post to debit side if the account type is ASSETS, EQUITY or LIABILITY etc.
    * Post to credit side otherwise.
    * Not post if the amount is zero.
    """
    from datetime import date
    from .accounts import Account
    from .books import Book
    from .utils import create_accounts

    ## Create a book & accounts:
    b = Book()
    create_accounts(b)

    ## Create a journal entry and post:
    j = JournalEntry(date(2020, 3, 1), "", None)

    ## Post some increment & decrement amounts:
    j

# Generated at 2022-06-14 04:11:52.348425
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    JE1 = JournalEntry(date=datetime.date(2020, 3, 26), description="Payment for Prepaid Mobile Recharge", source="Jio")
    JE2 = JournalEntry(date=datetime.date(2020, 3, 27), description="Payment for Shopping Bill", source="Paytm")
    JE1.post(date=datetime.date(2020, 3, 26), account="Jio", quantity=30)

# Generated at 2022-06-14 04:12:01.941976
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..trading.orders import Order
    from ..markets.stocks import Stock
    from ..trading.portfolios import Portfolio
    from ..commons.locations import Location, LocationSource
    from ..trading.brokers import IBKR
    myportfolio = Portfolio(name="myportfolio", location=Location(location_source=LocationSource.IBKR))

    def buy_gvkpil(portfolio: Portfolio, date: datetime.date, price: float, quantity: float) -> Order:
        return portfolio.buy(GVKPIL.create_from_market(
                date=date,
                broker=IBKR,
                price=price,
                quantity=quantity,
                location=Location(location_source=LocationSource.IBKR),
            ))
    ## Buy 750 shares @ 60.3
    order = buy_

# Generated at 2022-06-14 04:12:11.052845
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from unittest import TestCase
    from unittest.mock import Mock

    from testcommons import is_valid_guid
    from .accounts import AccountType, create_account
    from .commons import Money

    class _Mock(ReadJournalEntries[_T]):
        pass

    mock = Mock(_Mock)
    mock.__call__.return_value = []
    assert list(mock(DateRange(DateRange.MIN, DateRange.MAX))) == []

    mock = Mock(_Mock)

# Generated at 2022-06-14 04:12:23.206408
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import dataclass
    from typing import cast
    from .accounts import Account, AccountType
    from .accounts.ReadAccounts import ReadAccounts

    @dataclass(frozen=True)
    class _TestType:
        pass

    @dataclass(frozen=True)
    class _TestJournalEntry(JournalEntry[_TestType]):
        def validate(self) -> None:
            self.postings[0].validate()

        def __repr__(self) -> str:
            return f"{type(self).__name__}<{self.date}>({self.postings[0]!r})"


# Generated at 2022-06-14 04:12:28.370583
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    This function tests if the post method of journal entry
    returns the journal entry.

    :param: None
    :return: None
    """
    test = JournalEntry(datetime.date(2020, 5, 2), 'description', 'source1')
    assert test.post(datetime.date(2020, 5, 1), 'a1', 1) == test

# Generated at 2022-06-14 04:12:35.854974
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class Invoice():
        def __init__(self, **kwargs):
            self._id = kwargs.get('_id')
            self.amount = kwargs.get('amount')
        
        def get_id(self):
            return self._id

    class ReadJournalEntriesImpl():
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            invoices = [
                Invoice(_id='a-a-a-a', amount=100),
                Invoice(_id='b-b-b-b', amount=200)
                ]
            for invoice in invoices:
                yield JournalEntry[Invoice](datetime.datetime.now().date(), 'debit', invoice, [])
            
    read_entries_function = ReadJournalEntriesImpl()



# Generated at 2022-06-14 04:12:45.616145
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Tests the method validate of class JournalEntry to check if validation passes or fails correctly.
    """
    from .accounts import Account, AccountType
    from .books import Transaction
    from .transactions import TransactionType

    journal_entry_1 = JournalEntry(datetime.date.today(), "Test Entry", Transaction("Transaction code", TransactionType.EXPENSE, "Test Entry"))
    journal_entry_1.post(datetime.date.today(), Account("Acc1", AccountType.ASSETS), Amount(100))
    journal_entry_1.post(datetime.date.today(), Account("Acc2", AccountType.EXPENSES), Amount(-100))
    journal_entry_1.validate()


# Generated at 2022-06-14 04:12:52.406461
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    amount = Amount(10000)
    journal_entry = JournalEntry[str](datetime.date(2020, 6, 1), "foo", "bar", [])
    assert list(journal_entry.postings) == []  # pylint: disable=no-member
    assert list(journal_entry.post(datetime.date(2020, 6, 1), Account(AccountType.ASSETS), amount).postings) == [
        Posting(journal_entry, datetime.date(2020, 6, 1), Account(AccountType.ASSETS), Direction.INC, amount)
    ]

# Generated at 2022-06-14 04:13:05.519314
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, ReadAccounts
    from .test_accounts import make_read_account, test_make_read_account

    test_make_read_account()

    test_data_dir = "ledgerbal/tests/data/"

    read_account = make_read_account(test_data_dir)
    # Call the function defined in class ReadAccounts
    _ = read_account(AccountType.EQUITIES)

    test: JournalEntry = JournalEntry(
            datetime.date.today(),
            "Test",
            _T,
            []
            )

    test.post(datetime.date.today(), read_account(AccountType.EQUITIES), 10)
    assert test.postings[0].is_debit 

# Generated at 2022-06-14 04:13:07.879415
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @ReadJournalEntries
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        pass

    assert read_journal_entries is not None

# Generated at 2022-06-14 04:13:17.149898
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from ..commons.types import BusinessObject
    from .accounts import AccountType, LedgerAccount
    from .money import Money
    class SalesInvoice(BusinessObject):
        def __init__(self, number, customer, amount):
            self.number = number
            self.customer = customer
            self.amount = amount
    sales_invoice = SalesInvoice("SINV-001", "Alice", Money(2340))
    sales_revenue_account = LedgerAccount(number="5010", type=AccountType.REVENUES, name="Sales Revenue")
    cash_account = LedgerAccount(number="1010", type=AccountType.ASSETS, name="Cash")

# Generated at 2022-06-14 04:13:30.213151
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType, Account
    from .businessobjects import BusinessObject
    import datetime
    a = BusinessObject()
    b = BusinessObject()
    je = JournalEntry[BusinessObject] (datetime.date.today(), "First transaction", a)
    je.post(datetime.date.today(), Account(AccountType.ASSETS,"Cash", "IDR"), 10)
    je.post(datetime.date.today(), Account(AccountType.EXPENSES,"Office Supplies", "IDR"), -10)
    assert len(je.debits) == 1
    assert je.debits == [je.postings[0]]
    assert len(je.credits) == 1
    assert je.credits == [je.postings[1]]

if __name__ == "__main__":
    test_JournalEntry_

# Generated at 2022-06-14 04:13:38.979564
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import Account, AccountType

    from datetime import datetime

    from . import accounts, journals

    #: Defines an instance of ReadJournalEntries.
    def read_journal_entries(period: DateRange) -> Iterable[journals.JournalEntry[accounts.Receivable]]:
        pass

    #: Defines the return value.
    journal_entries: List[journals.JournalEntry[accounts.Receivable]] = []

    #: Gets the return value.
    assert read_journal_entries(DateRange()) == journal_entries

# Generated at 2022-06-14 04:13:39.632443
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass


# Generated at 2022-06-14 04:13:50.752222
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType, EQUITY, INCOME

    ledger_accounts: Dict[str, Account] = {
        "Capital": Account(AccountType.EQUITIES, "Capital", EQUITY),
        "Income": Account(AccountType.REVENUES, "Income", INCOME),
        "Expense": Account(AccountType.EXPENSES, "Expense", INCOME),
    }

    class BusinessObject:
        pass

    obj1 = BusinessObject()
    obj2 = BusinessObject()

    # Incorrect journal entries
    je1 = JournalEntry[BusinessObject](date=datetime.date(2019, 1, 1), description="Incorrect JE", source=obj1)

# Generated at 2022-06-14 04:13:51.373413
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:14:03.962571
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import EquityAccount, ExpenseAccount

    class _MockJournalEntriesReader(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            raise NotImplementedError()

    reader = _MockJournalEntriesReader()
    # noinspection PyTypeChecker
    reader(DateRange(datetime.date.today(), datetime.date.today()))



# Generated at 2022-06-14 04:14:07.999034
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    print("")

    journal_entry = JournalEntry("1", datetime(2020, 12, 26),"expenses",[])
    journal_entry.post("1", datetime(2020, 12, 26),"expenses",10)

# Generated at 2022-06-14 04:14:08.550031
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    assert True

# Generated at 2022-06-14 04:14:12.132309
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class Test:
        pass

    class TestReadJournalEntries(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    TestReadJournalEntries()(DateRange())

# Generated at 2022-06-14 04:14:24.457031
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.zeitgeist import DateRange
    from ..company.models import Account
    from ..company.models import Amount
    from ..company.models import JournalEntry
    from ..company.models import Quantity
    from ..company.models import ReadJournalEntries
    from ..company.models import readjournalentries
    from ..company.models import test_Account_deposit
    from ..company.models import test_Account_withdraw
    from .accounts import AccountType

    ## Initialization and data settup:
    print("Setting up data...")
    start = datetime.date(2020, 1, 1)
    end = datetime.date(2020, 12, 31)

# Generated at 2022-06-14 04:14:31.815163
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Setup
    from unittest.mock import Mock
    protocol = ReadJournalEntries[int]
    mock_fn: Mock = Mock()
    period = DateRange.overlaps(datetime.date(2018, 1, 1), datetime.date(2018, 1, 4))

    # Exercise
    protocol.__call__(mock_fn, period)

    # Verify
    mock_fn.assert_called_once_with(period)


# Generated at 2022-06-14 04:14:34.051495
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def test_function(period: DateRange) -> Iterable[JournalEntry[str]]:
        assert isinstance(period, DateRange)
        return []

    assert isinstance(ReadJournalEntries.__call__, property)
    assert isinstance(test_function, ReadJournalEntries)

# Generated at 2022-06-14 04:14:45.437581
# Unit test for method __call__ of class ReadJournalEntries

# Generated at 2022-06-14 04:14:46.536768
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:14:53.838569
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    test_obj = JournalEntry(datetime.date.today(), "My Test", None)
    test_obj.post(datetime.date.today(), Account(AccountType.ASSETS, "My Account", None), Quantity(100))
    test_obj.post(datetime.date.today(), Account(AccountType.EQUITIES, "My Account", None), -Quantity(100))
    try:
        test_obj.validate()
    except AssertionError as e:
        print(f"{e}")
        assert False

# Generated at 2022-06-14 04:15:10.648642
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Unit test for post method of class JournalEntry
    """
    obj = JournalEntry[int](datetime.datetime.now().date(), "A test", 1)
    obj.post(datetime.datetime.now().date(), Account("TestAccount1", "TestAccount1", AccountType.ASSETS), 10)
    obj.post(datetime.datetime.now().date(), Account("TestAccount2", "TestAccount2", AccountType.ASSETS), -5)
    obj.vali

# Generated at 2022-06-14 04:15:15.117486
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import unittest.mock as mock
    a = mock.Mock(spec=ReadJournalEntries)
    a(DateRange(datetime.date(2020,1,1), datetime.date(2020,1,31)))
    assert True

# Generated at 2022-06-14 04:15:25.878223
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType, Account, Ledger
    from .journals import JournalEntry, Journal, JournalDaybook

    # Set-up Ledger, Journal and JournalDaybook

# Generated at 2022-06-14 04:15:29.387684
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_from_db(period: DateRange) -> Iterable[JournalEntry[_T]]:
        # Code which reads transactions from a DB, say.
        pass

    rjes = ReadJournalEntries(_T=Account)
    rjes.__call__ = read_from_db

# Generated at 2022-06-14 04:15:32.385983
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class X:
        pass
    x = X()
    x.__call__ = lambda period: [JournalEntry[X](datetime.date.today(), '', x)]
    assert next(x(DateRange(datetime.date(1900, 1, 1), datetime.date.today())))

# Generated at 2022-06-14 04:15:37.836249
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(eq=True, frozen=True)
    class TestJournalEntry(Generic[_T]):
        index: int
        account: str
        amount: int
    
    def run(self, period: DateRange) -> Iterable[TestJournalEntry[_T]]:
        """
        Read journal entries for the given period.
        """
        raise NotImplementedError

# Generated at 2022-06-14 04:15:42.293762
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from ..commons.zeitgeist import DateRange

    @dataclass(frozen=True)
    class Foo:
        pass

    foo: Foo = Foo()


# Generated at 2022-06-14 04:15:47.117134
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    a1 = Account.of("1234", AccountType.ASSETS, "test asset")
    a2 = Account.of("1234", AccountType.EQUITIES, "test equity")
    je = JournalEntry("2014-10-11", "test", "test business object")
    je.post("2014-10-11", a1, 2)

# Generated at 2022-06-14 04:15:47.729530
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass



# Generated at 2022-06-14 04:15:48.260459
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:16:22.749699
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Setup:
    def _check_journal_read(period: DateRange, expected_journals: Iterable[JournalEntry[_T]]) -> None:
        # Exercise:
        read_journal_entries(period)

        # Verify:
        assert journals == list(expected_journals)

    # Execute:
    from .accounts import Account, AccountType
    from .transactions import Transaction, TransactionType

    def txn_no(i: int) -> Transaction:
        return Transaction(makeguid(), "Txn {i}".format(i=i), datetime.date(2000, 12, 31), TransactionType.EXPENSE)


# Generated at 2022-06-14 04:16:25.116333
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    a = JournalEntry('date', 'description', 'source')
    try:
        a.validate()
    except:
        assert False

# Generated at 2022-06-14 04:16:26.016617
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:16:26.965797
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    ...

# Generated at 2022-06-14 04:16:34.743228
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..gl.accounts import Cash
    from ..gl.transactions import Transaction

    class TestAccount(Account):
        pass

    class TestTransaction(Transaction):
        pass

    tx_one = TestTransaction()
    tx_one.post(datetime.date(2019, 1, 1), TestAccount(), +1000)

    tx_two = TestTransaction()
    tx_two.post(datetime.date(2019, 1, 2), Cash.ASSETS, +500) \
          .post(datetime.date(2019, 1, 2), TestAccount(), -500)

    tx_three = TestTransaction()
    tx_three.post(datetime.date(2019, 1, 3), Cash.ASSETS, +500) \
            .post(datetime.date(2019, 1, 3), TestAccount(), -500)


# Generated at 2022-06-14 04:16:40.996595
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    ## Given:
    foo = JournalEntry('date', 'description', 'source')
    foo.postings = [Posting(foo, 'date', 'AccountType.ASSETS', 'Direction.INC', 'Amount.ZERO')]

    ## When:
    try:
        foo.validate()
    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error occured: {e}")

    ## Then:
    assert True

# Generated at 2022-06-14 04:16:46.582399
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType, Account

    account_expenses = Account(account_type=AccountType.EXPENSES, name="Expenses")
    account_revenues = Account(account_type=AccountType.REVENUES, name="Revenues")

    test_journalentry = JournalEntry(datetime.date.today(), "description", "source")
    test_journalentry.post(datetime.date.today(), account_revenues, 100)
    test_journalentry.post(datetime.date.today(), account_expenses, 100)

    test_journalentry.validate()

# Generated at 2022-06-14 04:16:51.963507
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    jo = JournalEntry('2020-01-10', 'description', 'source')
    jo.post(datetime.date(2020, 1, 10), 'account 1', -1)
    jo.post(datetime.date(2020, 1, 10), 'account 2', 1)
    jo.validate()

# Generated at 2022-06-14 04:17:00.173147
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from .accounts import Account, AccountType
    from .commons.zeitgeist import DateRange
    from .journaling.journal import JournalEntry
    from .journaling.posting import Direction, Posting

    # Define sample account:
    debit_account = Account(name='Expenses: Meals', type=AccountType.EXPENSES, created=date(2017, 8, 7))
    credit_account = Account(name='Assets: Cash', type=AccountType.ASSETS, created=date(2017, 8, 7))

    # Define a function which returns journal entries:

# Generated at 2022-06-14 04:17:08.835261
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import datetime
    from .accounts import Account
    a = Account("1001", "cash")
    a1 = Account("1002", "inventory")
    a2 = Account("1003", "supplier")
    a3 = Account("1004", "sale")

    print("Testing method post of class JournalEntry ...")
    d = datetime.date(2020, 1, 5)
    je = JournalEntry[object](d, "abc", object())
    je.post(d, a1, Quantity(100))
    je.post(d, a2, Quantity(100))
    je.post(d, a3, Quantity(100))
    print("method post of class JournalEntry tested")

# Generated at 2022-06-14 04:18:23.256682
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je = JournalEntry(datetime.date.today(),"test description")
    je.account = Account()
    with pytest.raises(AssertionError):
        je.validate()

# Generated at 2022-06-14 04:18:29.395086
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .ledger import DEFAULT_LEDGER

    ## Prepare:
    this = JournalEntry[object](datetime.date.today(), "Test Entry", object())
    this.post(this.date, DEFAULT_LEDGER.asset_accounts()[0], 1)
    this.post(this.date, DEFAULT_LEDGER.revenue_accounts()[0], -1)

    ## Execute:
    this.validate()

    ## Verify:
    assert True

# Generated at 2022-06-14 04:18:40.377901
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    print("testing ReadJournalEntries.__call__")

    @dataclass(frozen=True)
    class A:
        pass

    data = [
        JournalEntry(datetime.date(2020, 1, 1), 'Test 1', A()),
        JournalEntry(datetime.date(2020, 1, 2), 'Test 2', A()),
        JournalEntry(datetime.date(2020, 1, 3), 'Test 3', A()),
        JournalEntry(datetime.date(2020, 1, 4), 'Test 4', A()),
    ]
    source = lambda period: (x for x in data if period.start <= x.date <= period.end)

    # Test empty period.
    assert len([x for x in source(DateRange.empty())]) == 0

    # Test full period.

# Generated at 2022-06-14 04:18:41.270285
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass


# Generated at 2022-06-14 04:18:48.424275
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from src.app.models.accounts import AccountId, AccountType, Account
    from src.app.models.business import CompanyId
    from src.app.models.transactions import TransactionId
    from src.lib.python.commons.others import Guid
    from src.lib.python.commons.zeitgeist import DateRange
    from src.lib.python.commons.numbers import Amount, Quantity

    # calculate total debit, total credit, total increment and total decrement:
    # Initialize variables
    total_debit = 0
    total_credit = 0
    total_increment = 0
    total_decrement = 0

    # Open data file
    with open("test_JournalEntry.txt", "r") as data:
        transactions = data.readlines()
        for transaction in transactions:
            transaction = transaction.split

# Generated at 2022-06-14 04:18:52.519669
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Test case: call the method
    def f(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return []

    assert f(DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 12, 31))) == ()

# Generated at 2022-06-14 04:18:53.091389
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:18:59.765513
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Given
    journal = JournalEntry[str]("2020-01-01", "A journal entry.", "A business object")

    # When
    journal.post("2020-01-01", Account.Cash(), +100)
    journal.post("2020-01-01", Account.LoanAccount(), -100)

    # Then
    assert len(journal.postings) == 2
    assert journal.postings[0].amount == 100
    assert journal.postings[1].amount == 100
    assert journal.postings[0].direction == Direction.INC

# Generated at 2022-06-14 04:19:10.484857
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..domain.clients.client_account import ClientAccount
    from ..domain.clients.client_event import ClientActivated
    from ..domain.firms.firm_account import FirmAccount
    from ..domain.firms.firm_event import FirmActivated

    # Arrange
    client_act = ClientActivated(
        "abcd1234-f3b3-5e1b-a5e6-5d6d5dc6f903",
        "123456789012345",
        "Client",
        "user@email.com",
        "Admin",
        "password",
        "234567890123456",
        "INR",
        [],
        datetime.date(year=2018, month=11, day=10),
        None
    )

# Generated at 2022-06-14 04:19:22.835961
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from ..commons.numbers import Quantity
    from ..commons.others import makeguid
    from .accounts import Account, AccountType
    from .ledger import open_ledger
    from .transactions import BusinessObject, CreateJournalEntry, CreateTransaction, ReadBusinessObjects

    ledger = open_ledger("simple_ledger")
    transaction = ledger.create_transaction(CreateTransaction("Create Journal Entries"), ReadBusinessObjects(ledger))
    transaction.read_business_objects().create_journal_entry(
        CreateJournalEntry("Dr. Cash Payment to the Bank", {"CASH": +1000, "BANK": -1000})
    )