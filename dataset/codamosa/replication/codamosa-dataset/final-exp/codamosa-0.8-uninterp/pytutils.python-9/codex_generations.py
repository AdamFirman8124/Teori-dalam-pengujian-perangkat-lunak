

# Generated at 2022-06-14 06:35:49.003588
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert not PyInfo.PY3
    assert isinstance("", PyInfo.string_types)
    assert isinstance(b"", PyInfo.string_types)
    assert not isinstance(u"", PyInfo.string_types)
    assert isinstance("", PyInfo.text_type)
    assert not isinstance(b"", PyInfo.text_type)
    assert isinstance(u"", PyInfo.text_type)
    assert isinstance(b"", PyInfo.binary_type)
    assert not isinstance("", PyInfo.binary_type)
    assert not isinstance(u"", PyInfo.binary_type)
    assert isinstance(1, PyInfo.integer_types)
    assert not isinstance(1.1, PyInfo.integer_types)

# Generated at 2022-06-14 06:35:57.279086
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

    # Test string_types
    assert isinstance("", PyInfo.string_types)

    # Test text_type
    assert issubclass(PyInfo.text_type, PyInfo.string_types)

    # Test binary_type
    assert issubclass(PyInfo.binary_type, PyInfo.string_types)
    assert isinstance(b"", PyInfo.binary_type)

    # Test integer_types
    if PyInfo.PY2:
        assert isinstance(1, PyInfo.integer_types)

# Generated at 2022-06-14 06:36:01.224655
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 | PyInfo.PY3
    assert type(PyInfo.PY2) == bool
    assert type(PyInfo.PY3) == bool
    assert type(PyInfo.string_types) == tuple
    assert type(PyInfo.string_types[0]) == type


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:36:08.940882
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import unittest

    class TestCase(unittest.TestCase):
        def test_PyInfo(self):
            self.assertIsNotNone(PyInfo)

            self.assertIsInstance(PyInfo.string_types, tuple)
            self.assertIsInstance(PyInfo.integer_types, tuple)
            self.assertIsInstance(PyInfo.class_types, tuple)

            self.assertIsInstance(PyInfo.text_type, type)
            self.assertIsInstance(PyInfo.binary_type, type)

    

# Generated at 2022-06-14 06:36:17.643763
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



# Generated at 2022-06-14 06:36:26.503110
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo().PY2 == (sys.version_info[0] == 2)
    assert PyInfo().PY3 == (sys.version_info[0] == 3)
    if PyInfo().PY3:
        assert PyInfo().string_types == (str,)
        assert PyInfo().text_type == str
        assert PyInfo().binary_type == bytes
        assert PyInfo().integer_types == (int,)
        assert PyInfo().class_types == (type,)
    else:  # PY2
        assert PyInfo().string_types == (basestring,)
        assert PyInfo().text_type == unicode
        assert PyInfo().binary_type == str
        assert PyInfo().integer_types == (int, long)
        assert PyInfo().class_types == (type, types.ClassType)
    assert PyInfo

# Generated at 2022-06-14 06:36:38.919409
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)
    assert PyInfo.PY2 != PyInfo.PY3

    if PyInfo.PY3:
        assert PyInfo.string_types == (str,)
        assert PyInfo.text_type == str
        assert PyInfo.binary_type == bytes
        assert PyInfo.integer_types == (int,)
        assert PyInfo.class_types == (type,)
        assert PyInfo.maxsize == sys.maxsize
    else:  # PyInfo.PY2
        assert PyInfo.string_types == (basestring,)
        assert PyInfo.text_type == unicode
        assert PyInfo.binary_type == str

# Generated at 2022-06-14 06:36:44.548831
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2
    assert PyInfo.string_types == (str, unicode)
    assert PyInfo.text_type is unicode
    assert PyInfo.binary_type is str
    assert PyInfo.integer_types == (int, long)
    assert PyInfo.class_types == (type, types.ClassType)
    assert PyInfo.maxsize == sys.maxsize

    assert sys.maxsize > 2 ** 32
    assert PyInfo().PY2



# Generated at 2022-06-14 06:36:56.205394
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance('abc', PyInfo.string_types)
        assert isinstance(u'abc', PyInfo.string_types)
        assert not isinstance(b'abc', PyInfo.string_types)
    else:
        assert not isinstance('abc', PyInfo.string_types)
        assert not isinstance(u'abc', PyInfo.string_types)
        assert isinstance(b'abc', PyInfo.string_types)

    assert isinstance('abc', PyInfo.text_type)
    assert isinstance(b'abc', PyInfo.binary_type)

    assert isinstance(1, PyInfo.integer_types)
    assert isinstance(1, PyInfo.class_types)

    assert isinstance(type(1), PyInfo.class_types)


test_PyInfo

# Generated at 2022-06-14 06:36:58.054967
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert(PyInfo.PY2 or PyInfo.PY3)



# Generated at 2022-06-14 06:37:03.337358
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert(PyInfo.class_types == (type, types.ClassType))
    else:
        assert(PyInfo.class_types == type)


# Used for unit test of class DictWrapper

# Generated at 2022-06-14 06:37:08.284860
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    Test PyInfo

    :return: Nothing
    """
    print(PyInfo.PY2)
    print(PyInfo.PY3)
    print(PyInfo.string_types)
    print(PyInfo.text_type)
    print(PyInfo.binary_type)
    print(PyInfo.integer_types)
    print(PyInfo.class_types)
    print(PyInfo.maxsize)


# test_PyInfo()

# Generated at 2022-06-14 06:37:13.902237
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance(u'\u077d', PyInfo.string_types)
    else:
        assert isinstance(1, PyInfo.integer_types)
        assert isinstance('\u077d', PyInfo.string_types)



# Generated at 2022-06-14 06:37:18.494738
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.maxsize == 9223372036854775807
    else:
        assert PyInfo.maxsize == 2147483647


if __name__ == '__main__':
    import pytest
    pytest.main()

# Generated at 2022-06-14 06:37:26.633387
# Unit test for constructor of class PyInfo
def test_PyInfo():
    isinstance("a", PyInfo.string_types)
    isinstance(u"a", PyInfo.string_types)
    isinstance(b"a", PyInfo.binary_type)
    assert not isinstance("a", PyInfo.binary_type)
    assert not isinstance(u"a", PyInfo.binary_type)
    assert not isinstance(b"a", PyInfo.string_types)
    assert not isinstance(b"a", PyInfo.text_type)


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:37:28.906029
# Unit test for constructor of class PyInfo
def test_PyInfo():
    """
    Returns PyInfo class object
    """
    assert isinstance(PyInfo(), PyInfo)



# Generated at 2022-06-14 06:37:38.704973
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance("", PyInfo.string_types)
        assert not isinstance(b"", PyInfo.string_types)

        assert isinstance(u"", PyInfo.text_type)
    else:
        assert isinstance("", PyInfo.string_types)
        assert isinstance(b"", PyInfo.string_types)

        assert isinstance("", PyInfo.text_type)


if __name__ == "__main__":
    import nose

    nose.runmodule()

# Generated at 2022-06-14 06:37:50.293387
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import textwrap

    lines = textwrap.dedent(
        """
        PY2 = {}
        PY3 = {}
        string_types = {}
        text_type = {}
        binary_type = {}
        integer_types = {}
        class_types = {}
        maxsize = {}
        """.format(
            PyInfo.PY2,
            PyInfo.PY3,
            repr(PyInfo.string_types),
            repr(PyInfo.text_type),
            repr(PyInfo.binary_type),
            repr(PyInfo.integer_types),
            repr(PyInfo.class_types),
            repr(PyInfo.maxsize),
        )
    )

    assert lines == __doc__


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:00.496616
# Unit test for constructor of class PyInfo
def test_PyInfo():
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
        assert PyInfo.class_types == (type, types.ClassType)

# Generated at 2022-06-14 06:38:02.297213
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:38:09.562175
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == (sys.version_info[0] == 2)
    assert PyInfo.PY3 == (sys.version_info[0] == 3)

# Generated at 2022-06-14 06:38:16.764415
# Unit test for constructor of class PyInfo
def test_PyInfo():
    print(PyInfo.PY3)
    print(PyInfo.PY2)
    print(type(PyInfo.PY3))
    print(type(PyInfo.PY2))
    print(PyInfo.text_type)
    print(PyInfo.string_types)
    print(PyInfo.integer_types)
    print(PyInfo.binary_type)
    print(PyInfo.maxsize)
    print(PyInfo.class_types)


#############################################
if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:38:18.709589
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # test case
    assert PyInfo.PY2 == True
    assert PyInfo.maxsize == 18446744073709551615
    assert type(PyInfo.maxsize) == int


# Generated at 2022-06-14 06:38:32.143492
# Unit test for constructor of class PyInfo
def test_PyInfo():

    if PyInfo.PY3:
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
        assert PyInfo.class_types == (type, types.ClassType)

    assert PyInfo.maxsize in (2147483647, 9223372036854775807)


test_PyInfo()

# Generated at 2022-06-14 06:38:36.633679
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(PyInfo.maxsize, (int, long))
    else:
        assert isinstance(PyInfo.maxsize, int)
    assert PyInfo.maxsize >= max(sys.maxsize, 2 * sys.maxsize)



# Generated at 2022-06-14 06:38:49.444985
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()
    assert pi.PY2 is sys.version_info[0] == 2
    assert pi.PY3 is sys.version_info[0] == 3
    if pi.PY3:
        assert pi.string_types == (str,)
        assert pi.text_type == str
        assert pi.binary_type == bytes
        assert pi.integer_types == (int,)
        assert pi.class_types == (type,)
        assert pi.maxsize == sys.maxsize
    else:  # PY2
        assert pi.string_types == (basestring,)
        assert pi.text_type == unicode
        assert pi.binary_type == str
        assert pi.integer_types == (int, long)
        assert pi.class_types == (type, types.ClassType)

# Generated at 2022-06-14 06:38:55.432979
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert len(PyInfo.string_types) == 1
    assert type("s") in PyInfo.string_types
    assert len(PyInfo.integer_types) == 2
    assert type(1) in PyInfo.integer_types
    assert len(PyInfo.class_types) == 2
    assert type in PyInfo.class_types

# Generated at 2022-06-14 06:39:07.443681
# Unit test for constructor of class PyInfo
def test_PyInfo():

    assert PyInfo.PY2 or PyInfo.PY3
    assert "PY2" in dir(PyInfo)
    assert "PY3" in dir(PyInfo)
    assert "PY2" in PyInfo.__dict__
    assert "PY3" in PyInfo.__dict__
    assert "string_types" in PyInfo.__dict__
    assert "text_type" in PyInfo.__dict__
    assert "binary_type" in PyInfo.__dict__
    assert "integer_types" in PyInfo.__dict__
    assert "class_types" in PyInfo.__dict__
    assert "maxsize" in PyInfo.__dict__
    assert str(PyInfo.PY2) in ["True", "False"]

# Generated at 2022-06-14 06:39:09.642544
# Unit test for constructor of class PyInfo
def test_PyInfo():
    try:
        text_type(b'Test')
    except:
        assert PyInfo.PY2



# Generated at 2022-06-14 06:39:20.964794
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from pyinfo import PyInfo
    PY2 = PyInfo.PY2
    PY3 = PyInfo.PY3
    assert PY2 ^ PY3
    if PY2:
        assert isinstance('', PyInfo.string_types)
        assert isinstance(u'', PyInfo.text_type)
        assert isinstance('', PyInfo.binary_type)
        assert isinstance(0, PyInfo.integer_types)
        assert isinstance(long(1), PyInfo.integer_types)
        assert isinstance(lambda: None, PyInfo.class_types)
        assert isinstance(lambda x: x, PyInfo.class_types)
    else:
        assert isinstance('', PyInfo.string_types)
        assert isinstance('', PyInfo.text_type)

# Generated at 2022-06-14 06:39:32.709641
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3


if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:39:39.272586
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from . import PyInfo

    print("PyInfo.PY2 = " + str(PyInfo.PY2))
    print("PyInfo.PY3 = " + str(PyInfo.PY3))

    if PyInfo.PY2:
        print("PyInfo.string_types = {}".format(PyInfo.string_types))
        print("PyInfo.text_type = " + str(PyInfo.text_type))
        print("PyInfo.binary_type = " + str(PyInfo.binary_type))
        print("PyInfo.integer_types = {}".format(PyInfo.integer_types))
        print("PyInfo.class_types = {}".format(PyInfo.class_types))
        print("PyInfo.maxsize = " + str(PyInfo.maxsize))

# Generated at 2022-06-14 06:39:47.193347
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:39:56.338344
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py2 = sys.version_info[0] == 2

    assert PyInfo.PY2 == py2

# Generated at 2022-06-14 06:40:00.492737
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert not PyInfo.PY2
    assert PyInfo.PY3
    assert isinstance("str", PyInfo.string_types)
    assert isinstance("str", PyInfo.text_type)
    assert isinstance("str", PyInfo.binary_type)
    assert isinstance(100, PyInfo.integer_types)
    assert isinstance(100, PyInfo.class_types)
    assert (1 << 31) - 1 == PyInfo.maxsize


test_PyInfo()

# Generated at 2022-06-14 06:40:04.886271
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2 and PyInfo.PY3:
        raise Exception(
            "Couldn't determine Python 2 or 3, Py2={}, Py3={}".format(
                PyInfo.PY2, PyInfo.PY3))

# Generated at 2022-06-14 06:40:08.398877
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 != PyInfo.PY3
    assert PyInfo.maxsize > 0
    assert PyInfo.text_type is str if PyInfo.PY3 else unicode

# Generated at 2022-06-14 06:40:12.328363
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Only for python3
    if not PyInfo.PY3:
        return
    assert isinstance('', PyInfo.string_types)
    assert isinstance(b'', PyInfo.binary_type)



# Generated at 2022-06-14 06:40:20.447045
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 is True or pyinfo.PY2 is False
    assert pyinfo.PY3 is True or pyinfo.PY3 is False

    string_types = pyinfo.string_types
    assert isinstance('abc', string_types)

    text_type = pyinfo.text_type
    assert isinstance('abc', text_type)

    binary_type = pyinfo.binary_type
    assert isinstance('abc', binary_type)

    integer_types = pyinfo.integer_types
    assert isinstance(123, integer_types)

    class_types = pyinfo.class_types
    assert isinstance(object, class_types)

    maxsize = pyinfo.maxsize
    assert isinstance(maxsize, int)

# Generated at 2022-06-14 06:40:23.242852
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import json
    import sys

    print(json.dumps(sys.version_info, indent=4))
    print(json.dumps(dict(locals()), indent=4))


if __name__ == "__main__":
    test_PyInfo()

# Generated at 2022-06-14 06:40:55.582414
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert isinstance(PyInfo.string_types, tuple)
        assert PyInfo.string_types == (basestring, )
        assert isinstance(PyInfo.text_type, unicode)
        assert PyInfo.text_type == unicode
        assert isinstance(PyInfo.binary_type, str)
        assert PyInfo.binary_type == str
        assert isinstance(PyInfo.integer_types, tuple)
        assert PyInfo.integer_types == (int, long)
        assert isinstance(PyInfo.class_types, tuple)
        assert PyInfo.class_types == (type, types.ClassType)
    else:  # PY3
        assert isinstance(PyInfo.string_types, tuple)
        assert PyInfo.string_types == (str, )

# Generated at 2022-06-14 06:41:00.344599
# Unit test for constructor of class PyInfo
def test_PyInfo():
    py2 = sys.version_info[0] == 2
    py3 = sys.version_info[0] == 3
    assert py2 ^ py3
    assert PyInfo.PY2 == py2
    assert PyInfo.PY3 == py3



# Generated at 2022-06-14 06:41:07.732834
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, str)
    assert isinstance(PyInfo.binary_type, str)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:41:18.400110
# Unit test for constructor of class PyInfo
def test_PyInfo():
    if PyInfo.PY2:
        assert PyInfo.string_types is (basestring,)
        assert PyInfo.text_type is unicode
        assert PyInfo.binary_type is str
        assert PyInfo.integer_types is (int, long)
        assert PyInfo.class_types is (type, types.ClassType)
    else:
        assert PyInfo.string_types is (str,)
        assert PyInfo.text_type is str
        assert PyInfo.binary_type is bytes
        assert PyInfo.integer_types is (int,)
        assert PyInfo.class_types is (type,)



# Generated at 2022-06-14 06:41:25.622128
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == sys.version_info[0] == 2
    assert PyInfo.PY3 == sys.version_info[0] == 3
    assert PyInfo.string_types
    assert PyInfo.text_type
    assert PyInfo.binary_type
    assert PyInfo.integer_types
    assert PyInfo.class_types
    assert PyInfo.maxsize

# Generated at 2022-06-14 06:41:27.920267
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert PyInfo.maxsize > 0

# Generated at 2022-06-14 06:41:30.558538
# Unit test for constructor of class PyInfo
def test_PyInfo():
    x = PyInfo()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 06:41:41.698195
# Unit test for constructor of class PyInfo
def test_PyInfo():
    import sys
    import types

    if PyInfo.PY3:
        assert PyInfo.string_types == (str, )
        assert isinstance('abc', PyInfo.string_types)
        assert not isinstance(b'abc', PyInfo.string_types)

        assert PyInfo.text_type == str
        assert isinstance('abc', PyInfo.text_type)
        assert not isinstance(b'abc', PyInfo.text_type)

        assert PyInfo.binary_type == bytes
        assert isinstance(b'abc', PyInfo.binary_type)
        assert not isinstance('abc', PyInfo.binary_type)

        assert PyInfo.integer_types == (int, )
        assert isinstance(1, PyInfo.integer_types)
        assert not isinstance(1.0, PyInfo.integer_types)

# Generated at 2022-06-14 06:41:51.818431
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)


# ======================================================================
# %% Constants
# ======================================================================

# constants used to annotate the argument types of a function
ARGTYPES = "argtypes"  # (type1, ...)
RESTYPE = "restype"    # type
ERRCHECK = "errcheck"  # function


# ======================================================================
# %% Getter and Setter
# ======================================================================

# Generated at 2022-06-14 06:41:56.676593
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 or PyInfo.PY3
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

# Generated at 2022-06-14 06:42:37.017000
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 == 1
    assert PyInfo.PY3 == 0
    assert PyInfo.maxsize == sys.maxsize

# Generated at 2022-06-14 06:42:40.576579
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.maxsize == sys.maxsize
    assert PyInfo.PY2 != PyInfo.PY3

if __name__ == '__main__':
    test_PyInfo()

# Generated at 2022-06-14 06:42:42.389047
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert isinstance(pyinfo, PyInfo)

# Generated at 2022-06-14 06:42:50.660297
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)

    try:
        import numpy
    except Exception:
        pass
    else:
        import numpy
        assert numpy.int64(1) == 1
        assert isinstance(numpy.int64(1), PyInfo.integer_types)



# Generated at 2022-06-14 06:42:58.749452
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

# Generated at 2022-06-14 06:43:04.478510
# Unit test for constructor of class PyInfo
def test_PyInfo():
    assert PyInfo.PY2 is not PyInfo.PY3

    assert isinstance(PyInfo.string_types, tuple)
    assert isinstance(PyInfo.text_type, type)
    assert isinstance(PyInfo.binary_type, type)
    assert isinstance(PyInfo.integer_types, tuple)
    assert isinstance(PyInfo.class_types, tuple)
    assert isinstance(PyInfo.maxsize, int)



# Generated at 2022-06-14 06:43:16.946273
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pyinfo = PyInfo()
    assert pyinfo.PY2 == (sys.version_info[0] == 2)
    assert pyinfo.PY3 == (sys.version_info[0] == 3)

    if pyinfo.PY3:
        assert pyinfo.string_types == (str,)
        assert pyinfo.text_type == str
        assert pyinfo.binary_type == bytes
        assert pyinfo.integer_types == (int,)
        assert pyinfo.class_types == (type,)
        assert pyinfo.maxsize == sys.maxsize
    else:
        assert pyinfo.string_types == (basestring,)
        assert pyinfo.text_type == unicode
        assert pyinfo.binary_type == str
        assert pyinfo.integer_types == (int, long)

# Generated at 2022-06-14 06:43:28.982450
# Unit test for constructor of class PyInfo
def test_PyInfo():
    from nose_parameterized import parameterized
    from test_utils import param_list_of_falsy_values, param_list_of_truthy_values

    @parameterized.expand(param_list_of_falsy_values)
    def test_PyInfo_false(falsy_value):
        assert not isinstance(falsy_value, PyInfo.string_types)
        assert not isinstance(falsy_value, PyInfo.integer_types)

    @parameterized.expand(param_list_of_truthy_values)
    def test_PyInfo_true(truthy_value):
        assert isinstance(truthy_value, (int, str))

# Generated at 2022-06-14 06:43:37.852228
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Test for Python 2
    old_version = sys.version_info[0]
    sys.version_info = (2, 5, 3, 'final', 0)
    info = PyInfo()
    assert info.PY2
    assert not info.PY3
    assert info.string_types == (basestring,)
    assert info.text_type == unicode
    assert info.binary_type == str
    assert info.class_types == (type, types.ClassType)
    assert info.integer_types == (int, long)
    assert isinstance(info.maxsize, (int, long))
    sys.version_info = old_version

    # Test for Python 3
    old_version = sys.version_info[0]
    sys.version_info = (3, 5, 3, 'final', 0)


# Generated at 2022-06-14 06:43:48.949662
# Unit test for constructor of class PyInfo
def test_PyInfo():
    pi = PyInfo()

    # Test if it is Python 2 or 3
    assert (pi.PY2 is True) or (pi.PY3 is True)

    # Test if it has attributes string_types, text_type, binary_type and integer_types
    assert hasattr(pi, "string_types"), "PyInfo object must have string_types attribute"
    assert hasattr(pi, "text_type"), "PyInfo object must have text_type attribute"
    assert hasattr(pi, "binary_type"), "PyInfo object must have binary_type attribute"
    assert hasattr(pi, "integer_types"), "PyInfo object must have integer_types attribute"

    # Test if it has attributes class_types and maxsize

# Generated at 2022-06-14 06:45:29.939145
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Check if the classname is not empty
    assert PyInfo.__name__ != ''

    # Check namespace
    ns = globals()
    assert PyInfo.__name__ in ns
    assert ns[PyInfo.__name__] == PyInfo


if __name__ == '__main__':
    try:
        test_PyInfo()
        print('TEST SUCEEDED')
    except AssertionError:
        print('TEST FAILED')

# Generated at 2022-06-14 06:45:43.029356
# Unit test for constructor of class PyInfo
def test_PyInfo():
    # Check type of class PyInfo
    assert isinstance(PyInfo, type(object))

    # Check field PY2 and PY3
    assert isinstance(PyInfo.PY2, bool)
    assert isinstance(PyInfo.PY3, bool)

    # Check field string_types
    assert isinstance(PyInfo.string_types, tuple)
    for item in PyInfo.string_types:
        assert isinstance(item, type(basestring))

    # Check field text_type
    assert isinstance(PyInfo.text_type, type(basestring))

    # Check field binary_type
    assert isinstance(PyInfo.binary_type, type(basestring))

    # Check field integer_types
    assert isinstance(PyInfo.integer_types, tuple)