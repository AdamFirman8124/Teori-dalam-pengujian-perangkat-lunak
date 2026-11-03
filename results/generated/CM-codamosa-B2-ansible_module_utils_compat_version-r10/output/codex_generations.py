

# Generated at 2026-11-02 09:31:57.587711
# Unit test for method __lt__ of class Version
def test_Version___lt__():
# nonce:5ba72cfc
    import pytest

    class ConcreteVersion(Version):
        """Minimal concrete subclass implementing parse and _cmp."""

        def parse(self, vstring):
            self.version = tuple(int(p) for p in vstring.split('.'))

        def __str__(self):
            return '.'.join(str(p) for p in self.version)

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

    v1 = ConcreteVersion('1.0')
    v1_equal = ConcreteVersion('1.0')
    v2 = ConcreteVersion('1.1')

    # strictly smaller version compares less than
    assert v1.__lt__(v2) is True
    assert v1 < v2

    # equal versions are not less than each other
    assert v1.__lt__(v1_equal) is False
    assert not (v1 < v1_equal)

    # greater versions are not less than smaller ones
    assert v2.__lt__(v1) is False
    assert not (v2 < v1)

    # strings are parsed before comparison
    assert v1.__lt__('1.1') is True
    assert v1 < '1.1'
    assert not (v1 < '0.9')

    # NotImplemented from _cmp propagates, resulting in TypeError
    with pytest.raises(TypeError):
        v1 < object()

# Generated at 2026-11-02 09:34:27.967657
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    # Simple numeric versions
    v = LooseVersion('1.5.1')
    assert v.vstring == '1.5.1'
    assert v.version == [1, 5, 1]

    v = LooseVersion('161')
    assert v.vstring == '161'
    assert v.version == [161]

    v = LooseVersion('8.02')
    assert v.version == [8, 2]  # leading zero stripped by int conversion

    v = LooseVersion('1996.07.12')
    assert v.version == [1996, 7, 12]

    v = LooseVersion('0.960923')
    assert v.version == [0, 960923]

    v = LooseVersion('3.1.1.6')
    assert v.version == [3, 1, 1, 6]

    # Numeric + alphabetic components
    v = LooseVersion('1.5.2b2')
    assert v.version == [1, 5, 2, 'b', 2]

    v = LooseVersion('3.10a')
    assert v.version == [3, 10, 'a']

    v = LooseVersion('3.4j')
    assert v.version == [3, 4, 'j']

    v = LooseVersion('2g6')
    assert v.version == [2, 'g', 6]

    v = LooseVersion('11g')
    assert v.version == [11, 'g']

    v = LooseVersion('2.2beta29')
    assert v.version == [2, 2, 'beta', 29]

    v = LooseVersion('2.0b1pl0')
    assert v.version == [2, 0, 'b', 1, 'pl', 0]

    # Multi-letter components
    v = LooseVersion('3.2.pl0')
    assert v.version == [3, 2, 'pl', 0]

    v = LooseVersion('5.5.kw')
    assert v.version == [5, 5, 'kw']

    # Trailing non-matching characters are kept as strings
    v = LooseVersion('1.13++')
    assert v.version == [1, 13, '++']

    # Uppercase letters are not matched by component_re and survive as strings
    v = LooseVersion('3.4A')
    assert v.version == [3, 4, 'A']

    # parse can be called on an existing instance to re-parse
    v = LooseVersion('1.0')
    v.parse('2.1.3b4')
    assert v.vstring == '2.1.3b4'
    assert v.version == [2, 1, 3, 'b', 4]

    # Constructing with no argument leaves version unset
    v = LooseVersion()
    try:
        v.version
        assert False, "expected AttributeError"
    except AttributeError:
        pass

# Generated at 2026-11-02 09:38:04.945721
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    test_cases = [
        # (input version string, expected __str__ output)
        ('0.4', '0.4'),
        ('0.4.0', '0.4'),        # zero patch component is dropped
        ('0.4.1', '0.4.1'),
        ('0.5a1', '0.5a1'),
        ('0.5b3', '0.5b3'),
        ('0.5', '0.5'),
        ('0.9.6', '0.9.6'),
        ('1.0', '1.0'),
        ('1.0.0', '1.0'),        # zero patch component is dropped
        ('1.0.4a3', '1.0.4a3'),
        ('1.0.4b1', '1.0.4b1'),
        ('1.0.4', '1.0.4'),
        ('2.7.12', '2.7.12'),
        ('10.20.30', '10.20.30'),
        ('1.1a0', '1.1a0'),
    ]

    for vstring, expected in test_cases:
        version = StrictVersion(vstring)
        actual = str(version)
        assert actual == expected, \
            "str(StrictVersion(%r)) returned %r, expected %r" % (vstring, actual, expected)

        # __str__ output should round-trip through parse
        reparsed = StrictVersion(actual)
        assert str(reparsed) == expected, \
            "round-trip of %r produced %r, expected %r" % (vstring, str(reparsed), expected)

    # __repr__ should generate code that recreates the instance
    version = StrictVersion('1.0.4a3')
    assert repr(version) == "StrictVersion ('1.0.4a3')"