

# Generated at 2026-11-03 05:39:28.721905
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    assert module_0.get_odd_collatz(1) == [1]
    assert module_0.get_odd_collatz(2) == [1]
    assert module_0.get_odd_collatz(3) == [1, 3, 5]
    assert module_0.get_odd_collatz(5) == [1, 5]
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(7) == [1, 5, 7, 11, 13, 17]
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]
    assert module_0.get_odd_collatz(27) == [1, 3, 5, 7, 11, 13, 17, 19, 21, 23, 25, 31, 41, 47, 53, 61, 71, 83, 91, 101, 107, 113, 121, 151, 161, 181, 205, 241, 307, 331, 403, 487, 611, 763, 919, 1219, 1519, 2059, 2779, 4171, 6259, 9389, 14083, 21125, 31691, 47537, 71307, 106961, 160441, 240661, 360991, 541487, 812231, 1218347, 1827521, 2741281, 4111921, 6167881, 9251821, 13877731, 20816597, 31224895, 46837343, 70256015, 105384023, 158076035, 237114053, 355671080]

# Generated at 2026-11-03 05:41:26.789487
# Unit test for function get_odd_collatz
def test_get_odd_collatz():
    # n is odd and already 1: loop never runs
    assert module_0.get_odd_collatz(1) == [1]

    # n is odd: starts with n itself
    assert module_0.get_odd_collatz(5) == [1, 5]

    # n is even: starts empty, collects odd terms of the sequence
    assert module_0.get_odd_collatz(6) == [1, 3, 5]
    assert module_0.get_odd_collatz(2) == [1]

    # Larger even example (known Collatz sequence)
    assert module_0.get_odd_collatz(14) == [1, 5, 7, 11, 13, 17]

    # Result must be sorted, contain only odd integers
    result = module_0.get_odd_collatz(27)
    assert result == sorted(result)
    assert all(x % 2 == 1 for x in result)
    assert all(isinstance(x, int) for x in result)
    assert result[0] == 1  # every Collatz sequence ends at 1