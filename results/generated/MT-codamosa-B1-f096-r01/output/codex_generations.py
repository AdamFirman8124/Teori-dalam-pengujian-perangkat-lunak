

# Generated at 2026-10-24 20:25:52.653587
# Unit test for function count_up_to
def test_count_up_to():
    # strictly below n
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # n itself excluded even when prime
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(7) == [2, 3, 5]

    # boundaries: nothing below 2
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]

    # composites excluded
    assert module_0.count_up_to(5) == [2, 3]
    assert module_0.count_up_to(9) == [2, 3, 5, 7]

# Generated at 2026-10-24 20:25:53.985377
# Unit test for function count_up_to
def test_count_up_to():
    # strictly below n
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # n itself excluded even when prime
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(7) == [2, 3, 5]

    # boundaries: nothing below 2
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]

    # composites excluded
    assert module_0.count_up_to(5) == [2, 3]
    assert module_0.count_up_to(9) == [2, 3, 5, 7]

# Generated at 2026-10-24 20:25:55.414482
# Unit test for function count_up_to
def test_count_up_to():
    # strictly below n
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # n itself excluded even when prime
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(7) == [2, 3, 5]

    # boundaries: nothing below 2
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]

    # composites excluded
    assert module_0.count_up_to(5) == [2, 3]
    assert module_0.count_up_to(9) == [2, 3, 5, 7]

# Generated at 2026-10-24 20:25:56.747583
# Unit test for function count_up_to
def test_count_up_to():
    # strictly below n
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # n itself excluded even when prime
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(7) == [2, 3, 5]

    # boundaries: nothing below 2
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]

    # composites excluded
    assert module_0.count_up_to(5) == [2, 3]
    assert module_0.count_up_to(9) == [2, 3, 5, 7]

# Generated at 2026-10-24 20:25:58.179534
# Unit test for function count_up_to
def test_count_up_to():
    # strictly below n
    assert module_0.count_up_to(10) == [2, 3, 5, 7]
    assert module_0.count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # n itself excluded even when prime
    assert module_0.count_up_to(11) == [2, 3, 5, 7]
    assert module_0.count_up_to(7) == [2, 3, 5]

    # boundaries: nothing below 2
    assert module_0.count_up_to(0) == []
    assert module_0.count_up_to(1) == []
    assert module_0.count_up_to(2) == []
    assert module_0.count_up_to(3) == [2]

    # composites excluded
    assert module_0.count_up_to(5) == [2, 3]
    assert module_0.count_up_to(9) == [2, 3, 5, 7]