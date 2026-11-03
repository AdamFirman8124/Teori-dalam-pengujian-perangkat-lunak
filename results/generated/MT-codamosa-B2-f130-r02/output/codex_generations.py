

# Generated at 2026-11-02 20:27:06.482361
# Unit test for function tri
def test_tri():
    # nonce:6002cdea
    assert module_0.tri(0) == [1]
    assert module_0.tri(1) == [1, 3]
    assert module_0.tri(2) == [1, 3, 2.0]
    assert module_0.tri(3) == [1, 3, 2.0, 8.0]
    assert module_0.tri(4) == [1, 3, 2.0, 8.0, 3.0]
    assert module_0.tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert module_0.tri(8) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0]
    assert module_0.tri(10) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0, 35.0, 6.0]

    result = module_0.tri(12)
    assert len(result) == 13
    # Even indices (i >= 2) hold i / 2 + 1
    for i in range(2, 13, 2):
        assert result[i] == i / 2 + 1
    # Odd indices follow the recurrence
    for i in range(3, 13, 2):
        assert result[i] == result[i - 1] + result[i - 2] + (i + 3) / 2
    # Entries beyond the seeds are floats
    assert all(isinstance(x, float) for x in module_0.tri(6)[2:])

    print("All tests passed!")


if __name__ == "__main__":
    test_tri()

# Generated at 2026-11-02 20:28:07.169823
# Unit test for function tri
def test_tri():
    # Base cases
    assert module_0.tri(0) == [1]
    assert module_0.tri(1) == [1, 3]

    # Even indices: i / 2 + 1 ; Odd indices: sum of previous two + (i + 3) / 2
    assert module_0.tri(2) == [1, 3, 2.0]
    assert module_0.tri(3) == [1, 3, 2.0, 8.0]
    assert module_0.tri(4) == [1, 3, 2.0, 8.0, 3.0]
    assert module_0.tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]

    # Longer sequence
    assert module_0.tri(8) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0]

    # Length checks
    assert len(module_0.tri(10)) == 11
    assert len(module_0.tri(20)) == 21

    # Negative n: loop never runs, returns initial list
    assert module_0.tri(-1) == [1, 3]
    assert module_0.tri(-5) == [1, 3]

    # Numeric equality holds regardless of int/float representation
    assert module_0.tri(3) == [1, 3, 2, 8]

    print("All tests passed!")

# Generated at 2026-11-02 20:29:27.726147
# Unit test for function tri
def test_tri():
# nonce:4a28cf66
    # Base case: n == 0 returns [1]
    assert module_0.tri(0) == [1]

    # n == 1 returns the initial list [1, 3]
    assert module_0.tri(1) == [1, 3]

    # Even index: i / 2 + 1
    assert module_0.tri(2) == [1, 3, 2.0]

    # Odd index: previous + second previous + (i + 3) / 2
    assert module_0.tri(3) == [1, 3, 2.0, 8.0]

    # Mix of even and odd computations
    assert module_0.tri(4) == [1, 3, 2.0, 8.0, 3.0]
    assert module_0.tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert module_0.tri(6) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0]
    assert module_0.tri(7) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0]

    # Length check: sequence contains n + 1 elements
    assert len(module_0.tri(10)) == 11

    # Values follow recurrence rules for a larger n
    result = module_0.tri(10)
    assert result[8] == 8 / 2 + 1          # even index
    assert result[9] == result[8] + result[7] + (9 + 3) / 2  # odd index
    assert result[10] == 10 / 2 + 1        # even index

    # All computed elements (index >= 2) should be floats due to true division
    for value in module_0.tri(9)[2:]:
        assert isinstance(value, float)

    print("All tests passed!")

# Generated at 2026-11-02 20:33:04.992798
# Unit test for function tri
def test_tri():
    assert module_0.tri(0) == [1]
    assert module_0.tri(1) == [1, 3]
    assert module_0.tri(2) == [1, 3, 2.0]
    assert module_0.tri(3) == [1, 3, 2.0, 8.0]
    assert module_0.tri(4) == [1, 3, 2.0, 8.0, 3.0]
    assert module_0.tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert module_0.tri(6) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0]
    assert module_0.tri(7) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0]
    assert module_0.tri(8) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0]
    assert module_0.tri(9) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0, 35.0]
    assert module_0.tri(10) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0, 35.0, 6.0]
    assert len(module_0.tri(20)) == 21
    # Even-indexed elements are i/2 + 1 (as float)
    result = module_0.tri(12)
    assert result[4] == 3.0
    assert result[6] == 4.0
    assert result[8] == 5.0
    assert result[10] == 6.0
    assert result[12] == 7.0