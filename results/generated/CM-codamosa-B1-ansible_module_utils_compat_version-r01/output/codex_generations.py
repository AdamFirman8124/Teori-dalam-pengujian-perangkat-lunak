

# Generated at 2026-10-24 21:34:09.284241
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

# Generated at 2026-10-24 21:34:19.611954
# Unit test for constructor of class Version
def test_Version():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.parse_called_with = vstring

    # 1. No argument: parse must not be called
    v = DummyVersion()
    assert getattr(v, 'parse_called_with', None) is None

    # 2. None: parse must not be called
    v = DummyVersion(None)
    assert getattr(v, 'parse_called_with', None) is None

    # 3. Empty string is falsy: parse must not be called
    #    because constructor is `if vstring: self.parse(vstring)`
    v = DummyVersion('')
    assert getattr(v, 'parse_called_with', None) is None

    # 4. String argument: must be passed to parse
    v = DummyVersion('1.0')
    assert v.parse_called_with == '1.0'

# Generated at 2026-10-24 21:34:27.008350
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

    for comparison_result, expected in (
        (-1, True),
        (0, True),
        (1, False),
    ):
        version = TestVersion(comparison_result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-24 21:34:34.740096
# Unit test for method __repr__ of class Version
def test_Version___repr__():
    class MockVersion(Version):
        """Minimal concrete subclass -- Version itself is abstract (no parse/_cmp)."""
        def parse(self, vstring):
            self.vstring = vstring
        def __str__(self):
            return self.vstring
        def _cmp(self, other):
            return 0

    v = MockVersion("1.2.3")
    assert v.__repr__() == "MockVersion ('1.2.3')"
    assert repr(v) == v.__repr__()          # repr() delegates to __repr__
    assert v.__class__.__name__ in v.__repr__()  # class name is embedded
    assert "'1.2.3'" in v.__repr__()        # str(self) is embedded, quoted

# Generated at 2026-10-24 21:34:42.049589
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

    for comparison_result, expected in ((-1, True), (0, True), (1, False)):
        version = TestVersion(comparison_result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-24 21:34:56.220253
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

# Generated at 2026-10-24 21:35:05.402815
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    test_cases = [
        ("1.5.1", [1, 5, 1]),
        ("1.5.2b2", [1, 5, 2, "b", 2]),
        ("161", [161]),
        ("3.10a", [3, 10, "a"]),
        ("8.02", [8, 2]),
        ("3.4j", [3, 4, "j"]),
        ("1996.07.12", [1996, 7, 12]),
        ("3.2.pl0", [3, 2, "pl", 0]),
        ("3.1.1.6", [3, 1, 1, 6]),
        ("2g6", [2, "g", 6]),
        ("11g", [11, "g"]),
        ("0.960923", [0, 960923]),
        ("2.2beta29", [2, 2, "beta", 29]),
        ("1.13++", [1, 13, "++"]),
        ("5.5.kw", [5, 5, "kw"]),
        ("2.0b1pl0", [2, 0, "b", 1, "pl", 0]),
    ]

    version = LooseVersion()

    for vstring, expected_components in test_cases:
        version.parse(vstring)

        assert version.vstring == vstring
        assert version.version == expected_components
        assert str(version) == vstring

# Generated at 2026-10-24 21:35:13.486634
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

# Generated at 2026-10-24 21:35:27.617126
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:35:30.149960
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:35:32.573001
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:35:34.986904
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:35:37.531643
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:35:39.946064
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:35:42.364024
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 21:35:44.780345
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 21:35:47.201078
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 21:35:49.622624
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:35:52.040136
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:35:54.469686
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:35:56.888383
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:35:59.303653
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:36:01.719490
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:36:04.139611
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 21:36:06.555014
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 21:36:08.974153
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 21:36:11.395442
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 21:36:13.814356
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 21:36:16.230044
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 21:36:18.646742
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:36:21.063962
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:36:23.482218
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:36:32.005277
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

        assert version.__le__(other) is expected
        assert version.compared_with is other

# Generated at 2026-10-24 21:36:40.222064
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

    for comparison_result, expected in (
        (-1, True),
        (0, True),
        (1, False),
        (NotImplemented, NotImplemented),
    ):
        version = ComparableVersion(comparison_result)

        assert version.__le__(other) is expected
        assert version.compared_with is other

# Generated at 2026-10-24 21:36:48.515669
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    import pytest

    valid_versions = [
        ("0.4", (0, 4, 0), None, "0.4"),
        ("0.4.0", (0, 4, 0), None, "0.4"),
        ("1.2.3", (1, 2, 3), None, "1.2.3"),
        ("0.5a1", (0, 5, 0), ("a", 1), "0.5a1"),
        ("0.5b3", (0, 5, 0), ("b", 3), "0.5b3"),
        ("1.0.4a3", (1, 0, 4), ("a", 3), "1.0.4a3"),
    ]

    for value, expected_version, expected_prerelease, expected_string in valid_versions:
        version = StrictVersion()
        version.parse(value)

        assert version.version == expected_version
        assert version.prerelease == expected_prerelease
        assert str(version) == expected_string

    invalid_versions = [
        "",
        "1",
        "2.7.2.2",
        "1.3.a4",
        "1.3pl1",
        "1.3c4",
        "1.2rc1",
        "v1.2",
    ]

    for value in invalid_versions:
        with pytest.raises(ValueError, match="invalid version number"):
            StrictVersion().parse(value)

# Generated at 2026-10-24 21:36:57.116619
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

    for comparison_result, expected in (
        (-1, True),
        (0, False),
        (1, False),
        (NotImplemented, NotImplemented),
    ):
        version = StubVersion(comparison_result)
        result = version.__lt__(other)

        assert result is expected
        assert version.compared_with is other

# Generated at 2026-10-24 21:37:03.464889
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, other):
            return self.comparison_result

    other = object()

    assert Version.__le__(StubVersion(-1), other) is True
    assert Version.__le__(StubVersion(0), other) is True
    assert Version.__le__(StubVersion(1), other) is False
    assert Version.__le__(StubVersion(NotImplemented), other) is NotImplemented

# Generated at 2026-10-24 21:37:05.993440
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:37:08.411834
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:37:10.831183
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:37:13.248750
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:37:15.668646
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:37:18.087339
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:37:20.505883
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:37:22.922871
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:37:25.343345
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:37:27.766589
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 21:37:30.200903
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 21:37:32.775262
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():assert str(StrictVersion("0.4")) == "0.4"

# Generated at 2026-10-24 21:37:39.922620
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

    for comparison_result, expected in [
        (-1, True),
        (0, True),
        (1, False),
    ]:
        version = TestVersion(comparison_result)
        assert version.__le__(other) is expected
        assert version.compared_with is other

    version = TestVersion(NotImplemented)
    assert version.__le__(other) is NotImplemented
    assert version.compared_with is other

# Generated at 2026-10-24 21:37:41.272006
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

# Generated at 2026-10-24 21:37:42.598975
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    # patch == 0 collapses to "major.minor"
    assert str(StrictVersion("1.2")) == "1.2"
    assert str(StrictVersion("1.2.0")) == "1.2"   # trailing .0 is dropped

    # patch != 0 keeps all three components
    assert str(StrictVersion("1.2.3")) == "1.2.3"
    assert str(StrictVersion("0.9.6")) == "0.9.6"

    # prerelease tag is appended (letter + number)
    assert str(StrictVersion("1.0.4a3")) == "1.0.4a3"
    assert str(StrictVersion("2.0b2")) == "2.0b2"        # patch 0 -> "2.0" + "b2"
    assert str(StrictVersion("1.2.0a1")) == "1.2a1"      # .0 dropped even with prerelease

    # round-trip: str output re-parses to an equal version
    for s in ("0.4", "0.4.0", "0.5a1", "1.0", "1.0.4b1", "2.7.13"):
        v = StrictVersion(s)
        assert StrictVersion(str(v)) == v

# Generated at 2026-10-24 21:37:51.188021
# Unit test for method __le__ of class Version
def test_Version___le__():
    other = object()

    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, value):
            assert value is other
            return self.comparison_result

    assert TestVersion(-1).__le__(other) is True
    assert TestVersion(0).__le__(other) is True
    assert TestVersion(1).__le__(other) is False
    assert TestVersion(NotImplemented).__le__(other) is NotImplemented

# Generated at 2026-10-24 21:37:53.902740
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:37:56.446194
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:37:58.866647
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:38:01.282730
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 21:38:03.703274
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 21:38:06.299904
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 21:38:08.718230
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:38:11.140354
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:38:13.551996
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:38:15.969621
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:38:18.390268
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:38:20.812194
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:38:23.230351
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:38:25.659781
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:38:28.077406
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:38:30.495254
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:38:32.913176
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:38:35.332358
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:38:37.753436
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:38:40.171284
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:38:42.589820
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:38:45.007928
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:38:47.425783
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:38:49.842301
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:38:52.261964
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:38:54.677250
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:38:57.094510
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:38:59.511249
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:39:01.929187
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:39:04.347729
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:39:06.765110
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:39:17.491309
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:39:31.638104
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:39:32.960723
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

# Generated at 2026-10-24 21:39:35.481695
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:39:37.998872
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:39:40.415028
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:39:42.834636
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:39:45.253630
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:39:47.671738
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:39:50.086479
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:39:52.502885
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:39:54.920254
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:39:57.335367
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:39:59.752533
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:40:02.166577
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:40:04.581696
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:40:06.999613
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:40:09.418747
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:40:25.551048
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:40:33.896153
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:40:36.430123
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:40:38.848732
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:40:41.264456
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:40:43.680096
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:40:46.221900
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:40:48.637376
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:40:51.060091
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:40:53.474192
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:40:55.892449
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:40:58.320349
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:41:00.737834
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:41:03.155672
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:41:05.574435
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:41:07.991864
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:41:10.408774
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:41:12.824092
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:41:15.239165
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:41:17.655259
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:41:20.071665
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:41:22.487316
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:41:24.905497
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:41:26.290140
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:41:32.982869
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

    less = TestVersion(-1)
    assert less.__le__(other) is True
    assert less.compared_with is other

    equal = TestVersion(0)
    assert equal.__le__(other) is True

    greater = TestVersion(1)
    assert greater.__le__(other) is False

    unsupported = TestVersion(NotImplemented)
    assert unsupported.__le__(other) is NotImplemented

# Generated at 2026-10-24 21:41:39.536280
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, other):
            return self.comparison_result

    other = object()

    assert TestVersion(-1).__lt__(other) is True
    assert TestVersion(0).__lt__(other) is False
    assert TestVersion(1).__lt__(other) is False
    assert TestVersion(NotImplemented).__lt__(other) is NotImplemented

# Generated at 2026-10-24 21:41:46.911312
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

# Generated at 2026-10-24 21:42:02.678130
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:42:05.099618
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:42:07.518488
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 21:42:09.932775
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:42:12.352529
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:42:14.769336
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:42:17.187890
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:42:19.603453
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:42:22.020680
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:42:24.438154
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:42:25.797935
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:42:28.139479
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:42:37.788297
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class TestVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result
            self.compared_with = None

        def _cmp(self, other):
            self.compared_with = other
            return self.comparison_result

    other = object()

    version = TestVersion(-1)
    assert version.__lt__(other) is True
    assert version.compared_with is other

    version = TestVersion(0)
    assert version.__lt__(other) is False

    version = TestVersion(1)
    assert version.__lt__(other) is False

    version = TestVersion(NotImplemented)
    assert version.__lt__(other) is NotImplemented

# Generated at 2026-10-24 21:42:39.105712
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

# Generated at 2026-10-24 21:42:47.735189
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class StubVersion(Version):
        def __init__(self, comparison_result):
            self.comparison_result = comparison_result

        def _cmp(self, other):
            return self.comparison_result

    other = object()

    assert StubVersion(-1).__lt__(other) is True
    assert StubVersion(0).__lt__(other) is False
    assert StubVersion(1).__lt__(other) is False
    assert StubVersion(NotImplemented).__lt__(other) is NotImplemented

# Generated at 2026-10-24 21:42:55.651909
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    version = LooseVersion()
    version.parse("1.5.2b2")

    assert version.vstring == "1.5.2b2"
    assert version.version == [1, 5, 2, "b", 2]
    assert str(version) == "1.5.2b2"

# Generated at 2026-10-24 21:42:58.316815
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:43:00.734431
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:43:03.274447
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:43:05.693232
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:43:08.109684
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:43:10.526789
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:43:12.942146
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:43:15.360268
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:43:17.777903
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:43:20.193231
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:43:22.610621
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:43:25.030866
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:43:27.447198
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:43:29.867516
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:43:32.288145
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 21:43:34.710266
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:43:37.125278
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:43:39.541141
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:43:41.956487
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:43:44.371902
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:43:46.787305
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 21:43:49.204299
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:43:51.621085
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:43:54.040253
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 21:43:56.457177
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 21:44:05.457087
# Unit test for method __lt__ of class Version
def test_Version___lt__():v_low = Version()