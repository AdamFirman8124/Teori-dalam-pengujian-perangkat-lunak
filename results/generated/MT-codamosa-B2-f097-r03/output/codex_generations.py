

# Generated at 2026-10-24 12:02:22.673733
# Unit test for function multiply

# Generated at 2026-10-24 12:02:25.037701
# Unit test for function multiply

# Generated at 2026-10-24 12:02:27.451897
# Unit test for function multiply

# Generated at 2026-10-24 12:02:29.870429
# Unit test for function multiply

# Generated at 2026-10-24 12:02:32.287704
# Unit test for function multiply

# Generated at 2026-10-24 12:02:34.707121
# Unit test for function multiply

# Generated at 2026-10-24 12:02:37.132265
# Unit test for function multiply

# Generated at 2026-10-24 12:02:39.551089
# Unit test for function multiply

# Generated at 2026-10-24 12:02:41.968292
# Unit test for function multiply

# Generated at 2026-10-24 12:02:44.390278
# Unit test for function multiply

# Generated at 2026-10-24 12:02:56.161232
# Unit test for function multiply
def test_multiply():assert module_0.multiply(3, 4) == 12

# Generated at 2026-10-24 12:03:07.753907
# Unit test for function multiply
def test_multiply():
    # single digits
    assert module_0.multiply(3, 4) == 12
    assert module_0.multiply(9, 9) == 81

    # multi-digit: only the last digit counts
    assert module_0.multiply(13, 4) == 12
    assert module_0.multiply(123, 47) == 21

    # zeros
    assert module_0.multiply(0, 5) == 0
    assert module_0.multiply(10, 3) == 0
    assert module_0.multiply(-10, 3) == 0

    # negatives: Python's % is non-negative, so -13 % 10 == 7
    assert module_0.multiply(-13, 4) == 28
    assert module_0.multiply(-3, -4) == 42


@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0),
    (5, 5, 25),
    (25, 35, 25),
    (-25, 35, 25),
    (-7, 7, 21),
])
def test_multiply_parametrized(a, b, expected):
    assert module_0.multiply(a, b) == expected