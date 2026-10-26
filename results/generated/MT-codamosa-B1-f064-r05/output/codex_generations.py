

# Generated at 2026-10-25 09:19:48.110220
# Unit test for function vowels_count

# Generated at 2026-10-25 09:19:50.525295
# Unit test for function vowels_count

# Generated at 2026-10-25 09:19:52.946919
# Unit test for function vowels_count

# Generated at 2026-10-25 09:19:55.357852
# Unit test for function vowels_count

# Generated at 2026-10-25 09:19:57.774907
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:00.189443
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:02.602544
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:05.019719
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:07.432782
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:09.848925
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:12.260418
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:14.673975
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:17.089187
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:19.505834
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:21.919577
# Unit test for function vowels_count

# Generated at 2026-10-25 09:20:29.295374
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()

# Generated at 2026-10-25 09:20:30.742600
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()

# Generated at 2026-10-25 09:20:32.070109
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()

# Generated at 2026-10-25 09:20:33.459209
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()

# Generated at 2026-10-25 09:20:34.801381
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()

# Generated at 2026-10-25 09:20:36.223423
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()

# Generated at 2026-10-25 09:20:37.766453
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()

# Generated at 2026-10-25 09:20:39.217466
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()

# Generated at 2026-10-25 09:20:40.732690
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()

# Generated at 2026-10-25 09:20:42.164428
# Unit test for function vowels_count
def test_vowels_count():
    # Standard cases
    assert module_0.vowels_count("abcde") == 2      # a, e
    assert module_0.vowels_count("ACEDY") == 3      # A, E, Y (trailing y counts)
    assert module_0.vowels_count("hello") == 2      # e, o
    assert module_0.vowels_count("world") == 1      # o

    # Trailing y / Y
    assert module_0.vowels_count("busy") == 1       # u + y
    assert module_0.vowels_count("Y") == 1          # Y alone
    assert module_0.vowels_count("y") == 1
    assert module_0.vowels_count("yaml") == 1       # y not at end â not counted

    # No vowels
    assert module_0.vowels_count("bcdfg") == 0
    assert module_0.vowels_count("") == 0

    # Mixed case vowels
    assert module_0.vowels_count("AbEcIdE") == 5

    # Digits and punctuation
    assert module_0.vowels_count("a1e2i!") == 3
    assert module_0.vowels_count("!!!") == 0

    print("All tests passed.")

test_vowels_count()