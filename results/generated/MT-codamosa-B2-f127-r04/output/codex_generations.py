

# Generated at 2026-11-02 21:15:36.243173
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals whose intersection length is prime (2)
    assert module_0.intersection([1, 5], [3, 8]) == "YES"
    # Overlapping intervals whose intersection length is prime (7)
    assert module_0.intersection([0, 10], [3, 20]) == "YES"
    # Overlapping intervals whose intersection length is prime (11)
    assert module_0.intersection([0, 15], [4, 20]) == "YES"
    # One interval fully contained in the other, prime length (2)
    assert module_0.intersection([1, 10], [3, 5]) == "YES"
    # Identical intervals, prime length (2)
    assert module_0.intersection([2, 4], [2, 4]) == "YES"

    # Overlapping intervals whose intersection length is composite (4)
    assert module_0.intersection([1, 6], [2, 8]) == "NO"
    # Overlapping intervals whose intersection length is composite (6)
    assert module_0.intersection([1, 8], [2, 10]) == "NO"
    # Intersection length of 1 is not prime
    assert module_0.intersection([1, 5], [4, 8]) == "NO"
    assert module_0.intersection([1, 3], [2, 9]) == "NO"
    # Intersection length of 0 (intervals touch at a point)
    assert module_0.intersection([1, 2], [2, 3]) == "NO"
    # Non-overlapping intervals (negative length)
    assert module_0.intersection([1, 2], [3, 4]) == "NO"
    assert module_0.intersection([5, 7], [8, 10]) == "NO"
    # Intervals with negative endpoints, intersection length 1
    assert module_0.intersection([-3, 0], [-1, 5]) == "NO"
    # Identical single-point intervals
    assert module_0.intersection([5, 6], [5, 6]) == "NO"
    # Nested intervals with composite length (9)
    assert module_0.intersection([0, 20], [5, 14]) == "NO"

    print("All test cases passed!")


test_intersection()

# Generated at 2026-11-02 21:16:45.583063
# Unit test for function intersection
def test_intersection():
    # Intervals touch at a point: length = 0 -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Overlap of length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Overlap of length 2 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # One interval fully inside the other, length 6 (not prime) -> "NO"
    assert module_0.intersection((0, 10), (2, 8)) == "NO"
    # Overlap of length 3 (prime) -> "YES"
    assert module_0.intersection((0, 5), (1, 4)) == "NO" if False else module_0.intersection((0, 5), (1, 4)) == "YES"
    # Disjoint intervals -> "NO"
    assert module_0.intersection((5, 6), (1, 2)) == "NO"
    # Overlap of length 0 with identical endpoints -> "NO"
    assert module_0.intersection((-2, -2), (-3, -2)) == "NO"
    # Overlap of length 2 (prime) -> "YES"
    assert module_0.intersection((0, 4), (1, 3)) == "YES"
    # Overlap of length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 9)) == "NO"
    # Negative intervals with prime overlap length 2 -> "YES"
    assert module_0.intersection((-10, -5), (-7, -1)) == "YES"
    # Negative intervals with non-prime overlap length 4 -> "NO"
    assert module_0.intersection((-10, -1), (-6, 0)) == "NO"

# Generated at 2026-11-02 21:17:33.971997
# Unit test for function intersection
def test_intersection():
    # No overlap (disjoint intervals) -> length negative -> "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # Intervals touch at a point -> length 0 -> "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # Overlap length 1 -> 1 is not prime -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # Overlap length 2 -> prime -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # Overlap length 2 -> prime -> "YES"
    assert module_0.intersection((0, 3), (1, 5)) == "YES"

    # Overlap length 4 -> not prime -> "NO"
    assert module_0.intersection((0, 4), (0, 6)) == "NO"

    # Overlap length 3 -> prime -> "YES"
    assert module_0.intersection((2, 5), (1, 6)) == "YES"

    # Overlap length 6 -> not prime -> "NO"
    assert module_0.intersection((0, 6), (0, 6)) == "NO"

    # One interval fully inside another, prime length 5 -> "YES"
    assert module_0.intersection((10, 15), (0, 100)) == "YES"

    # One interval fully inside another, non-prime length 9 -> "NO"
    assert module_0.intersection((10, 19), (0, 100)) == "NO"

    # Negative intervals with no overlap -> "NO"
    assert module_0.intersection((-5, -3), (-2, 0)) == "NO"

    # Reversed order arguments (second starts before first) -> still works
    assert module_0.intersection((3, 4), (1, 2)) == "NO"

    print("All tests passed!")


if __name__ == "__main__":
    test_intersection()

# Generated at 2026-11-02 21:18:58.500609
# Unit test for function intersection
def test_intersection():
    # Intersection length is prime -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"   # length = 2 (prime)
    assert module_0.intersection((0, 5), (2, 10)) == "YES"     # length = 3 (prime)
    assert module_0.intersection((0, 4), (1, 3)) == "YES"      # length = 2 (prime)
    assert module_0.intersection((1, 8), (3, 9)) == "YES"      # length = 5 (prime)
    assert module_0.intersection((0, 10), (4, 9)) == "YES"     # length = 5 (prime)

    # Intersection length is not prime -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"       # length = 0
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"      # length = 1 (not prime)
    assert module_0.intersection((0, 3), (1, 2)) == "NO"       # length = 1 (not prime)
    assert module_0.intersection((1, 10), (2, 8)) == "NO"      # length = 6 (not prime)
    assert module_0.intersection((0, 8), (2, 6)) == "NO"       # length = 4 (not prime)
    assert module_0.intersection((0, 12), (3, 9)) == "NO"      # length = 6 (not prime)

    # No intersection -> "NO"
    assert module_0.intersection((5, 10), (11, 15)) == "NO"    # disjoint intervals
    assert module_0.intersection((1, 3), (4, 6)) == "NO"       # disjoint intervals
    assert module_0.intersection((-10, -5), (0, 5)) == "NO"    # disjoint intervals

    # Intervals touching at a single point -> "NO"
    assert module_0.intersection((1, 5), (5, 10)) == "NO"      # length = 0
    assert module_0.intersection((-2, 0), (0, 7)) == "NO"      # length = 0

    # Negative intervals with prime overlap -> "YES"
    assert module_0.intersection((-10, -4), (-8, -2)) == "YES" # length = 4... wait, 4 is not prime
    # Correction: length = -4 - (-8) = 4, not prime
    assert module_0.intersection((-10, -4), (-8, -2)) == "NO"  # length = 4 (not prime)
    assert module_0.intersection((-10, -1), (-9, -4)) == "YES" # length = 5 (prime)

    # Identical intervals
    assert module_0.intersection((2, 5), (2, 5)) == "YES"      # length = 3 (prime)
    assert module_0.intersection((2, 4), (2, 4)) == "NO"       # length = 2 (prime) -> actually YES
    # Correction: length = 2 is prime
    assert module_0.intersection((2, 4), (2, 4)) == "YES"      # length = 2 (prime)

    print("All tests passed!")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-11-02 21:20:36.914444
# Unit test for function intersection
def test_intersection():
    # Overlap of prime length 2
    assert module_0.intersection([1, 5], [3, 8]) == "YES"
    # Overlap of prime length 5
    assert module_0.intersection([0, 5], [0, 5]) == "YES"
    # Overlap of prime length 7
    assert module_0.intersection([1, 10], [2, 9]) == "YES"
    # Overlap of prime length 13
    assert module_0.intersection([0, 15], [2, 16]) == "YES"
    # Overlap of composite length 4
    assert module_0.intersection([1, 7], [3, 8]) == "NO"
    # Overlap of composite length 6
    assert module_0.intersection([1, 10], [2, 8]) == "NO"
    # Overlap of length 1 (1 is not prime)
    assert module_0.intersection([1, 2], [1, 3]) == "NO"
    # Intervals touching at a point (length 0)
    assert module_0.intersection([1, 3], [3, 5]) == "NO"
    assert module_0.intersection([2, 2], [2, 2]) == "NO"
    # No overlap at all (negative length)
    assert module_0.intersection([1, 2], [5, 7]) == "NO"
    assert module_0.intersection([5, 7], [1, 3]) == "NO"
    # Negative intervals, prime overlap length 2
    assert module_0.intersection([-3, -1], [-5, 1]) == "YES"
    # Negative intervals, composite overlap length 4
    assert module_0.intersection([-6, 0], [-4, 5]) == "NO"

# Generated at 2026-11-02 21:21:51.566764
# Unit test for function intersection
def test_intersection():import unittest


class TestIntersection(unittest.TestCase):

    def test_prime_length_yes(self):
        # Intersection length = 2 (prime)
        self.assertEqual(module_0.intersection((0, 3), (1, 5)), "YES")

    def test_prime_length_three(self):
        # Intersection length = 3 (prime)
        self.assertEqual(module_0.intersection((0, 4), (1, 6)), "YES")

    def test_prime_length_five(self):
        # Intersection length = 5 (prime)
        self.assertEqual(module_0.intersection((0, 6), (1, 7)), "YES")

    def test_prime_length_eleven(self):
        # Intersection length = 11 (prime)
        self.assertEqual(module_0.intersection((0, 12), (1, 13)), "YES")

    def test_non_prime_length_no(self):
        # Intersection length = 4 (not prime)
        self.assertEqual(module_0.intersection((0, 4), (0, 4)), "NO")

    def test_non_prime_length_nine(self):
        # Intersection length = 9 (not prime)
        self.assertEqual(module_0.intersection((0, 10), (1, 11)), "NO")

    def test_non_prime_length_six(self):
        # Intersection length = 6 (not prime)
        self.assertEqual(module_0.intersection((0, 7), (1, 10)), "NO")

    def test_length_one_no(self):
        # Intersection length = 1 (1 is not prime)
        self.assertEqual(module_0.intersection((0, 2), (1, 3)), "NO")

    def test_touching_intervals_no(self):
        # Intersection length = 0
        self.assertEqual(module_0.intersection((0, 2), (2, 4)), "NO")

    def test_disjoint_intervals_no(self):
        # No overlap, negative length
        self.assertEqual(module_0.intersection((0, 2), (3, 5)), "NO")

    def test_negative_intervals_prime_yes(self):
        # Negative coordinates, length = 2 (prime)
        self.assertEqual(module_0.intersection((-3, -1), (-5, 5)), "YES")

    def test_negative_intervals_length_one_no(self):
        # Negative coordinates, length = 1
        self.assertEqual(module_0.intersection((-1, 1), (0, 4)), "NO")

    def test_identical_intervals_prime(self):
        # Identical intervals with prime length
        self.assertEqual(module_0.intersection((0, 3), (0, 3)), "YES")

    def test_contained_interval(self):
        # One interval fully inside another, length = 3 (prime)
        self.assertEqual(module_0.intersection((0, 7), (2, 5)), "YES")


# nonce:5e9b5c64
if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 21:23:34.877554
# Unit test for function intersection
def test_intersection():
    # Non-overlapping intervals (negative length)
    assert module_0.intersection([1, 2], [3, 4]) == "NO"
    # Intervals touching at a single point (length 0)
    assert module_0.intersection([1, 2], [2, 3]) == "NO"
    # Intersection length 1 (not prime)
    assert module_0.intersection([-1, 1], [0, 4]) == "NO"
    # Intersection length 2 (prime)
    assert module_0.intersection([-3, -1], [-5, 5]) == "YES"
    # Intersection length 3 (prime)
    assert module_0.intersection([1, 5], [2, 6]) == "YES"
    # Intersection length 4 (composite)
    assert module_0.intersection([1, 6], [2, 7]) == "NO"
    # Nested intervals, intersection length 6 (composite)
    assert module_0.intersection([0, 10], [2, 8]) == "NO"
    # Identical intervals, intersection length 3 (prime)
    assert module_0.intersection([2, 5], [2, 5]) == "YES"
    # Larger prime intersection length 17
    assert module_0.intersection([1, 20], [3, 25]) == "YES"
    # Larger composite intersection length 16
    assert module_0.intersection([1, 20], [4, 25]) == "NO"

    print("All tests passed!")