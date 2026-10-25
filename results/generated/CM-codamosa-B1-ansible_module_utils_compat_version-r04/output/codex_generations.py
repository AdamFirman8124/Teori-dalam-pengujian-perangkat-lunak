

# Generated at 2026-10-25 04:21:53.423179
# Unit test for method __str__ of class LooseVersion

# Generated at 2026-10-25 04:21:55.854190
# Unit test for method __str__ of class LooseVersion

# Generated at 2026-10-25 04:21:58.291663
# Unit test for method __str__ of class LooseVersion

# Generated at 2026-10-25 04:22:00.735089
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 04:22:03.149522
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 04:22:05.565845
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 04:22:07.981603
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 04:22:10.395250
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 04:22:12.809182
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 04:22:15.224438
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 04:22:19.580895
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():v = LooseVersion()
v.parse("1.5.2b2")
assert v.version == [1, 5, 2, 'b', 2], "expected [1, 5, 2, 'b', 2], got %r" % (v.version,)
assert v.vstring == "1.5.2b2"

# Generated at 2026-10-25 04:22:26.749643
# Unit test for constructor of class LooseVersion
def test_LooseVersion():
    version = LooseVersion("1.5.2b2")

    assert version.vstring == "1.5.2b2"
    assert version.version == [1, 5, 2, "b", 2]
    assert str(version) == "1.5.2b2"
    assert repr(version) == "LooseVersion ('1.5.2b2')"

# Generated at 2026-10-25 04:22:51.187679
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class TestVersion(Version):
        def __init__(self, comparison):
            self.comparison = comparison
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison

    other = object()

    for comparison, expected in [(-1, False), (0, True), (1, True)]:
        version = TestVersion(comparison)
        assert version.__ge__(other) is expected
        assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__ge__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 04:22:59.619940
# Unit test for method __le__ of class Version
def test_Version___le__():
    class DummyVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    for result, expected in [(-1, True), (0, True), (1, False)]:
        version = DummyVersion(result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

    version = DummyVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented

# Generated at 2026-10-25 04:23:02.181826
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:23:04.597097
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:23:07.013964
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:23:09.427812
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:23:11.842095
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:23:14.257062
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:23:22.454885
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:23:28.089409
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:23:33.717907
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:23:42.319664
# Unit test for method __repr__ of class Version
def test_Version___repr__():
    # Version is abstract (no __str__/parse); use a minimal concrete subclass
    class _V(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def __str__(self):
            return self.vstring

    v = _V('1.2.3')

    # Format: ClassName ('string')
    assert repr(v) == "_V ('1.2.3')"

    # repr() delegates to __repr__
    assert v.__repr__() == repr(v)

    # Docstring contract: repr generates code that recreates the instance
    v2 = eval(repr(v), {'_V': _V})
    assert isinstance(v2, _V)
    assert str(v2) == '1.2.3'

    # Empty string version (unparsed instance is not required to work;
    # constructor with a string always parses)
    v3 = _V('10')
    assert repr(v3) == "_V ('10')"

# Generated at 2026-10-25 04:24:06.078319
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

    version = StubVersion(-1)
    assert version.__lt__(other) is True
    assert version.compared_with is other

    assert StubVersion(0).__lt__(other) is False
    assert StubVersion(1).__lt__(other) is False
    assert StubVersion(NotImplemented).__lt__(other) is NotImplemented

# Generated at 2026-10-25 04:24:08.500844
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:24:10.916229
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:24:13.343242
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:24:15.753615
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:24:18.171087
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:24:20.586943
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:24:23.001060
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:24:25.416495
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:24:27.836975
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:24:30.250244
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 04:24:32.664773
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 04:24:35.079906
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 04:24:37.495333
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:24:39.910742
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:24:42.324982
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:24:44.739847
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:24:47.153325
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:24:49.570979
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:24:51.982261
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:24:54.396895
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:24:56.811975
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:24:59.226439
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:25:01.641084
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:25:04.058285
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:25:06.482102
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:25:08.897037
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:25:11.314703
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:25:13.728130
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:25:16.144108
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:25:18.560629
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:25:20.096436
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


# Generated at 2026-10-25 04:25:30.661576
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

# Generated at 2026-10-25 04:25:32.069397
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


# Generated at 2026-10-25 04:25:40.798446
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class StubVersion(Version):
        def __init__(self, cmp_result):
            self.cmp_result = cmp_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.cmp_result

    other = object()

    for cmp_result, expected in ((1, True), (0, False), (-1, False)):
        version = StubVersion(cmp_result)
        assert version.__gt__(other) is expected
        assert version.compared_with is other

    version = StubVersion(NotImplemented)
    assert version.__gt__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-25 04:26:11.521353
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # c > 0 -> True
    assert (_FakeVersion(1) >= _FakeVersion(0)) is True
    # c == 0 -> True: __ge__ must use >=, not >
    assert (_FakeVersion(0) >= _FakeVersion(0)) is True
    # c < 0 -> False
    assert (_FakeVersion(-1) >= _FakeVersion(0)) is False
    # NotImplemented is returned unchanged, not coerced to bool
    assert _FakeVersion(0).__ge__(object()) is NotImplemented


def test_Version___ge___passes_other_to_cmp():
    left, right = _FakeVersion(0), _FakeVersion(0)
    with mock.patch.object(type(left), "_cmp", return_value=0) as m:
        assert (left >= right) is True
    m.assert_called_once_with(right)


def test_Version___ge___real_subclasses():
    from distutils.version import LooseVersion, StrictVersion

    assert (LooseVersion("1.5.1") >= LooseVersion("1.5.0")) is True
    assert (LooseVersion("1.5.0") >= LooseVersion("1.5.0")) is True
    assert (LooseVersion("1.5.0") >= LooseVersion("1.5.1")) is False
    assert (StrictVersion("1.5.1") >= StrictVersion("1.5.0")) is True

# Generated at 2026-10-25 04:26:13.940100
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:26:16.356385
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:26:18.773749
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:26:21.185618
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:26:31.290938
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class _V(Version):
        def parse(self, vstring):
            self.vstring = vstring
            self.value = int(vstring)

        def _cmp(self, other):
            if isinstance(other, str):
                other = _V(other)
            if not isinstance(other, _V):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    # __lt__ must be inherited from Version, not redefined by the subclass.
    assert '__lt__' not in _V.__dict__
    assert _V.__lt__ is Version.__lt__

    # Instance vs instance.
    assert (_V('1') < _V('2')) is True
    assert (_V('2') < _V('1')) is False
    assert (_V('2') < _V('2')) is False

    # Instance vs string (string is parsed by _cmp).
    assert (_V('1') < '2') is True
    assert (_V('2') < '1') is False
    assert (_V('2') < '2') is False

    # Unsupported operand: __lt__ itself returns NotImplemented.
    assert Version.__lt__(_V('1'), 2) is NotImplemented
    assert Version.__lt__(_V('1'), None) is NotImplemented

# Generated at 2026-10-25 04:26:37.205322
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    test_cases = [
        ("0.4", "0.4"),
        ("0.4.0", "0.4"),
        ("0.4.1", "0.4.1"),
        ("1.0a1", "1.0a1"),
        ("1.0b2", "1.0b2"),
        ("1.0.0a1", "1.0a1"),
        ("1.0.4a3", "1.0.4a3"),
        ("1.0.4b1", "1.0.4b1"),
        ("10.20.30", "10.20.30"),
    ]

    for version_string, expected in test_cases:
        assert str(StrictVersion(version_string)) == expected

# Generated at 2026-10-25 04:26:55.027177
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:26:57.573272
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:26:59.988231
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:27:02.402216
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:27:04.986325
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:27:07.401610
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:27:09.816496
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:27:12.231459
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:27:14.646455
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:27:17.064391
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:27:19.484050
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:27:21.899595
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:27:24.314284
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:27:26.729237
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:27:29.144613
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 04:27:31.558568
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:27:33.972756
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:27:45.214781
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:27:54.852862
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:28:00.233833
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:28:01.597988
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:28:03.031537
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


# Generated at 2026-10-25 04:28:05.562969
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:28:07.977996
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:28:10.567433
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:28:12.982026
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:28:15.396604
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:28:17.814820
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:28:20.226470
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 04:28:22.641117
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 04:28:25.055481
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 04:28:27.470245
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:28:29.884691
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:28:32.299889
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:28:34.713876
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:28:37.128897
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:28:43.786964
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:28:49.316970
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    test_cases = [
        ("1.2", "1.2"),
        ("1.2.0", "1.2"),
        ("1.2.3", "1.2.3"),
        ("1.2a4", "1.2a4"),
        ("1.2.0b5", "1.2b5"),
        ("1.2.3a4", "1.2.3a4"),
        ("1.2.3b5", "1.2.3b5"),
    ]

    for version_string, expected in test_cases:
        assert str(StrictVersion(version_string)) == expected

# Generated at 2026-10-25 04:28:50.750511
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


# Generated at 2026-10-25 04:29:08.760033
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:29:11.176367
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:29:13.590895
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:29:16.006148
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:29:18.421098
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:29:20.835347
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:29:23.252095
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:29:25.825547
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:29:28.240895
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:29:30.653890
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:29:33.070536
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:29:35.488062
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:29:37.906392
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:29:40.321867
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:29:45.252710
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():version = StrictVersion()

# Generated at 2026-10-25 04:29:51.410165
# Unit test for method __le__ of class Version
def test_Version___le__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, other):
            return self.comparison_result

    other = object()

    assert TestVersion(-1).__le__(other) is True
    assert TestVersion(0).__le__(other) is True
    assert TestVersion(1).__le__(other) is False
    assert TestVersion(NotImplemented).__le__(other) is NotImplemented

# Generated at 2026-10-25 04:29:52.907349
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


# Generated at 2026-10-25 04:30:06.925812
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:30:09.346656
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:30:11.760715
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 04:30:14.295050
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:30:16.721227
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:30:19.137830
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:30:21.551493
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:30:23.967455
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:30:26.381142
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 04:30:28.795784
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:30:31.210850
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:30:33.622644
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:30:36.037879
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:30:38.453487
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:30:40.874876
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 04:30:43.288890
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:30:45.708882
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:30:48.124894
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:30:50.544233
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:30:52.957774
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:30:55.373986
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 04:30:57.786355
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:31:00.200221
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:31:02.617978
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 04:31:05.032710
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:31:07.447930
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 04:31:17.522525
# Unit test for method __ge__ of class Version