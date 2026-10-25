

# Generated at 2026-10-24 21:25:52.767214
# Unit test for function prime_fib

# Generated at 2026-10-24 21:25:55.185088
# Unit test for function prime_fib

# Generated at 2026-10-24 21:25:57.720079
# Unit test for function prime_fib

# Generated at 2026-10-24 21:26:02.291848
# Unit test for function prime_fib

# Generated at 2026-10-24 21:26:04.799285
# Unit test for function prime_fib

# Generated at 2026-10-24 21:26:07.315638
# Unit test for function prime_fib

# Generated at 2026-10-24 21:26:11.330136
# Unit test for function prime_fib

# Generated at 2026-10-24 21:26:13.824584
# Unit test for function prime_fib

# Generated at 2026-10-24 21:26:16.915386
# Unit test for function prime_fib

# Generated at 2026-10-24 21:26:35.211418
# Unit test for function prime_fib

# Generated at 2026-10-24 21:26:37.620210
# Unit test for function prime_fib

# Generated at 2026-10-24 21:26:51.754295
# Unit test for function prime_fib
def test_prime_fib():assert module_0.prime_fib(1) == 2

# Generated at 2026-10-24 21:27:00.719604
# Unit test for function prime_fib
def test_prime_fib():
    expected = [2, 3, 5, 13, 89, 233, 1597]

    for n, result in enumerate(expected, start=1):
        assert module_0.prime_fib(n) == result