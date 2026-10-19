

# Generated at 2022-06-14 06:35:44.927997
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert not PyInfo.PY2
    assert PyInfo.PY3
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes
    assert PyInfo.integer_types == (int,)
    assert PyInfo.class_types == (type,)

    assert PyInfo.maxsize == (1 << 63) - 1


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:35:49.663878
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from pyvalid import accepts, returns

    # I don't know how to test this class
    @accepts(object)
    @returns(bool)
    def _(x):
        return isinstance(x, PyInfo)

    PyInfo()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:35:55.426648
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("", PyInfo.string_types)
    assert isinstance(PyInfo.maxsize, int)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.PY3, bool)


__all__ = [
    'PyInfo',
]

# Generated at 2022-06-14 06:36:05.153914
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def check(py_version_info, py_full_version):
        info = PyInfo()
        assert info.PY2 or info.PY3
        assert isinstance(info.string_types, tuple)
        assert isinstance(info.text_type, type)
        assert isinstance(info.binary_type, type)
        assert isinstance(info.integer_types, tuple)
        assert isinstance(info.maxsize, int)
        assert isinstance(info.class_types, tuple)
        if info.PY2:
            assert isinstance(info.maxsize, (int, long))
        else:
            assert isinstance(info.maxsize, int)

    check((3, 4), "3.4.0")
    check((2, 7), "2.7.2")

# Generated at 2022-06-14 06:36:10.193819
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()
    assert p.PY2 == sys.version_info[0] == 2
    assert p.PY3 == sys.version_info[0] == 3


if __name__ == "__main__":
    test_PyInfo()
    print("Everything passed")

# Generated at 2022-06-14 06:36:12.758362
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (2 == sys.version_info[0])
    assert PyInfo.PY3 == (3 == sys.version_info[0])

# Generated at 2022-06-14 06:36:24.810071
# Unit test for constructor of class PyInfo
def test_PyInfo():
    the_str = "I am the string"
    the_int = 11
    the_float = 11.22
    the_list = [11, 22, 33]
    the_dict = {
        "one": 1,
        "two": 2,
    }
    the_class = str
    the_function = eval
    the_instance = eval
    the_module = eval
    the_iterator = eval
    the_tuple = tuple([11, 22, 33])

    def is_string(a):
        return PyInfo.PY2 and isinstance(a, basestring) or PyInfo.PY3 and isinstance(
            a, str
        )


# Generated at 2022-06-14 06:36:35.890313
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    if PyInfo.PY2:
        assert isinstance(PyInfo.binary_type, str)
    else:
        assert isinstance(PyInfo.binary_type, bytes)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:36:43.948724
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3

    assert PyInfo.string_types == (PyInfo.text_type,) or PyInfo.string_types == (PyInfo.text_type, PyInfo.binary_type)

    assert PyInfo.text_type == str or PyInfo.text_type == unicode

    assert PyInfo.binary_type == str or PyInfo.binary_type == bytes

    assert PyInfo.integer_types == (int,) or PyInfo.integer_types == (int, long)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:36:50.144475
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert PyInfo.string_types[0] == basestring
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types[0] == int
    assert PyInfo.integer_types[1] == long
    assert PyInfo.class_types[0] == type

# Generated at 2022-06-14 06:37:00.021775
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == int((1 << 63) - 1)

# Generated at 2022-06-14 06:37:08.236030
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.string_types == (basestring,) if PyInfo.PY2 else (str,)
    assert PyInfo.text_type == unicode if PyInfo.PY2 else str
    assert PyInfo.binary_type == str if PyInfo.PY2 else bytes
    assert PyInfo.integer_types == (int, long) if PyInfo.PY2 else (int,)
    assert PyInfo.class_types == (type, types.ClassType) if PyInfo.PY2 else (type,)
    assert isinstance(PyInfo.maxsize, int)


if __name__ == '__main__':
    import nose

# Generated at 2022-06-14 06:37:19.214453
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is True
    assert PyInfo.PY2 is False
    assert PyInfo.string_types is not None
    assert PyInfo.string_types is not (str,)
    assert PyInfo.binary_type is not None
    assert PyInfo.binary_type is not bytes
    assert PyInfo.maxsize == sys.maxsize
    assert PyInfo.class_types is not None
    assert PyInfo.class_types is not type
    assert PyInfo.text_type is not None
    assert PyInfo.text_type is not str
    assert PyInfo.integer_types is not None
    assert PyInfo.integer_types is not int


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# Generated at 2022-06-14 06:37:22.713270
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    print(PyInfo.maxsize)



# Generated at 2022-06-14 06:37:25.578156
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test if PyInfo is working
    assert PyInfo.PY2 or PyInfo.PY3
    # Test if string_type is working
    assert isinstanc

# Generated at 2022-06-14 06:37:27.276805
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:37:32.239184
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Just verify that class variables are defined at all
    assert PyInfo.PY2
    assert PyInfo.PY3
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.integer_types
    assert PyInfo.binary_type
    assert PyInfo.class_types
    assert PyInfo.maxsize


py_info = PyInfo()

# Generated at 2022-06-14 06:37:43.121923
# Unit test for constructor of class PyInfo
def test_PyInfo():
    '''
    Unittest for PyInfo class
    '''
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
        assert PyInfo.class_type == (type,)

# Generated at 2022-06-14 06:37:47.426947
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.class_types)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:00.496589
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    # `string_types`
    for _type in PyInfo.string_types:
        if PyInfo.PY2:
            assert not isinstance(1, _type)
            assert isinstance('1', _type)
            assert isinstance(u'1', _type)
        else:
            assert not isinstance(1, _type)
            assert isinstance('1', _type)

    # `binary_type`
    for _type in PyInfo.string_types:
        if PyInfo.PY3:
            assert isinstance(b'1', _type)
            assert not isinstance('1', _type)

# Generated at 2022-06-14 06:38:09.317521
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY2 is False
    assert PyInfo.PY3 is True or PyInfo.PY3 is False
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)


if __name__ == '__main__':
    test_PyInfo()
    print('Test Passed!')

# Generated at 2022-06-14 06:38:15.295831
# Unit test for constructor of class PyInfo

# Generated at 2022-06-14 06:38:21.949289
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance("", PyInfo.text_type)
        assert not isinstance(b"", PyInfo.string_types)
    else:  # PY2
        assert isinstance(u"", PyInfo.text_type)
        assert isinstance("", PyInfo.string_types)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:38:31.202761
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


if __name__ == '__main__':
    import pytest

    pytest.main()

# Generated at 2022-06-14 06:38:43.110213
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo
    if info.PY2:
        assert info.string_types == (basestring, )
        assert info.text_type is unicode
        assert info.binary_type is str
        assert info.integer_types == (int, long)
        assert info.class_types == (type, types.ClassType)
    else:
        assert info.string_types == (str, )
        assert info.text_type is str
        assert info.binary_type is bytes
        assert info.integer_types == (int, )
        assert info.class_types == (type, )

    assert info.maxsize >= 0x7FFFFFFF


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:38:55.433155
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance("", PyInfo.string_types)
        assert isinstance(b"", PyInfo.string_types)
        assert not isinstance(b"", PyInfo.text_type)

        assert isinstance("", PyInfo.string_types)
        assert isinstance(b"", PyInfo.binary_type)

        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(1, PyInfo.class_types)
    else:
        assert isinstance("", PyInfo.string_types)
        assert isinstance(u"", PyInfo.string_types)
        assert not isinstance(u"", PyInfo.text_type)

        assert isinstance("", PyInfo.binary_type)
        assert isinstance(u"", PyInfo.text_type)

       

# Generated at 2022-06-14 06:39:07.476697
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert(isinstance(b'asd', PyInfo.binary_type))
        assert(not isinstance('asd', PyInfo.binary_type))
        assert(isinstance(u'asd', PyInfo.text_type))
        assert(not isinstance('asd', PyInfo.text_type))
        assert(isinstance(int(1), PyInfo.integer_types))
        assert(isinstance(long(1), PyInfo.integer_types))
        assert(isinstance(1, PyInfo.integer_types))
        assert(not isinstance(1.0, PyInfo.integer_types))
    else:
        assert(isinstance(b'asd', PyInfo.binary_type))
        assert(not isinstance('asd', PyInfo.binary_type))

# Generated at 2022-06-14 06:39:12.060003
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    Unit test for constructor of class PyInfo.
    """

    assert PyInfo.PY2 != PyInfo.PY3
    assert PyInfo.PY2
    assert not PyInfo.PY3


if __name__ == "__main__":
    import nose

    nose.runmodule()

# Generated at 2022-06-14 06:39:16.810088
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    assert info.PY2 or info.PY3
    if info.PY2:
        assert isinstance(info.maxsize, int)
    elif info.PY3:
        assert isinstance(info.maxsize, int)
    else:
        assert False, 'never here'

# Generated at 2022-06-14 06:39:25.973939
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.PY2 != PyInfo.PY3

    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.string_types)
    assert not isinstance(123, PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert not isinstance(b"", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)
    assert not isinstance("", PyInfo.binary_type)
    assert isinstance(123, PyInfo.integer_types)
    assert not isinstance("", PyInfo.integer_types)
    assert isinstance(tuple, PyInfo.class_types)

# Generated at 2022-06-14 06:39:44.058295
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.maxsize, int)
    assert isinstance(PyInfo.string_types, tuple)
    assert issubclass(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert issubclass(PyInfo.integer_types[0], type)
    assert isinstance(PyInfo.class_types, tuple)
    assert issubclass(PyInfo.class_types[0], type)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:39:54.292986
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3

    # Unit test for string_types function
    assert isinstance(b"", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)

    # Unit test for text_type function
    assert isinstance(b"", PyInfo.text_type)
    assert isinstance(u"", PyInfo.text_type)

    # Unit test for binary_type function
    assert isinstance(b"", PyInfo.binary_type)
    assert not isinstance(u"", PyInfo.binary_type)

    # Unit test for integer_types function
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:40:01.417067
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from nose.tools import assert_equals, assert_false, assert_true, raises
    from nose.plugins.skip import SkipTest

    if PyInfo.PY2:
        raise SkipTest("Python 2")

    assert_false(PyInfo.PY3)

    def check_one_type(obj, type_):
        assert_true(isinstance(obj, type_))
        assert_true(isinstance(obj, PyInfo.string_types))
        assert_false(isinstance(obj, PyInfo.binary_type))

    assert_true(PyInfo.PY2 or PyInfo.PY3)
    assert_true(isinstance(object(), PyInfo.class_types))
    assert_true(isinstance("", PyInfo.text_type))
    assert_true(isinstance("", PyInfo.string_types))

# Generated at 2022-06-14 06:40:13.083484
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
    else:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:40:26.773569
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert type("") in PyInfo.string_types
        assert "a" in PyInfo.string_types
        assert type(b"") in PyInfo.string_types
        assert b"a" in PyInfo.string_types

        assert type("") == PyInfo.text_type
        assert "a" == PyInfo.text_type
        assert type(b"") != PyInfo.text_type
        assert b"a" != PyInfo.text_type

        assert type("") != PyInfo.binary_type
        assert "a" != PyInfo.binary_type
        assert type(b"") == Py

# Generated at 2022-06-14 06:40:36.655284
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # The constructor of class PyInfo is invoked implicitly when a
    # code calls PyInfo.PY2 or PyInfo.PY3 or PyInfo.string_types, etc.

    if PyInfo.PY3:
        assert PyInfo.maxsize == sys.maxsize
    elif PyInfo.PY2:
        if sys.platform.startswith("java"):
            # Jython always uses 32 bits.
            assert PyInfo.maxsize == int((1 << 31) - 1)
        else:
            # It's possible to have sizeof(long) != sizeof(Py_ssize_t).
            class X(object):

                def __len__(self):
                    return 1 << 31


# Generated at 2022-06-14 06:40:38.852600
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is False


# Generated at 2022-06-14 06:40:46.310401
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    >>> isinstance("foo", PyInfo.string_types)
    True
    >>> isinstance(b"foo", PyInfo.binary_type)
    True
    >>> isinstance(u"foo", PyInfo.text_type)
    True
    >>> isinstance(1, PyInfo.integer_types)
    True
    >>> isinstance(1L, PyInfo.integer_types)
    True
    >>> isinstance(set, PyInfo.class_types)
    True
    """


# min

# Generated at 2022-06-14 06:40:58.011017
# Unit test for constructor of class PyInfo
def test_PyInfo():
    value = PyInfo()
    if sys.version_info[0] == 2:
        assert value.PY2 is True
        assert value.PY3 is False
        assert value.string_types == (basestring,)
        assert value.text_type is unicode
        assert value.binary_type is str
        assert value.integer_types == (int, long)
        assert value.class_types == (type, types.ClassType)

    else:
        assert value.PY2 is False
        assert value.PY3 is True
        assert value.string_types == (str,)
        assert value.text_type is str
        assert value.binary_type is bytes
        assert value.integer_types == (int,)
        assert value.class_types == (type,)

# Generated at 2022-06-14 06:41:03.726045
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 or PyInfo.PY2

    if PyInfo.PY3:
        assert isinstance(u"a", PyInfo.text_type)
        assert isinstance(b"b", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(dict, PyInfo.class_types)
    else:
        assert isinstance(u"a", PyInfo.binary_type)
        assert isinstance(b"b", PyInfo.binary_type)
        assert isinstance(1, (int, long))
        assert isinstance(dict, (type, types.ClassType))

# Generated at 2022-06-14 06:41:29.660479
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is True
    assert isinstance(PyInfo.string_types, tuple)
    assert len(PyInfo.string_types) == 1
    assert PyInfo.text_type is str
    assert PyInfo.binary_type is bytes
    assert isinstance(PyInfo.integer_types, tuple)
    assert len(PyInfo.integer_types) == 1
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:41:38.869544
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py_info = PyInfo()

    assert isinstance(py_info.string_types, tuple)
    assert isinstance(py_info.string_types[0], type)
    assert isinstance(py_info.text_type, type)
    assert isinstance(py_info.binary_type, type)
    assert isinstance(py_info.integer_types, tuple)
    assert isinstance(py_info.integer_types[0], type)
    assert isinstance(py_info.class_types, tuple)
    assert isinstance(py_info.class_types[0], type)
    assert isinstance(py_info.maxsize, int)

# Generated at 2022-06-14 06:41:46.765222
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('abc', PyInfo.string_types)
        assert not isinstance('abc', PyInfo.class_types)
    else:  # PY3
        assert isinstance('abc', PyInfo.string_types)
        assert isinstance(str, PyInfo.class_types)
    assert isinstance('abc', PyInfo.text_type)
    assert not isinstance(sys.version_info, PyInfo.integer_types)


test_PyInfo()

# Generated at 2022-06-14 06:41:51.559989
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # To assert that a class has a constructor, just pass in the class.
    # We can do this since we know that objects of type 'type'
    # have a constructor.
    assert isinstance(PyInfo, type)



# Generated at 2022-06-14 06:41:59.885719
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(b'', PyInfo.binary_type)
    assert isinstance(u'', PyInfo.string_types)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(int(1), PyInfo.integer_types)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:42:04.602795
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.maxsize == (1 << 31) - 1

# Generated at 2022-06-14 06:42:16.801772
# Unit test for constructor of class PyInfo
def test_PyInfo():
    class C:
        pass

    class D(object):
        pass

    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance('a', PyInfo.string_types)
    assert isinstance(u'a', PyInfo.string_types)
    assert not isinstance(b'a', PyInfo.string_types)
    
    assert isinstance(u'a', PyInfo.text_type)
    assert not isinstance(b'a', PyInfo.text_type)

    assert isinstance(b'a', PyInfo.binary_type)
    assert not isinstance(u'a', PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1.1, PyInfo.integer_types)
    

# Generated at 2022-06-14 06:42:27.251191
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.maxsize == int((1 << 63) - 1)
    else:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.maxsize == int((1 << 63) - 1)



# Generated at 2022-06-14 06:42:35.117950
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    def test_type(type_):
        assert isinstance(type_(), type_)

    test_type(PyInfo.string_types)
    test_type(PyInfo.text_type)
    test_type(PyInfo.binary_type)
    test_type(PyInfo.integer_types)
    test_type(PyInfo.class_types)



# Generated at 2022-06-14 06:42:40.641650
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    assert pi.PY2 or pi.PY3
    assert len(pi.string_types) >= 1
    assert len(pi.integer_types) >= 1
    assert len(pi.class_types) >= 1
    assert pi.maxsize >= 0

# Generated at 2022-06-14 06:43:27.810478
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 or PyInfo.PY2
    assert type(PyInfo.string_types) == tuple
    assert type(PyInfo.text_type()) == str
    assert type(PyInfo.binary_type()) == bytes
    assert type(PyInfo.integer_types) == tuple
    assert type(PyInfo.class_types) == tuple
    assert type(PyInfo.maxsize) == int

# Generated at 2022-06-14 06:43:37.361367
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if __name__ == "__main__":
        # code used only for testing purposes
        print("PY2:", PyInfo.PY2)
        print("PY3:", PyInfo.PY3)
        assert PyInfo.PY2 + PyInfo.PY3 == 1
        print("string_types:", PyInfo.string_types)
        print("text_type:", PyInfo.text_type)
        print("binary_type:", PyInfo.binary_type)
        print("integer_types:", PyInfo.integer_types)
        print("class_types:", PyInfo.class_types)
        print("maxsize:", PyInfo.maxsize)

        # Try various values
        print(isinstance("hello", PyInfo.string_types))

# Generated at 2022-06-14 06:43:47.202579
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance('text', PyInfo.string_types)
        assert isinstance('text', PyInfo.text_type)
        assert not isinstance('text', PyInfo.binary_type)
    else:
        assert isinstance(u'text', PyInfo.string_types)
        assert isinstance(u'text', PyInfo.text_type)
        assert not isinstance(u'text', PyInfo.binary_type)

    assert isinstance(3, PyInfo.integer_types)
    assert isinstance(3, int)



# Generated at 2022-06-14 06:43:57.795599
# Unit test for constructor of class PyInfo
def test_PyInfo():
    PI = PyInfo()
    assert PI.PY2 == (sys.version_info[0] == 2)
    assert PI.PY3 == (sys.version_info[0] == 3)

    if sys.platform.startswith("java"):
        assert PI.maxsize == int((1 << 31) - 1)
    else:
        assert PI.maxsize == sys.maxsize

    assert isinstance(PI.string_types, tuple)
    assert isinstance(PI.text_type, text_type)
    assert isinstance(PI.binary_type, binary_type)
    assert isinstance(PI.integer_types, tuple)
    assert isinstance(PI.class_types, tuple)


# Generated at 2022-06-14 06:44:05.771700
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 is True or PyInfo.PY3 is False
    assert PyInfo.PY2 is True or PyInfo.PY2 is False
    assert PyInfo.string_types is tuple
    assert PyInfo.text_type is str or PyInfo.text_type is unicode
    assert PyInfo.binary_type is str or PyInfo.binary_type is bytes
    assert PyInfo.integer_types is tuple
    assert PyInfo.class_types is tuple

# Generated at 2022-06-14 06:44:07.312876
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    >>> PyInfo.PY2
    False
    """
    pass

# Generated at 2022-06-14 06:44:13.013413
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test PY2 PY3
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    # Test string_types
    if PyInfo.PY2:
        assert isinstance(PyInfo.string_types, tuple)
        assert isinstance(PyInfo.string_types[0], type)
        assert issubclass(PyInfo.string_types[0], object)
        assert PyInfo.string_types[0].__name__ == "basestring"
        assert len(PyInfo.string_types) == 1
    else:
        assert isinstance(PyInfo.string_types, tuple)
        assert isinstance(PyInfo.string_types[0], type)

# Generated at 2022-06-14 06:44:24.935894
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py2_tests = [
        (PyInfo.PY2, True),
        (PyInfo.PY3, False),
        (PyInfo.string_types, (basestring, )),
        (PyInfo.text_type, unicode),
        (PyInfo.binary_type, str),
        (PyInfo.integer_types, (int, long)),
        (PyInfo.class_types, (type, types.ClassType)),
        (PyInfo.maxsize, int((1 << 63) - 1)),
    ]


# Generated at 2022-06-14 06:44:28.236625
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3


# Py2to3 porting tools

# Generated at 2022-06-14 06:44:40.472708
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY3:
        assert isinstance(u'', PyInfo.string_types)
        assert isinstance(u'', PyInfo.text_type)
        assert isinstance(u'', PyInfo.binary_type)
        assert isinstance(u'', (int,))
        assert isinstance(u'', (type,))
    else:  # PY2
        assert isinstance(u'', (basestring,))
        assert isinstance(u'', (unicode,))
        assert isinstance(u'', (str,))
        assert isinstance(1, (int, long))