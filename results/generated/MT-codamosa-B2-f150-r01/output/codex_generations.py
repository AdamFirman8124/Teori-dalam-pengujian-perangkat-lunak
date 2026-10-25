

# Generated at 2026-10-24 10:52:59.255652
# Unit test for function x_or_y
def test_x_or_y():
    # primes -> x
    for p in [2, 3, 5, 7, 11, 13, 97, 101]:
        assert module_0.x_or_y(p, "prime", "composite") == "prime", p

    # composites -> y
    for c in [4, 6, 8, 9, 10, 12, 100, 121]:
        assert module_0.x_or_y(c, "prime", "composite") == "composite", c

    # edge cases
    assert module_0.x_or_y(1, "prime", "composite") == "composite"  # 1 is not prime
    assert module_0.x_or_y(0, "prime", "composite") == "composite"  # 0 % i == 0 -> y
    assert module_0.x_or_y(-7, "prime", "composite") == "prime"     # range empty -> x

    # distinct values to prove which branch ran
    assert module_0.x_or_y(7, 1, 0) == 1
    assert module_0.x_or_y(8, 1, 0) == 0

# Generated at 2026-10-24 10:53:00.621286
# Unit test for function x_or_y
def test_x_or_y():
    # primes -> x
    for p in [2, 3, 5, 7, 11, 13, 97, 101]:
        assert module_0.x_or_y(p, "prime", "composite") == "prime", p

    # composites -> y
    for c in [4, 6, 8, 9, 10, 12, 100, 121]:
        assert module_0.x_or_y(c, "prime", "composite") == "composite", c

    # edge cases
    assert module_0.x_or_y(1, "prime", "composite") == "composite"  # 1 is not prime
    assert module_0.x_or_y(0, "prime", "composite") == "composite"  # 0 % i == 0 -> y
    assert module_0.x_or_y(-7, "prime", "composite") == "prime"     # range empty -> x

    # distinct values to prove which branch ran
    assert module_0.x_or_y(7, 1, 0) == 1
    assert module_0.x_or_y(8, 1, 0) == 0

# Generated at 2026-10-24 10:53:01.995362
# Unit test for function x_or_y
def test_x_or_y():
    # primes -> x
    for p in [2, 3, 5, 7, 11, 13, 97, 101]:
        assert module_0.x_or_y(p, "prime", "composite") == "prime", p

    # composites -> y
    for c in [4, 6, 8, 9, 10, 12, 100, 121]:
        assert module_0.x_or_y(c, "prime", "composite") == "composite", c

    # edge cases
    assert module_0.x_or_y(1, "prime", "composite") == "composite"  # 1 is not prime
    assert module_0.x_or_y(0, "prime", "composite") == "composite"  # 0 % i == 0 -> y
    assert module_0.x_or_y(-7, "prime", "composite") == "prime"     # range empty -> x

    # distinct values to prove which branch ran
    assert module_0.x_or_y(7, 1, 0) == 1
    assert module_0.x_or_y(8, 1, 0) == 0

# Generated at 2026-10-24 10:53:03.383662
# Unit test for function x_or_y
def test_x_or_y():
    # primes -> x
    for p in [2, 3, 5, 7, 11, 13, 97, 101]:
        assert module_0.x_or_y(p, "prime", "composite") == "prime", p

    # composites -> y
    for c in [4, 6, 8, 9, 10, 12, 100, 121]:
        assert module_0.x_or_y(c, "prime", "composite") == "composite", c

    # edge cases
    assert module_0.x_or_y(1, "prime", "composite") == "composite"  # 1 is not prime
    assert module_0.x_or_y(0, "prime", "composite") == "composite"  # 0 % i == 0 -> y
    assert module_0.x_or_y(-7, "prime", "composite") == "prime"     # range empty -> x

    # distinct values to prove which branch ran
    assert module_0.x_or_y(7, 1, 0) == 1
    assert module_0.x_or_y(8, 1, 0) == 0

# Generated at 2026-10-24 10:53:04.991256
# Unit test for function x_or_y
def test_x_or_y():
    # primes -> x
    for p in [2, 3, 5, 7, 11, 13, 97, 101]:
        assert module_0.x_or_y(p, "prime", "composite") == "prime", p

    # composites -> y
    for c in [4, 6, 8, 9, 10, 12, 100, 121]:
        assert module_0.x_or_y(c, "prime", "composite") == "composite", c

    # edge cases
    assert module_0.x_or_y(1, "prime", "composite") == "composite"  # 1 is not prime
    assert module_0.x_or_y(0, "prime", "composite") == "composite"  # 0 % i == 0 -> y
    assert module_0.x_or_y(-7, "prime", "composite") == "prime"     # range empty -> x

    # distinct values to prove which branch ran
    assert module_0.x_or_y(7, 1, 0) == 1
    assert module_0.x_or_y(8, 1, 0) == 0