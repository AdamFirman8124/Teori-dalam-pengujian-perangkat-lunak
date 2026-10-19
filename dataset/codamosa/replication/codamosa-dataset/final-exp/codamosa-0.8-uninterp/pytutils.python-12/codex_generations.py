

# Generated at 2022-06-14 06:35:48.376672
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 or PyInfo.PY2
    assert not (PyInfo.PY3 and PyInfo.PY2)

    assert isinstance("blah", PyInfo.string_types)
    assert isinstance("blah", PyInfo.text_type)
    assert isinstance("blah".encode("ascii"), PyInfo.binary_type)

    for number in PyInfo.integer_types:
        assert isinstance(number(10), PyInfo.integer_types)
        assert not isinstance(10.0, PyInfo.integer_types)

    assert isinstance(int, PyInfo.class_types)


if __name__ == "__main__":
    test_PyInfo()
    print("Everything passed")

# Generated at 2022-06-14 06:35:53.593056
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True, 'PyInfo did not work'


if __name__ == '__main__':
    test_PyInfo()

###############################################################################
# End of code
###############################################################################

# Generated at 2022-06-14 06:36:01.043016
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

# Generated at 2022-06-14 06:36:09.813079
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert isinstance(pyinfo.PY2, bool)
    assert isinstance(pyinfo.PY3, bool)
    assert isinstance(pyinfo.string_types, tuple)
    assert isinstance(pyinfo.text_type, type) and not isinstance(pyinfo.text_type, tuple)
    assert isinstance(pyinfo.binary_type, type) and not isinstance(pyinfo.binary_type, tuple)
    assert isinstance(pyinfo.integer_types, tuple)
    assert isinstance(pyinfo.class_types, tuple)
    assert isinstance(pyinfo.maxsize, int)

# Generated at 2022-06-14 06:36:14.288115
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.maxsize == sys.maxsize
    elif PyInfo.PY3:
        assert PyInfo.maxsize == sys.maxsize
    else:
        assert False, 'Unsupported python version: %s' % sys.version_info[0]

# Generated at 2022-06-14 06:36:18.718275
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()
    assert isinstance(p, PyInfo)


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:36:21.122001
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py2 = sys.version_info[0] == 2
    assert PyInfo.PY2 == py2
    assert PyInfo.PY3 != py2

# Generated at 2022-06-14 06:36:27.998720
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()
    if p.PY2:
        text_type = unicode
        binary_type = str
        maxsize = int((1 << 31) - 1)
    else:
        text_type = str
        binary_type = bytes
        maxsize = int((1 << 63) - 1)

    assert isinstance(p.string_types, tuple)
    assert isinstance(p.string_types[0], type)
    assert isinstance(text_type(), p.text_type)
    assert isinstance(binary_type(), p.binary_type)
    assert isinstance(p.integer_types, tuple)
    assert isinstance(p.integer_types[0], type)
    assert isinstance(p.class_types, tuple)
    assert isinstance(p.class_types[0], type)


# Generated at 2022-06-14 06:36:36.994446
# Unit test for constructor of class PyInfo
def test_PyInfo():
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

# Generated at 2022-06-14 06:36:42.573391
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert not (PyInfo.PY2 and PyInfo.PY3)
    assert (
        sys.version_info[0] == 2
    ), "assert sys.version_info[0] == 2 | sys.version_info[0] == 3"



# Generated at 2022-06-14 06:36:51.704484
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

# Generated at 2022-06-14 06:37:02.941159
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance("", PyInfo.string_types)
        assert not isinstance(b"", PyInfo.string_types)
        assert not isinstance(1, PyInfo.string_types)
        assert isinstance("", PyInfo.text_type)
        assert not isinstance(b"", PyInfo.text_type)
        assert not isinstance(1, PyInfo.text_type)
        assert isinstance(b"", PyInfo.binary_type)
        assert not isinstance("", PyInfo.binary_type)
        assert not isinstance(1, PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)
        assert not isinstance("", PyInfo.integer_types)
        assert isinstance(type, PyInfo.class_types)

# Generated at 2022-06-14 06:37:10.478743
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 == (sys.version_info[0] == 2)
    assert pyinfo.PY3 == (sys.version_info[0] == 3)

    if pyinfo.PY3:
        assert isinstance('', pyinfo.string_types)
        assert isinstance(b'', pyinfo.string_types)
        assert isinstance(u'', pyinfo.string_types)
        assert not isinstance(b'', pyinfo.binary_type)
        assert isinstance(b'', pyinfo.text_type)
        assert isinstance(u'', pyinfo.text_type)
        assert isinstance(u'', pyinfo.binary_type)
        assert not isinstance(b'', pyinfo.text_type)

# Generated at 2022-06-14 06:37:16.249010
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (2 == sys.version_info[0])
    assert PyInfo.PY3 == (3 == sys.version_info[0])

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

# Generated at 2022-06-14 06:37:28.553410
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert py_info.PyInfo.PY2 == (sys.version_info[0] == 2)
    if py_info.PyInfo.PY2:
        assert py_info.PyInfo.PY3 == False
        assert py_info.PyInfo.string_types == (basestring,)
        assert py_info.PyInfo.text_type == unicode
        assert py_info.PyInfo.binary_type == str
        assert py_info.PyInfo.integer_types == (int, long)
        assert py_info.PyInfo.class_types == (type, types.ClassType)
        if sys.platform.startswith("java"):
            # Jython always uses 32 bits.
            assert py_info.PyInfo.maxsize == int((1 << 31) - 1)

# Generated at 2022-06-14 06:37:42.103106
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()

    if PyInfo.PY3:
        assert pyinfo is not None
        assert isinstance(pyinfo.string_types, tuple)
        assert isinstance(pyinfo.string_types[0], type)
        assert pyinfo.string_types[0] == str

        assert isinstance(pyinfo.text_type, type)
        assert pyinfo.text_type == str

        assert isinstance(pyinfo.binary_type, type)
        assert pyinfo.binary_type == bytes

        assert isinstance(pyinfo.integer_types, tuple)
        assert isinstance(pyinfo.integer_types[0], type)
        assert pyinfo.integer_types[0] == int

        assert isinstance(pyinfo.class_types, tuple)

# Generated at 2022-06-14 06:37:54.372111
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 or pyinfo.PY3
    assert pyinfo.PY2 != pyinfo.PY3

    if pyinfo.PY2:
        assert isinstance("", pyinfo.string_types)
        assert isinstance(u"", pyinfo.string_types)
        assert not isinstance("", pyinfo.integer_types)
        assert not isinstance(u"", pyinfo.integer_types)
        assert not isinstance("", pyinfo.class_types)
        assert not isinstance(u"", pyinfo.class_types)

        assert not isinstance(1, pyinfo.string_types)

# Generated at 2022-06-14 06:37:59.004272
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert isinstance(PyInfo.maxsize, (int, long))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:38:05.669823
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    if pi.PY2:
        assert isinstance("", pi.string_types)
        assert isinstance(u'', pi.text_type)
        assert isinstance('', pi.binary_type)
        assert isinstance(5, pi.integer_types)

# Generated at 2022-06-14 06:38:14.910124
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)

    assert isinstance(unicode(""), PyInfo.string_types)
    assert isinstance(str(u""), PyInfo.string_types)

    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(str(b""), PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:38:26.778789
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 or pyinfo.PY3
    assert isinstance('test', pyinfo.string_types)
    assert isinstance(b'test', pyinfo.binary_type)
    assert isinstance(1, pyinfo.integer_types)
    assert isinstance(int, pyinfo.class_types)



# Generated at 2022-06-14 06:38:32.985707
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

# Generated at 2022-06-14 06:38:40.472403
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types in ((type, types.ClassType),
                                  (type,))  # Support Jython
    assert PyInfo.maxsize == ((1 << 63) - 1)

    sys.version_info = (2, 3, 4, "final", 0)
    reload(sys)
    reload(sklearn)
    reload(sklearn.base)
    reload(sklearn.base.PyInfo)
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_

# Generated at 2022-06-14 06:38:45.526414
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.binary_type == bytes
    assert PyInfo.text_type == str
    PyInfo.PY3 = False
    assert PyInfo.binary_type == str
    assert PyInfo.text_type == unicode


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:38:51.370023
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print(PyInfo.PY3)
    print(PyInfo.PY2)
    print(PyInfo.string_types)
    print(PyInfo.text_type)
    print(PyInfo.binary_type)
    print(PyInfo.integer_types)
    print(PyInfo.class_types)
    print(PyInfo.maxsize)

# Generated at 2022-06-14 06:38:57.667032
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance('a', PyInfo.string_types)
    assert not isinstance(1, PyInfo.string_types)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(sys, PyInfo.class_types)
    if PyInfo.PY2:
        assert isinstance(Long(0), PyInfo.integer_types)
    else:
        assert not isinstance(Long(0), PyInfo.integer_types)

# Generated at 2022-06-14 06:39:04.270347
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    PyInfo.PY2 = False
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    PyInfo.PY3 = False
    assert PyInfo.PY3 == (sys.version_info[0] == 3)



# Generated at 2022-06-14 06:39:07.424479
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3



# Generated at 2022-06-14 06:39:13.954284
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

# Generated at 2022-06-14 06:39:23.064065
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.PY2 != PyInfo.PY3
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize >= 0
    assert len(PyInfo.string_types) == 1
    assert len(PyInfo.text_type) == 1
    assert len(PyInfo.binary_type) == 1
    assert len(PyInfo.integer_types) == 2
    assert len(PyInfo.class_types) == 2



# Generated at 2022-06-14 06:39:44.901312
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from unittest import TestCase

    class TestPyInfo(TestCase):

        def test(self):
            self.assertTrue(PyInfo.PY2 ^ PyInfo.PY3)

            assert type(PyInfo.string_types) == tuple
            assert sys.version_info[0] == 2 and isinstance(PyInfo.string_types[0], basestring)
            assert sys.version_info[0] == 3 and isinstance(PyInfo.string_types[0], str)
            assert type(PyInfo.text_type) == type
            assert sys.version_info[0] == 2 and isinstance(PyInfo.text_type("test"), unicode)
            assert sys.version_info[0] == 3 and isinstance(PyInfo.text_type("test"), str)

# Generated at 2022-06-14 06:39:55.076281
# Unit test for constructor of class PyInfo
def test_PyInfo():
    info1 = PyInfo()
    info2 = PyInfo()
    assert info1.PY2 == info2.PY2 and info1.PY3 == info2.PY3
    assert info1.string_types == info2.string_types
    assert info1.text_type == info2.text_type
    assert info1.binary_type == info2.binary_type
    assert info1.integer_types == info2.integer_types
    assert info1.class_types == info2.class_types
    assert info1.maxsize == info2.maxsize



# Generated at 2022-06-14 06:39:59.461991
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('string', PyInfo.string_types)

    assert isinstance(b'bytes', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert PyInfo.maxsize > (1 << 31)


# 编码和解码

# Generated at 2022-06-14 06:40:11.571211
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys

    py2 = sys.version_info[0] == 2
    py3 = sys.version_info[0] == 3

    assert PyInfo.PY2 == py2
    assert PyInfo.PY3 == py3

    if py2:
        assert PyInfo.string_types == basestring
        assert PyInfo.text_type == unicode
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)
        assert PyInfo.binary_type == str
        assert isinstance("", PyInfo.binary_type)
    else:
        assert PyInfo.string_types == str
        assert PyInfo.text_type == str
        assert PyInfo.integer_types == int
        assert PyInfo.class_types == type
        assert PyInfo

# Generated at 2022-06-14 06:40:13.265205
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:40:17.692568
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert "Py2" in repr(PyInfo)
    else:
        assert "Py3" in repr(PyInfo)

# Generated at 2022-06-14 06:40:18.788805
# Unit test for constructor of class PyInfo
def test_PyInfo():
    with pytest.raises(AttributeError):
        PyInfo().PY4



# Generated at 2022-06-14 06:40:31.358462
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    import platform

    assert PyInfo.PY2 or PyInfo.PY3
    assert len(PyInfo.string_types) == 1
    assert len(PyInfo.integer_types) == 2
    assert PyInfo.text_type == 'hello'

    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.maxsize == sys.maxsize
    else:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.maxsize == sys.maxint



# Generated at 2022-06-14 06:40:44.547408
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 == sys.version_info[0] == 2
    assert pyinfo.PY3 == sys.version_info[0] == 3
    assert pyinfo.string_types == sys.version_info[0] == 2 and (
        basestring,
    ) or (str,)
    assert pyinfo.text_type == sys.version_info[0] == 2 and unicode or str
    assert pyinfo.binary_type == sys.version_info[0] == 2 and str or bytes
    assert pyinfo.integer_types == sys.version_info[0] == 2 and (
        int,
        long,
    ) or (int,)

# Generated at 2022-06-14 06:40:57.169269
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert not isinstance(b'', PyInfo.string_types)
    assert isinstance(u'', PyInfo.text_type)
    assert not isinstance('', PyInfo.text_type)
    assert not isinstance(b'', PyInfo.text_type)
    assert isinstance(b'', PyInfo.binary_type)
    assert not isinstance('', PyInfo.binary_type)
    assert not isinstance(u'', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:41:27.620303
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, (int, long))


if __name__ == "__main__":
    test_PyInfo()
    print("Test finished")

# Generated at 2022-06-14 06:41:37.239004
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # PY2 or PY3
    assert PyInfo.string_types

    # PY2 or PY3
    assert PyInfo.text_type

    # PY2 or PY3
    assert PyInfo.binary_type

    # PY2 or PY3
    assert PyInfo.integer_types

    # PY2 or PY3
    assert PyInfo.class_types

    # PY2 or PY3
    assert PyInfo.maxsize

    # PY2 or PY3
    assert PyInfo.PY2 or PyInfo.PY3


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:41:39.214055
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.maxsize == sys.maxsize



# Generated at 2022-06-14 06:41:46.204913
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert type("") in PyInfo.string_types
    assert isinstance("", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)
    assert isinstance(type, PyInfo.class_types)



# Generated at 2022-06-14 06:41:56.758149
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert 'bytes' not in dir(__builtins__)
    if PyInfo.PY3:
        assert 'unicode' not in dir(__builtins__)

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance('a', PyInfo.string_types)
    assert isinstance(u'a', PyInfo.text_type)
    assert isinstance(b'a', PyInfo.binary_type)

    assert isinstance(PyInfo, PyInfo.class_types)
    assert PyInfo.maxsize > 0


# ----------------------------------------------------------------------
# |
# |  Public Functions
# |
# ----------------------------------------------------------------------

# Generated at 2022-06-14 06:42:03.212171
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance("test", PyInfo.string_types)
        assert isinstance(b"test", PyInfo.binary_type)
    elif PyInfo.PY3:
        assert isinstance("test", PyInfo.string_types)
        assert not isinstance(b"test", PyInfo.binary_type)



# Generated at 2022-06-14 06:42:07.989936
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert isinstance(PyInfo.string_types, tuple)

# Generated at 2022-06-14 06:42:22.175106
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert (PyInfo.PY2 or PyInfo.PY3) is True
    assert PyInfo.string_types is not None
    assert PyInfo.text_type is not None
    assert PyInfo.binary_type is not None
    assert PyInfo.maxsize is not None
    assert PyInfo.class_types is not None
    assert PyInfo.integer_types is not None
    assert isinstance(PyInfo.maxsize, int)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.integer_types, tuple)

# Generated at 2022-06-14 06:42:29.268798
# Unit test for constructor of class PyInfo
def test_PyInfo():
    i = PyInfo()
    assert isinstance(i.PY2, bool), "PY2 is not a boolean"
    assert isinstance(i.PY3, bool), "PY3 is not a boolean"
    assert isinstance(i.string_types, tuple), "string_types is not a tuple"
    assert isinstance(i.text_type, type), "text_type is not a type"
    assert isinstance(i.binary_type, type), "binary_type is not a type"
    assert isinstance(i.integer_types, tuple), "integer_types is not a tuple"
    assert isinstance(i.class_types, tuple), "class_types is not a tuple"
    assert isinstance(i.maxsize, int), "maxsize is not an int"

# Generated at 2022-06-14 06:42:34.488530
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:43:24.798899
# Unit test for constructor of class PyInfo
def test_PyInfo():
    attr_list = [
        "PY2",
        "PY3",
        "string_types",
        "text_type",
        "binary_type",
        "integer_types",
        "class_types",
        "maxsize",
    ]
    for attr in attr_list:
        assert getattr(PyInfo, attr) is not None

# Generated at 2022-06-14 06:43:33.632909
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:43:36.870563
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert sys.version_info[0] == 2



# Generated at 2022-06-14 06:43:48.806175
# Unit test for constructor of class PyInfo
def test_PyInfo():

    pyinfo = PyInfo()
    print("PY2: " + str(pyinfo.PY2))
    print("PY3: " + str(pyinfo.PY3))
    print("string_types: " + str(pyinfo.string_types))
    print("text_type: " + str(pyinfo.text_type))
    print("binary_type: " + str(pyinfo.binary_type))
    print("integer_types: " + str(pyinfo.integer_types))
    print("class_types: " + str(pyinfo.class_types))
    print("maxsize: " + str(pyinfo.maxsize))



# Generated at 2022-06-14 06:43:54.120543
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is True
    assert PyInfo.string_types is True
    assert PyInfo.text_type is True
    assert PyInfo.binary_type is True
    assert PyInfo.integer_types is True
    assert PyInfo.class_types is True
    assert PyInfo.maxsize is True

# Generated at 2022-06-14 06:44:07.604031
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    if PyInfo.PY2:
        assert isinstance('text', PyInfo.string_types)
        assert PyInfo.text_type is unicode
        assert PyInfo.binary_type is str
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(PyInfo, PyInfo.class_types)
        assert PyInfo.maxsize == sys.maxsize
    else:
        assert isinstance('text', PyInfo.string_types)
        assert PyInfo.text_type is str
        assert PyInfo.binary_type is bytes
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:44:20.119305
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("hello", PyInfo.string_types)
    assert isinstance(u"hello", PyInfo.string_types)
    assert isinstance(b"hello", PyInfo.binary_type)
    assert isinstance(2, PyInfo.integer_types)
    assert isinstance(2 ** 64, PyInfo.integer_types)
    assert not isinstance(2 ** 64 + 1, PyInfo.integer_types)


string_types = PyInfo.string_types
text_type = PyInfo.text_type
binary_type = PyInfo.binary_type
integer_types = PyInfo.integer_types
class_types = PyInfo.class_types
maxsize = PyInfo.maxsize

# Generated at 2022-06-14 06:44:24.481541
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == 1
    assert PyInfo.PY3 == 0
    assert PyInfo.maxsize == 2147483647


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:44:37.949832
# Unit test for constructor of class PyInfo

# Generated at 2022-06-14 06:44:44.516761
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert str in PyInfo.string_types
        assert unicode in PyInfo.string_types
        assert isinstance('a', PyInfo.string_types)

        assert PyInfo.binary_type == str
        assert PyInfo.maxsize == sys.maxsize
    else:
        assert str in PyInfo.string_types
        assert isinstance('a', PyInfo.string_types)
        assert not isinstance(u'a', PyInfo.string_types)

        assert PyInfo.binary_type == bytes
        assert PyInfo.maxsize == sys.maxsize


if __name__ == '__main__':
    test_PyInfo()