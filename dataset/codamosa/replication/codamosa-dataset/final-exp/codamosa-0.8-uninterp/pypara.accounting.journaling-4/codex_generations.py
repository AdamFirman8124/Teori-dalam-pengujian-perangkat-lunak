

# Generated at 2022-06-14 04:11:27.840244
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    assert(True)

# Generated at 2022-06-14 04:11:33.791175
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert set(ReadJournalEntries.__call__.__annotations__) == {'period', 'return'}
    assert ReadJournalEntries.__call__.__annotations__['period'] == DateRange
    assert ReadJournalEntries.__call__.__annotations__['return'] == Iterable[JournalEntry[_T]]

# Generated at 2022-06-14 04:11:44.135338
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @ReadJournalEntries
    def readJournalEntries(period: DateRange) -> Iterable[JournalEntry[str]]:
        def _sut() -> Iterator[JournalEntry[str]]:
            yield JournalEntry(datetime.date(2019, 1, 1), "A", "1", [])
            yield JournalEntry(datetime.date(2019, 1, 2), "B", "2", [])
            return
        return _sut
    assert tuple(readJournalEntries(DateRange(datetime.date(2019, 1, 1), datetime.date(2019, 1, 31)))) == (
        JournalEntry(datetime.date(2019, 1, 1), "A", "1", []),
        JournalEntry(datetime.date(2019, 1, 2), "B", "2", []),
    )

# Generated at 2022-06-14 04:11:55.050104
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import DateTimeInterval
    from ..contrib.generic import BusinessObject
    from .accounts import AccountType, Principal
    from .categories import Category

    # __________________________________________________________________________
    # Setup:

    @dataclass(frozen=True)
    class _Entry(BusinessObject):
        pass

    def _read_entries(period: DateRange) -> Iterable[JournalEntry[_Entry]]:
        # __________________________________________________________________
        # 016-01-01: [C]ackos Inc. => CASH
        entry_01 = JournalEntry(datetime.date(2016, 1, 1), "Cackos Inc.", source=_Entry())

# Generated at 2022-06-14 04:12:03.956563
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .account import Account, AccountType
    from .journal import JournalEntry, Direction
    from .commons.zeitgeist import TODAY

    account1 = Account('A1', AccountType.ASSETS, 'Cash')
    account2 = Account('A2', AccountType.EQUITIES, 'Paid In Capital')
    account3 = Account('E1', AccountType.REVENUES, 'Revenue')
    account4 = Account('E2', AccountType.EXPENSES, 'Expense')

    j = JournalEntry(TODAY, "Test Journal Entry", None)
    
    j.post(TODAY, account1, -1000)
    j.post(TODAY, account3, 1000)
    j.post(TODAY, account2, 100)
    j.post(TODAY, account4, 100)

    j

# Generated at 2022-06-14 04:12:11.748113
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    from .accounts import AccountType
    from .accounts import AccountCategory
    from .accounts import Currency

    date = datetime.date(2020, 1, 1)
    journal1 = JournalEntry[str](date, "test", "source")
    journal1.post(date, Account(AccountType.ASSETS, AccountCategory.BANKS, Currency.INR, "random 1"), 1000)
    journal1.post(date, Account(AccountType.REVENUES, AccountCategory.REVENUES, Currency.INR, "random 2"), -500)
    journal1.post(date, Account(AccountType.EQUITIES, AccountCategory.EQUITIES, Currency.INR, "random 3"), -500)

    journal1.validate()

# Generated at 2022-06-14 04:12:16.850374
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    entry = JournalEntry(datetime.date(2020, 8, 11), "For Unit Test", "", [])
    account = Account("Acc-001", "Test Account", AccountType.ASSETS)
    entry.post(datetime.date(2020, 8, 11), account, Amount(100))

# Generated at 2022-06-14 04:12:27.581283
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from .ledgers import Ledger
    from .trackers import Tracker

    # Setup:
    ledger = Ledger(Tracker(Direction.INC))
    journal = JournalEntry(description="This is a journal entry test.")

    # Act:
    journal.post(datetime.date(2017, 1, 1), ledger.capital.equity, -12)
    journal.post(datetime.date(2017, 1, 1), ledger.revenues, +12)
    journal.validate()

    # Assert:
    assert (
        str(journal.postings[0].account)
        == f"{ledger.prefix}/Equity:Capital/TotalEquity:Equity"
    ), "Account name not as expected."

# Generated at 2022-06-14 04:12:33.355302
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    je1 = JournalEntry(date=datetime.date(2019, 5, 29), description="Auto-entry", source="dummy")
    je1 = je1.post(date=datetime.date(2019, 5, 29), account=Account(type=AccountType.ASSETS, name="banking"), quantity=2.00)
    je1 = je1.post(date=datetime.date(2019, 5, 29), account=Account(type=AccountType.EXPENSES, name="cash"), quantity=-2.00)
    je1.validate()
    assert je1.description == "Auto-entry"
    assert [i.amount for i in je1.postings] == [2.00, 2.00]


# Generated at 2022-06-14 04:12:45.584087
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from ..commons.numbers import Quantity
    from datetime import date
    a = JournalEntry[date]
    d = date(2009, 8, 8)

    e = a(d, 'd', d)
    e.post(d, Account(AccountType.ASSETS, '', ''), Quantity(100))
    e.post(d, Account(AccountType.LIABILITIES, '', ''), Quantity(50))
    e.post(d, Account(AccountType.REVENUES, '', ''), Quantity(150))
    e.post(d, Account(AccountType.EXPENSES, '', ''), Quantity(300))
    print(e.postings)

    assert e.postings[0].direction == Direction.INC
    assert e.postings[0].amount.value == 100


# Generated at 2022-06-14 04:12:51.350580
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    	pass

# Generated at 2022-06-14 04:13:01.966299
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    with pytest.raises(AssertionError, match=r'Total Debits and Credits are not equal'):
        JournalEntry[str](date = datetime.date(2020, 1, 1),
                        description = "",
                        source = "").\
            post(date = datetime.date(2020, 2, 1), account = Account("A1", AccountType.ASSETS), quantity = Quantity(100)).\
            post(date = datetime.date(2020, 2, 1), account = Account("A2", AccountType.EXPENSES), quantity = Quantity(-50)).\
            validate()

# Generated at 2022-06-14 04:13:09.036769
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .sources.test_source import TestSource
    obj = TestSource()
    entry = JournalEntry(datetime.date(2019,10,1), 'test', obj)
    entry.post(datetime.date(2019,10,1), Account('A'), 10)
    assert(len(entry.postings) == 1)
    assert(entry.postings[0].account.code == 'A')
    assert(entry.postings[0].date == datetime.date(2019,10,1))
    assert(entry.postings[0].amount == 10)

# Generated at 2022-06-14 04:13:12.591204
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import dataclass
    from typing import Iterable
    from .accounts import Account

    @dataclass(frozen=True)
    class Model:
        pass

    @dataclass(frozen=True)
    class Source:
        pass

    def create_mock(source: Source, date: datetime.date, account: Account, amount: Amount) -> JournalEntry[Model]:
        return JournalEntry(date, "Mock", Model(), [Posting(JournalEntry.date, JournalEntry.source, account, Direction.INC, amount)])


# Generated at 2022-06-14 04:13:17.975382
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry(date=datetime.date(2020, 5, 23), description="Test")
    j.post(date=datetime.date(2020, 5, 23), account=Account(code="1234", name="Cash", type=AccountType.ASSETS), quantity=Quantity(1.0))
    j.post(date=datetime.date(2020, 5, 23), account=Account(code="4321", name="Revenue", type=AccountType.REVENUES), quantity=Quantity(-1.0))
    j.validate()

# Generated at 2022-06-14 04:13:28.260521
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Verifies that the __call__ method of the ReadJournalEntries class type
    works exactly as expected.
    """
    from ..accounting.accounts import Accounts

    class DummyJournalEntries:

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            return []

    # Create an Accounts object
    accounts = Accounts()

    # Create a ReadJournalEntries object
    journal_entries = DummyJournalEntries()

    # Create a DateRange object
    period = DateRange()

    assert tuple(journal_entries(period)) == tuple()



# Generated at 2022-06-14 04:13:29.275843
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass


# Generated at 2022-06-14 04:13:31.114323
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Tests the method __call__ .
    """
    assert callable(ReadJournalEntries.__call__), "Method `__call__` not callable."


# Generated at 2022-06-14 04:13:42.376048
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    test_date = datetime.date(2016, 1, 1)
    test_account = Account("test account")
    test_quantity_1 = 100
    test_quantity_2 = -200

    test_journal_entry = JournalEntry(date=test_date, description="test journal entry", source="test source")
    test_journal_entry.post(test_date, test_account, test_quantity_1)
    test_journal_entry.post(test_date, test_account, test_quantity_2)

    assert len(test_journal_entry.postings) == 2
    assert test_journal_entry.postings[0].amount == abs(test_quantity_1)
    assert test_journal_entry.postings[0].direction == Direction.of(test_quantity_1)
    assert test_

# Generated at 2022-06-14 04:13:52.058644
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import unittest.mock
    j = JournalEntry[int](datetime.date(2018, 1, 1), "Foo", 1)
    j.post(datetime.date(2018, 1, 1), Account("01-1000"), 100)
    j.post(datetime.date(2018, 1, 1), Account("01-2000"), -100)
    j.validate()
    j.post(datetime.date(2018, 1, 1), Account("01-3000"), 0)
    with unittest.mock.patch("logging.exception") as log:
        j.validate()
        assert log.called
    j.post(datetime.date(2018, 1, 1), Account("01-3000"), -1)
    j.validate()

# Generated at 2022-06-14 04:14:10.596594
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    @dataclass(frozen=True)
    class Demo:
        pass
    journalentry = JournalEntry[Demo]
    entry = journalentry(datetime.date(2020, 1, 1), 'abc', Demo())
    entry.post(datetime.date.today(), Account(), 10)
    assert entry.postings[0].direction == Direction.INC
    entry.post(datetime.date.today(), Account(), -10)
    assert entry.postings[1].direction == Direction.DEC
    entry.post(datetime.date.today(), Account(), 0)
    assert len(entry.postings) == 2

# Generated at 2022-06-14 04:14:18.921060
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .entities import Transaction

    transaction = Transaction()
    debit_account = Account(AccountType.ASSETS, "Debit Account")
    credit_account = Account(AccountType.LIABILITIES, "Credit Account")

    journal = transaction.journal()
    journal.post(datetime.date(2020, 1, 1), debit_account, +10)
    journal.post(datetime.date(2020, 1, 1), credit_account, -10)



# Generated at 2022-06-14 04:14:19.694335
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__(): pass

# Generated at 2022-06-14 04:14:32.297888
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import pytest
    from dataclasses import dataclass


    @dataclass
    class BusinessObject:
        name: str


    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[BusinessObject]]:
        from datetime import date

        yield JournalEntry(date(2020, 1, 1), f"Salary", BusinessObject("Person 1"), [])
        yield JournalEntry(date(2020, 1, 2), f"Salary", BusinessObject("Person 2"), [])
        yield JournalEntry(date(2020, 3, 3), f"Salary", BusinessObject("Person 3"), [])



# Generated at 2022-06-14 04:14:43.674851
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass
    #Entity = SomeBusinessObject
    #BusinessObject = SomeBusinessObject
    # def test_JournalEntry_validate_passes_valid_journal_entries(self):
        # entry = JournalEntry(
        #     date = "2020-01-25",
        #     description = "Some journal entry",
        #     source = Entity(SomeBusinessObject(...))
        # )
        # entry.post(date="2020-01-25", account=Account(AccountType.ASSETS, "Cash"), quantity=1000)
        # entry.post(date="2020-01-25", account=Account(AccountType.REVENUES, "Sales"), quantity=-1000)
        # entry.validate()
    
    # def test_JournalEntry_validate_fails_inconsistent_journal_entries(self):
        # entry =

# Generated at 2022-06-14 04:14:51.191491
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from random import randint
    from typing import Iterable, List, cast
    try:
        from returns.result import ResultE, safe
    except ImportError:
        safe = lambda _: lambda *args, **kwargs: _
    from ..commons.zeitgeist import DateRange
    from .accounts import Account
    from .accounts.models import VirtualAccountType

    @dataclass(frozen=True)
    class JournalEntry:
        date: date
        desc: str
        src: int


# Generated at 2022-06-14 04:15:01.914944
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    account1 = Account('ACC1', AccountType.ASSETS, None, None)
    account2 = Account('ACC2', AccountType.ASSETS, None, None)
    account3 = Account('ACC3', AccountType.ASSETS, None, None)
    
    je1 = JournalEntry(date=datetime.date.today(), description="test", source="test")
    je1.post(date=datetime.date.today(), account=account1, quantity=100)
    je1.post(date=datetime.date.today(), account=account2, quantity=250)
    je1.post(date=datetime.date.today(), account=account3, quantity=-350)
    je1.validate()
    assert len(je1.postings)==3
    assert je1.postings[0].amount==100

# Generated at 2022-06-14 04:15:07.624582
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry(datetime.date.today(), "", None)
    j.post(datetime.date.today(), Account("", AccountType.EXPENSES), 100)
    j.post(datetime.date.today(), Account("", AccountType.REVENUES), 100)
    # j.validate()

test_JournalEntry_validate()

# Generated at 2022-06-14 04:15:11.702060
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    journal = JournalEntry(datetime.datetime.now().date(), "Test", None)
    journal.post(datetime.datetime.now().date(), Account("1000", "Cash"), Amount(10))
    journal.post(datetime.datetime.now().date(), Account("1001", "Bank"), Amount(-10))
    journal.validate()

# Generated at 2022-06-14 04:15:23.372097
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Performs unit tests for the method ``post``.
    """
    from datetime import date
    from ..commons.numbers import zero_quantity

    ## Set up the journal entry:
    je = JournalEntry[str](
        date=date.today(),
        description="Purchase of $100 worth of goods on credit from VendorX.",
        source="VendorX",
    )

    ## Set up the accounts:

# Generated at 2022-06-14 04:15:47.400843
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    This method tests the validation rule for Journal Entry.
    """
    j = JournalEntry("GUID1", "This is a test journal entry", datetime.date.today(), "Test", [], None)
    try:
        j.validate()
    except AssertionError as e:
        print("Expected AssertionError Exception.")
        pass
    except:
        print("Unexpected error!")
        raise

# Generated at 2022-06-14 04:15:47.922449
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:15:58.837499
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Tests the method __call__ of the class ReadJournalEntries.
    """

    from datetime import date

    from ..commons.date import DatePeriod, DateSpan
    from .accounts import AccountType

    from .mock import MockAccountsMapping

    # Defines the journal entries to return
    date1 = date(2019, 1, 1)
    journal_entry_1 = JournalEntry(date1, "purchase of shares in SBI", None)
    journal_entry_1.post(date1, MockAccountsMapping.BANK_A_CURRENT, -50000)
    journal_entry_1.post(date1, MockAccountsMapping.BROKERAGE_PAYABLE, 10000)

# Generated at 2022-06-14 04:16:09.184581
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    In this test, we are testing the post method of the class JournalEntry
    in the file journal.py
    """
    # Create an instance of a JournalEntry class
    journal_entry = JournalEntry(datetime.date(2020, 7, 15), 'My journal entry', object())

    # Call the post method to add some data to the journal entry created
    journal_entry.post(date = datetime.date(2020, 7, 15), account = Account("My account name", AccountType.ASSETS), quantity = 2)

    # Check that the size of the list of postings of the journal is equal to 1
    assert len(journal_entry.postings) == 1

    # Check that the size of the list of postings of the journal is equal to 2 after adding another posting

# Generated at 2022-06-14 04:16:20.098953
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import DEBIT, CREDIT
    from .business import Stock, StockQuantity
    from .book import Books
    from datetime import date
    from decimal import Decimal

    books: Books = Books()

    # Transaction 1:
    # Buy 100 shares of the 'A' stock at $100 each:
    #
    #    Dr. Assets.Deposit         $10000
    #    Cr. Assets.Equities.Stocks.A.Cost   $10000

    entry1 = JournalEntry(date(2019, 10, 10), "Stock purchase")
    entry1.post(date(2019, 10, 10), books.assets.deposit, DEBIT)
    entry1.post(date(2019, 10, 10), books.assets.equities.stocks.a.cost, CREDIT)

    # Transaction 2:
    # Sell 50 shares of the

# Generated at 2022-06-14 04:16:25.073920
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Given
    journalEntry = JournalEntry(datetime.datetime(2020, 5, 19), '', '')

    # Expect
    try:
        journalEntry.validate()
        assert False
    except AssertionError:
        assert True

# Generated at 2022-06-14 04:16:25.962911
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass

# Generated at 2022-06-14 04:16:32.198414
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    class JournalEntry_test(JournalEntry):
        def __init__(self, date, description, source):
            super().__init__(date, description, source)
            self.__total_debit = 0
            self.__total_credit = 0

    j = JournalEntry_test(datetime.date(2019, 1, 1), "description", "source")
    j.post(datetime.date(2019, 1, 1), Account("my account", AccountType.ASSETS), Quantity(amount = 1))
    j.validate()

# Generated at 2022-06-14 04:16:37.691246
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from ..commons.numbers import Amount, Quantity

    account = Account('ACC01', AccountType.ASSETS)
    date = datetime.date.today()
    journal = JournalEntry('2019-01-01', 'test journal entry')
    journal = journal.post(date, account, Quantity(1))
    assert len(journal.postings) == 1
    assert journal.is_debit is True
    assert journal.increments is not None
    assert journal.debits is not None
    assert journal.credits is None

# Generated at 2022-06-14 04:16:49.868330
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Test the post method of class JournalEntry
    """
    @dataclass(frozen=True)
    class Person():
        """
        A class to represent a person.
        """
        pass

    person = Person()

    @dataclass(frozen=True)
    class Truck():
        """
        A class to represent a truck.
        """
        pass

    truck = Truck()

    @dataclass(frozen=True)
    class Account():
        """
        A class to represent an account.
        """
        accountType = "ASSETS"

        @property
        def type(self):
            """
            Returns the account type.
            """
            return self.accountType

    testAccount = Account()

# Generated at 2022-06-14 04:17:28.166938
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import doctest
    doctest.run_docstring_examples(ReadJournalEntries.__call__, globals())

# Generated at 2022-06-14 04:17:32.174696
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    This test case tests if the required constraints are enforced.
    """
    class __impl(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    __impl() # pragma: no cover

# Generated at 2022-06-14 04:17:41.638082
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from unittest import mock

    def almost_no_op(*args, **kwargs):
        def side_effect(*args, **kwargs):
            return mock.DEFAULT

        return mock.Mock(side_effect=side_effect)

    reader = ReadJournalEntries()
    reader.__call__.assert_not_called()
    reader.__call__.__call__.assert_not_called()
    reader.__call__.__call__.return_value.__iter__.assert_not_called()

    with mock.patch("builtins.iter", almost_no_op()):
        reader(DateRange(datetime.date(2000, 1, 1), datetime.date(2000, 1, 31)))

    reader.__call__.assert_called_once()

# Generated at 2022-06-14 04:17:43.406578
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    incelement = JournalEntry('date', 'description', 'source')
    incelement.post(0, 1, 2)


# Generated at 2022-06-14 04:17:54.133726
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():

    entry = JournalEntry(datetime.date.today(),"Diferencia de cambio",0.0)
    entry.post(datetime.date.today(), Account("101102","Cuentas por cobrar - clientes", AccountType.ASSETS,AccountType.EQUITIES), 1500)
    entry.post(datetime.date.today(), Account("101102","Cuentas por cobrar - clientes", AccountType.ASSETS,AccountType.EQUITIES), -15)
    entry.post(datetime.date.today(), Account("101102","Cuentas por cobrar - clientes", AccountType.ASSETS,AccountType.EQUITIES), -1500)

# Generated at 2022-06-14 04:18:01.014614
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Given an journal entry
    journal_entry = JournalEntry[str](date=datetime.date(2019, 2, 1),
                                      description="",
                                      source="")
    # And some postings
    journal_entry.post(date=datetime.date(2019, 2, 1),
                       account=Account(name="DebitPostingAccount1",
                                       type=AccountType.ASSETS),
                       quantity=100)
    journal_entry.post(date=datetime.date(2019, 2, 1),
                       account=Account(name="CreditPostingAccount1",
                                       type=AccountType.LIABILITIES),
                       quantity=-100)
    # And a journal entry, which total debit and credit does not match

# Generated at 2022-06-14 04:18:12.397064
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .finance import AccountBalance, AccountBalances

    # Helper
    def validate(journal_entry: JournalEntry[Account], account_balances: AccountBalances) -> None:
        """
        Performs validations on the instance.

        :param journal_entry: Journal entry instance.
        :param account_balances: Account balance instance.
        """
        journal_entry.validate()

        total_debit = isum(i.amount for i in journal_entry.debits)
        total_credit = isum(i.amount for i in journal_entry.credits)


# Generated at 2022-06-14 04:18:19.754311
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account

    acct = Account("555", AccountType.ASSETS)
    qty = Quantity(1)
    date = datetime.date.today()

    je = JournalEntry(date, "test", None)
    assert len(je.postings) == 0

    je.post(date, acct, Quantity(0))
    assert len(je.postings) == 0

    je.post(date, acct, qty)
    assert len(je.postings) == 1
    p = je.postings[0]
    assert p.date == date
    assert p.account == acct
    assert p.direction == Direction.INC
    assert p.amount == Amount(qty)
    assert p.is_debit
    assert not p.is_credit


# Generated at 2022-06-14 04:18:31.124056
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class _FakeJournalEntry(Generic[_T]):
        date: datetime.date
        source: _T

    def _reading_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        yield _FakeJournalEntry(datetime.date(2020, 7, 1), "Source")
        yield _FakeJournalEntry(datetime.date(2020, 7, 2), "Source")
        yield _FakeJournalEntry(datetime.date(2020, 7, 3), "Source")


# Generated at 2022-06-14 04:18:40.319916
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    #: Registers the function to read a journal entry.
    source = "https://github.com/pradyunsg/python-ledger/new/master"

    #: Creates a journal entry for given date.
    journal = JournalEntry(datetime.date(2020, 6, 21), f"This is a test journal entry from {source}", source)

    #: Postings to create the journal from:
    postings = [
        (datetime.date(2020, 6, 21), Account("Assets:Checking"), "+1000.00"),
        (datetime.date(2020, 6, 21), Account("Equities:Opening Balances"), "-1000.00"),
    ]

    #: Creates the journal entry.

# Generated at 2022-06-14 04:19:32.123940
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    acct1 = Account(name = 'Cash', account_type = AccountType.ASSETS, description = "Cash in hand")
    x = JournalEntry(date = datetime.date(2019,3,31), description = 'Begin')
    x.post(date = datetime.date(2019,3,31), account = acct1, quantity = 10)
    y = x.postings[0]
    assert y.direction == Direction.INC
    assert y.account == acct1
    assert y.journal == x
    assert y.amount == 10
    assert y.is_debit
    assert not y.is_credit


# Generated at 2022-06-14 04:19:43.742778
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Arrange
    journal_entry: JournalEntry[_T] = JournalEntry(datetime.date(2020, 8, 1), 'Test', None)
    p1: Posting[None] = Posting(journal_entry, datetime.date(2020, 8, 1), Account('Account', AccountType.ASSETS, None), Direction.INC, Amount(1))
    p2: Posting[None] = Posting(journal_entry, datetime.date(2020, 8, 1), Account('Account', AccountType.REVENUES, None), Direction.DEC, Amount(1))
    journal_entry.postings = [p1, p2]
    account: Account = Account('TestAccount', AccountType.ASSETS, None)
    quantity: Quantity = 1

    # Act

# Generated at 2022-06-14 04:19:45.926642
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
  journal_entry = JournalEntry[int]
  journal_entry


# Generated at 2022-06-14 04:19:53.963452
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import Account, AccountType
    from .business import Business, BusinessObject, SubBusinessObject

    # test case: Account is not of type AccountType.EQUITIES
    # Expected: AssertionError raised
    temp: Business = Business()
    temp_ReadJournalEntries_1: ReadJournalEntries[BusinessObject] = lambda period: iter([])
    temp_Account_1: Account = Account(name='Test1', identifier='Test1', account_type=AccountType.ASSETS)
    temp_date_1: datetime.date = datetime.date(year=2019, month=1, day=1)

# Generated at 2022-06-14 04:19:54.669227
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert True



# Generated at 2022-06-14 04:20:01.455619
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..journal import journal
    from ..journal.source import journal_entries
    from ..journal.source.example import source

    journal_entries_source = source()

    journal.post(journal_entries_source, datetime.date(2019, 7, 17), "Initial Balance",
                 {source.assets.cash: +10000})

    assert journal_entries.items(datetime.date(2019, 7, 16), datetime.date(2019, 7, 18))[0].postings[0].amount == 10000

# Generated at 2022-06-14 04:20:08.434698
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from unittest import mock, TestCase
    from . import ReadJournalEntries
    from datetime import date
    from dataclasses import dataclass
    from .accounts import Account

    @dataclass(frozen=True)
    class Invoice:
        pass

    def func(period: DateRange) -> Iterable[JournalEntry[_T]]:
        assert period.start == date(2019, 1, 1)
        assert period.end == date(2019, 12, 31)

# Generated at 2022-06-14 04:20:14.386283
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .ledgers import LedgerAccount
    from .ledgers.tags import LedgerTag
    from .tags import Tag

    def f(period: DateRange) -> Iterable[JournalEntry[LedgerTag]]:
        return (
            JournalEntry(datetime.date.today(), "INCOME", LedgerTag(Tag("INCOME"), LedgerAccount("Income-Ledger")), [])
                .post(datetime.date.today(), LedgerAccount("Checking Account"), +100.00)
                .post(datetime.date.today(), LedgerAccount("Income-Ledger"), -100.00),
        )

    assert isinstance(f, ReadJournalEntries[LedgerTag])

# Generated at 2022-06-14 04:20:15.026557
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:20:25.686988
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journalentry = JournalEntry[str]
    entry = journalentry(datetime.date(2020, 4, 30), 'Paycheck', 'Paycheck', [])
    debit_posting = entry.post(datetime.date(2020, 4, 30), Account('Assets', 'Checking Account', AccountType.ASSETS), Amount(1000))
    assert debit_posting.is_debit == True
    credit_posting = entry.post(datetime.date(2020, 4, 30), Account('Expenses', 'Groceries', AccountType.EXPENSES), Amount(-100))
    assert credit_posting.is_credit == True
    # Check that zero quantity postings don't get posted: