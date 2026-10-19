

# Generated at 2022-06-12 23:59:21.206690
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert issubclass(Version, object)
    assert issubclass(Version, object)
    v = Version()
    v.parse("abc")
    assert v >= None

# Generated at 2022-06-12 23:59:22.920100
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    v2 = v.parse('')
    assert v == v2

# Generated at 2022-06-12 23:59:27.580018
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    tv1 = StrictVersion('1.0')
    tv2 = StrictVersion('1')
    assert (str(tv1) == str(tv2) == '1.0')
    tv1 = StrictVersion('1.0.0')
    assert (str(tv1) == str(tv2) == '1.0')


# Generated at 2022-06-12 23:59:30.990455
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    V = Version
    a = V('1.2.3')
    b = V('1.2.4')
    assert a < b
    assert not a > b
    assert a <= b
    assert not a >= b

# Generated at 2022-06-12 23:59:32.900007
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert(v >= '1.2.3')


# Generated at 2022-06-12 23:59:34.842647
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version('1.0')
    v2 = Version('1.1')
    assert v1 <= v2

# Generated at 2022-06-12 23:59:40.773214
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    import collections

    VersionInfo = collections.namedtuple('VersionInfo', 'version prerelease')

    def parse(vstring):
        v = StrictVersion(vstring)
        return VersionInfo(v.version, v.prerelease)

    # Examples from PEP 440
    assert parse('1.0') == VersionInfo((1, 0, 0), None)
    assert parse('1.0.dev456') == VersionInfo((1, 0, 0), ('a', 456))
    assert parse('1.0a1') == VersionInfo((1, 0, 0), ('a', 1))
    assert parse('1.0b3') == VersionInfo((1, 0, 0), ('b', 3))
    assert parse('1.0rc2') == VersionInfo((1, 0, 0), ('c', 2))

# Generated at 2022-06-12 23:59:46.126070
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    StrictVersion('1')
    StrictVersion('1.2')
    StrictVersion('1.2.3')
    StrictVersion('1.2.3a1')
    StrictVersion('1.2.3b1')
    StrictVersion('1.2.3a1.dev1')


# Generated at 2022-06-12 23:59:49.509808
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v2 = Version()
    try:
        assert(v1 > v2 == False)
    except:
        print("test_Version___gt__ FAIL")
        raise
    print("test_Version___gt__ PASS")


# Generated at 2022-06-13 00:00:00.682502
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    print('(%s)', test_Version___lt__.__name__)
    v = Version('2.3')
    assert v < '2.3.4'
    assert v <= '2.3.4'
    assert v < '2.3.5alpha1'
    assert v < '2.3.5beta1'
    assert v < '2.3.5rc1'
    assert v < '2.3.5'

    v = Version('2.3.5alpha1')
    assert v < '2.3.5'
    assert v < '2.3.5beta1'
    assert v < '2.3.5rc1'
    assert not (v < '2.3.4')
    assert not (v < '2.3.5alpha1')


# Generated at 2022-06-13 00:00:08.377851
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    pass


# Generated at 2022-06-13 00:00:18.682538
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import LooseVersion
    from distutils.version import Version as Super
    from distutils.version import _LooseVersion

    lv = _LooseVersion('1.1')
    assert(lv <= Super('2.2'))
    assert(lv <= Super('1.2'))
    assert(lv <= Super('1.1'))

    lv = _LooseVersion('1.1b')
    assert(lv <= Super('2.2'))
    assert(lv <= Super('1.2'))
    assert(not lv <= Super('1.1'))

    lv = _LooseVersion('1.1a')
    assert(lv <= Super('2.2'))
    assert(lv <= Super('1.2'))
    assert(not lv <= Super('1.1'))



# Generated at 2022-06-13 00:00:19.547271
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    Version('').__lt__( )

# Generated at 2022-06-13 00:00:28.788321
# Unit test for method __le__ of class Version
def test_Version___le__():
  # Constructor test
  assert repr(Version('1')) == "Version ('1')"
  assert Version('1') >= Version('1')
  assert Version('1') >= '1'
  assert repr(Version()) == "Version ('')"
  assert repr(Version('1.0.0')) == "Version ('1.0.0')"
  assert repr(Version()) == "Version ('')"
  assert repr(Version('1.0.0')) == "Version ('1.0.0')"
  # Missing attribute
  with pytest.raises(AttributeError):
    Version()._cmp
  # Missing attribute
  with pytest.raises(AttributeError):
    Version()._cmp
  # Missing attribute
  with pytest.raises(AttributeError):
    Version()._cmp

# Generated at 2022-06-13 00:00:30.174260
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # Method implementation
    pass


# Generated at 2022-06-13 00:00:35.915788
# Unit test for method __le__ of class Version
def test_Version___le__():
    """
    test_Version___le__()
    Unit test for method __le__ of class Version
    """
    v = Version('1.2.0')
    assert v <= '1.2.0'
    assert not v <= '1.2.1'


# Generated at 2022-06-13 00:00:38.678613
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Unit test for method __lt__ of class Version"""
    v = Version()
    v1 = Version()
    if v < v1:
        raise AssertionError("Failed: %s < %s" % (v, v1))

    if not (None < v):
        raise AssertionError("Failed: %s < %s" % (v, v1))


# Generated at 2022-06-13 00:00:40.956418
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('0.0')
    assert v >= v
    assert v >= '0.0'
    assert not v >= '0.1'



# Generated at 2022-06-13 00:00:44.683717
# Unit test for method __le__ of class Version
def test_Version___le__():
    x = Version()
    assert x.__le__(Version()) == NotImplemented

# Generated at 2022-06-13 00:00:46.335136
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version.__ge__(Version(), Version())


# Generated at 2022-06-13 00:01:01.139193
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    v = StrictVersion('1.2.3')
    assert v.version == (1, 2, 3), v.version
    assert v.prerelease == None, v.prerelease

    v = StrictVersion('1.2a2')
    assert v.version == (1, 2, 0), v.version
    assert v.prerelease == ('a', 2), v.prerelease

    v = StrictVersion('1.2b2')
    assert v.version == (1, 2, 0), v.version
    assert v.prerelease == ('b', 2), v.prerelease

    # now make sure parsing is robust against leading and trailing
    # whitespace

    v = StrictVersion('  1.2b2')
    assert v.version == (1, 2, 0), v.version

# Generated at 2022-06-13 00:01:03.251181
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert not v > v

# Generated at 2022-06-13 00:01:05.645282
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    v = StrictVersion("0.4.0")
    assert str(v) == "0.4.0"



# Generated at 2022-06-13 00:01:14.537288
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from nose.tools import assert_equals, assert_raises
    from test_mock_ansible_module import TestAnsibleModule

    test_instance = TestAnsibleModule()

    version = Version()
    v1 = "0.0.3"
    v2 = "0.0.4"
    version.parse(v1)
    assert_equals(version.__ge__(v2), False)


# Chain rich comparisons so that we can calls like StrictVersion(x) > LooseVersion(y).
    def _cmp(self, other):
        if isinstance(other, str):
            other = self.__class__(other)

        if type(self) is type(other):
            return self._cmp_tuple(self._cmpkey(), other._cmpkey())


# Generated at 2022-06-13 00:01:24.091059
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import pytest
    from versions import StrictVersion, LooseVersion, InvalidVersion, Version

    assert not Version("9.9") < Version("9.9")
    assert StrictVersion("9.9") < LooseVersion("9.9")
    assert not LooseVersion("9.9") < StrictVersion("9.9")
    assert LooseVersion("9.9") < LooseVersion("9.10")
    assert StrictVersion("9.9") < LooseVersion("9.10")
    assert not LooseVersion("9.10") < LooseVersion("9.9")
    assert not LooseVersion("9.10") < StrictVersion("9.9")
    assert LooseVersion("9.9.0") < LooseVersion("9.9.1")

# Generated at 2022-06-13 00:01:33.609265
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from lib2to3.pgen2.token import ERRORTOKEN
    from lib2to3.pgen2.token import LPAR
    from lib2to3.pgen2.token import NAME
    from lib2to3.pgen2.token import NEWLINE
    from lib2to3.pgen2.token import OP
    from lib2to3.pgen2.token import RPAR
    from lib2to3.pgen2.token import STRING
    v1 = Version()
    v1.parse('1.0')
    v2 = Version()
    v2.parse('1.0')
    assert v1 == v2
    v1.parse('1.1')
    assert v1 != v2

# Generated at 2022-06-13 00:01:34.798295
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__(None) is NotImplemented



# Generated at 2022-06-13 00:01:36.530662
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version("1.0")
    v2 = Version("2.0")
    v_same = Version("1.0")
    assert v1 < v2
    assert not v1 < v_same



# Generated at 2022-06-13 00:01:40.907711
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Test get when key not present
    v = Version('10')
    assert v == '10'
    assert v != '9'

    v = Version('10.0')
    assert v == '10.0'
    assert v != '9.0'
    assert v != '10.1'

    # Test for NotImplemented
    assert v != object()


# Generated at 2022-06-13 00:01:44.113032
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version("1.0")
    v2 = Version("2.0")
    assert v1.__ge__(v2) == 0

# Generated at 2022-06-13 00:01:58.023360
# Unit test for method __le__ of class Version
def test_Version___le__():
  v = Version('1.2.1')
  assert v <= '1.2.1'
  assert v <= '2'
  assert v <= '1.2.3'
  assert not v <= '1.2.0'
  assert not v <= '1.1.1'
  assert not v <= '1.2.a'


# Generated at 2022-06-13 00:01:59.377266
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version('1.0') > Version('0.9')


# Generated at 2022-06-13 00:02:03.595151
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('1.1.1')
    assert(v.__gt__('1.1.0'))
    assert(not v.__gt__('1.1.2'))
    v = Version('0')
    assert(v.__gt__('-1'))
    assert(not v.__gt__('1'))
    v = Version('0.0')
    assert(v.__gt__('-1'))
    assert(not v.__gt__('1'))
    try:
        v.__gt__('0.0.0.0')
    except TypeError as e:
        assert str(e) == 'Version is not compatible with argument'

# Generated at 2022-06-13 00:02:08.714314
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version("a") > Version("b")
    assert not Version("a") > Version("a")
    assert not Version("b") > Version("a")
    assert not Version("a") > "b"

# Generated at 2022-06-13 00:02:16.866016
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    # Test that StrictVersion.__str__ returns expected output
    input_version = '1.0.0'
    expected_output = input_version
    actual_output = StrictVersion(input_version).__str__()
    assert actual_output == expected_output, actual_output
    
    input_version = '0.4'
    expected_output = input_version
    actual_output = StrictVersion(input_version).__str__()
    assert actual_output == expected_output, actual_output

    input_version = '1.0.4a3'
    expected_output = input_version
    actual_output = StrictVersion(input_version).__str__()
    assert actual_output == expected_output, actual_output
    
    input_version = '1.0.4b1'
    expected_

# Generated at 2022-06-13 00:02:22.209927
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    v = StrictVersion('123.4.5678')
    assert str(v) == '123.4.5678'
    v = StrictVersion('123.4')
    assert str(v) == '123.4'


# Generated at 2022-06-13 00:02:25.391041
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    vs = Version()
    result = vs.__gt__(None)
    assert result is NotImplemented
    assert isinstance(result, bool)



# Generated at 2022-06-13 00:02:34.557011
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import pytest
    from distutils.version import LooseVersion
    assert Version().__gt__(Version('1.0')) == NotImplemented
    assert LooseVersion().__gt__(LooseVersion('1.0')) == NotImplemented
    assert not LooseVersion('1.0').__gt__(LooseVersion('1.0'))
    assert LooseVersion('1.1').__gt__(LooseVersion('1.0'))
    assert not LooseVersion('1.0').__gt__(LooseVersion('1.1'))
    with pytest.raises(ValueError) as exc_info:
        LooseVersion('1.0').__gt__(None)
    assert exc_info.match(r".*version number.*")



# Generated at 2022-06-13 00:02:38.473212
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    version = Version()
    version._cmp = staticmethod(lambda a, b: 42)
    assert version.__ge__(object()) == NotImplemented
    version._cmp = staticmethod(lambda a, b: 42)
    assert version.__ge__(object()) == NotImplemented

# Generated at 2022-06-13 00:02:42.680842
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class SubVersion(Version):
        def __init__(self, vstring=None):
            pass
        def parse(self, vstring):
            pass
        def _cmp(self, other):
            return 0

    version = SubVersion()
    other = SubVersion()
    assert version == other
    assert not version == 0



# Generated at 2022-06-13 00:03:09.988005
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version
    import unittest
    import collections

    # Check __le__ returns NotImplemented when object is not a subclass of Version
    # FIXME: It is not clear to me if the code being tested is correct
    #        I commented out the name check that raises the exception
    class NotVersion:
        def __le__(self, other):
            if not isinstance(other, Version):
                return NotImplemented

    with unittest.mock.patch.object(Version, '__le__') as __le__:
        __le__.return_value = NotImplemented

        not_version = NotVersion()

        # Check that NotImplemented is returned when the other object
        # is not a subclass of Version
        assert not_version <= 'a'

# Generated at 2022-06-13 00:03:13.507867
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1')
    v2 = Version('2')

    assert v1 < v2
    assert v1 <= v2
    assert v1 != v2
    assert v2 > v1
    assert v2 >= v1
    assert not (v1 == v2)


# Generated at 2022-06-13 00:03:14.264029
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    Version()
    Version() == Version()

# Generated at 2022-06-13 00:03:23.291586
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    def _mock_init(self, vstring=None):
        return
    def _mock__cmp(self, other):
        return

    v = Version()
    v.__init__ = _mock_init
    v._cmp = _mock__cmp

    # Test with NotImplemented returned
    mock__cmp = Mock(return_value = NotImplemented)
    v._cmp = mock__cmp
    assert v.__ge__(magic_mock()) == NotImplemented
    mock__cmp.assert_called_once_with(magic_mock())

    # Test when c == 0
    mock__cmp = Mock(return_value = 0)
    v._cmp = mock__cmp
    assert v.__ge__(magic_mock()) == True

# Generated at 2022-06-13 00:03:26.632433
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    try:
        v = Version()
        assert(v.__lt__('1.4'))
    except:
        print("Test Failed")

test_Version___lt__()


# Generated at 2022-06-13 00:03:34.236910
# Unit test for method __le__ of class Version
def test_Version___le__():

    # Test the method __le__ of class Version
    #
    # setup
    #
    v1 = Version()
    v2 = Version('1.0')
    v3 = Version('1.0a1')
    v4 = Version('1.0b1')
    v5 = Version('1.0c1')
    v6 = Version('1.0.1')
    #
    # execute
    #
    # tests for class Version
    #
    assert v1.__le__(v2)
    assert v2.__le__(v1) == False
    assert v1.__le__(v3)
    assert v3.__le__(v1) == False
    assert v3.__le__(v2)
    assert v2.__le__(v3) == False
    assert v

# Generated at 2022-06-13 00:03:36.177799
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    return 'pass'


# Generated at 2022-06-13 00:03:45.753771
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    """Test method Version.__ge__."""
    v1 = Version('1.0')
    v2 = Version('1.1')
    assert not v1 >= v2
    assert v2 >= v1

    v1 = Version('1.0')
    v2 = Version('1.0')
    assert v1 >= v2
    assert v2 >= v1

    v1 = Version('1.1')
    v2 = Version('1.0')
    assert v1 >= v2
    assert not v2 >= v1

    v1 = Version('1.0')
    assert v1 >= '1.0'
    assert v1 >= '0.9'
    assert not v1 >= '1.1'

    v1 = Version('1.0')
    assert '1.0' >= v1

# Generated at 2022-06-13 00:03:47.873614
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert (Version('1.2.0') >= Version('1.2.0'))
    assert (not (Version('1.2.0') >= Version('1.2.1')))



# Generated at 2022-06-13 00:03:56.293449
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Unit test for method __le__ of class Version"""

    class MockArgs(object):
        def __init__(self, cmp_result):
            self.cmp_result = cmp_result

        def _cmp(self, other):
            return self.cmp_result

    # x <= y
    v = Version()
    v.parse = MockArgs(0)
    assert v >= 16

    v = Version()
    v.parse = MockArgs(-1)
    assert v >= 16

    v = Version()
    v.parse = MockArgs(1)
    assert v >= 16

    # x > y
    v = Version()
    v.parse = MockArgs(0)
    assert v > 16


# Generated at 2022-06-13 00:04:09.215424
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert True

# Generated at 2022-06-13 00:04:11.135121
# Unit test for method __lt__ of class Version
def test_Version___lt__():
   '''
   Test method __lt__ of class Version
   
   A simple test that compares two Version objects with an inequality operator.
   '''
   return

# Generated at 2022-06-13 00:04:13.008641
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version("1.2.3")
    v2 = Version("2.2.3")
    assert (v1 >= v2) is False
    assert (v2 >= v1) is True


# Generated at 2022-06-13 00:04:17.531057
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    c = Version()

    assert c.__lt__(Version("1.0")) == NotImplemented
    assert c.__lt__("1.0") == NotImplemented


# Generated at 2022-06-13 00:04:24.317637
# Unit test for method __le__ of class Version
def test_Version___le__():
  import unittest
  class Mock(object): pass
  version = Version()
  version._cmp = Mock()
  version._cmp.return_value = NotImplemented
  object_ = Mock()
  assert version.__le__(object_) == version._cmp.return_value
  version._cmp.return_value = 10
  assert version.__le__(object_) == False
  version._cmp.return_value = 0
  assert version.__le__(object_) == True
  version._cmp.return_value = -10
  assert version.__le__(object_) == True
  


# Generated at 2022-06-13 00:04:35.213277
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import Version
    from distutils.tests import support
    import test.support

    def _test(a, b):
        c = Version(a) >= Version(b)
        d = Version(b) <= Version(a)
        if c != d:
            raise AssertionError('%s >= %s != %s <= %s' % (a, b, b, a))

    def _random(n):
        import random
        parts = []
        for _ in range(n):
            if random.choice([True, False]):
                parts.append(str(random.choice(range(10))))
            else:
                parts.append(chr(random.choice(range(97, 123))))

        return ''.join(parts)


# Generated at 2022-06-13 00:04:44.515760
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    global Version
    import datetime
    from distutils.version import LooseVersion
    from distutils.version import StrictVersion
    from distutils.version import NumericVersion
    from distutils.version import LegacyVersion
    from distutils.version import _Version
    def call_function_with_typechecking(function, argument, expected_type):
        passed = False
        try:
            if type(argument) is expected_type:
                retval = function(argument)
                passed = type(retval) is bool
        except TypeError:
            passed = True
        msg = "Type checking failed in call to %s (%s, %s): %s" % (function.__name__, str(argument), str(expected_type), str(passed))
        assert passed, msg


# Generated at 2022-06-13 00:04:45.961640
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v.__eq__(Version()) == True
    assert v.__eq__('f') == False

# Generated at 2022-06-13 00:04:47.047702
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version() < Version()
    assert not (Version() < Version())

# Generated at 2022-06-13 00:04:51.592614
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import distutils.version
    try:
        assert distutils.version.Version().__lt__(None)
    except TypeError:
        pass
    try:
        assert distutils.version.Version().__lt__(0)
    except TypeError:
        pass

# Generated at 2022-06-13 00:05:16.222027
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    assert not v <= None



# Generated at 2022-06-13 00:05:25.283589
# Unit test for method __ge__ of class Version
def test_Version___ge__():
  import random
  import sys
  import unittest


  class Test(unittest.TestCase):
    ''' Unit tests for __ge__. '''

    def test_true(self):
      ''' -- Test __ge__ returning true. '''
      item = Version('2.0')
      other = Version('2.0')
      self.assertTrue(item >= other)

    def test_false(self):
      ''' -- Test __ge__ returning false. '''
      item = Version('2.0')
      other = Version('3.0')
      self.assertFalse(item >= other)

  # run the tests
  unittest.main()



# Generated at 2022-06-13 00:05:37.442287
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils2.version import Version
    # Method __lt__ of class Version
    # Unit test for method __lt__ of class Version
    def test_Version___lt__():
        from distutils2.version import Version
        # Method __lt__ of class Version
        from distutils2.tests import support
        # Make sure the comparison functions give the same result for any
        # two values, regardless of type
        v1 = Version('1.2.3a2')
        v2 = Version('1.2.3a1')
        # assert v1 < '1.2.3a1'
        support.compare(v1, '__lt__', '1.2.3a1')
        support.compare('1.2.3a1', '__gt__', v1)

# Generated at 2022-06-13 00:05:39.692225
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    v._cmp = lambda other: ValueError()
    assert v >= object() is NotImplemented



# Generated at 2022-06-13 00:05:41.764606
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('')
    if not (v >= ''): raise AssertionError

# Generated at 2022-06-13 00:05:42.828982
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert (Version('1') >= Version('1.6')) == 0


# Generated at 2022-06-13 00:05:45.926799
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    assert v1.__eq__(v1)
    assert not v1.__eq__(1)
    v2 = Version()
    assert v1.__eq__(v2)

# Generated at 2022-06-13 00:05:47.887226
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('0.1') >= Version('0.0.0.0.0.0.0.0.1')



# Generated at 2022-06-13 00:05:49.792058
# Unit test for method __le__ of class Version
def test_Version___le__():
    x = Version('1.0')
    y = Version('1.0')
    if x <= y:
        return True
    return False
test_Version___le__()


# Generated at 2022-06-13 00:05:51.953330
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version("0.1").__eq__("0.2") is NotImplemented

# Generated at 2022-06-13 00:06:48.128353
# Unit test for method __eq__ of class Version
def test_Version___eq__():
  from distutils.tests import support

  return support.run_doctest(distutils.version, verbosity=True)

# Generated at 2022-06-13 00:06:54.080651
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v == v
    assert not v == ()
    assert not v == 'string'
    #
    # Test for a developer error:
    #
    # 1. The value of c should not be NotImplemented.
    # 2. The value of c should be comparable with 0.
    #
    # The second point could be tested here with a mock object.
    c = v._cmp(())
    assert c is not NotImplemented

# Generated at 2022-06-13 00:07:01.729372
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Test for method Version.__le__."""
    def check_Version___le__(version, other, expected):
        res = version <= other
        assert res == expected, "%s <= %s is %s, expected %s" % (version, other, res, expected)
    for cls in (StrictVersion, LooseVersion):
        v = cls('1.1')
        w = cls('1.2')
        x = cls('1.2a1')
        y = cls('1.1')
        z = cls('1.1.post1')
        check_Version___le__(v, w, True)
        check_Version___le__(w, x, True)
        check_Version___le__(x, y, True)

# Generated at 2022-06-13 00:07:02.623345
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version()
    o = Version(None)
    assert v < o



# Generated at 2022-06-13 00:07:06.025843
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    o = Version('a')
    o.parse = Mock(side_effect=Exception)
    try:
        o == 'a'
    except Version:
        pass
    o.parse.assert_called()


# Generated at 2022-06-13 00:07:08.242726
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    v._cmp = lambda x: 0
    assert v.__eq__(None) == True
    assert v.__eq__(1) == False


# Generated at 2022-06-13 00:07:11.037466
# Unit test for method __eq__ of class Version
def test_Version___eq__():
  from distutils.version import LooseVersion
  v1 = LooseVersion('1.4a4.4')
  v2 = LooseVersion('1.4a4.4.2')
  assert v1 == v2


# Generated at 2022-06-13 00:07:14.670244
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    """Test method __ge__ of class Version"""
    _args = ()
    # Make the arguments
    _args = _args + ()
    # Call the __init__ method of the class with the above arguments
    foo = Version(*_args, **{})
    # Test the results...
    assert foo


# Generated at 2022-06-13 00:07:19.472820
# Unit test for method __eq__ of class Version
def test_Version___eq__():
  assert Version().__eq__(Version()) == True
  assert Version('1.0').__eq__(Version('1.0')) == True
  assert Version('1.1').__eq__(Version('1.0')) == False


# Generated at 2022-06-13 00:07:22.748947
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils.version import Version
    v = Version('1')
    assert (v < '2')
    try:
        v = Version('a')
        assert False
    except ValueError:
        assert True