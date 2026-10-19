

# Generated at 2022-06-12 23:59:32.260474
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    version = StrictVersion("0.4.1")
    assert version.version == (0, 4, 1)
    assert version.prerelease is None

    version = StrictVersion("0.4")
    assert version.version == (0, 4, 0)
    assert version.prerelease is None

    version = StrictVersion("0.4.0")
    assert version.version == (0, 4, 0)
    assert version.prerelease is None

    version = StrictVersion("0.5a1")
    assert version.version == (0, 5, 0)
    assert version.prerelease == ('a', 1)

    version = StrictVersion("0.5b3")
    assert version.version == (0, 5, 0)
    assert version.prerelease == ('b', 3)


# Generated at 2022-06-12 23:59:37.936802
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    ver = Version()
    assert (ver.__lt__(None) is NotImplemented)


    class MyVersion(Version):
        def __init__(self, vstring=None):
            Version.__init__(self, vstring)

        def parse(self, vstring):
            self.vstring = vstring

        def _cmp(self, other):
            raise Exception()
    v1 = MyVersion('foo')
    v2 = MyVersion('bar')
    assert (v1 < v2)



# Generated at 2022-06-12 23:59:39.174409
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    Version(vstring="1.0").__gt__("1.0")

# Generated at 2022-06-12 23:59:47.002980
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    sv = StrictVersion()
    sv.parse('1.2.0')
    assert str(sv) == '1.2.0'
    sv.parse('1.2a3')
    assert str(sv) == '1.2a3'
    sv.parse('1.2.0.0.0')
    assert str(sv) == '1.2'
    try:
        sv.parse('1.2.a')
        assert False
    except ValueError:
        pass


# Generated at 2022-06-12 23:59:50.281646
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v1.parse('1.0')

    v2 = Version()
    v2.parse('1.1')

    assert v2.__gt__(v1) == True, 'test_Version___gt__() failed'


# Generated at 2022-06-12 23:59:54.541801
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    l = ['a', '1', '1.0', '1.0c', '1.2.3b1', '1.3c4', '2.7.2.2', '1.3.a4', '1.3pl1']
    for v in l:
        try:
            StrictVersion(v)
            print('version', v, 'is valid')
        except ValueError as e:
            print('version', v, 'is invalid')

# Generated at 2022-06-12 23:59:56.464748
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert (Version('1.2.0') < Version('1.2.1'))



# Generated at 2022-06-12 23:59:59.134606
# Unit test for method __le__ of class Version
def test_Version___le__():
    version = Version('1.2.2')
    version2 = Version('1.2.1')
    assert version.__le__(version2) is False

# Generated at 2022-06-13 00:00:00.632093
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    print('Testing method __str__ of class StrictVersion')

# Generated at 2022-06-13 00:00:07.731944
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():

    v = StrictVersion('1.2.3')
    assert '1.2.3' == str(v)

    v = StrictVersion('1.2.0')
    assert '1.2' == str(v)

    v = StrictVersion('1.2.0')
    assert '1.2' == str(v)

    v = StrictVersion('1.2')
    assert '1.2' == str(v)

    v = StrictVersion('1.2a3')
    assert '1.2a3' == str(v)

    v = StrictVersion('1.2.3a4')
    assert '1.2.3a4' == str(v)


# Generated at 2022-06-13 00:00:19.021832
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils2.version import StrictVersion
    v = StrictVersion('1.2')
    assert v < '1.4'


# Generated at 2022-06-13 00:00:25.037680
# Unit test for method __le__ of class Version
def test_Version___le__():
    class X(Version):
        def parse(self, vstring):
            self.vstring = vstring
        def _cmp(self, other):
            if isinstance(other, str):
                other = X(other)
            return NotImplemented
    x = X('1.2')
    assert x <= '1.2'
    assert x <= X('1.2')
    assert not x <= X('1.3')
    assert not x <= '1.3'

    assert x <= '1.2.0'
    assert not x <= '1.1.9.9'
    assert x <= '1.0'
    assert x <= '2.0'


# Generated at 2022-06-13 00:00:26.607724
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v.__ge__(1) is NotImplemented

# Generated at 2022-06-13 00:00:29.537709
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()

    v._cmp = lambda other: NotImplemented
    assert v > 5 == NotImplemented

    v._cmp = lambda other: 6
    assert v > 5 == True

    v._cmp = lambda other: 4
    assert v > 5 == False


# Generated at 2022-06-13 00:00:32.529270
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # It's not possible to write a test
    raise NotImplementedError()

# Generated at 2022-06-13 00:00:39.400908
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Called with a string, this should call self.parse(other)
    # Note that this is the implementation of __lt__ for StrictVersion
    # StandardVersion and LooseVersion implement a different __lt__
    # method, so this test will not catch that class
    ver1 = Version("2.2a1")
    ver2 = Version("2.2")
    assert (ver1 < ver2)
# End of unit test for method __lt__ of class Version


# Generated at 2022-06-13 00:00:40.509935
# Unit test for method __gt__ of class Version
def test_Version___gt__():
  obj = TestVersion()
  output = obj.__gt__()
  assert type(output) == bool

# Generated at 2022-06-13 00:00:42.111632
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import distutils.version
    v = distutils.version.Version('0.0.0')
    assert v == '0.0.0'


# Generated at 2022-06-13 00:00:43.672592
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version()
    v2 = Version()
    assert not v1.__le__(v2)


_Version__le__ = test_Version___le__


# Generated at 2022-06-13 00:00:50.965542
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    """Unit test for method __gt__ of class Version."""

    from distutils.version import Version

    assert Version("1.0") > Version("0.1")
    assert Version("1.0") > Version("0.1.0")
    assert Version("1.0") > Version("1.0rc1")
    assert not (Version("1.0") > Version("1.0a1"))
    assert not (Version("1.0") > Version("1.0.post1"))



# Generated at 2022-06-13 00:01:08.869228
# Unit test for method __le__ of class Version
def test_Version___le__():
    import unittest

    class TestVersion(Version):
        def __init__(self, vstring):
            self.vstring = vstring
        def parse(self, vstring):
            self.vstring = vstring
        def __str__(self):
            return self.vstring

        def _cmp(self, other):
            if hasattr(other, "vstring"):
                return cmp(self.vstring, other.vstring)
            else:
                return cmp(self.vstring, other)

    class TestVersion_ClassImplements_LE(unittest.TestCase):
        def test_should_return_true_when_equal(self):
            v1 = TestVersion("v1")
            v2 = TestVersion("v1")
            self.assertTrue(v1 <= v2)
           

# Generated at 2022-06-13 00:01:10.439542
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import version
    v = version.Version('1.0')
    assert v < '1.1'

# Generated at 2022-06-13 00:01:11.608598
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1') == Version('1')


# Generated at 2022-06-13 00:01:13.716266
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    version = Version("short.version")

    assert version == Version("short.version")

    assert not version == Version("longer.version")



# Generated at 2022-06-13 00:01:17.669942
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    l1 = Version('1.0.0')
    l2 = Version('1.0.1')
    l3 = Version('1.1.0')
    l4 = Version('2.0.0')
    assert l1 < l2 and l1 < l3 and l1 < l4
    assert l2 < l3 and l2 < l4 and l3 < l4

# Generated at 2022-06-13 00:01:18.703832
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    pass


# Generated at 2022-06-13 00:01:20.328421
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1.1').__eq__(Version('1.1'))

# Generated at 2022-06-13 00:01:21.860981
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    # tests for __ge__ in class Version
    assert v is not None


# Generated at 2022-06-13 00:01:24.879041
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    version_v1 = Version(vstring='')
    version_v2 = Version(vstring='\x01\x02\x03')
    version_v1.parse('1')
    version_v2.parse('2')
    assert version_v1 != version_v2


# Generated at 2022-06-13 00:01:27.393607
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version('1.0') > Version('1.0alpha1')
    assert Version('1.0') > '1.0alpha1'

# Generated at 2022-06-13 00:01:36.556046
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version("1.0")
    v2 = Version("2.0")
    assert v1 < v2

# Generated at 2022-06-13 00:01:39.124005
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.0')
    v2 = Version('1.1')
    assert v1 < v2


# Generated at 2022-06-13 00:01:48.289316
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from collections.abc import Iterable
    from distutils.version import LooseVersion
    from distutils.version import Version
    from distutils.version import StrictVersion
    from distutils.version import _Version
    from distutils.version import IrrationalVersionError
    from distutils.version import _parse_version_info
    from distutils.version import _parse_version_parts
    from distutils.version import _parse_partial_version
    from distutils.version import _legacy_cmp

    # Create an instance of Version class
    version = Version()

    # Assign instance attributes
    version.__dict__['_version'] = _Version(['0', '0', '0'])

    # Call the method to test
    result = version.__lt__('_version')

    assert isinstance(result, bool)

# Generated at 2022-06-13 00:01:50.658740
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    for cls in StrictVersion, LooseVersion:
        assert cls('1.2.3') == cls('1.2.3')  # lgtm [py/comparison-in-boolean]

# Generated at 2022-06-13 00:01:55.196784
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('2.2')
    assert v >= '2.2'

# Generated at 2022-06-13 00:01:58.205871
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__('') is NotImplemented
    assert v.__gt__('1') == 1
    assert v.__gt__(2) == 1

# Generated at 2022-06-13 00:02:00.960762
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    a = Version('1.2.3')
    b = Version('1.2.3')
    c = Version('1.2.4')
    assert a == b
    assert a != c


# Generated at 2022-06-13 00:02:13.684027
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from types import ClassType
    from distutils.version import Version

    class DummyVersion(Version):

        def parse(self, vstring):
            self.set((1, 2, 3))

        def get_version(self):
            return (1, 2, 3)


    class DummyVersion2(Version):

        def parse(self, vstring):
            self.set((1, 2, 4))

        def get_version(self):
            return (1, 2, 4)

    v = DummyVersion()
    assert v.__class__ == DummyVersion
    assert v.__class__ == DummyVersion
    assert v.__class__ == DummyVersion
    v2 = DummyVersion()
    assert v < v2

    v3 = DummyVersion2()
    assert v3.__class__ == Dummy

# Generated at 2022-06-13 00:02:16.695915
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    v2 = Version()
    print(v1 == v2)


# Generated at 2022-06-13 00:02:21.093903
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert True == (Version("1.1") == Version("1.1"))
    assert False == (Version("1.2") == Version("1.1"))


# Generated at 2022-06-13 00:02:36.461599
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    q = Version.__eq__
    assert q(v1, v1)
    assert q(v1, "1.2")



# Generated at 2022-06-13 00:02:38.082509
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.2-3')
    assert (v == v)

# Generated at 2022-06-13 00:02:42.302264
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version('1.2')
    assert v <= '1.2'
    assert v <= '1.2.0'
    assert not v <= '1.2.0.0'
    assert not v <= '1.1'
    assert not v <= '1.3'
    assert not v <= '2.2'

# Generated at 2022-06-13 00:02:46.111333
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('2.0') == Version('2.0')
    assert Version('2.0') == '2.0'
    assert Version('2.0') != Version('1.0')
    assert Version('2.0') != '1.0'

from distutils.version import _predicate

from distutils.version import _LegacyVersion



# Generated at 2022-06-13 00:02:57.942224
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import Version
    from distutils.version import LooseVersion
    # Ensure that method Version.__ge__ always invoke method LooseVersion._cmp
    class TestVersion(Version):
        def parse(self, vstring):
            # Version.parse is implemented as a regexp
            self.version = []
            for part in vstring.split('.'):
                try:
                    self.version.append(int(part))
                except ValueError:
                    self.version.append(part)
            self.vstring = vstring
            self.is_prerelease = None
    v1 = TestVersion('1.0.0')
    v2 = TestVersion('2.0.0')
    assert not (v1 < v2)
    assert not (v1 <= v2)
    assert not (v1 == v2)

# Generated at 2022-06-13 00:03:02.316648
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import StrictVersion
    # call StrictVersion.__le__(self, other)
    version = StrictVersion(1)
    assert version.__le__(1)
    try:
        version.__le__(1.0)
    except TypeError:
        pass
    else:
        raise AssertionError



# Generated at 2022-06-13 00:03:05.736688
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version()
    assert v1.__ge__(v1)
    v2 = Version()
    assert v2.__ge__(v1)
    assert v1.__ge__(v2)
    # PSF-license


# Generated at 2022-06-13 00:03:14.733656
# Unit test for method __le__ of class Version
def test_Version___le__():
    # Test with literal parameters
    assert Version('0.0.0') <= Version('0.0.1')
    assert Version('0.0.0') <= Version('0.1.1')
    assert Version('0.0.0') <= Version('1.1.1')
    assert not Version('1.1.1') <= Version('0.0.0')
    assert Version('0.0.1') <= Version('0.1.1')
    assert Version('0.1.1') <= Version('1.1.1')
    assert not Version('1.1.1') <= Version('0.1.1')
    assert Version('1.2.1') <= Version('1.2.1')
    assert not Version('1.2.1') <= Version('1.2.0')

# Generated at 2022-06-13 00:03:16.123581
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version

    assert Version('1').__eq__('1') == 0

# Generated at 2022-06-13 00:03:18.620408
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.tests import support
    v = support.make_legacy_dist()['version']
    assert (v == '1.0')



# Generated at 2022-06-13 00:03:40.902842
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('10') >= Version('10')
    assert Version('10') >= '10'
    assert Version('10') >= 9
    assert Version('10') >= [9]
    assert not (Version('10') >= Version('11'))
    assert not (Version('10') >= '11')
    assert not (Version('10') >= 11)
    assert not (Version('10') >= [11])




# Generated at 2022-06-13 00:03:48.544057
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert not (LooseVersion("0.0.1a1") > LooseVersion("0.0.1a1"))
    assert LooseVersion("0.0.1a1") > LooseVersion("0.0.1a0")
    assert not (LooseVersion("0.0.1a1") > LooseVersion("0.0.1a1.post1"))
    assert not (LooseVersion("0.0.1a1") > None)
    assert LooseVersion("0.0.1a1") > "0.0.1a0"
    assert not (LooseVersion("0.0.1a1") > "0.0.1a1")
    assert not (LooseVersion("1.1a1") > LooseVersion("2.0.0"))
    assert LooseVersion(None) > Lo

# Generated at 2022-06-13 00:03:55.426808
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version('1.2.3')
    assert v1 > '1.2.0'
    assert v1 > '1.2'
    assert v1 > '1.0'
    assert v1 > '1'
    assert v1 > '0.9'

    assert '1.2.0' < v1
    assert '1.2' < v1
    assert '1.0' < v1
    assert '1' < v1
    assert '0.9' < v1



# Generated at 2022-06-13 00:03:56.977617
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.0')
    assert v == '1.0'


# Generated at 2022-06-13 00:04:00.498816
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest
    class Version___gt__(unittest.TestCase):
        def test_0(self):
            v = Version()
            self.assertEqual(v.__gt__(''), NotImplemented)
    return Version___gt__

# Generated at 2022-06-13 00:04:10.652355
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    global __test_id, __test_val, __test_exc
    __test_id = "Version.__eq__()"
    __test_val = None
    __test_exc = None

    def test_func():
        v1 = Version('0.0.0')
        v2 = Version('1.1.1')
        v3 = 'not a Version instance'


# Generated at 2022-06-13 00:04:18.853312
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v2 = Version()
    v1.parse('1.2.3')
    v2.parse('1.2.3-alpha1')
    assert v1.__gt__(v2) == False
    v1.parse('1.2.3-alpha1')
    v2.parse('1.2.3')
    assert v1.__gt__(v2) == True


# Generated at 2022-06-13 00:04:25.959575
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Test method Version.__lt__ with arguments from testcases
    """
    a = Version()
    b = Version(vstring='1.0')
    c = Version(vstring='1.5')
    d = Version(vstring='2.0')
    e = Version(vstring='1.2a1')
    f = Version(vstring='1.2.b1')
    g = Version(vstring='1.2.dev456')
    h = Version(vstring='1.2')
    i = Version(vstring='1.2.post345')
    j = Version(vstring='1.2.post456')
    k = Version(vstring='1.2+abc')
    l = Version(vstring='1.2+abc.456')

# Generated at 2022-06-13 00:04:28.794161
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert (v >= "1.2.3") == False


# Generated at 2022-06-13 00:04:29.716327
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version() <= Version()

# Generated at 2022-06-13 00:04:47.850909
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # Only run this test if class Version exists
    if 'Version' in globals():
        # Test Version.__ge__
        inst = Version()
        Version.__ge__( inst, None )


# Generated at 2022-06-13 00:04:57.649194
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    V = Version()
    def ok(v):
        return v < ''
    assert ok(Version())
    V = Version()
    def ok(v):
        return v < '1'
    assert not ok(Version())
    V = Version()
    def ok(v):
        return v < '1'
    assert ok(Version('0'))
    V = Version()
    def ok(v):
        return v < '1'
    assert not ok(Version('1'))
    V = Version()
    def ok(v):
        return v < '1'
    assert not ok(Version('1.1'))

# Generated at 2022-06-13 00:05:07.373902
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from ansible.parsing.version import Version

    assert Version('1.0a') < Version('1.0')
    assert Version('1.1') < Version('1.2')
    assert Version('2.0') < Version('2.1')
    assert Version('0.4.0') < Version('1.2')
    assert Version('1.2.0') < Version('1.2.1')
    assert Version('1.2.0') < Version('1.2.1.1')

    assert not Version('1.2.0') < Version('1.2.0')

    assert not Version('1.0') < Version('1.0a')
    assert not Version('1.2') < Version('1.1')
    assert not Version('2.1') < Version('2.0')
    assert not Version

# Generated at 2022-06-13 00:05:07.965286
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v == v


# Generated at 2022-06-13 00:05:09.333280
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    x = Version('1.0')
    y = Version('1.0')
    assert x >= y


# Generated at 2022-06-13 00:05:11.043946
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    v2 = Version()
    assert v1.__eq__(v2) == NotImplemented


# Generated at 2022-06-13 00:05:18.204849
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import pytest
    import distutils.version
    pytest.skip('Not a unit test.')
    print(distutils.version.__name__)
    print(dir(distutils.version))
    ver = distutils.version.Version('1.2')
    assert ver.__eq__(ver) == True
    assert ver.__eq__(object()) == NotImplemented

# Generated at 2022-06-13 00:05:21.503363
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Version.__eq__(Version(''), '')
    # Version.__eq__(Version('1'), '')
    # Version.__eq__(Version('1'), '1')
    pass

# Generated at 2022-06-13 00:05:23.830424
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from version import Version
    v = Version("1.3.3")
    assert v == "1.3.3"
    assert v == Version("1.3.3")

# Generated at 2022-06-13 00:05:27.300333
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    v._cmp = lambda x: 0
    assert (v >= Version())

    v._cmp = lambda x: 1
    assert (v >= Version())

    v._cmp = lambda x: -1
    assert not (v >= Version())

    v._cmp = lambda x: NotImplemented
    with pytest.raises(RuntimeError):
        v >= Version()

# Generated at 2022-06-13 00:05:50.807128
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import __main__
    class Version(__main__.Version):
        def _cmp(self, other):
            return -1

    assert Version("3.3") < Version("3.4")
    assert Version("3.3") < Version("4.0.0")
    assert Version("3.3") < Version("4.0.0.dev")
    assert Version("3.3") < Version("4.0.0.dev0")
    assert Version("3.3") < Version("4.0.0.dev1")
    assert Version("3.3") < Version("4.0.0.post0")
    assert Version("3.3") < Version("4.0.0.post1")


# Generated at 2022-06-13 00:05:53.328638
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    test = Version()
    c = test._cmp(None)
    if c is NotImplemented:
        c = 0
    return c >= -1

# Generated at 2022-06-13 00:05:54.728880
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    assert isinstance(v1.__lt__(v2), bool)

# Generated at 2022-06-13 00:05:56.405429
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('1.0') >= Version('1.0')
    assert Version('1.0') >= '1.0'


# Generated at 2022-06-13 00:05:58.168422
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1.0') == '1.0'



# Generated at 2022-06-13 00:06:03.210521
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class Version(version.Version):
        def _cmp(self, other):
            pass
    v1 = Version()
    v2 = Version()
    x = v1 >= v2
    if isinstance(x, bool):
        pass
    else:
        raise AssertionError


# Generated at 2022-06-13 00:06:05.396321
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version('1.0')
    v2 = Version('1.1')
    assert v1.__ge__(v2) == False


# Generated at 2022-06-13 00:06:06.268705
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version() < Version()

# Generated at 2022-06-13 00:06:08.613998
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import StrictVersion
    v = StrictVersion("1.1")
    assert (v == "1.1") == True
    assert (v == "1.2") == False

# Generated at 2022-06-13 00:06:09.551910
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version() < '1'

# Generated at 2022-06-13 00:07:36.234116
# Unit test for method __ge__ of class Version
def test_Version___ge__():
  v = Version()
  v2 = Version()
  assert v >= v2

# Generated at 2022-06-13 00:07:38.974165
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    global VersionApplication
    VersionApplication = Version("10.0.0")
    global VersionApplication
    assert VersionApplication >= "0.0.0"
    global VersionApplication
    assert VersionApplication >= "10.0.0"
    global VersionApplication
    assert not VersionApplication >= "10.0.1"

# Generated at 2022-06-13 00:07:41.821736
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    def check(obj1, obj2, result):
        assert (obj1 == obj2) == result

    v1 = Version("1.0")
    v2 = Version("2.0")
    check(v1, v1, True)
    check(v1, v2, False)

# Generated at 2022-06-13 00:07:42.711778
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v >= Version('1')

# Generated at 2022-06-13 00:07:47.560889
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # Tests for class Version
    v = Version() # tests for instance initialization
    assert v == (0,) # tests for version equivalence
    assert v >= (0,)
    assert not (v > (0,)) # tests for version ordering
    assert v < (1,)
    assert v <= (1,)
    assert (1,) > v
    assert (1,) >= v
    v = Version('1.2a2') # tests for initialization from string
    assert v == (1, 2, 'a', 2) # tests for version equivalence
    assert v >= (1, 2, 'a', 2)
    assert not (v > (1, 2, 'a', 2)) # tests for version ordering
    assert v < (1, 2, 'a', 3)
    assert v <= (1, 2, 'a', 3)

# Generated at 2022-06-13 00:07:55.775377
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    for text, version in [("1.2.3", (1, 2, 3)),
                          ("1.2a2", (1, 2, "a", 2)),
                          ("1.2.3b1", (1, 2, 3, "b", 1)),
                          ("2.2g6", (2, 2, "g", 6)),
                          ("2.2beta29", (2, 2, "beta", 29)),
                          ("1.13++", (1, 13, "++")),
                          ("5.5.kw", (5, 5, "kw")),
                          ("2.0b1pl0", (2, 0, "b", 1, "pl", 0))]:
        lv = LooseVersion(text)
        assert lv.version == version, (text, lv.version)

# Generated at 2022-06-13 00:07:56.520924
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    pass

# Generated at 2022-06-13 00:08:04.753578
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    """Unit test for method __eq__ of class Version."""

    import sys

    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    import distutils.version

    # First, we construct a few version objects to use for testing:

# Generated at 2022-06-13 00:08:13.287248
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('1.2')
    try:
        assert(v >= v)
        assert(v >= '1.2')
        assert(v >= '1.0')
        assert(v >= 1.0)
        assert(v >= '1.2.3')
        assert(v >= 1.2)
        assert(v >= 1.2)
        assert(v >= 1)
        assert(v >= '1')
        assert(v >= '1.2a')
        assert(v >= '1.2.a')
        assert(v >= '1.2.a.a')
    except:
        return



# Generated at 2022-06-13 00:08:16.899991
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # assert (Version('1.2') == 1.2) == 0
    # assert (Version('1.5') == 1.2) == 1
    # assert (Version('1.5') == 1.6) == -1

    assert (Version('0.2.8.dev0') == '0.2.8.dev0') == 0