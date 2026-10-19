

# Generated at 2022-06-14 04:11:31.493812
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    #Accounts
    assets = Account(1, AccountType.ASSETS, "Assets")
    expenses = Account(2, AccountType.EXPENSES, "Expenses")
    revenues = Account(3, AccountType.REVENUES, "Revenues")
    liabilities = Account(4, AccountType.LIABILITIES, "Liabilities")
    equities = Account(5, AccountType.EQUITIES, "Equities")

    #JournalEntry
    journalEntry = JournalEntry(date(2017, 9, 5), "description", "source")
    journalEntry.post(date(2017, 9, 5), assets, 400)
    journalEntry.post(date(2017, 9, 5), expenses, 800)
    journalEntry.post(date(2017, 9, 5), revenues, 1000)

# Generated at 2022-06-14 04:11:35.455475
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Tests ``__call__`` method of :class:`ReadJournalEntries`.
    """
    def function(period: DateRange) -> Iterable[JournalEntry[int]]:
        pass

    assert isinstance(function, ReadJournalEntries)

# Generated at 2022-06-14 04:11:45.289966
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from ..accounts.accounts import AccountType, Account
    from ..accounts.accounts import Postings
    j = JournalEntry(datetime.date.today(), "Test JournalEntry", Postings())
    j.post(j.date, Account(AccountType.ASSETS, 'EXP'), Amount(100))
    j.post(j.date, Account(AccountType.ASSETS, 'INC'), Amount(200))
    assert not j.postings[0].is_credit
    assert j.postings[1].is_credit
    assert j.postings[0].account.type == AccountType.ASSETS
    assert j.postings[1].account.type == AccountType.ASSETS
    assert j.postings[0].amount == Amount(100)
    assert j.postings[1].amount == Amount(200)

# Generated at 2022-06-14 04:11:55.096050
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    accountA = Account('A', AccountType.ASSETS)
    accountB = Account('B', AccountType.EQUITIES)
    entry = JournalEntry(datetime.date.today(), '', None)
    entry.post(datetime.date.today(), accountA, 1)
    entry.post(datetime.date.today(), accountB, 1)
    entry.post(datetime.date.today(), accountA, -1)
    entry.post(datetime.date.today(), accountB, -1)
    assert len(entry.increments) == 2
    assert len(entry.decrements) == 2
    assert len(entry.debits) == 1
    assert len(entry.credits) == 1

# Generated at 2022-06-14 04:12:03.992012
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType
    from .ledgers import Ledger, PostingRule

    ledger = Ledger("Test Ledger")
    ledger.add_rule(PostingRule(ledger.get_account(AccountType.REVENUES).get("Sales"), ledger.get_account(AccountType.ASSETS).get("Cash")))
    je1 = ledger.record("Test journal entry - 1").post("2020-01-01", Account("ASSETS", "Accounts receivable"), Amount("100"))
    je2 = ledger.record("Test journal entry - 2").post("2020-01-02", Account("ASSETS", "Cash"), Amount("100"))
    je3 = ledger.record("Test journal entry - 3").post("2020-01-03", Account("EQUITIES", "Equity"), Amount("100"))
    je4 = ledger.record

# Generated at 2022-06-14 04:12:09.434036
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import NewAccount, AccountType
    from .businesses import NewBusiness, BusinessType
    from .commons.numbers import Amount, Quantity
    from datetime import date

    ## Create a new account:
    account = NewAccount("0001", AccountType.LIABILITIES, "Credit")

    ## Create a new business:
    business = NewBusiness("0001", BusinessType.GOVERNMENT, "NZ Govt")

    ## Create journal entries:
    journal_entry = JournalEntry[Business]("Test Journal Entry")
    for i in range(5):
        journal_entry.post(date(2019, 1, 1), account, Quantity(-i))

    ## Add some postings:
    for i in range(5):
        journal_entry.post(date(2019, 1, 1), account, Quantity(i))

    ## Validate:


# Generated at 2022-06-14 04:12:21.168878
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    import datetime
    from dataclasses import dataclass
    from ..commons.numbers import Quantity
    from ..commons.others import DateRange, makeguid
    from .accounts import Account, AccountType

    @dataclass
    class Transaction(_T):
        """
        Stub implementation for transaction class.
        """

        #: Transaction date.
        date: datetime.date

        #: Description of the transaction.
        description: str

        #: Globally unique, ephemeral identifier.
        guid: Guid = makeguid()

        def journal(self, journal: JournalEntry[_T]) -> JournalEntry[_T]:
            """
            Posts the transaction to a journal entry.

            :param journal: Journal entry to post the transaction to.
            :return: Journal entry after posting.
            """

# Generated at 2022-06-14 04:12:28.040480
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Given
    journal_entry=JournalEntry(datetime.date(2020,2,3),"Trial of Journal Entry",None)
    journal_entry.post(datetime.date(2020,2,3),Account("1001","cash",AccountType.ASSETS),-500)
    journal_entry.post(datetime.date(2020,2,3),Account("4001","sundry debtors",AccountType.ASSETS),500)
    # When
    journal_entry.validate()
    # Then
    # No Error thrown

# Generated at 2022-06-14 04:12:28.582449
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:12:35.994488
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    entries = (
        JournalEntry(datetime.date(2019, 1, 1), "", None),
        JournalEntry(datetime.date(2019, 1, 2), "", None),
        JournalEntry(datetime.date(2020, 1, 1), "", None),
    )
    read_journal_entries = lambda period: entries

    assert list(read_journal_entries(DateRange(begin=datetime.date(2019, 1, 1), end=datetime.date(2019, 1, 10)))) == [entries[0], entries[1]]
    assert list(read_journal_entries(DateRange(begin=datetime.date(2019, 1, 1), end=datetime.date(2018, 1, 10)))) == [entries[0]]

# Generated at 2022-06-14 04:12:44.639079
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Initialize data
    journal = JournalEntry(date=datetime.date.today(), description="Test Entry", source=123456)
    date = datetime.date.today()
    account = Account(name="Assets", type=AccountType.ASSETS)
    quantity = Quantity(12)
    # Use the method post
    journal.post(date, account, quantity)
    # Assert results
    assert journal.postings[0].date == date
    assert journal.postings[0].account == account
    assert journal.postings[0].direction == Direction.INC

# Generated at 2022-06-14 04:12:53.747923
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    """
    Test validation method of the JournalEntry class.
    """

    ## Validate status of a correctly balanced journal entry:
    je = JournalEntry(datetime.date.today(), "Test Journal Entry", '')
    je.post(datetime.date.today(), Account("Cash", AccountType.ASSETS), Quantity(100))
    je.post(datetime.date.today(), Account("Equity"), Quantity(-100))
    je.validate()

    ## Raise assertion error for wrongly balanced journal entry:
    je = JournalEntry(datetime.date.today(), "Test Journal Entry", '')
    je.post(datetime.date.today(), Account("Cash", AccountType.ASSETS), Quantity(100))
    je.post(datetime.date.today(), Account("Equity"), Quantity(-90))

# Generated at 2022-06-14 04:13:06.586493
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    
    _fake_journal_entry_a = JournalEntry(datetime.date(2020, 1, 1), "fake_description_a", None)
    _fake_journal_entry_b = JournalEntry(datetime.date(2020, 1, 2), "fake_description_b", None)

    def _fake_journal_entries_reader(period: DateRange) -> Iterable[JournalEntry[_T]]:
        if period.end < datetime.date(2020, 1, 2):
            yield _fake_journal_entry_a

    assert list(_fake_journal_entries_reader([datetime.date(2020, 1, 1), datetime.date(2020, 1, 2)])) == [_fake_journal_entry_a]
    assert list(_fake_journal_entries_reader(datetime.date(2020, 1, 1)))

# Generated at 2022-06-14 04:13:16.405618
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class Entry(JournalEntry):
        def __init__(self, date, description, source, postings, guid=None):
            super().__init__(date, description, source, postings, guid)

    class JournalEntries(ReadJournalEntries):
        def __init__(self, entries):
            self._entries = entries

        def __call__(self, period):
            return (e for e in self._entries if period.contains(e.date))


# Generated at 2022-06-14 04:13:20.008654
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    ReadJournalEntries.__call__(lambda period: [JournalEntry[str](date=datetime.date.today(), description="", source="")], DateRange())



# Generated at 2022-06-14 04:13:31.884566
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import GeneralLedgerAccount
    joe = GeneralLedgerAccount('JoeAccount', AccountType.ASSETS)
    prop = GeneralLedgerAccount('PropertyAccount', AccountType.ASSETS)
    revenues = GeneralLedgerAccount('RevenuesAccount', AccountType.REVENUES)
    expenses = GeneralLedgerAccount('ExpensesAccount', AccountType.EXPENSES)
    journal = JournalEntry(date=datetime.date(2020, 5, 1), description='a journal entry', source=None)
    journal.post(date=datetime.date(2020, 4, 25), account=joe, quantity= +1000)
    journal.post(date=datetime.date(2020, 4, 25), account=revenues, quantity=-1000)

# Generated at 2022-06-14 04:13:42.783076
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountType
    from .ledgers import Ledger
    from ..unitofwork import UnitOfWork

    uow = UnitOfWork()
    journal = Ledger(uow)

    entry = JournalEntry(datetime.date.today(), "Sample entry") \
        .post(datetime.date.today(), Account("Revenue: Sales", AccountType.REVENUES), +1) \
        .post(datetime.date.today(), Account("Expenses: Freight", AccountType.EXPENSES), +1) \
        .post(datetime.date.today(), Account("Cash", AccountType.ASSETS), -1)

    journal.add(entry)
    uow.commit()

    entry = entry.post(datetime.date.today(), Account("Accounts Receivable", AccountType.ASSETS), +1)


# Generated at 2022-06-14 04:13:50.495018
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    proto = JournalEntry[None]
    with pytest.raises(AssertionError):
        proto().post(datetime.date.today(), Account(AccountType.ASSETS, "test"), 1).post(
            datetime.date.today(), Account(AccountType.ASSETS, "test"), -1
        ).validate()
    proto().post(datetime.date.today(), Account(AccountType.ASSETS, "test"), 1).post(
        datetime.date.today(), Account(AccountType.EXPENSES, "test"), -1
    ).validate()

# Generated at 2022-06-14 04:13:58.351556
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j1 = JournalEntry(datetime.date(2020, 1, 1), "Test", "Reference", [])
    j1.post(datetime.date(2020, 1, 1), "Account 1", 1000)
    j1.post(datetime.date(2020, 1, 1), "Account 2", -1000)
    j1.post(datetime.date(2020, 1, 1), "Account 3", 0)
    j1.post(datetime.date(2020, 1, 1), "Account 4", -500)
    j1.post(datetime.date(2020, 1, 1), "Account 5", 500)
    j1.validate()
    print("JournalEntry.validate passes")

# Generated at 2022-06-14 04:14:03.923992
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    journalEntry = JournalEntry(datetime.date(2020, 1, 1), "test journal entry", "test source")
    journalEntry.post(datetime.date(2020, 1, 1), Account("Assets"), 100)
    journalEntry.post(datetime.date(2020, 1, 1), Account("Expenses"), -100)

    journalEntry.validate()

# Generated at 2022-06-14 04:14:32.298214
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import ReadAccounts
    from .periods import Period
    from .periods import ReadPeriods


# Generated at 2022-06-14 04:14:35.259692
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class A:
        pass

    assert ReadJournalEntries.__isabstractmethod__
    ReadJournalEntries().register(
        lambda self, period: []
    ) #type: ignore

# Generated at 2022-06-14 04:14:46.294694
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from datetime import date
    from ..commons.others import makeguid

    class JournalEntry:
        def __init__(self, date: date, description: str, source: str):
            self.date = date
            self.description = description
            self.source = source
            self.postings = []
            self.guid = makeguid()

        def post(self, date: date, account: str, quantity: int):
            if (quantity != 0):
                self.postings.append(Posting(self, date, account, (Direction.INC.value if quantity > 0 else Direction.DEC.value), abs(quantity)))

    class Posting:
        def __init__(self, journal: JournalEntry, date: date, account: str, direction: int, amount: int):
            self.journal = journal


# Generated at 2022-06-14 04:14:57.754827
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    actual = []
    def add(*args):
        actual.append(args)

    entry = JournalEntry(date=datetime.date(2019, 1, 1), source=None)

    entry.post(date=datetime.date(2019, 1, 1), account=Account(AccountType.ASSETS, "CASH"), quantity=+10)
    entry.post(date=datetime.date(2019, 1, 1), account=Account(AccountType.EXPENSES, "FOOD"), quantity=-10)

    # Should succeed:
    entry.validate()

    entry.post(date=datetime.date(2019, 1, 1), account=Account(AccountType.EQUITIES, "CAPITAL"), quantity=+20)
    #Should fail:

# Generated at 2022-06-14 04:15:09.099443
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    #pylint: disable=anomalous-backslash-in-string
    # Test-cases:
    def _make_source(description: str, date: datetime.date) -> str:
        return f"{description}|{date:%d/%m/%Y}\n"

    def _make_account(number: str, type_: AccountType) -> Account:
        return Account(number=number, name=number, type=type_)


# Generated at 2022-06-14 04:15:09.645025
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:15:10.850979
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert ReadJournalEntries.__call__(None, None)



# Generated at 2022-06-14 04:15:22.513852
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    # Case: post a transaction of a journal entry
    # Case: post a transaction of a journal entry
    accountAssets = Account(accountType=AccountType.ASSETS, accountName="Assets")
    accountRevenues = Account(accountType=AccountType.REVENUES, accountName="Revenues")
    source = "My source"
    journalEntry = JournalEntry(source=source, date=datetime.date.today(), description="Today's journal")
    journalEntry.post(date=datetime.date.today(), account=accountAssets, quantity=100)
    journalEntry.post(date=datetime.date.today(), account=accountRevenues, quantity=-100)
    # Case: check the result after post a transaction
    assert journalEntry.source == source
    assert journalEntry.postings[0].source == source
    assert journal

# Generated at 2022-06-14 04:15:30.746815
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from datetime import date
    from typing import Iterable
    from dataclasses import dataclass
    from collections import abc

    @dataclass
    class Person:
        id: int
        name: str

    @dataclass
    class JournalEntry:
        date: date

    @ReadJournalEntries
    def read_journal_entries(period: DateRange) -> Iterable[JournalEntry]:
        yield JournalEntry(date(2019, 12, 31))
        yield JournalEntry(date(2020, 1, 1))
        yield JournalEntry(date(2020, 1, 2))


    assert isinstance(read_journal_entries, abc.Callable)



# Generated at 2022-06-14 04:15:41.732998
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    j = JournalEntry(datetime.date(2020,1,1), "Test", "Test")
    j.post(datetime.date(2020, 1, 1),  Account(AccountType.ASSETS, "Account1"), 100)
    j.post(datetime.date(2020, 1, 2),  Account(AccountType.REVENUES, "Account2"), -100)
    j.validate()

    j2 = JournalEntry(datetime.date(2020,1,1), "Test", "Test")
    j2.post(datetime.date(2020, 1, 1), Account(AccountType.ASSETS, "Account1"), 100)
    j2.post(datetime.date(2020, 1, 2), Account(AccountType.REVENUES, "Account2"), -50)

# Generated at 2022-06-14 04:15:56.505402
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    pass

# Generated at 2022-06-14 04:16:07.387977
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import AccountType
    from .events import BusinessEvent
    from .events import Ledger, Posting, EntryCreated
    from .events import is_valid, make_ledger, load, save
    from .events import create_journal_entry
    from .events import read_journal_entries as read_je
    from .events import read_journal_entry_postings as read_jep
    from .events import read_journal_entry_sources as read_jes
    from .events import read_journal_postings as read_jpo
    from .events import read_journal_posting_ledgers as read_jpl
    from .readers import find_accounts, find_open_entries

    # Let's create an account and a business object:
    account_number = "1111"

# Generated at 2022-06-14 04:16:10.337551
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    """
    Validates that `ReadJournalEntries` is a protocol type.
    """
    class MyReadJournalEntries(ReadJournalEntries[_T]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            pass

# Generated at 2022-06-14 04:16:20.855612
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # Arrange
    #    | _T |  period  |   result   |
    #    | ---| ---------| -----------|
    #    |  0 |  period0 | result0_0  |
    #    |  0 |  period1 | result0_1  |
    #    |  0 |  period2 | result0_2  |
    #    |  1 |  period0 | result1_0  |
    #    |  1 |  period1 | result1_1  |
    #    |  1 |  period2 | result1_2  |
    class FakeJournalEntries:
        def __init__(self, result: Iterable[JournalEntry]):
            self.result = result


# Generated at 2022-06-14 04:16:26.226107
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from ..libraries.postings import Postings
    from ..models.test import TestJournalEntries

    for j in TestJournalEntries():
        j.validate()
        try:
            Postings(j).validate()
        except:
            raise Exception(j)

# Generated at 2022-06-14 04:16:32.637055
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import AccountFactory

    # Creation of accounts
    assets = AccountFactory()["Assets"]

    # Creation of a journal entry
    journal = JournalEntry.new()
    journal.post(datetime.date.today(), assets, 100)

    # Verification of the journal entry
    assert journal.postings[0].direction == "INC", "The posting is not an increment"
    assert journal.postings[0].is_debit == True, "The posting is a debit"
    assert journal.postings[0].is_credit == False, "The posting is not a credit"

# Generated at 2022-06-14 04:16:34.195139
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # pylint: disable=unused-argument
    pass

# Generated at 2022-06-14 04:16:42.815467
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import SimpleAccount

    a = SimpleAccount('TEST', 'TEST', AccountType.ASSETS, 1000)
    b = SimpleAccount('TEST', 'TEST', AccountType.REVENUES, 1000)

    je = JournalEntry[str](
        date = datetime.date(2020, 3, 3),
        description = "Test",
        source = "TEST"
    )
    je.post(datetime.date(2020, 3, 3), a, 100.00)
    je.post(datetime.date(2020, 3, 3), b, -100.00)
    ## Check:
    assert je.postings[0].is_debit
    assert je.postings[1].is_credit
    return je

if __name__ == '__main__':
    je = test_JournalEntry_

# Generated at 2022-06-14 04:16:50.935187
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .postings import post_journal_entry

    date = datetime.date(2019, 8, 18)
    journal = JournalEntry(date, "Journal Entry")
    journal.post(date, Account("Cash", AccountType.ASSETS, "Assets"), -100)
    journal.post(date, Account("Revenues", AccountType.REVENUES, "Revenues"), 100)

    actual = tuple(post_journal_entry(journal))
    expected = \
        (Posting(journal, date, Account("Cash", AccountType.ASSETS, "Assets"), Direction.DEC, Amount(100)),
         Posting(journal, date, Account("Revenues", AccountType.REVENUES, "Revenues"), Direction.INC, Amount(100)))
    assert actual == expected


# Generated at 2022-06-14 04:16:52.806945
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    assert ReadJournalEntries.__call__.__qualname__ == "ReadJournalEntries.__call__"

# Generated at 2022-06-14 04:17:33.519615
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .globals import GLOBAL_ACCOUNTS

    # create a journal entry
    j = JournalEntry[str]("2020-09-13", "Test journal entry", "Object 123")
    # post debit
    j.post("2020-09-13", GLOBAL_ACCOUNTS.revenues, -100)
    # post credit
    j.post("2020-09-13", GLOBAL_ACCOUNTS.assets.bank, 100)
    # get postings
    postings = list(j.postings)
    # assert postings
    assert len(postings) == 2
    assert postings[0].direction == Direction.DEC
    assert postings[1].direction == Direction.INC
    assert postings[0].is_debit
    assert not postings[1].is_debit


# Generated at 2022-06-14 04:17:34.207544
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass

# Generated at 2022-06-14 04:17:42.871062
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    # Create 2 journal entries

    j1 = JournalEntry(date=datetime.date(2020, 9, 24), description='This is the first post')
    j2 = JournalEntry(date=datetime.date(2020, 9, 24), description='This is the second post')
    j1.post(date=datetime.date(2020, 9, 24), account=Account(account_type=AccountType.ASSETS, code='10', name='Cash', parent=None), quantity=Quantity(100))
    j1.post(date=datetime.date(2020, 9, 24), account=Account(account_type=AccountType.REVENUES, code='50', name='Interest Revenue', parent=None), quantity=Quantity(-100))

# Generated at 2022-06-14 04:17:45.724468
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journal_entry = JournalEntry(datetime.date.today(), "This is a test", "This is a test")
    journal_entry.post(datetime.date.today(), Account(1, "Cash", AccountType.ASSETS), 10)
    journal_entry.post(datetime.date.today(), Account(2, "Account Receivable", AccountType.LIABILITIES), -10)
    journal_entry.validate()

# Generated at 2022-06-14 04:17:55.130283
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    p1 = Posting(journal=None, date=datetime.date(1,1,1), account=Account(0, 'Account1', AccountType.ASSETS, 0), direction=Direction.INC, amount=Amount(10))
    p2 = Posting(journal=None, date=datetime.date(1,1,1), account=Account(0, 'Account2', AccountType.LIABILITIES, 0), direction=Direction.DEC, amount=Amount(10))
    je = JournalEntry(date=datetime.date(1, 1, 1), description='Test', source=None, postings=[p1,p2])
    try:
        je.validate()
    except:
        assert False

# Generated at 2022-06-14 04:17:56.879208
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class A:
        pass

    assert isinstance(ReadJournalEntries[A](), ReadJournalEntries)

test_ReadJournalEntries___call__()

# Generated at 2022-06-14 04:18:03.094684
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    journal_entry = JournalEntry[object].__new__(JournalEntry)
    journal_entry.date = datetime.date(2019,12,25)
    journal_entry.description = "Description"
    journal_entry.source = object
    journal_entry.postings.append(Posting(journal_entry, journal_entry.date, Account("Cash"), Direction.INC, Amount(500)))
    journal_entry.postings.append(Posting(journal_entry, journal_entry.date, Account("Sales"), Direction.DEC, Amount(500)))
    journal_entry.postings.append(Posting(journal_entry, journal_entry.date, Account("Income"), Direction.INC, Amount(500)))

# Generated at 2022-06-14 04:18:12.671800
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    class _S:
        def journal_entries(self, period: DateRange) -> Iterable[JournalEntry[_T]]:
            ...  # pragma: no cover

    _s = _S()
    _call = ReadJournalEntries.__getitem__(ReadJournalEntries, _s)
    assert _call(None) == _s.journal_entries(None)

ReadJournalEntries.register(
    type=ReadJournalEntries._SpecialForm(  # pylint: disable=protected-access
        name="SomeObject",
        __call__=ReadJournalEntries._SpecialForm.__getitem__(ReadJournalEntries._SpecialForm, "journal_entries"),
    )
)

# Generated at 2022-06-14 04:18:19.993358
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    from .accounts import Account, AccountType
    from .business import ExpenseReport, ExpenseReportLine

    def post(journal: JournalEntry[ExpenseReportLine], line: ExpenseReportLine):
        journal = journal.post(
            line.occurred, Account(AccountType.LIABILITIES, "Expenses", "Expense Account"), line.expense.amount
        )
        return journal

    try:
        journal = JournalEntry(datetime.date.today(), "Dummy", ExpenseReportLine(
            ExpenseReport(datetime.date.today(), "Dummy"), "Dummy", "Dummy", "Dummy", "Dummy", 0, 0
        )).validate()
    except AssertionError as e:
        pass

# Generated at 2022-06-14 04:18:30.519265
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    from .accounts import Account, AccountType
    from .journals import Journal

    j = Journal()
    a = Account(AccountType.ASSETS, "Cash", "Cash")
    b = Account(AccountType.EXPENSES, "Rent", "Rent")

    je = JournalEntry(datetime.date.today(), "Test", None)

    je.post(datetime.date.today(), a, 100)
    je.post(datetime.date.today(), b, -100)

    assert len(je.postings) == 2

    assert je.debits.amount == 100
    assert je.credits.amount == 100

    assert je.postings[0].amount == 100
    assert je.postings[1].amount == 100

# Generated at 2022-06-14 04:19:53.735770
# Unit test for method __call__ of class ReadJournalEntries

# Generated at 2022-06-14 04:20:03.670067
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():

    from .accounts import Account
    from .accounts import AccountType

    account1 = Account("Revenues", AccountType.REVENUES)
    account2 = Account("Expenses", AccountType.EXPENSES)
    account3 = Account("Assets", AccountType.ASSETS)
    account4 = Account("Equities", AccountType.EQUITIES)

    je1 = JournalEntry(datetime.date(2020, 7, 14), "test", "test", [])
    je1.post(datetime.date(2020, 7, 14), account1, 100)
    je1.post(datetime.date(2020, 7, 14), account2, -100)
    je1.validate()

    je2 = JournalEntry(datetime.date(2020, 7, 14), "test", "test", [])
    je2.post

# Generated at 2022-06-14 04:20:13.009706
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .accounts import Account, AccountType
    from .ledgers import Ledger, LedgerEntry
    from .business import Business
    from .books import Book, BookEntry

    def entry(ledger: Ledger, date: datetime.date, description: str, amount: Amount) -> JournalEntry[LedgerEntry]:
        return JournalEntry(date=date, description=description, source=LedgerEntry(date, description, amount),
                            postings=[Posting(journal=None, date=date, account=ledger.account, direction=Direction.INC,
                                              amount=amount)])


# Generated at 2022-06-14 04:20:16.936964
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    # type: () -> None
    class _ReadJournalEntries(ReadJournalEntries[object]):
        def __call__(self, period: DateRange) -> Iterable[JournalEntry[object]]:
            pass


# Generated at 2022-06-14 04:20:18.034995
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    pass


# Generated at 2022-06-14 04:20:27.816701
# Unit test for method post of class JournalEntry
def test_JournalEntry_post():
    journalEntry = JournalEntry(datetime.date(2020, 1, 1), 'description', 'source')
    journalEntry.post(datetime.date(2020, 1, 1), Account(1, 'Account name', '', '', datetime.date(2020, 1, 1), '', '', '', AccountType.ASSETS, False), 1)
    assert journalEntry.postings[0].direction == Direction.INC
    assert journalEntry.postings[0].amount.value == 1

    journalEntry = JournalEntry(datetime.date(2020, 1, 1), 'description', 'source')
    journalEntry.post(datetime.date(2020, 1, 1), Account(1, 'Account name', '', '', datetime.date(2020, 1, 1), '', '', '', AccountType.EXPENSES, False), -1)
   

# Generated at 2022-06-14 04:20:38.993116
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    from .time import FinancialPeriod

    from .ledgers import Ledger, read_ledger_entries
    from .time import quarterly_periods
    from .accounts import LedgerAccount, LedgerAccountMapping

    ledger = Ledger()
    ledger.roll_out(ledger_account_mapping=LedgerAccountMapping())

    def testee(source: JournalEntry, accounts_mapping: LedgerAccountMapping):
        """
        Tests if the invariant holds:
            If a Posting is debited, the corresponding account in the Ledger will be debited and vice-versa.
        """
        for posting in source.postings:
            if posting.is_debit:
                assert ledger.debits(posting.account.name, posting.amount) > 0

# Generated at 2022-06-14 04:20:46.660454
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass
    class JournalEntry1(JournalEntry):
        pass

    @dataclass
    class JournalEntry2(JournalEntry):
        pass

    def read(period: DateRange) -> Iterable[JournalEntry[str]]:
        return (JournalEntry1("date1", "desc1", "source1"), JournalEntry2("date2", "desc2", "source2"))

    assert len(list(read(DateRange("date_from", "date_to")))) == 2

# Generated at 2022-06-14 04:20:47.318570
# Unit test for method validate of class JournalEntry
def test_JournalEntry_validate():
    pass

# Generated at 2022-06-14 04:20:55.017628
# Unit test for method __call__ of class ReadJournalEntries
def test_ReadJournalEntries___call__():
    @dataclass(frozen=True)
    class TestJournalEntry(JournalEntry[_T]):
        pass
    @dataclass(frozen=True)
    class TestEntity:
        pass
    @dataclass(frozen=True)
    class TestAccount(Account):
        pass
    @dataclass(frozen=True)
    class TestPosting(Posting[_T]):
        pass