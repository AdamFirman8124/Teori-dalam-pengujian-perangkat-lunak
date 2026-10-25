

# Generated at 2026-10-24 10:36:07.437857
# Unit test for function tri
def test_tri():
    # Base cases
    assert module_0.tri(0) == [1]
    assert module_0.tri(1) == [1, 3]
    # Known values (even entries use i/2, so floats are expected)
    assert module_0.tri(2) == [1, 3, 2.0]
    assert module_0.tri(3) == [1, 3, 2.0, 8.0]
    assert module_0.tri(4) == [1, 3, 2.0, 8.0, 3.0]
    assert module_0.tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    # Length check
    assert len(module_0.tri(10)) == 11
    # Odd recurrence holds throughout
    t = module_0.tri(9)
    for i in range(2, 10):
        if i % 2 == 0:
            assert t[i] == 1 + i / 2
        else:
            assert t[i] == t[i - 1] + t[i - 2] + (i + 3) / 2
    print("All tri tests passed.")

test_tri()

# Generated at 2026-10-24 10:36:08.875020
# Unit test for function tri
def test_tri():
    # Base cases
    assert module_0.tri(0) == [1]
    assert module_0.tri(1) == [1, 3]
    # Known values (even entries use i/2, so floats are expected)
    assert module_0.tri(2) == [1, 3, 2.0]
    assert module_0.tri(3) == [1, 3, 2.0, 8.0]
    assert module_0.tri(4) == [1, 3, 2.0, 8.0, 3.0]
    assert module_0.tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    # Length check
    assert len(module_0.tri(10)) == 11
    # Odd recurrence holds throughout
    t = module_0.tri(9)
    for i in range(2, 10):
        if i % 2 == 0:
            assert t[i] == 1 + i / 2
        else:
            assert t[i] == t[i - 1] + t[i - 2] + (i + 3) / 2
    print("All tri tests passed.")

test_tri()

# Generated at 2026-10-24 10:36:10.206752
# Unit test for function tri
def test_tri():
    # Base cases
    assert module_0.tri(0) == [1]
    assert module_0.tri(1) == [1, 3]
    # Known values (even entries use i/2, so floats are expected)
    assert module_0.tri(2) == [1, 3, 2.0]
    assert module_0.tri(3) == [1, 3, 2.0, 8.0]
    assert module_0.tri(4) == [1, 3, 2.0, 8.0, 3.0]
    assert module_0.tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    # Length check
    assert len(module_0.tri(10)) == 11
    # Odd recurrence holds throughout
    t = module_0.tri(9)
    for i in range(2, 10):
        if i % 2 == 0:
            assert t[i] == 1 + i / 2
        else:
            assert t[i] == t[i - 1] + t[i - 2] + (i + 3) / 2
    print("All tri tests passed.")

test_tri()

# Generated at 2026-10-24 10:36:11.638222
# Unit test for function tri
def test_tri():
    # Base cases
    assert module_0.tri(0) == [1]
    assert module_0.tri(1) == [1, 3]
    # Known values (even entries use i/2, so floats are expected)
    assert module_0.tri(2) == [1, 3, 2.0]
    assert module_0.tri(3) == [1, 3, 2.0, 8.0]
    assert module_0.tri(4) == [1, 3, 2.0, 8.0, 3.0]
    assert module_0.tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    # Length check
    assert len(module_0.tri(10)) == 11
    # Odd recurrence holds throughout
    t = module_0.tri(9)
    for i in range(2, 10):
        if i % 2 == 0:
            assert t[i] == 1 + i / 2
        else:
            assert t[i] == t[i - 1] + t[i - 2] + (i + 3) / 2
    print("All tri tests passed.")

test_tri()

# Generated at 2026-10-24 10:36:13.020413
# Unit test for function tri
def test_tri():
    # Base cases
    assert module_0.tri(0) == [1]
    assert module_0.tri(1) == [1, 3]
    # Known values (even entries use i/2, so floats are expected)
    assert module_0.tri(2) == [1, 3, 2.0]
    assert module_0.tri(3) == [1, 3, 2.0, 8.0]
    assert module_0.tri(4) == [1, 3, 2.0, 8.0, 3.0]
    assert module_0.tri(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    # Length check
    assert len(module_0.tri(10)) == 11
    # Odd recurrence holds throughout
    t = module_0.tri(9)
    for i in range(2, 10):
        if i % 2 == 0:
            assert t[i] == 1 + i / 2
        else:
            assert t[i] == t[i - 1] + t[i - 2] + (i + 3) / 2
    print("All tri tests passed.")

test_tri()