

# Generated at 2026-11-02 22:30:31.164009
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
    assert module_0.fib4(15) == 1296

    # Consistency check: recurrence relation holds
    for n in range(10, 20):
        assert module_0.fib4(n) == module_0.fib4(n - 1) + module_0.fib4(n - 2) + module_0.fib4(n - 3) + module_0.fib4(n - 4)

# Generated at 2026-11-02 22:31:59.044546
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Recursive cases
    assert module_0.fib4(4) == 2    # 0 + 2 + 0 + 0
    assert module_0.fib4(5) == 4    # 2 + 0 + 2 + 0
    assert module_0.fib4(6) == 8    # 4 + 2 + 0 + 2
    assert module_0.fib4(7) == 14   # 8 + 4 + 2 + 0
    assert module_0.fib4(8) == 28   # 14 + 8 + 4 + 2
    assert module_0.fib4(9) == 54   # 28 + 14 + 8 + 4
    assert module_0.fib4(10) == 104 # 54 + 28 + 14 + 8

    # Larger value
    assert module_0.fib4(15) == 1736

    # Verify recurrence relation holds for a range of values
    def fib4_reference(n):
        seq = [0, 0, 2, 0]
        for i in range(4, n + 1):
            seq.append(seq[i-1] + seq[i-2] + seq[i-3] + seq[i-4])
        return seq[n]

    for n in range(4, 20):
        assert module_0.fib4(n) == fib4_reference(n), f"Mismatch at n={n}"

    print("All tests passed!")


if __name__ == "__main__":
    test_fib4()

# Generated at 2026-11-02 22:33:43.689717
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Computed cases
    assert module_0.fib4(4) == 2    # 0 + 0 + 2 + 0
    assert module_0.fib4(5) == 4    # 0 + 2 + 0 + 2
    assert module_0.fib4(6) == 8    # 2 + 0 + 2 + 4
    assert module_0.fib4(7) == 14   # 0 + 2 + 4 + 8
    assert module_0.fib4(8) == 28   # 2 + 4 + 8 + 14
    assert module_0.fib4(9) == 56   # 4 + 8 + 14 + 28
    assert module_0.fib4(10) == 108 # 8 + 14 + 28 + 56

    # Larger values
    assert module_0.fib4(15) == 2080
    assert module_0.fib4(20) == 73080
    assert module_0.fib4(25) == 2470696

    print("All test_fib4 tests passed!")


test_fib4()

# Generated at 2026-11-02 22:34:52.891929
# Unit test for function fib4
def test_fib4():
    # Base cases (n < 4)
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Computed cases
    assert module_0.fib4(4) == 2    # 0 + 0 + 2 + 0
    assert module_0.fib4(5) == 4    # 2 + 0 + 2 + 0
    assert module_0.fib4(6) == 8    # 4 + 2 + 0 + 2
    assert module_0.fib4(7) == 14   # 8 + 4 + 2 + 0
    assert module_0.fib4(8) == 28   # 14 + 8 + 4 + 2
    assert module_0.fib4(9) == 54   # 28 + 14 + 8 + 4
    assert module_0.fib4(10) == 104 # 54 + 28 + 14 + 8

    # Larger value to verify iterative accumulation
    assert module_0.fib4(15) == 19960

    # Consistency check: each value equals sum of previous four
    def ref(n):
        seq = [0, 0, 2, 0]
        if n < 4:
            return seq[n]
        for _ in range(4, n + 1):
            seq.append(sum(seq[-4:]))
            seq.pop(0)
        return seq[-1]

    for i in range(0, 30):
        assert module_0.fib4(i) == ref(i), f"module_0.fib4({i}) mismatch"

# Generated at 2026-11-02 22:36:13.878849
# Unit test for function fib4
def test_fib4():
    # Base cases: first four elements of the sequence
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Computed values: each is the sum of the previous four
    assert module_0.fib4(4) == 2    # 0 + 0 + 2 + 0
    assert module_0.fib4(5) == 4    # 0 + 2 + 0 + 2
    assert module_0.fib4(6) == 8    # 2 + 0 + 2 + 4
    assert module_0.fib4(7) == 14   # 0 + 2 + 4 + 8
    assert module_0.fib4(8) == 28   # 2 + 4 + 8 + 14
    assert module_0.fib4(9) == 54   # 4 + 8 + 14 + 28
    assert module_0.fib4(10) == 104 # 8 + 14 + 28 + 54

    # Larger value to exercise the loop and rolling window
    assert module_0.fib4(15) == 1490

    print("All tests passed!")


test_fib4()