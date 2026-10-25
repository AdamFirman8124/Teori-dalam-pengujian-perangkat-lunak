

# Generated at 2026-10-24 07:04:24.775188
# Unit test for function iscube
def test_iscube():
    assert module_0.iscube(0)
    assert module_0.iscube(1)
    assert module_0.iscube(8)
    assert module_0.iscube(27)
    assert module_0.iscube(64)
    assert module_0.iscube(-8)
    assert module_0.iscube(-27)

    assert not module_0.iscube(2)
    assert not module_0.iscube(9)
    assert not module_0.iscube(26)
    assert not module_0.iscube(-9)

# Generated at 2026-10-24 07:04:42.867837
# Unit test for function iscube
def test_iscube():
    # True cases: perfect cubes (positive, negative, zero)
    assert module_0.iscube(0) is True
    assert module_0.iscube(1) is True
    assert module_0.iscube(8) is True
    assert module_0.iscube(27) is True
    assert module_0.iscube(64) is True
    assert module_0.iscube(125) is True
    assert module_0.iscube(-27) is True   # negative cube, abs() handles it
    assert module_0.iscube(-8) is True
    assert module_0.iscube(1000) is True

    # False cases: non-cubes
    assert module_0.iscube(2) is False
    assert module_0.iscube(9) is False
    assert module_0.iscube(26) is False
    assert module_0.iscube(28) is False
    assert module_0.iscube(-2) is False
    assert module_0.iscube(63) is False
    assert module_0.iscube(65) is False

    # Boundary / precision-sensitive: 1e6 == 100**3
    assert module_0.iscube(1000000) is True
    assert module_0.iscube(999999) is False

# Generated at 2026-10-24 07:05:16.522924
# Unit test for function iscube

# Generated at 2026-10-24 07:05:20.357731
# Unit test for function iscube
def test_iscube():
    assert module_0.iscube(1) == True
    assert module_0.iscube(-1) == True
    assert module_0.iscube(0) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(2) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(100) == False
    assert module_0.iscube(1000000) == True
    assert module_0.iscube(1000001) == False
    assert module_0.iscube(512) == True
    assert module_0.iscube(729) == True
    assert module_0.iscube(1000) == True
    assert module_0.iscube(999) == False

# Generated at 2026-10-24 07:05:40.026242
# Unit test for function iscube
def test_iscube():
    assert module_0.iscube(0) is True
    assert module_0.iscube(1) is True
    assert module_0.iscube(8) is True
    assert module_0.iscube(27) is True
    assert module_0.iscube(1000) is True

    # Negative perfect cubes are accepted because iscube uses abs().
    assert module_0.iscube(-8) is True
    assert module_0.iscube(-27) is True

    assert module_0.iscube(2) is False
    assert module_0.iscube(9) is False
    assert module_0.iscube(26) is False
    assert module_0.iscube(-9) is False

# Generated at 2026-10-24 07:05:56.493223
# Unit test for function iscube
def test_iscube():
    # True cases: perfect cubes (positive, negative, zero)
    assert module_0.iscube(0) is True
    assert module_0.iscube(1) is True
    assert module_0.iscube(8) is True
    assert module_0.iscube(27) is True
    assert module_0.iscube(64) is True
    assert module_0.iscube(125) is True
    assert module_0.iscube(-27) is True   # negative cube, abs() handles it
    assert module_0.iscube(-8) is True
    assert module_0.iscube(1000) is True

    # False cases: non-cubes
    assert module_0.iscube(2) is False
    assert module_0.iscube(9) is False
    assert module_0.iscube(26) is False
    assert module_0.iscube(28) is False
    assert module_0.iscube(-2) is False
    assert module_0.iscube(63) is False
    assert module_0.iscube(65) is False

    # Boundary / precision-sensitive: 1e6 == 100**3
    assert module_0.iscube(1000000) is True
    assert module_0.iscube(999999) is False