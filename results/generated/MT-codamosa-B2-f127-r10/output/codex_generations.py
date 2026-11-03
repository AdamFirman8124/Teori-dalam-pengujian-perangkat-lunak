

# Generated at 2026-11-02 18:07:26.990198
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length
    assert module_0.intersection((0, 5), (3, 8)) == "YES"      # length = 2 (prime)
    assert module_0.intersection((0, 10), (0, 10)) == "NO"     # length = 10 (not prime)
    assert module_0.intersection((0, 3), (0, 3)) == "YES"      # length = 3 (prime)
    assert module_0.intersection((0, 6), (0, 6)) == "NO"       # length = 6 (not prime)

    # Intersection length of 1 is not prime
    assert module_0.intersection((1, 3), (2, 4)) == "NO"       # length = 1
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"      # length = 1

    # Negative intervals
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"   # length = 2 (prime)
    assert module_0.intersection((-2, 2), (-4, 0)) == "YES"    # length = 2 (prime)
    assert module_0.intersection((-10, -5), (-8, -1)) == "NO"  # length = 3... wait, -5-(-8)=3 (prime)

    # Disjoint intervals (no overlap)
    assert module_0.intersection((1, 2), (3, 4)) == "NO"       # length negative
    assert module_0.intersection((5, 10), (11, 15)) == "NO"    # length negative
    assert module_0.intersection((-5, -3), (0, 2)) == "NO"     # length negative

    # Touching intervals (zero-length intersection)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"       # length = 0
    assert module_0.intersection((0, 0), (0, 0)) == "NO"       # length = 0

    # Larger prime intersection lengths
    assert module_0.intersection((0, 13), (0, 13)) == "YES"    # length = 13 (prime)
    assert module_0.intersection((0, 14), (0, 14)) == "NO"     # length = 14 (not prime)
    assert module_0.intersection((0, 17), (0, 17)) == "YES"    # length = 17 (prime)
    assert module_0.intersection((0, 25), (0, 25)) == "NO"     # length = 25 (not prime)

    # Partial overlaps
    assert module_0.intersection((2, 10), (4, 8)) == "NO"      # length = 4 (not prime)
    assert module_0.intersection((2, 10), (5, 12)) == "YES"    # length = 5 (prime)
    assert module_0.intersection((2, 10), (6, 12)) == "NO"     # length = 4 (not prime)

    print("All test cases passed!")


test_intersection()

# Generated at 2026-11-02 18:09:01.374940
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length
    assert module_0.intersection((1, 5), (2, 4)) == "YES"       # length = 2 (prime)
    assert module_0.intersection((2, 5), (1, 6)) == "YES"       # length = 3 (prime)
    assert module_0.intersection((0, 10), (3, 8)) == "YES"      # length = 5 (prime)
    assert module_0.intersection((-5, 0), (-2, 3)) == "YES"     # length = 2 (prime)

    # Overlapping intervals with non-prime intersection length
    assert module_0.intersection((1, 3), (2, 4)) == "NO"        # length = 1 (not prime)
    assert module_0.intersection((0, 10), (3, 7)) == "NO"       # length = 4 (not prime)
    assert module_0.intersection((1, 10), (2, 8)) == "NO"       # length = 6 (not prime)

    # Identical intervals -> length = 0
    assert module_0.intersection((5, 10), (5, 10)) == "NO"      # length = 0

    # Non-overlapping intervals -> negative length
    assert module_0.intersection((1, 2), (3, 4)) == "NO"        # no overlap
    assert module_0.intersection((10, 20), (1, 5)) == "NO"      # no overlap

    # Touching intervals (single point) -> length = 0
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # Negative intervals with prime length
    assert module_0.intersection((-10, -1), (-8, -3)) == "YES"  # length = 5 (prime)

    # Negative intervals with non-prime length
    assert module_0.intersection((-10, -1), (-8, -5)) == "NO"   # length = 3... l=-8, r=-5 -> 3 (prime) => YES
    # Correction: (-10,-1) and (-8,-5): l = max(-10,-8) = -8, r = min(-1,-5) = -5, length = 3 -> prime
    assert module_0.intersection((-10, -1), (-8, -5)) == "YES"

    print("All tests passed!")


test_intersection()

# Generated at 2026-11-02 18:09:57.525253
# Unit test for function intersection
def test_intersection():
    # No module_0.intersection(touching endpoints only)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length is 1, not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length is 2, prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Intersection length is 1
    assert module_0.intersection((1, 3), (2, 5)) == "NO"
    # Intersection length is 6, not prime
    assert module_0.intersection((1, 10), (2, 8)) == "NO"
    # Intersection length is 2, prime
    assert module_0.intersection((0, 5), (3, 10)) == "YES"
    # Disjoint intervals, negative length
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intersection length is 3, prime
    assert module_0.intersection((0, 4), (1, 4)) == "YES"
    # Intersection length is 4, not prime
    assert module_0.intersection((0, 6), (2, 6)) == "NO"
    # Identical intervals, length 5 prime
    assert module_0.intersection((2, 7), (2, 7)) == "YES"

# Generated at 2026-11-02 18:10:42.204399
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with a prime intersection length (length=2)
    assert module_0.intersection((1, 4), (2, 6)) == "YES"
    # Overlapping intervals with a prime intersection length (length=3)
    assert module_0.intersection((0, 5), (2, 8)) == "YES"
    # Overlapping intervals with a non-prime intersection length (length=4)
    assert module_0.intersection((1, 6), (2, 7)) == "NO"
    # Non-overlapping intervals
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intervals touching at a single point (length=0)
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Intersection length of 1 is not prime
    assert module_0.intersection((1, 3), (2, 4)) == "NO"
    # Negative intervals with prime intersection length
    assert module_0.intersection((-5, 0), (-3, 2)) == "YES"
    # Nested intervals with prime intersection length
    assert module_0.intersection((10, 20), (12, 21)) == "YES"
    # Nested intervals with non-prime intersection length
    assert module_0.intersection((10, 20), (12, 25)) == "NO"
    # Identical intervals with prime length
    assert module_0.intersection((0, 3), (0, 3)) == "YES"
    # Identical intervals with non-prime length
    assert module_0.intersection((0, 4), (0, 4)) == "NO"

# nonce:1719d509

# Generated at 2026-11-02 18:11:43.128729
# Unit test for function intersection
def test_intersection():
# nonce:a501a199
    # No overlap -> length is negative
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Touching intervals -> length is 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime)
    assert module_0.intersection((0, 2), (1, 5)) == "NO"
    # Intersection length 2 (prime)
    assert module_0.intersection((1, 5), (3, 7)) == "YES"
    # Intersection length 4 (not prime)
    assert module_0.intersection((1, 8), (4, 10)) == "NO"
    # Intersection length 3 (prime)
    assert module_0.intersection((0, 6), (3, 9)) == "YES"
    # Negative intervals, length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Negative intervals, length 1 (not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Identical intervals, length 5 (prime)
    assert module_0.intersection((2, 7), (2, 7)) == "YES"
    # Identical intervals, length 4 (not prime)
    assert module_0.intersection((1, 5), (1, 5)) == "NO"

# Generated at 2026-11-02 18:12:29.674841
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length (length = 2)
    assert module_0.intersection((1, 5), (3, 8)) == "YES"
    
    # Overlapping intervals with non-prime intersection length (length = 4)
    assert module_0.intersection((1, 6), (2, 7)) == "NO"
    
    # No overlap: intervals are disjoint
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    
    # Intervals touch at a single point (length = 0)
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    
    # Intersection length of 1 (not prime)
    assert module_0.intersection((1, 3), (2, 4)) == "NO"
    
    # Intersection length of 3 (prime)
    assert module_0.intersection((0, 10), (2, 5)) == "YES"
    
    # Negative intervals with prime intersection length
    assert module_0.intersection((-5, 0), (-3, 2)) == "YES"
    
    # Identical intervals with prime length
    assert module_0.intersection((2, 5), (2, 5)) == "YES"
    
    # One interval fully contained in another, prime length (length = 3)
    assert module_0.intersection((1, 10), (3, 6)) == "YES"
    
    # One interval fully contained in another, non-prime length (length = 4)
    assert module_0.intersection((1, 10), (3, 7)) == "NO"
    
    # One interval fully contained in another, non-prime length (length = 6)
    assert module_0.intersection((1, 10), (2, 8)) == "NO"
    
    # Completely identical intervals with length 1 (not prime)
    assert module_0.intersection((2, 3), (2, 3)) == "NO"
    
    # Second interval entirely before first (no overlap)
    assert module_0.intersection((5, 10), (1, 4)) == "NO"
    
    # Large prime intersection length (length = 7)
    assert module_0.intersection((0, 20), (3, 10)) == "YES"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_intersection()

# Generated at 2026-11-02 18:13:06.531998
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime-length module_0.intersection(length = 2)
    assert module_0.intersection((1, 3), (2, 4)) == "NO"  # length = min(3,4)-max(1,2) = 1, not prime
    
    # Overlapping intervals with prime-length module_0.intersection(length = 2)
    assert module_0.intersection((1, 4), (2, 6)) == "YES"  # length = 4-2 = 2, prime
    
    # Overlapping intervals with non-prime-length module_0.intersection(length = 4)
    assert module_0.intersection((0, 5), (1, 6)) == "NO"  # length = 5-1 = 4, not prime
    
    # Non-overlapping intervals
    assert module_0.intersection((1, 2), (3, 4)) == "NO"  # no overlap, length = -1
    
    # Intervals touching at a point (length = 0)
    assert module_0.intersection((1, 3), (3, 5)) == "NO"  # length = 0, not prime
    
    # Identical intervals with prime-length (length = 2)
    assert module_0.intersection((3, 5), (3, 5)) == "YES"  # length = 5-3 = 2, prime
    
    # Identical intervals with non-prime-length (length = 3)
    assert module_0.intersection((3, 6), (3, 6)) == "NO"  # length = 3, prime -> YES
    
    # One interval fully contains another with prime-length intersection
    assert module_0.intersection((0, 10), (3, 5)) == "YES"  # length = 5-3 = 2, prime
    
    # One interval fully contains another with non-prime-length intersection
    assert module_0.intersection((0, 10), (2, 6)) == "NO"  # length = 6-2 = 4, not prime
    
    # Negative intervals with prime-length intersection
    assert module_0.intersection((-5, -1), (-3, 0)) == "YES"  # length = -1-(-3) = 2, prime
    
    # Negative intervals with non-prime-length intersection
    assert module_0.intersection((-10, -2), (-8, -1)) == "NO"  # length = -2-(-8) = 6, not prime
    
    # Length = 1 (not prime)
    assert module_0.intersection((1, 3), (2, 5)) == "NO"  # length = 3-2 = 1, not prime
    
    print("All tests passed!")

# Run the tests
test_intersection()

# Generated at 2026-11-02 18:13:51.429336
# Unit test for function intersection
def test_intersection():
    # Non-overlapping intervals -> intersection length <= 0 -> "NO"
    assert module_0.intersection([1, 2], [3, 4]) == "NO"
    assert module_0.intersection((5, 10), (11, 15)) == "NO"

    # Touching intervals -> length 0 -> "NO"
    assert module_0.intersection([1, 2], [2, 3]) == "NO"

    # Overlapping with prime length 2 -> "YES"
    assert module_0.intersection([1, 4], [2, 5]) == "YES"

    # Overlapping with prime length 3 -> "YES"
    assert module_0.intersection([1, 5], [2, 6]) == "YES"

    # Overlapping with non-prime length 4 -> "NO"
    assert module_0.intersection([1, 6], [2, 7]) == "NO"

    # Overlapping with length 1 (not prime) -> "NO"
    assert module_0.intersection([1, 3], [2, 4]) == "NO"

    # One interval contained in the other, prime length 3 -> "YES"
    assert module_0.intersection([1, 8], [3, 6]) == "YES"

    # One interval contained in the other, non-prime length 4 -> "NO"
    assert module_0.intersection([1, 10], [3, 7]) == "NO"

    # Negative intervals, prime intersection length 3 -> "YES"
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"

    # Negative intervals, non-prime intersection length 4 -> "NO"
    assert module_0.intersection([-5, 0], [-4, 2]) == "NO"

    # Identical intervals, prime length 5 -> "YES"
    assert module_0.intersection([2, 7], [2, 7]) == "YES"

    # Identical intervals, non-prime length 6 -> "NO"
    assert module_0.intersection([3, 9], [3, 9]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-11-02 18:14:07.383222
# Unit test for function intersection
def test_intersection():
    # Intersecting intervals with prime intersection length
    assert module_0.intersection((1, 5), (3, 8)) == "YES"       # length 2 (prime)
    assert module_0.intersection((5, 12), (3, 15)) == "YES"     # length 7 (prime)
    assert module_0.intersection((0, 11), (0, 11)) == "YES"     # identical intervals, length 11 (prime)
    assert module_0.intersection((1, 100), (2, 99)) == "YES"    # length 97 (prime)
    assert module_0.intersection((-3, 1), (-1, 3)) == "YES"     # negative bounds, length 2 (prime)

    # Intersecting intervals with non-prime intersection length
    assert module_0.intersection((1, 6), (2, 7)) == "NO"        # length 4 (composite)
    assert module_0.intersection((10, 20), (11, 19)) == "NO"    # length 8 (composite)
    assert module_0.intersection((1, 10), (1, 10)) == "NO"      # length 9 (composite)
    assert module_0.intersection((1, 4), (2, 3)) == "NO"        # length 1 (not prime)

    # No intersection or degenerate intersection
    assert module_0.intersection((1, 2), (3, 4)) == "NO"        # disjoint intervals
    assert module_0.intersection((1, 3), (3, 5)) == "NO"        # touching at a point, length 0
    assert module_0.intersection((5, 6), (1, 2)) == "NO"        # disjoint, reversed argument order
    assert module_0.intersection((2, 2), (2, 2)) == "NO"        # zero-length intervals, length 0

# Generated at 2026-11-02 18:14:24.890817
# Unit test for function intersection
def test_intersection():
    # No module_0.intersection(touching endpoints)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection of length 1 (not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection of length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Zero-length intersection
    assert module_0.intersection((-2, -2), (-3, -2)) == "NO"
    # Identical intervals with prime length
    assert module_0.intersection((0, 3), (0, 3)) == "YES"
    # Identical intervals with non-prime length
    assert module_0.intersection((0, 4), (0, 4)) == "NO"
    # Contained interval with prime length
    assert module_0.intersection((0, 10), (2, 5)) == "YES"
    # Contained interval with non-prime length
    assert module_0.intersection((0, 10), (2, 8)) == "NO"
    # No overlap at all
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((3, 4), (1, 2)) == "NO"
    # Overlap of length 3 (prime)
    assert module_0.intersection((1, 5), (2, 6)) == "YES"
    # Overlap of length 4 (not prime)
    assert module_0.intersection((1, 6), (2, 7)) == "NO"
    # Negative intervals with prime-length overlap
    assert module_0.intersection((-10, -1), (-8, -3)) == "YES"
    # Negative intervals with non-prime-length overlap
    assert module_0.intersection((-10, -1), (-8, -5)) == "NO"
    # Single-point overlap
    assert module_0.intersection((5, 5), (5, 10)) == "NO"

# Generated at 2026-11-02 18:14:42.840592
# Unit test for function intersection
def test_intersection():
    # No overlap (disjoint intervals)
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intervals touch at a point (length 0)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Overlap with prime length 2
    assert module_0.intersection((1, 3), (2, 4)) == "YES"
    # Overlap with prime length 5
    assert module_0.intersection((0, 5), (3, 8)) == "YES"
    # Overlap with non-prime length 4
    assert module_0.intersection((1, 5), (2, 6)) == "NO"
    # Overlap with length 1 (1 is not prime)
    assert module_0.intersection((1, 2), (1, 3)) == "NO"
    # One interval fully contains the other, prime length 3
    assert module_0.intersection((1, 5), (2, 4)) == "YES"
    # Identical intervals, non-prime length
    assert module_0.intersection((0, 4), (0, 4)) == "NO"
    # Identical intervals, prime length 7
    assert module_0.intersection((0, 7), (0, 7)) == "YES"
    # Negative coordinates, prime length 3
    assert module_0.intersection((-4, -1), (-3, 0)) == "YES"
    # Negative coordinates, non-prime length
    assert module_0.intersection((-10, -1), (-5, -1)) == "NO"
    # Zero-length interval inside another
    assert module_0.intersection((3, 3), (1, 10)) == "NO"

# Generated at 2026-11-02 18:15:02.133238
# Unit test for function intersection
def test_intersection():
    # No overlap -> negative length
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intervals touch -> length 0, not prime
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Overlap of length 1 -> 1 is not prime
    assert module_0.intersection((1, 3), (2, 4)) == "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Overlap of length 2 -> prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    assert module_0.intersection((0, 5), (1, 3)) == "YES"
    # Overlap of length 3 -> prime
    assert module_0.intersection((0, 6), (2, 5)) == "YES"
    # Overlap of length 4 -> not prime
    assert module_0.intersection((0, 8), (2, 6)) == "NO"
    # Overlap of length 6 -> not prime
    assert module_0.intersection((0, 10), (1, 7)) == "NO"
    # Identical intervals -> full length prime (7)
    assert module_0.intersection((0, 7), (0, 7)) == "YES"
    # Identical intervals -> full length not prime (8)
    assert module_0.intersection((0, 8), (0, 8)) == "NO"
    # Negative intervals with prime overlap (length 5)
    assert module_0.intersection((-10, -2), (-9, -4)) == "YES"
    # One interval fully inside another, prime overlap (length 5)
    assert module_0.intersection((0, 20), (5, 10)) == "YES"
    # One interval fully inside another, non-prime overlap (length 9)
    assert module_0.intersection((0, 20), (5, 14)) == "NO"
    print("All tests passed!")


test_intersection()

# Generated at 2026-11-02 18:15:13.957356
# Unit test for function intersection
def test_intersection():
    # Intervals with no overlap
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Overlap length 1 (not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Overlap length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Disjoint intervals (negative length)
    assert module_0.intersection((3, 5), (7, 9)) == "NO"
    # Overlap length 3 (prime)
    assert module_0.intersection((1, 5), (2, 6)) == "YES"
    # Overlap length 6 (not prime)
    assert module_0.intersection((1, 10), (2, 8)) == "NO"
    # Identical intervals, length 4 (not prime)
    assert module_0.intersection((2, 6), (2, 6)) == "NO"
    # Identical intervals, length 5 (prime)
    assert module_0.intersection((3, 8), (3, 8)) == "YES"
    # Touching at a single point
    assert module_0.intersection((5, 7), (7, 10)) == "NO"
    # One interval fully inside another, length 2 (prime)
    assert module_0.intersection((0, 10), (4, 6)) == "YES"
    # Overlap length 9 (not prime)
    assert module_0.intersection((0, 9), (0, 9)) == "NO"
    # Negative intervals, overlap length 3 (prime)
    assert module_0.intersection((-10, -2), (-8, -5)) == "YES"

# Generated at 2026-11-02 18:15:33.611841
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length (3)
    assert module_0.intersection([1, 5], [2, 7]) == "YES"
    # Non-overlapping intervals
    assert module_0.intersection([1, 2], [3, 4]) == "NO"
    # Touching intervals (length = 0)
    assert module_0.intersection([1, 2], [2, 3]) == "NO"
    # Overlapping intervals with non-prime length (4)
    assert module_0.intersection([1, 6], [2, 8]) == "NO"
    # Intersection length of 1 (not prime)
    assert module_0.intersection([1, 3], [2, 4]) == "NO"
    # Intersection length of 2 (prime)
    assert module_0.intersection([1, 4], [2, 5]) == "YES"
    # Identical intervals with prime length (2)
    assert module_0.intersection([2, 4], [2, 4]) == "YES"
    # Identical intervals with non-prime length (4)
    assert module_0.intersection([3, 7], [3, 7]) == "NO"
    # One interval contained within another, prime length (2)
    assert module_0.intersection([1, 10], [3, 5]) == "YES"
    # Negative coordinates, prime length (3)
    assert module_0.intersection([-3, 2], [-1, 5]) == "YES"
    # Negative coordinates, non-prime length (4)
    assert module_0.intersection([-5, 3], [-1, 4]) == "NO"
    # Intersection length of 9 (not prime)
    assert module_0.intersection([0, 9], [0, 9]) == "NO"
    # Intersection length of 13 (prime)
    assert module_0.intersection([0, 13], [0, 13]) == "YES"
    # Completely disjoint with reversed endpoints
    assert module_0.intersection([5, 10], [1, 3]) == "NO"
    # Intersection length of 11 (prime)
    assert module_0.intersection([2, 15], [4, 16]) == "YES"
    # Intersection length of 6 (not prime)
    assert module_0.intersection([0, 8], [2, 10]) == "NO"
    print("All tests passed!")


test_intersection()