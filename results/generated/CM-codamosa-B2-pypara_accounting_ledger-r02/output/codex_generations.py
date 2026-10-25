

# Generated at 2026-10-24 19:21:00.826071
# Unit test for method __eq__ of class Ledger
def test_Ledger___eq__():
    """
    Ensures ``__eq__`` compares account, initial balance, and entries.

    ``Ledger`` is a dataclass, so its generated ``__eq__`` compares all three
    fields â including ``entries``, which has ``init=False`` but is still part
    of the generated comparison.
    """
    from decimal import Decimal

    account = Account(...)

    ## Two ledgers with no entries and identical initial balances: equal.

# Generated at 2026-10-24 19:21:03.364453
# Unit test for constructor of class GeneralLedger

# Generated at 2026-10-24 19:21:05.779637
# Unit test for constructor of class GeneralLedger

# Generated at 2026-10-24 19:21:08.198718
# Unit test for constructor of class GeneralLedger

# Generated at 2026-10-24 19:21:10.619045
# Unit test for method __repr__ of class Ledger

# Generated at 2026-10-24 19:21:13.036778
# Unit test for method __repr__ of class Ledger

# Generated at 2026-10-24 19:21:15.453151
# Unit test for method __repr__ of class Ledger

# Generated at 2026-10-24 19:21:17.872642
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:21:20.288623
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:21:22.706633
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:21:25.124360
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:21:27.540428
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:21:30.089746
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:00.604648
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:03.018607
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:05.436104
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:07.852301
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:22:10.268613
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:22:12.685357
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:22:15.102092
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:22:17.518207
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:22:19.934554
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:22:22.355225
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:22:24.771591
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:22:27.187891
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:22:29.609926
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:32.030494
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:34.448869
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:36.864058
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:39.282983
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:41.700234
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:22:44.120030
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:22:46.745778
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:23:20.890426
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:23:23.308127
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:23:25.730903
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:23:28.148882
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:23:30.561453
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:23:32.980478
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:23:35.398001
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:23:37.816549
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:23:40.232367
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:23:42.647574
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:23:45.064819
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:23:47.483146
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:23:50.080015
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:24:07.290076
# Unit test for function compile_general_ledger_program
def test_compile_general_ledger_program():from unittest.mock import Mock


# Generated at 2026-10-24 19:24:28.602178
# Unit test for method __call__ of class GeneralLedgerProgram
def test_GeneralLedgerProgram___call__():
    period = Mock(name="period")
    initial_balances = Mock(name="initial_balances")
    journal_entries = Mock(name="journal_entries")
    expected = Mock(name="general_ledger")

    read_initial_balances = Mock(return_value=initial_balances)
    read_journal_entries = Mock(return_value=journal_entries)
    module = sys.modules[compile_general_ledger_program.__module__]


# Generated at 2026-10-24 19:24:31.024622
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:24:33.440651
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:24:35.872256
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:24:38.301418
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:24:40.718465
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:24:43.137342
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:24:45.555549
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:24:47.971607
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:24:50.386798
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:24:52.801828
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:24:55.220756
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:24:57.640706
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:25:00.061423
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:25:02.473986
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:25:04.892388
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:25:07.308646
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:25:09.728568
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:25:12.146271
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:25:14.565683
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:25:16.982083
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:25:19.399380
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:25:21.818379
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:25:24.234867
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:25:26.654869
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:25:29.070766
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:25:31.489754
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:25:33.906852
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:25:36.322478
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:25:38.738270
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:25:41.154683
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:25:56.091563
# Unit test for method __call__ of class ReadInitialBalances
def test_ReadInitialBalances___call__():
    from unittest.mock import Mock

    ## ReadInitialBalances is a Protocol: it cannot be instantiated, so the
    ## contract is exercised through a concrete implementation fed to the program.
    period = DateRange(datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
    account = Mock(spec=Account)
    balance = Balance(period.since, Quantity(Decimal("100")))

    seen = []

    def read_initial_balances(p):
        seen.append(p)
        return {account: balance}

    def read_journal_entries(p):
        return []

    program = compile_general_ledger_program(read_initial_balances, read_journal_entries)
    ledger = program(period)

    ## Called exactly once, with the exact period object passed in.
    assert seen == [period]

    ## Returned balances became the ledgers' opening balances.
    assert ledger.period is period
    assert ledger.ledgers[account].initial is balance
    assert ledger.ledgers[account].entries == []

# Generated at 2026-10-24 19:26:13.829059
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:16.361014
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:18.779094
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:21.194443
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:23.622405
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:26.038859
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:28.456069
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:30.872422
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:33.290491
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:35.710830
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:26:38.125255
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:26:40.549575
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:26:42.965054
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:26:45.380803
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:26:47.800388
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:26:50.215849
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:26:52.632097
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:26:55.050260
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:26:57.467760
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:26:59.885711
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:27:02.305215
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:27:04.723780
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:27:07.151786
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:27:09.570283
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:27:11.987461
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:27:35.263852
# Unit test for method add of class Ledger
def test_Ledger_add():from datetime import date

# Generated at 2026-10-24 19:27:37.688109
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:27:40.214287
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:27:42.631752
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:27:45.049946
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:27:47.467047
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:27:49.885111
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:27:52.302737
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:28:20.714604
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:28:23.130032
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:28:25.547182
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:28:27.966953
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:28:30.387548
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:28:32.804635
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:28:35.220799
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:28:37.640367
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:28:40.058599
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:28:42.476649
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:28:44.897039
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:28:47.311457
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:28:49.727169
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:28:52.143136
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:28:54.559792
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:28:56.976188
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:28:59.393491
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:29:01.809840
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:29:04.224660
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:29:06.641834
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:29:09.061694
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:11.477653
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:13.894596
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:16.311398
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:18.729072
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:21.144299
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:23.561736
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:25.977458
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:28.393935
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:30.810274
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:33.231053
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:35.646339
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:29:38.062082
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:29:40.477847
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:29:42.895087
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:29:45.310080
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:29:47.728069
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:29:50.143840
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:29:52.574754
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:29:54.988626
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:29:57.406748
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:29:59.826597
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:30:02.242741
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:30:04.660006
# Unit test for function compile_general_ledger_program

# Generated at 2026-10-24 19:30:07.076591
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:30:09.492358
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:30:11.907849
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:30:14.325524
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:30:16.744498
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:30:19.159809
# Unit test for function build_general_ledger

# Generated at 2026-10-24 19:30:21.577713
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:30:23.995590
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:30:26.412886
# Unit test for method __call__ of class ReadInitialBalances

# Generated at 2026-10-24 19:30:28.828667
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:30:31.248705
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:30:33.665526
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:30:36.081116
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:30:38.499814
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:30:40.920269
# Unit test for method __call__ of class GeneralLedgerProgram

# Generated at 2026-10-24 19:30:43.333650
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:30:45.752756
# Unit test for method add of class Ledger

# Generated at 2026-10-24 19:30:48.171060
# Unit test for method add of class Ledger