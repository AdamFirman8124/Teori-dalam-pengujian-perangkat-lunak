

# Generated at 2026-10-24 15:31:18.269938
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Version is abstract: it routes __eq__ through _cmp, which
    # subclasses must implement. Use a stub subclass to test the routing.
    class DummyVersion(Version):
        def __init__(self, cmp_result):
            self.cmp_result = cmp_result

        def _cmp(self, other):
            if isinstance(other, DummyVersion):
                return self.cmp_result
            return NotImplemented

    # _cmp == 0  ->  equal
    assert DummyVersion(0) == DummyVersion(0)

    # _cmp != 0  ->  not equal
    assert not (DummyVersion(1) == DummyVersion(-1))

    # _cmp returns NotImplemented -> __eq__ returns NotImplemented,
    # Python falls back to identity comparison
    a = DummyVersion(NotImplemented)
    assert a == a                      # same object -> True
    assert not (a == DummyVersion(0))  # different objects -> False

    # Comparing against an unsupported type (e.g. str) must not raise;
    # it falls through to False via NotImplemented
    assert not (DummyVersion(0) == "1.0")

    # The abstract base class itself has no _cmp: comparison raises
    try:
        Version() == Version()
    except AttributeError:
        pass
    else:
        raise AssertionError("Version() comparison should raise AttributeError")

# Generated at 2026-10-24 15:31:20.779960
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 15:31:23.196368
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 15:31:25.608872
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 15:31:28.024514
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:31:30.436482
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:31:32.850467
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:31:35.265180
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 15:31:37.676840
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 15:31:40.094257
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 15:31:42.513485
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-24 15:31:44.923192
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-24 15:31:47.336909
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-24 15:31:49.750276
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 15:31:52.163692
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 15:31:54.575919
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 15:31:56.988513
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 15:31:59.401729
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 15:32:01.813888
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 15:32:04.226576
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 15:32:06.639291
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 15:32:09.052592
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 15:32:11.465915
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 15:32:13.878313
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 15:32:16.295481
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 15:32:18.704289
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 15:32:21.117777
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 15:32:23.535235
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 15:32:25.951187
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:32:28.362495
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:32:30.774816
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:32:33.188731
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 15:32:35.602495
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 15:32:38.015202
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 15:32:40.461751
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 15:32:42.841137
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 15:32:45.254077
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 15:32:47.666133
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:32:50.078752
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:32:52.491722
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:32:54.905803
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:32:57.318463
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:32:59.731600
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:33:02.145593
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:33:04.559234
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:33:06.976136
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:33:09.388456
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 15:33:11.801176
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 15:33:14.216343
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 15:33:16.628487
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:33:19.046080
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:33:21.454516
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:33:23.866890
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:33:26.279426
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:33:28.692653
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 15:33:31.105529
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 15:33:33.518552
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 15:33:55.174435
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 15:34:09.514960
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    # valid string -> (expected .version, expected .prerelease)
    valid = {
        "0.4":     ((0, 4, 0), None),
        "0.4.0":   ((0, 4, 0), None),  # equivalent to 0.4
        "0.4.1":   ((0, 4, 1), None),
        "0.5a1":   ((0, 5, 0), ("a", 1)),
        "0.5b3":   ((0, 5, 0), ("b", 3)),
        "0.5":     ((0, 5, 0), None),
        "0.9.6":   ((0, 9, 6), None),
        "1.0":     ((1, 0, 0), None),
        "1.0.4a3": ((1, 0, 4), ("a", 3)),
        "1.0.4b1": ((1, 0, 4), ("b", 1)),
        "1.0.4":   ((1, 0, 4), None),
        "1.2.3":   ((1, 2, 3), None),
        "1.0a0":   ((1, 0, 0), ("a", 0)),
        "10.20.30b10": ((10, 20, 30), ("b", 10)),
    }


# Generated at 2026-10-24 15:34:14.758371
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 15:34:46.288004
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 15:35:33.875955
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 15:36:13.544412
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class FakeVersion(Version):
        def parse(self, vstring=None):
            self.vstring = vstring
        def _cmp(self, other):
            self.last_other = other
            return self.cmp_result
    greater = FakeVersion()
    greater.cmp_result = 1
    lesser = FakeVersion()
    lesser.cmp_result = -1
    equal = FakeVersion()
    equal.cmp_result = 0
    assert greater.__gt__(lesser) is True

# Generated at 2026-10-24 15:36:59.521783
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 15:37:38.647715
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 15:37:47.137633
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:37:48.554929
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:37:49.947392
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:39:10.801049
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 15:39:55.240838
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 15:40:42.939202
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 15:40:45.351002
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:40:47.055866
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 15:40:49.718381
# Unit test for method __le__ of class Version