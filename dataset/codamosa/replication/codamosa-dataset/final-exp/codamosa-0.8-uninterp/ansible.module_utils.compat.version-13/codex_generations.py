

# Generated at 2022-06-12 23:59:23.992757
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    version = StrictVersion()
    version.parse('1.2.3a2')
    assert version.version == (1, 2, 3)
    assert version.prerelease == ('a', 2)
    assert str(version) == '1.2.3a2'

    version.parse('1.2.3')
    assert version.version == (1, 2, 3)
    assert version.prerelease == None
    assert str(version) == '1.2.3'

    version.parse('1.2.3-1')
    assert version.version == (1, 2, 3)
    assert version.prerelease == None
    assert str(version) == '1.2.3'


# Generated at 2022-06-12 23:59:29.163151
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    def __eq__(self, other):
        c = self._cmp(other)
        if c is NotImplemented:
            return c
        return c == 0
    # Replace __eq__ with our method
    Version.__eq__ = __eq__


# Generated at 2022-06-12 23:59:38.203562
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    from distutils.version import StrictVersion

    v = StrictVersion("1.4.1")
    assert str(v) == "1.4.1"

    v = StrictVersion("1.4")
    assert str(v) == "1.4"

    v = StrictVersion("1.4")
    v._version = (1, 4, 0, 'a', 6)
    assert str(v) == "1.4a6"

    v = StrictVersion("1.4")
    v._version = (1, 4, 0, 'b', 4)
    assert str(v) == "1.4b4"

    v = StrictVersion("1.4")
    v._version = (1, 4, 0, 'c', 4)
    assert str(v) == "1.4"

   

# Generated at 2022-06-12 23:59:49.151296
# Unit test for method __le__ of class Version
def test_Version___le__():
    import math
    import unittest

#import Version
    
# from distutils.tests import support
#     from test.support import run_unittest



# Generated at 2022-06-12 23:59:57.505530
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    with pytest.raises(ValueError):
        StrictVersion('hello world')

    v = StrictVersion('1.3')
    assert v.version == (1,3,0)
    assert v.prerelease == None

    v = StrictVersion('1.3b4')
    assert v.version == (1,3,0)
    assert v.prerelease == ('b',4)

    v = StrictVersion('1.3.4')
    assert v.version == (1,3,4)
    assert v.prerelease == None


# Generated at 2022-06-12 23:59:58.926454
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    StrictVersion().parse("123.456.789.0ab1")


# Generated at 2022-06-13 00:00:00.681381
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version(vstring='1.0') < Version(vstring='2.0')


# Generated at 2022-06-13 00:00:10.925802
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion("1.2.3").__str__() == "1.2.3"
    assert StrictVersion("1.2.0").__str__() == "1.2"
    assert StrictVersion("1.2").__str__() == "1.2"
    assert StrictVersion("0.9.6").__str__() == "0.9.6"
    assert StrictVersion("1.0").__str__() == "1.0"
    assert StrictVersion("1.0.4b1").__str__() == "1.0.4b1"
    assert StrictVersion("1.0.4").__str__() == "1.0.4"
    assert StrictVersion("1").__str__() == "1"

# Generated at 2022-06-13 00:00:20.718714
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    StrictVersionStub = StrictVersion
    class StrictVersion(StrictVersionStub):
        def __init__(self, vstring=None):
            self.version = (0, 0, 0)
            self.prerelease = (0, 0)

# Generated at 2022-06-13 00:00:27.918798
# Unit test for method __le__ of class Version
def test_Version___le__():
    # Version.__le__(str)
    version = Version()
    version.parse("1.0")
    assert version <= "1.0"
    assert not version <= "2.0"
    assert not "2.0" <= version
    # Version.__le__(Version)
    version = Version()
    other = Version()
    assert version <= other
    other.parse("1.0")
    assert version <= other
    assert not other <= version
    version.parse("1.0")
    assert version <= other
    assert other <= version



# Generated at 2022-06-13 00:00:38.070163
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version()
    v2 = Version()
    if (v1 == v2):
        print("Test passed SUCCESSFULLY!")
    else:
        print("Test FAILED!")

test_Version___ge__()



# Generated at 2022-06-13 00:00:38.699951
# Unit test for method __le__ of class Version
def test_Version___le__():
    pass

# Generated at 2022-06-13 00:00:39.700846
# Unit test for method __lt__ of class Version
def test_Version___lt__():
	assert str(Version("1.1")) < str(Version("1.2"))

# Generated at 2022-06-13 00:00:40.571494
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('1').__ge__('2') == False


# Generated at 2022-06-13 00:00:45.054720
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version('1.0')
    v2 = Version('1.1')

    assert v1 <= v2


# Generated at 2022-06-13 00:00:47.215035
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    assert not v1 < v2



# Generated at 2022-06-13 00:00:49.592591
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    foo = Version()
    bar = Version()
    assert foo.__ge__(bar) in [True, False]
    return



# Generated at 2022-06-13 00:01:00.317531
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    Version = m.Version
    # test string arguments
    v1 = Version('1.2.3a1')
    v2 = Version('1.2.3a2')
    assert (v1 != v2)
    assert (v1 < v2)
    assert (v1 <= v2)
    assert (v2 == '1.2.3a2')
    assert (v2 > '1.2.3a1')
    assert (v2 >= '1.2.3a1')
    assert (v1 == '1.2.3a1')
    assert (v1 <= '1.2.3a2')
    assert (v1 >= '1.2.3a1')
    # test Version arguments
    v1 = Version('1.2.3a1')

# Generated at 2022-06-13 00:01:03.754280
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    class _Test:
        v1 = _Test()
        inst = Version("v1")
        c = inst._cmp(v1)
        assert c == -1



# Generated at 2022-06-13 00:01:08.320876
# Unit test for method __lt__ of class Version
def test_Version___lt__():

    # Setup


    v1 = Version('1.2')
    v2 = Version('1.2')
    v3 = Version('1.3')
    v4 = Version('3.3')

    # Exercise and Verify

    assert v1 < v3
    assert not v1 < v2
    return # test_Version___lt__



# Generated at 2022-06-13 00:01:25.218512
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Unit test for method __le__ of class Version"""
    v = Version("1.2.3")
    assert( not (v <= "1.2.3a") )


# Generated at 2022-06-13 00:01:30.069748
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import distutils.version as service
    # Construct a mock Version object
    v1 = service.Version('0.0.25')

    # Construct another mock Version object
    v2 = service.Version('0.0.25')
    # Check that v1 is gt v2
    assert v1.__gt__(v2) == False


# Generated at 2022-06-13 00:01:31.718205
# Unit test for method __le__ of class Version
def test_Version___le__():
    ver = Version('1.1')
    assert (ver <= '1.1') is True


# Generated at 2022-06-13 00:01:34.035172
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.2.3')
    v2 = Version('1.2.3.4')
    assert v1 != v2

# Generated at 2022-06-13 00:01:37.349682
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Test method __lt__ of class Version"""
    # Create the object
    obj = Version("1.2.2")
    # Check the result
    result = obj < "1.2.2"
    assert result == False
    # Check the type of the result
    assert isinstance(result, bool)


# Generated at 2022-06-13 00:01:41.665575
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils2.tests import unittest, support
    try:
        from distutils2._backport import UserDict
    except ImportError:
        from UserDict import UserDict
    try:
        from distutils2._backport import collections
    except ImportError:
        import collections
    v1 = Version()
    v2 = Version('2.0')
    assert v1 < v2

# Generated at 2022-06-13 00:01:45.467657
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v.__eq__(None) == False
    assert v.__eq__(NotImplemented) == True
    assert v.__eq__(Version()) == False


# Generated at 2022-06-13 00:01:47.315682
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert str(Version('1.2')) == '1.2'
test_Version___le__()


# Generated at 2022-06-13 00:01:54.210688
# Unit test for method __le__ of class Version
def test_Version___le__():
    import types

    # Test list from python 3.9.5 /Lib/distutils/version.py

# Generated at 2022-06-13 00:01:55.642057
# Unit test for method __le__ of class Version
def test_Version___le__():
    o = Version()
    assert o.__le__('1') == True

# Generated at 2022-06-13 00:02:28.499601
# Unit test for method __le__ of class Version
def test_Version___le__():
    a = Version()
    assert a.__le__(a)
    raise ValueError("Tests for Version.__le__() have not been implemented.")



# Generated at 2022-06-13 00:02:33.388651
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import StrictVersion

    v = StrictVersion('1.0a1')

    assert v == StrictVersion('1.0a1')
    assert not (v == StrictVersion('1.0'))
    assert not (v == StrictVersion('1.0a2'))
    assert not (v == 1)
    assert v == '1.0a1'

# Generated at 2022-06-13 00:02:35.137161
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version('1.2.3')
    assert(v < '1.2.4')

# Generated at 2022-06-13 00:02:36.941967
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v.__eq__(None) == NotImplemented


# Generated at 2022-06-13 00:02:39.260395
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version(vstring="1.0.0")
    v2 = Version(vstring="1.0.0")
    assert v1 == v2


# Generated at 2022-06-13 00:02:40.350506
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()


# Generated at 2022-06-13 00:02:44.902249
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import pytest
    from distutils.version import Version
    assert Version('1.1') >= '1.1'
    assert not (Version('1.1') >= '1.2')
    assert Version('1.2') >= '1.1'
    assert not (Version('1.1') >= '2.0')
    assert Version('2.0') >= '1.1'



# Generated at 2022-06-13 00:02:46.139898
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert(v.__gt__(4) == NotImplemented)

# Generated at 2022-06-13 00:02:57.942984
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    """Test method Version.__gt__"""
    # Make sure the method __gt__ works on the class Version
    # It should succeed
    v = Version('1.1.1')
    assert v > 1
    assert v > '1'


    # Make sure the method __gt__ works on the class Version
    # It should succeed
    v = Version('1.1.1')
    assert v >= 1
    assert v >= '1'


    # Make sure the method __gt__ works on the class Version
    # It should succeed
    v = Version('1.1.1')
    assert v == 1
    assert v == '1'


    # Make sure the method __gt__ works on the class Version
    # It should succeed
    v = Version('1.1.1')
    assert v < 2

# Generated at 2022-06-13 00:03:01.373098
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils.version import LooseVersion
    # Version tests, comparing with a string
    for v in LooseVersion("1.4.1") < "1.4.2", LooseVersion("1.4.2") > "1.4.1":
        pass


# Generated at 2022-06-13 00:03:36.533239
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert 3 <= 3
    assert 'a' <= 'a'
    assert [] <= []
    assert 'a' <= 'ab'
    assert 'ab' <= 'ac'
    assert 'a' <= 'a'


# Generated at 2022-06-13 00:03:42.840528
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import doctest
    from ansible.module_utils.version import Version
    from ansible.module_utils.six import PY3, u

    globs = {'v1': Version('1') if PY3 else Version('1') }

    failed, tests = doctest.testmod(m=Version, globs=globs)
    if failed == 0:
        print('%s' % u('✔ Version.__ge__()'))



# Generated at 2022-06-13 00:03:43.953416
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v >= '1'
    assert not (v >= '2')

# Generated at 2022-06-13 00:03:44.594553
# Unit test for method __lt__ of class Version
def test_Version___lt__():
  assert Version() < Version()


# Generated at 2022-06-13 00:03:47.021631
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version('3.0')
    x = (v <= Version('2.0'))
    assert isinstance(x, bool), repr(x)
    assert x is False, repr(x)

# Generated at 2022-06-13 00:03:57.135478
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import unittest

    class VersionTester(unittest.TestCase):
        def error_test(self, expected, object, object_name=None, object_names=None):
            try:
                object(self)
            except AssertionError as e:
                str_e = str(e)
                self.assertTrue(str_e.startswith(expected),
                                "unexpected AssertionError: '%s', expected '%s'" % (str_e, expected))
                return
            self.fail("AssertionError exception not raised")

        def test___ge__(self):
            class VersionSub(Version):
                def parse(self, vstring):
                    pass
                def _cmp(self, other):
                    raise NotImplementedError("_cmp method not implemented")


# Generated at 2022-06-13 00:04:03.832318
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('1.0') == Version('1.0')
    assert Version('1.0') != Version('1.1')
    assert Version('1.1') != Version('1.0')
    assert Version('1.0') < Version('1.1')
    assert Version('1.1') > Version('1.0')
    assert Version('1.1') >= Version('1.0')
    assert Version('1.0') <= Version('1.1')



# Generated at 2022-06-13 00:04:06.419572
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    ver1 = StrictVersion()
    ver2 = LooseVersion()
    if ver1 > ver2:
        raise Exception()

# Generated at 2022-06-13 00:04:09.245837
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert (v.__gt__('hello') is NotImplemented)

# Generated at 2022-06-13 00:04:10.665522
# Unit test for method __le__ of class Version
def test_Version___le__():
 n = Version(vstring='3')
 m = Version()
 assert n <= n  # __le__

# Generated at 2022-06-13 00:04:51.344937
# Unit test for method __le__ of class Version
def test_Version___le__():
    ver1 = Version(1.1)
    ver2 = Version(1.2)
    print(bool(ver1 <= ver2))
    print(bool(ver1 <= 1.1))

test_Version___le__()


# Generated at 2022-06-13 00:04:52.523352
# Unit test for method __le__ of class Version
def test_Version___le__():
    Version()
    assert False # TODO: implement your test here


# Generated at 2022-06-13 00:04:59.021175
# Unit test for method parse of class LooseVersion

# Generated at 2022-06-13 00:05:08.539558
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert_equal(Version('0.0').__le__(Version('0.0')), True)
    assert_equal(Version('0.0').__le__(Version('1.0')), True)
    assert_equal(Version('1.0').__le__(Version('0.0')), False)
    assert_equal(Version('0.0').__le__(Version('0.1')), True)
    assert_equal(Version('0.1').__le__(Version('0.0')), False)
    assert_equal(Version('0.0~').__le__(Version('0.0~')), True)
    assert_equal(Version('0.0~').__le__(Version('1.0~')), True)

# Generated at 2022-06-13 00:05:11.708640
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    try:
        env = dict()
        version = Version()
        Version.__lt__(version, other)
    except TypeError:
        pass
    except NotImplementedError:
        pass
    except Exception:
        raise TypeError
    else:
        raise TypeError

# Generated at 2022-06-13 00:05:23.786381
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    import re

    component_re = re.compile(r'(\d+ | [a-z]+ | \.)', re.VERBOSE)
    major,minor,micro = component_re.split('18.1')
    assert (int(major),int(minor),int(micro)) == (18, 1, 0), '18.1 should be (18, 1, 0)'

    major,minor = component_re.split('18.1.0')
    assert (int(major),int(minor)) == (18,1), '18.1.0 should be (18, 1)'

    major,minor,micro = component_re.split('18.1a')

# Generated at 2022-06-13 00:05:29.139503
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Test case for method __le__ of class Version"""
    V1 = Version('1.2.3')
    V2 = Version('2.2.3')
    assert (V1 <= V2) == True


# Generated at 2022-06-13 00:05:32.147465
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version("1.0") < Version("2.0")

# Generated at 2022-06-13 00:05:39.844250
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    # Test that parse can take a string or an iterable as argument
    v1 = LooseVersion()
    v2 = '0.4.0.0.4.0.0.4.0.0.4.0.0.4.0.0.4.0.0.4.0.0.4.0.0.4.0.0.4.0.0.4.0.0.4.0.0.4.0.0.4'
    v3 = '.'.join([str(i) for i in range(0,62)])
    assert v1.parse(v2) is None
    assert v1.parse(v3) is None
    # Test that parse raises a ValueError on invalid input
    v1 = LooseVersion(v2)

# Generated at 2022-06-13 00:05:41.593480
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    v.__gt__(None)



# Generated at 2022-06-13 00:07:09.799585
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version()
    v2 = Version()
    assert v1 <= v1
    assert not v1 < v1
    assert v2 <= v2
    assert not v2 < v2
    assert v1 <= v2
    assert v2 <= v1


# Generated at 2022-06-13 00:07:11.992063
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class _Version(Version):
        def _cmp(self, other):
            return 3
    v1 = _Version()
    assert not (v1 < v1)

# Generated at 2022-06-13 00:07:13.228137
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v.__ge__(v)


# Generated at 2022-06-13 00:07:24.361569
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    """Unit test for method parse of class LooseVersion
    """
    # it is not necessary to test all possible cases of the method
    # test cases that show interesting behaviour
    # a false value can be easily found using the doctest framework
    # first use the test_cases defined in base_test_case.py
    version_numbers = test_cases['version_numbers']

    # add some more test cases according to the rules defined above
    version_numbers.extend(['1.2.1.2', '1.2.0', '1.2.3.4.5'])

    # remove some cases that contain characters which are not decimal
    # digits or letters
    version_numbers = [num for num in version_numbers if num.isalnum()]

    for version_number in version_numbers:
        v = Lo

# Generated at 2022-06-13 00:07:26.392591
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    v2 = Version()
    assert(v2.__gt__(v) == NotImplemented)


# Generated at 2022-06-13 00:07:32.406798
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    def _test(self, other):
        c = self._cmp(other)
        if c is NotImplemented:
            return c
        return c > 0
    _test.__name__ = '__gt__'
    _test.__doc__ = ''
    Version.__gt__ = _test
    try:
        v1 = StrictVersion("1.0.0")
        v2 = StrictVersion("1.0.1")
        assert v2 > v1
    finally:
        del Version.__gt__



# Generated at 2022-06-13 00:07:41.200580
# Unit test for method __le__ of class Version
def test_Version___le__():
  import pytest
  from ansible.module_utils.six import PY2
  from ansible.module_utils.common.version import Version
  from ansible.module_utils.six.moves import StringIO
  from ansible.module_utils._text import to_text

  class TestVersion(Version):
      def parse(self, vstring):
        self.vstring = vstring
      def _cmp(self, other):
        return cmp(self.vstring, other)

  stream = StringIO()

  v1 = TestVersion("1.1")
  stream.write("Eq:")
  if v1 == "1.1":
      stream.write("1.1==1.1")
  else:
      stream.write("1.1!=1.1")

# Generated at 2022-06-13 00:07:51.550028
# Unit test for method __le__ of class Version
def test_Version___le__():
  from distutils.version import StrictVersion
  v1 = StrictVersion('1.2.3')
  assert v1 <= '1.2.3'
  assert v1 <= StrictVersion('1.2.3')
  assert not v1 <= '1.2.4'
  assert not v1 <= StrictVersion('1.2.4')
  assert v1 < v1.parse('1.2.4')
  assert v1 < v1.parse('1.2.4-alpha')
  assert v1 <= v1.parse('1.2.4')
  assert v1 <= v1.parse('1.2.4-alpha')
  assert v1.parse('1.2.4-alpha') <= '1.2.4'
  assert v1.parse('1.2.4-alpha') <= St

# Generated at 2022-06-13 00:07:52.760448
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('1.0') >= Version('1.0')



# Generated at 2022-06-13 00:07:56.807231
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class DummyVersion(Version):
        def parse(self, vstring):
            pass
        def __str__(self):
            return "1.0"
        def _cmp(self, other):
            return 1
    v1 = DummyVersion("1.0")
    v2 = DummyVersion("1.0")
    assert not (v1 < v2)
