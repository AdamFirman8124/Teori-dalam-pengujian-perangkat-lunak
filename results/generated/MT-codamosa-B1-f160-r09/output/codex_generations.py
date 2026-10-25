

# Generated at 2026-10-24 13:49:05.702388
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:08.305660
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:10.891269
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:13.309942
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:15.991812
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:18.403020
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:20.816951
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:23.234468
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:25.663772
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:28.086437
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:30.496230
# Unit test for function do_algebra

# Generated at 2026-10-24 13:49:44.367073
# Unit test for function do_algebra
def test_do_algebra():result = module_0.do_algebra(["+", "*"], [2, 3, 4])

# Generated at 2026-10-24 13:49:55.218971
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9  # 2+3*4-5
    assert module_0.do_algebra(['+'], [2, 3]) == 5
    assert module_0.do_algebra(['-'], [10, 3]) == 7
    assert module_0.do_algebra(['*'], [4, 5]) == 20
    assert module_0.do_algebra(['//'], [7, 2]) == 3
    assert module_0.do_algebra(['**'], [2, 3]) == 8
    assert module_0.do_algebra([], [42]) == 42