

# Generated at 2026-11-03 05:56:30.782903
# Unit test for function iscube
def test_iscube():
    # Positive perfect cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Negative perfect cubes (abs is applied, so these are cubes)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True

    # Zero is a perfect cube
    assert module_0.iscube(0) == True

    # Non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(4) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(180) == False

    # Large values
    assert module_0.iscube(10**18) == True          # (10**6)**3
    assert module_0.iscube(-(10**18)) == True
    assert module_0.iscube(10**18 + 1) == False

    # Values near cube roots that could suffer floating point issues
    assert module_0.iscube(3**3) == True
    assert module_0.iscube(4**3 + 1) == False
    assert module_0.iscube(5**3 - 1) == False

# Generated at 2026-11-03 05:57:38.174698
# Unit test for function iscube
def test_iscube():
    # Test positive perfect cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Test zero
    assert module_0.iscube(0) == True

    # Test negative perfect cubes (abs is applied)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True

    # Test non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(100) == False
    assert module_0.iscube(-2) == False

    # Test large numbers
    assert module_0.iscube(10**9) == True      # 1000^3
    assert module_0.iscube(1000000) == True    # 100^3
    assert module_0.iscube(10**9 + 1) == False

    # Test float input that is a cube value
    assert module_0.iscube(27.0) == True
    assert module_0.iscube(27.5) == False

    print("All tests passed!")

if __name__ == "__main__":
    test_iscube()

# Generated at 2026-11-03 05:59:01.943468
# Unit test for function iscube
def test_iscube():
    # Perfect positive cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Zero is a cube (0 ** 3 == 0)
    assert module_0.iscube(0) == True

    # Negative perfect cubes (abs makes them checkable)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True
    assert module_0.iscube(-1000) == True

    # Non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(25) == False
    assert module_0.iscube(-5) == False

    # Values adjacent to cubes
    assert module_0.iscube(7) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(28) == False
    assert module_0.iscube(63) == False
    assert module_0.iscube(65) == False

    # Large cubes
    assert module_0.iscube(10**9) == True        # 1000**3
    assert module_0.iscube(10**12) == True       # 10000**3
    assert module_0.iscube(2**30) == True        # 1024**3
    assert module_0.iscube(-10**9) == True

    # Large non-cubes
    assert module_0.iscube(10**9 + 1) == False
    assert module_0.iscube(10**9 - 1) == False
    assert module_0.iscube(2**30 + 1) == False
# nonce:20c95d0f

# Generated at 2026-11-03 06:00:09.513020
# Unit test for function iscube
def test_iscube():
    # Perfect cubes (positive)
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Perfect cubes (negative) - abs is applied, so negatives of cubes are cubes
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True

    # Zero is a perfect cube
    assert module_0.iscube(0) == True

    # Non-cubes (positive)
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(4) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(28) == False
    assert module_0.iscube(63) == False
    assert module_0.iscube(65) == False

    # Non-cubes (negative)
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-10) == False

    # Large perfect cube
    assert module_0.iscube(1000000) == True  # 100^3
    assert module_0.iscube(10**18) == True   # (10^6)^3

    # Large non-cube
    assert module_0.iscube(1000001) == False

# Generated at 2026-11-03 06:01:28.567238
# Unit test for function iscube
def test_iscube():
    # Positive perfect cubes
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000000) == True

    # Negative perfect cubes (abs makes them cubes)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True
    assert module_0.iscube(-125) == True

    # Zero is a perfect cube
    assert module_0.iscube(0) == True

    # Non-cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(100) == False
    assert module_0.iscube(180) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(999999) == False