

# Generated at 2026-11-03 04:34:17.524772
# Unit test for function intersection
def test_intersection():
    # No overlap -> "NO"
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    # Touching intervals, length 0 -> "NO"
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Overlap length 1 (not prime) -> "NO"
    assert module_0.intersection((1, 3), (2, 5)) == "NO"
    # Overlap length 2 (prime) -> "YES"
    assert module_0.intersection((0, 3), (1, 4)) == "YES"
    # Overlap length 4 (not prime) -> "NO"
    assert module_0.intersection((0, 6), (2, 8)) == "NO"
    # Overlap length 3 (prime) -> "YES"
    assert module_0.intersection((5, 10), (7, 12)) == "YES"
    # One interval contained in another, length 3 (prime) -> "YES"
    assert module_0.intersection((1, 10), (3, 6)) == "YES"
    # Overlap length 5 (prime) -> "YES"
    assert module_0.intersection((0, 5), (1, 6)) == "YES"
    # Overlap length 6 (not prime) -> "NO"
    assert module_0.intersection((0, 8), (2, 10)) == "NO"
    # Negative intervals, overlap length 2 (prime) -> "YES"
    assert module_0.intersection((-2, 2), (0, 4)) == "YES"
    # Negative intervals, overlap length 1 (not prime) -> "NO"
    assert module_0.intersection((-3, -1), (-5, -2)) == "NO"
    # Identical intervals, length 3 (prime) -> "YES"
    assert module_0.intersection((2, 5), (2, 5)) == "YES"
    # Completely disjoint with gap -> "NO"
    assert module_0.intersection((10, 20), (25, 30)) == "NO"
    # Overlap length 7 (prime) -> "YES"
    assert module_0.intersection((0, 7), (0, 7)) == "YES"
    print("All tests passed!")

test_intersection()

# Generated at 2026-11-03 04:37:41.572590
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals with prime intersection length
    assert module_0.intersection((1, 5), (2, 8)) == "YES"       # length = 3 (prime)
    assert module_0.intersection((3, 9), (1, 6)) == "YES"       # length = 3 (prime)
    assert module_0.intersection((1, 10), (5, 15)) == "YES"     # length = 5 (prime)
    assert module_0.intersection((0, 15), (2, 15)) == "YES"     # length = 13 (prime)

    # Overlapping intervals with non-prime intersection length
    assert module_0.intersection((1, 10), (2, 12)) == "NO"      # length = 8 (not prime)
    assert module_0.intersection((1, 10), (2, 6)) == "NO"       # length = 4 (not prime)
    assert module_0.intersection((1, 12), (0, 14)) == "NO"      # length = 12 (not prime)

    # One interval fully contained in another
    assert module_0.intersection((1, 10), (3, 6)) == "YES"      # length = 3 (prime)
    assert module_0.intersection((0, 100), (10, 20)) == "NO"    # length = 10 (not prime)

    # Touching intervals (length = 0)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    assert module_0.intersection((5, 7), (7, 10)) == "NO"

    # Disjoint intervals
    assert module_0.intersection((1, 2), (3, 4)) == "NO"
    assert module_0.intersection((10, 20), (1, 5)) == "NO"

    # Identical intervals
    assert module_0.intersection((1, 2), (1, 2)) == "NO"        # length = 1 (not prime)
    assert module_0.intersection((2, 5), (2, 5)) == "YES"       # length = 3 (prime)

    # Negative intervals
    assert module_0.intersection((-4, 1), (-2, 5)) == "YES"     # length = 3 (prime)
    assert module_0.intersection((-10, -1), (-5, 0)) == "NO"    # length = 4 (not prime)

    print("All test cases passed!")

test_intersection()

# Generated at 2026-11-03 04:40:08.821241
# Unit test for function intersection
def test_intersection():
    # No overlap (touching endpoints)
    assert module_0.intersection((1, 2), (2, 3)) == "NO"
    # Overlap of length 1 (not prime)
    assert module_0.intersection((-1, 1), (0, 4)) == "NO"
    # Overlap of length 2 (prime)
    assert module_0.intersection((-3, -1), (-5, 5)) == "YES"
    # Overlap of length 2 (prime)
    assert module_0.intersection((0, 4), (2, 6)) == "YES"
    # Touching at a point, length 0
    assert module_0.intersection((0, 2), (2, 4)) == "NO"
    # Overlap of length 3 (prime)
    assert module_0.intersection((0, 10), (2, 5)) == "YES"
    # Overlap of length 4 (not prime)
    assert module_0.intersection((0, 10), (4, 8)) == "NO"
    # Overlap of length 3 (prime)
    assert module_0.intersection((1, 5), (2, 6)) == "YES"
    # No overlap at all
    assert module_0.intersection((1, 5), (6, 9)) == "NO"
    # Identical intervals, length 8 (not prime)
    assert module_0.intersection((0, 8), (0, 8)) == "NO"
    # One interval contained in the other, length 3 (prime)
    assert module_0.intersection((0, 5), (1, 4)) == "YES"
    # Negative intervals, length 6 (not prime)
    assert module_0.intersection((-10, -1), (-5, -2)) == "NO"
    # Overlap of length 5 (prime)
    assert module_0.intersection((0, 7), (2, 9)) == "YES"
    # Overlap of length 9 (not prime)
    assert module_0.intersection((0, 12), (3, 10)) == "NO"

    print("All tests passed!")


if __name__ == "__main__":
    test_intersection()