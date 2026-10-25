

# Generated at 2026-10-24 04:47:26.775934
# Unit test for function intersperse

# Generated at 2026-10-24 04:47:29.189457
# Unit test for function intersperse

# Generated at 2026-10-24 04:47:31.742596
# Unit test for function intersperse

# Generated at 2026-10-24 04:47:34.269524
# Unit test for function intersperse

# Generated at 2026-10-24 04:47:36.676409
# Unit test for function intersperse

# Generated at 2026-10-24 04:47:39.088161
# Unit test for function intersperse

# Generated at 2026-10-24 04:47:41.499541
# Unit test for function intersperse

# Generated at 2026-10-24 04:47:45.413800
# Unit test for function intersperse
def test_intersperse():assert module_0.intersperse([], 0) == []

# Generated at 2026-10-24 04:47:50.946554
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([5, 10], -1) == [5, -1, 10,]

# Generated at 2026-10-24 04:47:54.813433
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2], 0) == [1, 0, 2]
    assert module_0.intersperse([1, 2, 3, 4], 9) == [1, 9, 2, 9, 3, 9, 4]
    assert module_0.intersperse([-1, -2, -3], 5) == [-1, 5, -2, 5, -3]