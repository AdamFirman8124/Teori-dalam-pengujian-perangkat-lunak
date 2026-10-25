

# Generated at 2026-10-24 12:21:29.860516
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-24 12:21:32.278661
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-24 12:21:34.699565
# Unit test for constructor of class LooseVersion

# Generated at 2026-10-24 12:21:37.124418
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 12:21:39.540624
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 12:21:41.961401
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 12:21:44.378829
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:22:11.023416
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:22:27.401675
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:22:30.069272
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:22:32.488970
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:22:35.081766
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:22:37.599380
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:22:40.027205
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:22:42.530614
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:22:45.039407
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:22:47.458200
# Unit test for method __str__ of class StrictVersion

# Generated at 2026-10-24 12:22:55.331383
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert str(StrictVersion("0.4")) == "0.4"
    assert str(StrictVersion("0.4.0")) == "0.4"
    assert str(StrictVersion("0.4.1")) == "0.4.1"
    assert str(StrictVersion("0.9.6")) == "0.9.6"
    assert str(StrictVersion("1.0")) == "1.0"
    assert str(StrictVersion("1.0.4")) == "1.0.4"
    assert str(StrictVersion("0.5a1")) == "0.5a1"
    assert str(StrictVersion("0.5b3")) == "0.5b3"
    assert str(StrictVersion("1.0.4a3")) == "1.0.4a3"
    assert str(StrictVersion("1.0.4b1")) == "1.0.4b1"
    v = StrictVersion("1.0.4b1")
    assert str(v) == "1.0.4b1"
    assert repr(v) == "StrictVersion ('1.0.4b1')"
    assert str(StrictVersion(str(StrictVersion("2.7.18a2")))) == "2.7.18a2"

# Generated at 2026-10-24 12:23:06.723979
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

# Generated at 2026-10-24 12:23:14.432259
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 12:23:26.282482
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():import unittest

# Generated at 2026-10-24 12:23:28.700606
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:23:31.405910
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:23:33.820329
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:23:36.236569
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:23:38.653840
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:23:41.208671
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:23:43.620160
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:23:46.034429
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:23:48.447262
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:23:50.861654
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:23:53.273937
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:23:55.686536
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:24:03.894879
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

# Generated at 2026-10-24 12:24:05.216598
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

# Generated at 2026-10-24 12:25:04.452482
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class ComparableVersion(Version):
        def __init__(self, value=None):
            super(ComparableVersion, self).__init__()
            self.value = value

        def parse(self, vstring):
            self.value = vstring

        def _cmp(self, other):
            if not isinstance(other, ComparableVersion):
                return NotImplemented
            if self.value == other.value:
                return 0
            return -1 if self.value < other.value else 1

    # equal instances compare equal
    assert ComparableVersion('1.0') == ComparableVersion('1.0')

    # unequal instances do not compare equal
    assert not (ComparableVersion('1.0') == ComparableVersion('2.0'))

    # comparison with an unsupported type returns NotImplemented from _cmp,
    # so __eq__ must propagate it (Python then falls back to identity check)
    assert not (ComparableVersion('1.0') == '1.0')

    # __eq__ returns NotImplemented itself when _cmp returns NotImplemented
    class NotImplementedVersion(Version):
        def parse(self, vstring):
            pass

        def _cmp(self, other):
            return NotImplemented

    assert NotImplementedVersion().__eq__(NotImplementedVersion()) is NotImplemented

# Generated at 2026-10-24 12:25:44.194806
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:25:46.703853
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:25:49.117861
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:25:51.532624
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:25:53.947936
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:25:56.448039
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:25:58.862427
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:26:01.274419
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:26:03.686598
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:26:05.106048
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

# Generated at 2026-10-24 12:26:46.984905
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:26:49.509380
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:26:51.921392
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:26:54.346020
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:26:56.759475
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:26:59.184519
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:27:01.596100
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:04.008670
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:06.420965
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:08.996243
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:10.405068
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:27.016001
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:29.778685
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class ComparableVersion(Version):
        def __init__(self, value=None):
            super(ComparableVersion, self).__init__()
            self.value = value

        def parse(self, vstring):
            self.value = vstring

        def _cmp(self, other):
            if not isinstance(other, ComparableVersion):
                return NotImplemented
            if self.value == other.value:
                return 0
            return -1 if self.value < other.value else 1

    # equal instances compare equal
    assert ComparableVersion('1.0') == ComparableVersion('1.0')

    # unequal instances do not compare equal
    assert not (ComparableVersion('1.0') == ComparableVersion('2.0'))

    # comparison with an unsupported type returns NotImplemented from _cmp,
    # so __eq__ must propagate it (Python then falls back to identity check)
    assert not (ComparableVersion('1.0') == '1.0')

    # __eq__ returns NotImplemented itself when _cmp returns NotImplemented
    class NotImplementedVersion(Version):
        def parse(self, vstring):
            pass

        def _cmp(self, other):
            return NotImplemented

    assert NotImplementedVersion().__eq__(NotImplementedVersion()) is NotImplemented

# Generated at 2026-10-24 12:27:31.106068
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

# Generated at 2026-10-24 12:27:33.859626
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:36.366060
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:38.935802
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:41.347956
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:27:43.904172
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:27:46.317665
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:27:48.730284
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:51.145584
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:53.704157
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:27:56.116907
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:27:58.532444
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:00.948579
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:03.364825
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:05.780688
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:08.194822
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:10.608605
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:28:13.022083
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:28:15.435569
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:28:17.847723
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:20.259990
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:22.670723
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:25.081351
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:28:27.493290
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:28:29.906347
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:28:32.320443
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:28:34.733551
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:28:37.147477
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:28:39.560249
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:41.974485
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:44.388343
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:46.801466
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:49.214654
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:51.627760
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:28:54.043665
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:56.458973
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:28:58.869113
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:01.281671
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:03.696154
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:06.110259
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:08.524736
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:10.936940
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:13.359662
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:29:15.778773
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:29:18.199892
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:29:20.624359
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:29:23.037675
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:29:25.452851
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:29:27.866254
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:29:30.280271
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:32.692036
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:35.104805
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:37.515897
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:29:39.931518
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:29:42.342251
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:29:44.754100
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:47.166509
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:49.578565
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:29:51.991922
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:29:54.404961
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:29:56.817381
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 12:29:59.466694
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:30:01.880360
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:30:40.151623
# Unit test for method __gt__ of class Version
def test_Version___gt__():v1 = LooseVersion('1.2.10')

# Generated at 2026-10-24 12:30:42.566865
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:30:44.980925
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:30:47.501239
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 12:30:49.915209
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:30:52.468234
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:30:54.880294
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 12:30:57.293239
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:30:59.708620
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:31:02.125629
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 12:31:04.534600
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 12:31:06.947373
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 12:31:09.360624
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 12:31:11.773221
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:14.186647
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:16.600514
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:19.014319
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 12:31:21.428122
# Unit test for method __lt__ of class Version