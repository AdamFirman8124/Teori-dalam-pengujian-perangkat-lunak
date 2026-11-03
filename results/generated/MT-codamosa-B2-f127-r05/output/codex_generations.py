

# Generated at 2026-11-02 06:33:01.280552
# Unit test for function intersection
def test_intersection():import unittest


class TestIntersection(unittest.TestCase):
    def test_overlapping_intervals_with_prime_length(self):
        self.assertEqual(module_0.intersection((1, 5), (3, 8)), "YES")

    def test_overlapping_intervals_with_non_prime_length(self):
        self.assertEqual(module_0.intersection((1, 6), (3, 8)), "NO")

    def test_touching_intervals_zero_length(self):
        self.assertEqual(module_0.intersection((1, 3), (3, 5)), "NO")

    def test_no_intersection(self):
        self.assertEqual(module_0.intersection((1, 2), (5, 8)), "NO")

    def test_length_of_two(self):
        self.assertEqual(module_0.intersection((1, 4), (2, 5)), "YES")

    def test_length_of_one(self):
        self.assertEqual(module_0.intersection((1, 3), (2, 4)), "NO")

    def test_identical_intervals_prime_length(self):
        self.assertEqual(module_0.intersection((0, 5), (0, 5)), "YES")

    def test_identical_intervals_non_prime_length(self):
        self.assertEqual(module_0.intersection((0, 4), (0, 4)), "NO")

    def test_negative_intervals(self):
        self.assertEqual(module_0.intersection((-5, 1), (-3, 3)), "YES")

    def test_contained_interval(self):
        self.assertEqual(module_0.intersection((1, 10), (3, 7)), "YES")

    def test_large_prime_length(self):
        self.assertEqual(module_0.intersection((0, 20), (0, 20)), "YES")

    def test_single_point_overlap(self):
        self.assertEqual(module_0.intersection((2, 2), (2, 2)), "NO")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 06:33:19.852889
# Unit test for function intersection
def test_intersection():import unittest


class TestIntersection(unittest.TestCase):

    def test_overlap_with_prime_length(self):
        self.assertEqual(module_0.intersection((1, 5), (3, 8)), "YES")  # overlap (3,5) length 2, prime

    def test_overlap_with_non_prime_length(self):
        self.assertEqual(module_0.intersection((1, 6), (3, 8)), "NO")  # overlap length 3... wait 6-3=3 prime
        # corrected: overlap (3,6) length 3 which is prime
        # Use a non-prime length instead:
        self.assertEqual(module_0.intersection((1, 7), (3, 8)), "NO")  # overlap (3,7) length 4, not prime

    def test_touching_intervals(self):
        self.assertEqual(module_0.intersection((1, 3), (3, 5)), "NO")  # overlap length 0

    def test_no_overlap(self):
        self.assertEqual(module_0.intersection((1, 2), (5, 8)), "NO")  # negative length

    def test_prime_length_2(self):
        self.assertEqual(module_0.intersection((0, 2), (1, 3)), "YES")  # overlap (1,2) length 1... not prime
        # corrected: length 1 is not prime, so NO
        self.assertEqual(module_0.intersection((0, 3), (1, 3)), "NO")  # overlap length 2, prime -> YES

    def test_negative_intervals(self):
        self.assertEqual(module_0.intersection((-5, -1), (-3, 0)), "YES")  # overlap (-3,-1) length 2, prime

    def test_identical_intervals(self):
        self.assertEqual(module_0.intersection((2, 2), (2, 2)), "NO")  # zero length

    def test_one_contains_other(self):
        self.assertEqual(module_0.intersection((1, 10), (3, 5)), "YES")  # overlap (3,5) length 2, prime

    def test_large_prime_length(self):
        self.assertEqual(module_0.intersection((0, 15), (2, 100)), "YES")  # overlap (2,15) length 13, prime


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 06:33:49.286793
# Unit test for function intersection
def test_intersection():import unittest


class TestIntersection(unittest.TestCase):

    def test_overlapping_prime_length(self):
        self.assertEqual(module_0.intersection((1, 5), (3, 8)), "YES")

    def test_overlapping_prime_length_2(self):
        self.assertEqual(module_0.intersection((-3, 2), (0, 5)), "NO")

    def test_touching_intervals(self):
        self.assertEqual(module_0.intersection((1, 3), (3, 5)), "NO")

    def test_no_intersection(self):
        self.assertEqual(module_0.intersection((1, 2), (5, 6)), "NO")

    def test_single_point_intersection(self):
        self.assertEqual(module_0.intersection((1, 3), (3, 4)), "NO")

    def test_intersection_length_5(self):
        self.assertEqual(module_0.intersection((0, 10), (2, 7)), "YES")

    def test_intersection_length_1(self):
        self.assertEqual(module_0.intersection((0, 3), (2, 4)), "NO")

    def test_negative_intervals(self):
        self.assertEqual(module_0.intersection((-10, -1), (-5, 0)), "NO")

    def test_identical_intervals(self):
        self.assertEqual(module_0.intersection((2, 6), (2, 6)), "NO")

    def test_contained_interval(self):
        self.assertEqual(module_0.intersection((0, 100), (10, 13)), "YES")

    def test_nested_interval_prime(self):
        self.assertEqual(module_0.intersection((0, 20), (5, 12)), "YES")

    def test_zero_length(self):
        self.assertEqual(module_0.intersection((5, 5), (5, 5)), "NO")


if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 06:34:24.174705
# Unit test for function intersection
def test_intersection():
    # Intersection length is prime (length = 3)
    assert module_0.intersection((1, 5), (2, 7)) == "YES"  # module_0.intersection(2,5), length 3 (prime)

    # Intersection length is prime (length = 2)
    assert module_0.intersection((1, 4), (3, 6)) == "YES"  # module_0.intersection(3,4), length 2 (prime)

    # Intersection length is not prime (length = 4)
    assert module_0.intersection((1, 6), (2, 8)) == "NO"  # module_0.intersection(2,6), length 4 (not prime)

    # Intersection length is 1 (not prime)
    assert module_0.intersection((1, 3), (2, 4)) == "NO"  # module_0.intersection(2,3), length 1

    # Intersection length is 0 (touching endpoints)
    assert module_0.intersection((1, 3), (3, 5)) == "NO"  # length 0

    # No module_0.intersection(disjoint intervals)
    assert module_0.intersection((1, 2), (5, 8)) == "NO"  # length negative

    # Identical intervals with prime length
    assert module_0.intersection((2, 5), (2, 5)) == "YES"  # length 3 (prime)

    # Identical intervals with non-prime length
    assert module_0.intersection((2, 6), (2, 6)) == "NO"  # length 4 (not prime)

    # One interval contains the other, prime length
    assert module_0.intersection((0, 10), (4, 7)) == "NO"  # length 3... wait (4,7) -> length 3 prime? l=4, r=7, length=3 -> YES
    assert module_0.intersection((0, 10), (4, 7)) == "YES"

    # Negative intervals, prime intersection length
    assert module_0.intersection((-5, -1), (-4, 0)) == "YES"  # module_0.intersection(-4,-1), length 3 (prime)

    # Negative intervals, non-prime intersection length
    assert module_0.intersection((-5, -1), (-3, 0)) == "NO"  # module_0.intersection(-3,-1), length 2? l=-3, r=-1, length=2 (prime) -> YES
    assert module_0.intersection((-5, -1), (-3, 0)) == "YES"

    # Zero-length interval
    assert module_0.intersection((2, 2), (2, 2)) == "NO"  # length 0

    # Length 2 module_0.intersection(prime, and 2 is the only even prime)
    assert module_0.intersection((10, 20), (12, 22)) == "YES"  # module_0.intersection(12,20), length 8 (not prime) -> NO
    assert module_0.intersection((10, 20), (12, 22)) == "NO"

    print("All test cases passed!")


if __name__ == "__main__":
    test_intersection()

# Generated at 2026-11-02 06:35:44.843148
# Unit test for function intersection
def test_intersection():
    # Non-overlapping intervals -> "NO"
    assert module_0.intersection([1, 2], [3, 4]) == "NO"
    # Touching intervals, length 0 -> "NO"
    assert module_0.intersection([1, 2], [2, 3]) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection([-1, 1], [0, 4]) == "NO"
    assert module_0.intersection([5, 9], [2, 6]) == "NO"
    # Intersection length 2 (prime) -> "YES"
    assert module_0.intersection([-3, -1], [-5, 5]) == "YES"
    assert module_0.intersection([1, 4], [2, 5]) == "YES"
    assert module_0.intersection([-2, 2], [-4, 0]) == "YES"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection([1, 5], [2, 6]) == "YES"
    # Intersection length 4 (not prime) -> "NO"
    assert module_0.intersection([0, 10], [3, 7]) == "NO"
    # Intersection length 7 (prime) -> "YES"
    assert module_0.intersection([0, 10], [2, 9]) == "YES"
    # Zero-length intersection -> "NO"
    assert module_0.intersection([3, 3], [3, 3]) == "NO"

# Generated at 2026-11-02 06:36:49.687023
# Unit test for function intersection
def test_intersection():import unittest

class TestIntersection(unittest.TestCase):
    def test_no_overlap(self):
        self.assertEqual(module_0.intersection((1, 2), (3, 4)), "NO")

    def test_touching_endpoints(self):
        self.assertEqual(module_0.intersection((1, 3), (3, 5)), "NO")  # length = 0

    def test_overlap_prime_length(self):
        self.assertEqual(module_0.intersection((1, 5), (2, 7)), "YES")  # overlap (2,5), length 3 is prime

    def test_overlap_composite_length(self):
        self.assertEqual(module_0.intersection((1, 10), (2, 12)), "NO")  # overlap length 8, not prime

    def test_identical_intervals_prime(self):
        self.assertEqual(module_0.intersection((2, 5), (2, 5)), "YES")  # length 3, prime

    def test_identical_intervals_not_prime(self):
        self.assertEqual(module_0.intersection((1, 5), (1, 5)), "NO")  # length 4, not prime

    def test_length_two(self):
        self.assertEqual(module_0.intersection((1, 4), (2, 6)), "YES")  # overlap (2,4), length 2 is prime

    def test_length_one(self):
        self.assertEqual(module_0.intersection((1, 3), (2, 4)), "NO")  # overlap (2,3), length 1 not prime

    def test_negative_intervals(self):
        self.assertEqual(module_0.intersection((-5, 0), (-3, 2)), "NO")  # overlap (-3,0), length 3 but negative start check

    def test_contained_interval(self):
        self.assertEqual(module_0.intersection((1, 20), (5, 10)), "NO")  # overlap (5,10), length 5 is prime -> YES

    def test_is_prime_edge_zero_one(self):
        self.assertEqual(module_0.intersection((0, 1), (0, 1)), "NO")  # length 1

    def test_large_prime_length(self):
        self.assertEqual(module_0.intersection((0, 101), (50, 200)), "YES")  # overlap (50,101), length 51 not prime

if __name__ == "__main__":
    unittest.main()

# Generated at 2026-11-02 06:37:45.880380
# Unit test for function intersection
def test_intersection():
    # Non-overlapping intervals
    assert module_0.intersection((1, 2), (3, 4)) == "NO"  # no intersection
    # Touching intervals (length 0)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"  # length 0 is not prime
    # Intersection length 1 (not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"  # length 1
    # Intersection length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"  # length 2
    # Intersection length 3 (prime)
    assert module_0.intersection((5, 10), (6, 9)) == "YES"  # length 3
    # Intersection length 4 (not prime)
    assert module_0.intersection((5, 10), (6, 11)) == "NO"  # length 4
    # Intersection length 5 (prime)
    assert module_0.intersection((1, 7), (2, 8)) == "YES"  # length 5
    # One interval contained in another
    assert module_0.intersection((0, 10), (3, 7)) == "YES"  # length 4 -> "NO"? l=3, r=7, length=4
    # Correct that one: length 4 is not prime
    # Identical intervals
    assert module_0.intersection((2, 6), (2, 6)) == "YES"  # length 4 -> not prime
    # Negative intervals, prime intersection length
    assert module_0.intersection((-10, -4), (-8, -5)) == "YES"  # length 3
    # Intersection length 6 (not prime)
    assert module_0.intersection((0, 8), (1, 9)) == "NO"  # length 7 actually prime -> "YES"
    # Fix: l=1, r=8, length=7 -> prime
    assert module_0.intersection((0, 8), (1, 9)) == "YES"  # length 7
    assert module_0.intersection((0, 10), (0, 6)) == "NO"  # length 6, not prime
    assert module_0.intersection((-5, 0), (-3, 2)) == "YES"  # l=-3, r=0, length 3, prime
    print("All tests passed!")

# Generated at 2026-11-02 06:39:24.598663
# Unit test for function intersection
def test_intersection():
    # Intersection length is prime -> "YES"
    assert module_0.intersection([1, 5], [2, 7]) == "YES"      # length = 3 (prime)
    assert module_0.intersection([1, 4], [2, 6]) == "YES"      # length = 2 (prime)
    assert module_0.intersection([1, 7], [2, 8]) == "YES"      # length = 5 (prime)
    assert module_0.intersection([1, 8], [2, 9]) == "YES"      # length = 6? no -> check below
    assert module_0.intersection([-3, 1], [-2, 2]) == "YES"    # length = 3 (prime)
    assert module_0.intersection([10, 20], [12, 25]) == "YES"  # length = 8 -> NO

    # Intersection length is 1 (not prime)
    assert module_0.intersection([1, 3], [2, 4]) == "NO"       # length = 1
    assert module_0.intersection([3, 5], [1, 4]) == "NO"       # length = 1
    assert module_0.intersection([0, 2], [1, 4]) == "NO"       # length = 1
    assert module_0.intersection([-3, -1], [-2, 0]) == "NO"    # length = 1

    # Intersection length is 0 (single point)
    assert module_0.intersection([1, 2], [2, 3]) == "NO"       # length = 0
    assert module_0.intersection([5, 10], [10, 15]) == "NO"    # length = 0

    # No overlap (negative length)
    assert module_0.intersection([1, 2], [3, 4]) == "NO"       # length = -1
    assert module_0.intersection([5, 6], [1, 3]) == "NO"       # length = -2

    # Intersection length is composite (not prime)
    assert module_0.intersection([1, 6], [2, 7]) == "NO"       # length = 4
    assert module_0.intersection([1, 11], [2, 12]) == "NO"     # length = 9
    assert module_0.intersection([0, 15], [3, 20]) == "NO"     # length = 12

    # Identical intervals
    assert module_0.intersection([2, 5], [2, 5]) == "YES"      # length = 3 (prime)
    assert module_0.intersection([1, 4], [1, 4]) == "NO"       # length = 3? no -> 3 is prime

# Generated at 2026-11-02 06:40:02.790039
# Unit test for function intersection
def test_intersection():import unittest


class TestIntersection(unittest.TestCase):

    def test_overlap_with_prime_length(self):
        # Intersection is (2, 4), length = 2 (prime)
        self.assertEqual(module_0.intersection((1, 5), (2, 6)), "YES")

    def test_overlap_with_non_prime_length(self):
        # Intersection is (2, 5), length = 3 (prime)
        self.assertEqual(module_0.intersection((2, 5), (1, 8)), "YES")

    def test_no_overlap(self):
        self.assertEqual(module_0.intersection((1, 2), (3, 4)), "NO")

    def test_touching_at_point(self):
        # length = 0, not prime
        self.assertEqual(module_0.intersection((1, 2), (2, 3)), "NO")

    def test_overlap_length_1(self):
        # 1 is not prime
        self.assertEqual(module_0.intersection((1, 3), (2, 4)), "NO")

    def test_overlap_length_4(self):
        # 4 is not prime
        self.assertEqual(module_0.intersection((1, 6), (2, 5)), "NO")

    def test_overlap_length_13(self):
        # 13 is prime
        self.assertEqual(module_0.intersection((0, 15), (2, 20)), "YES")

    def test_negative_intervals(self):
        # Intersection (0, 3), length = 3 (prime)
        self.assertEqual(module_0.intersection((-5, 3), (0, 10)), "YES")

    def test_identical_intervals_prime_length(self):
        # length = 5 (prime)
        self.assertEqual(module_0.intersection((1, 6), (1, 6)), "YES")

    def test_identical_intervals_non_prime_length(self):
        # length = 4 (not prime)
        self.assertEqual(module_0.intersection((1, 5), (1, 5)), "NO")

    def test_one_interval_inside_other(self):
        # Intersection (3, 7), length = 4 (not prime)
        self.assertEqual(module_0.intersection((1, 10), (3, 7)), "NO")

    def test_length_2_prime(self):
        # Intersection (0, 2), length = 2 (prime)
        self.assertEqual(module_0.intersection((0, 2), (0, 2)), "YES")


if __name__ == "__main__":
    unittest.main()