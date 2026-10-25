

# Generated at 2026-10-25 04:22:59.932889
# Unit test for function intersperse

# Generated at 2026-10-25 04:23:02.347059
# Unit test for function intersperse

# Generated at 2026-10-25 04:23:04.761742
# Unit test for function intersperse

# Generated at 2026-10-25 04:23:07.178496
# Unit test for function intersperse

# Generated at 2026-10-25 04:23:09.592435
# Unit test for function intersperse

# Generated at 2026-10-25 04:23:12.007684
# Unit test for function intersperse

# Generated at 2026-10-25 04:23:14.424908
# Unit test for function intersperse

# Generated at 2026-10-25 04:23:19.381943
# Unit test for function intersperse
def test_intersperse():assert module_0.intersperse([], 0) == []

# Generated at 2026-10-25 04:23:20.723431
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([42], 0) == [42]
    assert module_0.intersperse([1, 2], 0) == [1, 0, 2]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

# Generated at 2026-10-25 04:23:22.055659
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([42], 0) == [42]
    assert module_0.intersperse([1, 2], 0) == [1, 0, 2]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]