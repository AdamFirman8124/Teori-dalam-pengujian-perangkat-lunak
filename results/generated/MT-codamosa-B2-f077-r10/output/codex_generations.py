

# Generated at 2026-10-24 13:17:45.158293
# Unit test for function iscube

# Generated at 2026-10-24 13:17:47.571448
# Unit test for function iscube

# Generated at 2026-10-24 13:17:50.117111
# Unit test for function iscube

# Generated at 2026-10-24 13:17:52.529551
# Unit test for function iscube

# Generated at 2026-10-24 13:17:54.945988
# Unit test for function iscube

# Generated at 2026-10-24 13:17:57.361539
# Unit test for function iscube

# Generated at 2026-10-24 13:17:59.778856
# Unit test for function iscube

# Generated at 2026-10-24 13:18:02.187074
# Unit test for function iscube

# Generated at 2026-10-24 13:18:04.602481
# Unit test for function iscube

# Generated at 2026-10-24 13:18:18.148627
# Unit test for function iscube
def test_iscube():
    # Perfect cubes (positive)
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Perfect cubes (negative)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True

    # Zero is a cube
    assert module_0.iscube(0) == True

    # Not cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-9) == False

    # Large values
    assert module_0.iscube(10 ** 6) == True
    assert module_0.iscube(10 ** 6 + 1) == False

    print("All tests passed!")

# Generated at 2026-10-24 13:18:21.121858
# Unit test for function iscube
def test_iscube():
    # Perfect cubes (positive)
    assert module_0.iscube(1) == True
    assert module_0.iscube(8) == True
    assert module_0.iscube(27) == True
    assert module_0.iscube(64) == True
    assert module_0.iscube(125) == True
    assert module_0.iscube(1000) == True

    # Perfect cubes (negative)
    assert module_0.iscube(-1) == True
    assert module_0.iscube(-8) == True
    assert module_0.iscube(-27) == True
    assert module_0.iscube(-64) == True

    # Zero is a cube
    assert module_0.iscube(0) == True

    # Not cubes
    assert module_0.iscube(2) == False
    assert module_0.iscube(3) == False
    assert module_0.iscube(9) == False
    assert module_0.iscube(10) == False
    assert module_0.iscube(26) == False
    assert module_0.iscube(-2) == False
    assert module_0.iscube(-9) == False

    # Large values
    assert module_0.iscube(10 ** 6) == True
    assert module_0.iscube(10 ** 6 + 1) == False

    print("All tests passed!")