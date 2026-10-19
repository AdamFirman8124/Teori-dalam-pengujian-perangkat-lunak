

# Generated at 2022-06-12 23:59:19.003012
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version(1)
    v2 = Version(2)
    v3 = Version(3)
    assert v1 != v2
    assert v2 != v3
    assert v1 != v3
test_Version___eq__()


# Generated at 2022-06-12 23:59:21.260362
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    v = StrictVersion(vstring='0.4a1')
    assert str(v) == '0.4a1'


# Generated at 2022-06-12 23:59:29.107335
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion("1.2.3").__str__() == "1.2.3"
    assert StrictVersion("1.2.3a2").__str__() == "1.2.3a2"
    assert StrictVersion("1.2.3b2").__str__() == "1.2.3b2"
    assert StrictVersion("1.2").__str__() == "1.2"
    assert StrictVersion("1.2a1").__str__() == "1.2a1"
    assert StrictVersion("1.2b1").__str__() == "1.2b1"

# Generated at 2022-06-12 23:59:38.146172
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version
    v = Version('1.2.0')
    assert v <= '1.2.0'
    assert v <= '1.2'
    assert v <= '1.2rc0'
    assert v <= '1.2b3'
    assert v <= '1.2.0b3'
    assert v <= '1.2.0rc0'
    assert v <= '1.2.0.post456'
    assert v <= '1.2.0.post456.dev'
    assert not v <= '1.2.0.pre456.dev'
    try:
        v <= '1.2.0.dev456'
    except ValueError:
        pass
    else:
        raise AssertionError
    v = Version('1.2.0.dev456')
   

# Generated at 2022-06-12 23:59:49.139402
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import unittest
    import sys
    import os
    import types

    def _run_test(self):
        self.assertTrue(1.0 >= '2.0')
        self.assertFalse(1.0 >= '1.0')
        self.assertFalse(1.0 >= '1.1')

        # Test that int/float comparisons raise TypeError
        # (see issue 3184)
        self.assertRaises(TypeError, lambda: 7 >= "1.0")
        self.assertRaises(TypeError, lambda: sys.maxsize+1 >= "1.0")
        self.assertRaises(TypeError, lambda: 1.0 >= "1.0")
        self.assertRaises(TypeError, lambda: 1.1 >= "1.0")

        # Test that non-numeric comparisons raise TypeError


# Generated at 2022-06-12 23:59:56.615845
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    v = StrictVersion('0.4.0')
    assert str(v) == '0.4.0'
    v = StrictVersion('0.5a1')
    assert str(v) == '0.5a1'
    v = StrictVersion('1.0.4b1')
    assert str(v) == '1.0.4b1'
    v = StrictVersion('1.0.4')
    assert str(v) == '1.0.4'


# Generated at 2022-06-13 00:00:05.967482
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    instances = [
        Version(),
        Version('0'),
        Version('1'),
        Version('2.1'),
        Version('2.2'),
        Version('2.3'),
        Version('2.4'),
        Version('2.4.4'),
        Version('2.4.4.4'),
        Version('2.4.4.4.4'),
        Version('2.4.4.4.4.4')
    ]
    assert instances[0] == instances[0]
    assert not instances[0].__eq__(None)
    assert not instances[0].__eq__('0')
    assert not instances[0].__eq__('1')
    assert not instances[0].__eq__('2.1')
    assert not instances[0].__eq__('2.2')

# Generated at 2022-06-13 00:00:07.672113
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    c = Version("1.1") == Version("1.1")
    assert c == True

# Generated at 2022-06-13 00:00:14.980426
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    strictVersion = StrictVersion('0.1')
    assert str(strictVersion) == '0.1'

    strictVersion = StrictVersion('0.1.1')
    assert str(strictVersion) == '0.1.1'

    strictVersion = StrictVersion('0.1a1')
    assert str(strictVersion) == '0.1a1'

    strictVersion = StrictVersion('0.1b1')
    assert str(strictVersion) == '0.1b1'



# Generated at 2022-06-13 00:00:23.445511
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    expected_versions = {'1.0': '1.0', '2.0': '2.0', '2.0.0': '2.0',
                         '2.0.0.0': '2.0', '1.0a1': '1.0a1', '2.0b2': '2.0b2',
                         '2.0.0a1': '2.0a1', '2.0.0b2': '2.0b2',
                         '2.0.0.0a1': '2.0a1', '2.0.0.0b2': '2.0b2'}
    for version in expected_versions:
        v = StrictVersion(version)
        assert str(v) == expected_versions[version]


# Generated at 2022-06-13 00:00:36.953045
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    x=Version()
    y=Version()
    x._cmp=lambda self,other:1 if isinstance(other,str) else NotImplemented
    y._cmp=lambda self,other:1 if isinstance(other,str) else NotImplemented
    if x.__ge__(y) != NotImplemented:
        raise(AssertionError())
    return x.__ge__(y)

# Generated at 2022-06-13 00:00:39.840956
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version("1.1")
    v2 = Version("1.2")
    if not v2 >= v1:
        raise AssertionError("Version.__ge__ not functioning")


# Generated at 2022-06-13 00:00:40.719281
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    pass


# Generated at 2022-06-13 00:00:47.831590
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from ansiblelint import utils
    v1 = utils.Version('1.0.2')
    v2 = utils.Version('1.0.12')
    assert (v1 < v2)
    assert not (v1 < v1)
    assert not (v2 < v1)


# Generated at 2022-06-13 00:00:50.575122
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    x = Version()
    y = Version()
    try:
        x.__gt__(y)
    except NotImplementedError:
        pass





# Generated at 2022-06-13 00:00:56.342365
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version('1.0')
    w = Version('2.0')
    x = Version('2.0')
    y = Version('3.0')

    assert v <= w
    assert v <= x
    assert v <= y
    assert w <= x
    assert w <= y
    assert x <= y
    assert x <= x
    assert y <= y



# Generated at 2022-06-13 00:00:59.339752
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.2.3.a')
    v2 = Version('1.2.3.a')
    assert v1 == v2, 'Versions 1.2.3.a should be equal'


# Generated at 2022-06-13 00:01:01.669700
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # Setup
    v = Version('1.2.3')
    # Exercise
    # Verify
    assert v >= Version('1.2.3')
    assert not v >= Version('1.2.4')

# Generated at 2022-06-13 00:01:06.430104
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version().__eq__(Version()), '__eq__ should return True if the two versions are identical'
    assert not Version().__eq__(Version("0.0.0")), '__eq__ should return False if the two versions are not identical'


# Generated at 2022-06-13 00:01:09.745231
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v.__eq__(None) is NotImpleme
    assert v.__eq__([]) is NotImplemented
    assert v.__eq__('1') is False
    assert v.__eq__('1.0') is False


# Generated at 2022-06-13 00:01:32.928335
# Unit test for method __le__ of class Version
def test_Version___le__():
    import unittest
    from types import ModuleType


    class Version_TestCase(unittest.TestCase):
        def test_Version___le__(self):
            from ansible.module_utils._text import to_native

            # Ensure a NotImplementedError is raised when an invalid type is compared
            # to a Version object
            obj = Version('1.0')
            obj2 = object()
            with self.assertRaisesRegex(NotImplementedError, to_native(obj2)):
                obj <= obj2

            # Ensure a TypeError is raised when both objects are of the same type
            # but are not comparable
            obj3 = Version('1.0')
            obj4 = Version('1.1')
            with self.assertRaises(TypeError):
                obj3 <= obj4

            # Ensure '<

# Generated at 2022-06-13 00:01:38.973636
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """
    The _cmp method is not supposed to be called with NotImplemented,
    but catching it anyway just for safety.  (The test case for
    this was changed in Python 2.4, so this test is not quite
    as thorough as it might be.)
    """
    v = Version('1.2.3')
    assert v < '1.2.3'
    assert not(v < '1.2')
    assert v < '1.2.4'
    assert not(v < '1.2.2')
    assert v < '2.0'
    assert not(v < '1.2.3.0')
    assert not(v < 'xxx')
    assert not(v < 1.2)
    assert not(v < (1,2,3))

# Generated at 2022-06-13 00:01:39.361482
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    pass

# Generated at 2022-06-13 00:01:40.683755
# Unit test for method __le__ of class Version
def test_Version___le__():
    version1 = Version("1.0")
    version2 = Version("0.9")
    return version2 <= version1

# Generated at 2022-06-13 00:01:50.380372
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('1') < Version('1.1') == True, \
        "__lt__ should return True when left version < right version"
    assert Version('1') < Version('1') == False, \
        "__lt__ should return False when left version == right version"
    assert Version('1') < Version('0.9') == False, \
        "__lt__ should return False when left version > right version"
    assert Version('1.1') < Version('1.1.1') == True, \
        "__lt__ should return True when left version < right version"
    assert Version('1.1') < Version('1.1') == False, \
        "__lt__ should return False when left version == right version"

# Generated at 2022-06-13 00:01:55.641924
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert(Version("1.0") >= Version("1.0"))
    assert(not(Version("1.0") >= Version("2.0")))

# Generated at 2022-06-13 00:02:03.691719
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    cmp = Version.__ge__
    assert cmp(StrictVersion('1.13.0'), '1.13.0')
    assert cmp(StrictVersion('1.13.0'), StrictVersion('1.13.0'))
    assert cmp(StrictVersion('1.13.1'), StrictVersion('1.13.0'))
    assert cmp(StrictVersion('1.13.0'), StrictVersion('1.13'))
    assert cmp(StrictVersion('1.13.0'), StrictVersion('1.13a0'))
    assert cmp(StrictVersion('1.13.1a0'), StrictVersion('1.13.0'))



# Generated at 2022-06-13 00:02:14.473453
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    for input1, input2, expected_output in [
        ('0.0.0', '1.1.1', True),
        ('1.1.1', '0.0.0', False),
        ('1.1.1', '1.1.1', False),
        ('0.0.0', '0.0.0', False)
    ]:
        v1 = Version(input1)
        v2 = Version(input2)
        assert v1 < v2 == expected_output
        assert v1 <= v2 == expected_output
        assert v2 > v1 == (not expected_output)
        assert v2 >= v1 == (not expected_output)



# Generated at 2022-06-13 00:02:17.471038
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version('1.0')
    v2 = Version('2.0')
    assert v2 > v1
    assert v2.__gt__(v1)

# Generated at 2022-06-13 00:02:25.799290
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version()
    assert v._cmp(0) == -1
    assert v._cmp(1) == -1
    assert v._cmp(2) == -1
    assert v._cmp(3) == -1
    assert v._cmp(4) == -1

    assert v._cmp(None) == 1
    assert v._cmp([]) == 1
    assert v._cmp(["a"]) == 1

# Generated at 2022-06-13 00:02:52.830519
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version() == Version()
    assert Version('1.1') == Version('1.1')

# Generated at 2022-06-13 00:02:55.021386
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    a = Version("1.2")
    b = Version("1.2")
    assert a == b


# Generated at 2022-06-13 00:02:56.049234
# Unit test for method __le__ of class Version
def test_Version___le__():
  # This is a test stub
  pass

# Generated at 2022-06-13 00:03:05.346691
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1  = Version('1.0')
    v2  = Version('1.0')
    v3  = Version('1.0')
    v4  = Version('1.0')
    v5  = Version('1.0')
    v6  = Version('1.0')
    v7  = Version('1.0')
    v8  = Version('1.0')
    v9  = Version('1.0')
    v10 = Version('1.0')
    v11 = Version('1.0')
    v12 = Version('1.0')
    v13 = Version('1.0')
    v14 = Version('1.0')
    v15 = Version('1.0')
    v16 = Version('1.0')
    v17 = Version('1.0')
    v18

# Generated at 2022-06-13 00:03:06.558146
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert (Version() < None) == NotImplemented



# Generated at 2022-06-13 00:03:15.398799
# Unit test for method __ge__ of class Version
def test_Version___ge__():
  import unittest
  from distutils.version import Version
  class Test___ge__(unittest.TestCase):
    def test_with_StrictVersion_good(self):
      from distutils.version import StrictVersion
      a = Version('123')
      b = StrictVersion('123')
      self.assertEqual(a >= b, True)
    def test_with_StrictVersion_bad(self):
      from distutils.version import StrictVersion
      a = Version('123')
      b = StrictVersion('1234')
      self.assertEqual(a >= b, False)
    def test_with_str_equal(self):
      a = Version('123')
      self.assertEqual(a >= '123', True)

# Generated at 2022-06-13 00:03:17.976976
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version(None).__lt__(Version(None)) == NotImplemented

# Generated at 2022-06-13 00:03:25.417477
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import pytest

    from distutils2.version import Version

    class SubVersion(Version):

        def __init__(self, vstring=None):
            return Version.__init__(self, vstring)

        def _cmp(self, other):

            return (0)

    class SubSubVersion(SubVersion):

        def __init__(self, vstring=None):
            return SubVersion.__init__(self, vstring)

    my_version = SubVersion('1.0')
    another_version = SubVersion('1.0')
    equal_version = SubVersion('1.0')
    second_equal_version = SubVersion('1.0')
    different_version = SubVersion('1.1')
    not_a_version = (1.0)

# Generated at 2022-06-13 00:03:27.944714
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    t = Version("1.0")
    assert (t == Version("1.0")) == True
    assert (t == Version("1.1")) == False

# Generated at 2022-06-13 00:03:34.885092
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import LooseVersion

    assert LooseVersion('1.2.3') >= LooseVersion('1.2.3')
    assert LooseVersion('1.2.3') >= LooseVersion('1.2.3a')
    assert LooseVersion('1.2.3') >= LooseVersion('1.2.3.0')
    assert LooseVersion('1.2.3') >= LooseVersion('1.2.3.0.post.1')
    assert LooseVersion('1.2.3.0.post.1') >= LooseVersion('1.2.3')
    assert LooseVersion('1.2.3') >= LooseVersion('1.2.3a')
    assert LooseVersion('1.2.3c') >= LooseVersion('1.2.3')
    assert Lo

# Generated at 2022-06-13 00:04:30.105112
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    version = Version('1.2.3')
    assert (version > '1.1.1') == True

# Generated at 2022-06-13 00:04:31.013661
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    assert False

# Generated at 2022-06-13 00:04:32.750815
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    version = Version()
    return version.__lt__(object()) == NotImplemented

# Generated at 2022-06-13 00:04:36.532367
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version()
    v2 = Version()
    assert v1 <= v2
    assert v1 <= v1
    assert v1 <= "1.1"
    assert v1 <= 1.1
    assert v1 <= 1
    assert v1 is not None



# Generated at 2022-06-13 00:04:45.468808
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import unittest
    import test.support
    import platform

    class VersionTest(unittest.TestCase):
        def _check_lt(self, exp, v1, v2):
            with test.support.check_py3k_warnings():
                cmp = v1.__lt__(v2)
                self.assertEqual(cmp, exp, '%s.__lt__(%s) should be %s' % (v1, v2, exp))

        def test_version(self):
            self._check_lt(False, Version('1'), Version('1'))
            self._check_lt(True, Version('1'), Version('2'))
            self._check_lt(False, Version('2'), Version('1'))

        def test_same_class(self):
            self._check_lt

# Generated at 2022-06-13 00:04:47.372907
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__(1) is NotImplemented
    assert v.__gt__('1') is False


# Generated at 2022-06-13 00:04:50.591804
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("2.0")
    assert v1 < v2


# Generated at 2022-06-13 00:04:57.158100
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v2 = Version("2.0.0")

    assert v2.__ge__(v2)
    assert v2.__ge__("2.0.0")
    assert v2.__ge__("1.9")


    class OtherVersion(Version):
        pass

    assert not v2.__ge__(OtherVersion("2.0.0"))
    assert not v2.__ge__("other")

# Generated at 2022-06-13 00:04:58.784032
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    assert v1 < v2



# Generated at 2022-06-13 00:05:08.324188
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Version.__lt__()
    assert Version() < Version('0.0')
    assert Version('0.0') < Version('0.1')
    assert Version('0.0.0') < Version('0.0.1')
    assert Version('0.0-1') < Version('0.0-2')
    assert Version('0.0_1') < Version('0.0_2')
    assert Version('0.0a1') < Version('0.0a2')
    assert Version('0.0b1') < Version('0.0b2')
    assert Version('0.0c1') < Version('0.0c2')
    assert Version('0.0rc1') < Version('0.0rc2')

# Generated at 2022-06-13 00:07:10.635142
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('1.2.3')
    assert not v > v
    #
    v = Version('1.2.3')
    assert v > Version('1.2.2')
    #
    v = Version('1.2.3')
    assert not v > Version('1.2.4')
    #
    v = Version('1.2.3')
    assert not v > Version('1.3.3')

# Generated at 2022-06-13 00:07:13.541898
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version
    o = object()
    assert v().__lt__(o) is NotImplemented
    assert v().__lt__(None) is NotImplemented
    assert v().__lt__("") is NotImplemented


# Generated at 2022-06-13 00:07:18.272086
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version('1.0.0')
    v2 = Version('1.0.1')
    v3 = Version('2.0.0')

    assert(not v3 < v2)
    assert(v2 < v3)

# Generated at 2022-06-13 00:07:19.285048
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert True


# Generated at 2022-06-13 00:07:28.753146
# Unit test for method __lt__ of class Version

# Generated at 2022-06-13 00:07:38.335863
# Unit test for method __le__ of class Version
def test_Version___le__():
    import pytest
    from module.version import Version
    from module.version import LooseVersion


    #
    # Test for Version.__le__
    #
    v = Version('1.3.4.7')
    w = Version('1.3.3.6')
    z = LooseVersion('1.3.4.6')

    assert v <= v
    assert not (w <= v)
    assert v >= w
    assert not (v >= z)
    assert not (v == z)

    #
    # Test for LooseVersion.__le__
    #
    v = LooseVersion('1.3.4')
    w = LooseVersion('1.3.3.6')
    z = LooseVersion('1.3.4.6')

    assert v <= v

# Generated at 2022-06-13 00:07:40.109196
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils.version import Version
    v = Version("1.1")
    assert (v < "1.1.1")

# Generated at 2022-06-13 00:07:49.164666
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    """Test method __eq__ of class Version"""

    # Create an instance of Version
    v1 = Version()

    # Test initial value of v1.__eq__
    assert v1.__eq__() == NotImplemented, "Initial value for v1.__eq__ should be 'NotImplemented'"

    # Create an instance of Version
    v2 = Version()

    # Test initial value of v2.__eq__
    assert v2.__eq__() == NotImplemented, "Initial value for v2.__eq__ should be 'NotImplemented'"


# Generated at 2022-06-13 00:07:52.143226
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version("1.0")
    v2 = Version("2")
    v3 = Version("2.0.dev")
    v4 = Version(v3)
    assert v1 <= v2
    assert not v3 <= v1
    assert v3 <= v4



# Generated at 2022-06-13 00:07:53.271786
# Unit test for method __gt__ of class Version
def test_Version___gt__():
  assert Version().__gt__('') == NotImplemented

