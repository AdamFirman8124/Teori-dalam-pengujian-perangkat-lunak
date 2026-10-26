

# Generated at 2026-10-25 10:38:55.476833
# Unit test for function starts_one_ends
def test_starts_one_ends():
    # n = 1: only the number 1 itself
    assert module_0.starts_one_ends(1) == 1

    # n = 2: 10,11,12,...,19 and 21,31,41,51,61,71,81,91 (11 counted once) = 18
    assert module_0.starts_one_ends(2) == 18

    # n = 3: 18 * 10 = 180
    assert module_0.starts_one_ends(3) == 180

    # n = 5: 18 * 1000 = 18000
    assert module_0.starts_one_ends(5) == 18000

    # n = 10: 18 * 10^8 = 1800000000
    assert module_0.starts_one_ends(10) == 1800000000

    # Cross-check by brute force for small n
    for n in (1, 2, 3):
        count = 0
        for x in range(10 ** (n - 1) if n > 1 else 1, 10 ** n):
            s = str(x)
            if s[0] == '1' or s[-1] == '1':
                count += 1
        assert count == module_0.starts_one_ends(n), f"mismatch for n={n}"

    print("All tests passed.")


if __name__ == "__main__":
    test_starts_one_ends()

# Generated at 2026-10-25 10:38:57.896230
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:00.310263
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:02.738967
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:05.149945
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:07.615916
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:10.032101
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:12.450594
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:14.862579
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:17.276748
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:19.690885
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:22.105729
# Unit test for function starts_one_ends

# Generated at 2026-10-25 10:39:24.519077
# Unit test for function starts_one_ends