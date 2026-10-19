

# Generated at 2022-06-14 06:35:43.609095
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    >>> type(PyInfo.PY2)
    <class 'bool'>
    >>> PyInfo.binary_type is str
    False
    >>> PyInfo.binary_type is bytes
    True
    >>> PyInfo.string_types is tuple
    True
    >>> PyInfo.integer_types is tuple
    True
    """



# Generated at 2022-06-14 06:35:52.621300
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    if sys.platform.startswith("java"):
        assert PyInfo.maxsize == 2147483647
    else:
        assert PyInfo.maxsize == 9223372036854775807
    return



# Generated at 2022-06-14 06:35:56.838160
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
    print(type(PyInfo.maxsize))



# Generated at 2022-06-14 06:36:01.006587
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.class_types)



# Generated at 2022-06-14 06:36:11.145216
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert len(PyInfo.string_types) == 1
    assert len(PyInfo.text_type) == 1
    assert len(PyInfo.binary_type) == 1
    assert len(PyInfo.integer_types) == 1
    assert len(PyInfo.class_types) == 1
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert isinstance(u'', PyInfo.text_type)
    assert isinstance(b'', PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:18.958896
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("", PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)
    if PyInfo.PY2:
        assert isinstance(int, PyInfo.class_types)



# Generated at 2022-06-14 06:36:25.416033
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.integer_types[0], type)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.class_types[0], type)
    assert isinstance(PyInfo.maxsize, int)


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-14 06:36:26.708328
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True

# Generated at 2022-06-14 06:36:28.528478
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3

# Generated at 2022-06-14 06:36:32.933910
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize == 2 ** 63 - 1


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-14 06:36:39.414418
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Let's call the constructor just to make sure it doesn't throw.
    type(PyInfo())
    # Let's also check that it's a singleton.
    assert PyInfo() is PyInfo()

# Generated at 2022-06-14 06:36:42.010275
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

# Generated at 2022-06-14 06:36:55.368937
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import unittest

    class PyInfoTestCase(unittest.TestCase):
        def test_PY2(self):
            self.assertEqual(PyInfo.PY2, sys.version_info[0] == 2)

        def test_PY3(self):
            self.assertEqual(PyInfo.PY3, sys.version_info[0] == 3)

        if PyInfo.PY3:
            def test_string_types(self):
                self.assertEqual(PyInfo.string_types, (str,))

            def test_text_type(self):
                self.assertEqual(PyInfo.text_type, str)

            def test_binary_type(self):
                self.assertEqual(PyInfo.binary_type, bytes)


# Generated at 2022-06-14 06:37:09.051600
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY2 is False
    assert PyInfo.PY3 is True or PyInfo.PY3 is False
    assert PyInfo.PY3 != PyInfo.PY2

    assert isinstance('', PyInfo.string_types)
    for _bytes in (b'', bytes()):
        assert isinstance(_bytes, PyInfo.binary_type)
    for _str in ('', str()):
        assert isinstance(_str, PyInfo.text_type)
    assert isinstance(u'', PyInfo.text_type)
    assert isinstance(0, PyInfo.integer_types)
    assert not isinstance(0, PyInfo.class_types)


# Generated at 2022-06-14 06:37:13.115136
# Unit test for constructor of class PyInfo
def test_PyInfo():
    _ = PyInfo


if __name__ == "__main__":
    import sys

    print(sys.version)
    print(PyInfo.PY2)
    print(PyInfo.PY3)
    print(PyInfo.maxsize)

# Generated at 2022-06-14 06:37:14.454795
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3



# Generated at 2022-06-14 06:37:17.084666
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.PY2 ^ PyInfo.PY3

# Generated at 2022-06-14 06:37:23.690075
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """Testing constructor of PyInfo"""
    pyinfo = PyInfo()
    assert pyinfo.PY2 or pyinfo.PY3
    assert pyinfo.string_types
    assert pyinfo.text_type
    assert pyinfo.binary_type
    assert pyinfo.integer_types
    assert pyinfo.maxsize

# Generated at 2022-06-14 06:37:25.274420
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert not (PyInfo.PY2 and PyInfo.PY3)



# Generated at 2022-06-14 06:37:29.949152
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 in (True, False)
    assert PyInfo.PY3 in (True, False)

    assert PyInfo.string_types
    assert not PyInfo.text_type
    assert not PyInfo.binary_type
    assert not PyInfo.integer_types
    assert PyInfo.class_types
    assert not PyInfo.maxsize

# Generated at 2022-06-14 06:37:43.888609
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
    assert PyInfo.maxsize >= 0
    assert PyInfo.maxsize <= (1 << 63) - 1

# Generated at 2022-06-14 06:37:53.065184
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is False
    assert PyInfo.PY3 is True
    assert PyInfo.string_types is tuple
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type is str
    assert PyInfo.integer_types is tuple
    assert PyInfo.integer_types == (int,)
    assert PyInfo.class_types is tuple
    assert PyInfo.class_types == (type,)
    assert isinstance(PyInfo.maxsize, int)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:04.372330
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('text', PyInfo.string_types)
        assert not isinstance(b'binary', PyInfo.string_types)
        assert isinstance(b'\xff', PyInfo.binary_type)
        assert not isinstance('text', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(long(1), PyInfo.integer_types)
        assert isinstance(int, PyInfo.class_types)
        assert isinstance(type, PyInfo.class_types)
        assert PyInfo.maxsize == sys.maxint
    else:  # Python 3
        assert isinstance('text', PyInfo.string_types)
        assert not isinstance(b'binary', PyInfo.string_types)

# Generated at 2022-06-14 06:38:16.259053
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert len(PyInfo.string_types) == 1
    assert PyInfo.string_types[0] == str if PyInfo.PY3 else basestring
    assert PyInfo.text_type == str if PyInfo.PY3 else unicode
    assert PyInfo.binary_type
    assert PyInfo.binary_type in (str, bytes)
    assert PyInfo.integer_types
    assert len(PyInfo.integer_types) == 2
    assert PyInfo.integer_types[0] == int
    assert PyInfo.integer_types[1]

# Generated at 2022-06-14 06:38:20.673981
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test for string
    assert isinstance(PyInfo.string_types[0], type)
    assert not issubclass(PyInfo.string_types[0], object)
    # Test for text
    assert isinstance(PyInfo.text_type, type)
    assert not issubclass(PyInfo.text_type, object)
    # Test for binary_type
    assert isinstance(PyInfo.binary_type, type)
    assert not issubclass(PyInfo.binary_type, object)
    # Test for maxsize
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:38:33.618480
# Unit test for constructor of class PyInfo
def test_PyInfo():
    o = PyInfo()
    assert o.PY2 == (sys.version_info[0] == 2)
    assert o.PY3 == (sys.version_info[0] == 3)
    if sys.version_info[0] == 3:
        assert o.string_types == (str,)
        assert o.text_type == str
        assert o.binary_type == bytes
        assert o.integer_types == (int,)
        assert o.class_types == (type,)
        assert o.maxsize == sys.maxsize
    else:
        assert o.string_types == (basestring,)
        assert o.text_type == unicode
        assert o.binary_type == str
        assert o.integer_types == (int, long)

# Generated at 2022-06-14 06:38:40.600658
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import random
    from six import assertRaisesRegex

    x = PyInfo()

    # Test if PY2 or PY3 is set
    assert x.PY2 != x.PY3

    # Test that nothing is set twice
    assert x.PY2 == False or x.PY3 == False

    # Test that PY2 and PY3 are the opposite
    assert x.PY2 != x.PY3

    # test if maxsize is set correctly
    if x.PY2:
        assert x.maxsize == ((1 << 31) - 1)
    else:
        assert x.maxsize == ((1 << 63) - 1)


# Generated at 2022-06-14 06:38:53.755937
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('x', PyInfo.string_types)
        assert not isinstance('x', PyInfo.binary_type)
        assert isinstance(u'x', PyInfo.text_type)
        assert not isinstance(u'x', PyInfo.string_types)
        assert isinstance(1, PyInfo.integer_types)
        assert not isinstance(1, PyInfo.string_types)
        assert isinstance(int, PyInfo.class_types)
        assert not isinstance(int, PyInfo.string_types)
    else:  # PyInfo.PY3
        assert isinstance('x', PyInfo.string_types)
        assert not isinstance('x', PyInfo.binary_type)
        assert isinstance(b'x', PyInfo.binary_type)
       

# Generated at 2022-06-14 06:39:01.261279
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import platform

    if sys.version_info[0] == 2:
        assert PyInfo.PY2 is True
        assert PyInfo.PY3 is False
        assert PyInfo.maxsize == sys.maxint
        if sys.platform.startswith("java"):
            assert PyInfo.maxsize == 2 ** 31 - 1
        else:
            assert PyInfo.maxsize == 2 ** 63 - 1

        assert isinstance(3, PyInfo.integer_types)
        assert isinstance(u"test", PyInfo.string_types)
        if sys.platform.startswith("java"):
            assert isinstance(3, PyInfo.integer_types)
        else:
            assert isinstance(2 ** 33, PyInfo.integer_types)
        assert isinstance(u"test", PyInfo.string_types)
       

# Generated at 2022-06-14 06:39:04.911474
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """PyInfo is a meta-class for python version detection.
    """
    assert PyInfo.PY2
    assert not PyInfo.PY3
    print(PyInfo.__doc__)
    print(sys.version)

# Generated at 2022-06-14 06:39:21.866859
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.PY3 or type('') == str
    assert PyInfo.PY3 or type(u'') == unicode
    assert PyInfo.PY3 or type(b'') == str
    if PyInfo.PY3:
        assert type(u'') == str
        assert type(b'') == bytes
        assert type('') == str
        assert type(b'') == bytes


# Functions for python 2 to python 3

# Generated at 2022-06-14 06:39:25.533170
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py_info = PyInfo()
    assert py_info.binary_type == str
    assert py_info.string_types == (basestring,)
    assert py_info.text_type == unicode

# Generated at 2022-06-14 06:39:26.791194
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2



# Generated at 2022-06-14 06:39:36.285272
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(b"", PyInfo.string_types)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(u"", PyInfo.string_types)
        assert isinstance(u"", PyInfo.text_type)
        assert isinstance(0, PyInfo.integer_types)
        assert isinstance(0, PyInfo.integer_types)
        assert isinstance(int, PyInfo.class_types)

    if PyInfo.PY3:
        assert isinstance("", PyInfo.string_types)
        assert not isinstance("", PyInfo.binary_type)
        assert isinstance(b"", PyInfo.string_types)
        assert isinstance(b"", PyInfo.binary_type)

# Generated at 2022-06-14 06:39:39.279057
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print(PyInfo.PY2)
    print(PyInfo.PY3)
    print(PyInfo.string_types)


# Test
if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:39:53.102193
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3

    # See https://github.com/rasbt/one-python-ide/issues/60
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.string_types)

    assert isinstance("", PyInfo.text_type)
    assert isinstance(u"", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)

    assert not isinstance(u"", PyInfo.text_type)
    assert not isinstance(u"", PyInfo.binary_type)
    assert not isinstance(b"", PyInfo.text_type)
    assert not isinstance(b"", PyInfo.binary_type)


# Generated at 2022-06-14 06:39:53.888849
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert True



# Generated at 2022-06-14 06:39:56.779030
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo().PY2 == (sys.version_info[0] == 2)



# Generated at 2022-06-14 06:40:05.756863
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py2 = PyInfo.PY2
    py3 = PyInfo.PY3

    assert isinstance(py2, bool)
    assert isinstance(py3, bool)
    assert py2 != py3

    str_type = PyInfo.string_types
    assert isinstance(str_type, tuple)

    max_size = PyInfo.maxsize
    assert isinstance(max_size, int)
    assert max_size > 0


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:13.083903
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



# Generated at 2022-06-14 06:40:38.363334
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:40:41.830072
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if  PyInfo.PY2:
        assert(True)
        return
    assert(True)

if __name__ == "__main__":
    test_PyInfo()
    print("Test Successful!")

# Generated at 2022-06-14 06:40:50.504066
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

    if PyInfo.PY2:
        assert isinstance(PyInfo.maxsize, (int, long))
    else:
        assert isinstance(PyInfo.maxsize, int)

    assert PyInfo.maxsize >= 0



# Generated at 2022-06-14 06:40:58.766471
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Check that the PyInfo class has been created properly
    assert PyInfo.PY3 is True or PyInfo.PY2 is True

    # Check that all the attributes have been created properly
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:41:05.572690
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3
    assert PyInfo.PY2

    assert PyInfo.maxsize == sys.maxsize
    assert isinstance('', PyInfo.string_types)
    assert isinstance(b'', PyInfo.binary_type)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:41:18.846531
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is False
    assert PyInfo.PY3 is True
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes
    assert PyInfo.integer_types == (int,)
    assert PyInfo.class_types == (type,)
    assert PyInfo.maxsize == sys.maxsize


if __name__ == "__main__":
    param = 1
    if len(sys.argv) == 2:
        param = sys.argv.pop()
    if param == "1":
        # Unit test code
        test_PyInfo()
    else:
        # Interactive mode
        print(PyInfo.__doc__)
        sys.exit(-1)

# Generated at 2022-06-14 06:41:30.994231
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert not (PyInfo.PY2 and PyInfo.PY3)
    assert sys.maxsize == PyInfo.maxsize
    assert sys.maxsize == PyInfo.maxsize
    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)
    else:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:41:37.608556
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # type: () -> None
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(type(1), PyInfo.class_types)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:41:42.212051
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()

    for v in ('PY2', 'PY3', 'integer_types', 'class_types', 'string_types',
              'text_type', 'binary_type', 'maxsize'):
        assert hasattr(p, v)

# Generated at 2022-06-14 06:41:50.836643
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.text_type, type)
    if PyInfo.PY2:
        assert PyInfo.text_type == unicode
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)


text_type = PyInfo.text_type
binary_type = PyInfo.binary_type
integer_types = PyInfo.integer_types
maxsize = PyInfo.maxsize

if PyInfo.PY2:
    FileNotFoundError = IOError
else:
    FileNotFoundError = FileNotFoundError

# Generated at 2022-06-14 06:42:42.061565
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('', PyInfo.string_types)
        assert isinstance(u'', PyInfo.string_types)
        assert not isinstance(b'', PyInfo.string_types)
        assert isinstance('', PyInfo.text_type)
        assert not isinstance(u'', PyInfo.text_type)
        assert not isinstance(b'', PyInfo.text_type)
        assert isinstance(b'', PyInfo.binary_type)
        assert not isinstance('', PyInfo.binary_type)
        assert not isinstance(u'', PyInfo.binary_type)
        assert isinstance(123, PyInfo.integer_types)
        assert isinstance(123.45, PyInfo.integer_types)

# Generated at 2022-06-14 06:42:43.655331
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

# Generated at 2022-06-14 06:42:46.605495
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print(PyInfo.PY2)
    print(PyInfo.PY3)



# Generated at 2022-06-14 06:42:50.427381
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # sys.maxsize always has the same value as PyInfo.maxsize
    assert sys.maxsize == PyInfo.maxsize


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:43:02.934684
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert isinstance('a', PyInfo.string_types) is True
        assert isinstance('a', PyInfo.binary_type) is False
        assert isinstance('a', PyInfo.text_type) is True
        assert isinstance(5, PyInfo.integer_types) is True
        assert isinstance(5, PyInfo.class_types) is False

        assert isinstance('a', bytes) is False
        assert isinstance('a', str) is True

        assert isinstance(5, int) is True
        assert isinstance(5, type) is False

        assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:43:09.459319
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:43:15.911509
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)



# Generated at 2022-06-14 06:43:21.227005
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.string_types or PyInfo.text_type or PyInfo.binary_type or PyInfo.integer_types or PyInfo.class_types or PyInfo.maxsize

# Generated at 2022-06-14 06:43:29.500558
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert isinstance('a', PyInfo.string_types)
    assert isinstance(u'a', PyInfo.text_type)
    assert isinstance(b'a', PyInfo.binary_type)
    assert isinstance(23, PyInfo.integer_types)

# Generated at 2022-06-14 06:43:36.970703
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.text_type, type)

    if PyInfo.PY2:
        assert PyInfo.text_type == unicode
        assert PyInfo.maxsize == sys.maxsize  # int((1 << 31) - 1)
    else:
        assert PyInfo.text_type == str
        assert PyInfo.maxsize == sys.maxsize  # int((1 << 63) - 1)

# Generated at 2022-06-14 06:45:08.835513
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from pickle import dumps, loads
    from copy import deepcopy
    from io import BytesIO

    for i in range(1, 5):
        a = [PyInfo() for _ in range(i)]
        buf = BytesIO()
        dumps(a, buf)
        buf.seek(0, 0)
        b = loads(buf.read())

        assert(a == b)
        assert(deepcopy(a) == b)



# Generated at 2022-06-14 06:45:11.751560
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.text_type or PyInfo.binary_type
    assert PyInfo.string_types or PyInfo.integer_types



# Generated at 2022-06-14 06:45:25.967959
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert len(PyInfo.integer_types) == 2
    assert len(PyInfo.class_types) == 2
    if sys.platform.startswith("java"):
        # Jython always uses 32 bits.
        assert PyInfo.maxsize == int((1 << 31) - 1)
    else:
        # It's possible to have sizeof(long) != sizeof(Py_ssize_t).
        class X(object):
            def __len__(self):
                return 1 << 31

        try:
            len(X())
        except OverflowError:
            assert PyInfo.maxsize == int((1 << 31) - 1)
        else:
            assert PyInfo.maxsize == int((1 << 63) - 1)
        del X



# Generated at 2022-06-14 06:45:33.565936
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