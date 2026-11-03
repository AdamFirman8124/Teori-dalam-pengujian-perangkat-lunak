

# Generated at 2026-11-02 13:46:34.520404
# Unit test for method __le__ of class Version
def test_Version___le__():
    class _ComparableVersion(Version):
        """Minimal concrete Version subclass implementing _cmp on integers."""

        def parse(self, vstring):
            self.value = int(vstring)

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if isinstance(other, str):
                other = _ComparableVersion(other)
            if not isinstance(other, _ComparableVersion):
                return NotImplemented
            return (self.value > other.value) - (self.value < other.value)

    v1 = _ComparableVersion(1)
    v2 = _ComparableVersion(2)
    v3 = _ComparableVersion(3)

    # equal versions compare less-than-or-equal
    assert _ComparableVersion(2) <= v2

    # lesser instances compare less-than-or-equal to greater ones
    assert v1 <= v2
    assert v1 <= v3
    assert v2 <= v3

    # greater instances do not compare less-than-or-equal to lesser ones
    assert not v2 <= v1
    assert not v3 <= v1
    assert not v3 <= v2

    # comparison against a string (parsed to an instance of the same class)
    assert v1 <= '2'
    assert v2 <= '2'
    assert not v2 <= '1'

    # comparison with an unsupported type propagates NotImplemented
    assert v1.__le__(object()) is NotImplemented

# Generated at 2026-11-02 13:47:50.660006
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class MinimalVersion(Version):
        def parse(self, vstring):
            self.version = int(vstring)

        def __str__(self):
            return str(self.version)

        def _cmp(self, other):
            if isinstance(other, str):
                other = MinimalVersion(other)
            if not isinstance(other, MinimalVersion):
                return NotImplemented
            if self.version < other.version:
                return -1
            elif self.version > other.version:
                return 1
            return 0

    v1 = MinimalVersion('1')
    v2 = MinimalVersion('2')
    v3 = MinimalVersion('2')

    # less than
    assert (v1 < v2) is True
    # greater than
    assert (v2 < v1) is False
    # equal
    assert (v2 < v3) is False
    # comparison against a string is parsed
    assert (v1 < '2') is True
    # incompatible type -> _cmp returns NotImplemented -> TypeError raised
    with pytest.raises(TypeError):
        v1 < object()

# Generated at 2026-11-02 13:49:15.691556
# Unit test for constructor of class Version
def test_Version():
    # Version is an abstract base class; constructing with no argument
    # must succeed without invoking parse().
    v = Version()
    assert isinstance(v, Version)

    # Constructing with a version string delegates to parse(), which is
    # not implemented on the base class, so an AttributeError is expected.
    try:
        Version('1.0')
    except AttributeError:
        pass
    else:
        raise AssertionError("Version('1.0') should raise AttributeError "
                             "because parse() is not implemented")

# Generated at 2026-11-02 13:51:18.931210
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    # nonce:3c3fc8fe
    # Two-component versions with zero patch collapse to two parts
    assert str(StrictVersion('0.4')) == '0.4'
    assert str(StrictVersion('0.4.0')) == '0.4'
    assert str(StrictVersion('1.0')) == '1.0'

    # Three-component versions with non-zero patch keep all three parts
    assert str(StrictVersion('0.4.1')) == '0.4.1'
    assert str(StrictVersion('0.9.6')) == '0.9.6'
    assert str(StrictVersion('1.0.4')) == '1.0.4'

    # Pre-release tags are preserved
    assert str(StrictVersion('0.5a1')) == '0.5a1'
    assert str(StrictVersion('0.5b3')) == '0.5b3'
    assert str(StrictVersion('1.0.4a3')) == '1.0.4a3'
    assert str(StrictVersion('1.0.4b1')) == '1.0.4b1'
    assert str(StrictVersion('2.7a0')) == '2.7a0'

    # Round-trip: str(parse(str(v))) == str(v) for a sample of valid versions
    for vstring in ('0.4', '0.4.0', '0.4.1', '0.5a1', '0.5b3',
                    '0.9.6', '1.0', '1.0.4a3', '1.0.4b1', '1.0.4'):
        assert str(StrictVersion(vstring)) == vstring