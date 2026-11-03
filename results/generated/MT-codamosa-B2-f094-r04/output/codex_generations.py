

# Generated at 2026-11-02 15:37:20.369841
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10

    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25

    # Largest prime is 7 -> 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7

    # Largest prime is 97 even though 100 is larger (not prime) -> 9+7 = 16
    assert module_0.skjkasdkd([100, 97]) == 16

    # Larger non-prime is ignored -> largest prime 13 -> 1+3 = 4
    assert module_0.skjkasdkd([15, 13]) == 4

    # Empty list -> maxx stays 0 -> digit sum of "0" is 0
    assert module_0.skjkasdkd([]) == 0

    # No primes present -> maxx stays 0 -> 0
    assert module_0.skjkasdkd([4, 6, 8, 9, 10]) == 0

    # Single prime element
    assert module_0.skjkasdkd([2]) == 2

    # 1 passes isPrime in this implementation -> result is 1
    assert module_0.skjkasdkd([1]) == 1

    # Negative numbers are never selected (never > maxx=0)
    assert module_0.skjkasdkd([-3, -7, 13]) == 4

    # Largest prime among several primes -> 11 -> 1+1 = 2
    assert module_0.skjkasdkd([3, 5, 7, 11]) == 2

    # Two-digit prime -> 29 -> 2+9 = 11
    assert module_0.skjkasdkd([29, 28, 27]) == 11

    print("All tests passed!")


test_skjkasdkd()

# Generated at 2026-11-02 15:38:26.373787
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    # Largest prime is 4597 -> 4+5+9+7 = 25

# Generated at 2026-11-02 15:43:03.855165
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    # Largest prime is 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7
    # Largest prime is 13 -> 1+3 = 4
    assert module_0.skjkasdkd([3, 5, 11, 13, 2]) == 4
    # Single prime element 23 -> 2+3 = 5
    assert module_0.skjkasdkd([23]) == 5
    # Empty list -> maxx stays 0 -> digit sum 0
    assert module_0.skjkasdkd([]) == 0
    # No primes present -> 0
    assert module_0.skjkasdkd([4, 6, 8, 9, 10]) == 0
    # 1 is treated as prime by isPrime -> digit sum 1
    assert module_0.skjkasdkd([1, 1, 1]) == 1
    # Repeated max prime value
    assert module_0.skjkasdkd([13, 13, 4]) == 4
    # Prime with multi-digit sum
    assert module_0.skjkasdkd([97, 89, 2]) == 16  # 97 -> 9+7
    print("All tests passed!")


test_skjkasdkd()