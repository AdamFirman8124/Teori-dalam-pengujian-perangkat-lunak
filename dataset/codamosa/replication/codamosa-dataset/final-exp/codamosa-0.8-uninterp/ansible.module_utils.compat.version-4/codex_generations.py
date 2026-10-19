

# Generated at 2022-06-12 23:59:27.842612
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import StrictVersion
    assert StrictVersion("2.0.3") >= StrictVersion("2.0.2")
# End unit test for method __ge__ of class Version
test_Version___ge__()


# Generated at 2022-06-12 23:59:37.243126
# Unit test for method __le__ of class Version
def test_Version___le__():
    from ansible.module_utils.version import LooseVersion
    assert LooseVersion('2.1') <= LooseVersion('2.1')
    assert LooseVersion('2.1') <= LooseVersion('2.2')
    assert LooseVersion('2.1') <= LooseVersion('2.11')
    assert LooseVersion('2.1') <= LooseVersion('3')
    assert LooseVersion('2.1') <= LooseVersion('9')
    assert LooseVersion('2.1') <= LooseVersion('10')
    assert LooseVersion('2.1') <= LooseVersion('11')
    assert LooseVersion('2.1') <= LooseVersion('21')
    assert LooseVersion('2.1') <= LooseVersion('100')

# Generated at 2022-06-12 23:59:48.122526
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning
    from ansiblelint import versioning

# Generated at 2022-06-12 23:59:59.241976
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    try:
        StrictVersion('1')
        raise AssertionError("StrictVersion('1') should have raised ValueError")
    except ValueError:
        pass
    try:
        StrictVersion('1.2.3.4')
        raise AssertionError("StrictVersion('1.2.3.4') should have raised ValueError")
    except ValueError:
        pass

    v = StrictVersion('1.2')
    assert v.version == (1, 2, 0)
    assert v.prerelease == None
    v = StrictVersion('1.2.0')
    assert v.version == (1, 2, 0)
    assert v.prerelease == None

    v = StrictVersion('1.2a1')
    assert v.version == (1, 2, 0)
    assert v.pre

# Generated at 2022-06-13 00:00:02.146819
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    global Version
    v1 = Version("1.0")
    v2 = Version("2.0")
    assert v1 == v1
    assert v1 == "1.0"
    assert not v1 == "1.1"

# Generated at 2022-06-13 00:00:04.781385
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    expected = True
    ans = Version("2.0.0") == Version("2.0.0")
    return ans == expected


# Generated at 2022-06-13 00:00:05.336730
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    pass

# Generated at 2022-06-13 00:00:15.623465
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    '''Unit test for method __ge__ of class Version'''
    from distutils.version import Version

    assert not (Version('1.0') >= Version('1.0.post3')), \
        '''1.0 >= 1.0.post3 should be False'''
    assert not (Version('1.0') >= Version('1.0c1')), \
        '''1.0 >= 1.0c1 should be False'''
    assert not (Version('1.0') >= Version('1.0b1')), \
        '''1.0 >= 1.0b1 should be False'''
    assert Version('1.0') >= Version('1.0a2'), \
        '''1.0 >= 1.0a2 should be True'''

# Generated at 2022-06-13 00:00:23.870112
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils.version import Version
    from distutils.version import StrictVersion as SV
    from distutils.version import LooseVersion as LV

# Generated at 2022-06-13 00:00:27.173430
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    """Unit test for method __ge__ of class Version"""
    v1 = Version('1.2.3')
    v2 = Version('5.5.5')
    assert not v1.__ge__(v2)
    assert v2.__ge__(v1)
    try:
        v1.__ge__('v1')
    except TypeError:
        pass
    except Exception as e:
        print("Expected TypeError, got: %s" % e)
        assert False



# Generated at 2022-06-13 00:00:44.248040
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version()
    if v < 1:
        pass

# Generated at 2022-06-13 00:00:49.434671
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('1.2.3.4')
    other = Version('1.2.3.4')
    assert not v.__gt__(other)
    assert not v.__gt__('1.2.3.4')
    assert not v > other
    assert not v > '1.2.3.4'

# Generated at 2022-06-13 00:00:52.458238
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    v2 = Version()
    assert v1 == v2

# Generated at 2022-06-13 00:00:53.565180
# Unit test for method __ge__ of class Version
def test_Version___ge__(): assert True # FIXME


# Generated at 2022-06-13 00:01:02.272288
# Unit test for method __le__ of class Version
def test_Version___le__():
  from distutils.version import Version
  from distutils.version import LooseVersion
  v1 = Version('1.1')
  v2 = Version('1.2')
  v3 = Version('1.1')
  v4 = Version('1.1.1')
  v5 = Version('2.0')
  v6 = LooseVersion('1.2.3')
  assert v1 <= v2
  assert v1 <= 1.1
  assert v1 <= v3
  assert v1 <= v4
  assert v2 <= v5

# Generated at 2022-06-13 00:01:06.574929
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version(vstring="1.0")
    v2 = Version(vstring="1.0")
    v3 = Version(vstring="1.1")

    return (v1 == v2) and (v1 != v3)



# Generated at 2022-06-13 00:01:07.374918
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert (Version('1') == Version('1'))

# Generated at 2022-06-13 00:01:15.032302
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    cls = Version
    c = cls("0.0.0")
    assert c._cmp(cls("0.0.0")) == 0
    assert c._cmp(cls("0.0.1")) == -1
    assert c._cmp(cls("0.1.0")) == -1
    assert c._cmp(cls("0.1.1")) == -1
    assert c._cmp(cls("1.0.0")) == -1
    assert c._cmp(cls("1.0.1")) == -1
    assert c._cmp(cls("1.1.0")) == -1
    assert c._cmp(cls("1.1.1")) == -1



# Generated at 2022-06-13 00:01:24.536293
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils2.version import Version
    from distutils2.tests import unittest

    class VersionSubclass(Version):
        pass

    v1 = Version("1.0")
    v1_dup = Version("1.0")
    v2 = Version("2.0")
    v2_dup = Version("2.0")
    v2_other = VersionSubclass("2.0")

    assert (v1 >= v1_dup) is True
    assert (v2 >= v2_dup) is True
    assert (v2 >= v2_other) is True

    assert (v1 >= v2) is not True
    assert (v2 >= v1) is True
    assert (v2 >= None) is NotImplemented
    assert (v2 >= v2_other) is True

# Generated at 2022-06-13 00:01:28.981911
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('1.2.3')
    assert v.__gt__('1.2.2') == True
    assert v.__gt__('1.2.3') == False
    assert v.__gt__('1.1.1') == True
test_Version___gt__()

# Generated at 2022-06-13 00:01:47.607307
# Unit test for method __le__ of class Version
def test_Version___le__():
  assert_equal(Version('').__le__(''), True)


# Generated at 2022-06-13 00:01:52.893780
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import unittest
    class VersionTester(unittest.TestCase):
        def test_lt_str(self):
            v = Version()
            self.assertFalse(v.__lt__('1.0'))
            self.assertTrue(v.__lt__('1.0.post1'))
            self.assertFalse(v.__lt__('1.0b1'))
            self.assertTrue(v.__lt__('2.0b1'))
    unittest.main('distutils.tests.test_version', None, exit=False)


# Generated at 2022-06-13 00:01:55.089419
# Unit test for method __le__ of class Version
def test_Version___le__():
    a = Version()
    b = Version()
    assert a <= b


# Generated at 2022-06-13 00:01:56.611038
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    assert v.__le__() == False

# Generated at 2022-06-13 00:01:57.564572
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version("") < Version("")

# Generated at 2022-06-13 00:01:59.609412
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    """
    Invoke __ge__ and verify it behaves correctly
    """
    # XXX to be implemented
    raise NotImplementedError


# Generated at 2022-06-13 00:02:00.530812
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    version = Version("")
    assert (version >= "")
    # TODO: assert (version >= "")


# Generated at 2022-06-13 00:02:06.820102
# Unit test for method __ge__ of class Version
def test_Version___ge__():

    import sys
    if sys.version_info[0] >= 3:
        v1 = Version('1.34a')
        v2 = Version('1.34')
        assert not v1 >= v2
    else:
        v1 = Version('1.34a')
        v2 = Version('1.34')
        assert not v1.__ge__(v2)

    v1 = Version('1.34')
    v2 = Version('1.34')
    assert v1 >= v2

    v1 = Version('1.34b')
    v2 = Version('1.34a')
    assert v1 >= v2

    v1 = Version('1.34')
    v2 = Version('1.34a')
    assert not v1 >= v2

    v1 = Version('1.34a')
    v

# Generated at 2022-06-13 00:02:07.618509
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version()
    assert v.__lt__(None) == NotImplemented


# Generated at 2022-06-13 00:02:08.315012
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert (Version() == Version()) == True


# Generated at 2022-06-13 00:02:47.144721
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    # regular case
    assert v1 < v2 == True
    # TypeError
    try:
        v1 < None
    except TypeError:
        pass


# Generated at 2022-06-13 00:02:49.038536
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    version = Version()
    assert version.__gt__('1.0') == NotImplemented



# Generated at 2022-06-13 00:02:54.274305
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version('1.2.3')
    v2 = Version('1.2.4')
    if v < v2:
        pass

# Generated at 2022-06-13 00:02:54.912027
# Unit test for method __le__ of class Version
def test_Version___le__():
    return

# Generated at 2022-06-13 00:02:57.990933
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    a = StrictVersion('1.6.4.b1')
    __expected = '1.6.4b1'
    __actual = a.__str__()
    assert __expected == __actual


# Generated at 2022-06-13 00:03:07.466566
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    n = 0

    # test failure conditions
    # case 0
    try:
        n += 1
        v1 = Version()
        v2 = Version()
        v2.parse("a.b")
        v1._cmp(v2)
        assert False
    except ValueError:
        pass
    except:
        assert False

    # case 1
    try:
        n += 1
        v1 = Version()
        v1.parse("1.0")
        v2 = Version()
        v2._cmp(v1)
        assert False
    except ValueError:
        pass
    except:
        assert False

    # case 2

# Generated at 2022-06-13 00:03:09.528005
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    c = v.__ge__(99)
    assert c == NotImplemented

# Generated at 2022-06-13 00:03:13.223027
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    """Unit test for method __ge__ of class Version"""
    def _verify(v1, v2, expected):
        """Verify that v1 >= v2 evaluates to expected"""
        actual = (v1 >= v2)
        if actual != expected:
            raise AssertionError("%s >= %s did not evaluate to %s but to %s" % (
                v1, v2, expected, actual))
    #
    _verify(StrictVersion("1.0"), StrictVersion("1.0"), True)
    _verify(StrictVersion("1.0"), StrictVersion("1.0.post9"), False)
    _verify(StrictVersion("1.0"), StrictVersion("1.0.post9.dev9"), False)
# Cleanup
del test_Version___ge__



# Generated at 2022-06-13 00:03:20.973523
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import StrictVersion
    from distutils.version import LooseVersion

    for v1, v2 in [('1.2.3', '2.3.4'), ('0.9', '1.invalid')]:
        assert (StrictVersion(v1) >= StrictVersion(v1))
        assert (StrictVersion(v2) >= StrictVersion(v2))
        assert (StrictVersion(v1) >= StrictVersion(v1))
        assert (LooseVersion(v2) >= LooseVersion(v2))


# Generated at 2022-06-13 00:03:26.900793
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    ans = False
    try:
        v1 = Version('0.0.0')
        v2 = Version('1.0.0')
        ans = v1.__gt__(v2)
    except Exception as err:
        print(err)
    assert (ans == False)



# Generated at 2022-06-13 00:04:37.420023
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('5')
    v2 = Version('5.1')
    assert v1 < v2

# Generated at 2022-06-13 00:04:40.216382
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version

    v = Version('1.2.3')
    assert v <= '1.2.3'


# Generated at 2022-06-13 00:04:47.124091
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    cases = [
  ( ['v1, v2'],
    { 'args': [], 'v1': "", 'v2': "" } ),
  ( ['v1, v2'],
    { 'args': [], 'v1': "1", 'v2': "2" } ),
  ( ['v1, v2'],
    { 'args': [], 'v1': "1", 'v2': "1" } ),
]
    la = len(cases)
    for (i, ((argnames, kwargs), testinput)) in enumerate(cases):
        print('in case {}/{}:'.format(i + 1, la))
        v1 = Version(**kwargs)
        v2 = Version(**kwargs)

# Generated at 2022-06-13 00:04:58.784861
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version("1.2.3") <= Version("1.2.4")
    assert not (Version("1.2.4") <= Version("1.2.3"))
    assert not (Version("1.2.3") <= Version("1.2.3-1"))
    assert not (Version("1.2.3") <= Version("1.2.3a"))
    assert not (Version("1.2.3") <= Version("1.2.3.a"))
    assert not (Version("1.2.3") <= Version("1.2.3.a"))
    assert not (Version("1.2.3") <= Version("1.2.3.a"))
    assert not (Version("1.2.3") <= Version("1.2.3.a"))

# Generated at 2022-06-13 00:05:06.765387
# Unit test for method __le__ of class Version
def test_Version___le__():
   v1 = Version( )
   v2 = Version( )
   # set error variable to None
   err=None
   try:
      v1._cmp=v2._cmp=object()
      # Now compare v1 and v2
      if v1.__le__(v2) is True:
         # If the result is True, set error variable to True
         err=True
   except:
      # we want to catch all exceptions
      # and set error variable to True
      err=True
   # if error variable is None, all OK
   assert err is None, "Unexpected error in __le__ method of Version class"


# Generated at 2022-06-13 00:05:12.928913
# Unit test for method __le__ of class Version
def test_Version___le__():
    def gen_args():
        from random import choice
        from string import ascii_letters
        yield
        for _ in range(100):
            yield ''.join(choice(ascii_letters) for _ in range(10))
    args = list(gen_args())
    not_implemented_count = 0
    for vstring in args:
        v = Version(vstring)
        r = Version(vstring)
        l = Version(vstring)
        c = v._cmp(vstring)
        if c is NotImplemented:
            not_implemented_count += 1
        else:
            assert v >= v
            assert not v >= 'string'
            assert v >= c
            if v != c:
                assert v > c
            assert not v < c
            assert not v <= c

# Generated at 2022-06-13 00:05:23.262954
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import pytest
    v1 = Version("4.3.2.1")
    v2 = Version("4.3.2.1")
    assert v1 == v2
    v1 = Version("4.3.2.1")
    v2 = Version("4.3.2.2")
    assert v1 != v2
    v1 = Version("4.3.2.1")
    v2 = Version("4.3.2.alpha")
    assert v1 != v2
    v1 = Version("4.3.2.alpha")
    v2 = Version("4.3.2.beta")
    assert v1 != v2


# Generated at 2022-06-13 00:05:35.262704
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    vers = StrictVersion("1.2.3")
    if vers.version != (1,2,3):
        raise AssertionError("StrictVersion.parse test 1 failed")

    vers = StrictVersion("1.2")
    if vers.version != (1,2,0):
        raise AssertionError("StrictVersion.parse test 2 failed")

    vers = StrictVersion("1.2a3")
    if vers.version != (1,2,0) or vers.prerelease != ('a', 3):
        raise AssertionError("StrictVersion.parse test 3 failed")

    # Unit test for method __str__ of class StrictVersion

# Generated at 2022-06-13 00:05:46.182427
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from unittest import TestCase
    from distutils.version import Version
    class VersionTests(TestCase):
        def test___lt__(self):
            # Version.__lt__
            self.assertEqual(Version('1.2.2') < Version('1.2.2'), False)
            self.assertEqual(Version('1.2.1') < Version('1.2.2'), True)
            self.assertEqual(Version('1.2.1') < Version('1.2'), True)
            self.assertEqual(Version('1.2') < Version('1.2.1'), True)
            self.assertEqual(Version('1.2.a') < Version('1.2.b'), True)

# Generated at 2022-06-13 00:05:48.383361
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version('1.2.3')
    assert v <= '1.2.3'
    assert not (v <= '1.2.2')

# Generated at 2022-06-13 00:08:25.143016
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class TestVersion(Version):
        def _cmp(self, other):
            return -1

    v1 = TestVersion()
    v2 = TestVersion()
    assert(v1 < v2)



# Generated at 2022-06-13 00:08:29.338031
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v._cmp(None) is NotImplemented
    assert (v > None) == NotImplemented
    assert v._cmp(123) is NotImplemented
    assert (v > 123) == NotImplemented

# Generated at 2022-06-13 00:08:32.121196
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version("1") < Version("2")
    assert Version("1.0") < Version("1.1")
    assert Version("1.1.0") < Version("1.1.1")


# Generated at 2022-06-13 00:08:33.636368
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    """Test for a method __gt__ of a class Version"""
    raise NotImplementedError


# Generated at 2022-06-13 00:08:41.022945
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    assert (
        ( Version('1.2.3').__gt__('1.2.3') ) == False
    ), 'Version: test_Version___gt__ ans 1'

    assert (
        ( Version('2.2.3').__gt__('1.2.3') ) == True
    ), 'Version: test_Version___gt__ ans 2'

    assert (
        ( Version('1.3.3').__gt__('1.2.3') ) == True
    ), 'Version: test_Version___gt__ ans 3'

    assert (
        ( Version('1.2.4').__gt__('1.2.3') ) == True
    ), 'Version: test_Version___gt__ ans 4'



# Generated at 2022-06-13 00:08:43.341202
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    """Unit test for method __gt__ of class Version."""
    v1 = Version(1)
    v2 = Version(2)
    assert v1.__gt__(v2) == False
    assert v1.__gt__(1) == False
    v1 = Version(2)
    v2 = Version(1)
    assert v1.__gt__(v2) == True
    assert v1.__gt__(1) == True


# Generated at 2022-06-13 00:08:48.184979
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    other = object()
    assert v == other == NotImplemented

    v = Version()
    other = Exception()
    assert v == other == NotImplemented

    v = Version()
    other = 0
    assert v == other == NotImplemented

    v = Version('1')
    other = Version('1')
    assert v == other

    v = Version('1')
    other = Version('2')
    assert not v == other

# Generated at 2022-06-13 00:08:49.358467
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('1.2') >= Version('1.2')


# Generated at 2022-06-13 00:08:54.464027
# Unit test for method __lt__ of class Version
def test_Version___lt__():

    class version_subclass(Version):
        pass

    version_subclass_instance = version_subclass()

    assert version_subclass_instance.__lt__(version_subclass_instance) == NotImplemented
    # Error
    assert version_subclass_instance.__lt__() == NotImplemented

    # Error
    assert version_subclass_instance.__lt__(version_subclass) == NotImplemented

# Generated at 2022-06-13 00:08:55.909343
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    version = Version()
    eq_(version.__gt__(None), NotImplemented)

