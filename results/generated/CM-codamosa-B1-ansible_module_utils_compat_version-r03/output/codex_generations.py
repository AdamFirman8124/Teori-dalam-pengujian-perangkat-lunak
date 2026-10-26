

# Generated at 2026-10-25 10:29:03.918588
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    valid = [
        ("0.4",     (0, 4, 0), None,       "0.4"),
        ("0.4.0",   (0, 4, 0), None,       "0.4"),
        ("0.4.1",   (0, 4, 1), None,       "0.4.1"),
        ("0.5a1",   (0, 5, 0), ("a", 1),   "0.5a1"),
        ("0.5b3",   (0, 5, 0), ("b", 3),   "0.5b3"),
        ("1.0",     (1, 0, 0), None,       "1.0"),
        ("1.0.4a3", (1, 0, 4), ("a", 3),   "1.0.4a3"),
        ("1.0.4b1", (1, 0, 4), ("b", 1),   "1.0.4b1"),
    ]
    for vstring, version, prerelease, normalized in valid:
        v = StrictVersion()
        assert v.parse(vstring) is None
        assert v.version == version
        assert v.prerelease == prerelease
        assert str(v) == normalized
        assert StrictVersion(vstring).version == version
        assert StrictVersion(vstring).prerelease == prerelease

    invalid = ["1", "2.7.2.2", "1.3.a4", "1.3pl1", "1.3c4",
               "1.0a", "1..0", "a1.0", ""]
    for vstring in invalid:
        with pytest.raises(ValueError, match="invalid version number"):
            StrictVersion().parse(vstring)

    # Re-parsing resets previous prerelease state
    v = StrictVersion("1.0a1")
    v.parse("1.0")
    assert v.version == (1, 0, 0)
    assert v.prerelease is None

# Generated at 2026-10-25 10:29:05.453251
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    valid = [
        ("0.4",     (0, 4, 0), None,       "0.4"),
        ("0.4.0",   (0, 4, 0), None,       "0.4"),
        ("0.4.1",   (0, 4, 1), None,       "0.4.1"),
        ("0.5a1",   (0, 5, 0), ("a", 1),   "0.5a1"),
        ("0.5b3",   (0, 5, 0), ("b", 3),   "0.5b3"),
        ("1.0",     (1, 0, 0), None,       "1.0"),
        ("1.0.4a3", (1, 0, 4), ("a", 3),   "1.0.4a3"),
        ("1.0.4b1", (1, 0, 4), ("b", 1),   "1.0.4b1"),
    ]
    for vstring, version, prerelease, normalized in valid:
        v = StrictVersion()
        assert v.parse(vstring) is None
        assert v.version == version
        assert v.prerelease == prerelease
        assert str(v) == normalized
        assert StrictVersion(vstring).version == version
        assert StrictVersion(vstring).prerelease == prerelease

    invalid = ["1", "2.7.2.2", "1.3.a4", "1.3pl1", "1.3c4",
               "1.0a", "1..0", "a1.0", ""]
    for vstring in invalid:
        with pytest.raises(ValueError, match="invalid version number"):
            StrictVersion().parse(vstring)

    # Re-parsing resets previous prerelease state
    v = StrictVersion("1.0a1")
    v.parse("1.0")
    assert v.version == (1, 0, 0)
    assert v.prerelease is None

# Generated at 2026-10-25 10:29:21.736110
# Unit test for constructor of class Version
def test_Version():
    """Unit test for Version.__init__."""

    class DummyVersion(Version):
        def parse(self, vstring):
            self.parsed = vstring
            self.parse_call_count = getattr(self, "parse_call_count", 0) + 1

        def __str__(self):
            return getattr(self, "parsed", "")

        def _cmp(self, other):
            return 0

    # 1. No

# Generated at 2026-10-25 10:29:36.585379
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Version has no parse/_cmp, so use a minimal concrete subclass.
    class V(Version):
        def parse(self, vstring):
            self.vstring = vstring
            self.parts = [int(p) for p in vstring.split('.')]

        def _cmp(self, other):
            if isinstance(other, str):
                other = V(other)
            if not isinstance(other, V):
                return NotImplemented
            return (self.parts > other.parts) - (self.parts < other.parts)

        def __str__(self):
            return self.vstring

    # _cmp < 0  ->  True
    assert V('1.2') < V('1.10')

    # string operand is parsed by _cmp
    assert V('1.2') < '1.10'

    # _cmp > 0  ->  False
    assert not (V('1.10') < V('1.2'))

    # _cmp == 0 ->  False (not an error)
    assert not (V('1.2') < V('1.2'))

    # NotImplemented is returned verbatim from the dunder
    assert V('1.2').__lt__(object()) is NotImplemented

    # ...and the operator protocol turns that into TypeError
    try:
        V('1.2') < object()
    except TypeError:
        pass
    else:
        raise AssertionError('expected TypeError for uncomparable operand')

# Generated at 2026-10-25 10:29:44.468152
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:29:46.884894
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:29:49.301610
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:29:51.936871
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:30:00.035937
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:30:01.468272
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:30:09.146932
# Unit test for method __repr__ of class LooseVersion
def test_LooseVersion___repr__():
    """repr() should return Python code that recreates the instance."""
    from distutils.version import LooseVersion

    # Basic case: repr round-trips via eval
    v = LooseVersion('1.5.1')
    assert repr(v) == "LooseVersion ('1.5.1')", repr(v)
    assert eval(repr(v)) == v

    # Multi-component version with letters
    v = LooseVersion('2.2beta29')
    assert repr(v) == "LooseVersion ('2.2beta29')", repr(v)
    assert eval(repr(v)) == v

    # Version with prerelease-style suffix
    v = LooseVersion('1.5.2b2')
    assert repr(v) == "LooseVersion ('1.5.2b2')", repr(v)

    # Single numeric component
    v = LooseVersion('161')
    assert repr(v) == "LooseVersion ('161')", repr(v)

    # Odd-but-valid LooseVersion string is preserved verbatim
    v = LooseVersion('1.13++')
    assert repr(v) == "LooseVersion ('1.13++')", repr(v)

    # repr uses the stored vstring, so it matches str() exactly
    v = LooseVersion('3.4j')
    assert repr(v) == "LooseVersion ('%s')" % str(v), repr(v)

    print("test_LooseVersion___repr__ passed")


test_LooseVersion___repr__()

# Generated at 2026-10-25 10:30:16.015432
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    valid = [
        ("0.4",     (0, 4, 0), None,       "0.4"),
        ("0.4.0",   (0, 4, 0), None,       "0.4"),
        ("0.4.1",   (0, 4, 1), None,       "0.4.1"),
        ("0.5a1",   (0, 5, 0), ("a", 1),   "0.5a1"),
        ("0.5b3",   (0, 5, 0), ("b", 3),   "0.5b3"),
        ("1.0",     (1, 0, 0), None,       "1.0"),
        ("1.0.4a3", (1, 0, 4), ("a", 3),   "1.0.4a3"),
        ("1.0.4b1", (1, 0, 4), ("b", 1),   "1.0.4b1"),
    ]
    for vstring, version, prerelease, normalized in valid:
        v = StrictVersion()
        assert v.parse(vstring) is None
        assert v.version == version
        assert v.prerelease == prerelease
        assert str(v) == normalized
        assert StrictVersion(vstring).version == version
        assert StrictVersion(vstring).prerelease == prerelease

    invalid = ["1", "2.7.2.2", "1.3.a4", "1.3pl1", "1.3c4",
               "1.0a", "1..0", "a1.0", ""]
    for vstring in invalid:
        with pytest.raises(ValueError, match="invalid version number"):
            StrictVersion().parse(vstring)

    # Re-parsing resets previous prerelease state
    v = StrictVersion("1.0a1")
    v.parse("1.0")
    assert v.version == (1, 0, 0)
    assert v.prerelease is None

# Generated at 2026-10-25 10:30:32.292188
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:30:34.708095
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:30:37.286946
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:30:39.701728
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:30:42.326505
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:30:45.095151
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:30:47.657042
# Unit test for method __repr__ of class LooseVersion

# Generated at 2026-10-25 10:30:50.201859
# Unit test for method __repr__ of class LooseVersion

# Generated at 2026-10-25 10:30:52.616427
# Unit test for method __repr__ of class LooseVersion

# Generated at 2026-10-25 10:30:55.032244
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:30:57.448635
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:30:59.863480
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:31:02.282244
# Unit test for method __repr__ of class LooseVersion

# Generated at 2026-10-25 10:31:04.695834
# Unit test for method __repr__ of class LooseVersion

# Generated at 2026-10-25 10:31:07.111136
# Unit test for method __repr__ of class LooseVersion

# Generated at 2026-10-25 10:31:09.529689
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:31:11.997867
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:31:14.405036
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:31:16.817684
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:31:19.246275
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:31:21.657975
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:31:24.073317
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:31:26.491274
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:31:28.908973
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:31:31.334147
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:31:33.750088
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:31:36.170350
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:31:38.588006
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:31:56.157949
# Unit test for method __le__ of class Version
def test_Version___le__():
    class NumVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring
            self.parts = tuple(int(p) for p in vstring.split('.'))

        def __str__(self):
            return self.vstring

        def _cmp(self, other):
            if isinstance(other, str):
                other = NumVersion(other)
            if not isinstance(other, Version):
                return NotImplemented
            if self.parts == other.parts:
                return 0
            return -1 if self.parts < other.parts else 1

    v = NumVersion('1.2.3')

    assert (v <= NumVersion('1.2.3')) is True      # equal -> True
    assert (v <= NumVersion('1.2.4')) is True      # strictly less -> True
    assert (v <= NumVersion('1.2.2')) is False     # greater -> False
    assert (v <= '1.2.3') is True                  # string gets parsed
    assert (v <= '2.0.0') is True
    assert (v <= '1.0.0') is False
    assert NumVersion.__le__(v, object()) is NotImplemented

# Generated at 2026-10-25 10:31:57.658379
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    valid = [
        ("0.4",     (0, 4, 0), None,       "0.4"),
        ("0.4.0",   (0, 4, 0), None,       "0.4"),
        ("0.4.1",   (0, 4, 1), None,       "0.4.1"),
        ("0.5a1",   (0, 5, 0), ("a", 1),   "0.5a1"),
        ("0.5b3",   (0, 5, 0), ("b", 3),   "0.5b3"),
        ("1.0",     (1, 0, 0), None,       "1.0"),
        ("1.0.4a3", (1, 0, 4), ("a", 3),   "1.0.4a3"),
        ("1.0.4b1", (1, 0, 4), ("b", 1),   "1.0.4b1"),
    ]
    for vstring, version, prerelease, normalized in valid:
        v = StrictVersion()
        assert v.parse(vstring) is None
        assert v.version == version
        assert v.prerelease == prerelease
        assert str(v) == normalized
        assert StrictVersion(vstring).version == version
        assert StrictVersion(vstring).prerelease == prerelease

    invalid = ["1", "2.7.2.2", "1.3.a4", "1.3pl1", "1.3c4",
               "1.0a", "1..0", "a1.0", ""]
    for vstring in invalid:
        with pytest.raises(ValueError, match="invalid version number"):
            StrictVersion().parse(vstring)

    # Re-parsing resets previous prerelease state
    v = StrictVersion("1.0a1")
    v.parse("1.0")
    assert v.version == (1, 0, 0)
    assert v.prerelease is None

# Generated at 2026-10-25 10:32:02.915369
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, result):
            self.result = result
            self.seen = None

        def _cmp(self, other):
            self.seen = other
            return self.result

    other = object()

    # _cmp() < 0 and == 0 are <=, _cmp() > 0 is not
    assert Stub(-1).__le__(other) is True
    assert Stub(0).__le__(other) is True
    assert Stub(1).__le__(other) is False

    # Operator form
    assert (Stub(0) <= other) is True
    assert (Stub(1) <= other) is False

    # `other` is passed through to _cmp()
    stub = Stub(0)
    stub.__le__(other)
    assert stub.seen is other

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(other) is NotImplemented

# Generated at 2026-10-25 10:32:04.454535
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    valid = [
        ("0.4",     (0, 4, 0), None,       "0.4"),
        ("0.4.0",   (0, 4, 0), None,       "0.4"),
        ("0.4.1",   (0, 4, 1), None,       "0.4.1"),
        ("0.5a1",   (0, 5, 0), ("a", 1),   "0.5a1"),
        ("0.5b3",   (0, 5, 0), ("b", 3),   "0.5b3"),
        ("1.0",     (1, 0, 0), None,       "1.0"),
        ("1.0.4a3", (1, 0, 4), ("a", 3),   "1.0.4a3"),
        ("1.0.4b1", (1, 0, 4), ("b", 1),   "1.0.4b1"),
    ]
    for vstring, version, prerelease, normalized in valid:
        v = StrictVersion()
        assert v.parse(vstring) is None
        assert v.version == version
        assert v.prerelease == prerelease
        assert str(v) == normalized
        assert StrictVersion(vstring).version == version
        assert StrictVersion(vstring).prerelease == prerelease

    invalid = ["1", "2.7.2.2", "1.3.a4", "1.3pl1", "1.3c4",
               "1.0a", "1..0", "a1.0", ""]
    for vstring in invalid:
        with pytest.raises(ValueError, match="invalid version number"):
            StrictVersion().parse(vstring)

    # Re-parsing resets previous prerelease state
    v = StrictVersion("1.0a1")
    v.parse("1.0")
    assert v.version == (1, 0, 0)
    assert v.prerelease is None

# Generated at 2026-10-25 10:32:05.881731
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

# Generated at 2026-10-25 10:32:07.972527
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

# Generated at 2026-10-25 10:32:09.471305
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Version has no parse/_cmp, so use a minimal concrete subclass.
    class V(Version):
        def parse(self, vstring):
            self.vstring = vstring
            self.parts = [int(p) for p in vstring.split('.')]

        def _cmp(self, other):
            if isinstance(other, str):
                other = V(other)
            if not isinstance(other, V):
                return NotImplemented
            return (self.parts > other.parts) - (self.parts < other.parts)

        def __str__(self):
            return self.vstring

    # _cmp < 0  ->  True
    assert V('1.2') < V('1.10')

    # string operand is parsed by _cmp
    assert V('1.2') < '1.10'

    # _cmp > 0  ->  False
    assert not (V('1.10') < V('1.2'))

    # _cmp == 0 ->  False (not an error)
    assert not (V('1.2') < V('1.2'))

    # NotImplemented is returned verbatim from the dunder
    assert V('1.2').__lt__(object()) is NotImplemented

    # ...and the operator protocol turns that into TypeError
    try:
        V('1.2') < object()
    except TypeError:
        pass
    else:
        raise AssertionError('expected TypeError for uncomparable operand')

# Generated at 2026-10-25 10:32:12.540987
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:32:28.998936
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:32:31.416914
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:32:33.831258
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:32:36.269710
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:32:38.877311
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:32:41.297311
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:32:43.714011
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:32:46.158531
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:32:48.574403
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:32:50.990408
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:32:53.404851
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:32:55.825095
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:32:58.238936
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:33:00.651258
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:33:03.067802
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:33:05.482071
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:33:07.903008
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:33:10.319119
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 10:33:12.732344
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 10:33:15.147595
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 10:33:17.564137
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:33:19.981076
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:33:22.398808
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:33:24.812869
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:33:27.227203
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:33:29.643884
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:33:32.060134
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:33:34.472463
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:33:36.887611
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:33:39.305905
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:33:41.718263
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:33:44.132894
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:33:46.549249
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:33:48.962927
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:33:51.379113
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:33:53.793114
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:33:56.209921
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:33:58.627607
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:34:01.042319
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:34:03.461949
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:34:05.873830
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:34:08.288938
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:34:10.704723
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:34:13.123461
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:34:15.545789
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:34:17.959781
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:34:20.376510
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:34:22.791498
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:34:25.208355
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:34:27.627325
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:34:30.042920
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:34:32.457039
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:34:34.872625
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:34:37.287222
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:34:39.704514
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:34:42.118142
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:34:44.532553
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:34:46.947607
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:34:49.364986
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:34:51.777322
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:34:54.192953
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:34:56.606561
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:34:59.021535
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:35:01.436163
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:35:03.851411
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:35:06.266362
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:35:08.683498
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:35:11.102371
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:35:13.513993
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:35:15.932110
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:35:18.347083
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:35:20.761904
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:35:23.175195
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:35:25.591412
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:35:28.006724
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:35:30.423103
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:35:32.871609
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:35:35.285310
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 10:35:37.698261
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 10:35:40.111980
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 10:35:42.530268
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:35:45.064362
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:35:47.421591
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:35:49.833585
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:35:52.246286
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:35:54.657572
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:35:57.070666
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:35:59.484772
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:36:01.899985
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 10:36:04.317302
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:36:06.729344
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:36:09.142609
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:36:11.683820
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:36:13.971161
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:36:16.386404
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:36:36.344305
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 10:36:45.745819
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():version = StrictVersion()
version.parse("1.2.3")
assert version.version == (1, 2, 3)
assert version.prerelease is None

version.parse("2.7b4")
assert version.version == (2, 7, 0)
assert version.prerelease == ("b", 4)

# Generated at 2026-10-25 10:36:47.178385
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version._cmp is abstract."""
        def __init__(self, value):
            self.value = value
            super(ConcreteVersion, self).__init__()

        def _cmp(self, other):
            if isinstance(other, ConcreteVersion):
                other = other.value
            if not isinstance(other, (int, float)):
                return NotImplemented
            if self.value > other:
                return 1
            elif self.value < other:
                return -1
            return 0

    v = ConcreteVersion(2)

    # Greater-than cases
    assert v > 1
    assert v > ConcreteVersion(1)

    # Not-greater cases
    assert not (v > 2)
    assert not (v > 3)
    assert not (v > ConcreteVersion(3))

    # NotImplemented propagation: comparing against an unsupported
    # type must return NotImplemented, not raise or return False.
    assert v.__gt__("not-a-version") is NotImplemented
    assert v.__gt__(None) is NotImplemented

    # Rich comparison delegates through Version.__gt__, so the bool
    # of the reflected comparison must be handled by the other operand
    # (Python falls back / raises TypeError as appropriate).
    try:
        v > object()
        raised = False
    except TypeError:
        raised = True
    assert raised, "comparison with unsupported type should raise TypeError"

# Generated at 2026-10-25 10:36:48.587082
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, result):
            self.result = result
            self.seen = None

        def _cmp(self, other):
            self.seen = other
            return self.result

    other = object()

    # _cmp() < 0 and == 0 are <=, _cmp() > 0 is not
    assert Stub(-1).__le__(other) is True
    assert Stub(0).__le__(other) is True
    assert Stub(1).__le__(other) is False

    # Operator form
    assert (Stub(0) <= other) is True
    assert (Stub(1) <= other) is False

    # `other` is passed through to _cmp()
    stub = Stub(0)
    stub.__le__(other)
    assert stub.seen is other

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(other) is NotImplemented

# Generated at 2026-10-25 10:36:51.434315
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:37:04.671338
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:37:07.084561
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:37:09.671044
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:37:12.084227
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:37:14.496858
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 10:37:16.912545
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:37:19.342163
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:37:21.757227
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 10:37:24.171579
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:37:38.685630
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():from distutils.version import StrictVersion

    # Two-component versions with a zero patch are printed without the patch

# Generated at 2026-10-25 10:37:53.229122
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:37:54.643926
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:38:11.762035
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 10:38:14.424651
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:38:16.839891
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:38:19.256156
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 10:38:21.671836
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:38:24.086631
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:38:25.656055
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():from distutils.version import StrictVersion

    # Two-component versions with a zero patch are printed without the patch

# Generated at 2026-10-25 10:38:30.305298
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Version has no parse/_cmp, so use a minimal concrete subclass.
    class V(Version):
        def parse(self, vstring):
            self.vstring = vstring
            self.parts = [int(p) for p in vstring.split('.')]

        def _cmp(self, other):
            if isinstance(other, str):
                other = V(other)
            if not isinstance(other, V):
                return NotImplemented
            return (self.parts > other.parts) - (self.parts < other.parts)

        def __str__(self):
            return self.vstring

    # _cmp < 0  ->  True
    assert V('1.2') < V('1.10')

    # string operand is parsed by _cmp
    assert V('1.2') < '1.10'

    # _cmp > 0  ->  False
    assert not (V('1.10') < V('1.2'))

    # _cmp == 0 ->  False (not an error)
    assert not (V('1.2') < V('1.2'))

    # NotImplemented is returned verbatim from the dunder
    assert V('1.2').__lt__(object()) is NotImplemented

    # ...and the operator protocol turns that into TypeError
    try:
        V('1.2') < object()
    except TypeError:
        pass
    else:
        raise AssertionError('expected TypeError for uncomparable operand')

# Generated at 2026-10-25 10:38:31.683000
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version._cmp is abstract."""
        def __init__(self, value):
            self.value = value
            super(ConcreteVersion, self).__init__()

        def _cmp(self, other):
            if isinstance(other, ConcreteVersion):
                other = other.value
            if not isinstance(other, (int, float)):
                return NotImplemented
            if self.value > other:
                return 1
            elif self.value < other:
                return -1
            return 0

    v = ConcreteVersion(2)

    # Greater-than cases
    assert v > 1
    assert v > ConcreteVersion(1)

    # Not-greater cases
    assert not (v > 2)
    assert not (v > 3)
    assert not (v > ConcreteVersion(3))

    # NotImplemented propagation: comparing against an unsupported
    # type must return NotImplemented, not raise or return False.
    assert v.__gt__("not-a-version") is NotImplemented
    assert v.__gt__(None) is NotImplemented

    # Rich comparison delegates through Version.__gt__, so the bool
    # of the reflected comparison must be handled by the other operand
    # (Python falls back / raises TypeError as appropriate).
    try:
        v > object()
        raised = False
    except TypeError:
        raised = True
    assert raised, "comparison with unsupported type should raise TypeError"

# Generated at 2026-10-25 10:38:33.032195
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, result):
            self.result = result
            self.seen = None

        def _cmp(self, other):
            self.seen = other
            return self.result

    other = object()

    # _cmp() < 0 and == 0 are <=, _cmp() > 0 is not
    assert Stub(-1).__le__(other) is True
    assert Stub(0).__le__(other) is True
    assert Stub(1).__le__(other) is False

    # Operator form
    assert (Stub(0) <= other) is True
    assert (Stub(1) <= other) is False

    # `other` is passed through to _cmp()
    stub = Stub(0)
    stub.__le__(other)
    assert stub.seen is other

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(other) is NotImplemented

# Generated at 2026-10-25 10:38:34.377823
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version._cmp is abstract."""
        def __init__(self, value):
            self.value = value
            super(ConcreteVersion, self).__init__()

        def _cmp(self, other):
            if isinstance(other, ConcreteVersion):
                other = other.value
            if not isinstance(other, (int, float)):
                return NotImplemented
            if self.value > other:
                return 1
            elif self.value < other:
                return -1
            return 0

    v = ConcreteVersion(2)

    # Greater-than cases
    assert v > 1
    assert v > ConcreteVersion(1)

    # Not-greater cases
    assert not (v > 2)
    assert not (v > 3)
    assert not (v > ConcreteVersion(3))

    # NotImplemented propagation: comparing against an unsupported
    # type must return NotImplemented, not raise or return False.
    assert v.__gt__("not-a-version") is NotImplemented
    assert v.__gt__(None) is NotImplemented

    # Rich comparison delegates through Version.__gt__, so the bool
    # of the reflected comparison must be handled by the other operand
    # (Python falls back / raises TypeError as appropriate).
    try:
        v > object()
        raised = False
    except TypeError:
        raised = True
    assert raised, "comparison with unsupported type should raise TypeError"

# Generated at 2026-10-25 10:38:37.151551
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:38:54.758236
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:38:57.336280
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 10:39:00.191886
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:39:02.620132
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 10:39:05.034627
# Unit test for method __str__ of class StrictVersion