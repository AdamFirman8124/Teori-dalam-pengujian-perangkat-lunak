

# Generated at 2026-11-03 03:55:09.321678
# Unit test for function fib4
def test_fib4():
    # Base cases: first four elements of the sequence
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Sequence: each element is the sum of the previous four
    assert module_0.fib4(4) == 2    # 0 + 2 + 0 + 0
    assert module_0.fib4(5) == 4    # 2 + 0 + 2 + 0
    assert module_0.fib4(6) == 8    # 4 + 2 + 0 + 2
    assert module_0.fib4(7) == 14   # 8 + 4 + 2 + 0
    assert module_0.fib4(8) == 28   # 14 + 8 + 4 + 2
    assert module_0.fib4(9) == 54   # 28 + 14 + 8 + 4
    assert module_0.fib4(10) == 104 # 54 + 28 + 14 + 8

    # Larger value to exercise the sliding window logic
    assert module_0.fib4(15) == 1786

    print("All tests passed!")

# Generated at 2026-11-03 03:58:18.975546
# Unit test for function fib4
def test_fib4():
    # Base cases
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Iterative cases
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 6
    assert module_0.fib4(7) == 12
    assert module_0.fib4(8) == 24
    assert module_0.fib4(9) == 44
    assert module_0.fib4(10) == 80

    # Larger value
    assert module_0.fib4(15) == 1040

# Generated at 2026-11-03 03:59:50.830929
# Unit test for function fib4
def test_fib4():
    # Base cases (n < 4)
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Iterative cases
    assert module_0.fib4(4) == 2
    assert module_0.fib4(5) == 4
    assert module_0.fib4(6) == 8
    assert module_0.fib4(7) == 14
    assert module_0.fib4(8) == 28
    assert module_0.fib4(9) == 54
    assert module_0.fib4(10) == 104

# Generated at 2026-11-03 04:03:00.843582
# Unit test for function fib4
def test_fib4():
    # Base cases (n < 4)
    assert module_0.fib4(0) == 0
    assert module_0.fib4(1) == 0
    assert module_0.fib4(2) == 2
    assert module_0.fib4(3) == 0

    # Iteratively computed cases
    assert module_0.fib4(4) == 2    # 0 + 0 + 2 + 0
    assert module_0.fib4(5) == 4    # 0 + 2 + 0 + 2
    assert module_0.fib4(6) == 8    # 2 + 0 + 2 + 4
    assert module_0.fib4(7) == 14   # 0 + 2 + 4 + 8
    assert module_0.fib4(8) == 28   # 2 + 4 + 8 + 14
    assert module_0.fib4(9) == 54   # 4 + 8 + 14 + 28
    assert module_0.fib4(10) == 104 # 8 + 14 + 28 + 54
    assert module_0.fib4(11) == 200 # 14 + 28 + 54 + 104
    assert module_0.fib4(12) == 386 # 28 + 54 + 104 + 200
    assert module_0.fib4(15) == 2872

    # Consistency check: each result is sum of previous four
    n = 20
    seq = [module_0.fib4(i) for i in range(4, n)]
    for i in range(4, len(seq)):
        assert seq[i] == seq[i-1] + seq[i-2] + seq[i-3] + seq[i-4]

    print("All fib4 tests passed!")


if __name__ == "__main__":
    test_fib4()