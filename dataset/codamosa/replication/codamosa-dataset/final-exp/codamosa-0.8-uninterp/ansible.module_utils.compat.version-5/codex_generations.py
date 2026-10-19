

# Generated at 2022-06-12 23:59:28.821125
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    # Simple regular case
    version = StrictVersion("1.2b1")
    assert str(version) == "1.2b1"
    
    # Strip of trailing zeros
    version = StrictVersion("1.0.0")
    assert str(version) == "1.0"
    
    # Strip of trailing zero and pre-release version
    version = StrictVersion("1.0.0rc1")
    assert str(version) == "1.0rc1"
    
    # Pre-release version only
    version = StrictVersion("rc1")
    assert str(version) == "0.0rc1"
    
    # Pre-release version only with build number
    version = StrictVersion("rc1.1")
    assert str(version) == "0.0rc1.1"
    
   

# Generated at 2022-06-12 23:59:36.631543
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    from distutils.version import StrictVersion
    versions = ['0.4', '0.4.0', '0.4.1', '0.5a1', '0.5b3', '0.5', '0.9.6',
                '1.0', '1.0.4a3', '1.0.4b1', '1.0.4',
                '1', '2.7.2.2', '1.3.a4', '1.3pl1', '1.3c4']
    for version in versions:
        version = StrictVersion(version)


# Unit tests for class StrictVersion

# Generated at 2022-06-12 23:59:47.455672
# Unit test for method __le__ of class Version

# Generated at 2022-06-12 23:59:51.309599
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    def nop(*args, **kwargs):
        pass
    def method():
        Version(vstring=None).__eq__(nop())
    expected = AttributeError
    try:
        method()
    except expected:
        pass
    else:
        raise AssertionError("expected exception to be raised")


# Generated at 2022-06-12 23:59:58.017181
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    version = Version()
    version._cmp = lambda self, other: 0
    assert(version.__eq__('other') == True)
    version._cmp = lambda self, other: 1
    assert(version.__eq__('other') == False)
    version._cmp = lambda self, other: NotImplemented
    assert(version.__eq__('other') == NotImplemented)



# Generated at 2022-06-13 00:00:06.936201
# Unit test for method __lt__ of class Version

# Generated at 2022-06-13 00:00:08.750220
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v = DistributionMetadata.Version(vstring='1.0')
    assert v < '1.01'

# Generated at 2022-06-13 00:00:12.790630
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version()
    v2 = Version()
    assert v1.__ge__(v2)
    assert v2.__ge__(v1)
    assert v1.__ge__(v1)
    assert v2.__ge__(v2)



# Generated at 2022-06-13 00:00:14.825468
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    version = StrictVersion("2.0")
    assert str(version) == "2.0"

# Generated at 2022-06-13 00:00:21.666185
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion('1.5').__str__() == '1.5'
    assert StrictVersion('1.5.0').__str__() == '1.5.0'
    assert StrictVersion('1.5.0a1').__str__() == '1.5.0a1'
    assert StrictVersion('1.5.0b1').__str__() == '1.5.0b1'
    assert StrictVersion('1.5.0a10.dev10').__str__() == '1.5.0a10.dev10'


# Generated at 2022-06-13 00:00:35.610249
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    v._cmp = lambda x: True
    assert v == 1
    v._cmp = lambda x: False
    assert not (v == 1)
    assert not (v == "abc")


# Generated at 2022-06-13 00:00:37.816325
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v._cmp = lambda other: -1
    assert v >= 'foo'
test_Version___le__()

# Generated at 2022-06-13 00:00:39.582077
# Unit test for method __le__ of class Version
def test_Version___le__():
  v = Version()
  assert v.__le__(1) == NotImplemented

# Generated at 2022-06-13 00:00:42.111722
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # Invalid input
    with pytest.raises(TypeError):
        assert (test_Version.Version().__gt__(test_Version.Version()) not in [object(), None])
    # Ensure the method__gt__ of class Version is present
    assert (callable(test_Version.Version().__gt__))

# Generated at 2022-06-13 00:00:44.409342
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version.__gt__(Version(), Version()) is NotImplemented



# Generated at 2022-06-13 00:00:50.772974
# Unit test for method __le__ of class Version
def test_Version___le__():
    def check(self, other, expected):
        print("Version.__le__('{}', '{}') == {}".format(self, other, expected))
        assert Version(self).__le__(Version(other)) == expected
    check('0.9', '1.0', True)
    check('1.0', '1.0', True)
    check('1.1', '1.0', False)


# Generated at 2022-06-13 00:00:59.502887
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """This method tests the __lt__ method of class Version

    The following cases are considered:
        * a < b
        * b < a
        * a < a
    """
    a = Version('0.1.1')
    b = Version('0.2')
    if a < b:
        print('Passed test case 1')
    else:
        print('Failed test case 1')
    if b < a:
        print('Failed test case 2')
    else:
        print('Passed test case 2')
    if a < a:
        print('Failed test case 3')
    else:
        print('Passed test case 3')


# Generated at 2022-06-13 00:01:02.807557
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    v = StrictVersion('1.3b3')
    assert v.__str__() == '1.3b3'



# Generated at 2022-06-13 00:01:03.441380
# Unit test for method __lt__ of class Version
def test_Version___lt__():
  pass

# Generated at 2022-06-13 00:01:11.995681
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Version.__eq__() -> int
    # Tests for the method special_op __eq__ of class Version
    # Equivalence partitioning:
    #     returns == 0:

    from distutils.version import Version
    v1 = Version()
    v2 = Version()
    assert v1.__eq__(v2) == 0

    #     returns > 0:

    from distutils.version import Version
    v1 = Version()
    v2 = Version()
    assert v1 != v2

    #     returns < 0:

    from distutils.version import Version
    v1 = Version()
    v2 = Version()
    assert v1 != v2
    assert not v1.__eq__(v2)

# Generated at 2022-06-13 00:01:29.064087
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    import random
    n = random.randint(1, 1000)
    name = ''
    for i in range(n):
        name += chr(random.randint(0, 255))
    name = '{}'.format(name)

    try:
        v1 = Version()
        v2 = Version()
        assert (v1 == v2), "A version cannot be equal to another version"
    except:
        raise AssertionError("Error in Version.__eq__")
    

# Generated at 2022-06-13 00:01:33.141478
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version('3.0')
    assert (v == '3.0')
    assert (v == Version('3.0'))

    v = Version('3.0.0')
    assert (v == '3.0')
    assert (v == Version('3.0'))



# Generated at 2022-06-13 00:01:34.296290
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version() <= Version()
    assert Version() <= Version('0')



# Generated at 2022-06-13 00:01:36.211556
# Unit test for method __le__ of class Version
def test_Version___le__():
    version_class = Version
    value = lambda a, b: '{}'
    version_obj = version_class(value)
    assert version_obj <= value

# Generated at 2022-06-13 00:01:42.135155
# Unit test for method __le__ of class Version
def test_Version___le__():
    l = NotImplemented
    assert getattr(Version, '__le__')(l) == l
    assert getattr(Version, '__le__')(1) == NotImplemented
    assert getattr(Version, '__le__')(re.compile('test')) == NotImplemented
    assert getattr(Version, '__le__')([]) == NotImplemented
    assert getattr(Version, '__le__')({}) == NotImplemented
    assert getattr(Version, '__le__')(object()) == NotImplemented
    assert getattr(Version, '__le__')(object, 1) == NotImplemented
    assert getattr(Version, '__le__')(object, '1') == NotImplemented

# Generated at 2022-06-13 00:01:46.662699
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version
    v = Version('1.1')
    assert v <= v
    assert v <= '1.1'
    assert not v <= '1.1a1'
    assert not v <= '1.2'


# Generated at 2022-06-13 00:01:48.687852
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version()
    v2 = Version()
    assert v1 < v2
# End of unit test for method __lt__ of class Version


# Generated at 2022-06-13 00:01:55.027259
# Unit test for method __le__ of class Version
def test_Version___le__():
    import unittest
    import doctest
    import sys

    class C(Version):
        def parse(self, vstring):
            self._cmp = vstring
        def __str__(self):
            return self._cmp
        def __repr__(self):
            return "<C object>"

    class D(Version):
        def __str__(self):
            return "D"
        def __repr__(self):
            return "<D object>"

    class E(Version):
        def __str__(self):
            return "E"
        def __repr__(self):
            return "<E object>"

    class F:
        pass

    class CmpTestCase(unittest.TestCase):
        def test_equal(self):
            a = C(1)
            b = C(1)
           

# Generated at 2022-06-13 00:01:56.565636
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    assert (v == v) == True


# Generated at 2022-06-13 00:01:58.255020
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert (Version('1.2').__eq__(Version('1.2')) == True)


# Generated at 2022-06-13 00:02:18.118509
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    o = Version("1.0")
    return o.__eq__("2.0")

# Generated at 2022-06-13 00:02:22.153672
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    # Test failures
    try:
        raise AssertionError('Not implemented')
    except AssertionError:
        pass

# Generated at 2022-06-13 00:02:25.336642
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    assert not v == None
    assert not v < None
    assert v <= None
    assert not v > None
    assert v >= None


# Generated at 2022-06-13 00:02:30.980767
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Version class exposes only the interface it implements, and the
    #  underlying implementation is done in the subclasses - there is no
    #  need to test more than common interface.
    v1 = Version('1.0')
    v2 = Version('2.0')
    assert v1 == v1
    assert v1 != v2
    assert not(v1 == v2)
    return



# Generated at 2022-06-13 00:02:32.777514
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__('1.0') == True

# Generated at 2022-06-13 00:02:39.942362
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version()
    v1.parse('1.0')
    v2 = Version()
    v2.parse('1.2')
    v3 = Version()
    v3.parse('1.0')
    if v1 <= v2:
        print('Pass: v1 <= v2')
    else:
        print('Fail: v1 <= v2')
    if v1 <= v3:
        print('Pass: v1 <= v3')
    else:
        print('Fail: v1 <= v3')



# Generated at 2022-06-13 00:02:43.605709
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    """Test for method Version.__gt__."""
    assert (Version('1.0') > Version('0.9'))
    assert not (Version('1.0') > Version('1.0'))
    assert not (Version('1.0') > Version('1.1'))


# Generated at 2022-06-13 00:02:45.349672
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.4')
    v2 = Version('1.5b3')
    assert v1 < v2


# Generated at 2022-06-13 00:02:57.214826
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    print("Testing Version.__lt__", end="")

    assert Version("1.0") < Version("2.0")
    assert Version("1.0") < "2.0"
    assert not (Version("1.0") < Version("1.0"))
    assert not ("1.0" < Version("1.0"))
    assert not (Version("1.0") < "1.0")
    assert not ("1.0" < Version("1.0"))

    try:
        Version("1.0") < 1
    except TypeError:
        pass
    else:
        assert 0, "TypeError not raised"

    try:
        Version("1.0") < 1.1
    except TypeError:
        pass
    else:
        assert 0, "TypeError not raised"

    print("... ok")
# Unit

# Generated at 2022-06-13 00:03:00.665103
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert not (Version('1.0') <= Version('1.0'))
    assert (Version('1.0') <= Version('5.5'))
    assert (Version('1.0') <= '5.5')



# Generated at 2022-06-13 00:03:38.330811
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    inst = Version()

# Generated at 2022-06-13 00:03:39.973126
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    version = Version()
    version.__ge__('1.1')


# Generated at 2022-06-13 00:03:47.873822
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version("1.0")
    v2 = Version("1.0")
    assert v1 <= v2 

    v1 = Version("1.0")
    v2 = Version("0.9")
    assert not v1 <= v2 

    v1 = Version("1.0")
    v2 = Version("1.1")
    assert v1 <= v2 

    v1 = Version("1.0a1")
    v2 = Version("1.0b1")
    assert v1 <= v2 

    v1 = Version("1.0a")
    v2 = Version("1.0a1")
    assert v1 <= v2 

    v1 = Version("1.0a1")
    v2 = Version("1.0a")
    assert not v1 <= v2 
#

# Generated at 2022-06-13 00:03:53.328194
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    from lib2to3.fixes.fix_versions import Version
    from lib2to3.fixes.fix_versions import StrictVersion
    import unittest


    class VersionTestCase(unittest.TestCase):
        def test___gt__(self):
            """Check various cases of __gt__ of class Version."""

            v1 = Version('1.0')
            v2 = Version('2.0')
            v2_5 = Version('2.5')

            self.assertTrue(v1 < v2)
            self.assertTrue(v1 <= v2)
            self.assertTrue(v2 >= v1)
            self.assertTrue(v2 > v1)
            self.assertFalse(v1 >= v2)
            self.assertFalse(v1 > v2)

# Generated at 2022-06-13 00:04:02.862551
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Test method __lt__ of class Version."""

    version_v1 = Version('0.9.1')
    version_v2 = Version('0.9.2')
    version_v3 = Version('0.9.1')
    version_v4 = Version('0.9.11')

    assert version_v1 < version_v2
    assert version_v1 <= version_v3
    assert version_v3 <= version_v2
    assert version_v1 < version_v4
    assert not version_v4 <= version_v1
    assert not version_v1 == version_v4
    assert not version_v1 < version_v1
    assert not version_v1 > version_v1


# Generated at 2022-06-13 00:04:04.132230
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v = Version()
    v == None


# Generated at 2022-06-13 00:04:07.706853
# Unit test for method __lt__ of class Version
def test_Version___lt__():
  import unittest
  class TestVersion(unittest.TestCase):
    def test_less_than(self):
      self.assertTrue(Version('1') < Version('2'))

  unittest.main()



# Generated at 2022-06-13 00:04:10.250988
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    a = StrictVersion('1.2.0')
    b = StrictVersion('1.1.0')
    return a.__ge__(b)
test_Version___ge__()

# Generated at 2022-06-13 00:04:13.199776
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1')
    v2 = Version('2')
    if v1 == v2:
        return False
    return True

# Generated at 2022-06-13 00:04:18.822298
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version
    import unittest2
    class Version___gt___TestCase(unittest2.TestCase):
        def test_simple(self):
            v = Version('1.3')
            self.assertEqual(v.__gt__('1.2'), True)

# Generated at 2022-06-13 00:04:49.011183
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('3.2.2') < Version('3.2.3')



# Generated at 2022-06-13 00:04:57.528050
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    standard_versions = [
        '0.4', '0.4.0',
        '0.4.1',
        '0.5a1',
        '0.5b3',
        '0.5',
        '0.9.6',
        '1.0',
        '1.0.4a3',
        '1.0.4b1',
        '1.0.4',
    ]
    for ver in standard_versions:
        v = StrictVersion(ver)
        check_StrictVersion___str__(v, ver)

# Generated at 2022-06-13 00:04:58.824358
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version().__le__(Version()) == NotImplemented



# Generated at 2022-06-13 00:05:08.361459
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    method = Version().__lt__
    assert method(("<", ">", "==", ">=", "<=")) == True
    assert method(("==",)) == True
    assert method(("<", "<=", ">=")) == True
    assert method(("<=", ">", "==", ">=", "<")) == True
    assert method(("<", ">", ">=", "==", "<=")) == True
    assert method(("==", ">", ">=", "<", "<=")) == True
    assert method(("<=", ">=", ">", "<", "==")) == True
    assert method(("<", ">", ">=", "==", "<=")) == True
    assert method(("<=", ">", "<", ">=", "==")) == True

# Generated at 2022-06-13 00:05:10.464258
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1.0') == '1.0'
    assert Version('1.0') == '1.0.0'
    assert Version('1.0') != '1.1'

# Generated at 2022-06-13 00:05:12.301285
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version() == Version('1.2.3')
    assert Version() != Version('1.3.3')

# Generated at 2022-06-13 00:05:24.297973
# Unit test for method __lt__ of class Version
def test_Version___lt__():
  from distutils.version import Version
  assert Version("1.1")<Version("1.2")==False
  assert Version("1.1")<Version("1.1")==False
  assert Version("2.2")<Version("2.2")==False
  assert Version("1.1.1")<Version("1.3")==False
  assert Version("1.2")<Version("1.2.1")==False
  assert Version("1.3.3")<Version("1.3.6")==False
  assert Version("1.3.6")<Version("1.3.6.6")==False
  assert Version("1.1.1")<Version("2.2")==True
  assert Version("1.1.1")<Version("1.1.10")==True

# Generated at 2022-06-13 00:05:31.473253
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version("1.2.3") == Version("1.2.3")
    assert Version("1.2") == Version("1.2")
    assert Version("1.2") != Version("1.2.3")


# Generated at 2022-06-13 00:05:33.167777
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    ret = StrictVersion("0.4").__str__()
    assert ret == "0.4"


# Generated at 2022-06-13 00:05:34.868099
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version()
    v2 = Version()
    assert v.__eq__(v2) == 1

# Generated at 2022-06-13 00:06:00.645302
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    _test_Version_richcompare('__lt__')

# Generated at 2022-06-13 00:06:09.361542
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    A = Version("1.0")
    B = Version("1.1")
    assert A < B
    assert A <= B
    assert B > A
    assert B >= A
    assert A != B
    assert A._cmp(B) == -1
    assert A._cmp(A) == 0
    assert B._cmp(A) == 1

    C = Version("2.0")
    assert B < C
    assert B <= C
    assert C > B
    assert C >= B
    assert B != C
    assert B._cmp(C) == -1
    assert B._cmp(B) == 0
    assert C._cmp(B) == 1

    D = Version("1.1")
    assert B == D
    assert B >= D
    assert B <= D
    assert B._cmp(D) == 0



# Generated at 2022-06-13 00:06:16.674851
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    Version = __import__('distutils.version').version.Version
    v1 = Version('1')
    v2 = Version('2')
    v3 = Version('3')
    assert (v1.__gt__(v2) == False)
    assert (v1.__gt__(v3) == False)
    assert (v2.__gt__(v1) == True)
    assert (v2.__gt__(v3) == False)
    assert (v3.__gt__(v1) == True)
    assert (v3.__gt__(v2) == True)



# Generated at 2022-06-13 00:06:18.289156
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version().__gt__('1.0b1') is NotImplemented
# End unit test


# Generated at 2022-06-13 00:06:25.248219
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion("1.0.0a0").__str__() == "1.0.0a0"
    assert StrictVersion("1.0.0").__str__() == "1.0.0"
    assert StrictVersion("1.0").__str__() == "1.0.0"
    assert StrictVersion("3").__str__() == "3.0.0"
    assert StrictVersion("3.1").__str__() == "3.1.0"
    assert StrictVersion("3.1.2").__str__() == "3.1.2"

    assert StrictVersion("1.0.0a0").__str__() == "1.0.0a0"

# Generated at 2022-06-13 00:06:37.698966
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from warnings import warn
    from distutils.tests import support
    if hasattr(Version, '__lt__') and not hasattr(Version, '__lt__'):
        warn('__lt__ method defined in class Version but not __le__')
    if not hasattr(Version, '__lt__') and hasattr(Version, '__lt__'):
        warn('__lt__ method defined in class Version but not __lt__')
    if not hasattr(Version, '__lt__') and not hasattr(Version, '__lt__'):
        return
    if not hasattr(Version, '__lt__'):
        warn('__le__ method defined in class Version but not __le__')
    if not hasattr(Version, '__lt__'):
        warn('__le__ method defined in class Version but not __lt__')


# Generated at 2022-06-13 00:06:39.759214
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = StrictVersion('123.45')
    c = v._cmp(str(v))
    assert c == 0

# Generated at 2022-06-13 00:06:41.768136
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version("1.2.3a1")
    assert v == "1.2.3a1"


# Generated at 2022-06-13 00:06:43.551515
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version('1.1')
    v2 = Version('1.2')

    assert v1 <= v2

# Generated at 2022-06-13 00:06:46.308923
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version('1') > Version('1.1')
    assert Version('1.1') > Version('1.1.0')


# Generated at 2022-06-13 00:07:18.323909
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from sys import version_info
    from random import randrange, randint, random, uniform, triangular, gammavariate, gauss, lognormvariate, exponentiallovariate
    if version_info < (2, 7, 0, '', 0): 
        from distutils.tests.setuptools_build_py import random
    from collections import namedtuple
    from copy import deepcopy
    from pickle import dumps, loads, HIGHEST_PROTOCOL
    # Setup
    # Execution
    # Verification
    # Cleanup

# Generated at 2022-06-13 00:07:21.233837
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('2.0')
    v2 = Version(v1)
    assert v1 == v2
    v3 = Version('1.0')
    assert v1 != v3


# Generated at 2022-06-13 00:07:29.509332
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('2.6.22')
    v2 = Version('2.6.23')
    assert v1 != v2

    v1 = Version('2.6.22')
    v2 = Version('2.6.22')
    assert v1 == v2

    v1 = Version('2.6.23')
    v2 = Version('2.7.0')
    assert v1 != v2

    # Test integer comparisons
    assert Version('1.0') == 1
    assert Version('1.0') == 1.0

# Generated at 2022-06-13 00:07:31.525273
# Unit test for method __le__ of class Version
def test_Version___le__():
    ver = Version()
    try:
        res = ver.__le__(49)
    except:
        res = False
    return (res == False)


# Generated at 2022-06-13 00:07:36.988942
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    v._cmp = lambda other: NotImplemented
    assert v.__gt__(1) == NotImplemented
    v._cmp = lambda other: -1
    assert v.__gt__(1) == 0
    v._cmp = lambda other: 0
    assert v.__gt__(1) == 0
    v._cmp = lambda other: 1
    assert v.__gt__(1) == 1

# Generated at 2022-06-13 00:07:38.446211
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert (v > 0) == NotImplemented


# Generated at 2022-06-13 00:07:49.052370
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    from distutils.version import Version

    A = Version('1.2.1')
    B = Version('1.2.2')
    assert A < B
    assert A != B
    assert not (A >= B)
    assert not (A == B)
    assert A <= B

    C = Version('1.2.1')
    D = Version('1.2.1')
    assert C == D
    assert not (C != D)
    assert C <= D
    assert C >= D
    assert not (C < D)
    assert not (C > D)

    E = Version('1.2.1')
    F = Version('1.1.1')
    assert E > F
    assert E != F
    assert not (E <= F)
    assert not (E == F)
    assert E >= F

   

# Generated at 2022-06-13 00:07:51.061811
# Unit test for method __gt__ of class Version
def test_Version___gt__():

    v1 = Version("1.0")
    v2 = Version("2.0")
    assert v1 < v2     # __gt__


# Generated at 2022-06-13 00:07:58.577413
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    def t(v1, v2, eq):
        if (Version(v1) == Version(v2)) != eq:
            raise AssertionError(repr((v1, v2)) + ' != ' + repr(eq))
    t('0.0', '0', True)
    t('0.0', '0.0', True)
    t('0.0', '0.0.0', True)
    t('0.0', '1e-1', True)
    t('0.1', '0.1.0', True)
    t('0.0', '0.0.1', False)
    t('0.0', '0.1', False)
    t('0.0', '1', False)
    t('0.0.1', '0.0.2', False)


# Generated at 2022-06-13 00:08:06.271264
# Unit test for method __gt__ of class Version