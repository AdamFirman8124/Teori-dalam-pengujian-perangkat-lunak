

# Generated at 2022-06-12 23:59:18.072538
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    assert (v <= Version('1'))
    assert (v <= '1')
    assert not (v <= None)



# Generated at 2022-06-12 23:59:20.360341
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    if (Version.__lt__.im_func(Version('1'), Version('2')) != True):
        raise AssertionError

# Generated at 2022-06-12 23:59:29.451541
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():

    # Happy path
    v = StrictVersion("0.4.0")
    assert v.version == (0, 4, 0)
    assert v.prerelease is None

    v = StrictVersion("0.5")
    assert v.version == (0, 5, 0)
    assert v.prerelease is None

    v = StrictVersion("0.5a1")
    assert v.version == (0, 5, 0)
    assert v.prerelease == ('a', 1)

    v = StrictVersion("0.5.1a1")
    assert v.version == (0, 5, 1)
    assert v.prerelease == ('a', 1)

    v = StrictVersion("0.5b3")
    assert v.version == (0, 5, 0)

# Generated at 2022-06-12 23:59:32.649697
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # From the bug report, __ge__ of general case always returns true regardless of the
    # parameters unless NotImplemented is raised
    v = Version()
    assert v.__ge__(v)



# Generated at 2022-06-12 23:59:42.183172
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    sv = StrictVersion('1.2.3')
    assert sv.version == (1, 2, 3)
    assert sv.prerelease is None
    assert str(sv) == '1.2.3'
    assert repr(sv) == "StrictVersion ('1.2.3')"

    sv2 = StrictVersion('1.2.3a4')
    assert sv2.version == (1, 2, 3)
    assert sv2.prerelease == ('a', 4)
    assert str(sv2) == '1.2.3a4'
    assert repr(sv2) == "StrictVersion ('1.2.3a4')"

    sv = StrictVersion('1.2')
    assert sv.version == (1, 2, 0)
    assert sv.prerelease is None

# Generated at 2022-06-12 23:59:44.321203
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('0.3')
    v2 = Version('0.3')
    assert v == v2


# Generated at 2022-06-12 23:59:45.965562
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('1').__le__(Version('2'))

# Generated at 2022-06-12 23:59:47.686072
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert True
    # TODO: implement your test here
    raise NotImplementedError # noqa

# Generated at 2022-06-12 23:59:50.240188
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version()
    assert (v < Version()) == NotImplemented, (v < Version())
    assert (v < 1) == NotImplemented, (v < 1)


# Generated at 2022-06-12 23:59:57.017117
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version() < Version()
    assert Version() < Version('1.0')
    assert Version('1.0') < Version('2.0')
    assert not Version('1.0') < Version('1.0')
    assert Version('1.0') < Version('2.0.0')
    assert not Version('1.0') < Version('1.0.0')
    assert Version('1.0') < Version('2.0.0b')
    assert not Version('1.0') < Version('2.0.0a')
    assert Version('1.0') < Version('2.0.0dev')
    assert not Version('1.0') < Version('1.0dev')
    assert Version('1.0') < Version('2.0.0a1')

# Generated at 2022-06-13 00:00:07.933024
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest

    class TestCase(unittest.TestCase):

        def test_Version___gt__(self):
            self.assertEqual(Version().__gt__(Version()), NotImplemented)



# Generated at 2022-06-13 00:00:10.236796
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version('1.2')
    v2 = Version('1.3')
    assert v1 <= v2


# Generated at 2022-06-13 00:00:11.186744
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    pass


# Generated at 2022-06-13 00:00:13.712152
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v.parse('1.2.3')
    assert v <= '1.2.4'



# Generated at 2022-06-13 00:00:15.076685
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('2.0') == Version('2.0')

# Generated at 2022-06-13 00:00:16.437167
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version().__lt__(None)


# Generated at 2022-06-13 00:00:22.266960
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version("1.0")
    assert v == "1.0"
    assert v == Version("1.0")
    assert v == "1.0.dev0"
    assert v == Version("1.0.dev0")
    assert v != "1.1"
    assert v != Version("1.1")
    assert v != "1.0.b"
    assert v != Version("1.0.b")
    assert v != "1.0b"
    assert v != Version("1.0b")

# Generated at 2022-06-13 00:00:24.266951
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version(vstring="1.2")
    assert v == "1.2"



# Generated at 2022-06-13 00:00:26.863463
# Unit test for method __le__ of class Version
def test_Version___le__():
    class TestVersion(Version):
        def _cmp(self, other):
            return 0
    tv = TestVersion()
    assert tv <= TestVersion()
    assert tv <= '1.0'


# Generated at 2022-06-13 00:00:38.886055
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import os
    import sys
    import tempfile
    from distutils import version
    from random import Random
    from contextlib import contextmanager, ExitStack
    from io import StringIO
    from typing import *

    temp_dir = tempfile.mkdtemp()
    temp_path = os.path.join(temp_dir, 'temp.py')
    rand = Random(5)


# Generated at 2022-06-13 00:00:55.070267
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('1.0') < Version('2.0')
    assert Version('2.0') > Version('1.0')
    assert Version('1.0') != Version('1.1')
    assert Version('1.0') != Version('2.0')
    assert not Version('1.0') < ''
    #
    # Checking if the "not less than" relation on versions is
    # symmetric
    assert not Version('2.0') < Version('1.0')
    assert not Version('1.1') < Version('1.0')
    assert not Version('2.0') < Version('2.0')
    assert Version('1.0') < Version('1.0')
    #
    # Checking the arithmetic properties a < b and b > c implies a < c

# Generated at 2022-06-13 00:00:57.340146
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('') <= ''
    assert Version('') <= 'a'
    assert not Version('') <= None
    assert Version('a') <= 'a'

# Generated at 2022-06-13 00:01:02.014261
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from tests import test_version
    v = test_version.TestVersionClass()
    assert (v == v)
    v2 = test_version.TestVersionClass()
    assert isinstance(v2, Version)
    assert (v == v2)
    assert (v == "1.0.4")
    assert (v != "1.0.5")
    assert (v != "")
    assert (v != None)

# Generated at 2022-06-13 00:01:11.959013
# Unit test for method __le__ of class Version
def test_Version___le__():
    """
    Test Version.__le__()
    """
    v1 = Version('1.0')
    v2 = Version('2.0')
    v3 = Version('1.1')
    assert (v1 == v1) is True
    assert (v1 <= v1) is True
    assert (v1 < v1) is False
    assert (v1 >= v1) is True
    assert (v1 > v1) is False
    assert (v1 == v2) is False
    assert (v1 <= v2) is True
    assert (v1 < v2) is True
    assert (v1 >= v2) is False
    assert (v1 > v2) is False
    assert (v1 == v3) is False
    assert (v1 <= v3) is True

# Generated at 2022-06-13 00:01:15.667477
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version

    try:
        v = Version('1.4.0')
        v1 = Version('1.4.1')
        v2 = Version('1.4.2')
        v3 = Version('1.4.0')
        assert v == v3
        assert not v == v1
        assert not v1 == v2
    except:
        return False
    return True

# Generated at 2022-06-13 00:01:22.971931
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Test method __le__ of class Version."""
    version = Version('1.2.0')
    version_1 = Version('1.2.0')
    version_2 = Version('1.9.9')
    version_3 = Version('2.0.0')
    version_4 = Version('2.0.0')
    assert version_1 <= version == True
    assert version_2 <= version == False
    assert version >= version_3 == False
    assert version <= version_3 == True
    return

# Generated at 2022-06-13 00:01:30.619305
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest
    try:
        import _testcapi
    except ImportError:
        unittest.SkipTest("test requires _testcapi")

    class GTVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring
        def _cmp(self, other):
            # Force a TypeError
            return _testcapi.make_exception(TypeError)

    with unittest.TestCase() as tc:
        tc.assertTrue(GTVersion("x") > "x")



# Generated at 2022-06-13 00:01:32.738540
# Unit test for method __lt__ of class Version
def test_Version___lt__():
  # the line below should return the static type Error
  Version('1.2.3').__lt__(4)


# Generated at 2022-06-13 00:01:37.873234
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version('7.0')
    assert v < '10.0' is True
    assert v < '7.0' is False
    assert v < '7.0.0' is False
    assert v < '7.1' is True
    assert v < '7.1.0' is True
    assert v < '7.1.1' is True
    assert v < '7.2' is True
    assert v < '7.2.0' is True
    assert v < '7.2.1' is True


# Generated at 2022-06-13 00:01:42.543107
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import pytest
    import sys

    class MockArgs:
        def __init__(self, vstring=None):
            self.vstring = vstring
    
    class MockVersion:
        def __init__(self, vstring):
            self.args = MockArgs(vstring)
            if hasattr(Version, '_setup'):
                Version._setup(self)
    
    v = MockVersion('1:3.0.4-1ubuntu1')
    assert(v.__eq__('1:3.0.4-1ubuntu1'))



# Generated at 2022-06-13 00:02:03.789827
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import pytest
    from distutils.version import Version

# Generated at 2022-06-13 00:02:14.251938
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """ Check that __lt__ of class Version is correctly implemented

        Testing by comparing a version of the form MAJOR.MINOR.*,
        with its previous patch level
    """
    # instance of current class
    v = Version("1.0.3")
    # previous patch level
    p = Version("1.0.2")
    assert v > p
    assert v != p
    assert v.__lt__(p) == False
    assert v.__eq__(p) == False
    assert v.__gt__(p) == True
    assert v.__ge__(p) == True
    assert v.__le__(p) == False


# Generated at 2022-06-13 00:02:17.299891
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    print('>',end='')
    import version
    inst = version.Version()
    other = 42
    print(inst.__ge__(other))



# Generated at 2022-06-13 00:02:25.108904
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from . import version
    v1 = version.Version('1.1')
    v2 = version.Version('2.2')
    assert v1 < v2, '''Version('1.1') < Version('2.2') should be True'''
    assert not(v1 > v2), '''Version('1.1') > Version('2.2') should be False'''

# Generated at 2022-06-13 00:02:27.540679
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version()
    v2 = Version()
    assert v1.__ge__(v2)
    raise TypeError



# Generated at 2022-06-13 00:02:32.364841
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class Test(Version):
        def _cmp(self, other):
            return -1
    import unittest
    class Test___eq__(unittest.TestCase):
        def runTest(self):
            t = Test()
            self.assertTrue(t == Test())
            self.assertFalse(t == None)
    return Test___eq__()

# Generated at 2022-06-13 00:02:38.858770
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # Make sure Version instances are ordered correctly
    # The following test fails for instance for the StrictVersion
    # class (see bug #954724)
    class dummy(Version):
        pass
    d1 = dummy("2")
    d2 = dummy()
    assert not d1 < d2
    assert d1 <= d2
    assert d1 != d2
    assert d1 > d2
    assert d1 >= d2
# End unit test for method __ge__ of class Version


# Generated at 2022-06-13 00:02:40.306654
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('1.0.0') >= '1.0.0'

# Generated at 2022-06-13 00:02:47.538778
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import copy
    import pickle
    v = Version('1.2.3.4a3')
    assert v == '1.2.3.4a3'
    assert v <= '1.2.3.4a3'
    assert v < '1.2.3.4a4'
    assert v < '1.2.3.4b1'
    assert v < '1.2.3.5a1'
    assert v < '1.2.4a1'
    assert v < '1.2.4'
    assert v < '1.3a1'
    assert v < '1.3'
    assert v < '2a1'
    assert v < '2'
    assert '1.2.3.4a3' == v

# Generated at 2022-06-13 00:02:50.909929
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """
    Unit test for method __lt__ of class Version
    """
    v = Version()

    assert v.__lt__(None) == NotImplemented


# Generated at 2022-06-13 00:03:24.762431
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version
    ver1 = Version("1.0")
    ver2 = Version("2.0")
    assert ver1 < ver2
    assert ver1 <= ver2
    assert ver2 > ver1
    assert ver2 >= ver1
    assert not (ver1 > ver2)
    assert not (ver1 >= ver2)
    assert not (ver2 < ver1)
    assert not (ver2 <= ver1)
    ver1 = Version("1.0.0")
    ver2 = Version("2.0")
    assert ver1 < ver2
    assert ver1 <= ver2
    assert ver2 > ver1
    assert ver2 >= ver1
    assert not (ver1 > ver2)
    assert not (ver1 >= ver2)
    assert not (ver2 < ver1)

# Generated at 2022-06-13 00:03:28.072998
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v1.parse('1.0')
    v2 = Version()
    v2.parse('2.0')
    assert v1.__gt__(v2) == NotImplemented

# Generated at 2022-06-13 00:03:32.407248
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import unittest
    from distutils.version import Version
    class VersionTestCase(unittest.TestCase):
        def test_Version___eq__(self):
            v1 = Version('1.0')
            v2 = Version('1.0')
            self.assertEqual(v1, v2)

    # Case where we have a mixed type comparision
    v1 = Version('1.0')
    v2 = Version('1.0')
    if v1 == v2:
        pass
    else:
        raise Exception()



# Generated at 2022-06-13 00:03:33.674306
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    inst = Version()
    a = inst.__ge__()

# Generated at 2022-06-13 00:03:35.976977
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert (Version('1.2') == '1.2') == True

# Generated at 2022-06-13 00:03:38.819330
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    a = Version()
    b = Version()
    if a.__gt__(b) == a > b:
        pass

# Generated at 2022-06-13 00:03:47.169502
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    loose_version1 = LooseVersion('1.1')
    loose_version2 = LooseVersion('2.0')
    assert loose_version1 >= loose_version1
    assert loose_version1 >= LooseVersion('1.0')
    assert not loose_version1 >= LooseVersion('1.2')
    assert LooseVersion('1.2') >= loose_version1
    assert LooseVersion('1.1') >= loose_version1
    assert LooseVersion('1.1') >= LooseVersion('1.1')
    assert LooseVersion('1.2') >= LooseVersion('1.2')
    assert not loose_version1 >= LooseVersion('1.1.0')
    assert not loose_version2 >= LooseVersion('2.0.0')

# Generated at 2022-06-13 00:03:49.108444
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    assert v1.__lt__(v2)

# Generated at 2022-06-13 00:03:55.688043
# Unit test for method __le__ of class Version
def test_Version___le__():
    # Test with a known version string
    v = PEP440Version('1.2.3a1')
    assert v <= '1.2.3a1.dev', "Version __le__ when compared with a higher pre-release version did not return True"
    assert v <= '1.2.3', "Version __le__ when compared with a higher release version did not return True"
    assert v <= '1.2.3a1', "Version __le__ when compared with the same version did not return True"


# Generated at 2022-06-13 00:03:58.871965
# Unit test for method __le__ of class Version
def test_Version___le__():
    version = Version()
    version._cmp = None
    try:
        version.__le__('Other')
    except TypeError:
        pass
    except Exception as exc:
        print(str(exc))
        raise AssertionError from exc

# Generated at 2022-06-13 00:04:23.930225
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version
    v1 = Version('1.0')
    v2 = Version('2.0')
    if (v1 > v2):
        raise Exception((v1, v2))

# Generated at 2022-06-13 00:04:26.797190
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    obj = Version()
    result = obj.__lt__("A")
    assert result == NotImplemented
    assert result is NotImplemented


# Generated at 2022-06-13 00:04:31.536777
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    lsv = LooseVersion("1.5.1")
    assert lsv.version == [1, "5", "1"]
    lsv.parse("1.5.1")
    assert lsv.version == [1, "5", "1"]
    lsv.parse("1.5.2b2")
    assert lsv.version == [1, "5", "2", "b", "2"]
    lsv.parse("161")
    assert lsv.version == [161]
    lsv.parse("3.10a")
    assert lsv.version == [3, "10", "a"]
    lsv.parse("8.02")
    assert lsv.version == [8, "02"]
    lsv.parse("3.4j")

# Generated at 2022-06-13 00:04:33.185347
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    Version.__gt__(None, None)
    assert True # TODO: implement your test here

# Generated at 2022-06-13 00:04:43.212163
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils.version import StrictVersion
    s1 = StrictVersion('1.2.3')
    s2 = StrictVersion('1.2.4')
    assert (s1 < s2) == True
    assert (s1 <= s2) == True
    assert (s1 == s2) == False
    assert (s1 >= s2) == False
    assert (s1 > s2) == False
    s2 = StrictVersion('1.2.3')
    assert (s1 < s2) == False
    assert (s1 <= s2) == True
    assert (s1 == s2) == True
    assert (s1 >= s2) == True
    assert (s1 > s2) == False
    s2 = StrictVersion('1.2.0')

# Generated at 2022-06-13 00:04:44.903203
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert(v == None)


# Generated at 2022-06-13 00:04:50.675530
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version("2.0")
    v2 = Version("2.1")
    assert (v1 < v2) is True
    assert (v1 <= v2) is True
    assert (v1 == v2) is False
    assert (v1 != v2) is True
    assert (v1 > v2) is False
    assert (v1 >= v2) is False
test_Version___lt__()



# Generated at 2022-06-13 00:05:01.299083
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Test method __lt__ of class Version"""

    from distutils.version import Version
    from distutils.version import LooseVersion
    from distutils.version import StrictVersion

    # Test Version
    v1 = Version('2.1')
    assert v1 < '2.2'
    assert v1 < v1.parse('2.2')
    assert v1 < LooseVersion('2.2')
    assert v1 < StrictVersion('2.2')
    assert '2.0' < v1
    assert v1.parse('2.0') < v1
    assert LooseVersion('2.0') < v1
    assert StrictVersion('2.0') < v1

    # Test LooseVersion
    v2 = LooseVersion('2.1')
    assert v2 < '2.2'
   

# Generated at 2022-06-13 00:05:02.603134
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version
    v = Version()
    assert v == 0

# Generated at 2022-06-13 00:05:05.866762
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version().__gt__('1') is NotImplemented

    # __gt__ doesn't return a bool or int.
    assert type(Version().__gt__('1')) == NotImplementedType



# Generated at 2022-06-13 00:05:47.412929
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('4.4.4.4')
    assert(v == v)
    assert(v == '4.4.4.4')
    assert(v == '4.4.4.4.4')


# Generated at 2022-06-13 00:05:50.005620
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    for other in (1, 2):
        c = Version()._cmp(other)
        assert c > 0


# Generated at 2022-06-13 00:05:58.139798
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # Version must provide method __gt__ directly
    import unittest


    class C:
        pass


    class D(Version):
        def _cmp(self, other):
            return -1


    for C in (Version, D):
        for i in range(1, 4):
            l = [C('a'), C('b'), C('c')]
            assert l[i - 1] < l[i]
            assert l[i] > l[i - 1]
            assert not l[i - 1] > l[i]
            assert not l[i] < l[i - 1]


    class E(Version):
        def _cmp(self, other):
            if isinstance(other, int):
                return 1


    assert E() > 5
    assert not E() < 5



# Generated at 2022-06-13 00:06:04.180329
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version("1.0.0")
    v2 = Version("1.0.1")
    assert v1 < v2
    assert not v2 < v1
    assert not v1 < v1
    v2 = Version("2.0.0")
    assert v1 < v2
    v1 = Version("1.1.0")
    assert v1 < v2

# Generated at 2022-06-13 00:06:05.720363
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1')
    v2 = Version('2')
    assert v1 < v2

# Generated at 2022-06-13 00:06:08.421829
# Unit test for method __eq__ of class Version
def test_Version___eq__():

    assert(Version('1.0') == Version('1.0'))
    assert(Version('1.1') != Version('1.0'))
    assert(Version('2.0') != Version('1.0'))


# Generated at 2022-06-13 00:06:09.979033
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    version = Version()
    assert version.__eq__('') is NotImplemented


# Generated at 2022-06-13 00:06:12.139093
# Unit test for method __lt__ of class Version
def test_Version___lt__():
  # subtest - override in child class
  return



# Generated at 2022-06-13 00:06:13.274146
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('1.0') < Version('2.0')

# Generated at 2022-06-13 00:06:15.417194
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    print( 'Test method __gt__ of class Version' )

    v = Version('1')
    assert v > '0.0.0.0.0.1'

# Generated at 2022-06-13 00:07:44.673745
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('1.0a1') < Version('1.0b1')

# Generated at 2022-06-13 00:07:45.209651
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    return 0



# Generated at 2022-06-13 00:07:47.918592
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    print("Method __lt__ of class Version")
    lv = LooseVersion("1.0b2")
    nv = LooseVersion("1.0b3")
    assert lv < nv

# Generated at 2022-06-13 00:07:56.113105
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import platform
    ver_platform_py = platform.python_version_tuple()
    print(ver_platform_py)
    ver_platform_py = [int(c) for c in ver_platform_py]
    print(ver_platform_py)
    ver_platform_py = ver_platform_py[0:3]
    print(ver_platform_py)
    ver_platform_py = ".".join([str(c) for c in ver_platform_py])
    print(ver_platform_py)

    v_base = Version(ver_platform_py)
    print(v_base)
    v_base_str = str(v_base)
    print(v_base_str)

    v_s = Version("2.10.0a0")
    print(v_s)
    v

# Generated at 2022-06-13 00:08:04.522388
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    def testit(verstr, expected):
        """verstr -> expected, where expected is a tuple of
        (cmpval, major, minor, patch, prerelease, prerelease_num, serial)"""
        cmpval, major, minor, patch, prerelease, prerelease_num, serial = expected

        v = LooseVersion(verstr)

        assert v.vstring == verstr, 'v.vstring=%r, verstr=%r' % (v.vstring, verstr)
        assert v.version == (major, minor, patch, prerelease, prerelease_num, serial), \
               'v.version=%r, expected[1:]=%r' % (v.version, expected[1:])
        w = LooseVersion(str(v))

# Generated at 2022-06-13 00:08:06.847321
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version("1.0")
    v2 = Version("1.1")
    # lt: c < 0
    assert v1 < v2

# Generated at 2022-06-13 00:08:14.154273
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    assert NotImplemented == v1.__lt__(1)

    v1 = Version(1)
    assert NotImplemented == v1.__lt__('v2')

    v1 = Version('1')
    assert NotImplemented == v1.__lt__('v2')

    v1 = Version('1')
    assert False == v1.__lt__('1')

    v1 = Version('1')
    assert True == v1.__lt__('2')


# Generated at 2022-06-13 00:08:15.329202
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version("1.0") < Version("1.1")



# Generated at 2022-06-13 00:08:18.750735
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    for i in range(1, 9999):
        for j in range(1, 9999):
            if i > j:
                assert Version(i) > Version(j)
            elif i == j:
                assert not Version(i) > Version(j)
            else:
                assert not Version(i) > Version(j)


# Generated at 2022-06-13 00:08:20.102339
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    val = Version().__eq__(Version())
    assert val == NotImplemented

