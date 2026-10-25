

# Generated at 2026-10-25 01:32:32.271820
# Unit test for function x_or_y
def test_x_or_y():
    assert module_0.x_or_y(1, "x", "y") == "y"
    assert module_0.x_or_y(2, "x", "y") == "x"   # prime
    assert module_0.x_or_y(7, "x", "y") == "x"   # prime
    assert module_0.x_or_y(4, "x", "y") == "y"   # composite
    assert module_0.x_or_y(49, "x", "y") == "y"  # composite square

# Generated at 2026-10-25 01:32:37.081153
# Unit test for function x_or_y
def test_x_or_y():
    assert module_0.x_or_y(1, 10, 20) == 20   # 1 is not prime
    assert module_0.x_or_y(2, 10, 20) == 10   # prime
    assert module_0.x_or_y(7, "x", "y") == "x"
    assert module_0.x_or_y(4, "x", "y") == "y"  # composite
    assert module_0.x_or_y(15, True, False) is False

# Generated at 2026-10-25 01:32:42.201277
# Unit test for function x_or_y
def test_x_or_y():
    assert module_0.x_or_y(1, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(2, "prime", "not prime") == "prime"
    assert module_0.x_or_y(7, "prime", "not prime") == "prime"
    assert module_0.x_or_y(9, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(15, 10, 20) == 20
    assert module_0.x_or_y(17, 10, 20) == 10


test_x_or_y()
print("All tests passed.")

# Generated at 2026-10-25 01:32:47.628110
# Unit test for function x_or_y
def test_x_or_y():
    assert module_0.x_or_y(1, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(2, "prime", "not prime") == "prime"
    assert module_0.x_or_y(7, "prime", "not prime") == "prime"
    assert module_0.x_or_y(9, "prime", "not prime") == "not prime"
    assert module_0.x_or_y(12, 10, 20) == 20
    assert module_0.x_or_y(13, 10, 20) == 10

# Generated at 2026-10-25 01:32:53.157241
# Unit test for function x_or_y
def test_x_or_y():
    assert module_0.x_or_y(1, "x", "y") == "y"
    assert module_0.x_or_y(2, "x", "y") == "x"
    assert module_0.x_or_y(7, 10, 20) == 10
    assert module_0.x_or_y(9, 10, 20) == 20
    assert module_0.x_or_y(25, True, False) is False