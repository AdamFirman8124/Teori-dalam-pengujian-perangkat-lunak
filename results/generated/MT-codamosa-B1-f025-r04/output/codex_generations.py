

# Generated at 2026-10-24 15:21:25.846521
# Unit test for function factorize
def test_factorize():
    assert module_0.factorize(2) == [2]                    # prime
    assert module_0.factorize(3) == [3]
    assert module_0.factorize(4) == [2, 2]
    assert module_0.factorize(8) == [2, 2, 2]
    assert module_0.factorize(12) == [2, 2, 3]
    assert module_0.factorize(30) == [2, 3, 5]
    assert module_0.factorize(49) == [7, 7]
    assert module_0.factorize(97) == [97]                  # large prime
    assert module_0.factorize(360) == [2, 2, 2, 3, 3, 5]
    assert module_0.factorize(1) == []                     # edge case
    assert module_0.factorize(0) == []                     # edge case
    # product check: factors multiply back to n
    for n in [2, 12, 97, 360, 99991, 104729]:
        prod = 1
        for f in module_0.factorize(n):
            prod *= f
        assert prod == n

# Generated at 2026-10-24 15:21:28.260665
# Unit test for function factorize

# Generated at 2026-10-24 15:21:30.675204
# Unit test for function factorize

# Generated at 2026-10-24 15:21:33.088798
# Unit test for function factorize

# Generated at 2026-10-24 15:21:35.501994
# Unit test for function factorize

# Generated at 2026-10-24 15:21:37.915052
# Unit test for function factorize

# Generated at 2026-10-24 15:21:40.328393
# Unit test for function factorize

# Generated at 2026-10-24 15:21:42.881545
# Unit test for function factorize

# Generated at 2026-10-24 15:21:45.295825
# Unit test for function factorize

# Generated at 2026-10-24 15:21:47.711244
# Unit test for function factorize

# Generated at 2026-10-24 15:21:50.124408
# Unit test for function factorize

# Generated at 2026-10-24 15:21:52.537191
# Unit test for function factorize

# Generated at 2026-10-24 15:21:54.950675
# Unit test for function factorize