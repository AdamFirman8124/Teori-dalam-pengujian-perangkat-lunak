

# Generated at 2026-10-25 09:00:52.975339
# Unit test for method __str__ of class LooseVersion
def test_LooseVersion___str__():
    version_string = "2.0b1pl0"
    version = LooseVersion(version_string)

    assert str(version) == version_string

# Generated at 2026-10-25 09:01:11.111242
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 09:01:28.928978
# Unit test for constructor of class LooseVersion
def test_LooseVersion():v = LooseVersion("1.5.1")

# Generated at 2026-10-25 09:01:31.460555
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 09:01:33.877891
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 09:01:36.296093
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 09:01:38.843027
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 09:01:41.260950
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 09:01:52.582403
# Unit test for method __repr__ of class Version
def test_Version___repr__():from ansible.module_utils.compat.version import LooseVersion


# Generated at 2026-10-25 09:01:54.121138
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

# Generated at 2026-10-25 09:02:09.245391
# Unit test for method __le__ of class Version
def test_Version___le__():
    class TestVersion(Version):
        def __init__(self, value):
            self.value = value

        def _cmp(self, other):
            if not isinstance(other, TestVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    lower = TestVersion(1)
    equal = TestVersion(1)
    higher = TestVersion(2)

    assert lower <= higher
    assert lower <= equal
    assert not higher <= lower

    # Verify that __le__ preserves NotImplemented for unsupported types.
    assert Version.__le__(lower, object()) is NotImplemented

# Generated at 2026-10-25 09:02:12.455658
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

# Generated at 2026-10-25 09:02:42.349828
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    # two components, patch defaults to 0 and is omitted
    assert str(StrictVersion('0.4')) == '0.4'
    assert str(StrictVersion('1.0')) == '1.0'

    # three components with patch == 0 normalizes to two components
    assert str(StrictVersion('0.4.0')) == '0.4'
    assert str(StrictVersion('1.0.0')) == '1.0'

    # three components with patch != 0 is preserved
    assert str(StrictVersion('0.4.1')) == '0.4.1'
    assert str(StrictVersion('0.9.6')) == '0.9.6'
    assert str(StrictVersion('1.0.4')) == '1.0.4'

    # pre-release on x.y -> x.yaN / x.ybN
    assert str(StrictVersion('0.5a1')) == '0.5a1'
    assert str(StrictVersion('0.5b3')) == '0.5b3'

    # pre-release on x.y.z -> x.y.zaN / x.y.zbN
    assert str(StrictVersion('1.0.4a3')) == '1.0.4a3'
    assert str(StrictVersion('1.0.4b1')) == '1.0.4b1'

    # str is round-trip stable: str(parse(s)) re-parses to equal version
    for s in ['0.4', '0.4.0', '0.4.1', '0.5a1', '0.5b3', '0.5', '1.0.4a3', '1.0.4b1', '1.0.4']:
        assert str(StrictVersion(str(StrictVersion(s)))) == str(StrictVersion(s))

# Generated at 2026-10-25 09:03:05.596550
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Version.__lt__ routes through _cmp; exercise it via the concrete
    # subclasses StrictVersion and LooseVersion, plus the NotImplemented
    # path when compared against an incompatible type.

    # --- StrictVersion: less-than cases ---
    assert StrictVersion("1.0") < StrictVersion("1.1")
    assert StrictVersion("1.0") < StrictVersion("2.0")
    assert StrictVersion("1.0.0") < StrictVersion("1.0.1")
    assert StrictVersion("1.0a1") < StrictVersion("1.0")
    assert StrictVersion("1.0a1") < StrictVersion("1.0b1")
    assert StrictVersion("1.0a1") < StrictVersion("1.0a2")
    assert StrictVersion("1.0a1") < StrictVersion("1.0rc1")
    assert StrictVersion("1.0rc1") < StrictVersion("1.0")
    assert StrictVersion("0.9") < StrictVersion("1.0")

    # --- StrictVersion: not-less-than cases ---
    assert not (StrictVersion("1.1") < StrictVersion("1.0"))
    assert not (StrictVersion("1.0") < StrictVersion("1.0"))
    assert not (StrictVersion("1.0") < StrictVersion("1.0a1"))

    # --- StrictVersion: comparison against plain strings ---
    assert StrictVersion("1.0") < "1.1"
    assert not (StrictVersion("1.1") < "1.0")
    assert not (StrictVersion("1.0") < "1.0")

    # --- StrictVersion: incompatible type returns NotImplemented ---
    result = StrictVersion("1.0").__lt__(object())
    assert result is NotImplemented

    # --- LooseVersion: less-than cases (numeric tuple comparison) ---
    assert LooseVersion("1.0") < LooseVersion("1.1")
    assert LooseVersion("1.0") < LooseVersion("1.0.1")
    assert LooseVersion("1.0") < LooseVersion("2.0")
    assert LooseVersion("1") < LooseVersion("1.0")
    assert LooseVersion("1.0a") < LooseVersion("1.0b")

    # --- LooseVersion: not-less-than cases ---
    assert not (LooseVersion("1.1") < LooseVersion("1.0"))
    assert not (LooseVersion("1.0") < LooseVersion("1.0"))
    assert not (LooseVersion("1.0.1") < LooseVersion("1.0"))

    # --- LooseVersion: comparison against plain strings ---
    assert LooseVersion("1.0") < "1.1"
    assert not (LooseVersion("1.1") < "1.0")

    # --- LooseVersion: incompatible type returns NotImplemented ---
    result = LooseVersion("1.0").__lt__(object())
    assert result is NotImplemented

    # --- Rich comparison operators must be consistently routed ---
    assert (StrictVersion("1.0") <= "1.0")
    assert (StrictVersion("1.0") < StrictVersion("1.0.1"))

# Generated at 2026-10-25 09:03:19.910591
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, other):
            return self.comparison_result

    other = object()

    # Less than: -1 <= 0
    assert StubVersion(-1).__le__(other) is True

    # Equal to: 0 <= 0
    assert StubVersion(0).__le__(other) is True

    # Greater than: 1 <= 0
    assert StubVersion(1).__le__(other) is False

    # __le__ must propagate NotImplemented unchanged
    assert StubVersion(NotImplemented).__le__(other) is NotImplemented

# Generated at 2026-10-25 09:03:21.469413
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

# Generated at 2026-10-25 09:03:23.995374
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:03:26.414246
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:03:28.832294
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:03:31.250626
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 09:03:33.906521
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 09:03:36.521274
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 09:03:38.936753
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:03:41.354356
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:03:43.770442
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:03:56.692676
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

# Generated at 2026-10-25 09:03:58.128313
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

# Generated at 2026-10-25 09:04:01.409257
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

# Generated at 2026-10-25 09:04:02.726635
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

# Generated at 2026-10-25 09:04:19.291302
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

# Generated at 2026-10-25 09:04:21.709538
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:04:24.128058
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:04:26.544513
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:04:28.959010
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:04:31.408675
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:04:34.019498
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:04:36.437640
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:04:38.853790
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:04:41.270212
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:04:43.687128
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:04:46.106301
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:04:48.524322
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:04:50.938677
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:04:53.354051
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:04:55.773774
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:04:58.192760
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:05:00.611207
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:05:03.026756
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:05:05.440484
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 09:05:07.857140
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 09:05:10.274044
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 09:05:12.692007
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:05:15.106632
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:05:17.524134
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:05:19.945943
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:05:22.361977
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:05:24.778284
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:05:27.195983
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:05:29.610846
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:05:32.028729
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:05:34.445359
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:05:36.863616
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:05:39.282160
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:05:41.697796
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:05:44.118500
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:05:46.535826
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:05:48.953220
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:05:51.366608
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:05:53.782035
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:05:56.197606
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:05:58.618415
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:06:01.033463
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:06:03.448645
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 09:06:05.869016
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 09:06:08.286789
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 09:06:10.704894
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:06:13.123533
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:06:15.539124
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 09:06:20.111840
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:06:22.529202
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:06:24.945483
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:06:27.362558
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:06:29.780792
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:06:32.197499
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:06:34.613827
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:06:37.030438
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:06:39.446155
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:06:41.942787
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:06:44.360343
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:06:46.779724
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:06:49.197284
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:06:51.615095
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:06:54.033526
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:06:56.451211
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:06:58.873945
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:01.291908
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:03.707908
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:07:06.129489
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:07:08.545186
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:07:10.965344
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:13.381564
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:15.799115
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:18.216368
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:07:20.635119
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:07:23.052044
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:07:25.468561
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:27.884346
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:30.300927
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:33.502755
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:35.922913
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:38.337158
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:07:40.754987
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:07:43.179134
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:07:57.682808
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:07:59.025284
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

# Generated at 2026-10-25 09:08:00.474924
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

# Generated at 2026-10-25 09:08:04.611745
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

# Generated at 2026-10-25 09:08:07.680244
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:08:22.433707
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:08:29.185994
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:08:31.849136
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:08:34.505521
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:08:36.924605
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:08:39.340043
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:08:41.755651
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:08:44.176440
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:08:46.592861
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:08:49.010899
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:08:51.430126
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 09:08:53.876821
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:08:56.289261
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:08:58.714981
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:09:08.115726
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 09:09:10.533154
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 09:09:12.948457
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 09:09:22.440346
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:09:27.245883
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:09:28.983029
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 09:09:30.416259
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

# Generated at 2026-10-25 09:09:31.879032
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

# Generated at 2026-10-25 09:09:34.851108
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:09:51.714745
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:10:01.343595
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:10:02.776088
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

# Generated at 2026-10-25 09:10:04.148492
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

# Generated at 2026-10-25 09:10:06.974382
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:10:08.510676
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:10:25.201596
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 09:10:28.376340
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

# Generated at 2026-10-25 09:10:29.912159
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

# Generated at 2026-10-25 09:10:38.440139
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

# Generated at 2026-10-25 09:10:39.770262
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

# Generated at 2026-10-25 09:10:41.278809
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

# Generated at 2026-10-25 09:10:42.612057
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

# Generated at 2026-10-25 09:10:44.013329
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