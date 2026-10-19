

# Generated at 2022-06-12 23:59:24.911996
# Unit test for method __ge__ of class Version

# Generated at 2022-06-12 23:59:35.033496
# Unit test for method parse of class StrictVersion
def test_StrictVersion_parse():
    def _test_parse(vstring, expected_result):
        parsed = StrictVersion(vstring)
        actual_result = (vars(parsed) == expected_result)
        if (not actual_result):
            raise AssertionError("Failed to parse '%s'" % vstring)

    # version components
    _test_parse('1', {'version' : (1, 0, 0), 'prerelease' : None})
    _test_parse('1.2', {'version' : (1, 2, 0), 'prerelease' : None})
    _test_parse('1.2.3', {'version' : (1, 2, 3), 'prerelease' : None})

    # prerelease suffix

# Generated at 2022-06-12 23:59:46.323747
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    assert StrictVersion('2.7.2.2').__str__() == '2.7.2.2'
    assert StrictVersion('0.4.0').__str__() == '0.4.0'
    assert StrictVersion('0.4').__str__() == '0.4.0'
    assert StrictVersion('1.0.4a3').__str__() == '1.0.4a3'
    assert StrictVersion('1.0.4').__str__() == '1.0.4'
    assert StrictVersion('1.3pl1').__str__() == '1.3pl1'
    assert StrictVersion('1.3c4').__str__() == '1.3c4'

# Generated at 2022-06-12 23:59:47.287771
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version() > Version('1')

# Generated at 2022-06-12 23:59:54.887118
# Unit test for method __str__ of class StrictVersion

# Generated at 2022-06-12 23:59:58.428215
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('1.0')
    w = Version('1.1')
    assert(v < w)
    assert(v <= w)
    assert(v != w)
    assert(w > v)
    assert(v >= w)



# Generated at 2022-06-13 00:00:02.694712
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    assert Version() >= Version()

    class AlwaysGreater(Version):
        def _cmp(self, other):
            return 1

    class AlwaysLess(Version):
        def _cmp(self, other):
            return -1

    assert AlwaysGreater() >= AlwaysLess()
    assert not AlwaysLess() >= AlwaysGreater()
    assert not AlwaysGreater() >= AlwaysGreater()
    assert AlwaysLess() >= AlwaysLess()
    assert not AlwaysGreater() >= "1.0.0"
    assert not AlwaysLess() >= "1.0.0"
    assert AlwaysGreater() >= AlwaysGreater()
    assert AlwaysLess() >= AlwaysLess()
# Test the Version class by subclassing it, then testing instances of the
# subclass.

# Generated at 2022-06-13 00:00:04.267806
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    ver = Version()
    # TODO: implement unit test

# Generated at 2022-06-13 00:00:07.708033
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    print("test_Version___gt__")
    # Arrange
    a = None
    b = None

    # Act
    try:
        a > b
    except NotImplementedError:
        pass  # pass the test

    # Assert



# Generated at 2022-06-13 00:00:18.114143
# Unit test for method __str__ of class StrictVersion
def test_StrictVersion___str__():
    """test StrictVersion.__str__()"""
    # Test default behavior
    v = StrictVersion("1.2.3")
    assert(str(v) == "1.2.3")
    v = StrictVersion("1.2.3a1")
    assert(str(v) == "1.2.3a1")
    v = StrictVersion("1.2.3b1")
    assert(str(v) == "1.2.3b1")
    v = StrictVersion("1.2.3rc1")
    assert(str(v) == "1.2.3rc1")
    v = StrictVersion("1.2.3.dev1")
    assert(str(v) == "1.2.3.dev1")



# Generated at 2022-06-13 00:00:28.424221
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version()
    v.parse("0.1dev1")
    assert v <= "0.1dev1"
    assert v <= Version("0.1dev1")



# Generated at 2022-06-13 00:00:38.002141
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    old_stdout = sys.stdout
    try:
        sys.stdout = StringIO()
        _test_LooseVersion_parse()
        value = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    value = value[value.index('\n===') + 4 : value.rindex('\n===')]
    lines = [line for line in value.split('\n') if line.strip()]
    assert len(lines) == 1 and lines[0] == 'All ok'


# Generated at 2022-06-13 00:00:40.100633
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version("1.1") <= Version("1.1")
    assert not Version("1.2") <= Version("1.1")


# Generated at 2022-06-13 00:00:40.976025
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version('0.0.0')
    assert v > ''


# Generated at 2022-06-13 00:00:43.734023
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # No tests yet
    pass


# Generated at 2022-06-13 00:00:45.314834
# Unit test for method __gt__ of class Version
def test_Version___gt__():
  assert Version('2.2') > '2.1'


# Generated at 2022-06-13 00:00:51.192374
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from ansiblelint.ansible_linter import AnsibleLinter
    from ansiblelint.rules import RulesCollection

    filename = 'lib/ansiblelint/rules/Test_Version___ge__.py'
    uut = AnsibleLinter(filename, {}, RulesCollection())

    assert uut.rules._all_rules[0].id == "Test_Version___ge__"

# Generated at 2022-06-13 00:00:54.599990
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__('') is NotImplemented
    # TODO: implement unit tests for class Version
    pass # TODO: implement unit test

# Generated at 2022-06-13 00:00:56.385327
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    x = Version('1.0')
    assert(x >= '1.0') == True

# Generated at 2022-06-13 00:00:59.041545
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version()
    v2 = Version()
    assert v1 is not v2
    assert not v1.__eq__(v2)
    assert not v2.__eq__(v1)

# Generated at 2022-06-13 00:01:06.887519
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version
    
    
    
    
    
    
    

# Generated at 2022-06-13 00:01:08.591049
# Unit test for method __ge__ of class Version

# Generated at 2022-06-13 00:01:09.967585
# Unit test for method __le__ of class Version
def test_Version___le__():
    from distutils.version import Version
    assert Version('1.1') < Version('1.2')
    assert Version('1.2') <= Version('1.2')

# Generated at 2022-06-13 00:01:18.026829
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    from distutils.version import Version

    assert Version("1.2a1") < Version("1.2")
    assert Version("1.2") < Version("1.2.1")
    assert Version("1.2.1") < Version("1.2.1.1")
    assert Version("1.2a1") < Version("1.2.1")
    assert Version("1.2.1") < Version("1.2pl3")
    assert Version("1.2") < Version("1.2.1.1")
    assert Version("1.2pl3") < Version("1.2.1.1")
    assert Version("1.2.1.1") < Version("1.2.1.1pl2")

# Generated at 2022-06-13 00:01:21.980573
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import unittest

    class Version__gt__TestCase(unittest.TestCase):
        def test(self):
            v1 = Version("1.1")
            v2 = Version("1.2")
            return self.assertFalse(v1 > v2)

    t = Version__gt__TestCase()
    t.test()

# Generated at 2022-06-13 00:01:23.695327
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v1 = Version('1.0')
    v2 = Version('1.0')

    assert v1 == v2



# Generated at 2022-06-13 00:01:26.178585
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version('1.0')
    v2 = Version('1.0')
    assert v1 <= v2


# Generated at 2022-06-13 00:01:29.793525
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    ''' Version.__gt__(other) '''
    other_version = Version()
    version = Version()
    version._cmp = lambda x: 0
    assert version.__gt__(other_version) == False

# Generated at 2022-06-13 00:01:30.442926
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    pass

# Generated at 2022-06-13 00:01:38.362668
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    class Test_Version_Subclass(Version):
        def parse(self, vstring):
            self.version = [int(component) for component in vstring.split('.')]

        def _cmp(self, other):
            if isinstance(other, str):
                other = Test_Version_Subclass(other)
            # Make sure S is a Test_Version_Subclass so that the
            # comparison will not fall through to the Version class'
            # _cmp method.
            if not isinstance(other, Test_Version_Subclass):
                return NotImplemented
            if self.version == other.version:
                return 0
            if self.version < other.version:
                return -1
            return 1


# Generated at 2022-06-13 00:02:02.168451
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    assert v.__gt__(None) == NotImplemented
    assert v.__gt__('this is not a version') == NotImplemented
    assert v.__gt__(v) == False
    assert v.__gt__(Version(v)) == False


    class MyVersion(Version):

        def __init__(self, ver):
            self.ver = ver

        def __repr__(self):
            return "%s ('%s')" % (self.__class__.__name__, str(self))

        def __str__(self):
            return str(self.ver)

        def _cmp(self, other):
            if isinstance(other, str):
                other = MyVersion(other)
            return cmp(self.ver, other.ver)


# Generated at 2022-06-13 00:02:07.857843
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    assert Version('1.0') == Version('1.0') == '1.0'
    assert Version('1.3') == Version('1.3') == '1.3'
    assert Version('1.3') == Version('1.3') == '1.3'
    assert not (Version('1.3') == '1.4')
    assert Version('1.5') == Version('1.5') == '1.5'
    assert Version('1.5') == Version('1.5') == '1.5'
    assert not (Version('1.5') == '1.6')
    assert Version('1.1') == Version('1.1') == '1.1'
    assert Version('1.1') == Version('1.1') == '1.1'

# Generated at 2022-06-13 00:02:09.114331
# Unit test for method __ge__ of class Version
def test_Version___ge__():
  assert True



# Generated at 2022-06-13 00:02:16.992789
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    def check(v1, v2, expected):
        assert (v1 < v2) is expected

    check(Version('0.5.5.5'), Version('0.5.5.5'), False)
    check(Version('0.5.5.5'), Version('1.5.5.5'), True)
    check(Version('0.5.5.5'), Version('0.6.5.5'), True)
    check(Version('0.5.5.5'), Version('0.5.6.5'), True)
    check(Version('0.5.5.5'), Version('0.5.5.6'), True)

    check(Version('0.5.5.5'), '0.5.5.5', False)

# Generated at 2022-06-13 00:02:20.418091
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v2 = Version()
    v1.__gt__(v2)


# Generated at 2022-06-13 00:02:26.755151
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    from distutils.version import Version
    from distutils.tests import support
    from operator import eq

    v1 = Version('1.2.3.4')
    v2 = Version('1.2.3.4')
    v3 = Version('6.6.6.6')

    assert eq(v1, v2)
    assert not eq(v1, v3)


# Generated at 2022-06-13 00:02:30.301261
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    # Method Version.__eq__, line 91
    # Instance Version.__eq__, line 92
    # AssertionError: expected NotImplemented, got NotImplemented
    raise RuntimeError # todo: implement your test here


# Generated at 2022-06-13 00:02:40.439626
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert (Version('') < Version('')) == False
    assert (Version('') < Version('1.0')) == True
    assert (Version('1.0') < Version('')) == False
    assert (Version('1.0') < Version('1.0')) == False
    assert (Version('1.0') < Version('1.0a')) == False
    assert (Version('1.0a') < Version('1.0')) == True
    assert (Version('1.0a') < Version('1.0a')) == False
    assert (Version('1.0a') < Version('1.0alpha')) == False
    assert (Version('1.0alpha') < Version('1.0b')) == True
    assert (Version('1.0alpha') < Version('1.0alpha')) == False

# Generated at 2022-06-13 00:02:41.322815
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version() > '0'



# Generated at 2022-06-13 00:02:43.365313
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    """Test method __lt__ of class Version."""
    v = Version('1.2.3')
    assert v < '1.2.4'
    assert v <= '1.2.4'
    assert v < '1.3'
    assert not (v < '1.2')

# Generated at 2022-06-13 00:03:07.125032
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version("2.2.3")
    v2 = Version("2.2.1")

    assert v1 > v2

# Generated at 2022-06-13 00:03:10.884820
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    args = ()
    other = '5.4'
    retval = Version().__ge__(other)
    assert retval == NotImplemented, \
        'expected %r, got %r' % (NotImplemented, retval)


# Generated at 2022-06-13 00:03:11.750054
# Unit test for method __le__ of class Version
def test_Version___le__():
    assert Version() <= Version()

# Generated at 2022-06-13 00:03:13.544961
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    v1 = Version('1.3.0')
    v2 = Version('1.3.0')
    assert v1 >= v2


# Generated at 2022-06-13 00:03:21.236177
# Unit test for method __le__ of class Version
def test_Version___le__():
    x = Version('1.2.3')
    y = Version('1.2.4')

    if not (x <= x):
        print("FAIL: x <= x")
        return False

    if not (x <= y):
        print("FAIL: x <= y")
        return False

    if not (y >= x):
        print("FAIL: y >= x")
        return False

    if not (y >= y):
        print("FAIL: y >= y")
        return False

    if not (x < y):
        print("FAIL: x < y")
        return False

    if not (y > x):
        print("FAIL: y > x")
        return False

    if x in [y, x, y]:
        print("FAIL: x in [y, x, y]")
        return

# Generated at 2022-06-13 00:03:25.266491
# Unit test for method __le__ of class Version
def test_Version___le__():
    v1 = Version("1.2a")
    v2 = Version("1.2a1")
    assert v1 <= v2

# Generated at 2022-06-13 00:03:33.517392
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import pyangbind.lib.pybindJSON as pybindJSON
    import pickle
    V = Version(vstring="1")
    with open("test.txt", "w") as fd:
      fd.write(str(pybindJSON.dumps(V, mode="ietf")).replace("\\n", "n").replace("\\", ""))
    with open("test.txt", "r") as fd:
      d = fd.read()
      print(d)
    V2 = Version()
    pybindJSON.loads(d, V2, mode="ietf")
    assert V2.vstring == "1"
    assert V < "1.1"
    assert V > "0.0"
    assert V <= "1"
    assert V >= "1"



# Generated at 2022-06-13 00:03:38.293024
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v1 = Version()
    v2 = Version()
    assert v1 >= v2
    v1 = Version('3.3.3')
    v2 = Version('3.3.2')
    assert v1 > v2

# Generated at 2022-06-13 00:03:40.267425
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version('')
    assert v <= ''
    assert not (v <= '1')


# Generated at 2022-06-13 00:03:43.164509
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils.tests.test_version import Version
    
    v = Version("1.0a")
    w = Version("1.0b")
    result = v.__ge__(w)
    assert result == False



# Generated at 2022-06-13 00:04:35.625079
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    # __ge__ : Compare current instance to another instance of the same class
    v1 = Version()
    v2 = Version()
    v3 = Version()
    v4 = Version()
    v1._cmp = lambda val: -1
    assert v1 >= v2 is False
    v1._cmp = lambda val: 0
    assert v1 >= v2 is True
    assert v1 >= v3 is True
    assert v1 >= v4 is True
test_Version___ge__()


# Generated at 2022-06-13 00:04:38.603897
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    w = Version()
    assert v > w, "Test for method __gt__ of class Version failed."

# Generated at 2022-06-13 00:04:40.843547
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    v.parse("1.2.3")
    assert (v.__gt__("1.2.3") == False)

# Generated at 2022-06-13 00:04:43.776918
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    c = Version()
    assert isinstance(c, Version)
    with raises(NotImplementedError):
        c._cmp(None)
    assert c.__gt__('a') == NotImplemented
    assert c.__gt__(c) == NotImplemented




# Generated at 2022-06-13 00:04:48.819112
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import random
    for a in [ random.choice(('a', 'b', 'c')) + str(random.randint(0, 100)) + random.choice(('a', 'b', 'c'))
              for i in range(1000) ]:
        for b in [ random.choice(('a', 'b', 'c')) + str(random.randint(0, 100)) + random.choice(('a', 'b', 'c'))
                  for i in range(1000) ]:
            l = [ a, b ]
            l.sort()
            if (a > b) != (l[0] == a):
                return l, a, b
test_Version___gt__()



# Generated at 2022-06-13 00:04:51.671487
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    vers = Version('1%s' % (''))
    vers2 = Version('2%s' % (''))
    assert not (vers > vers2)

# Generated at 2022-06-13 00:04:53.274085
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1')
    v2 = Version('2')
    assert v1 < v2

# Generated at 2022-06-13 00:05:04.845148
# Unit test for method parse of class LooseVersion
def test_LooseVersion_parse():
    import re
    import unittest
    import types


# Generated at 2022-06-13 00:05:05.543735
# Unit test for method __le__ of class Version
def test_Version___le__():
    v = Version("2.2a1")
    assert v <= "2.2rc1"



# Generated at 2022-06-13 00:05:07.499296
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    r = Version('1.2')
    s = Version('1.2')
    t = Version('1.3')
    assert not r.__gt__(s)
    assert not r.__gt__(t)
    assert not s.__gt__(r)
    assert not s.__gt__(t)
    assert t.__gt__(r)
    assert not t.__gt__(s)



# Generated at 2022-06-13 00:06:47.018551
# Unit test for method __le__ of class Version
def test_Version___le__():
    pass

# Generated at 2022-06-13 00:06:56.460563
# Unit test for method __le__ of class Version
def test_Version___le__():
    # version.Version.__le__
    # Equality
    assert StrictVersion('1.2') <= StrictVersion('1.2') == StrictVersion('1.2')
    # Less than
    assert StrictVersion('1.1') <= StrictVersion('1.2')
    # Greater than
    assert not StrictVersion('1.3') <= StrictVersion('1.2')
    # Equal major number, less in minor number
    assert StrictVersion('1.2.1') <= StrictVersion('1.2.4')
    # Equal major and minor number, less in patch number
    assert StrictVersion('1.3.3a3') <= StrictVersion('1.3.3')
    # Equal major and minor number, less in micro number

# Generated at 2022-06-13 00:06:58.844880
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    assert Version('1') > Version('0.99')
    assert Version('1.0') > Version('1')
    assert Version('1.0.0') > Version('1.0')



# Generated at 2022-06-13 00:07:04.332077
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    import re
    import unittest

    class VersionTests(unittest.TestCase):
        data = [
            # (__version_class__, __init__args, expect)
            (Version, ('1',), NotImplemented),
        ]
        def test___gt__(self):
            for (version_class, initargs, expect) in self.data:
                with self.subTest(version_class=version_class, initargs=initargs, expect=expect):
                    testcase = version_class(*initargs)
                    self.assertEqual(testcase.__gt__('1'), expect)
# __gt__: No tests found
    unittest.main(exit=False)



# Generated at 2022-06-13 00:07:05.163023
# Unit test for method __le__ of class Version
def test_Version___le__():
   inst = Version()


# Generated at 2022-06-13 00:07:10.000627
# Unit test for method __ge__ of class Version
def test_Version___ge__():
    from distutils2.version import Version
    v = Version("2.1")
    assert v >= Version("2.1")
    assert v >= "2.1"
    assert v >= Version("2.0")
    assert v >= "2.0"
    assert not v >= Version("2.2")
    assert not v >= "2.2"
    #
    assert not v >= v
    assert v >= v


# Generated at 2022-06-13 00:07:12.205508
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    v1 = Version('1.20.3')
    v2 = Version('1.20.3')
    assert v1 == v2, 'bad version comparison'

# Generated at 2022-06-13 00:07:13.740006
# Unit test for method __eq__ of class Version
def test_Version___eq__():
    v = Version("1.0")
    assert v == "1.0"


# Generated at 2022-06-13 00:07:15.499101
# Unit test for method __lt__ of class Version
def test_Version___lt__():
    assert Version('1').__lt__('2')
    assert not Version('2').__lt__('1')

# Generated at 2022-06-13 00:07:19.142671
# Unit test for method __gt__ of class Version
def test_Version___gt__():
    v = Version()
    v._cmp = lambda x: 0
    assert v.__gt__(None) == False