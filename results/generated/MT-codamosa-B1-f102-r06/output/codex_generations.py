

# Generated at 2026-10-24 06:33:22.126390
# Unit test for function choose_num

# Generated at 2026-10-24 06:33:24.542154
# Unit test for function choose_num

# Generated at 2026-10-24 06:33:26.957230
# Unit test for function choose_num

# Generated at 2026-10-24 06:33:29.372211
# Unit test for function choose_num

# Generated at 2026-10-24 06:33:31.785527
# Unit test for function choose_num

# Generated at 2026-10-24 06:33:34.201180
# Unit test for function choose_num

# Generated at 2026-10-24 06:33:36.619035
# Unit test for function choose_num

# Generated at 2026-10-24 06:33:39.033251
# Unit test for function choose_num

# Generated at 2026-10-24 06:34:10.917992
# Unit test for function choose_num
def test_choose_num():assert module_0.choose_num(12, 15) == 14

# Generated at 2026-10-24 06:34:12.269880
# Unit test for function choose_num
def test_choose_num():
    assert module_0.choose_num(12, 82) == 82
    assert module_0.choose_num(13, 12) == -1  # x > y
    assert module_0.choose_num(12, 12) == 12  # single even
    assert module_0.choose_num(13, 13) == -1  # single odd
    assert module_0.choose_num(13, 14) == 14  # y even
    assert module_0.choose_num(13, 15) == 14  # y odd, x < y
    assert module_0.choose_num(1, 2) == 2
    assert module_0.choose_num(1, 1) == -1
    assert module_0.choose_num(2, 3) == 2
    assert module_0.choose_num(3, 5) == 4

# Generated at 2026-10-24 06:34:13.624223
# Unit test for function choose_num
def test_choose_num():
    assert module_0.choose_num(12, 82) == 82
    assert module_0.choose_num(13, 12) == -1  # x > y
    assert module_0.choose_num(12, 12) == 12  # single even
    assert module_0.choose_num(13, 13) == -1  # single odd
    assert module_0.choose_num(13, 14) == 14  # y even
    assert module_0.choose_num(13, 15) == 14  # y odd, x < y
    assert module_0.choose_num(1, 2) == 2
    assert module_0.choose_num(1, 1) == -1
    assert module_0.choose_num(2, 3) == 2
    assert module_0.choose_num(3, 5) == 4