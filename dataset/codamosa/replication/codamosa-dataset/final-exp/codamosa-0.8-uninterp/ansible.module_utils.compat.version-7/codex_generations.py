

# Generated at 2022-06-12 23:59:17.113623
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version("0.0.0")
    assert v == "0.0.0"

# Generated at 2022-06-12 23:59:18.117376
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version() <= 1 is NotImplemented



# Generated at 2022-06-12 23:59:20.196528
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.2.3.4')
    v2 = Version('1.2.3.4')
    v3 = Version('1.2.3.5')
    assert v1 == v2
    assert not v1 == v3

# Generated at 2022-06-12 23:59:30.104766
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    for version in (
        (0, 4),
        (0, 4, 0),
        (0, 4, 1),
        (0, 5, 0, ('a', 1)),
        (0, 5, 0, ('b', 3)),
        (0, 9, 6),
        (1, 0),
        (1, 0, 4, ('a', 3)),
        (1, 0, 4, ('b', 1)),
        (1, 0, 4),
    ):
        v = StrictVersion('.'.join(map(str, version)))
        assert str(v) == '.'.join(map(str, version))
        assert v.version == version[:3]
        if len(version) == 4:
            assert v.prerelease == version[3]
        else:
            assert v.prerelease is None



# Generated at 2022-06-12 23:59:38.456561
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    s = StrictVersion()
    s.parse('1.2.3')
    assert s.version == (1, 2, 3)
    assert s.prerelease == None
    s.parse('1.2.3a4')
    assert s.version == (1, 2, 3)
    assert s.prerelease == ('a', 4)
    s.parse('   1.2.3a4    ')
    assert s.version == (1, 2, 3)
    assert s.prerelease == ('a', 4)
    try:
        s.parse('1.2.3.4')
    except ValueError:
        assert True
    else:
        assert False, "should have raised ValueError"

test_StrictVersion_parse()


# Generated at 2022-06-12 23:59:39.339041
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert not Version() > Version()


# Generated at 2022-06-12 23:59:42.671226
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
	version = StrictVersion("1.2.3a4")
	assert str(version) == "1.2.3a4"


# Generated at 2022-06-12 23:59:51.973733
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    tests = [('0.1', (0, 1, 0)),
             ('1.2.3', (1, 2, 3)),
             ('1.2.3a1', (1, 2, 3)),
             ('1.2.3b5', (1, 2, 3)),
             ('1.2.0', (1, 2, 0)),
             ('1.2', (1, 2, 0)),
             ('0.1.dev456', (0, 1, 0)),
             ('0.1.dev', (0, 1, 0)),
             ('0.1.0dev456', (0, 1, 0)),
             ('0.1.0dev', (0, 1, 0)),
            ]

# Generated at 2022-06-12 23:59:54.357489
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    assert v <= '0'

# Generated at 2022-06-13 00:00:04.297482
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils2.version import Version
    from distutils2.version import LooseVersion
    from distutils2.version import StrictVersion
    v = LooseVersion('1.2.3')
    assert v == LooseVersion('1.2.2')
    assert v == LooseVersion('1.2.3')
    assert v == LooseVersion('1.2.3-a')
    assert v == LooseVersion('1.2.3-1')
    assert v == LooseVersion('1.2.3-1.1')
    assert v == LooseVersion('1.2.3-1.1.1')
    assert v == LooseVersion('1.2.3-b')
    assert v == LooseVersion('1.2.3-b-a')

# Generated at 2022-06-13 00:00:19.856190
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    import sys
    import unittest

    # Create an instance of the class we want to test
    v1 = Version('1.0')

    # Create a test case to test the functionality of the method
    # that the instance was created with
    class MyTest(unittest.TestCase):
        def runTest(self):
            v2 = Version('1.0')
            self.assertTrue(v1 >= v2)

    # Create a suite containing the test case
    suite = unittest.TestSuite()
    suite.addTest(MyTest())

    # Create a TextTestRunner object
    runner = unittest.TextTestRunner()

    # Run the suite using the runner.
    if not runner.run(suite).wasSuccessful():
        sys.exit(1)



# Generated at 2022-06-13 00:00:20.884883
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version().__eq__(None) == NotImplemented

# Generated at 2022-06-13 00:00:29.213606
# Unit test for method __le__ of class Version
def test_Version___le__():
    """
    >>> v = Version()
    >>> v
    Version ('0')

    >>> v.__le__('')
    True
    >>> v.__le__(None)
    True
    >>> v.__le__('0')
    True
    >>> v.__le__('1')
    True
    >>> v.__le__('a')
    True
    >>> v.__le__('zzzz')
    True

    >>> v.__le__('-1')
    NotImplemented
    >>> v.__le__('+1')
    NotImplemented
    >>> v.__le__(v)
    NotImplemented
    """
    pass



# Generated at 2022-06-13 00:00:39.402626
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    v = LooseVersion()

    for vstring in ('1.2.2.4', '1.5.5', '1.5.5pl1', '1.5.5a1', '1.5.5b3',
                    '1.0', '1.0pl1', '1.0a1', '1.0b3', '2g6', '11g',
                    '0.960923', '2.2beta29', '1.13++'):
        v.parse(vstring)
        assert str(v) == vstring

# class that knows how to compare both version strings and LooseVersion
# objects

# Generated at 2022-06-13 00:00:40.639638
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version("1.2.3") == Version("1.2.3")


# Generated at 2022-06-13 00:00:47.021304
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    # Version is the base class for all version number classes, so
    # this testcase is rather simple and don't do much.
    v1 = Version()
    v2 = Version()
    assert not (v1 < v2)
    assert not (v1 > v2)

# Generated at 2022-06-13 00:00:47.686520
# Unit test for method __eq__ of class Version
def test_Version___eq__(): pass

# Generated at 2022-06-13 00:00:50.055575
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # create the object
    v = Version('v1.2.3')
    assert v == 'v1.2.3'


# Generated at 2022-06-13 00:01:00.509214
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import LooseVersion
    assert LooseVersion('1.4') <= '1.4'
    assert LooseVersion('1.4') <= '1.4.0'
    assert LooseVersion('1.4') <= '1.4.10'
    assert LooseVersion('1.4') >= '1.4'
    assert LooseVersion('1.4') >= '1.4.0'
    assert LooseVersion('1.4') >= '1.4.10'
    assert LooseVersion('1.4') != '1.5'
    assert not (LooseVersion('1.4') < '1.4.0')
    assert not (LooseVersion('1.4') > '1.4.0')

# Generated at 2022-06-13 00:01:10.803010
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version('1.0.0')
    assert (v >= '1.0.0') is True
    assert (v >= Version('1.0.0')) is True
    assert (v >= '0.0.0') is True
    assert (v >= Version('0.0.0')) is True
    assert (v >= '1.0.1') is False
    assert (v >= Version('1.0.1')) is False

#
# This class is the base for the two main version numbering classes
# (StrictVersion and LooseVersion).  It defines a generic parser
# (parse()) that breaks the version string down into its components
# and a generic comparator (__cmp__) that performs component-by-component
# comparisons between version numbers.  In general, descending version
# numbers sort lower than ascending version numbers, so that

# Generated at 2022-06-13 00:01:32.534999
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.version import StrictVersion

    t = StrictVersion("1.1.1")
    assert t.__ge__("1.1.1")
    assert t.__ge__(StrictVersion("1.1.1"))
    assert not t.__ge__("1.1")
    assert not t.__ge__(StrictVersion("1.1"))
    assert t.__ge__("1.1-r1")
    assert t.__ge__(StrictVersion("1.1-r1"))
    assert not t.__ge__("1.2")
    assert not t.__ge__(StrictVersion("1.2"))
    assert not t.__ge__("1.1.1.1")
    assert not t.__ge__(StrictVersion("1.1.1.1"))



# Generated at 2022-06-13 00:01:36.523494
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    lv = LooseVersion('1.2.3')
    assert lv.version == [1, 2, 3]

    lv = LooseVersion('1.2.a3')
    assert lv.version == [1, 2, 'a', 3]

    lv = LooseVersion('1.2a3')
    assert lv.version == [1, 2, 'a', 3]

    lv = LooseVersion('1.2.3.4')
    assert lv.version == [1, 2, 3, 4]

    lv = LooseVersion('1.2.3-1')
    assert lv.version == [1, 2, 3, '-', 1]

    lv = LooseVersion('1.2.3dev11')

# Generated at 2022-06-13 00:01:37.131597
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version('') <= Version('')


# Generated at 2022-06-13 00:01:38.583355
# Unit test for method __le__ of class Version
def test_Version___le__():
    ver1 = Version('1.2.3')
    ver2 = Version('2.2.3')
    assert(ver1 <= ver2)


# Generated at 2022-06-13 00:01:39.241117
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    Version('') >= ''

# Generated at 2022-06-13 00:01:40.298173
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version('1.0')
    assert v <= '1.0'

# Generated at 2022-06-13 00:01:48.727398
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import random
    # If a == b, you should return False
    version_a = Version('1')
    version_b = Version('1')
    # If a < b, you should return False
    assert not (version_a > version_b)
    # If a > b, you should return True
    assert version_b > version_a
    # Test random comparisons
    for i in range(1000):
        version_a = Version(str(random.randint(1, 1000)))
        version_b = Version(str(random.randint(1, 1000)))
        assert (version_a > version_b) == (version_b < version_a)


# Generated at 2022-06-13 00:01:54.072683
# Unit test for method __le__ of class Version
def test_Version___le__():
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]
    # instance [0]

    import sys
    import unittest

    # class VersionTestCase(unittest.TestCase):
    #     def setUp(self):
    #         self.a = 'Ana'
    #         self.b = 'Bob'
    #         self.c = 'Cat'
    #         self.s = 'Steve'
    #         self.v = Version('1.2.3.4')
    #        

# Generated at 2022-06-13 00:01:56.060921
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version("1")
    v2 = Version("1")
    assert v1 == v2


# Generated at 2022-06-13 00:02:02.761144
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    # test_parse_1: Testing parsing of digits followed by letters.
    # Input is '1.2.A'
    # Expected output: (1, 2, 'A')
    def test_parse_1():
        v = LooseVersion('1.2.A')
        assert v.version == (1, 2, 'A')
        assert v.vstring == '1.2.A'
    # Call the tested method
    test_parse_1()

    # test_parse_2: Testing parsing of digits followed by letters.
    # Input is '3.2.2a2'
    # Expected output: (3, 2, 2, 'a', 2)
    def test_parse_2():
        v = LooseVersion('3.2.2a2')

# Generated at 2022-06-13 00:02:17.955015
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version
    class MyVersion(Version):
        def __init__(self, vstring=None):
            Version.__init__(self, vstring)
        def parse(self, vstring):
            pass
        def __le__(self, other):
            Version.__le__(self, other)
        def _cmp(self, other):
            return 1
    assert MyVersion() <= MyVersion()
    assert not MyVersion() >= MyVersion()
# Test ends


# Generated at 2022-06-13 00:02:22.432898
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import StrictVersion

    v = StrictVersion("1.2.3")
    assert v <= "1.2.3"



# Generated at 2022-06-13 00:02:24.034578
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert v == v


# Generated at 2022-06-13 00:02:26.846155
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version
    v = Version("1.0")
    assert (v == "1.0")
    assert (v == Version("1.0"))
    assert (v != "1.1")
    assert (v != Version("1.1"))


# Generated at 2022-06-13 00:02:35.435532
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert( Version('00') <= Version(0) == True )
    assert( Version('00') <= Version('0') == True )
    assert( Version('01') <= Version(1) == True )
    assert( Version('01') <= Version('1') == True )
    assert( Version('10') <= Version(10) == True )
    assert( Version(10) <= Version('10') == True )
    assert( Version('1.5') <= Version(1.5) == True )
    assert( Version('1.5') <= Version('1.5') == True )
    assert( Version(1.5) <= Version('1.5') == True )
    assert( Version('1.5-1') <= Version('1.5') == True )

# Generated at 2022-06-13 00:02:40.923488
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import StrictVersion
    a = StrictVersion('2.0')
    b = StrictVersion('2')
    c = StrictVersion('1.1')
    d = StrictVersion('2')
    assert a<=b
    assert not(a>=b)
    assert a>=c
    assert not(a<=c)
    assert a<=d
    assert a>=d


# Generated at 2022-06-13 00:02:41.718717
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version('1.0') > Version('0.9')



# Generated at 2022-06-13 00:02:48.319391
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version("1.0")
    assert v == "1.0"
    assert v <= "1.0"
    assert v >= "1.0"
    assert v <= "1.1"
    assert v < "1.1"
    assert v >= "0.1"
    assert v > "0.1"



# Generated at 2022-06-13 00:02:52.830025
# Unit test for method __eq__ of class Version
def test_Version___eq__():

    v1 = Version('1.2.3')
    v2 = Version('1.2.3')
    v3 = Version('1.2.4')
    assert v1 == v2
    assert v2 != v3


# Generated at 2022-06-13 00:02:54.578029
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version('2.0').__gt__('1.0') == True

# Generated at 2022-06-13 00:03:06.454312
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    other = Version()
    assert v <= other



# Generated at 2022-06-13 00:03:08.849207
# Unit test for method __le__ of class Version
def test_Version___le__():
    version = Version()
    version.parse('5.5.5')
    assert version == '5.5.5'
    assert version <= '5.5.5'
    assert version <= '5.5.6'
    assert not version <= '5.5.4'
    assert not version <= '5.4'

# Generated at 2022-06-13 00:03:09.735475
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()

# Generated at 2022-06-13 00:03:11.630038
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v.parse('0.0.0')
    assert v.__le__(v)



# Generated at 2022-06-13 00:03:12.476710
# Unit test for method __le__ of class Version
def test_Version___le__():
    return NotImplemented


# Generated at 2022-06-13 00:03:15.755850
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.0.0')
    v2 = Version('1.0.0')
    r1 = (v1 == v2)
    assert r1 == True
    v3 = Version('1.0.1')
    r2 = (v1 == v3)
    assert r2 == False


# Generated at 2022-06-13 00:03:17.142168
# Unit test for method __le__ of class Version
def test_Version___le__():
    a = Version()
    b = Version()
    return ((a == b) == (a <= b))

# Generated at 2022-06-13 00:03:27.679392
# Unit test for method __eq__ of class Version
def test_Version___eq__():

    def should_be(lhs, rhs, expected):
        actual = lhs == rhs
        assert actual == expected, '%r == %r => %r != %r' % (lhs, rhs, actual, expected)

    # Invalid string input argument
    should_be(Version('0.0.0-dev+abcdefghijklmnop'),
              Version('0.0.0-dev+abcdefghijklmnop'),
              True)

    # Invalid string input argument
    should_be(Version('0.0.0-dev+abcdefghijklmnop'),
              Version('0.0.0-dev+a'),
              False)

    # Invalid string input argument

# Generated at 2022-06-13 00:03:34.771859
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from types import ModuleType
    modules = []
    for name in [
        'distutils.version'
    ]:
        m = ModuleType(str(name))
        m.__file__ = __file__
        modules.append(m)
        try:
            exec("from {} import *".format(name), m.__dict__)
        except ImportError:
            pass
    modules.append(ModuleType("__main__"))
    g = {}
    l = {}
    x = Version("Some version")
    y = Version("Some version")
    # verify selector__gt__

    r = x._Version__gt__(y)
    if isinstance(r, bool):
        pass
    else:
        raise TypeError("r is not a bool")

    r = x._Version__gt__("Some version")

# Generated at 2022-06-13 00:03:41.897905
# Unit test for method __le__ of class Version
def test_Version___le__():
    # Version
    v = Version()
    # Version
    v1 = Version()
    assert v <= v1
    assert not v < v1
    assert v >= v1
    assert not v > v1
    # Version(value, ...)
    v2 = Version('1.0')
    assert v2 <= v2
    assert not v2 < v2
    assert v2 >= v2
    assert not v2 > v2
    # str
    assert v2 <= '1.0'
    assert not v2 < '1.0'
    assert v2 >= '1.0'
    assert not v2 > '1.0'
    # NotImplemented
    # TODO: not implemented exception?
    # assert v2 <= None
    # assert not v2 < None
    # assert v2 >= None
    #

# Generated at 2022-06-13 00:04:11.613193
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    class TestVersion(Version):
        def __init__(self, vstring=None):
            if vstring:
                self.parse(vstring)

        def parse(self, vstring):
            self.vstring = vstring

        def __repr__(self):
            return "%s ('%s')" % (self.__class__.__name__, str(self))

        def __str__(self):
            return self.vstring

        def _cmp(self, other):
            if self.__class__ is other.__class__ and \
               self.vstring == other.vstring:
                return 0
            else:
                return 1
    v1 = TestVersion('a')
    v2 = TestVersion('a')
    assert v1 == v2

# Generated at 2022-06-13 00:04:21.000269
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version("2.0")
    assert (v <= "2.0"), "2.0 <= 2.0"
    assert (v <= "2.0.0"), "2.0 <= 2.0.0"
    assert (v <= "2.0.0.0"), "2.0 <= 2.0.0.0"
    assert (v <= "3.0"), "2.0 <= 3.0"
    assert (v <= "3.0.0"), "2.0 <= 3.0.0"
    assert (v <= "3.0.0.0"), "2.0 <= 3.0.0.0"


# Generated at 2022-06-13 00:04:23.932372
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version(None)
    v2 = Version(None)
    assert (v1 <= v2) is NotImplemented
    assert (v1 <= 1) is NotImplemented

# Generated at 2022-06-13 00:04:30.223509
# Unit test for method __le__ of class Version
def test_Version___le__():
    version = Version()
    version._cmp = lambda other: -1
    assert version <= None

    version = Version()
    version._cmp = lambda other: 0
    assert version <= None

    version = Version()
    version._cmp = lambda other: 1
    assert version <= None

    version = Version()
    version._cmp = lambda other: NotImplemented
    assert version <= None



# Generated at 2022-06-13 00:04:33.792103
# Unit test for method __le__ of class Version
def test_Version___le__():
    ver = Version()
    other = NotImplemented
    ver._cmp = lambda x: 1
    assert ver.__le__(other) == 0
    ver._cmp = lambda x: NotImplemented
    assert ver.__le__(other) == NotImplemented

# Generated at 2022-06-13 00:04:38.749308
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    novo_Version = Version()
    novo_Version.parse('1.0')
    assert novo_Version == '1.0'
    novo_Version = Version()
    novo_Version.parse('1.0')
    assert not(novo_Version == '2.0')

# Generated at 2022-06-13 00:04:45.793903
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version(vstring='')
    assert v <= '' # False
    v = Version(vstring='')
    assert v <= '' # False
    v = Version(vstring='')
    assert v <= '' # False
    v = Version(vstring='')
    assert v <= '' # False
    v = Version(vstring='')
    assert v <= '' # False
    v = Version(vstring='')
    assert v <= '' # False
    v = Version(vstring='')
    assert v <= '' # False
    v = Version(vstring='')
    assert v <= '' # False
    v = Version(vstring='')
    assert v <= '' # False


# Generated at 2022-06-13 00:04:47.153596
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Test for method __le__ of class Version"""
    Version().__le__(1)


# Generated at 2022-06-13 00:04:50.715829
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version().__eq__(None) == NotImplemented
    assert Version(vstring="2.0").__eq__(None) == NotImplemented

# Generated at 2022-06-13 00:04:53.318209
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version('1.2')
    v2 = Version('1.3')
    v3 = Version('1.2')
    assert v1 <= v2
    assert v1 <= v3


# Generated at 2022-06-13 00:05:36.947300
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    version = Version()
    version._cmp = MagicMock(return_value=1)
    result = version.__gt__(1)
    assert result is True
    version._cmp.assert_called_once_with(1)



# Generated at 2022-06-13 00:05:40.526193
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('1.1')
    assert v == Version('1.1')
    assert v == '1.1'
    assert not (v == '1.2')
    assert not (v == '2.2')


# Generated at 2022-06-13 00:05:42.628626
# Unit test for method __le__ of class Version
def test_Version___le__():
    Version.__le__(1,0)
    Version.__le__(1,1)

# Generated at 2022-06-13 00:05:44.361430
# Unit test for method __le__ of class Version
def test_Version___le__():
    ver = Version('4.4')
    assert ver <= '4.12'



# Generated at 2022-06-13 00:05:45.489550
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert not Version.__le__(Version(), Version())

# Generated at 2022-06-13 00:05:52.538381
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    """Test method __eq__ of class Version"""
    test_cases = {
        'same' : (Version('1.2'), Version('1.2'), True),
        'different' : (Version('1.2'), Version('1.3'), False),
        'string' : (Version('1.2'), '1.2', True),
        'empty' : (Version('1.2'), '', True),
        'not version' : (Version('1.2'), [], NotImplemented),
    }
    fail_count, tests = 0, 0
    for case, params in test_cases.items():
        print('---> Testing case: %s' % case)

# Generated at 2022-06-13 00:05:58.759380
# Unit test for method __eq__ of class Version
def test_Version___eq__():
  from ansible.module_utils._text import to_text

  string1 = '1.0.0.0'
  string2 = '2.0.0.0'

  result1 = Version(vstring=string1)
  result2 = Version(vstring=string2)

  assert result1._cmp(result2) == -1 # Version._cmp
  assert result1.__eq__(result2) == False # Version.__eq__
  assert result2.__eq__(result1) == False # Version.__eq__
  assert result1.__eq__(string2) == False # Version.__eq__
  assert result2.__eq__(string1) == False # Version.__eq__
  assert result1.__eq__(result1) == True # Version.__eq__
  assert result2.__eq

# Generated at 2022-06-13 00:06:05.241956
# Unit test for method __le__ of class Version
def test_Version___le__():
    nums = [(2, 0, 0), (2, 0, 1), (2, 0, 2), (2, 1, 0)]
    for i in range(4):
        for j in range(4):
            v1 = Version(nums[i])
            v2 = Version(nums[j])
            expected = i <= j
            assert (v1 <= v2) == expected
            assert (v2 <= v1) == (not expected)


# Generated at 2022-06-13 00:06:07.997248
# Unit test for method __le__ of class Version
def test_Version___le__():
    """Test method __le__ of class Version."""
    # Default method
    assert Version().__le__() == NotImplemented
    # Default method
    assert Version().__le__(None) == NotImplemented


# Generated at 2022-06-13 00:06:09.551676
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    v.__gt__('a')
test_Version___gt__()


# Generated at 2022-06-13 00:09:05.752123
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    def f(self, other):
        try:
            return self._cmp(other) == 0
        except TypeError:
            return NotImplemented

    t = Version('1')
    assert t == '1'
    assert t == 1
    assert t == Version('1')
    assert not(t == '1.0')
    assert not(t == Version('1.0'))
    assert not(t == 1.0)
    assert not(t == 0)

