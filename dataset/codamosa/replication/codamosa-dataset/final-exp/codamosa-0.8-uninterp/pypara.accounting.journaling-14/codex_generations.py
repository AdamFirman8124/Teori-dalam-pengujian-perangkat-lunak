

# Generated at 2022-06-14 04:11:30.346806
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..accounting.accounts import Account, AccountType
    from .transactions import Transaction

    expense = Account(AccountType.EXPENSES, "Test Expense")
    invoice = Transaction(datetime.date.today(), "Test Invoice", "INV-000-000-0001")
    invoice.post(expense, 100)

    print(invoice.postings)

# Generated at 2022-06-14 04:11:41.496884
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from .accounts import AccountType
    from .accounts import Account, Amount, Quantity
    from .ledgers import Ledger

    ledger = Ledger.create("Test")

    def import_journal(ledger: Ledger, date: date, description: str, source_type: str, account_code: str,
                       amount: Amount, direction: Direction = None) -> None:
        journal = ledger.journal() \
            .post(date, ledger.account(account_code), amount if direction is None else (direction.value * amount))
        journal.description = description
        journal.source = source_type
        ledger.transact(journal)


# Generated at 2022-06-14 04:11:51.849616
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    _JournalEntry_post: JournalEntry = JournalEntry(datetime.date(2010, 1, 1), "Test", None)
    assert _JournalEntry_post.postings == []
    assert _JournalEntry_post.post(datetime.date(2010, 1, 1), Account("1000", "Test", {}, AccountType.ASSETS), Quantity(10)) == _JournalEntry_post
    assert _JournalEntry_post.postings == [Posting(_JournalEntry_post, datetime.date(2010, 1, 1), Account("1000", "Test", {}, AccountType.ASSETS), Direction.INC, Amount(10))]
    assert _JournalEntry_post.post(datetime.date(2010, 1, 1), Account("1000", "Test", {}, AccountType.ASSETS), Quantity.zero()) == _JournalEntry_post
    assert _JournalEntry_

# Generated at 2022-06-14 04:11:53.700831
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    #: @todo: Implement unit test for method __call__ of class ReadJournalEntries
    pass

# Generated at 2022-06-14 04:12:04.423191
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType, Account
    from .businessobjects import Customer
    from .journalentries import JournalEntry

    dummycustomer = Customer(id=1, name="Dummy Customer")
    dummyaccount = Account(id=1, name="Dummy", type=AccountType.ASSETS)

    je = JournalEntry[Customer](date=datetime.date(year=2020, month=1, day=1), source=dummycustomer, description="TEST")
    je.post(date=datetime.date(year=2020, month=1, day=1), account=dummyaccount, quantity=100).validate()
    je = JournalEntry[Customer](date=datetime.date(year=2020, month=1, day=1), source=dummycustomer, description="TEST")

# Generated at 2022-06-14 04:12:12.200083
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType, ASSET, EQUITY, LIABILITY, EXPENSE, REVENUE

    asset = ASSET
    equity = EQUITY
    liability = LIABILITY
    expense = EXPENSE
    revenue = REVENUE

    ## Test for debit/credit mismatch
    _ = JournalEntry[str](datetime.date(2020, 1, 1), "Journal Entry", "source")\
        .post(datetime.date(2020, 1, 1), asset, 100)\
        .post(datetime.date(2020, 1, 1), equity, -100)\
        .post(datetime.date(2020, 1, 1), liability, 100)\
        .post(datetime.date(2020, 1, 1), expense, -100)\
        .post(datetime.date(2020, 1, 1), revenue, 100)\
        .validate

# Generated at 2022-06-14 04:12:14.313698
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Test case for method post of class JournalEntry.
    """
    pass

# Generated at 2022-06-14 04:12:24.837394
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    a1 = Account("Assets", AccountType.ASSETS)
    e1 = Account("Equities", AccountType.EQUITIES)
    l1 = Account("Liabilities", AccountType.LIABILITIES)
    ri1 = Account("Revenues", AccountType.REVENUES)
    ex1 = Account("Expenses", AccountType.EXPENSES)

    j1 = JournalEntry("2019-08-19", "Test journal entry.", Business())
    j1.post("2019-08-19", a1, 100)
    j1.post("2019-08-19", e1, -100)
    j1.post("2019-08-19", l1, -100)
    j1.post("2019-08-19", ex1, -100)

    assert j1.postings[0].direction == Direction.INC
   

# Generated at 2022-06-14 04:12:28.585476
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from dataclasses import dataclass
    from typing import List

    @dataclass(frozen=True)
    class _BusinessObject:
        pass

    @dataclass(frozen=True)
    class _Journal:
        entries: List[JournalEntry[_BusinessObject]]

    _journal = _Journal.__new__(_Journal)
    _journal.__init__(
        entries=[
            JournalEntry(
                date=datetime.date(2019, 9, 11),
                description="Test journal entry",
                source=_BusinessObject(),
            )
        ]
    )

    _journal_reader: ReadJournalEntries[_BusinessObject] = lambda period: _journal.entries

    assert _journal_reader(DateRange(datetime.date.today(), datetime.date.today())) == _journal.entries
    assert _

# Generated at 2022-06-14 04:12:36.020991
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Setup
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[str]]:
        # Setup
        def post_to(account: Account, quantity: Quantity) -> JournalEntry[str]:
            """
            Returns a journal entry having posted the quantity to the given account.
            """
            return JournalEntry("", datetime.date.today(), "").post(datetime.date.today(), account, quantity)

        # Test
        # Given:
        # * Account: Assets:Cash
        # * Period range is D<1>
        # * There is a Journal entry posted on D<1>-1

        # Assert:
        # * The period range has no effect on the filtering.
        return [post_to(Account.from_string("Assets:Cash"), 10)]

    # Exercise
    result = read

# Generated at 2022-06-14 04:12:51.302491
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    ## 1 Prepare the context
    je = JournalEntry(
        date=datetime.date(2019, 12, 1),
        description="Journal entry",
        source="the source",
    )

    ## 2 Execute the method
    je.post(datetime.date(2019, 12, 1), Account(code="100", description="Cash"), +100)
    je.post(datetime.date(2019, 12, 1), Account(code="200", description="Credit card"), -100)

    ## 3 Assert the result
    assert list(je.increments) == [
        Posting(
            journal=je,
            date=datetime.date(2019, 12, 1),
            account=Account(code="100", description="Cash"),
            direction=Direction.INC,
            amount=Amount(+100),
        )
    ]


# Generated at 2022-06-14 04:12:53.233201
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    obj1 = JournalEntry()
    obj1.post(date, account, quantity)

# Generated at 2022-06-14 04:13:06.229437
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class TestJournalEntry(JournalEntry[None]):
        def __init__(self, date, source):
            super().__init__(date, "", source)

    def test_ReadJournalEntries(period: DateRange) -> Iterable[TestJournalEntry]:
        entry1 = TestJournalEntry(period.start, None)
        entry1.postings.append(
            Posting(entry1, entry1.date, Account("A", AccountType.REVENUES), Direction.INC, Amount(1))
        )
        entry1.postings.append(
            Posting(entry1, entry1.date, Account("B", AccountType.EXPENSES), Direction.DEC, Amount(1))
        )

        entry2 = TestJournalEntry(period.end, None)

# Generated at 2022-06-14 04:13:16.364786
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    a = JournalEntry[object]
    b = Posting[object]
    c = Account("Forex", "Cash")
    d = Account("Bank", "Cash")
    e = JournalEntry[object](datetime.date(2019,10,24), "Sample Journal Entry", "Sample Source")
    f = JournalEntry[object](datetime.date(2019,10,25), "Sample Journal Entry 1", "Sample Source 1")
    g = JournalEntry[object](datetime.date(2019,10,26), "Sample Journal Entry 2", "Sample Source 2")
    h = JournalEntry[object](datetime.date(2019,10,27), "Sample Journal Entry 3", "Sample Source 3")
    i = JournalEntry[object](datetime.date(2019,10,28), "Sample Journal Entry 4", "Sample Source 4")
    

# Generated at 2022-06-14 04:13:23.761009
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    with pytest.raises(AssertionError):
        JournalEntry.JournalEntry(date=datetime.date.today(), description="Income statement", source=None)\
            .post(date=datetime.date.today(), account="Revenues", quantity=100)\
            .post(date=datetime.date.today(), account="Expenses", quantity=100)\
            .validate()


# Generated at 2022-06-14 04:13:29.438969
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from .accounts import Account
    from .books import Book
    from .ledgers import Ledger

    book = Book(name='test', ledger=Ledger())

    # Create journal entry
    je = JournalEntry[Book](date.today(), 'test', book)

    # Create two accounts
    a1 = Account.create(book, 'a1', AccountType.EXPENSES, 'test')
    a2 = Account.create(book, 'a2', AccountType.EQUITIES, 'test')

    # Add two postings
    je.post(date(2020,8,16), a1, 1000).post(date(2020,8,16), a2, 1000)

    # Validate the journal entry
    je.validate()

    # Create another account

# Generated at 2022-06-14 04:13:40.505962
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    je = JournalEntry[int]()
    je.post(datetime.date.today(), Account("Assets", AccountType.ASSETS), +100.0)
    assert len(je.postings) == 1
    assert je.postings[0].amount == 100.0
    assert je.postings[0].direction == Direction.INC
    assert je.postings[0].is_debit
    assert not je.postings[0].is_credit
    je.post(datetime.date.today(), Account("Liabilities", AccountType.LIABILITIES), -100.0)
    assert len(je.postings) == 2
    assert je.postings[1].amount == 100.0
    assert je.postings[1].direction == Direction.DEC

# Generated at 2022-06-14 04:13:51.912849
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Test class JournalEntry to validate method for validating the instance.
    """

    #:Provides class JournalEntry.
    from . import accounts, journals

    #: Tests class Ledger which implements journals.ReadJournalEntries
    from .ledger import Ledger

    #: Provides class BusinessObject
    from .objects import BusinessObject

    #: Test JournalEntry for validation of period
    def test_validate():
        #: Test case for valid journal entry
        def test_valid():
            journal = JournalEntry[BusinessObject]()
            journal.date = datetime.datetime(2020,5,5)
            journal.description = 'valid entry'
            journal.source = BusinessObject("valid object")
            journal.postings.append(Posting(journal, journal.date, accounts.Account("cash"), Direction.INC, Amount(100)))


# Generated at 2022-06-14 04:13:54.229585
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class _MockSource:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

# Generated at 2022-06-14 04:13:54.890984
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:14:11.632487
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    import pytest

    def test_post_journal():
        from ddd_ledger.application.journal.accounts import Assets

        journal = JournalEntry[str]()

        journal.post(datetime.date(2019, 10, 1), Assets, 100).source = "test1"
        journal.post(datetime.date(2019, 10, 1), Assets, -50).source = "test2"

        assert journal.postings == [
            Posting(journal, datetime.date(2019, 10, 1), Assets, Direction.INC, 100),
            Posting(journal, datetime.date(2019, 10, 1), Assets, Direction.DEC, 50),
        ]

    def test_post_journal_with_zero_value():
        from ddd_ledger.application.journal.accounts import Assets


# Generated at 2022-06-14 04:14:14.006498
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert ReadJournalEntries(lambda period: period)


# Generated at 2022-06-14 04:14:22.408016
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    an_account = Account("An account")
    a_journal_entry = JournalEntry(
        date=datetime.date(2020, 1, 1),
        description="Some description",
        source=None,
    )
    a_journal_entry.post(date=datetime.date(2020, 1, 1), account=an_account, quantity=Quantity(100))
    a_journal_entry.post(date=datetime.date(2020, 1, 1), account=an_account, quantity=Quantity(-100))
    a_journal_entry.validate()

# Generated at 2022-06-14 04:14:33.068707
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Create a journal entry and write it to a ledger.
    journal = JournalEntry[None](
        date=datetime.date(2018, 9, 2),
        description="Shopping",
        source=None,
    )
    journal.post(date=journal.date, account=Account(name="Cash", type=AccountType.ASSETS), quantity=Quantity(-25))
    journal.post(date=journal.date, account=Account(name="Groceries", type=AccountType.EXPENSES), quantity=Quantity(+25))
    try:
        journal.validate()
        print("Passed.")
    except AssertionError:
        print("Failed.")
test_JournalEntry_validate()

# Generated at 2022-06-14 04:14:38.437573
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from financeager.commons.zeitgeist import DateTime
    from financeager.model.business import Payment
    from financeager.model.accounts import Account, AccountType

    # Create journal entry
    payment = Payment(DateTime.today(), DateTime.today(), "N26", "Test Payment", Amount.from_int(100))
    je = JournalEntry(
                        DateTime.today(),
                        "Test Journal Entry",
                        payment
                      )

    # Journal entry should have no postings at start
    assert len(je.postings) == 0

    # Post an increment event with amount 100 to an account
    je.post(DateTime.today(), Account("Test Account"), Quantity(100))
    assert len(je.postings) > 0

    # Post a decrement event with amount 100 to the same account

# Generated at 2022-06-14 04:14:45.057486
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def rjeFunc(period):
        return [(JournalEntry[int](datetime.date(2020, 1, 1), "", 123),)]
    from typing import Callable
    rje: Callable[[DateRange], Iterable[JournalEntry[int]]] = rjeFunc
    assert rje(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 1)))[0].date == datetime.date(2020, 1, 1)

# Generated at 2022-06-14 04:14:57.159786
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    a1 = Account(
        name="Manufacturing Overhead",
        type=AccountType.EXPENSES
    )
    a2 = Account(
        name="Cash",
        type=AccountType.ASSETS
    )
    journal = JournalEntry(
        date=datetime.date(2020, 1, 1),
        description="Payment for employee salary and utilities",
    )
    journal = journal.post(datetime.date(2020, 1, 1), a1, -1)
    journal = journal.post(datetime.date(2020, 1, 1), a2, +1)
    assert journal.postings[0].direction==Direction.DEC and journal.postings[1].direction==Direction.INC
    assert journal.postings[0].account == a1 and journal.postings[1].account == a2

# Generated at 2022-06-14 04:15:01.232294
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal = JournalEntry[object]("12/12/2020", "Test Journal Entry Posting", "Test Journal Entry News")
    journal.post("12/12/2020", "Test Journal Entry Account1", +100)
    journal.post("12/12/2020", "Test Journal Entry Account2", -100)

# Generated at 2022-06-14 04:15:12.035090
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    class JournalEntryTest(JournalEntry):
        pass

    from datetime import date
    from .accounts import Account, AccountType

    A = Account("A", AccountType.ASSETS)
    B = Account("B", AccountType.ASSETS)
    C = Account("C", AccountType.EQUITIES)
    D = Account("D", AccountType.EQUITIES)
    E = Account("E", AccountType.REVENUES)

    je = JournalEntryTest(date.today(), "", None)
    je.post(date.today(), A, 100)
    je.post(date.today(), B, -10)
    je.post(date.today(), C, 50)

    je.post(date.today(), D, -50)
    je.post(date.today(), E, -40)
    je.validate()

# Generated at 2022-06-14 04:15:19.339967
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..commons.money import USD
    from ..commons.zeitgeist import Date
    from .accounts import account

    j = JournalEntry(Date(2019, 12, 1), "Test", None)
    a = account("A", AccountType.ASSETS)
    j.post(Date(2019, 12, 1), a, USD(100))
    assert j.postings[0].amount == USD(100)



# Generated at 2022-06-14 04:15:42.296707
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    posting1 = Posting('a', datetime.date(2020,2,3), 'BS', Direction.INC, 1000)
    posting2 = Posting('b', datetime.date(2020,2,3), 'BS', Direction.INC, 2000)
    posting3 = Posting('c', datetime.date(2020,2,3), 'BS', Direction.DEC, 3000)

    journal_entry1 = JournalEntry(datetime.date(2020,2,3), 'journal entry 1', 'business source 1')
    journal_entry1.post(datetime.date(2020,2,3), 'BS', 1000)
    journal_entry1.post(datetime.date(2020,2,3), 'BS', 2000)
    journal_entry1.post(datetime.date(2020,2,3), 'BS', -3000)


# Generated at 2022-06-14 04:15:43.106114
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert False

# Generated at 2022-06-14 04:15:53.132779
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from unittest.mock import call, patch

    # Setup:
    class ReadJournalEntriesProxy:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry]:
            return mock_call.__call__(period)
    mock_result = (1, 2, 3)
    mock_call = patch.object(ReadJournalEntries, "__call__", wraps=ReadJournalEntriesProxy(), return_value = mock_result).start()

    # Exercise:
    result = ReadJournalEntries.__call__(ReadJournalEntriesProxy(), "PERIOD")

    # Verify:
    mock_call.assert_called_once_with("PERIOD")
    assert result == mock_result

    # Cleanup:
    patch.stopall()

# Generated at 2022-06-14 04:16:04.432667
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Tests method validate of class JournalEntry
    """
    from datetime import date, timedelta
    from ledger.accounts import Cash, Income, Expenses
    from ledger.categories import Category, Vehicle
    from ledger.commitments import Transaction

    mydate = date.today()
    six_months: timedelta = timedelta(180,0)
    my_period: DateRange = DateRange(mydate, mydate + six_months)

    # Create a journal entry with two postings:
    journal = JournalEntry[Transaction](
        date=mydate,
        description="Test journal",
        source=Transaction(Vehicle(), Cash(), Expenses(), Category(), "Gasoline purchase", mydate, mydate, 1)
    )

    journal.post(mydate, Cash(), -1)
    journal.post(mydate, Vehicle(), 1)


# Generated at 2022-06-14 04:16:09.470782
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    test_postings = [
        Posting(None, datetime.date.today(), Account("A", AccountType.ASSETS), Direction.INC, Amount(100)),
        Posting(None, datetime.date.today(), Account("A", AccountType.REVENUES), Direction.INC, Amount(100)),
    ]
    test_entry = JournalEntry(datetime.date.today(), "description", None, test_postings)
    test_entry.validate()

# Generated at 2022-06-14 04:16:20.310888
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from typing import Callable
    import unittest

    from ..commons.zeitgeist import DateRange

    def factory() -> Callable[[DateRange], Iterable[JournalEntry[str]]]:
        def func(period: DateRange) -> Iterable[JournalEntry[str]]:
            return list()

        return func

    ReadJournalEntries.register(factory)


# Generated at 2022-06-14 04:16:24.382816
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    #
    def target(period: DateRange) -> Iterable[JournalEntry[int]]:
        return ()
    #
    r: ReadJournalEntries[int]
    r = target

# Generated at 2022-06-14 04:16:25.429449
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert callable(ReadJournalEntries.__call__)

# Generated at 2022-06-14 04:16:32.271900
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j1 = JournalEntry(date=datetime.date.today(),
                      description="hello",
                      source=None)
    assert j1.postings == []

    r1 = j1.post(date=datetime.date.today(), account=Account("EXPENSES", AccountType.EXPENSES), quantity=Quantity(20))

    r2 = j1.post(date=datetime.date.today(), account=Account("REVENUE", AccountType.REVENUES), quantity=Quantity(20))

    r3 = j1.validate()
    assert r3 is None

# Generated at 2022-06-14 04:16:38.552314
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date

    j1 = JournalEntry(date.fromisoformat('2021-12-25'), 'TEST', None)

    j1.post(datetime.datetime.fromisoformat('2021-12-24'), 'My Savings Account', +100.00)
    j1.post(datetime.datetime.fromisoformat('2021-12-24'), 'My Savings Account', -100.00)

    print('debit postings =', [p.amount for p in j1.debits])
    print('credit postings =', [p.amount for p in j1.credits])

    assert len(j1.debits) == 1
    assert len(j1.credits) == 1
    
test_JournalEntry_post()

# Generated at 2022-06-14 04:17:18.079007
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .source import Source
    from .accounts import Account, AccountType

    # Create a source
    source = Source("121", "Purchase a laptop")

    # Create a journal entry
    journal_entry = JournalEntry(
        date=datetime.date(2018, 5, 1), description="Purchase a laptop", source=source
    )

    # Post the transaction by calling method post
    journal_entry.post(datetime.date(2018, 5, 1), Account("101", AccountType.ASSETS), -10000)

    # Validate the journal entry
    journal_entry.validate()

    assert journal_entry.postings[0].date == datetime.date(2018, 5, 1)
    assert journal_entry.postings[0].account.code == "101"
    assert journal_entry.postings[0].direction == Direction.DEC

# Generated at 2022-06-14 04:17:28.349546
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import create_accounts

    # Load accounts:
    accounts = create_accounts()

    # Define utility functions:
    def get_total_debit(entry: JournalEntry) -> Amount:
        return isum(i.amount for i in entry.debits)

    def get_total_credit(entry: JournalEntry) -> Amount:
        return isum(i.amount for i in entry.credits)

    # Define sample date:
    date = datetime.date(2018, 1, 1)

    # No posting entry:
    entry = JournalEntry(date, "", None)
    entry.validate()
    assert get_total_debit(entry) == 0
    assert get_total_credit(entry) == 0

    # Incorrect entry:
    entry = JournalEntry(date, "", None)

# Generated at 2022-06-14 04:17:38.678188
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import datetime
    from e1 import AccountType, Account, Direction
    from e1.Amount import Amount
    from e1.Quantity import Quantity
    from e1.journal.JournalEntry import JournalEntry
    from e1.journal.Posting import Posting

    _T = object
    # Create Journal Entry
    journal = JournalEntry(_T, datetime.date(2020,3,24),"Opening Balance", _T)
    # Post to the journal
    journal.post(datetime.date(2020,3,24), Account("Equity",AccountType.EQUITIES), Quantity(100, "USD"))
    journal.post(datetime.date(2020,3,24), Account("Cash",AccountType.ASSETS), Quantity(100, "USD"))

    # Assert if the postings are created properly

# Generated at 2022-06-14 04:17:39.735364
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert list(ReadJournalEntries.__call__.__annotations__) ==['return']


# Generated at 2022-06-14 04:17:42.247364
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    period = DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 2))
    assert list(ReadJournalEntries.__call__(lambda period: [], period)) == []

# Generated at 2022-06-14 04:17:52.841324
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from ..books import Stock, StockBook
    from ..books.stocks import StockTransaction
    from ..commons import Money
    from .accounts import Account, AccountType
    from .accounts.securities import SecuritiesAccount
    from .accounts.stocks import StockAccount

    ## Accounts:
    stock_investments = StockAccount("Stock Investments", "10", "100")

    ## Stock book:
    stock_book = StockBook()
    stock_book.post(StockTransaction(Stock("MGL", "Mahanagar Gas Limited"), 100, Money(1000), Money(10), Money(1000)))

    ## Sub-ledger accounts:
    sub = SecuritiesAccount(stock_account=stock_investments)
    sub.post(stock_book.entries)

    ## journal entry:
    j = JournalEntry[StockTransaction]()
    j.date = dat

# Generated at 2022-06-14 04:18:00.301125
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..accounts.accounts import EquityAccount, ExpenseAccount, AssetAccount, RevenueAccount

    journal_entry = JournalEntry[None]('2020-01-01', 'Journal Description', None)

    asset_account = AssetAccount('Test Asset Account', Guid('5b5606e0-2df0-4d4b-b733-73f7a0d8067d'))
    equity_account = EquityAccount('Test Equity Account', Guid('7f2aa1a0-7db3-49a6-b2c1-3b3f3f93e9d1'))
    expense_account = ExpenseAccount('Test Expense Account', Guid('a76a6f1f-03e0-4431-9bce-01c78db2e6d2'))

# Generated at 2022-06-14 04:18:00.836067
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass

# Generated at 2022-06-14 04:18:11.860992
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # pylint: disable=E1101,C0116,W0612
    # E1101: Module 'abc' has no 'ABC' member
    # C0116: Missing function or method docstring
    # W0612: Unused variable 'period'
    from dataclasses import dataclass
    from typing import ClassVar, Iterable, TypeVar
    from .accounts import Account, AccountType
    _T = TypeVar("_T")
    @dataclass(frozen=True)
    class Source(Generic[_T]):
        _source: ClassVar[ReadJournalEntries[_T]]
        # pylint: disable=E0602
        # E0602: Undefined variable '__annotations__'
        def __getattr__(self, name): return type(self)._source

# Generated at 2022-06-14 04:18:19.354413
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Given
    journal_entry = JournalEntry[str]('2019-02-01', 'Event', 'Source')

    # When
    journal_entry.post(date='2019-01-01', account=Account(guid='1', name='A1', type=AccountType.ASSETS), quantity=10)
    journal_entry.post(date='2019-01-01', account=Account(guid='2', name='A2', type=AccountType.ASSETS), quantity=-10)

    # Then
    posting_list = journal_entry.postings
    assert len(posting_list) == 2

    posting = posting_list[0]
    assert posting.journal == journal_entry
    assert posting.date == datetime.date(2019, 1, 1)

# Generated at 2022-06-14 04:19:34.257907
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:19:44.435079
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import abc
    from ..commons.zeitgeist import DateRanges

    ## Define a mock abstract base class:
    @dataclass(frozen=True)
    class _MockJournalEntries(abc.ABC):
        @abc.abstractmethod
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

    ## This should not recompile:
    _MockJournalEntries()

    ## Define a mock class applying protocol ReadJournalEntries:
    class _MockJournalEntries2(_MockJournalEntries):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            ...

    ## This should recompile to provide a specialized __call__ member:
    _MockJournalEntries2()

    ## Define a

# Generated at 2022-06-14 04:19:53.647814
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Create a "dummy" source for posting:
    @dataclass(frozen=True)
    class Source:
        pass
    
    # Create a journal entry:
    source = Source()
    journal_entry = JournalEntry[Source](datetime.date(2020, 1, 1), "test", source)
    
    # Post transaction to the journal entry:
    journal_entry.post(datetime.date(2020, 1, 1), Account.ASSETS.BANK_ACCOUNTS.CHECKING, 100)
    journal_entry.post(datetime.date(2020, 1, 1), Account.EXPENSES.FOOD, -50)
    journal_entry.post(datetime.date(2020, 1, 1), Account.EXPENSES.SHOPPING_MISC, -50)

    # Validate the journal entry:

# Generated at 2022-06-14 04:20:03.635703
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from typing import Callable
    import dataclasses
    import datetime

    from .accounts import ledger as accounts
    from .commons import numbers as nums
    from .commons import zeitgeist

    # Define a dummy value object for testing journal entries
    @dataclasses.dataclass(frozen=True)
    class DummyVO:
        pass

    # Define a dummy journal entry reader:
    def dummy_reader() -> Iterable[JournalEntry[DummyVO]]:
        for i in range(3):
            je = JournalEntry(datetime.date.today(), f"Dummy entry #{i}", DummyVO())
            je.post(datetime.date.today(), accounts.cash, nums.Amount(10 * i))

# Generated at 2022-06-14 04:20:10.081505
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    @dataclass(frozen=True)
    class T:
        pass

    je = JournalEntry[T](datetime.date(2020, 1, 1), "Test", T())
    je.post(datetime.date(2020, 1, 1), Account("EXPENSES", AccountType.EXPENSES), -100)
    je.post(datetime.date(2020, 1, 1), Account("REVENUES", AccountType.REVENUES), 100)

    je.validate()

# Generated at 2022-06-14 04:20:13.415768
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Arrange
    t = JournalEntry()
    
    # Act
    t.post(datetime.date.today(), Account("1010"), Quantity(100)) # Debit
    t.post(datetime.date.today(), Account("3020"), Quantity(-100))  # Credit
    
    # Assert
    t.validate()

# Generated at 2022-06-14 04:20:21.903334
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from .accounts import Account, AccountType

    a = Account(1, AccountType.ASSETS, "Cash")
    b = Account(2, AccountType.LIABILITIES, "John")
    j = JournalEntry(date(2018,12,30), "Transfer Cash to John", source = None)
    j.post(date(2018,12,30), a, -100)
    j.post(date(2018,12,30), b, 100)
    j.validate()

    assert(tuple(j.increments)[0].account == b)
    assert(tuple(j.decrements)[0].account == a)

# Generated at 2022-06-14 04:20:30.791425
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from datetime import date

    @dataclass
    class Source:
        pass

    account_debit = Account(AccountType.ASSETS, "Account Debit")
    account_credit = Account(AccountType.EXPENSES, "Account Credit")

    journal = JournalEntry(date(2020,5,5), "Test posting", Source())
    journal.post(date(2020,5,5), account_debit, 50)
    journal.post(date(2020,5,5), account_credit, 50)

    journal.post(date(2020,5,5), account_debit, 60)
    journal.post(date(2020,5,5), account_credit, 60)
    journal.post(date(2020,5,5), account_debit, 70)
    journal.post

# Generated at 2022-06-14 04:20:39.272800
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from dataclasses import dataclass

    @dataclass
    class Mock(object):
        guid: str

    journal_entry1 = JournalEntry[Mock](
        date=datetime.date(2020, 3, 24),
        description='',
        source=Mock(guid='x'),
    )

    journal_entry2 = journal_entry1.post(
        date=datetime.date(2020, 3, 24),
        account=Account('Assets:Cash', 'Cash', AccountType.ASSETS),
        quantity=Quantity(1000)
    )

    assert int(journal_entry2.postings[0].amount) == 1000

# Generated at 2022-06-14 04:20:44.388700
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    journal = JournalEntry(datetime.date.today(), "Test Journal", "Test Object")
    journal.post(datetime.date.today(), "Test Account", 1)
    journal.post(datetime.date.today(), "Test Account", -1)
    journal.validate()