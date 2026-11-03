

# Generated at 2026-11-02 15:44:38.961895
# Unit test for constructor of class LooseVersion
def test_LooseVersion():
    # Valid version strings (taken from the class docstring), along with
    # the expected parsed component lists.
    versions = (
        ('1.5.1', [1, 5, 1]),
        ('1.5.2b2', [1, 5, 2, 'b', 2]),
        ('161', [161]),
        ('3.10a', [3, 10, 'a']),
        ('8.02', [8, 2]),
        ('3.4j', [3, 4, 'j']),
        ('1996.07.12', [1996, 7, 12]),
        ('3.2.pl0', [3, 2, 'pl', 0]),
        ('3.1.1.6', [3, 1, 1, 6]),
        ('2g6', [2, 'g', 6]),
        ('11g', [11, 'g']),
        ('0.960923', [0, 960923]),
        ('2.2beta29', [2, 2, 'beta', 29]),
        ('1.13++', [1, 13, '++']),
        ('5.5.kw', [5, 5, 'kw']),
        ('2.0b1pl0', [2, 0, 'b', 1, 'pl', 0]),
    )

    for vstring, expected in versions:
        # Constructor with a version string should parse it
        v = LooseVersion(vstring)
        assert v.version == expected, \
            "LooseVersion(%r).version is %r, expected %r" % (vstring, v.version, expected)
        assert v.vstring == vstring, \
            "LooseVersion(%r).vstring is %r" % (vstring, v.vstring)
        # __str__ should round-trip the original string
        assert str(v) == vstring, \
            "str(LooseVersion(%r)) is %r" % (vstring, str(v))
        # __repr__ should produce code that recreates an equivalent object
        r = eval(repr(v))
        assert isinstance(r, LooseVersion)
        assert r.version == v.version, \
            "repr/eval round-trip failed for %r: %r" % (vstring, repr(v))
        # Calling parse() on a separately constructed instance must agree
        v2 = LooseVersion()
        v2.parse(vstring)
        assert v2.version == expected
        assert v2.vstring == vstring

    # Constructor with no argument should succeed without parsing anything
    v = LooseVersion()
    assert not hasattr(v, 'version')
    assert not hasattr(v, 'vstring')

    # Leading zeros in numeric components are tolerated (and dropped)
    v = LooseVersion('8.02')
    assert v.version == [8, 2]

    print("test_LooseVersion passed")

# Generated at 2026-11-02 15:47:05.842470
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    '''Test method parse of class StrictVersion.'''
    v = StrictVersion()

    # Valid version numbers without a pre-release tag
    v.parse('0.4')
    assert v.version == (0, 4, 0)
    assert v.prerelease is None

    v.parse('0.4.0')
    assert v.version == (0, 4, 0)
    assert v.prerelease is None

    v.parse('0.4.1')
    assert v.version == (0, 4, 1)
    assert v.prerelease is None

    v.parse('0.9.6')
    assert v.version == (0, 9, 6)
    assert v.prerelease is None

    v.parse('1.0')
    assert v.version == (1, 0, 0)
    assert v.prerelease is None

    v.parse('1.0.4')
    assert v.version == (1, 0, 4)
    assert v.prerelease is None

    # Valid version numbers with a pre-release tag
    v.parse('0.5a1')
    assert v.version == (0, 5, 0)
    assert v.prerelease == ('a', 1)

    v.parse('0.5b3')
    assert v.version == (0, 5, 0)
    assert v.prerelease == ('b', 3)

    v.parse('1.0.4a3')
    assert v.version == (1, 0, 4)
    assert v.prerelease == ('a', 3)

    v.parse('1.0.4b1')
    assert v.version == (1, 0, 4)
    assert v.prerelease == ('b', 1)

    # A missing patch component is normalized to 0
    v.parse('2.7a2')
    assert v.version == (2, 7, 0)
    assert v.prerelease == ('a', 2)

    # Invalid version numbers must raise ValueError
    for invalid in ('1', '2.7.2.2', '1.3.a4', '1.3pl1', '1.3c4', ''):
        try:
            StrictVersion().parse(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(
                "expected ValueError for invalid version %r" % invalid)

# Generated at 2026-11-02 15:48:30.108137
# Unit test for constructor of class StrictVersion
def test_StrictVersion():
    from distutils.version import StrictVersion

    # Constructing with a valid two-component version string
    v = StrictVersion('1.2')
    assert v.version == (1, 2, 0)
    assert v.prerelease is None
    assert str(v) == '1.2'

    # Constructing with a valid three-component version string
    v = StrictVersion('1.2.3')
    assert v.version == (1, 2, 3)
    assert v.prerelease is None
    assert str(v) == '1.2.3'

    # Constructing with a valid pre-release version string ('a')
    v = StrictVersion('1.2.3a1')
    assert v.version == (1, 2, 3)
    assert v.prerelease == ('a', 1)
    assert str(v) == '1.2.3a1'

    # Constructing with a valid pre-release version string ('b')
    v = StrictVersion('1.2.3b2')
    assert v.version == (1, 2, 3)
    assert v.prerelease == ('b', 2)
    assert str(v) == '1.2.3b2'

    # Pre-release without patch component
    v = StrictVersion('0.5b3')
    assert v.version == (0, 5, 0)
    assert v.prerelease == ('b', 3)
    assert str(v) == '0.5b3'

    # repr reconstructs an equivalent instance
    v = StrictVersion('1.0.4a3')
    assert repr(v) == "StrictVersion ('1.0.4a3')"

    # Constructing with no arguments should not parse anything
    v = StrictVersion()
    try:
        v.version
        raised = False
    except AttributeError:
        raised = True
    assert raised, "expected 'version' attribute to be unset"

    # Invalid version strings should raise ValueError
    for invalid in ('1', '2.7.2.2', '1.3.a4', '1.3pl1', '1.3c4', '', '1..2', 'a.b'):
        try:
            StrictVersion(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError(
                "expected ValueError for invalid version number '%s'" % invalid
            )