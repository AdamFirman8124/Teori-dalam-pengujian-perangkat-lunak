

# Generated at 2026-10-25 03:07:09.338289
# Unit test for function f

# Generated at 2026-10-25 03:07:11.753495
# Unit test for function f

# Generated at 2026-10-25 03:07:14.168588
# Unit test for function f

# Generated at 2026-10-25 03:07:16.582662
# Unit test for function f

# Generated at 2026-10-25 03:07:19.000033
# Unit test for function f

# Generated at 2026-10-25 03:07:21.413610
# Unit test for function f

# Generated at 2026-10-25 03:07:23.828195
# Unit test for function f

# Generated at 2026-10-25 03:07:26.242763
# Unit test for function f

# Generated at 2026-10-25 03:07:36.235385
# Unit test for function f
def test_f():assert module_0.f(1) == [1]

# Generated at 2026-10-25 03:07:37.577705
# Unit test for function f
def test_f():
    # Empty input
    assert module_0.f(0) == []

    # i=1 (odd): sum 1..1 = 1
    assert module_0.f(1) == [1]

    # i=2 (even): 2! = 2
    assert module_0.f(2) == [1, 2]

    # i=3 (odd): sum 1..3 = 6
    assert module_0.f(3) == [1, 2, 6]

    # i=4 (even): 4! = 24
    assert module_0.f(4) == [1, 2, 6, 24]

    # i=5 (odd): sum 1..5 = 15
    assert module_0.f(5) == [1, 2, 6, 24, 15]

    # i=6 (even): 6! = 720
    assert module_0.f(6) == [1, 2, 6, 24, 15, 720]

    # Each element matches: odd -> i*(i+1)//2, even -> i!
    for n in range(1, 11):
        result = module_0.f(n)
        assert len(result) == n
        for i, val in enumerate(result, start=1):
            expected = (i * (i + 1)) // 2 if i % 2 == 1 else 1
            if i % 2 == 0:
                for j in range(2, i + 1):
                    expected *= j
            assert val == expected, f"position {i}: got {val}, expected {expected}"

    print("All tests passed.")

test_f()

# Generated at 2026-10-25 03:07:38.907180
# Unit test for function f
def test_f():
    # Empty input
    assert module_0.f(0) == []

    # i=1 (odd): sum 1..1 = 1
    assert module_0.f(1) == [1]

    # i=2 (even): 2! = 2
    assert module_0.f(2) == [1, 2]

    # i=3 (odd): sum 1..3 = 6
    assert module_0.f(3) == [1, 2, 6]

    # i=4 (even): 4! = 24
    assert module_0.f(4) == [1, 2, 6, 24]

    # i=5 (odd): sum 1..5 = 15
    assert module_0.f(5) == [1, 2, 6, 24, 15]

    # i=6 (even): 6! = 720
    assert module_0.f(6) == [1, 2, 6, 24, 15, 720]

    # Each element matches: odd -> i*(i+1)//2, even -> i!
    for n in range(1, 11):
        result = module_0.f(n)
        assert len(result) == n
        for i, val in enumerate(result, start=1):
            expected = (i * (i + 1)) // 2 if i % 2 == 1 else 1
            if i % 2 == 0:
                for j in range(2, i + 1):
                    expected *= j
            assert val == expected, f"position {i}: got {val}, expected {expected}"

    print("All tests passed.")

test_f()