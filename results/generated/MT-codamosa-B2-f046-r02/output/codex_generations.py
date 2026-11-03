

# Generated at 2026-11-02 22:21:56.167649
# Unit test for function fib4
def test_fib4():
    # Test base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Test computed values
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104

    # Test larger value
    assert module_0.fib4(15) == 1490

    print("All test cases passed!")


if __name__ == "__main__":
    test_fib4()

# Generated at 2026-11-02 22:22:56.585668
# Unit test for function fib4
def test_fib4():
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(10) == 104
    assert module_0.fib4(12) == 386

# Generated at 2026-11-02 22:24:24.613409
# Unit test for function fib4
def test_fib4():
    # Base cases (n < 4)
    assert module_0.fib4(0) == 0, "module_0.fib4(0) should be 0"
    assert module_0.fib4(1) == 0, "module_0.fib4(1) should be 0"
    assert module_0.fib4(2) == 2, "module_0.fib4(2) should be 2"
    assert module_0.fib4(3) == 0, "module_0.fib4(3) should be 0"

    # Recursive cases: module_0.fib4(n) = module_0.fib4(n-1) + module_0.fib4(n-2) + module_0.fib4(n-3) + module_0.fib4(n-4)
    assert module_0.fib4(4) == 2, "module_0.fib4(4) should be 2"
    assert module_0.fib4(5) == 4, "module_0.fib4(5) should be 4"
    assert module_0.fib4(6) == 8, "module_0.fib4(6) should be 8"
    assert module_0.fib4(7) == 14, "module_0.fib4(7) should be 14"
    assert module_0.fib4(8) == 28, "module_0.fib4(8) should be 28"
    assert module_0.fib4(9) == 54, "module_0.fib4(9) should be 54"
    assert module_0.fib4(10) == 104, "module_0.fib4(10) should be 104"

    # Larger input to verify iterative computation
    assert module_0.fib4(11) == 200, "module_0.fib4(11) should be 200"
    assert module_0.fib4(12) == 386, "module_0.fib4(12) should be 386"
    assert module_0.fib4(15) == 2764, "module_0.fib4(15) should be 2764"

    print("All test_fib4 tests passed!")

# Generated at 2026-11-02 22:25:39.319469
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

# Generated at 2026-11-02 22:27:01.182860
# Unit test for function fib4
def test_fib4():
    # Test base cases (n < 4)
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Test computed values
    assert module_0.fib4(4) == 2   # 0 + 0 + 2 + 0
    assert module_0.fib4(5) == 4   # 0 + 2 + 0 + 2
    assert module_0.fib4(6) == 8   # 2 + 0 + 2 + 4
    assert module_0.fib4(7) == 14  # 0 + 2 + 4 + 8
    assert module_0.fib4(8) == 28  # 2 + 4 + 8 + 14

    # Test a larger value
    assert module_0.fib4(10) == 104
    assert module_0.fib4(15) == 5016

    print("All test cases passed!")


if __name__ == "__main__":
    test_fib4()