

# Generated at 2026-11-03 01:06:01.225142
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    # Single prime element
    assert module_0.skjkasdkd([7]) == 7
    assert module_0.skjkasdkd([2, 3]) == 3
    # Largest prime appears later in the list
    assert module_0.skjkasdkd([4, 6, 9, 13, 15, 17]) == 8  # 17 -> 1+7
    # Prime larger than surrounding composites
    assert module_0.skjkasdkd([10, 20, 31, 33]) == 4  # 31 -> 3+1
    # No primes present -> maxx stays 0 -> digit sum 0
    assert module_0.skjkasdkd([4, 6, 8, 9, 10]) == 0
    # Empty list -> 0
    assert module_0.skjkasdkd([]) == 0
    # 1 is treated as prime by isPrime (loop body never runs)
    assert module_0.skjkasdkd([1]) == 1
    # Repeated primes
    assert module_0.skjkasdkd([5, 5, 5, 5]) == 5
    # Large prime value
    assert module_0.skjkasdkd([997, 100, 50]) == 25  # 997 -> 9+9+7
# nonce:fef54769

# Generated at 2026-11-03 01:11:28.231265
# Unit test for function skjkasdkd

# Generated at 2026-11-03 01:12:38.419265
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # nonce:82ee64d3
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 25
    assert module_0.skjkasdkd([2, 3, 5, 7, 11, 13]) == 4
    assert module_0.skjkasdkd([4, 6, 8, 9, 10]) == 0
    assert module_0.skjkasdkd([97]) == 16
    assert module_0.skjkasdkd([7]) == 7
    assert module_0.skjkasdkd([29, 2, 14, 33]) == 11

# Generated at 2026-11-03 01:13:09.762514
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 10]) == 25
    # Largest prime is 7 -> 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7
    # Largest prime is 2 -> 2
    assert module_0.skjkasdkd([0, 2, 1, 1]) == 2
    # Single prime element
    assert module_0.skjkasdkd([13]) == 4
    # No primes present -> default 0 -> digit sum 0
    assert module_0.skjkasdkd([0, 4, 6, 8, 9]) == 0
    # Empty list -> 0
    assert module_0.skjkasdkd([]) == 0
    # Large prime in list
    assert module_0.skjkasdkd([10, 997, 100, 500]) == 9 + 9 + 7
    # Duplicates of largest prime
    assert module_0.skjkasdkd([11, 11, 4, 6]) == 2

# Generated at 2026-11-03 01:14:10.776479
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # nonce:ff921bf0
    # Largest prime is 181 -> 1 + 8 + 1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10

    # Largest prime is 4597 -> 4 + 5 + 9 + 7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25

    # Largest prime is 7 -> 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7

    # Largest prime is 31 -> 3 + 1 = 4
    assert module_0.skjkasdkd([3, 31, 3, 32, 3, 32, 32, 3, 32, 3, 3, 32, 32, 32, 31, 3, 3]) == 4

    # Largest prime is 97 -> 9 + 7 = 16
    assert module_0.skjkasdkd([10, 15, 23, 8, 97, 4]) == 16

    # Single prime element
    assert module_0.skjkasdkd([2]) == 2

    # Largest prime at the start of the list
    assert module_0.skjkasdkd([11, 4, 6]) == 2  # 11 -> 1 + 1

    # Multi-digit prime mid-list
    assert module_0.skjkasdkd([4, 89, 6]) == 17  # 89 -> 8 + 9

    # No primes present -> maxx stays 0 -> digit sum 0
    assert module_0.skjkasdkd([4, 6, 8, 9, 10]) == 0

    # Empty list -> 0
    assert module_0.skjkasdkd([]) == 0

    # Duplicates of the largest prime
    assert module_0.skjkasdkd([7, 7, 7]) == 7

    # Large prime beats larger non-primes
    assert module_0.skjkasdkd([997, 4, 6, 8, 1000]) == 25  # 997 -> 9 + 9 + 7

    # Result should be an int
    assert isinstance(module_0.skjkasdkd([2, 3]), int)