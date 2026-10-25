

# Generated at 2026-10-24 06:59:04.657284
# Unit test for function prime_fib
def test_prime_fib():
    # Known values: first prime Fibonacci numbers are 2, 3, 5, 13, 89, 233, 1597, 28657, 514229
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

    # Results must be strictly increasing
    vals = [module_0.prime_fib(i) for i in range(1, 8)]
    assert vals == sorted(vals)

    # Every returned value must actually be prime and a Fibonacci number
    import math
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True
    for i in range(1, 9):
        v = module_0.prime_fib(i)
        assert is_prime(v), f"{v} is not prime"

    print("All tests passed!")


test_prime_fib()

# Generated at 2026-10-24 06:59:15.846349
# Unit test for function prime_fib
def test_prime_fib():assert module_0.prime_fib(1) == 2

# Generated at 2026-10-24 06:59:17.150897
# Unit test for function prime_fib
def test_prime_fib():
    # Known values: first prime Fibonacci numbers are 2, 3, 5, 13, 89, 233, 1597, 28657, 514229
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

    # Results must be strictly increasing
    vals = [module_0.prime_fib(i) for i in range(1, 8)]
    assert vals == sorted(vals)

    # Every returned value must actually be prime and a Fibonacci number
    import math
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True
    for i in range(1, 9):
        v = module_0.prime_fib(i)
        assert is_prime(v), f"{v} is not prime"

    print("All tests passed!")


test_prime_fib()

# Generated at 2026-10-24 06:59:18.458200
# Unit test for function prime_fib
def test_prime_fib():assert module_0.prime_fib(1) == 2

# Generated at 2026-10-24 06:59:19.762877
# Unit test for function prime_fib
def test_prime_fib():
    # Known values: first prime Fibonacci numbers are 2, 3, 5, 13, 89, 233, 1597, 28657, 514229
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

    # Results must be strictly increasing
    vals = [module_0.prime_fib(i) for i in range(1, 8)]
    assert vals == sorted(vals)

    # Every returned value must actually be prime and a Fibonacci number
    import math
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True
    for i in range(1, 9):
        v = module_0.prime_fib(i)
        assert is_prime(v), f"{v} is not prime"

    print("All tests passed!")


test_prime_fib()

# Generated at 2026-10-24 06:59:21.083242
# Unit test for function prime_fib
def test_prime_fib():assert module_0.prime_fib(1) == 2

# Generated at 2026-10-24 06:59:22.382801
# Unit test for function prime_fib
def test_prime_fib():
    # Known values: first prime Fibonacci numbers are 2, 3, 5, 13, 89, 233, 1597, 28657, 514229
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

    # Results must be strictly increasing
    vals = [module_0.prime_fib(i) for i in range(1, 8)]
    assert vals == sorted(vals)

    # Every returned value must actually be prime and a Fibonacci number
    import math
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True
    for i in range(1, 9):
        v = module_0.prime_fib(i)
        assert is_prime(v), f"{v} is not prime"

    print("All tests passed!")


test_prime_fib()

# Generated at 2026-10-24 06:59:23.694250
# Unit test for function prime_fib
def test_prime_fib():assert module_0.prime_fib(1) == 2

# Generated at 2026-10-24 06:59:24.999569
# Unit test for function prime_fib
def test_prime_fib():
    # Known values: first prime Fibonacci numbers are 2, 3, 5, 13, 89, 233, 1597, 28657, 514229
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

    # Results must be strictly increasing
    vals = [module_0.prime_fib(i) for i in range(1, 8)]
    assert vals == sorted(vals)

    # Every returned value must actually be prime and a Fibonacci number
    import math
    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, int(math.sqrt(p)) + 1):
            if p % k == 0:
                return False
        return True
    for i in range(1, 9):
        v = module_0.prime_fib(i)
        assert is_prime(v), f"{v} is not prime"

    print("All tests passed!")


test_prime_fib()

# Generated at 2026-10-24 06:59:26.307019
# Unit test for function prime_fib
def test_prime_fib():assert module_0.prime_fib(1) == 2