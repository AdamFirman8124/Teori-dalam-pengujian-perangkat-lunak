

# Generated at 2026-10-24 15:44:37.866531
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime -> y
    assert module_0.x_or_y(1, "x", "y") == "y"

    # primes -> x
    for n in [2, 3, 5, 7, 11, 13, 17, 19, 29]:
        assert module_0.x_or_y(n, "x", "y") == "x", f"failed for prime {n}"

    # composites -> y
    for n in [4, 6, 8, 9, 10, 12, 14, 15, 16, 25, 100]:
        assert module_0.x_or_y(n, "x", "y") == "y", f"failed for composite {n}"

    # x and y passed through unchanged
    assert module_0.x_or_y(5, 100, 200) == 100
    assert module_0.x_or_y(4, 100, 200) == 200

# Generated at 2026-10-24 15:44:39.299273
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime -> y
    assert module_0.x_or_y(1, "x", "y") == "y"

    # primes -> x
    for n in [2, 3, 5, 7, 11, 13, 17, 19, 29]:
        assert module_0.x_or_y(n, "x", "y") == "x", f"failed for prime {n}"

    # composites -> y
    for n in [4, 6, 8, 9, 10, 12, 14, 15, 16, 25, 100]:
        assert module_0.x_or_y(n, "x", "y") == "y", f"failed for composite {n}"

    # x and y passed through unchanged
    assert module_0.x_or_y(5, 100, 200) == 100
    assert module_0.x_or_y(4, 100, 200) == 200

# Generated at 2026-10-24 15:44:40.733155
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime -> y
    assert module_0.x_or_y(1, "x", "y") == "y"

    # primes -> x
    for n in [2, 3, 5, 7, 11, 13, 17, 19, 29]:
        assert module_0.x_or_y(n, "x", "y") == "x", f"failed for prime {n}"

    # composites -> y
    for n in [4, 6, 8, 9, 10, 12, 14, 15, 16, 25, 100]:
        assert module_0.x_or_y(n, "x", "y") == "y", f"failed for composite {n}"

    # x and y passed through unchanged
    assert module_0.x_or_y(5, 100, 200) == 100
    assert module_0.x_or_y(4, 100, 200) == 200

# Generated at 2026-10-24 15:44:51.606995
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime -> y
    assert module_0.x_or_y(1, "x", "y") == "y"

    # primes -> x
    for n in [2, 3, 5, 7, 11, 13, 17, 19, 29]:
        assert module_0.x_or_y(n, "x", "y") == "x", f"failed for prime {n}"

    # composites -> y
    for n in [4, 6, 8, 9, 10, 12, 14, 15, 16, 25, 100]:
        assert module_0.x_or_y(n, "x", "y") == "y", f"failed for composite {n}"

    # x and y passed through unchanged
    assert module_0.x_or_y(5, 100, 200) == 100
    assert module_0.x_or_y(4, 100, 200) == 200

# Generated at 2026-10-24 15:45:02.343776
# Unit test for function x_or_y
def test_x_or_y():
    # n == 1 is not prime -> y
    assert module_0.x_or_y(1, "x", "y") == "y"

    # primes -> x
    for n in [2, 3, 5, 7, 11, 13, 17, 19, 29]:
        assert module_0.x_or_y(n, "x", "y") == "x", f"failed for prime {n}"

    # composites -> y
    for n in [4, 6, 8, 9, 10, 12, 14, 15, 16, 25, 100]:
        assert module_0.x_or_y(n, "x", "y") == "y", f"failed for composite {n}"

    # x and y passed through unchanged
    assert module_0.x_or_y(5, 100, 200) == 100
    assert module_0.x_or_y(4, 100, 200) == 200