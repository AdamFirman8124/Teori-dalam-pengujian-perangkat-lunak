

# Generated at 2026-10-25 07:24:36.004746
# Unit test for function count_up_to

# Generated at 2026-10-25 07:24:38.421647
# Unit test for function count_up_to

# Generated at 2026-10-25 07:24:40.839490
# Unit test for function count_up_to

# Generated at 2026-10-25 07:24:43.253106
# Unit test for function count_up_to

# Generated at 2026-10-25 07:24:45.668696
# Unit test for function count_up_to

# Generated at 2026-10-25 07:24:48.086813
# Unit test for function count_up_to

# Generated at 2026-10-25 07:24:50.497797
# Unit test for function count_up_to

# Generated at 2026-10-25 07:24:52.911596
# Unit test for function count_up_to

# Generated at 2026-10-25 07:24:55.325788
# Unit test for function count_up_to

# Generated at 2026-10-25 07:24:57.741683
# Unit test for function count_up_to

# Generated at 2026-10-25 07:25:00.159886
# Unit test for function count_up_to

# Generated at 2026-10-25 07:25:04.447645
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert module_0.count_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Generated at 2026-10-25 07:25:09.804531
# Unit test for function count_up_to
def test_count_up_to():
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(11) == [2, 3, 5, 7]   # 11 excluded (range is exclusive of n)
    assert module_0.count_up_to(12) == [2, 3, 5, 7, 11]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    print("All tests passed!")

test_count_up_to()