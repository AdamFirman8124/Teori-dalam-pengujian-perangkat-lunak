

# Generated at 2026-10-24 14:26:36.557300
# Unit test for function intersection

# Generated at 2026-10-24 14:26:57.206816
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length
    assert module_0.intersection([1, 5], [3, 8]) == "YES"      # length 2, prime
    # Overlapping intervals with non-prime intersection length
    assert module_0.intersection([1, 5], [2, 8]) == "NO"       # length 3... wait, 5-2=3 is prime
    assert module_0.intersection([1, 10], [2, 11]) == "NO"     # length 8, not prime
    # Touching intervals (empty intersection)
    assert module_0.intersection([1, 5], [5, 10]) == "NO"      # length 0
    # Disjoint intervals
    assert module_0.intersection([1, 3], [5, 10]) == "NO"      # length negative
    # Intersection length 1 (not prime by this function's rule)
    assert module_0.intersection([1, 4], [3, 6]) == "NO"       # length 1
    # Intersection length 4 (not prime)
    assert module_0.intersection([0, 10], [3, 7]) == "NO"      # length 4
    # Intersection length 5 (prime)
    assert module_0.intersection([0, 10], [3, 12]) == "YES"    # length 7

# Generated at 2026-10-24 14:26:59.721598
# Unit test for function intersection

# Generated at 2026-10-24 14:27:02.232939
# Unit test for function intersection

# Generated at 2026-10-24 14:27:04.644481
# Unit test for function intersection

# Generated at 2026-10-24 14:27:07.056898
# Unit test for function intersection

# Generated at 2026-10-24 14:27:09.469935
# Unit test for function intersection

# Generated at 2026-10-24 14:27:12.120529
# Unit test for function intersection

# Generated at 2026-10-24 14:27:14.620218
# Unit test for function intersection

# Generated at 2026-10-24 14:27:17.034044
# Unit test for function intersection

# Generated at 2026-10-24 14:27:19.448043
# Unit test for function intersection

# Generated at 2026-10-24 14:27:21.860604
# Unit test for function intersection

# Generated at 2026-10-24 14:27:24.273784
# Unit test for function intersection

# Generated at 2026-10-24 14:27:26.688395
# Unit test for function intersection

# Generated at 2026-10-24 14:27:29.101220
# Unit test for function intersection

# Generated at 2026-10-24 14:27:31.514001
# Unit test for function intersection

# Generated at 2026-10-24 14:27:33.926858
# Unit test for function intersection

# Generated at 2026-10-24 14:27:36.344141
# Unit test for function intersection

# Generated at 2026-10-24 14:27:38.752870
# Unit test for function intersection

# Generated at 2026-10-24 14:27:41.169668
# Unit test for function intersection

# Generated at 2026-10-24 14:27:43.586411
# Unit test for function intersection

# Generated at 2026-10-24 14:27:45.996980
# Unit test for function intersection

# Generated at 2026-10-24 14:27:51.772376
# Unit test for function intersection
def test_intersection():
    assert module_0.intersection([1, 5], [3, 7]) == "YES"    # overlap [3,5], length 2, prime
    assert module_0.intersection([1, 10], [2, 5]) == "YES"   # overlap [2,5], length 3, prime
    assert module_0.intersection([1, 10], [2, 6]) == "NO"    # overlap [2,6], length 4, not prime
    assert module_0.intersection([1, 3], [3, 5]) == "NO"     # touch at 3, length 0, not prime
    assert module_0.intersection([1, 2], [1, 2]) == "NO"     # length 1, is_prime(1) is False
    assert module_0.intersection([1, 3], [4, 6]) == "NO"     # disjoint, negative length

# Generated at 2026-10-24 14:28:07.965147
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:28:09.400127
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:28:10.946699
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:28:12.327027
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:28:13.689145
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:28:15.275095
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:28:16.627419
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:28:19.045000
# Unit test for function intersection

# Generated at 2026-10-24 14:28:21.456344
# Unit test for function intersection

# Generated at 2026-10-24 14:28:23.869493
# Unit test for function intersection

# Generated at 2026-10-24 14:28:26.283799
# Unit test for function intersection

# Generated at 2026-10-24 14:28:28.694646
# Unit test for function intersection

# Generated at 2026-10-24 14:28:31.107754
# Unit test for function intersection

# Generated at 2026-10-24 14:28:33.667957
# Unit test for function intersection

# Generated at 2026-10-24 14:28:36.080228
# Unit test for function intersection

# Generated at 2026-10-24 14:28:38.492094
# Unit test for function intersection

# Generated at 2026-10-24 14:28:40.905051
# Unit test for function intersection

# Generated at 2026-10-24 14:28:43.317046
# Unit test for function intersection

# Generated at 2026-10-24 14:28:45.729523
# Unit test for function intersection

# Generated at 2026-10-24 14:28:48.142044
# Unit test for function intersection

# Generated at 2026-10-24 14:28:50.554009
# Unit test for function intersection

# Generated at 2026-10-24 14:28:52.973896
# Unit test for function intersection

# Generated at 2026-10-24 14:28:55.389842
# Unit test for function intersection

# Generated at 2026-10-24 14:28:57.801238
# Unit test for function intersection

# Generated at 2026-10-24 14:29:00.214162
# Unit test for function intersection

# Generated at 2026-10-24 14:29:02.626507
# Unit test for function intersection

# Generated at 2026-10-24 14:29:05.038843
# Unit test for function intersection

# Generated at 2026-10-24 14:29:07.452172
# Unit test for function intersection

# Generated at 2026-10-24 14:29:09.864355
# Unit test for function intersection

# Generated at 2026-10-24 14:29:12.277040
# Unit test for function intersection

# Generated at 2026-10-24 14:29:14.689927
# Unit test for function intersection

# Generated at 2026-10-24 14:29:17.102416
# Unit test for function intersection

# Generated at 2026-10-24 14:29:19.515037
# Unit test for function intersection

# Generated at 2026-10-24 14:29:21.927920
# Unit test for function intersection

# Generated at 2026-10-24 14:29:24.341480
# Unit test for function intersection

# Generated at 2026-10-24 14:29:26.755017
# Unit test for function intersection

# Generated at 2026-10-24 14:29:29.167838
# Unit test for function intersection

# Generated at 2026-10-24 14:29:31.579683
# Unit test for function intersection

# Generated at 2026-10-24 14:29:33.992142
# Unit test for function intersection

# Generated at 2026-10-24 14:29:36.404927
# Unit test for function intersection

# Generated at 2026-10-24 14:29:38.821532
# Unit test for function intersection

# Generated at 2026-10-24 14:29:41.236784
# Unit test for function intersection

# Generated at 2026-10-24 14:29:43.650296
# Unit test for function intersection

# Generated at 2026-10-24 14:29:46.063312
# Unit test for function intersection

# Generated at 2026-10-24 14:29:48.475343
# Unit test for function intersection

# Generated at 2026-10-24 14:30:05.367665
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (2, 7)) == "YES"

# Generated at 2026-10-24 14:30:06.741151
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:30:08.175344
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:30:09.617741
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:30:11.053461
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:30:12.427907
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:30:13.780324
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:30:16.195322
# Unit test for function intersection

# Generated at 2026-10-24 14:30:18.608239
# Unit test for function intersection

# Generated at 2026-10-24 14:30:21.021948
# Unit test for function intersection

# Generated at 2026-10-24 14:30:23.632496
# Unit test for function intersection

# Generated at 2026-10-24 14:30:26.041150
# Unit test for function intersection

# Generated at 2026-10-24 14:30:28.453860
# Unit test for function intersection

# Generated at 2026-10-24 14:30:31.058000
# Unit test for function intersection

# Generated at 2026-10-24 14:30:33.474241
# Unit test for function intersection

# Generated at 2026-10-24 14:30:35.888031
# Unit test for function intersection

# Generated at 2026-10-24 14:30:38.300735
# Unit test for function intersection

# Generated at 2026-10-24 14:30:40.714639
# Unit test for function intersection

# Generated at 2026-10-24 14:30:43.127213
# Unit test for function intersection

# Generated at 2026-10-24 14:30:45.541200
# Unit test for function intersection

# Generated at 2026-10-24 14:30:47.953123
# Unit test for function intersection

# Generated at 2026-10-24 14:30:50.366365
# Unit test for function intersection

# Generated at 2026-10-24 14:30:52.780259
# Unit test for function intersection

# Generated at 2026-10-24 14:30:55.193689
# Unit test for function intersection

# Generated at 2026-10-24 14:30:57.605843
# Unit test for function intersection

# Generated at 2026-10-24 14:31:00.019405
# Unit test for function intersection

# Generated at 2026-10-24 14:31:02.437033
# Unit test for function intersection

# Generated at 2026-10-24 14:31:04.848725
# Unit test for function intersection

# Generated at 2026-10-24 14:31:07.260446
# Unit test for function intersection

# Generated at 2026-10-24 14:31:09.673780
# Unit test for function intersection

# Generated at 2026-10-24 14:31:35.206340
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (2, 6)) == "YES"

# Generated at 2026-10-24 14:31:36.557643
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:31:37.962826
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:31:40.465012
# Unit test for function intersection

# Generated at 2026-10-24 14:31:42.976868
# Unit test for function intersection

# Generated at 2026-10-24 14:31:45.391063
# Unit test for function intersection

# Generated at 2026-10-24 14:31:47.803072
# Unit test for function intersection

# Generated at 2026-10-24 14:31:50.379118
# Unit test for function intersection

# Generated at 2026-10-24 14:31:52.792187
# Unit test for function intersection

# Generated at 2026-10-24 14:31:55.205030
# Unit test for function intersection

# Generated at 2026-10-24 14:31:57.618073
# Unit test for function intersection

# Generated at 2026-10-24 14:32:00.030722
# Unit test for function intersection

# Generated at 2026-10-24 14:32:02.443628
# Unit test for function intersection

# Generated at 2026-10-24 14:32:04.890290
# Unit test for function intersection

# Generated at 2026-10-24 14:32:07.270067
# Unit test for function intersection

# Generated at 2026-10-24 14:32:09.683485
# Unit test for function intersection

# Generated at 2026-10-24 14:32:12.096114
# Unit test for function intersection

# Generated at 2026-10-24 14:32:14.509124
# Unit test for function intersection

# Generated at 2026-10-24 14:32:31.983660
# Unit test for function intersection
def test_intersection():
    # No overlap at all (length negative)
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Intervals touch at a single point (length 0)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Intersection length is 1 (1 is not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Intersection length is 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Intersection length is 3 (prime)
    assert module_0.intersection((10, 15), (12, 18)) == "YES"
    # Intersection length is 4 (not prime)
    assert module_0.intersection((0, 4), (0, 4)) == "NO"
    # Intersection length is 5 (prime)

# Generated at 2026-10-24 14:32:33.343352
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:32:34.741515
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:32:36.134802
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:32:37.503766
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:32:38.865507
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:32:40.222425
# Unit test for function intersection
def test_intersection():
    # no overlap -> NO
    assert module_0.intersection((1, 2), (3, 4)) == "NO"

    # touching at endpoint, length 0 -> NO
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # overlap length 1 is not prime -> NO
    assert module_0.intersection((1, 3), (2, 4)) == "NO"

    # overlap length 2 is prime -> YES
    assert module_0.intersection((1, 4), (2, 5)) == "YES"

    # overlap length 3 is prime -> YES
    assert module_0.intersection((0, 5), (1, 4)) == "YES"

    # overlap length 4 is not prime -> NO
    assert module_0.intersection((0, 5), (1, 5)) == "NO"

    # one interval inside the other, length 2 -> YES
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # overlap length 7 is prime -> YES
    assert module_0.intersection((1, 10), (2, 9)) == "YES"

    # overlap length 8 is not prime -> NO
    assert module_0.intersection((1, 10), (2, 10)) == "NO"

    # identical intervals, length 3 -> YES
    assert module_0.intersection((1, 4), (1, 4)) == "YES"

    # identical intervals, length 1 -> NO
    assert module_0.intersection((1, 2), (1, 2)) == "NO"

# Generated at 2026-10-24 14:32:42.737397
# Unit test for function intersection

# Generated at 2026-10-24 14:32:45.152455
# Unit test for function intersection

# Generated at 2026-10-24 14:32:47.565799
# Unit test for function intersection

# Generated at 2026-10-24 14:32:49.979577
# Unit test for function intersection

# Generated at 2026-10-24 14:32:52.572878
# Unit test for function intersection

# Generated at 2026-10-24 14:32:54.985098
# Unit test for function intersection

# Generated at 2026-10-24 14:32:57.397043
# Unit test for function intersection

# Generated at 2026-10-24 14:32:59.812415
# Unit test for function intersection

# Generated at 2026-10-24 14:33:02.229443
# Unit test for function intersection

# Generated at 2026-10-24 14:33:04.830915
# Unit test for function intersection

# Generated at 2026-10-24 14:33:07.243817
# Unit test for function intersection

# Generated at 2026-10-24 14:33:09.658193
# Unit test for function intersection

# Generated at 2026-10-24 14:33:12.274847
# Unit test for function intersection

# Generated at 2026-10-24 14:33:14.688608
# Unit test for function intersection

# Generated at 2026-10-24 14:33:17.102299
# Unit test for function intersection

# Generated at 2026-10-24 14:33:19.515381
# Unit test for function intersection

# Generated at 2026-10-24 14:33:21.927611
# Unit test for function intersection

# Generated at 2026-10-24 14:33:24.340547
# Unit test for function intersection

# Generated at 2026-10-24 14:33:26.753777
# Unit test for function intersection

# Generated at 2026-10-24 14:33:29.167075
# Unit test for function intersection

# Generated at 2026-10-24 14:33:31.580831
# Unit test for function intersection

# Generated at 2026-10-24 14:33:33.994180
# Unit test for function intersection

# Generated at 2026-10-24 14:33:36.407908
# Unit test for function intersection

# Generated at 2026-10-24 14:33:38.823156
# Unit test for function intersection

# Generated at 2026-10-24 14:33:41.239886
# Unit test for function intersection

# Generated at 2026-10-24 14:33:43.654148
# Unit test for function intersection

# Generated at 2026-10-24 14:33:46.072675
# Unit test for function intersection

# Generated at 2026-10-24 14:33:48.677195
# Unit test for function intersection

# Generated at 2026-10-24 14:33:51.094483
# Unit test for function intersection

# Generated at 2026-10-24 14:33:53.502351
# Unit test for function intersection

# Generated at 2026-10-24 14:33:55.914865
# Unit test for function intersection

# Generated at 2026-10-24 14:33:58.328325
# Unit test for function intersection

# Generated at 2026-10-24 14:34:00.741064
# Unit test for function intersection

# Generated at 2026-10-24 14:34:03.154195
# Unit test for function intersection

# Generated at 2026-10-24 14:34:05.567095
# Unit test for function intersection

# Generated at 2026-10-24 14:34:07.980186
# Unit test for function intersection

# Generated at 2026-10-24 14:34:10.393487
# Unit test for function intersection

# Generated at 2026-10-24 14:34:12.805825
# Unit test for function intersection

# Generated at 2026-10-24 14:34:15.223868
# Unit test for function intersection

# Generated at 2026-10-24 14:34:17.636454
# Unit test for function intersection

# Generated at 2026-10-24 14:34:20.049549
# Unit test for function intersection

# Generated at 2026-10-24 14:34:22.462949
# Unit test for function intersection

# Generated at 2026-10-24 14:34:24.875425
# Unit test for function intersection

# Generated at 2026-10-24 14:34:27.289909
# Unit test for function intersection

# Generated at 2026-10-24 14:34:29.702127
# Unit test for function intersection

# Generated at 2026-10-24 14:34:32.113743
# Unit test for function intersection

# Generated at 2026-10-24 14:34:34.527666
# Unit test for function intersection

# Generated at 2026-10-24 14:34:36.939440
# Unit test for function intersection

# Generated at 2026-10-24 14:34:39.351792
# Unit test for function intersection

# Generated at 2026-10-24 14:34:41.764325
# Unit test for function intersection

# Generated at 2026-10-24 14:34:44.176583
# Unit test for function intersection

# Generated at 2026-10-24 14:34:46.590230
# Unit test for function intersection

# Generated at 2026-10-24 14:34:49.003407
# Unit test for function intersection

# Generated at 2026-10-24 14:34:51.416357
# Unit test for function intersection

# Generated at 2026-10-24 14:34:53.830568
# Unit test for function intersection

# Generated at 2026-10-24 14:34:56.243057
# Unit test for function intersection

# Generated at 2026-10-24 14:34:58.656258
# Unit test for function intersection

# Generated at 2026-10-24 14:35:02.993320
# Unit test for function intersection

# Generated at 2026-10-24 14:35:05.405217
# Unit test for function intersection

# Generated at 2026-10-24 14:35:07.818337
# Unit test for function intersection

# Generated at 2026-10-24 14:35:10.231280
# Unit test for function intersection

# Generated at 2026-10-24 14:35:12.643979
# Unit test for function intersection

# Generated at 2026-10-24 14:35:15.058045
# Unit test for function intersection

# Generated at 2026-10-24 14:35:17.471047
# Unit test for function intersection

# Generated at 2026-10-24 14:35:19.883960
# Unit test for function intersection

# Generated at 2026-10-24 14:35:22.296860
# Unit test for function intersection

# Generated at 2026-10-24 14:35:24.710006
# Unit test for function intersection

# Generated at 2026-10-24 14:35:27.123282
# Unit test for function intersection

# Generated at 2026-10-24 14:35:29.536355
# Unit test for function intersection

# Generated at 2026-10-24 14:35:31.951942
# Unit test for function intersection

# Generated at 2026-10-24 14:35:34.366193
# Unit test for function intersection

# Generated at 2026-10-24 14:35:36.779236
# Unit test for function intersection

# Generated at 2026-10-24 14:35:39.219577
# Unit test for function intersection

# Generated at 2026-10-24 14:35:41.608104
# Unit test for function intersection

# Generated at 2026-10-24 14:35:44.020552
# Unit test for function intersection

# Generated at 2026-10-24 14:35:46.432229
# Unit test for function intersection

# Generated at 2026-10-24 14:35:48.846641
# Unit test for function intersection

# Generated at 2026-10-24 14:35:51.258777
# Unit test for function intersection

# Generated at 2026-10-24 14:35:53.672158
# Unit test for function intersection

# Generated at 2026-10-24 14:35:56.084604
# Unit test for function intersection

# Generated at 2026-10-24 14:35:58.503260
# Unit test for function intersection

# Generated at 2026-10-24 14:36:00.912016
# Unit test for function intersection

# Generated at 2026-10-24 14:36:03.325184
# Unit test for function intersection

# Generated at 2026-10-24 14:36:05.737744
# Unit test for function intersection

# Generated at 2026-10-24 14:36:08.150344
# Unit test for function intersection

# Generated at 2026-10-24 14:36:10.562585
# Unit test for function intersection

# Generated at 2026-10-24 14:36:12.976088
# Unit test for function intersection

# Generated at 2026-10-24 14:36:21.003068
# Unit test for function intersection

# Generated at 2026-10-24 14:36:23.416336
# Unit test for function intersection

# Generated at 2026-10-24 14:36:25.832249
# Unit test for function intersection

# Generated at 2026-10-24 14:36:28.244540
# Unit test for function intersection

# Generated at 2026-10-24 14:36:30.657594
# Unit test for function intersection

# Generated at 2026-10-24 14:36:33.069449
# Unit test for function intersection

# Generated at 2026-10-24 14:36:35.482877
# Unit test for function intersection

# Generated at 2026-10-24 14:36:37.897027
# Unit test for function intersection

# Generated at 2026-10-24 14:36:40.309582
# Unit test for function intersection