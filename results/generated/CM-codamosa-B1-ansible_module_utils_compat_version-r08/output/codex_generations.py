

# Generated at 2026-10-25 01:37:54.712152
# Unit test for constructor of class Version

# Generated at 2026-10-25 01:37:56.145312
# Unit test for constructor of class Version

# Generated at 2026-10-25 01:37:57.529697
# Unit test for constructor of class Version

# Generated at 2026-10-25 01:38:05.761488
# Unit test for constructor of class StrictVersion
def test_StrictVersion():
    version = StrictVersion("1.2.3a4")
    assert version.version == (1, 2, 3)
    assert version.prerelease == ("a", 4)
    assert str(version) == "1.2.3a4"

    version = StrictVersion("2.7")
    assert version.version == (2, 7, 0)
    assert version.prerelease is None
    assert str(version) == "2.7"

    # A constructor without an argument is permitted.
    assert isinstance(StrictVersion(), StrictVersion)

    invalid_versions = ("1", "2.7.2.2", "1.3.a4", "1.3pl1", "1.3c4")
    for invalid_version in invalid_versions:
        try:
            StrictVersion(invalid_version)
        except ValueError:
            pass
        else:
            raise AssertionError(
                "StrictVersion accepted invalid version %r" % invalid_version
            )

# Generated at 2026-10-25 01:38:07.222003
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


# Generated at 2026-10-25 01:38:32.342623
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():cases = {
        "1.5.1": [1, 5, 1],
        "1.5.2b2": [1, 5, 2, "b", 2],
        "161": [161],
        "1996.07.12": [1996, 7, 12],
        "3.2.pl0": [3, 2, "pl", 0],
        "2g6": [2, "g", 6],
        "1.13++": [1, 13, "++"],
        "2.0b1pl0": [2, 0, "b", 1, "pl", 0],
    }


# Generated at 2026-10-25 01:38:37.348181
# Unit test for method __repr__ of class LooseVersion
def test_LooseVersion___repr__():
    version = LooseVersion("1.5.2b2")

    assert repr(version) == "LooseVersion ('1.5.2b2')"

    recreated = eval(repr(version))
    assert isinstance(recreated, LooseVersion)
    assert recreated.version == version.version
    assert str(recreated) == str(version)

# Generated at 2026-10-25 01:38:43.905136
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    version = StubVersion(1)
    assert version.__ge__(other) is True
    assert version.compared_with is other

    assert StubVersion(0).__ge__(other) is True
    assert StubVersion(-1).__ge__(other) is False
    assert StubVersion(NotImplemented).__ge__(other) is NotImplemented

# Generated at 2026-10-25 01:38:46.422369
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:38:49.002933
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:38:51.382676
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:38:53.798072
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:38:56.217374
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:39:00.776796
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():version = LooseVersion()

# Generated at 2026-10-25 01:39:06.823767
# Unit test for method __le__ of class Version
def test_Version___le__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for result, expected in [(-1, True), (0, True), (1, False)]:
        version = TestVersion(result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:39:15.524696
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def _cmp(self, other):
            return other

    version = StubVersion()

    assert version.__le__(-1) is True
    assert version.__le__(0) is True
    assert version.__le__(1) is False
    assert version.__le__(NotImplemented) is NotImplemented

# Generated at 2026-10-25 01:39:26.582982
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class StubVersion(Version):
        def _cmp(self, other):
            return other

    version = StubVersion()

    assert version.__ge__(-1) is False
    assert version.__ge__(0) is True
    assert version.__ge__(1) is True
    assert version.__ge__(NotImplemented) is NotImplemented

# Generated at 2026-10-25 01:39:31.804298
# Unit test for method __repr__ of class Version
def test_Version___repr__():
    class TestVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def __str__(self):
            return self.vstring

        def _cmp(self, other):
            return NotImplemented

    version = TestVersion("1.2.3")
    assert repr(version) == "TestVersion ('1.2.3')"

# Generated at 2026-10-25 01:39:39.689541
# Unit test for method __le__ of class Version
def test_Version___le__():
    class ComparableVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for result, expected in ((-1, True), (0, True), (1, False)):
        version = ComparableVersion(result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

    version = ComparableVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:39:49.487559
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in [
        (-1, True),
        (0, True),
        (1, False),
    ]:
        version = StubVersion(comparison_result)
        assert version <= other is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:39:51.905755
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:39:54.321811
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:39:56.736904
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:39:59.152807
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:40:01.565274
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:40:03.986076
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:40:06.398535
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:40:22.189787
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 01:40:37.342018
# Unit test for method __lt__ of class Version
def test_Version___lt__():left = Version()

# Generated at 2026-10-25 01:40:46.353442
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class TestVersion(Version):
        def __init__(self, cmp_result):
            self.cmp_result = cmp_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.cmp_result

    other = object()

    for cmp_result, expected in [(-1, True), (0, False), (1, False)]:
        version = TestVersion(cmp_result)
        assert version.__lt__(other) is expected
        assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:41:09.124437
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    greater = StubVersion(1)
    assert greater.__gt__(other) is True
    assert greater.compared_with is other

    equal = StubVersion(0)
    assert equal.__gt__(other) is False

    lesser = StubVersion(-1)
    assert lesser.__gt__(other) is False

    unsupported = StubVersion(NotImplemented)
    assert unsupported.__gt__(other) is NotImplemented

# Generated at 2026-10-25 01:41:19.082969
# Unit test for method __le__ of class Version
def test_Version___le__():
    version = Version()
    other = object()

    for comparison_result, expected in [
        (-1, True),
        (0, True),
        (1, False),
    ]:
        version._cmp = lambda value, result=comparison_result: result
        assert version.__le__(other) is expected

    version._cmp = lambda value: NotImplemented
    assert version.__le__(other) is NotImplemented

# Generated at 2026-10-25 01:41:42.421645
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in (
        (-1, False),
        (0, True),
        (1, False),
        (NotImplemented, NotImplemented),
    ):
        version = TestVersion(comparison_result)

        result = version.__eq__(other)

        assert result is expected
        assert version.compared_with is other

# Generated at 2026-10-25 01:41:51.171348
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in (
        (-1, True),
        (0, True),
        (1, False),
        (NotImplemented, NotImplemented),
    ):
        version = StubVersion(comparison_result)
        result = Version.__le__(version, other)

        assert result is expected
        assert version.compared_with is other

# Generated at 2026-10-25 01:42:14.418378
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in (
        (-1, False),
        (0, True),
        (1, False),
    ):
        version = StubVersion(comparison_result)
        assert version.__eq__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__eq__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:42:36.321329
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    version = TestVersion(0)
    assert version.__eq__(other) is True
    assert version.compared_with is other

    assert TestVersion(1).__eq__(other) is False
    assert TestVersion(-1).__eq__(other) is False
    assert TestVersion(NotImplemented).__eq__(other) is NotImplemented

# Generated at 2026-10-25 01:42:44.316698
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for result, expected in [(-1, True), (0, False), (1, False)]:
        version = StubVersion(result)
        assert version.__lt__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:42:51.488238
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in (
        (-1, True),
        (0, True),
        (1, False),
    ):
        version = StubVersion(comparison_result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:42:59.370411
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class StubVersion(Version):
        def __init__(self, cmp_result):
            self.cmp_result = cmp_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.cmp_result

    other = object()

    for cmp_result, expected in [(-1, True), (0, False), (1, False)]:
        version = StubVersion(cmp_result)
        assert version.__lt__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:43:21.843911
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    version = TestVersion(0)
    assert version.__eq__(other) is True
    assert version.compared_with is other

    version = TestVersion(-1)
    assert version.__eq__(other) is False
    assert version.compared_with is other

    version = TestVersion(1)
    assert version.__eq__(other) is False
    assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__eq__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:43:44.217388
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    greater = StubVersion(1)
    assert greater.__gt__(other) is True
    assert greater.compared_with is other

    equal = StubVersion(0)
    assert equal.__gt__(other) is False

    less = StubVersion(-1)
    assert less.__gt__(other) is False

    unsupported = StubVersion(NotImplemented)
    assert unsupported.__gt__(other) is NotImplemented

# Generated at 2026-10-25 01:43:52.208420
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for result, expected in [(-1, False), (0, True), (1, True)]:
        version = TestVersion(result)
        assert version.__ge__(other) is expected
        assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__ge__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:43:54.723445
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:43:57.139486
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:43:59.553986
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:44:01.969543
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:44:04.385043
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:44:06.802378
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:44:09.213446
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 01:44:11.627694
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 01:44:16.784871
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 01:44:40.337380
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import StrictVersion, LooseVersion

    # StrictVersion: greater-than comparisons
    assert StrictVersion('1.1') > StrictVersion('1.0')
    assert StrictVersion('2.0') > StrictVersion('1.9.9')
    assert StrictVersion('1.0.1') > StrictVersion('1.0')
    assert StrictVersion('1.0a1') < StrictVersion('1.0')  # prerelease is less
    assert not (StrictVersion('1.0') > StrictVersion('1.0'))
    assert not (StrictVersion('1.0') > StrictVersion('2.0'))

    # StrictVersion: comparison against a plain string
    assert StrictVersion('1.5') > '1.4'
    assert not (StrictVersion('1.5') > '1.6')

    # LooseVersion: component-wise comparison
    assert LooseVersion('1.2.10') > LooseVersion('1.2.9')
    assert LooseVersion('2.0') > LooseVersion('1.9.1')
    assert LooseVersion('1.0') > '0.9'
    assert not (LooseVersion('1.0') > LooseVersion('1.0'))

    # Rich comparison protocol: __gt__ returns NotImplemented for
    # incomparable types instead of raising
    result = LooseVersion('1.0').__gt__(object())
    assert result is NotImplemented

    result = StrictVersion('1.0').__gt__(None)
    assert result is NotImplemented

# Generated at 2026-10-25 01:44:55.098140
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, other):
            return self.comparison_result

    assert TestVersion(1).__gt__(object()) is True
    assert TestVersion(0).__gt__(object()) is False
    assert TestVersion(-1).__gt__(object()) is False
    assert TestVersion(NotImplemented).__gt__(object()) is NotImplemented

# Generated at 2026-10-25 01:44:58.419911
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:45:00.837694
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:45:03.250464
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:45:05.668741
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:45:08.082657
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:45:10.498782
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:45:12.916703
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:45:15.329126
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:45:17.744461
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:45:20.160389
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:45:22.576104
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:45:24.991216
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:45:27.406747
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:45:29.820331
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:45:32.235040
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 01:45:45.315457
# Unit test for method __le__ of class Version
def test_Version___le__():
    class ConcreteVersion(Version):
        def parse(self, vstring):
            self.version = tuple(int(p) for p in vstring.split('.'))

        def __str__(self):
            return '.'.join(str(p) for p in self.version)

        def _cmp(self, other):
            if isinstance(other, str):
                other = ConcreteVersion(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self.version == other.version:
                return 0
            return -1 if self.version < other.version else 1

    # instance vs instance
    assert ConcreteVersion('1.0') <= ConcreteVersion('1.0')
    assert ConcreteVersion('1.0') <= ConcreteVersion('1.1')
    assert not (ConcreteVersion('1.2') <= ConcreteVersion('1.1'))

    # instance vs string (parsed via _cmp)
    assert ConcreteVersion('1.0') <= '1.0'
    assert ConcreteVersion('1.0') <= '1.1'
    assert not (ConcreteVersion('1.2') <= '1.1')

    # unsupported comparison type routes NotImplemented through __le__
    assert ConcreteVersion('1.0').__le__(object()) is NotImplemented
    assert not (ConcreteVersion('1.0') <= object())

# Generated at 2026-10-25 01:45:52.329700
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in (
        (-1, True),
        (0, True),
        (1, False),
        (NotImplemented, NotImplemented),
    ):
        version = StubVersion(comparison_result)
        result = version.__le__(other)

        assert result is expected
        assert version.compared_with is other

# Generated at 2026-10-25 01:45:59.697337
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for result, expected in [(-1, True), (0, True), (1, False)]:
        version = StubVersion(result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:46:06.349162
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in [
        (-1, False),
        (0, True),
        (1, True),
    ]:
        version = StubVersion(comparison_result)
        assert version.__ge__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__ge__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:46:08.882468
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:46:11.401730
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:46:13.817523
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:46:16.803305
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:46:19.217710
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:46:21.632408
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:46:24.047443
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:46:26.467390
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:46:28.886706
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:46:31.304713
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:46:33.870875
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:46:36.283946
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:46:38.698527
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:46:41.116060
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:46:43.530647
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 01:46:45.945160
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:46:48.361258
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:46:50.776293
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:46:53.191699
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:46:55.606929
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:46:58.027993
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 01:47:00.436706
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:47:02.851094
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:47:10.769130
# Unit test for method __ge__ of class Version
def test_Version___ge__():version = Version()

# Generated at 2026-10-25 01:47:27.250121
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.vstring = str(vstring)
            self.value = int(self.vstring)

        def __str__(self):
            return self.vstring

        def _cmp(self, other):
            if isinstance(other, str):
                other = DummyVersion(other)
            elif not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    # _cmp() == 0 -> True
    assert DummyVersion("1") == DummyVersion("1")
    assert DummyVersion("1") == "1"
    assert DummyVersion("2") == DummyVersion("2")

    # _cmp() < 0 or > 0 -> False
    assert not (DummyVersion("1") == DummyVersion("2"))
    assert not (DummyVersion("2") == DummyVersion("1"))
    assert not (DummyVersion("1") == "2")
    assert DummyVersion("1") != DummyVersion("2")

    # _cmp() is NotImplemented -> __eq__ returns NotImplemented
    assert DummyVersion("1").__eq__(object()) is NotImplemented
    assert DummyVersion("1").__eq__(1) is NotImplemented
    assert not (DummyVersion("1") == object())

# Generated at 2026-10-25 01:47:43.742412
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.vstring = str(vstring)
            self.value = int(self.vstring)

        def __str__(self):
            return self.vstring

        def _cmp(self, other):
            if isinstance(other, str):
                other = DummyVersion(other)
            elif not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    # _cmp() == 0 -> True
    assert DummyVersion("1") == DummyVersion("1")
    assert DummyVersion("1") == "1"
    assert DummyVersion("2") == DummyVersion("2")

    # _cmp() < 0 or > 0 -> False
    assert not (DummyVersion("1") == DummyVersion("2"))
    assert not (DummyVersion("2") == DummyVersion("1"))
    assert not (DummyVersion("1") == "2")
    assert DummyVersion("1") != DummyVersion("2")

    # _cmp() is NotImplemented -> __eq__ returns NotImplemented
    assert DummyVersion("1").__eq__(object()) is NotImplemented
    assert DummyVersion("1").__eq__(1) is NotImplemented
    assert not (DummyVersion("1") == object())

# Generated at 2026-10-25 01:47:51.825605
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for comparison_result, expected in [
        (-1, False),
        (0, True),
        (1, True),
    ]:
        version = StubVersion(comparison_result)
        assert Version.__ge__(version, other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert Version.__ge__(version, other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 01:47:54.343277
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:47:56.875078
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 01:47:59.290748
# Unit test for method __ge__ of class Version