

# Generated at 2026-11-03 01:02:27.341909
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    # n = 1 (odd, loop never runs)
    assert module_0.get_odd_collatz(1) == [1]
    # n = 2 (even start, immediately halves to 1)
    assert module_0.get_odd_collatz(2) == [1]
    # n = 3 (odd start)
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    # n = 5 (odd start)
    assert module_0.get_odd_collatz(5) == [1, 5]
    # n = 6 (even start)
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    # n = 7 (odd start, longer sequence)
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    # n = 14 (even start, reaches same sequence as 7)
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]
    # n = 27 (large case: verify sorted, all odd, starts at 1)
    result = module_0.get_odd_collatz(27)
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)
    assert result[0] == 1
    assert 27 in result

test_get_odd_collatz()

# Generated at 2026-11-03 01:04:49.862233
# Unit test for function get_odd_collatz

# Generated at 2026-11-03 01:06:54.174892
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(5) == [1, 5]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

# Generated at 2026-11-03 01:10:40.331491
# Unit test for function get_odd_collatz

# Generated at 2026-11-03 01:12:12.808139
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    # n = 1: starts odd, loop never runs
    assert module_0.get_odd_collatz(1) == [1]

    # n = 5 (odd start): 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(5) == [1, 5]

    # n = 6 (even start): 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(6) == [1, 3, 5]

    # n = 14 (even start): 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

    # n = 7 (odd start): 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

    # Result is always sorted ascending
    result = module_0.get_odd_collatz(27)
    assert result == sorted(result)
    assert result[0] == 1
# nonce:aaff59ee