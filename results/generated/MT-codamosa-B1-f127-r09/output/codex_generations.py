

# Generated at 2026-10-24 10:57:44.850313
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:57:47.518478
# Unit test for function intersection

# Generated at 2026-10-24 10:57:50.055831
# Unit test for function intersection

# Generated at 2026-10-24 10:57:52.474342
# Unit test for function intersection

# Generated at 2026-10-24 10:57:54.895683
# Unit test for function intersection

# Generated at 2026-10-24 10:58:11.397761
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length (2)
    assert module_0.intersection([1, 3], [2, 4]) == "YES"
    # Overlapping intervals with non-prime intersection length (4)
    assert module_0.intersection([1, 6], [3, 8]) == "NO"
    # Touching intervals -> length 0 -> NO
    assert module_0.intersection([1, 2], [2, 3]) == "NO"
    # Disjoint intervals -> negative length -> NO
    assert module_0.intersection([5, 7], [1, 3]) == "NO"
    # One interval fully inside another, prime length (3)
    assert module_0.intersection([1, 10], [3, 6]) == "YES"
    # Intersection length 1 (not prime by this implementation)
    assert module_0.intersection([1, 4], [3, 5]) == "NO"
    # Identical intervals, prime length (5)
    assert module_0.intersection([0, 5], [0, 5]) == "YES"
    # Identical intervals, non-prime length (6)
    assert module_0.intersection([0, 6], [0, 6]) == "NO"

# Generated at 2026-10-24 10:58:12.726895
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:14.030711
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:15.357147
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:16.667527
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:18.021831
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:19.350318
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:21.121626
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:22.637403
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:23.943969
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:25.330473
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:58:27.847178
# Unit test for function intersection

# Generated at 2026-10-24 10:58:30.374923
# Unit test for function intersection

# Generated at 2026-10-24 10:58:32.885367
# Unit test for function intersection

# Generated at 2026-10-24 10:58:35.408003
# Unit test for function intersection

# Generated at 2026-10-24 10:58:37.827460
# Unit test for function intersection

# Generated at 2026-10-24 10:58:40.244191
# Unit test for function intersection

# Generated at 2026-10-24 10:58:42.658577
# Unit test for function intersection

# Generated at 2026-10-24 10:58:45.075677
# Unit test for function intersection

# Generated at 2026-10-24 10:58:47.494448
# Unit test for function intersection

# Generated at 2026-10-24 10:58:49.910603
# Unit test for function intersection

# Generated at 2026-10-24 10:58:52.331200
# Unit test for function intersection

# Generated at 2026-10-24 10:58:54.748603
# Unit test for function intersection

# Generated at 2026-10-24 10:58:57.171822
# Unit test for function intersection

# Generated at 2026-10-24 10:58:59.603154
# Unit test for function intersection

# Generated at 2026-10-24 10:59:02.193864
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length (2)
    assert module_0.intersection([1, 3], [2, 4]) == "YES"
    # Overlapping intervals with non-prime intersection length (4)
    assert module_0.intersection([1, 6], [3, 8]) == "NO"
    # Touching intervals -> length 0 -> NO
    assert module_0.intersection([1, 2], [2, 3]) == "NO"
    # Disjoint intervals -> negative length -> NO
    assert module_0.intersection([5, 7], [1, 3]) == "NO"
    # One interval fully inside another, prime length (3)
    assert module_0.intersection([1, 10], [3, 6]) == "YES"
    # Intersection length 1 (not prime by this implementation)
    assert module_0.intersection([1, 4], [3, 5]) == "NO"
    # Identical intervals, prime length (5)
    assert module_0.intersection([0, 5], [0, 5]) == "YES"
    # Identical intervals, non-prime length (6)
    assert module_0.intersection([0, 6], [0, 6]) == "NO"

# Generated at 2026-10-24 10:59:03.510286
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:04.849267
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:06.168686
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:07.482357
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:08.793601
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:10.149164
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:11.471847
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:12.915790
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:14.222130
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:15.535414
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:16.849986
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:18.182129
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:19.515938
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:20.833998
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:22.141293
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:23.476747
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:24.792368
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:26.141334
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:27.866551
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:29.189933
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:30.505449
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:31.885076
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 10:59:34.452212
# Unit test for function intersection

# Generated at 2026-10-24 10:59:36.969078
# Unit test for function intersection

# Generated at 2026-10-24 10:59:39.475294
# Unit test for function intersection

# Generated at 2026-10-24 10:59:42.002265
# Unit test for function intersection

# Generated at 2026-10-24 10:59:44.546868
# Unit test for function intersection

# Generated at 2026-10-24 10:59:46.961587
# Unit test for function intersection

# Generated at 2026-10-24 10:59:49.376514
# Unit test for function intersection

# Generated at 2026-10-24 10:59:51.796100
# Unit test for function intersection

# Generated at 2026-10-24 10:59:54.211050
# Unit test for function intersection

# Generated at 2026-10-24 10:59:56.630256
# Unit test for function intersection

# Generated at 2026-10-24 10:59:59.060343
# Unit test for function intersection

# Generated at 2026-10-24 11:00:01.481762
# Unit test for function intersection

# Generated at 2026-10-24 11:00:03.896780
# Unit test for function intersection

# Generated at 2026-10-24 11:00:06.316518
# Unit test for function intersection

# Generated at 2026-10-24 11:00:08.735936
# Unit test for function intersection

# Generated at 2026-10-24 11:00:11.263316
# Unit test for function intersection

# Generated at 2026-10-24 11:00:13.684286
# Unit test for function intersection

# Generated at 2026-10-24 11:00:16.102167
# Unit test for function intersection

# Generated at 2026-10-24 11:00:18.522232
# Unit test for function intersection

# Generated at 2026-10-24 11:00:25.134113
# Unit test for function intersection
def test_intersection():
    # No overlap: intervals are disjoint
    assert module_0.intersection((1, 3), (5, 7)) == "NO"

    # Touching endpoints: intersection length is 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # Overlap length 4 (not prime)
    assert module_0.intersection((1, 5), (2, 8)) == "NO"

    # Overlap length 2 (prime)
    assert module_0.intersection((0, 10), (4, 6)) == "YES"

    # Overlap length 3 (prime)
    assert module_0.intersection((1, 5), (2, 7)) == "YES"

    # Negative interval endpoints, overlap length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # Negative endpoints, overlap length 1 (not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # One interval fully inside the other, overlap length 5 (prime)
    assert module_0.intersection((0, 10), (2, 7)) == "YES"

# Generated at 2026-10-24 11:00:26.460588
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:27.781985
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:29.100832
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:30.432574
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:31.750366
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:33.198278
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:34.835792
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:36.153596
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:39.033886
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:40.592040
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:41.913828
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:43.227302
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:44.537025
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:45.861501
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:47.225338
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:48.557346
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:49.867912
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:51.321997
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:55.828270
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:57.149778
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:58.470200
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:00:59.829338
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:02.335946
# Unit test for function intersection

# Generated at 2026-10-24 11:01:04.846663
# Unit test for function intersection

# Generated at 2026-10-24 11:01:07.263802
# Unit test for function intersection

# Generated at 2026-10-24 11:01:09.681480
# Unit test for function intersection

# Generated at 2026-10-24 11:01:12.101586
# Unit test for function intersection

# Generated at 2026-10-24 11:01:14.520047
# Unit test for function intersection

# Generated at 2026-10-24 11:01:17.073866
# Unit test for function intersection

# Generated at 2026-10-24 11:01:19.582220
# Unit test for function intersection

# Generated at 2026-10-24 11:01:21.299980
# Unit test for function intersection
def test_intersection():
    # No overlap: intervals are disjoint
    assert module_0.intersection((1, 3), (5, 7)) == "NO"

    # Touching endpoints: intersection length is 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # Overlap length 4 (not prime)
    assert module_0.intersection((1, 5), (2, 8)) == "NO"

    # Overlap length 2 (prime)
    assert module_0.intersection((0, 10), (4, 6)) == "YES"

    # Overlap length 3 (prime)
    assert module_0.intersection((1, 5), (2, 7)) == "YES"

    # Negative interval endpoints, overlap length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # Negative endpoints, overlap length 1 (not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # One interval fully inside the other, overlap length 5 (prime)
    assert module_0.intersection((0, 10), (2, 7)) == "YES"

# Generated at 2026-10-24 11:01:22.627040
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:24.089887
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:25.399365
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:33.361147
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:34.673463
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:36.069728
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:37.503569
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:38.830690
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:40.245186
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:41.756210
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:43.066320
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:44.466582
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:01:45.900989
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:02:06.809718
# Unit test for function intersection

# Generated at 2026-10-24 11:02:09.228824
# Unit test for function intersection

# Generated at 2026-10-24 11:02:11.651719
# Unit test for function intersection

# Generated at 2026-10-24 11:02:14.070853
# Unit test for function intersection

# Generated at 2026-10-24 11:02:16.488498
# Unit test for function intersection

# Generated at 2026-10-24 11:02:18.909012
# Unit test for function intersection

# Generated at 2026-10-24 11:02:21.327116
# Unit test for function intersection

# Generated at 2026-10-24 11:02:23.742414
# Unit test for function intersection

# Generated at 2026-10-24 11:02:26.403435
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length (2)
    assert module_0.intersection([1, 3], [2, 4]) == "YES"
    # Overlapping intervals with non-prime intersection length (4)
    assert module_0.intersection([1, 6], [3, 8]) == "NO"
    # Touching intervals -> length 0 -> NO
    assert module_0.intersection([1, 2], [2, 3]) == "NO"
    # Disjoint intervals -> negative length -> NO
    assert module_0.intersection([5, 7], [1, 3]) == "NO"
    # One interval fully inside another, prime length (3)
    assert module_0.intersection([1, 10], [3, 6]) == "YES"
    # Intersection length 1 (not prime by this implementation)
    assert module_0.intersection([1, 4], [3, 5]) == "NO"
    # Identical intervals, prime length (5)
    assert module_0.intersection([0, 5], [0, 5]) == "YES"
    # Identical intervals, non-prime length (6)
    assert module_0.intersection([0, 6], [0, 6]) == "NO"

# Generated at 2026-10-24 11:02:27.708837
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:02:29.016537
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:02:30.353178
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:02:31.683041
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:02:33.000736
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:02:34.309006
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:02:35.619946
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:19.115759
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:20.428121
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:21.738102
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:23.055021
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:24.372168
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:25.704170
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:27.016241
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:28.337132
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:29.668602
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:03:30.975323
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:05:10.705748
# Unit test for function intersection

# Generated at 2026-10-24 11:05:13.125874
# Unit test for function intersection

# Generated at 2026-10-24 11:05:15.722392
# Unit test for function intersection

# Generated at 2026-10-24 11:05:18.139677
# Unit test for function intersection

# Generated at 2026-10-24 11:05:20.555034
# Unit test for function intersection

# Generated at 2026-10-24 11:05:22.976981
# Unit test for function intersection

# Generated at 2026-10-24 11:05:25.405432
# Unit test for function intersection

# Generated at 2026-10-24 11:05:26.759199
# Unit test for function intersection
def test_intersection():
    # No overlap: intervals are disjoint
    assert module_0.intersection((1, 3), (5, 7)) == "NO"

    # Touching endpoints: intersection length is 0
    assert module_0.intersection((1, 2), (2, 3)) == "NO"

    # Overlap length 4 (not prime)
    assert module_0.intersection((1, 5), (2, 8)) == "NO"

    # Overlap length 2 (prime)
    assert module_0.intersection((0, 10), (4, 6)) == "YES"

    # Overlap length 3 (prime)
    assert module_0.intersection((1, 5), (2, 7)) == "YES"

    # Negative interval endpoints, overlap length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"

    # Negative endpoints, overlap length 1 (not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"

    # One interval fully inside the other, overlap length 5 (prime)
    assert module_0.intersection((0, 10), (2, 7)) == "YES"

# Generated at 2026-10-24 11:05:28.122791
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:05:29.453056
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:05:30.792505
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:05:32.147198
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:05:33.481186
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:05:34.792788
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()

# Generated at 2026-10-24 11:05:36.113465
# Unit test for function intersection
def test_intersection():
    # Prime overlap lengths -> YES
    assert module_0.intersection([0, 5], [3, 8]) == "YES"    # length 2
    assert module_0.intersection([0, 5], [2, 8]) == "YES"    # length 3
    assert module_0.intersection([1, 10], [3, 8]) == "YES"   # length 5
    assert module_0.intersection([0, 7], [0, 7]) == "YES"    # length 7
    assert module_0.intersection([-5, 0], [-3, 2]) == "YES"  # length 3

    # Non-prime overlap lengths -> NO
    assert module_0.intersection([0, 5], [4, 9]) == "NO"     # length 1
    assert module_0.intersection([0, 10], [0, 4]) == "NO"    # length 4
    assert module_0.intersection([0, 20], [0, 9]) == "NO"    # length 9

    # No overlap / touching -> NO
    assert module_0.intersection([0, 2], [5, 7]) == "NO"     # length -3
    assert module_0.intersection([0, 3], [3, 6]) == "NO"     # length 0

    print("All tests passed")

if __name__ == "__main__":
    test_intersection()