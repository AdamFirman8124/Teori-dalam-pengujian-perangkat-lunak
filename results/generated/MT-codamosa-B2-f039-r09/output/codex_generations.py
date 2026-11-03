

# Generated at 2026-11-02 21:33:00.881544
# Unit test for function prime_fib
def test_prime_fib():
    # Known prime Fibonacci numbers: 2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437
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

    # Result must itself be a prime Fibonacci number: verify primality
    import math

    def is_prime_check(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True

    result = module_0.prime_fib(5)
    assert is_prime_check(result)

    # Results should be strictly increasing with n
    assert module_0.prime_fib(4) < module_0.prime_fib(5) < module_0.prime_fib(6)

    print("All tests passed!")


if __name__ == "__main__":
    test_prime_fib()

# Generated at 2026-11-02 21:34:55.793133
# Unit test for function prime_fib
def test_prime_fib():
    # Basic known prime Fibonacci numbers
    assert module_0.prime_fib(1) == 2
    assert module_0.prime_fib(2) == 3
    assert module_0.prime_fib(3) == 5
    assert module_0.prime_fib(4) == 13
    assert module_0.prime_fib(5) == 89
    assert module_0.prime_fib(6) == 233
    assert module_0.prime_fib(7) == 1597
    assert module_0.prime_fib(8) == 28657

    # Larger values
    assert module_0.prime_fib(9) == 514229
    assert module_0.prime_fib(10) == 433494437

    # Results should be increasing
    values = [module_0.prime_fib(i) for i in range(1, 8)]
    assert values == sorted(values)

    # All returned values must be prime
    import math

    def is_prime_check(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True

    for i in range(1, 9):
        assert is_prime_check(module_0.prime_fib(i))

    # All returned values must be Fibonacci numbers
    fib_set = {0, 1}
    a, b = 0, 1
    while b <= 433494437:
        a, b = b, a + b
        fib_set.add(a)
    for i in range(1, 11):
        assert module_0.prime_fib(i) in fib_set

    print("All tests passed!")


test_prime_fib()

# Generated at 2026-11-02 21:38:24.570586
# Unit test for function prime_fib
def test_prime_fib():
    # Test known prime Fibonacci numbers
    assert module_0.prime_fib(1) == 2, "1st prime Fibonacci should be 2"
    assert module_0.prime_fib(2) == 3, "2nd prime Fibonacci should be 3"
    assert module_0.prime_fib(3) == 5, "3rd prime Fibonacci should be 5"
    assert module_0.prime_fib(4) == 13, "4th prime Fibonacci should be 13"
    assert module_0.prime_fib(5) == 89, "5th prime Fibonacci should be 89"
    assert module_0.prime_fib(6) == 233, "6th prime Fibonacci should be 233"
    assert module_0.prime_fib(7) == 1597, "7th prime Fibonacci should be 1597"
    assert module_0.prime_fib(8) == 28657, "8th prime Fibonacci should be 28657"
    assert module_0.prime_fib(9) == 514229, "9th prime Fibonacci should be 514229"
    assert module_0.prime_fib(10) == 433494437, "10th prime Fibonacci should be 433494437"

    # Verify results are strictly increasing
    prev = 0
    for i in range(1, 8):
        val = module_0.prime_fib(i)
        assert val > prev, f"module_0.prime_fib({i}) should exceed previous prime"
        prev = val

    # Verify each returned value is prime
    import math

    def is_prime_check(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True

    for i in range(1, 11):
        assert is_prime_check(module_0.prime_fib(i)), f"module_0.prime_fib({i}) is not prime"

    print("All tests passed!")


if __name__ == "__main__":
    test_prime_fib()

# Generated at 2026-11-02 21:39:54.546517
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
    assert module_0.prime_fib(10) == 433494437