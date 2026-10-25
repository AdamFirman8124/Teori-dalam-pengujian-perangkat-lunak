

# Generated at 2026-10-25 00:59:38.705093
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, -3, 14, 9, 8, 21, 45, 5, 100]) == 3
    assert module_0.specialFilter([]) == 0
    assert module_0.specialFilter([9, 10, 11]) == 1
    assert module_0.specialFilter([12, 24, 46, 100]) == 0
    assert module_0.specialFilter([31, 53, 75, 91]) == 4

# Generated at 2026-10-25 00:59:44.234750
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, -73, 14, -15]) == 1
    assert module_0.specialFilter([33, -2, -3, 45, 21, 109]) == 2
    assert module_0.specialFilter([11, 13, 55, 79, 99]) == 5
    assert module_0.specialFilter([10, 20, 42, 88]) == 0
    assert module_0.specialFilter([]) == 0

# Generated at 2026-10-25 00:59:50.480874
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, -73, 14, 23, 25, 100, 33]) == 2
    assert module_0.specialFilter([11, 13, 35, 79, 99]) == 5
    assert module_0.specialFilter([12, 21, 42, 88]) == 0
    assert module_0.specialFilter([1, 3, 9, 10]) == 0
    assert module_0.specialFilter([]) == 0

# Generated at 2026-10-25 00:59:56.420188
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, 12, 13, 19, 93, 39, 55, 10, -31]) == 6
    assert module_0.specialFilter([11, 33, 55, 77, 99]) == 5
    assert module_0.specialFilter([12, 24, 42, 100, 200]) == 0
    assert module_0.specialFilter([10, 9, 1, -11]) == 0
    assert module_0.specialFilter([]) == 0

# Generated at 2026-10-25 01:00:00.822556
# Unit test for function specialFilter
def test_specialFilter():
    assert module_0.specialFilter([15, -12, 3, 9, 12, 45, 77]) == 3
    assert module_0.specialFilter([11, 13, 25, 39]) == 3
    assert module_0.specialFilter([10, 20, 42, 88]) == 0
    assert module_0.specialFilter([]) == 0