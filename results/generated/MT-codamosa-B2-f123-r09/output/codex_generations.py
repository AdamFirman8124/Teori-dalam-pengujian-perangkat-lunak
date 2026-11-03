

# Generated at 2026-11-02 09:23:29.448146
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    # n = 1: odd, loop doesn't run, returns [1]
    assert module_0.get_odd_collatz(1) == [1]

    # n = 2 (even): 2 -> 1.0, odd numbers: [1]
    assert module_0.get_odd_collatz(2) == [1]

    # n = 5 (odd): 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(5) == [1, 5]

    # n = 6 (even): 6 -> 3.0 -> 10 -> 5.0 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(6) == [1, 3, 5]

    # n = 7 (odd): 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> ... -> 1
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

    # n = 14 (even): 14 -> 7.0 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> ... -> 1
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

    # Larger input: verify structural properties (sorted, contains n, ends sequence at 1)
    result = module_0.get_odd_collatz(27)
    assert result == sorted(result)
    assert 27 in result
    assert result[0] == 1  # 1 is always in the sequence and is smallest

    # Result for even starting value should not include n itself
    result = module_0.get_odd_collatz(100)
    assert 100 not in result
    assert result == sorted(result)
    assert result[0] == 1

    # Duplicate-free check (each odd number appears once)
    result = module_0.get_odd_collatz(9)  # 9 -> 28 -> 14 -> 7 -> 22 -> 11 -> ... -> 1
    assert result == [1, 5, 7, 9, 11, 13, 17]
    assert len(result) == len(set(result))

    print("All tests passed!")

# Generated at 2026-11-02 09:28:24.231218
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    # n = 1: loop never runs, initial odd list [1] is returned
    assert module_0.get_odd_collatz(1) == [1]

    # n = 2: even start -> empty initial list, only 1 added
    assert module_0.get_odd_collatz(2) == [1]

    # n = 3: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(3) == [1, 3, 5]

    # n = 5: 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(5) == [1, 5]

    # n = 6: even start -> 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(6) == [1, 3, 5]

    # n = 7: 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> ... -> 1
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

    # n = 10: even start -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
    assert module_0.get_odd_collatz(10) == [1, 5]

    # n = 14: even start -> 14 -> 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> ... -> 1
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

    # Result must always be sorted ascending
    result = module_0.get_odd_collatz(27)
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)
    assert result[0] == 1

    # Large odd number
    assert module_0.get_odd_collatz(25) == [1, 5, 19, 25, 37, 47]

    # Edge case: n = 0 (even, loop never runs)
    assert module_0.get_odd_collatz(0) == []

    # Duplicates should not appear in the sorted output
    assert len(module_0.get_odd_collatz(9)) == len(set(module_0.get_odd_collatz(9)))

    print("All tests passed!")