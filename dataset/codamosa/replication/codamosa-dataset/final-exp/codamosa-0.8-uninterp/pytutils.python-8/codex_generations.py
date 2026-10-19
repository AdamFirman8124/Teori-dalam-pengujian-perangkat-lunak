

# Generated at 2022-06-14 06:35:49.454324
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Check that the global variable PY2 is True
    assert PyInfo.PY2

    # Check that the global variable PY3 is False
    assert not PyInfo.PY3

    # Check that the global variable string_types is a tuple and contains only
    # one element. The element should be a string type
    assert type(PyInfo.string_types) == tuple
    assert len(PyInfo.string_types) == 1
    assert type(PyInfo.string_types[0]) == str

    # Check that the global variable text_type is a string
    assert type(PyInfo.text_type) == str

    # Check that the global variable binary_type is a string
    assert type(PyInfo.binary_type) == str

    # Check that the global variable integer_types is a tuple and contains only
    # two elements. The elements

# Generated at 2022-06-14 06:35:53.588773
# Unit test for constructor of class PyInfo
def test_PyInfo():
    for attr in 'PY2 PY3 string_types binary_type text_type integer_types class_types'.split():
        assert getattr(PyInfo, attr, None) is not None



# Generated at 2022-06-14 06:36:00.228020
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(PyInfo, PyInfo.class_types)


if __name__ == "__main__":
    test_PyInfo()
    print("All done!")

# Generated at 2022-06-14 06:36:05.335088
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo, object)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:36:13.043476
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert type(PyInfo.PY2) == bool
    assert type(PyInfo.PY3) == bool
    assert type(PyInfo.string_types) == tuple
    assert type(PyInfo.text_type) == type
    assert type(PyInfo.binary_type) == type
    assert type(PyInfo.integer_types) == tuple
    assert type(PyInfo.class_types) == tuple
    assert type(PyInfo.maxsize) == int

# Generated at 2022-06-14 06:36:25.057760
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.PY2 != PyInfo.PY3
    import types
    assert PyInfo.class_types is not None

    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
        assert PyInfo.maxsize == sys.maxsize  # int(9223372036854775807)
    else:
        assert PyInfo.string_

# Generated at 2022-06-14 06:36:32.748041
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

# Generated at 2022-06-14 06:36:42.999861
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    if PyInfo.PY3:
        assert PyInfo.maxsize == sys.maxsize
    else:
        if sys.platform.startswith("java"):
            assert PyInfo.maxsize == int((1 << 31) - 1)
        else:
            class X(object):

                def __len__(self):
                    return 1 << 31

            try:
                len(X())
            except OverflowError:
                # 32-bit
                assert PyInfo.maxsize == int((1 << 31) - 1)
            else:
                # 64-bit
                assert PyInfo.maxsize == int((1 << 63) - 1)
           

# Generated at 2022-06-14 06:36:51.227342
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True


if PyInfo.PY3:
    def iteritems(dictionary, **kwargs):
        return iter(dictionary.items(**kwargs))
else:
    def iteritems(dictionary, **kwargs):
        return dictionary.iteritems(**kwargs)


if PyInfo.PY3:
    import urllib.parse as urlparse
else:
    import urlparse



# Generated at 2022-06-14 06:36:55.852848
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('', PyInfo.text_type)
    else:
        assert isinstance('', PyInfo.string_types)


# PyLint does not like isinstance() built-in function
# pylint: disable=E0123, C0121



# Generated at 2022-06-14 06:37:11.933005
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('', PyInfo.string_types)
        assert not isinstance(b'', PyInfo.string_types)
        assert isinstance(u'', PyInfo.text_type)
        assert not isinstance('', PyInfo.text_type)
        assert isinstance(b'', PyInfo.binary_type)
        assert not isinstance('', PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert not isinstance(1.1, PyInfo.integer_types)
        assert isinstance(int, PyInfo.class_types)
        assert isinstance(type, PyInfo.class_types)
    else:
        assert isinstance('', PyInfo.string_types)
        assert isinstance(b'', PyInfo.string_types)

# Generated at 2022-06-14 06:37:23.041107
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test case for public attributes
    pyinfo = PyInfo()
    assert pyinfo.PY2 is True or pyinfo.PY2 is False
    assert pyinfo.PY3 is True or pyinfo.PY3 is False
    assert isinstance(pyinfo.string_types, tuple)
    assert isinstance(pyinfo.text_type, type)
    assert isinstance(pyinfo.binary_type, type)
    assert isinstance(pyinfo.integer_types, tuple)
    assert isinstance(pyinfo.class_types, tuple)
    assert isinstance(pyinfo.maxsize, int)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:37:33.307513
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (2 == sys.version_info[0])
    assert PyInfo.PY3 == (3 == sys.version_info[0])

    if PyInfo.PY3:
        assert isinstance('', PyInfo.string_types)
        assert isinstance(b'', PyInfo.binary_type)
        assert isinstance(123, PyInfo.integer_types)
        assert isinstance(type, PyInfo.class_types)
        assert isinstance(type(''), PyInfo.class_types)
    else:
        assert isinstance(u'', PyInfo.string_types)
        assert isinstance('', PyInfo.binary_type)

# Generated at 2022-06-14 06:37:43.450346
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


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:37:56.304837
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('hello', PyInfo.string_types)
        assert not isinstance(b'hello', PyInfo.string_types)
        assert isinstance(u'hello', PyInfo.text_type)
        assert isinstance(1, PyInfo.integer_types)

        assert not isinstance(1, PyInfo.class_types)
        assert isinstance(int, PyInfo.class_types)

        assert type(1) is PyInfo.integer_types[0]
    else:
        assert isinstance('hello', PyInfo.string_types)
        assert isinstance(b'hello', PyInfo.string_types)
        assert isinstance(u'hello', PyInfo.text_type)
        assert isinstance(1, PyInfo.integer_types)


# Generated at 2022-06-14 06:38:03.746198
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyi = PyInfo()
    assert isinstance(pyi.string_types, tuple)


# Current file directory
d = os.path.dirname(__file__)

# Add current file directory to python import path
if d not in sys.path:
    sys.path.append(d)

# Add root project directory to python import path
if d not in sys.path:
    sys.path.append(os.path.abspath(os.path.join(d, '..')))

# Generated at 2022-06-14 06:38:13.514001
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.integer_types[0], type)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.class_types[0], type)
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

# Generated at 2022-06-14 06:38:17.801611
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.PY2 == (sys.version_info[0] == 2)



# Generated at 2022-06-14 06:38:25.974347
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo, object)
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)



# Generated at 2022-06-14 06:38:33.517041
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    if info.PY3:
        assert isinstance("3", info.string_types)
        assert isinstance(u"3", info.text_type)
        assert isinstance(b"3", info.binary_type)
    else:
        assert isinstance("3", info.string_types)
        assert isinstance(u"3", info.text_type)
        assert isinstance(b"3", info.binary_type)



# Generated at 2022-06-14 06:38:50.062386
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert issubclass(PyInfo.string_types, tuple)
    assert isinstance('', PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)
    assert issubclass(PyInfo.text_type, str)
    assert isinstance('', PyInfo.text_type)
    assert not isinstance(1, PyInfo.text_type)
    assert issubclass(PyInfo.binary_type, str)
    assert isinstance(b'', PyInfo.binary_type)
    assert not isinstance(1, PyInfo.binary_type)
    assert issubclass(PyInfo.integer_types, tuple)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:59.317296
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert int in PyInfo.integer_types
    assert long in PyInfo.integer_types
    assert not (bytes in PyInfo.integer_types)
    assert str in PyInfo.string_types
    assert unicode in PyInfo.string_types
    assert not (bytes in PyInfo.string_types)
    assert "maxsize: " + str(PyInfo.maxsize)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:39:02.413376
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.maxsize < PyInfo.maxsize + 1


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:39:09.643044
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys

    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    assert isinstance('', PyInfo.string_types)
    assert not isinstance(b'', PyInfo.string_types)

    assert isinstance('', PyInfo.text_type)
    assert not isinstance(b'', PyInfo.text_type)

    assert isinstance(b'', PyInfo.binary_type)
    assert not isinstance('', PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert not isinstance(1.1, PyInfo.integer_types)

    assert isinstance(sys, PyInfo.class_types)

# Generated at 2022-06-14 06:39:19.025885
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 or PyInfo.PY2
    assert isinstance('a', PyInfo.string_types)
    assert isinstance(u'a', PyInfo.string_types)

    if not PyInfo.PY3:
        assert isinstance('a', PyInfo.text_type)
    if not PyInfo.PY2:
        assert isinstance(b'a', PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:39:25.428623
# Unit test for constructor of class PyInfo

# Generated at 2022-06-14 06:39:34.414429
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("ABC", PyInfo.string_types)
    assert isinstance(None, PyInfo.string_types) is False
    assert isinstance("ABC", PyInfo.binary_type) is False
    assert isinstance("ABC".encode("UTF-8"), PyInfo.binary_type)
    assert isinstance(123, PyInfo.integer_types)
    assert isinstance(None, PyInfo.integer_types) is False
    assert isinstance(type, PyInfo.class_types)
    assert isinstance(None, PyInfo.class_types) is False
    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:39:45.935493
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test if correct version has been imported
    if sys.version_info[0] == 2:
        assert PyInfo.PY2 is True
        assert PyInfo.PY3 is False
    else:
        assert PyInfo.PY2 is False
        assert PyInfo.PY3 is True

    # Test if correct types are imported
    if sys.version_info[0] == 2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
    else:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)

# Generated at 2022-06-14 06:39:56.210564
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    def assert_type(pytype, py2type, py3type):
        assert pytype == py2type if PyInfo.PY2 else py3type

    assert_type(PyInfo.string_types, basestring, str)
    assert_type(PyInfo.text_type, unicode, str)
    assert_type(PyInfo.binary_type, str, bytes)
    assert_type(PyInfo.integer_types, (int, long), int)
    assert_type(PyInfo.class_types, (type, types.ClassType), type)

    assert PyInfo.maxsize is not None

# Generated at 2022-06-14 06:40:01.326356
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    Unit test for constructor of class PyInfo
    """
    assert PyInfo().PY2 == True or PyInfo().PY2 == False
    assert PyInfo().PY3 == True or PyInfo().PY3 == False
    assert isinstance(PyInfo().string_types, tuple)
    assert isinstance(PyInfo().text_type, str)
    assert isinstance(PyInfo().binary_type, str) or isinstance(
        PyInfo().binary_type, tuple)
    assert isinstance(PyInfo().class_types, tuple)
    assert isinstance(PyInfo().maxsize, int)
    return True



# Generated at 2022-06-14 06:40:15.052112
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import platform

    assert PyInfo.PY2 == (platform.python_version_tuple()[0] == '2')
    assert PyInfo.PY3 == (platform.python_version_tuple()[0] == '3')


# Assert that PY2 and PY3 are both logically True

# Generated at 2022-06-14 06:40:22.237419
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is True
    assert PyInfo.PY2 is False

    assert PyInfo.string_types == (str, )
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes
    assert PyInfo.integer_types == (int, )
    assert PyInfo.class_types == (type, )

    assert PyInfo.maxsize == (1 << 31) - 1

# Generated at 2022-06-14 06:40:24.059460
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert(PyInfo.PY3 == False)
    elif PyInfo.PY3:
        assert(PyInfo.PY2 == False)

# Generated at 2022-06-14 06:40:36.835962
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Check whether the version number is correctly detected or not
    assert (PyInfo.PY2 or PyInfo.PY3)

    # Check whether the class object is correctly detected or not
    assert (PyInfo.PY2 and issubclass(types.ClassType, object)) or (not PyInfo.PY2 and issubclass(type, object))

    # Check the string type
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)

    # Check the text type
    assert isinstance('', PyInfo.text_type)
    assert not isinstance(u'', PyInfo.text_type)

    # Check the binary type
    assert isinstance('', PyInfo.binary_type)
    assert isinstance(u'', PyInfo.binary_type)

    # Check

# Generated at 2022-06-14 06:40:45.457097
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.maxsize == sys.maxsize
    else:
        assert PyInfo.string_types == str
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == int
        assert PyInfo.maxsize == sys.maxsize



# Generated at 2022-06-14 06:40:55.361444
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print("Py2: {}, Py3: {}, maxsize: {}".format(PyInfo.PY2, PyInfo.PY3, PyInfo.maxsize))
    print("string types: {}".format(PyInfo.string_types))
    print("text type: {}".format(PyInfo.text_type))
    print("binary type: {}".format(PyInfo.binary_type))
    print("integer types: {}".format(PyInfo.integer_types))
    print("class types: {}".format(PyInfo.class_types))


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:41:01.834532
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == True  # PY2
    assert PyInfo.PY3 == False

    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)

    assert PyInfo.maxsize == int((1 << 63) - 1)

# Generated at 2022-06-14 06:41:12.575960
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Py2 and Py3 doesn't have dunder method __len__
    assert hasattr(PyInfo, "__len__") is False
    # PyInfo is a class type
    assert isinstance(PyInfo, type)
    # PyInfo can't iterable
    assert hasattr(PyInfo, "__iter__") is False
    # PyInfo can't use str()
    assert hasattr(PyInfo, "__str__") is False
    # PyInfo can't use repr()
    assert hasattr(PyInfo, "__repr__") is False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from pprint import pprint

    pprint(PyInfo.__dict__)

# Generated at 2022-06-14 06:41:22.101159
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('string', PyInfo.string_types)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(type, PyInfo.class_types)
        assert PyInfo.maxsize == sys.maxsize
    else:
        assert isinstance('string', PyInfo.string_types)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(type, PyInfo.class_types)
        print(PyInfo.maxsize)
        assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:41:32.416581
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert str in PyInfo.string_types
        assert unicode in PyInfo.string_types
        assert bytes not in PyInfo.string_types
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert long in PyInfo.integer_types
        assert type in PyInfo.class_types
        assert types.ClassType in PyInfo.class_types

    if PyInfo.PY3:
        assert str in PyInfo.string_types
        assert bytes in PyInfo.string_types
        assert unicode not in PyInfo.string_types
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert long not in PyInfo.integer_types
        assert type in PyInfo.class_types

# Generated at 2022-06-14 06:41:58.394053
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('abc', PyInfo.string_types)
    assert isinstance(b'abc', PyInfo.binary_type)
    assert isinstance(u'abc', PyInfo.text_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(object, PyInfo.class_types)

# Generated at 2022-06-14 06:42:00.705941
# Unit test for constructor of class PyInfo
def test_PyInfo():
    PyInfo()


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:42:07.660478
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    if PyInfo.PY2:
        assert isinstance(u'', PyInfo.text_type)
    else:
        assert PyInfo.text_type == str
    assert isinstance('', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:42:18.843990
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import six

    assert PyInfo.PY2 == six.PY2
    assert PyInfo.PY3 == six.PY3

    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)

    # str in PyInfo.string_types
    assert(PyInfo.PY2 and str in PyInfo.string_types) or (PyInfo.PY3 and str not in PyInfo.string_types)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:42:25.134965
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is (not PyInfo.PY3)
    assert type(PyInfo.string_types) == tuple
    assert type(PyInfo.text_type) == str
    assert type(PyInfo.integer_types) == tuple
    assert type(PyInfo.class_types) == tuple
    assert type(PyInfo.maxsize) == int

# Generated at 2022-06-14 06:42:33.952130
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


# Unit test
if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:42:44.854835
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    Unit test for constructor of class PyInfo
    """
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance("a", PyInfo.string_types)
    assert isinstance(u"a", PyInfo.string_types)
    assert not isinstance(b"a", PyInfo.string_types)

    assert isinstance("a", PyInfo.text_type)
    assert not isinstance(u"a", PyInfo.text_type)
    assert not isinstance(b"a", PyInfo.text_type)

    assert isinstance(b"a", PyInfo.binary_type)
    assert not isinstance("a", PyInfo.binary_type)
    assert not isinstance(u"a", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)


# Generated at 2022-06-14 06:42:49.680295
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not True and PyInfo.PY3 is True
    assert PyInfo.string_types == (str,)
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.maxsize == 2 ** 63 - 1


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:43:01.090173
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    Test the constructor of class PyInfo
    """
    assert PyInfo().PY2 == (sys.version_info[0] == 2)
    if sys.version_info[0] == 2:
        assert PyInfo().maxsize == sys.maxsize
        assert PyInfo().PY3 is False
        assert PyInfo().binary_type is str
        assert PyInfo().integer_types == (int, long)
        assert PyInfo().text_type is unicode
        assert PyInfo().string_types == (str, unicode)
        assert PyInfo().class_types == (type, types.ClassType)
    else:
        assert PyInfo().PY3


# Convert a variable from unicode to str

# Generated at 2022-06-14 06:43:09.170830
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == True or PyInfo.PY3 == True
    assert PyInfo.PY2 != PyInfo.PY3

    pyver = sys.version_info[0]
    assert PyInfo.PY2 == (pyver == 2)
    assert PyInfo.PY3 == (pyver == 3)

# Generated at 2022-06-14 06:43:58.120469
# Unit test for constructor of class PyInfo
def test_PyInfo():
    instance = PyInfo()
    if instance.PY3:
        assert isinstance("", instance.string_types)
    else:
        assert isinstance("", instance.string_types)

    if instance.PY2:
        assert isinstance("", instance.binary_type)
    else:
        assert isinstance("", instance.string_types)

    if instance.PY2:
        assert isinstance(u"", instance.text_type)
    else:
        assert isinstance("", instance.text_type)

    if instance.PY3:
        assert isinstance(123, instance.integer_types)
    else:
        assert isinstance(123, instance.integer_types)

    if instance.PY3:
        assert isinstance(int, instance.class_types)

# Generated at 2022-06-14 06:44:06.605581
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.binary_type == str
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == (1 << 63) - 1


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:44:11.142545
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert not isinstance(PyInfo.PY2, str)
    assert not isinstance(PyInfo.PY3, str)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:44:24.036526
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
    else:  # PY2
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str

    assert PyInfo.maxsize > 0

    # test PyInfo.maxsize
    if sys.version_info < (3,):
        import platform

        # on 64-bit, could be 2**32-1 or 2**63-1
        # on 32-bit

# Generated at 2022-06-14 06:44:29.991052
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:44:41.309974
# Unit test for constructor of class PyInfo

# Generated at 2022-06-14 06:44:42.594785
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.maxsize, (int))

# Generated at 2022-06-14 06:44:50.594237
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == 9223372036854775807
    assert PyInfo.maxsize < sys.maxsize


if __name__ == "__main__":
    import nose

    nose.main()

# Generated at 2022-06-14 06:44:58.632702
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert isinstance("".encode("utf-8"), PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(maxsize, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:45:05.349791
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(27, PyInfo.integer_types)
    assert isinstance(b'a', PyInfo.binary_type)
    assert isinstance('a', PyInfo.string_types)
    assert isinstance(u'a', PyInfo.string_types)
    assert isinstance(PyInfo, PyInfo.class_types)


if __name__ == '__main__':
    test_PyInfo()