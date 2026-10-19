

# Generated at 2022-06-12 23:59:20.473812
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version("1.0") == "1.0"
    assert Version("1.0") != "2.0"
    assert Version("1.0") < "2.0"
    assert Version("2.0") > "1.0"
    assert Version("1.0") <= "1.0"
    assert Version("1.0") >= "1.0"

# Generated at 2022-06-12 23:59:22.150638
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import types
    v = Version()
    assert type(v.__gt__) == types.MethodType



# Generated at 2022-06-12 23:59:23.949437
# Unit test for method __le__ of class Version
def test_Version___le__():
    # Calling the method
    assert Version("1.0") <= Version("1.0")



# Generated at 2022-06-12 23:59:29.450758
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    try:
        assert StrictVersion('2.7.2').__str__() == '2.7.2'
    except AssertionError as exc:
        raise AssertionError("Expected '2.7.2' but got: %s" % exc.args[0]) from None


# Generated at 2022-06-12 23:59:30.940416
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert not (v == None)

# Generated at 2022-06-12 23:59:32.456316
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    import doctest
    doctest.testmod(verbose=0)

# Generated at 2022-06-12 23:59:39.643823
# Unit test for method parse of class StrictVersion

# Generated at 2022-06-12 23:59:43.389234
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version(vstring = '1.2.3')
    other = Version()
    other.parse('1.2.3')
    assert v <= other

# Generated at 2022-06-12 23:59:44.368670
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    StrictVersion("123")


# Generated at 2022-06-12 23:59:53.187321
# Unit test for method __str__ of class StrictVersion

# Generated at 2022-06-13 00:00:04.267443
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    test_object = Version()
    assert(test_object >= '0')

# Generated at 2022-06-13 00:00:05.869039
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__(1) == NotImplemented


# Generated at 2022-06-13 00:00:09.588255
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('1.0') <= Version('1.0')
    assert Version('1.0') <= Version('1.1')
    assert Version('1.0') <= Version('2.0')
    assert Version('1.0') <= Version('1.0.post1')

# Generated at 2022-06-13 00:00:19.628153
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('1') < Version('2')
    assert Version('1.0') < Version('1.1')
    assert Version('1.0') < Version('1.0.1')

    assert not(Version('1') < Version('1'))
    assert not(Version('1.0') < Version('1.0'))
    assert not(Version('1.0.0') < Version('1.0.0'))
    assert not(Version('1.1') < Version('1.0'))
    assert not(Version('1.0.1') < Version('1.0.0'))
    assert not(Version('1.0.0') < Version('1'))
    assert not(Version('1.0.1') < Version('1.1'))
# /Unit test for method __lt__ of class Version
#

# Generated at 2022-06-13 00:00:28.860255
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # docstring of method __lt__ of class Version
    Test_Version___lt__ = TestCase(
        url='https://docs.python.org/3.7/library/distutils.version.html#distutils.version.LooseVersion.__lt__')
    try:
        import distutils.version
        from distutils.version import LooseVersion
    except ImportError:
        Test_Version___lt__.skipTest('no distutils.version')
    else:
        from distutils.version import LooseVersion

        f = LooseVersion('1.0a1')
        g = LooseVersion('1.0b1')
        h = LooseVersion('1.0c1')
        i = LooseVersion('1.0')
        j = LooseVersion('1.0.4.2')
        # Test for method

# Generated at 2022-06-13 00:00:32.223031
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v2 = Version()
    assert (v1 > v2) == False


# Generated at 2022-06-13 00:00:34.421566
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    assert v1 < v2



# Generated at 2022-06-13 00:00:36.262497
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version('1.1') >= '1.1'

# Generated at 2022-06-13 00:00:44.388061
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from lib2to3.pgen2.token import STRING, NUMBER
    from lib2to3.fixer_util import Leaf, Node
    from lib2to3 import pytree
    from lib2to3.pygram import python_symbols as syms

    class EmptyVersion(Version):
        pass

    class EmptyVersionSub(EmptyVersion):
        pass

    class StrictVersionSub(StrictVersion):
        pass

    class LooseVersionSub(LooseVersion):
        pass

    # Test positive cases
    assert EmptyVersion() == EmptyVersion()
    assert EmptyVersion() == EmptyVersionSub()
    assert EmptyVersionSub() == EmptyVersion()

    assert StrictVersion() == StrictVersion()
    assert StrictVersion() == StrictVersionSub()
    assert StrictVersionSub() == StrictVersion()

    assert LooseVersion

# Generated at 2022-06-13 00:00:52.400422
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    assert StrictVersion("1.0").version == (1, 0, 0)
    assert StrictVersion("1.0a").version == (1, 0, 0) and StrictVersion("1.0a").prerelease == ("a", 0)
    assert StrictVersion("1.0.0").version == (1, 0, 0)
    assert StrictVersion("1").version == (1, 0, 0)
    assert StrictVersion("1.0.0a4").version == (1, 0, 0) and StrictVersion("1.0.0a4").prerelease == ("a", 4)
    assert StrictVersion("1.0.0b3").version == (1, 0, 0) and StrictVersion("1.0.0b3").prerelease == ("b", 3)

# Generated at 2022-06-13 00:01:03.251593
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.2.3')
    assert(v == '1.2.3')
test_Version___eq__()

# Generated at 2022-06-13 00:01:09.578931
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version(vstring='1.0') >= '1.0'
    assert Version(vstring='1.0') >= '0.9'
    assert Version(vstring='1.0') >= '1.0a'
    assert Version(vstring='1.0') >= '1.0.1'
    assert not (Version(vstring='1.0') >= '1.0.0.0.0.1')
    assert not (Version(vstring='1.0') >= '2.0')



# Generated at 2022-06-13 00:01:11.764299
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    r = Version()
    r.parse("1.2")
    s = Version()
    s.parse("1.2")
    Assert( r < s == False )

# Generated at 2022-06-13 00:01:14.498825
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version('1.2')
    v2 = Version('1.2')
    assert (v1 == v2)
    assert (not v1 > v2)
    assert (v1 >= v2)
    assert (not v1 < v2)
    assert (v1 <= v2)

# Generated at 2022-06-13 00:01:15.029149
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert True



# Generated at 2022-06-13 00:01:23.484056
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.tests import support
    from distutils.version import StrictVersion
    eq_(Version('1.5.1').__le__(Version('1.5.2dev')), True)
    eq_(Version('1.5.1').__le__('1.5.2dev'), True)
    eq_(Version('1.5.1a1').__le__(Version('1.5.1.post1')), False)
    eq_(Version('1.5.1a1').__le__('1.5.1.post1'), False)
    eq_(Version('1.5.1.post1').__le__('1.5.1a1'), True)



# Generated at 2022-06-13 00:01:33.842174
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    v.parse('1.0')
    assert v >= '1.0'
    assert v >= '0.9'
    assert v >= '0.99'
    assert v >= '0.999'
    assert v >= '1.0.dev'
    assert v >= '1.0.a'
    assert v >= '1.0.b'
    assert v >= '1.0.1'
    assert v >= '1.0.2'
    assert v >= '1.0.alpha'
    assert v >= '1.0.beta'
    assert v >= '1.0.dev0'
    assert v >= '1.0.dev1'
    assert not v >= '0.6.1'
    assert not v >= '1.1'

# Generated at 2022-06-13 00:01:35.899663
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version("1.0")
    assert v <= "1.1"
    assert not (v <= "0.9")
    assert v <= "1.0"
    assert not (v <= "1.0.post1")



# Generated at 2022-06-13 00:01:37.744754
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    a = Version('1')
    b = Version('1.0')
    assert a >= b
    assert a == b
    assert not (a > b)


# Generated at 2022-06-13 00:01:42.782499
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    print("Testing __ge__")
    import types
    v = Version("1.2.3.4")
    if type(v.__ge__("1.2.3.4")) == types.BooleanType:
        print("__ge__ returned a boolean value as expected")
    elif type(v.__ge__("1.2.3.4")) == int:
        print("__ge__ returned an int value", v.__ge__("1.2.3.4"))
    else:
        print("__ge__ returned some weird type:", type(v.__ge__("1.2.3.4")))


# Generated at 2022-06-13 00:01:51.360168
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('1.0')
    assert v >= '1.0'

# Generated at 2022-06-13 00:01:56.782869
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    import unittest
    # Test version comparison
    versionpattern = re.compile(r'(\d+ | [a-z]+ | \.)', re.VERBOSE)

    def cmp(a, b):
        return (a > b) - (a < b)

    def splitUp(v):
        return versionpattern.split(v)

    def com(a,b):
        return cmp(parse(a), parse(b))


# Generated at 2022-06-13 00:02:05.022115
# Unit test for method __ge__ of class Version

# Generated at 2022-06-13 00:02:08.885380
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import doctest, version

    doctest.testmod(version, report=0)

# Generated at 2022-06-13 00:02:12.055981
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version("1.1.1")
    assert v <= "1.1.1"
    assert v <= "1.1.2"
    assert not v <= "1.1.0"

# Generated at 2022-06-13 00:02:16.769978
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest

    class Version_TestCase(unittest.TestCase):
        def test(self):
            # TODO: write tests for __gt__
            assert True

    unittest.main()


# Generated at 2022-06-13 00:02:29.840084
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assertVersionEqual(Version(), Version())
    assertVersionNotEqual(Version(), Version('1.0'))

    v1 = Version('1.0')
    assertVersionEqual(v1, v1)
    assertVersionEqual(v1, Version('1.0'))
    assertVersionNotEqual(v1, Version('1.1'))

    v1 = Version('1.1')
    assertVersionEqual(v1, v1)
    assertVersionEqual(v1, Version('1.1'))
    assertVersionNotEqual(v1, Version('1.0'))

    v1 = Version('0.9.9')
    assertVersionEqual(v1, v1)
    assertVersionEqual(v1, Version('0.9.9'))

# Generated at 2022-06-13 00:02:34.418853
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    
    # Create an instance of Version
    version = Version('0.0')

    # Call method __lt__ with arguments
    # version._cmp(other)
    try:
        version._cmp(other)
    except NameError:
        pass    

# Generated at 2022-06-13 00:02:37.282989
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.2.3.a1')
    v2 = Version('1.2.3.b1')
    assert (v1 < v2) == True


# Generated at 2022-06-13 00:02:45.915480
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    def p(s):
        s = LooseVersion(s)
        return tuple(s.version)
    assert p('3.10a') == (3, 10, 'a')
    assert p('8.02') == (8, 2)
    assert p('3.4j') == (3, 4, 'j')
    assert p('1996.07.12') == (1996, 7, 12)
    assert p('3.2.pl0') == (3, 2, 'pl', 0)
    assert p('3.1.1.6') == (3, 1, 1, 6)
    assert p('2g6') == (2, 'g', 6)
    assert p('11g') == (11, 'g')
    assert p('0.960923') == (0, 960923)
    assert p

# Generated at 2022-06-13 00:03:04.144444
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest

    class VersionTest(unittest.TestCase):
        def test___gt__(self):
            v = Version()
            self.assertFalse(v.__gt__(Version()))

    unittest.main()



# Generated at 2022-06-13 00:03:05.857531
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('2.2.1')
    assert(v >= '2.2.1')


# Generated at 2022-06-13 00:03:07.506348
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    v._cmp = lambda x: 1
    assert v > 'a' == True


# Generated at 2022-06-13 00:03:11.916262
# Unit test for method __le__ of class Version
def test_Version___le__():
    a = Version('1.0.0')
    b = Version('1.0.0')
    c = Version('1.0.1')
    d = Version('2.0.0')
    assert a <= b
    assert a <= c
    assert a < c
    assert a <= d
    assert a < d


# Generated at 2022-06-13 00:03:17.830417
# Unit test for method __le__ of class Version
def test_Version___le__():
    import types
    v1 = Version('11.12')
    v2 = Version('11.12')
    v3 = Version('11.13')
    v4 = '1.2'
    assert v1 <= v2
    assert not (v1 <= v3)
    assert v2 <= v3
    try:
        v1 <= v4
    except TypeError:
        pass
    else:
        assert False, 'exception not raised'


# Generated at 2022-06-13 00:03:28.523563
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import unittest
    class Stub(Version):
        def __init__(self, x=1):
            self._cmp = lambda o: o._cmp(0)
            super(Stub,self).__init__()
        def __repr__(self):
            return "Stub"

    class Stub2(Stub):
        def __init__(self):
            self._cmp = lambda o: o._cmp(1)
            super(Stub2, self).__init__()
        def __repr__(self):
            return "Stub2"

    class StubException(Stub):
        def __init__(self):
            self._cmp = lambda o: NotImplemented
            super(StubException, self).__init__()
        def __repr__(self):
            return "StubException"



# Generated at 2022-06-13 00:03:33.646977
# Unit test for method __le__ of class Version
def test_Version___le__():
    e = Version()
    try:
        e.__le__("asd")
        assert False, "Should have failed"
    except NotImplementedError:
        assert True
    except:
        assert False, "Should have failed with NotImplementedError"
    e.parse("asd")
    assert not e.__le__("asd")
    assert e.__le__("bac")
    assert e.__le__("bac")
    assert e.__le__("bac1")
    assert e.__le__("bac1.5")
    assert not e.__le__("b1")
    assert not e.__le__("b1.5")



# Generated at 2022-06-13 00:03:36.850185
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    v2 = Version()
    v1.parse(v2)
    assert v1 == v2

# Generated at 2022-06-13 00:03:39.131697
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    version = Version()
    version._cmp = lambda x: 1
    assert version == 1


# Generated at 2022-06-13 00:03:47.407239
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion('0.4').__str__() == '0.4'
    assert StrictVersion('0.4.0').__str__() == '0.4.0'
    assert StrictVersion('0.4.1').__str__() == '0.4.1'
    assert StrictVersion('0.5a1').__str__() == '0.5a1'
    assert StrictVersion('0.5b3').__str__() == '0.5b3'
    assert StrictVersion('0.5').__str__() == '0.5'
    assert StrictVersion('0.9.6').__str__() == '0.9.6'
    assert StrictVersion('1.0').__str__() == '1.0'

# Generated at 2022-06-13 00:04:09.253368
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from test.support import import_module
    distutils = import_module('distutils')
    distutils.version = import_module('distutils.version')
    distutils.version.StrictVersion = import_module('distutils.version').StrictVersion
    v = distutils.version.StrictVersion("1.2.3a0")
    assert (v == v)
    assert (v == "1.2.3a0")
    assert (v != "1.2.3c1")

# Generated at 2022-06-13 00:04:10.703226
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert_raises(NotImplementedError, Version().__le__, None)





# Generated at 2022-06-13 00:04:12.697195
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version('1') > Version('0')

# Generated at 2022-06-13 00:04:14.408875
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version() == Version()


# Generated at 2022-06-13 00:04:16.084647
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    obj = Version(None)
    assert obj == 1

# Generated at 2022-06-13 00:04:17.595636
# Unit test for method __le__ of class Version
def test_Version___le__():
    Version.__le__(Version(), None)

# Generated at 2022-06-13 00:04:22.894097
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    ver1 = Version(vstring='0')
    ver2 = Version(vstring='1')
    assert ver1 == Version(vstring='0')
    assert ver1 != Version(vstring='1')
    assert str(ver1) == '0'
    assert str(ver2) == '1'
    assert str(ver2) != str(ver1)
    assert ver1 == ver1
    assert ver1 != ver2


# Generated at 2022-06-13 00:04:33.141634
# Unit test for method __le__ of class Version
def test_Version___le__():
    for x,y,expected in [
        ('2.5.3', '2.5.3', True),
        ('2.5.3', '2.5b1', True),
        ('2.5.3', '2.5', True),
        ('2.5.3', '2.5a1', True),
        ('2.5.3', '2.4.1', False),
        ('2.5.3', '2.5.3a1', False),
        ('2.5.3', '2.5.3b1', False),
        ]:
        v1 = StrictVersion(x)
        v2 = StrictVersion(y)
        assert bool(v1 <= v2) == expected
test_Version___le__()



# Generated at 2022-06-13 00:04:43.175524
# Unit test for method __le__ of class Version
def test_Version___le__():
    import pytest

    # Test a number of interesting values for version.

# Generated at 2022-06-13 00:04:44.902603
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('0.1.1') <= Version('0.1.1')



# Generated at 2022-06-13 00:05:23.860597
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    """
    # Check basic behavior of class Version
    # Tests for method of class Version: __gt__
    """

    def test_Version___gt__():
        assert Version(
            '1.2.3') > Version('1.2.1'), 'Version 1.2.3 > 1.2.1'
        assert Version(
            '1.3') > Version('1.2'), 'Version 1.3 > 1.2'
        assert Version(
            '2.0') > Version('1.2.3'), 'Version 2.0 > 1.2.3'
        assert Version(
            '2.1.1') > Version('2'), 'Version 2.1.1 > 2'
        assert Version(
            '1.0.a') > Version('1.0'), 'Version 1.0.a > 1.0'


# Generated at 2022-06-13 00:05:24.645553
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version() <= Version()


# Generated at 2022-06-13 00:05:29.088492
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.2.3')
    v2 = Version('1.3.3')
    assert (v1 < v2) == True


# Generated at 2022-06-13 00:05:35.685363
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('0.4.0')
    assert v >= '0.4.0'
    assert v >= '0.4.0.dev0'
    assert v >= Version('0.4.0')
    assert v >= Version('0.4.0.dev0')
    assert not v >= '0.4.1'
    assert not v >= Version('0.4.1')



# Generated at 2022-06-13 00:05:39.450442
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    assert (v1 < v2) == False
    assert (v2 < v1) == False



# Generated at 2022-06-13 00:05:41.932368
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version('1.0')
    assert v1 >= '1.0', "v1 >= '1.0'"


# Generated at 2022-06-13 00:05:42.539560
# Unit test for method __le__ of class Version
def test_Version___le__():
    pass

# Generated at 2022-06-13 00:05:44.643065
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.1')
    v2 = Version('1.2')
    assert v1 < v2

# Generated at 2022-06-13 00:05:48.821044
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    """
    # 1
    >>> v1 = Version('1.0')
    >>> v2 = Version('1.1')
    >>> v1 == v2
    False
    # 2
    >>> v1 = Version('1.1')
    >>> v2 = Version('1.1')
    >>> v1 == v2
    True
    """

# Generated at 2022-06-13 00:05:53.201580
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version,StrictVersion,LooseVersion

    v1 = Version('1.1')
    v2 = Version('1.2')

    assert v1.__gt__(v2) == False, "v1.__gt__(v2) is not False"


# Generated at 2022-06-13 00:07:02.077367
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    # Uncomment the following line to use the pregenerated results
    # return _test_Version___gt__.results_gen
    #
    # Note: The following line raises an exception if the
    #       pregenerated results file is not present
    _test_Version___gt__.results_gen = np.load(_testcf)

    v1 = Version()
    v2 = Version()
    return v1 > v2

_test_Version___gt__.results_gen = np.load(_testcf)



# Generated at 2022-06-13 00:07:04.974645
# Unit test for method __le__ of class Version
def test_Version___le__():
    Version_instance = Version()
    # calling __le__ method wth an instance argument
    try:
        Version_instance.__le__()
    except TypeError:
        pass


# Generated at 2022-06-13 00:07:13.465796
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import distutils.version

    v = distutils.version.LooseVersion("1.3.3")
    assert (v > "1.3.2")
    assert not (v > "1.3.3")
    assert not (v > "1.3.4")
    assert not (v > "1.4")

    v = distutils.version.LooseVersion("1.24")
    assert (v > "1.3.4")
    assert not (v > "1.24")
    assert not (v > "1.3a4")
    assert not (v > "2.0")

    v = distutils.version.LooseVersion("1.3.4~rc2")
    assert not (v > "1.3.4~rc1")
    assert not (v > "1.3.4")

# Generated at 2022-06-13 00:07:21.647693
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest
    class Version___gt__ (unittest.TestCase):
        def test_Version___gt__(self):
            import distutils.version as version
            v1 = version.StrictVersion('1.0')
            v2 = version.StrictVersion('1.0.0')
            self.assertEqual(v2>v1, False)
            self.assertEqual(v1>v2, False)
            self.assertEqual(v1>v1, False)
    unittest.main()


# Generated at 2022-06-13 00:07:30.910789
# Unit test for method __gt__ of class Version

# Generated at 2022-06-13 00:07:31.935010
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    """Test method __ge__ of class Version"""



# Generated at 2022-06-13 00:07:33.417583
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    assert v1.__eq__(v1)


# Generated at 2022-06-13 00:07:36.710046
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    assert 1 < v1

    v2 = Version('1.2.3')
    assert 3 > v1 and 3 >= v2 and 3 > v2


# Generated at 2022-06-13 00:07:38.605971
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('1.0') < Version('1.1')
    assert not Version('1.0') < Version('1.0')

# Generated at 2022-06-13 00:07:42.930223
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v_obj = Version()
    v_obj2 = Version()

    # Version == Version
    try:
        v_obj == v_obj
    except NotImplementedError as e:
        raise AssertionError(str(e))

    # Version != int
    try:
        v_obj == 1
        assert False, "unexpected success"
    except NotImplementedError as e:
        pass

    # Version == Version
    assert (v_obj == v_obj2) is False


# Generated at 2022-06-13 00:09:00.482744
# Unit test for method __le__ of class Version
def test_Version___le__():
    x = Version()
    assert x.__le__(x) is True
    assert x.__le__(None) is NotImplemented


# Generated at 2022-06-13 00:09:01.806589
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    o = Version()
    o2 = Version()
    assert o == o
    assert o == o2

# Generated at 2022-06-13 00:09:02.754829
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version() == ''

# Generated at 2022-06-13 00:09:07.785500
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from . import util
    from . import expect

    # Test with int
    v = Version("1.3.3")
    expect.equal(v.__eq__(1), False)

    # Test with str
    v = Version("1.3.3")
    expect.equal(v.__eq__("1.3.3"), True)

    # Test with object
    v = Version("1.3.3")
    o = Version("1.3.3")
    expect.equal(v.__eq__(o), True)
