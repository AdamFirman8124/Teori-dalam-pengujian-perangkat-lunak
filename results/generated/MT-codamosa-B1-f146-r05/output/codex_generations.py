

# Generated at 2026-10-24 15:34:22.300084
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

# Generated at 2026-10-24 15:34:23.770688
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

# Generated at 2026-10-24 15:34:25.152857
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

# Generated at 2026-10-24 15:34:27.750285
# Unit test for function specialFilter

# Generated at 2026-10-24 15:34:30.276884
# Unit test for function specialFilter

# Generated at 2026-10-24 15:34:32.690308
# Unit test for function specialFilter

# Generated at 2026-10-24 15:34:35.190745
# Unit test for function specialFilter

# Generated at 2026-10-24 15:34:50.691152
# Unit test for function specialFilter
def test_specialFilter():assert module_0.specialFilter([15, 35, 11, 22, 12]) == 3