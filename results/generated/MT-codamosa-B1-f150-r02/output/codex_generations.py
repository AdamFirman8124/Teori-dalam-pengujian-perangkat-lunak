

# Generated at 2026-10-25 11:18:31.385294
# Unit test for function x_or_y
def test_x_or_y():
    assert module_0.x_or_y(1, "x", "y") == "y"
    assert module_0.x_or_y(2, "x", "y") == "x"
    assert module_0.x_or_y(3, "x", "y") == "x"
    assert module_0.x_or_y(4, "x", "y") == "y"
    assert module_0.x_or_y(9, 10, 20) == 20
    assert module_0.x_or_y(97, 10, 20) == 10

# Generated at 2026-10-25 11:18:52.581528
# Unit test for function x_or_y
def test_x_or_y():
    assert module_0.x_or_y(1, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(2, "prime", "not prime") == "prime"
    assert module_0.x_or_y(7, "x", "y") == "x"
    assert module_0.x_or_y(9, "x", "y") == "y"
    assert module_0.x_or_y(25, 10, 20) == 20
    assert module_0.x_or_y(29, 10, 20) == 10

# Generated at 2026-10-25 11:19:14.081026
# Unit test for function x_or_y
def test_x_or_y():
    assert module_0.x_or_y(1, "x", "y") == "y"   # 1 is not prime
    assert module_0.x_or_y(2, "x", "y") == "x"   # prime
    assert module_0.x_or_y(7, "x", "y") == "x"   # prime
    assert module_0.x_or_y(4, "x", "y") == "y"   # composite
    assert module_0.x_or_y(15, "x", "y") == "y"  # composite

# Generated at 2026-10-25 11:19:30.557179
# Unit test for function x_or_y
def test_x_or_y():
    # n is prime -> returns x
    assert module_0.x_or_y(7, "prime", "not") == "prime"
    assert module_0.x_or_y(2, "prime", "not") == "prime"
    assert module_0.x_or_y(3, "prime", "not") == "prime"
    assert module_0.x_or_y(13, 1, 0) == 1

    # n is composite -> returns y
    assert module_0.x_or_y(4, "prime", "not") == "not"
    assert module_0.x_or_y(9, "prime", "not") == "not"
    assert module_0.x_or_y(100, 1, 0) == 0

    # edge cases
    assert module_0.x_or_y(1, "prime", "not") == "not"   # 1 is not prime
    assert module_0.x_or_y(0, "prime", "not") == "prime"  # loop skipped, falls to else
    assert module_0.x_or_y(-5, "prime", "not") == "prime"  # negative: loop skipped

    print("All tests passed.")

test_x_or_y()

# Generated at 2026-10-25 11:19:41.250413
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 10, 20) == 20

    # primes return x
    for p in [2, 3, 5, 7, 11, 13, 17, 19]:
        assert module_0.x_or_y(p, "x", "y") == "x", f"failed for prime {p}"

    # composites return y
    for c in [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 25, 27]:
        assert module_0.x_or_y(c, "x", "y") == "y", f"failed for composite {c}"

    # different x, y values
    assert module_0.x_or_y(7, 100, 200) == 100
    assert module_0.x_or_y(8, 100, 200) == 200