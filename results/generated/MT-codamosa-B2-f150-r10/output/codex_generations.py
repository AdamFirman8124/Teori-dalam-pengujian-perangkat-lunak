

# Generated at 2026-10-24 21:44:41.484699
# Unit test for function x_or_y

# Generated at 2026-10-24 21:44:43.900930
# Unit test for function x_or_y

# Generated at 2026-10-24 21:44:46.318684
# Unit test for function x_or_y

# Generated at 2026-10-24 21:44:48.885167
# Unit test for function x_or_y

# Generated at 2026-10-24 21:44:51.305166
# Unit test for function x_or_y

# Generated at 2026-10-24 21:44:53.720072
# Unit test for function x_or_y

# Generated at 2026-10-24 21:44:56.142205
# Unit test for function x_or_y

# Generated at 2026-10-24 21:44:58.558625
# Unit test for function x_or_y

# Generated at 2026-10-24 21:45:03.004803
# Unit test for function x_or_y
def test_x_or_y():assert module_0.x_or_y(1, 10, 20) == 20

# Generated at 2026-10-24 21:45:04.333944
# Unit test for function x_or_y
def test_x_or_y():
    # Primes -> x
    assert module_0.x_or_y(2, "prime", "not") == "prime"
    assert module_0.x_or_y(3, "prime", "not") == "prime"
    assert module_0.x_or_y(7, "prime", "not") == "prime"
    assert module_0.x_or_y(13, "prime", "not") == "prime"
    # Composites -> y
    assert module_0.x_or_y(4, "prime", "not") == "not"
    assert module_0.x_or_y(9, "prime", "not") == "not"
    assert module_0.x_or_y(15, "prime", "not") == "not"
    # Edge cases
    assert module_0.x_or_y(1, "prime", "not") == "not"   # 1 is not prime
    print("All tests passed.")

test_x_or_y()

# Generated at 2026-10-24 21:45:05.663807
# Unit test for function x_or_y
def test_x_or_y():
    # Primes -> x
    assert module_0.x_or_y(2, "prime", "not") == "prime"
    assert module_0.x_or_y(3, "prime", "not") == "prime"
    assert module_0.x_or_y(7, "prime", "not") == "prime"
    assert module_0.x_or_y(13, "prime", "not") == "prime"
    # Composites -> y
    assert module_0.x_or_y(4, "prime", "not") == "not"
    assert module_0.x_or_y(9, "prime", "not") == "not"
    assert module_0.x_or_y(15, "prime", "not") == "not"
    # Edge cases
    assert module_0.x_or_y(1, "prime", "not") == "not"   # 1 is not prime
    print("All tests passed.")

test_x_or_y()