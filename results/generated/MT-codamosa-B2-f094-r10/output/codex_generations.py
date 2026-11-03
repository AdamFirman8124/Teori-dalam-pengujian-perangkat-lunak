

# Generated at 2026-11-02 13:37:16.633333
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> digit sum 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    # Largest prime is 4597 -> digit sum 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    # Same as above with trailing 10 instead of 1 -> still 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 10]) == 25
    # Largest prime is 7 -> digit sum 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7
    # Largest prime is 7 (2 also prime but smaller) -> 7
    assert module_0.skjkasdkd([1, 0, 8, 2, 1, 7]) == 7
    # Single prime element 2 -> 2
    assert module_0.skjkasdkd([2]) == 2
    # No primes present -> maxx stays 0 -> digit sum 0
    assert module_0.skjkasdkd([4, 6, 8, 9, 10]) == 0
    # All elements are the same prime -> 7
    assert module_0.skjkasdkd([7, 7, 7]) == 7
    # Composites larger than primes are ignored
    assert module_0.skjkasdkd([100, 101, 99, 98]) == 2  # 101 is prime -> 1+0+1 = 2
    # Negative and zero values are not prime; largest prime 3 -> 3
    assert module_0.skjkasdkd([-5, 0, 1, 3, 4, 6]) == 3
    print("All tests passed!")


test_skjkasdkd()

# Generated at 2026-11-02 13:38:30.953990
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10
    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25
    # Largest prime is 5 -> 5
    assert module_0.skjkasdkd([1,25,2,5,4,5,5,6,3]) == 5
    # Largest prime is 7 -> 7
    assert module_0.skjkasdkd([0,8,1,2,1,7]) == 7
    # Largest prime is 31 -> 3+1 = 4
    assert module_0.skjkasdkd([3,31,3,32,3,32,3,31,3,31,3,31,3,31]) == 4
    # Single element list with prime
    assert module_0.skjkasdkd([13]) == 4
    # No primes larger than 0 -> maxx stays 0, digit sum 0
    assert module_0.skjkasdkd([4, 6, 8, 9]) == 0
    # isPrime treats 1 as prime (loop range empty), so maxx becomes 1
    assert module_0.skjkasdkd([1]) == 1
    # Composites and negatives ignored; prime found
    assert module_0.skjkasdkd([-3, -2, 10, 11]) == 2

# Generated at 2026-11-02 13:39:26.590551
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1 + 8 + 1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10
    # Largest prime is 4597 -> 4 + 5 + 9 + 7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25
    # Largest prime is 7 -> 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7
    # Largest prime is 7 -> 7
    assert module_0.skjkasdkd([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 7
    # Single prime number 2 -> 2
    assert module_0.skjkasdkd([2]) == 2
    # Two primes, largest is 13 -> 1 + 3 = 4
    assert module_0.skjkasdkd([5, 13]) == 4
    # Largest prime is 101 -> 1 + 0 + 1 = 2
    assert module_0.skjkasdkd([100, 101, 4]) == 2
    # No primes in list -> maxx stays 0 -> digit sum of "0" = 0
    assert module_0.skjkasdkd([4, 6, 8, 9]) == 0
    # Empty list -> maxx stays 0 -> 0
    assert module_0.skjkasdkd([]) == 0
    # Large prime -> 9 + 9 + 9 + 9 + 8 + 9 = 53
    assert module_0.skjkasdkd([10, 999983]) == 53

# Generated at 2026-11-02 13:40:14.707921
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10

    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25

    # Largest prime is 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7

    # Largest prime is 7 among composites
    assert module_0.skjkasdkd([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6]) == 7

    # Single prime element
    assert module_0.skjkasdkd([13]) == 4

    # Largest prime among several primes
    assert module_0.skjkasdkd([11, 13, 2, 7]) == 4

    # Composite larger than any prime is ignored
    assert module_0.skjkasdkd([10, 7]) == 7

    # Duplicates of the maximum prime
    assert module_0.skjkasdkd([97, 97, 89]) == 16

    # No primes in the list -> digit sum of 0
    assert module_0.skjkasdkd([4, 6, 8, 9, 10]) == 0

    # Empty list -> 0
    assert module_0.skjkasdkd([]) == 0

    # Large prime near one million -> 9+9+9+9+8+3 = 47
    assert module_0.skjkasdkd([999983]) == 47

# Generated at 2026-11-02 13:41:22.104323
# Unit test for function skjkasdkd
def test_skjkasdkd():
    # Largest prime is 181 -> 1+8+1 = 10
    assert module_0.skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3]) == 10

    # Largest prime is 4597 -> 4+5+9+7 = 25
    assert module_0.skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1]) == 25

    # Largest prime is 7 -> 7
    assert module_0.skjkasdkd([0, 8, 1, 2, 1, 7]) == 7

    # Largest prime is 31 -> 3+1 = 4
    assert module_0.skjkasdkd([3, 31, 7, 2, 13, 7, 3, 5, 4, 7, 2, 3, 4, 7, 2, 3, 5, 1, 3, 4, 4, 5]) == 4

    # Single prime element: 13 -> 1+3 = 4
    assert module_0.skjkasdkd([13]) == 4

    # Single element list with 2 -> 2
    assert module_0.skjkasdkd([2]) == 4 // 2  # sum of digits of 2 is 2

    # No primes in list -> maxx stays 0 -> sum of digits of "0" is 0
    assert module_0.skjkasdkd([4, 6, 8, 9, 10, 12]) == 0

    # Empty list -> returns 0
    assert module_0.skjkasdkd([]) == 0

    # 1 is treated as prime by isPrime (loop range is empty) -> digit sum of 1 is 1
    assert module_0.skjkasdkd([1]) == 1

    # Mixed list where 1 and 2 are present -> largest "prime" is 2 -> 2
    assert module_0.skjkasdkd([1, 2]) == 2

    # Primes with same digit sum but different values: largest prime 101 -> 1+0+1 = 2
    assert module_0.skjkasdkd([101, 11, 7]) == 2

    # Large prime: 999983 -> 9+9+9+9+8+3 = 47
    assert module_0.skjkasdkd([999983, 3, 5]) == 47