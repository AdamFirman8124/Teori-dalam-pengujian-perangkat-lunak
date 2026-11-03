

# Generated at 2026-11-03 00:02:48.162408
# Unit test for function get_odd_collatz
def test_get_odd_collatz():# n = 1: already odd, loop never runs
    assert module_0.get_odd_collatz(1) == [1]

    # n = 5: 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(5) == [1, 5]

    # n = 2: even start, 2 -> 1
    assert module_0.get_odd_collatz(2) == [1]

    # n = 6: even start, 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(6) == [1, 3, 5]

    # n = 3: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(3) == [1, 3, 5]

    # n = 14: 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

    # n = 7: 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

    # Result must always be sorted and contain only odd integers
    result = module_0.get_odd_collatz(27)
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)
    assert all(isinstance(x, int) for x in result)

    # First element of a non-empty result for odd n must be 1 (Collatz ends at 1)
    assert module_0.get_odd_collatz(27)[0] == 1
    assert module_0.get_odd_collatz(97)[0] == 1

# Generated at 2026-11-03 00:03:36.499306
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    # n = 1: sequence immediately ends, only [1]
    assert module_0.get_odd_collatz(1) == [1]

    # n = 2: even -> 1, odd numbers collected: [1]
    assert module_0.get_odd_collatz(2) == [1]

    # n = 3: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1; odds: [3, 5, 1] sorted
    assert module_0.get_odd_collatz(3) == [1, 3, 5]

    # n = 5: 5 -> 16 -> 8 -> 4 -> 2 -> 1; odds: [5, 1] sorted
    assert module_0.get_odd_collatz(5) == [1, 5]

    # n = 6: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1; odds sorted
    assert module_0.get_odd_collatz(6) == [1, 3, 5]

    # n = 7: 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

    # n = 14: 14 -> 7 -> ... same trajectory as 7 from that point
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

    # Result must always be sorted and contain only odd numbers
    result = module_0.get_odd_collatz(27)
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)
    assert result[0] == 1

# Generated at 2026-11-03 00:04:39.268920
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(5) == [1, 5]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(3) == [1, 3]
    assert module_0.get_odd_collatz(9) == [1, 5, 7, 13, 17, 11, 9] or module_0.get_odd_collatz(9) == sorted([1, 5, 7, 13, 17, 11, 9])

# Generated at 2026-11-03 00:06:26.686342
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    # n = 1: starts odd, loop never runs
    assert module_0.get_odd_collatz(1) == [1]

    # Even starting values begin with an empty list
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(12) == [1, 3, 5]
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

    # Odd starting values include n itself
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(5) == [1, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert module_0.get_odd_collatz(25) == [1, 5, 11, 13, 17, 19, 25, 29]

    # Same odd subsequence for n and 2*n
    assert module_0.get_odd_collatz(6) == module_0.get_odd_collatz(3)
    assert module_0.get_odd_collatz(28) == module_0.get_odd_collatz(14)

    # Structural checks: sorted ascending, all ints, no even numbers
    result = module_0.get_odd_collatz(97)
    assert result == sorted(result)
    assert all(isinstance(x, int) for x in result)
    assert all(x % 2 == 1 for x in result)
    assert result[0] == 1  # sequence always reaches 1