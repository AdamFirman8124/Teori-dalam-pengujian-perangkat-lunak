

# Generated at 2026-10-24 06:54:36.015317
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 06:54:38.542246
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 06:54:40.957049
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 06:54:43.374925
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 06:54:45.921557
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 06:54:48.328415
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 06:55:04.194300
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    from distutils.version import LooseVersion

    cases = {
        "1.5.1":       [1, 5, 1],
        "2.2beta29":   [2, 2, 'beta', 29],
        "161":         [161],
        "3.10a":       [3, 10, 'a'],
        "8.02":        [8, 2],          # leading zero dropped by int()
        "3.4j":        [3, 4, 'j'],
        "1996.07.12":  [1996, 7, 12],
        "3.2.pl0":     [3, 2, 'pl', 0],
        "3.1.1.6":     [3, 1, 1, 6],
        "2g6":         [2, 'g', 6],
        "11g":         [11, 'g'],
        "0.960923":    [0, 960923],
        "2.2beta29":   [2, 2, 'beta', 29],
        "1.13++":      [1, 13, '++'],   # unmatched chars survive as a string part
        "5.5.kw":      [5, 5, 'kw'],
        "2.0b1pl0":    [2, 0, 'b', 1, 'pl', 0],
    }

    for vstring, expected in cases.items():
        v = LooseVersion(vstring)

        # parse stores the raw string untouched
        assert v.vstring == vstring, f"vstring: {v.vstring!r} != {vstring!r}"

        # ...and builds a mixed int/str component list
        assert v.version == expected, f"{vstring}: {v.version!r} != {expected!r}"

        # __str__ round-trips via the stored string
        assert str(v) == vstring

# Generated at 2026-10-24 06:55:17.084259
# Unit test for method parse of class StrictVersion

# Generated at 2026-10-24 06:55:30.927518
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():sv = StrictVersion()

# Generated at 2026-10-24 06:55:33.451687
# Unit test for method __repr__ of class LooseVersion

# Generated at 2026-10-24 06:55:35.961011
# Unit test for method __repr__ of class LooseVersion

# Generated at 2026-10-24 06:55:38.486582
# Unit test for method __repr__ of class LooseVersion

# Generated at 2026-10-24 06:55:40.898462
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 06:55:43.312014
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 06:55:45.727875
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 06:55:48.142370
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:55:50.568373
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:55:58.986907
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:56:32.673396
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:56:35.090158
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:56:37.506230
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:56:39.919875
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 06:56:42.335590
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 06:56:44.752218
# Unit test for method parse of class LooseVersion

# Generated at 2026-10-24 06:56:47.167835
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 06:56:49.581300
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 06:56:51.995425
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 06:56:54.409780
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 06:56:56.827702
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 06:56:59.243656
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 06:57:02.167516
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:57:03.501923
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:57:04.837753
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:57:15.376312
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version itself is abstract (no _cmp)."""

        def parse(self, vstring):
            self._num = int(vstring)

        def __str__(self):
            return str(self._num)

        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self._num < other._num:
                return -1
            if self._num > other._num:
                return 1
            return 0

    # greater than
    assert ConcreteVersion('2') > ConcreteVersion('1')
    assert ConcreteVersion('2') > '1'

    # not greater than
    assert not (ConcreteVersion('1') > ConcreteVersion('2'))
    assert not (ConcreteVersion('1') > '2')

    # equal -> not greater
    assert not (ConcreteVersion('1') > ConcreteVersion('1'))
    assert not (ConcreteVersion('1') > '1')

    # incomparable type -> __gt__ returns NotImplemented, does not raise
    assert ConcreteVersion('1').__gt__(object()) is NotImplemented

    # comparing against a different Version subclass is incomparable
    class OtherVersion(ConcreteVersion):
        pass

    assert ConcreteVersion('1').__gt__(OtherVersion('0')) is NotImplemented

# Generated at 2026-10-24 06:57:27.868545
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 06:57:56.848601
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    # Valid: two-component version, no prerelease
    v = StrictVersion('1.2')
    assert v.version == (1, 2, 0)
    assert v.prerelease is None
    assert str(v) == '1.2'

    # Valid: three-component version
    v = StrictVersion('1.2.3')
    assert v.version == (1, 2, 3)
    assert v.prerelease is None
    assert str(v) == '1.2.3'

    # Two-component with .0 patch normalizes to two-component string
    v = StrictVersion('1.2.0')
    assert v.version == (1, 2, 0)
    assert str(v) == '1.2'

    # Prerelease 'a'
    v = StrictVersion('1.0.4a3')
    assert v.version == (1, 0, 4)
    assert v.prerelease == ('a', 3)
    assert str(v) == '1.0.4a3'

    # Prerelease 'b'
    v = StrictVersion('0.5b3')
    assert v.version == (0, 5, 0)
    assert v.prerelease == ('b', 3)
    assert str(v) == '0.5b3'

    # Invalid: single component
    try:
        StrictVersion('1')
        assert False, "expected ValueError"
    except ValueError:
        pass

    # Invalid: four components
    try:
        StrictVersion('2.7.2.2')
        assert False, "expected ValueError"
    except ValueError:
        pass

    # Invalid: prerelease without number
    try:
        StrictVersion('1.3.a4')
        assert False, "expected ValueError"
    except ValueError:
        pass

    # Invalid: bad prerelease tag
    try:
        StrictVersion('1.3pl1')
        assert False, "expected ValueError"
    except ValueError:
        pass

    try:
        StrictVersion('1.3c4')
        assert False, "expected ValueError"
    except ValueError:
        pass

    # Empty string is invalid
    try:
        StrictVersion('')
        assert False, "expected ValueError"
    except ValueError:
        pass


test_StrictVersion_parse()
print("test_StrictVersion_parse: all assertions passed")

# Generated at 2026-10-24 06:57:58.174841
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 06:57:59.484152
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version itself is abstract (no _cmp)."""

        def parse(self, vstring):
            self._num = int(vstring)

        def __str__(self):
            return str(self._num)

        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self._num < other._num:
                return -1
            if self._num > other._num:
                return 1
            return 0

    # greater than
    assert ConcreteVersion('2') > ConcreteVersion('1')
    assert ConcreteVersion('2') > '1'

    # not greater than
    assert not (ConcreteVersion('1') > ConcreteVersion('2'))
    assert not (ConcreteVersion('1') > '2')

    # equal -> not greater
    assert not (ConcreteVersion('1') > ConcreteVersion('1'))
    assert not (ConcreteVersion('1') > '1')

    # incomparable type -> __gt__ returns NotImplemented, does not raise
    assert ConcreteVersion('1').__gt__(object()) is NotImplemented

    # comparing against a different Version subclass is incomparable
    class OtherVersion(ConcreteVersion):
        pass

    assert ConcreteVersion('1').__gt__(OtherVersion('0')) is NotImplemented

# Generated at 2026-10-24 06:58:00.800779
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 06:58:02.125930
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version itself is abstract (no _cmp)."""

        def parse(self, vstring):
            self._num = int(vstring)

        def __str__(self):
            return str(self._num)

        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self._num < other._num:
                return -1
            if self._num > other._num:
                return 1
            return 0

    # greater than
    assert ConcreteVersion('2') > ConcreteVersion('1')
    assert ConcreteVersion('2') > '1'

    # not greater than
    assert not (ConcreteVersion('1') > ConcreteVersion('2'))
    assert not (ConcreteVersion('1') > '2')

    # equal -> not greater
    assert not (ConcreteVersion('1') > ConcreteVersion('1'))
    assert not (ConcreteVersion('1') > '1')

    # incomparable type -> __gt__ returns NotImplemented, does not raise
    assert ConcreteVersion('1').__gt__(object()) is NotImplemented

    # comparing against a different Version subclass is incomparable
    class OtherVersion(ConcreteVersion):
        pass

    assert ConcreteVersion('1').__gt__(OtherVersion('0')) is NotImplemented

# Generated at 2026-10-24 06:58:04.839695
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:58:06.268962
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:58:07.585953
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:58:10.367399
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:58:11.686011
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:58:13.071579
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 06:58:14.385039
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    from distutils.version import LooseVersion

    cases = {
        "1.5.1":       [1, 5, 1],
        "2.2beta29":   [2, 2, 'beta', 29],
        "161":         [161],
        "3.10a":       [3, 10, 'a'],
        "8.02":        [8, 2],          # leading zero dropped by int()
        "3.4j":        [3, 4, 'j'],
        "1996.07.12":  [1996, 7, 12],
        "3.2.pl0":     [3, 2, 'pl', 0],
        "3.1.1.6":     [3, 1, 1, 6],
        "2g6":         [2, 'g', 6],
        "11g":         [11, 'g'],
        "0.960923":    [0, 960923],
        "2.2beta29":   [2, 2, 'beta', 29],
        "1.13++":      [1, 13, '++'],   # unmatched chars survive as a string part
        "5.5.kw":      [5, 5, 'kw'],
        "2.0b1pl0":    [2, 0, 'b', 1, 'pl', 0],
    }

    for vstring, expected in cases.items():
        v = LooseVersion(vstring)

        # parse stores the raw string untouched
        assert v.vstring == vstring, f"vstring: {v.vstring!r} != {vstring!r}"

        # ...and builds a mixed int/str component list
        assert v.version == expected, f"{vstring}: {v.version!r} != {expected!r}"

        # __str__ round-trips via the stored string
        assert str(v) == vstring

# Generated at 2026-10-24 06:58:22.780536
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class FakeVersion(Version):
        """Concrete subclass; Version._cmp is abstract."""
        def _cmp(self, other):
            if isinstance(other, FakeVersion):
                other = other.vstring
            if not isinstance(other, str):
                return NotImplemented
            a = [int(x) for x in self.vstring.split('.')]
            b = [int(x) for x in other.split('.')]
            return (a > b) - (a < b)

        def parse(self, vstring):
            self.vstring = vstring

    v = FakeVersion('1.2.3')

    # strictly greater -> True
    assert (v >= FakeVersion('1.2.2')) is True
    # equal -> True
    assert (v >= FakeVersion('1.2.3')) is True
    # strictly lesser -> False
    assert (v >= FakeVersion('1.2.10')) is False   # numeric compare, not string

    # _cmp returns NotImplemented (non-string, non-Version) -> __ge__ must
    # return NotImplemented, not raise or coerce to a bool
    assert (v >= 42) is NotImplemented
    assert (v >= None) is NotImplemented

# Generated at 2026-10-24 06:58:34.124569
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class FakeVersion(Version):
        """Concrete subclass; Version._cmp is abstract."""
        def _cmp(self, other):
            if isinstance(other, FakeVersion):
                other = other.vstring
            if not isinstance(other, str):
                return NotImplemented
            a = [int(x) for x in self.vstring.split('.')]
            b = [int(x) for x in other.split('.')]
            return (a > b) - (a < b)

        def parse(self, vstring):
            self.vstring = vstring

    v = FakeVersion('1.2.3')

    # strictly greater -> True
    assert (v >= FakeVersion('1.2.2')) is True
    # equal -> True
    assert (v >= FakeVersion('1.2.3')) is True
    # strictly lesser -> False
    assert (v >= FakeVersion('1.2.10')) is False   # numeric compare, not string

    # _cmp returns NotImplemented (non-string, non-Version) -> __ge__ must
    # return NotImplemented, not raise or coerce to a bool
    assert (v >= 42) is NotImplemented
    assert (v >= None) is NotImplemented

# Generated at 2026-10-24 06:59:21.329520
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    v = LooseVersion()
    v.parse("1.5.2b2")
    assert v.vstring == "1.5.2b2"
    assert v.version == [1, 5, 2, "b", 2]

    v.parse("161")
    assert v.vstring == "161"
    assert v.version == [161]

    v.parse("3.10a")
    assert v.vstring == "3.10a"
    assert v.version == [3, 10, "a"]

    v.parse("8.02")
    assert v.version == [8, 2]

    v.parse("1.13++")
    assert v.vstring == "1.13++"
    assert v.version == [1, 13, "++"]

    v.parse("2.0b1pl0")
    assert v.version == [2, 0, "b", 1, "pl", 0]

    v.parse("")
    assert v.vstring == ""
    assert v.version == []

# Generated at 2026-10-24 06:59:22.639824
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version itself is abstract (no _cmp)."""

        def parse(self, vstring):
            self._num = int(vstring)

        def __str__(self):
            return str(self._num)

        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self._num < other._num:
                return -1
            if self._num > other._num:
                return 1
            return 0

    # greater than
    assert ConcreteVersion('2') > ConcreteVersion('1')
    assert ConcreteVersion('2') > '1'

    # not greater than
    assert not (ConcreteVersion('1') > ConcreteVersion('2'))
    assert not (ConcreteVersion('1') > '2')

    # equal -> not greater
    assert not (ConcreteVersion('1') > ConcreteVersion('1'))
    assert not (ConcreteVersion('1') > '1')

    # incomparable type -> __gt__ returns NotImplemented, does not raise
    assert ConcreteVersion('1').__gt__(object()) is NotImplemented

    # comparing against a different Version subclass is incomparable
    class OtherVersion(ConcreteVersion):
        pass

    assert ConcreteVersion('1').__gt__(OtherVersion('0')) is NotImplemented

# Generated at 2026-10-24 06:59:23.967840
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 06:59:25.429335
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class FakeVersion(Version):
        """Concrete subclass; Version._cmp is abstract."""
        def _cmp(self, other):
            if isinstance(other, FakeVersion):
                other = other.vstring
            if not isinstance(other, str):
                return NotImplemented
            a = [int(x) for x in self.vstring.split('.')]
            b = [int(x) for x in other.split('.')]
            return (a > b) - (a < b)

        def parse(self, vstring):
            self.vstring = vstring

    v = FakeVersion('1.2.3')

    # strictly greater -> True
    assert (v >= FakeVersion('1.2.2')) is True
    # equal -> True
    assert (v >= FakeVersion('1.2.3')) is True
    # strictly lesser -> False
    assert (v >= FakeVersion('1.2.10')) is False   # numeric compare, not string

    # _cmp returns NotImplemented (non-string, non-Version) -> __ge__ must
    # return NotImplemented, not raise or coerce to a bool
    assert (v >= 42) is NotImplemented
    assert (v >= None) is NotImplemented

# Generated at 2026-10-24 06:59:26.734556
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 06:59:38.124226
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class FakeVersion(Version):
        """Concrete subclass; Version._cmp is abstract."""
        def _cmp(self, other):
            if isinstance(other, FakeVersion):
                other = other.vstring
            if not isinstance(other, str):
                return NotImplemented
            a = [int(x) for x in self.vstring.split('.')]
            b = [int(x) for x in other.split('.')]
            return (a > b) - (a < b)

        def parse(self, vstring):
            self.vstring = vstring

    v = FakeVersion('1.2.3')

    # strictly greater -> True
    assert (v >= FakeVersion('1.2.2')) is True
    # equal -> True
    assert (v >= FakeVersion('1.2.3')) is True
    # strictly lesser -> False
    assert (v >= FakeVersion('1.2.10')) is False   # numeric compare, not string

    # _cmp returns NotImplemented (non-string, non-Version) -> __ge__ must
    # return NotImplemented, not raise or coerce to a bool
    assert (v >= 42) is NotImplemented
    assert (v >= None) is NotImplemented

# Generated at 2026-10-24 07:00:04.542453
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class _TestVersion(Version):
        """Concrete subclass providing a simple _cmp for testing."""

        component_re = re.compile(r'(\d+ | [a-z]+ | \.)', re.VERBOSE)

        def parse(self, vstring):
            self.vstring = vstring
            components = [x for x in self.component_re.split(vstring) if x and x != '.']
            for i, obj in enumerate(components):
                try:
                    components[i] = int(obj)
                except ValueError:
                    pass
            self.version = components

        def _cmp(self, other):
            if isinstance(other, str):
                other = _TestVersion(other)
            other = _TestVersion(str(other))
            if self.version < other.version:
                return -1
            if self.version > other.version:
                return 1
            return 0

    # Numeric comparisons via < operator
    assert (_TestVersion('1.0') < _TestVersion('2.0')) is True
    assert (_TestVersion('2.0') < _TestVersion('1.0')) is False
    assert (_TestVersion('1.0') < _TestVersion('1.0')) is False
    assert (_TestVersion('1.0') < _TestVersion('1.1')) is True
    assert (_TestVersion('1.9') < _TestVersion('1.10')) is True

    # Comparison against a plain string (parsed internally)
    assert (_TestVersion('1.0') < '2.0') is True
    assert (_TestVersion('2.0') < '1.0') is False
    assert (_TestVersion('1.0') < '1.0') is False

    # Comparison against a non-comparable type returns NotImplemented
    assert (_TestVersion('1.0').__lt__(object())) is NotImplemented

    # Mixed component types (numeric vs. alphabetic), mirroring LooseVersion semantics
    assert (_TestVersion('1.0a') < _TestVersion('1.0b')) is True
    assert (_TestVersion('1.0b') < _TestVersion('1.0a')) is False

    # Rich comparison consistency: lt must agree with gt and ge
    a = _TestVersion('1.2.3')
    b = _TestVersion('1.2.4')
    assert (a < b) is True
    assert (b < a) is False
    assert (a < a) is False

# Generated at 2026-10-24 07:00:17.662016
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:00:20.355850
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:00:26.050466
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:00:49.731084
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.value = int(vstring)

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    assert DummyVersion("1") < DummyVersion("2")
    assert not DummyVersion("2") < DummyVersion("1")
    assert not DummyVersion("1") < DummyVersion("1")
    assert DummyVersion("1").__lt__("x") is NotImplemented

# Generated at 2026-10-24 07:00:59.943288
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.value = int(vstring)

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    assert DummyVersion("1") < DummyVersion("2")
    assert not DummyVersion("2") < DummyVersion("1")
    assert not DummyVersion("1") < DummyVersion("1")
    assert DummyVersion("1").__lt__("x") is NotImplemented

# Generated at 2026-10-24 07:01:11.308792
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 07:01:17.663157
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    from distutils.version import LooseVersion

    cases = {
        "1.5.1":       [1, 5, 1],
        "2.2beta29":   [2, 2, 'beta', 29],
        "161":         [161],
        "3.10a":       [3, 10, 'a'],
        "8.02":        [8, 2],          # leading zero dropped by int()
        "3.4j":        [3, 4, 'j'],
        "1996.07.12":  [1996, 7, 12],
        "3.2.pl0":     [3, 2, 'pl', 0],
        "3.1.1.6":     [3, 1, 1, 6],
        "2g6":         [2, 'g', 6],
        "11g":         [11, 'g'],
        "0.960923":    [0, 960923],
        "2.2beta29":   [2, 2, 'beta', 29],
        "1.13++":      [1, 13, '++'],   # unmatched chars survive as a string part
        "5.5.kw":      [5, 5, 'kw'],
        "2.0b1pl0":    [2, 0, 'b', 1, 'pl', 0],
    }

    for vstring, expected in cases.items():
        v = LooseVersion(vstring)

        # parse stores the raw string untouched
        assert v.vstring == vstring, f"vstring: {v.vstring!r} != {vstring!r}"

        # ...and builds a mixed int/str component list
        assert v.version == expected, f"{vstring}: {v.version!r} != {expected!r}"

        # __str__ round-trips via the stored string
        assert str(v) == vstring

# Generated at 2026-10-24 07:01:19.016039
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.value = int(vstring)

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    assert DummyVersion("1") < DummyVersion("2")
    assert not DummyVersion("2") < DummyVersion("1")
    assert not DummyVersion("1") < DummyVersion("1")
    assert DummyVersion("1").__lt__("x") is NotImplemented

# Generated at 2026-10-24 07:01:21.733234
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:01:23.066530
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:01:24.428208
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:01:25.727630
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version itself is abstract (no _cmp)."""

        def parse(self, vstring):
            self._num = int(vstring)

        def __str__(self):
            return str(self._num)

        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self._num < other._num:
                return -1
            if self._num > other._num:
                return 1
            return 0

    # greater than
    assert ConcreteVersion('2') > ConcreteVersion('1')
    assert ConcreteVersion('2') > '1'

    # not greater than
    assert not (ConcreteVersion('1') > ConcreteVersion('2'))
    assert not (ConcreteVersion('1') > '2')

    # equal -> not greater
    assert not (ConcreteVersion('1') > ConcreteVersion('1'))
    assert not (ConcreteVersion('1') > '1')

    # incomparable type -> __gt__ returns NotImplemented, does not raise
    assert ConcreteVersion('1').__gt__(object()) is NotImplemented

    # comparing against a different Version subclass is incomparable
    class OtherVersion(ConcreteVersion):
        pass

    assert ConcreteVersion('1').__gt__(OtherVersion('0')) is NotImplemented

# Generated at 2026-10-24 07:01:27.029279
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.value = int(vstring)

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    assert DummyVersion("1") < DummyVersion("2")
    assert not DummyVersion("2") < DummyVersion("1")
    assert not DummyVersion("1") < DummyVersion("1")
    assert DummyVersion("1").__lt__("x") is NotImplemented

# Generated at 2026-10-24 07:01:28.361088
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class FakeVersion(Version):
        """Concrete subclass; Version._cmp is abstract."""
        def _cmp(self, other):
            if isinstance(other, FakeVersion):
                other = other.vstring
            if not isinstance(other, str):
                return NotImplemented
            a = [int(x) for x in self.vstring.split('.')]
            b = [int(x) for x in other.split('.')]
            return (a > b) - (a < b)

        def parse(self, vstring):
            self.vstring = vstring

    v = FakeVersion('1.2.3')

    # strictly greater -> True
    assert (v >= FakeVersion('1.2.2')) is True
    # equal -> True
    assert (v >= FakeVersion('1.2.3')) is True
    # strictly lesser -> False
    assert (v >= FakeVersion('1.2.10')) is False   # numeric compare, not string

    # _cmp returns NotImplemented (non-string, non-Version) -> __ge__ must
    # return NotImplemented, not raise or coerce to a bool
    assert (v >= 42) is NotImplemented
    assert (v >= None) is NotImplemented

# Generated at 2026-10-24 07:01:29.651714
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version itself is abstract (no _cmp)."""

        def parse(self, vstring):
            self._num = int(vstring)

        def __str__(self):
            return str(self._num)

        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self._num < other._num:
                return -1
            if self._num > other._num:
                return 1
            return 0

    # greater than
    assert ConcreteVersion('2') > ConcreteVersion('1')
    assert ConcreteVersion('2') > '1'

    # not greater than
    assert not (ConcreteVersion('1') > ConcreteVersion('2'))
    assert not (ConcreteVersion('1') > '2')

    # equal -> not greater
    assert not (ConcreteVersion('1') > ConcreteVersion('1'))
    assert not (ConcreteVersion('1') > '1')

    # incomparable type -> __gt__ returns NotImplemented, does not raise
    assert ConcreteVersion('1').__gt__(object()) is NotImplemented

    # comparing against a different Version subclass is incomparable
    class OtherVersion(ConcreteVersion):
        pass

    assert ConcreteVersion('1').__gt__(OtherVersion('0')) is NotImplemented

# Generated at 2026-10-24 07:01:32.614400
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:01:33.912717
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:01:35.214880
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:01:36.550406
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class FakeVersion(Version):
        """Concrete subclass; Version._cmp is abstract."""
        def _cmp(self, other):
            if isinstance(other, FakeVersion):
                other = other.vstring
            if not isinstance(other, str):
                return NotImplemented
            a = [int(x) for x in self.vstring.split('.')]
            b = [int(x) for x in other.split('.')]
            return (a > b) - (a < b)

        def parse(self, vstring):
            self.vstring = vstring

    v = FakeVersion('1.2.3')

    # strictly greater -> True
    assert (v >= FakeVersion('1.2.2')) is True
    # equal -> True
    assert (v >= FakeVersion('1.2.3')) is True
    # strictly lesser -> False
    assert (v >= FakeVersion('1.2.10')) is False   # numeric compare, not string

    # _cmp returns NotImplemented (non-string, non-Version) -> __ge__ must
    # return NotImplemented, not raise or coerce to a bool
    assert (v >= 42) is NotImplemented
    assert (v >= None) is NotImplemented

# Generated at 2026-10-24 07:01:37.876055
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 07:01:40.761252
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:01:42.048454
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:01:43.343082
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:01:45.950132
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 07:01:48.363305
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 07:01:50.929588
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 07:01:53.347932
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 07:01:55.774520
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 07:01:58.189997
# Unit test for method __le__ of class Version

# Generated at 2026-10-24 07:02:00.604216
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:02:03.018581
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:02:05.452065
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:02:07.866217
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 07:02:10.279889
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 07:02:12.694767
# Unit test for method __lt__ of class Version

# Generated at 2026-10-24 07:02:15.109921
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 07:02:27.594128
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 07:02:50.221241
# Unit test for method __gt__ of class Version

# Generated at 2026-10-24 07:02:56.587130
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 07:03:19.288252
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:20.584932
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:21.891061
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:23.241147
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version itself is abstract (no _cmp)."""

        def parse(self, vstring):
            self._num = int(vstring)

        def __str__(self):
            return str(self._num)

        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self._num < other._num:
                return -1
            if self._num > other._num:
                return 1
            return 0

    # greater than
    assert ConcreteVersion('2') > ConcreteVersion('1')
    assert ConcreteVersion('2') > '1'

    # not greater than
    assert not (ConcreteVersion('1') > ConcreteVersion('2'))
    assert not (ConcreteVersion('1') > '2')

    # equal -> not greater
    assert not (ConcreteVersion('1') > ConcreteVersion('1'))
    assert not (ConcreteVersion('1') > '1')

    # incomparable type -> __gt__ returns NotImplemented, does not raise
    assert ConcreteVersion('1').__gt__(object()) is NotImplemented

    # comparing against a different Version subclass is incomparable
    class OtherVersion(ConcreteVersion):
        pass

    assert ConcreteVersion('1').__gt__(OtherVersion('0')) is NotImplemented

# Generated at 2026-10-24 07:03:26.066063
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:27.364370
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:28.673739
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:31.126255
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version itself is abstract (no _cmp)."""

        def parse(self, vstring):
            self._num = int(vstring)

        def __str__(self):
            return str(self._num)

        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self._num < other._num:
                return -1
            if self._num > other._num:
                return 1
            return 0

    # greater than
    assert ConcreteVersion('2') > ConcreteVersion('1')
    assert ConcreteVersion('2') > '1'

    # not greater than
    assert not (ConcreteVersion('1') > ConcreteVersion('2'))
    assert not (ConcreteVersion('1') > '2')

    # equal -> not greater
    assert not (ConcreteVersion('1') > ConcreteVersion('1'))
    assert not (ConcreteVersion('1') > '1')

    # incomparable type -> __gt__ returns NotImplemented, does not raise
    assert ConcreteVersion('1').__gt__(object()) is NotImplemented

    # comparing against a different Version subclass is incomparable
    class OtherVersion(ConcreteVersion):
        pass

    assert ConcreteVersion('1').__gt__(OtherVersion('0')) is NotImplemented

# Generated at 2026-10-24 07:03:32.422419
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 07:03:33.804153
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    from distutils.version import LooseVersion

    cases = {
        "1.5.1":       [1, 5, 1],
        "2.2beta29":   [2, 2, 'beta', 29],
        "161":         [161],
        "3.10a":       [3, 10, 'a'],
        "8.02":        [8, 2],          # leading zero dropped by int()
        "3.4j":        [3, 4, 'j'],
        "1996.07.12":  [1996, 7, 12],
        "3.2.pl0":     [3, 2, 'pl', 0],
        "3.1.1.6":     [3, 1, 1, 6],
        "2g6":         [2, 'g', 6],
        "11g":         [11, 'g'],
        "0.960923":    [0, 960923],
        "2.2beta29":   [2, 2, 'beta', 29],
        "1.13++":      [1, 13, '++'],   # unmatched chars survive as a string part
        "5.5.kw":      [5, 5, 'kw'],
        "2.0b1pl0":    [2, 0, 'b', 1, 'pl', 0],
    }

    for vstring, expected in cases.items():
        v = LooseVersion(vstring)

        # parse stores the raw string untouched
        assert v.vstring == vstring, f"vstring: {v.vstring!r} != {vstring!r}"

        # ...and builds a mixed int/str component list
        assert v.version == expected, f"{vstring}: {v.version!r} != {expected!r}"

        # __str__ round-trips via the stored string
        assert str(v) == vstring

# Generated at 2026-10-24 07:03:35.114048
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class FakeVersion(Version):
        """Concrete subclass; Version._cmp is abstract."""
        def _cmp(self, other):
            if isinstance(other, FakeVersion):
                other = other.vstring
            if not isinstance(other, str):
                return NotImplemented
            a = [int(x) for x in self.vstring.split('.')]
            b = [int(x) for x in other.split('.')]
            return (a > b) - (a < b)

        def parse(self, vstring):
            self.vstring = vstring

    v = FakeVersion('1.2.3')

    # strictly greater -> True
    assert (v >= FakeVersion('1.2.2')) is True
    # equal -> True
    assert (v >= FakeVersion('1.2.3')) is True
    # strictly lesser -> False
    assert (v >= FakeVersion('1.2.10')) is False   # numeric compare, not string

    # _cmp returns NotImplemented (non-string, non-Version) -> __ge__ must
    # return NotImplemented, not raise or coerce to a bool
    assert (v >= 42) is NotImplemented
    assert (v >= None) is NotImplemented

# Generated at 2026-10-24 07:03:36.421087
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 07:03:37.735045
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.value = int(vstring)

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    assert DummyVersion("1") < DummyVersion("2")
    assert not DummyVersion("2") < DummyVersion("1")
    assert not DummyVersion("1") < DummyVersion("1")
    assert DummyVersion("1").__lt__("x") is NotImplemented

# Generated at 2026-10-24 07:03:39.054953
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 07:03:40.433629
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.value = int(vstring)

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    assert DummyVersion("1") < DummyVersion("2")
    assert not DummyVersion("2") < DummyVersion("1")
    assert not DummyVersion("1") < DummyVersion("1")
    assert DummyVersion("1").__lt__("x") is NotImplemented

# Generated at 2026-10-24 07:03:41.754318
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 07:03:44.702996
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:45.996933
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:47.321769
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:51.559484
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class FakeVersion(Version):
        """Concrete subclass; Version._cmp is abstract."""
        def _cmp(self, other):
            if isinstance(other, FakeVersion):
                other = other.vstring
            if not isinstance(other, str):
                return NotImplemented
            a = [int(x) for x in self.vstring.split('.')]
            b = [int(x) for x in other.split('.')]
            return (a > b) - (a < b)

        def parse(self, vstring):
            self.vstring = vstring

    v = FakeVersion('1.2.3')

    # strictly greater -> True
    assert (v >= FakeVersion('1.2.2')) is True
    # equal -> True
    assert (v >= FakeVersion('1.2.3')) is True
    # strictly lesser -> False
    assert (v >= FakeVersion('1.2.10')) is False   # numeric compare, not string

    # _cmp returns NotImplemented (non-string, non-Version) -> __ge__ must
    # return NotImplemented, not raise or coerce to a bool
    assert (v >= 42) is NotImplemented
    assert (v >= None) is NotImplemented

# Generated at 2026-10-24 07:03:54.532863
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:55.966480
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:57.276544
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:03:58.586987
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.value = int(vstring)

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if not isinstance(other, DummyVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    assert DummyVersion("1") < DummyVersion("2")
    assert not DummyVersion("2") < DummyVersion("1")
    assert not DummyVersion("1") < DummyVersion("1")
    assert DummyVersion("1").__lt__("x") is NotImplemented

# Generated at 2026-10-24 07:04:01.393857
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:04:02.827627
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:04:04.158359
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:04:06.581666
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 07:04:09.002799
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 07:04:11.421331
# Unit test for method __ge__ of class Version

# Generated at 2026-10-24 07:04:13.835782
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:04:16.251711
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:04:17.787346
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:04:19.096924
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class ConcreteVersion(Version):
        """Minimal concrete subclass; Version itself is abstract (no _cmp)."""

        def parse(self, vstring):
            self._num = int(vstring)

        def __str__(self):
            return str(self._num)

        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self._num < other._num:
                return -1
            if self._num > other._num:
                return 1
            return 0

    # greater than
    assert ConcreteVersion('2') > ConcreteVersion('1')
    assert ConcreteVersion('2') > '1'

    # not greater than
    assert not (ConcreteVersion('1') > ConcreteVersion('2'))
    assert not (ConcreteVersion('1') > '2')

    # equal -> not greater
    assert not (ConcreteVersion('1') > ConcreteVersion('1'))
    assert not (ConcreteVersion('1') > '1')

    # incomparable type -> __gt__ returns NotImplemented, does not raise
    assert ConcreteVersion('1').__gt__(object()) is NotImplemented

    # comparing against a different Version subclass is incomparable
    class OtherVersion(ConcreteVersion):
        pass

    assert ConcreteVersion('1').__gt__(OtherVersion('0')) is NotImplemented

# Generated at 2026-10-24 07:04:20.407261
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 07:04:21.731982
# Unit test for method __le__ of class Version
def test_Version___le__():
    class Stub(Version):
        def __init__(self, cmp_result):
            self._cmp_result = cmp_result
            self.seen_other = None

        def _cmp(self, other):
            self.seen_other = other
            return self._cmp_result

    # c < 0 -> True, via operator and direct call
    assert Stub(-1) <= Stub(0)
    assert Stub(-1).__le__(Stub(0)) is True

    # c == 0 -> True
    assert Stub(0) <= Stub(0)
    assert Stub(0).__le__(Stub(0)) is True

    # c > 0 -> False
    assert not (Stub(1) <= Stub(0))
    assert Stub(1).__le__(Stub(0)) is False

    # NotImplemented is propagated unchanged
    assert Stub(NotImplemented).__le__(Stub(0)) is NotImplemented

    # `other` is passed through to _cmp
    left, right = Stub(0), Stub(0)
    left <= right
    assert left.seen_other is right

# Generated at 2026-10-24 07:04:24.536293
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:04:27.607907
# Unit test for method __eq__ of class Version

# Generated at 2026-10-24 07:04:28.917500
# Unit test for method __eq__ of class Version