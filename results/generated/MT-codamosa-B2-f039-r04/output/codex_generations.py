

# Generated at 2026-10-25 02:35:21.309966
# Unit test for function prime_fib
def test_prime_fib():
    expected = [2, 3, 5, 13, 89, 233, 1597]

    for n, expected_value in enumerate(expected, start=1):
        assert module_0.prime_fib(n) == expected_value

# Generated at 2026-10-25 02:35:45.345798
# Unit test for function prime_fib
def test_prime_fib():
    expected = [
        2,
        3,
        5,
        13,
        89,
        233,
        1597,
        28657,
        514229,
        433494437,
    ]

    for n, prime in enumerate(expected, start=1):
        assert module_0.prime_fib(n) == prime

# Generated at 2026-10-25 02:36:08.848603
# Unit test for function prime_fib
def test_prime_fib():
    expected = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437]

    for n, value in enumerate(expected, start=1):
        assert module_0.prime_fib(n) == value

# Generated at 2026-10-25 02:36:22.353563
# Unit test for function prime_fib
def test_prime_fib():
    expected = {
        1: 2,
        2: 3,
        3: 5,
        4: 13,
        5: 89,
        6: 233,
        7: 1597,
    }

    for n, result in expected.items():
        assert module_0.prime_fib(n) == result

# Generated at 2026-10-25 02:36:38.830701
# Unit test for function prime_fib
def test_prime_fib():
    assert module_0.prime_fib(1) == 2
    assert module_0.prime_fib(2) == 3
    assert module_0.prime_fib(3) == 5
    assert module_0.prime_fib(4) == 13
    assert module_0.prime_fib(5) == 89
    assert module_0.prime_fib(6) == 233