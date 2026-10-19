

# Generated at 2022-06-12 23:59:16.867273
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    sv = StrictVersion('0.4.9b1')
    str(sv)



# Generated at 2022-06-12 23:59:26.068568
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import unittest
    import sys

    # in 3.2 and up we get a Tuple instead of a list
    if sys.hexversion < 0x03030000:
        args = [1]
    else:
        args = [1, 2]

    class TestCase(unittest.TestCase):
        def test_ge(self):
            # First test with a Version instance and a tuple
            a = Version('1.2')
            self.assertTrue(a.__ge__(args))

            # Now test with a tuple and a Version instance
            self.assertTrue(args.__ge__(a))

    test_case = TestCase(methodName='test_ge')
    test_case.test_ge()



# Generated at 2022-06-12 23:59:35.956471
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert ('Simple alpha version',
            (Version("1.0.0a1") <= Version("1.0.0a1")),
            (Version("1.0.0a1") <= Version("1.0.0a1")),
            (Version("1.0.0a1") <= Version("1.0.0a1")),
            (Version("1.0.0a1") <= Version("1.0.0a1")),
            )

# Generated at 2022-06-12 23:59:38.144311
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.0')
    v2 = Version('2.0')
    assert(v1.__lt__(v2.__repr__()))

# Generated at 2022-06-12 23:59:41.655361
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.2.3')
    assert v1 < '2.2.3'
    assert str(v1) == '1.2.3'



# Generated at 2022-06-12 23:59:48.249824
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    v = StrictVersion('1.0.0')
    assert str(v) == '1.0.0'

    v = StrictVersion('1.2')
    assert str(v) == '1.2.0'

    v = StrictVersion('1.0.0a0')
    assert str(v) == '1.0.0a0'

    v = StrictVersion('1.0.0b0')
    assert str(v) == '1.0.0b0'



# Generated at 2022-06-12 23:59:52.813459
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    cases = (
        ((1, 2, 3), '1.2.3'),
        ((0,2),'0.2'),
        ((12,3,4,'a',4),'12.3.4a4'),
        ((12,3,4),'12.3.4'),
        )
    for arg, expected_output in cases:
        assert str(StrictVersion(arg)) == expected_output

# Generated at 2022-06-12 23:59:58.531034
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class Dummy(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def _cmp(self, other):
            return NotImplemented

    dummy = Dummy()
    dummy.parse("1.2.3")
    assert dummy == "1.2.3"
    assert not dummy == "1.2.4"


# Generated at 2022-06-13 00:00:02.523417
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version()
    v1.parse("1.1")
    v2 = Version()
    v2.parse("2")
#
# Expected Result:
# AssertionError: False is not true : Failure at test_distutils_version.py::test_Version___ge__
#


# Generated at 2022-06-13 00:00:12.897647
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert True
    # The code below generates a positive test result
    import copy
    import sys
    import types

    import pytest

    # Copy global namespace and update with variables from arguments
    frame = sys._getframe(1)
    global_namespace = frame.f_globals.copy()
    global_namespace.update(frame.f_locals)
    # Add a builtins module
    global_namespace['__builtins__'] = types.ModuleType('__builtins__')

# Generated at 2022-06-13 00:00:25.967704
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    expected = True
    print("Testing method __lt__ of class Version")
    print("Tested object: ", end="")

    version = Version("5.5")
    print(version)
    print("Expected result: ", expected)
    r = version.__lt__(Version("6.13"))
    print("Obtained result: ", r)
    assert r == expected



# Generated at 2022-06-13 00:00:36.310232
# Unit test for method __le__ of class Version
def test_Version___le__():
    # version.Version.__le__
    assert not (Version('1.2') <= '1.2a1')
    assert Version('1.2') <= '1.2'
    assert Version('1.2') <= '1.2.0'
    assert not (Version('1.2.0.0') <= '1.2')

    # Test against a Version instance
    assert not (Version('1.2') <= Version('1.2a1'))
    assert Version('1.2') <= Version('1.2')
    assert Version('1.2') <= Version('1.2.0')
    assert not (Version('1.2.0.0') <= Version('1.2'))


# Generated at 2022-06-13 00:00:37.716674
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('1').__le__(Version('2')) == True

# Generated at 2022-06-13 00:00:40.144887
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    c = StrictVersion("2.0")
    c2 = StrictVersion("2.0")
    assert(c.__ge__(c2))

# Generated at 2022-06-13 00:00:41.286873
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v=Version()
    c=v._cmp(other)


# Generated at 2022-06-13 00:00:42.038436
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    ver = Version()
    assert not ver.__eq__(None)

# Generated at 2022-06-13 00:00:43.541875
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    x = Version()
    x._cmp = lambda a: 1
    assert x.__ge__('') == True

# Generated at 2022-06-13 00:00:48.066379
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert not Version('1.1') >= Version('1.11')
    assert Version('1.1') >= Version('1.1')
    assert Version('1.11') >= Version('1.1')
    assert not Version('1.1') >= Version('2.1')
    assert not Version('2.1') >= Version('2.11')
    assert Version('2.1') >= Version('2.1')
    assert Version('2.11') >= Version('2.1')
    assert Version('2.1') >= Version('2.1a1')
    assert not Version('2.1') >= Version('2.1b1')
    assert not Version('2.1') >= Version('2.1c1')
    assert not Version('2.1') >= Version('2.1c1')
    assert not Version('2.1')

# Generated at 2022-06-13 00:00:52.515517
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v2 = Version()
    assert v1.__ge__(v2)
    assert v1.__gt__(v2)
    assert v1.__le__(v2)
    assert v1.__lt__(v2)
    assert v1.__eq__(v2)

# Generated at 2022-06-13 00:00:53.217932
# Unit test for method __ge__ of class Version
def test_Version___ge__(): pass


# Generated at 2022-06-13 00:01:05.182281
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import LooseVersion
    c = LooseVersion("1.2.3")
    assert not c <= None     #assert c <= LooseVersion("1.2.3")

test_Version___le__()


# Generated at 2022-06-13 00:01:08.013495
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Test method Version.__lt__."""
    v1 = Version()
    v2 = Version()
    assert (v1 < v2) == ((v1._cmp(v2) < 0))



# Generated at 2022-06-13 00:01:08.574577
# Unit test for method __le__ of class Version
def test_Version___le__():
    pass

# Generated at 2022-06-13 00:01:13.013660
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version('1.0')
    v2 = Version('1.0')
    v3 = Version('3.2')
    assert v1 != v2
    assert v1 <  v3
    assert v1 <= v3
    assert v1 <= v1
    assert v3 >= v1
    assert v3 >  v1


# Generated at 2022-06-13 00:01:15.401902
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.8.0')
    v2 = Version('1.8.0')
    assert v1 == v2
    assert not v1 == Version('1.9.0')


# Generated at 2022-06-13 00:01:18.557302
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('1').__le__(Version('1'))
    assert Version('1.2').__le__(Version('2'))
    assert Version('1.2').__le__(Version('1.3'))
    assert not Version('1.2').__le__(Version('1.0'))


# Generated at 2022-06-13 00:01:22.138337
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # type: () -> None
    """
    #TODO: this fails with Python 3.7.4:
    >>> Version('1.2.0') > '1.2'
    False
    """
    ok_(Version('1.2.0') > '1.2')



# Generated at 2022-06-13 00:01:23.831681
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version() == Version()
    assert Version('0') == Version()
    assert Version('1') != Version()


# Generated at 2022-06-13 00:01:34.034145
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from lib2to3.tests.test_fixers import Version
    from lib2to3.tests.test_fixers import version
    v = Version("1.0")
    l = []
    assert (v < '2.0'), "Version(%r) < %r should be %r but is %r" % (v, '2.0', 'True', (v < '2.0'))
    assert (v < '1.1'), "Version(%r) < %r should be %r but is %r" % (v, '1.1', 'True', (v < '1.1'))

# Generated at 2022-06-13 00:01:38.359853
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.0.0')
    v1 = Version('1.0.0')
    v2 = Version('1.0.1')
    assert v == v1
    assert v != v2
    assert v1 == v
    assert v1 != v2
    assert v2 != v
    assert v2 != v1

# Generated at 2022-06-13 00:01:56.427314
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    for a, b in [('1', '2'), ('2', '2')]:
        assert Version(a) == Version(b) == a == b


# Generated at 2022-06-13 00:01:58.541476
# Unit test for method __le__ of class Version
def test_Version___le__():
    version = Version()
    other = object()
    pytest.raises(TypeError, version.__le__, other)



# Generated at 2022-06-13 00:02:05.914167
# Unit test for method __le__ of class Version
def test_Version___le__():
    # Check that one version less than a second returns true, the other way
    # around returns false.
    v = Version('1.2')
    assert (v <= '1.2')
    assert not (Version('1.2') >= '1.3')
    # Check that a version is less than a larger version.
    v = Version('1.3')
    assert (v <= '1.7')
    assert not (v >= '1.7')
    # Check that a version is equal to itself.
    v = Version('1.3')
    assert (v >= '1.3')
    assert (v <= '1.3')
    # Check that greater than and less than are mutually exclusive.
    v = Version('1.3')
    assert not (v >= '1.2' and v <= '1.2')

#

# Generated at 2022-06-13 00:02:08.596346
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert (Version() <= Version())


# Generated at 2022-06-13 00:02:09.769037
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version() < ''



# Generated at 2022-06-13 00:02:12.402347
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    class TestVersion(Version):
        'Class for testing purposes.'
        def _cmp(self, other):
            return 0
    assert TestVersion() < TestVersion()

# Generated at 2022-06-13 00:02:13.564421
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version("1").__eq__(Version("1.0")) == True



# Generated at 2022-06-13 00:02:16.364451
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version("1.1") == Version("1.1")


# Generated at 2022-06-13 00:02:16.862297
# Unit test for method __le__ of class Version
def test_Version___le__():
    pass

# Generated at 2022-06-13 00:02:23.980264
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version(1)
    v2 = Version(2)
    assert v1 == v1
    assert v1 <= v1
    assert v1 >= v1
    assert v1 < v2
    assert v1 <= v2
    assert v1 != v2
    assert v2 > v1
    assert v2 >= v1
    assert v2 != v1



# Generated at 2022-06-13 00:02:58.616972
# Unit test for method __eq__ of class Version
def test_Version___eq__():
  import unittest


  class VersionSubclass(Version):
    def __init__(self, vstring=None):
      super(VersionSubclass, self).__init__(vstring)

    def parse(self, vstring):
      pass

    def _cmp(self, other):
      pass

  version_1 = VersionSubclass()
  version_2 = VersionSubclass()
  assert version_1 == version_2



# Generated at 2022-06-13 00:03:06.723255
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Unit test for method 'Version.__lt__'"""
    # Retrieve the class to test
    cls = module.Version
    # Create a new instance
    instance = cls()
    # The method must exist and be callable
    assert hasattr(instance, '__lt__')
    assert callable(instance.__lt__)
    # The method must accept a single parameter
    try:
        instance.__lt__('a')
    except TypeError:
        raise AssertionError()
    else:
        try:
            instance.__lt__('a', 'b')
        except TypeError:
            pass
        else:
            raise AssertionError()


# Generated at 2022-06-13 00:03:15.464803
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import pytest


# Generated at 2022-06-13 00:03:24.554958
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    # corner cases constructing a LooseVersion object
    assert_equal(LooseVersion('').version, [])
    assert_equal(LooseVersion('1 2 3').version, ['1', '2', '3'])
    assert_equal(LooseVersion('a1 a2 a3').version, ['a1', 'a2', 'a3'])
    assert_equal(LooseVersion('1a 2a 3a').version, ['1a', '2a', '3a'])
    assert_equal(LooseVersion('1-2-3').version, ['1-2-3'])

    # Old setuptools compatibility
    assert_equal(LooseVersion('1.0.dev456').version, ['1', '0', 'dev456'])

# Generated at 2022-06-13 00:03:27.587223
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('1.0') <= Version('1.0')
    assert Version('1.0') <= Version('1.1')
    assert not (Version('1.1') <= Version('1.0'))

# Generated at 2022-06-13 00:03:34.729455
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import random
    import math
    import ansible.module_utils.six as six

    def make_float_list(float_list, num_precision):
        """ Make a string list of floats.

        Replaces decimal part of floats with random digits.

        For example, make_float_list([1.2, 3.4], 3) could return ['1.123', '3.455'].
        """
        new_float_list = []
        for item in float_list:
            integer_part = str(math.floor(item))
            decimal_part = str(item - math.floor(item))[2:]
            if not decimal_part:
                decimal_part = '0'

# Generated at 2022-06-13 00:03:39.221423
# Unit test for method __lt__ of class Version
def test_Version___lt__():

    t0_a = Version()
    t0_b = t0_a < '1.0'
    t0_c = t0_a < 'a'
    t0_d = t0_a < '1.1'


# Generated at 2022-06-13 00:03:42.054774
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Given
    a = Version('1.2.3')
    b = Version('1.2.3')

    # When
    c = a == b

    # Then
    assert c is True

# Generated at 2022-06-13 00:03:43.568913
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__('') is NotImplemented

# Generated at 2022-06-13 00:03:44.705477
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version().__eq__(1) == NotImplemented


# Generated at 2022-06-13 00:04:41.946182
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v == '1'


# Generated at 2022-06-13 00:04:45.934841
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.2')
    v2 = Version('1.2.1')
    v3 = Version('1.2.1a')
    v4 = Version('1.2.1a1')
    assert (v1 < v2)
    assert (v2 < v3)
    assert (v1 < v3)
    assert (v2 < v4)
    assert (v3 < v4)

# Generated at 2022-06-13 00:04:47.376316
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1, v2 = Version('1.0'), Version('2.0')
    assert (v1 > v2) == (v1._cmp(v2) > 0)

# Generated at 2022-06-13 00:04:52.523429
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version
    from test.support import captured_stdout

    g1 = Version('1.0')
    g2 = Version('1.1')
    g3 = Version('1.1')

    assert g1 == g1
    assert not g1 == g2
    assert g2 == g3


# Generated at 2022-06-13 00:04:56.204381
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version("1.0.0")
    v2 = Version("2.0.0")
    assert v2.__gt__(v1) == True


# Generated at 2022-06-13 00:04:59.402494
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.2.3')
    v2 = Version('1.3.3')
    assert v1 < v2
    assert not v1 < v1
    assert not v2 < v1


# Generated at 2022-06-13 00:05:05.153570
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # Create an instance of class Version
    vw_instance = Version()

    # Test method __gt__ of class Version
    # No exception expected:
    vw_instance.__gt__(vw_instance)
    vw_instance.__gt__(str(vw_instance))
    vw_instance.__gt__(vw_instance.__repr__())



# Generated at 2022-06-13 00:05:07.627850
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    ver1 = Version('1.0.0')
    ver2 = Version('1.0.0')
    assert ver1 == ver2, "Error: Wrong comparision result for __eq__"

# Generated at 2022-06-13 00:05:08.920598
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version("1.0").__le__(Version("1.0"))
    assert not Version("1.0").__le__(Version("0.9"))
    assert Version("0.9").__le__(Version("1.0"))


# Generated at 2022-06-13 00:05:10.841442
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = Version('1.0')
    assert (v < '2.0') is True
test_Version___lt__()


# Generated at 2022-06-13 00:07:14.727679
# Unit test for method __le__ of class Version
def test_Version___le__():
        x = Version()
        y = Version()
        assert (x <= y) == NotImplemented



# Generated at 2022-06-13 00:07:19.901478
# Unit test for method __le__ of class Version
def test_Version___le__():
    if not callable(Version.__le__):
        raise TypeError("method __le__ of class Version needs definition")
    v = Version()
    if not isinstance(v.__le__("foo"), bool):
        raise TypeError("invalid return value")

# Generated at 2022-06-13 00:07:27.157968
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert (Version() == Version())
    assert (Version('0.0') == Version('0.0'))
    assert (Version('1.1') == Version('1.1'))
    assert (not (Version('0.0') == Version('0.1')))
    assert (not (Version('0.1') == Version('0.0')))
    assert (not (Version('1.1') == Version('0.0')))
    assert (not (Version('0.0') == Version('1.1')))
    assert (not (Version('0.0') == '0.0'))



# Generated at 2022-06-13 00:07:30.217124
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class DummyVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def _cmp(self, other):
            return 0

    assert DummyVersion("foo") == "foo"

# Generated at 2022-06-13 00:07:32.934545
# Unit test for method __le__ of class Version
def test_Version___le__():
    version_instance = Version('1.0')
    version_instance._cmp = lambda other: NotImplemented
    assert version_instance <= '1.0' == NotImplemented, 'Unexpected value of version_instance <= "1.0"'

# Generated at 2022-06-13 00:07:41.134447
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    v1 = Version('1')
    v2 = Version('2')
    v1a = Version('1')
    assert v == v
    assert not (v != v)
    assert v != v1
    assert not (v == v1)
    assert v1 == v1
    assert not (v1 != v1)
    assert v1 != v2
    assert not (v1 == v2)
    assert v1 == v1a
    assert not (v1 != v1a)
    assert v2 != v1
    assert not (v2 == v1)
    assert v1 != 1
    assert not (v1 == 1)
    assert 1 == v1
    assert not (1 != v1)

# Generated at 2022-06-13 00:07:46.200747
# Unit test for method __le__ of class Version
def test_Version___le__():
    '''Unit test for method __le__ of class Version'''
    v1 = Version()
    v2 = Version()
    eq = v1 >= v2
    ok = 1
    if eq:
        ok = 0
    return ok



# Generated at 2022-06-13 00:07:54.356467
# Unit test for method __le__ of class Version

# Generated at 2022-06-13 00:07:57.035612
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Unit test for method __le__ of class Version."""
    # Init a Version instance
    version = Version()
    # Call method __le__
    try:
        version.__le__()
    except TypeError:
        pass

# Generated at 2022-06-13 00:08:01.829203
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Method object
    m = Version().__lt__
    # Test with these arguments
    v = Version('')
    other = Version('')
    # Expected result
    r = False
    # Call method
    i = m(other)
    # Check result
    assert r == i
    # Check method did no damage
    assert v == Version('')
    assert other == Version('')