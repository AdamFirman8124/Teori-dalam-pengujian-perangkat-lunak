

# Generated at 2026-11-02 23:13:16.722880
# Unit test for function prime_fib
def test_prime_fib():
    # Test the first several prime Fibonacci numbers
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

    # Verify results are prime
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True

    for i in range(1, 11):
        assert is_prime(module_0.prime_fib(i)), f"module_0.prime_fib({i}) is not prime"

    # Verify results are Fibonacci numbers
    def is_fibonacci(x):
        a, b = 0, 1
        while a < x:
            a, b = b, a + b
        return a == x

    for i in range(1, 11):
        assert is_fibonacci(module_0.prime_fib(i)), f"module_0.prime_fib({i}) is not Fibonacci"

    # Results should be strictly increasing
    values = [module_0.prime_fib(i) for i in range(1, 8)]
    assert all(values[i] < values[i + 1] for i in range(len(values) - 1))

    print("All tests passed!")


if __name__ == "__main__":
    test_prime_fib()

# Generated at 2026-11-02 23:15:19.679992
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

# Generated at 2026-11-02 23:17:02.075524
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
    # Verify results are prime Fibonacci numbers
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True

    def fib_sequence(limit):
        f = [0, 1]
        while f[-1] < limit:
            f.append(f[-1] + f[-2])
        return f

    fibs = fib_sequence(500000)
    prime_fibs = [x for x in fibs if is_prime(x)]
    for i in range(1, 9):
        assert module_0.prime_fib(i) == prime_fibs[i - 1]

# Generated at 2026-11-02 23:19:34.551135
# Unit test for function prime_fib
def test_prime_fib():
    # Test the first few prime Fibonacci numbers
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

    # Verify results are prime
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True

    for i in range(1, 8):
        assert is_prime(module_0.prime_fib(i)), f"module_0.prime_fib({i}) is not prime"

    # Verify results appear in the Fibonacci sequence
    fibs = [0, 1]
    while len(fibs) < 60:
        fibs.append(fibs[-1] + fibs[-2])
    for i in range(1, 8):
        assert module_0.prime_fib(i) in fibs, f"module_0.prime_fib({i}) not in Fibonacci sequence"

    # Results should be strictly increasing
    values = [module_0.prime_fib(i) for i in range(1, 7)]
    assert values == sorted(values)
    assert len(set(values)) == len(values)

    print("All tests passed!")


if __name__ == "__main__":
    test_prime_fib()