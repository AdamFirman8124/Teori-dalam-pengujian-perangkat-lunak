

# Generated at 2026-11-02 11:57:28.886142
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Recursive cases
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104
    assert module_0.fib4(11) == 200
    assert module_0.fib4(12) == 386
    assert module_0.fib4(13) == 744
    assert module_0.fib4(14) == 1434
    assert module_0.fib4(15) == 2764

# Generated at 2026-11-02 12:00:16.358610
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Computed cases (each element is sum of previous four)
    assert module_0.fib4(4) == 2    # 0 + 0 + 2 + 0
    assert module_0.fib4(5) == 4    # 0 + 2 + 0 + 2
    assert module_0.fib4(6) == 8    # 2 + 0 + 2 + 4
    assert module_0.fib4(7) == 14   # 0 + 2 + 4 + 8
    assert module_0.fib4(8) == 28   # 2 + 4 + 8 + 14
    assert module_0.fib4(9) == 54   # 4 + 8 + 14 + 28
    assert module_0.fib4(10) == 104 # 8 + 14 + 28 + 54

    # Larger value
    assert module_0.fib4(15) == 1454

    print("All fib4 tests passed!")


if __name__ == "__main__":
    test_fib4()

# Generated at 2026-11-02 12:03:03.735772
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Computed values
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104

    # Larger value to exercise the loop
    assert module_0.fib4(15) == 1942

    # Consistency: recurrence holds for n >= 4
    for n in range(4, 20):
        assert module_0.fib4(n) == module_0.fib4(n - 1) + module_0.fib4(n - 2) + module_0.fib4(n - 3) + module_0.fib4(n - 4)

    print("All tests passed!")


test_fib4()

# Generated at 2026-11-02 12:04:45.261578
# Unit test for function fib4

# Generated at 2026-11-02 12:05:34.781588
# Unit test for function fib4
def test_fib4():assert module_0.fib4(0) == 0

# Generated at 2026-11-02 12:06:07.335561
# Unit test for function fib4

# Generated at 2026-11-02 12:06:47.206401
# Unit test for function fib4
def test_fib4():assert module_0.fib4(0) == 0