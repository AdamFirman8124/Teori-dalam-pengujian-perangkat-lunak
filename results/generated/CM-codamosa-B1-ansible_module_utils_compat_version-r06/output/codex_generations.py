

# Generated at 2026-10-24 13:06:22.429461
# Unit test for constructor of class LooseVersion
def test_LooseVersion():
    # no string -> parse() not called
    v = LooseVersion()
    assert not hasattr(v, 'vstring')
    assert not hasattr(v, 'version')

    # empty string is falsy, same as None
    v = LooseVersion("")
    assert not hasattr(v, 'vstring')

    # numeric only
    v = LooseVersion("1.5.1")
    assert v.vstring == "1.5.1"
    assert v.version == [1, 5, 1]
    assert str(v) == "1.5.1"
    assert repr

# Generated at 2026-10-24 13:06:24.850296
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 13:06:27.268205
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 13:06:57.287391
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 13:07:16.438387
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 13:08:17.030189
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():v = LooseVersion()

# Generated at 2026-10-24 13:08:37.952883
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 13:09:05.903140
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 13:09:39.388115
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 13:10:32.943446
# Unit test for method __repr__ of class LooseVersion
def test_LooseVersion___repr__():
    # __repr__ is: "LooseVersion ('%s')" % str(self)
    # __str__ returns the original vstring
    test_versions = [
        "1.5.1",
        "1.5.2b2",
        "161",
        "3.10a",
        "8.02",
        "3.4j",
        "1996.07.12",
        "3.2.pl0",
        "2g6",
        "11g",
        "2.2beta29",
        "1.13++",
        "5.5.kw",
        "2.0b1pl0",
    ]

    for vs in test_versions:
        lv = LooseVersion(vs)
        expected = "LooseVersion ('%s')" % vs
        assert repr(lv) == expected, f"repr({vs!r}) = {repr(lv)!r}, expected {expected!r}"

        # repr should be valid Python to recreate the instance
        recreated = eval(repr(lv))
        assert isinstance(recreated, LooseVersion)
        assert str(recreated) == vs
        assert recreated.version == lv.version

# Generated at 2026-10-24 13:10:53.239814
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


# Generated at 2026-10-24 13:11:46.980541
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

# Generated at 2026-10-24 13:12:43.811075
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 13:12:45.758902
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 13:13:02.142271
# Unit test for constructor of class StrictVersion
def test_StrictVersion():
    # 1. two components -> patch defaults to 0
    v = StrictVersion('0.4')
    assert v.version == (0, 4, 0)
    assert v.prerelease is None

    # 2. three components, no prerelease
    v = StrictVersion('1.0.4')
    assert v.version == (1, 0, 4)
    assert v.prerelease is None

    # 3. with prerelease 'a' / 'b'
    v = StrictVersion('0.5a1')
    assert v.version == (0, 5, 0)
    assert v.prerelease == ('a', 1)

    v = StrictVersion('0.5b3')
    assert v.version == (0, 5, 0)
    assert v.prerelease == ('b', 3)

    v = StrictVersion('1.0.4a3')
    assert v.version == (1, 0, 4)
    assert v.prerelease == ('a', 3)

    v = StrictVersion('1.0.4b1')
    assert v.version == (1, 0, 4)
    assert v.prerelease == ('b', 1)

    # 4. 0.4 and 0.4.0 are equivalent
    assert StrictVersion('0.4').version == StrictVersion('0.4.0').version
    assert StrictVersion('0.4') == StrictVersion('0.4.0')

# Generated at 2026-10-24 13:13:20.573721
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class StubVersion(Version):
        def __init__(self, result):
            self._result = result
            self.seen = []
        def parse(self, vstring):
            pass
        def _cmp(self, other):
            self.seen.append(other)
            return self._result
    # _cmp < 0 -> True
    a = StubVersion(-1)
    assert (a < object()) is True
    assert a.__lt__(object()) is True
    assert a.seen[0] is not None
    # _cmp == 0 -> False
    b = StubVersion(0)
    assert (b < object()) is False
    # _cmp > 0 -> False
    c = StubVersion(1)
    assert (c < object()) is False
    # arbitrary magnitudes
    assert (StubVersion(-100) < object()) is True
    assert (StubVersion(100) < object()) is False
    # NotImplemented is propagated as-is
    d = StubVersion(NotImplemented)
    assert d.__lt__(object()) is NotImplemented
    assert (d < object()) is NotImplemented if False else d.__lt__(object()) is NotImplemented
    # other argument is forwarded to _cmp
    e = StubVersion(-1)
    sentinel = object()
    e.__lt__(sentinel)

# Generated at 2026-10-24 13:13:50.985752
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

# Generated at 2026-10-24 13:13:52.419550
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 13:13:53.853904
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 13:13:57.778166
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 13:14:23.481974
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 13:15:02.051317
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 13:15:21.062367
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 13:15:37.379797
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 13:15:38.812533
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 13:15:41.681198
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 13:15:43.028723
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 13:15:44.398748
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 13:15:58.376512
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    cases = [
        ("0.4", "0.4"),
        ("0.4.0", "0.4"),  # patch 0 is normalized away
        ("0.4.1", "0.4.1"),
        ("0.5", "0.5"),
        ("0.5a1", "0.5a1"),
        ("0.5b3", "0.5b3"),
        ("0.9.6", "0.9.6"),
        ("1.0", "1.0"),
        ("1.0.4a3", "1.0.4a3"),
        ("1.0.4b1", "1.0.4b1"),
        ("1.0.4", "1.0.4"),
        ("1.2.0b2", "1.2b2"),  # patch 0 normalized away, prerelease kept
        ("1.0a10", "1.0a10"),
        ("10.20.30", "10.20.30"),
    ]
    for vstring, expected in cases:
        assert str(StrictVersion(vstring)) == expected

# Generated at 2026-10-24 13:16:04.462539
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class StubVersion(Version):
        def __init__(self, result):
            self._result = result
            self.seen = []
        def parse(self, vstring):
            pass
        def _cmp(self, other):
            self.seen.append(other)
            return self._result
    # _cmp < 0 -> True
    a = StubVersion(-1)
    assert (a < object()) is True
    assert a.__lt__(object()) is True
    assert a.seen[0] is not None
    # _cmp == 0 -> False
    b = StubVersion(0)
    assert (b < object()) is False
    # _cmp > 0 -> False
    c = StubVersion(1)
    assert (c < object()) is False
    # arbitrary magnitudes
    assert (StubVersion(-100) < object()) is True
    assert (StubVersion(100) < object()) is False
    # NotImplemented is propagated as-is
    d = StubVersion(NotImplemented)
    assert d.__lt__(object()) is NotImplemented
    assert (d < object()) is NotImplemented if False else d.__lt__(object()) is NotImplemented
    # other argument is forwarded to _cmp
    e = StubVersion(-1)
    sentinel = object()
    e.__lt__(sentinel)