

# Generated at 2022-06-14 04:11:24.647604
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():

	import datetime
	from machinist import Blueprint, construct
	from machinist.accounting import AccountBlueprint

	# Make blueprints
	journal_blueprint = Blueprint[JournalEntry[None]](
		lambda b: JournalEntry(
			date=b.date,
			description=b.description,
			source=None
		)
	)	

	# Create instance of account blueprint
	account = construct(AccountBlueprint)		

	# Create an instance of journal entry
	journal = journal_blueprint.construct()

	# Create instance of account blueprint
	account = construct(AccountBlueprint)		

	## Check:
	journal.post(datetime.date(2020, 9, 5), account, 1)
	assert len(journal.postings)

# Generated at 2022-06-14 04:11:36.627562
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account

    je = JournalEntry("2020-01-02", "Test description")

    a1 = Account("Assets")
    a2 = Account("Assets")
    a3 = Account("Revenues")
    a4 = Account("Expenses")

    je.post("2020-01-02", a1, +1000)
    je.post("2020-01-02", a2, -1000)
    je.post("2020-01-02", a3, -1000)
    je.post("2020-01-02", a4, +1000)

    ## Get total debit and credit amounts:
    total_debit = isum(i.amount for i in je.debits)
    total_credit = isum(i.amount for i in je.credits)


# Generated at 2022-06-14 04:11:39.831835
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Setup:
    class T:
        ...

    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[T]]:
        ...

    # Exercise:
    assert read_journal_entries

# Generated at 2022-06-14 04:11:47.051363
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Test method post of class JournalEntry
    """
    origin = JournalEntry(datetime.date(2018, 1, 1), "", "origin")
    acc = Account(AccountType.ASSETS, "")
    origin.post(datetime.date(2018, 1, 1), acc, Quantity(100))
    origin.post(datetime.date(2018, 1, 2), acc, Quantity(-50))
    origin.post(datetime.date(2018, 1, 3), acc, Quantity(-25))
    origin.post(datetime.date(2018, 1, 4), acc, Quantity(-25))
    print(origin.increments)
    print(origin.debits)

# Generated at 2022-06-14 04:11:57.176582
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .business import Business
    from .businesses import Businesses
    from .accountants import Accountant
    from .services import Services
    from .tasks import Task
    from .tasks import TaskType
    from .workers import Workers
    from dataclasses import field
    from dataclasses import make_dataclass
    from datetime import date
    from .worklogs import Worklog

    from datetime import datetime
    from datetime import timedelta

    # CREATE DUMMY BUSINESS


# Generated at 2022-06-14 04:12:04.561957
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    je1 = JournalEntry[int](datetime.date.today(), "test description", 1)
    je1.post(datetime.date.today(), Account("asset", AccountType.ASSETS), 1)
    je1.post(datetime.date.today(), Account("expense", AccountType.EXPENSES), -1)
    je1.validate()

    # assert throws Assertion Error
    with pytest.raises(AssertionError):
        je2 = JournalEntry[int](datetime.date.today(), "test description", 2)
        je2.post(datetime.date.today(), Account("asset", AccountType.ASSETS), 1)
        je2.validate()

# Generated at 2022-06-14 04:12:12.272372
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import AccountType
    from .units import Unit
    from .sources import InventorySource

    def make_postings() -> List[Posting[InventorySource]]:
        return [
        Posting(journal, datetime.date.today(), Account(AccountType.EQUITIES, "Equity"), Direction.INC, Amount(500)),
        Posting(journal, datetime.date.today(), Account(AccountType.REVENUES, "Revenue"), Direction.DEC, Amount(500)),
        ]

    source = InventorySource(Unit(Unit.Type.PIECE), "Foo", "Bar", 1)
    journal = JournalEntry(datetime.date.today(), "Foo", source, postings=make_postings())

    journal.validate()

    # Test for unequal debits and credits
    journal.postings = make_

# Generated at 2022-06-14 04:12:17.453595
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..odk.persistence import MockODK
    from ..odk.read import read_odk
    from .accounts import Account

    ## Setup:
    mock = MockODK()
    read = read_odk(mock)
    mock.add_account(Account("Bank"))
    mock.add_account(Account("Expenses"))

    ## Create and register a journal entry:
    journal_entry = JournalEntry(datetime.date(2020, 1, 1), "Some description", None)
    journal_entry.post(journal_entry.date, mock["Bank"], +1000)
    journal_entry.post(journal_entry.date, mock["Expenses"], -1000)
    mock.add_journal_entry(journal_entry)

    ## Test:

# Generated at 2022-06-14 04:12:18.479574
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert False


# Generated at 2022-06-14 04:12:24.831634
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account
    
    asset_account=Account.ASSETS.create_account(name='cash',code='01')
    entry=JournalEntry.create(date=datetime.date.today())
    entry.post(date=datetime.date.today(), account=asset_account, quantity=+100)
    entry.post(date=datetime.date.today(), account=asset_account, quantity=-100)
    entry.validate()



# Generated at 2022-06-14 04:12:33.746689
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from tests.persistence.fakesource import FakeSource

    source = FakeSource()

    def read_fn(period: DateRange) -> Iterable[JournalEntry[FakeSource]]:
        yield JournalEntry[FakeSource](date=period.start_date, description="a journal entry", source=source)

    assert not list(ReadJournalEntries[FakeSource].__args__)
    ReadJournalEntries[FakeSource].__args__ = (FakeSource,)

    assert list(ReadJournalEntries[FakeSource].__args__) == [FakeSource]
    assert isinstance(read_fn, ReadJournalEntries[FakeSource])

# Generated at 2022-06-14 04:12:41.682791
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    test_account = Account("Cash", "Cash", AccountType.ASSETS)
    test_journalentry = JournalEntry(date=datetime.datetime.today(), description="test", source=None)
    test_journalentry.post(datetime.datetime.today(), test_account, 10)
    test_journalentry.post(datetime.datetime.today(), test_account, -10)
    test_journalentry.validate()

# Generated at 2022-06-14 04:12:49.198337
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    """
    Test JournalEntry.post
    """
    entry = JournalEntry[object](date=datetime.date.today(), description='test', source=object())
    entry1 = entry.post(account=Account('',''), date=datetime.date.today(), quantity=3)
    entry2 = entry.post(account=Account('',''), date=datetime.date.today(), quantity=0)
    entry3 = entry.post(account=Account('',''), date=datetime.date.today(), quantity=-3)

    assert len(entry1.postings) == 1
    assert len(entry2.postings) == 0
    assert len(entry3.postings) == 1

# Generated at 2022-06-14 04:12:55.690668
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():

    from ..commons.types import Unit

    from .accounts import AccountType, Account
    from .commons import AccountValue

    ## Define a simple journal entry:
    j = JournalEntry(datetime.date(2020, 1, 1), "Test", None) \
        .post(datetime.date(2020, 1, 1), Account(AccountType.ASSETS, "A1", "A1"), +100) \
        .post(datetime.date(2020, 1, 1), Account(AccountType.EQUITIES, "O1", "O1"), -100)

    ## Validate:
    j.validate()

# Generated at 2022-06-14 04:12:57.045541
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    ...



# Generated at 2022-06-14 04:13:03.596872
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class Foo:
        pass

    result = ReadJournalEntries.__call__(lambda period: [], DateRange(datetime.date(2012, 1, 1), datetime.date(2012, 1, 1)))
    assert len(result) == 0
    #assert isinstance(result, [])
    #assert isinstance(result, Iterable[JournalEntry[Foo]])

# Generated at 2022-06-14 04:13:13.548910
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    '''
    Description : Test cases of method post in class JournalEntry
    Attribute:
        None
    Return:
        None
    '''
    print("Start test_JournalEntry_post")
    # test JounalEntry
    dt = datetime.date.today()
    acc1 = Account("Cash in hand")
    acc2 = Account("Food")
    acc3 = Account("Petrol")
    acc4 = Account("Stationary")
    acc5 = Account("Other Expenses")
    acc6 = Account("Income from contract")
    acc7 = Account("Savings Account")
    acc8 = Account("Investments")
    acc9 = Account("Short Term Loan")
    acc10 = Account("Long Term Loan")
    acc11 = Account("Equity")
    acc12 = Account("Liabilities")

    # test post


# Generated at 2022-06-14 04:13:19.113515
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.zeitgeist import as_date, at_end_of
    from datetime import date
    from typing import NamedTuple

    class Data(NamedTuple):
        pass

    def read_journals(period: DateRange) -> Iterable[JournalEntry[Data]]:
        return [
            JournalEntry(as_date('2019-07-01'), 'Journal 1', Data(), []),
            JournalEntry(at_end_of('2019-07-31'), 'Journal 2', Data(), []),
            JournalEntry(as_date('2019-08-01'), 'Journal 3', Data(), [])
        ]

    assert all(i.date <= date(2019, 8, 1) for i in read_journals(DateRange(as_date('2019-05-01'), as_date('2019-09-01'))))




# Generated at 2022-06-14 04:13:24.945052
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry(datetime.date(2018, 6, 1), "A", "T")
    j.post(j.date, Account(1, "A", AccountType.ASSETS), Quantity(100))
    j.post(j.date, Account(2, "B", AccountType.EQUITIES), Quantity(-100))
    j.validate()

# Generated at 2022-06-14 04:13:34.956629
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from datetime import timedelta
    from dateutil.parser import parse
    from streamz.utils import Dummy

    start_date = date(2019, 1, 1)
    end_date = start_date + timedelta(days=5)

    input_journal_entries = (
        JournalEntry[Dummy](parse("2019-01-03"), "JE-1", Dummy()),
        JournalEntry[Dummy](parse("2019-01-05"), "JE-2", Dummy()),
        JournalEntry[Dummy](parse("2019-01-08"), "JE-3", Dummy()),
    )

    actual_journal_entries = set(ReadJournalEntries()(DateRange(start_date, end_date)))

# Generated at 2022-06-14 04:13:42.839799
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class Test:
        def __call__(self):
            pass
    Test()

# Generated at 2022-06-14 04:13:52.684160
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # arrange
    from .accounts import AccountType, Account

    journal_entry = JournalEntry[int](datetime.date(2020, 4, 1), "description", "source")
    journal_entry.post(datetime.date(2020, 4, 1), Account("1", "Account 1", AccountType.EXPENSES), Quantity(100))
    journal_entry.post(datetime.date(2020, 4, 1), Account("2", "Account 2", AccountType.EXPENSES), Quantity(-100))
    journal_entry.post(datetime.date(2020, 4, 1), Account("3", "Account 3", AccountType.EQUITIES), Quantity(100))
    journal_entry.post(datetime.date(2020, 4, 1), Account("4", "Account 4", AccountType.EQUITIES), Quantity(-100))
    journal_entry

# Generated at 2022-06-14 04:13:59.654016
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # set up
    jr = JournalEntry('01/01/2020', 'Test')
    date = '01/01/2020'
    account = Account('Cash', 'Assets')
    quantity = 1000

    # execute
    jr.post(date, account, quantity)

    # assert
    assert jr.postings[0].journal == jr
    assert jr.postings[0].date == datetime.date(2020, 1, 1)
    assert jr.postings[0].account == account
    assert jr.postings[0].direction == Direction.INC
    assert jr.postings[0].amount == 1000


# Generated at 2022-06-14 04:14:03.867233
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Define the function.
    def f(period: DateRange):
        return 1

    # Assert the function is compatible with the protocol.
    assert ReadJournalEntries.__orig_bases__[0].__subclasscheck__(f.__class__)

# Generated at 2022-06-14 04:14:11.232974
# Unit test for method validate of class JournalEntry

# Generated at 2022-06-14 04:14:12.530094
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Note: no asserts because this is an abstract class method.
    print("Method ReadJournalEntries.__call__()")

# Generated at 2022-06-14 04:14:20.002023
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from ..commons.datetime import now
    from ..commons.zeitgeist import DateRange

    class SampleJournal:
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[int]]:
            yield JournalEntry(now(), "First entry", source=1)

    assert isinstance(SampleJournal()(DateRange()), Iterable)
    assert isinstance(list(SampleJournal()(DateRange()))[0], JournalEntry)

# Generated at 2022-06-14 04:14:32.541820
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from pytest import raises
    from ..commons.zeitgeist import DateTimeRange
    from .accounts import Account, ReadAccounts
    from .books import Book, BookId, ReadBooks
    from .categories import Category, ReadCategories


# Generated at 2022-06-14 04:14:33.356628
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass

# Generated at 2022-06-14 04:14:37.024344
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert hasattr(ReadJournalEntries, "__call__")
    assert callable(ReadJournalEntries.__call__)
    assert isinstance(ReadJournalEntries.__call__, property)

# Generated at 2022-06-14 04:15:00.074443
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType

    #: Date of the entry.

    date=datetime.date(2018,10,10)

    #: Description of the entry.

    description="Cash entered in the bank"

    #: Business object as the source of the journal entry.

    source=Account(AccountType.ASSETS, "Cash", "CHF")

    #: Postings of the journal entry.

    postings=[]

    #: Globally unique, ephemeral identifier.

    guid=makeguid()

    journal_entry = JournalEntry(date, description, source, postings, guid)

    assert journal_entry.date == date
    assert journal_entry.description == description
    assert journal_entry.source == source
    assert journal_entry.postings == postings
    assert journal_entry.guid == guid

    #: Date

# Generated at 2022-06-14 04:15:04.402657
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return []

    read_journal_entries()


# noinspection PyUnusedLocal

# Generated at 2022-06-14 04:15:13.184784
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Arrange
    def _make_journal_entries(begin: datetime.date, end: datetime.date) -> Iterable[JournalEntry[_T]]:
        for date in range(begin.toordinal(), end.toordinal() + 1):
            yield JournalEntry(datetime.date.fromordinal(date), "", None)

    # Act
    read_journal_entries = ReadJournalEntries(_make_journal_entries)
    entries = read_journal_entries(
        DateRange(datetime.date.fromordinal(15), datetime.date.fromordinal(18))
    )

    # Assert
    assert isinstance(entries, Iterable)
    assert len(entries) == 4 # type: ignore



# Generated at 2022-06-14 04:15:20.685178
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal: JournalEntry[str] = JournalEntry("2019-10-14", "Description", "Source")
    journal.post("2019-10-14", Account("A", AccountType.ASSETS), 100)
    journal.post("2019-10-14", Account("A", AccountType.ASSETS), -100)
    journal.post("2019-10-14", Account("A", AccountType.ASSETS), 0)
    assert journal.postings == [Posting(journal, "2019-10-14", Account("A", AccountType.ASSETS), Direction.INC, 100)]

# Generated at 2022-06-14 04:15:22.082867
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass  # explicitly noop.

# Generated at 2022-06-14 04:15:24.427419
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @ReadJournalEntries
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry[_T]]:
        pass
    assert callable(read_journal_entries)

# Generated at 2022-06-14 04:15:27.949360
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def fake_journal_entry_reader(*args, **kwargs) -> Iterable[JournalEntry[str]]: ...
    ReadJournalEntries[str]().__call__ = fake_journal_entry_reader

# Generated at 2022-06-14 04:15:29.960943
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    posting = Posting()
    journal_entry = JournalEntry()
    journal_entry.postings.append(posting)
    journal_entry.validate()

# Generated at 2022-06-14 04:15:37.138849
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @ReadJournalEntries
    def _(period: DateRange) -> Iterable[JournalEntry[_T]]:
        return [
            JournalEntry(datetime.date(1970, 1, 1), "test", None)
                .post(datetime.date(1970, 1, 1), Account("test", AccountType.ASSETS), +100)
                .post(datetime.date(1970, 1, 1), Account("test", AccountType.EXPENSES), -100)
        ]


# Generated at 2022-06-14 04:15:39.696177
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class ReadJournalEntriesImpl(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

# Generated at 2022-06-14 04:16:21.823217
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():

    # Arrange
    j: JournalEntry[object] = JournalEntry(date=datetime.date(2019,1,1), description="Test", source=object())

    # Act
    j.post(date=datetime.date(2019,1,1), account=Account(type=AccountType.ASSETS, name="Cash"), quantity=+5)
    j.post(date=datetime.date(2019,1,1), account=Account(type=AccountType.EXPENSES, name="Fee"), quantity=-5)
    j.post(date=datetime.date(2019,1,1), account=Account(type=AccountType.ASSETS, name="Cash"), quantity=+5)

# Generated at 2022-06-14 04:16:26.011611
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class SomeSource(ReadJournalEntries[int]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[int]]:
            pass

    _ = SomeSource()
    # The above code should not result in any errors.

# Generated at 2022-06-14 04:16:30.502952
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class JournalEntrySource(ReadJournalEntries[str]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[str]]:
            return []

    j = JournalEntrySource()

    assert j(DateRange(datetime.date(2020, 1, 1), datetime.date(2020, 1, 31)))

# Generated at 2022-06-14 04:16:38.681715
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    def journal_entries() -> Iterable[JournalEntry[_T]]:
        for i in range(10):
            yield JournalEntry(
                datetime.date(2018, 1, 1) + datetime.timedelta(i),
                f"description_{i}",
                None
            )

    def caller(period: DateRange):
        return journal_entries()

    assert issubclass(type(caller), ReadJournalEntries)
    assert len(list(caller(DateRange.entire(datetime.date(2018, 1, 1), datetime.date(2018, 1, 10))))) == 10

# Generated at 2022-06-14 04:16:49.869822
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from typing import Callable

    # noinspection PyMissingOrEmptyDocstring,PyShadowingNames
    class ReadJournalEntriesImpl(ReadJournalEntries[str]):
        def __init__(self, journal_entry: JournalEntry[str]):
            self.journal_entry: JournalEntry[str] = journal_entry

        def __call__(self, period: DateRange) -> Iterable[JournalEntry[str]]:
            yield self.journal_entry

    # noinspection PyMissingOrEmptyDocstring
    class ReadJournalEntriesImplFactory:
        def __init__(self, journal_entry: JournalEntry[str]):
            self.journal_entry = journal_entry

        def __call__(self) -> ReadJournalEntriesImpl:
            return ReadJournalEntriesImpl(self.journal_entry)


# Generated at 2022-06-14 04:16:58.994685
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    test_acc1 = Account("1010", AccountType.ASSETS)
    test_acc2 = Account("2010", AccountType.ASSETS)
    test_acc3 = Account("3100", AccountType.EXPENSES)
    test_acc4 = Account("4100", AccountType.LIABILITIES)
    test_acc5 = Account("5000", AccountType.REVENUES)
    test_acc6 = Account("6000", AccountType.EQUITIES)

    test_je = JournalEntry(datetime.date.today(), "Test", None)
    test_je.post(datetime.date.today(), test_acc1, -400)
    test_je.post(datetime.date.today(), test_acc2, 100)
    test_je.post(datetime.date.today(), test_acc3, 100)
    test

# Generated at 2022-06-14 04:17:04.809311
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    ## Setup:
    from .accounts import Account
    from .types import BusinessObject
    from .book import Book
    from .ledger import Ledger
    from .journal import Journal
    from .descriptors import Descriptor

    ## Setup:
    book = Book(Descriptor(name="Test Book"))
    ledger = Ledger(name="Test Ledger", normal_balance=AccountType.ASSETS, book=book)
    journal = Journal(name="Test Journal")
    journal.add_account(ledger.account)
    
    ## Given:
    journal_entry = JournalEntry(datetime.date(2000, 1, 1), "Journal Entry", BusinessObject())

    ## When:
    journal_entry.post(datetime.date(2000, 1, 1), ledger.account, 10000)

# Generated at 2022-06-14 04:17:14.382350
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Given
    je = JournalEntry(
        date=datetime.date(2020, 10, 1), description="Transaction1", source=None,
    )
    date = je.date
    account1 = Account(
        guid=Guid("a3cd3add-93eb-4f15-8e78-35b9eee34432"),
        name="Assets-Cash",
        type=AccountType.ASSETS,
    )
    account2 = Account(
        guid=Guid("a3cd3add-93eb-4f15-8e78-35b9eee34432"),
        name="Expenses-Rent",
        type=AccountType.EXPENSES,
    )
    # When
    je.post(date, account1, 100)
    je.post(date, account2, -100)

# Generated at 2022-06-14 04:17:20.027859
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..models.accounts import Account
    account = Account("foo", AccountType.ASSETS)
    entry = JournalEntry(datetime.date.today(), "Testing", object())
    entry.post(datetime.date.today(), account, 10.0)
    entry.validate()



# Generated at 2022-06-14 04:17:28.145295
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Setup:
    from ..ledger import JournalEntries as jes
    number_of_entries = jes.count

    # Exercise:
    entries = jes(DateRange.of(datetime.date(2019, 10, 5), datetime.date(2019, 10, 7)))

    # Verify:
    assert isinstance(entries, Iterable)
    entries = list(entries)
    assert isinstance(entries, list)
    assert len(entries) == number_of_entries
    for j in entries:
        assert isinstance(j, JournalEntry)
        # TODO write more validations

# Generated at 2022-06-14 04:18:47.151459
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # journal entry with minimum data
    journal_entry = JournalEntry(datetime.date.today(), "it is a test", None)
    account_balance = Account("Balance", AccountType.ASSETS)
    account_credit = Account("Credit", AccountType.REVENUES)
    account_debit = Account("Debit", AccountType.EXPENSES)
    # post 1 euro
    journal_entry.post(datetime.date.today(), account_balance, Quantity(1))
    assert len(journal_entry.postings) == 1
    assert journal_entry.postings[0].amount.quantity == Quantity(1)
    assert journal_entry.postings[0].direction == Direction.INC
    # post -2 euro
    journal_entry.post(datetime.date.today(), account_balance, Quantity(-2))

# Generated at 2022-06-14 04:18:55.002055
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    
    from ..commons.zeitgeist import Date
    from .accounts import Account, AccountType, BalanceType

    # Test
    def __call__(_):
        j = JournalEntry[str]()
        j.post(Date(2020, 5, 16), Account('A1', AccountType.EXPENSES, BalanceType.DR), Quantity(1000))
        j.post(Date(2020, 5, 16), Account('A2', AccountType.REVENUES, BalanceType.CR), Quantity(1000))
        return [j]

    ReadJournalEntries['str'] = __call__
    assert len(ReadJournalEntries['str'](DateRange(Date(2020,5,15), Date(2020,5,17)))) == 1

# Generated at 2022-06-14 04:18:55.479548
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    assert True

# Generated at 2022-06-14 04:19:02.896219
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from typing import Dict, List
    from ..commons.numbers import Quantity
    from .accounts import Account
    from .journal import JournalEntry

    # Forst create the actual journal entries
    entry1 = JournalEntry(date(2019, 4, 3), "Asset Acquisition", None).post(date(2019, 4, 3), Account("bank-1000"), Quantity(100000))
    entry2 = JournalEntry(date(2019, 4, 4), "Equity Investment", None).post(date(2019, 4, 4), Account("equity-1000"), Quantity(-50000))

    entries = [entry1, entry2]

    # Now create the test helper function that compares the journal entries

# Generated at 2022-06-14 04:19:12.049520
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    bank = Account(type=AccountType.ASSETS, name="bank")
    credit_card = Account(type=AccountType.LIABILITIES, name="credit card")
    furniture = Account(type=AccountType.EXPENSES, name="furniture")
    salary = Account(type=AccountType.REVENUES, name="salary")

    j = JournalEntry[str](
        "2020-01-20",
        "my first journal entry",
        "my business object"
    )
    j.post(
        "2020-01-20", bank, 1_000
    ).post(
        "2020-01-20", credit_card, -500
    )
    
    print(j)

    assert len(j.postings) == 2
    assert j.postings[0].amount == 1_000

# Generated at 2022-06-14 04:19:21.267509
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    #Arrange
    a1 = Account('a1', 'Assets')
    a2 = Account('a2', 'Assets')
    je1 = JournalEntry(datetime.date(2020,1,1), 'je1', 'source1')
    je1.postings = [Posting(je1, datetime.date(2020,1,1), a1, Direction.INC, Amount(100)), Posting(je1, datetime.date(2020,1,1), a2, Direction.DEC, Amount(100))]

    #Act
    je1.validate()
    
    #Assert
    # No exception occured if no assert is raised

# Generated at 2022-06-14 04:19:29.273694
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from . import Account, AccountType
    from .accounts import AccountToExpenseMapping
    from .commons.others import makeguid

    CreditCardAccount = Account(
        "Credit Card", AccountType.ASSETS, AccountToExpenseMapping.for_asset("Credit Card")
    )

    j1 = JournalEntry[str](
        date=datetime.date.today(),
        description="Check JE validation",
        source=makeguid(),
        guid=makeguid(),
    )
    j1.post(datetime.date.today(), CreditCardAccount, Amount(100.00))
    j1.post(datetime.date.today(), CreditCardAccount, Amount(-100.00))
    j1.validate()

# Generated at 2022-06-14 04:19:37.056415
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from builtins import int, range
    from ..commons.zeitgeist import Date
    from ..commons.numbers import isum
    
    # TODO
    return
    
    c = [JournalEntry(Date(d), "source", "description") for d in range(1, 10)]
    c[0] = c[0].post(Date(1), "cash", 100)
    c[0] = c[0].post(Date(1), "expenses", -100)
    c[1] = c[1].post(Date(2), "cash", 200)
    c[1] = c[1].post(Date(2), "revenue", -200)
    c[2] = c[2].post(Date(3), "a", 100)

# Generated at 2022-06-14 04:19:46.185609
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..accounts.account_repo import AccountRepository
    from ..commons.context import get_context
    from ..commons.events import publish
    from ..commons.events import subscribe
    from ..diary.events import DiaryEntryCreated

    ## Create a context and register the account repository:
    context = get_context()
    context.register("account_repo", AccountRepository())

    ## Create a new account to post to:
    publish(DiaryEntryCreated(datetime.date.today(), "Test"))
    publish(AccountCreated("Test"))
    account = context.account_repo.of_name("Test")

    ## Check that the account represents a zero-balance:
    assert account.balance.is_zero(), f"Account balance is not zero: {account.balance}"

    ## Invoke post of JournalEntry and check the balance

# Generated at 2022-06-14 04:19:52.561804
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # arrange
    journal = JournalEntry[int](
        date=datetime.date(2020, 2, 23),
        description="Test JournalEntry validate() method",
        source=1)

    # act
    journal.post(datetime.date(2020, 2, 23), Account("test-1000", AccountType.ASSETS), Quantity(200.00))
    journal.post(datetime.date(2020, 2, 23), Account("test-2000", AccountType.EQUITIES), Quantity(-200.00))

    # assert
    journal.validate()