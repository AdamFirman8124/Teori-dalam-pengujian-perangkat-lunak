

# Generated at 2026-11-03 02:16:01.677451
# Unit test for function get_odd_collatz
def test_get_odd_collatz():assert module_0.get_odd_collatz(1) == [1]

# Generated at 2026-11-03 02:17:14.178320
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    # Odd starting value: n itself is included
    assert module_0.get_odd_collatz(5) == [1, 5]

    # Even starting value: n itself is not included
    assert module_0.get_odd_collatz(6) == [1, 3, 5]

    # Edge case: n == 1
    assert module_0.get_odd_collatz(1) == [1]

    # Power of two: only reaches 1
    assert module_0.get_odd_collatz(8) == [1]

    # Even input with a longer sequence
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

    # Odd input with the same trajectory
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]

    # Another odd input
    assert module_0.get_odd_collatz(9) == [1, 5, 7, 9, 11, 13, 17]

    # Property checks over a range of inputs:
    # result is sorted, contains only odd numbers,
    # and includes n itself when n is odd.
    for start in range(1, 30):
        result = module_0.get_odd_collatz(start)
        assert result == sorted(result), f"not sorted for n={start}: {result}"
        assert all(x % 2 == 1 for x in result), f"even value in result for n={start}"
        assert result[-1] == 1, f"must always contain 1 for n={start}"
        if start % 2 == 1:
            assert start in result, f"odd start {start} missing from result"

    print("test_get_odd_collatz passed")


test_get_odd_collatz()

# Generated at 2026-11-03 02:18:26.471060
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(5) == [1, 5]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]
    assert module_0.get_odd_collatz(9) == [1, 5, 7, 9, 11, 13, 17]