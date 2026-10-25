

# Generated at 2026-10-24 13:57:29.955059
# Unit test for function starts_one_ends

# Generated at 2026-10-24 13:57:32.376718
# Unit test for function starts_one_ends

# Generated at 2026-10-24 13:57:34.793669
# Unit test for function starts_one_ends

# Generated at 2026-10-24 13:57:37.205964
# Unit test for function starts_one_ends

# Generated at 2026-10-24 13:57:45.222117
# Unit test for function starts_one_ends
def test_starts_one_ends():assert module_0.starts_one_ends(1) == 1

# Generated at 2026-10-24 13:57:46.544594
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # n = 1: only the number 1
    assert module_0.starts_one_ends(1) == 1

    # n = 2: 10-19 (10) + 21,31,...,91 (8) + 11 counted once = 18
    assert module_0.starts_one_ends(2) == 18

    # n = 3: 18 * 10 = 180
    assert module_0.starts_one_ends(3) == 180

    # n = 4: 18 * 100 = 1800
    assert module_0.starts_one_ends(4) == 1800

    # General formula holds for larger n
    assert module_0.starts_one_ends(10) == 18 * 10**8


if __name__ == "__main__":
    test_starts_one_ends()
    print("all tests passed")

# Generated at 2026-10-24 13:57:47.852488
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # n = 1: only the number 1
    assert module_0.starts_one_ends(1) == 1

    # n = 2: 10-19 (10) + 21,31,...,91 (8) + 11 counted once = 18
    assert module_0.starts_one_ends(2) == 18

    # n = 3: 18 * 10 = 180
    assert module_0.starts_one_ends(3) == 180

    # n = 4: 18 * 100 = 1800
    assert module_0.starts_one_ends(4) == 1800

    # General formula holds for larger n
    assert module_0.starts_one_ends(10) == 18 * 10**8


if __name__ == "__main__":
    test_starts_one_ends()
    print("all tests passed")

# Generated at 2026-10-24 13:57:49.216367
# Unit test for function starts_one_ends
def test_starts_one_ends():
    assert module_0.starts_one_ends(1) == 1
    assert module_0.starts_one_ends(2) == 18
    assert module_0.starts_one_ends(3) == 180
    assert module_0.starts_one_ends(4) == 1800
    assert module_0.starts_one_ends(5) == 18000

    # brute-force verification for n = 2, 3
    for n, expected in [(2, 18), (3, 180)]:
        count = sum(
            1 for x in range(10**(n-1), 10**n)
            if str(x).startswith('1') or str(x).endswith('1')
        )
        assert module_0.starts_one_ends(n) == count == expected