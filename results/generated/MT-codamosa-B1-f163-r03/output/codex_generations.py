

# Generated at 2026-10-24 10:43:58.648261
# Unit test for function generate_integers

# Generated at 2026-10-24 10:44:01.066818
# Unit test for function generate_integers

# Generated at 2026-10-24 10:44:03.486547
# Unit test for function generate_integers

# Generated at 2026-10-24 10:44:05.906385
# Unit test for function generate_integers

# Generated at 2026-10-24 10:44:08.326231
# Unit test for function generate_integers

# Generated at 2026-10-24 10:44:12.507242
# Unit test for function generate_integers
def test_generate_integers():
    assert module_0.generate_integers(2, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    assert module_0.generate_integers(1, 3) == [2]
    assert module_0.generate_integers(5, 5) == []
    assert module_0.generate_integers(9, 10) == []

# Generated at 2026-10-24 10:44:18.299788
# Unit test for function generate_integers
def test_generate_integers():
    # Basic cases
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]   # order-independent
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(3, 7) == [4, 6]

    # Clamped to [2, 8] range
    assert module_0.generate_integers(-3, 100) == [2, 4, 6, 8]
    assert module_0.generate_integers(0, 2) == [2]

    # No even numbers in range
    assert module_0.generate_integers(9, 11) == []
    assert module_0.generate_integers(10, 20) == []

    # Single-value ranges
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(5, 5) == []

    # Negative ranges
    assert module_0.generate_integers(-10, -5) == []

    print("All tests passed!")


test_generate_integers()

# Generated at 2026-10-24 10:44:19.626348
# Unit test for function generate_integers
def test_generate_integers():
    # Basic cases
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]   # order-independent
    assert module_0.generate_integers(1, 5) == [2, 4]
    assert module_0.generate_integers(3, 7) == [4, 6]

    # Clamped to [2, 8] range
    assert module_0.generate_integers(-3, 100) == [2, 4, 6, 8]
    assert module_0.generate_integers(0, 2) == [2]

    # No even numbers in range
    assert module_0.generate_integers(9, 11) == []
    assert module_0.generate_integers(10, 20) == []

    # Single-value ranges
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(5, 5) == []

    # Negative ranges
    assert module_0.generate_integers(-10, -5) == []

    print("All tests passed!")


test_generate_integers()

# Generated at 2026-10-24 10:44:31.659078
# Unit test for function generate_integers
def test_generate_integers():
    # basic range 2 to 8
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    # order should not matter
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    assert module_0.generate_integers(132, 2) == [2, 4, 6, 8]

    # no evens in 2..8 overlap
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(0, 1) == []

    # clamping to [2, 8]
    assert module_0.generate_integers(0, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(1, 10) == [2, 4, 6, 8]

    # partial overlaps
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(5, 6) == [6]

    # single values
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []