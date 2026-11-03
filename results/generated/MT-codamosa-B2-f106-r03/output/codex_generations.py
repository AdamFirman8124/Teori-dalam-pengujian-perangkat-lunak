

# Generated at 2026-11-02 12:55:08.097262
# Unit test for function f
def test_f():
    assert module_0.f(0) == []
    assert module_0.f(1) == [1]
    assert module_0.f(2) == [1, 2]
    assert module_0.f(3) == [1, 2, 6]
    assert module_0.f(4) == [1, 2, 6, 24]
    assert module_0.f(5) == [1, 2, 6, 24, 15]
    assert module_0.f(6) == [1, 2, 6, 24, 15, 720]
    assert module_0.f(7) == [1, 2, 6, 24, 15, 720, 28]
    # Even indices yield factorials, odd indices yield triangular sums
    result = module_0.f(8)
    assert result[1] == 2 * 1          # factorial of 2
    assert result[3] == 4 * 3 * 2 * 1  # factorial of 4
    assert result[5] == 6 * 5 * 4 * 3 * 2 * 1  # factorial of 6
    assert result[7] == 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1  # factorial of 8
    assert result[0] == 1              # sum 1..1
    assert result[2] == 1 + 2 + 3      # sum 1..3
    assert result[4] == 1 + 2 + 3 + 4 + 5  # sum 1..5

# Generated at 2026-11-02 12:56:05.466557
# Unit test for function f
def test_f():
    assert module_0.f(0) == []
    assert module_0.f(1) == [1]
    assert module_0.f(2) == [1, 2]
    assert module_0.f(3) == [1, 2, 6]
    assert module_0.f(4) == [1, 2, 6, 24]
    assert module_0.f(5) == [1, 2, 6, 24, 15]
    assert module_0.f(6) == [1, 2, 6, 24, 15, 720]
    assert module_0.f(7) == [1, 2, 6, 24, 15, 720, 28]
    assert all(isinstance(x, int) for x in module_0.f(10))
    # even indices are factorials, odd indices are triangular numbers
    result = module_0.f(8)
    assert result[0] == 1 and result[2] == 6 and result[4] == 15 and result[6] == 28
    assert result[1] == 2 and result[3] == 24 and result[5] == 720 and result[7] == 40320

# Generated at 2026-11-02 12:57:16.728951
# Unit test for function f
def test_f():
    # i odd -> sum of 1..i; i even -> factorial of i
    assert module_0.f(0) == []
    assert module_0.f(1) == [1]                       # sum 1
    assert module_0.f(2) == [1, 2]                    # 2! = 2
    assert module_0.f(3) == [1, 2, 6]                 # sum 1+2+3 = 6
    assert module_0.f(4) == [1, 2, 6, 24]             # 4! = 24
    assert module_0.f(5) == [1, 2, 6, 24, 15]         # sum 1+..+5 = 15
    assert module_0.f(6) == [1, 2, 6, 24, 15, 720]    # 6! = 720
    assert module_0.f(7) == [1, 2, 6, 24, 15, 720, 28]
    assert module_0.f(8) == [1, 2, 6, 24, 15, 720, 28, 40320]
    assert len(module_0.f(10)) == 10
    # verify element types are ints
    assert all(isinstance(v, int) for v in module_0.f(9))

# Generated at 2026-11-02 12:58:14.958449
# Unit test for function f
def test_f():
    # n = 0: empty range, empty list
    assert module_0.f(0) == []

    # n = 1: odd -> sum 1..1 = 1
    assert module_0.f(1) == [1]

    # n = 2: odd sum 1, even 2! = 2
    assert module_0.f(2) == [1, 2]

    # n = 3: odd sum 1+2+3 = 6
    assert module_0.f(3) == [1, 2, 6]

    # n = 5: mix of factorials (even) and sums (odd)
    assert module_0.f(5) == [1, 2, 6, 24, 15]

    # n = 6: 6! = 720
    assert module_0.f(6) == [1, 2, 6, 24, 15, 720]

    # n = 7: 7th element is sum 1..7 = 28
    assert module_0.f(7) == [1, 2, 6, 24, 15, 720, 28]

    # n = 8: 8! = 40320
    assert module_0.f(8) == [1, 2, 6, 24, 15, 720, 28, 40320]

    # Length check
    assert len(module_0.f(10)) == 10

    # Each even index (1-based) should be factorial, odd index should be triangular sum
    result = module_0.f(9)
    import math
    for i in range(1, 10):
        if i % 2 == 0:
            assert result[i - 1] == math.factorial(i)
        else:
            assert result[i - 1] == i * (i + 1) // 2

# Generated at 2026-11-02 12:59:36.479411
# Unit test for function f
def test_f():
    assert module_0.f(0) == []
    assert module_0.f(1) == [1]
    assert module_0.f(2) == [1, 2]
    assert module_0.f(3) == [1, 2, 6]
    assert module_0.f(5) == [1, 2, 6, 24, 15]
    assert module_0.f(6) == [1, 2, 6, 24, 15, 720]
    assert module_0.f(4) == [1, 2, 6, 24]