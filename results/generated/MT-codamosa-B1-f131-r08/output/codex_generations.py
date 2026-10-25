

# Generated at 2026-10-24 04:21:41.659638
# Unit test for function digits

# Generated at 2026-10-24 04:21:44.074552
# Unit test for function digits

# Generated at 2026-10-24 04:21:46.486066
# Unit test for function digits

# Generated at 2026-10-24 04:21:48.902973
# Unit test for function digits

# Generated at 2026-10-24 04:21:52.409940
# Unit test for function digits
def test_digits():assert module_0.digits(135) == 15

# Generated at 2026-10-24 04:21:57.546616
# Unit test for function digits
def test_digits():
    # All odd digits -> product of them
    assert module_0.digits(5) == 5
    assert module_0.digits(135) == 15        # 1*3*5
    assert module_0.digits(111) == 1
    assert module_0.digits(999) == 729

    # Mixed digits -> product of odd digits only
    assert module_0.digits(1234) == 3        # only 1 and 3 are odd
    assert module_0.digits(2468) == 0        # no odd digits
    assert module_0.digits(305) == 15        # 3*5 (0 is skipped, even)

    # Edge cases
    assert module_0.digits(0) == 0           # 0 is even -> no odd digits
    assert module_0.digits(1) == 1           # smallest odd input
    assert module_0.digits(100) == 1         # single odd digit among evens

    print("All tests passed.")

test_digits()

# Generated at 2026-10-24 04:21:58.867436
# Unit test for function digits
def test_digits():
    # All odd digits -> product of them
    assert module_0.digits(5) == 5
    assert module_0.digits(135) == 15        # 1*3*5
    assert module_0.digits(111) == 1
    assert module_0.digits(999) == 729

    # Mixed digits -> product of odd digits only
    assert module_0.digits(1234) == 3        # only 1 and 3 are odd
    assert module_0.digits(2468) == 0        # no odd digits
    assert module_0.digits(305) == 15        # 3*5 (0 is skipped, even)

    # Edge cases
    assert module_0.digits(0) == 0           # 0 is even -> no odd digits
    assert module_0.digits(1) == 1           # smallest odd input
    assert module_0.digits(100) == 1         # single odd digit among evens

    print("All tests passed.")

test_digits()

# Generated at 2026-10-24 04:22:00.298246
# Unit test for function digits
def test_digits():
    # All odd digits -> product of them
    assert module_0.digits(5) == 5
    assert module_0.digits(135) == 15        # 1*3*5
    assert module_0.digits(111) == 1
    assert module_0.digits(999) == 729

    # Mixed digits -> product of odd digits only
    assert module_0.digits(1234) == 3        # only 1 and 3 are odd
    assert module_0.digits(2468) == 0        # no odd digits
    assert module_0.digits(305) == 15        # 3*5 (0 is skipped, even)

    # Edge cases
    assert module_0.digits(0) == 0           # 0 is even -> no odd digits
    assert module_0.digits(1) == 1           # smallest odd input
    assert module_0.digits(100) == 1         # single odd digit among evens

    print("All tests passed.")

test_digits()