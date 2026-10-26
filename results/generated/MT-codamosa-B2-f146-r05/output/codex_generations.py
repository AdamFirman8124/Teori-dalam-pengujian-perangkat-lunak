

# Generated at 2026-10-25 08:53:24.858683
# Unit test for function specialFilter

# Generated at 2026-10-25 08:53:27.274905
# Unit test for function specialFilter

# Generated at 2026-10-25 08:53:29.691070
# Unit test for function specialFilter

# Generated at 2026-10-25 08:53:32.108100
# Unit test for function specialFilter

# Generated at 2026-10-25 08:53:34.524195
# Unit test for function specialFilter

# Generated at 2026-10-25 08:53:40.241364
# Unit test for function specialFilter
def test_specialFilter():assert module_0.specialFilter([15, 33, 1422, 1]) == 2

# Generated at 2026-10-25 08:53:42.716800
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([10]) == 0
    assert module_0.specialFilter([101, 303, 505]) == 3

# Generated at 2026-10-25 08:53:44.239458
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([10]) == 0
    assert module_0.specialFilter([101, 303, 505]) == 3

# Generated at 2026-10-25 08:53:45.670630
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