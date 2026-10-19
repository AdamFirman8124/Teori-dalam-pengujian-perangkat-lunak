

# Generated at 2024-06-03 02:54:15.491286
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.zeitgeist import DateRange

# Generated at 2024-06-03 02:54:21.173210
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.zeitgeist import DateRange

# Generated at 2024-06-03 02:54:24.695980
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:54:28.119789
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:54:31.390476
# Unit test for method add of class Ledger
def test_Ledger_add():    account = Account("Cash")

# Generated at 2024-06-03 02:54:34.444084
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial Revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), direction=1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Create a DateRange for the test

# Generated at 2024-06-03 02:54:38.165072
# Unit test for method add of class Ledger
def test_Ledger_add():    account = Account("Cash")

# Generated at 2024-06-03 02:54:40.722551
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:54:45.393613
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00")))}

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial entry",
                    postings=[
                        Posting(account=Account("Cash"), amount=Amount(Decimal("100.00")), direction=1),
                        Posting(account=Account("Revenue"), amount=Amount(Decimal("100.00")), direction=-1),
                    ],
                )
            ]

    # Define the period
    period = DateRange(since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31))

    # Compile

# Generated at 2024-06-03 02:54:48.377726
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:54:57.983166
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), 1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), -1),
                    ],
                )
            ]

    # Create a DateRange for the test

# Generated at 2024-06-03 02:55:02.015784
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:55:04.990421
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:55:08.494043
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:55:12.042135
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    def mock_read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
            Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
        }

    def mock_read_journal_entries(period: DateRange) -> List[JournalEntry]:
        return [
            JournalEntry(
                date=period.since,
                description="Initial cash deposit",
                postings=[
                    Posting(account=Account("Cash"), amount=Amount(Decimal("1000.00")), direction=1),
                    Posting(account=Account("Revenue"), amount=Amount(Decimal("1000.00")), direction=-1),
                ],
            )
        ]

    # Define the period for the test

# Generated at 2024-06-03 02:55:15.176937
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:55:18.975120
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial Revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), True),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), False),
                    ],
                )
            ]

    # Create a DateRange for the test

# Generated at 2024-06-03 02:55:22.479668
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("Cash"): Balance(period.since, Quantity(Decimal(1000)))}

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial Entry",
                    postings=[
                        Posting(account=Account("Cash"), amount=Amount(Decimal(1000)), direction=1),
                        Posting(account=Account("Revenue"), amount=Amount(Decimal(1000)), direction=-1)
                    ]
                )
            ]

    # Create mock instances
    mock_read_initial_balances = MockReadInitialBalances()
    mock_read_journal_entries = MockReadJournalEntries()

    # Compile the general ledger program
    program = compile_general_ledger

# Generated at 2024-06-03 02:55:27.117790
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.zeitgeist import DateRange

# Generated at 2024-06-03 02:55:32.092608
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    def mock_read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
            Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
        }

    def mock_read_journal_entries(period: DateRange) -> List[JournalEntry]:
        return [
            JournalEntry(
                date=period.since,
                description="Initial cash deposit",
                postings=[
                    Posting(account=Account("Cash"), amount=Amount(Decimal("1000.00")), direction=1),
                    Posting(account=Account("Revenue"), amount=Amount(Decimal("1000.00")), direction=-1),
                ],
            )
        ]

    # Define the period for the test

# Generated at 2024-06-03 02:55:40.214753
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    def mock_read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
            Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
        }

    def mock_read_journal_entries(period: DateRange) -> List[JournalEntry]:
        return [
            JournalEntry(
                date=period.since,
                description="Initial revenue",
                postings=[
                    Posting(account=Account("Revenue"), amount=Amount(Decimal("500.00")), direction=1),
                    Posting(account=Account("Cash"), amount=Amount(Decimal("500.00")), direction=-1),
                ],
            )
        ]

    # Define the period for the test

# Generated at 2024-06-03 02:55:43.349221
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), 1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), -1),
                    ],
                )
            ]

    # Create a DateRange for the test

# Generated at 2024-06-03 02:55:46.609269
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal('1000.00')))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal('200.00')), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal('1200.00'))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 02:55:49.495530
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal(1000)))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal(200)), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal(1200))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 02:55:53.072088
# Unit test for method add of class Ledger
def test_Ledger_add():    account = Account("Cash")

# Generated at 2024-06-03 02:55:57.015831
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("Cash"): Balance(period.since, Quantity(Decimal(1000)))}

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial Entry",
                    postings=[
                        Posting(account=Account("Cash"), amount=Amount(Decimal(1000)), direction=1),
                        Posting(account=Account("Revenue"), amount=Amount(Decimal(1000)), direction=-1)
                    ]
                )
            ]

    # Create mock instances
    read_initial_balances = MockReadInitialBalances()
    read_journal_entries = MockReadJournalEntries()

    # Compile the general ledger program

# Generated at 2024-06-03 02:56:01.104430
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Define a mock DateRange
    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))

    # Define mock initial balances
    account1 = Account("Cash")
    account2 = Account("Revenue")
    initial_balances = {
        account1: Balance(datetime.date(2023, 1, 1), Quantity(Decimal(1000))),
        account2: Balance(datetime.date(2023, 1, 1), Quantity(Decimal(0))),
    }

    # Define mock journal entries
    journal_entry1 = JournalEntry(
        date=datetime.date(2023, 1, 2),
        description="Sale",
        postings=[
            Posting(account=account1, amount=Amount(Decimal(500)), direction=1),
            Posting(account=account2, amount=Amount(Decimal(500)), direction=-1),
        ],
    )
    journal_entries

# Generated at 2024-06-03 02:56:04.590540
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:56:08.288534
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:56:11.515588
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:56:35.488782
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:56:40.537438
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:56:43.493500
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:56:47.004712
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal(1000)))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal(200)), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal(1200))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 02:56:53.027165
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    def mock_read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
            Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
        }

    def mock_read_journal_entries(period: DateRange) -> List[JournalEntry]:
        return [
            JournalEntry(
                date=period.since,
                description="Initial revenue",
                postings=[
                    Posting(account=Account("Revenue"), amount=Amount(Decimal("500.00")), direction=1),
                    Posting(account=Account("Cash"), amount=Amount(Decimal("500.00")), direction=-1),
                ],
            )
        ]

    # Define the period

# Generated at 2024-06-03 02:56:56.902399
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal(1000)))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal(200)), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal(1200))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 02:57:00.126290
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), direction=1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 02:57:03.408566
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:57:07.143732
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal(1000)))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal(200)), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal(1200))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 02:57:11.586473
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), direction=1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 02:57:28.157066
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:57:31.886923
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial Revenue",
                    postings=[
                        Posting(account=Account("Revenue"), amount=Amount(Decimal("500.00")), direction=1),
                        Posting(account=Account("Cash"), amount=Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 02:57:35.315263
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:57:38.595397
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(account=Account("Revenue"), amount=Amount(Decimal("500.00")), direction=1),
                        Posting(account=Account("Cash"), amount=Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 02:57:42.972393
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal(1000)))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal(200)), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal(1200))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 02:57:46.743812
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal('1000.00')))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal('200.00')), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal('1200.00'))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 02:57:51.430329
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial Revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), direction=1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 02:57:55.089289
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:57:58.597212
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.zeitgeist import DateRange

# Generated at 2024-06-03 02:58:02.116371
# Unit test for method add of class Ledger
def test_Ledger_add():    account = Account("Cash")

# Generated at 2024-06-03 02:58:38.049227
# Unit test for method add of class Ledger
def test_Ledger_add():    account = Account("Cash")

# Generated at 2024-06-03 02:58:41.477729
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial Revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), 1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), -1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 02:58:50.943703
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount

# Generated at 2024-06-03 02:58:54.094374
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 02:58:57.444017
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00")))}

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial entry",
                    postings=[
                        Posting(account=Account("Cash"), amount=Amount(Decimal("1000.00")), direction=1),
                        Posting(account=Account("Equity"), amount=Amount(Decimal("1000.00")), direction=-1),
                    ],
                )
            ]

    # Define the period
    period = DateRange(since=datetime.date(2023, 1, 1), until=datetime.date(2023, 12, 31))



# Generated at 2024-06-03 02:59:01.520515
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal(1000)))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal(200)), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal(1200))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 02:59:05.730467
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {Account("Cash"): Balance(period.since, Quantity(Decimal(1000)))}

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial entry",
                    postings=[
                        Posting(account=Account("Cash"), amount=Amount(Decimal(1000)), direction=1),
                        Posting(account=Account("Revenue"), amount=Amount(Decimal(1000)), direction=-1),
                    ],
                )
            ]

    # Create mock instances
    mock_read_initial_balances = MockReadInitialBalances()
    mock_read_journal_entries = MockReadJournalEntries()

    # Compile the general ledger program
    program = compile_general_ledger

# Generated at 2024-06-03 02:59:09.553835
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 02:59:12.937872
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), direction=1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 02:59:16.029755
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 03:00:10.708632
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Define a mock DateRange
    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))

    # Define mock initial balances
    account1 = Account("Cash")
    account2 = Account("Revenue")
    initial_balances = {
        account1: Balance(datetime.date(2023, 1, 1), Quantity(Decimal(1000))),
        account2: Balance(datetime.date(2023, 1, 1), Quantity(Decimal(0))),
    }

    # Define mock journal entries
    journal_entry1 = JournalEntry(
        date=datetime.date(2023, 1, 2),
        description="Sale",
        postings=[
            Posting(account=account1, amount=Amount(Decimal(500)), direction=1),
            Posting(account=account2, amount=Amount(Decimal(500)), direction=-1),
        ],
    )
    journal_entries

# Generated at 2024-06-03 03:00:14.263543
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    def mock_read_initial_balances(period: DateRange) -> InitialBalances:
        return {
            Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
            Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
        }

    def mock_read_journal_entries(period: DateRange) -> List[JournalEntry]:
        return [
            JournalEntry(
                date=period.since,
                description="Initial revenue",
                postings=[
                    Posting(account=Account("Revenue"), amount=Amount(Decimal("500.00")), direction=1),
                    Posting(account=Account("Cash"), amount=Amount(Decimal("500.00")), direction=-1),
                ],
            )
        ]

    # Define the period

# Generated at 2024-06-03 03:00:18.522612
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(account=Account("Revenue"), amount=Amount(Decimal("500.00")), direction=1),
                        Posting(account=Account("Cash"), amount=Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 03:00:21.482978
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 03:00:24.648188
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Define a mock DateRange
    period = DateRange(datetime.date(2023, 1, 1), datetime.date(2023, 12, 31))

    # Define mock initial balances
    account1 = Account("Cash")
    account2 = Account("Revenue")
    initial_balances = {
        account1: Balance(datetime.date(2023, 1, 1), Quantity(Decimal(1000))),
        account2: Balance(datetime.date(2023, 1, 1), Quantity(Decimal(0))),
    }

    # Define mock journal entries
    journal_entry1 = JournalEntry(
        date=datetime.date(2023, 1, 15),
        description="Sale",
        postings=[
            Posting(account=account1, amount=Amount(Decimal(500)), direction=1),
            Posting(account=account2, amount=Amount(Decimal(500)), direction=-1),
        ],
    )
    journal_entries

# Generated at 2024-06-03 03:00:27.960889
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 03:00:36.938746
# Unit test for method add of class Ledger
def test_Ledger_add():    account = Account("Cash")

# Generated at 2024-06-03 03:00:40.392425
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal('1000.00')))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal('200.00')), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal('1200.00'))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 03:00:43.305075
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 03:00:46.538529
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 03:02:33.249097
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), direction=1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 03:02:37.171437
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.zeitgeist import DateRange

# Generated at 2024-06-03 03:02:41.603086
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(Account("Revenue"), Amount(Decimal("500.00")), direction=1),
                        Posting(Account("Cash"), Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Create a DateRange for the test

# Generated at 2024-06-03 03:02:47.074607
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():    # Mock implementations for ReadInitialBalances and ReadJournalEntries
    class MockReadInitialBalances:
        def __call__(self, period: DateRange) -> InitialBalances:
            return {
                Account("Cash"): Balance(period.since, Quantity(Decimal("1000.00"))),
                Account("Revenue"): Balance(period.since, Quantity(Decimal("0.00"))),
            }

    class MockReadJournalEntries:
        def __call__(self, period: DateRange) -> List[JournalEntry]:
            return [
                JournalEntry(
                    date=period.since,
                    description="Initial revenue",
                    postings=[
                        Posting(account=Account("Revenue"), amount=Amount(Decimal("500.00")), direction=1),
                        Posting(account=Account("Cash"), amount=Amount(Decimal("500.00")), direction=-1),
                    ],
                )
            ]

    # Define the period for the test

# Generated at 2024-06-03 03:02:50.712228
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 03:02:54.651001
# Unit test for method add of class Ledger
def test_Ledger_add():    # Create a mock account and initial balance
    account = Account(name="Cash")
    initial_balance = Balance(date=datetime.date(2023, 1, 1), value=Quantity(Decimal(1000)))

    # Create a ledger for the account
    ledger = Ledger(account=account, initial=initial_balance)

    # Create a mock posting
    journal_entry = JournalEntry(date=datetime.date(2023, 1, 2), description="Sale", postings=[])
    posting = Posting(account=account, amount=Amount(Decimal(200)), direction=1, journal=journal_entry)

    # Add the posting to the ledger
    ledger_entry = ledger.add(posting)

    # Assertions
    assert ledger_entry.ledger == ledger
    assert ledger_entry.posting == posting
    assert ledger_entry.balance == Quantity(Decimal(1200))
    assert ledger.entries[-1] == ledger_entry


# Generated at 2024-06-03 03:02:57.904559
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity

# Generated at 2024-06-03 03:03:01.316316
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 03:03:06.794235
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2024-06-03 03:03:11.059674
# Unit test for function build_general_ledger
def test_build_general_ledger():    from ..commons.numbers import Amount, Quantity