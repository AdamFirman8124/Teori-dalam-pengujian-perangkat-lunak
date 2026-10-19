

# Generated at 2022-06-12 23:59:17.211223
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    test_obj = StrictVersion('0.4.0')
    assert test_obj.__str__() == "0.4.0"

# Generated at 2022-06-12 23:59:27.317980
# Unit test for method __gt__ of class Version
def test_Version___gt__():
  import copy
  from distutils.version import Version
  from distutils.version import LooseVersion
  from distutils.version import StrictVersion
  # Test everything with StrictVersion
  v = StrictVersion
  assert (v('1.2.3') > '1.2.3') == False
  assert (v('1.2.3') > '1.2.2') == True
  assert (v('1.2.3') > '1.1.3') == True
  assert (v('1.2.3') > '1.2.2b2') == True
  assert (v('1.2.3') > '1.2.3rc2') == False
  assert (v('1.2.3rc2') > v('1.2.3')) == False

# Generated at 2022-06-12 23:59:34.217793
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion('1.2.3').__str__() == '1.2.3'
    assert StrictVersion('1.2').__str__() == '1.2'
    assert StrictVersion('1.2.3a1').__str__() == '1.2.3a1'
    assert StrictVersion('1.2b3').__str__() == '1.2b3'
    assert StrictVersion('1.2a1b3').__str__() == '1.2a1b3'


# Generated at 2022-06-12 23:59:38.287631
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class TestVersion:
        
        def __eq__(self, other):
            c = self._cmp(other)
            if c is NotImplemented:
                return c
            return c == 0

        def _cmp(self, other):
            return NotImplemented
        pass

    v1 = TestVersion()
    v2 = TestVersion()

    assert v1 == v2

# Generated at 2022-06-12 23:59:40.691170
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    f = StrictVersion('0.1.1')
    assert f.__str__() == '0.1.1'


# Generated at 2022-06-12 23:59:42.768810
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('3') >= Version('3')

# Generated at 2022-06-12 23:59:47.820450
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('0.9.6')
    # Test for equivalence relation (Reflexivity)
    assert v == v
    # Test for equivalence relation (Symmetry)
    assert not (v != v)
    # Test for equivalence relation (Transitivity)
    assert v == v
    assert not (v != v)
    assert v == v


# Generated at 2022-06-12 23:59:52.071967
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version("1.2.3") > Version("1.2.2")
    # assert Version("1.2.3") > "1.2.3"  # AttributeError: 'str' object has no attribute 'parse'
    assert Version("1.2.3") > Version("1.2.2")  # True

# Generated at 2022-06-12 23:59:54.021827
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    return True

# Generated at 2022-06-12 23:59:56.827765
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # object __gt__(self, other)
    # Implement __gt__(self, other)
    assert True # TODO: implement your test here


# Generated at 2022-06-13 00:00:09.092587
# Unit test for method __le__ of class Version
def test_Version___le__():
    global Version
    from distutils.version import StrictVersion

    v = StrictVersion("1.2.3a4")
    assert v <= "1.2.3a4"
    assert v <= StrictVersion("1.2.3a4")
    assert not v <= "1.2.3a3"
    assert not v <= StrictVersion("1.2.3a3")

# Generated at 2022-06-13 00:00:10.925400
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version()
    v2 = Version()
    assert v1.__le__(v2)

# Generated at 2022-06-13 00:00:14.640320
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    a = Version('1.2')
    b = Version('1.2')
    assert a == b

    a = Version('1.2')
    b = Version('1.3')
    assert not a == b

# Generated at 2022-06-13 00:00:18.682881
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    # Check if (Version() == Version()) raises TypeError
    try:
        v == v
    except TypeError:
        pass
    else:
        # If no exception raised, report error
        raise AssertionError("Error in Version.__eq__")


# Generated at 2022-06-13 00:00:21.115485
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version("1.2.2a2")
    assert (v1 > "1.2.2a1"), "v1 should be greater than '1.2.2a1'"


# Generated at 2022-06-13 00:00:23.811745
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v.parse("1.0")
    assert (v <= Version("1.0"))



# Generated at 2022-06-13 00:00:25.711592
# Unit test for method __le__ of class Version
def test_Version___le__():
    Version___le__ = Version.__le__
    v = Version()
    assert v.__le__('') is NotImplemented



# Generated at 2022-06-13 00:00:34.174156
# Unit test for method __eq__ of class Version
def test_Version___eq__():

    class TestVersion(Version):

        def parse(self, vstring):
            self.version = tuple(int(i) for i in vstring.split('.'))

        def _cmp(self, other):
            return NotImplemented

    v_one = TestVersion("1.2.3")

    assert v_one == v_one
    assert v_one != "1.2.3"
    assert "1.2.3" != v_one

    assert v_one != None
    assert v_one != [1, 2, 3]
    assert v_one != (1, 2, 3)


# Generated at 2022-06-13 00:00:36.410451
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v._cmp = lambda x: 0
    assert v <= 1



# Generated at 2022-06-13 00:00:38.189485
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v2 = Version()
    assert v <= v2


# Generated at 2022-06-13 00:00:47.214826
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    assert False # TODO: implement your test here


# Generated at 2022-06-13 00:00:48.607177
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version("1.0") == Version("1.0")

# Generated at 2022-06-13 00:00:56.082876
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    if '' in __annotations__:
        return

    v1 = Version('1.2.3.4')
    v2 = Version('1.5.6.7')

    assert (v1 > v2) == False
    assert (v1 > '1.5.6.7') == False
    assert (v2 > '1.2.3.4') == True
    assert (v2 > v1) == True

    assert (v1 < v2) == True
    assert (v1 < '1.5.6.7') == True
    assert (v2 < '1.2.3.4') == False
    assert (v2 < v1) == False




# Generated at 2022-06-13 00:00:59.084259
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    ver1 = Version('1.1')
    ver2 = Version('2.0')
    assert ver1 == Version('1.1')
    assert ver1 != ver2
    assert ver1 != '1.1'


# Generated at 2022-06-13 00:01:03.788072
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Make sure the lt method returns True
    v = Version('1.0')
    assert v < '2.0'
    # Make sure the lt method returns False
    v = Version('2.0')
    assert not v < '1.0'
    # Make sure the lt method returns NotImplemented
    class TestVersion(Version):
        def _cmp(self, other):
            return NotImplemented
    v = TestVersion('1.0')
    assert v < '2.0' is NotImplemented


# Generated at 2022-06-13 00:01:06.931567
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version
    assert Version >= Version
    assert Version >= '1.0'
    assert Version >= '1.0.0'
    assert Version() >= None


# Generated at 2022-06-13 00:01:07.531291
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version().__lt__(None)

# Generated at 2022-06-13 00:01:12.410354
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version('1.0')
    v2 = Version('2.0')
    assert (v1 < v2) == True
    assert (v1 > v2) == False
    assert (v1 == v2) == False
    assert (v1 <= v2) == True
    assert (v1 >= v2) == False
    assert (v1 != v2) == True


# Generated at 2022-06-13 00:01:16.802961
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils2.version import Version
    from distutils2.version import LooseVersion
    v1 = Version("1.0.4")
    v2 = Version("1.0.5")
    v3 = Version("3.0.0")
    assert v2.__gt__(v1)
    assert v2.__gt__(v2) == False
    assert v2.__gt__(v3) == False

# Generated at 2022-06-13 00:01:18.740447
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version().__le__(None) is NotImplemented

# Generated at 2022-06-13 00:01:29.886406
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1')
    v2 = Version('1.0')
    if v1 == v2:
        print('ok')
    else:
        print('ko')

# Generated at 2022-06-13 00:01:31.592999
# Unit test for method __lt__ of class Version
def test_Version___lt__():
   version = Version("1.12")
   return version.__lt__("2.2")


# Generated at 2022-06-13 00:01:33.997369
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    version = Version()
    version2 = Version()
    assert version._cmp(version2) == 0
    assert version.__gt__(version2) == False


# Generated at 2022-06-13 00:01:41.886366
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils.version import LooseVersion
    x = LooseVersion('1.0-a2')
    y = LooseVersion('1.0-a4')
    # Check that type(x) == type(y) is False
    assert type(x) == type(y), "type(x) == type(y)"
    # Check that x < y is True
    assert x < y, "x < y"
    # Check that x <= y is True
    assert x <= y, "x <= y"
    # Check that x == y is False
    assert x == y, "x == y"
    # Check that x >= y is False
    assert x >= y, "x >= y"
    # Check that x > y is False
    assert x > y, "x > y"

# Generated at 2022-06-13 00:01:51.516139
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from six import u
    from py3kcompat import text_type
    from packaging.version import Version
    class StrictVersion(Version):
        pass
    class LooseVersion(Version):
        pass
    version = StrictVersion('1.0')
    # Test with valid input
    str_version = str(version)
    assert version == str_version, 'Test failed for StrintVersion'
    version = LooseVersion('1.0')
    str_version = str(version)
    assert version == str_version, 'Test failed for LooseVersion'
    # Test with invalid input
    version = StrictVersion('1.0')
    str_version = str(version)
    assert version != u(str_version), 'Test failed for StrintVersion'
    version = LooseVersion('1.0')
    str_version

# Generated at 2022-06-13 00:01:54.925746
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version().__gt__(1) == NotImplemented
    return



# Generated at 2022-06-13 00:01:57.244118
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version("1")
    assert v > "0"
    assert not v > "1"
    assert not v > "2"

# Generated at 2022-06-13 00:02:05.263165
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class VersionSelf(Version):
        def __init__(self, vstring): pass
        def parse(self, vstring): pass
        def __str__(self): return ''
        def __cmp__(self, other): return NotImplemented
        def __hash__(self): return hash(str(self))
        def __nonzero__(self): return False

    class VersionOther(Version):
        def __init__(self, vstring): pass
        def parse(self, vstring): pass
        def __str__(self): return ''
        def _cmp(self, other): return 0

    version_self  = VersionSelf('')
    version_other = VersionOther('')

    expected = NotImplemented
    actual = version_self.__gt__(version_other)

    assert actual == expected


# Unit test

# Generated at 2022-06-13 00:02:16.071411
# Unit test for method parse of class LooseVersion

# Generated at 2022-06-13 00:02:26.292052
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import nose
    import sys

    import ansible.module_utils.distro_info

    class VersionTest(ansible.module_utils.distro_info.Version):
        def parse(self, vstring):
            self.vstring = vstring
            self.version = [int(s) for s in vstring.split('.')]

    v1 = VersionTest('1.9.9')
    v2 = VersionTest('1.10.0')

    assert v1 < v2
    assert not v2 < v1
    assert not v1 < v1
    assert not v2 < v2

# Generated at 2022-06-13 00:02:57.264556
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    assert v1._cmp(v2) == 0
    assert v1 < v2



# Generated at 2022-06-13 00:02:58.282540
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert not (Version() > Version())

# Generated at 2022-06-13 00:03:00.573131
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version()
    for i in range(1, 100):
        assert v.__lt__(i) == NotImplemented


# Generated at 2022-06-13 00:03:06.762491
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    if  Version('1.1').__lt__(Version('1.1')) != False:
        print('Failed')
        return False
    elif  Version('1.1').__lt__(Version('1.2')) != True:
        print('Failed')
        return False
    elif  Version('1.2').__lt__(Version('1.1')) != False:
        print('Failed')
        return False
    else:
        return True


# Generated at 2022-06-13 00:03:07.972226
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v > None

# Generated at 2022-06-13 00:03:10.150374
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Test method __lt__ of class Version"""
    from datetime import datetime

    startTime = datetime.now()

    test_strict_version = StrictVersion('1.1.1')

    print(str(datetime.now() - startTime)[:-3])
    return (True)

# Generated at 2022-06-13 00:03:11.384942
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert_equal(Version().__eq__(Version()), True)


# Generated at 2022-06-13 00:03:12.574125
# Unit test for method __eq__ of class Version
def test_Version___eq__(): assert Version().__eq__(object) is NotImplemented


# Generated at 2022-06-13 00:03:17.121563
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version
    v1 = Version('2.2a2')
    v2 = Version('2.2')
    assert(v1 == v2)
    v1 = Version('1.1a1')
    v2 = Version('2.2')
    assert(v1 != v2)

# Generated at 2022-06-13 00:03:18.450370
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    v2 = Version()
    assert v1 == v2

# Generated at 2022-06-13 00:03:45.075413
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    ver1 = Version("1.2")
    ver2 = Version("1.3")
    # should return a boolean
    assert isinstance(ver1 < ver2, bool)

# Generated at 2022-06-13 00:03:47.282896
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # Just Create an instance and check the method __gt__
    from distutils2.version import Version
    v = Version("10.1")
    v.__gt__("10.0")


# Generated at 2022-06-13 00:03:50.132987
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # version.py:81:
    assert Version('1') == Version('1')  # unit test for method __eq__ of class Version

# Generated at 2022-06-13 00:03:53.439183
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__(b'0.1.1') == True
    assert v.__gt__(0.2) == True
    assert v.__gt__('1.1.0') == False
test_Version___gt__()


# Generated at 2022-06-13 00:03:55.943054
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    _lt = Version(vstring='1.0').__lt__
    assert _lt('1.1') == True
    assert _lt('1.0') == False


# Generated at 2022-06-13 00:03:57.521133
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    c = Version()
    assert c.__eq__(Version()) == True


# Generated at 2022-06-13 00:03:59.508705
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Setup
    v1 = Version()
    # Test
    assert v1.__eq__(v1) == True



# Generated at 2022-06-13 00:04:02.086320
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version

    v = Version("1.1")
    assert v > 1.0

# Generated at 2022-06-13 00:04:03.624520
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    other = Version()
    assert v == other

# Generated at 2022-06-13 00:04:12.187248
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import itertools
    import math

    import pytest

    from packaging.version import Version

    class TestVersion(Version):
        # Override so that we can easily test comparisons against other
        # types (str).
        def _cmp(self, other):
            if not isinstance(other, TestVersion):
                impl = getattr(super(TestVersion, self), '_cmp', None)
                if impl is not None:
                    return impl(other)
                else:
                    return NotImplemented
            return Version._cmp(self, other)


    class TestBase(object):

        def __init__(self):
            self.versions = self.get_versions()

        @classmethod
        def get_versions(cls):
            raise NotImplemented


# Generated at 2022-06-13 00:05:05.506246
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    a = Version()
    b = Version()
    c = Version()
    d = Version()
    assert a == b
    assert b == a
    assert a == c


# Generated at 2022-06-13 00:05:06.690896
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.1')
    assert(v == v)


# Generated at 2022-06-13 00:05:08.137578
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version()
    v.parse("2.0")
    assert v < "3.0"



# Generated at 2022-06-13 00:05:14.125157
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    """
    **Tests**

    #. Basic function
    """

    from pkglib_testing.util import extract_from_tb
    from ..version import Version

    def func_a():
        try:
            a = Version('a.b') == Version('b.a')
        except Exception as e:
            return extract_from_tb(e.__traceback__)
        else:
            return None

    result_a = func_a()
    expected_a = None
    assert result_a == expected_a



# Generated at 2022-06-13 00:05:24.917285
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    test_cases = [
        # (values, expected)
        (([Version('1.0'), Version('1.0.0')],), False),
        (([Version('1.0'), Version('2.0')],), True),
        (([Version('1.0'), Version('1.0.1')],), True),
        (([Version('1.0'), Version('0.9.9')],), False),
    ]
    for test_case, expected in test_cases:

        # The Version objects can be unpacked in 2 ways which result in the
        # same behavior
        for length in [1, 2]:
            assert len(test_case) == length, "len(test_case) == %i, length == %i" % (len(test_case), length)
            value = test_case[0]
            args

# Generated at 2022-06-13 00:05:27.733870
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    pass
_Version___gt__ = test_Version___gt__

# Generated at 2022-06-13 00:05:38.301591
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Tests for method __eq__ of class Version
    #
    # Should return True iff self and other represent the same version number;
    # False otherwise
    #

    v = StrictVersion("1.0.0")
    assert (v == StrictVersion("1.0.0"))
    assert not (v == StrictVersion("1.0.1"))
    assert not (v == StrictVersion("1.1.0"))
    assert not (v == StrictVersion("2.0.0"))
    assert not (v == "1.0.0")
    assert not (v == "1.0.1")
    assert not (v == "1.1.0")
    assert not (v == "2.0.0")
    assert not (v == "a")
    assert not (v == "A")

# Generated at 2022-06-13 00:05:39.692035
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1.0') == Version('1.0')

# Generated at 2022-06-13 00:05:42.204976
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.2.3')

    # Test equality with string
    assert(v == '1.2.3')

# Generated at 2022-06-13 00:05:46.396769
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version('1.0')
    v2 = Version('2.0')
    assert v1 < v2
    assert v1 <= v2
    assert not(v1 == v2)
    assert not(v1 > v2)
    assert not(v1 >= v2)
    assert not(v1 != v2)



# Generated at 2022-06-13 00:06:50.215864
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version(vstring='1')
    v2 = Version(vstring='2')
    assert (v1.__gt__(v2)) == False
    assert (v2.__gt__(v1)) == True
    assert (v1.__gt__(v1)) == False

# Generated at 2022-06-13 00:06:51.429178
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('1.1') < Version('1.2')



# Generated at 2022-06-13 00:06:59.634505
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """
    Method `__lt__` of class `Version` should compare correctly.

    Here we test it with a number of known good inputs.
    """
    assert StrictVersion('1.2') < StrictVersion('2.0')
    assert StrictVersion('1.0.0') < StrictVersion('1.0.1')
    assert StrictVersion('1.0.0b1') < StrictVersion('1.0.1b1')
    assert StrictVersion('1.0.0a2') < StrictVersion('1.0.1a2')
    assert StrictVersion('1.0.0a2.post') < StrictVersion('1.0.1a2.post')

# Generated at 2022-06-13 00:07:02.927148
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils.version import LooseVersion
    a = LooseVersion("1.0")
    b = LooseVersion("1.0.post1")
    c = LooseVersion("1.0c1")
    assert not (a < a)
    assert a < b
    assert a < c
    assert not (b < a)
    assert not (b < b)
    assert b < c
    assert not (c < a)
    assert not (c < b)
    assert not (c < c)


# Generated at 2022-06-13 00:07:05.392767
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version().__gt__(None) is NotImplemented
    assert Version()._cmp(None) is NotImplemented



# Generated at 2022-06-13 00:07:13.941140
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    LVP = LooseVersion
    def test(v, expected):
        lv = LVP(v)
        assert lv.version == tuple(expected)
    yield test, "1.5.1", [1,5,1]
    yield test, "161", [161]
    yield test, "3.10a", [3,10,'a']
    yield test, "8.02", [8,2]
    yield test, "3.4j", [3,4,'j']
    yield test, "1996.07.12", [1996,7,12]
    yield test, "3.2.pl0", [3,2,'pl',0]
    yield test, "3.1.1.6", [3,1,1,6]

# Generated at 2022-06-13 00:07:15.334445
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version()._cmp(Version()) == 0


# Generated at 2022-06-13 00:07:18.695856
# Unit test for method __lt__ of class Version
def test_Version___lt__():

    assert Version('0.0.1') < Version('0.1.0')


# Generated at 2022-06-13 00:07:21.929478
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version("1.2.3")
    v2 = Version("1.2.4")
    assert v1 < v2
    assert v1 <= v2
    assert not v1 > v2
    assert not v1 >= v2


# Generated at 2022-06-13 00:07:24.360002
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version('0.0.0')
    v2 = Version('0.1.0')
    assert v1.__gt__(v2)


# Generated at 2022-06-13 00:08:18.512209
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    class VersionSub(Version):
        def _cmp(self, other):
            return self.__gt__(other)

    a = VersionSub('1.1')
    b = VersionSub('1.1')
    c = VersionSub('2.1')

    assert(a == b)
    assert(a < c)
    assert(a <= b)
    assert(c > a)
    assert(c >= a)


# Generated at 2022-06-13 00:08:22.886973
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version("1") < Version("1.1")
    assert Version("1.1") < Version("2")
    assert Version("1.1") < Version("1.2")
    assert not Version("2") < Version("1.1")
    assert not Version("1.2") < Version("1.1")
    assert not Version("1.1") < Version("1.1")

    # Rejects comparisons with non-version objects
    with pytest.raises(TypeError):
        _ = Version("1.1") < "1"

# Generated at 2022-06-13 00:08:29.701413
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    expected = None
    actual = None
    try:
        v1 = Version()
        v2 = Version()
        v1.parse('1.0')
        v2.parse('1.0')
        expected = False
        actual = v1 < v2
    except:
        print( 'Unexpected error:' )
        print( str( sys.exc_info()[1] ) )
        raise
    if expected != actual:
        print( '%s != %s' % ( repr( expected ), repr( actual ) ) )
        raise AssertionError
    return

# Generated at 2022-06-13 00:08:38.475121
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Version.__lt__()"""
    # Version number comparison tests
    # Expected results:
    #     StrictVersion
    #         0.4       < 0.4.0     < 0.4.1a1  < 0.4.1
    #         0.4.1a1   < 0.4.1a2   < 0.4.1b1  < 0.4.1b2
    #         0.4.1b2   < 0.4.1
    #         0.4.1     < 0.4.2a1
    #         0.4.2a1   < 0.4.2a2
    #         0.4.2b1   < 0.4.2
    #         0.4.2     < 0.5a1
    #         0.5a1     <

# Generated at 2022-06-13 00:08:39.604313
# Unit test for method __lt__ of class Version
def test_Version___lt__():
  v = Version('1.0')
  assert v < '1.1'



# Generated at 2022-06-13 00:08:41.166714
# Unit test for method __gt__ of class Version
def test_Version___gt__():
	assert Version('1.2.3').__gt__('1.2.4') == False, 'Version.__gt__()'


# Generated at 2022-06-13 00:08:44.776773
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version()
    assert not (v < v)
    assert v < '0.0'

    for v1 in ['1.0', '1.0.0', '1.0.0.0']:
        for v2 in ['1.0', '1.0.0', '1.0.0.0']:
            ver1 = Version(v1)
            ver2 = Version(v2)

            assert ver1 < '2.0'
            assert ver2 < '2.0'
            assert ver1 <= ver2
            assert ver1 <= v2
            assert ver1 <= '1.0'
            assert ver1 <= '1.0.0'
            assert ver1 <= '1.0.0.0'
            assert not ver1 < ver2
            assert not ver1 < v2

# Generated at 2022-06-13 00:08:46.418375
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version("1.0")
    v2 = Version("2.0")
    assert v1 < v2


# Generated at 2022-06-13 00:08:48.022761
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('0.1').__lt__(Version('0.2'))


# Generated at 2022-06-13 00:08:50.548992
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('1.2.3')
    w = Version('2.3.3')
    if not v.__gt__(w):
        assert False, 'v.__gt__(w) reports False, expected True'
