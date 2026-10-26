

# Generated at 2026-10-25 07:31:11.739136
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

# Generated at 2026-10-25 07:31:13.272612
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

# Generated at 2026-10-25 07:31:14.697989
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

# Generated at 2026-10-25 07:31:16.072791
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

# Generated at 2026-10-25 07:31:17.469806
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