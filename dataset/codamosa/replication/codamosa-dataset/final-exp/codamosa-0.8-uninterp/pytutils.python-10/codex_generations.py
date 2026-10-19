

# Generated at 2022-06-14 06:35:47.915873
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.string_types[0], tuple)
    assert isinstance(PyInfo.string_types[0][0], type)
    assert isinstance(PyInfo.string_types[0][1], type)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.integer_types[0], type)
    assert isinstance(PyInfo.integer_types[1], type)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.class_types[0], type)
    assert isinstance(PyInfo.class_types[1], type)
   

# Generated at 2022-06-14 06:36:01.691505
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('abc', PyInfo.string_types)
        assert not isinstance(b'abc', PyInfo.string_types)
        assert isinstance(u'abc', PyInfo.text_type)
        assert not isinstance(b'abc', PyInfo.binary_type)
        assert not isinstance(u'abc', PyInfo.binary_type)
    elif PyInfo.PY3:
        assert not isinstance('abc', PyInfo.string_types)
        assert isinstance(b'abc', PyInfo.string_types)
        assert not isinstance(u'abc', PyInfo.text_type)
        assert isinstance(b'abc', PyInfo.binary_type)
        assert isinstance(u'abc', PyInfo.binary_type)



# Generated at 2022-06-14 06:36:10.950565
# Unit test for constructor of class PyInfo
def test_PyInfo():

    info = PyInfo()

    assert info.PY2 == (sys.version_info[0] == 2)
    assert info.PY3 == (sys.version_info[0] == 3)

    if info.PY2:
        assert info.string_types == (basestring,)
        assert info.text_type == unicode
        assert info.binary_type == str
        assert info.integer_types == (int, long)
        assert info.class_types == (type, types.ClassType)
    else:
        assert info.string_types == (str,)
        assert info.text_type == str
        assert info.binary_type == bytes
        assert info.integer_types == (int,)
        assert info.class_types == (type,)

# Generated at 2022-06-14 06:36:22.975200
# Unit test for constructor of class PyInfo
def test_PyInfo():
    global pyinfo
    pyinfo = PyInfo()

    if pyinfo.PY2:
        assert isinstance('aa', pyinfo.string_types)
        assert isinstance(u'aa', pyinfo.text_type)
        assert isinstance(b'aa', pyinfo.binary_type)
        assert isinstance(1, pyinfo.integer_types)

        assert isinstance(list, pyinfo.class_types)

    if pyinfo.PY3:
        assert isinstance('aa', pyinfo.string_types)
        assert isinstance('aa', pyinfo.text_type)
        assert isinstance(b'aa', pyinfo.binary_type)
        assert isinstance(1, pyinfo.integer_types)

        assert isinstance(list, pyinfo.class_types)

# Generated at 2022-06-14 06:36:29.320896
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

# Generated at 2022-06-14 06:36:32.121612
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 + PyInfo.PY3 == 1


# ClassImporter is a class which helps import module and its class
# using the dot notation.

# Generated at 2022-06-14 06:36:42.511562
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py2 = PyInfo()
    assert py2.PY2 == True
    assert py2.PY3 == False
    assert py2.string_types == (basestring,)
    assert py2.text_type == unicode
    assert py2.binary_type == str
    assert py2.integer_types == (int, long)
    assert py2.class_types == (type, types.ClassType)
    py3 = PyInfo()
    assert py3.PY2 == False
    assert py3.PY3 == True
    assert py3.string_types == (str,)
    assert py3.text_type == str
    assert py3.binary_type == bytes
    assert py3.integer_types == (int,)
    assert py3.class_types == (type,)

# Generated at 2022-06-14 06:36:55.609650
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py2 = PyInfo()
    assert py2.PY2
    assert not py2.PY3
    assert py2.string_types == basestring
    assert py2.text_type == unicode
    assert py2.binary_type == str
    assert py2.integer_types == (int, long)
    assert py2.class_types == (type, types.ClassType)
    assert py2.maxsize == (1 << 63) - 1

    py3 = PyInfo()
    assert not py3.PY2
    assert py3.PY3
    assert py3.string_types == str
    assert py3.text_type == str
    assert py3.binary_type == bytes
    assert py3.integer_types == int
    assert py3.class_types == type

# Generated at 2022-06-14 06:36:57.192684
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert PyInfo.text_type == ''.__class__
    else:
        assert PyInfo.text_type == unicode



# Generated at 2022-06-14 06:36:58.638390
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:37:02.591560
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        print('runtime is Python 2')
    else:
        print('runtime is Python 3')


# test_PyInfo()

# Generated at 2022-06-14 06:37:13.885414
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.string_types[0], type)

    assert isinstance(PyInfo.text_type, type)

    assert isinstance(PyInfo.binary_type, type)

    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.integer_types[0], type)

    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.class_types[0], type)

    assert isinstance(PyInfo.maxsize, int)

    if PyInfo.PY3:
        assert PyInfo.text_type != PyInfo.binary_type
    else:
        assert PyInfo.text_type == PyInfo.binary

# Generated at 2022-06-14 06:37:22.206343
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2, "PY2 must be True"
    assert not PyInfo.PY3, "PY3 must be False"

    for t in [PyInfo.string_types, PyInfo.text_type, PyInfo.binary_type,
              PyInfo.integer_types, PyInfo.class_types, PyInfo.maxsize]:
        assert isinstance(t, (tuple, str)), "type must be tuple or str"


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 06:37:28.961830
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test exception
    try:
        import sys
        sys.modules['sys'].version_info = (3, 4)
        reload(PyInfo)
    except Exception as e:
        assert isinstance(e, AssertionError)

    try:
        import sys
        sys.modules['sys'].version_info = (2, 7)
        reload(PyInfo)
    except Exception as e:
        assert isinstance(e, AssertionError)

# Generated at 2022-06-14 06:37:40.560909
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if not PyInfo.PY2:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)

    else:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)



# Generated at 2022-06-14 06:37:47.162456
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('a', PyInfo.string_types)
    assert isinstance(u'a', PyInfo.string_types)
    assert isinstance(b'a', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:37:53.041415
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    py_info = PyInfo()
    assert py_info.PY2 == sys.version_info[0] == 2
    assert py_info.PY3 == sys.version_info[0] == 3
    assert py_info.maxsize == sys.maxsize
    """
    pass


py_info = PyInfo()

# Generated at 2022-06-14 06:38:04.095630
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    Verify that class PyInfo itself has valid values.
    """
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple) and len(PyInfo.string_types) == 1
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple) and len(PyInfo.integer_types) == 1
    assert isinstance(PyInfo.class_types, tuple) and len(PyInfo.class_types) == 1
    assert isinstance(PyInfo.maxsize, int) and PyInfo.maxsize >= 0


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:08.670053
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (3 == sys.version_info[0])
    assert PyInfo.PY2 == (2 == sys.version_info[0])


if __name__ == '__main__':
    sys.exit(
        unittest.main()
    )

# Generated at 2022-06-14 06:38:18.814887
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance("", PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)
    assert not isinstance(None, PyInfo.string_types)

    assert isinstance("", PyInfo.text_type)
    assert not isinstance(1, PyInfo.text_type)
    assert not isinstance(None, PyInfo.text_type)

    assert isinstance("", PyInfo.binary_type)
    assert not isinstance(1, PyInfo.binary_type)
    assert not isinstance(None, PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert not isinstance("", PyInfo.integer_types)
    assert not isinstance(None, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:34.866846
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not True
    assert PyInfo.PY2 is not False
    assert PyInfo.PY3 is not True
    assert PyInfo.PY3 is not False

    assert isinstance('', PyInfo.string_types)
    assert not isinstance(u'', PyInfo.string_types)

    assert isinstance('', PyInfo.binary_type)
    assert not isinstance(u'', PyInfo.binary_type)

    assert isinstance(u'', PyInfo.text_type)
    assert not isinstance('', PyInfo.text_type)

    assert isinstance(1, PyInfo.integer_types)
    assert not isinstance(1.1, PyInfo.integer_types)

    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:41.383343
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if not PyInfo.PY2:
        assert PyInfo.maxsize == sys.maxsize, "Maxsize value is not correct."
        assert PyInfo.string_types == (str,), "String types are not correct."
        assert PyInfo.text_type == str, "Text type is not correct."
        assert PyInfo.binary_type == bytes, "Binary type is not correct."
        assert PyInfo.integer_types == (int,), "Integer types are not correct."
        assert PyInfo.class_types == (type,), "Class types are not correct."
    else:
        assert PyInfo.maxsize == 2147483647, "Maxsize value is not correct."
        assert PyInfo.string_types == (basestring,), "String types are not correct."

# Generated at 2022-06-14 06:38:46.088718
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert 'long' in PyInfo.integer_types
    assert 32 < PyInfo.maxsize < sys.maxsize


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:38:57.202218
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is True or PyInfo.PY2 is True
    assert PyInfo.PY3 is False or PyInfo.PY2 is False
    assert PyInfo.PY2 is False or isinstance("Hello World", PyInfo.string_types)
    assert PyInfo.PY3 is False or isinstance("Hello World", PyInfo.string_types)
    assert PyInfo.PY2 is False or isinstance("Hello World".encode("utf8"), PyInfo.binary_type)
    assert PyInfo.PY3 is False or isinstance("Hello World".encode("utf8"), PyInfo.binary_type)
    assert PyInfo.PY2 is False or isinstance("Hello World".decode("utf8"), PyInfo.text_type)

# Generated at 2022-06-14 06:38:59.110936
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:39:07.566525
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == sys.version_info[0] == 2
    assert PyInfo.PY3 == sys.version_info[0] == 3

    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)

        assert PyInfo.maxsize == sys.maxsize
    else:  # PY2
        import types
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.t

# Generated at 2022-06-14 06:39:12.294254
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """Run when the program starts (module.py)"""
    i = PyInfo()
    if i.PY2:
        print("Python 2.x")
    elif i.PY3:
        print("Python 3.x")
    else:
        raise RuntimeError("Not Supported Python version")



# Generated at 2022-06-14 06:39:18.824038
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


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:39:31.042898
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from .pybase import type_assert
    from .utils import get_attrs

    info = PyInfo()
    assert isinstance(info, object)

# Generated at 2022-06-14 06:39:41.836887
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from six import PY2
    from six import PY3

    assert PyInfo.PY2 == PY2
    assert PyInfo.PY3 == PY3
    assert PyInfo.maxsize == maxsize

    if PY2:
        assert isinstance(u"", PyInfo.text_type)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:39:56.133564
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == True or PyInfo.PY3 == False
    assert PyInfo.PY2 == True or PyInfo.PY2 == False
    assert PyInfo.maxsize != None
    assert isinstance(PyInfo.maxsize, IntegerTypes)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.string_types, tuple)



# Generated at 2022-06-14 06:39:59.127687
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    for i, j in ((PyInfo.PY2, 2), (PyInfo.PY3, 3)):
        if i:
            assert sys.version_info[0] == j

# Generated at 2022-06-14 06:40:11.429371
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Check PY2 and PY3
    if PyInfo.PY2:
        assert sys.version_info[0] == 2
    else:
        assert sys.version_info[0] == 3

    # Check string_types
    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
    else:
        assert PyInfo.string_types == (str,)

    # Check text_type
    if PyInfo.PY2:
        assert PyInfo.text_type == unicode
    else:
        assert PyInfo.text_type == str

    # Check binary_type
    if PyInfo.PY2:
        assert PyInfo.binary_type == str
    else:
        assert PyInfo.binary_type == bytes

    # Check integer_types

# Generated at 2022-06-14 06:40:16.265313
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance('a', PyInfo.string_types)
    assert isinstance(u'a', PyInfo.string_types)
    assert isinstance(b'a', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.integer_types)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:40:20.663461
# Unit test for constructor of class PyInfo
def test_PyInfo():
    class Clazz(object):
        def __init__(self):
            self._clazz = "Clazz"

    clazz = Clazz()
    if PyInfo.PY3:
        assert clazz._clazz == "Clazz"
    else:
        assert clazz._Clazz__clazz == "Clazz"


# Use the PyInfo class to import the right module depending on the Python
# version

# Generated at 2022-06-14 06:40:24.914239
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p2 = PyInfo.PY2
    p3 = PyInfo.PY3
    assert not p2 or not p3
    assert p2 or p3

    st = type(PyInfo.string_types[0])
    assert st is str or st is unicode or st is basestring
    assert cmp(PyInfo.maxsize, (1 << 32) - 1) >= 0


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:37.290426
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is sys.version_info[0] == 2
    assert PyInfo.PY3 is sys.version_info[0] == 3

    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type is str
        assert PyInfo.binary_type is bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)

        assert isinstance('', PyInfo.string_types)
        assert isinstance(b'', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(type, PyInfo.class_types)
    else:  # PY2
        assert PyInfo.string_types == (basestring,)
        assert PyInfo

# Generated at 2022-06-14 06:40:43.384941
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert PyInfo.PY3
    assert isinstance("str", PyInfo.string_types)
    assert isinstance(u"unicode", PyInfo.string_types)
    assert isinstance("str", PyInfo.text_type)
    assert isinstance(b"bytes", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.class_types)
    assert isinstance(1, PyInfo.maxsize)

# Generated at 2022-06-14 06:40:54.913866
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.string_types == ((basestring,) if PyInfo.PY2 else (str,))
    assert PyInfo.text_type == (unicode if PyInfo.PY2 else str)
    assert PyInfo.binary_type == (str if PyInfo.PY2 else bytes)
    assert PyInfo.integer_types == ((int, long) if PyInfo.PY2 else (int,))
    assert PyInfo.class_types == ((type, types.ClassType) if PyInfo.PY2 else (type,))

# Generated at 2022-06-14 06:41:06.085302
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
    assert PyInfo.string_types == (str, ) if PyInfo.PY3 else (str, unicode)
    assert PyInfo.text_type == str if PyInfo.PY3 else unicode
    assert PyInfo.binary_type == bytes if PyInfo.PY3 else str

# Generated at 2022-06-14 06:41:31.046461
# Unit test for constructor of class PyInfo
def test_PyInfo():
    PyInfo()

    if PyInfo.PY2:
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance("", PyInfo.string_types)
        assert isinstance(u"", PyInfo.text_type)
    else:
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance("", PyInfo.string_types)
        assert isinstance(u"", PyInfo.string_types)

# Generated at 2022-06-14 06:41:42.026675
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('example', PyInfo.string_types)
        assert isinstance(u'example', PyInfo.text_type)
        assert isinstance(u'example'.encode('utf-8'), PyInfo.binary_type)
        assert isinstance(-1, PyInfo.integer_types)
        assert isinstance(int, PyInfo.class_types)
        assert PyInfo.maxsize == sys.maxsize
    else:  # PyInfo.PY3
        assert isinstance('example', PyInfo.string_types)
        assert isinstance('example', PyInfo.text_type)
        assert isinstance(b'example', PyInfo.binary_type)
        assert isinstance(-1, PyInfo.integer_types)
        assert isinstance(int, PyInfo.class_types)
       

# Generated at 2022-06-14 06:41:51.447244
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from MoreStringFunctions import py_info

    a = py_info()
    b = PyInfo()
    assert a.PY2 == b.PY2
    assert a.PY3 == b.PY3
    assert a.string_types == b.string_types
    assert a.text_type == b.text_type
    assert a.binary_type == b.binary_type
    assert a.integer_types == b.integer_types
    assert a.class_types == b.class_types
    assert a.maxsize == b.maxsize


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:42:04.852120
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('a', PyInfo.string_types)
        assert isinstance(u'a', PyInfo.string_types)
        assert isinstance(u'a', PyInfo.text_type)
        assert isinstance('a', PyInfo.binary_type)
        assert not isinstance(u'a', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(1, PyInfo.class_types)
        assert isinstance(PyInfo, PyInfo.class_types)
        assert isinstance(PyInfo.__name__, PyInfo.string_types)
    elif PyInfo.PY3:
        assert isinstance('a', PyInfo.string_types)

# Generated at 2022-06-14 06:42:17.054629
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # test maxsize
    try:
        PyInfo.maxsize + 1
    except OverflowError:
        pass
    else:
        raise AssertionError("maxsize should be 'maxsize of int'.")

    # test string_types
    assert isinstance('', PyInfo.string_types)
    if PyInfo.PY3:
        assert not isinstance(b'', PyInfo.string_types)
    else:
        assert isinstance(b'', PyInfo.string_types)

    # test integer_types
    assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:42:27.370255
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    assert pi.PY2 == (sys.version_info[0] == 2)
    assert pi.PY3 == (sys.version_info[0] == 3)

    assert isinstance('abc', pi.string_types)
    assert isinstance(u'abc', pi.string_types)
    assert not isinstance(object(), pi.string_types)

    if pi.PY2:
        assert type(pi.text_type()) == unicode
        assert pi.binary_type() == str
        assert isinstance(3, pi.integer_types)

# Generated at 2022-06-14 06:42:39.473855
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
    else:  # PyInfo.PY3
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:42:45.424120
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(classmethod, PyInfo.class_types)



# Generated at 2022-06-14 06:42:53.750594
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # type: () -> None
    """
    This is a unit test for constructor of class PyInfo.
    """
    print(PyInfo.PY2)
    print(PyInfo.PY3)
    print(PyInfo.string_types)
    print(PyInfo.text_type)
    print(PyInfo.binary_type)
    print(PyInfo.integer_types)
    print(PyInfo.class_types)
    print(PyInfo.maxsize)


# Unit test start
test_PyInfo()



# Generated at 2022-06-14 06:42:58.830342
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3
    assert sys.version_info[0] == 3

    assert PyInfo.PY2
    assert sys.version_info[0] == 2


if __name__ == '__main__':
    import pytest

    pytest.main(['--color'])

# Generated at 2022-06-14 06:43:46.390344
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("abc", PyInfo.string_types)
    assert isinstance(u"abc", PyInfo.string_types)
    assert not isinstance(b"abc", PyInfo.string_types)
    assert isinstance(100, PyInfo.integer_types)

# Generated at 2022-06-14 06:43:51.532169
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is False
    assert isinstance('hello', PyInfo.string_types)
    assert isinstance(u'hello', PyInfo.text_type)
    assert isinstance(b'hello', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:43:53.920794
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize > 0


if '__main__' == __name__:
    test_PyInfo()

# Generated at 2022-06-14 06:44:07.349742
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(u'', PyInfo.text_type)
        assert isinstance('', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance('', PyInfo.string_types)
        assert not isinstance(b'', PyInfo.string_types)
        assert isinstance(object, PyInfo.class_types)
    else:
        assert isinstance('', PyInfo.text_type)
        assert isinstance(b'', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance('', PyInfo.string_types)
        assert isinstance(b'', PyInfo.string_types)
        assert isinstance(object, PyInfo.class_types)

# Generated at 2022-06-14 06:44:08.936778
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    assert pyinfo.PyInfo.PY2 == (sys.version_info[0] == 2)
    assert pyinfo.PyInfo.PY3 == (sys.version_info[0] == 3)



# Generated at 2022-06-14 06:44:14.870436
# Unit test for constructor of class PyInfo
def test_PyInfo():
    a = PyInfo()
    for atr in dir(a):
        if not atr.startswith("__"):
            print("{}: {}".format(atr, getattr(a, atr)))


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:44:22.687450
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
    else:
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:44:27.233039
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert (1,) == PyInfo.string_types
    assert 'test' == PyInfo.text_type
    assert b'test' == PyInfo.binary_type
    assert (1,) == PyInfo.integer_types
    assert (int,) == PyInfo.class_types
    assert PyInfo.maxsize == 2 ** 32 - 1

# Generated at 2022-06-14 06:44:34.791089
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert (
        len(PyInfo.string_types) == 1
        and not PyInfo.string_types[0].__name__.endswith("str")
    )
    assert len(PyInfo.integer_types) in (1, 2) and not any(
        i.__name__.endswith("int") for i in PyInfo.integer_types
    )
    assert len(PyInfo.class_types) == 1
    assert not PyInfo.class_types[0].__name__.endswith("type")
    assert type(PyInfo.maxsize) == int

# Generated at 2022-06-14 06:44:38.052816
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()
    print(p.PY2, p.PY3)
    print(p.string_types, p.text_type, p.binary_type)
    print(p.integer_types, p.class_types)
    print(p.maxsize)

