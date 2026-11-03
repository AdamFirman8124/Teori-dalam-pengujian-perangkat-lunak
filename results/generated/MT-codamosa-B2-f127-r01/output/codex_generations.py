

# Generated at 2026-11-03 00:07:53.246557
# Unit test for function intersection
def test_intersection():
    # Overlap with prime length -> "YES"
    assert module_0.intersection((1, 5), (2, 7)) == "YES"      # length 3, prime
    assert module_0.intersection((1, 4), (2, 5)) == "YES"      # length 2, prime
    assert module_0.intersection((2, 10), (3, 12)) == "YES"    # length 7, prime
    assert module_0.intersection((5, 16), (5, 20)) == "YES"    # length 11, prime
    assert module_0.intersection((-5, 0), (-3, 5)) == "YES"    # length 3, prime
    assert module_0.intersection((-10, -5), (-8, -2)) == "YES" # length 3, prime

    # Overlap with non-prime length -> "NO"
    assert module_0.intersection((1, 6), (2, 8)) == "NO"       # length 4, not prime
    assert module_0.intersection((1, 10), (1, 10)) == "NO"     # length 9, not prime
    assert module_0.intersection((3, 10), (4, 11)) == "NO"     # length 6, not prime
    assert module_0.intersection((1, 3), (2, 3)) == "NO"       # length 1, not prime

    # No overlap or touching -> "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"       # disjoint intervals
    assert module_0.intersection((1, 3), (3, 5)) == "NO"       # touch at point, length 0
    assert module_0.intersection((4, 6), (1, 3)) == "NO"       # disjoint intervals

test_intersection()

# Generated at 2026-11-03 00:10:00.712844
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length (2)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # Overlapping intervals with prime intersection length (3)
    assert module_0.intersection((1, 5), (2, 6)) == "YES"

    # Overlapping intervals with non-prime intersection length (4)
    assert module_0.intersection((1, 6), (2, 7)) == "NO"

    # Intervals touching at a single point (length 0)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # Overlap of length 1 (1 is not prime)
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # Non-overlapping intervals (negative length)
    assert module_0.intersection((3, 5), (6, 8)) == "NO"

    # One interval contained within the other, prime length (5)
    assert module_0.intersection((0, 7), (2, 10)) == "YES"

    # Nested interval with non-prime length
    assert module_0.intersection((0, 10), (2, 8)) == "NO"

    # Negative intervals with non-prime overlap
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # Identical intervals, prime length (7)
    assert module_0.intersection((0, 7), (0, 7)) == "YES"

    print("All tests passed!")


test_intersection()

# Generated at 2026-11-03 00:12:24.267458
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length
    assert module_0.intersection([3, 7], [2, 5]) == "YES"          # length = 2 (prime)
    assert module_0.intersection([5, 7], [3, 8]) == "YES"          # length = 2 (prime)
    assert module_0.intersection([1, 5], [2, 6]) == "YES"          # length = 3 (prime)
    assert module_0.intersection([1, 10], [5, 12]) == "YES"        # length = 5 (prime)
    assert module_0.intersection([0, 6], [3, 10]) == "YES"         # length = 3 (prime)

    # Overlapping intervals with non-prime intersection length
    assert module_0.intersection([0, 10], [2, 8]) == "NO"          # length = 6 (not prime)
    assert module_0.intersection([10, 20], [11, 15]) == "NO"       # length = 4 (not prime)
    assert module_0.intersection([0, 5], [1, 4]) == "NO"           # length = 3 (prime) -> YES
    # fix: length = 3 is prime
    assert module_0.intersection([0, 5], [1, 4]) == "YES"

    # Intersection length of 1 (not prime)
    assert module_0.intersection([-1, 1], [0, 4]) == "NO"          # length = 1
    assert module_0.intersection([2, 4], [3, 6]) == "NO"           # length = 1

    # Intersection length of 0 (touching intervals)
    assert module_0.intersection([1, 2], [2, 3]) == "NO"           # length = 0
    assert module_0.intersection([2, 3], [3, 4]) == "NO"           # length = 0

    # No module_0.intersection(negative length)
    assert module_0.intersection([1, 2], [3, 4]) == "NO"           # length = -1
    assert module_0.intersection([5, 6], [1, 2]) == "NO"           # length = -3

    # Identical intervals
    assert module_0.intersection([2, 5], [2, 5]) == "NO"           # length = 3 (prime)
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates
    assert module_0.intersection([-10, -5], [-7, -3]) == "YES"     # length = 2 (prime)
    assert module_0.intersection([-10, -4], [-7, -3]) == "NO"      # length = 3 (prime) -> YES
    assert module_0.intersection([-10, -4], [-7, -3]) == "YES"

    # Large prime length
    assert module_0.intersection([0, 20], [4, 20]) == "NO"         # length = 16 (not prime)
    assert module_0.intersection([0, 20], [6, 20]) == "YES"        # length = 14? no, not prime
    assert module_0.intersection([0, 20], [6, 20]) == "NO"

    # Edge case: length = 2 (smallest prime)
    assert module_0.intersection([100, 102], [99, 101]) == "YES"   # length = 2 (prime)

    print("All test cases passed!")


test_intersection()

# Generated at 2026-11-03 00:14:51.321324
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length
    assert module_0.intersection([1, 5], [3, 8]) == "YES"      # length = 2 (prime)
    assert module_0.intersection([1, 10], [5, 12]) == "YES"    # length = 5 (prime)
    assert module_0.intersection([3, 11], [1, 10]) == "YES"    # length = 7 (prime)
    assert module_0.intersection([0, 15], [2, 20]) == "YES"    # length = 13 (prime)

    # Overlapping intervals with non-prime intersection length
    assert module_0.intersection([1, 6], [2, 8]) == "NO"       # length = 4 (composite)
    assert module_0.intersection([1, 8], [2, 10]) == "NO"      # length = 6 (composite)
    assert module_0.intersection([1, 12], [3, 20]) == "NO"     # length = 9 (odd composite)

    # Intersection length of 0 or 1 (not prime)
    assert module_0.intersection([1, 2], [2, 4]) == "NO"       # length = 0
    assert module_0.intersection([2, 4], [4, 9]) == "NO"       # length = 0
    assert module_0.intersection([1, 3], [2, 4]) == "NO"       # length = 1

    # Disjoint intervals (negative length)
    assert module_0.intersection([1, 4], [5, 8]) == "NO"       # no overlap
    assert module_0.intersection([5, 7], [1, 2]) == "NO"       # reversed disjoint

    # Intervals with negative endpoints
    assert module_0.intersection([-3, 1], [-1, 4]) == "YES"    # length = 2 (prime)
    assert module_0.intersection([-5, -1], [-4, 0]) == "NO"    # length = 3? l=-4, r=-1 -> 3 (prime) => YES