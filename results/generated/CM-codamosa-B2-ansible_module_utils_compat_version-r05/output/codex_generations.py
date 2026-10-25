

# Generated at 2026-10-24 12:24:39.685985
# Unit test for method __str__ of class LooseVersion

# Generated at 2026-10-24 12:24:42.101799
# Unit test for method __str__ of class LooseVersion

# Generated at 2026-10-24 12:24:44.514000
# Unit test for method __str__ of class LooseVersion

# Generated at 2026-10-24 12:24:46.928140
# Unit test for constructor of class StrictVersion

# Generated at 2026-10-24 12:24:49.342403
# Unit test for constructor of class StrictVersion

# Generated at 2026-10-24 12:24:51.756236
# Unit test for constructor of class StrictVersion

# Generated at 2026-10-24 12:24:54.170593
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:24:56.583143
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:24:58.996143
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:25:01.410764
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-24 12:25:03.824079
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-24 12:25:20.336256
# Unit test for constructor of class LooseVersion
def test_LooseVersion():v = LooseVersion("1.5.2b2")
assert str(v) == "1.5.2b2"
assert v.version == [1, 5, 2, 'b', 2]
v2 = LooseVersion("3.4.1.6")
assert v2.version == [3, 4, 1, 6]
v3 = LooseVersion()
assert v3.version == []

# Generated at 2026-10-24 12:25:41.227267
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:25:43.643853
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:25:46.060495
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:25:48.473926
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 12:25:50.888905
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 12:25:53.301696
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 12:25:55.714754
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:25:58.127305
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:26:00.540881
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:26:02.954823
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:26:12.171353
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:26:16.061936
# Unit test for method __eq__ of class Version
def test_Version___eq__():from ansible.module_utils.compat.version import StrictVersion


# Generated at 2026-10-24 12:26:48.026964
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        """Concrete Version whose _cmp returns a preset value,
        so we can verify __le__ routes through _cmp correctly."""

        def __init__(self, cmp_result):
            self.cmp_result = cmp_result

        def _cmp(self, other):
            return self.cmp_result

    # _cmp == 0 (equal) -> True
    assert StubVersion(0) <= StubVersion(0) is True

    # _cmp < 0 (less than) -> True
    assert StubVersion(-1) <= StubVersion(0) is True

    # _cmp > 0 (greater than) -> False
    assert StubVersion(1) <= StubVersion(0) is False

    # __le__ delegates entirely to _cmp, even for non-Version operands
    assert StubVersion(-1) <= 'anything' is True

    # _cmp returns NotImplemented -> both sides decline,
    # Python falls back and raises TypeError
    with pytest.raises(TypeError):
        StubVersion(NotImplemented) <= StubVersion(0)

# Generated at 2026-10-24 12:26:50.442720
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:26:53.038213
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:26:55.462574
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:26:57.959813
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:00.384752
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:02.801717
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:05.212673
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:27:07.625824
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:27:22.210835
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():assert str(StrictVersion("1.2")) == "1.2"

# Generated at 2026-10-24 12:27:25.284701
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:41.806775
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:44.219383
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:46.632698
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:49.047097
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:51.462559
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:53.877556
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:27:56.291749
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:27:58.706782
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:28:01.131222
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:28:03.547943
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:28:05.964378
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:28:08.378077
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:28:10.791792
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:28:13.205116
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:28:15.619099
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:28:18.035616
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:28:20.446068
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:28:22.858054
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:25.275214
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:27.685170
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:30.103219
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:32.515521
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:34.928309
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:37.342857
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:39.755549
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:42.173891
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:44.589031
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:46.998760
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:49.412918
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:51.826273
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:28:54.240275
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:28:56.654885
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:28:59.066734
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:29:01.478849
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:29:03.892926
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:29:06.306533
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:29:08.719389
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:29:11.132755
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:29:13.549493
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:29:15.979875
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:29:18.422354
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:29:20.832750
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:23.245461
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:25.660086
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:28.072948
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:30.486167
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:32.899680
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:35.311607
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:29:37.724525
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:29:40.137409
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:29:42.550606
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:44.973629
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:47.378820
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:49.792734
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:52.205973
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:54.619140
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:57.034200
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:59.446428
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:30:01.860994
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:30:03.289820
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class NumericVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def _cmp(self, other):
            if not isinstance(other, NumericVersion):
                return NotImplemented
            return (self.vstring > other.vstring) - (self.vstring < other.vstring)

    v1 = NumericVersion('1.0')
    v2 = NumericVersion('2.0')
    v1_equal = NumericVersion('1.0')

    # greater-than: True
    assert (v2 > v1) is True

    # less-than: False
    assert (v1 > v2) is False

    # equal: False
    assert (v1 > v1_equal) is False

    # _cmp returning NotImplemented propagates, and Python
    # raises TypeError when the reflected op also fails
    with pytest.raises(TypeError):
        v1 > 'not-a-version'

# Generated at 2026-10-24 12:30:06.153692
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:30:07.500091
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:30:24.484977
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:30:25.814644
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from ansible.module_utils.compat.version import Version

    # Version is abstract (no _cmp/parse); use a minimal concrete subclass
    class SimpleVersion(Version):
        def parse(self, vstring):
            self.version = int(vstring)

        def _cmp(self, other):
            if isinstance(other, str):
                other = SimpleVersion(other)
            if not isinstance(other, SimpleVersion):
                return NotImplemented
            if self.version < other.version:
                return -1
            if self.version > other.version:
                return 1
            return 0

    v1 = SimpleVersion('1')
    v2 = SimpleVersion('2')
    v1_again = SimpleVersion('1')

    # greater-or-equal: equal values
    assert v1 >= v1_again is True

    # greater-or-equal: equal via string comparison
    assert (v1 >= '1') is True

    # greater-or-equal: greater value
    assert (v2 >= v1) is True
    assert (v2 >= '1') is True

    # not greater-or-equal: lesser value
    assert (v1 >= v2) is False
    assert (v1 >= '2') is False

    # NotImplemented propagates for incompatible types (no TypeError)
    assert v1.__ge__(object()) is NotImplemented
    assert (v1 >= object()) is False  # reflected op also fails -> False

# Generated at 2026-10-24 12:30:28.579741
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:30:30.099269
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:30:32.602598
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:30:35.101977
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:30:37.515667
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:30:40.061581
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:30:42.473185
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 12:30:44.886519
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 12:30:47.300879
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 12:30:49.713806
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:30:52.333250
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:30:54.747176
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:30:57.165936
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:30:59.575056
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:31:02.001085
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:31:04.412869
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:06.825016
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:09.238452
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:11.650025
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:14.066560
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:16.486927
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:18.895121
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:21.305967
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:48.150039
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:49.892058
# Unit test for method __le__ of class Version
def test_Version___le__():
    class StubVersion(Version):
        """Concrete Version whose _cmp returns a preset value,
        so we can verify __le__ routes through _cmp correctly."""

        def __init__(self, cmp_result):
            self.cmp_result = cmp_result

        def _cmp(self, other):
            return self.cmp_result

    # _cmp == 0 (equal) -> True
    assert StubVersion(0) <= StubVersion(0) is True

    # _cmp < 0 (less than) -> True
    assert StubVersion(-1) <= StubVersion(0) is True

    # _cmp > 0 (greater than) -> False
    assert StubVersion(1) <= StubVersion(0) is False

    # __le__ delegates entirely to _cmp, even for non-Version operands
    assert StubVersion(-1) <= 'anything' is True

    # _cmp returns NotImplemented -> both sides decline,
    # Python falls back and raises TypeError
    with pytest.raises(TypeError):
        StubVersion(NotImplemented) <= StubVersion(0)

# Generated at 2026-10-24 12:31:51.339682
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class NumericVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def _cmp(self, other):
            if not isinstance(other, NumericVersion):
                return NotImplemented
            return (self.vstring > other.vstring) - (self.vstring < other.vstring)

    v1 = NumericVersion('1.0')
    v2 = NumericVersion('2.0')
    v1_equal = NumericVersion('1.0')

    # greater-than: True
    assert (v2 > v1) is True

    # less-than: False
    assert (v1 > v2) is False

    # equal: False
    assert (v1 > v1_equal) is False

    # _cmp returning NotImplemented propagates, and Python
    # raises TypeError when the reflected op also fails
    with pytest.raises(TypeError):
        v1 > 'not-a-version'

# Generated at 2026-10-24 12:31:52.963670
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class NumericVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def _cmp(self, other):
            if not isinstance(other, NumericVersion):
                return NotImplemented
            return (self.vstring > other.vstring) - (self.vstring < other.vstring)

    v1 = NumericVersion('1.0')
    v2 = NumericVersion('2.0')
    v1_equal = NumericVersion('1.0')

    # greater-than: True
    assert (v2 > v1) is True

    # less-than: False
    assert (v1 > v2) is False

    # equal: False
    assert (v1 > v1_equal) is False

    # _cmp returning NotImplemented propagates, and Python
    # raises TypeError when the reflected op also fails
    with pytest.raises(TypeError):
        v1 > 'not-a-version'

# Generated at 2026-10-24 12:31:54.602366
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class NumericVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def _cmp(self, other):
            if not isinstance(other, NumericVersion):
                return NotImplemented
            return (self.vstring > other.vstring) - (self.vstring < other.vstring)

    v1 = NumericVersion('1.0')
    v2 = NumericVersion('2.0')
    v1_equal = NumericVersion('1.0')

    # greater-than: True
    assert (v2 > v1) is True

    # less-than: False
    assert (v1 > v2) is False

    # equal: False
    assert (v1 > v1_equal) is False

    # _cmp returning NotImplemented propagates, and Python
    # raises TypeError when the reflected op also fails
    with pytest.raises(TypeError):
        v1 > 'not-a-version'

# Generated at 2026-10-24 12:31:56.134700
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class NumericVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def _cmp(self, other):
            if not isinstance(other, NumericVersion):
                return NotImplemented
            return (self.vstring > other.vstring) - (self.vstring < other.vstring)

    v1 = NumericVersion('1.0')
    v2 = NumericVersion('2.0')
    v1_equal = NumericVersion('1.0')

    # greater-than: True
    assert (v2 > v1) is True

    # less-than: False
    assert (v1 > v2) is False

    # equal: False
    assert (v1 > v1_equal) is False

    # _cmp returning NotImplemented propagates, and Python
    # raises TypeError when the reflected op also fails
    with pytest.raises(TypeError):
        v1 > 'not-a-version'

# Generated at 2026-10-24 12:31:58.875855
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:32:15.377222
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:32:33.406833
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:32:34.727733
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from ansible.module_utils.compat.version import Version

    # Version is abstract (no _cmp/parse); use a minimal concrete subclass
    class SimpleVersion(Version):
        def parse(self, vstring):
            self.version = int(vstring)

        def _cmp(self, other):
            if isinstance(other, str):
                other = SimpleVersion(other)
            if not isinstance(other, SimpleVersion):
                return NotImplemented
            if self.version < other.version:
                return -1
            if self.version > other.version:
                return 1
            return 0

    v1 = SimpleVersion('1')
    v2 = SimpleVersion('2')
    v1_again = SimpleVersion('1')

    # greater-or-equal: equal values
    assert v1 >= v1_again is True

    # greater-or-equal: equal via string comparison
    assert (v1 >= '1') is True

    # greater-or-equal: greater value
    assert (v2 >= v1) is True
    assert (v2 >= '1') is True

    # not greater-or-equal: lesser value
    assert (v1 >= v2) is False
    assert (v1 >= '2') is False

    # NotImplemented propagates for incompatible types (no TypeError)
    assert v1.__ge__(object()) is NotImplemented
    assert (v1 >= object()) is False  # reflected op also fails -> False

# Generated at 2026-10-24 12:32:58.556124
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:32:59.891446
# Unit test for method __eq__ of class Version
def test_Version___eq__():from ansible.module_utils.compat.version import StrictVersion


# Generated at 2026-10-24 12:33:08.785972
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    test_cases = [
        ("1.5.1", [1, 5, 1]),
        ("1.5.2b2", [1, 5, 2, "b", 2]),
        ("8.02", [8, 2]),
        ("2g6", [2, "g", 6]),
        ("1.13++", [1, 13, "++"]),
        ("2.0b1pl0", [2, 0, "b", 1, "pl", 0]),
    ]

    version = LooseVersion()

    for vstring, expected in test_cases:
        version.parse(vstring)

        assert version.vstring == vstring
        assert version.version == expected
        assert str(version) == vstring

# Generated at 2026-10-24 12:33:10.135424
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from ansible.module_utils.compat.version import Version

    # Version is abstract (no _cmp/parse); use a minimal concrete subclass
    class SimpleVersion(Version):
        def parse(self, vstring):
            self.version = int(vstring)

        def _cmp(self, other):
            if isinstance(other, str):
                other = SimpleVersion(other)
            if not isinstance(other, SimpleVersion):
                return NotImplemented
            if self.version < other.version:
                return -1
            if self.version > other.version:
                return 1
            return 0

    v1 = SimpleVersion('1')
    v2 = SimpleVersion('2')
    v1_again = SimpleVersion('1')

    # greater-or-equal: equal values
    assert v1 >= v1_again is True

    # greater-or-equal: equal via string comparison
    assert (v1 >= '1') is True

    # greater-or-equal: greater value
    assert (v2 >= v1) is True
    assert (v2 >= '1') is True

    # not greater-or-equal: lesser value
    assert (v1 >= v2) is False
    assert (v1 >= '2') is False

    # NotImplemented propagates for incompatible types (no TypeError)
    assert v1.__ge__(object()) is NotImplemented
    assert (v1 >= object()) is False  # reflected op also fails -> False

# Generated at 2026-10-24 12:33:11.484977
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class NumericVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def _cmp(self, other):
            if not isinstance(other, NumericVersion):
                return NotImplemented
            return (self.vstring > other.vstring) - (self.vstring < other.vstring)

    v1 = NumericVersion('1.0')
    v2 = NumericVersion('2.0')
    v1_equal = NumericVersion('1.0')

    # greater-than: True
    assert (v2 > v1) is True

    # less-than: False
    assert (v1 > v2) is False

    # equal: False
    assert (v1 > v1_equal) is False

    # _cmp returning NotImplemented propagates, and Python
    # raises TypeError when the reflected op also fails
    with pytest.raises(TypeError):
        v1 > 'not-a-version'

# Generated at 2026-10-24 12:33:14.114410
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:33:16.725222
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:33:19.140768
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:33:23.868577
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:33:26.410740
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:33:27.774082
# Unit test for method __eq__ of class Version
def test_Version___eq__():from ansible.module_utils.compat.version import StrictVersion


# Generated at 2026-10-24 12:33:30.546483
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:33:51.232165
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:34:11.609013
# Unit test for method __lt__ of class Version
def test_Version___lt__():version = Version()

# Generated at 2026-10-24 12:34:14.027931
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:34:16.440682
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:34:18.855167
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:34:21.269529
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:34:23.684756
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:34:31.064674
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:34:32.379083
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from ansible.module_utils.compat.version import Version

    # Version is abstract (no _cmp/parse); use a minimal concrete subclass
    class SimpleVersion(Version):
        def parse(self, vstring):
            self.version = int(vstring)

        def _cmp(self, other):
            if isinstance(other, str):
                other = SimpleVersion(other)
            if not isinstance(other, SimpleVersion):
                return NotImplemented
            if self.version < other.version:
                return -1
            if self.version > other.version:
                return 1
            return 0

    v1 = SimpleVersion('1')
    v2 = SimpleVersion('2')
    v1_again = SimpleVersion('1')

    # greater-or-equal: equal values
    assert v1 >= v1_again is True

    # greater-or-equal: equal via string comparison
    assert (v1 >= '1') is True

    # greater-or-equal: greater value
    assert (v2 >= v1) is True
    assert (v2 >= '1') is True

    # not greater-or-equal: lesser value
    assert (v1 >= v2) is False
    assert (v1 >= '2') is False

    # NotImplemented propagates for incompatible types (no TypeError)
    assert v1.__ge__(object()) is NotImplemented
    assert (v1 >= object()) is False  # reflected op also fails -> False

# Generated at 2026-10-24 12:34:33.688944
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from ansible.module_utils.compat.version import Version

    # Version is abstract (no _cmp/parse); use a minimal concrete subclass
    class SimpleVersion(Version):
        def parse(self, vstring):
            self.version = int(vstring)

        def _cmp(self, other):
            if isinstance(other, str):
                other = SimpleVersion(other)
            if not isinstance(other, SimpleVersion):
                return NotImplemented
            if self.version < other.version:
                return -1
            if self.version > other.version:
                return 1
            return 0

    v1 = SimpleVersion('1')
    v2 = SimpleVersion('2')
    v1_again = SimpleVersion('1')

    # greater-or-equal: equal values
    assert v1 >= v1_again is True

    # greater-or-equal: equal via string comparison
    assert (v1 >= '1') is True

    # greater-or-equal: greater value
    assert (v2 >= v1) is True
    assert (v2 >= '1') is True

    # not greater-or-equal: lesser value
    assert (v1 >= v2) is False
    assert (v1 >= '2') is False

    # NotImplemented propagates for incompatible types (no TypeError)
    assert v1.__ge__(object()) is NotImplemented
    assert (v1 >= object()) is False  # reflected op also fails -> False

# Generated at 2026-10-24 12:34:36.353249
# Unit test for method __lt__ of class Version