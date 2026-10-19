

# Generated at 2022-06-12 23:59:16.509804
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert (Version('2.0') >= '2.0' )

# Generated at 2022-06-12 23:59:19.640205
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # Version.__gt__: NotImplemented => NotImplemented
    try:
        Version.__gt__(Version, "str")
    except NotImplementedError:
        pass

# Generated at 2022-06-12 23:59:22.018544
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = StrictVersion('1.2')
    v2 = StrictVersion('1.2')
    assert version.Version.__ge__(v1, v2)

# Generated at 2022-06-12 23:59:23.855878
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # Version
    v = Version()
    v1 = Version()
    v2 = Version()

# Generated at 2022-06-12 23:59:31.233660
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion('0.5').__str__() == '0.5'
    assert StrictVersion('1.0').__str__() == '1.0'
    assert StrictVersion('1.0.4a3').__str__() == '1.0.4a3'
    assert StrictVersion('1.0.4b1').__str__() == '1.0.4b1'
    assert StrictVersion('1.0.4').__str__() == '1.0.4'

test_StrictVersion___str__()



# Generated at 2022-06-12 23:59:39.169042
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1, v2 = Version("1.2.1"), Version("1.2")
    assert v1._cmp(v2) == 1
    assert (v1 < v2) == False
    assert (v1 <= v2) == False
    assert (v1 == v2) == False
    assert (v1 != v2) == True
    assert (v1 > v2) == True
    assert (v1 >= v2) == True
    v1, v2 = Version("1.2"), Version("1.2")
    assert v1._cmp(v2) == 0
    assert (v1 < v2) == False
    assert (v1 <= v2) == True
    assert (v1 == v2) == True
    assert (v1 != v2) == False
    assert (v1 > v2) == False

# Generated at 2022-06-12 23:59:42.077425
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    v = StrictVersion('2')
    assert v.__str__() == '2'


# Generated at 2022-06-12 23:59:47.907098
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    v_str = StrictVersion('0.5a1').__str__()
    assert v_str == '0.5a1'
    v_str = StrictVersion('0.4').__str__()
    assert v_str == '0.4'
    v_str = StrictVersion('1.0.4').__str__()
    assert v_str == '1.0.4'
    return


# Generated at 2022-06-12 23:59:49.791013
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v == v, "Version.__eq__(): self-comparison failed"


# Generated at 2022-06-12 23:59:51.270722
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version('1.0.0')
    assert v <= '1.0.0'



# Generated at 2022-06-13 00:00:01.242768
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # This method is tested in StrictVersion, LooseVersion and LegacyVersion
    pass # Unit test for method __gt__ of class Version

# Generated at 2022-06-13 00:00:06.154741
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    """
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    SEE UNIT TESTS AT END OF FILE
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    """


# Generated at 2022-06-13 00:00:10.633379
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    f_v = Version
    f_vi = f_v.__init__
    f_v.__init__ = lambda self, vstring=None: f_vi(self, "1.2.a0")
    if f_v() == "1.2.a0":
        return True
    return False


# Generated at 2022-06-13 00:00:15.465579
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from .Version import Version

    v1 = Version('v0.1.1a1')
    v2 = Version('v0.2b2')
    assert v1.__gt__(v1) == False, '__gt__ method failed!'
    assert v1.__gt__(v2) == False, '__gt__ method failed!'



# Generated at 2022-06-13 00:00:23.740519
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest
    from ansible.module_utils.six import u
    from ansible.module_utils.common._collections_compat import OrderedDict

    class TestVersion(unittest.TestCase):
        def test___gt__(self):
            self.assertTrue(StrictVersion('1.1') > StrictVersion('1.0'))
            self.assertFalse(StrictVersion('1.1') > StrictVersion('1.1'))
            self.assertFalse(StrictVersion('1.1') > StrictVersion('1.2'))

            self.assertTrue(LooseVersion('1.1') > LooseVersion('1.0'))
            self.assertFalse(LooseVersion('1.1') > LooseVersion('1.1'))

# Generated at 2022-06-13 00:00:24.503885
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    assert v.__ge__(v) is NotImplemented


# Generated at 2022-06-13 00:00:27.067775
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    ver = Version()
    sn = '1.1.1'
    n = ver._cmp(sn)
    try:
        n > 0
    except Exception:
        assert False

# Generated at 2022-06-13 00:00:27.928035
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    pass # tested in test_version



# Generated at 2022-06-13 00:00:29.534952
# Unit test for method __eq__ of class Version
def test_Version___eq__():

    from distutils.version import Version

    v = Version("1.0a")
    assert v == "1.0a"

# Generated at 2022-06-13 00:00:32.072357
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version("1.2") <= "1.2"

# Generated at 2022-06-13 00:00:39.882608
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version(1) <= Version(2)


# Generated at 2022-06-13 00:00:46.126750
# Unit test for method __le__ of class Version
def test_Version___le__():
    class TestVersion(Version):
        def parse(self, string):
            pass
        def _cmp(self, other):
            return 0

    version = TestVersion()

    # The only case that returns NotImplemented is if the class
    # of other is not TestVersion.
    other = TestVersion()
    result = version.__le__(other)
    assert result is True

    other = Version()
    result = version.__le__(other)
    assert result is NotImplemented

    # Everything else returns True or False
    other = "1.0.dev"
    result = version.__le__(other)
    assert result is True

    other = (1,)
    result = version.__le__(other)
    assert result is True

# Generated at 2022-06-13 00:00:47.684134
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('1.0') >= '1.0'

# Generated at 2022-06-13 00:00:50.436156
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    """test_Version___ge__"""
    v1 = Version("1.0")
    v2 = Version("1.0")
    return v1 >= v2

# Generated at 2022-06-13 00:00:53.961075
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version("1.1")

    assert v1 == Version("1.1")

    assert not v1 == Version("1.2")

# Generated at 2022-06-13 00:00:56.910362
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version()
    v2 = Version()
    v1._cmp = lambda x: 0
    v2._cmp = lambda x: 0
    assert (v1 >= v2)



# Generated at 2022-06-13 00:01:04.102377
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('1.2.3')
    assert v >= v == True
    assert v >= Version('1.2.3') == True
    assert v >= '1.2.3' == True
    assert v >= '1.2.4' == False
    assert v >= '1.2.4b4' == False
    assert v >= '1.2.4b4' == False
    assert v >= '1.2.4a3' == True
    assert v >= '1.2.3+2' == True
    assert v >= '1.2.3.post42' == True
    assert v >= '1.2.3.dev42' == False
    assert v >= '1.2.3.dev1' == True
    assert v >= '1.2.3.dev' == False



# Generated at 2022-06-13 00:01:13.484009
# Unit test for method __le__ of class Version
def test_Version___le__():
    # Test positional args
    v = Version("1.2.3")
    assert v <= "1.4.3"
    assert v <= "1.2.6"
    assert v <= "1.2.3"
    assert not v <= "1.2.2"
    assert not v <= "1.1.3"
    assert not v <= "0.2.3"
    # Test keyword args
    v = Version("1.2.3")

# Generated at 2022-06-13 00:01:14.283493
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    return True

# Generated at 2022-06-13 00:01:15.313096
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Create an instance of class Version
    my_instance = Version()
    

# Generated at 2022-06-13 00:01:33.726848
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import StrictVersion, LooseVersion
    assert not (StrictVersion('1') >= 1), 'not (StrictVersion(\'1\') >= 1)'
    assert not (StrictVersion('1') >= 1.0), 'not (StrictVersion(\'1\') >= 1.0)'
    assert not (StrictVersion('1') >= '1'), 'not (StrictVersion(\'1\') >= \'1\')'
    assert not (StrictVersion('1') >= '1.0'), 'not (StrictVersion(\'1\') >= \'1.0\')'
    assert not (StrictVersion('1') >= StrictVersion('1.0')), 'not (StrictVersion(\'1\') >= StrictVersion(\'1.0\'))'

# Generated at 2022-06-13 00:01:39.358167
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('1.2.3')
    assert not v.__ge__(None)
    assert v.__ge__('1.2.3')
    assert v.__ge__('1.2.2')
    assert not v.__ge__('1.2.4')
    assert not v.__ge__(Version('1.2'))
    assert not v.__ge__('1.2')
    assert v.__ge__(Version('1.2.3'))
    assert v.__ge__(Version('1.2.2'))
    assert not v.__ge__(Version('1.2.4'))
    assert not v.__ge__(Version('1.2'))
    assert v.__ge__(LooseVersion('1.2.3'))
    assert v.__ge

# Generated at 2022-06-13 00:01:39.978305
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version("1") >= Version("1")



# Generated at 2022-06-13 00:01:49.541472
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import Version
    v = Version()
    try:
        v >= '1'
        assert 0, 'method __ge__ of class Version should have raised ValueError'
    except ValueError:
        pass
    v._version = (1,)
    try:
        v >= '2'
        assert 0, 'method __ge__ of class Version should have raised ValueError'
    except ValueError:
        pass
    v._version = (2,)
    try:
        v >= '1'
        assert 0, 'method __ge__ of class Version should have raised ValueError'
    except ValueError:
        pass
    v = Version('3')
    v._version = (1,)

# Generated at 2022-06-13 00:01:54.182797
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert not Version('1.2.3').__le__('1.2.2')
    assert Version('1.2.3').__le__('1.2.3')
    assert Version('1.2.3').__le__('1.2.4')
    assert Version('1.2.3').__le__(Version('1.2.2'))
    assert Version('1.2.3').__le__(Version('1.2.3'))
    assert Version('1.2.3').__le__(Version('1.2.4'))

# Generated at 2022-06-13 00:01:56.945686
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # caller: Version.__ge__
    # called: Version._cmp

    # caller: Version.__ge__
    # called: Version._cmp
    pass


# Generated at 2022-06-13 00:01:58.254883
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version(1) == Version(1)

# Generated at 2022-06-13 00:02:01.656489
# Unit test for method __le__ of class Version
def test_Version___le__():
    version = Version("2.2")
    version2 = Version("2.2")
    try:
        assert version <= version2
    except:
        raise AssertionError("Version class `__le__` method does not return the correct version")
test_Version___le__()

# Generated at 2022-06-13 00:02:07.535945
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('1.0') <= '1.0'
    assert not (Version('1.0') <= '0.5')
    assert Version('1.0') <= '1.0'
    assert not (Version('1.0') <= '1.1')
    assert Version('1.0.0') <= '1.0'
    assert not (Version('1.0.1') <= '1.0')
    assert Version('1.0.0') <= '1.0.0'
    assert not (Version('1.0.1') <= '1.0.0')
    assert Version('1.0.0') <= '1.0.0.0'
    assert not (Version('1.0.1') <= '1.0.0.0')

# Generated at 2022-06-13 00:02:09.554075
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from . import distutils2
    from . import distutils2_tests
    from distutils2 import dist
    from distutils2.tests import support
    from distutils2_tests import support
    v1 = dist.LooseVersion('1.2a2')
    v2 = dist.LooseVersion('1.2a2')
    assert v1 >= v2


# Generated at 2022-06-13 00:02:30.169830
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version("1.1a").__le__("1.1a") == True
    assert Version("1.1a").__le__("1.1b") == True
    assert Version("1.1a").__le__("1.2") == True
    assert Version("1.1a").__le__("1.2a") == True
    assert Version("1.1b").__le__("1.1a") == False
    assert Version("1.1b").__le__("1.1b") == True
    assert Version("1.1b").__le__("1.2") == True
    assert Version("1.1b").__le__("1.2a") == True
    assert Version("1.2").__le__("1.1a") == False

# Generated at 2022-06-13 00:02:33.747590
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version('')
    assert str(v) == ''
    assert repr(v) == "Version ('None')"
    assert v == 'None'
    assert v <= 'abc'


# Generated at 2022-06-13 00:02:34.701362
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    pass


# Generated at 2022-06-13 00:02:36.852343
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils2.version import Version
    v = Version()
    assert v == None
    return # __le__


# Generated at 2022-06-13 00:02:38.126360
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('1.0') <= Version('1.1')


# Generated at 2022-06-13 00:02:42.008393
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    test_cases = (
        (
            Version('1.0'),
            1,
        ),
        (
            Version('1.1'),
            0,
        ),
    )
    for arg, val in test_cases:
        assert val == arg.__eq__(val)


# Generated at 2022-06-13 00:02:50.296301
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Test method __le__ of class Version"""

    # Initialise with optional argument
    v = Version('1.2')
    assert v.__repr__() == "Version ('1.2')"
    assert str(v) == '1.2'

    # Initialise without optional argument
    v = Version()
    assert v.__repr__() == "Version ('')"
    assert str(v) == ''




# Generated at 2022-06-13 00:02:53.611770
# Unit test for method __le__ of class Version
def test_Version___le__():
    version = Version("0.0.1")
    other = Version("0.0.1")
    assert version <= other

# Generated at 2022-06-13 00:02:56.703040
# Unit test for method __le__ of class Version

# Generated at 2022-06-13 00:02:58.186415
# Unit test for method __le__ of class Version
def test_Version___le__():
    a = Version()
    b = Version()
    assert a <= b


# Generated at 2022-06-13 00:03:32.548689
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import sys
    import lib_version
    v = lib_version.Version('abcdef')
    w = lib_version.Version('abcdef')
    x = lib_version.Version('abcdef')
    x.parse('123.456')
    y = lib_version.StrictVersion('1.1.1')
    z = lib_version.LooseVersion('1.1.1')
    assert not v == 'abcdef'
    assert v == w
    assert not v == x
    assert y == z
    assert not z == 'abcdef'



# Generated at 2022-06-13 00:03:33.209368
# Unit test for method __ge__ of class Version
def test_Version___ge__(): return True



# Generated at 2022-06-13 00:03:36.717057
# Unit test for method __eq__ of class Version
def test_Version___eq__():
  from distutils.version import Version
  assert Version('0').__eq__(Version('0')) == True

test_Version___eq__()

# Generated at 2022-06-13 00:03:39.930200
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.2.3')
    assert v == '1.2.3'
    assert v != '1.2.4'

# Generated at 2022-06-13 00:03:41.476526
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    version = Version(vstring='1.0')
    assert version == '1.2'



# Generated at 2022-06-13 00:03:46.674918
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()

# Generated at 2022-06-13 00:03:52.496236
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import StrictVersion
    from distutils.tests import support


# Generated at 2022-06-13 00:03:54.061532
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    x = Version()
    y = Version()
    assert (x == y) == False


# Generated at 2022-06-13 00:03:58.031132
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1.0').__eq__('1.0') == 0
    assert Version('1.0a').__eq__('1.0a') == 0
    assert Version('1.0').__eq__('2.0') == -1
    assert Version('1.0').__eq__('0.9') == 1


# Generated at 2022-06-13 00:04:02.086416
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.0')
    v2 = Version('1.0')
    v3 = Version('1.1')
    assert(v1 == v2)
    assert(v1 != v3)

# Generated at 2022-06-13 00:04:35.579339
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import pytest
    class TestVersion(Version):
        def _cmp(self, other):
            return 0
    assert TestVersion().__eq__(TestVersion())
    assert not TestVersion().__eq__(None)
    with pytest.raises(TypeError):
        TestVersion().__eq__(123)

# Generated at 2022-06-13 00:04:40.961017
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    v1 = Version()
    v2 = Version()

    assert(v >= v1 == 0)
    assert(v >= v2 == 0)
    assert(v1 >= v == 0)
    assert(v1 >= v2 == 0)
    assert(v2 >= v == 0)
    assert(v2 >= v1 == 0)



# Generated at 2022-06-13 00:04:44.570182
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    """Unit test for Version.__eq__
    """
    v1 = Version('1.0')
    assert v1.__eq__(Version('1.0'))
    assert not v1.__eq__(Version('2.0'))

# Generated at 2022-06-13 00:04:55.328885
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    for cls in [StrictVersion, LooseVersion]:
        assert cls('3.0') >= cls('3.0')
        assert not cls('3.0') >= cls('3.1')
        assert cls('3.1') >= cls('3.0')
        assert cls('3.0.0') >= cls('3.0')
        assert cls('3.0') >= cls('3.0.0')
        assert cls('3.1.2.2') >= cls('3.1.2.2')
        assert not cls('3.1.2.2') >= cls('3.1.2.3')
        assert cls('3.1.2.3') >= cls('3.1.2.2')

# Generated at 2022-06-13 00:04:59.952188
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    global v2_7_8
    global v2_7_8_1
    v2_7_8 = Version("2.7.8")
    v2_7_8_1 = Version("2.7.8-1")
    assert v2_7_8 == v2_7_8_1
test_Version___eq__()


# Generated at 2022-06-13 00:05:05.305961
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    for i in range(200):
        v = Version("1.0")
        assert v >= Version("1.0")
    for i in range(200):
        v = Version("1.0")
        assert v >= "1.0"
    for i in range(200):
        v = Version("1.0")
        assert v >= 1.0

# Generated at 2022-06-13 00:05:08.899538
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from ansible.release import __version__
    from distutils.version import LooseVersion, StrictVersion
    cver = StrictVersion(__version__)
    lver = LooseVersion(__version__)
    assert cver.__eq__(cver) == True
    #assert cver.__eq__(lver) == True




# Generated at 2022-06-13 00:05:15.587427
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.1.1')
    v2 = Version('1.1.1')

    assert (v1 == v2) ==  True

    v1 = Version('1.1.1')
    v2 = Version('1.1.2')

    assert (v1 == v2) == False

    v1 = Version('1.1.1')
    v2 = Version('1.1.1.0')

    assert (v1 == v2) == True

# Generated at 2022-06-13 00:05:18.884995
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1')
    assert v == '1'
    assert v != '2'

# Generated at 2022-06-13 00:05:26.951743
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from ansible.module_utils.six import PY3
    from ansible.module_utils._text import to_bytes, to_text
    from ansible.module_utils.common.version import Version
    from io import BytesIO

    def _compare(a, b):
        v = Version(a)
        v2 = Version(b)
        eq = v == v2
        return eq

    v1 = Version("1.1")
    v2 = Version("1.2")
    if not _compare(v1, v1):
        return False
    if v1 == v2:
        return False
    if v2 == v1:
        return False
    if not _compare(v2, v2):
        return False


# Generated at 2022-06-13 00:07:39.654484
# Unit test for method parse of class LooseVersion

# Generated at 2022-06-13 00:07:40.411419
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()

# Generated at 2022-06-13 00:07:44.144323
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version().__eq__('2.0') == False

# Generated at 2022-06-13 00:07:47.231591
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert (Version('1.2') == Version('1.2'))
assert not (Version('1.2') == Version('1.1'))
assert not (Version('1.2') == '1.2')


# Generated at 2022-06-13 00:07:49.654768
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.2b')
    v2 = Version('1.2')
    assert v1 != v2
    assert v1 == v1
    assert v2 == v2



# Generated at 2022-06-13 00:07:52.371390
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version("1.1.1")
    v2 = Version("1.1.1")
    assert v1.__eq__(v2) == True
    assert v2.__eq__(v1) == True


# Generated at 2022-06-13 00:07:53.900900
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    assert not v1.__eq__(None)


# Generated at 2022-06-13 00:07:55.491285
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1.2').__eq__(Version('1.2')) == True

# Generated at 2022-06-13 00:07:58.245994
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version
    v=Version()
    v.parse('1')

    exc_detected = False
    try:
        v == '2'
    except Exception as exc:
        exc_detected = True
    assert exc_detected # because _cmp('') raises a ValueError

# Generated at 2022-06-13 00:08:06.079799
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    import unittest
    class Test(unittest.TestCase):
        def test_parse(self):
            for base in (LooseVersion, StrictVersion):
                v = base('1.0')
                self.assertEqual(v.version, (1,0))
                v = base('1.2.3')
                self.assertEqual(v.version, (1,2,3))
                v = base('1.2.3.4')
                self.assertEqual(v.version, (1,2,3,4))
                v = base('1.2.0')
                self.assertEqual(v.version, (1,2,0))
                v = base('1.2pl3')
                self.assertEqual(v.version, (1,2,'pl',3))
               