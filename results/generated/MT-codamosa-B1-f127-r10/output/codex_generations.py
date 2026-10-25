

# Generated at 2026-10-24 21:38:24.196038
# Unit test for function intersection

# Generated at 2026-10-24 21:38:26.609016
# Unit test for function intersection

# Generated at 2026-10-24 21:38:29.027258
# Unit test for function intersection

# Generated at 2026-10-24 21:38:31.444828
# Unit test for function intersection

# Generated at 2026-10-24 21:38:33.865544
# Unit test for function intersection

# Generated at 2026-10-24 21:38:36.281046
# Unit test for function intersection

# Generated at 2026-10-24 21:38:38.698186
# Unit test for function intersection

# Generated at 2026-10-24 21:38:41.118539
# Unit test for function intersection

# Generated at 2026-10-24 21:38:43.536287
# Unit test for function intersection

# Generated at 2026-10-24 21:38:45.953787
# Unit test for function intersection

# Generated at 2026-10-24 21:38:48.373315
# Unit test for function intersection

# Generated at 2026-10-24 21:38:50.788786
# Unit test for function intersection

# Generated at 2026-10-24 21:38:53.208467
# Unit test for function intersection

# Generated at 2026-10-24 21:38:55.623840
# Unit test for function intersection

# Generated at 2026-10-24 21:38:58.042282
# Unit test for function intersection

# Generated at 2026-10-24 21:39:00.461157
# Unit test for function intersection

# Generated at 2026-10-24 21:39:02.878826
# Unit test for function intersection

# Generated at 2026-10-24 21:39:05.297371
# Unit test for function intersection

# Generated at 2026-10-24 21:39:07.716498
# Unit test for function intersection

# Generated at 2026-10-24 21:39:12.738870
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 7)) == "YES"

# Generated at 2026-10-24 21:39:14.331986
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

# Generated at 2026-10-24 21:39:15.970885
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

# Generated at 2026-10-24 21:39:17.292437
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

# Generated at 2026-10-24 21:39:18.625291
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

# Generated at 2026-10-24 21:39:19.944598
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

# Generated at 2026-10-24 21:39:21.293019
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

# Generated at 2026-10-24 21:39:22.660628
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

# Generated at 2026-10-24 21:39:23.985955
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

# Generated at 2026-10-24 21:39:25.303387
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

# Generated at 2026-10-24 21:39:26.648835
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

# Generated at 2026-10-24 21:39:27.974719
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

# Generated at 2026-10-24 21:39:29.299969
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

# Generated at 2026-10-24 21:39:30.621458
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

# Generated at 2026-10-24 21:39:31.945707
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

# Generated at 2026-10-24 21:39:33.275278
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

# Generated at 2026-10-24 21:39:35.697941
# Unit test for function intersection

# Generated at 2026-10-24 21:39:38.119186
# Unit test for function intersection

# Generated at 2026-10-24 21:39:40.533735
# Unit test for function intersection

# Generated at 2026-10-24 21:39:42.951398
# Unit test for function intersection

# Generated at 2026-10-24 21:39:45.366537
# Unit test for function intersection

# Generated at 2026-10-24 21:39:47.784849
# Unit test for function intersection

# Generated at 2026-10-24 21:39:50.202848
# Unit test for function intersection

# Generated at 2026-10-24 21:39:52.620854
# Unit test for function intersection

# Generated at 2026-10-24 21:39:55.036348
# Unit test for function intersection

# Generated at 2026-10-24 21:39:57.455023
# Unit test for function intersection

# Generated at 2026-10-24 21:39:59.870794
# Unit test for function intersection

# Generated at 2026-10-24 21:40:02.291014
# Unit test for function intersection

# Generated at 2026-10-24 21:40:04.704556
# Unit test for function intersection

# Generated at 2026-10-24 21:40:07.120924
# Unit test for function intersection

# Generated at 2026-10-24 21:40:09.539316
# Unit test for function intersection

# Generated at 2026-10-24 21:40:10.916336
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

# Generated at 2026-10-24 21:40:12.302093
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

# Generated at 2026-10-24 21:40:13.622480
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

# Generated at 2026-10-24 21:40:14.938347
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

# Generated at 2026-10-24 21:40:16.277413
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

# Generated at 2026-10-24 21:40:17.589133
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

# Generated at 2026-10-24 21:40:18.909016
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

# Generated at 2026-10-24 21:40:20.230530
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

# Generated at 2026-10-24 21:40:21.544872
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

# Generated at 2026-10-24 21:40:22.897440
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

# Generated at 2026-10-24 21:40:24.212955
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

# Generated at 2026-10-24 21:40:25.536740
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

# Generated at 2026-10-24 21:40:26.874725
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

# Generated at 2026-10-24 21:40:28.214105
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

# Generated at 2026-10-24 21:40:29.552831
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

# Generated at 2026-10-24 21:40:30.877073
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

# Generated at 2026-10-24 21:40:32.201043
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

# Generated at 2026-10-24 21:40:34.722674
# Unit test for function intersection

# Generated at 2026-10-24 21:40:37.140530
# Unit test for function intersection

# Generated at 2026-10-24 21:40:39.557436
# Unit test for function intersection

# Generated at 2026-10-24 21:40:42.907412
# Unit test for function intersection

# Generated at 2026-10-24 21:40:45.326845
# Unit test for function intersection

# Generated at 2026-10-24 21:40:47.756022
# Unit test for function intersection

# Generated at 2026-10-24 21:40:50.189108
# Unit test for function intersection

# Generated at 2026-10-24 21:40:52.769866
# Unit test for function intersection

# Generated at 2026-10-24 21:40:55.196872
# Unit test for function intersection

# Generated at 2026-10-24 21:40:57.626862
# Unit test for function intersection

# Generated at 2026-10-24 21:41:00.041727
# Unit test for function intersection

# Generated at 2026-10-24 21:41:02.458161
# Unit test for function intersection

# Generated at 2026-10-24 21:41:04.875964
# Unit test for function intersection

# Generated at 2026-10-24 21:41:07.291280
# Unit test for function intersection

# Generated at 2026-10-24 21:41:09.708318
# Unit test for function intersection

# Generated at 2026-10-24 21:41:12.124782
# Unit test for function intersection

# Generated at 2026-10-24 21:41:14.541711
# Unit test for function intersection

# Generated at 2026-10-24 21:41:16.957883
# Unit test for function intersection

# Generated at 2026-10-24 21:41:19.376118
# Unit test for function intersection

# Generated at 2026-10-24 21:41:21.796178
# Unit test for function intersection

# Generated at 2026-10-24 21:41:24.214934
# Unit test for function intersection

# Generated at 2026-10-24 21:41:25.592146
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

# Generated at 2026-10-24 21:41:26.923766
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

# Generated at 2026-10-24 21:41:28.268873
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

# Generated at 2026-10-24 21:41:29.705843
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

# Generated at 2026-10-24 21:41:33.680458
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

# Generated at 2026-10-24 21:41:35.005831
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

# Generated at 2026-10-24 21:41:36.397888
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

# Generated at 2026-10-24 21:41:37.745403
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

# Generated at 2026-10-24 21:41:39.068848
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

# Generated at 2026-10-24 21:41:40.399382
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

# Generated at 2026-10-24 21:41:41.719824
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

# Generated at 2026-10-24 21:41:43.039968
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

# Generated at 2026-10-24 21:41:44.364549
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

# Generated at 2026-10-24 21:41:45.679354
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

# Generated at 2026-10-24 21:41:53.163951
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

# Generated at 2026-10-24 21:41:54.510763
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

# Generated at 2026-10-24 21:41:55.919419
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

# Generated at 2026-10-24 21:41:57.238585
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

# Generated at 2026-10-24 21:41:58.556575
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

# Generated at 2026-10-24 21:41:59.883615
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

# Generated at 2026-10-24 21:42:02.413370
# Unit test for function intersection

# Generated at 2026-10-24 21:42:04.955019
# Unit test for function intersection

# Generated at 2026-10-24 21:42:07.373870
# Unit test for function intersection

# Generated at 2026-10-24 21:42:09.791997
# Unit test for function intersection

# Generated at 2026-10-24 21:42:12.208859
# Unit test for function intersection

# Generated at 2026-10-24 21:42:14.626491
# Unit test for function intersection

# Generated at 2026-10-24 21:42:17.045093
# Unit test for function intersection

# Generated at 2026-10-24 21:42:19.462204
# Unit test for function intersection

# Generated at 2026-10-24 21:42:21.879100
# Unit test for function intersection

# Generated at 2026-10-24 21:42:24.299571
# Unit test for function intersection

# Generated at 2026-10-24 21:42:29.711808
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 7)) == "YES"

# Generated at 2026-10-24 21:42:36.389570
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

# Generated at 2026-10-24 21:42:37.713234
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

# Generated at 2026-10-24 21:42:39.029463
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

# Generated at 2026-10-24 21:42:40.771896
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

# Generated at 2026-10-24 21:42:42.206902
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

# Generated at 2026-10-24 21:42:43.526055
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

# Generated at 2026-10-24 21:42:44.841327
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

# Generated at 2026-10-24 21:42:46.160309
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

# Generated at 2026-10-24 21:42:47.479130
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

# Generated at 2026-10-24 21:42:48.816446
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

# Generated at 2026-10-24 21:43:01.282773
# Unit test for function intersection

# Generated at 2026-10-24 21:43:03.699598
# Unit test for function intersection

# Generated at 2026-10-24 21:43:06.267664
# Unit test for function intersection

# Generated at 2026-10-24 21:43:08.682926
# Unit test for function intersection

# Generated at 2026-10-24 21:43:11.100744
# Unit test for function intersection

# Generated at 2026-10-24 21:43:13.516069
# Unit test for function intersection

# Generated at 2026-10-24 21:43:15.934500
# Unit test for function intersection

# Generated at 2026-10-24 21:43:18.353667
# Unit test for function intersection

# Generated at 2026-10-24 21:43:20.769777
# Unit test for function intersection

# Generated at 2026-10-24 21:43:23.184844
# Unit test for function intersection

# Generated at 2026-10-24 21:43:25.604546
# Unit test for function intersection

# Generated at 2026-10-24 21:43:28.028483
# Unit test for function intersection

# Generated at 2026-10-24 21:43:30.443369
# Unit test for function intersection

# Generated at 2026-10-24 21:43:32.865126
# Unit test for function intersection

# Generated at 2026-10-24 21:43:35.282189
# Unit test for function intersection

# Generated at 2026-10-24 21:43:37.699224
# Unit test for function intersection

# Generated at 2026-10-24 21:43:40.115016
# Unit test for function intersection

# Generated at 2026-10-24 21:43:42.531965
# Unit test for function intersection

# Generated at 2026-10-24 21:43:44.949585
# Unit test for function intersection

# Generated at 2026-10-24 21:43:47.366208
# Unit test for function intersection

# Generated at 2026-10-24 21:43:49.783027
# Unit test for function intersection

# Generated at 2026-10-24 21:43:52.198613
# Unit test for function intersection

# Generated at 2026-10-24 21:43:54.616214
# Unit test for function intersection

# Generated at 2026-10-24 21:43:59.723710
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 7)) == "YES"

# Generated at 2026-10-24 21:44:01.075497
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

# Generated at 2026-10-24 21:44:02.413603
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

# Generated at 2026-10-24 21:44:26.873910
# Unit test for function intersection

# Generated at 2026-10-24 21:44:29.291945
# Unit test for function intersection

# Generated at 2026-10-24 21:44:31.715248
# Unit test for function intersection

# Generated at 2026-10-24 21:44:34.128179
# Unit test for function intersection

# Generated at 2026-10-24 21:44:36.545605
# Unit test for function intersection

# Generated at 2026-10-24 21:44:38.963802
# Unit test for function intersection

# Generated at 2026-10-24 21:44:41.382011
# Unit test for function intersection

# Generated at 2026-10-24 21:44:43.794826
# Unit test for function intersection

# Generated at 2026-10-24 21:44:46.212638
# Unit test for function intersection

# Generated at 2026-10-24 21:44:48.630438
# Unit test for function intersection

# Generated at 2026-10-24 21:44:51.044044
# Unit test for function intersection

# Generated at 2026-10-24 21:44:53.461018
# Unit test for function intersection

# Generated at 2026-10-24 21:44:55.879501
# Unit test for function intersection

# Generated at 2026-10-24 21:44:58.295556
# Unit test for function intersection

# Generated at 2026-10-24 21:45:03.312309
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 7)) == "YES"

# Generated at 2026-10-24 21:45:04.636772
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

# Generated at 2026-10-24 21:45:05.972185
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

# Generated at 2026-10-24 21:45:07.372230
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

# Generated at 2026-10-24 21:45:08.702173
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

# Generated at 2026-10-24 21:45:10.061094
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

# Generated at 2026-10-24 21:46:31.450280
# Unit test for function intersection

# Generated at 2026-10-24 21:46:33.867956
# Unit test for function intersection

# Generated at 2026-10-24 21:46:36.300851
# Unit test for function intersection

# Generated at 2026-10-24 21:46:38.718348
# Unit test for function intersection

# Generated at 2026-10-24 21:46:41.139141
# Unit test for function intersection

# Generated at 2026-10-24 21:46:43.553023
# Unit test for function intersection

# Generated at 2026-10-24 21:46:45.973102
# Unit test for function intersection

# Generated at 2026-10-24 21:46:48.394548
# Unit test for function intersection

# Generated at 2026-10-24 21:46:50.813395
# Unit test for function intersection

# Generated at 2026-10-24 21:46:53.382434
# Unit test for function intersection

# Generated at 2026-10-24 21:46:55.799314
# Unit test for function intersection

# Generated at 2026-10-24 21:46:58.214892
# Unit test for function intersection

# Generated at 2026-10-24 21:47:00.632623
# Unit test for function intersection

# Generated at 2026-10-24 21:47:10.595808
# Unit test for function intersection
def test_intersection():assert module_0.intersection((1, 5), (3, 10)) == "YES"

# Generated at 2026-10-24 21:47:11.910865
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

# Generated at 2026-10-24 21:47:13.362866
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

# Generated at 2026-10-24 21:47:14.679928
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

# Generated at 2026-10-24 21:47:16.010361
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

# Generated at 2026-10-24 21:47:17.329368
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