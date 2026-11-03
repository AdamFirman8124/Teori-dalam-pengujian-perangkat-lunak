

# Generated at 2026-11-02 20:10:13.531535
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y (1 is not prime)
    assert module_0.x_or_y(1, 'x', 'y') == 'y'
    # Prime numbers return x
    assert module_0.x_or_y(2, 'x', 'y') == 'x'
    assert module_0.x_or_y(3, 'x', 'y') == 'x'
    assert module_0.x_or_y(5, 'x', 'y') == 'x'
    assert module_0.x_or_y(7, 'x', 'y') == 'x'
    assert module_0.x_or_y(13, 'x', 'y') == 'x'
    assert module_0.x_or_y(97, 'x', 'y') == 'x'
    # Composite numbers return y
    assert module_0.x_or_y(4, 'x', 'y') == 'y'
    assert module_0.x_or_y(6, 'x', 'y') == 'y'
    assert module_0.x_or_y(9, 'x', 'y') == 'y'
    assert module_0.x_or_y(10, 'x', 'y') == 'y'
    assert module_0.x_or_y(15, 'x', 'y') == 'y'
    # Works with arbitrary return values
    assert module_0.x_or_y(11, 100, 200) == 100
    assert module_0.x_or_y(12, 100, 200) == 200

# Generated at 2026-11-02 20:12:18.211785
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 8, 5) == 5
    # n == 2 is prime (loop body never runs), returns x
    assert module_0.x_or_y(2, 8, 5) == 8
    # prime numbers return x
    assert module_0.x_or_y(3, 33, 521) == 33
    assert module_0.x_or_y(7, 34, 12) == 34
    assert module_0.x_or_y(13, 100, 200) == 100
    # composite numbers return y
    assert module_0.x_or_y(15, 8, 5) == 5
    assert module_0.x_or_y(4, 20, 6) == 6
    assert module_0.x_or_y(9, 5, 11) == 11
    assert module_0.x_or_y(100, 7, 9) == 9
    print("All tests passed!")

test_x_or_y()

# Generated at 2026-11-02 20:13:42.260884
# Unit test for function x_or_y
def test_x_or_y():
    # nonce:9d29ed7d
    # n == 1 -> returns y (1 is not prime)
    assert module_0.x_or_y(1, 10, 20) == 20
    # n == 2 -> smallest prime, loop doesn't execute, returns x
    assert module_0.x_or_y(2, 10, 20) == 10
    # n == 3 -> prime, returns x
    assert module_0.x_or_y(3, 10, 20) == 10
    # n == 4 -> composite, returns y
    assert module_0.x_or_y(4, 10, 20) == 20
    # n == 5 -> prime, returns x
    assert module_0.x_or_y(5, 10, 20) == 10
    # n == 6 -> composite, returns y
    assert module_0.x_or_y(6, 10, 20) == 20
    # n == 7 -> prime, returns x
    assert module_0.x_or_y(7, 10, 20) == 10
    # n == 9 -> composite (perfect square), returns y
    assert module_0.x_or_y(9, 10, 20) == 20
    # n == 13 -> prime, returns x
    assert module_0.x_or_y(13, 10, 20) == 10
    # n == 15 -> composite, returns y
    assert module_0.x_or_y(15, 10, 20) == 20
    # larger prime -> returns x
    assert module_0.x_or_y(97, "prime", "composite") == "prime"
    # larger composite -> returns y
    assert module_0.x_or_y(100, "prime", "composite") == "composite"
    # distinct x and y values to avoid accidental passes
    assert module_0.x_or_y(29, "yes", "no") == "yes"
    assert module_0.x_or_y(49, "yes", "no") == "no"

# Generated at 2026-11-02 20:15:49.156689
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y
    assert module_0.x_or_y(1, 'prime', 'not_prime') == 'not_prime'
    # n == 2 is prime, returns x
    assert module_0.x_or_y(2, 'prime', 'not_prime') == 'prime'
    # small primes return x
    assert module_0.x_or_y(3, 'prime', 'not_prime') == 'prime'
    assert module_0.x_or_y(5, 'prime', 'not_prime') == 'prime'
    assert module_0.x_or_y(7, 'prime', 'not_prime') == 'prime'
    assert module_0.x_or_y(13, 'prime', 'not_prime') == 'prime'
    assert module_0.x_or_y(97, 'prime', 'not_prime') == 'prime'
    # composite numbers return y
    assert module_0.x_or_y(4, 'prime', 'not_prime') == 'not_prime'
    assert module_0.x_or_y(6, 'prime', 'not_prime') == 'not_prime'
    assert module_0.x_or_y(9, 'prime', 'not_prime') == 'not_prime'
    assert module_0.x_or_y(15, 'prime', 'not_prime') == 'not_prime'
    assert module_0.x_or_y(100, 'prime', 'not_prime') == 'not_prime'
    # works with numeric arguments too
    assert module_0.x_or_y(7, 10, 20) == 10
    assert module_0.x_or_y(8, 10, 20) == 20
    # edge cases: 0 and negatives fall through to else, returning x
    assert module_0.x_or_y(0, 'prime', 'not_prime') == 'prime'
    assert module_0.x_or_y(-5, 'prime', 'not_prime') == 'prime'

test_x_or_y()

# Generated at 2026-11-02 20:17:54.066263
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 returns y (1 is not prime)
    assert module_0.x_or_y(1, 10, 20) == 20

    # Prime numbers return x
    assert module_0.x_or_y(2, 10, 20) == 10
    assert module_0.x_or_y(3, 10, 20) == 10
    assert module_0.x_or_y(5, 10, 20) == 10
    assert module_0.x_or_y(7, 10, 20) == 10
    assert module_0.x_or_y(11, 10, 20) == 10
    assert module_0.x_or_y(13, 10, 20) == 10
    assert module_0.x_or_y(97, 10, 20) == 10

    # Composite numbers return y
    assert module_0.x_or_y(4, 10, 20) == 20
    assert module_0.x_or_y(6, 10, 20) == 20
    assert module_0.x_or_y(9, 10, 20) == 20
    assert module_0.x_or_y(15, 10, 20) == 20
    assert module_0.x_or_y(100, 10, 20) == 20

    # Works with arbitrary value types
    assert module_0.x_or_y(7, "yes", "no") == "yes"
    assert module_0.x_or_y(8, "yes", "no") == "no"
    assert module_0.x_or_y(1, "yes", "no") == "no"