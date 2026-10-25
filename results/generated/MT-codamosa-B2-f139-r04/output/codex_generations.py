

# Generated at 2026-10-24 14:15:07.219998
# Unit test for function special_factorial

# Generated at 2026-10-24 14:15:09.634410
# Unit test for function special_factorial

# Generated at 2026-10-24 14:15:12.048083
# Unit test for function special_factorial

# Generated at 2026-10-24 14:15:14.467470
# Unit test for function special_factorial

# Generated at 2026-10-24 14:15:16.888433
# Unit test for function special_factorial

# Generated at 2026-10-24 14:15:19.301239
# Unit test for function special_factorial

# Generated at 2026-10-24 14:15:21.719985
# Unit test for function special_factorial

# Generated at 2026-10-24 14:15:26.425037
# Unit test for function special_factorial
def test_special_factorial():
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2
    assert module_0.special_factorial(3) == 12
    assert module_0.special_factorial(4) == 288
    assert module_0.special_factorial(5) == 34560
    assert module_0.special_factorial(6) == 24883200

# Generated at 2026-10-24 14:15:37.119385
# Unit test for function special_factorial
def test_special_factorial():
    # n! product: 1, 1, 2, 12, 288, 34560, 24883200, 125411328000, ...
    assert module_0.special_factorial(0) == 1
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2
    assert module_0.special_factorial(3) == 12
    assert module_0.special_factorial(4) == 288
    assert module_0.special_factorial(5) == 34560
    assert module_0.special_factorial(6) == 24883200
    assert module_0.special_factorial(7) == 125411328000
    assert module_0.special_factorial(8) == 5056584744960000


@pytest.mark.parametrize("n,expected", [
    (0, 1), (1, 1), (2, 2), (3, 12), (4, 288),
    (5, 34560), (6, 24883200), (7, 125411328000),
])
def test_special_factorial_param(n, expected):
    assert module_0.special_factorial(n) == expected


def test_matches_naive_product():
    for n in range(0, 15):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected


def test_negative_returns_one():
    # loop body never runs -> 1 (document this behavior, or add a guard)
    assert module_0.special_factorial(-5) == 1

# Generated at 2026-10-24 14:15:38.599045
# Unit test for function special_factorial
def test_special_factorial():
    # n! product: 1, 1, 2, 12, 288, 34560, 24883200, 125411328000, ...
    assert module_0.special_factorial(0) == 1
    assert module_0.special_factorial(1) == 1
    assert module_0.special_factorial(2) == 2
    assert module_0.special_factorial(3) == 12
    assert module_0.special_factorial(4) == 288
    assert module_0.special_factorial(5) == 34560
    assert module_0.special_factorial(6) == 24883200
    assert module_0.special_factorial(7) == 125411328000
    assert module_0.special_factorial(8) == 5056584744960000


@pytest.mark.parametrize("n,expected", [
    (0, 1), (1, 1), (2, 2), (3, 12), (4, 288),
    (5, 34560), (6, 24883200), (7, 125411328000),
])
def test_special_factorial_param(n, expected):
    assert module_0.special_factorial(n) == expected


def test_matches_naive_product():
    for n in range(0, 15):
        expected = 1
        for i in range(1, n + 1):
            expected *= math.factorial(i)
        assert module_0.special_factorial(n) == expected


def test_negative_returns_one():
    # loop body never runs -> 1 (document this behavior, or add a guard)
    assert module_0.special_factorial(-5) == 1