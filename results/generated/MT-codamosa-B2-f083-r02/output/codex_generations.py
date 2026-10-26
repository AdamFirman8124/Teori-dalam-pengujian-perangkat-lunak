

# Generated at 2026-10-25 07:02:26.106543
# Unit test for function starts_one_ends

# Generated at 2026-10-25 07:02:28.522168
# Unit test for function starts_one_ends

# Generated at 2026-10-25 07:02:36.444060
# Unit test for function starts_one_ends
def test_starts_one_ends():
    assert module_0.starts_one_ends(1) == 1
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000

# Generated at 2026-10-25 07:02:37.836239
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

# Generated at 2026-10-25 07:02:39.280222
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

# Generated at 2026-10-25 07:02:40.716762
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

# Generated at 2026-10-25 07:02:42.147023
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