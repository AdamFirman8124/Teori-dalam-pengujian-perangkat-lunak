

# Generated at 2026-11-03 05:02:32.863368
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    # Largest prime is 5 -> digit sum 5
    assert module_0.skjkasdkd([1, 25, 2, 1, 0, 5, 4]) == 5
    # No primes in list -> returns 0
    assert module_0.skjkasdkd([4, 32, 4, 8, 16]) == 0
    # Single prime element
    assert module_0.skjkasdkd([7]) == 7
    # Largest prime is 13 -> 1+3 = 4
    assert module_0.skjkasdkd([10, 11, 12, 13]) == 4
    # Only even composite numbers -> 0
    assert module_0.skjkasdkd([6, 8, 10, 12]) == 0
    # Largest prime is 97 -> 9+7 = 16
    assert module_0.skjkasdkd([97, 4, 89, 15]) == 16
    # Prime 2 is the only prime -> 2
    assert module_0.skjkasdkd([2]) == 2

# Generated at 2026-11-03 05:04:14.873743
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # nonce:648e2d98
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 10]) == 25
    # Largest prime is 7 -> 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7
    # Composite numbers larger than primes must be ignored
    assert module_0.skjkasdkd([7, 100, 121, 4]) == 7
    # No primes present -> maxx stays 0 -> digit sum 0
    assert module_0.skjkasdkd([4, 6, 8, 9, 10]) == 0
    # Empty list -> 0
    assert module_0.skjkasdkd([]) == 0
    # Single prime element
    assert module_0.skjkasdkd([13]) == 4
    # Duplicate largest primes
    assert module_0.skjkasdkd([2, 3, 5, 11, 11]) == 2
    # Largest prime appearing first
    assert module_0.skjkasdkd([29, 2, 3, 4]) == 11

# Generated at 2026-11-03 05:07:13.520631
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    # Largest prime is 5107 -> 5+1+0+7 = 13
    assert module_0.skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3]) == 13
    # Largest prime is 83 -> 8+3 = 11
    assert module_0.skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6]) == 11
    # Largest prime is 3 -> 3
    assert module_0.skjkasdkd([0, 81, 12, 3, 1, 21]) == 3
    # Largest prime is 7 -> 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7
    # Single prime element
    assert module_0.skjkasdkd([13]) == 4
    # No primes greater than 0 -> maxx stays 0 -> digit sum 0
    assert module_0.skjkasdkd([0, 0, 0]) == 0
    # Large prime at end
    assert module_0.skjkasdkd([2, 4, 6, 999983]) == 9 + 9 + 9 + 9 + 8 + 3
    print("All tests passed!")


test_skjkasdkd()

# Generated at 2026-11-03 05:11:05.971329
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> digit sum 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10

    # Largest prime is 4597 -> digit sum 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25

    # Largest prime is 7 -> digit sum 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7

    # Largest prime is 13 -> digit sum 1+3 = 4
    assert module_0.skjkasdkd([2, 3, 5, 7, 11, 13]) == 4

    # Single element list with a prime -> 97 -> 9+7 = 16
    assert module_0.skjkasdkd([97]) == 16

    # No primes in list (all composite) -> maxx stays 0 -> digit sum 0
    assert module_0.skjkasdkd([4, 6, 8, 9, 10]) == 0

    # Primes larger than composites should win even when composites are bigger
    # Largest prime is 29 -> 2+9 = 11
    assert module_0.skjkasdkd([100, 29, 28, 27]) == 11

    # Two-digit prime at the end -> 53 -> 5+3 = 8
    assert module_0.skjkasdkd([10, 20, 30, 53]) == 8