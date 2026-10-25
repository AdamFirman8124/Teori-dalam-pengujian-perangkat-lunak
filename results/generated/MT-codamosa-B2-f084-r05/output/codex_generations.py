

# Generated at 2026-10-24 05:40:36.075093
# Unit test for function solve

# Generated at 2026-10-24 05:40:38.489592
# Unit test for function solve

# Generated at 2026-10-24 05:40:40.903784
# Unit test for function solve

# Generated at 2026-10-24 05:40:43.317533
# Unit test for function solve

# Generated at 2026-10-24 05:40:45.732244
# Unit test for function solve

# Generated at 2026-10-24 05:40:48.144640
# Unit test for function solve

# Generated at 2026-10-24 05:40:50.560642
# Unit test for function solve

# Generated at 2026-10-24 05:40:52.973398
# Unit test for function solve

# Generated at 2026-10-24 05:40:55.386985
# Unit test for function solve

# Generated at 2026-10-24 05:40:57.800334
# Unit test for function solve

# Generated at 2026-10-24 05:41:01.749077
# Unit test for function solve
def test_solve():assert module_0.solve(1234) == "1010"

# Generated at 2026-10-24 05:41:07.693866
# Unit test for function solve
def test_solve():
    # digit sum 0 -> binary "0"
    assert module_0.solve(0) == "0", "module_0.solve(0) failed"

    # single digit: digit sum == digit, binary of that digit
    assert module_0.solve(1) == "1", "module_0.solve(1) failed"
    assert module_0.solve(5) == "101", "module_0.solve(5) failed"
    assert module_0.solve(8) == "1000", "module_0.solve(8) failed"

    # classic examples
    assert module_0.solve(1000) == "1", "module_0.solve(1000) failed"   # 1+0+0+0 = 1
    assert module_0.solve(150) == "110", "module_0.solve(150) failed"   # 1+5+0 = 6 -> 110
    assert module_0.solve(147) == "1100", "module_0.solve(147) failed"  # 1+4+7 = 12 -> 1100

    # returns a string of only 0/1 characters
    result = module_0.solve(98765)
    assert isinstance(result, str), "solve must return a string"
    assert set(result) <= {"0", "1"}, "solve must return binary digits only"

    # digit sum is base-10, binary string matches that value
    n = 123456789
    expected = bin(sum(int(d) for d in str(n)))[2:]
    assert module_0.solve(n) == expected, "module_0.solve(123456789) failed"

    print("All tests passed!")


if __name__ == "__main__":
    test_solve()