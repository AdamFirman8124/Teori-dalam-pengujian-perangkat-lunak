

# Generated at 2026-10-25 09:28:29.419759
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

# Generated at 2026-10-25 09:28:30.877647
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

# Generated at 2026-10-25 09:28:32.181245
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

# Generated at 2026-10-25 09:28:33.595631
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

# Generated at 2026-10-25 09:28:48.490723
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

# Generated at 2026-10-25 09:28:49.898399
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

# Generated at 2026-10-25 09:28:51.331698
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

# Generated at 2026-10-25 09:28:52.865796
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

# Generated at 2026-10-25 09:28:54.324290
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

# Generated at 2026-10-25 09:28:55.755471
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

# Generated at 2026-10-25 09:28:57.220046
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

# Generated at 2026-10-25 09:28:59.934917
# Unit test for function intersection

# Generated at 2026-10-25 09:29:02.350308
# Unit test for function intersection

# Generated at 2026-10-25 09:29:09.762976
# Unit test for function intersection
def test_intersection():assert module_0.intersection([1, 5], [2, 7]) == "YES"

# Generated at 2026-10-25 09:29:12.749371
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

# Generated at 2026-10-25 09:29:14.165777
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

# Generated at 2026-10-25 09:29:15.601553
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

# Generated at 2026-10-25 09:29:17.138681
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

# Generated at 2026-10-25 09:29:18.671496
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

# Generated at 2026-10-25 09:29:20.111149
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

# Generated at 2026-10-25 09:29:21.647994
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

# Generated at 2026-10-25 09:29:23.178986
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

# Generated at 2026-10-25 09:29:24.562500
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

# Generated at 2026-10-25 09:29:27.557164
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

# Generated at 2026-10-25 09:29:30.100145
# Unit test for function intersection

# Generated at 2026-10-25 09:29:32.575384
# Unit test for function intersection

# Generated at 2026-10-25 09:29:34.982055
# Unit test for function intersection

# Generated at 2026-10-25 09:29:37.394771
# Unit test for function intersection

# Generated at 2026-10-25 09:29:39.808369
# Unit test for function intersection

# Generated at 2026-10-25 09:29:42.330199
# Unit test for function intersection

# Generated at 2026-10-25 09:29:44.746592
# Unit test for function intersection

# Generated at 2026-10-25 09:29:47.160379
# Unit test for function intersection

# Generated at 2026-10-25 09:29:49.573680
# Unit test for function intersection

# Generated at 2026-10-25 09:29:51.985956
# Unit test for function intersection

# Generated at 2026-10-25 09:29:54.401780
# Unit test for function intersection

# Generated at 2026-10-25 09:29:56.816493
# Unit test for function intersection

# Generated at 2026-10-25 09:29:59.230866
# Unit test for function intersection

# Generated at 2026-10-25 09:30:01.643693
# Unit test for function intersection

# Generated at 2026-10-25 09:30:04.059715
# Unit test for function intersection

# Generated at 2026-10-25 09:30:06.470291
# Unit test for function intersection

# Generated at 2026-10-25 09:30:08.889210
# Unit test for function intersection

# Generated at 2026-10-25 09:30:11.309977
# Unit test for function intersection

# Generated at 2026-10-25 09:30:13.719543
# Unit test for function intersection

# Generated at 2026-10-25 09:30:16.134964
# Unit test for function intersection

# Generated at 2026-10-25 09:30:18.554492
# Unit test for function intersection

# Generated at 2026-10-25 09:30:20.966985
# Unit test for function intersection

# Generated at 2026-10-25 09:30:23.382086
# Unit test for function intersection

# Generated at 2026-10-25 09:30:25.796778
# Unit test for function intersection

# Generated at 2026-10-25 09:30:28.214021
# Unit test for function intersection

# Generated at 2026-10-25 09:30:30.632116
# Unit test for function intersection

# Generated at 2026-10-25 09:30:35.862944
# Unit test for function intersection
def test_intersection():assert module_0.intersection([1, 5], [3, 7]) == "YES"

# Generated at 2026-10-25 09:30:38.338957
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

# Generated at 2026-10-25 09:30:39.875160
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

# Generated at 2026-10-25 09:30:54.477156
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

# Generated at 2026-10-25 09:30:57.346663
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

# Generated at 2026-10-25 09:31:09.062819
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

# Generated at 2026-10-25 09:31:10.726039
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

# Generated at 2026-10-25 09:31:12.238582
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

# Generated at 2026-10-25 09:31:13.811368
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

# Generated at 2026-10-25 09:31:15.203888
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

# Generated at 2026-10-25 09:31:18.076941
# Unit test for function intersection

# Generated at 2026-10-25 09:31:20.493104
# Unit test for function intersection

# Generated at 2026-10-25 09:31:23.184558
# Unit test for function intersection

# Generated at 2026-10-25 09:31:25.598698
# Unit test for function intersection

# Generated at 2026-10-25 09:31:28.012199
# Unit test for function intersection

# Generated at 2026-10-25 09:31:30.741554
# Unit test for function intersection

# Generated at 2026-10-25 09:31:33.156428
# Unit test for function intersection

# Generated at 2026-10-25 09:31:35.573474
# Unit test for function intersection

# Generated at 2026-10-25 09:31:37.987176
# Unit test for function intersection

# Generated at 2026-10-25 09:31:40.400918
# Unit test for function intersection

# Generated at 2026-10-25 09:31:42.814369
# Unit test for function intersection

# Generated at 2026-10-25 09:31:45.300513
# Unit test for function intersection

# Generated at 2026-10-25 09:31:47.714534
# Unit test for function intersection

# Generated at 2026-10-25 09:31:50.128291
# Unit test for function intersection

# Generated at 2026-10-25 09:31:52.738816
# Unit test for function intersection
def test_intersection():assert module_0.intersection([1, 5], [2, 7]) == "YES"

# Generated at 2026-10-25 09:31:54.106353
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

# Generated at 2026-10-25 09:31:55.506884
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

# Generated at 2026-10-25 09:31:56.900763
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

# Generated at 2026-10-25 09:31:58.280297
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

# Generated at 2026-10-25 09:32:00.361577
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

# Generated at 2026-10-25 09:32:01.782528
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

# Generated at 2026-10-25 09:32:03.214508
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

# Generated at 2026-10-25 09:32:04.622145
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

# Generated at 2026-10-25 09:32:05.999412
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

# Generated at 2026-10-25 09:32:08.745742
# Unit test for function intersection

# Generated at 2026-10-25 09:32:11.162418
# Unit test for function intersection

# Generated at 2026-10-25 09:32:13.577180
# Unit test for function intersection

# Generated at 2026-10-25 09:32:16.013938
# Unit test for function intersection

# Generated at 2026-10-25 09:32:18.428127
# Unit test for function intersection

# Generated at 2026-10-25 09:32:20.912246
# Unit test for function intersection

# Generated at 2026-10-25 09:32:23.269734
# Unit test for function intersection

# Generated at 2026-10-25 09:32:25.683268
# Unit test for function intersection

# Generated at 2026-10-25 09:32:28.097513
# Unit test for function intersection

# Generated at 2026-10-25 09:32:30.515123
# Unit test for function intersection

# Generated at 2026-10-25 09:32:32.926912
# Unit test for function intersection

# Generated at 2026-10-25 09:32:35.342080
# Unit test for function intersection

# Generated at 2026-10-25 09:32:37.755542
# Unit test for function intersection

# Generated at 2026-10-25 09:32:40.169864
# Unit test for function intersection

# Generated at 2026-10-25 09:32:42.780070
# Unit test for function intersection

# Generated at 2026-10-25 09:32:45.197686
# Unit test for function intersection

# Generated at 2026-10-25 09:32:47.610712
# Unit test for function intersection

# Generated at 2026-10-25 09:32:50.025981
# Unit test for function intersection

# Generated at 2026-10-25 09:32:52.440322
# Unit test for function intersection

# Generated at 2026-10-25 09:32:54.912911
# Unit test for function intersection

# Generated at 2026-10-25 09:32:57.301676
# Unit test for function intersection

# Generated at 2026-10-25 09:32:59.712654
# Unit test for function intersection

# Generated at 2026-10-25 09:33:02.127624
# Unit test for function intersection

# Generated at 2026-10-25 09:33:04.541416
# Unit test for function intersection

# Generated at 2026-10-25 09:33:06.957348
# Unit test for function intersection

# Generated at 2026-10-25 09:33:09.369908
# Unit test for function intersection

# Generated at 2026-10-25 09:33:11.848163
# Unit test for function intersection

# Generated at 2026-10-25 09:33:14.263651
# Unit test for function intersection

# Generated at 2026-10-25 09:33:16.676311
# Unit test for function intersection

# Generated at 2026-10-25 09:33:19.106114
# Unit test for function intersection

# Generated at 2026-10-25 09:33:21.525275
# Unit test for function intersection

# Generated at 2026-10-25 09:33:23.939652
# Unit test for function intersection

# Generated at 2026-10-25 09:33:26.355529
# Unit test for function intersection

# Generated at 2026-10-25 09:33:30.199024
# Unit test for function intersection

# Generated at 2026-10-25 09:33:32.646280
# Unit test for function intersection

# Generated at 2026-10-25 09:33:35.027993
# Unit test for function intersection

# Generated at 2026-10-25 09:33:37.442187
# Unit test for function intersection

# Generated at 2026-10-25 09:33:39.857557
# Unit test for function intersection

# Generated at 2026-10-25 09:33:42.270305
# Unit test for function intersection

# Generated at 2026-10-25 09:33:44.686776
# Unit test for function intersection

# Generated at 2026-10-25 09:33:47.100958
# Unit test for function intersection

# Generated at 2026-10-25 09:33:49.514116
# Unit test for function intersection

# Generated at 2026-10-25 09:33:51.930772
# Unit test for function intersection

# Generated at 2026-10-25 09:33:54.343431
# Unit test for function intersection

# Generated at 2026-10-25 09:33:56.760845
# Unit test for function intersection

# Generated at 2026-10-25 09:33:59.176023
# Unit test for function intersection

# Generated at 2026-10-25 09:34:01.593625
# Unit test for function intersection

# Generated at 2026-10-25 09:34:04.005196
# Unit test for function intersection

# Generated at 2026-10-25 09:34:06.418496
# Unit test for function intersection

# Generated at 2026-10-25 09:34:08.835186
# Unit test for function intersection

# Generated at 2026-10-25 09:34:11.327805
# Unit test for function intersection

# Generated at 2026-10-25 09:34:13.696983
# Unit test for function intersection

# Generated at 2026-10-25 09:34:16.115834
# Unit test for function intersection

# Generated at 2026-10-25 09:34:18.530794
# Unit test for function intersection

# Generated at 2026-10-25 09:34:20.942984
# Unit test for function intersection

# Generated at 2026-10-25 09:34:23.448611
# Unit test for function intersection

# Generated at 2026-10-25 09:34:25.861738
# Unit test for function intersection

# Generated at 2026-10-25 09:34:28.275883
# Unit test for function intersection

# Generated at 2026-10-25 09:34:30.690762
# Unit test for function intersection

# Generated at 2026-10-25 09:34:33.104779
# Unit test for function intersection

# Generated at 2026-10-25 09:34:35.566059
# Unit test for function intersection

# Generated at 2026-10-25 09:34:37.979265
# Unit test for function intersection

# Generated at 2026-10-25 09:34:40.393707
# Unit test for function intersection

# Generated at 2026-10-25 09:34:46.093441
# Unit test for function intersection

# Generated at 2026-10-25 09:34:48.508681
# Unit test for function intersection

# Generated at 2026-10-25 09:34:50.923974
# Unit test for function intersection

# Generated at 2026-10-25 09:34:53.337951
# Unit test for function intersection

# Generated at 2026-10-25 09:34:55.751267
# Unit test for function intersection

# Generated at 2026-10-25 09:34:58.164853
# Unit test for function intersection

# Generated at 2026-10-25 09:35:00.567611
# Unit test for function intersection

# Generated at 2026-10-25 09:35:02.981840
# Unit test for function intersection

# Generated at 2026-10-25 09:35:05.395817
# Unit test for function intersection

# Generated at 2026-10-25 09:35:07.809421
# Unit test for function intersection

# Generated at 2026-10-25 09:35:10.223746
# Unit test for function intersection

# Generated at 2026-10-25 09:35:12.637800
# Unit test for function intersection

# Generated at 2026-10-25 09:35:15.052689
# Unit test for function intersection

# Generated at 2026-10-25 09:35:17.468096
# Unit test for function intersection

# Generated at 2026-10-25 09:35:19.882722
# Unit test for function intersection

# Generated at 2026-10-25 09:35:22.297143
# Unit test for function intersection

# Generated at 2026-10-25 09:35:24.711810
# Unit test for function intersection

# Generated at 2026-10-25 09:35:27.177047
# Unit test for function intersection

# Generated at 2026-10-25 09:35:29.572365
# Unit test for function intersection

# Generated at 2026-10-25 09:35:31.998997
# Unit test for function intersection

# Generated at 2026-10-25 09:35:34.415195
# Unit test for function intersection

# Generated at 2026-10-25 09:35:36.829190
# Unit test for function intersection

# Generated at 2026-10-25 09:35:39.243419
# Unit test for function intersection

# Generated at 2026-10-25 09:35:41.657847
# Unit test for function intersection

# Generated at 2026-10-25 09:35:44.072931
# Unit test for function intersection

# Generated at 2026-10-25 09:35:46.484878
# Unit test for function intersection

# Generated at 2026-10-25 09:35:48.899484
# Unit test for function intersection

# Generated at 2026-10-25 09:35:51.316450
# Unit test for function intersection

# Generated at 2026-10-25 09:35:53.727182
# Unit test for function intersection

# Generated at 2026-10-25 09:35:56.140871
# Unit test for function intersection

# Generated at 2026-10-25 09:36:06.515466
# Unit test for function intersection

# Generated at 2026-10-25 09:36:08.929332
# Unit test for function intersection

# Generated at 2026-10-25 09:36:11.342898
# Unit test for function intersection

# Generated at 2026-10-25 09:36:13.756531
# Unit test for function intersection

# Generated at 2026-10-25 09:36:16.169968
# Unit test for function intersection

# Generated at 2026-10-25 09:36:18.585069
# Unit test for function intersection

# Generated at 2026-10-25 09:36:20.999390
# Unit test for function intersection

# Generated at 2026-10-25 09:36:23.414013
# Unit test for function intersection

# Generated at 2026-10-25 09:36:25.830022
# Unit test for function intersection

# Generated at 2026-10-25 09:36:28.244813
# Unit test for function intersection

# Generated at 2026-10-25 09:36:30.660752
# Unit test for function intersection

# Generated at 2026-10-25 09:36:33.074323
# Unit test for function intersection

# Generated at 2026-10-25 09:36:35.488607
# Unit test for function intersection

# Generated at 2026-10-25 09:36:37.902218
# Unit test for function intersection

# Generated at 2026-10-25 09:36:40.316399
# Unit test for function intersection

# Generated at 2026-10-25 09:36:42.784699
# Unit test for function intersection

# Generated at 2026-10-25 09:36:45.199355
# Unit test for function intersection

# Generated at 2026-10-25 09:36:47.613516
# Unit test for function intersection

# Generated at 2026-10-25 09:36:50.024504
# Unit test for function intersection

# Generated at 2026-10-25 09:36:52.438131
# Unit test for function intersection

# Generated at 2026-10-25 09:36:54.852239
# Unit test for function intersection

# Generated at 2026-10-25 09:36:57.268240
# Unit test for function intersection

# Generated at 2026-10-25 09:36:59.679906
# Unit test for function intersection

# Generated at 2026-10-25 09:37:02.094880
# Unit test for function intersection

# Generated at 2026-10-25 09:37:04.508599
# Unit test for function intersection

# Generated at 2026-10-25 09:37:06.932580
# Unit test for function intersection

# Generated at 2026-10-25 09:37:09.344198
# Unit test for function intersection

# Generated at 2026-10-25 09:37:11.756307
# Unit test for function intersection

# Generated at 2026-10-25 09:37:14.169970
# Unit test for function intersection

# Generated at 2026-10-25 09:37:16.583582
# Unit test for function intersection

# Generated at 2026-10-25 09:37:34.997255
# Unit test for function intersection

# Generated at 2026-10-25 09:37:37.411029
# Unit test for function intersection

# Generated at 2026-10-25 09:37:39.826131
# Unit test for function intersection

# Generated at 2026-10-25 09:37:48.785299
# Unit test for function intersection
def test_intersection():
    # Overlapping intervals, intersection length is prime (5) -> YES
    assert module_0.intersection((1, 5), (3, 10)) == "YES"          # length = 5 - 3 = 2? adjust below
    # Actual: l = max(1,3)=3, r = min(5,10)=5, length = 2 (prime) -> YES
    assert module_0.intersection((1, 5), (3, 10)) == "YES"

    # Overlapping intervals, intersection length is composite (4) -> NO
    assert module_0.intersection((1, 7), (3, 9)) == "NO"            # l=3, r=7, length=4

    # Overlapping intervals, intersection length is 1 (not prime) -> NO
    assert module_0.intersection((2, 4), (3, 6)) == "NO"            # l=3, r=4, length=1

    # Intervals touch at a single point, length = 0 -> NO
    assert module_0.intersection((1, 3), (3, 5)) == "NO"

    # Disjoint intervals, r < l, length negative -> NO
    assert module_0.intersection((1, 2), (5, 8)) == "NO"

    # Identical intervals, prime length (3) -> YES
    assert module_0.intersection((2, 5), (2, 5)) == "YES"           # l=2, r=5, length=3

    # Identical intervals, length 0 (single point) -> NO
    assert module_0.intersection((4, 4), (4, 4)) == "NO"

    # Negative intervals with prime intersection length (2) -> YES
    assert module_0.intersection((-5, -1), (-3, 2)) == "YES"        # l=-3, r=-1, length=2

    # Negative intervals with composite length (9) -> NO
    assert module_0.intersection((-10, 1), (-9, 3)) == "NO"         # l=-9, r=1, length=10? l=max(-10,-9)=-9, r=min(1,3)=1, length=10

    # Intersection length is prime 13 -> YES
    assert module_0.intersection((0, 20), (7, 10)) == "YES"         # l=7, r=10, length=3

    # One interval fully inside another, prime length (5) -> YES
    assert module_0.intersection((0, 10), (3, 8)) == "YES"          # l=3, r=8, length=5

    # One interval fully inside another, length 1 -> NO
    assert module_0.intersection((0, 10), (3, 4)) == "NO"           # l=3, r=4, length=1

    print("All tests passed!")

# Generated at 2026-10-25 09:37:50.248019
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

# Generated at 2026-10-25 09:37:51.820598
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

# Generated at 2026-10-25 09:37:53.351686
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

# Generated at 2026-10-25 09:37:54.873288
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

# Generated at 2026-10-25 09:37:56.232460
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

# Generated at 2026-10-25 09:37:57.637233
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

# Generated at 2026-10-25 09:37:59.173140
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

# Generated at 2026-10-25 09:38:01.711049
# Unit test for function intersection

# Generated at 2026-10-25 09:38:04.589888
# Unit test for function intersection

# Generated at 2026-10-25 09:38:07.005895
# Unit test for function intersection