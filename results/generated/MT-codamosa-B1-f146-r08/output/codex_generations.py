

# Generated at 2026-10-24 11:14:46.695858
# Unit test for function specialFilter
def test_specialFilter():
    # official examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # empty / no matches
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([10, 12, 22]) == 0      # 10 not >10; 12,22 even first digit

    # boundary: 11 is the smallest qualifying value
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([10]) == 0

    # negatives are excluded by the num > 10 guard (never stringified)
    assert module_0.specialFilter([-11, -33, -99]) == 0

    # multi-digit: only first + last digits matter
    assert module_0.specialFilter([101, 111, 123, 999]) == 3   # 101,111,999
    print("all tests passed")

# Generated at 2026-10-24 11:14:48.022999
# Unit test for function specialFilter
def test_specialFilter():
    # official examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # empty / no matches
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([10, 12, 22]) == 0      # 10 not >10; 12,22 even first digit

    # boundary: 11 is the smallest qualifying value
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([10]) == 0

    # negatives are excluded by the num > 10 guard (never stringified)
    assert module_0.specialFilter([-11, -33, -99]) == 0

    # multi-digit: only first + last digits matter
    assert module_0.specialFilter([101, 111, 123, 999]) == 3   # 101,111,999
    print("all tests passed")

# Generated at 2026-10-24 11:14:49.342385
# Unit test for function specialFilter
def test_specialFilter():
    # official examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # empty / no matches
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([10, 12, 22]) == 0      # 10 not >10; 12,22 even first digit

    # boundary: 11 is the smallest qualifying value
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([10]) == 0

    # negatives are excluded by the num > 10 guard (never stringified)
    assert module_0.specialFilter([-11, -33, -99]) == 0

    # multi-digit: only first + last digits matter
    assert module_0.specialFilter([101, 111, 123, 999]) == 3   # 101,111,999
    print("all tests passed")

# Generated at 2026-10-24 11:14:50.651077
# Unit test for function specialFilter
def test_specialFilter():
    # official examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # empty / no matches
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([10, 12, 22]) == 0      # 10 not >10; 12,22 even first digit

    # boundary: 11 is the smallest qualifying value
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([10]) == 0

    # negatives are excluded by the num > 10 guard (never stringified)
    assert module_0.specialFilter([-11, -33, -99]) == 0

    # multi-digit: only first + last digits matter
    assert module_0.specialFilter([101, 111, 123, 999]) == 3   # 101,111,999
    print("all tests passed")

# Generated at 2026-10-24 11:14:51.962977
# Unit test for function specialFilter
def test_specialFilter():
    # official examples
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2

    # empty / no matches
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([10, 12, 22]) == 0      # 10 not >10; 12,22 even first digit

    # boundary: 11 is the smallest qualifying value
    assert module_0.specialFilter([11]) == 1
    assert module_0.specialFilter([10]) == 0

    # negatives are excluded by the num > 10 guard (never stringified)
    assert module_0.specialFilter([-11, -33, -99]) == 0

    # multi-digit: only first + last digits matter
    assert module_0.specialFilter([101, 111, 123, 999]) == 3   # 101,111,999
    print("all tests passed")