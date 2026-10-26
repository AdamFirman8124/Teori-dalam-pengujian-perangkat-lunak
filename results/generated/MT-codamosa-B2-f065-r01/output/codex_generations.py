

# Generated at 2026-10-25 11:48:50.361380
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by < len(s)
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(100, 1) == "010"

    # no shift / full rotation
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12, 2) == "12"

    # shift > len(s) -> reversed
    assert module_0.circular_shift(123, 5) == "321"

# Generated at 2026-10-25 11:48:51.965761
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by < len(s)
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(100, 1) == "010"

    # no shift / full rotation
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12, 2) == "12"

    # shift > len(s) -> reversed
    assert module_0.circular_shift(123, 5) == "321"

# Generated at 2026-10-25 11:48:53.503384
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by < len(s)
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(100, 1) == "010"

    # no shift / full rotation
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12, 2) == "12"

    # shift > len(s) -> reversed
    assert module_0.circular_shift(123, 5) == "321"

# Generated at 2026-10-25 11:48:54.958148
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by < len(s)
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(100, 1) == "010"

    # no shift / full rotation
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12, 2) == "12"

    # shift > len(s) -> reversed
    assert module_0.circular_shift(123, 5) == "321"

# Generated at 2026-10-25 11:48:56.476314
# Unit test for function circular_shift
def test_circular_shift():
    # shift right by < len(s)
    assert module_0.circular_shift(12345, 2) == "45123"
    assert module_0.circular_shift(12, 1) == "21"
    assert module_0.circular_shift(100, 1) == "010"

    # no shift / full rotation
    assert module_0.circular_shift(12345, 0) == "12345"
    assert module_0.circular_shift(12345, 5) == "12345"
    assert module_0.circular_shift(12, 2) == "12"

    # shift > len(s) -> reversed
    assert module_0.circular_shift(123, 5) == "321"