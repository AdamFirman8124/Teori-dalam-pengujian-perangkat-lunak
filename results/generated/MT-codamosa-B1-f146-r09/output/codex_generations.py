

# Generated at 2026-10-24 16:10:51.069771
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

# Generated at 2026-10-24 16:10:52.389830
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

# Generated at 2026-10-24 16:11:08.966694
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

# Generated at 2026-10-24 16:11:25.455863
# Unit test for function specialFilter
def test_specialFilter():
    # basic cases: only numbers > 10 with odd first and last digit count
    assert module_0.specialFilter([15, -73, 14, -15]) == 1  # only 15 qualifies
    assert module_0.specialFilter([33, -32, -45]) == 1      # only 33 qualifies

    # empty list
    assert module_0.specialFilter([]) == 0

    # all qualify
    assert module_0.specialFilter([33, 13, 55, 15, 11, 111, 135, 137]) == 8

    # none qualify: <= 10 or even first/last digit
    assert module_0.specialFilter([5, 7, 10, 12, 14, 22, 44, 20, 21, 42]) == 0

    # boundary of > 10 (10 itself does not count)
    assert module_0.specialFilter([10, 11]) == 1  # 10 excluded, 11: 1 and 1 odd

    # negative numbers never count because num > 10 fails
    assert module_0.specialFilter([-15, -33, -55, -137]) == 0

    # mixed first/last digit parity
    assert module_0.specialFilter([15, 14, 41, 22, 35, 56]) == 2  # 15 and 35

# Generated at 2026-10-24 16:11:27.967787
# Unit test for function specialFilter

# Generated at 2026-10-24 16:11:30.550294
# Unit test for function specialFilter

# Generated at 2026-10-24 16:11:32.967129
# Unit test for function specialFilter