

# Generated at 2022-06-14 06:35:49.357313
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test for Python 2.7.16 (default, Mar  4 2019, 09:02:22)
    # [GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert not isinstance(b"", PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)
    assert PyInfo.text_type == unicode
    assert isinstance(u"", PyInfo.text_type)
    assert PyInfo.binary_type == str
   

# Generated at 2022-06-14 06:35:55.128484
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3, "PyInfo.PY2 or PyInfo.PY3 must be True"
    assert PyInfo.maxsize >= 0, "PyInfo.maxsize must be nonnegative"
    assert PyInfo.maxsize > 0, "PyInfo.maxsize must be positive"

# Generated at 2022-06-14 06:36:04.783831
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance("S", PyInfo.string_types)
        assert isinstance(u"S", PyInfo.string_types)
        assert not isinstance(b"S", PyInfo.string_types)
        assert isinstance(u"S", PyInfo.text_type)
        assert not isinstance("S", PyInfo.text_type)
        assert isinstance(b"S", PyInfo.binary_type)
        assert not isinstance(u"S", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert not isinstance(1.1, PyInfo.integer_types)
        class A(object):
            pass

        a = A()
        assert isinstance(a, PyInfo.class_types)

# Generated at 2022-06-14 06:36:13.042257
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True

    assert PyInfo.PY2 is False or type(PyInfo.text_type) is unicode
    assert PyInfo.PY3 is False or type(PyInfo.text_type) is str

    assert PyInfo.PY2 is False or type(PyInfo.binary_type) is str
    assert PyInfo.PY3 is False or type(PyInfo.binary_type) is bytes



# Generated at 2022-06-14 06:36:18.642408
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("abc", PyInfo.string_types)
    assert isinstance(u"abc", PyInfo.text_type)
    assert isinstance(u"abc", PyInfo.string_types)

# Generated at 2022-06-14 06:36:25.292247
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.maxsize, int)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:36:29.793383
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (PyInfo.PY2 == False)
    assert PyInfo.PY2 == (PyInfo.PY3 == False)


if __name__ == '__main__':

    print(test_PyInfo())

# Generated at 2022-06-14 06:36:36.739344
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

# Generated at 2022-06-14 06:36:44.791525
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
    assert isinstance(getattr(PyInfo, 'basestring', None),
                      type) or PyInfo.PY2 is False

# Generated at 2022-06-14 06:36:46.621352
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3


test_PyInfo()

# Generated at 2022-06-14 06:36:57.138652
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(__builtins__, dict)
        assert isinstance(__builtins__['True'], bool)
        assert isinstance(__builtins__['False'], bool)
        assert isinstance(__builtins__['None'], types.NoneType)
    else:  # PY3
        assert isinstance(__builtins__, dict)
        assert isinstance(__builtins__['True'], bool)
        assert isinstance(__builtins__['False'], bool)
        assert isinstance(__builtins__['None'], types.NoneType)


# Generated at 2022-06-14 06:37:10.760275
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.PY2 == (sys.version_info[0] == 2)

    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)

        assert PyInfo.maxsize == (1 << 63) - 1
    else:  # PY2
        assert PyInfo.string_types == (str, unicode)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)

# Generated at 2022-06-14 06:37:14.522656
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-14 06:37:19.182926
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Confirm that PyInfo is a new-style class
    assert isinstance(PyInfo, type), 'PyInfo is not a new-style class'

    # Confirm that PyInfo can be instantiated
    info = PyInfo()
    assert isinstance(info, object), 'PyInfo instance is not of type object'



# Generated at 2022-06-14 06:37:24.970870
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from os import uname

    pyinfo = PyInfo()
    assert pyinfo.PY2 is False and pyinfo.PY3 is True, 'Python Version Error'
    if not uname()[0] == 'Windows':
        assert pyinfo.maxsize == (1 << 63) - 1, 'Max Size Error'

# Generated at 2022-06-14 06:37:36.478465
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PY2 == PyInfo.PY2
    assert PY3 == PyInfo.PY3
    assert string_types == PyInfo.string_types
    assert text_type == PyInfo.text_type
    assert binary_type == PyInfo.binary_type
    assert integer_types == PyInfo.integer_types
    assert class_types == PyInfo.class_types
    assert maxsize == PyInfo.maxsize


# def test_bytes_str():
#     assert PY2 == isinstance(bytes_str(u"", "utf-8"), str)
#     assert PY3 == isinstance(bytes_str(u"", "utf-8"), bytes)
#     assert PY2 == isinstance(bytes_str("", "utf-8"), str)
#     assert PY3 == isinstance(bytes_str("

# Generated at 2022-06-14 06:37:46.779552
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    if PyInfo.PY2:
        assert any(s in str(PyInfo.string_types) for s in ["str", "unicode"])
        assert "str" in str(PyInfo.binary_type)
        assert all(s in str(PyInfo.integer_types) for s in ["int", "long"])
    elif PyInfo.PY3:
        assert (
            any(s in str(PyInfo.string_types) for s in ["<class 'str'>", "<class 'bytes'>"])
        )
        assert "str" in str(PyInfo.text_type)
        assert "bytes" in str(PyInfo.binary_type)
        assert "<class 'int'>" in str(PyInfo.integer_types)
    return

# Generated at 2022-06-14 06:37:58.420877
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert PyInfo.PY2 is not PyInfo.PY3
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance('a', PyInfo.string_types)
    assert isinstance(u'a', PyInfo.string_types)
    assert isinstance([], PyInfo.class_types)
    if PyInfo.PY3:
        assert isinstance(b'a', PyInfo.binary_type)
        assert isinstance("", PyInfo.text_type)
    else:
        assert isinstance("a", PyInfo.binary_type)
        assert isinstance(u'', PyInfo.text_type)


# for tests

# Generated at 2022-06-14 06:38:06.549086
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import platform
    import struct

    print("Python 2.x is %s" % PyInfo.PY2)
    print("Python 3.x is %s" % PyInfo.PY3)
    print("Python info:")
    print(sys.version)
    print(sys.version_info)
    print(sys.byteorder)
    print(sys.maxsize)
    print(platform.architecture())
    print(tuple(platform.python_version_tuple()))
    print(platform.system())
    print(struct.calcsize("P") * 8)
    print(platform.platform())
    print(platform.machine())


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:18.008839
# Unit test for constructor of class PyInfo
def test_PyInfo():
    test_dict = [
        ("sys.version_info[0]", 2, 3),
        ("string_types", (basestring,), (str,)),
        ("text_type", unicode, str),
        ("binary_type", str, bytes),
        ("integer_types", (int, long), (int,)),
        ("maxsize", None, 9223372036854775807 if sys.maxsize == 9223372036854775807 else 2147483647),  # noqa
    ]
    if sys.platform.startswith("java"):
        test_dict[-1][1] = 2147483647

    for k, v1, v2 in test_dict:
        if PyInfo.PY2:
            if v1 is None:
                assert v2 > 2147483647

# Generated at 2022-06-14 06:38:30.879314
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    assert pi.PY2 == (sys.version_info[0] == 2)
    assert pi.PY3 == (sys.version_info[0] == 3)
    assert pi.string_types == (basestring, )
    assert pi.text_type == unicode
    assert pi.binary_type == str
    assert pi.integer_types == (int, long)
    assert pi.class_types == (type, types.ClassType)

# Generated at 2022-06-14 06:38:36.129336
# Unit test for constructor of class PyInfo
def test_PyInfo():
    try:
        from nose.tools import assert_equal
    except ImportError:
        sys.exit('Sorry, you need to install nose for unit testing')

    assert_equal(PyInfo.PY2, True)
    assert_equal(PyInfo.PY3, False)



# Generated at 2022-06-14 06:38:43.256164
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert 'str' in PyInfo.string_types
    assert isinstance('str', PyInfo.string_types)
    assert 'str' in PyInfo.string_types
    assert isinstance('str', PyInfo.string_types)
    assert isinstance('str', PyInfo.string_types)
    # test_PyInfo()

# Generated at 2022-06-14 06:38:49.367481
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(2 ** 63 - 1, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:38:59.088985
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Verify PY2 and PY3.
    assert (PyInfo.PY2 and not PyInfo.PY3) or (not PyInfo.PY2 and PyInfo.PY3)

    # Verify string_types.
    assert isinstance("", PyInfo.string_types)
    assert not isinstance(2, PyInfo.string_types)
    assert not isinstance(object(), PyInfo.string_types)

    # Verify text_type.
    assert isinstance("", PyInfo.text_type)
    assert isinstance(2, PyInfo.text_type)
    assert not isinstance(object(), PyInfo.text_type)

    # Verify binary_type.
    assert not isinstance("", PyInfo.binary_type)
    assert not isinstance(2, PyInfo.binary_type)
    assert not isinstance

# Generated at 2022-06-14 06:39:07.801635
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert len(PyInfo.string_types) == 1
    # assert isinstance('a', PyInfo.string_types)
    assert len(PyInfo.integer_types) == 2
    # assert isinstance(1, PyInfo.integer_types)
    # assert isinstance(2L, PyInfo.integer_types)
    # assert not isinstance(3.4, PyInfo.integer_types)
    if PyInfo.PY2:
        assert len(PyInfo.class_types) == 2
    else:  # PY3
        assert len(PyInfo.class_types) == 1



# Generated at 2022-06-14 06:39:11.535847
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print(PyInfo.PY2)
    print(PyInfo.PY3)
    print(isinstance(PyInfo.integer_types, int))


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:39:12.826680
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pass



# Generated at 2022-06-14 06:39:18.925018
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is False
    assert PyInfo.string_types == (str, unicode)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)



# Generated at 2022-06-14 06:39:26.166521
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.text_type, type)
    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type is unicode
    elif PyInfo.PY3:
        assert isinstance(PyInfo.binary_type, type)
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type is str
    else:
        raise ValueError("PyInfo.PY2 and PyInfo.PY3 are both False.")



# Generated at 2022-06-14 06:39:41.728405
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)

    # text_type
    if PyInfo.PY3:
        assert isinstance("", PyInfo.text_type)
        assert not isinstance(u"", PyInfo.text_type)
    else:
        assert isinstance(u"", PyInfo.text_type)

    assert isinstance(b"", PyInfo.binary_type)

    # maxsize
    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:39:45.149600
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize > 0


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:39:58.244221
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # normal case
    assert PyInfo.PY2 is True  # noqa
    assert PyInfo.PY3 is False  # noqa
    assert PyInfo.string_types[0] == (basestring,)  # noqa
    assert PyInfo.text_type == unicode  # noqa
    assert PyInfo.binary_type == str  # noq
    assert PyInfo.integer_types[0] == int  # noqa
    assert PyInfo.integer_types[1] == long  # noqa
    assert PyInfo.class_types[0] == type  # noqa
    assert PyInfo.class_types[1] == types.ClassType  # noqa
    assert PyInfo.maxsize == (1 << 63) - 1  # noqa

    # abnormal case

# Generated at 2022-06-14 06:40:02.556400
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 == (2 == sys.version_info[0])
    assert pyinfo.PY3 == (3 == sys.version_info[0])

# Generated at 2022-06-14 06:40:06.327270
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    print(sys.version_info)
    print(PyInfo.PY2)
    print(PyInfo.PY2)
    print(PyInfo.PY3)



# Generated at 2022-06-14 06:40:07.493666
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo is not None

# Generated at 2022-06-14 06:40:10.150621
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:40:14.012858
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance("hello", PyInfo.string_types)
    assert isinstance(b"hello", PyInfo.binary_type)

    assert issubclass(type, PyInfo.class_types)

# Generated at 2022-06-14 06:40:27.511637
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert type(PyInfo.PY2) is bool
    assert type(PyInfo.PY3) is bool

    assert hasattr(PyInfo, "string_types")
    assert hasattr(PyInfo, "text_type")
    assert type(PyInfo.string_types) == tuple
    assert isinstance(PyInfo.string_types[0], type)
    assert isinstance(PyInfo.text_type, type)
    assert hasattr(PyInfo, "binary_type")
    assert hasattr(PyInfo, "integer_types")
    assert hasattr(PyInfo, "maxsize")
    assert isinstance(PyInfo.maxsize, int)
    assert hasattr(PyInfo, "class_types")



# Generated at 2022-06-14 06:40:34.940942
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import time
    import types
    assert PyInfo.PY2 or PyInfo.PY3, "Neither Python2 nor Python3!"

    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types

    if PyInfo.PY2:
        assert isinstance(PyInfo.maxsize, long)
    else:
        assert isinstance(PyInfo.maxsize, int)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:58.247954
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Unit test for constructor of class PyInfo
    pyinfo = PyInfo()
    assert pyinfo.PY2 is True
    assert pyinfo.PY3 is False
    assert str == pyinfo.text_type
    assert int in pyinfo.integer_types
    assert long in pyinfo.integer_types

if __name__ == "__main__":
    pytest.main()

# Generated at 2022-06-14 06:41:03.059193
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 is True or pyinfo.PY3 is True
    assert isinstance(pyinfo.string_types, tuple)
    assert isinstance(pyinfo.text_type, type)
    assert isinstance(pyinfo.binary_type, type)
    assert isinstance(pyinfo.integer_types, tuple)
    assert isinstance(pyinfo.class_types, tuple)


if __name__ == "__main__":
    pytest.main(__file__)

# Generated at 2022-06-14 06:41:04.864367
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()
    print(p.PY2, p.PY3)

# Generated at 2022-06-14 06:41:16.282915
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance("", PyInfo.string_types)
        assert isinstance("", PyInfo.text_type)
        assert isinstance("", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(1, PyInfo.integer_types)
        print("PyInfo.PY2")
    else:
        assert isinstance("", PyInfo.string_types)
        assert isinstance("", PyInfo.text_type)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert PyInfo.maxsize == 2147483647

# Generated at 2022-06-14 06:41:23.812047
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode  # noqa: F821
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)  # noqa: F821
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:41:32.882468
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert type(PyInfo.string_types) == tuple
        assert type(PyInfo.string_types[0]) == type
        assert PyInfo.string_types[0].__name__ == 'basestring'

        assert type(PyInfo.text_type) == type
        assert PyInfo.text_type.__name__ == 'unicode'

        assert type(PyInfo.binary_type) == type
        assert PyInfo.binary_type.__name__ == 'str'

        assert type(PyInfo.integer_types) == tuple
        assert type(PyInfo.integer_types[0]) == type
        assert PyInfo.integer_types[0].__name__ == 'int'
        assert type(PyInfo.integer_types[1]) == type

# Generated at 2022-06-14 06:41:42.988836
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    # Check types
    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.string_types)
    assert not isinstance(0, PyInfo.string_types)
    assert isinstance(0, PyInfo.integer_types)
    assert not isinstance(0.0, PyInfo.integer_types)
    assert isinstance(type(0), PyInfo.class_types)

    # Check maxsize
    assert len(range(PyInfo.maxsize)) == PyInfo.maxsize
    if PyInfo.PY2:
        try:
            len(range(PyInfo.maxsize + 1))
        except OverflowError:
            pass
        else:
            assert False


# Function to convert string to unicode

# Generated at 2022-06-14 06:41:49.677379
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from sys import maxint

    s = PyInfo.string_types
    assert isinstance('foo', s)
    assert not isinstance(u'foo', s)
    assert not isinstance(b'foo', s)

    if PyInfo.PY3:
        assert PyInfo.maxsize > maxint
    else:
        # It's possible to have sizeof(long) != sizeof(Py_ssize_t).
        assert PyInfo.maxsize < maxint

# Generated at 2022-06-14 06:41:59.083862
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info = PyInfo()
    assert info.PY2 != info.PY3
    if info.PY2:
        assert info.string_types == (basestring,)
        assert info.text_type == unicode
        assert info.binary_type == str
        assert info.integer_types == (int, long)
        assert info.class_types == (type, types.ClassType)
        assert info.maxsize in (2147483647, 9223372036854775807)
    else:
        assert info.string_types == (str,)
        assert info.text_type == str
        assert info.binary_type == bytes
        assert info.integer_types == (int,)
        assert info.class_types == (type,)

# Generated at 2022-06-14 06:42:01.235162
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:42:47.910079
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Check the value of PY2
    assert PyInfo.PY2 is True or PyInfo.PY2 is False

    # Check the value of PY3
    assert PyInfo.PY3 is True or PyInfo.PY3 is False

    # Check the value of string_types
    assert isinstance(PyInfo.string_types, tuple)
    for t in PyInfo.string_types:
        assert isinstance(t, type)

    # Check the value of text_type
    assert isinstance(PyInfo.text_type, type)

    # Check the value of binary_type
    assert isinstance(PyInfo.binary_type, type)

    # Check the value of integer_types
    assert isinstance(PyInfo.integer_types, tuple)

# Generated at 2022-06-14 06:42:58.617186
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

    # print(maxsize)  # 64-bit = 9223372036854775807
    # print(type(maxsize))  # long

# Generated at 2022-06-14 06:43:01.141196
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert sys.version_info[0] == PyInfo.PY2 or sys.version_info[0] == PyInfo.PY3

# Generated at 2022-06-14 06:43:14.732590
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == sys.version_info[0] == 2
    assert PyInfo.PY3 == sys.version_info[0] == 3

    if PyInfo.PY3:
        assert PyInfo.string_types == [str, ]
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == [int, ]
        assert PyInfo.class_types == [type, ]
        assert PyInfo.maxsize == sys.maxsize
    else:  # PY2
        assert PyInfo.string_types == [basestring, ]
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == [int, long]

# Generated at 2022-06-14 06:43:25.720105
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    assert pi.PY2 == (sys.version_info[0] == 2)
    assert pi.PY3 == (sys.version_info[0] == 3)
    if pi.PY3:
        assert pi.string_types == (str,)
        assert pi.text_type is str
        assert pi.binary_type is bytes
        assert pi.class_types == (type,)
        assert pi.integer_types == (int,)
        assert pi.maxsize > 0
    else:
        assert pi.string_types == (basestring,)
        assert pi.text_type is unicode
        assert pi.binary_type is str
        assert pi.class_types == (type, types.ClassType)
        assert pi.integer_types == (int, long)
        assert pi.maxsize

# Generated at 2022-06-14 06:43:27.856621
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:43:36.386953
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)

    assert isinstance(b"", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(0, PyInfo.integer_types)

# Generated at 2022-06-14 06:43:43.778734
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3
    assert not PyInfo.PY2
    assert isinstance(PyInfo.string_types, tuple)
    assert 'int' in PyInfo.integer_types.__name__
    assert 'type' in PyInfo.class_types.__name__

    import sys
    assert sys.maxsize == PyInfo.maxsize


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:43:52.172710
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    if PyInfo.PY3:
        assert isinstance("", PyInfo.string_types)
        assert isinstance("", PyInfo.text_type)
        assert not isinstance("", PyInfo.binary_type)
        assert isinstance(b"", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(1, PyInfo.integer_types)
    else:
        assert isinstance("", PyInfo.string_types)
        assert not isinstance("", PyInfo.text_type)
        assert isinstance(u"", PyInfo.text_type)
        assert isinstance("", PyInfo.binary_type)
        assert not isinstance(b"", PyInfo.binary_type)

# Generated at 2022-06-14 06:44:03.825134
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
    else:  # PY3
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)

if __name__ == "__main__":
    test_PyInfo()