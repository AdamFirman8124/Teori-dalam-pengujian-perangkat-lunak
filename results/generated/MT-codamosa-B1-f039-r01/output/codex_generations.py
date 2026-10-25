

# Generated at 2026-10-25 01:51:06.271523
# Unit test for function prime_fib

# Generated at 2026-10-25 01:51:08.686843
# Unit test for function prime_fib

# Generated at 2026-10-25 01:51:11.103358
# Unit test for function prime_fib

# Generated at 2026-10-25 01:51:57.152538
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

    assert [module_0.prime_fib(n) for n in range(1, 11)] == expected

# Generated at 2026-10-25 01:52:13.938549
# Unit test for function prime_fib
def test_prime_fib():
    assert module_0.prime_fib(1) == 2
    assert module_0.prime_fib(2) == 3
    assert module_0.prime_fib(3) == 5
    assert module_0.prime_fib(4) == 13
    assert module_0.prime_fib(5) == 89
    assert module_0.prime_fib(6) == 233

# Generated at 2026-10-25 01:52:16.417065
# Unit test for function prime_fib

# Generated at 2026-10-25 01:52:18.875667
# Unit test for function prime_fib

# Generated at 2026-10-25 01:52:21.370924
# Unit test for function prime_fib

# Generated at 2026-10-25 01:53:11.300428
# Unit test for function prime_fib
def test_prime_fib():
    expected = [2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437]

    for n, value in enumerate(expected, start=1):
        assert module_0.prime_fib(n) == value