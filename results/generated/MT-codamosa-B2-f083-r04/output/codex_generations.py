

# Generated at 2026-10-25 05:30:45.139125
# Unit test for function starts_one_ends
def test_starts_one_ends():
    assert module_0.starts_one_ends(1) == 1
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000

    # brute-force cross-check for n = 1, 2, 3
    for n, expected in [(1, 1), (2, 18), (3, 180)]:
        count = 0
        for i in range(10**(n-1), 10**n) if n > 1 else range(1, 10):
            s = str(i)
            if s[0] == '1' or s[-1] == '1':
                count += 1
        assert module_0.starts_one_ends(n) == count == expected

# Generated at 2026-10-25 05:30:46.503849
# Unit test for function starts_one_ends
def test_starts_one_ends():
    assert module_0.starts_one_ends(1) == 1
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000

    # brute-force cross-check for n = 1, 2, 3
    for n, expected in [(1, 1), (2, 18), (3, 180)]:
        count = 0
        for i in range(10**(n-1), 10**n) if n > 1 else range(1, 10):
            s = str(i)
            if s[0] == '1' or s[-1] == '1':
                count += 1
        assert module_0.starts_one_ends(n) == count == expected

# Generated at 2026-10-25 05:30:47.996903
# Unit test for function starts_one_ends
def test_starts_one_ends():
    assert module_0.starts_one_ends(1) == 1
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000

    # brute-force cross-check for n = 1, 2, 3
    for n, expected in [(1, 1), (2, 18), (3, 180)]:
        count = 0
        for i in range(10**(n-1), 10**n) if n > 1 else range(1, 10):
            s = str(i)
            if s[0] == '1' or s[-1] == '1':
                count += 1
        assert module_0.starts_one_ends(n) == count == expected

# Generated at 2026-10-25 05:30:49.429469
# Unit test for function starts_one_ends
def test_starts_one_ends():
    assert module_0.starts_one_ends(1) == 1
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000

    # brute-force cross-check for n = 1, 2, 3
    for n, expected in [(1, 1), (2, 18), (3, 180)]:
        count = 0
        for i in range(10**(n-1), 10**n) if n > 1 else range(1, 10):
            s = str(i)
            if s[0] == '1' or s[-1] == '1':
                count += 1
        assert module_0.starts_one_ends(n) == count == expected

# Generated at 2026-10-25 05:30:50.863623
# Unit test for function starts_one_ends
def test_starts_one_ends():
    assert module_0.starts_one_ends(1) == 1
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000

    # brute-force cross-check for n = 1, 2, 3
    for n, expected in [(1, 1), (2, 18), (3, 180)]:
        count = 0
        for i in range(10**(n-1), 10**n) if n > 1 else range(1, 10):
            s = str(i)
            if s[0] == '1' or s[-1] == '1':
                count += 1
        assert module_0.starts_one_ends(n) == count == expected