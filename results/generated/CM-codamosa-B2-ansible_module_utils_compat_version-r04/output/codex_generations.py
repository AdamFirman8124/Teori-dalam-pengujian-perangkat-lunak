

# Generated at 2026-11-02 13:49:52.528719
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    '''Unit test for method __eq__ of class Version'''

    class ConcreteVersion(Version):
        """Minimal concrete Version subclass providing _cmp for testing."""

        def __init__(self, vstring=None, value=0):
            Version.__init__(self, vstring)
            self.value = value

        def __str__(self):
            return str(self.value)

        def _cmp(self, other):
            if isinstance(other, ConcreteVersion):
                other_value = other.value
            elif isinstance(other, str):
                other_value = ConcreteVersion(other).value
            else:
                return NotImplemented
            return (self.value > other_value) - (self.value < other_value)

    # Identical values compare equal
    assert ConcreteVersion(value=1) == ConcreteVersion(value=1)

    # An instance compares equal to itself
    v = ConcreteVersion(value=5)
    assert v == v

    # Different values do not compare equal
    assert not (ConcreteVersion(value=1) == ConcreteVersion(value=2))

    # Comparison against a string that parses to an equal version
    assert ConcreteVersion(value=3) == ConcreteVersion('3')

    # Comparison against a string that parses to a different version
    assert not (ConcreteVersion(value=3) == ConcreteVersion('4'))

    # _cmp returning NotImplemented propagates out of __eq__
    assert ConcreteVersion(value=1).__eq__(42) is NotImplemented

    # When both sides return NotImplemented, == falls back to identity
    assert not (ConcreteVersion(value=1) == 42)

    # The abstract Version class has no _cmp, so == delegates and fails
    try:
        Version('1') == Version('1')
    except AttributeError:
        pass
    else:
        assert False, "expected AttributeError from missing _cmp"

# Generated at 2026-11-02 13:52:36.463940
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from ansible.module_utils.compat.version import Version

    class ConcreteVersion(Version):
        """Concrete subclass implementing _cmp for testing Version.__lt__."""

        def parse(self, vstring):
            self.vstring = vstring
            self.version = tuple(int(p) for p in vstring.split('.'))

        def __str__(self):
            return self.vstring

        def _cmp(self, other):
            if isinstance(other, str):
                other = ConcreteVersion(other)
            if not isinstance(other, ConcreteVersion):
                return NotImplemented
            if self.version < other.version:
                return -1
            if self.version > other.version:
                return 1
            return 0

    # Less than
    assert ConcreteVersion('1.0') < ConcreteVersion('2.0')
    assert ConcreteVersion('1.0') < '2.0'
    # Not less than
    assert not (ConcreteVersion('2.0') < ConcreteVersion('1.0'))
    assert not (ConcreteVersion('1.0') < ConcreteVersion('1.0'))
    assert not (ConcreteVersion('2.0') < '1.0')
    # NotImplemented path: comparison with unsupported type raises TypeError
    try:
        ConcreteVersion('1.0') < 123
        assert False, "Expected TypeError for unsupported comparison type"
    except TypeError:
        pass

# Generated at 2026-11-02 13:54:30.171495
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    # Two-component versions
    assert str(StrictVersion('0.4')) == '0.4'
    assert str(StrictVersion('1.0')) == '1.0'
    assert str(StrictVersion('2.13')) == '2.13'

    # Three-component version with zero patch collapses to two components
    assert str(StrictVersion('0.4.0')) == '0.4'
    assert str(StrictVersion('1.0.0')) == '1.0'

    # Three-component versions with non-zero patch
    assert str(StrictVersion('0.4.1')) == '0.4.1'
    assert str(StrictVersion('0.9.6')) == '0.9.6'
    assert str(StrictVersion('1.0.4')) == '1.0.4'

    # Prerelease versions without a patch component
    assert str(StrictVersion('0.5a1')) == '0.5a1'
    assert str(StrictVersion('0.5b3')) == '0.5b3'
    assert str(StrictVersion('1.0a2')) == '1.0a2'
    assert str(StrictVersion('1.0b10')) == '1.0b10'

    # Prerelease versions with a non-zero patch component
    assert str(StrictVersion('1.0.4a3')) == '1.0.4a3'
    assert str(StrictVersion('1.0.4b1')) == '1.0.4b1'
    assert str(StrictVersion('2.7.2a0')) == '2.7.2a0'

    # __str__ output should round-trip through parse
    for vstring in ('0.4', '0.4.0', '0.4.1', '0.5a1', '0.5b3',
                    '0.9.6', '1.0', '1.0.4a3', '1.0.4b1', '1.0.4'):
        assert str(StrictVersion(StrictVersion(vstring))) == \
            str(StrictVersion(vstring))

# Generated at 2026-11-02 13:56:16.153124
# Unit test for method __str__ of class LooseVersion
def test_LooseVersion___str__():
    # nonce:02d9c01f
    vstrings = [
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
    for vstring in vstrings:
        v = LooseVersion(vstring)
        assert str(v) == vstring, \
            "str(LooseVersion(%r)) should return %r, got %r" % (
                vstring, vstring, str(v))

    # __str__ must return the exact string passed to parse
    v = LooseVersion('9.9.9')
    v.parse('4.5.6a1')
    assert str(v) == '4.5.6a1'