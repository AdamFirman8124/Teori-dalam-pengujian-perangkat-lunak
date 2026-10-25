

# Generated at 2026-10-24 04:37:59.831656
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

# Generated at 2026-10-24 04:38:01.154381
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

# Generated at 2026-10-24 04:38:02.479219
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

# Generated at 2026-10-24 04:38:03.797655
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

# Generated at 2026-10-24 04:38:05.122179
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