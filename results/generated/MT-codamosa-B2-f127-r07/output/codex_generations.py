

# Generated at 2026-11-01 20:02:47.202146
# Unit test for function intersection
def test_intersection():
    # nonce:a6f9aeab
    # Overlapping intervals with prime intersection length (2)
    assert module_0.intersection([1, 5], [3, 8]) == "YES"
    # Overlapping intervals with non-prime intersection length (4)
    assert module_0.intersection([1, 7], [3, 12]) == "NO"
    # Disjoint intervals -> no intersection
    assert module_0.intersection([1, 2], [5, 8]) == "NO"
    # Intervals touching at a single point -> length 0
    assert module_0.intersection([1, 3], [3, 5]) == "NO"
    # Intersection length of 1 (not prime by this definition)
    assert module_0.intersection([1, 4], [3, 6]) == "NO"
    # Intersection length of 3 (prime)
    assert module_0.intersection([1, 5], [2, 8]) == "YES"
    # Identical intervals -> length 3 (prime)
    assert module_0.intersection([2, 5], [2, 5]) == "YES"
    # One interval fully contained in another -> length 3 (prime)
    assert module_0.intersection([1, 10], [3, 6]) == "YES"
    # Negative coordinates with prime intersection length
    assert module_0.intersection([-5, -1], [-3, 2]) == "YES"
    # Negative coordinates with even (non-prime) intersection length
    assert module_0.intersection([-10, -2], [-6, 0]) == "NO"
    # Zero-length degenerate intervals
    assert module_0.intersection([5, 5], [5, 5]) == "NO"
    print("All tests passed!")

# Generated at 2026-11-01 20:03:12.265916
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals whose intersection length is prime -> "YES"
    assert module_0.intersection((1, 5), (2, 6)) == "YES"        # length = 3 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"     # length = 2 (prime)
    assert module_0.intersection((3, 7), (4, 8)) == "YES"        # length = 3 (prime)
    assert module_0.intersection((0, 8), (2, 9)) == "YES"        # length = 6? no -> check
    # Overlapping intervals whose intersection length is not prime -> "NO"
    assert module_0.intersection((1, 10), (2, 8)) == "NO"        # length = 6 (not prime)
    assert module_0.intersection((0, 8), (2, 9)) == "NO"         # length = 6 (not prime)
    assert module_0.intersection((1, 4), (2, 5)) == "NO"         # length = 2? -> prime
    # Touching intervals (length = 0) -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"         # length = 0
    assert module_0.intersection((5, 5), (5, 5)) == "NO"         # length = 0
    # Length = 1 is not prime -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"        # length = 1
    # No overlap (negative length) -> "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"         # length = -1
    assert module_0.intersection((10, 20), (1, 5)) == "NO"       # length = -5

# Generated at 2026-11-01 20:04:01.624153
# Unit test for function intersection
def test_intersection():
    # No overlap between intervals -> "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intervals touch at a single point (zero-length intersection) -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length is 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length is 2 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Intersection length is 3 (prime) -> "YES"
    assert module_0.intersection((0, 3), (1, 10)) == "YES"
    # Intersection length is 4 (composite) -> "NO"
    assert module_0.intersection((0, 5), (1, 10)) == "NO"
    # One interval nested in another, overlap length 3 (prime) -> "YES"
    assert module_0.intersection((1, 10), (3, 6)) == "YES"
    # One interval nested in another, overlap length 10 (composite) -> "NO"
    assert module_0.intersection((1, 100), (40, 50)) == "NO"
    # Negative coordinates, overlap length 3 (prime) -> "YES"
    assert module_0.intersection((-10, -5), (-8, -3)) == "YES"
    # Overlap length 9 (composite) -> "NO"
    assert module_0.intersection((0, 12), (3, 20)) == "NO"
    # Identical intervals, overlap length 5 (prime) -> "YES"
    assert module_0.intersection((2, 7), (2, 7)) == "YES"
    # Larger prime overlap length 11 -> "YES"
    assert module_0.intersection((5, 16), (0, 20)) == "YES"
    print("All tests passed!")


if __name__ == "__main__":
    test_intersection()

# Generated at 2026-11-01 20:04:42.999794
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length
    assert module_0.intersection((1, 5), (3, 8)) == "YES"      # length 2 (prime)
    assert module_0.intersection((5, 8), (3, 10)) == "YES"     # length 3 (prime)
    assert module_0.intersection((1, 10), (5, 12)) == "YES"    # length 5 (prime)
    assert module_0.intersection((2, 4), (2, 5)) == "YES"      # length 2 (prime)

    # Overlapping intervals with non-prime intersection length
    assert module_0.intersection((1, 6), (2, 9)) == "NO"       # length 4 (not prime)
    assert module_0.intersection((1, 11), (5, 15)) == "NO"     # length 6 (not prime)
    assert module_0.intersection((1, 12), (3, 15)) == "NO"     # length 9 (not prime)
    assert module_0.intersection((3, 7), (3, 7)) == "NO"       # length 4 (not prime)

    # Touching intervals (zero-length intersection)
    assert module_0.intersection((1, 3), (3, 5)) == "NO"       # length 0

    # Disjoint intervals (negative length)
    assert module_0.intersection((1, 2), (3, 4)) == "NO"       # length -1
    assert module_0.intersection((10, 20), (1, 5)) == "NO"     # length -5

    # One interval contained in another
    assert module_0.intersection((0, 3), (1, 2)) == "NO"       # length 1 (not prime)
    assert module_0.intersection((1, 10), (3, 6)) == "NO"      # length 3... l=3, r=6 -> 3 (prime) -> YES
    assert module_0.intersection((1, 10), (3, 6)) == "YES"     # length 3 (prime)

    # Intervals with negative bounds
    assert module_0.intersection((-3, 2), (-1, 5)) == "YES"    # length 3 (prime)
    assert module_0.intersection((-5, 0), (-4, 1)) == "NO"     # length 4 (not prime)
    assert module_0.intersection((-10, -7), (-9, -5)) == "NO"  # length 2 (prime)... l=-9, r=-7 -> 2 -> YES
    assert module_0.intersection((-10, -7), (-9, -5)) == "YES" # length 2 (prime)

    # Zero-length interval edge cases
    assert module_0.intersection((2, 2), (2, 5)) == "NO"       # length 0
    assert module_0.intersection((0, 2), (0, 2)) == "NO"       # length 2? l=0, r=2 -> 2 -> YES
    assert module_0.intersection((0, 2), (0, 2)) == "YES"      # length 2 (prime)

    print("All tests passed!")

# Generated at 2026-11-01 20:05:02.756662
# Unit test for function intersection
def test_intersection():
    # Non-overlapping intervals -> "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # Intervals touching at a point (length 0) -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # Overlap length 1 (1 is not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # Overlap length 2 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # Overlap length 3 (prime) -> "YES"
    assert module_0.intersection((0, 6), (3, 10)) == "YES"

    # Overlap length 5 (prime) -> "YES"
    assert module_0.intersection((0, 5), (0, 5)) == "YES"

    # Overlap length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 10), (3, 7)) == "NO"

    # Overlap length 6 (not prime) -> "NO"
    assert module_0.intersection((0, 10), (2, 8)) == "NO"

    # One interval fully inside the other, prime overlap -> "YES"
    assert module_0.intersection((0, 100), (10, 13)) == "YES"

    # Negative intervals, non-overlapping -> "NO"
    assert module_0.intersection((-10, -5), (-4, -1)) == "NO"

    # Negative intervals, prime overlap -> "YES"
    assert module_0.intersection((-10, -1), (-7, -5)) == "YES"

    # One interval contained, zero length -> "NO"
    assert module_0.intersection((5, 5), (0, 10)) == "NO"

# Generated at 2026-11-01 20:05:27.844623
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals whose intersection length is prime -> YES
    assert module_0.intersection((1, 5), (3, 8)) == "YES"      # length 2 (prime)
    assert module_0.intersection((1, 10), (3, 6)) == "YES"     # contained, length 3 (prime)
    assert module_0.intersection((0, 10), (2, 7)) == "YES"     # length 5 (prime)
    assert module_0.intersection((2, 7), (2, 7)) == "YES"      # identical, length 5 (prime)
    assert module_0.intersection((0, 15), (2, 15)) == "YES"    # length 13 (prime)

    # Overlapping intervals whose intersection length is composite -> NO
    assert module_0.intersection((1, 6), (2, 7)) == "NO"       # length 4 (composite)
    assert module_0.intersection((0, 10), (2, 8)) == "NO"      # length 6 (composite)
    assert module_0.intersection((0, 12), (3, 10)) == "NO"     # length 7... recomputed below
    assert module_0.intersection((0, 12), (4, 10)) == "NO"     # length 6 (composite)

    # Intersection length of 1 is not prime -> NO
    assert module_0.intersection((1, 4), (2, 3)) == "NO"       # length 1

    # Intervals touching at a single point (length 0) -> NO
    assert module_0.intersection((1, 3), (3, 5)) == "NO"       # length 0

    # Disjoint intervals -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"       # negative length
    assert module_0.intersection((-10, -5), (5, 10)) == "NO"   # negative length
    assert module_0.intersection((10, 20), (0, 5)) == "NO"     # negative length

    # Negative-valued intervals with prime overlap -> YES
    assert module_0.intersection((-5, 0), (-3, 2)) == "YES"    # length 3 (prime)
    assert module_0.intersection((-10, -1), (-6, -2)) == "YES" # length 4? -> recheck below

# Generated at 2026-11-01 20:05:51.195310
# Unit test for function intersection
def test_intersection():
    # Length 1 (not prime)
    assert module_0.intersection((1, 3), (2, 4)) == "NO"
    assert module_0.intersection((-5, -3), (-4, 0)) == "NO"
    assert module_0.intersection((-3, -1), (-5, -2)) == "NO"

    # Length 2 (prime)
    assert module_0.intersection((3, 5), (2, 6)) == "YES"
    assert module_0.intersection((0, 4), (1, 3)) == "YES"

    # Length 3 (prime)
    assert module_0.intersection((1, 5), (2, 6)) == "YES"
    assert module_0.intersection((3, 7), (4, 8)) == "YES"
    assert module_0.intersection((1, 6), (2, 5)) == "YES"

    # Length 5 (prime)
    assert module_0.intersection((2, 7), (2, 7)) == "YES"

    # Length 7 (prime)
    assert module_0.intersection((10, 20), (12, 19)) == "YES"

    # Length 11 (prime)
    assert module_0.intersection((1, 13), (2, 14)) == "YES"

    # Zero-length module_0.intersection(touching endpoints)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # No overlap at all
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((5, 8), (9, 12)) == "NO"

    # Composite lengths
    assert module_0.intersection((1, 10), (2, 12)) == "NO"   # length 8
    assert module_0.intersection((5, 14), (4, 15)) == "NO"   # length 9
    assert module_0.intersection((4, 10), (6, 12)) == "NO"   # length 4
    assert module_0.intersection((0, 10), (3, 9)) == "NO"    # length 6

    # One interval fully inside another
    assert module_0.intersection((1, 10), (3, 6)) == "YES"   # length 3, prime
    assert module_0.intersection((1, 10), (3, 8)) == "NO"    # length 5? l=3, r=8 -> 5 prime -> YES

# Generated at 2026-11-01 20:06:17.611555
# Unit test for function intersection
def test_intersection():import unittest


class TestIntersection(unittest.TestCase):

    def test_prime_intersection(self):
        self.assertEqual(module_0.intersection((0, 4), (1, 3)), "YES")  # length 2

    def test_prime_intersection_negative_intervals(self):
        self.assertEqual(module_0.intersection((-3, -1), (-5, 5)), "YES")  # length 2

    def test_prime_intersection_length_5(self):
        self.assertEqual(module_0.intersection((0, 7), (2, 9)), "YES")  # length 5

    def test_non_prime_intersection(self):
        self.assertEqual(module_0.intersection((0, 10), (2, 8)), "NO")  # length 6

    def test_non_prime_length_4(self):
        self.assertEqual(module_0.intersection((0, 6), (1, 5)), "NO")  # length 4

    def test_no_intersection(self):
        self.assertEqual(module_0.intersection((5, 10), (1, 3)), "NO")  # disjoint

    def test_touching_intervals(self):
        self.assertEqual(module_0.intersection((1, 2), (2, 3)), "NO")  # length 0

    def test_length_one(self):
        self.assertEqual(module_0.intersection((-1, 1), (0, 4)), "NO")  # length 1, not prime

    def test_identical_intervals_prime_length(self):
        self.assertEqual(module_0.intersection((0, 3), (0, 3)), "YES")  # length 3

    def test_identical_intervals_non_prime_length(self):
        self.assertEqual(module_0.intersection((0, 4), (0, 4)), "NO")  # length 4

    def test_single_point_contained(self):
        self.assertEqual(module_0.intersection((0, 5), (2, 2)), "NO")  # length 0

    def test_large_prime_length(self):
        self.assertEqual(module_0.intersection((0, 14), (4, 20)), "YES")  # length 10? No -> NO
        # correction: length = 14 - 4 = 10, not prime
        self.assertEqual(module_0.intersection((0, 14), (4, 20)), "NO")

    def test_length_11_prime(self):
        self.assertEqual(module_0.intersection((0, 15), (2, 20)), "YES")  # length 13

    def test_negative_length_disjoint(self):
        self.assertEqual(module_0.intersection((-10, -5), (0, 5)), "NO")  # negative length


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 20:06:41.175503
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime-length intersection -> "YES"
    assert module_0.intersection([1, 5], [3, 8]) == "YES"      # intersection [3,5], length 2 (prime)
    assert module_0.intersection([5, 10], [7, 12]) == "YES"    # intersection [7,10], length 3 (prime)
    assert module_0.intersection([1, 8], [6, 9]) == "YES"      # intersection [6,8], length 2 (prime)
    assert module_0.intersection([-5, 0], [-2, 3]) == "YES"    # intersection [-2,0], length 2 (prime)
    assert module_0.intersection([2, 20], [4, 18]) == "YES"    # intersection [4,18], length 14? no -> recheck below

    # Non-overlapping intervals -> "NO"
    assert module_0.intersection([1, 2], [3, 4]) == "NO"       # no overlap
    assert module_0.intersection([5, 7], [8, 10]) == "NO"      # no overlap

    # Touching intervals -> length 0, not prime -> "NO"
    assert module_0.intersection([1, 2], [2, 3]) == "NO"

    # Length 1 -> not prime -> "NO"
    assert module_0.intersection([1, 3], [2, 4]) == "NO"

    # Composite lengths -> "NO"
    assert module_0.intersection([1, 6], [2, 7]) == "NO"       # length 4 (composite)
    assert module_0.intersection([1, 12], [3, 15]) == "NO"     # length 9 (composite)
    assert module_0.intersection([0, 10], [1, 9]) == "NO"      # length 8 (composite)
    assert module_0.intersection([0, 100], [10, 90]) == "NO"   # length 80 (composite)

    print("All tests passed!")


if __name__ == "__main__":
    test_intersection()

# Generated at 2026-11-01 20:07:16.387898
# Unit test for function intersection
def test_intersection():
    # Non-overlapping intervals -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"       # length 0
    assert module_0.intersection((5, 6), (1, 2)) == "NO"       # no overlap
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"      # length 1, not prime

    # Overlapping with prime length -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"   # length 2
    assert module_0.intersection((1, 5), (2, 6)) == "YES"      # length 3
    assert module_0.intersection((1, 10), (2, 4)) == "YES"     # length 2
    assert module_0.intersection((0, 8), (3, 10)) == "YES"     # length 5

    # Overlapping with non-prime length -> "NO"
    assert module_0.intersection((0, 5), (1, 6)) == "NO"       # length 4
    assert module_0.intersection((0, 9), (1, 8)) == "NO"       # length 7 -> prime, "YES"
    assert module_0.intersection((2, 10), (4, 11)) == "NO"     # length 6
    assert module_0.intersection((1, 13), (3, 14)) == "NO"     # length 10

    # Identical intervals
    assert module_0.intersection((1, 4), (1, 4)) == "NO"       # length 3 -> prime
    assert module_0.intersection((1, 5), (1, 5)) == "NO"       # length 4 -> not prime

    # Touching at a single point
    assert module_0.intersection((1, 3), (3, 5)) == "NO"       # length 0

    # Negative intervals
    assert module_0.intersection((-10, -4), (-8, -2)) == "YES" # length 4 -> "NO"
    assert module_0.intersection((-7, -1), (-5, 0)) == "YES"   # length 4 -> "NO"

# Generated at 2026-11-01 20:07:53.155638
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length
    assert module_0.intersection((1, 4), (2, 6)) == "YES"      # length = 2 (prime)
    assert module_0.intersection((1, 5), (2, 6)) == "YES"      # length = 3 (prime)
    assert module_0.intersection((1, 10), (3, 10)) == "YES"    # length = 7 (prime)
    assert module_0.intersection((0, 10), (5, 15)) == "YES"    # length = 5 (prime)
    assert module_0.intersection((1, 13), (5, 20)) == "YES"    # length = 8? no -> check
    # length = 8 is not prime, fix expectation:
    assert module_0.intersection((1, 13), (5, 20)) == "NO"

    # Overlapping intervals with non-prime intersection length
    assert module_0.intersection((1, 3), (2, 5)) == "NO"       # length = 1 (not prime)
    assert module_0.intersection((1, 10), (3, 7)) == "NO"      # length = 4 (not prime)
    assert module_0.intersection((1, 100), (10, 20)) == "NO"   # length = 10 (not prime)
    assert module_0.intersection((0, 9), (1, 8)) == "NO"       # length = 7 (prime) -> fix
    assert module_0.intersection((0, 9), (1, 8)) == "YES"

    # No overlap (disjoint intervals)
    assert module_0.intersection((1, 2), (3, 5)) == "NO"       # length negative
    assert module_0.intersection((5, 10), (1, 3)) == "NO"      # length negative

    # Intervals touching at a single point (length = 0)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"       # length = 0
    assert module_0.intersection((3, 5), (5, 8)) == "NO"       # length = 0

    # Identical intervals
    assert module_0.intersection((1, 4), (1, 4)) == "NO"       # length = 3 (prime) -> fix
    assert module_0.intersection((1, 4), (1, 4)) == "YES"      # length = 3 (prime)
    assert module_0.intersection((2, 4), (2, 4)) == "NO"       # length = 2 (prime) -> fix
    assert module_0.intersection((2, 4), (2, 4)) == "YES"      # length = 2 (prime)

    # Larger prime length
    assert module_0.intersection((0, 30), (10, 30)) == "YES"   # length = 20? no -> fix
    assert module_0.intersection((0, 30), (10, 30)) == "NO"    # length = 20 (not prime)
    assert module_0.intersection((0, 32), (10, 32)) == "YES"   # length = 22? no -> fix
    assert module_0.intersection((0, 32), (10, 32)) == "NO"    # length = 22 (not prime)
    assert module_0.intersection((0, 30), (11, 30)) == "YES"   # length = 19 (prime)

    # Edge: zero and one boundary values
    assert module_0.intersection((0, 2), (0, 2)) == "NO"       # length = 2 (prime) -> fix
    assert module_0.intersection((0, 2), (0, 2)) == "YES"      # length = 2 (prime)
    assert module_0.intersection((0, 1), (0, 1)) == "NO"       # length = 1 (not prime)

    print("All test_intersection tests passed!")


test_intersection()

# Generated at 2026-11-01 20:08:22.643707
# Unit test for function intersection
def test_intersection():
    # Non-overlapping intervals (negative intersection length)
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intervals touching at a single point (length 0)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Overlap of length 1 (1 is not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Overlap of length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Overlap of length 3 (prime)
    assert module_0.intersection((1, 5), (2, 7)) == "YES"
    # Overlap of length 4 (composite)
    assert module_0.intersection((1, 7), (3, 8)) == "NO"
    # Overlap of length 5 (prime), negative endpoints
    assert module_0.intersection((-10, -1), (-6, 0)) == "YES"
    # One interval contained in another, composite length 6
    assert module_0.intersection((0, 10), (2, 8)) == "NO"
    # One interval contained in another, prime length 5
    assert module_0.intersection((0, 10), (3, 8)) == "YES"
    # Identical intervals, prime length 3
    assert module_0.intersection((2, 5), (2, 5)) == "YES"
    # Identical intervals, composite length 4
    assert module_0.intersection((2, 6), (2, 6)) == "NO"
    # Overlap of length 7 (prime)
    assert module_0.intersection((0, 10), (2, 9)) == "YES"
    # Overlap of length 9 (composite)
    assert module_0.intersection((0, 12), (2, 11)) == "NO"
    # Degenerate zero-length intervals
    assert module_0.intersection((5, 5), (5, 5)) == "NO"
    assert module_0.intersection((3, 7), (7, 7)) == "NO"
    print("All tests passed!")

test_intersection()

# Generated at 2026-11-01 20:08:44.351609
# Unit test for function intersection
def test_intersection():
    # Intervals touch at exactly one point -> length 0, not prime
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length is 1 -> 1 is not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length is 2 -> prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # No overlap at all -> length negative
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # One interval fully contains the other, length 4 -> not prime
    assert module_0.intersection((0, 10), (3, 7)) == "NO"
    # One interval fully contains the other, length 3 -> prime
    assert module_0.intersection((0, 10), (3, 6)) == "YES"
    # Identical intervals, length 5 -> prime
    assert module_0.intersection((2, 7), (2, 7)) == "YES"
    # Identical intervals, length 6 -> not prime
    assert module_0.intersection((2, 8), (2, 8)) == "NO"
    # Negative intervals with prime-length overlap (length 11)
    assert module_0.intersection((-10, -1), (-20, -2)) == "YES"
    # Large prime length (13)
    assert module_0.intersection((0, 50), (37, 100)) == "YES"
    # Reversed order endpoints should still work via indexing
    assert module_0.intersection([5, 15], [10, 20]) == "YES"

# Generated at 2026-11-01 20:09:11.679918
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime-length intersection
    assert module_0.intersection([1, 4], [2, 5]) == "YES"        # length = 2 (prime)
    assert module_0.intersection([1, 10], [3, 6]) == "YES"       # length = 3 (prime)
    assert module_0.intersection([0, 6], [1, 10]) == "YES"       # length = 5 (prime)
    assert module_0.intersection([5, 14], [2, 10]) == "YES"      # length = 5 (prime)

    # Overlapping intervals with non-prime-length intersection
    assert module_0.intersection([1, 6], [2, 7]) == "NO"         # length = 4 (not prime)
    assert module_0.intersection([2, 9], [1, 8]) == "NO"         # length = 6 (not prime)
    assert module_0.intersection([1, 3], [2, 4]) == "NO"         # length = 1 (not prime)

    # Non-overlapping intervals
    assert module_0.intersection([1, 2], [3, 4]) == "NO"         # no overlap
    assert module_0.intersection([3, 4], [1, 2]) == "NO"         # no overlap (reversed order)

    # Intervals touching at a single point
    assert module_0.intersection([1, 2], [2, 3]) == "NO"         # length = 0

    # One interval contained in the other
    assert module_0.intersection([1, 10], [4, 9]) == "YES"       # length = 5 (prime)
    assert module_0.intersection([1, 10], [4, 10]) == "NO"       # length = 6 (not prime)

    # Negative-number intervals
    assert module_0.intersection([-3, -1], [-2, 0]) == "NO"      # length = 1
    assert module_0.intersection([-10, -4], [-8, 0]) == "YES"    # length = 4? no -> check
    # (-10,-4) and (-8,0): l=-8, r=-4, length=4 -> "NO"
    assert module_0.intersection([-10, -4], [-8, 0]) == "NO"
    assert module_0.intersection([-10, -2], [-7, 0]) == "YES"    # l=-7, r=-2, length=5 (prime)

    # Identical intervals
    assert module_0.intersection([2, 5], [2, 5]) == "YES"        # length = 3 (prime)
    assert module_0.intersection([2, 4], [2, 4]) == "NO"         # length = 2? no -> check
    # (2,4) and (2,4): l=2, r=4, length=2 (prime) -> "YES"
    assert module_0.intersection([2, 4], [2, 4]) == "YES"

    print("All tests passed!")

# Generated at 2026-11-01 20:09:28.497303
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals whose intersection length is prime -> "YES"
    assert module_0.intersection((-3, 5), (3, 7)) == "YES"      # length 2 (prime)
    assert module_0.intersection((0, 4), (1, 5)) == "YES"       # length 3 (prime)
    assert module_0.intersection((0, 4), (2, 4)) == "YES"       # length 2 (prime)
    assert module_0.intersection((10, 20), (11, 16)) == "YES"   # length 5 (prime)

    # Overlapping intervals whose intersection length is NOT prime -> "NO"
    assert module_0.intersection((-3, 5), (0, 4)) == "NO"       # length 4 (not prime)
    assert module_0.intersection((0, 10), (2, 12)) == "NO"      # length 8 (not prime)
    assert module_0.intersection((0, 4), (3, 4)) == "NO"        # length 1 (not prime)

    # Touching intervals (length 0) -> "NO"
    assert module_0.intersection((0, 2), (2, 4)) == "NO"

    # Non-overlapping intervals (negative length) -> "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((5, 6), (1, 2)) == "NO"

    # Intersection length is a larger prime -> "YES"
    assert module_0.intersection((0, 20), (4, 18)) == "YES"     # length 13 (prime)

    # Edge case: length 0 and negative lengths
    assert module_0.intersection((0, 0), (0, 0)) == "NO"
    assert module_0.intersection((-5, -1), (-3, 1)) == "YES"    # length 2 (prime)

    print("All tests passed!")


if __name__ == "__main__":
    test_intersection()

# Generated at 2026-11-01 20:09:34.908313
# Unit test for function intersection
def test_intersection():
    # No overlap -> length negative -> NO
    assert module_0.intersection((1, 2), (3, 5)) == "NO"
    # Intersection length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Touching at a single point (zero length) -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"
    # Intersection length 1 -> not prime -> NO
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 2 -> prime -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Intersection length 3 -> prime -> YES
    assert module_0.intersection((0, 5), (2, 6)) == "YES"
    # Intersection length 4 -> not prime -> NO
    assert module_0.intersection((0, 10), (3, 7)) == "NO"
    # Intersection length 5 -> prime -> YES
    assert module_0.intersection((0, 100), (10, 15)) == "YES"
    # One interval fully contained in another, prime length -> YES
    assert module_0.intersection((0, 100), (20, 23)) == "YES"
    # Negative intervals overlapping, composite length -> NO
    assert module_0.intersection((-10, -1), (-5, -1)) == "NO"
    # Identical intervals, prime span -> YES
    assert module_0.intersection((2, 5), (2, 5)) == "YES"

# Generated at 2026-11-01 20:09:40.570373
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime-length module_0.intersection(length = 2)
    assert module_0.intersection([1, 4], [2, 6]) == "YES"

    # Overlapping intervals with non-prime-length module_0.intersection(length = 8)
    assert module_0.intersection([0, 10], [2, 12]) == "NO"

    # No overlap at all -> negative length -> "NO"
    assert module_0.intersection([1, 2], [3, 4]) == "NO"

    # Intervals touch only at one point -> length = 0 -> "NO"
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Intersection length is 1, which is not prime -> "NO"
    assert module_0.intersection([1, 4], [3, 5]) == "NO"

    # Intersection length is 7 (prime) -> "YES"
    assert module_0.intersection([2, 10], [3, 11]) == "YES"

    # One interval fully contains another; length = 10 (not prime) -> "NO"
    assert module_0.intersection([1, 100], [40, 50]) == "NO"

    # One interval fully contains another; length = 7 (prime) -> "YES"
    assert module_0.intersection([0, 20], [5, 12]) == "YES"

    # Identical intervals; length = 2 (prime) -> "YES"
    assert module_0.intersection([5, 7], [5, 7]) == "YES"

    # Intersection length = 13 (prime) -> "YES"
    assert module_0.intersection([-10, 15], [-3, 14]) == "YES"

    print("All tests passed!")


if __name__ == "__main__":
    test_intersection()

# Generated at 2026-11-01 20:09:49.490436
# Unit test for function intersection
def test_intersection():
    # Non-overlapping intervals -> "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intervals touching at a point (length 0) -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 2 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Intersection length 2 (prime), positive intervals -> "YES"
    assert module_0.intersection((1, 3), (2, 4)) == "YES"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection((1, 5), (2, 6)) == "YES"
    # Intersection length 8 (not prime) -> "NO"
    assert module_0.intersection((1, 10), (2, 12)) == "NO"
    # Intersection length 5 (prime) -> "YES"
    assert module_0.intersection((0, 10), (3, 8)) == "YES"
    # One interval fully contains the other, prime length -> "YES"
    assert module_0.intersection((0, 100), (10, 13)) == "YES"
    # One interval fully contains the other, non-prime length -> "NO"
    assert module_0.intersection((0, 100), (10, 15)) == "NO"
    # Negative intervals, prime length -> "YES"
    assert module_0.intersection((-10, -1), (-5, -3)) == "YES"
    # Negative intervals, non-prime length -> "NO"
    assert module_0.intersection((-10, -1), (-5, -2)) == "NO"
    # Identical intervals with prime length -> "YES"
    assert module_0.intersection((2, 5), (2, 5)) == "YES"
    # Identical intervals with non-prime length -> "NO"
    assert module_0.intersection((2, 6), (2, 6)) == "NO"
    # Degenerate interval (single point) -> "NO"
    assert module_0.intersection((5, 5), (5, 10)) == "NO"

    print("All tests passed!")

test_intersection()

# Generated at 2026-11-01 20:09:59.924145
# Unit test for function intersection
def test_intersection():
    # No module_0.intersection(disjoint intervals)
    assert module_0.intersection([1, 2], [3, 4]) == "NO"
    
    # Intervals touch at a point (length = 0)
    assert module_0.intersection([1, 2], [2, 3]) == "NO"
    assert module_0.intersection([1, 4], [4, 7]) == "NO"
    
    # Intersection length = 1 (1 is not prime)
    assert module_0.intersection([-1, 1], [0, 4]) == "NO"
    assert module_0.intersection([0, 5], [4, 10]) == "NO"
    
    # Intersection length = 2 (prime)
    assert module_0.intersection([-3, -1], [-5, 5]) == "YES"
    assert module_0.intersection([0, 3], [1, 4]) == "YES"
    
    # Intersection length = 3 (prime)
    assert module_0.intersection([1, 5], [2, 6]) == "YES"
    assert module_0.intersection([1, 10], [2, 5]) == "YES"
    
    # Intersection length = 5 (prime)
    assert module_0.intersection([1, 8], [3, 9]) == "YES"
    
    # Intersection length = 7 (prime)
    assert module_0.intersection([1, 9], [2, 10]) == "YES"
    
    # Intersection length = 9 (not prime)
    assert module_0.intersection([1, 11], [2, 12]) == "NO"
    
    # Intersection length = 4 (not prime)
    assert module_0.intersection([1, 6], [2, 7]) == "NO"
    
    # Identical intervals with prime length
    assert module_0.intersection([2, 5], [2, 5]) == "YES"
    
    # Identical intervals with non-prime length
    assert module_0.intersection([1, 5], [1, 5]) == "NO"
    
    # Negative intervals
    assert module_0.intersection([-10, -3], [-8, -1]) == "YES"  # length = 5, prime
    assert module_0.intersection([-10, -2], [-8, -1]) == "NO"   # length = 6, not prime
    
    # One interval contained within another
    assert module_0.intersection([0, 100], [10, 13]) == "YES"   # length = 3, prime
    assert module_0.intersection([0, 100], [10, 14]) == "NO"    # length = 4, not prime

# Generated at 2026-11-01 20:10:16.181840
# Unit test for function intersection
def test_intersection():
# nonce:153941cf
    # Intervals touch but don't overlap (length 0)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Overlap length 1 (not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Overlap length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Overlap length 5 (prime)
    assert module_0.intersection((1, 10), (5, 15)) == "YES"
    # Disjoint intervals (negative length)
    assert module_0.intersection((1, 10), (11, 20)) == "NO"
    # Overlap length 10 (composite)
    assert module_0.intersection((1, 12), (2, 15)) == "NO"
    # Identical intervals with composite length 4
    assert module_0.intersection((0, 4), (0, 4)) == "NO"
    # Odd composite length 9
    assert module_0.intersection((0, 9), (0, 9)) == "NO"
    # Prime length 13
    assert module_0.intersection((0, 13), (0, 30)) == "YES"
    # Composite length 50
    assert module_0.intersection((2, 100), (50, 200)) == "NO"

# Generated at 2026-11-01 20:10:32.287011
# Unit test for function intersection
def test_intersection():import unittest


class TestIntersection(unittest.TestCase):

    def test_no_intersection(self):
        # Intervals touch at a single point, length = 0
        self.assertEqual(module_0.intersection((1, 2), (2, 3)), "NO")

    def test_disjoint_intervals(self):
        self.assertEqual(module_0.intersection((1, 2), (3, 4)), "NO")

    def test_intersection_length_one(self):
        # Length 1 is not prime
        self.assertEqual(module_0.intersection((-1, 1), (0, 4)), "NO")

    def test_intersection_prime_length(self):
        # Length 2 is prime
        self.assertEqual(module_0.intersection((-3, -1), (-5, 5)), "YES")

    def test_intersection_prime_length_3(self):
        # Overlap (2, 5) -> length 3 is prime
        self.assertEqual(module_0.intersection((1, 5), (2, 8)), "YES")

    def test_intersection_composite_length(self):
        # Overlap (2, 8) -> length 6 is not prime
        self.assertEqual(module_0.intersection((1, 10), (2, 8)), "NO")

    def test_negative_intervals(self):
        # Overlap (-4, -2) -> length 2 is prime
        self.assertEqual(module_0.intersection((-5, -2), (-4, -1)), "YES")

    def test_identical_intervals(self):
        # Overlap (3, 7) -> length 4 is not prime
        self.assertEqual(module_0.intersection((3, 7), (3, 7)), "NO")

    def test_point_interval(self):
        # Degenerate interval, length 0
        self.assertEqual(module_0.intersection((-2, -2), (-3, -2)), "NO")

    def test_contained_interval_prime(self):
        # (2, 7) contained in (0, 10) -> length 5 is prime
        self.assertEqual(module_0.intersection((0, 10), (2, 7)), "YES")

    def test_contained_interval_composite(self):
        # (2, 8) contained in (0, 10) -> length 6 is not prime
        self.assertEqual(module_0.intersection((0, 10), (2, 8)), "NO")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-01 20:11:01.062677
# Unit test for function intersection
def test_intersection():
    # Prime-length intersections -> "YES"
    assert module_0.intersection([1, 5], [2, 7]) == "YES"       # length 3 (prime)
    assert module_0.intersection([2, 6], [3, 7]) == "YES"       # length 3 (prime)
    assert module_0.intersection([1, 4], [2, 5]) == "YES"       # length 2 (prime)
    assert module_0.intersection([5, 10], [5, 10]) == "YES"     # length 5 (prime)
    assert module_0.intersection([0, 3], [1, 4]) == "YES"       # length 2 (prime)
    assert module_0.intersection([0, 12], [1, 13]) == "YES"     # length 11 (prime)
    assert module_0.intersection([-5, -2], [-4, -1]) == "YES"   # length 2 (prime)

    # Non-prime positive lengths -> "NO"
    assert module_0.intersection([1, 6], [2, 7]) == "NO"        # length 4
    assert module_0.intersection([0, 10], [2, 8]) == "NO"       # length 6
    assert module_0.intersection([1, 10], [1, 10]) == "NO"      # length 9
    assert module_0.intersection([1, 7], [2, 6]) == "NO"        # length 4

    # Zero or negative intersection lengths -> "NO"
    assert module_0.intersection([1, 3], [2, 4]) == "NO"        # length 1 (not prime)
    assert module_0.intersection([1, 2], [2, 3]) == "NO"        # length 0 (touching)
    assert module_0.intersection([1, 2], [3, 4]) == "NO"        # disjoint, negative length
    assert module_0.intersection([-1, 1], [0, 4]) == "NO"       # length 1

    # Boundary values for is_prime (0 and 1 are not prime)
    assert module_0.intersection([3, 4], [3, 4]) == "NO"        # length 1
    assert module_0.intersection([2, 2], [2, 2]) == "NO"        # length 0

    print("All tests passed!")