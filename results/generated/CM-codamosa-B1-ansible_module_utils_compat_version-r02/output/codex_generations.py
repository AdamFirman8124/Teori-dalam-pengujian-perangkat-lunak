

# Generated at 2026-10-25 06:40:08.420548
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 06:40:10.837638
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 06:40:13.253632
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 06:40:15.667217
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 06:40:18.085611
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 06:40:20.498252
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 06:40:22.916847
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:40:25.333643
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:40:27.746283
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:40:30.157777
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 06:40:32.573808
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 06:40:35.084073
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 06:40:37.502741
# Unit test for constructor of class StrictVersion

# Generated at 2026-10-25 06:40:39.919298
# Unit test for constructor of class StrictVersion

# Generated at 2026-10-25 06:40:42.333203
# Unit test for constructor of class StrictVersion

# Generated at 2026-10-25 06:40:44.752549
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 06:40:47.167163
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 06:40:49.580294
# Unit test for method __repr__ of class Version

# Generated at 2026-10-25 06:41:10.786035
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:41:30.650025
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:41:33.179660
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:41:35.593060
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 06:41:38.222622
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 06:41:40.687594
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 06:41:43.103119
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 06:41:45.514284
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 06:41:47.926668
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 06:41:50.342234
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:41:52.756168
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:41:55.173505
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:41:57.586555
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:42:00.005677
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:42:02.418538
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:42:04.831265
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:42:07.256809
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:42:09.663078
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:42:26.665193
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

# Generated at 2026-10-25 06:42:42.927793
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 06:42:45.343010
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 06:42:47.936208
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-25 06:42:50.354280
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 06:42:52.770679
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 06:42:55.185019
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 06:42:57.599407
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:43:00.011984
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:43:02.424481
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:43:04.840176
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:43:07.258502
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:43:09.672661
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:43:12.090082
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 06:43:14.505693
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 06:43:16.920759
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 06:43:19.339065
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 06:43:21.757439
# Unit test for method __lt__ of class Version

# Generated at 2026-10-25 06:43:26.811211
# Unit test for method __lt__ of class Version
def test_Version___lt__():v1 = LooseVersion("1.0")
v2 = LooseVersion("1.1")
v3 = LooseVersion("1.0")
assert (v1 < v2) is True
assert (v2 < v1) is False
assert (v1 < v3) is False
assert (v1 < "2.0") is True
assert (StrictVersion("1.0.0") < StrictVersion("1.0.1")) is True

# Generated at 2026-10-25 06:43:59.847310
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

# Generated at 2026-10-25 06:44:02.265825
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 06:44:04.684314
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 06:44:07.272869
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-25 06:44:09.687226
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 06:44:12.102727
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 06:44:14.530620
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-25 06:44:16.945284
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:44:19.362328
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:44:21.844313
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:44:24.261648
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:44:26.678535
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:44:29.159547
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:44:31.577826
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:44:33.993423
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:44:36.409044
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:44:38.826336
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:44:41.242778
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:44:43.682011
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:44:46.097283
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:44:59.036276
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:45:00.474744
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:45:01.903604
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

# Generated at 2026-10-25 06:45:03.255587
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

# Generated at 2026-10-25 06:45:04.593045
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

# Generated at 2026-10-25 06:45:05.925530
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

# Generated at 2026-10-25 06:45:08.480003
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:45:10.898255
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:45:13.314963
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:45:16.026579
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:45:18.445050
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:45:20.856959
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:45:23.272274
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:25.716191
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:28.497526
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:30.910151
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:33.325597
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:35.742107
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:38.161379
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:40.754453
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:43.173638
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:45.588262
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:45:48.011070
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:45:50.422396
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:45:52.838651
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:45:55.254187
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:46:10.919335
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:46:12.361938
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

# Generated at 2026-10-25 06:46:13.683230
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

# Generated at 2026-10-25 06:46:15.119404
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

# Generated at 2026-10-25 06:46:16.632828
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

# Generated at 2026-10-25 06:46:45.897793
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:46:48.312342
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:46:50.728961
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:46:53.142475
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:46:55.560128
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:46:57.975995
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:47:00.651512
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

# Generated at 2026-10-25 06:47:02.530615
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

# Generated at 2026-10-25 06:47:04.170363
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

# Generated at 2026-10-25 06:47:05.604231
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

# Generated at 2026-10-25 06:47:07.142907
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

# Generated at 2026-10-25 06:47:08.572985
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

# Generated at 2026-10-25 06:47:10.114725
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

# Generated at 2026-10-25 06:47:13.079027
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

# Generated at 2026-10-25 06:47:14.512822
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

# Generated at 2026-10-25 06:47:15.876737
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

# Generated at 2026-10-25 06:47:17.267359
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

# Generated at 2026-10-25 06:47:35.078114
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 06:47:37.495276
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 06:47:39.910151
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-25 06:47:42.327214
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:47:44.738845
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:47:47.152610
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:47:49.564692
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:47:51.977353
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:47:54.393830
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:47:56.809693
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:47:59.226250
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:48:01.637686
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:48:04.058370
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:48:06.474542
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:48:08.891180
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:48:11.308307
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:48:13.726129
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:48:16.137365
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:48:18.558047
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:48:20.969621
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:48:23.387105
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:48:25.806392
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:48:28.221415
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:48:30.633907
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:48:33.055358
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:48:35.471389
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:48:37.886354
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:48:40.303994
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:48:42.718091
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:48:45.134894
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:48:51.893664
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:48:54.307820
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:48:56.725040
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:48:59.139177
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:49:01.557575
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:49:03.973316
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:49:06.386773
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:49:08.803818
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:49:11.220457
# Unit test for method __le__ of class Version

# Generated at 2026-10-25 06:49:13.634159
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:49:16.069093
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:49:18.485294
# Unit test for method __ge__ of class Version

# Generated at 2026-10-25 06:49:20.899799
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:49:23.316818
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:49:25.732783
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:49:28.147942
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:49:30.565559
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:49:32.980963
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:49:35.393727
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:49:37.809955
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:49:40.225189
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:49:42.639751
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:49:45.056175
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:49:47.472826
# Unit test for method __gt__ of class Version

# Generated at 2026-10-25 06:49:49.887454
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:49:52.305132
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:49:54.721300
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:49:57.137186
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:49:59.552700
# Unit test for method __eq__ of class Version

# Generated at 2026-10-25 06:50:01.967154
# Unit test for method __eq__ of class Version