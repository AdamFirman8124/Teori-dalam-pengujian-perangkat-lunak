

# Generated at 2026-10-25 03:45:17.901283
# Unit test for function prime_fib
def test_prime_fib():assert module_0.prime_fib(1) == 2

# Generated at 2026-10-25 03:45:34.388808
# Unit test for function prime_fib
def test_prime_fib():
    assert module_0.prime_fib(1) == 2
    assert module_0.prime_fib(2) == 3
    assert module_0.prime_fib(3) == 5
    assert module_0.prime_fib(4) == 13
    assert module_0.prime_fib(5) == 89
    assert module_0.prime_fib(6) == 233

# Generated at 2026-10-25 03:45:55.689516
# Unit test for function prime_fib
def test_prime_fib():assert module_0.prime_fib(1) == 2

# Generated at 2026-10-25 03:46:20.365195
# Unit test for function prime_fib
def test_prime_fib():
    expected = [2, 3, 5, 13, 89, 233, 1597, 28657]

    for n, value in enumerate(expected, start=1):
        assert module_0.prime_fib(n) == value

# Generated at 2026-10-25 03:46:48.728752
# Unit test for function prime_fib
def test_prime_fib():
    expected = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229]

    for n, value in enumerate(expected, start=1):
        assert module_0.prime_fib(n) == value