

# Generated at 2026-10-24 22:52:48.524786
# Unit test for function do_algebra

# Generated at 2026-10-24 22:52:50.940390
# Unit test for function do_algebra

# Generated at 2026-10-24 22:52:53.357473
# Unit test for function do_algebra

# Generated at 2026-10-24 22:52:55.774637
# Unit test for function do_algebra

# Generated at 2026-10-24 22:52:58.201999
# Unit test for function do_algebra

# Generated at 2026-10-24 22:53:00.618607
# Unit test for function do_algebra

# Generated at 2026-10-24 22:53:07.659176
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+", "-"], [10, 5, 3]) == 12
    assert module_0.do_algebra(["+", "*"], [2, 3, 4]) == 14  # Operator precedence
    assert module_0.do_algebra(["/"], [10, 2]) == 5
    assert module_0.do_algebra(["**"], [2, 3]) == 8
    assert module_0.do_algebra([], [7]) == 7

# Generated at 2026-10-24 22:53:15.471944
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+"], [2, 3]) == 5
    assert module_0.do_algebra(["-"], [10, 4]) == 6
    assert module_0.do_algebra(["*"], [3, 5]) == 15
    assert module_0.do_algebra(["/"], [20, 4]) == 5
    assert module_0.do_algebra(["+", "*", "-"], [2, 3, 4, 5]) == 9
    assert module_0.do_algebra([], [7]) == 7

# Generated at 2026-10-24 22:53:21.484257
# Unit test for function do_algebra
def test_do_algebra():
    assert module_0.do_algebra(["+"], [2, 3]) == 5
    assert module_0.do_algebra(["-"], [10, 4]) == 6
    assert module_0.do_algebra(["*"], [3, 5]) == 15
    assert module_0.do_algebra(["/"], [10, 2]) == 5
    assert module_0.do_algebra(["+", "*"], [2, 3, 4]) == 14  # 2 + (3 * 4)
    assert module_0.do_algebra(["**"], [2, 3]) == 8
    assert module_0.do_algebra([], [7]) == 7