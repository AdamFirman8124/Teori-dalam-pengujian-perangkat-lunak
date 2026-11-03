

# Generated at 2026-11-02 15:51:44.940426
# Unit test for method __str__ of class LooseVersion
def test_LooseVersion___str__():
    # __str__ should return the exact version string that was parsed
    version_strings = [
        '1.5.1',
        '1.5.2b2',
        '161',
        '3.10a',
        '8.02',
        '3.4j',
        '1996.07.12',
        '3.2.pl0',
        '3.1.1.6',
        '2g6',
        '11g',
        '0.960923',
        '2.2beta29',
        '1.13++',
        '5.5.kw',
        '2.0b1pl0',
    ]

    for vstring in version_strings:
        v = LooseVersion(vstring)
        assert str(v) == vstring, (
            "str(LooseVersion(%r)) should be %r, got %r"
            % (vstring, vstring, str(v))
        )

    # Also verify str() works when constructed via parse()
    v = LooseVersion()
    v.parse('1.2.3')
    assert str(v) == '1.2.3'

    # Round-trip: str of a version compared to an equivalent string
    v = LooseVersion('1.5.2b2')
    assert str(v) == '1.5.2b2'
    assert v == LooseVersion('1.5.2b2')

# Generated at 2026-11-02 15:53:38.847742
# Unit test for constructor of class StrictVersion
def test_StrictVersion():
    """StrictVersion(vstring) parses valid version strings and rejects invalid ones."""
    # Two-component version: patch component defaults to 0
    v = StrictVersion('1.2')
    assert v.version == (1, 2, 0)
    assert v.prerelease is None
    assert str(v) == '1.2'
    assert repr(v) == "StrictVersion ('1.2')"

    # Three-component version
    v = StrictVersion('1.2.3')
    assert v.version == (1, 2, 3)
    assert v.prerelease is None
    assert str(v) == '1.2.3'

    # Pre-release tags
    v = StrictVersion('0.5a1')
    assert v.version == (0, 5, 0)
    assert v.prerelease == ('a', 1)
    assert str(v) == '0.5a1'

    v = StrictVersion('1.0.4b1')
    assert v.version == (1, 0, 4)
    assert v.prerelease == ('b', 1)

    # No argument: nothing is parsed, no attributes set
    v = StrictVersion()
    assert not hasattr(v, 'version')
    assert not hasattr(v, 'prerelease')

    # Invalid version strings raise ValueError
    for invalid in ('1', '2.7.2.2', '1.3.a4', '1.3pl1', '1.3c4', 'abc', ' 1.2'):
        try:
            StrictVersion(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError('ValueError not raised for %r' % invalid)

# Generated at 2026-11-02 15:55:56.880590
# Unit test for constructor of class Version
def test_Version():"""Test the Version abstract base class constructor."""

# Generated at 2026-11-02 15:57:31.221729
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Version is abstract (no _cmp/parse), so build a concrete subclass
    # to exercise the rich-comparison routing in Version.__eq__.
    class ConcreteVersion(Version):
        def parse(self, vstring):
            self.value = int(vstring)

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if not isinstance(other, ConcreteVersion):
                other = ConcreteVersion(str(other))
            if self.value < other.value:
                return -1
            elif self.value > other.value:
                return 1
            return 0

    v1 = ConcreteVersion('1')
    v2 = ConcreteVersion('1')
    v3 = ConcreteVersion('2')

    # equal instances compare equal
    assert v1.__eq__(v2) is True
    assert v1 == v2

    # unequal instances do not compare equal
    assert v1.__eq__(v3) is False
    assert not v1 == v3
    assert v1 != v3

    # comparison against a parseable string is supported
    assert v1.__eq__('1') is True
    assert v1 == '1'
    assert v1.__eq__('2') is False

    # if _cmp returns NotImplemented, __eq__ propagates it
    class NotImplementedCmpVersion(Version):
        def _cmp(self, other):
            return NotImplemented

    nv = NotImplementedCmpVersion()
    assert nv.__eq__(v1) is NotImplemented

    # the bare Version class has no _cmp, so __eq__ raises AttributeError
    bare = Version()
    try:
        bare.__eq__(bare)
    except AttributeError:
        pass
    else:
        raise AssertionError("expected AttributeError from Version.__eq__ without _cmp")

# Generated at 2026-11-02 15:58:54.828598
# Unit test for method __str__ of class LooseVersion
def test_LooseVersion___str__():
    # __str__ should return the original version string exactly as given
    test_cases = [
        '1.5.1',
        '1.5.2b2',
        '161',
        '3.10a',
        '8.02',
        '3.4j',
        '1996.07.12',
        '3.2.pl0',
        '3.1.1.6',
        '2g6',
        '11g',
        '0.960923',
        '2.2beta29',
        '1.13++',
        '5.5.kw',
        '2.0b1pl0',
    ]
    for vstring in test_cases:
        v = LooseVersion(vstring)
        assert str(v) == vstring, "str(%r) returned %r, expected %r" % (
            vstring, str(v), vstring)

    # Leading zeroes must be preserved (string is stored, not rebuilt)
    assert str(LooseVersion('8.02')) == '8.02'
    assert str(LooseVersion('0.960923')) == '0.960923'

    # Works after explicit parse() as well
    v = LooseVersion()
    v.parse('1.2.3')
    assert str(v) == '1.2.3'

    # Components should be parsed into ints where possible (indirect check
    # that parse ran before __str__ is called)
    v = LooseVersion('1.5.1')
    assert v.version == [1, 5, 1]
    assert str(v) == '1.5.1'