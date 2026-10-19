

# Generated at 2022-06-14 06:35:46.415318
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    assert isinstance(PyInfo.string_types, tuple)
    if not PyInfo.PY3:  # Python 2 does not define int
        assert basestring in PyInfo.string_types
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:35:55.625998
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py_info = PyInfo()

    assert py_info.PY2 or py_info.PY3
    assert py_info.PY2 ^ py_info.PY3

    assert isinstance("", py_info.string_types)
    assert isinstance(u"", py_info.string_types)
    assert not isinstance(b"", py_info.string_types)
    assert not isinstance(1, py_info.string_types)
    assert not isinstance(1.0, py_info.string_types)

    assert isinstance("", py_info.text_type)
    assert isinstance(u"", py_info.text_type)
    if py_info.PY2:
        assert not isinstance(b"", py_info.text_type)

# Generated at 2022-06-14 06:36:00.554284
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('hello', PyInfo.string_types)
    assert isinstance('hello', PyInfo.text_type)
    assert isinstance(u'hello', PyInfo.text_type)



# Generated at 2022-06-14 06:36:06.086639
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 and not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert len(PyInfo.integer_types) == 2
    assert PyInfo.class_types == (type, types.ClassType)



# Generated at 2022-06-14 06:36:11.526486
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance(b"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(10, PyInfo.integer_types)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:36:23.846664
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert not (PyInfo.PY2 and PyInfo.PY3)

    s = 'python-future is awesome'
    assert isinstance(s, PyInfo.string_types)
    b = s.encode('utf8')
    assert isinstance(b, PyInfo.binary_type)

    if PyInfo.PY2:
        u = unicode(s)
        assert isinstance(u, PyInfo.text_type)
    else:
        assert isinstance(s, PyInfo.text_type)

    try:
        n = int(s)
    except ValueError:
        pass
    else:
        assert isinstance(n, PyInfo.integer_types)

    class MyClass(object):
        pass

    my_obj = MyClass

# Generated at 2022-06-14 06:36:26.866449
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True


# 执行test函数
test_PyInfo()

# Generated at 2022-06-14 06:36:36.939022
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print("Test for constructor of class PyInfo")
    pyinfo=PyInfo()

    assert pyinfo.PY2==sys.version_info[0]==2
    assert pyinfo.PY3==sys.version_info[0]==3
    assert pyinfo.string_types==(basestring,)
    assert pyinfo.text_type==unicode
    assert pyinfo.binary_type==str
    assert pyinfo.integer_types==(int, long)
    assert pyinfo.class_types==(type, types.ClassType)
    assert pyinfo.maxsize==sys.maxsize

    print("Passed!")


# Generated at 2022-06-14 06:36:46.382081
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance('a', PyInfo.string_types)  # PY2 is str, PY3 is str
    assert not isinstance(b'a', PyInfo.string_types)  # PY2 is str, PY3 is str
    assert isinstance(b'a', PyInfo.binary_type)  # PY2 is str, PY3 is bytes
    assert isinstance('a', PyInfo.text_type)  # PY2 is unicode, PY3 is str
    assert not isinstance(b'a', PyInfo.text_type)  # PY2 is unicode, PY3 is str
    assert isinstance(2, PyInfo.integer_types)  # PY2 is (int, long), PY3 is int
    # PY2 is (type, types.ClassType), PY3 is

# Generated at 2022-06-14 06:36:56.684873
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 is True or pyinfo.PY2 is False
    assert pyinfo.PY3 is not pyinfo.PY2
    assert pyinfo.maxsize > 0
    if pyinfo.PY3:
        assert pyinfo.string_types == str
        assert pyinfo.text_type == str
        assert pyinfo.binary_type == bytes
        assert pyinfo.integer_types == int
        assert pyinfo.class_types == type
    else:
        assert isinstance(pyinfo.string_types, tuple)
        assert basestring in pyinfo.string_types
        assert pyinfo.text_type == unicode
        assert pyinfo.binary_type == str
        assert isinstance(pyinfo.integer_types, tuple)
        assert int in pyinfo.integer_

# Generated at 2022-06-14 06:37:07.499681
# Unit test for constructor of class PyInfo
def test_PyInfo():
    c = PyInfo()
    assert c.PY2 == PythonInfo.PY2
    assert c.PY3 == PythonInfo.PY3
    if PythonInfo.PY3:
        assert c.string_types == PythonInfo.string_types
        assert c.text_type == PythonInfo.text_type
        assert c.binary_type == PythonInfo.binary_type
        assert c.integer_types == PythonInfo.integer_types
        assert c.class_types == PythonInfo.class_types
        assert c.maxsize == PythonInfo.maxsize
    else:
        assert c.string_types == PythonInfo.string_types
        assert c.text_type == PythonInfo.text_type
        assert c.binary_type == PythonInfo.binary_type
        assert c.integer_types == PythonInfo.integer_types


# Generated at 2022-06-14 06:37:11.015668
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()

    assert isinstance(info.PY2, bool)
    assert isinstance(info.PY3, bool)



# Generated at 2022-06-14 06:37:15.786508
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print('PyInfo.PY2 = ', PyInfo.PY2)
    print('PyInfo.PY3 = ', PyInfo.PY3)
    print('PyInfo.maxsize = ', PyInfo.maxsize)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:37:22.206354
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not None
    assert PyInfo.PY3 is not None
    assert PyInfo.maxsize is not None
    assert PyInfo.string_types is not None
    assert PyInfo.text_type is not None
    assert PyInfo.class_types is not None
    assert PyInfo.binary_type is not None
    assert PyInfo.integer_types is not None



# Generated at 2022-06-14 06:37:28.274442
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type is unicode
    assert PyInfo.binary_type is str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:37:39.604596
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (
        sys.version_info[0] == 2
    ), "Definition of class PyInfo is incorrect."
    assert PyInfo.PY3 == (
        sys.version_info[0] == 3
    ), "Definition of class PyInfo is incorrect."
    assert PyInfo.string_types == (
        basestring,
    ), "Definition of class PyInfo is incorrect."
    assert PyInfo.text_type == unicode, "Definition of class PyInfo is incorrect."
    assert PyInfo.binary_type == str, "Definition of class PyInfo is incorrect."
    assert PyInfo.integer_types == (
        int,
        long,
    ), "Definition of class PyInfo is incorrect."

# Generated at 2022-06-14 06:37:41.229098
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == False or PyInfo.PY3 == True



# Generated at 2022-06-14 06:37:45.436279
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("hello", PyInfo.string_types)
    assert isinstance(b"hello", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(long(1), PyInfo.integer_types)

# Generated at 2022-06-14 06:37:49.379998
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance('Hello world', PyInfo.string_types)
    assert isinstance(b'Hello binary', PyInfo.binary_type)
    assert isinstance(123, PyInfo.integer_types)


# Py3's assertions that raise exceptions

# Generated at 2022-06-14 06:37:53.240389
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 == sys.version_info[0] == 2
    assert pyinfo.PY3 == sys.version_info[0] == 3



# Generated at 2022-06-14 06:38:05.398032
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('abc', PyInfo.string_types)
    assert isinstance(True, PyInfo.integer_types)
    assert isinstance(PyInfo, PyInfo.class_types)

    if PyInfo.PY2:
        assert isinstance(u'abc', PyInfo.text_type)
        assert isinstance('abc', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(long(1), PyInfo.integer_types)
    else:
        assert isinstance('abc', PyInfo.text_type)
        assert isinstance(b'abc', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:15.431326
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def output():
        print(PyInfo.PY2)
        print(PyInfo.PY3)
        print(PyInfo.string_types)
        print(PyInfo.text_type)
        print(PyInfo.binary_type)
        print(PyInfo.integer_types)
        print(PyInfo.class_types)
        print(PyInfo.maxsize)

    if PyInfo.PY2:
        assert PyInfo.PY2 == True
        assert PyInfo.PY3 == False
        string_types = (unicode, str)
        text_type = unicode
        binary_type = str
        integer_types = (int, long)
        class_types = (type, types.ClassType)
        maxsize = sys.maxsize
        assert PyInfo.string_types == string_types
       

# Generated at 2022-06-14 06:38:20.962176
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True and PyInfo.PY3 is False
    assert isinstance("abc", PyInfo.string_types)
    assert isinstance("abc", PyInfo.text_type)
    assert isinstance("abc", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:33.870094
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert isinstance('str', PyInfo.string_types)
        assert 'str' == PyInfo.text_type
        assert isinstance(b'bytes', PyInfo.string_types)
        assert isinstance(b'bytes', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(int, PyInfo.class_types)
        assert isinstance(type(1), PyInfo.class_types)
    else:  # PY2
        assert isinstance('str', PyInfo.string_types)

# Generated at 2022-06-14 06:38:38.050124
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()

# Generated at 2022-06-14 06:38:47.472212
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py_info = PyInfo()

    assert(py_info.PY2)
    assert(not py_info.PY3)
    assert(py_info.string_types == (basestring,))
    assert(py_info.text_type == unicode)
    assert(py_info.binary_type == str)
    assert(py_info.integer_types == (int, long))
    assert(py_info.class_types == (type, types.ClassType))
    assert(py_info.maxsize == sys.maxsize)



# Generated at 2022-06-14 06:38:52.407908
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)


__all__ = ["PyInfo"]

# Generated at 2022-06-14 06:39:04.116719
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from slate.constants import pyinfo

    assert isinstance(pyinfo.PY2, bool)
    assert isinstance(pyinfo.PY3, bool)
    assert isinstance(pyinfo.string_types, tuple)
    for s in pyinfo.string_types:
        assert issubclass(s, basestring)
    assert isinstance(pyinfo.text_type, basestring)
    assert isinstance(pyinfo.binary_type, basestring)
    assert isinstance(pyinfo.integer_types, tuple)
    for s in pyinfo.integer_types:
        assert issubclass(s, (int, long))
    assert isinstance(pyinfo.class_types, tuple)
    for s in pyinfo.class_types:
        assert issubclass(s, (type, types.ClassType))


# Generated at 2022-06-14 06:39:17.330737
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance("", PyInfo.string_types)
        assert isinstance("", PyInfo.text_type)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(0, PyInfo.integer_types)
        assert isinstance(type, PyInfo.class_types)
    else:  # PY2
        assert isinstance("", PyInfo.string_types)
        assert isinstance(u"", PyInfo.text_type)
        assert isinstance("", PyInfo.binary_type)
        assert isinstance(0, PyInfo.integer_types)
        assert isinstance(type, PyInfo.class_types)
        assert isinstance(types.ClassType, PyInfo.class_types)

# Generated at 2022-06-14 06:39:26.295758
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    import types  # last as it is a Py2-only module

    class PY3(object):
        PY2 = False
        PY3 = True
        string_types = str,
        text_type = str
        binary_type = bytes
        integer_types = int,
        class_types = type,

        maxsize = sys.maxsize

    class PY2(object):
        PY2 = True
        PY3 = False
        string_types = basestring,
        text_type = unicode
        binary_type = str
        integer_types = (int, long)
        class_types = (type, types.ClassType)


# Generated at 2022-06-14 06:39:39.942142
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.binary_type)
    assert isinstance(3, PyInfo.integer_types)
    assert isinstance(3.4, float)


if __name__=="__main__":
    test_PyInfo()
    print("tests passed")

# Generated at 2022-06-14 06:39:45.081758
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.maxsize == maxsize


# Sample usage of class PyInfo

# Generated at 2022-06-14 06:39:46.991623
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

# Generated at 2022-06-14 06:39:59.096571
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3 is True

    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.string_types) is False

    assert isinstance(u"", PyInfo.text_type)
    assert isinstance(b"", PyInfo.text_type) is False

    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(b"", PyInfo.binary_type) is False

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.integer_types)

    assert isinstance

# Generated at 2022-06-14 06:40:03.255516
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)



# Generated at 2022-06-14 06:40:13.402514
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 ^ PyInfo.PY3
    assert isinstance('a', PyInfo.string_types)
    assert isinstance(b'a', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)
    if PyInfo.PY3:
        assert isinstance('a', PyInfo.text_type)
        assert not isinstance(b'a', PyInfo.text_type)
    else:
        assert isinstance(u'a', PyInfo.text_type)
        assert not isinstance('a', PyInfo.text_type)
    assert PyInfo.maxsize >= 2 ** 31 - 1
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:40:27.276220
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.string_types == (str, ) if PyInfo.PY3 else (basestring, )
    assert PyInfo.text_type == str if PyInfo.PY3 else unicode
    assert PyInfo.binary_type == bytes if PyInfo.PY3 else str
    assert PyInfo.integer_types == (int, ) if PyInfo.PY3 else (int, long)
    assert PyInfo.class_types == (type, ) if PyInfo.PY3 else (type, types.ClassType)

# Generated at 2022-06-14 06:40:36.976397
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from flashtext import KeywordProcessor

    # Default
    kp_default = KeywordProcessor(case_sensitive=False)
    kp_default.add_keyword("test")
    kp_default.add_keyword("test1")
    kp_default.add_keyword("test2")
    assert kp_default.extract_keywords("test", span_info=True) == [(0, 4)]
    assert kp_default.extract_keywords("test", include_overlapping_keywords=True, span_info=True) \
           == [(0, 4)]
    assert kp_default.extract_keywords("test", span_info=True, return_all=True) == [(0, 4)]

# Generated at 2022-06-14 06:40:43.065728
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    print(info.PY2)
    print(info.PY3)
    print(info.string_types)
    print(info.text_type)
    print(info.binary_type)
    print(info.maxsize)
    return True


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:46.531434
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert isinstance(PyInfo.string_types, tuple)



# Generated at 2022-06-14 06:41:17.540530
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # This is the unit test for constructor of class PyInfo

    pyinf = PyInfo()
    assert pyinf.PY2 is True or pyinf.PY2 is False
    assert pyinf.PY3 is True or pyinf.PY3 is False
    assert type(pyinf.string_types) is tuple
    assert type(pyinf.text_type) is str
    assert type(pyinf.binary_type) is str
    assert type(pyinf.integer_types) is tuple
    assert type(pyinf.class_types) is tuple
    assert type(pyinf.maxsize) is int or type(pyinf.maxsize) is long


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:41:18.791250
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:41:31.575764
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert not isinstance(b"", PyInfo.string_types)

    assert isinstance("", PyInfo.text_type)
    assert not isinstance(u"", PyInfo.text_type)
    assert not isinstance(b"", PyInfo.text_type)

    assert not isinstance("", PyInfo.binary_type)
    assert not isinstance(u"", PyInfo.binary_type)
    assert isinstance(b"", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:41:36.587709
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.integer_types == (int, long) if PyInfo.PY2 else (int,)
    assert PyInfo.string_types == (basestring,) if PyInfo.PY2 else (str,)
    print(PyInfo.maxsize)


test_PyInfo()

# Generated at 2022-06-14 06:41:40.741394
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.string_types is not None
    assert PyInfo.text_type is not None
    assert PyInfo.binary_type is not None
    assert PyInfo.class_types is not None


# Generated at 2022-06-14 06:41:48.987961
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def check(check_name):
        pni = PyInfo()
        assert isinstance(pni, PyInfo)
        assert isinstance(getattr(pni, check_name, None), bool)

    check('PY2')
    check('PY3')
    check('string_types')
    check('text_type')
    check('binary_type')
    check('integer_types')
    check('maxsize')


# this is the "pytest marker"
pytestmark = pytest.mark.support



# Generated at 2022-06-14 06:41:58.707389
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 is not pyinfo.PY3
    assert pyinfo.PY3 is sys.version_info[0] == 3


if PyInfo.PY2:

    # Python 2 support
    import futures
    import requests

    Future = futures.Future

    def urlopen(request):
        try:
            _r = requests.request(
                request.get_method(),
                request.get_full_url(),
                data=request.data,
                headers=request.headers,
            )
        except requests.RequestException as e:
            raise urllib2.HTTPError(
                e.response.url, e.response.status_code, e.response.reason, e.response.headers, None
            )
        else:
            return urllib2.add

# Generated at 2022-06-14 06:42:00.452448
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:42:08.485830
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from pyinfo.pyinfo import PyInfo

    py2 = PyInfo.PY2
    py3 = PyInfo.PY3

    if (py2) or (py3):
        version = sys.version_info
        if version[0] == 2:
            # Python 2
            assert (py2)
            assert (not py3)
        elif version[0] == 3:
            # Python 3
            assert (py3)
            assert (not py2)
        else:
            raise RuntimeError("Unknown Python version: %r" % sys.version)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:42:22.601121
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert len(PyInfo.string_types) == 1
        assert PyInfo.string_types[0] is str
        assert PyInfo.text_type is basestring
        assert PyInfo.binary_type is str
        assert len(PyInfo.integer_types) == 2
        assert PyInfo.integer_types[0] is int
        assert PyInfo.integer_types[1] is long
        assert len(PyInfo.class_types) == 2
        assert PyInfo.class_types[0] is type
        assert PyInfo.class_types[1] is types.ClassType
    else:
        assert len(PyInfo.string_types) == 1
        assert PyInfo.string_types[0] is str
        assert PyInfo.text_type is str
        assert PyInfo.binary_

# Generated at 2022-06-14 06:43:14.942430
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from nose.tools import eq_
    from nose.tools import ok_

    ok_(PyInfo.PY2 or PyInfo.PY3)

    eq_(PyInfo.string_types, str if PyInfo.PY3 else basestring)
    eq_(PyInfo.text_type, str if PyInfo.PY3 else unicode)
    eq_(PyInfo.binary_type, bytes if PyInfo.PY3 else str)
    eq_(PyInfo.integer_types, int if PyInfo.PY3 else tuple([int, long]))
    eq_(PyInfo.class_types, type if PyInfo.PY3 else tuple([type, types.ClassType]))


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:43:20.452267
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import unittest

    class TestPyInfo(unittest.TestCase):
        def test_PY2(self):
            import sys
            self.assertEqual(PyInfo.PY2, sys.version_info[0] == 2)

        def test_PY3(self):
            import sys
            self.assertEqual(PyInfo.PY3, sys.version_info[0] == 3)

        def test_string_types(self):
            self.assertTrue(isinstance(PyInfo.string_types, tuple))

        def test_text_type(self):
            self.assertTrue(isinstance(PyInfo.text_type, type))

        def test_binary_type(self):
            self.assertTrue(isinstance(PyInfo.binary_type, type))


# Generated at 2022-06-14 06:43:23.427437
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:43:25.720211
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.string_types or PyInfo.text_type or PyInfo.binary_type or PyInfo.integer_types

# Generated at 2022-06-14 06:43:36.124621
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print("--- In test_PyInfo() ---")
    print("PyInfo.PY2 = {}".format(PyInfo.PY2))
    print("PyInfo.PY3 = {}".format(PyInfo.PY3))
    print("PyInfo.string_types = {}".format(PyInfo.string_types))
    print("PyInfo.text_type = {}".format(PyInfo.text_type))
    print("PyInfo.binary_type = {}".format(PyInfo.binary_type))
    print("PyInfo.integer_types = {}".format(PyInfo.integer_types))
    print("PyInfo.class_types = {}".format(PyInfo.class_types))
    print("PyInfo.maxsize = {}".format(PyInfo.maxsize))



# Generated at 2022-06-14 06:43:47.777737
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.__name__, PyInfo.string_types)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)

    if PyInfo.PY2:
        assert isinstance(PyInfo.string_types[0], type)
        assert isinstance(PyInfo.text_type, types.ClassType)
        assert isinstance(PyInfo.binary_type, types.ClassType)
        assert isinstance(PyInfo.integer_types[0], types.ClassType)
        assert isinstance(PyInfo.integer_types[1], types.ClassType)
        assert isinstance(PyInfo.class_types[0], types.ClassType)
        assert isinstance(PyInfo.class_types[1], types.ClassType)

# Generated at 2022-06-14 06:43:57.570579
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance(PyInfo.string_types, tuple)
        assert isinstance(PyInfo.text_type, type)
        assert isinstance(PyInfo.binary_type, type)
        assert isinstance(PyInfo.integer_types, tuple)
        assert isinstance(PyInfo.class_types, tuple)
        assert isinstance(PyInfo.maxsize, int)
        assert PyInfo.string_types == (str, )
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int, )
        assert PyInfo.class_types == (type, )
        assert PyInfo.maxsize == sys.maxsize
    else:  # PY2
        assert isinstance(PyInfo.string_types, tuple)

# Generated at 2022-06-14 06:44:04.912939
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print(PyInfo.PY2)
    print(PyInfo.PY3)
    print(PyInfo.string_types)
    print(PyInfo.text_type)
    print(PyInfo.binary_type)
    print(PyInfo.integer_types)
    print(PyInfo.class_types)
    print(PyInfo.maxsize)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:44:07.653556
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (PyInfo.PY3 is False)
    assert PyInfo.PY3 == (PyInfo.PY2 is False)

# Generated at 2022-06-14 06:44:13.412702
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
    else:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)
        assert PyInfo.maxsize == sys.maxsize

