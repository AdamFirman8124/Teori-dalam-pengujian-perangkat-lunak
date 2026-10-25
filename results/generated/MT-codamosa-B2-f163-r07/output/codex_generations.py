

# Generated at 2026-10-24 15:36:52.661667
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

# Generated at 2026-10-24 15:36:54.094066
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

# Generated at 2026-10-24 15:36:55.528938
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

# Generated at 2026-10-24 15:36:56.961517
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

# Generated at 2026-10-24 15:37:30.549387
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