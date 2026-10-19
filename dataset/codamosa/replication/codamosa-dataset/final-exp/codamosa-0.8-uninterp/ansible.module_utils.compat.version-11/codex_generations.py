

# Generated at 2022-06-12 23:59:24.036304
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version().__le__(Version()) == NotImplemented
    assert Version().__le__(Version('1')) == NotImplemented
    assert Version().__le__(Version('1.0')) == NotImplemented

# Generated at 2022-06-12 23:59:29.721630
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    x = Version(0)
    y = Version(1)
    assert (x > y) is False
    assert (x >= y) is False
    assert (x < y) is True
    assert (x <= y) is True
    assert (x == y) is False
    assert (x != y) is True

# Generated at 2022-06-12 23:59:32.157399
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('2.7.0')
    assert v > '2.2.0'
    assert v > '2.7'

# Generated at 2022-06-12 23:59:37.068466
# Unit test for method __le__ of class Version
def test_Version___le__():
    ver1 = Version('1.2.3')
    ver2 = Version('1.3')
    asserteq(ver1 <= ver2, True)
    asserteq(ver1 <= '1.2.3', True)

    ver3 = Version('2.0')
    asserteq(ver1 <= ver3, True)
    asserteq(ver1 <= '2.0', True)



# Generated at 2022-06-12 23:59:47.955993
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    ver = Version('1.2.3')

    assert ver.__gt__('1.10') == 0

    assert (ver.__ge__('1.10') == ver.__gt__('1.10') or
            ver.__ge__('1.10') == (not ver.__gt__('1.10')))

    assert (ver.__ge__('1.10') == ver.__le__('1.10') or
            ver.__ge__('1.10') == (not ver.__le__('1.10')))

    assert (ver.__ge__('1.10') == ver.__lt__('1.10') or
            ver.__ge__('1.10') == (not ver.__lt__('1.10')))


# Generated at 2022-06-12 23:59:55.377256
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    StrictVersion("0.4").__str__() == "0.4"
    StrictVersion("0.4.0").__str__() == "0.4"
    StrictVersion("0.4").__str__() == "0.4.0"
    StrictVersion("0.4.1").__str__() == "0.4.1"
    StrictVersion("0.5a1").__str__() == "0.5a1"
    StrictVersion("0.5b3").__str__() == "0.5b3"
    StrictVersion("0.5").__str__() == "0.5"
    StrictVersion("0.9.6").__str__() == "0.9.6"
    StrictVersion("1.0").__str__() == "1.0"

# Generated at 2022-06-12 23:59:57.028405
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version(vstring='1.0')
    v2 = Version(vstring='2.0')
    assert (v2 > v)

# Generated at 2022-06-12 23:59:58.876895
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    v.parse("1.0")
    assert v > "0.9"

# Generated at 2022-06-13 00:00:07.435483
# Unit test for method parse of class StrictVersion

# Generated at 2022-06-13 00:00:17.858797
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    test_instances = [
        StrictVersion("0.4"),
        StrictVersion("0.4.0"),
        StrictVersion("0.4.1"),
        StrictVersion("0.5a1"),
        StrictVersion("0.5b3"),
        StrictVersion("0.5"),
        StrictVersion("0.9.6"),
        StrictVersion("1.0"),
        StrictVersion("1.0.4a3"),
        StrictVersion("1.0.4b1"),
        StrictVersion("1.0.4"),
    ]

# Generated at 2022-06-13 00:00:35.420138
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest
    import platform
    from pip._internal.utils.typing import MYPY_CHECK_RUNNING
    if not MYPY_CHECK_RUNNING:
        class Test(unittest.TestCase):
            def test_eq_ignore_case(self):
                # pylint: disable=comparison-with-callable,no-member
                ver = Version("abc")
                self.assertTrue(ver > "ABC")
                self.assertFalse(ver > "xyz")
        unittest.main()


# Generated at 2022-06-13 00:00:37.268234
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__(None) == NotImplemented


# Generated at 2022-06-13 00:00:39.755154
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version

    version = Version()
    try:
        version.__gt__(0)
    except TypeError:
        pass


# Generated at 2022-06-13 00:00:40.399282
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version('1') > Version('0')



# Generated at 2022-06-13 00:00:41.286739
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    assert v <= v is True

# Generated at 2022-06-13 00:00:42.561620
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('1.0')
    assert v > '0.9'

# Generated at 2022-06-13 00:00:44.093431
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert not Version('1.0.0').__gt__(Version('1.0.0'))
    assert Version('1.0.1').__gt__(Version('1.0.0'))

# Generated at 2022-06-13 00:00:46.337960
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    """Test method __ge__ of class Version with (Version('1.3'), Version('1.3')).
    Expected: True
    """
    v = Version
    exp = True
    arg0 = Version('1.3')
    arg1 = Version('1.3')
    res = v.__ge__(arg0, arg1)
    assert res == exp



# Generated at 2022-06-13 00:00:47.483152
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    pass


# Generated at 2022-06-13 00:00:56.278321
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import collections

    import pytest

    from distutils.version import Version

    class TestVersion(Version):
        RE = "foo"
        def parse(self, vstring):
            self.version = vstring

    v = TestVersion("bar")

    assert isinstance(v >= "1", bool)
    assert isinstance(v >= 1, bool)
    assert not isinstance(v >= object(), bool)
    assert not isinstance(v >= collections.deque(), bool)
    assert not v >= object()
    assert not v >= collections.deque()


    with pytest.raises(TypeError):
        v > object()

    with pytest.raises(NotImplementedError):
        v >= collections.deque()

    with pytest.raises(NotImplementedError):
        "1" >= v

   

# Generated at 2022-06-13 00:01:08.141367
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version('1.2.2')
    v2 = Version('1.2.1')
    assert v1 >= v2


# Generated at 2022-06-13 00:01:09.718122
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = get_version('0.0.0')
    assert v >= v
    assert v >= "0.0.0"


# Generated at 2022-06-13 00:01:11.244059
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    o = Version()
    o._cmp = lambda x: x > 0
    assert o > 0

# Generated at 2022-06-13 00:01:12.402142
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version

    v1 = Version("1.1")
    v2 = Version("2")

    assert v1 <= v2

# Generated at 2022-06-13 00:01:14.462235
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('42')
    assert(v >= '41')
    assert(v >= '42')
    assert(not (v >= '43'))

# Generated at 2022-06-13 00:01:20.713046
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    version = StrictVersion('1.0')
    t = version > '1.0'
    assert t == False
    assert type(t) is bool
    t = version > '3.0'
    assert t == False
    assert type(t) is bool
    t = version > '0.9'
    assert t == True
    assert type(t) is bool
    t = version > StrictVersion('1.0')
    assert t == False
    assert type(t) is bool
    t = version > StrictVersion('3.0')
    assert t == False
    assert type(t) is bool
    t = version > StrictVersion('0.9')
    assert t == True
    assert type(t) is bool
test_Version___gt__()


# Generated at 2022-06-13 00:01:22.548898
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v1 = Version('1')
    assert v1 >= v
test_Version___le__()


# Generated at 2022-06-13 00:01:24.094333
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version() >= Version()


# Generated at 2022-06-13 00:01:27.790165
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    global _test_version_string
    _test_version_string = '3.3.3.3.3'
    lv = LooseVersion('3.3.3.3.3')
    assert lv.version == [3, 3, 3, 3, 3]
    assert lv.vstring == '3.3.3.3.3'
    assert repr(lv) == "LooseVersion ('3.3.3.3.3')"
    assert str(lv) == '3.3.3.3.3'



# Generated at 2022-06-13 00:01:29.323223
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version() > '0.0'


# Generated at 2022-06-13 00:01:41.697340
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest
    class Test_Version(unittest.TestCase):
        def test(self):
            # Version.__gt__
            self.assertTrue(Version('1') > Version('1'))
    unittest.main()



# Generated at 2022-06-13 00:01:49.116582
# Unit test for method __ge__ of class Version
def test_Version___ge__():
  version = Version()
  version._cmp = mock.Mock(return_value=NotImplemented)
  assert not version.__ge__('foo')
  version._cmp = mock.Mock(return_value=-1)
  assert not version.__ge__('foo')
  version._cmp = mock.Mock(return_value=0)
  assert version.__ge__('foo')
  version._cmp = mock.Mock(return_value=1)
  assert version.__ge__('foo')


# Generated at 2022-06-13 00:01:51.842068
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version('1.0')
    v2 = Version('1.0')
    v3 = Version('1.1')
    assert v1 >= v2
    assert not v1 >= v3
    assert v3 >= v1
    assert v3 >= v2

# Generated at 2022-06-13 00:01:53.003958
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version()
    v2 = Version("1.0")
    assert v1 <= v2




# Generated at 2022-06-13 00:01:56.470951
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('1.0')
    assert False is v.__gt__(2)
    assert Exception is type(v.__gt__('a.1'))

# Generated at 2022-06-13 00:01:58.159271
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v._cmp = lambda other: NotImplemented
    assert not v <= object()



# Generated at 2022-06-13 00:02:00.202716
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    impl = Version(vstring='1.2.3')
    assert impl.__gt__('1.2.3') is False


# Generated at 2022-06-13 00:02:02.125659
# Unit test for method __le__ of class Version
def test_Version___le__():
    # Setup
    test = Version()
    # Test
    test.__le__(10)
    # Verify


# Generated at 2022-06-13 00:02:02.969332
# Unit test for method __le__ of class Version
def test_Version___le__():
    return True


# Generated at 2022-06-13 00:02:04.528682
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert (Version().__le__('')) == NotImplemented



# Generated at 2022-06-13 00:02:12.969482
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    assert v <= '1.0'



# Generated at 2022-06-13 00:02:21.403017
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    lv = LooseVersion('1.0.4a3')
    assert str(lv) == '1.0.4a3'
    lv.parse('1.0.4b1')
    assert str(lv) == '1.0.4b1'
    lv.parse('1.0.4')
    assert str(lv) == '1.0.4'

    # Must strip any surrounding whitespace
    lv.parse('\t1.0.4 \r\n')
    assert str(lv) == '1.0.4'


# Generated at 2022-06-13 00:02:27.273663
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version

    major = 2
    minor = 3
    micro = 4
    pre = serial = ''

    ver = Version(str(major) + '.' + str(minor) + '.' + str(micro))
    assert ver.__le__(str(major) + '.' + str(minor) + '.' + str(micro)) == True

# Generated at 2022-06-13 00:02:36.047878
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import mock
    import unittest

    class VersionTest(unittest.TestCase):

        def test_Version___ge__(self):
            import sys
            import types

            import version

            if sys.hexversion >= 0x03000000:
                self.assertIsInstance(version.Version, type)
            else:
                self.assertIsInstance(version.Version, types.ClassType)

            # Patch Version._cmp to always return 0 for any input
            # so that the comparison returns True.
            with mock.patch.object(version.Version, '_cmp', mock.Mock(return_value=0)):

                self.assertTrue(version.Version() >= '1')
            # Test that _cmp was called with the string '1'
            version.Version._cmp.assert_called_with('1')


# Generated at 2022-06-13 00:02:41.711432
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    ver = Version()
    ver.parse('1.2.3.4')
    assert ver >= '0.9.9.9'
    assert not ver >= '1.2.3.4.5'
    ver2 = Version()
    ver2.parse('1.2.3.4')
    assert ver >= ver2
    ver3 = Version()
    ver3.parse('1.2.3.4.5')
    assert not ver >= ver3


# Generated at 2022-06-13 00:02:47.792008
# Unit test for method __le__ of class Version
def test_Version___le__():
    # XXX: Refactor with tests in test_version
    import sys

    # this one compares equal
    v1 = StrictVersion('1.0')
    v2 = StrictVersion('1.0')
    assert v1.__le__(v1)
    if sys.version_info < (2, 4):
        # On pre-2.4 implementations, self-comparisons raised an
        # AttributeError, so we'll assume that that's what's supposed
        # to happen
        try:
            v1.__le__(v1)
        except AttributeError as e:
            pass
        else:
            fail("AttributeError not raised for self-comparison")

    # this one shouldn't compare equal
    v1 = StrictVersion('1.0')
    v2 = StrictVersion('1.1')


# Generated at 2022-06-13 00:02:50.394584
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import random
    for i in range(100000):
        assert random.randint(-1,1)>=0

# Generated at 2022-06-13 00:02:52.979184
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('1.2')
    assert v.__ge__('1.1')


# Generated at 2022-06-13 00:02:59.359110
# Unit test for method __le__ of class Version
def test_Version___le__():

    v_cls = distutils.version.StrictVersion
    assert( v_cls('1.0.0') <= v_cls('1.0.0') )
    assert( not (v_cls('1.0.0') <= v_cls('0.1.0')) )
    assert( v_cls('0.1.0') <= v_cls('1.0.0') )



# Generated at 2022-06-13 00:02:59.979626
# Unit test for method __le__ of class Version
def test_Version___le__():
    pass

# Generated at 2022-06-13 00:03:12.122490
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('1.2.3')
    assert v <= '1.2.3'
    assert v >= '1.2.3'
    assert v >= '1.2.2'
    assert v <= '1.2.4'
    assert v >= '1.2.2a1'


    try:
        v >= 'xxx'
    except ValueError:
        pass
    else:
        assert 0, "expected ValueError"


test_Version___ge__()



# Generated at 2022-06-13 00:03:12.880785
# Unit test for method __ge__ of class Version
def test_Version___ge__():
  v = Version( '2' )
  assert v >= '1'


# Generated at 2022-06-13 00:03:19.462185
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    def tfunc(self, other):
        c = self._cmp(other)
        if c is NotImplemented:
            return c
        return c >= 0

    v = Version()
    assert tfunc(v, 1) == True
    assert tfunc(v, 1.0) == True
    assert tfunc(v, 1.1) == False
    assert tfunc(v, 1.1) == False
    assert tfunc(v, 1.1) == False
    assert tfunc(v, 1.1) == False
    assert tfunc(v, 1.1) == False

# Issue #7943: Added to detect when version_info was expected but version_string was passed.

# Generated at 2022-06-13 00:03:21.275573
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    f = Version()
    try:
        f.__ge__('string')
    except NotImplementedError:
        pass

# Generated at 2022-06-13 00:03:32.150130
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version("2.0").__ge__("2.0")
    assert Version("2.0").__ge__("1.0")
    assert not Version("1.0").__ge__("2.0")
    assert not Version("1.0").__ge__("1.0rc1")
    assert not Version("1.0").__ge__("1.0b2")
    assert not Version("1.0").__ge__("1.0c1")
    assert Version("0.4.0").__ge__("0.4")
    assert Version("1.0.4.0").__ge__("1.0.4")
    assert Version("1.0").__ge__("1.0rc1")
    assert not Version("1.0rc1").__ge__("1.0")

# Generated at 2022-06-13 00:03:36.796171
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('1.0')
    assert v >= '1.0'
    assert v >= Version('1.0')
    assert not v >= '1.1'
    assert not v >= Version('1.1')
    assert not v >= 'invalid vstring'

# Generated at 2022-06-13 00:03:39.665533
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    lv = LooseVersion("1.5.1")
    print("version:", lv, ",words:",lv.version)


# Generated at 2022-06-13 00:03:47.644739
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v >= Version()


    v = Version()
    assert v >= Version('1')
    assert v != Version('1')
    assert v < Version('1')


    assert Version('1') >= Version('1')
    assert Version('1') == Version('1')
    assert Version('1') <= Version('1')

    assert Version('1') >= Version('0')
    assert Version('1') != Version('0')
    assert Version('1') > Version('0')


    assert Version('0') >= Version('1')
    assert Version('0') != Version('1')
    assert Version('0') < Version('1')

    assert Version('01') != Version('1')
    assert Version('01') != Version('1.0')
    assert Version('1.0') != Version('01')


   

# Generated at 2022-06-13 00:03:51.757286
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    version = Version('/domains/example.com/dist/pwntools/pwntools-3.13.0+dev.post2.g9ff6e65-py2.py3-none-any.whl')
    other = Version('/domains/example.com/dist/pwntools/pwntools-3.13.0+dev.post2.g9ff6e65-py2.py3-none-any.whl')
    got = version.__ge__(other)
    assert got == True
    
    


# Generated at 2022-06-13 00:03:53.285736
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    inst = Version()
    assert inst >= None
    assert not (inst >= 3)


# Generated at 2022-06-13 00:04:07.125956
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('0.01')
    assert v >= v
    assert not (v >= '0.02')



# Generated at 2022-06-13 00:04:08.328658
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    ver = Version()
    assert (ver >= None) == NotImplemented



# Generated at 2022-06-13 00:04:14.781882
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    testcase = '''
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from distutils.version import Version
from distutils.tests import support
import unittest
import sys
if __name__ == "__main__":
    unittest.main()
'''
    script = """if __name__ == "__main__":
    support.run_unittest(VersionTestCase)
"""

    def check(self):
        self.assertTrue(Version('1.2.3') >= '1.2.3a')
        self.assertTrue(Version('1.2.3') >= Version('1.2.3a'))
        self.assertFalse(Version('1.2.3') >= '1.2.3.0')

# Generated at 2022-06-13 00:04:23.918981
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    # test non-int components
    assert LooseVersion("1.2a2").version == [1, "2a2"]
    assert LooseVersion("1.2b4").version == [1, "2b4"]
    assert LooseVersion("3.10a").version == [3, "10a"]
    assert LooseVersion("3.4j").version == [3, "4j"]
    assert LooseVersion("2.2beta29").version == [2, "2beta29"]
    assert LooseVersion("1.13++").version == [1, "13++"]
    assert LooseVersion("5.5.kw").version == [5, "5", "kw"]
    assert LooseVersion("2.0b1pl0").version == [2, "0b1pl0"]

    # test int components

# Generated at 2022-06-13 00:04:28.793894
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    a = Version()
    assert a >= None
    assert not a >= ''
    assert not a >= '1'
    assert not a >= '1.2'
    assert not a >= '2.2'
    assert not a >= '1.2a1'

# Generated at 2022-06-13 00:04:30.382653
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v.__ge__(5) == NotImplemented



# Generated at 2022-06-13 00:04:32.045405
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    obj = Version()
    assert obj.__ge__(obj) == True


# Generated at 2022-06-13 00:04:42.293890
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils import log
    from distutils.tests import support
    from distutils.version import Version, StrictVersion, LooseVersion
    from test.support import run_unittest
    import unittest

    class VersionTestCase(support.EnvironGuard,
      support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

        def test_ge(self):
            a = Version('1.2.3')
            b = Version('1.2.3')
            self.assertTrue(a >= b)
            b = Version('1.2.4')
            self.assertFalse(a >= b)
            b = Version('1.3.3')
            self.assertFalse(a >= b)
            b = Version('2.2.3')
            self.assertFalse(a >= b)


# Generated at 2022-06-13 00:04:46.406287
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.tests import support
    from random import uniform, random, seed
    from re import compile
    from unittest import TestCase, main

    class TestVersion(Version):
        version_re = compile(r"^(\d+) \. (\d+) $", RE_FLAGS)

        def parse(self, vstring):
            match = self.version_re.match(vstring)
            if not match:
                raise ValueError("invalid version number '%s'" % vstring)

            major, minor = match.group(1, 2)
            self.major = int(major)
            self.minor = int(minor)

        def __str__(self):
            return "%d.%d" % (self.major, self.minor)


# Generated at 2022-06-13 00:04:57.858789
# Unit test for method __ge__ of class Version
def test_Version___ge__():
  import base64
  import distutils.version
  import json
  import uuid


# Generated at 2022-06-13 00:05:22.048138
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import sys
    ver = Version('0')
    assert ver >= '0'
    assert ver >= ver



# Generated at 2022-06-13 00:05:23.896894
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version('1.0')
    v2 = Version('1.1')
    assert v1 >= v2

# Generated at 2022-06-13 00:05:36.303138
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # From issue #318 - version number comparison fails for 0.4.4-134
    # https://github.com/ansible/ansible/issues/318
    #
    # Test needed since the issue report relies on a behavior of
    # the stdlib `distutils.version` module which does not exist
    # in the vendored copy used by Ansible.

    a = Version('0.4.4-1')
    b = Version('0.4.4-2')

    assert a < b
    assert a <= b
    assert not a > b
    assert not a >= b

    assert b > a
    assert b >= a
    assert not b < a
    assert not b <= a

    assert a != b
    assert not a == b


# Generated at 2022-06-13 00:05:38.766949
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version("5.5").__ge__(NotImplemented) == NotImplemented

# Generated at 2022-06-13 00:05:48.383349
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():

    def test_given_string_returns_tuple_of_int_and_string_components():
        def given_string_returns_tuple_of_int_and_string_components(vstring):
            instance = LooseVersion(vstring)
            return instance.version

        assert [1, 5, 1] == given_string_returns_tuple_of_int_and_string_components('1.5.1')
        assert [1, 5, 2, 'b', 2] == given_string_returns_tuple_of_int_and_string_components('1.5.2b2')
        assert [161] == given_string_returns_tuple_of_int_and_string_components('161')
        assert [3, 10, 'a'] == given_string_return

# Generated at 2022-06-13 00:05:54.611946
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import _BaseVersion
    from distutils.version import LooseVersion
    assert _BaseVersion.__ge__(_BaseVersion('0.4.2'), _BaseVersion('0.4.2')) is True
    assert _BaseVersion.__ge__(_BaseVersion('0.4.3'), _BaseVersion('0.4.2')) is True
    assert _BaseVersion.__ge__(_BaseVersion('0.4.2'), _BaseVersion('0.4.3')) is False

    assert LooseVersion.__ge__(LooseVersion('1.1'), LooseVersion('1.0.1')) is True
    assert LooseVersion.__ge__(LooseVersion('1.1'), LooseVersion('1.0.1a')) is True

# Generated at 2022-06-13 00:05:56.043605
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v >= v
    assert not v >= Version("1")



# Generated at 2022-06-13 00:05:57.827274
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    a = Version('1.3.0')
    b = Version('1.3.0')
    print(a == b)
    print(a <= b)
    print(a >= b)



# Generated at 2022-06-13 00:06:01.128402
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    for i in range(random.randrange(5)):
        v = Version()
        v1 = v.__ge__(version)

# Generated at 2022-06-13 00:06:06.467597
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    ver = Version("1.2.a")
    oth = Version("2.2.a")
    thr = Version("1.1.a")
    tru = Version("1.2.a")

    assert ver >= tru
    assert not ver >= oth
    assert not ver >= thr
    # assert ver >= "1.2.a"
    # assert not ver >= "2.2.a"
    # assert not ver >= "1.1.a"



# Generated at 2022-06-13 00:06:59.644644
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    print('Test is not implemented')



# Generated at 2022-06-13 00:07:03.490321
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('') >= ''
    assert Version('') >= 'a'
    assert Version('') >= '0.0.1'
    assert Version('') >= '0.0.1a'
    assert Version('') >= '0.0.1a1'
    assert not (Version('0.0.1') >= '')
    assert Version('0.0.1') >= '0.0.1'
    assert Version('0.0.1') >= '0.0.1a'
    assert Version('0.0.1') >= '0.0.1a1'
    assert not (Version('0.0.1a') >= '')
    assert not (Version('0.0.1a') >= '0.0.1')

# Generated at 2022-06-13 00:07:05.829530
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version("1.2") >= Version("1.2")
    assert not (Version("1.2") >= Version("1.3"))


# Generated at 2022-06-13 00:07:14.346467
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # Test if the method generates the correct result
    # when a class instance is compared with another class instance
    version1 = StrictVersion('1.0.0')
    version2 = StrictVersion('2.0.0')
    assert (version1 >= version2) == False
    assert (version2 >= version1) == True

    # Test if the method generates the correct result
    # when a class instance is compared with a string
    assert (version1 >= '1.0.0') == True
    assert (version2 >= '2.0.0') == True
    assert (version1 >= '1.1.0') == False
    assert (version2 >= '2.1.0') == False

    # Test if the method generates the correct result
    # when a string is compared with a class instance

# Generated at 2022-06-13 00:07:24.815857
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    class Version___ge__(unittest.TestCase):
        def test__Version___ge__1(self):
            version = Version()
            version._cmp = lambda *args, **kwargs: NotImplemented
            other = NotImplemented
            self.assertEqual(version.__ge__(other), other)
        def test__Version___ge__2(self):
            version = Version()
            version._cmp = lambda *args, **kwargs: 0
            other = NotImplemented
            self.assertEqual(version.__ge__(other), True)
    unittest.main(exit=False)

# Generated at 2022-06-13 00:07:26.482877
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    with pytest.raises(NotImplementedError):
        Version___ge__()


# Generated at 2022-06-13 00:07:33.311862
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    version_string_1 = Version()
    version_string_2 = '2.6.4'

    # Test with a valid version number
    assert version_string_1 >= version_string_2

    version_string_1 = '2.6.4'
    version_string_2 = '2.7.4'

    # Test with an invalid version number
    assert version_string_1 >= version_string_2

    version_string_1 = '2.6.4'
    version_string_2 = '2.6.4'

    # Test with an invalid version number
    assert version_string_1 >= version_string_2

# Generated at 2022-06-13 00:07:35.509475
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    def _f(): v >= 1
    _f()

# Generated at 2022-06-13 00:07:39.095103
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import unittest
    class Version___ge__TestCase(unittest.TestCase):
        def test_true(self):
            self.assertTrue(Version('0') >= '0')
    unittest.main(argv=[''], verbosity=2, exit=False)


# Generated at 2022-06-13 00:07:40.445772
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    #self = Version()
    assert (1 >= 1)  # True is not NotImplemented