

# Generated at 2026-10-24 15:15:51.128861
# Unit test for function generate_integers

# Generated at 2026-10-24 15:15:53.542925
# Unit test for function generate_integers

# Generated at 2026-10-24 15:15:55.957690
# Unit test for function generate_integers

# Generated at 2026-10-24 15:16:10.277980
# Unit test for function generate_integers
def test_generate_integers():
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(3, 3) == []
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(0, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(4, 4) == [4]

# Generated at 2026-10-24 15:16:11.647104
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

# Generated at 2026-10-24 15:16:42.759242
# Unit test for function generate_integers
def test_generate_integers():
    # basic range, ascending and descending
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # completely outside [2, 8]
    assert module_0.generate_integers(10, 14) == []
    assert module_0.generate_integers(0, 1) == []
    assert module_0.generate_integers(9, 9) == []

    # clamped to [2, 8]
    assert module_0.generate_integers(1, 10) == [2, 4, 6, 8]
    assert module_0.generate_integers(-5, 5) == [2, 4]

    # single value
    assert module_0.generate_integers(2, 2) == [2]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []

    # odd / partial ranges
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(4, 7) == [4, 6]
    assert module_0.generate_integers(2, 3) == [2]
    assert module_0.generate_integers(7, 8) == [8]
    assert module_0.generate_integers(5, 6) == [6]

# Generated at 2026-10-24 15:16:45.174001
# Unit test for function generate_integers

# Generated at 2026-10-24 15:16:47.588131
# Unit test for function generate_integers

# Generated at 2026-10-24 15:16:50.002276
# Unit test for function generate_integers