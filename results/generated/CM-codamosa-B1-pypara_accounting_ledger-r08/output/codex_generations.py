

# Generated at 2026-10-24 12:23:48.482804
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:23:50.897598
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:23:53.309932
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:23:55.722021
# Unit test for constructor of class LedgerEntry

# Generated at 2026-10-24 12:24:07.967111
# Unit test for constructor of class LedgerEntry
def test_LedgerEntry():import datetime

# Generated at 2026-10-24 12:24:27.032169
# Unit test for constructor of class LedgerEntry
def test_LedgerEntry():
    """
    Tests that LedgerEntry stores its constructor arguments correctly.
    """
    from unittest.mock import MagicMock

    ## Stub the ledger:
    ledger = MagicMock()

    ## Stub a counter-posting (opposite direction) and a journal containing it:
    counter_posting = MagicMock()
    counter_posting.direction = -1
    posting = MagicMock()
    posting.direction = 1
    posting.date = datetime.date(2023, 1, 15)
    posting.amount = Amount(Decimal("100.00"))
    posting.journal.description = "Test entry"
    posting.journal.postings = [posting, counter_posting]

    ## Construct the ledger entry:
    balance = Quantity(Decimal("150.00"))
    entry = LedgerEntry(ledger, posting, balance)

    ## Assert constructor arguments are stored as-is:
    assert entry.ledger is ledger
    assert entry.posting is posting
    assert entry.balance is balance

# Generated at 2026-10-24 12:24:29.452702
# Unit test for method __repr__ of class GeneralLedger

# Generated at 2026-10-24 12:24:31.871793
# Unit test for method __repr__ of class GeneralLedger

# Generated at 2026-10-24 12:24:34.281176
# Unit test for method __repr__ of class GeneralLedger

# Generated at 2026-10-24 12:24:36.694688
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:24:39.213923
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:24:41.630708
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:24:44.044302
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:24:46.458035
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:24:48.870875
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:24:51.284011
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:24:53.697591
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:24:56.111333
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:24:58.527455
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:25:00.938333
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:25:03.352039
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:25:29.161474
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:25:57.069411
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:25:59.485917
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:26:01.897119
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:26:04.314575
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:26:41.384335
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:26:43.799430
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:26:46.217794
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:26:48.628940
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:26:51.040694
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:26:53.453068
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:26:55.863931
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:26:58.276554
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:27:00.838362
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:27:03.251048
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:27:05.663593
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:27:43.612772
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:27:46.028433
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:27:48.441711
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:27:51.050863
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:27:53.563306
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:27:55.989145
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:27:58.402694
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:28:00.822385
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:28:03.235905
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:28:05.652743
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:28:08.067111
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:28:10.481568
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:28:12.895290
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:28:15.309288
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:28:17.723418
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:28:20.136445
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:28:22.547799
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:28:24.961211
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:28:27.375026
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:28:29.788629
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:28:32.201754
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:28:34.614732
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:28:37.027924
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 12:28:39.441701
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:28:41.854540
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:28:44.268106
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:28:46.685055
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:28:49.095238
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:28:51.508881
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:28:53.936006
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:28:56.347954
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:28:58.759911
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:29:01.184092
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:03.596253
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:06.008907
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:08.423668
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:10.837069
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:13.260683
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:15.701111
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:29:18.140946
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:29:20.568099
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:29:22.980723
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:25.394907
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:27.808937
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:30.224677
# Unit test for method add of class Ledger

# Generated at 2026-10-24 12:29:32.636192
# Unit test for method add of class Ledger

# Generated at 2026-10-24 12:29:35.049944
# Unit test for method add of class Ledger

# Generated at 2026-10-24 12:29:37.461427
# Unit test for method add of class Ledger

# Generated at 2026-10-24 12:29:39.873449
# Unit test for method add of class Ledger

# Generated at 2026-10-24 12:29:42.286702
# Unit test for method add of class Ledger

# Generated at 2026-10-24 12:29:44.701339
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:47.114509
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:49.539330
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:51.952959
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:54.366470
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:56.780300
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:29:59.194179
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:30:01.607795
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:30:47.333057
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:30:49.747405
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:30:52.359346
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:30:54.772792
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:30:57.186929
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:30:59.600149
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:31:02.014400
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 12:31:04.423836
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:31:06.833257
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:31:09.245426
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:31:11.657650
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:31:14.077717
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:31:16.490564
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:31:18.903889
# Unit test for method add of class Ledger

# Generated at 2026-10-24 12:31:21.315818
# Unit test for method add of class Ledger

# Generated at 2026-10-24 12:31:39.442164
# Unit test for method add of class Ledger
def test_Ledger_add():from decimal import Decimal

# Generated at 2026-10-24 12:31:42.082148
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:31:45.080637
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:32:02.892680
# Unit test for function build_general_ledger

# Generated at 2026-10-24 12:32:14.167457
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():
    read_initial_balances = Mock(return_value=sentinel.initial_balances)
    read_journal_entries = Mock(return_value=sentinel.journal_entries)

    with patch.object(
        __import__(
            compile_general_ledger_program.__module__,
            fromlist=["build_general_ledger"],
        ),
        "build_general_ledger",
        return_value=sentinel.general_ledger,
    ) as build_general_ledger_mock:
        program = module_0.compile_general_ledger_program(
            read_initial_balances,
            read_journal_entries,
        )

        result = program(sentinel.period)

    assert result is sentinel.general_ledger
    read_initial_balances.assert_called_once_with(sentinel.period)
    read_journal_entries.assert_called_once_with(sentinel.period)
    build_general_ledger_mock.assert_called_once_with(
        sentinel.period,
        sentinel.journal_entries,
        sentinel.initial_balances,
    )

# Generated at 2026-10-24 12:33:08.552504
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 12:33:11.462487
# Unit test for function compile_general_ledger_program