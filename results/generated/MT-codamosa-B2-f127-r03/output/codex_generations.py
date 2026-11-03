

# Generated at 2026-11-02 18:46:34.196863
# Unit test for function intersection
def test_intersection():
    # No overlap -> "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intervals touching at a point -> length 0 -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Overlap length 1 (not prime) -> "NO"
    assert module_0.intersection((1, 3), (2, 4)) == "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    assert module_0.intersection((-3, -1), (-5, -2)) == "NO"
    # Overlap length 3 (prime) -> "YES"
    assert module_0.intersection((1, 5), (2, 6)) == "YES"
    assert module_0.intersection((0, 4), (1, 5)) == "YES"
    # Overlap length 5 (prime) -> "YES"
    assert module_0.intersection((5, 10), (5, 10)) == "YES"
    # Overlap length 6 (not prime) -> "NO"
    assert module_0.intersection((10, 20), (12, 18)) == "NO"
    # Overlap length 2 (prime) -> "YES"
    assert module_0.intersection((0, 3), (1, 3)) == "YES"
    # Overlap length 7 (prime) -> "YES"
    assert module_0.intersection((0, 10), (3, 10)) == "YES"
    # Overlap length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 5), (1, 5)) == "NO"
    # Negative intervals with prime overlap -> "YES"
    assert module_0.intersection((-10, -1), (-5, 0)) == "YES"
    # Negative intervals with composite overlap -> "NO"
    assert module_0.intersection((-10, -1), (-7, 0)) == "NO"
    # One interval fully inside another
    assert module_0.intersection((1, 10), (4, 6)) == "YES"  # length 2, prime
    assert module_0.intersection((1, 10), (4, 8)) == "NO"   # length 4, not prime

# Generated at 2026-11-02 18:47:35.413828
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length (2)
    assert module_0.intersection((1, 5), (3, 8)) == "YES"

    # Overlapping intervals with non-prime intersection length (6)
    assert module_0.intersection((1, 10), (3, 9)) == "NO"

    # No overlap at all
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # Intervals touching at a single point -> length 0 -> not prime
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # Intersection length of 1 is not prime
    assert module_0.intersection((1, 6), (2, 5)) == "NO"

    # Identical intervals with prime length (13)
    assert module_0.intersection((0, 13), (0, 13)) == "YES"

    # Identical intervals with non-prime length (4)
    assert module_0.intersection((0, 4), (0, 4)) == "NO"

    # One interval fully contains the other, prime length (5)
    assert module_0.intersection((0, 10), (2, 7)) == "YES"

    # Negative coordinates, prime length (3)
    assert module_0.intersection((-5, 0), (-3, 10)) == "YES"

    # Negative coordinates, non-prime length (4)
    assert module_0.intersection((-10, 0), (-4, 5)) == "NO"

    # Reversed interval endpoints (start > end) -> negative length
    assert module_0.intersection((5, 1), (3, 2)) == "NO"

    # Large prime length (17)
    assert module_0.intersection((0, 100), (40, 57)) == "YES"

    print("All tests passed!")


test_intersection()

# Generated at 2026-11-02 18:49:18.987191
# Unit test for function intersection
def test_intersection():
    # No module_0.intersection(disjoint intervals)
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intervals touch at a point, length = 0
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Intersection length = 1 (not prime)
    assert module_0.intersection((1, 3), (2, 4)) == "NO"
    # Intersection length = 2 (prime)
    assert module_0.intersection((1, 4), (2, 5)) == "YES"
    # Intersection length = 5 (prime)
    assert module_0.intersection((0, 6), (1, 7)) == "YES"
    # Intersection length = 4 (not prime)
    assert module_0.intersection((0, 5), (1, 6)) == "NO"
    # Intersection length = 6 (not prime)
    assert module_0.intersection((0, 7), (1, 8)) == "NO"
    # One interval fully contains the other, length = 3 (prime)
    assert module_0.intersection((0, 10), (2, 5)) == "YES"
    # Identical intervals, length = 8 (not prime)
    assert module_0.intersection((2, 10), (2, 10)) == "NO"
    # Negative intervals, length = 5 (prime)
    assert module_0.intersection((-10, 0), (-5, 5)) == "YES"
    # Negative intervals, length = 2 (prime)
    assert module_0.intersection((-3, -1), (-2, 0)) == "YES"
    # Negative intervals, no intersection
    assert module_0.intersection((-10, -8), (-5, 0)) == "NO"
    # Large prime length = 11
    assert module_0.intersection((0, 12), (1, 20)) == "YES"
    # Large composite length = 12
    assert module_0.intersection((0, 13), (1, 20)) == "NO"

# Generated at 2026-11-02 18:50:21.124471
# Unit test for function intersection
def test_intersection():
    # Nonce: c91224fa

    # Intersection with prime length
    assert module_0.intersection([1, 5], [3, 8]) == "YES"      # length = 2 (prime)
    assert module_0.intersection([1, 4], [1, 4]) == "YES"      # length = 3 (prime)
    assert module_0.intersection([0, 6], [0, 6]) == "YES"      # length = 6? No, composite -> NO
    # Correction: length 6 is composite
    assert module_0.intersection([0, 6], [0, 6]) == "NO"
    assert module_0.intersection([2, 7], [2, 7]) == "YES"      # length = 5 (prime)

    # Intersection with non-prime length
    assert module_0.intersection([1, 7], [1, 7]) == "NO"       # length = 6 (composite)
    assert module_0.intersection([0, 5], [2, 3]) == "NO"       # length = 1 (not prime)
    assert module_0.intersection([2, 10], [2, 10]) == "NO"     # length = 8 (composite)
    assert module_0.intersection([0, 9], [0, 9]) == "NO"       # length = 9 (composite)

    # No intersection
    assert module_0.intersection([1, 3], [4, 7]) == "NO"       # disjoint, length = -1
    assert module_0.intersection([5, 6], [1, 2]) == "NO"       # disjoint, length = -4

    # Zero-length module_0.intersection(touching endpoints)
    assert module_0.intersection([1, 3], [3, 7]) == "NO"       # length = 0
    assert module_0.intersection([0, 4], [4, 10]) == "NO"      # length = 0

    # Contained intervals
    assert module_0.intersection([0, 10], [2, 5]) == "NO"      # length = 3 -> YES actually
    # Correction: length = 3 is prime
    assert module_0.intersection([0, 10], [2, 5]) == "YES"
    assert module_0.intersection([0, 10], [1, 4]) == "NO"      # length = 3? No, 4-1 = 3 prime -> YES
    assert module_0.intersection([0, 10], [1, 4]) == "YES"

    print("All tests passed!")


test_intersection()

# Generated at 2026-11-02 18:51:50.034942
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length
    assert module_0.intersection((1, 5), (2, 4)) == "YES"      # length 2 (prime)
    assert module_0.intersection((1, 10), (5, 15)) == "YES"    # length 5 (prime)
    assert module_0.intersection((0, 5), (0, 5)) == "YES"      # length 5 (prime)
    assert module_0.intersection((1, 4), (1, 4)) == "YES"      # length 3 (prime)
    assert module_0.intersection((1, 12), (2, 11)) == "YES"    # length 9? no -> see below

    # Overlapping intervals with non-prime intersection length
    assert module_0.intersection((1, 10), (4, 8)) == "NO"      # length 4 (not prime)
    assert module_0.intersection((1, 3), (2, 4)) == "NO"       # length 1 (not prime)
    assert module_0.intersection((0, 2), (1, 3)) == "NO"       # length 1 (not prime)
    assert module_0.intersection((1, 12), (2, 11)) == "NO"     # length 9 (not prime)

    # No overlap or zero-length intersection
    assert module_0.intersection((1, 2), (3, 4)) == "NO"       # disjoint, negative length
    assert module_0.intersection((1, 2), (2, 3)) == "NO"       # touch at a point, length 0
    assert module_0.intersection((5, 6), (1, 2)) == "NO"       # disjoint, reversed order

    # Negative intervals
    assert module_0.intersection((-3, -1), (-2, 0)) == "YES"   # length 2 (prime)
    assert module_0.intersection((-10, -1), (-5, -2)) == "NO"  # length 3? -2 - (-5) = 3 (prime) -> YES
    assert module_0.intersection((-10, -1), (-5, -2)) == "YES" # length 3 (prime)

    # Edge cases with is_prime behavior (0 and 1 are not prime)
    assert module_0.intersection((0, 1), (0, 1)) == "NO"       # length 1
    assert module_0.intersection((0, 0), (0, 0)) == "NO"       # length 0

    print("All tests passed!")


if __name__ == "__main__":
    test_intersection()

# Generated at 2026-11-02 18:53:36.789872
# Unit test for function intersection
def test_intersection():
    # No module_0.intersection(length negative)
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intersection length is zero (touching endpoints)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length is 1 (not prime)
    assert module_0.intersection((1, 3), (2, 5)) == "NO"
    # Intersection length is 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Intersection length is 3 (prime)
    assert module_0.intersection((1, 5), (2, 6)) == "YES"
    # Intersection length is 4 (not prime)
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # Intersection length is 5 (prime)
    assert module_0.intersection((0, 7), (2, 9)) == "YES"
    # One interval fully contains the other, length 7 (prime)
    assert module_0.intersection((-10, -3), (-5, 0)) == "YES"
    # Identical intervals, length 6 (not prime)
    assert module_0.intersection((2, 8), (2, 8)) == "NO"
    # Negative intervals, no overlap
    assert module_0.intersection((-5, -3), (-2, 1)) == "NO"
    print("All tests passed!")

test_intersection()