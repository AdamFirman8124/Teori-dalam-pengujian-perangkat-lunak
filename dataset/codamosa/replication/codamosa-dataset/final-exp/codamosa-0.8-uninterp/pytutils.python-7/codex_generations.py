

# Generated at 2022-06-14 06:35:49.094943
# Unit test for constructor of class PyInfo
def test_PyInfo():
    PY2 = sys.version_info[0] == 2
    PY3 = sys.version_info[0] == 3

    assert PyInfo.PY2 == PY2
    assert PyInfo.PY3 == PY3

    if PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)
    else:  # PY2
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:36:01.208317
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert PyInfo.__dict__.get('PY4', None) is None

    if PyInfo.PY2:
        assert type(u'A') == PyInfo.text_type
        assert type(1) != PyInfo.text_type

# Generated at 2022-06-14 06:36:10.127946
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3

    if PyInfo.PY2:
        assert isinstance('', PyInfo.string_types)
        assert not isinstance(b'', PyInfo.string_types)
        assert type(1) in PyInfo.integer_types

# Generated at 2022-06-14 06:36:11.902560
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is not True
    assert PyInfo.PY2 is True



# Generated at 2022-06-14 06:36:24.215257
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def t(expected, actual):
        assert expected == actual, '\nExpected: %r\n  Actual: %r' % (expected, actual)

    if PyInfo.PY2:
        assert PyInfo.PY3 is False
    else:  # PY3
        assert PyInfo.PY2 is False

    t(True, PyInfo.string_types[0]('abc') == 'abc')
    t(True, PyInfo.text_type('abc') == 'abc')
    t(True, 'abc' == PyInfo.binary_type(b'abc'))
    t(True, 1 == PyInfo.integer_types[0]())
    t(True, 1 == PyInfo.maxsize)


# Run unit tests.
if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:36:35.468129
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('string', PyInfo.string_types)
        assert not isinstance(u'unicode-string', PyInfo.string_types)
        assert isinstance(u'unicode-string', PyInfo.text_type)
        assert isinstance(b'bytes-string', PyInfo.binary_type)
        assert not isinstance(b'bytes-string', PyInfo.text_type)
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:41.525815
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert hasattr(PyInfo, "string_types") and hasattr(PyInfo, "text_type") and hasattr(PyInfo, "binary_type") and hasattr(PyInfo, "integer_types") and hasattr(PyInfo, "maxsize") and hasattr(PyInfo, "class_types")

# Generated at 2022-06-14 06:36:49.150909
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("abc", PyInfo.string_types)
    assert isinstance("abc".encode("utf-8"), PyInfo.binary_type)
    assert isinstance(u"abc", PyInfo.text_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(len, PyInfo.class_types)

# Generated at 2022-06-14 06:36:57.374384
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert isinstance("abc", PyInfo.string_types) is True
    assert isinstance("abc", PyInfo.binary_type) is False
    assert isinstance("abc", PyInfo.text_type) is True
    assert isinstance(b"abc", PyInfo.binary_type) is True
    assert isinstance(b"abc", PyInfo.string_types) is True
    assert isinstance(b"abc", PyInfo.text_type) is False
    assert isinstance(1, PyInfo.integer_types) is True
    assert isinstance(1, int) is True
    assert isinstance(1, PyInfo.class_types) is False
    assert isinstance(int, PyInfo.class_types) is True

# Generated at 2022-06-14 06:37:11.018026
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # testing class initialization
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.maxsize == sys.maxsize

    assert PyInfo.string_types == (str, )
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes

    # testing string
    str1 = "abc"
    assert isinstance(str1, PyInfo.string_types)

    str2 = "你好欢迎来到中国！"
    assert isinstance(str2, PyInfo.string_types)

    # testing byte
    byte1 = b"abc"
    assert isinstance(byte1, PyInfo.binary_type)

# Generated at 2022-06-14 06:37:20.427403
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

# Generated at 2022-06-14 06:37:31.550441
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import platform

    assert not PyInfo.PY2 or PyInfo.PY3 == 0
    assert PyInfo.PY3 or PyInfo.PY2 == 0
    assert PyInfo.PY2 or not (PyInfo.string_types == (basestring,))
    assert PyInfo.PY3 or not (PyInfo.string_types == (str,))
    assert PyInfo.PY2 or not (PyInfo.text_type == unicode)
    assert PyInfo.PY3 or not (PyInfo.text_type == str)
    assert PyInfo.PY2 or not (PyInfo.binary_type == str)
    assert PyInfo.PY3 or not (PyInfo.binary_type == bytes)
    assert PyInfo.PY2 or not (PyInfo.integer_types == (int, long))
   

# Generated at 2022-06-14 06:37:32.736800
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3



# Generated at 2022-06-14 06:37:45.637720
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    assert isinstance(PyInfo.string_types, tuple)
    for x in PyInfo.string_types:
        assert isinstance(x, type)

    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)

    assert isinstance(PyInfo.integer_types, tuple)
    for x in PyInfo.integer_types:
        assert isinstance(x, type)

    assert isinstance(PyInfo.class_types, tuple)
    for x in PyInfo.class_types:
        assert isinstance(x, type)

    assert isinstance(PyInfo.maxsize, int)



# Generated at 2022-06-14 06:37:47.772696
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:37:58.415856
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # test string
    assert PyInfo.PY2 == True or PyInfo.PY2 == False
    assert PyInfo.PY3 == True or PyInfo.PY3 == False
    assert isinstance("test", PyInfo.string_types)
    assert isinstance("test", PyInfo.binary_type)
    assert isinstance("test", PyInfo.text_type)
    assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:04.626032
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    for item in PyInfo.string_types:
        assert isinstance("", item)
        assert not isinstance(b"", item)
    for item in PyInfo.binary_types:
        assert not isinstance("", item)
        assert isinstance(b"", item)
    for item in PyInfo.integer_types:
        assert isinstance(0, item)

# Generated at 2022-06-14 06:38:08.069424
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is False
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == int((1 << 31) - 1)

# Generated at 2022-06-14 06:38:12.067511
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import json
    info = json.dumps(dict(PyInfo.__dict__), indent=4)
    print(info)
    assert info


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:15.802305
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2
    assert not pyinfo.PY3


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("All tests passed")

# Generated at 2022-06-14 06:38:33.467193
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.PY2 == (sys.version_info[0] == 2)

    if PyInfo.PY2:
        import types
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
    elif PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)

# Generated at 2022-06-14 06:38:37.814561
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)


# No need to unit test this method

# Generated at 2022-06-14 06:38:45.653339
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert len(PyInfo.string_types) == 1
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert len(PyInfo.integer_types) == 2
    assert len(PyInfo.class_types) == 2
    assert PyInfo.maxsize == 9223372036854775807
    assert len(str(PyInfo.maxsize)) == 19

# Generated at 2022-06-14 06:38:54.152992
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert type("") == PyInfo.binary_type
    else:
        assert type("") == PyInfo.text_type

    if PyInfo.PY2:
        assert type("") == PyInfo.binary_type
    else:
        assert type(b"") == PyInfo.binary_type

    if PyInfo.PY2:
        assert type(1) == PyInfo.integer_types
    else:
        assert type(1) == PyInfo.integer_types

    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:39:04.608973
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is (True if sys.version_info[0] == 2 else False)
    assert PyInfo.PY3 is (True if sys.version_info[0] == 3 else False)
    assert PyInfo.maxsize is sys.maxsize if PyInfo.PY3 else (
        int((1 << 31) - 1) if sys.platform.startswith("java") else int((1 << 63) - 1))
    assert type(PyInfo.string_types) is tuple
    assert type(PyInfo.text_type) is type
    assert type(PyInfo.binary_type) is type
    assert type(PyInfo.integer_types) is tuple
    assert type(PyInfo.class_types) is tuple

# Generated at 2022-06-14 06:39:18.244664
# Unit test for constructor of class PyInfo
def test_PyInfo():
    try:
        x = PyInfo()
    except Exception:
        print("Constructor of class PyInfo failed")
        assert False


# Generated at 2022-06-14 06:39:26.811298
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.string_types, tuple)
    assert len(PyInfo.string_types) == 1
    assert isinstance(PyInfo.string_types[0], type)

    assert isinstance(PyInfo.text_type, type)

    assert isinstance(PyInfo.binary_type, type)

    assert isinstance(PyInfo.integer_types, tuple)
    assert len(PyInfo.integer_types) == 2
    assert isinstance(PyInfo.integer_types[0], type)
    assert isinstance(PyInfo.integer_types[1], type)

    assert isinstance(PyInfo.class_types, tuple)
    assert len(PyInfo.class_types) == 2
    assert isinstance(PyInfo.class_types[0], type)

# Generated at 2022-06-14 06:39:31.271116
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert sys.version_info[0] == 2 or sys.version_info[0] == 3
    assert sys.version_info[0] == PyInfo.PY2 + PyInfo.PY3

test_PyInfo()

# Generated at 2022-06-14 06:39:35.351476
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is not PyInfo.PY2
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1.0, PyInfo.integer_types) is False
    assert isinstance('1', PyInfo.string_types)
    assert isinstance(u'1', PyInfo.string_types)

# Generated at 2022-06-14 06:39:40.626159
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is False
    assert PyInfo.PY2 is True
    assert PyInfo.string_types == (str, unicode)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)



# Generated at 2022-06-14 06:39:58.718619
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)
    assert isinstance(PyInfo, PyInfo.class_types)
    assert isinstance(object, PyInfo.class_types)
    assert isinstance(map, types.BuiltinFunctionType)
    assert isinstance(map, PyInfo.class_types)
    assert isinstance(object, PyInfo.class_types)
    assert isinstance(test_PyInfo, types.FunctionType)
    assert isinstance(test_PyInfo, PyInfo.class_types)

# Generated at 2022-06-14 06:40:04.082329
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert type(PyInfo.text_type()) == PyInfo.text_type
    assert type(PyInfo.binary_type()) == PyInfo.binary_type
    assert type(PyInfo.maxsize) == int

# Generated at 2022-06-14 06:40:09.692130
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not None
    assert PyInfo.PY3 is not None

    assert PyInfo.string_types is not None
    assert PyInfo.text_type is not None
    assert PyInfo.integer_types is not None
    assert PyInfo.class_types is not None

    assert PyInfo.maxsize is not None


# end of file

# Generated at 2022-06-14 06:40:15.015705
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert type(PyInfo.maxsize) is int
    assert type(PyInfo.string_types) is tuple
    assert type(PyInfo.text_type) is type
    assert type(PyInfo.binary_type) is type
    assert type(PyInfo.integer_types) is tuple
    assert type(PyInfo.class_types) is tuple

# Generated at 2022-06-14 06:40:23.207201
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(6, PyInfo.integer_types)
    assert isinstance(object, PyInfo.class_types)
    assert isinstance(type, PyInfo.class_types)


# Don't need to import PyInfo
if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:28.409963
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert type("") in PyInfo.string_types
    assert isinstance("", PyInfo.text_type)
    assert isinstance("", PyInfo.binary_type)
    assert type(0) in PyInfo.integer_types

# Generated at 2022-06-14 06:40:30.643051
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert PyInfo.maxsize > 0



# Generated at 2022-06-14 06:40:43.896106
# Unit test for constructor of class PyInfo
def test_PyInfo():

    if PyInfo.PY2:
        assert isinstance("", PyInfo.string_types)
        assert not isinstance(b"", PyInfo.string_types)
        assert isinstance(u"", PyInfo.string_types)

        assert isinstance(u"", PyInfo.text_type)
        assert not isinstance(b"", PyInfo.text_type)

        assert isinstance(b"", PyInfo.binary_type)
        assert not isinstance(u"", PyInfo.binary_type)

        assert isinstance(1, PyInfo.integer_types)
        assert not isinstance(1.0, PyInfo.integer_types)

        assert isinstance(int, PyInfo.class_types)
        assert not isinstance(1, PyInfo.class_types)


# Generated at 2022-06-14 06:40:56.174294
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("", PyInfo.binary_type)

    assert isinstance(b"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

    assert not isinstance(1, PyInfo.string_types)
    assert not isinstance(1, PyInfo.text_type)
    assert not isinstance(1, PyInfo.binary_type)

    assert not isinstance("", PyInfo.integer_types)
    assert not isinstance("", PyInfo.class_types)

# Generated at 2022-06-14 06:41:04.073319
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    assert isinstance(PyInfo.string_types, tuple)
    for item in PyInfo.string_types:
        assert isinstance(item, type)

    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)

    assert isinstance(PyInfo.integer_types, tuple)
    for item in PyInfo.integer_types:
        assert isinstance(item, type)

    assert isinstance(PyInfo.class_types, tuple)
    for item in PyInfo.class_types:
        assert isinstance(item, type)

    assert isinstance(PyInfo.maxsize, int)


if __name__ == '__main__':
    test

# Generated at 2022-06-14 06:41:28.749605
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3, "Unsupported python version detected"

    assert isinstance('a', PyInfo.string_types)
    assert isinstance(b'a', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:41:40.042826
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from datetime import datetime
    from nose.tools import eq_

    class Test:
        pass

    tests = [
        PyInfo.PY2,
        PyInfo.PY3,
        PyInfo.string_types,
        PyInfo.text_type,
        PyInfo.binary_type,
        PyInfo.integer_types,
        PyInfo.class_types,
        PyInfo.maxsize,
    ]
    if PyInfo.PY2:
        eq_(tests, [
            True,
            False,
            (basestring, ),
            unicode,
            str,
            (int, long),
            (type, types.ClassType),
            9223372036854775807,
        ])

# Generated at 2022-06-14 06:41:46.087620
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert isinstance(b'', PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:41:53.440552
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    assert pi.PY2 != pi.PY3
    assert type(pi.string_types) == tuple
    assert type(pi.text_type) == type
    assert type(pi.binary_type) == type
    assert type(pi.maxsize) == int
    assert type(pi.integer_types) == tuple
    assert type(pi.class_types) == tuple



# Generated at 2022-06-14 06:42:06.649461
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py_info = PyInfo()
    print("python version: %s" % sys.version)
    if py_info.PY2:
        print("It is PY2")
    else:
        print("It is PY3")

    if isinstance("", py_info.string_types):
        print("It True")
    else:
        print("It false")

    if isinstance("", py_info.text_type):
        print("It True")
    else:
        print("It false")

    if isinstance(b"", py_info.binary_type):
        print("It True")
    else:
        print("It false")

    if isinstance(10, py_info.integer_types):
        print("It True")
    else:
        print("It false")


# Generated at 2022-06-14 06:42:14.687429
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)
    assert isinstance('', PyInfo.text_type)
    assert not isinstance(1, PyInfo.text_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:42:26.220115
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # The constructor of class PyInfo is empty
    pyinfo = PyInfo()

    # Verify string_types
    assert isinstance(pyinfo.string_types, types.TupleType)
    assert hasattr(pyinfo.string_types, '__contains__')

    # Verify text_type
    assert isinstance(pyinfo.text_type, types.TypeType)
    assert hasattr(pyinfo.text_type, '__contains__')

    # Verify binary_type
    assert isinstance(pyinfo.binary_type, types.TypeType)
    assert hasattr(pyinfo.binary_type, '__contains__')

    # Verify integer_types
    assert isinstance(pyinfo.integer_types, types.TupleType)
    assert hasattr(pyinfo.integer_types, '__contains__')

    #

# Generated at 2022-06-14 06:42:40.082628
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)
        assert PyInfo.maxsize == sys.maxsize
    else:  # PY2
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:42:46.094332
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    assert info.PY2 == (sys.version_info[0] == 2)
    assert info.PY3 == (sys.version_info[0] == 3)
    assert isinstance(info.string_types, tuple)
    assert isinstance(info.text_type, type)
    assert isinstance(info.binary_type, type)
    assert isinstance(info.integer_types, tuple)
    assert isinstance(info.class_types, tuple)
    assert isinstance(info.maxsize, int)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:42:55.155610
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(getattr(PyInfo, 'PY2'), bool)
    assert isinstance(getattr(PyInfo, 'PY3'), bool)
    assert isinstance(getattr(PyInfo, 'string_types'), tuple)
    assert isinstance(getattr(PyInfo, 'text_type'), type)
    assert isinstance(getattr(PyInfo, 'binary_type'), type)
    assert isinstance(getattr(PyInfo, 'integer_types'), tuple)
    assert isinstance(getattr(PyInfo, 'class_types'), tuple)
    assert isinstance(getattr(PyInfo, 'maxsize'), int)

# Generated at 2022-06-14 06:43:47.481742
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def assert_same_type(type1, type2):
        assert type1 is type2

    assert_same_type(str, PyInfo.string_types[0])
    assert_same_type(str, PyInfo.text_type)
    assert_same_type(bytes, PyInfo.binary_type)
    assert_same_type(int, PyInfo.integer_types[0])
    assert_same_type(type, PyInfo.class_types[0])

    # Maxsize
    if sys.version_info[0] == 2:
        if sys.platform.startswith("java"):
            assert PyInfo.maxsize == 2147483647
        else:
            assert PyInfo.maxsize == 9223372036854775807
    else:
        assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:43:52.045602
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 and not PyInfo.PY2
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes
    assert PyInfo.integer_types == (int,)
    assert PyInfo.class_types == (type,)
    assert PyInfo.maxsize == sys.maxsize


if __name__ == "__main__":
    test_PyInfo()
    print("Everything passed")

# Generated at 2022-06-14 06:44:04.126676
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == ((1 << 63) - 1)

    # py3_env_setup
    sys.version_info = (3, 0, 0)
    reload(PyInfo)
    assert not PyInfo.PY2
    assert PyInfo.PY3
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes
    assert PyInfo.integer_

# Generated at 2022-06-14 06:44:12.109559
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance("", PyInfo.binary_type)
        assert not isinstance("", PyInfo.string_types)

        assert isinstance(b"", PyInfo.string_types)
        assert isinstance(b"", PyInfo.binary_type)

        assert isinstance(b"".decode("utf8"), PyInfo.text_type)
        assert not isinstance(b"".decode("utf8"), PyInfo.string_types)
    else:  # PY2
        assert isinstance("", PyInfo.string_types)
        assert not isinstance("", PyInfo.binary_type)

        assert isinstance(u"", PyInfo.text_type)
        assert not isinstance(u"", PyInfo.string_types)


# Generated at 2022-06-14 06:44:24.439615
# Unit test for constructor of class PyInfo
def test_PyInfo():
    with pytest.raises(TypeError):
        PyInfo()


# Test cases for class PyInfo

# Generated at 2022-06-14 06:44:30.039567
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 + PyInfo.PY3 == 1
    print(PyInfo.maxsize)


if __name__ == "__main__":
    # test_PyInfo()
    print("unittest done!")

# Generated at 2022-06-14 06:44:41.322115
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py = PyInfo()

    assert py.PY2 == sys.version_info[0] == 2
    assert py.PY3 == sys.version_info[0] == 3

    if py.PY2:
        assert isinstance(py.string_types[0], basestring)
        assert py.string_types == (basestring,)
        assert py.text_type == unicode
        assert isinstance(py.binary_type, str)
        assert isinstance(py.integer_types[0], int)
        # end if
    else:
        assert isinstance(py.string_types[0], str)
        assert py.string_types == (str,)
        assert isinstance(py.text_type, types.BuiltinFunctionType)
        assert isinstance(py.binary_type, bytes)

# Generated at 2022-06-14 06:44:48.567435
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2
    assert not pyinfo.PY3
    assert pyinfo.string_types == (basestring,)
    assert pyinfo.text_type == unicode
    assert pyinfo.binary_type == str
    assert pyinfo.integer_types == (int, long)
    assert pyinfo.class_types == (type, types.ClassType)
    assert pyinfo.maxsize == (1 << 31) - 1



# Generated at 2022-06-14 06:44:51.042192
# Unit test for constructor of class PyInfo
def test_PyInfo():
    a = '__main__'
    assert a in sys.modules


test_PyInfo()

# Generated at 2022-06-14 06:45:03.162712
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

    assert len(PyInfo.string_types) == 1
    assert len(PyInfo.integer_types) == 2
    assert len(PyInfo.class_types) == 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()