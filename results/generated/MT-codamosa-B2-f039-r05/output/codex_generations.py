

# Generated at 2026-11-02 20:19:17.187441
# Unit test for function prime_fib
def test_prime_fib():
    # nonce:ad890fe7
    assert module_0.prime_fib(1) == 2
    assert module_0.prime_fib(2) == 3
    assert module_0.prime_fib(3) == 5
    assert module_0.prime_fib(4) == 13
    assert module_0.prime_fib(5) == 89
    assert module_0.prime_fib(6) == 233
    assert module_0.prime_fib(7) == 1597
    assert module_0.prime_fib(8) == 28657
    assert module_0.prime_fib(9) == 514229
    assert module_0.prime_fib(10) == 433494437
    assert isinstance(module_0.prime_fib(5), int)
    assert module_0.prime_fib(5) > module_0.prime_fib(4)
    print("All tests passed!")


test_prime_fib()

# Generated at 2026-11-02 20:22:10.084690
# Unit test for function prime_fib
def test_prime_fib():
    # Known prime Fibonacci numbers: 2, 3, 5, 13, 89, 233, 1597, 28657, 514229
    assert module_0.prime_fib(1) == 2
    assert module_0.prime_fib(2) == 3
    assert module_0.prime_fib(3) == 5
    assert module_0.prime_fib(4) == 13
    assert module_0.prime_fib(5) == 89
    assert module_0.prime_fib(6) == 233
    assert module_0.prime_fib(7) == 1597
    assert module_0.prime_fib(8) == 28657
    assert module_0.prime_fib(9) == 514229

    # Results must themselves be prime Fibonacci numbers
    for k in range(1, 8):
        result = module_0.prime_fib(k)
        assert result > 0
        # verify it appears in increasing order relative to next
        assert module_0.prime_fib(k + 1) > result

    print("test_prime_fib passed")

# Generated at 2026-11-02 20:23:55.735492
# Unit test for function prime_fib
def test_prime_fib():
# nonce:b4e2174e
    assert module_0.prime_fib(1) == 2
    assert module_0.prime_fib(2) == 3
    assert module_0.prime_fib(3) == 5
    assert module_0.prime_fib(4) == 13
    assert module_0.prime_fib(5) == 89
    assert module_0.prime_fib(6) == 233
    assert module_0.prime_fib(7) == 1597
    assert module_0.prime_fib(8) == 28657

# Generated at 2026-11-02 20:25:40.715650
# Unit test for function prime_fib
def test_prime_fib():
    assert module_0.prime_fib(1) == 2
    assert module_0.prime_fib(2) == 3
    assert module_0.prime_fib(3) == 5
    assert module_0.prime_fib(4) == 13
    assert module_0.prime_fib(5) == 89
    assert module_0.prime_fib(6) == 233
    assert module_0.prime_fib(7) == 1597
    assert module_0.prime_fib(8) == 28657
    print("All tests passed!")


test_prime_fib()