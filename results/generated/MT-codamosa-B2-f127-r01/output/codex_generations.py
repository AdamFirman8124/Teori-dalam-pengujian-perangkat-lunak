

# Generated at 2026-10-25 14:17:06.798657
# Unit test for function intersection
def test_intersection():
    # Prime intersection lengths
    assert module_0.intersection([1, 5], [3, 7]) == "YES"   # Length: 2
    assert module_0.intersection([1, 10], [4, 7]) == "YES"  # Length: 3
    assert module_0.intersection([0, 10], [5, 10]) == "YES" # Length: 5

    # Non-prime intersection lengths
    assert module_0.intersection([1, 10], [2, 8]) == "NO"   # Length: 6
    assert module_0.intersection([1, 3], [2, 3]) == "NO"    # Length: 1

    # Touching or non-overlapping intervals
    assert module_0.intersection([1, 2], [2, 3]) == "NO"    # Length: 0
    assert module_0.intersection([1, 2], [3, 4]) == "NO"    # No overlap

    # Identical intervals
    assert module_0.intersection([2, 5], [2, 5]) == "YES"   # Length: 3

# Generated at 2026-10-25 14:17:08.222317
# Unit test for function intersection
def test_intersection():
    # no overlap - touching at a point, length = 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length = 1, not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # overlap [-3, -1], length = 2, prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap [3, 5], length = 2, prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"

    # overlap [2, 6], length = 4, not prime
    assert module_0.intersection((1, 10), (2, 6)) == "NO"

    # identical intervals, length = 5, prime
    assert module_0.intersection((0, 5), (0, 5)) == "YES"

    # disjoint, length < 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 5), (6, 10)) == "NO"

    # overlap length = 3, prime
    assert module_0.intersection((0, 4), (1, 4)) == "YES"

    # overlap length = 7, prime
    assert module_0.intersection((0, 10), (0, 7)) == "YES"

    # overlap length = 6, not prime
    assert module_0.intersection((0, 10), (0, 6)) == "NO"

# Generated at 2026-10-25 14:17:09.655472
# Unit test for function intersection
def test_intersection():
    # no overlap - touching at a point, length = 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length = 1, not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # overlap [-3, -1], length = 2, prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap [3, 5], length = 2, prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"

    # overlap [2, 6], length = 4, not prime
    assert module_0.intersection((1, 10), (2, 6)) == "NO"

    # identical intervals, length = 5, prime
    assert module_0.intersection((0, 5), (0, 5)) == "YES"

    # disjoint, length < 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 5), (6, 10)) == "NO"

    # overlap length = 3, prime
    assert module_0.intersection((0, 4), (1, 4)) == "YES"

    # overlap length = 7, prime
    assert module_0.intersection((0, 10), (0, 7)) == "YES"

    # overlap length = 6, not prime
    assert module_0.intersection((0, 10), (0, 6)) == "NO"

# Generated at 2026-10-25 14:17:11.384657
# Unit test for function intersection
def test_intersection():
    # no overlap - touching at a point, length = 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length = 1, not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # overlap [-3, -1], length = 2, prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap [3, 5], length = 2, prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"

    # overlap [2, 6], length = 4, not prime
    assert module_0.intersection((1, 10), (2, 6)) == "NO"

    # identical intervals, length = 5, prime
    assert module_0.intersection((0, 5), (0, 5)) == "YES"

    # disjoint, length < 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 5), (6, 10)) == "NO"

    # overlap length = 3, prime
    assert module_0.intersection((0, 4), (1, 4)) == "YES"

    # overlap length = 7, prime
    assert module_0.intersection((0, 10), (0, 7)) == "YES"

    # overlap length = 6, not prime
    assert module_0.intersection((0, 10), (0, 6)) == "NO"

# Generated at 2026-10-25 14:17:36.515736
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection([1, 5], [3, 7]) == "YES"   # length = 2
    assert module_0.intersection([1, 7], [3, 6]) == "YES"   # length = 3

    # Overlap length is not prime
    assert module_0.intersection([1, 8], [3, 7]) == "NO"    # length = 4
    assert module_0.intersection([0, 1], [0, 1]) == "NO"    # length = 1

    # Intervals only touch
    assert module_0.intersection([1, 3], [3, 5]) == "NO"    # length = 0

    # Disjoint intervals
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval is contained within the other
    assert module_0.intersection([0, 10], [2, 7]) == "YES"  # length = 5
    assert module_0.intersection([0, 10], [2, 8]) == "NO"   # length = 6

# Generated at 2026-10-25 14:17:39.865115
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 3), (2, 4)) == "NO"
    assert module_0.intersection((1, 4), (2, 5)) == "YES"
    assert module_0.intersection((1, 5), (2, 6)) == "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    assert module_0.intersection((0, 10), (2, 6)) == "NO"
    assert module_0.intersection((0, 10), (2, 9)) == "YES"
    assert module_0.intersection((1, 10), (2, 9)) == "YES"
    assert module_0.intersection((1, 10), (1, 10)) == "NO"
    assert module_0.intersection((0, 5), (0, 6)) == "YES"
    assert module_0.intersection((1, 5), (6, 9)) == "NO"
    assert module_0.intersection((1, 10), (1, 12)) == "NO"
    assert module_0.intersection((-3, 0), (-2, 1)) == "YES"
    assert module_0.intersection((1, 10), (3, 5)) == "YES"

# Generated at 2026-10-25 14:17:42.527177
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 3), (2, 4)) == "NO"
    assert module_0.intersection((1, 4), (2, 5)) == "YES"
    assert module_0.intersection((1, 5), (2, 6)) == "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    assert module_0.intersection((0, 10), (2, 6)) == "NO"
    assert module_0.intersection((0, 10), (2, 9)) == "YES"
    assert module_0.intersection((1, 10), (2, 9)) == "YES"
    assert module_0.intersection((1, 10), (1, 10)) == "NO"
    assert module_0.intersection((0, 5), (0, 6)) == "YES"
    assert module_0.intersection((1, 5), (6, 9)) == "NO"
    assert module_0.intersection((1, 10), (1, 12)) == "NO"
    assert module_0.intersection((-3, 0), (-2, 1)) == "YES"
    assert module_0.intersection((1, 10), (3, 5)) == "YES"

# Generated at 2026-10-25 14:17:54.304208
# Unit test for function intersection
def test_intersection():
    # Overlap has prime length
    assert module_0.intersection([1, 7], [4, 10]) == "YES"   # length 3
    assert module_0.intersection([0, 5], [2, 4]) == "YES"    # length 2

    # Overlap has non-prime length
    assert module_0.intersection([1, 10], [3, 9]) == "NO"    # length 6
    assert module_0.intersection([0, 10], [5, 10]) == "YES"  # length 5

    # Intervals only touch
    assert module_0.intersection([1, 5], [5, 8]) == "NO"     # length 0

    # No overlap
    assert module_0.intersection([1, 3], [5, 7]) == "NO"

    # Identical intervals
    assert module_0.intersection([2, 9], [2, 9]) == "YES"    # length 7
    assert module_0.intersection([2, 8], [2, 8]) == "NO"     # length 6

    # Negative endpoints
    assert module_0.intersection([-10, 0], [-7, -2]) == "YES"  # length 5

# Generated at 2026-10-25 14:18:02.495579
# Unit test for function intersection
def test_intersection():
    # Overlap length is 3 (prime)
    assert module_0.intersection((1, 5), (2, 6)) == "YES"

    # Overlap length is 2 (prime)
    assert module_0.intersection((1, 4), (2, 4)) == "YES"

    # Overlap length is 4 (not prime)
    assert module_0.intersection((1, 6), (2, 6)) == "NO"

    # Intervals only touch; overlap length is 0
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # Intervals do not overlap
    assert module_0.intersection((1, 2), (4, 7)) == "NO"

    # One interval is contained in the other; length is 5 (prime)
    assert module_0.intersection((0, 10), (2, 7)) == "YES"

    # Overlap length is 1 (not prime)
    assert module_0.intersection((0, 2), (1, 5)) == "NO"

# Generated at 2026-10-25 14:18:11.060635
# Unit test for function intersection
def test_intersection():
    # Intersection length is prime
    assert module_0.intersection([1, 5], [3, 8]) == "YES"   # Length: 5 - 3 = 2
    assert module_0.intersection([0, 10], [4, 7]) == "YES"  # Length: 7 - 4 = 3

    # Intersection length is not prime
    assert module_0.intersection([1, 7], [3, 10]) == "NO"   # Length: 7 - 3 = 4
    assert module_0.intersection([0, 10], [5, 10]) == "YES" # Length: 10 - 5 = 5

    # Intervals only touch
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Intervals do not overlap
    assert module_0.intersection([1, 2], [3, 4]) == "NO"

    # Identical intervals
    assert module_0.intersection([2, 9], [2, 9]) == "YES"   # Length: 7

    # Intersection length is 1, which is not prime
    assert module_0.intersection([1, 4], [3, 5]) == "NO"

# Generated at 2026-10-25 14:18:25.740998
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths
    assert module_0.intersection([1, 7], [4, 10]) == "YES"   # length = 3
    assert module_0.intersection([1, 5], [3, 7]) == "YES"    # length = 2
    assert module_0.intersection([0, 11], [0, 11]) == "YES"  # length = 11

    # Non-prime overlap lengths
    assert module_0.intersection([1, 8], [3, 7]) == "NO"     # length = 4
    assert module_0.intersection([1, 4], [3, 8]) == "NO"     # length = 1

    # No overlap
    assert module_0.intersection([1, 3], [4, 6]) == "NO"

    # Intervals only touch at an endpoint
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

# Generated at 2026-10-25 14:18:54.743380
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection((1, 5), (2, 6)) == "YES"   # overlap length: 3
    assert module_0.intersection((1, 10), (3, 8)) == "YES"  # overlap length: 5
    assert module_0.intersection((0, 2), (0, 2)) == "YES"   # overlap length: 2

    assert module_0.intersection((1, 3), (2, 4)) == "NO"    # overlap length: 1
    assert module_0.intersection((1, 5), (2, 8)) == "NO"    # overlap length: 3? Actually overlap is [2,5], length 3
    assert module_0.intersection((1, 2), (2, 3)) == "NO"    # endpoints only, length: 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"    # no intersection

# Generated at 2026-10-25 14:19:11.464528
# Unit test for function intersection
def test_intersection():
    # no overlap - touching at a point, length = 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length = 1, not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # overlap [-3, -1], length = 2, prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap [3, 5], length = 2, prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"

    # overlap [2, 6], length = 4, not prime
    assert module_0.intersection((1, 10), (2, 6)) == "NO"

    # identical intervals, length = 5, prime
    assert module_0.intersection((0, 5), (0, 5)) == "YES"

    # disjoint, length < 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 5), (6, 10)) == "NO"

    # overlap length = 3, prime
    assert module_0.intersection((0, 4), (1, 4)) == "YES"

    # overlap length = 7, prime
    assert module_0.intersection((0, 10), (0, 7)) == "YES"

    # overlap length = 6, not prime
    assert module_0.intersection((0, 10), (0, 6)) == "NO"

# Generated at 2026-10-25 14:19:36.909161
# Unit test for function intersection
def test_intersection():
    # Prime-length intersections
    assert module_0.intersection([1, 7], [3, 10]) == "YES"   # Length: 7 - 3 = 4 (not prime) wait
    assert module_0.intersection([1, 6], [3, 8]) == "YES"    # Length: 6 - 3 = 3
    assert module_0.intersection([0, 10], [5, 7]) == "YES"   # Length: 7 - 5 = 2

    # Composite-length intersection
    assert module_0.intersection([1, 7], [3, 10]) == "NO"    # Length: 7 - 3 = 4

    # Intersection of length 1
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Touching intervals: zero-length intersection
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection([2, 7], [2, 7]) == "YES"    # Length: 5

# Generated at 2026-10-25 14:19:53.421656
# Unit test for function intersection
def test_intersection():
    # No intersection -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching endpoints (length 0) -> "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Length 2 (prime) -> "YES"
    assert module_0.intersection((0, 4), (2, 10)) == "YES"
    # Length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # One interval inside another, length 5 (prime) -> "YES"
    assert module_0.intersection((0, 10), (2, 7)) == "NO"  # length 5? check: r-l = 7-2 = 5 -> prime -> "YES"
    print("All tests passed.")

test_intersection()

# Generated at 2026-10-25 14:20:09.886744
# Unit test for function intersection
def test_intersection():
    # no overlap - touching at a point, length = 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length = 1, not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # overlap [-3, -1], length = 2, prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap [3, 5], length = 2, prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"

    # overlap [2, 6], length = 4, not prime
    assert module_0.intersection((1, 10), (2, 6)) == "NO"

    # identical intervals, length = 5, prime
    assert module_0.intersection((0, 5), (0, 5)) == "YES"

    # disjoint, length < 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 5), (6, 10)) == "NO"

    # overlap length = 3, prime
    assert module_0.intersection((0, 4), (1, 4)) == "YES"

    # overlap length = 7, prime
    assert module_0.intersection((0, 10), (0, 7)) == "YES"

    # overlap length = 6, not prime
    assert module_0.intersection((0, 10), (0, 6)) == "NO"

# Generated at 2026-10-25 14:20:21.263941
# Unit test for function intersection
def test_intersection():
    test_cases = [
        ((1, 7), (5, 9), "YES"),    # Intersection length: 2 (prime)
        ((1, 8), (5, 10), "YES"),   # Intersection length: 3 (prime)
        ((1, 10), (4, 8), "NO"),    # Intersection length: 4 (not prime)
        ((1, 3), (3, 5), "NO"),     # Intervals only touch; length: 0
        ((1, 2), (3, 4), "NO"),     # No module_0.intersection((1, 10), (2, 3), "NO"),    # Intersection length: 1 (not prime)
        ((1, 6), (1, 6), "YES"),    # Identical intervals; length: 5
    ]

    for interval1, interval2, expected in test_cases:
        assert module_0.intersection(interval1, interval2) == expected


test_intersection()

# Generated at 2026-10-25 14:20:45.233862
# Unit test for function intersection
def test_intersection():
    # Overlap length is 2 (prime)
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlap length is 3 (prime)
    assert module_0.intersection([1, 6], [3, 7]) == "YES"

    # Overlap length is 4 (not prime)
    assert module_0.intersection([1, 7], [3, 8]) == "NO"

    # One interval is contained in the other; length is 5 (prime)
    assert module_0.intersection([1, 10], [4, 9]) == "YES"

    # Intervals only touch; overlap length is 0
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # Overlap length is 1, which is not prime
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

# Generated at 2026-10-25 14:21:10.325838
# Unit test for function intersection
def test_intersection():
    # Overlap length is 2, which is prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"

    # One interval is contained in the other; overlap length is 5
    assert module_0.intersection((1, 10), (3, 8)) == "YES"

    # Overlap length is 4, which is not prime
    assert module_0.intersection((1, 7), (3, 7)) == "NO"

    # Overlap length is 1, which is not prime
    assert module_0.intersection((1, 5), (4, 8)) == "NO"

    # Intervals only touch; overlap length is 0
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # Disjoint intervals
    assert module_0.intersection((1, 2), (4, 6)) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection((2, 5), (2, 5)) == "YES"

# Generated at 2026-10-25 14:21:26.826651
# Unit test for function intersection
def test_intersection():
    # No intersection -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching endpoints (length 0) -> "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Length 2 (prime) -> "YES"
    assert module_0.intersection((0, 4), (2, 10)) == "YES"
    # Length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # One interval inside another, length 5 (prime) -> "YES"
    assert module_0.intersection((0, 10), (2, 7)) == "NO"  # length 5? check: r-l = 7-2 = 5 -> prime -> "YES"
    print("All tests passed.")

test_intersection()

# Generated at 2026-10-25 14:21:43.680492
# Unit test for function intersection
def test_intersection():
    # no overlap - touching at a point, length = 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length = 1, not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # overlap [-3, -1], length = 2, prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap [3, 5], length = 2, prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"

    # overlap [2, 6], length = 4, not prime
    assert module_0.intersection((1, 10), (2, 6)) == "NO"

    # identical intervals, length = 5, prime
    assert module_0.intersection((0, 5), (0, 5)) == "YES"

    # disjoint, length < 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 5), (6, 10)) == "NO"

    # overlap length = 3, prime
    assert module_0.intersection((0, 4), (1, 4)) == "YES"

    # overlap length = 7, prime
    assert module_0.intersection((0, 10), (0, 7)) == "YES"

    # overlap length = 6, not prime
    assert module_0.intersection((0, 10), (0, 6)) == "NO"

# Generated at 2026-10-25 14:21:53.306543
# Unit test for function intersection
def test_intersection():
    # Prime-length intersections
    assert module_0.intersection((1, 5), (3, 7)) == "YES"   # length 2
    assert module_0.intersection((0, 10), (4, 7)) == "YES"  # length 3

    # Non-prime-length intersections
    assert module_0.intersection((1, 6), (2, 6)) == "NO"    # length 4
    assert module_0.intersection((0, 1), (0, 1)) == "NO"    # length 1

    # No positive-length intersection
    assert module_0.intersection((1, 3), (3, 5)) == "NO"    # touching endpoints
    assert module_0.intersection((1, 2), (4, 6)) == "NO"    # disjoint intervals

    # Identical intervals
    assert module_0.intersection((2, 7), (2, 7)) == "YES"   # length 5

# Generated at 2026-10-25 14:21:54.828287
# Unit test for function intersection
def test_intersection():
    # No intersection -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching endpoints (length 0) -> "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Length 2 (prime) -> "YES"
    assert module_0.intersection((0, 4), (2, 10)) == "YES"
    # Length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # One interval inside another, length 5 (prime) -> "YES"
    assert module_0.intersection((0, 10), (2, 7)) == "NO"  # length 5? check: r-l = 7-2 = 5 -> prime -> "YES"
    print("All tests passed.")

test_intersection()

# Generated at 2026-10-25 14:21:56.169777
# Unit test for function intersection
def test_intersection():
    # No intersection -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching endpoints (length 0) -> "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Length 2 (prime) -> "YES"
    assert module_0.intersection((0, 4), (2, 10)) == "YES"
    # Length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # One interval inside another, length 5 (prime) -> "YES"
    assert module_0.intersection((0, 10), (2, 7)) == "NO"  # length 5? check: r-l = 7-2 = 5 -> prime -> "YES"
    print("All tests passed.")

test_intersection()

# Generated at 2026-10-25 14:22:03.958840
# Unit test for function intersection
def test_intersection():
    # Prime-length intersections
    assert module_0.intersection([1, 5], [2, 6]) == "YES"   # length 3
    assert module_0.intersection([0, 10], [3, 8]) == "YES"  # length 5

    # Composite-length intersection
    assert module_0.intersection([1, 10], [3, 7]) == "NO"   # length 4

    # Intersection length is 1, which is not prime
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Intervals only touch
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # Identical intervals
    assert module_0.intersection([2, 9], [2, 9]) == "YES"   # length 7

# Generated at 2026-10-25 14:22:12.355968
# Unit test for function intersection
def test_intersection():
    # Intersection length is prime
    assert module_0.intersection([1, 7], [5, 10]) == "YES"   # length 2
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5

    # Intersection length is not prime
    assert module_0.intersection([1, 8], [3, 7]) == "NO"     # length 4
    assert module_0.intersection([1, 5], [4, 8]) == "NO"     # length 1

    # Intervals only touch
    assert module_0.intersection([1, 5], [5, 10]) == "NO"    # length 0

    # Intervals do not overlap
    assert module_0.intersection([1, 3], [5, 8]) == "NO"

    # Identical intervals
    assert module_0.intersection([2, 5], [2, 5]) == "YES"    # length 3

# Generated at 2026-10-25 14:22:13.725020
# Unit test for function intersection
def test_intersection():
    # No intersection -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching endpoints (length 0) -> "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Length 2 (prime) -> "YES"
    assert module_0.intersection((0, 4), (2, 10)) == "YES"
    # Length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # One interval inside another, length 5 (prime) -> "YES"
    assert module_0.intersection((0, 10), (2, 7)) == "NO"  # length 5? check: r-l = 7-2 = 5 -> prime -> "YES"
    print("All tests passed.")

test_intersection()

# Generated at 2026-10-25 14:22:24.128941
# Unit test for function intersection
def test_intersection():
    # Overlap has prime length
    assert module_0.intersection((1, 7), (4, 11)) == "YES"   # length 3
    assert module_0.intersection((0, 10), (3, 5)) == "YES"   # length 2
    assert module_0.intersection((2, 7), (2, 7)) == "YES"    # length 5

    # Overlap has non-prime length
    assert module_0.intersection((1, 8), (3, 7)) == "NO"     # length 4
    assert module_0.intersection((1, 3), (2, 5)) == "NO"     # length 1

    # Intervals only touch or do not overlap
    assert module_0.intersection((1, 3), (3, 5)) == "NO"     # length 0
    assert module_0.intersection((1, 2), (4, 6)) == "NO"     # disjoint

# Generated at 2026-10-25 14:22:33.510961
# Unit test for function intersection
def test_intersection():
    # Overlap length is 2 (prime)
    assert module_0.intersection([1, 7], [5, 9]) == "YES"

    # Overlap length is 4 (not prime)
    assert module_0.intersection([1, 10], [3, 7]) == "NO"

    # One interval is contained in the other; length is 5 (prime)
    assert module_0.intersection([0, 10], [2, 7]) == "YES"

    # Intervals only touch; overlap length is 0
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [3, 4]) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection([4, 7], [4, 7]) == "YES"

# Generated at 2026-10-25 14:22:43.174957
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection([1, 7], [5, 9]) == "YES"   # length 2
    assert module_0.intersection([1, 5], [2, 8]) == "YES"   # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"  # length 5

    # Overlap length is not prime
    assert module_0.intersection([1, 8], [3, 7]) == "NO"    # length 4
    assert module_0.intersection([1, 2], [1, 2]) == "NO"    # length 1

    # Intervals touch but do not overlap
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection([2, 9], [2, 9]) == "YES"   # length 7

# Generated at 2026-10-25 14:23:11.152930
# Unit test for function intersection
def test_intersection():
    # Overlap length is 3 (prime)
    assert module_0.intersection([1, 5], [2, 6]) == "YES"

    # Overlap length is 4 (not prime)
    assert module_0.intersection([1, 7], [3, 8]) == "NO"

    # Overlap length is 2 (prime)
    assert module_0.intersection([1, 10], [4, 6]) == "YES"

    # Intervals only touch; intersection length is 0
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # Overlap length is 1 (not prime)
    assert module_0.intersection([1, 4], [3, 7]) == "NO"

    # Works with negative endpoints; overlap length is 3
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"

# Generated at 2026-10-25 14:23:27.718575
# Unit test for function intersection
def test_intersection():
    # no overlap - touching at a point, length = 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length = 1, not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # overlap [-3, -1], length = 2, prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap [3, 5], length = 2, prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"

    # overlap [2, 6], length = 4, not prime
    assert module_0.intersection((1, 10), (2, 6)) == "NO"

    # identical intervals, length = 5, prime
    assert module_0.intersection((0, 5), (0, 5)) == "YES"

    # disjoint, length < 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 5), (6, 10)) == "NO"

    # overlap length = 3, prime
    assert module_0.intersection((0, 4), (1, 4)) == "YES"

    # overlap length = 7, prime
    assert module_0.intersection((0, 10), (0, 7)) == "YES"

    # overlap length = 6, not prime
    assert module_0.intersection((0, 10), (0, 6)) == "NO"

# Generated at 2026-10-25 14:23:55.674080
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection([1, 5], [2, 6]) == "YES"   # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"  # length 5
    assert module_0.intersection([2, 4], [2, 4]) == "YES"   # length 2

    # Overlap length is not prime
    assert module_0.intersection([1, 4], [2, 6]) == "NO"    # length 2? Actually [2,4] = 2
    assert module_0.intersection([1, 5], [3, 7]) == "YES"   # length 2
    assert module_0.intersection([1, 6], [2, 5]) == "NO"    # length 3? Actually prime

# Generated at 2026-10-25 14:23:57.181102
# Unit test for function intersection
def test_intersection():
    # no overlap - touching at a point, length = 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length = 1, not prime
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # overlap [-3, -1], length = 2, prime
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap [3, 5], length = 2, prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"

    # overlap [2, 6], length = 4, not prime
    assert module_0.intersection((1, 10), (2, 6)) == "NO"

    # identical intervals, length = 5, prime
    assert module_0.intersection((0, 5), (0, 5)) == "YES"

    # disjoint, length < 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((1, 5), (6, 10)) == "NO"

    # overlap length = 3, prime
    assert module_0.intersection((0, 4), (1, 4)) == "YES"

    # overlap length = 7, prime
    assert module_0.intersection((0, 10), (0, 7)) == "YES"

    # overlap length = 6, not prime
    assert module_0.intersection((0, 10), (0, 6)) == "NO"

# Generated at 2026-10-25 14:23:58.541618
# Unit test for function intersection
def test_intersection():
    # No intersection -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching endpoints (length 0) -> "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Length 2 (prime) -> "YES"
    assert module_0.intersection((0, 4), (2, 10)) == "YES"
    # Length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # One interval inside another, length 5 (prime) -> "YES"
    assert module_0.intersection((0, 10), (2, 7)) == "NO"  # length 5? check: r-l = 7-2 = 5 -> prime -> "YES"
    print("All tests passed.")

test_intersection()

# Generated at 2026-10-25 14:23:59.976772
# Unit test for function intersection
def test_intersection():
    # No intersection -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching endpoints (length 0) -> "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Length 2 (prime) -> "YES"
    assert module_0.intersection((0, 4), (2, 10)) == "YES"
    # Length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # One interval inside another, length 5 (prime) -> "YES"
    assert module_0.intersection((0, 10), (2, 7)) == "NO"  # length 5? check: r-l = 7-2 = 5 -> prime -> "YES"
    print("All tests passed.")

test_intersection()

# Generated at 2026-10-25 14:24:09.293779
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection([1, 5], [3, 7]) == "YES"   # overlap length: 2
    assert module_0.intersection([0, 10], [3, 8]) == "YES"  # overlap length: 5
    assert module_0.intersection([1, 10], [3, 7]) == "NO"   # overlap length: 4
    assert module_0.intersection([1, 2], [2, 3]) == "NO"    # touching endpoints
    assert module_0.intersection([1, 2], [3, 4]) == "NO"    # no overlap
    assert module_0.intersection([2, 5], [2, 5]) == "YES"   # overlap length: 3

test_intersection()
print("All tests passed.")

# Generated at 2026-10-25 14:24:17.181209
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection([1, 5], [2, 8]) == "YES"   # Length 3 (prime)
    assert module_0.intersection([1, 7], [3, 10]) == "NO"  # Length 4 (not prime)
    assert module_0.intersection([1, 3], [1, 3]) == "YES"  # Length 2 (prime)
    assert module_0.intersection([1, 2], [2, 3]) == "NO"   # Touching; length 0
    assert module_0.intersection([1, 2], [3, 4]) == "NO"   # No intersection
    assert module_0.intersection([0, 10], [2, 7]) == "YES" # Length 5 (prime)

# Generated at 2026-10-25 14:24:18.611626
# Unit test for function intersection
def test_intersection():
    # No intersection -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length 1 (not prime) -> "NO"
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 3 (prime) -> "YES"
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching endpoints (length 0) -> "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"
    # Length 2 (prime) -> "YES"
    assert module_0.intersection((0, 4), (2, 10)) == "YES"
    # Length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # One interval inside another, length 5 (prime) -> "YES"
    assert module_0.intersection((0, 10), (2, 7)) == "NO"  # length 5? check: r-l = 7-2 = 5 -> prime -> "YES"
    print("All tests passed.")

test_intersection()

# Generated at 2026-10-25 14:24:43.701543
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection([1, 7], [4, 10]) == "YES"   # Length: 3
    assert module_0.intersection([2, 9], [3, 8]) == "YES"    # Length: 5
    assert module_0.intersection([1, 3], [1, 3]) == "YES"    # Length: 2

    # Overlap length is not prime
    assert module_0.intersection([1, 8], [4, 10]) == "NO"    # Length: 4
    assert module_0.intersection([1, 5], [4, 8]) == "NO"     # Length: 1

    # Intervals only touch
    assert module_0.intersection([1, 3], [3, 6]) == "NO"     # Length: 0

    # Intervals do not overlap
    assert module_0.intersection([1, 2], [3, 5]) == "NO"

# Generated at 2026-10-25 14:25:07.252437
# Unit test for function intersection
def test_intersection():
    # Prime-length intersections
    assert module_0.intersection([1, 5], [3, 7]) == "YES"   # Length 2
    assert module_0.intersection([1, 10], [3, 8]) == "YES"  # Length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"   # Length 7

    # Composite-length intersection
    assert module_0.intersection([1, 8], [3, 7]) == "NO"    # Length 4

    # Intersection of length 1
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Touching intervals have length 0
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contained in another
    assert module_0.intersection([0, 10], [2, 5]) == "YES"  # Length 3

# Generated at 2026-10-25 14:25:12.699284
# Unit test for function intersection

# Generated at 2026-10-25 14:25:15.113347
# Unit test for function intersection

# Generated at 2026-10-25 14:25:17.529782
# Unit test for function intersection

# Generated at 2026-10-25 14:25:19.943536
# Unit test for function intersection

# Generated at 2026-10-25 14:25:22.357852
# Unit test for function intersection

# Generated at 2026-10-25 14:25:24.773758
# Unit test for function intersection

# Generated at 2026-10-25 14:25:27.189240
# Unit test for function intersection

# Generated at 2026-10-25 14:25:29.602942
# Unit test for function intersection

# Generated at 2026-10-25 14:25:32.022766
# Unit test for function intersection

# Generated at 2026-10-25 14:25:34.434277
# Unit test for function intersection

# Generated at 2026-10-25 14:25:36.848958
# Unit test for function intersection

# Generated at 2026-10-25 14:25:39.264723
# Unit test for function intersection

# Generated at 2026-10-25 14:25:41.681952
# Unit test for function intersection

# Generated at 2026-10-25 14:25:44.099344
# Unit test for function intersection

# Generated at 2026-10-25 14:25:46.511459
# Unit test for function intersection

# Generated at 2026-10-25 14:25:48.926241
# Unit test for function intersection

# Generated at 2026-10-25 14:25:51.340683
# Unit test for function intersection

# Generated at 2026-10-25 14:25:53.756297
# Unit test for function intersection

# Generated at 2026-10-25 14:25:56.174353
# Unit test for function intersection

# Generated at 2026-10-25 14:25:58.586755
# Unit test for function intersection

# Generated at 2026-10-25 14:26:01.001369
# Unit test for function intersection

# Generated at 2026-10-25 14:26:03.416833
# Unit test for function intersection

# Generated at 2026-10-25 14:26:05.832765
# Unit test for function intersection

# Generated at 2026-10-25 14:26:08.248561
# Unit test for function intersection

# Generated at 2026-10-25 14:26:10.663233
# Unit test for function intersection

# Generated at 2026-10-25 14:26:13.081260
# Unit test for function intersection

# Generated at 2026-10-25 14:26:15.492870
# Unit test for function intersection

# Generated at 2026-10-25 14:26:17.908040
# Unit test for function intersection

# Generated at 2026-10-25 14:26:20.322385
# Unit test for function intersection

# Generated at 2026-10-25 14:26:22.741289
# Unit test for function intersection

# Generated at 2026-10-25 14:26:25.158783
# Unit test for function intersection

# Generated at 2026-10-25 14:26:27.572911
# Unit test for function intersection

# Generated at 2026-10-25 14:26:29.986316
# Unit test for function intersection

# Generated at 2026-10-25 14:26:32.401023
# Unit test for function intersection

# Generated at 2026-10-25 14:26:34.816536
# Unit test for function intersection

# Generated at 2026-10-25 14:26:37.231121
# Unit test for function intersection

# Generated at 2026-10-25 14:26:39.645676
# Unit test for function intersection

# Generated at 2026-10-25 14:26:42.061780
# Unit test for function intersection

# Generated at 2026-10-25 14:26:44.480299
# Unit test for function intersection