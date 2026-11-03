

# Generated at 2026-11-03 00:06:45.436789
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    from distutils.version import StrictVersion

    # Two-component version: patch defaults to 0
    v = StrictVersion('1.2')
    assert v.version == (1, 2, 0)
    assert v.prerelease is None
    assert str(v) == '1.2'

    # Three-component version
    v = StrictVersion('1.2.3')
    assert v.version == (1, 2, 3)
    assert v.prerelease is None
    assert str(v) == '1.2.3'

    # Multi-digit components
    v = StrictVersion('10.20.30')
    assert v.version == (10, 20, 30)
    assert str(v) == '10.20.30'

    # 'a' pre-release tag on two-component version
    v = StrictVersion('1.2a1')
    assert v.version == (1, 2, 0)
    assert v.prerelease == ('a', 1)
    assert str(v) == '1.2a1'

    # 'b' pre-release tag on three-component version
    v = StrictVersion('1.2.3b2')
    assert v.version == (1, 2, 3)
    assert v.prerelease == ('b', 2)
    assert str(v) == '1.2.3b2'

    # Multi-digit pre-release number
    v = StrictVersion('1.0.4a3')
    assert v.version == (1, 0, 4)
    assert v.prerelease == ('a', 3)
    assert str(v) == '1.0.4a3'

    # Explicit zero patch is normalized away in __str__
    v = StrictVersion('1.2.0a1')
    assert v.version == (1, 2, 0)
    assert v.prerelease == ('a', 1)
    assert str(v) == '1.2a1'

    # Calling parse directly on an unparsed instance
    v = StrictVersion()
    v.parse('2.0.1')
    assert v.version == (2, 0, 1)
    assert v.prerelease is None

    # Invalid version strings must raise ValueError via parse
    for bad in ('1', '2.7.2.2', '1.3.a4', '1.3pl1', '1.3c4',
                'abc', '1.', '.1.2', '1..2', ' 1.2', '1.2 ', ''):
        try:
            StrictVersion().parse(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(
                "expected ValueError for invalid version %r" % bad)

    # Constructor with no argument leaves instance unparsed
    v = StrictVersion()
    assert not hasattr(v, 'version')

# Generated at 2026-11-03 00:08:39.295821
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():"""Test StrictVersion.__str__ round-trips and normalizes correctly."""
    # Two-component versions (patch == 0 renders without the patch part)

# Generated at 2026-11-03 00:10:48.520292
# Unit test for constructor of class StrictVersion
def test_StrictVersion():
    # Constructing with no argument creates an instance without parsing
    v = StrictVersion()
    assert not hasattr(v, 'version')
    assert not hasattr(v, 'prerelease')

    # Valid version strings are parsed into version/prerelease attributes
    valid = [
        ('0.4', (0, 4, 0), None),
        ('0.4.0', (0, 4, 0), None),
        ('0.4.1', (0, 4, 1), None),
        ('0.5a1', (0, 5, 0), ('a', 1)),
        ('0.5b3', (0, 5, 0), ('b', 3)),
        ('0.5', (0, 5, 0), None),
        ('0.9.6', (0, 9, 6), None),
        ('1.0', (1, 0, 0), None),
        ('1.0.4a3', (1, 0, 4), ('a', 3)),
        ('1.0.4b1', (1, 0, 4), ('b', 1)),
        ('1.0.4', (1, 0, 4), None),
    ]
    for vstring, expected_version, expected_prerelease in valid:
        v = StrictVersion(vstring)
        assert v.version == expected_version, \
            "wrong version for %r: %r" % (vstring, v.version)
        assert v.prerelease == expected_prerelease, \
            "wrong prerelease for %r: %r" % (vstring, v.prerelease)

    # Invalid version strings raise ValueError at construction time
    for vstring in ['1', '2.7.2.2', '1.3.a4', '1.3pl1', '1.3c4']:
        try:
            StrictVersion(vstring)
        except ValueError:
            pass
        else:
            raise AssertionError(
                "StrictVersion(%r) should raise ValueError" % vstring)

    # An unparsed instance has no usable version state
    v = StrictVersion()
    try:
        str(v)
    except AttributeError:
        pass
    else:
        raise AssertionError("unparsed StrictVersion str() should fail")

# Generated at 2026-11-03 00:13:24.379319
# Unit test for method __repr__ of class Version
def test_Version___repr__():
    # Version is an abstract base class; create a minimal concrete subclass
    # so that parse/__str__ are available for __repr__ to use.
    class _ConcreteVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def __str__(self):
            return self.vstring

    v = _ConcreteVersion('1.2.3')
    expected = "_ConcreteVersion ('1.2.3')"
    assert repr(v) == expected, "repr(%r) should be %r, got %r" % (v, expected, repr(v))

    # repr must embed the class name and the string form of the version
    assert repr(v).startswith(_ConcreteVersion.__name__ + ' (')
    assert "'1.2.3'" in repr(v)

    # A different version string produces a different repr
    v2 = _ConcreteVersion('4.5')
    assert repr(v2) == "_ConcreteVersion ('4.5')"
    assert repr(v) != repr(v2)