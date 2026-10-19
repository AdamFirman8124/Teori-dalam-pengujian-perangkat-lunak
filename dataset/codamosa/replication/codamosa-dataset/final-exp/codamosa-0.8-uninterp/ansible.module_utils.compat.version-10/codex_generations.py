

# Generated at 2022-06-12 23:59:26.684815
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version()
    v2 = Version()
    v3 = Version()
    v4 = Version()

    v1.parse('1.0.0')
    v2.parse('2.0.0')
    v3.parse('1.0.0')
    v4.parse('1.1.0')

    assert not v1.__ge__(v2)
    assert v1.__ge__(v3)
    assert v1.__ge__(v4)



# Generated at 2022-06-12 23:59:36.372950
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    v = StrictVersion()
    v.parse('3.4')
    assert v.version == (3, 4, 0), (
        "version tuple not as expected")
    assert v.prerelease is None, (
        "no prerelease should be returned")
    assert str(v) == '3.4', (
        "reconstructed version string not as expected")

    v.parse('3.4.0a2')
    assert v.version == (3, 4, 0), (
        "version tuple not as expected")
    assert v.prerelease == ('a', 2), (
        "prerelease returned not as expected")

    v.parse('3.4.0.2')
    assert v.version == (3, 4, 0), (
        "trailing .0 should be stripped from version string.")

    # Now try some

# Generated at 2022-06-12 23:59:47.226411
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    """Tests for the parse method of class StrictVersion"""
    v = StrictVersion()
    v.parse('1.2')
    assert v.version == (1,2,0)
    assert v.prerelease == None
    v.parse('1.2a1')
    assert v.version == (1,2,0)
    assert v.prerelease == ('a',1)
    v.parse('1.2.3')
    assert v.version == (1,2,3)
    assert v.prerelease == None
    v.parse('1.2.3b1')
    assert v.version == (1,2,3)
    assert v.prerelease == ('b',1)

# Generated at 2022-06-12 23:59:48.499796
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version().__eq__(None) is NotImplemented


# Generated at 2022-06-12 23:59:49.710502
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('1.2.3') <= Version('1.3')


# Generated at 2022-06-12 23:59:56.667782
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v.__ge__(1)
    assert v.__ge__(1.0)
    assert v.__ge__('1')
    assert v.__ge__('1.0')
    assert v.__ge__(1.1)
    assert v.__ge__('1.2.3')
    assert not v.__ge__(1.1, 1)
    assert not v.__ge__('1.1', '1')
    assert not v.__ge__(1.2, 3)
    assert not v.__ge__('1.2', '3')
    assert not v.__ge__(1.2, 4)
    assert not v.__ge__('1.2', '4')

# Generated at 2022-06-13 00:00:01.290103
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('1.2') >= Version('1.2')
    assert Version('1.2') >= '1.2'
    assert Version('1.2') >= '1.1'
    assert not Version('1.2') >= '1.3'
    assert not Version('1.2') >= Version('1.3')



# Generated at 2022-06-13 00:00:03.853551
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    version = distutils.version.Version()
    assert version.__eq__('foo') == NotImplemented



# Generated at 2022-06-13 00:00:07.934008
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version("1.2")
    w = Version("1.3")

    assert v <= w
    assert not v < w
    assert not v > w
    assert v < "1.3"
    assert v <= "1.3"
    assert not v >= "1.3"
    assert not v > "1.3"


# Generated at 2022-06-13 00:00:18.339378
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion('0.4.0').__str__() == '0.4.0'
    assert StrictVersion('0.4.1').__str__() == '0.4.1'
    assert StrictVersion('0.5a1').__str__() == '0.5a1'
    assert StrictVersion('0.5b3').__str__() == '0.5b3'
    assert StrictVersion('0.9.6').__str__() == '0.9.6'
    assert StrictVersion('1.0').__str__() == '1.0'
    assert StrictVersion('1.0.4a3').__str__() == '1.0.4a3'

# Generated at 2022-06-13 00:00:25.113000
# Unit test for method __eq__ of class Version
def test_Version___eq__(): assert Version().__eq__(Version())

# Generated at 2022-06-13 00:00:30.587465
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    r = Version()
    r.parse = lambda x: None
    r._cmp = lambda x: -1
    assert(r.__ge__(None)) == False
    r._cmp = lambda x: 1
    assert(r.__ge__(None)) == True
    r._cmp = lambda x: 0
    assert(r.__ge__(None)) == True
    r._cmp = lambda x: NotImplemented
    assert(r.__ge__(None)) == NotImplemented
    assert(Version().__ge__(None)) == NotImplemented

# Generated at 2022-06-13 00:00:41.716218
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v is v >= v


    class TestVersion(Version):
        def parse(self, vstring):
            self.version = vstring
            self.other = MapVersion(vstring)
        def _cmp(self, other):
            if isinstance(other, Version):
                other = other.other
            return cmp(self.version, other)

    v1 = TestVersion('1.0')
    assert v1 >= '1.0'
    assert v1 >= '1.0rc2'
    assert v1 >= '1.0.0'
    assert v1 >= '1.0.0rc2'
    assert not (v1 >= '1.1')

    v1.other.version = '1.1'
    assert not (v1 >= '1.1')

# Generated at 2022-06-13 00:00:43.649331
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # Version.__gt__
    assert(Version("3.4") > Version("2.1"))
    assert(Version("1.2") > Version("1.2b2"))
    assert(not Version("1.2") > Version("1.2"))

# Generated at 2022-06-13 00:00:47.633369
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version('1.1.1')
    v2 = Version('1.1.2')
    assert v1.__gt__(v2) == False
    assert v2.__gt__(v1) == True

# Generated at 2022-06-13 00:00:50.008052
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    c = v._cmp()
    c = Version.__gt__(v,other)
    assert c is NotImplemented

# Generated at 2022-06-13 00:00:54.012571
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Test case for method __lt__ of class Version."""
    v1 = Version("1.0")
    v2 = Version("2.0")
    assert v1 < v2

# Generated at 2022-06-13 00:00:56.253129
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version("1.2.3")
    v2 = Version("1.3.3")
    assert v1 < v2


# Generated at 2022-06-13 00:00:58.221280
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version('1')
    v2 = Version('1')
    assert v1.__ge__(v2.vstring())

# Generated at 2022-06-13 00:01:01.878166
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import (
        Version,
        )
    from distutils.version import (
        LooseVersion,
        )

    v1 = Version("1.0.0")
    v2 = Version("1.0.0")

    assert v1 <= v2
    assert v1 <= "1.0.0"

# Generated at 2022-06-13 00:01:09.910255
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version
    v = Version('1.3.3')
    assert (Version('1.2.3') != v)

# Generated at 2022-06-13 00:01:11.763509
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    assert v1.__lt__(v2) == NotImplemented

# Generated at 2022-06-13 00:01:12.900830
# Unit test for method __le__ of class Version
def test_Version___le__():
    instance = Version()

# Generated at 2022-06-13 00:01:18.323862
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.2.3-4')
    # Check for a plain version instance
    # On the same version
    assert v == Version('1.2.3-4')
    # On a different version
    assert not v == Version('1.2.3-5')
    # Check for a string
    # On the same version
    assert v == '1.2.3-4'
    # On a different version
    assert not v == '1.2.3-5'
    # Check for a different type
    assert not v == 1

# Generated at 2022-06-13 00:01:25.968692
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import StrictVersion, LooseVersion
    v1 = StrictVersion('1')
    v2 = StrictVersion('2')
    v11 = StrictVersion('1.1')
    assert v1 != v2
    assert v1 != v11
    assert v1 != 1
    assert v1 != 1.1
    assert 1 != v1
    assert 1.1 != v1
    assert v1 != '1'
    assert v1 != '1.1'
    assert '1' != v1
    assert '1.1' != v1
    assert not v1 == v2
    assert not v1 == v11
    assert not v1 == 1
    assert not v1 == 1.1
    assert not 1 == v1
    assert not 1.1 == v1

# Generated at 2022-06-13 00:01:28.647510
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    v2 = Version()
    assert(v >= v2)
# End unit test for method __ge__ of class Version


# Generated at 2022-06-13 00:01:31.593234
# Unit test for method __eq__ of class Version
def test_Version___eq__():
  """Test __eq__ method of Version"""
  a = Version('1.2.3')
  b = Version()
  b.parse('1.2.3')
  eq_(a,b)


# Generated at 2022-06-13 00:01:38.859285
# Unit test for method __le__ of class Version
def test_Version___le__():
    import unittest
    from distutils.version import LooseVersion, StrictVersion
    from distutils.tests.test_version import VersionBase

    class VersionTest(VersionBase):

        def __init__(self, *args):
            VersionBase.__init__(self, *args)

            for pver in self.parse_version:
                for lver in self.loose_version:
                    if lver <= pver:
                        self.assertGreaterEqual(
                            LooseVersion(lver), StrictVersion(pver)
                        )
                    else:
                        self.assertLess(
                            LooseVersion(lver), StrictVersion(pver)
                        )

    ###################################################################

    class VersionSub(VersionTest):
        pass

    ###################################################################


# Generated at 2022-06-13 00:01:39.866173
# Unit test for method __le__ of class Version
def test_Version___le__():
    sv = Version("1.2.3")
    assert sv <= "1.2.3"


# Generated at 2022-06-13 00:01:41.057971
# Unit test for method __le__ of class Version
def test_Version___le__():
    my_class = Version()
    my_class.__le__(1)


# Generated at 2022-06-13 00:01:50.096342
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version()._cmp('1.12') == 0
    assert Version('1') == '1'
    assert Version('1') >= '1'
    return
try:
    test_Version___ge__()
except:
    pass

    # Unit test for method __str__ of class Version

# Generated at 2022-06-13 00:01:51.458679
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    pass


# Generated at 2022-06-13 00:02:03.046774
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from ansible_test._internal.unit.compat.mock import patch
    from ansible_test._internal.utils.version import Version

    v = Version()
    # Version()
    with patch('ansible_test._internal.utils.version.Version.__gt__', return_value=False):
        with patch('ansible_test._internal.utils.version.Version.__eq__', return_value=True):
            assert v.__ge__('other') == True

    with patch('ansible_test._internal.utils.version.Version.__gt__', return_value=True):
        with patch('ansible_test._internal.utils.version.Version.__eq__', return_value=False):
            assert v.__ge__('other') == True


# Generated at 2022-06-13 00:02:05.524947
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    # Test for NotImplemented equality
    assert v.__ge__('') is NotImplemented

# Generated at 2022-06-13 00:02:15.979114
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version(vstring='0.9')
    assert v.__le__('0.9') == True
    assert v.__le__('0.9.0') == True
    assert v.__le__('0.9a1') == True
    assert v.__le__('0.9.1') == True
    assert v.__le__('0.9.1a1') == True
    assert v.__le__('1.0') == True
    assert v.__le__('1.0b3') == True
    assert v.__le__('1.0rc1') == True
    assert v.__le__('1.0.0') == True
    assert v.__le__('1.0.0rc1') == True



# Generated at 2022-06-13 00:02:16.782248
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert True

# Generated at 2022-06-13 00:02:29.840380
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Test that __lt__ properly compares versions.
    from distutils.version import StrictVersion
    assert (StrictVersion('1.5') < StrictVersion('1.6.0a1'))
    assert (not (StrictVersion('1.5a1') < StrictVersion('1.5')))
    assert (StrictVersion('1.5a1') < StrictVersion('1.5a2'))
    assert (StrictVersion('1.5a2') < StrictVersion('1.5a10'))
    assert (StrictVersion('1.5a10') < StrictVersion('1.5b1'))
    assert (StrictVersion('1.5b1') < StrictVersion('1.5c1'))

# Generated at 2022-06-13 00:02:32.948289
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    v.parse = lambda x: x
    v.version = 1
    assert v >= 1
    assert v >= "1"

# Generated at 2022-06-13 00:02:42.765017
# Unit test for method __ge__ of class Version
def test_Version___ge__(): # unit test for method __ge__ of class Version
    a_version = Version('5.2.6')
    b_version = Version('5.2.6')
    c_version = Version('5.2.7')
    assert a_version >= b_version == a_version.__ge__(b_version)
    assert a_version <= b_version == a_version.__le__(b_version)
    assert a_version == b_version == a_version.__eq__(b_version)
    assert a_version != c_version == a_version.__ne__(c_version)
    assert a_version <= c_version == a_version.__le__(c_version)
    assert a_version < c_version == a_version.__lt__(c_version)
    assert c_version > a_

# Generated at 2022-06-13 00:02:44.601977
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version("1.4.4")
    assert v > "1.4"
    assert v > Version("1.4")



# Generated at 2022-06-13 00:02:59.860550
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    global v
    v = Version('1.2.3')
    if (v >= 0) == False:
        raise AssertionError()

# Generated at 2022-06-13 00:03:01.265876
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert not v.__eq__(v)



# Generated at 2022-06-13 00:03:09.060352
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from . import version
    v1 = version.Version("1.2.3")
    v2 = version.Version("1.2.3")
    assert v1 == v2

    v1 = version.Version("1.2.3")
    v2 = version.Version("1.2.4")
    assert v1 != v2

    v1 = version.Version("1.2.3")
    v2 = version.Version("1.2.3b")
    assert v1 != v2

    v1 = version.Version("0.0.0")
    assert v1 == 0


# Generated at 2022-06-13 00:03:09.645817
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert not (Version('1') >= '2')


# Generated at 2022-06-13 00:03:18.795101
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # This is a slightly simplified version of test_verlib.py:VersionTestCase
    class TestVersionClass(Version):
        def parse(self, vstring):
            self.vstring = vstring
        def __str__(self):
            return self.vstring
        def _cmp(self, other):
            if isinstance(other, str):
                other = TestVersionClass(other)
            assert isinstance(other, TestVersionClass)
            return (self.vstring > other.vstring) - (self.vstring < other.vstring)
    testcases = ['4', '4.5', '4.5.1', '4.5.2', '4.5.1.5.2']
    for a, b in zip(testcases, testcases[1:]):
        a, b = TestVersionClass(a),

# Generated at 2022-06-13 00:03:29.803635
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import random
    import operator
    import functools

    # This is not a perfect test, since the implementation of _cmp is
    # not assumed to be perfectly consistent with __lt__, __gt__, etc.
    # As a result, the test for __ge__ may not exactly mirror that for
    # __lt__.  In general, the __ge__ test is not as thorough as the
    # __lt__ test.

    # Create a dictionary such that v1 <op> v2 == expected,
    # for all operators <op> in operators.

# Generated at 2022-06-13 00:03:30.946603
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    for x in (1, 2, 3):
        pass
    else:
        pass

# Generated at 2022-06-13 00:03:31.876825
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('1.0.0') <= Version('1.0.0')

# Generated at 2022-06-13 00:03:33.486688
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.2.3')
    assert(v == '1.2.3')



# Generated at 2022-06-13 00:03:44.315341
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version

    test_vectors = (
        # version1 version2 bool
        ('2.0', '2', True),
        ('2.1', '2.0', True),
        ('2.1', '2.1.0', True),
        ('2.1.2', '2.1.2', True),
        ('2.1.2', '2.1.1', True),
        ('2.1.2b', '2.1.2a', True),
        ('2.1.2a', '2.1.2b', False),
        ('2.1', '2.2', False),
        ('2.0', None, False),
    )


# Generated at 2022-06-13 00:04:02.304613
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version() >= Version()

# Generated at 2022-06-13 00:04:11.411089
# Unit test for method __ge__ of class Version

# Generated at 2022-06-13 00:04:22.907713
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Test that two instances of the same version are equal
    # even if they have different metadata
    v1 = StrictVersion('1.0')
    v2 = StrictVersion('1.0')
    assert v1 == v2

    v1 = StrictVersion('1.0a1')
    v2 = StrictVersion('1.0a1')
    assert v1 == v2

    v1 = StrictVersion('1.0.post1')
    v2 = StrictVersion('1.0.post1')
    assert v1 == v2

    # Test that two instances of different versions are not equal
    assert StrictVersion('1.0a1') != StrictVersion('1.0a2')
    assert StrictVersion('1.0') != StrictVersion('1.0.post1')

    # Test that a

# Generated at 2022-06-13 00:04:30.262356
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import _LooseVersion
    from distutils.version import _StrictVersion
    from distutils.version import Version
    assert(Version('1.2') == Version('1.2'))
    assert(Version('1.2') == '1.2')
    assert(not (Version('1.2') == '2.3'))
    assert(Version() == '')
    assert(Version() == Version())
    assert(not (Version() == Version('1.0')))


# Generated at 2022-06-13 00:04:31.522508
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version().__ge__('') == NotImplemented

# Generated at 2022-06-13 00:04:32.836273
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert (v == Version())



# Generated at 2022-06-13 00:04:36.261449
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.0')
    assert v == '1.0'
    assert v == Version('1.0')
    assert v != '1.1'
    assert v != Version('1.1')

# Generated at 2022-06-13 00:04:39.282782
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert_raises(NotImplementedError, object(), object())
# Unit tests for method __ge__ of class StrictVersion

# Generated at 2022-06-13 00:04:41.125109
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Test for method __le__ of class Version"""
    # No-op test for abstract class Version -- it's just a placeholder
    pass


# Generated at 2022-06-13 00:04:42.289198
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('')
    assert v == Version('')


# Generated at 2022-06-13 00:05:09.940868
# Unit test for method __eq__ of class Version
def test_Version___eq__():

    class MyVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring
        def _cmp(self, other):
            return 0
        def __repr__(self):
            return "MyVersion('%s')" % self.vstring
        def __str__(self):
            return self.vstring

    # test __eq__
    v1 = MyVersion('1.1.1')
    assert v1 == '1.1.1'
    assert v1 == MyVersion('1.1.1')
    assert v1 == v1
    assert not v1 == '1.1.2'
    assert not v1 == MyVersion('1.1.2')
    assert not v1 == '1.1'
    assert not v1 == MyVersion('1.1')

# Generated at 2022-06-13 00:05:11.374795
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v._cmp = lambda x : -1
    assert v <= Version()

# Generated at 2022-06-13 00:05:22.053013
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version('1.2')
    v2 = Version('1.2')
    assert v1 >= v2
    assert not v1 < v2
    assert not v1 > v2
    assert v1 <= v2


    assert not v1 >= v2 + 0.1
    assert v1 < v2 + 0.1
    assert not v1 <= v2 + 0.1
    assert not v1 > v2 + 0.1

    assert not v1 + 0.1 >= v2
    assert not v1 + 0.1 < v2
    assert v1 + 0.1 <= v2
    assert v1 + 0.1 > v2

# Generated at 2022-06-13 00:05:24.855620
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('0.0.0') <= Version('0.0.0')
    assert Version('0.0.0') <= Version('0.0.0')

# Generated at 2022-06-13 00:05:27.208641
# Unit test for method __le__ of class Version
def test_Version___le__():
    Version()
    return None



# Generated at 2022-06-13 00:05:29.684738
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert (Version("1.0") <= "a" == NotImplemented)


# Generated at 2022-06-13 00:05:34.416928
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version(vstring="a.b")
    v2 = Version(vstring="a.b")
    v3 = Version(vstring="a.b.c")
    assert(v1 == v2)
    assert(v1 != v3)



# Generated at 2022-06-13 00:05:35.336377
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    print('Test __ge__ of class Version')

# Generated at 2022-06-13 00:05:40.478440
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    result = None

    try:
        v1 = Version('1.2.3')
        v2 = Version('1.2.3')
        result = v1 == v2
    except:
        pass
    test_version___eq___result = result

    assert test_version___eq___result



# Generated at 2022-06-13 00:05:43.667023
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import Version
    from distutils import version
    v = Version('1.23')
    assert (v >= version.LooseVersion('1.23')) == True

# Generated at 2022-06-13 00:06:51.355102
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    return None # this method is not worth testing separately


    def _cmp(self, other):
        if isinstance(other, StringType):
            other = self.__class__(other)
        if isinstance(other, self.__class__):
            return self._compare(other)
        else:
            return NotImplemented



# Generated at 2022-06-13 00:06:54.527869
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    try:
        ver = Version("1.0.0")
        return ver >= Version("1.0.0")
    except BaseException as e:
        print("Exception: %s" % e)
    return False
assert test_Version___ge__()


# Generated at 2022-06-13 00:06:55.490354
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    return


# Generated at 2022-06-13 00:06:56.988423
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    f = Version('1.0')
    g = Version('1.0')
    assert f == g


# Generated at 2022-06-13 00:06:58.131439
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('1.2') >= Version('1.2')

# Generated at 2022-06-13 00:07:00.306601
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    version1 = Version(vstring='1.1.1')
    version2 = Version(vstring='1.1.2')
    answer = version1 >= version2
    assert answer == False


# Generated at 2022-06-13 00:07:02.920546
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.0')
    v2 = Version('2.0')
    v3 = Version('1.0')
    assert v1 == v1
    assert not (v1 == v2)
    assert not (v2 == v1)
    assert v1 == v3



# Generated at 2022-06-13 00:07:09.720295
# Unit test for method __le__ of class Version
def test_Version___le__():
    import sys
    import pytest

    if not hasattr(sys, 'gettotalrefcount'):
        pytest.skip('needs sys.gettotalrefcount()')

    from distutils.version import Version
    x = Version('1.0a')
    y = Version('1.0b')
    z = Version('1.0')
    pytest.raises(TypeError, "x <= ''")
    assert x <= y
    assert y <= x
    assert x <= z
    assert z <= x
    assert z <= y
    assert y <= z



# Generated at 2022-06-13 00:07:20.391391
# Unit test for method __eq__ of class Version

# Generated at 2022-06-13 00:07:29.758046
# Unit test for method __le__ of class Version
def test_Version___le__():
    import random
    import unittest
    random_str = lambda s: ''.join(random.choice(s) for _ in range(random.randint(2, 3)))
    random_digit = lambda: str(random.randint(0, 9))
    random_digit_pairs = lambda: random_str('2346789')
    random_digit_triples = lambda: random_str('23456789')
    random_digit_1_9 = lambda: random_str('13456789')
    random_digit_2_9 = lambda: random_str('23456789')
    random_digit_5_9 = lambda: random_str('56789')
    random_digit_n_9 = lambda: random_digit()
    random_non_digit = lambda: random.choice('._-+')
    random_

# Generated at 2022-06-13 00:08:34.555829
# Unit test for method __ge__ of class Version
def test_Version___ge__():
  version = Version()
  assert(version.__ge__(1) == NotImplemented)



# Generated at 2022-06-13 00:08:36.638243
# Unit test for method __le__ of class Version
def test_Version___le__():
    print('Running unit test for method __le__ of class Version()')
    a = Version('1.1.1')
    assert a.__le__(a) == True


# Generated at 2022-06-13 00:08:38.548791
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.2.3.dev1')
    assert v == '1.2.3.dev1'



# Generated at 2022-06-13 00:08:39.914269
# Unit test for method __le__ of class Version
def test_Version___le__():
    version = Version()
    assert version.__le__(3) == NotImplemented



# Generated at 2022-06-13 00:08:45.254733
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version()
    v2 = Version()
    v1.parse(v2)

    assert not v1._cmp(v2)

    assert v1 >= v2
    assert v2 >= v1
    assert not (v1 > v2)
    assert not (v2 > v1)

    assert not v1._cmp(v1)

    assert v1 >= v1
    assert v1 <= v1
    assert not (v1 < v1)
    assert not (v1 > v1)

    assert v2._cmp(v1)

    assert v2 >= v1
    assert not (v2 <= v1)
    assert v2 > v1
    assert not (v2 < v1)



# Generated at 2022-06-13 00:08:51.896628
# Unit test for method __le__ of class Version
def test_Version___le__():

    v = Version('1.2.3a4')
    assert (v <= '1.2.3a4')
    assert (v <= '1.2.3b1')
    assert (v <= '1.2.3')
    assert (v <= '1.2.3f3')
    assert (v <= '1.2')
    assert (v <= '1')
    assert (v <= '1.2.3a5')

    assert not (v <= '1.2.3a3')
    assert not (v <= '1.2.2')
    assert not (v <= '1.1.5')

# Generated at 2022-06-13 00:08:56.658542
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import unittest
    class TestVersion___eq__(unittest.TestCase):
        def setUp(self):
            self.Version = _get_object('Version')
        def test__eq__(self):
            self.assertTrue(self.Version()._cmp(self.Version()) == 0)
    return unittest.TestLoader().loadTestsFromTestCase(TestVersion___eq__)

# Generated at 2022-06-13 00:08:57.391956
# Unit test for method __le__ of class Version
def test_Version___le__():
  return



# Generated at 2022-06-13 00:08:58.286089
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version().__eq__(Version()) == NotImplemented


# Generated at 2022-06-13 00:09:02.682835
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('1')
    assert v >= Version('1')
    assert v >= '1'
    assert not v >= '2'
    assert not v >= '1.1'
    assert not v >= Version('2')
    assert not v >= Version('1.1')
test_Version___ge__()

