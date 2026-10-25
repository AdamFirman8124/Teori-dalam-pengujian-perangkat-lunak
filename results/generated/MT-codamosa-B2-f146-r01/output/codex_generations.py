

# Generated at 2026-10-24 21:08:29.319008
# Unit test for function specialFilter

# Generated at 2026-10-24 21:08:31.732920
# Unit test for function specialFilter

# Generated at 2026-10-24 21:08:34.150618
# Unit test for function specialFilter

# Generated at 2026-10-24 21:08:36.569369
# Unit test for function specialFilter

# Generated at 2026-10-24 21:08:43.086265
# Unit test for function specialFilter
def test_specialFilter():assert module_0.specialFilter([15, -73, 14, -15]) == 1

# Generated at 2026-10-24 21:08:44.419115
# Unit test for function specialFilter
def test_specialFilter():
    # Numbers > 10 with odd first AND last digit
    assert module_0.specialFilter([15, -73, 14, -15]) == 1      # only 15 qualifies
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2  # 33 and 109... wait, 109 last digit is 9, first is 1 â yes; 45 ends in 5, starts 4 â no
    assert module_0.specialFilter([11, 13, 17, 19]) == 4        # all qualify
    assert module_0.specialFilter([22, 24, 30, 44]) == 0        # none qualify
    assert module_0.specialFilter([]) == 0                      # empty list
    assert module_0.specialFilter([10]) == 0                    # 10 is not > 10
    assert module_0.specialFilter([97, 101, 123, 555]) == 2     # 97, 555 qualify
    print("All tests passed!")

test_specialFilter()

# Generated at 2026-10-24 21:08:45.737706
# Unit test for function specialFilter
def test_specialFilter():
    # Numbers > 10 with odd first AND last digit
    assert module_0.specialFilter([15, -73, 14, -15]) == 1      # only 15 qualifies
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2  # 33 and 109... wait, 109 last digit is 9, first is 1 â yes; 45 ends in 5, starts 4 â no
    assert module_0.specialFilter([11, 13, 17, 19]) == 4        # all qualify
    assert module_0.specialFilter([22, 24, 30, 44]) == 0        # none qualify
    assert module_0.specialFilter([]) == 0                      # empty list
    assert module_0.specialFilter([10]) == 0                    # 10 is not > 10
    assert module_0.specialFilter([97, 101, 123, 555]) == 2     # 97, 555 qualify
    print("All tests passed!")

test_specialFilter()

# Generated at 2026-10-24 21:08:47.059738
# Unit test for function specialFilter
def test_specialFilter():
    # Numbers > 10 with odd first AND last digit
    assert module_0.specialFilter([15, -73, 14, -15]) == 1      # only 15 qualifies
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2  # 33 and 109... wait, 109 last digit is 9, first is 1 â yes; 45 ends in 5, starts 4 â no
    assert module_0.specialFilter([11, 13, 17, 19]) == 4        # all qualify
    assert module_0.specialFilter([22, 24, 30, 44]) == 0        # none qualify
    assert module_0.specialFilter([]) == 0                      # empty list
    assert module_0.specialFilter([10]) == 0                    # 10 is not > 10
    assert module_0.specialFilter([97, 101, 123, 555]) == 2     # 97, 555 qualify
    print("All tests passed!")

test_specialFilter()