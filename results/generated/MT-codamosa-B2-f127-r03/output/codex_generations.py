

# Generated at 2026-10-25 01:09:58.505815
# Unit test for function intersection

# Generated at 2026-10-25 01:10:01.023170
# Unit test for function intersection

# Generated at 2026-10-25 01:10:03.564178
# Unit test for function intersection

# Generated at 2026-10-25 01:10:05.988548
# Unit test for function intersection

# Generated at 2026-10-25 01:10:08.402707
# Unit test for function intersection

# Generated at 2026-10-25 01:10:10.817145
# Unit test for function intersection

# Generated at 2026-10-25 01:10:13.231506
# Unit test for function intersection

# Generated at 2026-10-25 01:10:15.646420
# Unit test for function intersection

# Generated at 2026-10-25 01:10:18.061264
# Unit test for function intersection

# Generated at 2026-10-25 01:10:20.478537
# Unit test for function intersection

# Generated at 2026-10-25 01:10:22.898064
# Unit test for function intersection

# Generated at 2026-10-25 01:10:25.315312
# Unit test for function intersection

# Generated at 2026-10-25 01:10:27.730054
# Unit test for function intersection

# Generated at 2026-10-25 01:10:30.144890
# Unit test for function intersection

# Generated at 2026-10-25 01:10:32.557671
# Unit test for function intersection

# Generated at 2026-10-25 01:10:40.834600
# Unit test for function intersection
def test_intersection():
    # No intersection -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection (2, 3), length 1 -> not prime -> NO
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 2 (prime) -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching at a single point, length 0 -> NO
    assert module_0.intersection((0, 4), (4, 8)) == "NO"
    # One interval fully inside another, length 4 -> not prime -> NO
    assert module_0.intersection((0, 10), (3, 7)) == "YES" if False else "NO" == module_0.intersection((0, 10), (3, 7))
    # Length 3 (prime) -> YES
    assert module_0.intersection((0, 5), (2, 8)) == "YES"
    # Length 5 (prime) -> YES
    assert module_0.intersection((1, 10), (5, 15)) == "YES"
    # Length 6 (not prime) -> NO
    assert module_0.intersection((0, 10), (2, 12)) == "NO"
    # Identical intervals, length 10 (not prime) -> NO
    assert module_0.intersection((0, 10), (0, 10)) == "NO"
    # Identical intervals, length 7 (prime) -> YES
    assert module_0.intersection((0, 7), (0, 7)) == "YES"
    # Negative intervals, length 2 (prime) -> YES
    assert module_0.intersection((-10, -4), (-8, 0)) == "YES"
    print("All tests passed!")


test_intersection()

# Generated at 2026-10-25 01:10:50.740885
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection([1, 8], [3, 10]) == "YES"   # Length: 5
    assert module_0.intersection([0, 11], [2, 7]) == "YES"   # Length: 5
    assert module_0.intersection([1, 4], [2, 5]) == "YES"    # Length: 2

    # Overlap length is not prime
    assert module_0.intersection([1, 7], [3, 10]) == "NO"    # Length: 4
    assert module_0.intersection([1, 5], [2, 6]) == "NO"     # Length: 3?

# Generated at 2026-10-25 01:10:57.929371
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection([1, 5], [3, 7]) == "YES"   # Overlap length: 2
    assert module_0.intersection([1, 7], [3, 8]) == "NO"    # Overlap length: 4
    assert module_0.intersection([1, 3], [3, 5]) == "NO"    # Touching endpoints
    assert module_0.intersection([1, 2], [3, 4]) == "NO"    # No intersection
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES" # Overlap length: 3
    assert module_0.intersection([0, 1], [0, 1]) == "NO"    # Length 1 is not prime

# Generated at 2026-10-25 01:11:06.428097
# Unit test for function intersection
def test_intersection():
    # Prime-length intersections
    assert module_0.intersection([1, 7], [5, 9]) == "YES"   # Length 2
    assert module_0.intersection([1, 8], [3, 9]) == "YES"   # Length 5
    assert module_0.intersection([0, 10], [2, 5]) == "YES"  # Length 3
    assert module_0.intersection([4, 11], [4, 11]) == "YES" # Length 7

    # Non-prime-length intersections
    assert module_0.intersection([1, 10], [3, 9]) == "NO"   # Length 6
    assert module_0.intersection([1, 2], [1, 3]) == "NO"    # Length 1
    assert module_0.intersection([-10, -2], [-7, -3]) == "NO"  # Length 4

    # Empty intersections
    assert module_0.intersection([1, 3], [3, 5]) == "NO"    # Touching endpoints
    assert module_0.intersection([1, 2], [3, 4]) == "NO"    # Disjoint intervals

# Generated at 2026-10-25 01:11:12.775457
# Unit test for function intersection
def test_intersection():
    # Intersection length is 2 (prime)
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Intersection length is 3 (prime)
    assert module_0.intersection([0, 10], [4, 7]) == "YES"

    # Intersection length is 4 (not prime)
    assert module_0.intersection([1, 8], [4, 8]) == "NO"

    # Intersection length is 1 (not prime)
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Intervals only touch, so intersection length is 0
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Intervals do not overlap
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection([2, 7], [2, 7]) == "YES"

# Generated at 2026-10-25 01:11:20.352898
# Unit test for function intersection
def test_intersection():
    # Overlap length is 2, which is prime
    assert module_0.intersection([1, 7], [5, 10]) == "YES"

    # Overlap length is 4, which is not prime
    assert module_0.intersection([1, 8], [4, 10]) == "NO"

    # One interval contains the other; overlap length is 5
    assert module_0.intersection([1, 10], [3, 8]) == "YES"

    # Intervals only touch; overlap length is 0
    assert module_0.intersection([1, 5], [5, 9]) == "NO"

    # Intervals do not overlap
    assert module_0.intersection([1, 3], [5, 7]) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection([2, 13], [2, 13]) == "YES"

# Generated at 2026-10-25 01:11:22.883704
# Unit test for function intersection

# Generated at 2026-10-25 01:11:25.397627
# Unit test for function intersection

# Generated at 2026-10-25 01:11:27.917136
# Unit test for function intersection

# Generated at 2026-10-25 01:11:30.332131
# Unit test for function intersection

# Generated at 2026-10-25 01:11:32.750058
# Unit test for function intersection

# Generated at 2026-10-25 01:11:35.161399
# Unit test for function intersection

# Generated at 2026-10-25 01:11:37.576490
# Unit test for function intersection

# Generated at 2026-10-25 01:11:39.992176
# Unit test for function intersection

# Generated at 2026-10-25 01:11:52.198469
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 7)) == "YES"

# Generated at 2026-10-25 01:12:00.503442
# Unit test for function intersection
def test_intersection():
    test_cases = [
        ((1, 7), (4, 10), "YES"),   # Intersection length: 3 (prime)
        ((1, 6), (4, 10), "YES"),   # Intersection length: 2 (prime)
        ((1, 8), (4, 10), "NO"),    # Intersection length: 4
        ((0, 10), (2, 7), "YES"),   # Contained interval, length: 5
        ((1, 3), (3, 5), "NO"),     # Intervals only touch
        ((1, 2), (3, 4), "NO"),     # No module_0.intersection((2, 3), (2, 3), "NO"),     # Intersection length: 1
    ]

    for interval1, interval2, expected in test_cases:
        assert module_0.intersection(interval1, interval2) == expected
        # Intersection should be symmetric
        assert module_0.intersection(interval2, interval1) == expected

# Generated at 2026-10-25 01:12:06.228408
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection([1, 5], [2, 4]) == "YES"   # overlap length: 2
    assert module_0.intersection([1, 8], [3, 7]) == "NO"    # overlap length: 4
    assert module_0.intersection([1, 3], [5, 8]) == "NO"    # no overlap
    assert module_0.intersection([1, 3], [3, 6]) == "NO"    # intervals only touch
    assert module_0.intersection([-5, 2], [-3, 0]) == "YES" # overlap length: 3
    assert module_0.intersection([0, 1], [0, 1]) == "NO"    # overlap length: 1

# Generated at 2026-10-25 01:12:13.399123
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths
    assert module_0.intersection([1, 5], [3, 7]) == "YES"       # Length 2
    assert module_0.intersection([1, 6], [3, 8]) == "YES"       # Length 3
    assert module_0.intersection([-5, 2], [-3, 4]) == "YES"     # Length 5

    # Composite or non-prime overlap lengths
    assert module_0.intersection([1, 7], [3, 9]) == "NO"        # Length 4
    assert module_0.intersection([0, 1], [0, 1]) == "NO"        # Length 1

    # Touching and disjoint intervals
    assert module_0.intersection([1, 3], [3, 5]) == "NO"        # Length 0
    assert module_0.intersection([1, 2], [3, 4]) == "NO"        # No overlap

    # One interval contained in the other
    assert module_0.intersection([0, 10], [2, 5]) == "YES"      # Length 3

# Generated at 2026-10-25 01:12:20.053417
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection([1, 7], [5, 9]) == "YES"   # Overlap length: 2
    assert module_0.intersection([1, 8], [3, 7]) == "NO"    # Overlap length: 4
    assert module_0.intersection([1, 10], [3, 8]) == "YES"  # Overlap length: 5
    assert module_0.intersection([0, 3], [0, 3]) == "YES"   # Overlap length: 3
    assert module_0.intersection([0, 1], [0, 1]) == "NO"    # Overlap length: 1
    assert module_0.intersection([1, 3], [3, 5]) == "NO"    # Touching; length: 0
    assert module_0.intersection([1, 2], [4, 6]) == "NO"    # No overlap
    assert module_0.intersection([-5, 2], [-3, 0]) == "YES" # Overlap length: 3

# Generated at 2026-10-25 01:12:22.469577
# Unit test for function intersection

# Generated at 2026-10-25 01:12:24.885630
# Unit test for function intersection

# Generated at 2026-10-25 01:12:27.300887
# Unit test for function intersection

# Generated at 2026-10-25 01:12:29.717335
# Unit test for function intersection

# Generated at 2026-10-25 01:12:32.131719
# Unit test for function intersection

# Generated at 2026-10-25 01:12:34.548217
# Unit test for function intersection

# Generated at 2026-10-25 01:12:36.970795
# Unit test for function intersection

# Generated at 2026-10-25 01:12:39.386015
# Unit test for function intersection

# Generated at 2026-10-25 01:12:41.803250
# Unit test for function intersection

# Generated at 2026-10-25 01:12:44.214846
# Unit test for function intersection

# Generated at 2026-10-25 01:12:46.630626
# Unit test for function intersection

# Generated at 2026-10-25 01:12:49.045551
# Unit test for function intersection

# Generated at 2026-10-25 01:12:51.460960
# Unit test for function intersection

# Generated at 2026-10-25 01:12:53.875138
# Unit test for function intersection

# Generated at 2026-10-25 01:12:56.290620
# Unit test for function intersection

# Generated at 2026-10-25 01:12:58.704924
# Unit test for function intersection

# Generated at 2026-10-25 01:13:01.119936
# Unit test for function intersection

# Generated at 2026-10-25 01:13:03.537733
# Unit test for function intersection

# Generated at 2026-10-25 01:13:05.948302
# Unit test for function intersection

# Generated at 2026-10-25 01:13:08.363095
# Unit test for function intersection

# Generated at 2026-10-25 01:13:09.776783
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 7)) == "YES"

# Generated at 2026-10-25 01:13:18.314090
# Unit test for function intersection
def test_intersection():
    # Prime-length overlaps
    assert module_0.intersection((1, 5), (2, 6)) == "YES"     # Length 3
    assert module_0.intersection((1, 4), (2, 6)) == "YES"     # Length 2
    assert module_0.intersection((0, 10), (2, 9)) == "YES"    # Length 7
    assert module_0.intersection((-5, 0), (-3, 2)) == "YES"   # Length 3

    # Non-prime-length overlaps
    assert module_0.intersection((1, 6), (2, 6)) == "NO"      # Length 4
    assert module_0.intersection((0, 1), (0, 1)) == "NO"      # Length 1

    # Touching and disjoint intervals
    assert module_0.intersection((1, 3), (3, 5)) == "NO"      # Length 0
    assert module_0.intersection((1, 2), (3, 4)) == "NO"      # No overlap

# Generated at 2026-10-25 01:13:24.671099
# Unit test for function intersection
def test_intersection():
    # Intersection length is 3, which is prime
    assert module_0.intersection((1, 5), (2, 6)) == "YES"

    # Intersection length is 2, which is prime
    assert module_0.intersection((1, 3), (1, 4)) == "YES"

    # Intersection length is 4, which is not prime
    assert module_0.intersection((1, 5), (1, 6)) == "NO"

    # Intervals only touch, so the intersection length is 0
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # Intervals do not overlap
    assert module_0.intersection((1, 2), (4, 7)) == "NO"

    # Intersection length is 1, which is not prime
    assert module_0.intersection((1, 5), (4, 8)) == "NO"

# Generated at 2026-10-25 01:13:32.265211
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection([1, 5], [3, 7]) == "YES"  # Length 2 (prime)
    assert module_0.intersection([1, 7], [3, 8]) == "NO"   # Length 4
    assert module_0.intersection([1, 2], [3, 4]) == "NO"   # No intersection
    assert module_0.intersection([1, 3], [3, 5]) == "NO"   # Touching endpoints; length 0
    assert module_0.intersection([1, 6], [1, 6]) == "YES"  # Length 5 (prime)
    assert module_0.intersection([2, 6], [3, 4]) == "NO"   # Length 1 is not prime
    assert module_0.intersection([0, 10], [3, 6]) == "YES" # Length 3 (prime)

# Generated at 2026-10-25 01:13:40.029550
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection((1, 7), (3, 5)) == "YES"   # Length 2
    assert module_0.intersection((1, 5), (2, 5)) == "YES"   # Length 3
    assert module_0.intersection((1, 10), (3, 8)) == "YES"  # Length 5

    # Overlap length is not prime
    assert module_0.intersection((1, 7), (3, 7)) == "NO"    # Length 4
    assert module_0.intersection((1, 5), (4, 8)) == "NO"    # Length 1

    # Intervals only touch
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # No intersection
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # Identical intervals
    assert module_0.intersection((2, 9), (2, 9)) == "YES"   # Length 7

# Generated at 2026-10-25 01:13:46.375854
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection([1, 7], [5, 9]) == "YES"   # Overlap length: 2
    assert module_0.intersection([1, 10], [7, 15]) == "YES" # Overlap length: 3
    assert module_0.intersection([1, 8], [3, 7]) == "NO"    # Overlap length: 4
    assert module_0.intersection([1, 3], [3, 5]) == "NO"    # Touching endpoints
    assert module_0.intersection([1, 2], [3, 4]) == "NO"    # No overlap
    assert module_0.intersection([2, 7], [2, 7]) == "YES"   # Overlap length: 5

# Generated at 2026-10-25 01:13:49.060172
# Unit test for function intersection

# Generated at 2026-10-25 01:13:51.605835
# Unit test for function intersection

# Generated at 2026-10-25 01:13:54.020863
# Unit test for function intersection

# Generated at 2026-10-25 01:13:56.438760
# Unit test for function intersection

# Generated at 2026-10-25 01:13:58.855559
# Unit test for function intersection

# Generated at 2026-10-25 01:14:01.268874
# Unit test for function intersection

# Generated at 2026-10-25 01:14:03.686783
# Unit test for function intersection

# Generated at 2026-10-25 01:14:06.103150
# Unit test for function intersection

# Generated at 2026-10-25 01:14:08.518779
# Unit test for function intersection

# Generated at 2026-10-25 01:14:11.117407
# Unit test for function intersection
def test_intersection():
    # No intersection -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection (2, 3), length 1 -> not prime -> NO
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length 2 (prime) -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Touching at a single point, length 0 -> NO
    assert module_0.intersection((0, 4), (4, 8)) == "NO"
    # One interval fully inside another, length 4 -> not prime -> NO
    assert module_0.intersection((0, 10), (3, 7)) == "YES" if False else "NO" == module_0.intersection((0, 10), (3, 7))
    # Length 3 (prime) -> YES
    assert module_0.intersection((0, 5), (2, 8)) == "YES"
    # Length 5 (prime) -> YES
    assert module_0.intersection((1, 10), (5, 15)) == "YES"
    # Length 6 (not prime) -> NO
    assert module_0.intersection((0, 10), (2, 12)) == "NO"
    # Identical intervals, length 10 (not prime) -> NO
    assert module_0.intersection((0, 10), (0, 10)) == "NO"
    # Identical intervals, length 7 (prime) -> YES
    assert module_0.intersection((0, 7), (0, 7)) == "YES"
    # Negative intervals, length 2 (prime) -> YES
    assert module_0.intersection((-10, -4), (-8, 0)) == "YES"
    print("All tests passed!")


test_intersection()

# Generated at 2026-10-25 01:14:19.143524
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection((1, 5), (3, 8)) == "YES"   # Length 2
    assert module_0.intersection((1, 6), (2, 5)) == "YES"   # Length 3

    # Overlap length is not prime
    assert module_0.intersection((1, 7), (2, 6)) == "NO"    # Length 4
    assert module_0.intersection((1, 5), (4, 8)) == "NO"    # Length 1

    # Intervals only touch
    assert module_0.intersection((1, 3), (3, 5)) == "NO"    # Length 0

    # Intervals do not overlap
    assert module_0.intersection((1, 2), (4, 6)) == "NO"

    # Identical intervals
    assert module_0.intersection((2, 7), (2, 7)) == "YES"   # Length 5

# Generated at 2026-10-25 01:14:27.747194
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths
    assert module_0.intersection([1, 7], [4, 10]) == "YES"  # length 3
    assert module_0.intersection([1, 5], [3, 7]) == "YES"   # length 2
    assert module_0.intersection([0, 10], [2, 9]) == "YES"  # length 7

    # Non-prime overlap lengths
    assert module_0.intersection([1, 5], [1, 5]) == "NO"    # length 4
    assert module_0.intersection([1, 4], [3, 6]) == "NO"    # length 1

    # Touching intervals and disjoint intervals
    assert module_0.intersection([1, 3], [3, 5]) == "NO"    # length 0
    assert module_0.intersection([1, 2], [3, 4]) == "NO"    # no overlap

    # One interval contained within another
    assert module_0.intersection([1, 10], [3, 8]) == "YES"  # length 5

# Generated at 2026-10-25 01:14:36.142409
# Unit test for function intersection
def test_intersection():
    # Overlap length is 2 (prime)
    assert module_0.intersection([1, 7], [5, 9]) == "YES"

    # Overlap length is 3 (prime)
    assert module_0.intersection([1, 8], [5, 10]) == "YES"

    # Overlap length is 4 (not prime)
    assert module_0.intersection([1, 9], [5, 10]) == "NO"

    # One interval contained in another; overlap length is 6
    assert module_0.intersection([1, 10], [3, 9]) == "NO"

    # No overlap
    assert module_0.intersection([1, 3], [4, 6]) == "NO"

    # Intervals only touch at one endpoint
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection([2, 7], [2, 7]) == "YES"

# Generated at 2026-10-25 01:14:44.641656
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection([1, 8], [3, 10]) == "YES"   # length 5
    assert module_0.intersection([0, 10], [2, 5]) == "YES"   # length 3
    assert module_0.intersection([1, 5], [3, 7]) == "YES"    # length 2

    # Overlap length is not prime
    assert module_0.intersection([1, 7], [3, 8]) == "NO"     # length 4
    assert module_0.intersection([0, 1], [0, 1]) == "NO"     # length 1

    # Intervals only touch or do not overlap
    assert module_0.intersection([1, 3], [3, 5]) == "NO"     # length 0
    assert module_0.intersection([1, 2], [3, 4]) == "NO"     # disjoint

# Generated at 2026-10-25 01:14:47.059556
# Unit test for function intersection

# Generated at 2026-10-25 01:14:49.475660
# Unit test for function intersection

# Generated at 2026-10-25 01:14:51.890944
# Unit test for function intersection

# Generated at 2026-10-25 01:14:54.305683
# Unit test for function intersection

# Generated at 2026-10-25 01:14:56.720770
# Unit test for function intersection

# Generated at 2026-10-25 01:14:59.138215
# Unit test for function intersection

# Generated at 2026-10-25 01:15:01.551550
# Unit test for function intersection

# Generated at 2026-10-25 01:15:03.967053
# Unit test for function intersection

# Generated at 2026-10-25 01:15:06.382759
# Unit test for function intersection

# Generated at 2026-10-25 01:15:08.798254
# Unit test for function intersection

# Generated at 2026-10-25 01:15:11.213743
# Unit test for function intersection

# Generated at 2026-10-25 01:15:13.629549
# Unit test for function intersection

# Generated at 2026-10-25 01:15:16.042624
# Unit test for function intersection

# Generated at 2026-10-25 01:15:18.457554
# Unit test for function intersection

# Generated at 2026-10-25 01:15:20.873222
# Unit test for function intersection

# Generated at 2026-10-25 01:15:23.288747
# Unit test for function intersection

# Generated at 2026-10-25 01:15:25.704357
# Unit test for function intersection

# Generated at 2026-10-25 01:15:28.119994
# Unit test for function intersection

# Generated at 2026-10-25 01:15:30.538355
# Unit test for function intersection

# Generated at 2026-10-25 01:15:32.950678
# Unit test for function intersection

# Generated at 2026-10-25 01:15:35.366265
# Unit test for function intersection

# Generated at 2026-10-25 01:15:37.780813
# Unit test for function intersection

# Generated at 2026-10-25 01:15:40.196062
# Unit test for function intersection

# Generated at 2026-10-25 01:15:42.611596
# Unit test for function intersection

# Generated at 2026-10-25 01:15:45.027244
# Unit test for function intersection

# Generated at 2026-10-25 01:15:47.453583
# Unit test for function intersection

# Generated at 2026-10-25 01:15:49.858555
# Unit test for function intersection

# Generated at 2026-10-25 01:15:52.276453
# Unit test for function intersection

# Generated at 2026-10-25 01:15:54.692676
# Unit test for function intersection

# Generated at 2026-10-25 01:15:57.110240
# Unit test for function intersection

# Generated at 2026-10-25 01:15:59.525283
# Unit test for function intersection

# Generated at 2026-10-25 01:16:01.939397
# Unit test for function intersection

# Generated at 2026-10-25 01:16:04.354945
# Unit test for function intersection

# Generated at 2026-10-25 01:16:06.770908
# Unit test for function intersection

# Generated at 2026-10-25 01:16:09.185268
# Unit test for function intersection

# Generated at 2026-10-25 01:16:11.603948
# Unit test for function intersection

# Generated at 2026-10-25 01:16:14.017047
# Unit test for function intersection

# Generated at 2026-10-25 01:16:16.431668
# Unit test for function intersection

# Generated at 2026-10-25 01:16:18.847085
# Unit test for function intersection

# Generated at 2026-10-25 01:16:21.261963
# Unit test for function intersection

# Generated at 2026-10-25 01:16:23.677962
# Unit test for function intersection

# Generated at 2026-10-25 01:16:26.098501
# Unit test for function intersection

# Generated at 2026-10-25 01:16:28.509692
# Unit test for function intersection

# Generated at 2026-10-25 01:16:30.923647
# Unit test for function intersection

# Generated at 2026-10-25 01:16:33.339094
# Unit test for function intersection

# Generated at 2026-10-25 01:16:35.754086
# Unit test for function intersection

# Generated at 2026-10-25 01:16:38.169530
# Unit test for function intersection

# Generated at 2026-10-25 01:16:40.585056
# Unit test for function intersection

# Generated at 2026-10-25 01:16:42.999142
# Unit test for function intersection

# Generated at 2026-10-25 01:16:45.414771
# Unit test for function intersection

# Generated at 2026-10-25 01:16:47.832158
# Unit test for function intersection

# Generated at 2026-10-25 01:16:50.246178
# Unit test for function intersection

# Generated at 2026-10-25 01:16:52.660899
# Unit test for function intersection

# Generated at 2026-10-25 01:16:55.075700
# Unit test for function intersection

# Generated at 2026-10-25 01:16:57.490727
# Unit test for function intersection

# Generated at 2026-10-25 01:16:59.906342
# Unit test for function intersection

# Generated at 2026-10-25 01:17:02.319405
# Unit test for function intersection

# Generated at 2026-10-25 01:17:04.734722
# Unit test for function intersection

# Generated at 2026-10-25 01:17:07.149339
# Unit test for function intersection

# Generated at 2026-10-25 01:17:09.563849
# Unit test for function intersection

# Generated at 2026-10-25 01:17:11.978978
# Unit test for function intersection

# Generated at 2026-10-25 01:17:20.172324
# Unit test for function intersection
def test_intersection():assert module_0.intersection([1, 5], [2, 7]) == "YES"

# Generated at 2026-10-25 01:17:28.672993
# Unit test for function intersection
def test_intersection():
    # Prime-length overlaps
    assert module_0.intersection([1, 8], [3, 6]) == "YES"       # length 3
    assert module_0.intersection([0, 10], [2, 7]) == "YES"      # length 5
    assert module_0.intersection([-10, 0], [-7, -2]) == "YES"   # length 5

    # Non-prime-length overlaps
    assert module_0.intersection([1, 8], [3, 7]) == "NO"        # length 4
    assert module_0.intersection([0, 10], [2, 8]) == "NO"       # length 6
    assert module_0.intersection([1, 2], [1, 2]) == "NO"        # length 1

    # No positive-length overlap
    assert module_0.intersection([1, 3], [3, 5]) == "NO"        # touching only
    assert module_0.intersection([1, 2], [4, 5]) == "NO"        # disjoint

# Generated at 2026-10-25 01:17:36.576315
# Unit test for function intersection
def test_intersection():
    # Prime-length intersections
    assert module_0.intersection((1, 5), (3, 7)) == "YES"   # Length 2
    assert module_0.intersection((1, 6), (3, 8)) == "YES"   # Length 3
    assert module_0.intersection((1, 8), (3, 9)) == "YES"   # Length 5

    # Non-prime-length intersection
    assert module_0.intersection((1, 10), (3, 9)) == "NO"   # Length 6

    # Touching intervals have zero-length intersection
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # Disjoint intervals
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection((2, 4), (2, 4)) == "YES"

    # Function should be symmetric
    assert module_0.intersection((3, 7), (1, 5)) == "YES"

# Generated at 2026-10-25 01:17:44.441842
# Unit test for function intersection
def test_intersection():
    # Overlap length is 2 (prime)
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlap length is 5 (prime)
    assert module_0.intersection([0, 10], [2, 7]) == "YES"

    # Overlap length is 4 (not prime)
    assert module_0.intersection([1, 7], [3, 9]) == "NO"

    # Intervals only touch; overlap length is 0
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval is contained in the other; length is 3 (prime)
    assert module_0.intersection([0, 10], [4, 7]) == "YES"

    # Identical intervals with length 1 (not prime)
    assert module_0.intersection([2, 3], [2, 3]) == "NO"

# Generated at 2026-10-25 01:17:52.239042
# Unit test for function intersection
def test_intersection():
    # Overlap length is 3 (prime)
    assert module_0.intersection([1, 7], [4, 10]) == "YES"

    # Overlap length is 2 (prime)
    assert module_0.intersection([1, 5], [3, 8]) == "YES"

    # Overlap length is 4 (not prime)
    assert module_0.intersection([1, 8], [3, 7]) == "NO"

    # Overlap length is 1 (not prime)
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Intervals only touch; overlap length is 0
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [4, 7]) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection([2, 7], [2, 7]) == "YES"

# Generated at 2026-10-25 01:17:54.812559
# Unit test for function intersection

# Generated at 2026-10-25 01:17:57.230455
# Unit test for function intersection

# Generated at 2026-10-25 01:17:59.640758
# Unit test for function intersection

# Generated at 2026-10-25 01:18:02.056455
# Unit test for function intersection

# Generated at 2026-10-25 01:18:04.470830
# Unit test for function intersection

# Generated at 2026-10-25 01:18:06.885718
# Unit test for function intersection

# Generated at 2026-10-25 01:18:10.360232
# Unit test for function intersection

# Generated at 2026-10-25 01:18:12.775813
# Unit test for function intersection

# Generated at 2026-10-25 01:18:15.351936
# Unit test for function intersection
def test_intersection():assert module_0.intersection([1, 5], [2, 7]) == "YES"

# Generated at 2026-10-25 01:18:23.472322
# Unit test for function intersection
def test_intersection():
    # Prime-length intersections
    assert module_0.intersection([1, 5], [2, 7]) == "YES"   # [2, 5], length 3
    assert module_0.intersection([0, 10], [3, 5]) == "YES"  # [3, 5], length 2

    # Non-prime-length intersection
    assert module_0.intersection([1, 8], [3, 7]) == "NO"    # [3, 7], length 4

    # No intersection
    assert module_0.intersection([1, 3], [5, 8]) == "NO"

    # Intervals only touch, so intersection length is 0
    assert module_0.intersection([1, 3], [3, 6]) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection([4, 9], [4, 9]) == "YES"   # Length 5

    # Intersection length is 1, which is not prime
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

# Generated at 2026-10-25 01:18:30.332271
# Unit test for function intersection
def test_intersection():
    # Prime intersection lengths
    assert module_0.intersection((1, 5), (2, 5)) == "YES"   # Length 3
    assert module_0.intersection((0, 10), (3, 8)) == "YES"  # Length 5
    assert module_0.intersection((0, 2), (0, 2)) == "YES"   # Length 2

    # Non-prime intersection lengths
    assert module_0.intersection((1, 7), (3, 10)) == "NO"   # Length 4
    assert module_0.intersection((0, 5), (4, 8)) == "NO"    # Length 1

    # No positive-length intersection
    assert module_0.intersection((1, 2), (2, 3)) == "NO"    # Touching endpoints
    assert module_0.intersection((1, 2), (3, 4)) == "NO"    # Disjoint intervals

# Generated at 2026-10-25 01:18:37.297275
# Unit test for function intersection
def test_intersection():
    # Overlap length is 2 (prime)
    assert module_0.intersection([1, 7], [5, 9]) == "YES"

    # Overlap length is 4 (not prime)
    assert module_0.intersection([1, 8], [3, 7]) == "NO"

    # One interval contained in another; length is 3 (prime)
    assert module_0.intersection([-5, 10], [-2, 1]) == "YES"

    # Identical intervals; length is 5 (prime)
    assert module_0.intersection([0, 5], [0, 5]) == "YES"

    # Intervals touch but do not overlap
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Disjoint intervals
    assert module_0.intersection([1, 2], [3, 4]) == "NO"

    # Overlap length is 1, which is not prime
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

# Generated at 2026-10-25 01:18:44.566255
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection((1, 8), (3, 10)) == "YES"   # overlap length: 5
    assert module_0.intersection((1, 11), (5, 15)) == "NO"   # overlap length: 6
    assert module_0.intersection((1, 5), (3, 5)) == "YES"    # overlap length: 2
    assert module_0.intersection((1, 5), (4, 8)) == "NO"     # overlap length: 1
    assert module_0.intersection((1, 5), (5, 10)) == "NO"    # intervals only touch
    assert module_0.intersection((1, 3), (5, 8)) == "NO"     # no intersection
    assert module_0.intersection((2, 9), (2, 9)) == "YES"    # overlap length: 7

test_intersection()

# Generated at 2026-10-25 01:18:51.529735
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection([1, 7], [4, 10]) == "YES"   # length 3
    assert module_0.intersection([0, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([2, 4], [2, 4]) == "YES"    # length 2

    # Overlap length is not prime
    assert module_0.intersection([1, 8], [3, 7]) == "NO"     # length 4
    assert module_0.intersection([1, 5], [2, 3]) == "NO"     # length 1

    # Intervals only touch
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # Intervals do not overlap
    assert module_0.intersection([1, 2], [3, 4]) == "NO"

    # Negative interval boundaries
    assert module_0.intersection([-10, 0], [-7, -2]) == "YES"  # length 5

# Generated at 2026-10-25 01:18:54.054412
# Unit test for function intersection

# Generated at 2026-10-25 01:18:56.471952
# Unit test for function intersection

# Generated at 2026-10-25 01:18:58.894522
# Unit test for function intersection

# Generated at 2026-10-25 01:19:01.308522
# Unit test for function intersection

# Generated at 2026-10-25 01:19:03.722794
# Unit test for function intersection

# Generated at 2026-10-25 01:19:06.139520
# Unit test for function intersection

# Generated at 2026-10-25 01:19:08.559253
# Unit test for function intersection

# Generated at 2026-10-25 01:19:10.974710
# Unit test for function intersection

# Generated at 2026-10-25 01:19:13.387789
# Unit test for function intersection

# Generated at 2026-10-25 01:19:15.804954
# Unit test for function intersection

# Generated at 2026-10-25 01:19:17.276220
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 7)) == "YES"

# Generated at 2026-10-25 01:19:29.827735
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection((1, 5), (3, 7)) == "YES"   # length 2
    assert module_0.intersection((1, 6), (3, 8)) == "YES"   # length 3
    assert module_0.intersection((1, 10), (3, 8)) == "YES"  # length 5

    # Overlap length is not prime
    assert module_0.intersection((1, 7), (3, 9)) == "NO"    # length 4
    assert module_0.intersection((1, 9), (3, 9)) == "NO"    # length 6

    # No overlap or intervals only touch
    assert module_0.intersection((1, 3), (4, 6)) == "NO"
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # Identical and contained intervals
    assert module_0.intersection((2, 4), (2, 4)) == "YES"   # length 2
    assert module_0.intersection((1, 10), (4, 6)) == "YES"  # length 2


if __name__ == "__main__":
    test_intersection()
    print("All tests passed.")

# Generated at 2026-10-25 01:19:38.327150
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection([1, 7], [4, 10]) == "YES"   # length = 3
    assert module_0.intersection([0, 5], [2, 4]) == "YES"    # length = 2
    assert module_0.intersection([-5, 1], [-3, 0]) == "YES"  # length = 3

    # Overlap length is not prime
    assert module_0.intersection([1, 8], [3, 7]) == "NO"     # length = 4
    assert module_0.intersection([1, 2], [1, 2]) == "NO"     # length = 1

    # Intervals only touch
    assert module_0.intersection([1, 3], [3, 5]) == "NO"     # length = 0

    # No intersection
    assert module_0.intersection([1, 2], [4, 5]) == "NO"

    print("All tests passed.")


test_intersection()

# Generated at 2026-10-25 01:19:44.871001
# Unit test for function intersection
def test_intersection():
    # Overlap length is 3 (prime)
    assert module_0.intersection([1, 7], [4, 8]) == "YES"

    # Overlap length is 2 (prime)
    assert module_0.intersection([1, 4], [2, 6]) == "YES"

    # Overlap length is 4 (not prime)
    assert module_0.intersection([1, 8], [3, 7]) == "NO"

    # Intervals only touch; overlap length is 0
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No intersection
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # Identical intervals with prime length
    assert module_0.intersection([-2, 3], [-2, 3]) == "YES"

# Generated at 2026-10-25 01:19:51.536263
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection([1, 5], [3, 7]) == "YES"   # overlap length: 2
    assert module_0.intersection([1, 6], [3, 8]) == "YES"   # overlap length: 3
    assert module_0.intersection([1, 10], [3, 9]) == "NO"   # overlap length: 6
    assert module_0.intersection([1, 3], [2, 5]) == "NO"    # overlap length: 1
    assert module_0.intersection([1, 3], [3, 5]) == "NO"    # touching endpoints
    assert module_0.intersection([1, 2], [3, 4]) == "NO"    # no intersection
    assert module_0.intersection([2, 7], [2, 7]) == "YES"   # overlap length: 5

# Generated at 2026-10-25 01:19:57.781725
# Unit test for function intersection
def test_intersection():
    # Overlap length is prime
    assert module_0.intersection([1, 5], [3, 7]) == "YES"   # length 2
    assert module_0.intersection([0, 10], [4, 9]) == "YES"  # length 5

    # Overlap length is not prime
    assert module_0.intersection([1, 8], [3, 7]) == "NO"    # length 4
    assert module_0.intersection([1, 5], [4, 8]) == "NO"    # length 1

    # Intervals only touch
    assert module_0.intersection([1, 3], [3, 6]) == "NO"

    # No intersection
    assert module_0.intersection([1, 2], [4, 7]) == "NO"

    # Identical intervals
    assert module_0.intersection([2, 5], [2, 5]) == "YES"   # length 3

    # Negative endpoints
    assert module_0.intersection([-5, 1], [-3, 2]) == "NO"  # length 4