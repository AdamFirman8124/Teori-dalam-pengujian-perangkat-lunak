

# Generated at 2022-06-14 06:35:44.449543
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.text_type)
    assert not isinstance("", PyInfo.binary_type)
    assert isinstance(b"", PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:35:54.606301
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3

    assert isinstance(u'', PyInfo.text_type)
    assert isinstance('', PyInfo.binary_type)
    assert isinstance(0, PyInfo.integer_types)
    assert isinstance((), PyInfo.class_types)

    # Python 3.3+ has a sys.maxsize of 9223372036854775807 (64 bits)
    # Python 3.2 has a sys.mazsize of 2147483647 (32 bits)
    # Python 2.7.x has a sys.maxsize of 9223372036854775807 (64 bits)
    # Python 2.6.x has a sys.maxsize of 2147483647 (32 bits)

    # const long maxsize = ((sizeof(ssize_t) == sizeof

# Generated at 2022-06-14 06:35:59.385986
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True
    assert PyInfo.PY3 is False

    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)

    # Take care of 64-bit system
    assert PyInfo.maxsize in (2147483647, 9223372036854775807)

# Generated at 2022-06-14 06:36:04.255248
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3, "Should be Python 2 or Python 3"
    assert isinstance("", PyInfo.string_types)
    assert isinstance(u"", PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(type, PyInfo.class_types)
    assert PyInfo.maxsize > 0



# Generated at 2022-06-14 06:36:17.707106
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # prove that the object is a Singleton
    assert PyInfo() is PyInfo()

    # prove that the field "PY2" and "PY3" are correct
    assert PyInfo.PY2 is not PyInfo.PY3
    assert PyInfo.PY2 is (sys.version_info[0] == 2)
    assert PyInfo.PY3 is (sys.version_info[0] == 3)

    # prove that the fields "string_types", "text_type", "binary_type",
    # "integer_types" and "class_types" are correct
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)

# Generated at 2022-06-14 06:36:21.817736
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert not PyInfo.PY3
    else:
        assert PyInfo.PY3

# Generated at 2022-06-14 06:36:35.413993
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is True or PyInfo.PY3 is True
    assert isinstance('', PyInfo.string_types)
    assert isinstance(u'', PyInfo.string_types)
    assert isinstance(b'', PyInfo.string_types)
    assert isinstance('', PyInfo.text_type)
    assert isinstance(u'', PyInfo.text_type)
    assert not isinstance(b'', PyInfo.text_type)
    assert isinstance(b'', PyInfo.binary_type)
    assert not isinstance(u'', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1000000000, PyInfo.integer_types)
    assert not isinstance(1.0, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:45.538095
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo().string_types, tuple)
    assert isinstance(PyInfo().text_type, type)
    assert isinstance(PyInfo().binary_type, type)
    assert isinstance(PyInfo().integer_types, tuple)
    assert isinstance(PyInfo().class_types, tuple)
    assert isinstance(PyInfo().maxsize, int)


if __name__ == "__main__":
    import sys
    import os

    basename = os.path.basename(sys.argv[0])
    if basename == "__init__.py" or basename.startswith("test_"):
        import unittest

        basename = os.path.splitext(basename)[0]

# Generated at 2022-06-14 06:36:56.566580
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY3 or PyInfo.PY2
    assert isinstance('', PyInfo.string_types)
    assert isinstance(b'', PyInfo.binary_type)
    assert isinstance(b'', PyInfo.string_types)
    assert not isinstance(b'', PyInfo.text_type)
    assert isinstance(u'', PyInfo.string_types)
    assert isinstance(u'', PyInfo.text_type)
    assert not isinstance(u'', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, int)
    assert not isinstance(1, str)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, int)
    assert not isinstance(1, str)

# Generated at 2022-06-14 06:36:57.470948
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:37:08.252341
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)

    if PyInfo.PY3:
        assert type(u"") == PyInfo.string_types[0]
    else:
        assert type(u"") in PyInfo.string_types
    if PyInfo.PY3:
        assert type(u"") == PyInfo.text_type
    else:
        assert type(u"") == PyInfo.text_type
    assert type(b"") == PyInfo.binary_type

# Generated at 2022-06-14 06:37:12.167830
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert PyInfo.maxsize > 0
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:37:18.845634
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY3:
        assert isinstance(1, PyInfo.integer_types)
    else:
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:37:21.775281
# Unit test for constructor of class PyInfo
def test_PyInfo():
    try:
        PyInfo()
    except:
        pass

# Generated at 2022-06-14 06:37:31.874214
# Unit test for constructor of class PyInfo
def test_PyInfo():
    test_py2 = "python2.7.9"
    test_py3 = "python3.7.0"
    sys.version = test_py2
    assert isinstance(PyInfo.PY2, bool)
    assert not PyInfo.PY2
    assert isinstance(PyInfo.PY3, bool)
    assert PyInfo.PY3
    sys.version = test_py3
    assert isinstance(PyInfo.PY2, bool)
    assert PyInfo.PY2
    assert isinstance(PyInfo.PY3, bool)
    assert not PyInfo.PY3
    sys.version = sys.version


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:37:36.196233
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == True or PyInfo.PY3 == True
    assert PyInfo.maxsize >= 0


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:37:46.648720
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.string_types, type(tuple)), "string_types = %s not %s" % (type(PyInfo.string_types), type(tuple))
    assert isinstance(PyInfo.string_types[0], type(str)), "string_types[0] = %s not %s" % (type(PyInfo.string_types[0]), type(str))
    assert isinstance(PyInfo.text_type, type(str)), "text_type = %s not %s" % (type(PyInfo.text_type), type(str))
    assert isinstance(PyInfo.binary_type, type(bytes)), "binary_type = %s not %s" % (type(PyInfo.binary_type), type(bytes))

# Generated at 2022-06-14 06:37:53.316623
# Unit test for constructor of class PyInfo
def test_PyInfo():
    test_PY3 = PyInfo.PY3
    test_PY2 = PyInfo.PY2

    if sys.version_info[0] == 3:
        assert (PyInfo.PY3) is True
        assert (PyInfo.PY2) is False
    else:  # PY2
        assert (PyInfo.PY2) is True
        assert (PyInfo.PY3) is False



# Generated at 2022-06-14 06:38:04.477423
# Unit test for constructor of class PyInfo
def test_PyInfo():
    p = PyInfo()
    assert p.PY2 == (sys.version_info[0] == 2)
    assert p.PY3 == (sys.version_info[0] == 3)
    assert p.string_types == basestring if p.PY2 else (str,)
    assert p.text_type == unicode if p.PY2 else str
    assert p.binary_type == str if p.PY2 else bytes
    assert p.integer_types == (int, long) if p.PY2 else (int,)
    assert p.class_types == (type, types.ClassType) if p.PY2 else (type,)
    assert p.maxsize == sys.maxsize if p.PY3 else sys.maxsize - 1


PY2 = PyInfo.PY2
PY3

# Generated at 2022-06-14 06:38:07.739358
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)

# Generated at 2022-06-14 06:38:19.796637
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()

    assert pi.PY2 or pi.PY3, "not PY2 or PY3"
    assert isinstance("s", pi.string_types), "not string in string_types"
    assert isinstance("s", pi.text_type), "not string in text_type"
    assert isinstance("s", pi.binary_type), "not string in binary_type"
    assert isinstance(1, pi.integer_types), "not int in integer_types"
    assert isinstance(
        type(lambda: 1), pi.class_types), "not type in class_types"
    assert pi.maxsize in (2147483647, 9223372036854775807), "not maxsize"


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:31.529497
# Unit test for constructor of class PyInfo
def test_PyInfo():
    class A(object):
        pass

    assert PyInfo.PY3 or PyInfo.PY2
    assert not (PyInfo.PY3 and PyInfo.PY2)
    assert isinstance("a", PyInfo.string_types)
    assert isinstance("a", PyInfo.text_type)
    assert isinstance("a", PyInfo.string_types)
    assert isinstance("a", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(PyInfo, PyInfo.class_types)
    assert isinstance(A, PyInfo.class_types)
    assert PyInfo.maxsize == 9223372036854775807



# Generated at 2022-06-14 06:38:35.263529
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert (PyInfo.PY2 and not PyInfo.PY3) or (not PyInfo.PY2 and PyInfo.PY3)


if __name__ == '__main__':
    pytest.main([__file__, '-v', '-s'])

# Generated at 2022-06-14 06:38:44.190438
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def check_PyInfo(py_info):
        assert type(py_info.PY2) == bool
        assert type(py_info.PY3) == bool
        assert type(py_info.string_types) == tuple
        assert type(py_info.text_type) == type
        assert type(py_info.binary_type) == type
        assert type(py_info.integer_types) == tuple
        assert type(py_info.maxsize) == int

    check_PyInfo(PyInfo())

# Generated at 2022-06-14 06:38:53.146459
# Unit test for constructor of class PyInfo
def test_PyInfo():
    translate_this = {
        'py2_msg': 'PY2=%s',
        'py3_msg': 'PY3=%s',
        'string_types_msg': 'string_types=%s',
        'text_type_msg': 'text_type=%s, binary_type=%s, integer_types=%s, class_types=%s, maxsize=%s',
    }
    print(translate_this['py2_msg'] % str(PyInfo.PY2))
    print(translate_this['py3_msg'] % str(PyInfo.PY3))
    print(translate_this['string_types_msg'] % str(PyInfo.string_types))

# Generated at 2022-06-14 06:38:56.528975
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo().PY2 is True
    assert PyInfo().PY3 is False


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:39:03.757312
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(5, PyInfo.integer_types)
    assert isinstance(5, PyInfo.integer_types)
    assert isinstance(5, PyInfo.integer_types)
    assert isinstance(5, PyInfo.integer_types)



# Generated at 2022-06-14 06:39:07.690785
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.text_type(), PyInfo.string_types)
    assert isinstance(PyInfo.binary_type(), PyInfo.string_types)
    assert isinstance(2, PyInfo.integer_types)

# Generated at 2022-06-14 06:39:11.954979
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3


# or call directly from the Python interpreter
if __name__ == '__main__':
    print('Py2={}, Py3={}'.format(PyInfo.PY2, PyInfo.PY3))

# Generated at 2022-06-14 06:39:16.492546
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """unit test for constructor of class PyInfo"""


if __name__ == '__main__':
    pyfunc_logging.debug = True
    logger = logging.getLogger('PyInfo')
    logger.setLevel(logging.DEBUG)
    test_PyInfo()

# Generated at 2022-06-14 06:39:39.110404
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance("s", PyInfo.string_types)
        assert isinstance(u"s", PyInfo.string_types)
        assert not isinstance(b"s", PyInfo.string_types)
        assert isinstance("s", PyInfo.text_type)
        assert not isinstance(u"s", PyInfo.text_type)
        assert isinstance(b"s", PyInfo.binary_type)
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:39:41.609602
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Check if Python version properly detected
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:39:49.925463
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert PyInfo.text_type is PyInfo.string_types[0]
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert PyInfo.class_types is PyInfo.integer_types[0]
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:40:00.326301
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 is False
    assert pyinfo.PY3 is True

    assert pyinfo.string_types == (str,)
    assert pyinfo.text_type == str
    assert pyinfo.binary_type == bytes
    assert pyinfo.integer_types == (int,)
    assert pyinfo.class_types == (type,)

    assert pyinfo.maxsize == (1 << 63) - 1

    assert pyinfo.PY2 is not True
    assert pyinfo.PY2 is not False
    assert pyinfo.PY3 is not True
    assert pyinfo.PY3 is not False

    assert pyinfo.string_types is not (str, bytes)
    assert pyinfo.string_types is not (str, bytes, bytearray)
    assert pyinfo.text_

# Generated at 2022-06-14 06:40:06.559286
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert not PyInfo.PY2
    assert PyInfo.PY3
    assert PyInfo.string_types == (str,)
    assert PyInfo.text_type == str
    assert PyInfo.binary_type == bytes
    assert PyInfo.integer_types == (int,)
    assert PyInfo.class_types == (type,)
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:40:16.383240
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str
        assert PyInfo.integer_types == (int, long)
        assert PyInfo.class_types == (type, types.ClassType)

    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)

    # Default maxsize is 2^31
    assert PyInfo.maxsize == 2147483647

# Generated at 2022-06-14 06:40:21.026694
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == (1 << 31) - 1

# Generated at 2022-06-14 06:40:27.360222
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not None and isinstance(PyInfo.PY2, bool)
    assert PyInfo.PY3 is not None and isinstance(PyInfo.PY3, bool)
    assert PyInfo.maxsize is not None and isinstance(PyInfo.maxsize, int)
    assert PyInfo.string_types is not None and isinstance(PyInfo.string_types, tuple)
    assert PyInfo.binary_type is not None and isinstance(PyInfo.binary_type, type)
    assert PyInfo.integer_types is not None and isinstance(PyInfo.integer_types, tuple)
    assert PyInfo.class_types is not None and isinstance(PyInfo.class_types, tuple)


# Generated at 2022-06-14 06:40:32.051339
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert type(PyInfo.maxsize) is int
    assert PyInfo.maxsize > 0
    assert sys.maxint in PyInfo.integer_types
    assert sys.maxint == PyInfo.maxsize
    assert PyInfo.PY2 or PyInfo.PY3

# Generated at 2022-06-14 06:40:43.122921
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
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
        assert PyInfo.class_types == (type,)

# Generated at 2022-06-14 06:41:04.361330
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys

    assert PyInfo.PY2 is (sys.version_info[0] == 2)
    assert PyInfo.PY3 is (sys.version_info[0] == 3)

    info = PyInfo()
    assert info.PY2 is (sys.version_info[0] == 2)
    assert info.PY3 is (sys.version_info[0] == 3)

# Generated at 2022-06-14 06:41:18.400755
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # check if PyInfo's members are valid
    assert PyInfo.PY2 != PyInfo.PY3
    assert not (PyInfo.PY2 and PyInfo.PY3)
    assert type(PyInfo.PY2) is bool
    assert type(PyInfo.PY3) is bool

    # type attribute string_types
    assert isinstance("test", PyInfo.string_types)
    assert not isinstance(2, PyInfo.string_types)

    # type attribute integer_types
    assert isinstance(1, PyInfo.integer_types)
    assert not isinstance("test", PyInfo.integer_types)

    # type attribute text_type
    assert isinstance("test", PyInfo.text_type)
    assert not isinstance(1, PyInfo.text_type)

    # type attribute binary_type


# Generated at 2022-06-14 06:41:29.171753
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info >= (2, 0))
    assert PyInfo.PY3 == (sys.version_info >= (3, 0))
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)


# Get PyInfo object
py_info = PyInfo()

# Generated at 2022-06-14 06:41:40.098272
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

# Generated at 2022-06-14 06:41:51.710297
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # test PY2, PY3
    assert (PyInfo.PY2 != PyInfo.PY3)

    # test string_types
    assert (isinstance('', (PyInfo.string_types)))
    assert (isinstance(u'', (PyInfo.string_types)))
    assert (not isinstance(1, (PyInfo.string_types)))

    # test text_type
    assert (isinstance('', (PyInfo.text_type)))
    assert (isinstance(u'', (PyInfo.text_type)))
    assert (not isinstance(1, (PyInfo.text_type)))
    assert (not isinstance((), (PyInfo.text_type)))

    # test binary_type
    assert (isinstance('', (PyInfo.binary_type)))

# Generated at 2022-06-14 06:42:05.015253
# Unit test for constructor of class PyInfo
def test_PyInfo():
    def test(name, expected, value):
        if value == expected:
            print("{} == {}".format(name, value))
            return True
        else:
            print("{} == {} != {}".format(name, value, expected))
            return False

    import sys
    import types

    is_py2 = (2, 7) == sys.version_info[:2]
    is_py3 = (3, 4) == sys.version_info[:2]
    is_64bit = sys.maxsize > 2 ** 32

    # string type
    if is_py2:
        assert type("foo") == str
        assert issubclass(str, basestring)
    else:
        assert type("foo") == str
        assert not issubclass(str, basestring)

    # basestring


# Generated at 2022-06-14 06:42:11.780661
# Unit test for constructor of class PyInfo
def test_PyInfo():
    _ = PyInfo()
    return


py2 = PyInfo.PY2
py3 = PyInfo.PY3

string_types = PyInfo.string_types
text_type = PyInfo.text_type
binary_type = PyInfo.binary_type
integer_types = PyInfo.integer_types
class_types = PyInfo.class_types

maxsize = PyInfo.maxsize

# Generated at 2022-06-14 06:42:20.502682
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert not PyInfo.PY3
    assert PyInfo.PY2
    assert PyInfo.string_types == (basestring,)
    assert PyInfo.text_type == unicode
    assert PyInfo.binary_type == str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:42:31.195279
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    assert pi.PY2 or pi.PY3
    assert isinstance(pi.string_types, tuple)
    assert isinstance(pi.text_type, type)
    assert isinstance(pi.binary_type, type)
    assert isinstance(pi.integer_types, tuple)
    assert isinstance(pi.class_types, tuple)
    assert isinstance(pi.maxsize, int)

    assert pi.PY2 ^ pi.PY3
    assert pi.text_type() != pi.binary_type()
    assert isinstance(pi.text_type(), pi.string_types)
    assert isinstance(pi.binary_type(), pi.string_types)
    assert isinstance(1, pi.integer_types)
    assert isinstance(1, pi.integer_types)
   

# Generated at 2022-06-14 06:42:33.590620
# Unit test for constructor of class PyInfo
def test_PyInfo():
    test_PyInfo_PY2()
    test_PyInfo_PY3()



# Generated at 2022-06-14 06:43:23.622844
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3
    assert isinstance('s', PyInfo.string_types)
    assert not isinstance(b'\x00', PyInfo.text_type)
    assert isinstance(b'\x00', PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(type, PyInfo.class_types)
    assert isinstance(sys.maxsize, int)
    assert PyInfo.maxsize >= sys.maxsize

if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:43:25.911099
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is (2 == sys.version_info[0])
    assert PyInfo.PY3 is (3 == sys.version_info[0])

# Generated at 2022-06-14 06:43:36.492368
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import platform
    import sys

    from .info import PyInfo

    is_64 = platform.architecture()[0] == "64bit"
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert (
        PyInfo.maxsize == (sys.maxsize if sys.version_info[0] == 3 else (1 << 63) - 1)
        if is_64
        else ((1 << 31) - 1)
    )
    assert (
        PyInfo.maxsize == (sys.maxsize if sys.version_info[0] == 3 else (1 << 63) - 1)
        if is_64
        else ((1 << 31) - 1)
    )



# Generated at 2022-06-14 06:43:44.700500
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance("str", PyInfo.string_types)
    assert isinstance(u"unicode", PyInfo.string_types)
    assert isinstance(b"bytes", PyInfo.binary_type)
    assert isinstance(10, PyInfo.integer_types)
    assert isinstance(int, PyInfo.class_types)
    if PyInfo.PY2:
        assert isinstance(long(1), PyInfo.integer_types)
        assert isinstance(int, PyInfo.class_types)

# Generated at 2022-06-14 06:43:52.701094
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert (
            PyInfo.string_types == (basestring,)
        ), "PyInfo.string_types for Py2 is not as expected"
        assert PyInfo.text_type == unicode, "PyInfo.text_type for Py2 is not as expected"
        assert PyInfo.binary_type == str, "PyInfo.binary_type for Py2 is not as expected"
        assert (
            PyInfo.integer_types == (int, long)
        ), "PyInfo.integer_types for Py2 is not as expected"
        assert (
            PyInfo.class_types == (type, types.ClassType)
        ), "PyInfo.class_types for Py2 is not as expected"

# Generated at 2022-06-14 06:43:58.783281
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert type(next(iter(PyInfo.string_types))) is type("")
        assert type(PyInfo.maxsize) is type(2 ** 31 - 1)
    else:  # PY3
        assert type(next(iter(PyInfo.string_types))) is type("")
        assert type(PyInfo.maxsize) is type(2 ** 63 - 1)

# Generated at 2022-06-14 06:44:09.086555
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from datetime import datetime
    from datetime import timedelta
    from datetime import tzinfo

    class MyTzInfo(tzinfo):

        def utcoffset(self, dt):
            return timedelta(hours=9)

        def dst(self, dt):
            return timedelta(0)

        def tzname(self, dt):
            return "+0900"

    dt = datetime(2013, 2, 20, 12, 0, 0, 0)
    dt_jp = dt.replace(tzinfo=MyTzInfo())
    dt_str = dt_jp.isoformat()


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:44:11.013631
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3



# Generated at 2022-06-14 06:44:23.936700
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

# Generated at 2022-06-14 06:44:33.109314
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # PY2
    assert isinstance(PyInfo.string_types[0], basestring)
    assert isinstance(PyInfo.text_type, unicode)
    assert isinstance(PyInfo.binary_type, str)
    assert isinstance(PyInfo.integer_types[0], int)
    assert isinstance(PyInfo.integer_types[1], long)
    assert isinstance(PyInfo.class_types[0], type)
    assert isinstance(PyInfo.class_types[1], types.ClassType)

    # PY3
    assert isinstance(PyInfo.string_types[0], str)
    assert isinstance(PyInfo.text_type, str)
    assert isinstance(PyInfo.binary_type, bytes)
    assert isinstance(PyInfo.integer_types[0], int)