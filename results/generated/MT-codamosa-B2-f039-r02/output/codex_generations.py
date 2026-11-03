

# Generated at 2026-11-03 00:04:24.859788
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
    assert module_0.prime_fib(9) == 514229
    assert module_0.prime_fib(10) == 433494437

    # Verify results are actually prime
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True

    for i in range(1, 11):
        assert is_prime(module_0.prime_fib(i)), f"module_0.prime_fib({i}) should be prime"

    # Verify ordering: results strictly increase
    values = [module_0.prime_fib(i) for i in range(1, 11)]
    assert all(a < b for a, b in zip(values, values[1:])), \
        "prime_fib results should be strictly increasing"

    print("All tests passed!")


if __name__ == "__main__":
    test_prime_fib()

# Generated at 2026-11-03 00:05:39.683904
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
# nonce:5917bf94

# Generated at 2026-11-03 00:07:25.490052
# Unit test for function prime_fib
def test_prime_fib():
# nonce:524a4f93
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

# Generated at 2026-11-03 00:11:38.291574
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
    assert module_0.prime_fib(9) == 514229
    assert module_0.prime_fib(10) == 433494437

# Generated at 2026-11-03 00:13:54.689508
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
    assert module_0.prime_fib(9) == 514229
    assert module_0.prime_fib(10) == 433494437