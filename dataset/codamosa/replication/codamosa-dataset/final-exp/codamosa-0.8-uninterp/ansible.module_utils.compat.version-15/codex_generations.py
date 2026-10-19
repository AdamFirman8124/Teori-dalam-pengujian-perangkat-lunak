

# Generated at 2022-06-12 23:59:20.064779
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version("1.0") <= Version("1.0")
    assert Version("1.0") <= Version("1.1")
    assert not Version("1.1") <= Version("1.0")

# Generated at 2022-06-12 23:59:29.961032
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import LooseVersion
    import unittest

    class TestVersion_ge(unittest.TestCase):

        def test__ge(self):
            # test that instances of Version are ordered correctly

            # as defined by LooseVersion

            # examples from the docstring
            self.assertTrue(LooseVersion('1.2.0') >= LooseVersion('1.2'))
            self.assertTrue(LooseVersion('1.2.0') >= LooseVersion('1.2.0'))
            self.assertTrue(LooseVersion('1.2.0') >= LooseVersion('1.2b1'))
            self.assertTrue(LooseVersion('1.2.1') >= LooseVersion('1.2.0'))

# Generated at 2022-06-12 23:59:32.009209
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version()
    assert v.__lt__(1) is NotImplemented

# Generated at 2022-06-12 23:59:33.709049
# Unit test for method __lt__ of class Version
def test_Version___lt__():assert_equals(Version("1.0").__lt__("1.1"),True)

# Generated at 2022-06-12 23:59:35.639327
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    a = Version("2.3.3")
    b = Version("2.3.3")
    assert a <= b


# Generated at 2022-06-12 23:59:42.572858
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    for s in [
        '1.2', '2.0', '1.2.3', '1.2.3a1', '1.2.3b2',
        '1.2.3.4', '1.2.3a1.post345', '1.2.3a1.dev345',
    ]:
        version = StrictVersion(s)
        assert s == str(version), '%s != %s' % (s, str(version))



# Generated at 2022-06-12 23:59:43.895089
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    o = Version()
    assert(o == o._cmp(o))



# Generated at 2022-06-12 23:59:52.883249
# Unit test for method __str__ of class StrictVersion

# Generated at 2022-06-12 23:59:54.302725
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    return None


# Generated at 2022-06-13 00:00:04.256602
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion('1').__str__() == '1'
    assert StrictVersion('1.2').__str__() == '1.2'
    assert StrictVersion('1.2.0').__str__() == '1.2'
    assert StrictVersion('1.2.0a0').__str__() == '1.2a0'
    assert StrictVersion('1.2.0b1').__str__() == '1.2b1'
    assert StrictVersion('1.2.0.0').__str__() == '1.2'
    assert StrictVersion('1.2.0.0a0').__str__() == '1.2a0'
    assert StrictVersion('1.2.0.0b1').__str__() == '1.2b1'
   

# Generated at 2022-06-13 00:00:16.632442
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    ver = Version()
    assert ver == ver
    assert ver != 'string'



# Generated at 2022-06-13 00:00:24.460225
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion('0.4').__str__() == '0.4'
    assert StrictVersion('0.4.0').__str__() == '0.4.0'
    assert StrictVersion('0.4.3').__str__() == '0.4.3'
    assert StrictVersion('0.4a0').__str__() == '0.4a0'
    assert StrictVersion('0.4a3').__str__() == '0.4a3'
    assert StrictVersion('0.4b0').__str__() == '0.4b0'
    assert StrictVersion('0.4b3').__str__() == '0.4b3'
    assert StrictVersion('0.9.6').__str__() == '0.9.6'
# Unit test

# Generated at 2022-06-13 00:00:27.356777
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    v.parse('1.5a')

    assert v > '1.3'
    assert v > '1.5'
    assert v >= '1.5'
    assert v >= '1.5a'

# Generated at 2022-06-13 00:00:28.194422
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    r = True
    return r

# Generated at 2022-06-13 00:00:32.713212
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():

    import unittest

    class StrictVersion___str__TestCase(unittest.TestCase):

        def test(self):
            sv1 = StrictVersion('1.0.0')
            self.assertEqual(str(sv1), '1.0.0')
            sv2 = StrictVersion('1.0a1')
            self.assertEqual(str(sv2), '1.0a1')

    unittest.main(StrictVersion___str__TestCase, None, verbosity=2)

if __name__ == '__main__':
    test_StrictVersion___str__()



# Generated at 2022-06-13 00:00:40.919520
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert str(StrictVersion('1.0')) == '1.0'
    assert str(StrictVersion('1.0.0')) == '1.0'
    assert str(StrictVersion('1.0a1')) == '1.0a1'
    assert str(StrictVersion('1.0.0a1')) == '1.0a1'
    assert str(StrictVersion('1.0b2')) == '1.0b2'
    assert str(StrictVersion('1.0.0b2')) == '1.0b2'



# Generated at 2022-06-13 00:00:45.519034
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    ver1 = Version('1')
    assert ver1 < '2'
    assert ver1 < '1.2'
    assert not ver1 < '1.0'



# Generated at 2022-06-13 00:00:49.854956
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    v = StrictVersion('1.2.4')
    assert str(v) == '1.2.4'

    v = StrictVersion('1.2.4a1')
    assert str(v) == '1.2.4a1'



# Generated at 2022-06-13 00:01:00.395300
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import nose.tools
    class A(Version):
        def __init__(self, vstring=None, version_info=None):
            self.version_info = version_info or (1, 0, 0)
            Version.__init__(self, vstring)
        def parse(self, vstring):
            if vstring is not None:
                self.version_info = [int(x) for x in vstring.split('.')]
        def _cmp(self, other):
            if isinstance(other, str):
                other = self.__class__(other)
            try: nose.tools.assert_true(isinstance(other, self.__class__))
            except: raise TypeError(type(other))
            return cmp(self.version_info, other.version_info)

# Generated at 2022-06-13 00:01:01.434751
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    pass


# Generated at 2022-06-13 00:01:07.926736
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version('1.3')
    v2 = Version('2.0')
    assert v1.__gt__(v2) == False


# Generated at 2022-06-13 00:01:09.156466
# Unit test for method __gt__ of class Version
def test_Version___gt__():
  # gt(arg0: Version) -> int
  pass


# Generated at 2022-06-13 00:01:10.041399
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import pytest
    assert True



# Generated at 2022-06-13 00:01:12.824540
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v1.parse('1.3a3')
    v2 = Version()
    v2.parse('1.3a4')
    return v1 > v2

# Generated at 2022-06-13 00:01:19.829882
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    Version_ = Version()



import os
import sys
import struct

try:
    import io
except ImportError:
    # Python < 2.6
    io = None

__all__ = ['VendorImporter']

# This is the base prefix where the vendored packages will be imported from.
VENDOR_BASE = os.path.join(os.path.dirname(__file__), 'vendor')

# This is a version identifier used to know the version of the vendored
# packages.
VENDOR_VERSION_ID = 'RANCHER-VENDOR-VERSION'

# This dictionary will contain all of the vendored packages and the path
# to their root within the vendored directory.

# Generated at 2022-06-13 00:01:20.842014
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    return v1 < v2


# Generated at 2022-06-13 00:01:26.178109
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v1.parse("1.0")
    v2 = Version()
    v2.parse("2.0")
#Test normal case
    assert v1 < v2
#Test Right side is a str
    assert v1 < "2.0"
    pass



# Generated at 2022-06-13 00:01:31.295569
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils.version import Version
    v = Version(0, 0, 1)
    assert v < Version(0, 0, 2)
    assert v < Version(0, 1, 0)
    assert v < Version(1, 0, 0)
    assert not v < Version(0, 0, 0)
    assert not v < Version(0, 0, 1)



# Generated at 2022-06-13 00:01:37.188718
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    instance = Version()
    # AssertionError: expected NotImplemented, got -1
    if instance._cmp('str'):
        raise AssertionError("expected NotImplemented, got %r" %
            (instance._cmp('str'),))
    # AssertionError: expected False, got True
    if instance > 'str':
        raise AssertionError("expected False, got True")
    # AssertionError: expected True, got False
    if instance < 'str':
        raise AssertionError("expected True, got False")

# Generated at 2022-06-13 00:01:39.559915
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # v = Version()
    # v2 = Version()
    # compare(v < v2, 0)
    pass

# Generated at 2022-06-13 00:01:52.567528
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class VersionTest(Version):
        def parse(self, vstring):
            self.v = int(vstring)
        # Unit test for method _cmp of class VersionTest
        def test___cmp__():
            self.assertEqual(self.v, self.v)
        # Unit test for method parse of class VersionTest
        def test_parse():
            self.assertEqual(self.v, 1)
    # Unit test for class VersionTest
    class Test_VersionTest(unittest.TestCase):
        def setUp(self):
            self.obj = VersionTest()



# Generated at 2022-06-13 00:01:55.501739
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    v2 = Version()
    assert v1 == v2

# Generated at 2022-06-13 00:02:00.026060
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('0.0.1')
    assert v1 == Version('0.0.1')
    assert v1 != Version('0.0.2')
    v1 = Version('0.1.1')
    assert v1 == Version('0.1.1')
    assert v1 != Version('0.1.2')

# Generated at 2022-06-13 00:02:05.913751
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Imports.
    import doctest
    import distutils.version
    import types

    # Set up.
    original_modules = list(sys.modules.keys())
    try:
        # Test.
        doctest.run_docstring_examples(distutils.version.Version.__lt__,
                                       globals(),
                                       verbose=False)
        # Verify.
        assert types.FunctionType is type(distutils.version.Version.__lt__)
    finally:
        # Tear down.
        for key in list(sys.modules.keys()):
            if key not in original_modules:
                del sys.modules[key]



# Generated at 2022-06-13 00:02:11.661370
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import sys
    import unittest
    class Test(unittest.TestCase):
        def test___lt__(self):
            self.assertIsInstance(Version.__lt__(Version(), None), bool)
    Test().test___lt__()

# Generated at 2022-06-13 00:02:13.605645
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import pytest
    # Version is an abstract data type and cannot be instantiated
    with pytest.raises(TypeError):
        Version()

# Generated at 2022-06-13 00:02:22.710056
# Unit test for method __eq__ of class Version

# Generated at 2022-06-13 00:02:24.992776
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    u = Version()
    if v != u:
        raise

# Generated at 2022-06-13 00:02:27.420555
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.3')
    v2 = Version('1.3')
    assert (v1 == v2)


# Generated at 2022-06-13 00:02:29.404404
# Unit test for method __eq__ of class Version
def test_Version___eq__():
  # Test with default args
  v = Version()
  assert v.__eq__(1) == False



# Generated at 2022-06-13 00:03:05.674596
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version
    from py.test import raises

    # constructor with valid value
    v = Version('1.2.3.4')

    # constructor with invalid value
    raises(TypeError, Version, 1)

    # __repr__
    assert repr(v) == "Version ('1.2.3.4')"

    # __eq__
    assert v == v
    assert v == '1.2.3.4'
    assert v == Version('1.2.3.4')
    assert v == 1.2
    raises(TypeError, 'v == 1')

    # __lt__
    assert v < '1.3'
    assert v < Version('1.3')

    # __le__
    assert v <= v
    assert v <= '1.2.3.4'

# Generated at 2022-06-13 00:03:07.003758
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v > 1

# Generated at 2022-06-13 00:03:09.059715
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    Version.__gt__
    assert True # TODO: implement your test here


# Generated at 2022-06-13 00:03:12.292612
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    f = Version.__lt__
    args = (None, )
    expected = None  # ?
    actual = f(*args)
    error_message = "Expected {}, got {}".format(expected, actual)
    assert actual == expected, error_message


# Generated at 2022-06-13 00:03:16.254934
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import pytest


    v = Version('1.1.1')
    assert v == Version('1.1.1')
    assert v == '1.1.1'

    assert not (v == Version('1.1.2'))
    assert not (v == '1.1.2')

    with pytest.raises(ValueError):
        v == ''

    with pytest.raises(ValueError):
        v == None

# Generated at 2022-06-13 00:03:18.093601
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    v2 = Version()
    assert(v1 == v2)



# Generated at 2022-06-13 00:03:21.049135
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import sys

    if sys.version_info < (2, 7):
        return

    from distutils.version import StrictVersion

    a = StrictVersion('1.1.1')
    b = StrictVersion('1.0.0')
    assert (a > b)



# Generated at 2022-06-13 00:03:23.900906
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('0.1') < Version('0.2')

# Generated at 2022-06-13 00:03:29.379707
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v1.parse('1.2.3')
    v2 = Version()
    v2.parse('1.2.3')
    assert (v1 == v2)
    assert (not (v1 > v2))
    assert (v1 >= v2)
    assert (not (v1 < v2))
    assert (v1 <= v2)

# Generated at 2022-06-13 00:03:31.679269
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert (v == None) == False
    del v
    version = Version('0.0')
    assert (version == '0.0') == True
    assert (version == '0.1') == False
    del version


# Generated at 2022-06-13 00:03:56.975682
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    v1 = Version('5.5')
    v2 = Version('6.2')
    assert v1 == v1
    assert v1 == '5.5'
    assert not v1 == v2



# Generated at 2022-06-13 00:04:02.955087
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('2.6') < Version('2.6')
    assert Version('2.6') < Version('2.6.1')
    assert Version('2.6.1') < Version('2.6.1.9000')
    assert Version('2.6.1') < Version('2.6.2')
    assert Version('2.6.9.9') < Version('2.6.10')

# Generated at 2022-06-13 00:04:04.544692
# Unit test for method __lt__ of class Version
def test_Version___lt__():
  assert_raises(NotImplementedError, Version().__lt__, None)



# Generated at 2022-06-13 00:04:07.786723
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Version.__lt__
    #assert Version('1.2.3') < '1.2.10'
    assert Version('1.2.3') < Version('1.2.10')



# Generated at 2022-06-13 00:04:10.444531
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import StrictVersion
    import pytest
    v = StrictVersion("3.0.0")
    w = StrictVersion("2.0.0")
    assert v < w
    assert not v > w

# Generated at 2022-06-13 00:04:11.740291
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    ver = Version()
    assert ver.__lt__(None) is NotImplemented

# Generated at 2022-06-13 00:04:13.759289
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    l = LooseVersion()
    l.parse("1.0")
    assert l.version == [1, 0]
    l.parse("a.b.c")
    assert l.version == ['a', 'b', 'c']
    l.parse("1.0b1")
    assert l.version == [1, 0, 'b', 1]


# Generated at 2022-06-13 00:04:24.395484
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    """Check Version.__eq__() method."""
    from lib2to3.pgen2.tokenize import NUMBER

    class VersionTestCase(Version):
        def __eq__(self, other):
            return Version.__eq__(self, other)


    v1, v2 = VersionTestCase(), VersionTestCase()
    # Check that __eq__ works on a subclass.
    assert (v1 == v2) == True

    v2.parse('1.2')
    assert (v1 == v2) == False
    assert (v1 == '1.2') == False

    v1.parse('1.2')
    assert (v1 == v2) == True
    assert (v1 == '1.2') == True

    v2.parse('1.2a1')

# Generated at 2022-06-13 00:04:28.883423
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version
    import unittest
    version = Version('1.0')
    other = Version('2.0')
    unittest.TestCase().assertNotEqual(version, other)


# Generated at 2022-06-13 00:04:38.603449
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    #
    # Test the method '__gt__' of the class 'Version'
    #
    # The __gt__ method of the Version class allows to compare version numbers
    # with the '>' operator. It returns true if the number that is compared to
    # another version number is bigger than the other number.
    #
    # Example:
    #
    #     >>> Version('1.9.3') > Version('1.9.2')
    #     True
    #
    #     >>> Version('1.9.3') > Version('1.9.3')
    #     False
    #
    #     >>> Version('1.9.3') > Version('1.9.4')
    #     False
    #
    return True


# Generated at 2022-06-13 00:05:37.441606
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    LooseVersion.parse("1.5.1")
    LooseVersion.parse("1.5.2b2")
    LooseVersion.parse("161")
    LooseVersion.parse("3.10a")
    LooseVersion.parse("8.02")
    LooseVersion.parse("3.4j")
    LooseVersion.parse("1996.07.12")
    LooseVersion.parse("3.2.pl0")
    LooseVersion.parse("3.1.1.6")
    LooseVersion.parse("2g6")
    LooseVersion.parse("11g")
    LooseVersion.parse("0.960923")
    LooseVersion.parse("2.2beta29")
    LooseVersion.parse("1.13++")

# Generated at 2022-06-13 00:05:47.372688
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import unittest

    import distutils.version

    class VersionTestCase(unittest.TestCase):
        def test_Version___lt__(self):
            # __lt__
            self.assertTrue(distutils.version.LooseVersion('1.0') < distutils.version.LooseVersion('2.0'))
            self.assertFalse(distutils.version.LooseVersion('1.0') < distutils.version.LooseVersion('1.0'))
            self.assertFalse(distutils.version.LooseVersion('2.0') < distutils.version.LooseVersion('1.0'))

            self.assertTrue(distutils.version.LooseVersion('1.0') < '2.0')

# Generated at 2022-06-13 00:05:53.830412
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # No object type has been set as the default yet.
    # We need to explicitly pass object as the first parameter.
    class TestVersion(Version, object):
        def __init__(self, vstring=None):
            assert vstring
            self.version = vstring
            self.parse(vstring)

        def __repr__(self):
            return "%s ('%s')" % (self.__class__.__name__, str(self))

        def parse(self, vstring):
            assert vstring == self.version

        def _cmp(self, other):
            return NotImplemented

    # Test class Version

    # Call function __eq__ of class Version
    # v is an instance of class Version
    # Compare v with a string.
    testVersion = TestVersion("1.1")

# Generated at 2022-06-13 00:05:55.308386
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    version = Version()
    version2 = Version()
    if version != version2:
        raise AssertionError()

# Generated at 2022-06-13 00:05:57.101034
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    r = Version('1.5.1') > 6
    if r == NotImplemented:
        r = False
    assert r is True,repr(r)


# Generated at 2022-06-13 00:06:00.701842
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version
    import pytest

    with pytest.raises(NotImplementedError):
        Version() > '0.0'


# Generated at 2022-06-13 00:06:09.398509
# Unit test for method __lt__ of class Version
def test_Version___lt__():
  import math
  import random

  def check(type_, self, other, expected):
    actual = type_.__lt__(self, other)
    try:
      assert actual == expected
    except AssertionError:
      print("Failed assertion: expected %s, got %s" % (expected, actual))
      raise

  # Alias
  c = check

  # Test numeric values.
  c(Version, 0, 0, False)
  c(Version, 0, 1, True)
  c(Version, 2, 1, False)
  c(Version, 2, 2, False)
  c(Version, 1, math.pi, True)
  c(Version, 1, math.e, True)
  c(Version, math.pi, math.e, True)
  # Test the case where an integer is compared to

# Generated at 2022-06-13 00:06:18.886822
# Unit test for method __lt__ of class Version
def test_Version___lt__(): assert Version().__lt__(object()) == NotImplemented


_numeric_re = re.compile(r'(\d+)')
_numeric_repl = r'{.\g<0>}'
_letter_re = re.compile(r'([a-zA-Z])')
_letter_repl = r'{\g<0>}'
_version_re = re.compile(r'^v?(?P<release>[-_\.\w]+)(?P<pre>[-_\.]?[a-zA-Z]+(?P<dev>dev)?)?$', RE_FLAGS)

# Generated at 2022-06-13 00:06:25.563080
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version
    from distutils.version import LooseVersion
    from distutils.version import StrictVersion
    from distutils.version import UnsupportedVersionError

    # increase at the beginning of a sequence
    assert StrictVersion('1.2b0') > StrictVersion('1.2a0')
    assert LooseVersion('1.2b0') > LooseVersion('1.2a0')
    with pytest.raises(UnsupportedVersionError):
        StrictVersion('3b0') > '1.2a0'
    assert LooseVersion('3b0') > '1.2a0'
    # same number of elements in the version sequence, increase in the middle
    assert StrictVersion('1.2b3') > StrictVersion('1.2b2')

# Generated at 2022-06-13 00:06:36.579059
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    ver_a = Version()

    ver_a.parse("1.2")
    ver_b = Version("1.3")
    assert ver_a < ver_b

    ver_b.parse("1.3")
    assert ver_a < ver_b

    ver_b.parse("1.2")
    assert not (ver_a < ver_b)

    ver_b = Version("1.1")
    assert ver_a > ver_b

    ver_b = Version()
    assert not (ver_a > ver_b)

    ver_b.parse("1.2")
    assert not (ver_a > ver_b)

# Generated at 2022-06-13 00:08:12.634123
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    versionA = Version("4.4")
    versionB = Version("4.5")
    assert not versionA.__gt__(versionB)



# Generated at 2022-06-13 00:08:13.634078
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v.__eq__(None) == NotImplemented



# Generated at 2022-06-13 00:08:15.138997
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert "assert" not in Version().__gt__.__code__.co_code.hex()



# Generated at 2022-06-13 00:08:18.311367
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import StrictVersion

    assert StrictVersion('1.2') == StrictVersion('1.2')
    assert not StrictVersion('1.2') == StrictVersion('1.3')
    assert not StrictVersion('1.2') == '1.2'


# Generated at 2022-06-13 00:08:19.402188
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1.2') == Version('1.2')



# Generated at 2022-06-13 00:08:20.429028
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1') == '1'


# Generated at 2022-06-13 00:08:22.139024
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version("1.8.0")
    v2 = Version("1.7.3")
    assert v1 > v2

# Generated at 2022-06-13 00:08:26.216934
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version
    v = Version('1.1.1')
    assert v == '1.1.1'
    assert v == Version('1.1.1')
    assert not (v != '1.1.1')
    assert not (v != Version('1.1.1'))

# Generated at 2022-06-13 00:08:31.273484
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import ansible.module_utils.distro_util.version
    v1 = ansible.module_utils.distro_util.version.Version('2.0')
    v2 = ansible.module_utils.distro_util.version.Version('2.0')
    try:
        x = (v1 == v2)
    except AssertionError:
        x = False
    assert x

# Generated at 2022-06-13 00:08:39.675397
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    """Unit test for method parse of class LooseVersion

    The test cases are taken from the module documentation
    of the LooseVersion class.
    """
    def test_lv(vstring):
        try:
            version = LooseVersion(vstring)
            print('LooseVersion(%s) -> %s' % (vstring, str(version)))
        except:
            print('LooseVersion(%s) -> FAILED' % (vstring,))

    test_lv('1.5.1')
    test_lv('1.5.2b2')
    test_lv('161')
    test_lv('3.10a')
    test_lv('8.02')
    test_lv('3.4j')
    test_lv('1996.07.12')