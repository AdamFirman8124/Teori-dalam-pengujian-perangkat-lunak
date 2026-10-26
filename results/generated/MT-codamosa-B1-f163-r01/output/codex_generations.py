

# Generated at 2026-10-25 07:31:49.259154
# Unit test for function generate_integers
def test_generate_integers():
    # Normal + reversed order
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Inside bounds
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []

    # Clamped to 2-8
    assert module_0.generate_integers(0, 5) == [2, 4]
    assert module_0.generate_integers(5, 20) == [6, 8]
    assert module_0.generate_integers(-10, 100) == [2, 4, 6, 8]

    # Entirely outside bounds
    assert module_0.generate_integers(0, 1) == []
    assert module_0.generate_integers(9, 10) == []

# Generated at 2026-10-25 07:31:50.955336
# Unit test for function generate_integers
def test_generate_integers():
    # Normal + reversed order
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Inside bounds
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []

    # Clamped to 2-8
    assert module_0.generate_integers(0, 5) == [2, 4]
    assert module_0.generate_integers(5, 20) == [6, 8]
    assert module_0.generate_integers(-10, 100) == [2, 4, 6, 8]

    # Entirely outside bounds
    assert module_0.generate_integers(0, 1) == []
    assert module_0.generate_integers(9, 10) == []

# Generated at 2026-10-25 07:31:52.300088
# Unit test for function generate_integers
def test_generate_integers():
    # Normal + reversed order
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Inside bounds
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []

    # Clamped to 2-8
    assert module_0.generate_integers(0, 5) == [2, 4]
    assert module_0.generate_integers(5, 20) == [6, 8]
    assert module_0.generate_integers(-10, 100) == [2, 4, 6, 8]

    # Entirely outside bounds
    assert module_0.generate_integers(0, 1) == []
    assert module_0.generate_integers(9, 10) == []

# Generated at 2026-10-25 07:31:53.825002
# Unit test for function generate_integers
def test_generate_integers():
    # Normal + reversed order
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Inside bounds
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []

    # Clamped to 2-8
    assert module_0.generate_integers(0, 5) == [2, 4]
    assert module_0.generate_integers(5, 20) == [6, 8]
    assert module_0.generate_integers(-10, 100) == [2, 4, 6, 8]

    # Entirely outside bounds
    assert module_0.generate_integers(0, 1) == []
    assert module_0.generate_integers(9, 10) == []

# Generated at 2026-10-25 07:31:55.160573
# Unit test for function generate_integers
def test_generate_integers():
    # Normal + reversed order
    assert module_0.generate_integers(2, 8) == [2, 4, 6, 8]
    assert module_0.generate_integers(8, 2) == [2, 4, 6, 8]

    # Inside bounds
    assert module_0.generate_integers(3, 7) == [4, 6]
    assert module_0.generate_integers(4, 4) == [4]
    assert module_0.generate_integers(3, 3) == []

    # Clamped to 2-8
    assert module_0.generate_integers(0, 5) == [2, 4]
    assert module_0.generate_integers(5, 20) == [6, 8]
    assert module_0.generate_integers(-10, 100) == [2, 4, 6, 8]

    # Entirely outside bounds
    assert module_0.generate_integers(0, 1) == []
    assert module_0.generate_integers(9, 10) == []