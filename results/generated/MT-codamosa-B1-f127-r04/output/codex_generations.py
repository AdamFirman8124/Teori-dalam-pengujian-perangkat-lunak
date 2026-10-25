

# Generated at 2026-10-24 21:06:17.412147
# Unit test for function intersection

# Generated at 2026-10-24 21:06:19.833807
# Unit test for function intersection

# Generated at 2026-10-24 21:06:22.252624
# Unit test for function intersection

# Generated at 2026-10-24 21:06:24.673546
# Unit test for function intersection

# Generated at 2026-10-24 21:06:29.984855
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 7)) == "YES"

# Generated at 2026-10-24 21:06:31.325485
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:32.692086
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:34.010422
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:35.335672
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:36.666119
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:37.987981
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:39.315102
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:40.737290
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:42.061178
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:43.474407
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:44.797038
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:46.121134
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:47.439387
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:48.768126
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:50.094858
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:51.428420
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:52.745548
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:54.076695
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:55.397497
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:06:57.923150
# Unit test for function intersection

# Generated at 2026-10-24 21:07:00.370290
# Unit test for function intersection

# Generated at 2026-10-24 21:07:02.870853
# Unit test for function intersection

# Generated at 2026-10-24 21:07:05.435944
# Unit test for function intersection

# Generated at 2026-10-24 21:07:07.852927
# Unit test for function intersection

# Generated at 2026-10-24 21:07:10.269296
# Unit test for function intersection

# Generated at 2026-10-24 21:07:12.698765
# Unit test for function intersection

# Generated at 2026-10-24 21:07:15.109752
# Unit test for function intersection

# Generated at 2026-10-24 21:07:17.527179
# Unit test for function intersection

# Generated at 2026-10-24 21:07:19.943877
# Unit test for function intersection

# Generated at 2026-10-24 21:07:22.362470
# Unit test for function intersection

# Generated at 2026-10-24 21:07:24.780802
# Unit test for function intersection

# Generated at 2026-10-24 21:07:27.195412
# Unit test for function intersection

# Generated at 2026-10-24 21:07:29.611592
# Unit test for function intersection

# Generated at 2026-10-24 21:07:32.029748
# Unit test for function intersection

# Generated at 2026-10-24 21:07:34.445782
# Unit test for function intersection

# Generated at 2026-10-24 21:07:36.862446
# Unit test for function intersection

# Generated at 2026-10-24 21:07:39.278430
# Unit test for function intersection

# Generated at 2026-10-24 21:07:41.694522
# Unit test for function intersection

# Generated at 2026-10-24 21:07:44.114911
# Unit test for function intersection

# Generated at 2026-10-24 21:07:51.670598
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 10)) == "YES"

# Generated at 2026-10-24 21:07:52.992295
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:07:54.326160
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:07:55.646928
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:07:56.982084
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:07:58.355757
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:07:59.675342
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:01.000836
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:02.335186
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:03.731716
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:05.098857
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:06.428666
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:07.776466
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:09.102829
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:10.428125
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:11.745169
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:13.065080
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:14.383667
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:16.076024
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:18.648501
# Unit test for function intersection

# Generated at 2026-10-24 21:08:21.069127
# Unit test for function intersection

# Generated at 2026-10-24 21:08:23.483246
# Unit test for function intersection

# Generated at 2026-10-24 21:08:25.904920
# Unit test for function intersection

# Generated at 2026-10-24 21:08:28.321710
# Unit test for function intersection

# Generated at 2026-10-24 21:08:30.739384
# Unit test for function intersection

# Generated at 2026-10-24 21:08:33.155512
# Unit test for function intersection

# Generated at 2026-10-24 21:08:35.571585
# Unit test for function intersection

# Generated at 2026-10-24 21:08:37.990379
# Unit test for function intersection

# Generated at 2026-10-24 21:08:39.625102
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:41.004672
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:42.338239
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:43.720385
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:45.044965
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:46.483716
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:48.255004
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:49.659127
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:50.987727
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:52.373240
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:53.685834
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:55.001655
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:56.321893
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:08:57.765294
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:09:00.282441
# Unit test for function intersection

# Generated at 2026-10-24 21:09:02.913992
# Unit test for function intersection

# Generated at 2026-10-24 21:09:05.436432
# Unit test for function intersection

# Generated at 2026-10-24 21:09:07.853843
# Unit test for function intersection

# Generated at 2026-10-24 21:09:10.270251
# Unit test for function intersection

# Generated at 2026-10-24 21:09:12.683457
# Unit test for function intersection

# Generated at 2026-10-24 21:09:16.916803
# Unit test for function intersection

# Generated at 2026-10-24 21:09:19.334840
# Unit test for function intersection

# Generated at 2026-10-24 21:09:21.754420
# Unit test for function intersection

# Generated at 2026-10-24 21:09:24.168773
# Unit test for function intersection

# Generated at 2026-10-24 21:09:26.583964
# Unit test for function intersection

# Generated at 2026-10-24 21:09:29.002570
# Unit test for function intersection

# Generated at 2026-10-24 21:09:31.417077
# Unit test for function intersection

# Generated at 2026-10-24 21:09:33.833811
# Unit test for function intersection

# Generated at 2026-10-24 21:09:36.252343
# Unit test for function intersection

# Generated at 2026-10-24 21:09:38.667472
# Unit test for function intersection

# Generated at 2026-10-24 21:09:41.086062
# Unit test for function intersection

# Generated at 2026-10-24 21:09:43.500381
# Unit test for function intersection

# Generated at 2026-10-24 21:09:45.916019
# Unit test for function intersection

# Generated at 2026-10-24 21:09:48.332503
# Unit test for function intersection

# Generated at 2026-10-24 21:09:50.751397
# Unit test for function intersection

# Generated at 2026-10-24 21:09:53.167384
# Unit test for function intersection

# Generated at 2026-10-24 21:09:55.585431
# Unit test for function intersection

# Generated at 2026-10-24 21:09:58.000756
# Unit test for function intersection

# Generated at 2026-10-24 21:10:00.419832
# Unit test for function intersection

# Generated at 2026-10-24 21:10:02.837703
# Unit test for function intersection

# Generated at 2026-10-24 21:10:05.254493
# Unit test for function intersection

# Generated at 2026-10-24 21:10:07.670236
# Unit test for function intersection

# Generated at 2026-10-24 21:10:10.089117
# Unit test for function intersection

# Generated at 2026-10-24 21:10:12.505272
# Unit test for function intersection

# Generated at 2026-10-24 21:10:14.921312
# Unit test for function intersection

# Generated at 2026-10-24 21:10:17.337453
# Unit test for function intersection

# Generated at 2026-10-24 21:10:24.846192
# Unit test for function intersection
def test_intersection():assert module_0.intersection([1, 5], [3, 7]) == "YES"

# Generated at 2026-10-24 21:10:26.168527
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:10:31.842903
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:10:33.157450
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:10:34.746506
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:10:36.124497
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:10:43.014980
# Unit test for function intersection
def test_intersection():assert module_0.intersection([1, 5], [3, 7]) == "YES"

# Generated at 2026-10-24 21:10:44.342495
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:10:45.663628
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:10:46.982356
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:10:48.310709
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:10:49.630880
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:11:01.224196
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:11:02.676886
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:11:04.002998
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:11:05.330147
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:11:07.747502
# Unit test for function intersection

# Generated at 2026-10-24 21:11:10.165265
# Unit test for function intersection

# Generated at 2026-10-24 21:11:12.583537
# Unit test for function intersection

# Generated at 2026-10-24 21:11:14.999408
# Unit test for function intersection

# Generated at 2026-10-24 21:11:17.420046
# Unit test for function intersection

# Generated at 2026-10-24 21:11:19.836515
# Unit test for function intersection

# Generated at 2026-10-24 21:11:22.254121
# Unit test for function intersection

# Generated at 2026-10-24 21:11:24.673133
# Unit test for function intersection

# Generated at 2026-10-24 21:11:27.089724
# Unit test for function intersection

# Generated at 2026-10-24 21:11:29.505043
# Unit test for function intersection

# Generated at 2026-10-24 21:11:31.921589
# Unit test for function intersection

# Generated at 2026-10-24 21:11:34.335638
# Unit test for function intersection

# Generated at 2026-10-24 21:11:36.755483
# Unit test for function intersection

# Generated at 2026-10-24 21:11:39.173291
# Unit test for function intersection

# Generated at 2026-10-24 21:11:41.589447
# Unit test for function intersection

# Generated at 2026-10-24 21:11:44.007687
# Unit test for function intersection

# Generated at 2026-10-24 21:11:49.985157
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 7)) == "YES"

# Generated at 2026-10-24 21:12:12.804646
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:12:14.123714
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:12:15.459488
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:12:16.793442
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:12:19.314030
# Unit test for function intersection

# Generated at 2026-10-24 21:12:21.839714
# Unit test for function intersection

# Generated at 2026-10-24 21:12:24.257228
# Unit test for function intersection

# Generated at 2026-10-24 21:12:26.677060
# Unit test for function intersection

# Generated at 2026-10-24 21:12:29.097694
# Unit test for function intersection

# Generated at 2026-10-24 21:12:31.512965
# Unit test for function intersection

# Generated at 2026-10-24 21:12:33.931297
# Unit test for function intersection

# Generated at 2026-10-24 21:12:36.500673
# Unit test for function intersection

# Generated at 2026-10-24 21:12:38.917113
# Unit test for function intersection

# Generated at 2026-10-24 21:12:41.331572
# Unit test for function intersection

# Generated at 2026-10-24 21:12:43.750028
# Unit test for function intersection

# Generated at 2026-10-24 21:12:46.163285
# Unit test for function intersection

# Generated at 2026-10-24 21:12:48.580339
# Unit test for function intersection

# Generated at 2026-10-24 21:12:50.996046
# Unit test for function intersection

# Generated at 2026-10-24 21:12:53.414461
# Unit test for function intersection

# Generated at 2026-10-24 21:12:55.831455
# Unit test for function intersection

# Generated at 2026-10-24 21:12:58.247329
# Unit test for function intersection

# Generated at 2026-10-24 21:13:00.667192
# Unit test for function intersection

# Generated at 2026-10-24 21:13:49.527675
# Unit test for function intersection

# Generated at 2026-10-24 21:13:51.943656
# Unit test for function intersection

# Generated at 2026-10-24 21:14:02.493111
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 4), (2, 6)) == "YES"

# Generated at 2026-10-24 21:14:03.872487
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:14:05.194089
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:14:06.521197
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:14:07.850211
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:14:10.380202
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:14:11.815230
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:14:13.129566
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:14:14.446739
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()

# Generated at 2026-10-24 21:14:15.790345
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length 2 (prime) -> YES
    assert module_0.intersection([1, 5], [3, 7]) == "YES"

    # Overlapping intervals, intersection length 4 (not prime) -> NO
    assert module_0.intersection([1, 6], [3, 8]) == "NO"

    # Touching intervals (length 0) -> NO
    assert module_0.intersection([1, 3], [3, 5]) == "NO"

    # No overlap (r < l, negative length) -> NO
    assert module_0.intersection([1, 2], [4, 6]) == "NO"

    # One interval contains the other, length 5 (prime) -> YES
    assert module_0.intersection([1, 8], [2, 5]) == "YES"

    # Intersection length 1 (not prime) -> NO
    assert module_0.intersection([1, 4], [3, 6]) == "NO"

    # Identical intervals, length 3 (prime) -> YES
    assert module_0.intersection([2, 5], [2, 5]) == "YES"

    # Negative coordinates, length 7 (prime) -> YES
    assert module_0.intersection([-10, -1], [-5, 3]) == "YES"

    # Intersection length 9 (not prime) -> NO
    assert module_0.intersection([0, 10], [1, 12]) == "NO"

    print("All tests passed!")


test_intersection()